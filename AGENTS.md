# AGENTS.md

Guidance for AI coding agents (Claude Code, Codex, Warp, etc.) working in this repository.

## What this repo is

A portable agent skill implemented entirely as Markdown. The runtime artifact is `SKILL.md`: the agent reads its YAML frontmatter and editor prompt. There is no build step, and the repo should avoid wording that limits support to one or two harnesses.

## Relationship to upstream

This repository is a permanent fork of [blader/humanizer](https://github.com/blader/humanizer), not a staging area for pull requests against it. Upstream has ruled on this explicitly. Closing the French adaptation's policy question in [issue #163](https://github.com/blader/humanizer/issues/163) (June 2026), the maintainer wrote:

> I prefer localized variants to remain separate community repositories so each language can evolve without adding duplicate runtime authorities here. Humanizer-fr is the right shape, so I am closing this policy question with appreciation.

Later language requests follow that shape by default; issues [#194](https://github.com/blader/humanizer/issues/194) and [#203](https://github.com/blader/humanizer/issues/203) propose Chinese adaptations as separate repos in their titles. The ecosystem around this skill is forks, by design.

Consequences for anyone working here:

- **Do not prepare pull requests to upstream for language or register work, and do not propose them.** The answer is already on record.
- The German preset and `scripts/de_typo_lint.py` live here permanently. Peer projects occupy the same niche independently: `marmbiz/humanizer-de` (the most developed, actively released), `ferr079/humanizer-fr`, `LangeVC/txtHumanizer`. See the Sources block in the German preset for how they relate.
- One thing the policy does *not* cover: the English preset layer (`preset-neutral-professional-en.md`, `preset-academic-en.md`) is register calibration, not localization, so upstream has never been asked about it. Do not assume either answer.

Branch layout follows from this:

- `main` — the default branch and the version actually used. Upstream plus the preset layer.
- `upstream-main` — a clean mirror of `blader/humanizer`, tracking `origin/main`.

To take upstream changes: `git checkout upstream-main && git pull`, then `git checkout main && git merge upstream-main`. Resolve conflicts in favour of upstream for anything upstream owns (pattern numbering, packaging metadata, frontmatter), and in favour of this fork for the preset layer. Where upstream restructures a section this fork extends, adopt their structure and re-apply the extension on top rather than restoring the old shape, or the same conflict returns at every sync.

## Key files

- `SKILL.md` — the skill itself. Portable YAML frontmatter (`name`, `description`, `license`, `metadata.version`) followed by the canonical, numbered pattern list with before/after examples, the default `PERSONALITY AND SOUL` voice, and Voice Calibration routing. **This is the source of truth for universal patterns.**
- `references/preset-<name>-<lang>.md` — one file per named voice preset (`neutral professional` EN/DE, `academic` EN). Each file is self-contained: voice mode, language scope, register-specific rules, sources, and example transformation. SKILL.md routes the user request to the matching file. Reference files do not repeat §1 through §33; those apply universally on top of every preset.
- `README.md` — for humans: installation, usage, a summary table of the patterns, and a version history.
- `.claude-plugin/plugin.json` — optional Claude Code plugin manifest.
- `.claude-plugin/marketplace.json` — optional single-repo marketplace entry so `/plugin marketplace add blader/humanizer` works.
- `scripts/validate-package.py` — dependency-free package and synchronization checks used locally and in CI.

## The maintenance contract

`SKILL.md` and `README.md` must stay in sync. When you change behavior or content:

- **Patterns:** the skill currently defines **33 numbered patterns**. If you add, remove, or renumber any, update the README pattern table, its "N Patterns Detected" heading, and every cross-reference in the same change. Keep numbering stable unless you are deliberately renumbering.
- **Voice Calibration:** the skill supports two overrides to the default `PERSONALITY AND SOUL` voice: writing samples (Option A) and named presets (Option B). Presets are not numbered patterns; they shift register and voice but do not change anti-pattern detection. Sample wins over preset when both are supplied.
- **Preset files live in `references/`.** SKILL.md routes the user request to the matching reference file. Each reference file is self-contained: voice mode, language scope, register-specific rules, sources, example transformation. The numbered patterns §1 through §33 in SKILL.md apply on top of every preset and are not repeated in reference files.
- **Adding a new preset:** create `references/preset-<name>-<lang>.md` following the structure of `preset-neutral-professional-en.md`, starting with the frontmatter block (`preset`, `lang`, `version`, `status`). The filename must follow from `preset` and `lang`. Add a row to the routing table in SKILL.md (Option B section) and to the table in README.md (Voice Calibration section). Do not move §1 through §33 into reference files; they stay universal.
- **Preset status and version live in the preset's frontmatter, and nowhere else as a source.** A `draft` preset must be marked as draft with its version in both tables, so the choice is never made without knowing the rules are provisional. `scripts/validate-presets.py` enforces this; before it existed the status was maintained by hand in five places. Prose version history inside a preset file is a changelog and is left alone.
- **Preset language scope:** the EN presets derive from convergent English style guides (Google, Microsoft, Apple, IBM, GOV.UK, GitLab, Plain Language, Chicago) and explicitly do not transfer to other languages (e.g., German tolerates passive voice and nominalised constructions that English style guides reject). A non-English preset is a separate research effort: identify the convergent style-guide tradition for the target language (Duden + DIN 5008 + BAMF plain-Deutsch for German; Académie + plain-French guidance for French; etc.) and add a sibling reference file with its own scope statement. Do not auto-translate the English rules into another language. The `neutral professional de` preset is at draft v0.3: German sources lead, English sources are admitted only for mechanism and only after a documented transferability check, no imported English thresholds, and the em-dash rule inverts. See `references/preset-neutral-professional-de.md` for source plan and divergence notes.
- **Word-pair tables are illustrative, not authoritative.** The Avoid/Prefer table in the common-words rule (in `preset-neutral-professional-en.md`) is a starter set of the seven highest-frequency AI tells, not a maintained word list. The canonical sources are Microsoft Wordiness.yml (errata-ai/Microsoft on GitHub) and the Plain Language word-substitution lists at plainlanguage.gov. The reference file points at these via `curl` examples; do not commit an expanded copy of either source into this repo, because both drift and a stale embedded copy is worse than a fresh fetch. If a new pair is genuinely common in AI output and missing from the canonical sources, file an issue first; only add to the local table if the source maintainers reject the addition.
- **Version:** `SKILL.md` frontmatter stores the version under `metadata.version`, `README.md` has a "Version History" section, and `.claude-plugin/plugin.json` has a `version` field. Bump them together so package metadata matches the skill. Keep the skill version under `metadata`; a top-level `version` key is not portable across Agent Skills hosts. (`marketplace.json` intentionally omits a version so `plugin.json` stays the package source of truth.)
- **Compatibility:** keep install and usage language harness-neutral. The skill should work in any agent harness that can load Markdown skill instructions; Claude Code, OpenCode, Codex, and other harnesses are examples, not limits.
- **Validation:** run `python3 scripts/validate-package.py` and `python3 scripts/validate-presets.py`, then `npx skills add . --list` and `claude plugin validate .` before publishing. The two validators are deliberately separate: the first is upstream's and owns the skill package, the second is this fork's and owns the preset layer. Keeping them apart means an upstream sync cannot collide with our checks.
- **Non-obvious fixes:** if you change the prompt to handle a tricky failure mode (a repeated mis-edit, an unexpected tone shift), add a short note to the README version history explaining what was fixed and why.

## Editing SKILL.md

- Preserve valid YAML frontmatter (formatting and indentation).
- The prompt below the frontmatter is the product. Edit it like a careful instruction document, not code.
