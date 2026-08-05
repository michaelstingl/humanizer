#!/usr/bin/env python3
"""Typography hint generator for German prose.

Surfaces candidates for the mechanical rules in
references/preset-neutral-professional-de.md: dash glyph, quotation marks,
apostrophe, spacing. It reports where a German typographic norm is probably
missed so the prose pass can spend its attention on judgement instead of on
character hunting.

It does not decide anything. Every finding is a hint that needs reading in
context. Legitimate reasons to leave a flagged character alone:

  - quoted English text, English work titles, bibliography entries
  - verbatim quotation of someone else's writing, where the received state has
    to stay provable (contract, procurement, legal, archived correspondence)
  - product, brand and identifier names
  - code, config or data shown in running prose
  - deliberate register choices in dialogue or literary passages

Therefore this tool never rewrites anything. It has no fix mode on purpose:
replacing a character without reading the passage around it can corrupt a
quotation, a work title or an identifier, and no exception list is reliable
enough to make that safe. The hints are input for a person or for the prose
pass; the edit itself is a judgement call. A clean run is not evidence that the
prose is good.

Usage:
    de_typo_lint.py FILE [FILE ...]     check
    de_typo_lint.py -                   check stdin
    de_typo_lint.py --list              list rules

Exit codes: 0 no hints, 1 hints to review, 2 usage error.

Markdown-aware: skips fenced code blocks, indented code, inline code spans,
URLs and link destinations, and YAML frontmatter. Suppression:

    <!-- de-typo-lint: off -->   ... <!-- de-typo-lint: on -->
    any line ending in            <!-- de-typo-lint: ignore-line -->

A rules catalog that quotes wrong glyphs on purpose (like the DE preset
itself) turns the linter off at the top of the file.
"""

import argparse
import re
import sys

EM_DASH = "—"      # — Geviertstrich, English setting
EN_DASH = "–"      # – Halbgeviertstrich, German Gedankenstrich
LDQUO, RDQUO = "“", "”"   # " " English
GLDQUO, GRDQUO = "„", "“"  # „ " German (opening low, closing high)
APOS = "’"         # ’ typographic apostrophe
NBSP = " "

# Abbreviations that DIN 5008 sets with a space between the parts.
ABBREVS = ["z.B.", "d.h.", "u.a.", "z.T.", "i.d.R.", "u.U.", "o.Ä.", "v.a.",
           "s.o.", "s.u.", "u.v.m.", "z.Zt.", "i.A."]

# Units that take a space after the number.
UNITS = ["kg", "km", "cm", "mm", "kW", "kWh", "MB", "GB", "TB", "ms", "GHz",
         "MHz", "EUR", "Mio", "Mrd"]

# Function words that must not be capitalised mid-heading. German nouns are
# capitalised, so capitalised *function* words are the actual English-title-case
# import.
FUNCTION_WORDS = ["Der", "Die", "Das", "Den", "Dem", "Des", "Ein", "Eine",
                  "Und", "Oder", "Aber", "Mit", "Ohne", "Für", "Von", "Zu",
                  "Im", "In", "An", "Auf", "Bei", "Als", "Wie", "Nach",
                  "Über", "Unter", "Aus", "Durch", "Gegen", "Um", "Vor"]

RULES = {
    "DE-T01": "Geviertstrich (—) statt Halbgeviertstrich (–) als Gedankenstrich",
    "DE-T02": "Englische Anführungszeichen (“ ”) statt deutscher („ “)",
    "DE-T03": "Gerade Anführungszeichen (\") statt deutscher („ “)",
    "DE-T04": "Schreibmaschinen-Apostroph (') statt typografischem (’)",
    "DE-T05": "Doppeltes Leerzeichen nach dem Satzende",
    "DE-T06": "Abkürzung ohne Spatium (z.B. statt z. B.)",
    "DE-T07": "Zahl und Einheit ohne Leerzeichen (50% statt 50 %)",
    "DE-T08": "Bis-Strich mit Spatien (2024 – 2026 statt 2024–2026)",
    "DE-T09": "Emoji vor der Überschrift",
    "DE-T10": "Englische Title-Case in der Überschrift",
}

# Rules a machine can state with certainty. Still not rules a machine may
# apply on its own: see the module docstring.
MECHANICAL = {"DE-T01", "DE-T02", "DE-T03", "DE-T04", "DE-T05", "DE-T06",
           "DE-T07", "DE-T08"}


class Finding:
    def __init__(self, path, line, col, rule, excerpt):
        self.path, self.line, self.col, self.rule, self.excerpt = (
            path, line, col, rule, excerpt)

    def __str__(self):
        mark = " [mechanisch]" if self.rule in MECHANICAL else " [Urteil nötig]"
        return "%s:%d:%d: %s %s%s | %s" % (
            self.path, self.line, self.col, self.rule, RULES[self.rule],
            mark, self.excerpt)


def mask(line):
    """Blank out spans where typography rules do not apply.

    Inline code, URLs and markdown link destinations keep their length so
    column numbers stay true; their characters become a sentinel. A sentinel
    rather than a space, because blanking with spaces would manufacture
    multi-space runs and trip the double-space rule.
    """
    out = list(line)

    def blank(m):
        for i in range(m.start(), m.end()):
            out[i] = "\x00"

    for pat in (r"`[^`]*`",                    # inline code
                r"<[^>]+>",                    # html tags and autolinks
                r"\]\([^)]*\)",                # link destination
                r"https?://\S+",               # bare URL
                r"\b[\w.-]+@[\w.-]+\b"):       # email
        for m in re.finditer(pat, line):
            blank(m)
    return "".join(out)


