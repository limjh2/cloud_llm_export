#!/usr/bin/env python3
"""Rebuild the private SHA-256 ledger for immutable export payloads."""

from __future__ import annotations

import hashlib
import os
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPORTS = ROOT / "exports"
MANIFEST = ROOT / "FILE_MANIFEST.tsv"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    paths = sorted(path for path in EXPORTS.rglob("*") if path.is_file())
    fd, temporary_name = tempfile.mkstemp(
        dir=ROOT, prefix=".FILE_MANIFEST.", suffix=".tmp", text=True
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as output:
            output.write("relative_path\tsize_bytes\tsha256\n")
            for path in paths:
                relative = path.relative_to(ROOT).as_posix()
                output.write(f"{relative}\t{path.stat().st_size}\t{sha256(path)}\n")
        os.replace(temporary_name, MANIFEST)
    finally:
        if os.path.exists(temporary_name):
            os.unlink(temporary_name)
    print(f"Wrote {MANIFEST.name}: {len(paths)} files")


if __name__ == "__main__":
    main()
