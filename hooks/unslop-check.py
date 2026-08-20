#!/usr/bin/env python3
"""Stop-hook adapter that holds a reply to the unslop rules before it lands.

Two checks, both aimed at a failure that instructions alone did not prevent:
the rules were stated in global instructions and the closing pass still got
skipped for a whole session's worth of documents.

  A. Mechanical tells in the reply itself. Only the rules that are word or
     phrase lists, matched literally. Roughly half the skill.
  B. A document was written and the skill was never loaded. This is the check
     that catches the failure above.

The adapter carries no rules of its own, as CONTRIBUTING requires. Every term
below is verified at runtime against skills/engineering/unslop/SKILL.md, and a
term that has left the skill is reported as drift rather than enforced.

What it cannot check: rules 27 through 30 and the "adding soul" section.
Voiceless prose, dense sentences, hedging, and weak verbs propped up by adverbs
need a reader. Nothing here substitutes for running the skill.
"""

import json
import re
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent / "skills" / "engineering" / "unslop" / "SKILL.md"

# (rule number, rule name, terms, what to do instead)
# Every term is a literal lifted from the skill, checked against it at runtime.
# Single words also match their common inflections; phrases match literally.
# Terms whose innocent use is common are deliberately absent: features, surface,
# harness, primitive, vector, scaffolding, landscape. Matching those produces
# noise, and a check that cries wolf gets turned off.
RULES = [
    (7, "AI vocabulary",
     ["crucial", "delve", "enduring", "enhance", "fostering", "garner", "interplay",
      "intricate", "pivotal", "showcase", "tapestry", "testament", "underscore", "vibrant"],
     "use the plain word"),
    (8, "Fancy ways to say is",
     ["serves as", "stands as", "boasts"],
     "say is or has"),
    (13, "Em dash",
     ["\u2014", "--"],
     "end the sentence or use a comma"),
    (19, "Curly quotes",
     ["\u2018", "\u2019", "\u201c", "\u201d"],
     "use straight quotes"),
    (20, "Chatbot phrases",
     ["I hope this helps", "Let me know if", "Of course!", "Certainly!", "smoking gun"],
     "delete it"),
    (22, "Sycophancy",
     ["Great question", "You're absolutely right"],
     "respond directly"),
    (23, "Filler",
     ["in order to", "due to the fact that", "it is important to note that"],
     "cut it or use the short form"),
    (26, "Abstract metaphor nouns",
     ["substrate", "wedge", "locus", "vantage", "nexus", "bedrock", "modality",
      "paradigm", "gold-plating", "north star", "flywheel", "endgame"],
     "pick the concrete word"),
    (31, "Fancy synonyms",
     ["utilize", "leverage", "facilitate", "numerous", "in the event that"],
     "use, help, many, or if"),
    (1, "Puffery",
     ["pivotal moment", "testament to", "evolving landscape", "setting the stage",
      "indelible mark", "deeply rooted"],
     "state what happened"),
    (4, "Promotional language",
     ["nestled", "vibrant", "breathtaking", "groundbreaking", "renowned", "stunning",
      "must-visit"],
     "describe it neutrally"),
    (5, "Vague attributions",
     ["Experts believe", "Industry reports suggest", "Some critics argue"],
     "name the source or cut it"),
]

# "Not just X, but Y" is rule 9. It is a shape rather than a term, so it is the
# one pattern written by hand.
NOT_JUST = (9, "Not just X, but Y",
            re.compile(r"\bnot (?:just|only|merely)\b[^.!?\n]{0,60}?\bbut\b", re.I),
            "state the point directly")


def compile_term(term):
    """A word also matches its inflections; a phrase matches as written."""
    escaped = re.escape(term)
    if re.fullmatch(r"[A-Za-z]+", term):
        return re.compile(r"\b" + escaped + r"(?:s|es|d|ed|ing)?\b", re.I)
    if term[0].isalpha():
        return re.compile(r"\b" + escaped, re.I)
    return re.compile(escaped)


# A Bash heredoc or redirect is how documents get written when the shell is the
# tool of choice, so watching Write and Edit alone would have missed every
# document this hook exists because of.
DOC_WRITE = re.compile(r"(?:>|>>|\btee\b)\s+[\"']?\S+\.(?:md|mdx|markdown)\b")


