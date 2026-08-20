# Engineering workflow

Turn a fuzzy change request into buildable, sliced work, and keep context intact across every seam.

```text
Frame → Specify → Slice → Build → Review → Hand off
```

1. **Frame** the request. [plan-change](../../skills/engineering/plan-change/SKILL.md) decides how much discovery it deserves, then runs [grill-with-docs](../../skills/engineering/grill-with-docs/SKILL.md) and [domain-modeling](../../skills/engineering/domain-modeling/SKILL.md) when the design is unsettled.
2. **Specify** the outcome. [to-spec](../../skills/engineering/to-spec/SKILL.md) synthesizes the settled conversation into a specification on the issue tracker.
3. **Slice** the work. [to-tickets](../../skills/engineering/to-tickets/SKILL.md) breaks the specification into vertical slices that each declare what blocks them.
4. **Build** each slice with your environment's implementation tooling.
5. **Review** the result with your environment's review tooling.
6. **Hand off** what the next person or session needs, using [handoff](../../skills/engineering/handoff/SKILL.md).

Stage 1 is a decision, not a cost you always pay. `plan-change` picks one of three routes and tells you which it took:

| Route | When | What runs |
| --- | --- | --- |
| Settled and small | Unambiguous, fits one session, no durable decision comes out of it | Nothing. Straight to implementation. |
| Settled and substantial | Outcome agreed and terminology clear, but the work crosses layers or sessions | Skip the interview, write the specification. |
| Unsettled | Terminology, boundaries, ownership, or acceptance are open | Interview first, then the specification. |

When two routes look equally plausible it takes the more thorough one, because guessing costs more than a question. The two examples below show the first and third.

Stages 1 through 3 and stage 6 are what this workflow owns: turning a fuzzy request into buildable, sliced work, and keeping context intact across the seams. Stages 4 and 5 are deliberately not included; see below.

## See it work

Read one of these before setting anything up. Both are complete runs on a fictional application, showing what you type and what comes back.

[**Adding a project label**](examples/add-project-label.md) takes the unsettled route: three questions, a glossary entry, a published specification, one ticket, and the handoff. It is the loop at full length, which costs one round trip.

[**Raising an upload limit**](examples/raise-the-upload-limit.md) takes the settled-and-small route: framing gets out of the way in a single line and nothing else runs except the check at the end, which catches a proxy setting that would have silently capped uploads anyway.

## Set it up

Once per repository, run [setup-engineering-skills](../../skills/engineering/setup-engineering-skills/SKILL.md). It records which issue tracker the repository uses, its triage labels, and where domain documents live. [to-spec](../../skills/engineering/to-spec/SKILL.md) and [to-tickets](../../skills/engineering/to-tickets/SKILL.md) both require that configuration, so skipping it stalls the loop at stage 2.

The skills themselves need to be discoverable first; the [root README](../../README.md) covers that once for every workflow.

## Run it

1. **Start with [plan-change](../../skills/engineering/plan-change/SKILL.md)** and stay in the conversation while it runs. It decides how much discovery the request deserves and carries it through to a published specification, interviewing you along the way.
2. **Follow the loop from there,** carrying the handoff contract across every stage boundary. The boundary that matters most is the one where you leave for your own build and review tooling, because that is where context goes missing.

When a stage needs a fact about the codebase, delegate the lookup to a subagent with the [scout prompt](../../agents/scout.md) instead of asking the user something you could find yourself.

## What this workflow leaves out

There is no implementation skill and no review skill here. Writing the smallest coherent change, matching local conventions, adding focused tests, inspecting a diff, and reporting findings by severity are general engineering practice, and [create-skills](../../skills/miscellaneous/create-skills/SKILL.md) says not to restate it. A skill that only repeats what a competent agent already does adds a file to load without changing the outcome.

Both stages are also better served by whatever the host environment already provides: a test-first workflow for building, and a dedicated review command for reviewing. Use those, and carry the handoff contract across the boundary so the loop stays intact.
