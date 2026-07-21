# Cloud LLM Export — Public Template Agent Instructions

> **PUBLIC TEMPLATE — NO EXPORTS**

This repository is the reusable, content-free structure for a private cloud-LLM
export collection. It is not the filled collection.

## Publication boundary

The complete reachable history of this repository must contain only reusable
structure. Never add or push provider payloads, export-set rows, file manifests,
hashes, original filenames or paths, account identifiers, collection-specific
reports, or holding-specific status and decision history.

A request to “push” means publish only this audited template unless the owner
explicitly and unambiguously changes the policy. Never push a filled repository,
a `local/*` branch, `--all`, or `--mirror`. Deleting private material in a later
commit is insufficient because Git history retains it.

Before every push, run:

```bash
python scripts/validate.py
python scripts/audit_public_tree.py
```

Enable the blocking hook in each clone:

```bash
git config core.hooksPath .githooks
```

## Private-instance model

Instantiate a filled collection as a separate sibling repository with
independent history. Its branch should be `local/library`; it must have no
remote or upstream and must never receive a push target. Git branches alone are
not a privacy boundary.

In a filled instance:

- Raw provider exports under `exports/` are immutable source evidence.
- One export set lives at `exports/<provider>/YYYY-MM-DD/`; preserve its
  provider-supplied internal layout.
- Register every set in `EXPORTS.tsv`, rebuild `FILE_MANIFEST.tsv` with
  `python scripts/build_manifest.py`, and run `python scripts/validate.py`.
- Never upload, publish, force-add, normalize, or expose private export contents
  without an explicit bounded disclosure request.
- Check `inbox/` near the start of collection work. Every item except its
  README is pending intake and must not be deleted.

## Template editing rules

- Keep `EXPORTS.tsv` and `FILE_MANIFEST.tsv` header-only here.
- Use only synthetic, obviously fictional examples.
- Do not copy collection-specific documentation from a filled instance.
- Keep the public audit allowlist synchronized with intentional structural
  changes.
- Run both checks before committing and before pushing.

## Trismegistus conventions

This is a Trismegistus 1.7.0 reference-collection template. Project memory,
slice discipline, inbox/output boundaries, and shared-memory conventions are
documented in the root files. Per-machine memory is always gitignored.
