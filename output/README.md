# Output

> **PUBLIC TEMPLATE — NO EXPORTS**

This folder is the project output space: the default place for agents to write
things that are about the project but are not part of the project itself. It
keeps such deliverables from being scattered across the project root or wedged
into canonical documents where they do not belong. Collection-derived output
must never enter this public template.

Most of what lands here is addressed *to the user*; some of it — a session
handoff above all — is addressed to an agent. See "Who An Output File Is
Addressed To" below.

A deliverable is not only prose. Two forms belong here:

- **Written answers** — reports, analyses, explanations, comparisons, answers to
  questions.
- **Reusable artifacts** — a tool, script, or other generic thing the work
  produced that is meant to be used elsewhere. The test is **"from this project
  but not of this project."**

## Default Handling Rules

- `README.md` documents this folder and is not itself a deliverable.
- One dated entry per deliverable, so entries sort by date:
  `YYYY-MM-DD-topic.md` for a single file, `YYYY-MM-DD-topic/` for a package
  (for example an engine plus a generic README, a template config, and example
  inputs).
- Output files are point-in-time artifacts. They may go stale, and no one is
  obliged to keep them current; a reader wanting the present state should look
  at the canonical project documents.
- Anything durable a deliverable establishes (a decision, a finding the
  project acts on) must also be recorded in the canonical documents. An output
  file must never be the only home of project-critical knowledge.
- Unlike `inbox/`, nothing here is pending work: agents do not need to check,
  process, or tidy this folder. The user reads, keeps, moves, or deletes its
  contents freely.
- Two kinds of file live here by who they are addressed to — the user, or an
  agent — and the folder leans toward the user. Session handoffs are the
  agent-addressed kind; see "Who An Output File Is Addressed To" below.

## `scripts/` Versus `output/`

`scripts/` — or whatever the project's scripts home is called — holds the
project's **own machinery**: things it runs on itself. `output/` holds artifacts
meant to **travel** to another project or to the user.

An artifact can be both, and then it exists twice on purpose:

- Keep the **wired** instance in `scripts/`, with the project's real config and
  data.
- Put a **clean, generic** copy in `output/`, with all project specifics moved
  out into config or input files.
- The `scripts/` copy must **never depend on `output/` at runtime.** Output is
  user-controlled — they may move, keep, or delete it freely — so a runtime
  dependency on it is a broken project waiting to happen.

Designing the artifact generic from the start, with project specifics in
config or data, makes the `output/` export a straight copy rather than a
rewrite.

## This Folder Is Not Tracked, So It Is A Transit Lane

`output/` is gitignored except for this `README.md` and the `.gitignore` itself.
Deliverables belong to the user, not to the project's history. Tracking the
README is also what keeps the folder present in a fresh clone, since git cannot
track an empty directory.

This differs from `inbox/` deliberately. An inbox file arrived from outside and
is often the only copy, so the inbox is tracked. An output deliverable was
produced by the project and can be produced again, so output remains a
user-controlled transit lane. The tracking rule is **git holds what it would
cost something to lose**, not that every flow folder has the same treatment.

That makes `output/` a lane rather than storage. **Anything that must not be
lost has to leave it:**

- Promote a recurring or valuable category to its own tracked top-level home
  (see "Spinning Off A Category" below).
- Or move the deliverable where it is actually going — for a reusable tool, that
  is the project meant to use it, whose `inbox/` is a perfectly good delivery
  address.
- When the project also runs the exported tool, the wired `scripts/` copy is
  already tracked, so the export is never the only copy.

## Spinning Off A Category

When one kind of output keeps recurring and becomes a real fixture of the
project — research reports, audit summaries, comparison studies, exported tools
— promote that category to its own named top-level home (for example `reports/`
or `exports/`), record the decision in `DECISION_LOG.md`, and note the new home
here. A promoted home is tracked, which is also how a deliverable stops being
transient. `output/` is the general-purpose space that remains for everything
that has not earned its own folder.

## Relationship To The Kit

Like `workshop/`, `inbox/`, `staging/`, and `decisions/`, this folder is **the
target project's own** — not trismegistus formwork. It moves to the target
project root during setup and stays when the copied `trismegistus/` kit is
assimilated and removed. It is where the project speaks back.

## Who An Output File Is Addressed To

Everything here is readable. Agents may list, read, and cite this folder when
asked. What varies is **who the file was written for**:

| | Addressed to the user | Addressed to an agent |
|---|---|---|
| **Typical file** | a report, analysis, comparison, or exported tool | a session handoff |
| **Naming** | `YYYY-MM-DD-topic.md` or `YYYY-MM-DD-topic/` | `YYYY-MM-DDTHHMMSS±HHMM-session-handoff.md` |
| **When to act on it** | never as current instructions; it is a point-in-time artifact | only when the user names or pastes it |

`output/` **leans toward the first kind** — that is what it is for, and the
agent-addressed files are the exception rather than the pattern. An `inbox/`
message is the reverse: almost always addressed to an agent, because an inbox is
processed by the agent working in the project that owns it. That holds whether a
project writes to its own inbox or to another project's.

Neither kind is a source of truth, and finding one is not the user handing it to
you. A session handoff carries a guard header saying so; it also says the file is
not stale merely because nobody read it. See `HANDOFF_PROTOCOL.md`.
