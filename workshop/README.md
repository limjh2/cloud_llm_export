# The Athanor — Idea Workshop

> **PUBLIC TEMPLATE — NO EXPORTS**

This is the project's idea workshop — the athanor: a tracked holding pen for
ideas that carry **no commitment**. An idea here might become a roadmap slice,
might inspire something else that does, or might go nowhere. All three are fine.
Putting something here promises nothing — it is the stage *before* a
`ROADMAP.md` slice, where a thought can sit without being scheduled.

```text
workshop  ->  ROADMAP.md slice  ->  built
(maybe)       (committed to)

... or it stays, quietly shapes something else, or dies. No obligation.
```

## Add an idea

1. Copy `_TEMPLATE.md` to a new `kebab-case-name.md` in this folder.
2. Write a few plain lines — enough that future-you remembers the thought.

That is the whole ritual. For a fleeting half-thought not worth a file, use the
scratch lane below until it earns one.

## Connections, not status

Ideas are not graded on a maturity ladder; there is no status stamp to maintain.
Record how ideas **relate** instead, with `[[other-idea]]` links in an idea's
`Related` section.

- An idea with no links is an **isolate** ("raw") — an observation, not a label.
- Never destructively **merge** two ideas. Keep both and record the relationship;
  the "we saw this twice, from two angles" record is often the valuable part.
- "Supersedes" is just the strongest link — an annotated edge, not a deletion.

Example of the form:

```md
# Offline-first sync

Let the project work fully offline and reconcile on reconnect, instead of
assuming a live server.

## Related

- [[conflict-resolution-rules]] — depends on this being decided first
```

The index of ideas is **emergent** from the links. Read them; do not
hand-maintain a master list.

## The scratch lane

`scratch/` is gitignored — drop half-thoughts there that are too raw to be even
an isolate. Untracked is not off-limits — it is **readable**, so you and any
assisting agent can work in it. Promote a scratch note by giving it a real idea
file here.

## Leaving the workshop

- **Promotion** — turn the idea into a `ROADMAP.md` slice when you commit to
  building it. Keep the idea file, or move it somewhere durable; do not delete
  it. The slice records what is being built, while the idea file records the
  thinking that got there — and every `[[link]]` pointing at it depends on the
  file still existing.
- **Death** — leave the file with a short note on why it stalled. Deleting
  outright loses the "why we didn't"; prefer parking.

**When an idea leaves, its incoming links stay — annotate them.** A `[[link]]`
pointing at an idea that has been promoted or moved is not a broken reference to
repair by deletion: the relationship it records really happened, and since the
index is emergent from the links, that edge is the only place it is written
down. Say where the idea went, in the same annotated-edge form used above:

```markdown
- [[offline-first-sync]] — promoted to R014; the conflict rules below are what
  that slice deferred
```

Sweeping the other way is the cheap check: after moving an idea out, grep the
workshop for its name and annotate whatever points at it.

## Relationship to the kit

This workshop is **the target project's own** — not trismegistus formwork. Setup
moves it to the project root, and it is a **permanent part**: as the copied
`trismegistus/` kit atrophies part by part, the workshop is never one of the
parts that goes. Make sure any idea worth acting on has been promoted to
`ROADMAP.md` or recorded in the project's durable notes; the rest can keep
sitting here with no obligation.

## In the public template

Ideas here concern the reusable structure, the format rules, and the
verification tooling. An idea about a specific holding belongs to the private
instance that holds it, never to template history.
