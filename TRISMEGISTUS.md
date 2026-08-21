# trismegistus Provenance

trismegistus-Version: 10.7.0

- **Role:** Public, content-free reference-collection template
- **Origin archetype:** `reference_collection_foundation`, adapted for immutable
  directory-valued export sets
- **Scaffolded:** not recorded (the original stamp carried no date, and the
  template's own audit rejects the dates involved as private-instance tokens)
- **Last upgraded:** 2026-08-21
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
- **Hardening:** a standing, finite `H###` hardening-pass practice; a new run
  needs a new release or material change, a user-reported symptom, new evidence
  from a named dependency, or an explicit owner request. Completion does not
  schedule a successor; the practice is never retired.
- **Model policy:** **none**, meaning no class of model is excluded by this
  convention. A future restriction would cover the whole project unless it
  names a narrower condition.
- **Project skills:** if this project authors an Agent Skill, its one canonical,
  tracked copy lives at `skills/<skill-name>/SKILL.md`; create `skills/` only on
  first use. `.claude/`, `.codex/`, `.agents/`, and `.pi/` are ignored generated
  harness doorways. Installed external skills remain canonical at their source
  and are reached only through an ignored, regenerable pointer; no tracked
  symlink points to an absolute path outside this project.
- **Inbox:** `inbox/` at the project root is the intake area; every file there
  except `README.md` is pending intake, handled per `inbox/README.md`. It is a
  drop point, not a workspace, and is tracked, including pending intake.
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
- **Flow-folder tracking:** git holds what it would cost something to lose —
  `inbox/`, `staging/`, `workshop/`, and `decisions/` are tracked; `output/` is
  not, because the project can produce a deliverable again.
- **Shared agent memory:** `MEMORY.md` at the project root is the one memory
  every agent reads and edits — tracked, committed, and permanent like this
  stamp. It carries its own format rules, holds only what is not derivable from
  the project, and excludes facts about the user personally, which are the same
  in every repository and do not belong in a pushable file. Project facts go
  here and nowhere else; a harness store may hold user-level memory or a
  redirect, but never a second copy of this project's facts.
- **Handoffs:** a session handoff is an ordinary `output/` file, named
  `YYYY-MM-DDTHHMMSS±HHMM-session-handoff.md` and written only on an explicit
  request; it follows the root `HANDOFF_PROTOCOL.md`, which is permanent like
  this stamp and self-contained.
- **Git:** local-first; coherent commits after verified slices. The one
  `git-workflow` declaration has three explicit values — `local-only`,
  `solo-main`, and `branch-and-pr`; this project declares `solo-main`, and an
  absent line is also effective `solo-main`. The default is commit to main, with
  no feature branches or pull requests — but pushing is subordinate to the
  publication boundary in `AGENTS.md`, which is stricter: a filled instance has
  no remote at all (its own `local-only` custody), and this template is pushed
  only after `scripts/validate.py` and `scripts/audit_public_tree.py` pass.
- **Sibling family:** **none declared**. The optional paired root lines
  `sibling-family: <logical-id>` / `sibling-role: template | filled` are absent
  here; the pair is informational, grants no cross-project authority, and never
  inferred from repository names, remotes, or neighbouring projects. This is a
  deliberate absence (see D009), not a placeholder or a `none` value.
- **Publication boundary:** public template and private collection histories are
  permanently separate. `python scripts/audit_public_tree.py` blocks
  collection-derived public state by exact path across all reachable history;
  `python scripts/validate.py` reconciles a filled local instance.
- **Subprojects:** **none**. If a child is added later, a full subproject belongs
  under `homunculi/<child>/` and owns its files, while an alkahest belongs under
  `alkahest/<child>/` and keeps working papers for a deliverable that remains at
  this root. Create neither lane merely for this declaration; one repository
  and one parent boundary line continue throughout.

Software-only conventions the kit carries — localization and input-method
support, desktop launchers, and GUI behaviour and verification — do not apply to
this non-code source collection. See `DECISION_LOG.md` D004.

## Atrophy Log

Parts of the copied `trismegistus/` folder removed as this project took over
their function. Newest first.

- [2026-08-21] Removed the re-supplied 10.7.0 kit in full under the
  10.0.0 upgrade-time atrophy rule. The 10.4.0–10.6.x upgrade-procedure
  changes and the 10.7.0 downloaded-input rule were reconciled into the
  permanent guidance; no modified or unrecognized kit part was present. The
  kit was gitignored and untracked, so this log records its removal.
- [2026-08-14] Removed the re-supplied 10.3.0 kit in full under the
  10.0.0 upgrade-time atrophy rule, with owner approval. The 10.2.0 and 10.3.0
  deltas were assimilated into the permanent parts; `HANDOFF_PROTOCOL.md` was
  already self-contained and a dead-pointer sweep found only provenance or
  historical references. The kit was gitignored and untracked, so this log is
  the record of its removal.
- [2026-08-12] Removed the re-supplied 10.1.0 kit in full under the
  already-stamped upgrade-time atrophy rule. The permanent parts at the root,
  the 15 protocol headings in `AGENTS.md`, and the verification checks establish
  redundancy; the generated skill pointer review found none. The kit was
  gitignored and untracked, so this log is the record of its removal.
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

- [2026-08-21] Upgraded 10.3.0 -> 10.7.0: adopted the 10.4.0 completion and
  declaration-driven publication contract, 10.5.0 post-condition and inbox
  invariant checks, 10.6.x terminal-state and reconciliation clarifications,
  and 10.7.0 content validation for downloaded project input. This project has
  no download path, so no retrofit was needed; the re-supplied kit was removed
  after verification under the 10.0.0 upgrade-time atrophy rule.
- [2026-08-14] Upgraded 10.1.0 -> 10.3.0: adopted 10.2.0 (Git publication
  policy made explicit — three values, existing `solo-main` preserved and
  consistent with the project's remote) and 10.3.0 (optional path-free sibling
  family — reviewed and deliberately left **undeclared**; no claim is
  preserved because none existed, per the lazy opt-in rule). Both releases add
  no protocol heading and no new project file. The re-supplied kit is removed
  after verification under the 10.0.0 upgrade-time atrophy rule.
- [2026-08-12] Upgraded 5.1.1 -> 10.1.0: adopted tracked inbox intake, the
  permanent-guidance baseline catch-up, project-owned skill boundaries, the
  docket and trigger-based hardening rules, and the 10.0.0 upgrade-time
  atrophy branch. Reviewed **none** for model policy, standing goals, project
  index, subprojects, and generated skill doorways; GUI, localization, and
  desktop-launcher conventions remain inapplicable under D004.
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
