# agent-workflows

Arthur’s portable, reusable AI development playbook. It packages the habits that make agent-assisted work dependable—clear plans, deliberate implementation, independent review, and useful handoffs—without binding them to one model, editor, or tool.

Everything here is plain Markdown and intentionally small enough to adapt to the repository in front of you.

## The core loop

```text
Planner → Builder → Reviewer → Handoff
```

1. The **Planner** turns a request into an approved, actionable plan.
2. The **Builder** implements that plan while following the target repository’s conventions.
3. The **Reviewer** independently examines the result and reports evidence-backed findings.
4. The **Handoff** preserves the context needed for the next person or session.

## Skills and agents

**Skills** are short, reusable instructions for a kind of work: planning, implementing, reviewing, or handing off. They describe a workflow and its expected output.

**Agent prompts** define a role in the loop. Use them when your coding environment can delegate work to separate agents or when you want a consistent perspective in a new chat.

## Start here

1. Choose the next stage and read its [skill](skills/).
2. Paste or reference that skill in your chosen coding agent.
3. If your environment supports subagents, give the matching prompt from [agents/](agents/) to the agent doing that role.
4. Carry the structured handoff into the next stage or a later session.

Begin with [plan-change](skills/plan-change/SKILL.md), then follow the loop. The [example walkthrough](examples/add-project-label.md) shows every artifact working together.

## A short example

For a request such as “add an optional project label to a task form,” ask the Planner to use [the planning skill](skills/plan-change/SKILL.md) and [planner prompt](agents/planner.md). Once the plan is approved, give it to a Builder using [implement-change](skills/implement-change/SKILL.md). Then run [review-change](skills/review-change/SKILL.md) independently and finish with [handoff](skills/handoff/SKILL.md). The complete fictional version is in [examples/](examples/).

## Portable by design

The canonical assets are generic Markdown. They work manually in Codex, Claude Code, and other coding-agent CLIs; see [docs/portability.md](docs/portability.md). This first version deliberately has no installer, CI, platform adapter, or vendored third-party content.

External skills that complement this playbook live in [the curated catalog](catalog/third-party-skills.md). The catalog points to upstream projects; it does not copy or maintain them here.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a change.

## License

This project is licensed under the [MIT License](LICENSE).
