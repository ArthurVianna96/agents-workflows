# Hooks

Host-specific adapters. These are not portable, and this repository does not
claim they are. Each one wires a canonical skill into one coding agent's
lifecycle. See [ADR-0001](../docs/adr/0001-host-adapters-live-in-hooks.md) for
why they live here rather than in `skills/`.

An adapter decides only *when* the host invokes a skill. Rules belong in the
skill. An adapter that starts carrying rules of its own is a defect.

## unslop-check.py

A Claude Code `Stop` hook. It checks a reply against the `unslop` skill before
that reply lands, on two counts.

**Mechanical tells.** Some rules are word or phrase lists, so the script matches
them literally: AI vocabulary, em dashes, curly quotes, chatbot phrases,
sycophancy, filler, puffery, fancy synonyms. On a hit it blocks the turn and
names the rule number, the match, and what to write instead.

**The closing pass.** When a session has written a Markdown document and never
loaded the `unslop` skill, the hook blocks and says so. It finds those documents
in `Write` and `Edit` calls and in shell redirects and heredocs. A page written
with `cat > page.md` is still a page, and watching the file tools alone would
miss it.

The second check exists because the first is not enough. A short rule list in a
global instruction file covers the mechanical patterns. It carries neither rules
27 to 30 nor the "adding soul" section, and one session shipped seven documents
that way before anyone noticed.

So the honest ceiling here is about half the skill. Voiceless prose, dense
sentences, passive voice, and adverbs propping up weak verbs all need a reader.
No exit code substitutes for one. The block message says as much, so a silent
pass never reads as "this prose is good".

Two things keep the check from becoming noise. Some terms stay out because
their innocent use is common: `features`, `surface`, `harness`, `primitive`,
`vector`, `scaffolding`, `landscape`. And the script strips code fences, inline
code, blockquotes, and link targets before it matches anything, so a banned word
under discussion does not read as one in use.

The script also verifies every term against the skill each time it runs. If a
term has left the skill, it reports drift instead of enforcing the term. That is
how this adapter stays inside the boundary ADR-0001 draws.
`python3 hooks/test_unslop_check.py` covers the drift check, the redaction, and
both document signals.

To install it, point the `Stop` hook in your `~/.claude/settings.json` at this
script. It fails open. A missing transcript, unreadable input, a missing skill
file, or a second block on an already-stopped turn all exit silently, because a
hook that can wedge a session is worse than no hook.

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
