# Unslop

> Locally adapted from Lauren Tan’s [pstack unslop](https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md), retrieved 2026-08-19. Copyright © 2026 Lauren Tan; MIT licensed. See [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md).

## Purpose

Edit prose to remove common AI writing patterns while preserving factual accuracy, meaning, intended tone, and the author’s voice.

## When to use

Use as a final prose pass for human-facing documentation, explanations, release notes, or narrative text. Do not apply it where a prescribed style, legal wording, or direct quotation must remain unchanged.

## Required context

- The text to edit and its intended audience.
- Required facts, source attribution, style constraints, and any text that must not change.

## Workflow

1. Scan for generic phrasing, puffery, vague attribution, needless jargon, filler, excessive hedging, and formulaic conclusions.
2. Rewrite in plain, concrete language. Preserve the author’s point of view where it fits and do not invent facts or sources.
3. Prefer specific nouns and verbs over abstract metaphor, promotional language, and weak verb-plus-adverb constructions.
4. Break dense sentences when it improves comprehension. Prefer active voice when the actor is known and relevant.
5. Remove distracting habits such as overused em dashes, decorative emojis, title-case headings, repetitive bold labels, and chatbot-style closings when they do not suit the context.
6. Self-audit: identify what still reads as generated rather than written for this audience, then fix it without flattening the voice.

## Expected output

Provide the revised text and briefly identify any fact, quotation, or style constraint that prevented a change.

## Completion criteria

The text is specific, readable, and appropriate to its audience; its meaning and factual claims are preserved; and no new unsupported claims have been introduced.
