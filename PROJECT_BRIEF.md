# Cloud LLM Export Template — Project Brief

## Purpose

Provide a reusable, provider-neutral structure for keeping complete cloud-LLM
account exports locally while preserving provider layout and mechanically
verifiable integrity metadata.

## Goals

1. Keep dated provider deliveries intact.
2. Reconcile a set catalog, a file-level SHA-256 ledger, and the live corpus.
3. Make future intake routine and downstream corpus ownership unambiguous.
4. Prevent private collection history from entering public Git history.

## Non-goals

- Publishing real exports or collection-derived metadata
- Parsing, searching, or presenting conversations
- Editing or deduplicating provider files in place
- Treating a newer snapshot as a replacement for an older one
