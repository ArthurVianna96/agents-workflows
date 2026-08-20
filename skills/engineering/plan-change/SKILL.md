---
name: plan-change
description: Route a change request through discovery to a buildable specification by sequencing the grilling, domain-modeling, and specification skills. Use when a request needs planning and it is unclear how much discovery it deserves.
---

# Plan a change

Take a requested change from "someone asked for this" to a specification another person or agent can build. This skill decides which discovery stages the request deserves, runs them in order, and owns the transitions between them. It does not replace `grill-with-docs` or `to-spec`; it sequences them and enforces the conditions each one assumes.

Run this in the conversation with the user. `grill-with-docs` interviews the user directly, and `to-spec` synthesizes the conversation it is running in, so neither survives being handed to a detached agent. Delegate fact-finding to sub-agents freely; never delegate a decision that belongs to the user.

## Required context

- The requested change and the user outcome behind it.
- Repository conventions, current behavior, and constraints in the affected area.
- The configured issue tracker and triage label vocabulary. If they have not been provided, use `setup-engineering-skills` before step 4.

## Workflow

### 1. Triage the route

Choose the route before doing any work, and say which one you chose and why.

- **Settled and small.** Behavior is unambiguous, the work fits one session, and no durable decision comes out of it. Say so and send it straight to implementation; stop here.
- **Settled and substantial.** The outcome is agreed and the terminology and boundaries are clear, but the work crosses layers or sessions. Skip the interview and go to step 3.
- **Unsettled.** Terminology, ownership, boundaries, architecture, or acceptance are open, and you would have to guess to write the spec. Go to step 2.

When two routes seem equally plausible, take the more thorough one. Guessing costs more than an extra round of questions.

### 2. Resolve the design

Use `grill-with-docs`. Interview the user in rounds until the frontier is empty, and record durable decisions in the glossary and decision records as they crystallize.

Do not compress the interview to reach the spec sooner. An unasked question becomes a silent assumption in the spec.

### 3. Gate the handover

Confirm every condition below before writing anything:

- Every branch of the design tree has been visited; nothing is silently assumed.
- The user has explicitly confirmed shared understanding.
- Durable decisions live in the glossary and decision records, not only in the conversation.
- The issue tracker and triage vocabulary are configured.

If a condition fails, name it and resolve it. Return to step 2 for an open design question; use `setup-engineering-skills` for missing tracker configuration.

### 4. Write the specification

Use `to-spec`. Synthesize the settled conversation rather than reopening it, and confirm the test seams with the user as that skill requires.

### 5. Route the work forward

- Multiple vertical slices, delegated work, or more than one session: use `to-tickets`.
- One coherent session: hand the specification straight to implementation.

## Expected output

The published specification is the artifact. Close with the shared handoff contract:

```text
Task goal:
Decisions:
Files changed:
Validation performed:
Remaining risks:
Next action:
```

Record the chosen route and any skipped stage under decisions. List glossary and decision-record edits under files changed. Name the exit ramp under next action.

## Completion criteria

The chosen route is stated and justified; no unresolved design branch was carried silently into the spec; durable decisions are recorded in the project's documents; the specification is published to the configured tracker; and the next action names a specific downstream skill.
