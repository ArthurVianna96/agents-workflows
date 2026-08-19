# Turn a plan into tickets

> Locally adapted from Matt Pocock’s [to-tickets](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md), retrieved 2026-08-19. Copyright © 2026 Matt Pocock; MIT licensed. See [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md).

## Purpose

Break a plan, specification, or settled conversation into independently verifiable vertical-slice tickets with explicit blocking relationships.

## When to use

Use after a plan or specification is agreed and the implementation should be tracked, delegated, or completed across sessions.

## Required context

- An agreed plan, specification, or settled conversation.
- Relevant repository behavior, domain language, and decision records.
- The chosen ticket destination: local Markdown files or an issue tracker.

## Workflow

1. Read all supplied references and inspect the relevant codebase when context is incomplete.
2. Draft tracer-bullet vertical slices. Each slice should deliver an end-to-end behavior, be verifiable on its own, and fit in a fresh work session.
3. Record blocking edges. A ticket with no blockers can start immediately.
4. Treat a codebase-wide mechanical migration as an exception: use expand–migrate–contract steps and keep each step safe to validate.
5. Present the numbered breakdown with each ticket’s title, blockers, and delivered behavior. Refine it until approved.
6. Publish the approved tickets in dependency order to the chosen location. Do not modify a parent issue unless explicitly asked.

## Ticket template

```text
# <number>: <ticket title>

## What to build

The end-to-end behavior this ticket makes work, from the user’s perspective.

## Acceptance criteria

- [ ] A specific, falsifiable behavior or outcome.

## Blocked by

- None (can start immediately), or links/titles of required tickets.

## Notes

- Essential context, decisions, or prototype-derived detail.
```

Avoid brittle file paths and code snippets unless a snippet captures an essential decision more precisely than prose.

## Expected output

Provide the approved ticket set, its location or issue references, blocking relationships, and the next executable ticket using the shared handoff contract.

## Completion criteria

Each ticket is independently understandable and demonstrable, blockers are explicit, acceptance criteria are testable, and the first unblocked ticket is clear.
