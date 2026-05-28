# AGENTS.md

Guidance for AI coding agents (Claude Code, Codex, Warp, etc.) working in this repository.

## What this repo is

A portable agent skill implemented entirely as Markdown. The runtime artifact is `SKILL.md`: the agent reads its YAML frontmatter and editor prompt. There is no build step, and the repo should avoid wording that limits support to one or two harnesses.

## Key files

- `SKILL.md` — the skill itself. Portable YAML frontmatter (`name`, `description`, `license`, `metadata.version`) followed by the canonical, numbered pattern list with before/after examples. **This is the source of truth.**
- `README.md` — for humans: installation, usage, a summary table of the patterns, and a version history.
- `.claude-plugin/plugin.json` — optional Claude Code plugin manifest.
- `.claude-plugin/marketplace.json` — optional single-repo marketplace entry so `/plugin marketplace add blader/humanizer` works.
- `scripts/validate-package.py` — dependency-free package and synchronization checks used locally and in CI.

## The maintenance contract

`SKILL.md` and `README.md` must stay in sync. When you change behavior or content:

- **Patterns:** the skill currently defines **33 numbered patterns**. If you add, remove, or renumber any, update the README pattern table, its "N Patterns Detected" heading, and every cross-reference in the same change. Keep numbering stable unless you are deliberately renumbering.
- **Voice Calibration:** the skill supports two overrides to the default `PERSONALITY AND SOUL` voice: writing samples (Option A) and named presets (Option B, currently `neutral professional` and `academic`). Presets are not numbered patterns; they shift register and voice but do not change anti-pattern detection. If you add a new preset, update both SKILL.md (Option B section) and README.md (Voice Calibration section). Sample wins over preset when both are supplied.
- **Preset language scope:** all currently shipped presets are English-only. The register-specific rules under `neutral professional` derive from convergent English style guides (Google, Microsoft, Apple, IBM, GOV.UK, GitLab, Plain Language, Chicago) and explicitly do not apply to German, French, Spanish, or other languages where formal-writing conventions differ (e.g., German tolerates passive voice and nominalised constructions that English style guides reject). A non-English preset is a separate research effort: identify the convergent style-guide tradition for the target language (Duden + DIN 5008 + plain-government guidance for German; Académie + plain-French guidance for French; etc.), then add a sibling preset with its own scope statement. Do not auto-translate the English rules into another language.
- **Word-pair tables are illustrative, not authoritative.** The Avoid/Prefer table in the common-words rule is a starter set of the seven highest-frequency AI tells, not a maintained word list. The canonical sources are Microsoft Wordiness.yml (errata-ai/Microsoft on GitHub) and the Plain Language word-substitution lists at plainlanguage.gov. The skill points at these via `curl` and `WebFetch` examples; do not commit an expanded copy of either source into this repo, because both drift and a stale embedded copy is worse than a fresh fetch. If a new pair is genuinely common in AI output and missing from the canonical sources, file an issue first; only add to the local table if the source maintainers reject the addition.
- **Version:** `SKILL.md` frontmatter stores the version under `metadata.version`, `README.md` has a "Version History" section, and `.claude-plugin/plugin.json` has a `version` field. Bump them together so package metadata matches the skill. Keep the skill version under `metadata`; a top-level `version` key is not portable across Agent Skills hosts. (`marketplace.json` intentionally omits a version so `plugin.json` stays the package source of truth.)
- **Compatibility:** keep install and usage language harness-neutral. The skill should work in any agent harness that can load Markdown skill instructions; Claude Code, OpenCode, Codex, and other harnesses are examples, not limits.
- **Validation:** run `python3 scripts/validate-package.py`, `npx skills add . --list`, and `claude plugin validate .` before publishing.
- **Non-obvious fixes:** if you change the prompt to handle a tricky failure mode (a repeated mis-edit, an unexpected tone shift), add a short note to the README version history explaining what was fixed and why.

## Editing SKILL.md

- Preserve valid YAML frontmatter (formatting and indentation).
- The prompt below the frontmatter is the product. Edit it like a careful instruction document, not code.
