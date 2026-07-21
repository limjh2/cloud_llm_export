# trismegistus Provenance

trismegistus-Version: 1.7.0

- **Role:** Public, content-free reference-collection template
- **Origin archetype:** `reference_collection_foundation`, adapted for immutable
  directory-valued export sets

## Conventions

- Root project-memory files define purpose, status, roadmap, decisions, and
  collection format.
- `python scripts/validate.py` reconciles a filled local instance.
- `python scripts/audit_public_tree.py` blocks collection-derived public state.
- Root `inbox/` is pending intake; root `output/` is non-canonical.
- Per-machine shared memory and private handoffs are gitignored.
- Public template and private collection histories are permanently separate.

Software-only GUI, localization, IME, and desktop-launcher conventions do not
apply to this non-code source collection.
