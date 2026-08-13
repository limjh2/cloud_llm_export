# Staging

> **PUBLIC TEMPLATE — NO EXPORTS**

This folder is the project's **transit lane**: where material from `inbox/` is
worked on while it is being integrated into the project, before it reaches the
places where it belongs.

It exists because integration is often a conversation rather than a single
move. When absorbing something takes three sessions and the only two states are
"in the inbox" and "done", the material sits in the inbox looking pending
indefinitely. That is how intake areas silt up — not from volume, but from
having no exit for multi-session work. This folder is that exit.

## Default Handling Rules

- `README.md` documents this folder and is not itself staged material.
- **Every file here has a named destination.** That is the exit rule. If you
  cannot say where a file is going, it does not belong here: un-triaged material
  goes back to `inbox/`, and something that turned out to be an idea rather than
  material becomes a `workshop/` idea file.
- Keep the folder small enough to read at a glance. A staging folder nobody can
  summarize has stopped being a transit lane.
- Note the destination in the file or in the project's own notes when the
  integration will span sessions, so a later session can finish it without
  reconstructing the plan.
- When the material lands in its durable home, remove it from here. Do not leave
  a copy behind "just in case" — that is what the destination and git history
  are for.

## Why This Folder Is Tracked

The project's flow folders are tracked on one rule: **git holds what it would
cost something to lose.**

| Folder | Tracked | Why |
|---|---|---|
| `inbox/` | **yes** | arriving material is usually the only copy |
| `staging/` | **yes** | partially integrated; expensive to recreate |
| `output/` | no | deliverables the user keeps, moves, or deletes |
| `workshop/` | yes | durable project thinking |
| `decisions/` | yes | durable records |

`output/` is the exception because the project produced it and can produce it
again. Arriving inbox material, partially integrated staging work, workshop
ideas, and decision records all cost something real to lose, so git keeps them.

## Relationship To The Kit

Like `workshop/`, `inbox/`, `output/`, and `decisions/`, this folder is **the
target project's own** — not trismegistus formwork. It moves to the target
project root during setup and stays when the copied `trismegistus/` kit is
assimilated and removed.

It is distinct from a `drafts/` folder, where a project keeps one: `drafts/`
holds work the project **authored and has committed to**, while `staging/` holds
material that **arrived from outside** and is being absorbed. Different origins,
different owners. A project with both should keep the line explicit.

## In the public template

This folder stays empty except for this file. Staged material is always
collection-specific, so anything else tracked here would be a publication-
boundary violation — `scripts/audit_public_tree.py` rejects it by path.
