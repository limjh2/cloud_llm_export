# Staging

> **PUBLIC TEMPLATE — NO EXPORTS**

Tracked transit lane for material that arrived through `inbox/` and is being
integrated across more than a single move.

In a filled local instance this is where a provider delivery is examined,
described, and reconciled before it is accepted as an immutable export set under
`exports/<provider>/YYYY-MM-DD/`. Every file here has a named destination; if
you cannot name one, the material is still un-triaged (`inbox/`) or is an idea
rather than material (`workshop/`). Nothing stays after its integration lands.

Never stage by copying out of an accepted export set. Accepted sets are source
evidence and are not edited, extracted over, or duplicated.

## In the public template

This folder stays empty except for this file. Staged material is always
collection-specific, so anything else tracked here would be a publication-
boundary violation — `scripts/audit_public_tree.py` rejects it by path.
