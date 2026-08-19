# agent-workflows

Arthur’s portable, reusable AI development playbook. It packages the habits that make agent-assisted work dependable—resolving a design before building it, writing down the decisions that outlive the conversation, slicing work so it can be verified, and handing off without losing context—without binding them to one model, editor, or tool.

Everything here is plain Markdown and intentionally small enough to adapt to the repository in front of you.

## The core loop

```text
Frame → Specify → Slice → Build → Review → Hand off
```

1. **Frame** the request. [plan-change](skills/plan-change/SKILL.md) decides how much discovery it deserves, then runs [grill-with-docs](skills/grill-with-docs/SKILL.md) and [domain-modeling](skills/domain-modeling/SKILL.md) when the design is unsettled.
2. **Specify** the outcome. [to-spec](skills/to-spec/SKILL.md) synthesizes the settled conversation into a specification on the issue tracker.
3. **Slice** the work. [to-tickets](skills/to-tickets/SKILL.md) breaks the specification into vertical slices that each declare what blocks them.
4. **Build** each slice with your environment’s implementation tooling.
5. **Review** the result with your environment’s review tooling.
6. **Hand off** what the next person or session needs, using [handoff](skills/handoff/SKILL.md).

Stages 1 through 3 and stage 6 are what this playbook owns: turning a fuzzy request into buildable, sliced work, and keeping context intact across the seams. Stages 4 and 5 are deliberately not included; see below.

## What this playbook leaves out

There is no implementation skill and no review skill here. Writing the smallest coherent change, matching local conventions, adding focused tests, inspecting a diff, and reporting findings by severity are general engineering practice, and [create-skills](skills/create-skills/SKILL.md) says not to restate it. A skill that only repeats what a competent agent already does adds a file to load without changing the outcome.

Both stages are also better served by whatever the host environment already provides: a test-first workflow for building, and a dedicated review command for reviewing. Use those, and carry the handoff contract across the boundary so the loop stays intact.

## Skills and agents

**Skills** are short, reusable instructions for a kind of work: framing, interviewing, domain modeling, specifying, ticketing, handing off, or editing prose. They describe a workflow and its expected output.

**Agent prompts** define a role you can delegate. The loop has exactly one: the [scout](agents/scout.md), which finds facts without making decisions. Framing and specification interview the user and read the live conversation, so they run with you rather than in a detached agent.

## Start here

Once per repository:

1. **Make the skills discoverable.** Copy or symlink the folders in [skills/](skills/) into your coding agent's project location, as described in [docs/portability.md](docs/portability.md). Manual use works too: open a `SKILL.md` and paste it alongside your task.
2. **Run [setup-skills](skills/setup-skills/SKILL.md).** It records which issue tracker this repository uses, its triage labels, and where domain documents live. [to-spec](skills/to-spec/SKILL.md) and [to-tickets](skills/to-tickets/SKILL.md) both require that configuration, so skipping this stalls the loop at stage 2.

Then, for each request:

3. **Start with [plan-change](skills/plan-change/SKILL.md)** and stay in the conversation while it runs. It decides how much discovery the request deserves and carries it through to a published specification, interviewing you along the way.
4. **Follow the loop from there,** carrying the handoff contract across every stage boundary. The boundary that matters most is the one where you leave for your own build and review tooling, because that is where context goes missing.

When a stage needs a fact about the codebase, delegate the lookup to a subagent with the [scout prompt](agents/scout.md) instead of asking the user something you could find yourself.

The [example walkthrough](examples/add-project-label.md) follows one small feature — an optional project label on a task form — through every stage, including the interview and the handoff. To add or revise a workflow, use [create-skills](skills/create-skills/SKILL.md); it defines the shared format and validates every skill here.

## Portable by design

The canonical assets are generic Markdown. They work manually in Codex, Claude Code, and other coding-agent CLIs; see [docs/portability.md](docs/portability.md). This first version deliberately has no installer, CI, release automation, or platform adapter.

Three stages of the loop — [grill-with-docs](skills/grill-with-docs/SKILL.md), [to-spec](skills/to-spec/SKILL.md), and [to-tickets](skills/to-tickets/SKILL.md) — began as MIT-licensed work by others, as did [unslop](skills/unslop/SKILL.md) for prose and [triage](skills/triage/SKILL.md) for the issue queue. They are maintained here as local adaptations and are core to the loop rather than optional add-ons. [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) records where they came from; it does not make them external dependencies, and nothing needs separate installation.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a change.

## License

This project is licensed under the [MIT License](LICENSE).
