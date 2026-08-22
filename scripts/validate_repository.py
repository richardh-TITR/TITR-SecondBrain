#!/usr/bin/env python3
"""Lightweight repository safety and consistency checks."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IGNORED_PARTS = {".git", "__pycache__", ".venv", "venv", "dist", "build"}
TEXT_SUFFIXES = {".md", ".json", ".yml", ".yaml", ".py", ".txt"}
FORBIDDEN_PATH_PARTS = {
    "live-vault",
    "client-data",
    "personal-data",
    "production-data",
    "credentials",
    "secrets",
    "backups",
    "transcripts",
    "recordings",
}
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "generic bearer token": re.compile(r"\bBearer\s+[A-Za-z0-9._~+/=-]{20,}\b", re.IGNORECASE),
}


def tracked_candidate_files() -> list[Path]:
    result: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if any(part in IGNORED_PARTS for part in relative.parts):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in {"AGENTS.md", "CLAUDE.md"}:
            result.append(path)
    return sorted(result)


def main() -> int:
    errors: list[str] = []
    files = tracked_candidate_files()

    for path in files:
        relative = path.relative_to(ROOT)
        lowered_parts = {part.lower() for part in relative.parts}
        forbidden = lowered_parts.intersection(FORBIDDEN_PATH_PARTS)
        if forbidden:
            errors.append(f"forbidden operational path: {relative}")

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"not UTF-8: {relative}")
            continue

        if text and not text.endswith("\n"):
            errors.append(f"missing final newline: {relative}")

        for name, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"possible {name} in {relative}")

    for schema_path in sorted((ROOT / "schemas").glob("*.json")):
        try:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON in {schema_path.relative_to(ROOT)}: {exc}")
            continue
        if "$schema" not in schema or "$id" not in schema:
            errors.append(f"schema metadata missing in {schema_path.relative_to(ROOT)}")

    for template in sorted((ROOT / "vault-template" / "_templates").glob("*.md")):
        text = template.read_text(encoding="utf-8")
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            errors.append(f"template frontmatter missing: {template.relative_to(ROOT)}")
        if "synthetic" not in text.lower() and template.name != "daily.md":
            errors.append(f"template must be visibly synthetic: {template.relative_to(ROOT)}")

    adr_dir = ROOT / "docs" / "decisions"
    for adr in sorted(adr_dir.glob("*.md")):
        text = adr.read_text(encoding="utf-8")
        if "- Status:" not in text or "- Date:" not in text:
            errors.append(f"ADR metadata missing: {adr.relative_to(ROOT)}")

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Repository validation passed ({len(files)} text files checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
