# Cloud LLM Export — Public Template Agent Instructions

> **PUBLIC TEMPLATE — NO EXPORTS**

This repository is the reusable, content-free structure for a private cloud-LLM
export collection. It is not the filled collection.

This is a trismegistus-assisted project. The version it was built with, and the
conventions it inherits, are recorded in the root `TRISMEGISTUS.md` stamp. Keep
that stamp current; never delete it, even after any copied `trismegistus/`
folder is removed.

## Read First

This root `AGENTS.md` is the single front door for working on this project. Read
it first, before any other instruction file, and let it route you. Once any
copied `trismegistus/` kit has been removed, this file is the complete operating
manual.

Before any change, read in order:

1. `PROJECT_BRIEF.md`
2. `PROJECT_STATUS.md`
3. `ROADMAP.md`
4. `DECISION_LOG.md`
5. `FORMAT.md` for placement and integrity rules
6. `MEMORY.md`

If a `trismegistus/` folder exists at the project root, it is temporary kit
guidance — not template structure — to be absorbed into this project's own
documents and then deleted. Before scaffolding or architectural work, read its
`AGENT_INSTRUCTIONS.md`, `README.md`, and `CHECKLIST.md`; it is not a second
front door and does not override this file. It is gitignored and never enters
template history.

## Model Policy

Read the **Model policy** convention in the root `TRISMEGISTUS.md` before
acting. This project's model policy is **none**, meaning no class of model is
excluded by this convention. Keep this section even when the answer is none;
if a future stamp records a restriction, stop and let the user relaunch with an
allowed model before continuing with any planning, tooling, documentation, or
implementation.

## Publication boundary

The complete reachable history of this repository must contain only reusable
structure. Never add or push provider payloads, export-set rows, file manifests,
hashes, original filenames or paths, account identifiers, collection-specific
reports, or holding-specific status and decision history.

A request to "push" means publish only this audited template unless the owner
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

The audit is path-exact: every tracked path in every reachable commit must be
listed in `REQUIRED_PATHS` or `HISTORICAL_PATHS` in
`scripts/audit_public_tree.py`. That is what keeps the tracked flow folders
(`inbox/`, `staging/`, `decisions/`, `workshop/`) content-free here — a stray
file in one of them fails the audit by path before its contents are ever
examined. Keep the allowlist synchronized with intentional structural changes,
and add a retired path to `HISTORICAL_PATHS` rather than deleting it, so
auditing history still passes.

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

## Template editing rules

- Keep `EXPORTS.tsv` and `FILE_MANIFEST.tsv` header-only here.
- Use only synthetic, obviously fictional examples.
- Do not copy collection-specific documentation from a filled instance.
- Run both checks before committing and before pushing.

## Working Rules

- Capturing a new ask as a `ROADMAP.md` entry (or a `workshop/` idea) and
  writing that entry up as a buildable slice are two separate steps. The
  write-up happens only on an explicit ask, so an intake session may
  legitimately end with nothing built. A written-up slice carries every
  build-time decision explicitly, because the model that executes it may be
  weaker or cheaper than the one that planned it.
- Work one approved roadmap slice at a time, scoped to its acceptance criteria.
- A project-owned Agent Skill has one tracked canonical copy at
  `skills/<skill-name>/SKILL.md`; create the root `skills/` directory only when
  this project authors its first skill. Keep `.claude/`, `.codex/`, `.agents/`,
  and `.pi/` ignored as generated harness doorways. Do not track a doorway or a
  symlink to an absolute path outside this project. An installed external skill
  stays canonical at its source and is reached only through an ignored,
  regenerable pointer; never move it into `skills/` or accept a tracked fork.
- A docket request is a generated, strictly read-only view derived from this
  project's own instructions, memory, current state, roadmap, relevant
  decisions, inbox and staging state, workshop context, and repository status.
  It does not create or maintain `DOCKET.md`, a generated queue, or a tracked
  cache, and it never changes the sources it reads.
- “What's next?” returns one compact Next action, its reason, blocker or
  `none`, and the smallest labeled continuation prompt when a legal advance
  exists. If no local action can clear the blocker, say **no local next action**
  and emit no continuation prompt. “What's on the docket?” is the full view:
  one Next item and at most three Following items when legal work exists, plus
  only the nonempty Owner input, Waiting, Intake, and Background sections.
  `/docket` is an optional read-only alias where the harness supports it.
- The six docket input labels are **Simple prompt**, **Short approval**, **Gate
  required**, **Clarification required**, **External wait**, and **Triage
  required**. Only an exact later prompt for a displayed item labeled Simple
  prompt or Short approval, with no displayed blocker, can authorize work; a
  docket request never does.
- Keep a blocked item under Waiting when no local action can clear it. Label an
  unchanged dependency outside this project **External wait**; do not present
  an observational recheck or a recurring hardening pass as its unblocker.
