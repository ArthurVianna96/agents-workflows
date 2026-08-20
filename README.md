# agent-workflows

Arthur's portable playbook of skills and workflows for agent-assisted work. It defines how a request becomes finished work, across engineering and other domains, without binding to one model, editor, or tool.

Everything here is plain Markdown and intentionally small enough to adapt to the repository in front of you.

## Workflows

A workflow is an ordered set of stages for one kind of work, written as a page plus the skills that run its stages. Skills are shared rather than owned: a workflow sequences them, it does not contain them, so `handoff` and `unslop` serve every workflow here.

| Workflow | What it is for |
| --- | --- |
| [Engineering](workflows/engineering/README.md) | Turning a change request into specified, sliced, verifiable work, and handing it off without losing context. |
| [Learning](workflows/learning/README.md) | Studying a concept until you can explain it yourself, and leaving a note that proves it. |
| [Job-hunting](workflows/job-hunting/README.md) | Turning one job posting into an application package that survives a technical screen. |

Open the one that matches the work in front of you. Each page carries its own loop, its own setup, and its own worked examples.

## Skills, agents, and hooks

**Skills** are short, reusable instructions for a kind of work: framing, interviewing, domain modeling, specifying, ticketing, teaching, documenting, handing off, editing prose, or building and screening a resume. They describe a workflow stage and its expected output. They live under [skills/](skills/), grouped into `engineering`, `productivity`, and `miscellaneous`. [ADR-0002](docs/adr/0002-skills-are-organized-by-category.md) records why those groups exist and why no host ever sees them.

**Hooks** are host-specific adapters in [hooks/](hooks/). They are not portable, and the repository does not pretend otherwise. Each one wires a canonical skill into one coding agent's lifecycle and carries no rules the skill does not already state. [ADR-0001](docs/adr/0001-host-adapters-live-in-hooks.md) records why they sit outside `skills/`.

**Agent prompts** define a role you can delegate. There is exactly one: the [scout](agents/scout.md), which finds facts without making decisions. Framing and specification interview the user and read the live conversation, so they run with you rather than in a detached agent.

To add or revise any of them, use [create-skills](skills/miscellaneous/create-skills/SKILL.md). It defines the shared format, and `ruby scripts/validate.rb` checks that the repository still holds together.

## Start here

1. **Make the skills discoverable.** Copy or symlink the skill folders under [skills/](skills/) into your coding agent's project location, as described in [docs/portability.md](docs/portability.md). They are grouped into category directories here; the category is dropped on the way in, so `skills/engineering/handoff` installs as `handoff`. Manual use works too: open a `SKILL.md` and paste it alongside your task.
2. **Open the workflow you want** from the table above and follow its page. Each one says what to configure once and what to run per request.

## Portable by design

The canonical assets are generic Markdown. They work manually in Codex, Claude Code, and other coding-agent CLIs; see [docs/portability.md](docs/portability.md). This first version deliberately has no installer, CI, release automation, or platform adapter.

Several skills began as MIT-licensed work by others: [grill-with-docs](skills/engineering/grill-with-docs/SKILL.md), [to-spec](skills/engineering/to-spec/SKILL.md), and [to-tickets](skills/engineering/to-tickets/SKILL.md) in the engineering loop, [unslop](skills/engineering/unslop/SKILL.md) for prose, and [triage](skills/engineering/triage/SKILL.md) for the issue queue. They are maintained here as local adaptations rather than optional add-ons. [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) records where they came from; it does not make them external dependencies, and nothing needs separate installation.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a change.

## License

This project is licensed under the [MIT License](LICENSE).
