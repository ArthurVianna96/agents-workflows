# Hooks

Host-specific adapters. These are not portable, and this repository does not
claim they are. Each one wires a canonical skill into one coding agent's
lifecycle. See [ADR-0001](../docs/adr/0001-host-adapters-live-in-hooks.md) for
why they live here rather than in `skills/`.

An adapter decides only *when* the host invokes a skill. Rules belong in the
skill. An adapter that starts carrying rules of its own is a defect.

## docs-drift.py

A Claude Code `PreToolUse` hook on `Bash`. When a `git commit` stages changes
to watched source files and the message carries no `Docs-checked:` trailer, it
blocks the commit and hands the agent the documents that may now contradict
the change. The agent reads them, judges, and commits again with the trailer.

The checker judges nothing itself. It answers "which documents claim to
describe what you just changed" and lets the agent, which already has the
change in context, decide whether anything actually contradicts.

Configure it per repository in `.claude/docs-drift.json`:

| Key | Meaning |
| --- | --- |
| `watch` | Globs whose change can invalidate a document. |
| `docs` | Globs for present-tense documents that may need updating. |
| `records` | Globs for point-in-time records. Checked for contradiction, never edited; a contradiction means writing a superseding record. |
| `exclude` | Globs removed from every other set. |
| `generated` | `{"file", "command"}` pairs. The generator re-runs and any difference blocks the commit outright, since that check is exact and needs no judgment. |

Install it for yourself by pointing `.claude/settings.local.json` at this
script; that file is gitignored, so the hook stays local until its
false-positive rate is known.

Run `python3 hooks/test_docs_drift.py` after changing it.

## Limits

Commits made outside Claude Code never reach the hook, and neither does a
commit whose message arrives through `git commit -F <file>`, since the trailer
is matched in the command string.
