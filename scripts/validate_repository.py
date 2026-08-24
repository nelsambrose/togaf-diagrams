#!/usr/bin/env python3
"""Run deterministic integrity checks for the diagram library."""

from __future__ import annotations

import hashlib
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
SITEMAP = ROOT / "sitemap.xml"
DOCUMENTS = (README, INDEX, SITEMAP)
ACTIVE = ROOT / "docs" / "diagrams"
EXCEPTIONS = ROOT / "scripts" / "diagram-exceptions.txt"
SITE_PREFIX = "https://nelsambrose.github.io/togaf-diagrams/"
REPOSITORY_PREFIX = "https://github.com/nelsambrose/togaf-diagrams"
ASSET_SUFFIXES = {".png", ".webp"}
KEBAB_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.(?:png|webp)$")
LOCAL_REFERENCE = re.compile(
    r'''(?:src|srcset|href)=["']([^"']+)["']|!\[[^]]*]\(([^)\s]+)(?:\s+["'][^"']*["'])?\)''',
    re.IGNORECASE,
)
DIAGRAM_REFERENCE = re.compile(r"docs/diagrams/[A-Za-z0-9_./-]+\.(?:png|webp)")
SEARCH_ENTRY = re.compile(
    r'''\{\s*title:\s*["'][^"']+["'].*?img:\s*["']([^"']+)["'].*?href:\s*["']([^"']+)["'].*?\}'''
)


def repository_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def logical_stem(reference: str) -> str:
    return str(Path(reference).with_suffix(""))


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


def github_anchor(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text.strip().lower())
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"\s", "-", text)


