---
name: screen-resume
description: Review a resume against a specific job posting from a hiring screener's seat, giving a pass or reject verdict, a requirement-by-requirement coverage check, and concrete rewrites. Use when someone asks for resume or CV feedback, wants a resume tailored to a job description or posting URL, asks whether they should apply, or returns with a revised draft for another pass.
---

# Screen a resume against a job posting

Review from the seat of the person who decides whether this resume moves forward, not from the seat of a friend being encouraging. The useful output is a verdict plus the specific edits that change it. Generic advice that would apply to any resume is worth nothing.

This skill assumes one target role. Without a posting you can only judge craft, which is the weaker exercise. Ask for the posting.

This skill reviews. The `build-resume` skill builds. They pair: build, screen, revise, screen, ship. When a finding needs the resume rewritten rather than corrected, hand it back to `build-resume` with the finding rather than rewriting the whole document from the reviewer's seat.

## Required context

- The resume, as a file to read directly rather than a summary. Only the rendered document shows layout defects.
- The job posting, in full. A URL is enough when you can recover the text.
- Any application note, cover letter, or form answers that ship alongside the resume. They are part of the package and can contradict it.

## Workflow

### 1. Recover the posting's real requirements

Fetch the posting. If the URL returns a page shell with no job text, it is client-rendered and the text lives behind an API call. Find the endpoint the page uses, request it directly, and read the structured record. Fall back to asking the user to paste the text.

The structured record usually carries hard filters the prose never states: minimum years, seniority level, salary band, timezone, region, language level, and required expertise tags. These decide more screens than the prose does. Extract them and repeat them back. The applicant has usually read only the prose.

Separate the posting into three lists.

- **Hard filters.** Numbers and named technologies. Keyword screens and tired humans match these literally.
- **Demonstrable requirements.** Capabilities that need evidence, such as queue work, query performance, or production debugging.
- **Disposition requirements.** Ownership, ambiguity, customer contact, wearing many hats. These need a story, not a keyword.

### 2. Read the resume twice

First pass, six seconds, as a screener with a stack of them. Note only what the eye lands on: title, first line of the summary, company names, any number. Write down the verdict this pass produces.

Second pass, closely, checking every claim against the posting.

### 3. Lead with the verdict

State whether you would forward this resume or reject it, in the first two sentences, before any advice. Name the one or two things that decided it. An applicant who does not know that line one sank them will fix the wrong things.

Then say which of those reasons are **framing** and which are **capability**. Framing defects cost nothing to fix and are the highest-value finding in most reviews. A candidate who writes "4+ years" against a six-year minimum while their own timeline shows five is not short of experience, they are short of arithmetic.

### 4. Build the coverage table

One row per requirement, in the posting's own words.

| They want | Resume shows | Gap |
| --- | --- | --- |

Fill the middle column with the actual bullet text or "nothing". Never write "partially covered" without quoting what covers it.

### 5. Run the defect checks

Check each one. Most are invisible on a normal read.

**Contradictions.** Compare every technical claim against every other one, including across the resume, the application note, and earlier versions you have seen. Adjacent bullets that contradict each other are common, and they are fatal. The specific one is usually true. The summary is usually the one the applicant wishes were true. Quote both and say which an interview will test.

**Claimed but not evidenced.** Any technology in a skills list that appears in no bullet. On a senior resume this is the difference between listing a tool and having shipped with it. Flag the ones the posting names.

**Evidenced but not claimed.** Any technology demonstrated in a bullet that is missing from the skills list. Keyword screens read the list. This is a free fix.

**Present everywhere except the current role.** Check the posting's primary technology against the most recent role on its own. A skill that appears in the summary, the skills list, and three older roles but in no bullet of the current job reads as something the applicant used to do. Searching the file hides this defect, because the term is present. Search the current role.

**Volume metrics.** Counts of files, migrations, repositories, or commits measure output, not judgment. They read as padding next to a real technical detail. Recommend cutting them.

