---
name: implement-change
description: Implement an approved software change and validate it against repository conventions. Use when a plan or acceptance criteria are ready for execution.
---

# Implement a change

## Purpose

Deliver an approved change while preserving repository conventions and making the result easy to verify.

## When to use

Use after a plan is approved or when the requested implementation scope and acceptance criteria are already clear.

## Required context

- The approved plan or an equivalent clear task statement.
- Repository conventions, relevant code, tests, and documentation.
- Acceptance criteria, constraints, and any prior decisions.

## Workflow

1. Re-read the plan and inspect the affected areas before editing.
2. Implement the smallest complete change that satisfies the acceptance criteria.
3. Keep the change consistent with local style, architecture, error handling, and documentation practices.
4. Add or update focused tests when behavior changes.
5. Run the relevant validation and inspect the final diff for unintended changes.
6. Prepare a handoff that records the implementation, validation, risks, and next action.

## Expected output

Provide a concise implementation summary, files changed, validation performed and results, deviations from the plan, remaining risks, and a recommended next action using the shared handoff contract.

## Completion criteria

The requested behavior is implemented, relevant validation has been run or explicitly explained, the diff is scoped, and the next reviewer has the context needed to assess it.