def read_allowlist(errors: list[str]) -> set[str]:
    if not EXCEPTIONS.is_file():
        errors.append("Missing scripts/diagram-exceptions.txt")
        return set()

    entries: set[str] = set()
    for number, raw_line in enumerate(EXCEPTIONS.read_text(encoding="utf-8").splitlines(), 1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if Path(line).suffix in ASSET_SUFFIXES:
            errors.append(f"{repository_path(EXCEPTIONS)}:{number}: use a logical stem without an extension")
        if not line.startswith("docs/diagrams/"):
            errors.append(f"{repository_path(EXCEPTIONS)}:{number}: entry must start with docs/diagrams/")
        if line in entries:
            errors.append(f"{repository_path(EXCEPTIONS)}:{number}: duplicate entry: {line}")
        entries.add(line)
    return entries


def readme_anchors(content: str) -> set[str]:
    anchors: set[str] = set()
    occurrences: defaultdict[str, int] = defaultdict(int)
    for match in re.finditer(r"^#{1,6}\s+(.+?)\s*$", content, re.MULTILINE):
        base = github_anchor(match.group(1).rstrip("#").rstrip())
        count = occurrences[base]
        occurrences[base] += 1
        anchors.add(base if count == 0 else f"{base}-{count}")
    return anchors


def check_local_references(errors: list[str]) -> int:
    checked = 0
    for document in DOCUMENTS:
        if not document.is_file():
            errors.append(f"Missing required document: {repository_path(document)}")
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
            checked += 1
    return checked


def check_assets(errors: list[str], document_text: str, allowlist: set[str]) -> int:
    assets = sorted(path for path in ACTIVE.rglob("*") if path.suffix.lower() in ASSET_SUFFIXES)
    formats: defaultdict[str, set[str]] = defaultdict(set)
    hashes: defaultdict[str, list[Path]] = defaultdict(list)

    for asset in assets:
        relative = repository_path(asset)
        stem = logical_stem(relative)
        formats[stem].add(asset.suffix.lower())
        if not KEBAB_NAME.fullmatch(asset.name):
            errors.append(f"Active diagram filename is not lowercase kebab-case: {relative}")
        digest = hashlib.sha256(asset.read_bytes()).hexdigest()
        hashes[digest].append(asset)

    for stem, suffixes in sorted(formats.items()):
        if suffixes != ASSET_SUFFIXES:
            errors.append(f"Active diagram requires PNG and WebP versions: {stem} ({sorted(suffixes)})")

    for duplicate_group in hashes.values():
        if len(duplicate_group) > 1:
            paths = ", ".join(repository_path(path) for path in duplicate_group)
            errors.append(f"Byte-for-byte duplicate active assets: {paths}")

    referenced = {logical_stem(reference) for reference in DIAGRAM_REFERENCE.findall(document_text)}
    active_stems = set(formats)
    for stem in sorted(active_stems - referenced - allowlist):
        errors.append(f"Active diagram is neither published nor allowlisted: {stem}")
    for stem in sorted(allowlist - active_stems):
        errors.append(f"Allowlisted diagram does not exist as an active pair: {stem}")
    for stem in sorted(allowlist & referenced):
        errors.append(f"Published diagram should be removed from the exceptions file: {stem}")

    for reference in sorted(set(re.findall(r"archive/[A-Za-z0-9_./-]+\.(?:png|webp)", document_text))):
        errors.append(f"Archived diagram must not be published: {reference}")

    return len(assets)


def check_catalogue(errors: list[str], readme: str, index: str, sitemap: str) -> int:
    anchors = readme_anchors(readme)
    for anchor in re.findall(r"\]\(#([^)]+)\)", readme):
        if anchor not in anchors:
            errors.append(f"README contains an unresolved internal anchor: #{anchor}")

    search_block_match = re.search(r"const diagrams = \[(.*?)\n\s*\];", index, re.DOTALL)
    if not search_block_match:
        errors.append("Could not locate the website search catalogue")
        return 0

    entries = SEARCH_ENTRY.findall(search_block_match.group(1))
    search_stems: set[str] = set()
    for image, href in entries:
        image_path = ROOT / image
        if not image_path.is_file():
            errors.append(f"Search catalogue references a missing image: {image}")
        webp = image_path.with_suffix(".webp")
        if not webp.is_file():
            errors.append(f"Search catalogue image has no WebP pair: {repository_path(webp)}")
        search_stems.add(logical_stem(image))
        if not href.startswith(f"{REPOSITORY_PREFIX}#"):
            errors.append(f"Search catalogue has an unexpected diagram link: {href}")
        else:
            anchor = href.split("#", 1)[1]
            if anchor not in anchors:
                errors.append(f"Search catalogue link does not resolve in README: #{anchor}")

    sitemap_stems = {
        logical_stem(reference)
        for reference in DIAGRAM_REFERENCE.findall(sitemap)
        if reference.endswith(".png")
    }
    for stem in sorted(search_stems - sitemap_stems):
        errors.append(f"Search catalogue diagram is missing from sitemap.xml: {stem}")
    for stem in sorted(sitemap_stems - search_stems):
        errors.append(f"Sitemap diagram is missing from the search catalogue: {stem}")

    sections = list(re.finditer(r'<section class="category-section" id="([^"]+)"', index))
    catalogue_total = 0
    category_total = 0
    for position, section in enumerate(sections):
        end = sections[position + 1].start() if position + 1 < len(sections) else index.find("</main>", section.end())
        block = index[section.start():end]
        declared = re.search(r'<span class="category-count">(\d+) diagrams?</span>', block)
        actual = len(re.findall(r'class="card"', block))
        if not declared:
            errors.append(f"Category {section.group(1)} has no declared diagram count")
        elif int(declared.group(1)) != actual:
            errors.append(
                f"Category {section.group(1)} declares {declared.group(1)} diagrams but contains {actual} cards"
            )
        if section.group(1) != "featured":
            catalogue_total += actual
            category_total += 1

    category_stat = re.search(r'<div class="stat-number">(\d+)</div><div class="stat-label">Categories</div>', index)
    if not category_stat or int(category_stat.group(1)) != category_total:
        errors.append(f"Category statistic does not match the {category_total} catalogue categories")

    diagram_stat = re.search(r'<div class="stat-number">(\d+)\+?</div><div class="stat-label">Diagrams</div>', index)
    if not diagram_stat or int(diagram_stat.group(1)) > catalogue_total:
        errors.append(f"Diagram statistic is incompatible with the {catalogue_total} catalogue entries")
    if len(entries) != catalogue_total:
        errors.append(f"Search catalogue has {len(entries)} entries but the visible catalogue has {catalogue_total} cards")

    return len(entries)


def main() -> int:
    errors: list[str] = []
    checked_references = check_local_references(errors)

    readme = README.read_text(encoding="utf-8")
    index = INDEX.read_text(encoding="utf-8")
    sitemap = SITEMAP.read_text(encoding="utf-8")
    document_text = "\n".join((readme, index, sitemap))

    if "`index.md`" in readme:
        errors.append("README refers to index.md; the GitHub Pages entry point is index.html")

    allowlist = read_allowlist(errors)
    asset_count = check_assets(errors, document_text, allowlist)
    catalogue_count = check_catalogue(errors, readme, index, sitemap)

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Repository validation passed "
        f"({checked_references} local references, {asset_count} active assets, "
        f"{catalogue_count} catalogue entries checked)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
