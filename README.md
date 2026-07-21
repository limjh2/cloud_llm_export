# Cloud LLM Export Template

> **PUBLIC TEMPLATE — NO EXPORTS**

Reusable structure and verification tooling for a private, provider-neutral
collection of intact cloud-LLM account exports.

The public repository intentionally contains no provider payloads, catalog
rows, filenames, hashes, or collection-derived reports. A filled collection is
a separate local-only repository with independent history and no remote.

## Instantiate privately

1. Copy this structure into a separate local project.
2. Initialize independent Git history on a `local/library` branch and remove
   every remote.
3. Place complete deliveries in `exports/<provider>/YYYY-MM-DD/`.
4. Add one row per set to `EXPORTS.tsv`.
5. Run `python scripts/build_manifest.py` and `python scripts/validate.py`.

Never turn a filled clone into the public repository. See `AGENTS.md` and
`PUBLIC_TEMPLATE.md` for the publication boundary.

## Template verification

```bash
python scripts/validate.py
python scripts/audit_public_tree.py
```
