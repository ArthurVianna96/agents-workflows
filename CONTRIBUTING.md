# Contributing

Keep this repository portable, focused, and safe to publish.

- Write in neutral, agent- and provider-independent language. Do not require a specific model, coding-agent product, or plugin. If a workflow needs an external command-line tool, state the prerequisite or manual fallback.
- Follow [the shared skill convention](skills/create-skills/SKILL.md): matching lowercase-hyphenated directory and `name`, a concise trigger description, one H1, and imperative instructions.
- Keep each skill focused on one repeatable outcome. State the required context, expected output, and completion criteria when they materially improve the workflow.
- Make outputs explicit enough for the next stage or session to use without guessing, including the stages this playbook hands to the host environment.
- Vendor third-party skills only when their license permits it, and only when the skill earns a place in the loop. Keep the upstream URL and author in the skill, retain the required license notice in `THIRD_PARTY_NOTICES.md`, and label local adaptations clearly.
- Never add secrets, customer data, employer-specific material, private repository details, or credentials.

Before proposing a change, read the affected file as a standalone artifact, run `ruby scripts/validate-skills.rb`, check its links, and make sure it fits the shared handoff contract where applicable.
