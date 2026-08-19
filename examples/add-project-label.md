# Example: add an optional project label

A full run of the loop on one small feature, showing what you type and what comes back. The application is fictional.

**The request.** Add an optional Project label field to the create-task form, save it with the task, show it under the title in the list, and keep existing tasks working.

## 1. Frame

You type:

```text
/plan-change add an optional project label to the create-task form, saved with
the task and shown under the title in the list
```

The first thing back is the route, and why:

> **Route: unsettled.** The request names a field and where it appears, but not what a project label *is*. Free text or a fixed set? One per task or several? Writing a spec now means guessing three times. Running the interview.

Then one round of questions. Everything answerable now arrives at once, each with a recommendation you can accept in a word:

```text
❓ Q1 - Label vocabulary: free text, or chosen from a set the user maintains?
➡️ Free text. A managed set is a separate feature with its own UI.

❓ Q2 - Cardinality: can a task carry more than one?
➡️ One. Several turns this into tagging, useless without filtering.

❓ Q3 - Blank input: stored empty string, or absent field?
➡️ Absent. An empty string creates two ways to mean "no label".
```

You answer as briefly as you like:

```text
1 free text  2 one  3 absent
```

Finding facts is not your job. While you answer, a scout checks whether existing rows deserialize without a migration and reports that they do. Only questions that depended on that answer waited.

`domain-modeling` writes the one durable decision into the project glossary, which is a `CONTEXT.md` at the repository root defining the terms this codebase uses. A new entry appears under its `## Language` heading:

```md
**Project label**:
A single optional free-text string on a task. Absence is the only way to say
"no label"; an empty string is never stored.
_Avoid_: Tag, category, group
```

That file is read before exploring, so the next person to touch tasks finds the term already defined instead of inventing "tag" next to it. Decisions with more weight than a definition go to `docs/adr/` as a numbered record instead.

## 2. Specify

The frontier is empty, so `to-spec` runs. It asks one thing before writing:

> The existing create-task component test is the highest seam that already exists. Testing there rather than adding a new one. Does that match your expectation?

Then it publishes an issue to whatever tracker `setup-skills` configured, labelled `ready-for-agent`:

```text
#41  Optional project label on tasks                    [ready-for-agent]

     ## Problem Statement
     Users group tasks by retyping a prefix into the title.
     ## Solution
     One optional free-text label per task, shown under the title.
     ## User Stories
     1. As a user, I want to label a task as I create it, so that ...
     ...
     ## Implementation Decisions
     Optional trimmed string. Blank input omitted, never stored empty.
     ## Out of Scope
     Filtering, editing an existing label, a managed label vocabulary.
```

Nothing in it was invented. Every decision traces to an answer you gave.

## 3. Slice

```text
/to-tickets 41
```

Model, form, and list are one thin path through every layer, demoable on its own, so this stays a single ticket rather than three horizontal ones:

```text
1. Optional project label end to end        Blocked by: none
   Create a task with a label, see it in the list, existing tasks unaffected.
```

`to-tickets` asks whether the granularity is right before publishing anything.

## 4. Build and review

Your own tooling. The playbook has no opinion here beyond what comes back out: a diff, and the handoff contract.

## 5. Hand off

Committing runs the drift check, which names `README.md` as describing the create-task form. It does, and the new field belongs there, so you update it and record the judgment:

```text
Docs-checked: README.md updated with the label field;
docs/data-model.md unaffected, it describes storage rather than the form
```

Then the contract that carries context to whoever picks this up next:

```text
Task goal: Optional project label on tasks, shown in the list.
Decisions: Single optional free-text label; blank omitted; filtering out of scope.
Files changed: src/task.ts, src/CreateTaskForm.tsx, src/TaskList.tsx, tests.
Validation performed: Model, form, and list tests pass; type check passes.
Remaining risks: Live persistence unverified beyond deserialization tests.
Next action: Merge, or frame a separate change for filtering.
```

## What it cost

Three questions and one round trip. In exchange, nothing downstream had to guess what a label was, and the decision survives in the glossary after the conversation is gone.
