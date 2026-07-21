#!/usr/bin/env python3
"""Reject public template trees or history containing private collection data."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ALLOWED_PATHS = {
    ".githooks/pre-push", ".gitignore", "AGENTS.md", "DECISION_LOG.md",
    "EXPORTS.tsv", "FILE_MANIFEST.tsv", "FORMAT.md", "MEMORY_PROTOCOL.md",
    "PROJECT_BRIEF.md", "PROJECT_STATUS.md", "PUBLIC_TEMPLATE.md",
    "README.md", "ROADMAP.md", "TRISMEGISTUS.md", "inbox/README.md",
    "output/README.md", "scripts/audit_public_tree.py",
    "scripts/build_manifest.py", "scripts/validate.py",
}
EXPECTED_TSV = {
    "EXPORTS.tsv": b"provider\texport_date\trelative_path\tfile_count\tsize_bytes\tnotes\n",
    "FILE_MANIFEST.tsv": b"relative_path\tsize_bytes\tsha256\n",
}
PUBLIC_MARKER = b"PUBLIC TEMPLATE \xe2\x80\x94 NO EXPORTS"
MARKER_DOCS = {"AGENTS.md", "PROJECT_STATUS.md", "README.md"}
HASH_RE = re.compile(rb"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])")
HOME_PATH_RE = re.compile(rb"/home/[^/\s]+/")
MAX_FILE_BYTES = 1_000_000
PRIVATE_TOKENS = (
    b"stuff_to_organize", b"Conversation Archaeologist", b"Ross",
    b"2026-04-27", b"2026-05-29", b"2026-07-02", b"2026-07-19",
    b"2026-07-21", b"limjh2",
)


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT)


def paths_for(commit: str | None) -> set[str]:
    command = ("ls-files", "-z") if commit is None else (
        "ls-tree", "-rz", "--name-only", commit
    )
    return {item.decode() for item in git(*command).split(b"\0") if item}


def read(commit: str | None, path: str) -> bytes:
    return (ROOT / path).read_bytes() if commit is None else git("show", f"{commit}:{path}")


def audit(label: str, commit: str | None) -> list[str]:
    paths = paths_for(commit)
    problems: list[str] = []
    missing = sorted(ALLOWED_PATHS - paths)
    extra = sorted(paths - ALLOWED_PATHS)
    if missing:
        problems.append(f"{label}: required structural files missing: {missing}")
    if extra:
        problems.append(f"{label}: non-template tracked paths: {extra}")
    for path in sorted(paths & ALLOWED_PATHS):
        try:
            data = read(commit, path)
        except (OSError, subprocess.CalledProcessError) as exc:
            problems.append(f"{label}: cannot read {path}: {exc}")
            continue
        if len(data) > MAX_FILE_BYTES:
            problems.append(f"{label}: {path} exceeds the size limit")
        if b"\0" in data:
            problems.append(f"{label}: {path} appears binary")
        if path in EXPECTED_TSV and data != EXPECTED_TSV[path]:
            problems.append(f"{label}: {path} must contain its header only")
        if path in MARKER_DOCS and PUBLIC_MARKER not in data:
            problems.append(f"{label}: {path} lacks the public-template marker")
        if path != "scripts/audit_public_tree.py":
            if HASH_RE.search(data):
                problems.append(f"{label}: {path} contains a SHA-256-like value")
            if HOME_PATH_RE.search(data):
                problems.append(f"{label}: {path} contains an absolute home path")
            if any(token in data for token in PRIVATE_TOKENS):
                problems.append(f"{label}: {path} contains a private-instance token")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--working-tree", action="store_true")
    group.add_argument("--commit")
    group.add_argument("--history", metavar="REV")
    args = parser.parse_args()
    if args.working_tree:
        problems = audit("working tree", None)
        scope = "working tree"
    elif args.commit:
        problems = audit(args.commit, args.commit)
        scope = args.commit
    else:
        revision = args.history or "HEAD"
        commits = git("rev-list", revision).decode().splitlines()
        problems = [problem for commit in commits for problem in audit(commit, commit)]
        scope = f"{len(commits)} commit(s) reachable from {revision}"
    for problem in problems:
        print(f"PROBLEM: {problem}", file=sys.stderr)
    if problems:
        print(f"FAIL: {len(problems)} public-template problem(s).", file=sys.stderr)
        return 1
    print(f"OK: public-template audit passed for {scope}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
