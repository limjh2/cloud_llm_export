# Agent Memory Protocol

Per-project agent memory may be exposed through a gitignored `claude_memory`
symlink. It is local machine state and never part of the public template or a
collection commit.

The target is the Claude Code memory directory keyed to the project's absolute
launch path. Link the whole `memory/` directory, never `MEMORY.md` alone.

`MEMORY.md` is a one-line-per-memory index. Each linked fact file uses
frontmatter with a short `name`, one-line `description`, and a `metadata.type`
of `user`, `feedback`, `project`, or `reference`. Read before writing, update
instead of duplicating, remove false or obsolete facts, and keep every index
line synchronized with exactly one file.

Do not store facts already present in repository policy, project memory, code,
or Git history. Verify any remembered path or behavior before relying on it.