def check_line(path, lineno, raw):
    text = mask(raw)
    found = []

    def add(rule, col):
        start = max(0, col - 25)
        found.append(Finding(path, lineno, col + 1, rule,
                             raw[start:col + 25].strip()))

    for m in re.finditer(EM_DASH, text):
        add("DE-T01", m.start())

    # U+201D never occurs in German setting. U+201C is ambiguous: it is the
    # German *closing* quote and the English *opening* quote. Treat it as
    # English only where it opens a quotation, i.e. at a word boundary before
    # a word character.
    for m in re.finditer(RDQUO, text):
        add("DE-T02", m.start())
    for m in re.finditer(r"(?:(?<=^)|(?<=[\s(\[]))%s(?=\w)" % LDQUO, text):
        add("DE-T02", m.start())

    # Straight double quotes used as quotation marks, not as code delimiters.
    for m in re.finditer(r'"', text):
        add("DE-T03", m.start())

    # Apostrophe between letters or before a trailing s: Nutzer's, geht's
    for m in re.finditer(r"(?<=\w)'(?=\w)|(?<=\w)'(?=\s|$)", text):
        add("DE-T04", m.start())

    for m in re.finditer(r"[.!?:]  +(?=\S)", text):
        add("DE-T05", m.start())

    for abbr in ABBREVS:
        for m in re.finditer(re.escape(abbr), text):
            add("DE-T06", m.start())

    for m in re.finditer(r"\d\s*%", text):
        if NBSP not in m.group() and " " not in m.group():
            add("DE-T07", m.start())
    for m in re.finditer(r"\d(%s)\b" % "|".join(UNITS), text):
        add("DE-T07", m.start())

    for m in re.finditer(r"\d\s+[%s%s]\s+\d" % (EN_DASH, EM_DASH), text):
        add("DE-T08", m.start())

    if re.match(r"^#{1,6}\s", raw):
        heading = raw.split(" ", 1)[1] if " " in raw else ""
        lead = heading.lstrip()
        if re.match(r"^[^\w\s#]", lead) and not lead.startswith(
                ("`", "[", "*", "_", '"', "'", "(", GLDQUO, LDQUO, EN_DASH, EM_DASH)):
            add("DE-T09", len(raw) - len(heading))
        # Drop a leading emoji or symbol so the first *word* is word one.
        words = [w for w in heading.split() if re.search(r"\w", w)]
        for w in words[1:]:
            if w.strip(".,:;()[]„“\"'") in FUNCTION_WORDS:
                add("DE-T10", raw.index(w))
                break
    return found


def iter_prose_lines(lines):
    """Yield (index, line) for lines where typography rules apply."""
    fence = None
    in_frontmatter = lines and lines[0].rstrip() == "---"
    enabled = True
    for i, line in enumerate(lines):
        stripped = line.strip()
        if in_frontmatter:
            if i > 0 and stripped == "---":
                in_frontmatter = False
            continue
        if "de-typo-lint: off" in line:
            enabled = False
            continue
        if "de-typo-lint: on" in line:
            enabled = True
            continue
        m = re.match(r"^(```+|~~~+)", stripped)
        if m:
            token = m.group(1)[:3]
            if fence is None:
                fence = token
            elif token == fence:
                fence = None
            continue
        if fence is not None or not enabled:
            continue
        if "de-typo-lint: ignore-line" in line:
            continue
        if re.match(r"^(    |\t)\S", line):   # indented code block
            continue
        yield i, line


def process(path, lines):
    findings = []
    for i, line in iter_prose_lines(lines):
        findings.extend(check_line(path, i + 1, line.rstrip("\n")))
    return findings


def main():
    ap = argparse.ArgumentParser(add_help=True, description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*", help="files to check, or - for stdin")
    ap.add_argument("--list", action="store_true", help="list rules and exit")
    ap.add_argument("--quiet", action="store_true", help="exit code only")
    args = ap.parse_args()

    if args.list:
        for rid, desc in sorted(RULES.items()):
            print("%s  %s%s" % (rid, desc,
                                "  [mechanisch]" if rid in MECHANICAL else "  [Urteil nötig]"))
        return 0
    if not args.files:
        ap.print_usage()
        return 2

    all_findings = []
    for path in args.files:
        if path == "-":
            lines = sys.stdin.read().splitlines(keepends=True)
            all_findings.extend(process("<stdin>", lines))
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                lines = fh.readlines()
        except OSError as exc:
            sys.stderr.write("%s: %s\n" % (path, exc))
            return 2
        all_findings.extend(process(path, lines))

    all_findings.sort(key=lambda f: (f.path, f.line, f.col))
    if not args.quiet:
        for f in all_findings:
            print(f)
        if all_findings:
            counts = {}
            for f in all_findings:
                counts[f.rule] = counts.get(f.rule, 0) + 1
            print("\n%d Hinweise: %s" % (
                len(all_findings),
                ", ".join("%s×%d" % (r, n) for r, n in sorted(counts.items()))))
            print("Hinweise, kein Urteil: im Kontext pruefen. Zitate, "
                  "Werktitel, Eigennamen und Code behalten ihre Schreibung.")
    return 1 if all_findings else 0


if __name__ == "__main__":
    sys.exit(main())
