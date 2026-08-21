# Job-hunting workflow

Turn one job posting into an application package that survives a technical screen.

```text
Ground → Build → Screen → Revise → Send → Write back
```

1. **Ground** the facts. A master resume of confirmed claims and a bullet bank of real work that does not fit a one-pager. This is the input every other stage reads from.
2. **Build** the tailored package with [build-resume](../../skills/productivity/build-resume/SKILL.md), which recovers the posting's requirements, mines the applicant's repositories for evidence, and drafts against a coverage list.
3. **Screen** the result with [screen-resume](../../skills/productivity/screen-resume/SKILL.md), from the seat of the person deciding whether it moves forward.
4. **Revise** against the findings that survive judgment, then screen again.
5. **Send.** Yours, always. Nothing here submits an application.
6. **Write back** everything learned to the fact base, including corrections and open questions.

Stages 2 and 3 are deliberately different seats. Build selects and composes; screen rejects. Running both in one pass produces a document that agrees with itself, which is the one property a review cannot supply.

## The failure this catches

Every tailoring pass applies pressure toward the posting. Nothing pushes back except the facts, so without a fact base outside the document, a resume drifts one plausible sentence at a time until something on it is false. The drift is rarely a lie. It is usually an ambiguity resolved in the direction the posting wants.

A source line reading "Node services and a Python service, over PostgreSQL, MySQL, and Redis" is true and unpinned. Tailored for a posting that names PostgreSQL and Prisma, it becomes "Prisma over PostgreSQL," which reads well, matches two keywords, and is wrong. The schema file said `mysql`. Nobody invented anything; the resume just answered a question the source left open.

The second failure is thinner and more common. A skills list names twelve technologies and the experience bullets evidence four. The other eight are assertions, and a technical screen finds them in the order the interviewer cares about most.

Both are fixed by the same discipline: **claims live in a fact base, the fact base is built from evidence, and the resume selects from it.** Never the other way around.

## Ground the facts

Two files, anywhere that persists between applications.

```text
resume.md      the master: confirmed claims only, one document, no tailoring
highlights.md  the bullet bank: real work that does not fit the one-pager
```

The master is what is true, not what fits. The bullet bank holds everything that could not fit, with a note on which kind of posting each entry serves, and marks anything unconfirmed as unconfirmed until the applicant says otherwise.

The first `build-resume` run creates both if they are missing. There is no setup skill, because the fact base is two Markdown files and a rule, not a configuration.

Record dates and sources on every entry. A bullet bank without provenance becomes a second thing you have to verify.

## Mine, do not interview

The highest-value step in the loop, and the one most often skipped.

"Tell me about a time you tuned a query" returns a vague memory. Reading the applicant's migration directory returns the partial index they actually wrote, and the commit message next to it explains the production bug that caused it. One is a claim. The other is evidence with a file path.

`build-resume` carries the map of which requirement to look for in which part of a repository, and requires checking authorship before claiming anything on a team repository. What comes out goes into the bullet bank first, with file and commit references, so the next posting asking for the same capability costs one read instead of another dig.

## Set it up

Nothing to configure. Ground the fact base once, as above, and the skills need to be discoverable first; the [root README](../../README.md) covers that once for every workflow.

## Run it

1. **Give [build-resume](../../skills/productivity/build-resume/SKILL.md) the posting** and point it at the fact base and the repositories.
2. **Hand the package to [screen-resume](../../skills/productivity/screen-resume/SKILL.md)** and let it reject. Verify any factual claim a review makes before acting on it; a confident review can be wrong about your own code.
3. **Loop until it says ship it.** Each round should be shorter than the last. A review that always finds something is manufacturing work.
4. **Run [unslop](../../skills/engineering/unslop/SKILL.md)** over any cover letter or long-form answer before it goes out.

## See it work

Read one before running anything. Both are complete runs on a fictional applicant, showing what you type and what comes back.

[**Tailoring for a Node and Prisma role**](examples/tailoring-for-a-node-role.md) is the loop at full length: repository mining that turns a keyword into a bullet, a screen that catches a contradiction the build introduced, and the point where the review says stop.

[**Covering a missing framework**](examples/covering-a-missing-framework.md) is the short case. The posting names a framework the applicant has never used, and the answer is a disclosure written into the application note rather than a line added to the skills list.

## What this workflow leaves out

**Sourcing and scoring.** Finding postings, filtering by pay, region, and stack, and deciding what deserves an application is a separate loop that runs on feeds rather than on one posting. This workflow starts once a posting is worth the effort.

**Submitting.** No skill here sends an email, fills a form, or messages a recruiter. Research, drafting, and review are the machine's half; pressing submit is the applicant's, always. The asymmetry is deliberate: a bad draft costs a revision, and a bad submission costs the application.

**Interview preparation**, beyond the list of questions a resume provokes but cannot answer. `screen-resume` separates those from document edits so they do not get "fixed" by deleting the interesting line.
