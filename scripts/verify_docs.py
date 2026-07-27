#!/usr/bin/env python3
"""Validate every repository-owned GitBook without external dependencies."""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
POLICY = json.loads(
    (REPOSITORY_ROOT / "docs-policy.json").read_text(encoding="utf-8")
)

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*]\(([^)]+)\)")
HTML_IMAGE = re.compile(r"<img\s+[^>]*src=[\"']([^\"']+)[\"']", re.IGNORECASE)
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
PENDING_TRANSLATION_NOTICE = re.compile(
    r'\A{% hint style="warning" %}\s*'
    r"本页中文内容正在审核中，以下暂时显示英文原文。\s*"
    r"{% endhint %}\s*",
    re.DOTALL,
)


@dataclass(frozen=True)
class DocumentRoot:
    key: str
    path: Path
    language: str
    exclude_directories: frozenset[str]
    translation_statuses: frozenset[str]


def document_roots() -> list[DocumentRoot]:
    roots: list[DocumentRoot] = []
    for key, config in POLICY["document_roots"].items():
        roots.append(
            DocumentRoot(
                key=key,
                path=(REPOSITORY_ROOT / config["path"]).resolve(),
                language=config["language"],
                exclude_directories=frozenset(
                    config.get("exclude_directories", [])
                ),
                translation_statuses=frozenset(
                    config.get("translation_statuses", [])
                ),
            )
        )
    return roots


def relative_to(root: DocumentRoot, path: Path) -> str:
    return path.relative_to(root.path).as_posix()


def is_included(root: DocumentRoot, path: Path) -> bool:
    relative = path.relative_to(root.path)
    return not relative.parts or relative.parts[0] not in root.exclude_directories


def markdown_files(root: DocumentRoot) -> list[Path]:
    excluded = set(POLICY["public_term_exclusions"])
    return [
        path
        for path in sorted(root.path.rglob("*.md"))
        if ".git" not in path.parts
        and is_included(root, path)
        and relative_to(root, path) not in excluded
    ]


def parse_links(text: str) -> list[str]:
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


def content_without_frontmatter(path: Path) -> str:
    return FRONTMATTER.sub("", path.read_text(encoding="utf-8"), count=1)


def validate_summary(root: DocumentRoot, errors: list[str]) -> set[str]:
    summary = root.path / "SUMMARY.md"
    if not summary.is_file():
        errors.append(f"{root.key}: SUMMARY.md is missing")
        return set()

    text = summary.read_text(encoding="utf-8")
    headings = re.findall(r"^##\s+(.+?)\s*$", text, re.MULTILINE)
    expected_headings = POLICY["section_headings"][root.language]
    if headings != expected_headings:
        errors.append(
            f"{root.key}: SUMMARY.md journey sections must be "
            f"{expected_headings!r}, found {headings!r}"
        )

    links = parse_links(text)
    duplicates = sorted({link for link in links if links.count(link) > 1})
    if duplicates:
        errors.append(f"{root.key}: duplicate SUMMARY.md links: {duplicates}")

    for link in links:
        if not (root.path / link).is_file():
            errors.append(f"{root.key}: missing SUMMARY.md target: {link}")

    return set(links)


def validate_navigation_coverage(
    root: DocumentRoot, nav_links: set[str], errors: list[str]
) -> None:
    excluded = set(POLICY["markdown_exclusions"])
    pages = {
        relative_to(root, path)
        for path in root.path.rglob("*.md")
        if ".git" not in path.parts
        and is_included(root, path)
        and relative_to(root, path) not in excluded
    }
    missing = sorted(pages - nav_links)
    if missing:
        errors.append(f"{root.key}: pages missing from SUMMARY.md: {missing}")


def validate_local_references(root: DocumentRoot, errors: list[str]) -> None:
    for path in markdown_files(root):
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
                resolved.relative_to(root.path)
            except ValueError:
                errors.append(
                    f"{root.key}: {relative_to(root, path)} references outside "
                    f"its document root: {raw_target}"
                )
                continue
            if not resolved.exists():
                errors.append(
                    f"{root.key}: {relative_to(root, path)} has a broken local "
                    f"reference: {raw_target}"
                )


def validate_handoffs(root: DocumentRoot, errors: list[str]) -> None:
    for page, owner in POLICY["handoffs"].items():
        path = root.path / page
        if not path.is_file():
            errors.append(f"{root.key}: required handoff page is missing: {page}")
            continue
        metadata = parse_frontmatter(path)
        if metadata.get("content_status") != "handoff":
            errors.append(f"{root.key}: {page} must declare content_status: handoff")
        if metadata.get("content_owner") != owner:
            errors.append(f"{root.key}: {page} must declare content_owner: {owner}")


def validate_translation_status(root: DocumentRoot, errors: list[str]) -> None:
    if not root.translation_statuses:
        return
    for path in markdown_files(root):
        if path.name == "SUMMARY.md":
            continue
        status = parse_frontmatter(path).get("translation_status")
        if status not in root.translation_statuses:
            errors.append(
                f"{root.key}: {relative_to(root, path)} must declare one of "
                f"translation_status={sorted(root.translation_statuses)}"
            )
        if status == "pending" and "本页中文内容正在审核中" not in path.read_text(
            encoding="utf-8"
        ):
            errors.append(
                f"{root.key}: pending page needs a visible Chinese review notice: "
                f"{relative_to(root, path)}"
            )


