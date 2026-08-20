# Example: learning what a database index actually does

A complete session. The concept is one most engineers can already talk about, which is exactly the kind that hides a gap.

**The concept.** Why an index makes reads faster and writes slower.

## Teach

```text
/learn-stuff why a database index makes reads faster and writes slower
```

> **Teacher.** Four steps.
>
> 1. Without an index, finding rows where `email = 'x'` means reading every row in the table and checking each one. A million rows, a million checks.
> 2. An index is a second structure, stored separately, holding just that column's values in sorted order, each paired with a pointer to the row it came from.
> 3. Sorted is the whole trick. You can jump to the middle, compare, and throw away half the remaining entries. A million rows becomes about twenty comparisons.
> 4. That second structure is real and has to stay true. Every insert, update, and delete of an indexed column writes to the index as well as the table.
>
> Three pitfalls people hit:
>
> - "Add more indexes, get more speed." Each index taxes every write to that table, forever. Indexes are a read/write trade, not free speed.
> - An index on a column with two possible values rarely helps. If half the table matches, the planner will often scan anyway, and it is right to.
> - An index on `(country, city)` serves a query filtering on `country`, or on both. It does not serve one filtering on `city` alone. The order is not decoration.

```text
switch to the intern
```

## Grill

> **Intern.** Hi. So I get that the index is sorted and the table isn't. But why does sorted mean faster? Couldn't the database just go straight to the right place in the table?

```text
It's like the index at the back of a book. You look up the word and it tells
you the page number.
```

> **Intern.** That's the same picture the Teacher used, and it's the part I still don't follow. A book index works for me because it's alphabetical, so I can flip to roughly the right place with my thumb. What is the equivalent of flipping to roughly the right place here? The database doesn't have a thumb.

The analogy was doing the work an explanation should have been doing. The Intern names what it still cannot see and asks again, narrower.

```text
Fair. It jumps to the middle entry and compares. If the value it wants sorts
before that, everything after the middle is gone, and it repeats on what's
left. Each comparison halves the search.
```

> **Intern.** Got it, that one I can follow. Next thing then. If being sorted is what makes it fast, why keep a second structure at all? Why not just keep the table itself sorted by email and search that?

```text
back to the teacher, I don't know why the table isn't just kept sorted
```

## Repair

> **Teacher.** One gap, then it's back to you.
>
> A table can be kept in physical order, and some databases do exactly that; it is usually called a clustered index. But a row has many columns and queries filter on many of them. One physical order can serve only one of those. Sorting the table by email helps email lookups and does nothing for lookups by signup date.
>
> A secondary index buys you another sort order without duplicating every column. That is the thing you cannot get by sorting the table itself, because a table has only one physical order to give.
>
> That's the gap. Explain it back to me in your own words.

```text
The table can only be sorted one way at a time, and I need fast lookups on more
than one column. An index gives me a second sort order over just the column I
care about, pointing back at the rows.
```

> **Teacher.** That's it. Back to the Intern.

```text
switch to the intern
```

## Grill, again

> **Intern.** OK. Last thing bugging me. You said every write updates the index too. So if I put an index on five columns, an insert writes six times?

```text
Roughly, yes. One table write plus one per index. That's why "add an index"
isn't free, and why you add them for queries you actually run.
```

> **Intern.** That connects to the first pitfall the Teacher listed, so I think I'm out of questions. Want me to write it up?

```text
yes
```

## The note

> **Intern.** Written to `/Users/arthur/notes/lessons/database-indexes.md`.

```markdown
---
date: 2026-08-20
tags: [databases, lesson]
---

# What a database index actually does

## What it is

A second, separate structure holding one column's values in sorted order, each
value pointing back at the row it came from. The table stays as it was.

## How it works

Sorted means you can halve the search with every comparison instead of checking
rows one at a time. A million rows takes about twenty comparisons.

The cost is that the index is a real thing that must stay true, so every insert,
update, and delete of that column writes to the index as well. Five indexes on a
table means roughly six writes per insert.

That is the whole trade: [[indexes]] buy read speed with write speed.

## What I got wrong

I explained it as "like the index at the back of a book" and stopped there. The
analogy is fine but it skips the mechanism, and I couldn't say what the database
was actually doing when I was pushed on it. The missing piece was binary search.

I also assumed you could just keep the table sorted and skip the index. You
can, but a table has only one physical order, and I usually want fast lookups on
more than one column. A secondary index is how you get a second sort order
without a second copy of every column.

## Still fuzzy

When the planner decides to ignore an index and scan anyway. I know it happens
when lots of rows match, but not where the line is or who decides.
```

The last section is the point. It names what to come back for, in the words of someone who did not understand this an hour ago.
