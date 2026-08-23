#!/usr/bin/env python3
"""Validate repository-local references and entry-point consistency."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
DOCUMENTS = (ROOT / "README.md", ROOT / "index.html", ROOT / "sitemap.xml")
LOCAL_REFERENCE = re.compile(
    r'''(?:src|srcset|href)=["']([^"']+)["']|!\[[^]]*]\(([^)\s]+)(?:\s+["'][^"']*["'])?\)''',
    re.IGNORECASE,
)
SITE_PREFIX = "https://nelsambrose.github.io/togaf-diagrams/"


def normalise_reference(document: Path, reference: str) -> Path | None:
    reference = reference.strip()
    if "${" in reference:
        return None
    if reference.startswith(SITE_PREFIX):
        relative = reference.removeprefix(SITE_PREFIX)
        return ROOT / unquote(urlsplit(relative).path)

    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc or reference.startswith(("#", "mailto:", "javascript:")):
        return None

    relative = unquote(parsed.path)
    if not relative or relative == "/":
        return None
    if relative.startswith("/"):
        return ROOT / relative.lstrip("/")
    return document.parent / relative


def main() -> int:
    errors: list[str] = []
    checked_references = 0

    for document in DOCUMENTS:
        if not document.is_file():
            errors.append(f"Missing required document: {document.relative_to(ROOT)}")
            continue

        content = document.read_text(encoding="utf-8")
        for match in LOCAL_REFERENCE.finditer(content):
            reference = match.group(1) or match.group(2)
            target = normalise_reference(document, reference)
            if target is None:
                continue
            target = target.resolve()
            try:
                relative_target = target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{document.name}: path escapes repository: {reference}")
                continue
            if not target.exists():
                errors.append(f"{document.name}: missing local target: {relative_target}")
            checked_references += 1

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "`index.md`" in readme:
        errors.append("README refers to index.md; the GitHub Pages entry point is index.html")

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Repository validation passed ({checked_references} local references checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
