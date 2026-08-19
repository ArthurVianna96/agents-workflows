# Third-party skill catalog

This page distinguishes bundled local adaptations from upstream-only recommendations. Review current upstream instructions and licenses before adding another dependency or syncing a local adaptation.

## Bundled and locally adapted

These skills are already available under `skills/`; no separate installation is required. Each retains its upstream link and MIT notice.

| Skill | Upstream | Author | Purpose | Preferred use | License/source note | Installation guidance |
| --- | --- | --- | --- | --- | --- | --- |
| grill-with-docs | [mattpocock/skills](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) | Matt Pocock | A rigorous planning interview that also develops a project’s glossary and decision records. | Use to resolve terminology, ownership, architecture, or boundary decisions before writing a spec. | MIT; local adaptation and full notice in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md). | Bundled at [`skills/grill-with-docs`](../skills/grill-with-docs/SKILL.md). |
| to-spec | [mattpocock/skills](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-spec/SKILL.md) | Matt Pocock | Synthesizes settled conversation and repository context into a buildable specification. | Use after the problem is understood and before decomposing a multi-session change into tickets. | MIT; local adaptation and full notice in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md). | Bundled at [`skills/to-spec`](../skills/to-spec/SKILL.md). |
| to-tickets | [mattpocock/skills](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md) | Matt Pocock | Breaks a plan, specification, or conversation into independently verifiable vertical-slice tickets with blocking relationships. | Use after a plan or spec is agreed and implementation work should be tracked or delegated. | MIT; local adaptation and full notice in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md). | Bundled at [`skills/to-tickets`](../skills/to-tickets/SKILL.md). |
| unslop | [cursor/plugins pstack](https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md) | Lauren Tan (pstack) | Edits writing to remove common AI patterns while preserving meaning and intended tone. | Use as a final prose pass for human-facing documentation, explanations, or other narrative text. | MIT; local adaptation and full notice in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md). | Bundled at [`skills/unslop`](../skills/unslop/SKILL.md). |

## Linked upstream collections

These recommendations remain upstream-owned. Follow their installation guidance; they are not bundled here.

| Skill collection | Upstream | Author | Purpose | Preferred use | License/source note | Installation guidance |
| --- | --- | --- | --- | --- | --- | --- |
| Superpowers | [obra/superpowers](https://github.com/obra/superpowers) | Jesse Vincent / Prime Radiant | A collection of software-development skills, including disciplined debugging, planning, and test-driven work. | Use when a project benefits from a broader, opinionated development workflow in addition to these portable core roles. | MIT; see the upstream [license](https://github.com/obra/superpowers/blob/main/LICENSE). | Follow the setup instructions in the upstream README for your agent environment. |
| Anthropic Skills | [anthropics/skills](https://github.com/anthropics/skills) | Anthropic | Reference skills for agent workflows such as document and spreadsheet tasks. | Use as a source of task-specific patterns when the work matches an upstream skill. | Licensing varies by skill; inspect the relevant skill’s source and [license](https://github.com/anthropics/skills/blob/main/skills/pdf/LICENSE.txt) before use. | Use the upstream README’s installation or manual-use instructions. |
| Agentic Plugin Marketplace | [wshobson/agents](https://github.com/wshobson/agents) | Seth Hobson | A broad marketplace of modular skills, agents, and workflow components across several coding environments. | Use when a task needs a domain-specific skill beyond this repository’s four core workflow stages. | MIT; see the upstream [license](https://github.com/wshobson/agents/blob/main/LICENSE). | Follow the upstream README for your environment and install only the needed component. |

Catalog entries are recommendations, not endorsements or compatibility guarantees. Verify current content, licensing, and environment support before use.
