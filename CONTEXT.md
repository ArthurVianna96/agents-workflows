# agent-workflows

Arthur's portable playbook of skills and workflows for agent-assisted work. It defines how a request becomes finished work, across engineering and other domains, without binding to one model, editor, or tool.

## Language

### What the repository contains

**Skill**:
A self-contained instruction package for one kind of work, at `skills/<category>/<name>/SKILL.md`. Portable Markdown that any coding agent can read.
_Avoid_: Prompt, template, command

**Workflow**:
An ordered set of stages for one kind of work, expressed as a page under `workflows/<name>/` plus the skills that run its stages. Engineering, learning, and job-hunting are the three. A workflow may enter through a routing skill, as engineering does through `plan-change`, or through a single skill, as learning does through `learn-stuff` and job-hunting does through `build-resume`.
_Avoid_: Pipeline, process, flow

**Routing skill**:
A skill that triages a request and sequences other work rather than doing it. `plan-change` is one, and the only one. A workflow does not need one.
_Avoid_: Orchestrator, controller, dispatcher

**Adapter**:
Host-specific glue in `hooks/` that wires a canonical skill into one coding agent's lifecycle. Never portable, and never carries a rule its skill does not already state.
_Avoid_: Integration, plugin, extension

**Agent prompt**:
A role definition in `agents/` for work delegated to a subagent. There is one, the scout, which finds facts and makes no decisions.
_Avoid_: Persona, subagent config

**Category**:
One of `engineering`, `productivity`, or `miscellaneous`. The validator enforces the list, so adding one is a deliberate edit rather than a new directory.
_Avoid_: Namespace, group, folder

### Kinds of document

**Present-tense document**:
A document describing how the system works now. The only kind that can drift, and the only kind edited in place.
_Avoid_: Living doc, evergreen note

**Point-in-time record**:
A document describing a decision, finding, or understanding at the moment it was made. Superseded by a new record, never edited to match new code.
_Avoid_: Historical doc, archive, changelog

**Generated artifact**:
A file a tool produces from a source. Never hand-edited; disagreement means re-running the generator or fixing its input.
_Avoid_: Build output, derived file

**Drift**:
The state of a present-tense document making a claim the code contradicts. Proximity to a change is not drift; only a false claim is.
_Avoid_: Staleness, rot, decay

### How work moves

**Route**:
Which of three paths `plan-change` picks for a request: settled and small, settled and substantial, or unsettled.
_Avoid_: Path, mode, track

**Frontier**:
During an interview, every decision whose prerequisites are already settled, and therefore every question that can be asked in the current round.
_Avoid_: Backlog, queue, open items

**Handoff contract**:
The six-field block carrying context across a stage or session boundary: task goal, decisions, files changed, validation performed, remaining risks, next action.
_Avoid_: Summary, status update, report

**Fact base**:
The confirmed claims a job-hunting document is allowed to draw from, held outside any one application as a master resume plus a bullet bank. Tailoring selects from it and never adds to it; new facts are written back only after being verified.
_Avoid_: Source of truth, profile, resume data

**Docs-checked trailer**:
A commit trailer naming each document considered during a drift check and what was concluded about it. Usually the only record of that judgment that outlives the session.
_Avoid_: Doc note, checklist
