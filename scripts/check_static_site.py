#!/usr/bin/env python3
"""Check local static-site links and asset references."""

from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if value is None:
                continue
            if name in {"href", "src"}:
                self.refs.append((name, value))


def _is_external(ref: str) -> bool:
    parsed = urlparse(ref)
    return parsed.scheme in {"http", "https", "mailto", "tel"}


def _target_path(source: Path, ref: str) -> Path | None:
    if _is_external(ref) or ref.startswith("#"):
        return None
    parsed = urlparse(ref)
    if parsed.path == "":
        return None
    path = unquote(parsed.path)
    if path.startswith("/"):
        return ROOT / path.lstrip("/")
    return (source.parent / path).resolve()


def check_html_refs() -> list[str]:
    errors: list[str] = []
    for html_file in sorted(ROOT.glob("*.html")):
        parser = LinkParser()
        parser.feed(html_file.read_text(encoding="utf-8"))
        for attr, ref in parser.refs:
            target = _target_path(html_file, ref)
            if target is None:
                continue
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{html_file.name}: {attr} escapes site root: {ref}")
                continue
            if not target.exists():
                errors.append(f"{html_file.name}: missing {attr}: {ref}")
    return errors


def check_project_assets() -> list[str]:
    errors: list[str] = []
    projects_path = ROOT / "projects.json"
    projects = json.loads(projects_path.read_text(encoding="utf-8"))
    for project in projects:
        refs: list[str] = []
        if project.get("screenshot"):
            refs.append(project["screenshot"])
        for screenshot in project.get("screenshots", []):
            refs.append(screenshot.get("src", ""))
        for ref in refs:
            if ref and not (ROOT / ref).exists():
                errors.append(f"projects.json:{project.get('id')}: missing screenshot {ref}")
    return errors


def main() -> int:
    errors = check_html_refs() + check_project_assets()
    if errors:
        print("Static-site check failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Static-site check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
