---
name: build-resume
description: Build a resume tailored to one job posting, sourcing every claim from a maintained fact base and from the applicant's own repositories. Use when someone asks for a resume or CV written or tailored for a specific role, wants an application package assembled, or wants a gap in a posting's requirements covered honestly.
---

# Build a resume for one posting

Write the document a screener will read, from evidence that already exists. The work is
retrieval and selection, not composition. Most weak resumes are not badly written; they claim
things nothing backs, and omit things the applicant actually did.

This skill builds. The `screen-resume` skill reviews. Run them in a loop: build, screen,
revise, screen, ship. Do not review your own draft in the same pass you wrote it.

## Required context

- **A fact base.** A master resume of confirmed facts, plus a bullet bank holding real work
  that does not fit a one-pager. Create both if they do not exist; everything below depends on
  them.
- **The posting in full.** A URL is enough when you can recover the text.
- **Access to the applicant's actual work.** Repositories, if any. This is where the strongest
  bullets come from and where most agents never look.
- **Any package that ships alongside** the resume: cover letter, application note, form answers.

## The rule that outranks the rest

**Invent nothing.** Every claim in the finished document traces to the fact base or to
something you read in the applicant's own code. A resume with one invented line turns every
checkable detail on it into a liability.

Ambiguity is the failure mode to watch, not fabrication. You will rarely write something
outright false. You will regularly resolve a vague source line in the direction the posting
wants. Both are wrong; the second is harder to catch.

## Workflow

### 1. Recover the posting and split its requirements

Fetch the posting. If the URL returns a page shell with no job text, the page is
client-rendered: find the API endpoint it calls and read the structured record, or render the
DOM with a headless browser. Structured records also carry hard filters the prose omits, such
as minimum years, region, salary band, and required expertise tags.

Split the requirements into hard filters, demonstrable capabilities, and disposition
requirements. `screen-resume` describes this split; use the same three lists so the two skills
agree.

Write the lists into a `posting.md` alongside the resume, with the capture date and the URL. A
posting you cannot re-read is a posting you cannot check the resume against later.

### 2. Mine the repositories before you interview the applicant

This step produces the best material and is the one most often skipped. Asking "tell me about
a time you tuned a query" gets a vague memory. Reading the applicant's migrations gets the
partial index they wrote and the commit message explaining the production bug behind it.

Work through the posting's demonstrable requirements and go looking:

| Requirement | Where the evidence lives |
| --- | --- |
| Schema design, migrations | Migration directories, schema files, index declarations |
| Query performance | Composite and partial indexes, raw SQL, query comments, caching tables |
| Queues, async, background jobs | Broker config, consumer code, dead-letter and retry handling |
| Webhooks | Route handlers, signature verification, idempotency keys |
| Testing | Test directories and their tiers, fixtures, end-to-end specs, CI config |
| Production debugging | Monitors, alert rules, health checks, and the commits that added them |
| Observability | Dashboard definitions, structured log lines, alert queries in comments |

Read commit messages too. A message like `fix(worker): ownership by lease, end of double
processing` is a complete incident story: symptom, diagnosis, and fix, in the applicant's own
words.

**Verify authorship before claiming anything.** Check who wrote the file and who wrote the
commit. On a team repository, an impressive design may belong to someone else. Confirm it, then
say so in the fact base.

**Record findings in the bullet bank, not directly in the resume.** Include file paths and
commit references. The next posting that asks for the same capability then costs one read
instead of another dig.

### 3. Interview only for what the code cannot answer

Repositories give you mechanisms. They do not give you scope, intent, motive, or outcome. Ask
about those, and ask specifically:

- What a product actually does, in the words a user would use. An abstraction like "a unified
  platform" describes nothing; the concrete thing is both shorter and more credible.
- Which parts of a system the applicant built and which parts they did not.
- Whether something shipped, and to whom.
- What a self-reported metric measures and how it was measured.

**Record attribution boundaries explicitly in the fact base.** When an applicant says they
built the interface and the data gateway but not the model training, write the line down.
Boundaries erode across revisions, and a cover letter three drafts later will claim the whole
system unless something on file says otherwise.

### 4. Draft against the requirement list, not from the top down

Take the posting's requirements in order and pick the evidence that covers each. Then arrange
what you selected into a document. Writing the resume front to back produces a document about
the applicant rather than a document about the fit.

When writing each bullet:

- **Name the mechanism, not the quality.** "Verifies each webhook signature against the raw
  request body, with idempotency keys on the writes behind it" beats "experienced with
  webhooks." The specific detail is what separates someone who shipped it from someone who
  listed it.
- **Lead with the pattern, prove it with the incident.** A bullet that opens with one bug makes
  the whole capability look like that bug's fallout. State the practice first, then use the
  incident as evidence.
- **Prefer the specific claim to the general one, even when the general one sounds bigger.**
  "Led a team of 3 engineers" beats "experience leading teams." A vague claim sitting between
  precise ones reads as the soft spot, and plurals overstate.
