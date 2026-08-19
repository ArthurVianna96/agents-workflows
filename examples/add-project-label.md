# Example: add an optional project label

This fictional walkthrough demonstrates the full loop for a small feature in an imaginary task application. It is deliberately self-contained: no private repository, customer data, or production commands are involved.

## Request

Add an optional **Project label** text field to the create-task form. Save it with a task and show it below the task title in the task list when present. Existing tasks must continue to work.

## 1. Planner artifact

**Current state.** `Task` has `title` and `completed`. The create form submits a title; the list renders title and status. The repository uses component tests for form behavior and unit tests for model serialization.

**Decisions.** The label is optional, trimmed before save, and represented as `projectLabel?: string`. An empty value is omitted rather than stored as an empty string. No filtering or editing UI is included.

**Plan.**

1. Extend the task model and serialization to accept an optional `projectLabel` without changing existing records.
2. Add a labeled text input to the create-task form and include a trimmed value in the create request only when non-empty.
3. Render a secondary project-label line under the title only when a task has one.
4. Add model tests for absent and present labels, plus form/list tests for saving and rendering behavior.
5. Run the focused test suites and the project’s standard type check.

```text
Task goal: Add an optional project label to created tasks and display it in the list.
Decisions: Optional trimmed string; omit empty values; no filtering or editing in this change.
Files changed: Expected task model, create form, task list, and focused tests.
Validation performed: Planning inspection only; implementation validation is pending.
Remaining risks: Existing persisted tasks must deserialize without a label.
Next action: Approve this plan, then give it to the Builder role.
```

## 2. Builder artifact

**Implementation summary.** The model now accepts an optional `projectLabel`. The form trims its input and omits it when blank. The list renders a muted secondary line only for labeled tasks. Tests cover both new and existing task shapes.

```text
Task goal: Add an optional project label to created tasks and display it in the list.
Decisions: Implemented the approved optional/trimmed/omitted representation; did not add filtering or editing.
Files changed: src/task.ts, src/CreateTaskForm.tsx, src/TaskList.tsx, and their focused tests.
Validation performed: Task model tests passed; create-form and list component tests passed; type check passed.
Remaining risks: The fictional example does not exercise a live persistence migration; compatibility is covered by deserialization tests.
Next action: Give the diff and this handoff to the Reviewer role for independent review.
```

## 3. Reviewer artifact

**Review coverage.** Compared the implementation with the plan; inspected optional-field serialization, blank-input behavior, conditional rendering, and tests.

**Findings.** No blocking findings. The code omits blank labels, preserves tasks without labels, and only renders the secondary line when present. Focused tests cover the stated behavior.

```text
Task goal: Add an optional project label to created tasks and display it in the list.
Decisions: No change to the approved scope; reviewer confirmed optional-field behavior.
Files changed: Reviewed src/task.ts, src/CreateTaskForm.tsx, src/TaskList.tsx, and focused tests.
Validation performed: Reviewed the Builder-reported passing tests and traced the relevant behavior; no additional commands run in this fictional example.
Remaining risks: Live persistence behavior should be checked in the real application if its storage layer differs from the model tests.
Next action: Merge if normal project checks are satisfied; otherwise have the Builder address any environment-specific persistence concern.
```

## 4. Final handoff

The review is clean for the approved scope. This separate handoff is what a release owner or a later session receives:

```text
Task goal: Add an optional project label to created tasks and display it in the list.
Decisions: The label is an optional trimmed string; blank input is omitted; filtering and editing remain out of scope.
Files changed: src/task.ts, src/CreateTaskForm.tsx, src/TaskList.tsx, and focused model and component tests.
Validation performed: Focused model, form, and list tests passed; type check passed; independent review found no blocking issues.
Remaining risks: Confirm live persistence behavior if the real storage layer has requirements beyond model deserialization.
Next action: Merge after any normal repository-wide checks, or open a separate plan for filtering or editing.
```
