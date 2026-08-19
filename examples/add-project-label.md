# Example: add an optional project label

This fictional walkthrough demonstrates the loop for a small feature in an imaginary task application. It is deliberately self-contained: no private repository, customer data, or production commands are involved.

## Request

Add an optional **Project label** text field to the create-task form. Save it with a task and show it below the task title in the task list when present. Existing tasks must continue to work.

## 1. Frame

`plan-change` triages the request first. The request names a field and a place to show it, but it does not settle what a project label *is*: free text or a known set, one per task or several, and whether existing tasks without one are a valid state. Those are terminology and boundary questions, so the route is **unsettled** and the interview runs.

`grill-with-docs` asks the frontier in one round:

```text
❓ Q1 - Label vocabulary: is a project label free text, or chosen from a set the user maintains?
➡️ Free text for now; a managed set is a bigger feature with its own management UI.

❓ Q2 - Cardinality: can a task carry more than one label?
➡️ One. Multiple labels turns this into tagging, which needs filtering to be useful.

❓ Q3 - Blank input: is an empty label a stored empty string or an absent field?
➡️ Absent. A stored empty string creates two ways to mean "no label".
```

A scout answers a fact question in parallel, so nobody has to ask the user: the persistence layer deserializes unknown-absent fields without a migration, verified in the model's deserialization tests.

The user confirms all three recommendations. `domain-modeling` records the durable one: **project label** enters the glossary as a single optional free-text string on a task, with absence as the only representation of "no label".

## 2. Specify

The frontier is empty and the user has confirmed shared understanding, so the gate passes and `to-spec` synthesizes without reopening anything. The seam is checked first: the existing create-task component test is the highest seam that already exists, so the feature is tested there rather than at a new one.

The published specification states the problem from the user's perspective, the solution, user stories covering labeled and unlabeled tasks, and the implementation decisions from the interview: optional trimmed string, blank omitted rather than stored, no filtering or editing in this change. It carries the `ready-for-agent` triage label.

## 3. Slice

The work is one vertical slice: the model, the form, and the list are a single tracer bullet that is demoable on its own, so `to-tickets` produces one ticket with no blockers rather than splitting by layer.

## 4. Build and review

Both happen with the host environment's own tooling. The slice is implemented test-first, then reviewed with whatever review command the environment provides. The playbook's only requirement across this boundary is that the handoff contract comes back out of it.

## 5. Hand off

```text
Task goal: Add an optional project label to created tasks and display it in the list.
Decisions: Single optional free-text label; blank input omitted rather than stored; filtering and editing out of scope. Recorded in the glossary.
Files changed: src/task.ts, src/CreateTaskForm.tsx, src/TaskList.tsx, and focused model and component tests.
Validation performed: Focused model, form, and list tests passed; type check passed; independent review found no blocking issues.
Remaining risks: Confirm live persistence if the real storage layer has requirements beyond model deserialization.
Next action: Merge after normal repository-wide checks, or frame a separate change for filtering or editing.
```
