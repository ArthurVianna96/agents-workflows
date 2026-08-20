# Hooks

Host-specific adapters. These are not portable, and this repository does not
claim they are. Each one wires a canonical skill into one coding agent's
lifecycle. See [ADR-0001](../docs/adr/0001-host-adapters-live-in-hooks.md) for
why they live here rather than in `skills/`.

An adapter decides only *when* the host invokes a skill. Rules belong in the
skill. An adapter that starts carrying rules of its own is a defect.

## unslop-check.py

A Claude Code `Stop` hook. Before a reply lands it holds the turn to the
`unslop` skill, on two counts.

**Mechanical tells.** The rules that are word or phrase lists, matched
literally against the reply: AI vocabulary, em dashes, curly quotes, chatbot
phrases, sycophancy, filler, puffery, fancy synonyms, and the rest. On a hit it
blocks with the rule number, the match, and what to write instead.

**The closing pass.** If the session wrote a Markdown document and never loaded
the `unslop` skill, it blocks and says so. Documents are detected from `Write`
and `Edit` and from shell redirects and heredocs, because a document written
with `cat > page.md` is still a document.

That second check exists because the first is not enough. The short list in a
global instruction file covers the mechanical rules; it does not carry rules 27
to 30 or the "adding soul" section, and a whole session's worth of documents
once shipped without them.

Roughly half the skill is enforceable this way. Voiceless prose, dense
sentences, passive voice, and adverbs propping up weak verbs need a reader,
and no exit code substitutes for one.

Terms whose innocent use is common are left out on purpose: `features`,
`surface`, `harness`, `primitive`, `vector`, `scaffolding`, `landscape`. A
check that cries wolf gets turned off. Code fences, inline code, blockquotes,
and link targets are stripped first, so a banned word being discussed is not
treated as a banned word being used.

Every term is verified against the skill at runtime. One that has left the
skill is reported as drift instead of enforced, which is how the adapter stays
inside the boundary ADR-0001 draws. `python3 hooks/test_unslop_check.py` checks
that, and the redaction, and both document signals.

Install it by pointing your `~/.claude/settings.json` `Stop` hook at this
script. It fails open: no transcript, unreadable input, or a missing skill file
all exit silently rather than stopping a session.

## docs-drift.py

A Claude Code `PreToolUse` hook on `Bash`. When a `git commit` stages changes
to watched source files and the message carries no `Docs-checked:` trailer, it
blocks the commit and hands the agent the documents that may now contradict
the change. The agent reads them, judges, and commits again with the trailer.

The trailer must name at least one of the listed documents. A bare
`Docs-checked: none` is rejected, because the trailer is the only record of
that reasoning which outlives the session: a later session recovers it with
`git log --grep=Docs-checked` and has nothing else to go on. Citing by
basename is enough, and naming a document before the trailer does not count.

The rules for judging and recording live in the `write-docs` skill, which is
portable. This adapter decides only when to ask, which is what keeps it inside
the boundary ADR-0001 draws.

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

Only `watch` matches trigger the check, so a document describing another
document drifts silently. A README section that names the skills goes stale
when a skill is added, and no watched source changed, so nothing reports it.
Adding the `docs` paths to `watch` would trade that for naming every document
on every documentation commit, which is why this is a gap rather than a
setting.
