#!/usr/bin/env python3
"""Fixture tests for the unslop Stop hook.

Run with `python3 hooks/test_unslop_check.py`. No test runner, matching
scripts/validate.rb and test_docs_drift.py: one command, no dependencies.
"""

import importlib.util
import json
import tempfile
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "unslop_check", Path(__file__).parent / "unslop-check.py"
)
unslop = importlib.util.module_from_spec(spec)
spec.loader.exec_module(unslop)

failures = []


def check(name, condition):
    print(f"  {'ok  ' if condition else 'FAIL'} {name}")
    if not condition:
        failures.append(name)


def transcript(reply, tools=None):
    """Write a one-turn transcript and return its path."""
    rows = [
        {"type": "user", "message": {"content": "go"}},
        {"type": "assistant", "message": {"content":
            [{"type": "text", "text": reply}] + (tools or [])}},
    ]
    handle = tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False)
    handle.write("\n".join(json.dumps(row) for row in rows))
    handle.close()
    return handle.name


def findings(reply, tools=None):
    text, wrote_doc, loaded_skill = unslop.load_turn(transcript(reply, tools))
    prose = unslop.redact(text)
    hits = [
        f"{number}:{term}"
        for number, _, terms, _ in unslop.RULES
        for term in terms
        if unslop.compile_term(term).search(prose)
    ]
    if unslop.NOT_JUST[2].search(prose):
        hits.append("9:not-just")
    return hits, wrote_doc, loaded_skill


print("the adapter carries no rules of its own")
check(
    "every enforced term still appears in the skill",
    unslop.drifted_terms(unslop.SKILL.read_text(encoding="utf-8")) == [],
)

print("mechanical tells")
check("clean prose is silent", findings("The loader parses the file.")[0] == [])
check("ai vocabulary is caught", "7:crucial" in findings("This is a crucial fix.")[0])
check("inflections are caught", "7:showcase" in findings("It showcases the fix.")[0])
check("em dash is caught", "13:—" in findings("One thing — then another.")[0])
check("hyphen-as-dash is caught", "13:--" in findings("One thing -- then another.")[0])
check("curly quotes are caught", "19:’" in findings("It’s here.")[0])
check("sycophancy is caught", "22:Great question" in findings("Great question! Here.")[0])
check("not-just-but is caught", "9:not-just" in findings("Not just faster, but safer.")[0])
check("filler is caught", "23:in order to" in findings("Run it in order to pass.")[0])

print("a banned word discussed is not a banned word used")
check("code fence is redacted", findings("```\nutilize the substrate\n```")[0] == [])
check("inline code is redacted", findings("Avoid `crucial` and `leverage`.")[0] == [])
check("blockquote is redacted", findings("> Great question! I hope this helps!")[0] == [])
check("link target is redacted", findings("See [docs](https://x.dev/delve/page).")[0] == [])

print("ambiguous terms are left alone on purpose")
check("features is not enforced", findings("The release features two fixes.")[0] == [])
check("harness is not enforced", findings("The harness runs the tool.")[0] == [])
check("surface is not enforced", findings("Surface the finding to the user.")[0] == [])

print("the closing pass")
write = [{"type": "tool_use", "name": "Write", "input": {"file_path": "a/b.md"}}]
heredoc = [{"type": "tool_use", "name": "Bash",
            "input": {"command": "cat > docs/page.md <<'EOF'\nhi\nEOF"}}]
skill = [{"type": "tool_use", "name": "Skill", "input": {"skill": "unslop"}}]
check("a Write to markdown counts as a document", findings("done", write)[1])
check("a shell heredoc counts too", findings("done", heredoc)[1])
check("a shell command touching no document does not", not findings("done", [
    {"type": "tool_use", "name": "Bash", "input": {"command": "ls -la"}}])[1])
check("loading the skill is recorded", findings("done", skill)[2])

if failures:
    print(f"\nunslop-check: {len(failures)} failing")
    raise SystemExit(1)
print("\nunslop-check: OK")
