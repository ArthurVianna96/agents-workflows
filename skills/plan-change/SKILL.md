---
name: plan-change
description: Create an actionable, scoped plan for a software change. Use when requirements need investigation, decisions, or approval before implementation.
---

# Plan a change

## Purpose

Turn a requested change into a small, actionable plan that another person or agent can implement with confidence.

## When to use

Use before a non-trivial implementation, when requirements are ambiguous, or when the work needs agreement before files change.

## Required context

- The task goal and intended user outcome.
- Relevant repository guidance, existing behavior, and constraints.
- Known non-goals, risks, and acceptance criteria.

## Workflow

1. Inspect the relevant code, documentation, tests, and repository conventions.
2. State the current behavior and the desired behavior; call out gaps or assumptions.
3. Identify the smallest coherent set of changes, including tests and documentation where appropriate.
4. Record decisions, alternatives that matter, dependencies, and risks.
5. Write ordered implementation steps with enough file- and behavior-level detail to execute.

## Expected output

Provide an actionable plan containing: goal, current state, decisions and assumptions, ordered changes, validation approach, risks, and the next action. Use the shared handoff contract when handing the plan to another role.

## Completion criteria

The scope, decisions, affected areas, and validation approach are explicit; an implementer can begin without rediscovering the task; unresolved choices are clearly marked for approval.
