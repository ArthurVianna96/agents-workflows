# Example: a change that skips the loop

Most work does not deserve an interview. This shows the short route, and the one part of the playbook that still runs.

**The request.** Raise the file upload limit from 5MB to 25MB.

## Frame, briefly

```text
/plan-change raise the upload limit from 5MB to 25MB
```

> **Route: settled and small.** The behavior is unambiguous, it fits one session, and no durable decision comes out of it. Going straight to implementation.

That is the whole framing step. No questions, no spec, no ticket. `plan-change` triages first precisely so it can get out of the way, and a skill that always ran the full interview would be one you stopped invoking.

## Build

One constant, one test.

## The part that still runs

Committing triggers the drift check:

```text
Documentation drift check. This commit changes files that documents describe.

Changed and watched:
  src/upload/limits.ts

Documents that may need updating:
  README.md
  docs/api-reference.md
  docs/deployment.md

A document is stale only when the change contradicts what it claims.
```

`README.md` says "files up to 5MB". That is now false, so it gets updated. `docs/api-reference.md` documents the 413 response without naming a size, so it stays as it is. `docs/deployment.md` sets `client_max_body_size 10m` in the proxy config, which the new limit would silently defeat, so that gets fixed too. That one nobody would have thought to check.

Then commit with the judgment recorded:

```text
Docs-checked: README.md updated from 5MB to 25MB;
docs/deployment.md proxy limit raised to match, it would have capped uploads
at 10MB regardless of the application setting;
docs/api-reference.md unaffected, it documents the 413 without naming a size
```

A trailer naming no document is rejected. `Docs-checked: none` is indistinguishable from never having looked, and six months from now `git log --grep=Docs-checked` is the only place that reasoning still exists.

## The point

The loop scales down to nothing. What does not scale down is the check at the end, because a two-line change is exactly the kind nobody remembers to document.
