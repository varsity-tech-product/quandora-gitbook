#!/usr/bin/env python3
"""Validate the public GitBook structure without external dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / "SUMMARY.md"
POLICY = json.loads((ROOT / "docs-policy.json").read_text(encoding="utf-8"))

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*]\(([^)]+)\)")
HTML_IMAGE = re.compile(r"<img\s+[^>]*src=[\"']([^\"']+)[\"']", re.IGNORECASE)
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def public_markdown_files() -> list[Path]:
    excluded = set(POLICY["public_term_exclusions"])
    return [
        path
        for path in sorted(ROOT.rglob("*.md"))
        if ".git" not in path.parts and relative(path) not in excluded
    ]


def parse_summary_links(text: str) -> list[str]:
    links: list[str] = []
    for target in MARKDOWN_LINK.findall(text):
        target = target.strip().split("#", 1)[0]
        if target and not target.startswith(("http://", "https://", "mailto:")):
            links.append(unquote(target))
    return links


def parse_frontmatter(path: Path) -> dict[str, str]:
    match = FRONTMATTER.match(path.read_text(encoding="utf-8"))
    if not match:
        return {}
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line or line.startswith((" ", "\t")):
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip("\"'")
    return values


def validate_summary(errors: list[str]) -> set[str]:
    text = SUMMARY.read_text(encoding="utf-8")
    headings = re.findall(r"^##\s+(.+?)\s*$", text, re.MULTILINE)
    required = POLICY["required_sections"]
    if headings != required:
        errors.append(
            "SUMMARY.md sections must exactly match the required user journey: "
            f"expected {required!r}, found {headings!r}"
        )

    links = parse_summary_links(text)
    duplicates = sorted({link for link in links if links.count(link) > 1})
    if duplicates:
        errors.append(f"SUMMARY.md contains duplicate page links: {duplicates}")

    for link in links:
        if not (ROOT / link).is_file():
            errors.append(f"SUMMARY.md target does not exist: {link}")

    return set(links)


def validate_navigation_coverage(nav_links: set[str], errors: list[str]) -> None:
    excluded = set(POLICY["markdown_exclusions"])
    pages = {
        relative(path)
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts and relative(path) not in excluded
    }
    missing = sorted(pages - nav_links)
    if missing:
        errors.append(f"Markdown pages missing from SUMMARY.md: {missing}")


def validate_local_references(errors: list[str]) -> None:
    for path in public_markdown_files():
        text = path.read_text(encoding="utf-8")
        targets = MARKDOWN_LINK.findall(text) + HTML_IMAGE.findall(text)
        for raw_target in targets:
            target = unquote(raw_target.strip().split("#", 1)[0])
            if not target or target.startswith(
                ("http://", "https://", "mailto:", "data:")
            ):
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(
                    f"{relative(path)} references a path outside the repository: "
                    f"{raw_target}"
                )
                continue
            if not resolved.exists():
                errors.append(
                    f"{relative(path)} has a broken local reference: {raw_target}"
                )


def validate_handoffs(errors: list[str]) -> None:
    for page, owner in POLICY["handoffs"].items():
        path = ROOT / page
        if not path.is_file():
            errors.append(f"Required handoff page is missing: {page}")
            continue
        metadata = parse_frontmatter(path)
        if metadata.get("content_status") != "handoff":
            errors.append(f"{page} must declare content_status: handoff")
        if metadata.get("content_owner") != owner:
            errors.append(f"{page} must declare content_owner: {owner}")


def validate_public_language(errors: list[str]) -> None:
    forbidden_terms = [
        re.compile(rf"\b{re.escape(term)}\b", re.IGNORECASE)
        for term in POLICY["forbidden_public_terms"]
    ]
    deprecated = [
        re.compile(pattern, re.IGNORECASE | re.DOTALL)
        for pattern in POLICY["deprecated_claim_patterns"]
    ]
    for path in public_markdown_files():
        text = path.read_text(encoding="utf-8")
        for pattern in forbidden_terms:
            if pattern.search(text):
                errors.append(
                    f"{relative(path)} contains internal-only term: "
                    f"{pattern.pattern}"
                )
        for pattern in deprecated:
            if pattern.search(text):
                errors.append(
                    f"{relative(path)} contains a deprecated factor-gate claim"
                )


def validate_registration_url(errors: list[str]) -> None:
    canonical = POLICY["registration_url"]
    required_pages = ("README.md", "getting-started/quickstart.md")
    for page in required_pages:
        if canonical not in (ROOT / page).read_text(encoding="utf-8"):
            errors.append(f"{page} must contain the canonical registration URL")


def main() -> int:
    errors: list[str] = []
    nav_links = validate_summary(errors)
    validate_navigation_coverage(nav_links, errors)
    validate_local_references(errors)
    validate_handoffs(errors)
    validate_public_language(errors)
    validate_registration_url(errors)

    if errors:
        print("Documentation verification failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Documentation verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

