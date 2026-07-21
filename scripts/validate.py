#!/usr/bin/env python3
"""Reconcile the export catalog, file ledger, and live private corpus."""

from __future__ import annotations

import csv
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "EXPORTS.tsv"
MANIFEST = ROOT / "FILE_MANIFEST.tsv"
EXPORTS = ROOT / "exports"
DATE_RE = re.compile(r"^20\d{2}-\d{2}-\d{2}$")

REQUIRED = {
    ".gitignore", "AGENTS.md", "README.md", "PROJECT_BRIEF.md",
    "PROJECT_STATUS.md", "ROADMAP.md", "DECISION_LOG.md", "FORMAT.md",
    "TRISMEGISTUS.md", "MEMORY_PROTOCOL.md", "EXPORTS.tsv",
    "FILE_MANIFEST.tsv", "inbox/README.md", "output/README.md",
    "scripts/build_manifest.py", "scripts/validate.py",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def main() -> int:
    problems: list[str] = []
    for relative in sorted(REQUIRED):
        if not (ROOT / relative).is_file():
            problems.append(f"missing required file: {relative}")
    if problems:
        for problem in problems:
            print(f"ERROR: {problem}")
        return 1

    catalog = read_tsv(CATALOG)
    manifest = read_tsv(MANIFEST)
    catalog_paths: set[str] = set()

    for row in catalog:
        provider = row.get("provider", "")
        export_date = row.get("export_date", "")
        relative = row.get("relative_path", "")
        expected = f"exports/{provider}/{export_date}"
        if provider != provider.lower() or not provider:
            problems.append(f"invalid provider: {provider!r}")
        if not DATE_RE.fullmatch(export_date):
            problems.append(f"invalid export date: {export_date!r}")
        if relative != expected:
            problems.append(f"catalog path {relative!r} should be {expected!r}")
        if relative in catalog_paths:
            problems.append(f"duplicate catalog path: {relative}")
        catalog_paths.add(relative)
        export_root = ROOT / relative
        if not export_root.is_dir():
            problems.append(f"cataloged export directory missing: {relative}")
            continue
        files = [path for path in export_root.rglob("*") if path.is_file()]
        try:
            wanted_count = int(row.get("file_count", ""))
            wanted_size = int(row.get("size_bytes", ""))
        except ValueError:
            problems.append(f"non-integer count/size in catalog row: {relative}")
            continue
        if len(files) != wanted_count:
            problems.append(f"{relative}: file count differs from catalog")
        if sum(path.stat().st_size for path in files) != wanted_size:
            problems.append(f"{relative}: total size differs from catalog")

    live_sets = {
        path.relative_to(ROOT).as_posix()
        for provider in EXPORTS.iterdir()
        if provider.is_dir()
        for path in provider.iterdir()
        if path.is_dir()
    } if EXPORTS.is_dir() else set()
    for relative in sorted(live_sets - catalog_paths):
        problems.append(f"uncataloged export set: {relative}")
    for relative in sorted(catalog_paths - live_sets):
        problems.append(f"catalog row without export set: {relative}")

    manifest_rows: dict[str, dict[str, str]] = {}
    for row in manifest:
        relative = row.get("relative_path", "")
        if relative in manifest_rows:
            problems.append(f"duplicate manifest path: {relative}")
        manifest_rows[relative] = row
    live_files = {
        path.relative_to(ROOT).as_posix(): path
        for path in EXPORTS.rglob("*") if path.is_file()
    }
    for relative in sorted(set(live_files) - set(manifest_rows)):
        problems.append(f"export file missing from manifest: {relative}")
    for relative in sorted(set(manifest_rows) - set(live_files)):
        problems.append(f"manifest path missing on disk: {relative}")
    for relative in sorted(set(live_files) & set(manifest_rows)):
        path = live_files[relative]
        row = manifest_rows[relative]
        try:
            wanted_size = int(row.get("size_bytes", ""))
        except ValueError:
            problems.append(f"manifest size is not an integer: {relative}")
            continue
        if path.stat().st_size != wanted_size:
            problems.append(f"size mismatch: {relative}")
        elif sha256(path) != row.get("sha256", ""):
            problems.append(f"SHA-256 mismatch: {relative}")

    pending = [
        path for path in (ROOT / "inbox").rglob("*")
        if path.is_file() and path.name != "README.md"
    ]
    if pending:
        problems.append(f"pending inbox intake: {len(pending)} file(s)")
    if problems:
        for problem in problems:
            print(f"ERROR: {problem}")
        print(f"Validation FAILED: {len(problems)} problem(s).")
        return 1
    total_size = sum(path.stat().st_size for path in live_files.values())
    print(
        f"Validation PASS: {len(catalog)} export sets, {len(live_files)} files, "
        f"{total_size} bytes; all SHA-256 hashes match."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
