# AGENTS.md

Guidance for AI coding agents (Claude Code, Codex, Warp, etc.) working in this repository.

## What this repo is

A portable agent skill implemented entirely as Markdown. The runtime artifact is `SKILL.md`: the agent reads its YAML frontmatter and editor prompt. There is no build step, and the repo should avoid wording that limits support to one or two harnesses.

## Key files

- `SKILL.md` — the skill itself. Portable YAML frontmatter (`name`, `description`, `license`, `metadata.version`) followed by the canonical, numbered pattern list with before/after examples, the default `PERSONALITY AND SOUL` voice, and Voice Calibration routing. **This is the source of truth for universal patterns.**
- `references/preset-<name>-<lang>.md` — one file per named voice preset (`neutral professional` EN/DE, `academic` EN). Each file is self-contained: voice mode, language scope, register-specific rules, sources, and example transformation. SKILL.md routes the user request to the matching file. Reference files do not repeat §1 through §30; those apply universally on top of every preset.
- `README.md` — for humans: installation, usage, a summary table of the patterns, and a version history.
- `.claude-plugin/plugin.json` — optional Claude Code plugin manifest.
- `.claude-plugin/marketplace.json` — optional single-repo marketplace entry so `/plugin marketplace add blader/humanizer` works.
- `scripts/validate-package.py` — dependency-free package and synchronization checks used locally and in CI.

## The maintenance contract

`SKILL.md` and `README.md` must stay in sync. When you change behavior or content:

- **Patterns:** the skill currently defines **33 numbered patterns**. If you add, remove, or renumber any, update the README pattern table, its "N Patterns Detected" heading, and every cross-reference in the same change. Keep numbering stable unless you are deliberately renumbering.
- **Voice Calibration:** the skill supports two overrides to the default `PERSONALITY AND SOUL` voice: writing samples (Option A) and named presets (Option B). Presets are not numbered patterns; they shift register and voice but do not change anti-pattern detection. Sample wins over preset when both are supplied.
- **Preset files live in `references/`.** SKILL.md routes the user request to the matching reference file. Each reference file is self-contained: voice mode, language scope, register-specific rules, sources, example transformation. The numbered patterns §1 through §30 in SKILL.md apply on top of every preset and are not repeated in reference files.
- **Adding a new preset:** create `references/preset-<name>-<lang>.md` following the structure of `preset-neutral-professional-en.md`. Add a row to the routing table in SKILL.md (Option B section) and to the table in README.md (Voice Calibration section). Do not move §1 through §30 into reference files; they stay universal.
- **Preset language scope:** the EN presets derive from convergent English style guides (Google, Microsoft, Apple, IBM, GOV.UK, GitLab, Plain Language, Chicago) and explicitly do not transfer to other languages (e.g., German tolerates passive voice and nominalised constructions that English style guides reject). A non-English preset is a separate research effort: identify the convergent style-guide tradition for the target language (Duden + DIN 5008 + BAMF plain-Deutsch for German; Académie + plain-French guidance for French; etc.) and add a sibling reference file with its own scope statement. Do not auto-translate the English rules into another language. The `neutral professional de` preset is currently in research stage; see `references/preset-neutral-professional-de.md` for source plan and divergence notes.
- **Word-pair tables are illustrative, not authoritative.** The Avoid/Prefer table in the common-words rule (in `preset-neutral-professional-en.md`) is a starter set of the seven highest-frequency AI tells, not a maintained word list. The canonical sources are Microsoft Wordiness.yml (errata-ai/Microsoft on GitHub) and the Plain Language word-substitution lists at plainlanguage.gov. The reference file points at these via `curl` examples; do not commit an expanded copy of either source into this repo, because both drift and a stale embedded copy is worse than a fresh fetch. If a new pair is genuinely common in AI output and missing from the canonical sources, file an issue first; only add to the local table if the source maintainers reject the addition.
- **Version:** `SKILL.md` frontmatter stores the version under `metadata.version`, `README.md` has a "Version History" section, and `.claude-plugin/plugin.json` has a `version` field. Bump them together so package metadata matches the skill. Keep the skill version under `metadata`; a top-level `version` key is not portable across Agent Skills hosts. (`marketplace.json` intentionally omits a version so `plugin.json` stays the package source of truth.)
- **Compatibility:** keep install and usage language harness-neutral. The skill should work in any agent harness that can load Markdown skill instructions; Claude Code, OpenCode, Codex, and other harnesses are examples, not limits.
- **Validation:** run `python3 scripts/validate-package.py`, `npx skills add . --list`, and `claude plugin validate .` before publishing.
- **Non-obvious fixes:** if you change the prompt to handle a tricky failure mode (a repeated mis-edit, an unexpected tone shift), add a short note to the README version history explaining what was fixed and why.

## Editing SKILL.md

- Preserve valid YAML frontmatter (formatting and indentation).
- The prompt below the frontmatter is the product. Edit it like a careful instruction document, not code.
