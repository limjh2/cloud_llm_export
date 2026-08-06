# trismegistus Provenance

trismegistus-Version: 5.1.1

- **Role:** Public, content-free reference-collection template
- **Origin archetype:** `reference_collection_foundation`, adapted for immutable
  directory-valued export sets
- **Scaffolded:** not recorded (the original stamp carried no date, and the
  template's own audit rejects the dates involved as private-instance tokens)
- **Last upgraded:** 2026-08-06
- **Source kit:** trismegistus deployable kit

## How To Read This

This project was started from the trismegistus kit. The copied `trismegistus/`
guidance folder atrophies part by part as the project takes over each part's
function, and may already be gone entirely. This stamp records the provenance,
the conventions the project continues to follow, and — in the Atrophy Log below
— which parts of the kit have been removed and when.

The kit is gitignored in this repository and never enters template history, so
its removal leaves no diff. The Atrophy Log is the only record of it.

## Conventions This Project Follows

- **Project memory:** canonical `PROJECT_BRIEF.md`, `PROJECT_STATUS.md`,
  `ROADMAP.md`, and `DECISION_LOG.md` are kept current, alongside `FORMAT.md`
  for the collection format.
- **Slices:** work advances one signed-off `R###` roadmap slice at a time; a
  slice is done only when acceptance criteria are met, verification passes,
  durable docs are updated, and a coherent commit exists.
- **Two-step slices:** capturing an ask as a `ROADMAP.md` entry (or a
  `workshop/` idea) and writing that entry up as a buildable slice are separate
  steps; the write-up happens only on an explicit ask. A written-up slice
  carries every build-time decision explicitly, because the model that executes
  it may be weaker or cheaper than the one that planned it.
- **Hardening:** a standing `H###` hardening-pass series, re-run after batches
  of change; never retired.
- **Inbox:** `inbox/` at the project root is the intake area; every file there
  except `README.md` is pending intake, handled per `inbox/README.md`. It is a
  drop point, not a workspace, and is untracked except its `README.md` and
  `.gitignore`.
- **Staging:** `staging/` at the project root is the tracked transit lane where
  inbox material is worked on while it is being integrated; every file in it has
  a named destination, and material leaves once integration finishes.
- **Output:** `output/` at the project root is where agents write deliverables
  addressed to the user — written answers and reusable artifacts ("from this
  project but not of this project") — one dated entry each. Output is not
  project memory, is untracked except its `README.md` and `.gitignore`, and
  anything worth keeping is promoted to its own tracked top-level home.
- **Decisions:** `decisions/` at the project root holds durable decision records
  and the evidence behind them. A filed record is finished: never edited to
  reflect a later decision, and never a replacement for the `DECISION_LOG.md`
  line.
- **Flow-folder tracking:** git holds what a session invested work in, not what
  is passing through — `staging/`, `workshop/`, and `decisions/` are tracked;
  `inbox/` and `output/` are not.
- **Shared agent memory:** `MEMORY.md` at the project root is the one memory
  every agent reads and edits — tracked, committed, and permanent like this
  stamp. It carries its own format rules, holds only what is not derivable from
  the project, and excludes facts about the user personally, which are the same
  in every repository and do not belong in a pushable file.
- **Handoffs:** a session handoff is an ordinary `output/` file, named
  `YYYY-MM-DDTHHMMSS±HHMM-session-handoff.md` and written only on an explicit
  request; it follows the root `HANDOFF_PROTOCOL.md`, which is permanent like
  this stamp and self-contained.
- **Git:** local-first; coherent commits after verified slices. The default is
  solo-main — commit to main, with no feature branches or pull requests — but
  pushing is subordinate to the publication boundary in `AGENTS.md`, which is
  stricter: a filled instance has no remote at all, and this template is pushed
  only after `scripts/validate.py` and `scripts/audit_public_tree.py` pass.
- **Publication boundary:** public template and private collection histories are
  permanently separate. `python scripts/audit_public_tree.py` blocks
  collection-derived public state by exact path across all reachable history;
  `python scripts/validate.py` reconciles a filled local instance.

Software-only conventions the kit carries — localization and input-method
support, desktop launchers, and GUI behaviour and verification — do not apply to
this non-code source collection. See `DECISION_LOG.md` D004.

## Atrophy Log

Parts of the copied `trismegistus/` folder removed as this project took over
their function. Newest first.

- [2026-08-06] Removed the re-supplied 5.1.1 kit in full, with owner approval,
  once the upgrade deltas were assimilated. `AGENTS.md` carries all eleven
  protocols, `HANDOFF_PROTOCOL.md` is self-contained, and the permanent parts
  are all at the root. The project is fully assimilated; the kit was gitignored,
  so this log is the only record of the removal.
- [2026-08-06] Re-supplied the whole kit at 5.1.1 for this upgrade, gitignored
  and untracked, to read its changelog deltas and templates.
- [date not recorded] Removed the copied kit in one act under the pre-3.0.0
  assimilation model, before this stamp carried a log. Backfilled from the
  repository's initial state: no kit path has ever been tracked here, and the
  permanent parts were created directly at the project root.

## Upgrade History

- [2026-08-06] Upgraded 1.7.0 -> 5.1.1: adopted 2.0.0 (folder-local `inbox/`
  and `output/` ignores, tracked `staging/` and `decisions/`, solo-main git),
  3.0.0 (atrophy model, two-step slices, this Atrophy Log), 4.0.0 (root
  `HANDOFF_PROTOCOL.md`; `.trismegistus-local/` was already absent, so
  instructions only), 4.2.0 (Stamp Instruction Check), and 5.0.0 (`MEMORY.md`
  replaces the deleted `MEMORY_PROTOCOL.md`; the `claude_memory` symlink and its
  ignore line are retired). 3.1.0 GUI behaviour was rejected as inapplicable;
  3.2.0, 4.1.0, 5.1.0 and the patch releases arrived with the kit copy and
  needed no adoption. Both project scripts were updated for the new permanent
  parts.
- [date not recorded] Built with trismegistus 1.7.0.
