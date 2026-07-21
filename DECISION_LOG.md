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
