#!/usr/bin/env python3
"""Commit-time documentation drift check.

Reads a Claude Code PreToolUse hook payload on stdin. When a commit stages
changes to watched source files and its message carries no Docs-checked
trailer, this blocks the commit and hands the agent the documents that may
now contradict the change.

The checker decides nothing about content. It answers "which documents claim
to describe what you just changed" and returns that to the agent, which reads
them and judges. See hooks/README.md for the configuration schema.
"""

import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

TRAILER = "Docs-checked:"
CONFIG_NAME = ".claude/docs-drift.json"


def glob_to_regex(pattern):
    """Translate a config glob to a regex anchored at the repository root.

    `**` crosses directory separators; a single `*` does not. Everything else
    is escaped, so a pattern is never a surprise regex.
    """
    out, i = [], 0
    while i < len(pattern):
        if pattern.startswith("**/", i):
            out.append("(?:.*/)?")
            i += 3
        elif pattern.startswith("**", i):
            out.append(".*")
            i += 2
        elif pattern[i] == "*":
            out.append("[^/]*")
            i += 1
        elif pattern[i] == "?":
            out.append("[^/]")
            i += 1
        else:
            out.append(re.escape(pattern[i]))
            i += 1
    return re.compile("^" + "".join(out) + "$")


def matches_any(path, patterns):
    return any(glob_to_regex(p).match(path) for p in patterns)


def select(paths, include, exclude=()):
    return [p for p in paths if matches_any(p, include) and not matches_any(p, exclude)]


def cited_documents(command, known):
    """Documents from `known` named in the text following the trailer marker.

    Only text after the marker counts, so a `git add README.md` earlier in the
    same command line is not mistaken for a citation.
    """
    index = command.find(TRAILER)
    if index == -1:
        return []
    tail = command[index + len(TRAILER):]
    return [p for p in known if p in tail or PurePosixPath(p).name in tail]


def decide(*, staged, command, watch, docs, records, exclude=(), generated_stale=()):
    """Pure decision. Returns {"allow": bool, "reason": str}.

    `staged` is the list of repository-relative paths in the staged diff.
    `command` is the shell command being run, searched for the trailer.
    `watch` and `exclude` are glob lists from the config; `docs` and
    `records` are already-resolved repository paths.
    `generated_stale` names generated artifacts that no longer match their
    generator, which is a deterministic failure and blocks on its own.
    """
    if generated_stale:
        names = ", ".join(sorted(generated_stale))
        return {
            "allow": False,
            "reason": (
                f"Generated artifacts are out of date: {names}.\n"
                "Re-run the generator named in .claude/docs-drift.json and stage "
                "the result. This check is exact, so there is nothing to judge."
            ),
        }

    touched = select(staged, watch, exclude)
    if not touched:
        return {"allow": True, "reason": "No watched source files staged."}

    candidates = sorted(docs)
    immutable = sorted(records)

    if TRAILER in command:
        cited = cited_documents(command, candidates + immutable)
        if cited:
            return {"allow": True, "reason": f"Trailer cites {', '.join(cited)}."}
        listing = "\n".join(f"  {p}" for p in candidates + immutable)
        return {
            "allow": False,
            "reason": (
                f"The {TRAILER} trailer names no document.\n\n"
                "This trailer is the only record of your reasoning that outlives "
                "the session. A later session recovers it with\n"
                "`git log --grep=Docs-checked` and has nothing else to go on, so "
                '"none" or "n/a" is indistinguishable from skipping the check.\n\n'
                f"Name at least one of:\n{listing}\n\n"
                "For example:\n"
                f"  {TRAILER} README.md unaffected, it does not describe this behavior"
            ),
        }

    lines = [
        "Documentation drift check. This commit changes files that documents describe.",
        "",
        "Changed and watched:",
    ]
    lines += [f"  {p}" for p in sorted(touched)]
    if candidates:
        lines += ["", "Documents that may need updating:"]
        lines += [f"  {p}" for p in candidates]
    if immutable:
        lines += ["", "Records to check but never edit:"]
        lines += [f"  {p}" for p in immutable]
    lines += [
        "",
        "Read the ones that plausibly cover this change and judge them.",
        "A document is stale only when the change contradicts what it claims.",
        "Refactoring behind an unchanged description is not drift.",
        "",
        "A record that the code now contradicts is not edited. Write a new record",
        "superseding it, or fix the code.",
        "",
        f"Then commit again with a {TRAILER} trailer that names each document you",
        "read and what you concluded about it. Naming no document is rejected:",
        "the trailer is the only record of this reasoning that outlives the",
        "session, and a later session recovers it from `git log` alone.",
        "",
        f"  {TRAILER} README.md updated for the new category;",
        "                docs/portability.md unaffected, it describes skill format",
    ]
    return {"allow": False, "reason": "\n".join(lines)}


def run(args, cwd):
    return subprocess.run(
        args, cwd=cwd, capture_output=True, text=True, check=False
    )


def generated_mismatches(config, cwd):
    """Re-run each generator and report artifacts whose output changed."""
    stale = []
    for entry in config.get("generated", []):
        artifact, command = entry.get("file"), entry.get("command")
        if not artifact or not command:
            continue
        before = Path(cwd, artifact)
        previous = before.read_bytes() if before.exists() else None
        result = run(["bash", "-lc", command], cwd)
        if result.returncode != 0:
            stale.append(f"{artifact} (generator failed)")
            continue
        if before.exists() and before.read_bytes() != previous:
            stale.append(artifact)
            if previous is not None:
                before.write_bytes(previous)  # a check must not edit the tree
    return stale


def main():
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0

    command = (payload.get("tool_input") or {}).get("command", "")
    if "git commit" not in command:
        return 0

    cwd = payload.get("cwd") or "."
    config_path = Path(cwd, CONFIG_NAME)
    if not config_path.exists():
        return 0

    try:
        config = json.loads(config_path.read_text())
    except (json.JSONDecodeError, ValueError):
        return 0

    staged = [
        line
        for line in run(
            ["git", "diff", "--cached", "--name-only"], cwd
        ).stdout.splitlines()
        if line
    ]
    tracked = [
        line for line in run(["git", "ls-files"], cwd).stdout.splitlines() if line
    ]
    exclude = config.get("exclude", [])

    verdict = decide(
        staged=staged,
        command=command,
        watch=config.get("watch", []),
        docs=select(tracked, config.get("docs", []), exclude),
        records=select(tracked, config.get("records", []), exclude),
        exclude=exclude,
        generated_stale=generated_mismatches(config, cwd) if staged else [],
    )

    if verdict["allow"]:
        return 0

    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": verdict["reason"],
            }
        },
        sys.stdout,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