**Undercutting metrics.** Small absolute numbers the applicant is proud of and a reader is not. A monthly revenue figure that converts to three digits makes a real engineering story look like a hobby. Convert it, or cut it.

**Self-reported claims.** No one can verify a percentage about the applicant's own product, and an interviewer will ask where it came from. Keep the number. Tell the applicant to have the measurement ready.

**Junior markers.** Items that signal inexperience whatever the truth is. Markup languages filed under programming languages, tutorial-scale projects, coursework sitting on a resume with five years of employment behind it.

**Layout.** Orphaned section headers at a page break, a final page under two-thirds full, bullet counts weighted toward old roles instead of recent ones, and density mismatched to the channel. A dense resume rewards a careful reader and fails a six-second skim, so name which channel it is built for.

### 6. Handle genuine gaps without inventing anything

Never add a technology the applicant has not used, and never soften a claim into something that reads as coverage. Once a resume contains one invented line, every checkable detail on it becomes a liability.

For a named technology the applicant lacks, choose one.

- Name the closest adjacent experience honestly and say what transfers and what does not.
- Volunteer the gap in the application note, which is stronger than being caught by it.
- Accept it and let the rest of the match carry the application.

When an application note is the answer, draft it. It should admit the gap in the first clause, state what carries over, state plainly what does not, and end on the strongest part of the match. Roughly this shape:

```text
I should flag one gap before you find it. I haven't used <technology>. My <adjacent stack>
is <specifics>, so <what transfers> carries over directly. What doesn't carry over is
<the honest remainder>, and I'd be learning that. Everything else on your list is what I
work in daily, including <the requirement they listed as a plus>.
```

Never round a number up in writing. If the applicant is under a stated minimum, say the true figure and put the useful follow-up next to it.

### 7. Give rewrites, not adjectives

Every finding that survives to the report needs either a replacement line or a specific instruction. "Strengthen your summary" is not a finding. Write the summary.

Mark anything that is the applicant's judgment rather than a defect as optional, and say why you would go one way.

### 8. Separate paper from preparation

Split the closing into two lists.

- **Fix before sending.** Edits to the document.
- **Prepare for the call.** Questions the resume provokes but cannot answer, such as an active side venture next to a full-time application, a metric that needs a measurement story, or a short stint.

Do not turn interview questions into resume edits. Removing the provocative line usually removes the interesting one.

### 9. Re-review a revision

When the applicant returns with a new draft, read the file again rather than reasoning from the last version. Then:

- Lead with what changed and whether it worked.
- Verify each prior finding as fixed, partially fixed, or ignored.
- Check whether a fix introduced a new inconsistency, especially between the resume and the application note.
- Shorten each round. A fifth pass that is as long as the first is manufacturing work.
- **Say when it is done.** Once the resume covers every requirement or handles one honestly, say ship it and stop. An agent that always finds something teaches the applicant to ignore it.

## Expected output

A report in this order.

```text
Verdict:            forward or reject, and the one or two reasons
What decided it:    framing defects separated from capability gaps
Coverage table:     requirement, evidence, gap
Blocking issues:    contradictions and hard misses, with rewrites
Smaller fixes:      cuts, keyword additions, layout
Fix before sending: the document edits
Prepare for call:   what the paper cannot answer
```

Keep praise specific and short. Naming the two or three bullets that are genuinely strong tells the applicant what not to lose in the next revision, which is useful. General encouragement is not.

## Completion criteria

- The verdict appears before the advice, and names what would change it.
- Every requirement in the posting appears in the coverage table, including hard filters that only exist in structured data.
- Every claimed gap quotes the resume text that creates it.
- Every finding carries a rewrite or a specific instruction.
- The review invents nothing and rounds no number up.
- The report separates interview preparation from document edits.
- On a revision pass, the report is shorter than the previous one and states plainly whether the resume is ready to send.
