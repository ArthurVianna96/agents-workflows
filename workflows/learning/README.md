# Learning workflow

Learn a concept, then find out whether you actually understand it.

```text
Teach → (you switch) → Grill → (you switch back) → Repair → Grill → Note
```

The whole loop lives in one skill, [learn-stuff](../../skills/engineering/learn-stuff/SKILL.md). You move between its two roles yourself, in either direction, at any point.

## The failure this catches

You read a clean explanation, feel that it landed, and discover later that what landed was the explanation rather than the understanding. Recognizing vocabulary is not understanding an idea, and nothing inside a well-written explanation tells the two apart.

So this loop makes you do the explaining. **The Teacher is the fallback, not the shortcut.** If the Teacher does the explaining, you stay passive and still feel productive, which is the same failure wearing a different hat.

## The two roles

**Teacher**, a senior engineer. Explains in steps, names the pitfalls, and stops when you say so. It never tells you how well you understand something; that is the Intern's job to test, not the Teacher's to predict.

In repair mode it answers one named gap and stops, then hands the explaining straight back to you. A repair that turns into a second lecture puts you back in the passenger seat.

**Intern**, an entry-level engineer. Asks beginner questions one at a time, following its own confusion. When an answer does not land it says so and asks again, narrower.

The Intern never supplies the answer it is asking for. No hints, no multiple choice, no finishing your sentence. The moment it offers an answer you can pass by agreeing with it, and the explanation this session exists to extract never gets made.

It manages that by judging whether an answer made sense **to it**, never whether the answer is **correct**. It has no expertise to check correctness against, and reaching for some would mean holding the answer. The cost is real: a clear and wrong explanation gets past it. What it catches is an explanation that is vague, circular, or borrowed.

## Switching is yours

Say "switch to the intern" when you have a first mental model, and "back to the teacher, I'm stuck on X" when you hit a wall. The loop follows your understanding rather than a fixed script, and the session never decides you are ready.

The Intern running out of questions is the pass mark.

## The note

The Intern writes it, in its own beginner language. Not the Teacher's words, and not the expert phrasing you have just proven you can produce. The note is worth something precisely because it sounds like someone who recently did not understand this.

It covers what the thing is, how it works, what you got wrong on the way and what fixed it, and what is still fuzzy. That last part is the most useful line in the note when you come back to it.

A note is a **point-in-time record**, so [write-docs](../../skills/engineering/write-docs/SKILL.md) governs it. It records what you understood on that day and is left as written. When your understanding deepens, run the loop again and write a new note; do not revise the old one into agreement, or you lose the evidence of what changed.

## Set it up

Once, run [setup-learning-skills](../../skills/engineering/setup-learning-skills/SKILL.md). It records whether your notes go to an Obsidian vault or a local folder, and where. The configuration is personal rather than repository-scoped, so you answer once and it follows you between projects.

The skills need to be discoverable first; the [root README](../../README.md) covers that once for every workflow.

## Run it

Name the concept and start. Switch when you are ready, get repaired when you are stuck, and stop when the Intern runs out of questions.

## See it work

[**Learning what a database index actually does**](examples/learning-database-indexes.md) is a complete session: the Teacher's first explanation, an analogy the Intern refuses, one repair, and the note that came out the other end.
