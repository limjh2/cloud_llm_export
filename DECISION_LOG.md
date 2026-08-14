# Cloud LLM Export Template — Decision Log

## D001 — Public structure and private holdings use separate repositories

- Status: Active
- Decision: The pushable template and every filled collection have independent
  histories. Filled repositories use `local/*`, have no remote, and are never
  pushed.
- Rationale: Ignoring payloads is insufficient when filenames, hashes, catalog
  rows, and collection history are themselves private.

## D002 — Provider deliveries remain intact

- Status: Active
- Decision: Each delivery retains its internal layout and coexists with older
  deliveries under a provider/date directory.
- Rationale: Repacking, normalization, and replacement destroy provenance.

## D003 — Catalog plus full file hashes define local verification

- Status: Active
- Decision: Filled instances reconcile one export-set row per delivery with one
  file-manifest row per preserved file.
- Rationale: Directory presence alone cannot detect silent modification or
  truncation.

## D004 — Software-only kit conventions do not apply

- Status: Active
- Date: 2026-08-06
- Decision: The trismegistus conventions for localization and input-method
  support, desktop launchers, and GUI behaviour and verification are declined
  and omitted from `TRISMEGISTUS.md` and `AGENTS.md`.
- Rationale: This project is a non-code source-collection structure with no user
  interface. Carrying the bullets would leave standing rules nothing can satisfy
  or check. Recorded here because the stamp template asks for a reason whenever a
  convention is trimmed.

## D005 — Trismegistus 5.1.1 conventions adopted

- Status: Active
- Date: 2026-08-06
- Decision: Upgraded from trismegistus 1.7.0 to 5.1.1. Adopted the tracked
  `staging/`, `decisions/`, and `workshop/` flow folders; folder-local
  `inbox/.gitignore` and `output/.gitignore` in place of root-level rules; the
  root `HANDOFF_PROTOCOL.md`; and `MEMORY.md`, which replaces the deleted
  `MEMORY_PROTOCOL.md` and retires the `claude_memory` symlink convention.
- Rationale: This repository's purpose is to supply reusable structure, so
  structure the kit now defines belongs in it rather than being mapped onto
  something else. The folder-local ignores matter more here than in an ordinary
  project: they travel with the folders when the template is instantiated, which
  root-level rules do not. Tracked memory replaces a per-machine symlink that
  never arrived with a clone.
- Consequence: The three tracked flow folders stay empty except for their
  `README.md` files in the public template. Their contents are always
  collection-specific, and `scripts/audit_public_tree.py` rejects any other
  tracked path in them.

## D006 — The public audit separates required structure from allowed history

- Status: Active
- Date: 2026-08-06
- Decision: `scripts/audit_public_tree.py` splits its single `ALLOWED_PATHS` set
  into `REQUIRED_PATHS` (the structure the current template must contain,
  checked only against the tip being audited) and `HISTORICAL_PATHS` (paths that
  were structural in earlier commits). Their union is what every reachable
  commit is checked against.
- Rationale: The old set was both the completeness check and the boundary check,
  so any structural change made every earlier commit fail — deleting
  `MEMORY_PROTOCOL.md` in D005 would have blocked every push through the
  `.githooks/pre-push` hook. The boundary check is the one that protects
  privacy and still applies to all history unchanged; only the completeness
  check is time-dependent.
- Consequence: A retired structural path is moved to `HISTORICAL_PATHS`, never
  deleted from the allowlist.

## D007 — The copied kit is removed; the project is fully assimilated

- Status: Active
- Date: 2026-08-06
- Decision: The `trismegistus/` kit re-supplied for the 5.1.1 upgrade was
  deleted with owner approval once its deltas were assimilated. No kit copy is
  kept in the repository, and none ever enters template history.
- Rationale: The kit is temporary formwork. `AGENTS.md` carries all eleven of
  its protocols, `HANDOFF_PROTOCOL.md` was written self-contained rather than
  pointing into `trismegistus/templates/`, and the verification commands are the
  project's own — so nothing load-bearing depended on the folder.
- Consequence: Because the kit was gitignored, its deletion produced no diff.
  The `TRISMEGISTUS.md` Atrophy Log is the only record. A future upgrade
  re-copies the kit from the canonical workspace, reads the changelog entries
  newer than the stamped version, and removes it again.

## D008 — Trismegistus 10.1.0 upgrade applicability

- Status: Active
- Date: 2026-08-12
- Decision: Upgrade this already-stamped template from trismegistus 5.1.1 to
  10.1.0. Adopt tracked inbox intake, the 6.1.0 permanent-guidance catch-up,
  the docket and trigger-based hardening rules, the project-owned skill boundary
  with ignored harness doorways, and upgrade-time atrophy. Record **none** for
  the model policy, standing goals, project index, and subprojects. Do not
  create `skills/`, `INDEX.md`, `homunculi/`, or `alkahest/` without an actual
  adopter in this template.
- Rationale: The template has no pending intake, old handoff folder, memory
  symlink/store, project-owned skills, child project, user interface, or
  collection of entries that needs an index. Its durable deliverable is
  reusable structure and verification tooling, so the index and GUI-related
  conventions do not apply. A generated-skill doorway review found none.
- Consequence: `inbox/.gitignore` is retired and becomes historical-only for
  public-tree auditing; `output/` remains the sole untracked flow folder.
  Existing self-contained `HANDOFF_PROTOCOL.md` and tracked `MEMORY.md` were
  retained while their current guidance was checked and refreshed. The
  re-supplied kit is removed after verification under the 10.0.0 upgrade-time
  atrophy rule because the project already had a durable stamp and every
  permanent function remains at the root. The post-removal Dead Pointer Review
  found only provenance or conditional references to the former kit and no
  actionable pointer into `templates/`, `trismegistus/`, or
  `.trismegistus-local`.

## D009 — Trismegistus 10.3.0 upgrade applicability

- Status: Active
- Date: 2026-08-14
- Decision: Upgrade this already-stamped template from trismegistus 10.1.0 to
  10.3.0. Adopt the 10.2.0 explicit Git publication policy (three mutually
  exclusive values — `local-only`, `solo-main`, `branch-and-pr`) and the 10.3.0
  optional path-free sibling-family declaration. **Preserve `git-workflow:
  solo-main`**: the existing declaration is valid, matches the stamp, and is
  consistent with the project's actual remote (`origin` on GitHub) and its
  pushable-template publication boundary. **Declare no sibling family**: the
  project carries no `sibling-family`/`sibling-role` lines anywhere, and per the
  10.3.0 lazy rule "preserve no claim" — an upgrade never requires a project to
  answer this optional convention, and a `none` placeholder is forbidden.
- Rationale: Both releases are Minor, add no protocol heading and no new project
  file, and are deliberately opt-in. `solo-main` remains the correct description
  of this template's Git custody: a filled instance is `local-only` by standing
  convention (no remote, never pushed), while the template itself pushes only
  after both verification checks pass. The sibling-family pair is informational
  only, grants no cross-project authority, and would be inferred from nothing;
  a later owner choice, not this upgrade, is what would add it.
- Consequence: `AGENTS.md` now carries the three-value Git rule and the
  sibling-family boundary while keeping the single `solo-main` declaration and
  no sibling claim; the stamp records both. No project file, registry, or
  protocol heading was created. The re-supplied 10.3.0 kit is removed after
  verification under the 10.0.0 upgrade-time atrophy rule, pending the
  final-removal owner confirmation.
