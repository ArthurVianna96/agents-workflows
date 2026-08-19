# Turn a conversation into a specification

> Locally adapted from Matt Pocock’s [to-spec](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-spec/SKILL.md), retrieved 2026-08-19. Copyright © 2026 Matt Pocock; MIT licensed. See [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md).

## Purpose

Synthesize settled conversation and repository understanding into a buildable specification without restarting discovery.

## When to use

Use after the problem and major decisions are understood, especially before a multi-session change is planned, delegated, or split into tickets.

## Required context

- The settled conversation, decisions, and constraints.
- Relevant codebase behavior, glossary, decision records, and repository conventions.
- The intended destination for the spec: a Markdown file, issue, or project tracker.

## Workflow

1. Inspect the relevant repository areas if they have not already been examined.
2. Synthesize known context; do not reopen discovery unless repository evidence contradicts a decision.
3. Identify the highest useful behavioral seams for validation. Prefer existing seams and discuss new ones that materially affect the design.
4. Draft the specification below, using the project’s domain language and recording explicit out-of-scope decisions.
5. Review the specification with the requester, then save or publish it in the agreed location.

## Specification template

```text
# <Feature or change name>

## Problem statement

The problem from the user’s perspective.

## Solution

The intended outcome from the user’s perspective.

## User stories

1. As a <actor>, I want <feature>, so that <benefit>.

## Implementation decisions

- Modules, interfaces, architectural decisions, schema changes, API contracts, or interaction decisions that must survive implementation.

## Testing decisions

- Behavioral seams, important cases, and relevant existing test patterns.

## Out of scope

- Explicit exclusions for this change.

## Further notes

- Dependencies, rollout considerations, or unresolved questions.
```

Avoid brittle file paths and implementation snippets. Include a small prototype-derived snippet only when it records a decision more precisely than prose can.

## Expected output

Provide the completed specification, its location, validation decisions, open questions, and the next action using the shared handoff contract.

## Completion criteria

The specification explains the problem, outcome, scope, durable decisions, and validation approach well enough to plan or divide the implementation without rediscovery.