def redact(text):
    """Drop spans where a banned term is being discussed rather than used."""
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", " ", text)
    text = re.sub(r"^\s*>.*$", " ", text, flags=re.M)   # quoting someone else
    text = re.sub(r"\]\([^)]*\)", " ", text)            # link targets
    text = re.sub(r"https?://\S+", " ", text)
    return text


def load_turn(path):
    """Return (reply text, doc was written, skill was loaded) for this session."""
    entries = []
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    def blocks(entry):
        content = entry.get("message", {}).get("content")
        return content if isinstance(content, list) else []

    last_prompt = 0
    for index, entry in enumerate(entries):
        if entry.get("type") != "user":
            continue
        content = entry.get("message", {}).get("content")
        # A tool result is also a "user" entry; a real prompt is a string or text.
        if isinstance(content, str) or any(b.get("type") == "text" for b in blocks(entry)):
            last_prompt = index

    reply = []
    for entry in entries[last_prompt:]:
        if entry.get("type") == "assistant":
            reply += [b.get("text", "") for b in blocks(entry) if b.get("type") == "text"]

    wrote_doc = False
    loaded_skill = False
    for entry in entries:
        for block in blocks(entry):
            if block.get("type") != "tool_use":
                continue
            name, params = block.get("name"), block.get("input") or {}
            if name == "Skill" and params.get("skill") == "unslop":
                loaded_skill = True
            elif name in ("Write", "Edit", "NotebookEdit"):
                if str(params.get("file_path", "")).endswith((".md", ".mdx", ".markdown")):
                    wrote_doc = True
            elif name == "Bash" and DOC_WRITE.search(str(params.get("command", ""))):
                wrote_doc = True

    return "\n".join(reply), wrote_doc, loaded_skill


def drifted_terms(skill_text):
    """Terms this adapter enforces that the skill no longer lists.

    The adapter must add no rules of its own, so a term that has left the skill
    is reported rather than quietly enforced.
    """
    lowered = skill_text.lower()
    missing = [
        term
        for _, _, terms, _ in RULES
        for term in terms
        if any(character.isalpha() for character in term) and term.lower() not in lowered
    ]
    return sorted(set(missing))


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    transcript = payload.get("transcript_path")
    if not transcript or not Path(transcript).exists():
        return 0

    try:
        skill_text = SKILL.read_text(encoding="utf-8")
    except OSError:
        # Without the skill there is no authority to enforce, so say nothing.
        return 0

    try:
        reply, wrote_doc, loaded_skill = load_turn(transcript)
    except Exception:
        return 0

    findings = []
    prose = redact(reply)
    for number, name, terms, fix in RULES:
        for term in terms:
            hit = compile_term(term).search(prose)
            if hit:
                findings.append(f"  Rule {number} ({name}): \"{hit.group(0).strip()}\" -> {fix}")

    number, name, pattern, fix = NOT_JUST
    hit = pattern.search(prose)
    if hit:
        findings.append(f"  Rule {number} ({name}): \"{hit.group(0).strip()}\" -> {fix}")

    if wrote_doc and not loaded_skill:
        findings.append(
            "  Closing pass: this session wrote a document and never loaded the "
            "unslop skill. The short list does not carry rules 27 to 30 or the "
            "\"adding soul\" section. Run the skill over what you wrote."
        )

    if not findings:
        return 0

    drift = drifted_terms(skill_text)
    note = ""
    if drift:
        note = ("\n\nThis hook is enforcing terms the skill no longer lists: "
                + ", ".join(drift) + ". Fix the hook to match the skill.")

    # A second block would loop, so once the turn has already been stopped,
    # report and let it through.
    if payload.get("stop_hook_active"):
        print(json.dumps({
            "systemMessage": "unslop: tells remain in this reply.\n" + "\n".join(findings)
        }))
        return 0

    print(json.dumps({
        "decision": "block",
        "reason": ("The unslop rules are not met. Rewrite the reply, then finish.\n\n"
                   + "\n".join(findings)
                   + "\n\nThese are the mechanical rules only. Rules 27 to 30 "
                     "(plain speech, dense sentences, active voice, adverbs) and "
                     "the \"adding soul\" section still need your own read."
                   + note),
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
