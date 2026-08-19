# ADR-0001 — Host adapters live in hooks/, never in skills/

- **Status:** Accepted
- **Date:** 2026-08-19
- **Related:** [CONTRIBUTING](../../CONTRIBUTING.md), [portability](../portability.md)

## Context

Skills in this repository are portable Markdown. `CONTRIBUTING.md` requires
provider-independent language and forbids requiring a specific coding-agent
product, and `create-skills` restricts frontmatter to `name` and `description`
so both Codex and Claude Code can read the same file.

Some useful automation cannot meet that bar. A documentation-drift checker has
to speak one host's hook protocol and settings format to run at all. Putting it
in `skills/` would either break the portability guarantee or force the skill to
describe an integration it cannot perform.

`docs/portability.md` already anticipates this case: "When a repeated
integration is genuinely valuable, add it as a small adapter that points back
to these canonical files rather than making the adapter the source of truth."

## Decision

Host-specific adapters live in a top-level `hooks/` directory, never inside
`skills/`. Each adapter points back to a canonical skill and carries no
authority the skill does not already have. The skill remains the source of
truth; the adapter only decides when the host invokes it.

The skill validator reads `skills/*/SKILL.md` only, so adapters sit outside its
contract by construction rather than by exception.

## Consequences

`hooks/` becomes a documented category alongside `skills/` and `agents/`, with
a rule in `CONTRIBUTING.md` directing host-specific work there.

Adapters are not portable, and the repository stops claiming they are. A user
on another host reads the adapter as a reference implementation and writes
their own, which is the same relationship the repository already has with the
build and review stages it delegates.

An adapter that starts carrying rules absent from its skill is a defect. The
rules belong in the skill.
