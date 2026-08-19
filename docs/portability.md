# Portability

## Canonical format

Each local skill lives at `skills/<skill-name>/SKILL.md`. Its folder name and `name` must match and use lowercase hyphenated words. Every `SKILL.md` begins with this YAML frontmatter:

```yaml
---
name: <skill-name>
description: <what the skill does>. Use when <specific user intent or task context>.
---
```

The body starts with one Markdown H1 and contains concise, imperative instructions. Use headings and templates only when they make the workflow more reliable. Keep each skill focused on one job, under 500 lines, and put optional detail in a directly linked `references/` file.

The canonical frontmatter intentionally uses only `name` and `description`. Codex requires those fields for a `SKILL.md`; Claude Code accepts that same portable subset. Both products use the description for discovery, so it must state the task and concrete trigger language. Host-specific fields, dynamic command injection, permissions, and invocation policies stay out of canonical skills because they do not transfer cleanly.

The files intentionally avoid coding-agent-specific commands, model names, plugins, and installation syntax. An external CLI may be part of a workflow when it is necessary, but the skill must state that prerequisite or a manual fallback. A skill should still make sense when pasted into a plain chat. Run `ruby scripts/validate-skills.rb` after any skill change.

The bundled skills adapted from third parties follow the same portable structure. Their provenance and license notices live in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md); they are maintained locally and do not update from upstream automatically.

## Manual use

In Codex, Claude Code, or another coding-agent CLI, open the appropriate `SKILL.md` and provide its instructions with the task context. If the environment supports delegated agents, also provide the matching file from `agents/` as that agent’s role prompt. If it does not, run the roles sequentially in separate sessions or chats.

For automatic discovery, keep this repository’s `skills/` directory as the source of truth and expose its skill folders in the host’s project location:

- Codex discovers repository skills from `.agents/skills/<skill-name>/SKILL.md`.
- Claude Code discovers project skills from `.claude/skills/<skill-name>/SKILL.md`.

Copy or symlink each skill folder into the appropriate host location; do not maintain divergent copies. The shared frontmatter and provider-neutral body work in both environments. See the official [Codex skill documentation](https://developers.openai.com/codex/skills) and [Claude Code skill documentation](https://code.claude.com/docs/en/slash-commands) for host-specific discovery and optional features.

For each transition, carry the handoff contract forward: task goal, decisions, files changed, validation performed, remaining risks, and next action. This preserves enough context without assuming any platform’s memory or orchestration features.

## Why there is no installer

Version 1 avoids automated installers and platform adapters on purpose. Manual use keeps the canonical Markdown visible, portable, and easy to adapt to a repository’s local conventions. It also avoids claiming support for tool-specific packaging formats before the workflow has proven useful in regular work.

When a repeated integration is genuinely valuable, add it as a small adapter that points back to these canonical files rather than making the adapter the source of truth.
