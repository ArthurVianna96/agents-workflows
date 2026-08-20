# Example: tailoring for a Node and Prisma role

A complete run. The applicant is a full-stack engineer with two employers behind them and a
maintained fact base. The posting asks for TypeScript on both ends, React on web and mobile,
PostgreSQL and Prisma "including schema design, migrations, and query performance", webhooks,
and someone who "takes testing and production debugging seriously".

## Build

```text
/build-resume https://example.com/jobs/1504 — fact base in ~/job-hunt/profile,
my repos are ~/code/main-app and ~/code/second-product
```

> Fetched the posting. The page returned an empty body, so it is client-rendered; I pulled the
> DOM with a headless browser instead. Three hard filters the prose does not mention: **six
> years minimum**, remote restricted to LatAm, and a stated range of $5,000–7,100/month.
>
> You are at four years eleven months. I am not going to round that up, and I would not raise
> the number unprompted. Everything else is worth pursuing.
>
> Requirements split into the three lists, written to `posting.md`. Now mining the repos rather
> than asking you what you remember.

The agent reads rather than interviews. Four requirements go looking for four kinds of file.

> Four findings, all verified as your commits with `git log`:
>
> **Query performance.** `ix_case_lease_until` indexes `lease_until` with
> `postgresql_where=status IN ('pending','processing')`. A partial index on a work queue, so
> the poller's index stays sized to in-flight rows instead of growing with every finished case.
> The commit that added it reads *"fix(worker): ownership by lease, end of double processing"*,
> so it came out of a real bug: two workers claiming the same case.
>
> **Webhooks.** The billing route captures the raw body through a pre-parsing hook, because
> signature verification needs the unparsed bytes, then dispatches six event types with
> idempotency keys on the writes behind them.
>
> **Testing.** Three tiers: service tests, route tests, and end-to-end specs.
>
> **Production debugging.** A monitor counting messages that ended with a running tool and
> never reached a terminal state, shipping through a log pipeline to a dashboard alert. The
> commit before it added a keepalive. That pair is a whole incident: symptom, diagnosis, fix,
> and a guard so it cannot come back silently.
>
> All four are in the bullet bank now with file paths. Two questions the code cannot answer.

```text
The app is a personal finance app, insights feed plus an AI chat over the
user's own data. I built the chat UI and the gateway between the model and
the financial data. I did not train the model.
```

> Recorded, including the boundary. The resume will say you built the interface and the
> gateway, and will not say you trained anything. That line erodes across revisions unless
> something on file holds it.

## Screen

```text
/screen-resume the package in applications/2026-08-20-example/
```

> **Reject, on one issue, and it is on the page twice.**
>
> Bullet 1 says "Prisma ORM over PostgreSQL and Redis". Bullet 2 says "19 Prisma migrations on
> MySQL, 29 Alembic revisions on PostgreSQL". Those cannot both be true. The specific one
> usually is, which would make the summary line and the application note wrong as well, because
> the note repeats the claim word for word.
>
> Everything else is close to ready. The query-performance bullet is the most convincing thing
> on the page.

The build introduced this. The source line read "Node services and a Python service, over
PostgreSQL, MySQL, and Redis", with the database list trailing both services, and tailoring
resolved the ambiguity toward the posting.

```text
check it
```

> Both schema files declare `provider = "mysql"` and there is no PostgreSQL connection string
> anywhere in that repo. The second repo is `postgresql+asyncpg`. **Prisma is on MySQL.
> PostgreSQL is the Python side.** The review is right.
>
> Corrected in five places: the summary, the stack bullet, the application note, the coverage
> table, and the master resume, which is where it came from. I also pinned each ORM to its own
> engine in the master so the next tailoring pass cannot resolve it differently.

## Revise

```text
/screen-resume again
```

> The contradiction is gone and consistent in all three places. One requirement is still
> uncovered: the posting says "takes testing and production debugging seriously" and your
> skills line answers with keywords. Across eleven bullets there is no testing story. It is the
> only line item where you assert instead of demonstrate, and that contrast is louder now that
> the rest is concrete.

The evidence was already in the bullet bank from stage 2. It had not been selected.

> Added, and traded the least relevant bullet on the page to pay for it. Leading with the
> incident made testing look like one bug's fallout, so the bullet leads with the practice and
> uses the incident as proof:
>
> *Test in three tiers across the two products: service tests behind auth, billing and storage,
> route tests, and end-to-end specs, with the failure paths covered too. Debugging goes the same
> way. A communication-error toast traced to streams dropping mid-turn without a keepalive,
> fixed, then guarded by a monitor that alerts if it returns.*
>
> Rendered and checked: two pages, no orphaned heading, no split bullet.

```text
/screen-resume
```

> Every named requirement now has a checkable claim behind it. **Send it.** You are still a year
> under the stated minimum, and you cannot write your way past that. But minimums are a proxy
> for whether someone has owned production systems end to end, and this answers that directly
> enough that a decent hiring manager will look past the proxy.

## Write back

Four repository findings, one product description, one attribution boundary, one corrected
database claim, and the note that the master's ambiguity caused it. All dated, all in the
bullet bank.

The next posting asking about query performance costs one read of that file.
