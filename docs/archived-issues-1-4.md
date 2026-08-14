# Archived issues #1-#4

These four issues were closed and then deleted from GitHub on 14 August 2026,
after their contents had been triaged item by item. Deletion is permanent, so
the full text is preserved here rather than lost.

What survived the triage:

- The HIX target problem became issue #8, sharpened in the process: the section
  claims a five-band scale where the source gives two reference points, and sets
  a target for a register the index was never validated on.
- The German pattern work became issues #5 (§31), #6 (§33) and #7 (worked
  example transformation).
- The fork architecture note went into `~/.claude/CLAUDE.md`, outside this repo,
  because its readers are sessions that never open the repo.
- Preset versioning, the klartext spot-check, the §14 dash conflict and the
  Wikipedia revision pin were done during the same session; see the git history
  around 7d8cc12, 02bf48b, 574dcd3 and 7698de9.

Deliberately dropped, with reasons recorded in the session: distribution beyond
this machine (clone plus symlink is already the whole install), a running log of
misfires from daily use, the AI-iness density pre-check (would collide with the
German Quick-Check), an upstream pull request for the em dash in §26, and the
remaining cherry-pick and research candidates listed in #2 and #3.

---

# Archiv: Issues #1-#4 aus michaelstingl/humanizer

Gesichert am 2026-08-14 vor dem Löschen. Enthält Bodies und alle Kommentare.



---

## #1 Merge upstream v2.9.1 into feature/voice-presets

angelegt 2026-08-14T17:54 von michaelstingl, Status open

`feature/voice-presets` is seven commits behind `main` (now at upstream v2.9.1). The branch carries the voice-preset system, the German preset and `de_typo_lint.py`; upstream has since added three patterns, moved the version into `metadata`, and added packaging plus a validation script.

Numbering lines up: §30 is `Diff-Anchored Writing` on both sides, upstream appends §31 to §33. No renumbering needed.

## What upstream brings

| Version | Content |
|---|---|
| v2.8.0 | §31 Manufactured Punchlines, §32 Aphorism Formulas, §33 Conversational Rhetorical Openers |
| v2.8.3 | Frontmatter: `version:` moves to `metadata.version`; a top-level key is not portable across hosts |
| v2.9.0 | No-fabrication rule, invocation modes |
| v2.9.1 | `.claude-plugin/plugin.json`, `marketplace.json`, `scripts/validate-package.py`, CI workflow, harness-neutral wording |

## Conflicts

Four blocks, two of them trivial.

- **`SKILL.md` §26** — upstream uses an em dash where this branch uses a comma. Keep the comma: §14 asks for exactly that.
- **`SKILL.md` Voice Calibration** — upstream reworked Option A, this branch added Option B below it. Take upstream's Option A, keep Option B.
- **`AGENTS.md`, two blocks** — upstream describes frontmatter, pattern count, validation and harness neutrality; this branch describes the preset system. Merge both, do not choose.

## Decisions

- [ ] Drop `compatibility: claude-code opencode` from the frontmatter. Upstream deliberately names no harness.
- [ ] Set one version across `metadata.version`, `.claude-plugin/plugin.json` and the README version history.
- [ ] Replace "§1 through §30" with "§33" in four places: `SKILL.md` twice, `AGENTS.md` twice.
- [ ] Decide how the German preset relates to the new patterns. §32 overlaps with "Keine Aphorismen als Absatzschluss", §33 with "Kein Signposting an den Leser". Either the preset references the pattern numbers, or the duplication stays on purpose.
- [ ] `python3 scripts/validate-package.py` has to pass.

## Separate defect on this branch

In `SKILL.md`, the paragraph about `de_typo_lint.py` sits inside the preset table, between the German row and the academic row. The table breaks there and the academic row renders as text.

## Suggested order

1. Fix the broken table first, so the merge does not carry it along.
2. `git merge main`, resolve the four blocks.
3. Renumber the references, set the version, drop `compatibility`.
4. `python3 scripts/validate-package.py`, then read `--help` output and the preset routing once end to end.



### Kommentar von michaelstingl, 2026-08-14T17:57

## Done, with two deviations from the plan

