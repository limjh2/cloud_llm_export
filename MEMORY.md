# Shared Agent Memory

> **PUBLIC TEMPLATE — NO EXPORTS**

This is the project's whole memory. Every agent — Claude Code, Codex, local
models, whatever comes next — reads and edits this one file. It is not a harness
feature the project borrows: it is versioned with the repository, diffable in
review, and it arrives intact on any machine that clones it. It is a **permanent
part**, tracked and committed, and is never removed.

## What Belongs Here

Memory holds what is **not derivable from the project**. Three types:

- **`feedback`** — guidance the user has given on how agents should work, both
  corrections and confirmed approaches. Record the reason, not just the rule.
- **`project`** — ongoing work, goals, or constraints not derivable from the
  code or git history.
- **`reference`** — pointers to external resources: URLs, dashboards, tickets.

**Facts about the user personally** — their role, expertise, and preferences,
independent of any one project — are **not** project memory, and there is no
`user` type here. They are the same fact in every repository the user works in,
and this file is pushable. If the harness keeps its own memory, that is where
such a fact goes; if it does not, the fact is simply not written down. Do not
record one here to avoid losing it.

**Project facts go here and nowhere else.** If a harness keeps a per-project
memory store of its own — a directory keyed to this project's path, or any
equivalent — do not write a project fact into it, however convenient its default
write path is. That store is machine-local and unpushable: a fact written there
is invisible to every other agent, to every clone, and to review. A harness
store may hold **user-level memory**, or a **redirect** pointing here. It may
not hold a second copy of this project's facts.

The failure is silent, which is why it needs a rule rather than vigilance. Both
files look fine on their own; nothing reports that the project's whole memory
sits in one of them while the other is empty. If you find project facts in such
a store, move them into this file and leave a redirect behind.

**Do not store what the repository already records.** Structure, past fixes, git
history, and anything already in the canonical documents or `AGENTS.md` do not
belong in memory. If a reader could learn it by reading the project, it is not
memory.

**In this public template, no entry may be collection-derived.** This file is
tracked and pushable, so it is inside the publication boundary described in
`AGENTS.md`. Facts about providers, deliveries, filenames, hashes, or account
identifiers belong to a private instance's own `MEMORY.md`, never to template
history. Entries here concern the reusable structure and its tooling only.

## Format

One entry per fact, newest first, under `## Memories`:

```markdown
### <short-kebab-case-slug>

**Type:** feedback | project | reference
**Recorded:** YYYY-MM-DD

<the fact, in a sentence or two>

**Why:** <what makes it true — the reason behind the guidance or constraint>
**How to apply:** <what an agent should do differently because of it>
```

- `**Why:**` and `**How to apply:**` are required for `feedback` and `project`.
  A `reference` entry needs only the fact and what it is for.
- **Convert relative dates to absolute** before saving. "Last week" is unreadable
  a month later, and this file is read long after it is written.
- Link related entries with `[[slug]]`. A `[[slug]]` with no matching entry yet
  is fine — it marks something worth writing later, not an error.

## Editing Rules

- **Read before writing.** Read the whole file first; it is short by design.
- **Update, don't duplicate.** Before adding an entry, check whether one already
  covers the fact and revise that entry instead. Two near-copies of a fact are
  worse than either alone, because a later reader cannot tell which is current.
- **Delete what is wrong.** A memory found to be false or obsolete is removed,
  not annotated. This file is versioned — git holds what it used to say.
- **Trust but verify on read.** An entry reflects what was true when it was
  written. If one names a file, function, or flag, confirm it still exists
  before acting on it.

## Pruning

This is one file and it stays one file. It has no size limit, because a numbered
threshold invites the file to grow up to it.

Prune by asking what an entry has become. Memory is narrow: what is not
derivable from the project. Content that outgrows this file has usually stopped
being memory and turned into **project state** — which is what
`PROJECT_BRIEF.md`, `PROJECT_STATUS.md`, `ROADMAP.md`, and `DECISION_LOG.md`
are for. An entry that has become a decision belongs in `DECISION_LOG.md` and a
`decisions/` record; one that has become planned work belongs in `ROADMAP.md`.
Move it there and delete it here.

A file that keeps growing under that rule is a signal that facts are landing in
memory which should have landed in a canonical document.

---

## Memories

<!-- Newest first. No entries yet. -->
