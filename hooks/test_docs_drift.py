#!/usr/bin/env python3
"""Fixture tests for the documentation drift checker.

Run with `python3 hooks/test_docs_drift.py`. No test runner, matching
scripts/validate-skills.rb: one command, no dependencies.
"""

import importlib.util
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "docs_drift", Path(__file__).parent / "docs-drift.py"
)
drift = importlib.util.module_from_spec(spec)
spec.loader.exec_module(drift)

WATCH = ["skills/**/*.md", "agents/*.md", "hooks/*.py"]
DOCS = ["README.md", "docs/portability.md"]
RECORDS = ["docs/adr/0001-host-adapters-live-in-hooks.md"]
EXCLUDE = ["docs/issues/**"]

failures = []


def check(name, condition, detail=""):
    if condition:
        print(f"  ok   {name}")
    else:
        print(f"  FAIL {name} {detail}")
        failures.append(name)


def verdict(staged, command="git commit -m 'x'", generated_stale=()):
    return drift.decide(
        staged=staged,
        command=command,
        watch=WATCH,
        docs=DOCS,
        records=RECORDS,
        exclude=EXCLUDE,
        generated_stale=generated_stale,
    )


print("glob translation")
check("** crosses directories", drift.glob_to_regex("skills/**/*.md").match("skills/a/SKILL.md") is not None)
check("* stops at separator", drift.glob_to_regex("agents/*.md").match("agents/a/b.md") is None)
check("dots are literal", drift.glob_to_regex("README.md").match("READMEXmd") is None)

print("prefilter")
check("docs-only change is allowed", verdict(["README.md"])["allow"])
check("empty stage is allowed", verdict([])["allow"])
check("watched change blocks", not verdict(["skills/triage/SKILL.md"])["allow"])
check("excluded path does not trigger", verdict(["docs/issues/a.md"])["allow"])

print("trailer")
check(
    "trailer admits the retry",
    verdict(["skills/triage/SKILL.md"], command="git commit -m 'x\n\nDocs-checked: README.md unaffected'")["allow"],
)
check(
    "trailer in a heredoc body is seen",
    verdict(["hooks/docs-drift.py"], command="git commit -F - <<'EOF'\nx\n\nDocs-checked: none\nEOF")["allow"],
)

print("block message")
blocked = verdict(["skills/triage/SKILL.md", "agents/scout.md"])
check("names the changed watched files", "skills/triage/SKILL.md" in blocked["reason"])
check("lists candidate docs", "docs/portability.md" in blocked["reason"])
check("separates records from docs", "never edit" in blocked["reason"])
check("states the contradiction rule", "contradicts" in blocked["reason"])
check("tells the agent how to proceed", "Docs-checked:" in blocked["reason"])

print("generated artifacts")
gen = verdict(["skills/a/SKILL.md"], generated_stale=["api.yaml"])
check("generated mismatch blocks", not gen["allow"])
check("generated mismatch is exact, not a judgment", "nothing to judge" in gen["reason"])
check(
    "generated mismatch outranks the trailer",
    not verdict(["skills/a/SKILL.md"], command="git commit -m 'Docs-checked: all'", generated_stale=["api.yaml"])["allow"],
)

print()
if failures:
    print(f"{len(failures)} failing: {', '.join(failures)}")
    sys.exit(1)
print("docs-drift: OK")
