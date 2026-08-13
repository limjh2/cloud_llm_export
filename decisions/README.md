# Decisions

> **PUBLIC TEMPLATE — NO EXPORTS**

Durable records of decisions and the evidence behind them.

A record here is **authoritative and kept**. It is not intake, not work in
progress, not a deliverable, and not superseded material — those are `inbox/`,
`staging/`, `output/`, and an archive respectively.

## What Belongs Here

- **Filled-in decision records** — the Markdown a questionnaire, gate, or review
  matrix produces once its questions are answered. A tool may deliver its record
  into `inbox/` because that is its write path, not because the record is
  intake; a filled-in record is the opposite of pending. Processing it means
  acting on the decisions and filing the record here.
- Other records whose value is the *reasoning and evidence* rather than the
  outcome alone — comparison studies that settled a choice, audit results, the
  option set considered before a major change.

## Why This Is Not `DECISION_LOG.md`

A `DECISION_LOG.md` entry states what was decided and why, briefly. A record
here carries what the log cannot: the full option set, the evidence table, the
notes written while deciding, and the items considered and rejected. Six months
later that is usually the part worth having.

The two are complementary. A decision worth logging should still get its
`DECISION_LOG.md` line; this folder holds the long form behind it.

## Rules

- Records are **not** processed, pruned, or reorganized. Once filed, a record is
  finished.
- Never edit a record to reflect a later decision. Write a new one; the old
  record is what was true when it was made.
- Name records `YYYY-MM-DD-topic.md`, keeping whatever name the producing tool
  gave where that is already dated and sortable.

## Relationship To The Kit

Like `workshop/`, `inbox/`, `staging/`, and `output/`, this folder is **the
target project's own** — not trismegistus formwork. It moves to the target
project root during setup and stays when the copied `trismegistus/` kit is
assimilated and removed. It is tracked: a record is durable project state by
definition.

## In the public template

This folder stays empty except for this file. A record describing a specific
holding — its providers, deliveries, or verification results — belongs only in
the private instance that holds it. The public tree audit rejects any other
tracked path here.
