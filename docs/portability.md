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

The files intentionally avoid coding-agent-specific commands, model names, plugins, and installation syntax. An external CLI may be part of a workflow when it is necessary, but the skill must state that prerequisite or a manual fallback. A skill should still make sense when pasted into a plain chat. Run `ruby scripts/validate.rb` after any change; it checks the skill convention and every internal link.

The bundled skills adapted from third parties follow the same portable structure. Their provenance and license notices live in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md); they are maintained locally and do not update from upstream automatically.

## Manual use

In Codex, Claude Code, or another coding-agent CLI, open the appropriate `SKILL.md` and provide its instructions with the task context. Framing and specification interview the user and synthesize the conversation they run in, so run them in the session with the user rather than handing them to a detached agent. When a stage needs a fact from the codebase, delegate that lookup to a subagent using [`agents/scout.md`](../agents/scout.md) as its role prompt; if the environment has no subagents, look the fact up yourself before returning to the user.

For automatic discovery, keep this repository’s `skills/` directory as the source of truth and expose its skill folders where the host looks for them:

- Codex reads personal skills from `$CODEX_HOME/skills/<skill-name>/SKILL.md`, which defaults to `~/.codex/skills`. Its bundled `skill-installer` documents that path, and `/skills` lists what it found.
- Claude Code reads personal skills from `~/.claude/skills/<skill-name>/SKILL.md` and project skills from `.claude/skills/<skill-name>/SKILL.md` in the repository.

Symlink each skill folder into the appropriate host location rather than copying it, so this repository stays the single source of truth and a pull updates every host at once. Do not maintain divergent copies. Check the host's own documentation for project-scoped discovery before relying on it; the personal paths above are the ones verified here. The shared frontmatter and provider-neutral body work in both environments. See the official [Codex skill documentation](https://developers.openai.com/codex/skills) and [Claude Code skill documentation](https://code.claude.com/docs/en/slash-commands) for host-specific discovery and optional features.

For each transition, carry the handoff contract forward: task goal, decisions, files changed, validation performed, remaining risks, and next action. This preserves enough context without assuming any platform’s memory or orchestration features.

## Why there is no installer

Version 1 avoids automated installers and platform adapters on purpose. Manual use keeps the canonical Markdown visible, portable, and easy to adapt to a repository’s local conventions. It also avoids claiming support for tool-specific packaging formats before the workflow has proven useful in regular work.

When a repeated integration is genuinely valuable, add it as a small adapter that points back to these canonical files rather than making the adapter the source of truth.
