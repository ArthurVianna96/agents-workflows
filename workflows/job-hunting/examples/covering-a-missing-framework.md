# Example: covering a missing framework

The short case. The posting names a framework the applicant has never used, and the resume
cannot fix that. What happens instead takes one exchange.

**The posting.** *Full-Stack Engineer — Node.js, NestJS, Prisma & React.* Everything on the
list is the applicant's daily work except NestJS. Their Node services are Fastify.

## The decision

```text
/build-resume — NestJS is in the title and I've never touched it
```

> Three ways to handle a named technology you do not have. Adding it to the skills list is not
> one of them.
>
> **Name the adjacent experience and be precise about the seam.** Fastify and NestJS are both
> TypeScript frameworks over the same HTTP layer, and Prisma and PostgreSQL sit identically
> under either. The runtime, the ORM, the migrations, and the REST design all carry over. What
> does not carry over is Nest's decorator and dependency-injection model, which is a genuinely
> different way to structure an application.
>
> **Volunteer it in the application note.** Stronger than being caught by it, and it costs one
> short paragraph.
>
> **Or accept it** and let the rest of the match carry the application. Everything else on their
> list you have.
>
> I would do the second, because their form has a message field and because the note lets you
> control the framing. Either way the resume says nothing about NestJS.

```text
do that
```

> Written to `application-note.md`:
>
> > I should flag one gap before you find it: I haven't used NestJS. My Node services are
> > Fastify with Prisma, in TypeScript, and my PostgreSQL work is on the Python side with
> > SQLAlchemy and Alembic, so the runtime, the ORM, the migrations and the REST design all
> > carry over. What doesn't carry over is Nest's decorator and dependency-injection structure,
> > and I'd be learning that. Everything else on your list is what I work in daily, including
> > the React Native side you list as a plus.
>
> The gap is in the first clause, what transfers is next, what does not is stated plainly, and
> it ends on the strongest part of the match.

## Why not soften it instead

The tempting alternative is a resume line like "experienced with Node frameworks including
Fastify and similar," which matches the keyword without technically claiming anything. It does
not survive one follow-up question, and the applicant now looks evasive about a gap that was
never disqualifying.

The note version has the opposite property: it spends the gap deliberately and buys credibility
for every other claim on the page. A candidate who volunteers what they do not know is easier
to believe about what they do.

## The check that goes with it

```text
/screen-resume
```

> NestJS appears nowhere in the resume, which is correct. Two related findings.
>
> **Cypress is in your skills line and in no bullet.** It is now the only item there in that
> position, since your end-to-end specs are a different tool. Keep it only if you would be
> comfortable being interviewed on it. Nobody misses a tool you did not list; everybody notices
> one you cannot talk about.
>
> **Two technologies your bullets demonstrate are missing from the skills line.** That is a free
> keyword match you are throwing away. Add them.

The same discipline in both directions: a skills list should be the index of the evidence, not
a wish list next to it.
