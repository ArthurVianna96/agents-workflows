# Review a change

## Purpose

Independently assess a change for correctness, regressions, maintainability, and unmet requirements.

## When to use

Use after implementation and before merge or handoff, especially when an independent perspective can catch missed cases.

## Required context

- The task goal, approved plan, and acceptance criteria.
- The changed files or diff, relevant surrounding code, and repository conventions.
- Validation already performed and its results.

## Workflow

1. Understand the intended behavior before judging the implementation.
2. Inspect the diff and relevant surrounding code; trace important behavior and edge cases.
3. Check correctness, regressions, tests, security or data concerns, compatibility, and maintainability in proportion to the change.
4. Report only actionable findings, ordered by severity, with file/location evidence and an explanation of impact.
5. Distinguish findings from questions and state clearly when no blocking findings remain.

## Expected output

Provide prioritized findings with evidence, a short summary of review coverage, validation gaps, remaining risks, and the next action using the shared handoff contract.

## Completion criteria

The review is independent, evidence-backed, scoped to the requested change, and clear enough for a builder to act on without interpretation.
