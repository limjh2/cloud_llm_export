# Cloud LLM Export Template — Roadmap

## R001 — Maintain the reusable structure

**Status:** Ongoing maintenance

- Keep provider-neutral placement and integrity rules coherent.
- Keep validators compatible with an empty template and filled local instances.
- Keep the public-tree audit restrictive.

## Private-instance intake pattern

A local instance may define a bounded slice for each future provider delivery:
move the intact set from inbox, add its catalog row, rebuild the file manifest,
validate, and commit only to the local repository.
