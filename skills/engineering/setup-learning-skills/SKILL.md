---
name: setup-learning-skills
description: Configure where the learning workflow writes its notes by recording an Obsidian vault or a local folder. Use when setting up the learning workflow before running a study session.
---

# Setup Learning Skills

Record where `learn-stuff` writes the note that ends a study session.

This configuration is personal rather than repository-scoped. You learn concepts, not repositories, so the answer lives in your home directory and follows you between projects. Write nothing into the repository you happen to be standing in, and nothing into `docs/agents/`.

This is a prompt-driven skill, not a deterministic script. Explore, present what you found, confirm with the user, then write.

## Where the answer lives

`~/.config/agent-workflows/learning.md`, in this shape:

```markdown
# Learning destination

- **Kind:** Obsidian vault
- **Path:** /Users/you/notes/lessons

`learn-stuff` writes each session's note here as a point-in-time record.
```

Both fields are required.

`Kind` is `Obsidian vault` or `Local folder`. It tells `learn-stuff` whether wiki-links and frontmatter tags belong in a note or whether plain Markdown is the house style.

`Path` is absolute, so it resolves whatever directory the session started in. It names the folder notes land in, which may be a subfolder of a vault rather than its root.

## Process

### 1. Explore

Read before asking. Do not ask the user for anything you can find.

- `~/.config/agent-workflows/learning.md`: if it exists, this is a re-run. Read it and treat its values as the answer to confirm rather than a blank slate.
- An Obsidian vault: a directory containing an `.obsidian` folder. Look where notes usually live, such as a documents, notes, or iCloud directory. If the platform keeps its own vault registry, read it rather than searching the whole home directory.
- A folder already used for this: names like `lessons-learned`, `lessons`, `learning`, or a `learning` subfolder inside a notes directory.

### 2. Present findings and ask

Summarise what you found in a line or two, then ask exactly one question, leading with the recommended answer so the user can accept it in a word.

Pick the recommendation from what exploration found:

- **One vault found, already holding unrelated notes**: propose a `lessons` subfolder inside it, so session notes do not scatter through what is already there.
- **One vault found, empty or already dedicated to this**: propose its root. A vault named for lessons with nothing else in it does not need a subfolder, and adding one buys a level of nesting and nothing else.
- **Several vaults found**: name them and ask which.
- **No vault, but a lessons-style folder found**: propose that folder.
- **Nothing found**: propose a local folder at `~/lessons-learned`.

Offer the other kind in the same question. The two choices are an Obsidian vault or a local folder; anything else is a local folder with a different path.

If this is a re-run, ask whether to keep the recorded destination or replace it.

### 3. Write

- Create `~/.config/agent-workflows/` if it does not exist.
- Create the destination folder if it does not exist. A destination that only exists in a config file fails at the end of a session, which is the worst moment to find out.
- Write `learning.md` in the shape above. Replace the file's contents; never append, or a second run leaves two destinations and no way to tell which one wins.
- Read the file back and show the user the two values you recorded.

## Expected output

`~/.config/agent-workflows/learning.md` holding one `Kind` and one absolute `Path`, both confirmed by the user, with the destination folder existing on disk.

## Completion criteria

- The file exists and holds exactly one destination.
- `Path` is absolute and names a folder that exists.
- `Kind` is `Obsidian vault` or `Local folder`.
- Nothing was written inside the repository.
- A second run of this skill would find the file and offer to replace it rather than adding to it.
