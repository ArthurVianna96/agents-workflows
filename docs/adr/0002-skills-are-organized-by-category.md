# ADR-0002 — Skills are organized by category

- **Status:** Accepted
- **Date:** 2026-08-19
- **Related:** [create-skills](../../skills/create-skills/SKILL.md), [portability](../portability.md), [ADR-0001](0001-host-adapters-live-in-hooks.md)

## Context

The repository began as one workflow with twelve skills in a flat
`skills/<name>/` layout. It is becoming a collection of workflows across
domains, starting with learning, and a flat directory of forty skills is
unnavigable.

The flat layout is not merely a habit. `create-skills` documents it as
required, `scripts/validate-skills.rb` globs exactly one level, and both the
install instructions and `docs/portability.md` assume it.

Both hosts read a flat `<name>/SKILL.md`, so categories cannot survive
installation. Symlinks resolve that: the source path may be nested while the
installed name stays flat, which is how `mattpocock/skills` distributes a
categorized repository.

## Decision

Skills live at `skills/<category>/<name>/SKILL.md`. The categories are
`engineering`, `productivity`, and `miscellaneous`. The validator globs two
levels and rejects any category outside that list.

Categories are a repository-side concern. They disappear at install time, and
no host ever sees them.

Skills are shared across workflows rather than owned by one. A workflow
sequences skills; it does not contain them.

## Consequences

Adding a category is a deliberate edit to the validator rather than a side
effect of creating a directory, so a typo fails loudly instead of producing a
fourth category no document mentions.

`handoff` and `unslop` stay available to every workflow instead of becoming
engineering-flavored by filing.

The move costs less now than it ever will again. Reorganizing later means
moving every folder, re-pointing every symlink across two hosts, and editing
four documents that name the flat path.