def validate_public_language(root: DocumentRoot, errors: list[str]) -> None:
    forbidden_terms = [
        re.compile(rf"\b{re.escape(term)}\b", re.IGNORECASE)
        for term in POLICY["forbidden_public_terms"]
    ]
    deprecated = [
        re.compile(pattern, re.IGNORECASE | re.DOTALL)
        for pattern in POLICY["deprecated_claim_patterns"]
    ]
    for path in markdown_files(root):
        text = path.read_text(encoding="utf-8")
        for pattern in forbidden_terms:
            if pattern.search(text):
                errors.append(
                    f"{root.key}: {relative_to(root, path)} contains "
                    f"internal-only term: {pattern.pattern}"
                )
        for pattern in deprecated:
            if pattern.search(text):
                errors.append(
                    f"{root.key}: {relative_to(root, path)} contains a "
                    "deprecated factor-gate claim"
                )


def validate_registration_url(root: DocumentRoot, errors: list[str]) -> None:
    canonical = POLICY["registration_url"]
    for page in ("README.md", "getting-started/quickstart.md"):
        path = root.path / page
        if not path.is_file():
            errors.append(f"{root.key}: required registration page is missing: {page}")
        elif canonical not in path.read_text(encoding="utf-8"):
            errors.append(
                f"{root.key}: {page} must contain the canonical registration URL"
            )


def validate_locale_parity(
    roots: dict[str, DocumentRoot],
    nav_links: dict[str, set[str]],
    errors: list[str],
) -> None:
    source_key, translation_key = POLICY["locale_parity"]
    source_links = nav_links[source_key]
    translation_links = nav_links[translation_key]
    if source_links != translation_links:
        missing = sorted(source_links - translation_links)
        extra = sorted(translation_links - source_links)
        errors.append(
            f"locale parity failed: {translation_key} missing={missing}, extra={extra}"
        )

    source_summary = roots[source_key].path / "SUMMARY.md"
    translation_summary = roots[translation_key].path / "SUMMARY.md"
    if not source_summary.is_file() or not translation_summary.is_file():
        return

    source_headings = re.findall(
        r"^##\s+(.+?)\s*$",
        source_summary.read_text(encoding="utf-8"),
        re.MULTILINE,
    )
    translation_headings = re.findall(
        r"^##\s+(.+?)\s*$",
        translation_summary.read_text(encoding="utf-8"),
        re.MULTILINE,
    )
    if len(source_headings) != len(translation_headings):
        errors.append("locale parity failed: journey section counts differ")

    for page in sorted(source_links):
        source_path = roots[source_key].path / page
        translation_path = roots[translation_key].path / page
        if not source_path.is_file() or not translation_path.is_file():
            continue
        status = parse_frontmatter(translation_path).get("translation_status")
        if status == "pending":
            fallback = PENDING_TRANSLATION_NOTICE.sub(
                "", content_without_frontmatter(translation_path), count=1
            )
            source_content = content_without_frontmatter(source_path)
            if fallback != source_content:
                errors.append(
                    "locale parity failed: pending fallback has drifted from "
                    f"English source: {page}"
                )
        if (
            status in {"draft", "reviewed"}
            and content_without_frontmatter(source_path)
            == content_without_frontmatter(translation_path)
        ):
            errors.append(
                f"locale parity failed: translated page matches English source: {page}"
            )


def validate_compatibility_mirror(
    roots: dict[str, DocumentRoot],
    nav_links: dict[str, set[str]],
    errors: list[str],
) -> None:
    compatibility_key, source_key = POLICY["compatibility_mirror"]
    compatibility = roots[compatibility_key]
    source = roots[source_key]
    compatibility_summary = compatibility.path / "SUMMARY.md"
    source_summary = source.path / "SUMMARY.md"
    if compatibility_summary.is_file() and source_summary.is_file():
        if compatibility_summary.read_bytes() != source_summary.read_bytes():
            errors.append(
                "temporary root compatibility SUMMARY.md has drifted from en"
            )
    if nav_links[compatibility_key] != nav_links[source_key]:
        errors.append("temporary root compatibility navigation has drifted from en")
        return
    for page in sorted(nav_links[source_key]):
        compatibility_path = compatibility.path / page
        source_path = source.path / page
        if not compatibility_path.is_file() or not source_path.is_file():
            continue
        compatibility_text = compatibility_path.read_text(encoding="utf-8")
        source_text = source_path.read_text(encoding="utf-8")
        if compatibility_text != source_text:
            errors.append(
                f"temporary root compatibility page has drifted from en: {page}"
            )


def validate_glossary(errors: list[str]) -> None:
    path = REPOSITORY_ROOT / "localization/glossary.json"
    if not path.is_file():
        errors.append("localization/glossary.json is missing")
        return
    glossary = json.loads(path.read_text(encoding="utf-8"))
    terms = glossary.get("terms")
    if not isinstance(terms, list) or not terms:
        errors.append("localization glossary must contain a non-empty terms list")
        return
    english_terms: set[str] = set()
    for index, term in enumerate(terms):
        if not isinstance(term, dict) or not term.get("en") or not term.get("zh-CN"):
            errors.append(f"localization glossary term {index} needs en and zh-CN")
            continue
        if term["en"] in english_terms:
            errors.append(f"duplicate localization glossary term: {term['en']}")
        english_terms.add(term["en"])


def main() -> int:
    errors: list[str] = []
    roots = {root.key: root for root in document_roots()}
    nav_links: dict[str, set[str]] = {}

    for root in roots.values():
        nav_links[root.key] = validate_summary(root, errors)
        validate_navigation_coverage(root, nav_links[root.key], errors)
        validate_local_references(root, errors)
        validate_handoffs(root, errors)
        validate_translation_status(root, errors)
        validate_public_language(root, errors)
        validate_registration_url(root, errors)

    validate_locale_parity(roots, nav_links, errors)
    validate_compatibility_mirror(roots, nav_links, errors)
    validate_glossary(errors)

    if errors:
        print("Documentation verification failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Documentation verification passed for compatibility, en, and zh.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