The merge is complete and pushed. Every checklist item above is resolved.

**Deviation 1: rebase instead of merge.** The branch was rebased onto `origin/main` rather than merged. Six conflict rounds instead of the four blocks predicted here, but the same substance and the same resolutions: upstream's Option A kept, Option B preserved on top, the §26 comma kept over upstream's em dash, both `AGENTS.md` blocks merged rather than chosen between.

One resolution deserves recording because it is a policy, not a one-off. Upstream cut 242 lines from `SKILL.md` in v2.9.1 for portability, including the long Voice Calibration bullet list. Their condensed version was kept and the preset layer rebuilt on top of it, rather than restoring the old list. Restoring it would have reproduced this same conflict at every future sync. That rule is now written into `AGENTS.md`.

**Deviation 2: the branch in the title no longer exists.** `feature/voice-presets` had been sitting unmerged since 28 May with no PR, while the symlinked skill ran from it. A stray `git checkout main` would have silently stripped 716 lines from the live skill. The layout is now:

- `main` — default branch, this fork's version, what the skill actually runs from
- `upstream-main` — clean mirror of `blader/humanizer`, tracks `origin/main`

`feature/voice-presets` and the pre-rebase backup branch are deleted. Syncs are now `git merge upstream-main` into `main`.

## Checklist

