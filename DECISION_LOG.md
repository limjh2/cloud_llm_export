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
