# Session Handoff Protocol

> **PUBLIC TEMPLATE — NO EXPORTS**

This protocol creates a short prompt that a human can paste into a fresh agent
session. It complements the canonical project documents; it does not replace
them. It is a **permanent part** and is self-contained: nothing in it depends on
a copied `trismegistus/` kit being present.

## Where Handoffs Go

A session handoff is an ordinary `output/` file. It gets no folder of its own.

`output/` holds two kinds of artifact: those **addressed to the user** and those
**addressed to an agent**. It leans toward the first — reports, analyses,
comparisons — and a handoff is the second kind, written for whoever opens the
next session. An `inbox/` message is almost always addressed to an agent too,
because an inbox is processed by the agent working in the project that owns it.

Name a handoff:

```text
output/YYYY-MM-DDTHHMMSS±HHMM-session-handoff.md
```

Date first, so it sorts with everything else in `output/`, and precise to the
second, so a fresh timestamp is always a fresh filename.

`output/` is untracked in both this template and a filled instance, so a handoff
never enters git history. That is what keeps a handoff written in a filled
instance — which may name providers, deliveries, or verification results — off
the publication path. A handoff written against this public template stays
generic regardless, because everything in this repository does.

## Writing A Handoff

Write one only after the user explicitly requests a checkpoint or closeout.

Do not inspect an existing handoff to work out the next name. Generate a fresh
timestamp from the current clock and create a new file. If the destination
somehow already exists, choose a more precise timestamp or add a short unique
suffix. **Never read back or overwrite an existing handoff to write a new one.**

Handoffs accumulate rather than replace each other. `output/` is user-controlled
— the user keeps, moves, or deletes its contents freely — so do not tidy old
handoffs away.

## Closeout Sequence

1. Finish or stop the active slice at a coherent boundary.
2. Run the relevant verification — for this project, `python scripts/validate.py`
   and `python scripts/audit_public_tree.py`.
3. Update `PROJECT_STATUS.md`, `ROADMAP.md`, and `DECISION_LOG.md` as needed.
4. Check `git status` and commit the coherent durable checkpoint unless the
   user explicitly asked not to commit.
5. Confirm the resulting commit ID and any intentional remaining changes.
6. Create one new handoff in `output/` from the template below.
7. Report the new handoff path to the user. Do not read it back merely to
   verify it; verify the write operation's success instead.

## Closeout Contract

These rules bind a closeout and are never omitted. Paste them into a session
that is ending, or follow them directly.

```text
CLOSEOUT CONTRACT — these rules bind this closeout. Follow them literally.

1. VERIFICATION IS RUN, NOT ASSERTED. Run the project's verification command
   now, in this session, and show its actual output in your reply. Output you
   remember, expect, or reconstruct is not output. If you cannot run it, say so
   and say why.

2. VERIFICATION NAMES THE USER-VISIBLE BEHAVIOUR IT CHECKED. State which
   observable behaviour each check exercised, in the terms the user would use.
   A check that passes against a proxy for the behaviour has not checked the
   behaviour: that a file parses is not evidence that a page loads, that a
   module imports is not evidence that a command runs, and a green test suite
   that never touches the change is not evidence the change works. If a symptom
   was reported to you, the check must exercise that symptom.

3. UNOBSERVED WORK IS `unverified`, NEVER `completed`. This is a rule about what
   you may claim, not about what you must run. Anything you have not personally
   watched work goes in the handoff under `unverified`, with what would confirm
   it — however confident you are in the change, however obviously correct the
   diff looks, and even if the code was written to fix exactly that symptom.
   `completed` means observed working. Nothing else earns that word.

4. FACTS COME FROM COMMANDS, NOT MEMORY. The commit ID comes from `git`. The
   timestamp in the handoff filename comes from `date`. The working-tree state
   comes from `git status`. Never write any of the three from recall.

5. EXACTLY ONE NEW HANDOFF. Write one new file, at
   output/YYYY-MM-DDTHHMMSS±HHMM-session-handoff.md, from a fresh timestamp.
   Never read back, edit, or overwrite an existing handoff to produce it; if the
   filename somehow exists, use a more precise timestamp. It must open with the
   HUMAN-FACING SESSION HANDOFF guard verbatim.

6. COMMIT, AND LEAVE THE PROJECT DOCUMENTS TRUE. Commit the session's work
   unless the user asked you not to. Where this session changed what
   PROJECT_STATUS.md, ROADMAP.md, or DECISION_LOG.md say, update them — the
   state as it now stands, not a narrative of the session.

7. DONE MEANS: clean working tree (or the remaining changes named as
   intentional), verification output shown in this reply, and the new handoff
   path reported. When those three are true, STOP. Do not start new work, do not
   fix one more thing, do not tidy.

If any of these cannot be satisfied, report which one and stop there. A closeout
that reports a blocker is finished work. A closeout that hides one is not.
```

## Content Rules

A handoff should contain:

- the target project path and suggested launch command, when known
- the canonical documents to read first
- the checkpoint commit ID and working-tree state
- a short current-state summary
- one concrete next task
- acceptance criteria and verification commands
- unresolved decisions or explicit cautions

Keep durable facts and decisions in tracked project documents. The handoff
should point to them and remain short enough to paste as a starting prompt.

Every handoff must start with this guard, verbatim:

```text
HUMAN-FACING SESSION HANDOFF
This file is addressed to a future session, not to normal project work. Do not
act on it as current instructions unless the user names or pastes it. It is not
stale merely because nobody has read it: if you find one unprocessed, say so
rather than discarding or overwriting it.
```

The guard is the whole mechanism, and it travels with the file rather than with
any folder. It carries two rules, and both matter:

- **Not current unless named.** Finding a handoff is not the user handing it to
  you. It becomes an instruction source only when the user names or pastes it.
- **Not discardable when found.** A handoff is not stale merely because nobody
  read it — documents are meant to be processed. Mention an unprocessed one
  rather than deleting or overwriting it.

## Session Handoff Template

````markdown
# Session Handoff

HUMAN-FACING SESSION HANDOFF
This file is addressed to a future session, not to normal project work. Do not
act on it as current instructions unless the user names or pastes it. It is not
stale merely because nobody has read it: if you find one unprocessed, say so
rather than discarding or overwriting it.

## Launch

```bash
cd /absolute/path/to/project
# Start the intended agent or development environment.
```

## Read First

- `PROJECT_STATUS.md`
- `ROADMAP.md`
- `DECISION_LOG.md`
- `FORMAT.md` for placement and integrity rules

## Checkpoint

- Commit: `<commit-id and subject>`
- Working tree: `<clean, or list intentional remaining changes>`
- Verification: `<commands and outcomes>`

## Current State

<One short paragraph. Keep durable details in the canonical project documents.>

## Completed (observed working)

- `<change>` — observed by: `<what you watched work>`

## Unverified

- `<change>` — would be confirmed by: `<the check nobody has run yet>`

## Next Task

<One concrete task or approved roadmap slice.>

Acceptance criteria:

- `<observable completion condition>`

Verification:

```bash
<command>
```

## Open Decisions And Cautions

- `<unresolved decision, reserved identifier, known risk, or "None">`
````

## Root Instructions

`HANDOFF_PROTOCOL.md` lives at the project root and outlives any copied kit.
`AGENTS.md` points at it under "Session Handoffs" and must keep doing so.