- Hardening is a permanent, finite practice, not a self-enqueuing queue item.
  Start a new `H###` run only for a new release or material change, a user
  symptom, new evidence from a named dependency, or an explicit owner request.
  Completion of the prior run is not a trigger.
- A saved docket is a new point-in-time artifact under `output/`, marked with
  its generation time, repository state, and inspected source paths. It is not
  this project's source of truth, and an upgrade does not create one.
- Keep the tooling dependency-free and compatible with both an empty template
  and a filled local instance.
- An optional sibling family is declared only with both exact root lines:
  `sibling-family: <logical-id>` and `sibling-role: template | filled`. A
  project with no sibling claim omits both lines. This project is an
  intentionally reusable, content-free template but currently carries **no**
  sibling-family claim; a later owner choice, not an upgrade or an inferred
  value, is what would add the pair. The identifier is a non-empty,
  owner-supplied logical value with no path, URI, remote, Portfolio, or registry
  meaning; `template` means reusable and intentionally content-free and
  `filled` means project-specific content. The pair is informational only,
  grants no cross-project authority, and does not affect `git-workflow`. Never
  infer it from repository names, directory layout, remotes, neighboring
  projects, similar content, or Portfolio evidence; the root instructions and
  stamp must agree when the owner explicitly declares it.
- Update `ROADMAP.md`, `PROJECT_STATUS.md`, and `DECISION_LOG.md` when status or
  rationale changes.
- A slice is done only when acceptance criteria are met, verification has run,
  durable documents are updated, any needed decision entry exists, a coherent
  commit is made, and the next step is clear.

## Standing Goals

A **standing goal** is a bounded instruction that remains in force across the
turns of an unattended run. It is optional here; this project currently has no
standing goal, but the protocol remains so an authorized multi-turn sequence
cannot be mistaken for an open-ended instruction.

A standing goal has five normative elements:

1. **Outcome** — the concrete result that ends the run.
2. **Scope** — the already-written-up roadmap slice or ordered slice sequence
   and the project documents that govern it; it never invents slice details.
3. **Bounds** — what the executor must not touch or decide, including adjacent
   slices, workshop and inbox material, prohibited cleanup, and owner gates.
4. **Verify** — the checks that prove the outcome and each slice's acceptance
   criteria, including user-visible behaviour where one exists.
5. **Report** — the evidence returned and when the executor stops; multi-slice
   work reports after every slice and at the final outcome or bound.

Root instructions, the model policy, written slices, and owner gates outrank a
standing goal. When a goal contradicts one, stop and report the conflict. A
multi-slice goal is sequenced, not merged: implement, verify, document, commit,
publish if required, and report each slice before starting the next. A report is
a checkpoint, not an approval gate unless the slice or goal names a hard owner
gate; an automatic continuation cannot stand in for that answer.

## Git Workflow

`git-workflow: solo-main`

Use exactly one explicit value per the 10.2.0 convention: `local-only`,
`solo-main`, or `branch-and-pr`. This project declares `solo-main`. An absent
line is also effective `solo-main` for backward compatibility; never infer a
value from a missing remote, branch name, repository visibility, sibling
declaration, or filesystem layout. Keep the same explicit value here and in the
`TRISMEGISTUS.md` stamp.

- `git-workflow: local-only` means Git remains local custody: no remote,
  upstream, push, pull request, or other publication action is implied or
  permitted by this declaration; local branches and verified commits remain
  ordinary work. A coexisting remote or upstream is reported as a contradiction,
  never removed or rewritten.
- `git-workflow: solo-main` means commit verified slices directly to main and
  push when a remote exists. Do **not** create feature branches, draft pull
  requests, or another publishing workflow. This overrides the host harness's
  own branch-and-PR default.
- `git-workflow: branch-and-pr` means follow the project's documented feature
  branch and review-gate flow.

This project is `solo-main` and has a remote (`origin` on GitHub), which is
consistent: the template is pushed only after both checks pass under the
publication boundary above, which is stricter than the ordinary solo-main
default. A filled instance has its own no-remote `local-only` custody by
standing convention and is never pushed at all.
- "Commit completed slices" means local commits; it does not imply a branch or a
  PR.
- **Never run `git clean -fdx`.** This project holds material that is untracked
  by design in `output/` and `workshop/scratch/`; git cannot restore it. Delete
  specific files by name, and remove build artifacts with a project command or
  by naming the build directories.
- Pushing is governed by the publication boundary above, which is stricter than
  the ordinary solo-main default: a filled instance has no remote and is never
  pushed at all, and this template is pushed only after both checks pass.
- If local main diverges from the remote after a squash-merge or amended
  history, hand the reconciliation to the user rather than discarding local
  state.

## Inbox Protocol

