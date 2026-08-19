# Portability

## Canonical format

Each local skill lives at `skills/<skill-name>/SKILL.md`. It is ordinary Markdown with the same sections:

- purpose
- when to use
- required context
- workflow
- expected output
- completion criteria

The files intentionally avoid product-specific commands, model names, plugins, and installation syntax. A skill should still make sense when pasted into a plain chat.

The bundled skills adapted from third parties follow the same portable structure. Their provenance and license notices live in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md); they are maintained locally and do not update from upstream automatically.

## Manual use

In Codex, Claude Code, or another coding-agent CLI, open the appropriate `SKILL.md` and provide its instructions with the task context. If the environment supports delegated agents, also provide the matching file from `agents/` as that agent’s role prompt. If it does not, run the roles sequentially in separate sessions or chats.

For each transition, carry the handoff contract forward: task goal, decisions, files changed, validation performed, remaining risks, and next action. This preserves enough context without assuming any platform’s memory or orchestration features.

## Why there is no installer

Version 1 avoids automated installers and platform adapters on purpose. Manual use keeps the canonical Markdown visible, portable, and easy to adapt to a repository’s local conventions. It also avoids claiming support for tool-specific packaging formats before the workflow has proven useful in regular work.

When a repeated integration is genuinely valuable, add it as a small adapter that points back to these canonical files rather than making the adapter the source of truth.
