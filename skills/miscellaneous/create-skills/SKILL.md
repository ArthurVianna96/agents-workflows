---
name: create-skills
description: Create or update portable agent skills using this repository's shared format and conventions. Use when adding a skill, revising a skill, or checking skill compatibility across Codex and Claude Code.
---

# Create skills

Create skills as small, self-contained instruction packages. Write only the task-specific process an agent needs; assume the agent already knows general software-engineering practice.

## Required structure

Put every skill at `skills/<category>/<skill-name>/SKILL.md`. The categories are `engineering`, `productivity`, and `miscellaneous`; the validator rejects anything else, so adding a fourth is a deliberate edit rather than a new directory.

```text
skills/
└── <category>/
    └── <skill-name>/
        └── SKILL.md
```

Use lowercase hyphenated names. Match the directory name and the frontmatter `name` exactly. The category is not part of the name and never reaches the host, which reads a flat `<skill-name>/SKILL.md`.

Start every `SKILL.md` with this portable frontmatter:

```yaml
---
name: <skill-name>
description: <what the skill does>. Use when <specific user intent or task context>.
---
```

Use only `name` and `description` in frontmatter. This is the common subset used for discovery by Codex and Claude Code. Make the description concrete, concise, and rich in the words a user would naturally use.

Follow frontmatter with one human-readable H1, then imperative instructions. Use Markdown headings, ordered steps, and short templates where they make the workflow more reliable.

## Authoring conventions

- Give each skill one clear job and a verb-led, hyphenated name.
- State prerequisites, decisions, outputs, and completion checks when they are essential to the workflow.
- Keep the body under 500 lines. Put optional, detailed material in a directly linked `references/` file; keep references one level from `SKILL.md`.
- Add scripts or assets only when they provide repeatable, deterministic value. Explain when to use each bundled resource.
- Write for a fresh agent with only the task and repository context. Do not rely on a prior conversation or hidden state.
- Avoid coding-agent, model, and plugin-specific commands. Refer to another local skill by its name rather than a provider-specific invocation syntax. Use an external CLI only when it is central to the workflow, and state its prerequisite or manual fallback.
- Preserve source and license notices when adapting third-party material. Record the full required notice in `THIRD_PARTY_NOTICES.md`.
- Do not add a README, changelog, installation guide, or other auxiliary file inside a skill unless it is a direct runtime resource.

## Workflow

1. Identify the repeated task, its user-facing triggers, and a concrete expected result.
2. Inspect related skills to prevent overlap and reuse existing conventions or templates.
3. Create the skill folder and `SKILL.md` with the required frontmatter and H1.
4. Write only the non-obvious workflow, validation, and output guidance needed to perform the task reliably.
5. Add a directly linked reference, script, or asset only when it is necessary for repeated use.
6. Run `ruby scripts/validate.rb` and fix every reported error.
7. Read the skill as a standalone artifact and test it on a realistic request before relying on it.

## Template

```markdown
---
name: <skill-name>
description: <what the skill does>. Use when <specific user intent or task context>.
---

# <Human-readable title>

<One or two sentences of task-specific orientation.>

## Required context

- <Inputs or repository state that must be understood.>

## Workflow

1. <Imperative step.>
2. <Imperative step.>

## Expected output

<The artifact, result, or report to produce.>

## Completion criteria

- <How the agent verifies completion.>
```

## Completion criteria

The skill passes the repository validator, has a precise trigger description, works without provider-specific syntax, and gives another agent enough instruction to complete its narrow task.