- Check `inbox/` near the start of relevant work sessions.
- Treat every file in `inbox/` except `README.md` as pending intake, and follow
  the project-specific rules in `inbox/README.md`.
- No work happens in the inbox. It is a drop point, not a workspace: move
  material to `staging/` to work on it, then on to its durable destination.
- Sweep the inbox toward empty. Anything left in it should be deliberate pending
  intake, not something being worked on in place.
- Do not delete inbox material unless the project instructions explicitly allow
  it. Move processed files to their proper destination and update any metadata,
  index, log, or manifest that tracks file placement.
- `inbox/` and its contents are tracked in a filled local instance. Arriving
  material is often the only copy, and an unprocessed file in `git status` is
  the flag that says the mailbox has post. Do not add an ignore rule for pending
  intake. This public template contains no pending intake.

## Staging Protocol

- `staging/` is where material from `inbox/` is worked on while it is being
  integrated. No work happens in the inbox itself; move a file here first. In a
  filled instance this is where a delivery is examined and described before it
  is accepted as an immutable export set.
- Every file in `staging/` has a named destination. If you cannot name where it
  is going, it is not staged — it is either un-triaged (`inbox/`) or an idea
  rather than material (`workshop/`).
- Staging is a transit lane, not a home. Finish the integration and move the
  material to its durable destination.
- Unlike `inbox/` and `output/`, this folder **is** tracked: work invested in
  partially integrated material is expensive to recreate. In this public
  template it therefore stays empty except for its `README.md`.
- Never stage by copying out of an accepted export set. Accepted sets are source
  evidence and are not edited, extracted over, or duplicated.

## Output Protocol