- **Cut volume metrics.** Counts of files, migrations, commits, or repositories measure effort,
  not judgment, and they are the phrase a skeptic pushes on. Named specifics carry the claim
  without them.
- **Convert small absolute numbers or drop them.** A revenue figure that converts to three
  digits makes real engineering look like a hobby.
- **Never round a number up.** Under a stated minimum, give the true figure when asked and do
  not raise it unprompted. A career start year lets a reader do the arithmetic without stating
  a number that fails a filter on line one.

### 5. Cover genuine gaps without softening anything

For a named technology the applicant has not used, pick one:

- Name the closest adjacent experience, and state plainly what transfers and what does not.
- Volunteer the gap in an application note, which is stronger than being caught by it.
- Accept it and let the rest of the match carry the application.

Never add the technology to a skills list on the theory that it is close enough. `screen-resume`
carries a template for the application note.

### 6. Run the pre-render checks

Each of these has shipped a defective resume at least once. Check all of them.

**The current-role check.** The most recent role must independently evidence the posting's
primary technology. A skill present in the summary, the skills list, and three older roles but
absent from the current one reads as something the applicant used to do. This defect is
invisible when you search the file, because the term is present. Search the current role.

**Unbacked keywords, both directions.** Anything in the skills list appearing in no bullet is a
claim waiting to be tested. Anything demonstrated in a bullet but missing from the skills list
is a free keyword match being thrown away.

**The contradiction sweep.** Compare every technical claim against every other one, across the
resume, the application note, and the cover letter. Pay attention where tailoring resolved an
ambiguity: if the source said one service used "PostgreSQL, MySQL, and Redis" collectively, a
tailored line claiming a specific ORM runs on the one the posting names is a guess. Go back to
the configuration file and read the actual value.

**Attribution.** Nothing claims work the fact base assigns to someone else.

**Placeholders.** No bracketed slot survives into a rendered document.

### 7. Render, then verify the rendered artifact

Verify the PDF, not the Markdown. Layout defects exist only in the output.

- **Page count and fill.** A final page holding a line or two is worse than one page less.
- **Orphaned headings.** A role heading stranded at the foot of a page. Preventing this needs
  the no-break rule on the heading *and* on the dates line beneath it; holding only the heading
  lets the break fall one element later and strands it anyway.
- **Split bullets** across a page boundary.
- **Bullet weight.** More bullets on old roles than recent ones inverts the reader's interest.

**Every edit has a length cost, and you pay it in the same pass.** Adding a bullet without
removing something spills the page. Decide the trade deliberately: name the weakest line on the
page and cut it, rather than discovering the overflow after rendering and trimming whatever is
nearest.

### 8. Write everything new back to the fact base

Anything learned while building this resume belongs in the master or the bullet bank before the
session ends, with the date and the source. This is the step that compounds; skipping it means
the next posting starts from the same thin material.

Also record:

- **Corrections**, with what was wrong and how it was verified. A fact base that only accretes
  claims will eventually contradict itself.
- **Ambiguity you had to resolve.** Pin the resolved fact in the master so the next tailoring
  pass cannot resolve it differently. An ambiguous source file will be read wrong eventually.
- **Open questions** the applicant should answer before an interview, separated from claims.

**Do not rewrite applications already sent.** Those files record what was actually submitted.
Update the master and the unsent packages, and note the divergence.

### 9. Loop with the reviewer, and stop

Hand the package to `screen-resume`, apply what survives judgment, and re-render. Reject review
findings that would trade a specific claim for a generic one, and verify any factual claim a
reviewer makes before acting on it: a confident review can be wrong, and a resume defect
asserted is still only a hypothesis until you have read the source.

Stop when every requirement is covered or honestly handled. Say so plainly. A reviewer that
always finds something teaches the applicant to ignore it.

## Channel note

A dense resume full of specifics rewards a careful reader and fails a six-second skim. Build
for the channel: a company that screens properly earns the detailed version; a high-volume job
board needs the same facts cut to one line per bullet. Keep both variants rather than
compromising into one that serves neither.

## Expected output

An application directory containing:

```text
posting.md          the requirements, hard filters, capture date, and a coverage table
resume.md           the tailored source
resume.pdf          the rendered artifact, verified
application-note.md any gap disclosure or form answers, when the application has a field
```

Plus updated master and bullet-bank files, and a one-line entry in whatever tracks applications.

## Completion criteria

- Every claim traces to the fact base or to source the agent read directly.
- The posting's demonstrable requirements are covered by mechanisms, not adjectives.
- The current role evidences the posting's primary technology on its own.
- No contradiction survives between the resume, the note, and the fact base.
- The rendered document has no orphaned heading, split bullet, or near-empty final page.
- No number is rounded up, and no gap is disguised.
- Everything learned is written back, including corrections and open questions.
