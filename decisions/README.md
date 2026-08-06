# Decisions

> **PUBLIC TEMPLATE — NO EXPORTS**

Durable records whose value is the reasoning and evidence behind a decision, not
the outcome alone: comparison studies, audit results, filled-in decision
records, and the option sets considered before a structural change.

Name records `YYYY-MM-DD-topic.md`. A record is finished when filed: it is never
processed, pruned, reorganized, or edited to reflect a later decision. Write a
new record instead — the old one is what was true when it was made.

This folder does not replace `DECISION_LOG.md`. A decision worth logging still
gets its `D###` line there; this folder holds the long form behind it.

## In the public template

This folder stays empty except for this file. A real record describes a specific
holding — its providers, deliveries, or verification results — so it belongs to a
private instance. `scripts/audit_public_tree.py` rejects anything else tracked
here by path.
