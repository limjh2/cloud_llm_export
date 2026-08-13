# Cloud LLM Export Inbox

This folder is the project intake area: a **drop point** for new, unsorted, or
not-yet-processed material that should be visible to future agent sessions but
has not yet been classified into the project's normal structure.

It is also a **cross-project mailbox**. An agent working in one project can
write into another project's `inbox/`, which is how material moves between
projects without anyone carrying it by hand.

**No work happens in the inbox.** It is a drop point, not a workspace. Material
that needs working on moves to `staging/` first.

## Default Handling Rules

- `README.md` documents the inbox and is not itself pending intake.
- Everything else in this folder should be considered unprocessed.
- **Move, don't work in place.** Material that needs more than a single move —
  anything requiring a conversation, a decision, or several sessions — goes to
  `staging/`, which is the folder for integration in progress.
- Preserve each provider delivery intact until its provider and delivery date
  are established. Move processed files to their correct durable location
  instead of leaving duplicate copies here.
- **Sweep toward empty.** An inbox with a standing population is not an inbox.
  Keep it small enough that its contents are actionable at a glance.

## This Folder Is Tracked

`inbox/` is tracked, including its contents in a filled local instance. Two
reasons, and the second is the one that is easy to lose:

1. **Material here is usually the only copy.** It arrived from outside and the
   project cannot reproduce it. Git is the backup for the window between "a
   file was dropped in" and "someone processed it" — exactly when the file is
   irreplaceable.
2. **Tracking is what makes a drop visible.** An unprocessed item appears in
   `git status` as `??`. That is the flag on the mailbox: a standing cue that
   tells a session intake is waiting without depending on the session
   remembering to look.

This does not weaken "sweep toward empty": a tracked inbox nags until it is
swept, which applies more pressure to clear it than an ignored one does.

`output/` remains untracked, and the asymmetry is deliberate. Inbox material
arrived from outside and is usually the only copy; an output deliverable was
produced by the project and can be produced again.

## Relationship To The Kit

Like `workshop/`, `staging/`, `output/`, and `decisions/`, this inbox is **the
target project's own** — not trismegistus formwork. It moves to the target
project root during setup and stays when the copied `trismegistus/` kit is
assimilated and removed.

The flow runs in a line rather than a circle:

```text
inbox/  →  staging/  →  the project's own documents
                     ↘  output/     what the project says back to you
                     ↘  workshop/   what it is not doing yet
                     ↘  decisions/  what it settled, and why
```

The inbox is intake for *material*; `workshop/` is a holding pen for *ideas*. A
thought dropped into the inbox can be processed into a `workshop/` idea file.

## In the public template

This public repository contains no pending intake. Real provider deliveries and
collection-derived material belong only in a separate private instance and
must never enter template history.