- [x] `compatibility:` dropped from frontmatter (upstream's frontmatter adopted wholesale)
- [x] One version across `metadata.version`, `plugin.json`, README history: 2.9.1 everywhere, no bump
- [x] "§1 through §30" replaced. Note the count here was low: it was eight occurrences across five files, not four
- [x] German preset related to the new patterns, see below
- [x] `python3 scripts/validate-package.py` passes
- [x] Broken preset table fixed, found independently before the merge. The duplicated fallback sentence about unrecognised preset names was removed at the same time
- [x] `--help` output and preset routing read end to end

## Item 4 needs a correction, including to this issue

The mapping proposed here is wrong in one place, and the note written during the sync was wrong in another. Per pattern:

**§32 Aphorism Formulas: already partly covered.** The preset's "Keine Aphorismen als Absatzschluss" reaches the same tell in closing position, sourced from `humanizer-de` and arrived at independently of the English catalog. The gap is narrower than assumed: §32's wider formula family ("X ist die Sprache des Y", "X wird zur Falle") anywhere in a paragraph. The existing rule should be extended, keeping its German citation, rather than a second rule added.

**§33 Conversational Rhetorical Openers: no overlap with "Kein Signposting an den Leser".** These are different tells. §33 is the fake-candid hook ("Honestly?", "Here's the thing"). The German signposting rule corresponds to **§28 Signposting and Announcements**, which predates v2.8.0. §33 remains the doubtful one for transfer: the nearest German candidates ("Ganz ehrlich:", "Sagen wir es so:") sit in a more casual register than this preset targets, so it is worth checking whether the tell exists in German technical prose at all before writing a rule for it.

**§31 Manufactured Punchlines: not covered.** The Rhythmus section addresses the opposite failure, uniform sentence length, and explicitly permits long German sentences. A run of short declaratives staged for drama is a separate tell and still missing.

Both affected German rules now name the upstream pattern they correspond to, so the mapping is visible in the file instead of being re-derived at each sync. The remaining gaps are listed individually under "Open questions for the next research round".

## Also landed, outside this issue's scope

- **`NOTICE` added.** The pattern material adapts the English and German Wikipedia project pages, which are CC BY-SA 4.0, not MIT. That is now recorded with revision-history links and a description of the changes, alongside a second copyright line in `LICENSE` for the preset layer. Side effect worth knowing: GitHub's licence detector no longer matches the MIT template exactly and reports `NOASSERTION`, the same as `marmbiz/humanizer-de`, which carries plain MIT for the same reason.
- **Upstream's fork policy recorded in `AGENTS.md`.** Per blader/humanizer#163, localized variants stay separate community repositories. This fork is permanent and not a staging area for upstream PRs. Noted there so the question is not reopened.
- **Three facts corrected in the German preset's source block.** `humanizer-de` is at v5.19.0 and is not a GitHub fork of blader but an independent repository deriving parts from it; `klartext` has been dormant since April 2026; `txtHumanizer`'s README example fabricates figures and company details, which makes it unusable as a model under the no-fabrication rule added in v2.9.0.

## Still open

No worked example transformation exists for the German preset, and none can be borrowed. A survey of the German-language sources found that none of them has one either: not Wikipedia:DE (revision of 5 July 2026), not `humanizer-de` across its 63 KB README and `de-naturalness.md`, not its 27 test scenarios, which give inputs and pass conditions but no rewritten output. The longest German before/after material anywhere is two sentences long, and the `humanizer-de` examples carry CC BY-SA rather than MIT.

So the example has to be built here: an AI-typical German passage rewritten strictly by the preset's own rules, with every edit annotated by rule and source code. That keeps it derivable rather than invented, and gives `de_typo_lint.py` its first fixture.



### Kommentar von michaelstingl, 2026-08-14T18:00

Two items from a review of the merged `main`. Both are for you; I am not touching the repo.

## 1. The live skill is still running the pre-merge version

The working tree that `~/.claude/skills/humanizer` symlinks to is still checked out on `feature/voice-presets`. That branch is deleted on the remote, so the checkout is orphaned and `main` is 18 commits ahead of the local copy.

Every invocation of the skill right now loads the old `SKILL.md`: no §31 to §33, the old frontmatter, and the broken preset table. The merge is done but not in effect.

```
git checkout main && git pull --ff-only
```

Worth checking whether any other checkout points at the deleted branch.

## 2. §14 and the German dash rule contradict each other, and the sample rule decides it the wrong way

Three statements in the merged `main` cannot all hold for German text.

`SKILL.md:201` — "The final rewrite contains no em dashes (—) or en dashes (–)."
`SKILL.md:211` — "scan it for `—` and `–`. Any hit means the draft isn't done."
`references/preset-neutral-professional-de.md` — the German Gedankenstrich **is** the en dash with spaces; every em dash in German prose is an English-typography import.

So §14 forbids the glyph that German typography requires, and its final scan rejects a correct German rewrite. The preset says "the dash rule inverts", but §14 states its ban in absolute terms and the scan is written as a hard gate.

On top of that, v2.9.0 added at `SKILL.md:41`:

> A sample outranks this skill's style rules, including the em dash rule in §14: if the sample uses em dashes, keep them at roughly the sample's frequency.

For English that is sound: the em dash is a style preference there. For German it is not a preference but a wrong character. Since a sample outranks a preset, a German sample containing `—` currently makes the rewrite reproduce the error at the author's frequency.

The German preset mentions neither rule. Suggested resolution:

- Scope §14's ban and its final scan to English, or state the German exception in §14 itself so the gate does not fire on `–`.
- Add the sample case to the German preset: a sample governs rhythm, register and vocabulary, but not glyphs. Typography follows the norm, not the sample.
- If that is accepted, `de_typo_lint.py` stays valid as written; if not, it will contradict §14 on every German file it checks.

Observed in practice today: a German documentation pass under this preset replaced `—` with `–` throughout, which §14's scan would have rejected as unfinished.

## Not reviewed

`agents/openai.yaml` names no preset. Probably correct, since the presets are requested by name at invocation time, but nobody has confirmed it.



---

## #2 Cherry-pick candidates from upstream pull requests

angelegt 2026-08-14T18:04 von michaelstingl, Status open

Candidates from closed pull requests in `blader/humanizer`, kept here because the maintainer's stated position is that one-paragraph rules win over taxonomies, so several of these will not land upstream and are ours to adopt or drop.

| Priority | PR | What | Effort |
|---|---|---|---|
| high | #115 adelaidasofia | AI-iness density pre-check: tier-1 tells per 100 words, pass strength light/mixed/full | ~41 lines in `SKILL.md` |
| medium | #108 bdevz | Citation, fair-use quote and cross-references per rule | polish pass over every rule |
| low | #116 AnthonyDavidAdams | Debunking-pose headings as an explicit heading scan | small, in `preset-neutral-professional-en.md` |
| later | #124 edonadei | Caliper eval suite | medium, external dependencies |
| not now | #111 philippdubach | Era-aware vocabulary | ages fast |

**#117 CoveMB (Factual Integrity Hard Rule) is done.** Upstream landed the substance in v2.9.0 as the no-fabrication rule. Nothing to cherry-pick.

## Note on #115

If adopted, the density pre-check belongs in `SKILL.md` and not in a preset: it is language-independent. The German preset already has a Quick-Check of its own, taken from `klartext`; the two would need reconciling so a German pass does not run two pre-checks.

## Possible small PRs back upstream

- Connector clustering as a language-independent pattern. It covers German "darüber hinaus" and English "furthermore" alike.
- Patterns present in the German Wikipedia page that the English one lacks, where they survive translation.

One resolution from the merge is a candidate too: `SKILL.md` §26 uses an em dash in a sentence explaining a rule, which §14 forbids. This fork carries a comma there.

## Stale, needs re-checking

The note that §31 was contested between #126 and #127 predates v2.8.0. Upstream's §31 is now "Manufactured Punchlines", which is neither. Both PRs need looking at again before this is worth anything.



### Kommentar von michaelstingl, 2026-08-14T18:19

## The stale §31 note, resolved

Checked both pull requests. They are not two takes on one pattern, and one of them is no longer a candidate.

**#126 "Add §31 conversational rhetorical openers; extend §20 with offer-to-continue closers" — landed upstream, nothing to cherry-pick.** Its substance shipped in v2.8.0. The release commit names exactly this material: "three style/cadence patterns from the remaining PRs: manufactured punchlines, aphorism formulas, and conversational rhetorical openers", plus "Extend the chatbot artifact rule to catch offer-to-continue closers". The openers are now **§33**, not §31, and the closers went into §20 as proposed. Both are in this fork since the v2.9.1 merge.

**#127 "Add pattern 31: reference-markup artifacts" — did not land, still a candidate.** Unrelated to #126 beyond having claimed the same number at the time. It should be assessed on its own merits rather than as the loser of a contest that never happened.

Upstream's §31 today is "Manufactured Punchlines and Staccato Drama", which is neither PR. The numbering collision is what made the two look related.

Suggested edit to the table above: drop the #126 row, keep #127 as a separate low-priority candidate with its actual subject.

## While checking this

**#116 debunking-pose headings is more expensive than "low / small".** The rule itself is small, but `AGENTS.md` requires a bracket code per rule in the preset files, and `preset-neutral-professional-en.md` cites a style guide for every rule it carries. An upstream pull request is not a style guide. Adopting #116 means first finding whether Microsoft, Google, GOV.UK or Chicago say anything about posing headings, and if none of them do, the rule does not go in as written. Re-estimating it as research, not as a cherry-pick.

**Item 4 of #1 produced one adoption.** A spot-check of klartext's seven German-specific patterns found six covered and one missing: abstract container words ("Aspekt", "Bereich", "Rahmen") standing where the concrete thing belongs. `humanizer-de` carries the same pattern independently, so it rests on two German sources and needed no transferability check. Added in 02bf48b, with a carve-out for "Faktor" and "Komponente" as fixed technical terms.



---

## #3 German preset: from draft v0.3 to v1.0

angelegt 2026-08-14T18:04 von michaelstingl, Status open

`references/preset-neutral-professional-de.md` is at draft v0.3. What v1.0 requires.

## Blocking

- [ ] **A worked example transformation.** The preset has rules and sources but no before/after. None can be borrowed: the survey recorded in #1 found that no German-language source has one either, and the longest German before/after material anywhere is two sentences. It has to be built here: an AI-typical German passage rewritten strictly by the preset's own rules, every edit annotated by rule and source code. That also gives `de_typo_lint.py` its first fixture.
- [ ] **Validate the HIX target** against a corpus of German technical documentation. No existing dataset was found, so the corpus has to be assembled first.
- [ ] **Spot-check the klartext patterns**: are all seven starred tells in our list?
- [ ] **Cover the remaining upstream patterns.** Per the mapping in #1: §31 Manufactured Punchlines has no German counterpart yet, and §33 Conversational Rhetorical Openers may not transfer at all. Check whether the tell exists in German technical prose before writing a rule for it.

## Research, unordered

- [ ] Cross-check Duden-Mentor output against our rules
- [ ] Work through the DIN SPEC 33429 rule set (Leichte Sprache) for what transfers
- [ ] Extract concrete word substitutions from the federal plain-German guidance
- [ ] Consider txtHumanizer's three-stage workflow (analyse, recommend, finetune) as an optional mode. Caveat recorded in #1: its README example fabricates figures, which makes it unusable as a model under the no-fabrication rule.
- [ ] Build a German test corpus from our own texts, before and after AI editing, for regression tracking
- [ ] Watch the German Wikipedia page for changes since our snapshot. A diff routine would make this cheap.

## Open conflict, tracked in #1

§14 forbids the en dash outright while the German preset requires it, and a writing sample outranks §14. Until that is resolved, a German rewrite that is typographically correct fails the §14 scan.



### Kommentar von michaelstingl, 2026-08-14T18:19

Two items off this list.

**"Spot-check the klartext patterns: are all seven starred tells in our list?" — done, six of seven were.** The gap was Muster 13, abstract container words ("Aspekt", "Bereich", "Rahmen") standing where the concrete thing belongs. The near-miss was "im Rahmen der Umsetzung", which appeared here only as an example inside the Genitivketten rule. `humanizer-de` carries the same pattern independently as "Abstrakta", so the new rule rests on two German sources and needed no transferability check. Added in 02bf48b with a carve-out: in technical prose "Faktor" and "Komponente" are often terms with fixed meaning and stay. The coverage result is recorded in the klartext source entry so nobody repeats the check.

**"Open conflict, tracked in #1" — resolved in 574dcd3.** §14 is now scoped to English, and its closing scan takes a second exception: under a preset that states a typographic norm, the preset wins, so a German pass scans for `—` alone and leaves `–` in place. The sample rule from v2.9.0 is settled in the same edit, and against the direction it pointed: a sample governs rhythm, register and vocabulary, not glyphs. A German sample full of em dashes reproduces an error rather than expressing a voice. The full statement lives in the preset's Typografie section, which the Divergence bullet points at.

No change was needed in `de_typo_lint.py` or the German Quick-Check. Both already looked for the em dash alone, so the tooling was right and the skill's own gate was the part that was wrong.

**This unblocks the worked example.** It was blocked in a way worth naming: the example will necessarily contain Halbgeviertstriche, so writing it before this fix would have produced a showcase that the skill's own closing scan rejected as unfinished.



---

## #4 Fork operations: preset versioning, distribution, documentation

angelegt 2026-08-14T18:04 von michaelstingl, Status open

Operational questions about running this fork, none of them about pattern content.

## Preset architecture

- [ ] **Give each preset its own `version` in its frontmatter.** Today only the skill carries a version (2.9.1), so the German preset's draft status lives in prose at the top of the file. `validate-package.py` would need to know about the new field.
- [ ] **Cross-link the preset files.** The German preset has a divergence section pointing at the English rules; the English one does not point back.

## Distribution

`~/.claude/skills/humanizer` is a symlink into a clone of this fork, now on `main`. That works for one machine and one account.

- [ ] Decide how the skill reaches other machines or accounts: a dotfiles repository, a marketplace entry through the `.claude-plugin` manifests that v2.9.1 added, or an npx-style package.

The manifests are already in the repository, so the marketplace route may be closest.

## Documentation

- [ ] **Write a memory note about this fork**, in the shape of the existing `reference_capability-gate.md`: fork architecture, the symlink, which branch is live, where the presets are, and how a new preset is added. The branch layout changed during the merge in #1, which is exactly the kind of fact that needs recording somewhere durable.

## Observations to collect during everyday use

Nothing to decide yet; these need data first.

- [ ] Which of the numbered patterns fire daily, which never?
- [ ] Which `neutral professional` rules get ignored in practice?
- [ ] Which German patterns over- or under-trigger?
- [ ] How often is the skill run against text that was already human-written, and what happens?

