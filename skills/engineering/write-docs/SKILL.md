---
name: write-docs
description: Write and update documentation so it stays checkable against the code it describes, and respond to reports that a change may have invalidated one. Use when creating or revising a document, or when a drift check names documents a commit may have made stale.
---

# Write docs

Documentation rots because nothing separates a document that describes the present from one that records a moment. The first can be contradicted by code and has to be updated. The second cannot, and editing it destroys the only thing it was for. Decide which you are holding before writing a word.

Use `unslop` for the prose itself. This skill covers only what makes a document checkable.

## Required context

- The subject, and the code or behavior it describes.
- The repository's documentation inventory, if it declares one, and which category this document falls into.
- For an update, the change that prompted it.

## Classify first

The category decides what you are permitted to do.

**Present-tense documents** say how the system works now: READMEs, architecture and context documents, API references, runbooks, agent instruction files. These are the only documents that can drift and the only ones you edit in place.

**Point-in-time records** say what was decided, planned, or found at a moment: decision records, specifications, plans, issues, post-mortems. These never change to match new code. A record the code contradicts gets superseded, never edited.

**Generated artifacts** are produced by a tool from a source. Never hand-edit one. If it disagrees with the code, re-run its generator. If the output is wrong, fix the generator or its input.

## Writing a present-tense document

Write claims a reader can check. "The loader parses the file before validation" can be compared against the code and found false. "The loader is designed to be flexible" cannot, so it will never be reported stale, because nothing can contradict it. A sentence that survives every possible code change is decoration. Cut it.

Name the mechanism, the command, the field, or the number. Prefer the claim that fails loudly over the one that stays vaguely true.

Keep one subject per document. A document covering three unrelated areas gets named by every change to any of them, and that noise is what makes people switch the check off.

Declare what the document covers, where its consumer tolerates frontmatter:

```yaml
---
covers:
  - src/ingest/**
  - src/schema/*.ts
---
```

Declare it while writing. Retrofitting coverage across an existing corpus costs far more than one line at authoring time. Check the consumer first: a document rendered by a site generator or imported as raw text may print the block as visible content. When it would, leave it out and say so in the document, so the next author does not assume it was forgotten.

## Superseding a record

When code contradicts a record there are two honest moves. Fix the code, if the decision still stands. Or write a new record stating the new decision, referencing the old one, and mark the old one superseded.

Never revise the old record's substance. It exists to say what was decided and why, at a time when that was true. A record edited to match today's code is no longer evidence of anything.

Follow the repository's existing record format and numbering. Use `domain-modeling` when the change also moves terminology or introduces a decision worth recording.

## Responding to a drift report

A host may run a drift check when work is committed. It reports which documents claim to describe what changed. It judges nothing, and it is not claiming anything is wrong.

1. Read the documents that plausibly cover the change. Skip the ones that obviously do not.

2. Judge contradiction, not proximity. A document is stale only when the change makes a claim in it false. Renaming a private function, reorganizing a module, or replacing an implementation behind an unchanged description is not drift. Changing a documented default, command, schema, route, field, or promise is.

3. Update what contradicts. Supersede records. Leave everything else alone, and resist editing a document merely because it appeared in the report.

4. Record what you concluded about every document you considered, in a `Docs-checked:` trailer on the commit:

```text
Docs-checked: README.md updated for the new flag;
docs/deploy.md unaffected, it describes the pipeline rather than the CLI
```

Name each document and state the decision. This trailer is usually the only record of the judgment that outlives the session. A later session recovers it from the commit history and gets either your reasoning or nothing. A trailer naming no document is indistinguishable from never having looked.

## Expected output

A document in the right category, written in checkable claims, with its coverage declared where the consumer allows it. For an update prompted by a change, a `Docs-checked:` trailer naming every document considered and what was decided about each.

## Completion criteria

The document's category is unambiguous from its content; no record was edited to match new code; no generated artifact was hand-edited; every claim added can be shown false by some change; and each document named in a drift report was either updated, superseded, or explicitly cleared in the trailer.
