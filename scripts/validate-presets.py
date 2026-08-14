#!/usr/bin/env python3
"""Validate the voice-preset layer without external dependencies.

Upstream's validate-package.py owns the skill package: version sync, pattern
numbering, the line budget. This script owns what this fork adds on top, so
the two stay separable and upstream syncs do not collide with our checks.

Each preset file declares its identity in YAML frontmatter, and that
declaration is the single source of truth. The status and version of a preset
were previously repeated in five places by hand, which is exactly the kind of
thing that drifts on the next bump.

What it deliberately does NOT check: the version numbers that appear in a
preset's prose history ("v0.2 added...", "v0.3 replaces..."). Those are a
changelog and are supposed to name older versions. Only the title line is
required to match, because that is the one that goes stale unnoticed.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = (ROOT / "SKILL.md").read_text()
README = (ROOT / "README.md").read_text()
PRESET_DIR = ROOT / "references"

REQUIRED_KEYS = ("preset", "lang", "version", "status")
VALID_STATUS = {"draft", "stable"}

errors: list[str] = []


def fail(path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if match is None:
        return None
    fields = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip().strip("\"'")
    return fields


preset_files = sorted(PRESET_DIR.glob("preset-*.md"))
if not preset_files:
    raise SystemExit("No preset files found in references/")

for path in preset_files:
    text = path.read_text()
    fields = parse_frontmatter(text)

    if fields is None:
        fail(path, "missing YAML frontmatter")
        continue

    missing = [key for key in REQUIRED_KEYS if key not in fields]
    if missing:
        fail(path, f"frontmatter missing {', '.join(missing)}")
        continue

    preset, lang = fields["preset"], fields["lang"]
    version, status = fields["version"], fields["status"]

    if status not in VALID_STATUS:
        fail(path, f"status must be one of {sorted(VALID_STATUS)}, found {status!r}")

    expected_name = f"preset-{preset}-{lang}.md"
    if path.name != expected_name:
        fail(path, f"frontmatter implies filename {expected_name}")

    # The routing table in SKILL.md is what makes a preset reachable at all.
    rows = [line for line in SKILL.splitlines() if path.name in line]
    if not rows:
        fail(path, "not routed from the SKILL.md preset table")
    readme_rows = [line for line in README.splitlines() if path.name in line]
    if not readme_rows:
        fail(path, "not listed in the README preset table")

    # A draft has to say so where the user chooses a preset, not only inside
    # the file, or the choice is made without knowing the rules are provisional.
    if status == "draft":
        marker = f"v{version}"
        for label, found in (("SKILL.md", rows), ("README.md", readme_rows)):
            for row in found:
                if "draft" not in row.lower() or marker not in row:
                    fail(path, f"{label} row must mark this preset as draft {marker}")
    else:
        for label, found in (("SKILL.md", rows), ("README.md", readme_rows)):
            if any("draft" in row.lower() for row in found):
                fail(path, f"{label} still marks this preset as draft, frontmatter says {status}")

    # Title line is the copy most likely to go stale on a version bump.
    title = text.split("---\n", 2)[-1].lstrip().splitlines()[0]
    if status == "draft" and version not in title:
        fail(path, f"title line does not carry version {version}: {title!r}")

# An entry pointing at a file that does not exist fails silently at runtime:
# the agent is told to read a preset and finds nothing.
for referenced in set(re.findall(r"references/(preset-[a-z0-9-]+\.md)", SKILL + README)):
    if not (PRESET_DIR / referenced).exists():
        errors.append(f"references/{referenced}: routed but the file does not exist")

if errors:
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    raise SystemExit(f"{len(errors)} preset problem(s) found")

print(f"Preset layer is valid ({len(preset_files)} presets)")