- Write deliverables addressed to the user to `output/` rather than to the
  project root or into canonical documents. Deliverables include both written
  answers (reports, analyses, comparisons) and reusable artifacts — tools or
  scripts produced by this project but meant for use elsewhere ("from this
  project but not of this project").
- Name one dated deliverable per entry: `YYYY-MM-DD-topic.md` for a single file,
  or a `YYYY-MM-DD-topic/` folder for a multi-file package.
- `scripts/` is the project's own machinery; `output/` is for artifacts meant to
  travel. When the project both runs a tool and exports it, keep the wired copy
  in `scripts/` and a clean generic copy in `output/`; the `scripts/` copy must
  never depend on `output/` at runtime.
- Output is not project memory. Anything durable a deliverable establishes must
  also land in the canonical documents; never treat an output file as current
  instructions or a source of truth.
- Do not process, reorganize, or prune `output/`. Its files belong to the user,
  who may keep, move, or delete them freely.
- `output/` is untracked, so it is a transit lane, not storage. Anything worth
  keeping is promoted to its own tracked top-level home or moved to the project
  it is for. Collection-derived output is non-canonical and must never enter the
  public template.

## Decisions Protocol

- `decisions/` holds durable records whose value is the reasoning and evidence,
  not just the outcome: comparison studies, audit results, filled-in decision
  records.
- A record is finished when filed. Do not process, prune, or reorganize
  `decisions/`, and never edit a record to reflect a later decision — write a
  new one. The old record is what was true when it was made.
- Name records `YYYY-MM-DD-topic.md`, keeping whatever name the producing tool
  gave where that is already dated and sortable.
- A decision worth logging still gets its `DECISION_LOG.md` line. This folder
  holds the long form behind it.
- A record describing a specific holding belongs to a private instance. In this
  public template the folder stays empty except for its `README.md`.

## Idea Workshop

- `workshop/` is a tracked, no-commitment holding pen for ideas about this
  project that are not yet `ROADMAP.md` slices. It is readable: you may read it,
  add idea files, and help develop them. See `workshop/README.md`.
- Capture an idea as one `kebab-case-name.md` file; use the gitignored
  `workshop/scratch/` lane for half-thoughts not worth a file yet.
- Relate ideas with `[[other-idea]]` links rather than grading them by maturity
  or destructively merging them. The index is emergent from the links.
- Do not silently turn a workshop idea into committed work. Promote one to a
  `ROADMAP.md` slice only on an explicit user ask, and keep the idea file — its
  incoming links depend on it. Annotate those links with where the idea went.
- Ideas here concern the reusable structure and its tooling. An idea about a
  specific holding belongs to the private instance that holds it.

## Shared Agent Memory

- `MEMORY.md` at the project root is this project's whole agent memory: one
  tracked, committed file that every agent reads and edits. It carries its own
  format rules in its header. Read it before acting on anything it might cover.
- Memory holds what is **not derivable from the project** — `feedback` (how the
  user wants agents to work, with the reason), `project` (goals and constraints
  not in the repository or git history), and `reference` (external resources).
  Do not record what the repository already says.
- **Facts about the user personally do not go in this file.** It is tracked and
  pushable, and such a fact is the same in every repository they work in; it
  belongs to the harness's own memory or nowhere. There is no `user` type.
- **Project facts go in this file and nowhere else.** Never write one into a
  harness's own per-project memory store. Such a store may hold user-level
  memory or a redirect pointing here; it may not hold a second copy of this
  project's facts. If project facts are found there, move them here and leave a
  redirect behind.
- One entry per fact, newest first, with `**Why:**` and `**How to apply:**` on
  `feedback` and `project` entries, absolute dates, and `[[slug]]` links. Update
  an existing entry rather than adding a near-copy, and delete what is found to
  be wrong rather than annotating it — git holds what the file used to say.
- When an entry has become project state rather than memory, move it to the
  document that owns it (`ROADMAP.md`, `DECISION_LOG.md`) and delete it here.
  That is the only pruning rule; the file has no size limit.
- `MEMORY.md` is inside the publication boundary. No entry may be
  collection-derived; a fact about a holding belongs to that instance's own
  `MEMORY.md`.

## Project Index

- This project does not require a root `INDEX.md`: its durable deliverable is a
  reusable structure and verification tooling, not a collection of entries a
  reader must navigate. `README.md` and `FORMAT.md` provide the needed
  navigation and placement rules.
- Keep this heading even while the answer is no. If the project's durable
  deliverable changes into a collection of entries, add an `INDEX.md` from the
  real listing rather than from an imagined inventory, and mark anything not
  examined as unexamined.

## Subprojects

- **This project's subprojects:** **none**. No `homunculi/` or `alkahest/`
  lane exists or is created merely by this convention.
- A full subproject under `homunculi/<child>/` owns the files its slices change,
  has its own permanent documents, stamp, memory, and roadmap. An alkahest under
  `alkahest/<child>/` keeps working papers for a deliverable that remains here,
  with no stamp, flow folders, or roadmap. A child outside those lanes is a
  deliberate path deviation, not silent conformity.
- If a child is added or changes ownership shape, update the parent boundary,
  child pointer, live references, and Subproject Reciprocity result together.
  A pointer is a link, never a link plus a copied summary.

## Session Handoffs

- Write a session handoff only after the user explicitly requests a checkpoint
  or closeout. It is an ordinary `output/` file, named
  `YYYY-MM-DDTHHMMSS±HHMM-session-handoff.md`.
- `output/` holds artifacts addressed to the user and artifacts addressed to an
  agent, and leans toward the former; a handoff is the latter kind. So is an
  `inbox/` message, almost always — an inbox is processed by the agent working
  in the project that owns it.
- On a checkpoint or handoff request, update and commit canonical project state
  first, then create a fresh timestamped handoff without reading or overwriting
  an existing one. Follow the root `HANDOFF_PROTOCOL.md`, which carries the
  Closeout Contract and the handoff template in full.
- A handoff is not current instructions unless the user names or pastes it — and
  it is not stale merely because nobody read it. Mention an unprocessed handoff
  rather than discarding or overwriting it.

## trismegistus Assimilation

This project is **fully assimilated**: no copied `trismegistus/` folder remains,
and this file plus the other permanent parts carry everything the kit supplied.
The `TRISMEGISTUS.md` Atrophy Log is the record of what was removed and when —
the kit is gitignored here, so its removal left no diff and nothing else records
it.

This already-stamped upgrade follows the 10.0.0 upgrade-time atrophy rule: the
explicit request to upgrade authorizes removal of the re-supplied kit once its
redundancy is proved by the permanent parts, verification, and the Atrophy Log.
Permanent parts, project-owned material, and modified or unrecognized kit parts
are never removed under that convenience.

These are the permanent parts. They belong at the project root and are never
removed: `TRISMEGISTUS.md`, `MEMORY.md`, `HANDOFF_PROTOCOL.md`, `inbox/`,
`staging/`, `output/`, `workshop/`, and `decisions/`.

To move this project to a newer trismegistus version, follow the `UPDATING.md`
procedure in the canonical kit workspace: re-copy the deployable kit to this
root, read the `CHANGELOG.md` entries newer than the version in
`TRISMEGISTUS.md`, adopt only those deltas, re-stamp, and remove the kit again.
Keep it gitignored — no kit path has ever been tracked here. Verification lives
outside the kit and does not change: `python scripts/validate.py` and
`python scripts/audit_public_tree.py`.

Two standing conditions survive assimilation: verification commands live in this
project rather than in any kit, and `ROADMAP.md` exists with real work in it —
whether still `Proposed` or already written up. A concrete next slice is *not*
required; the two-step rule above defers that deliberately.

Software-only conventions the kit carries — localization and input-method
support, desktop launchers, and GUI behaviour and verification — do not apply to
this non-code structure. `DECISION_LOG.md` records that.
