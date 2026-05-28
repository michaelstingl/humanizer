# Voice preset: `neutral professional` (Deutsch). Research in progress.

**Status:** Stub. The full rule set for German neutral-professional writing has not been compiled against the source guides yet. The orientation points below are widely-known starting positions for German formal writing; the binding rule set will follow once the canonical style guides have been reviewed.

Loaded by SKILL.md when the user requests "neutral professional de" or "neutrales Deutsch" or equivalent. The numbered patterns §1 through §30 in SKILL.md still apply unchanged where language-independent (em dashes, rule-of-three, slogan closures, knowledge-cutoff disclaimers, sycophantic tone, etc.). The English `neutral professional` register rules from `preset-neutral-professional-en.md` do **not** apply here: see the divergence section below for why.

## Scope: German (de)

This preset targets German neutral-professional prose: technical READMEs, API documentation, internal write-ups, vendor-facing documents, RFC-like specifications written in German. It does not target citizen-facing public-service German (Bürgersprache), which has its own stricter conventions, nor literary or marketing German.

## Sources to consult (TODO)

The full rule set must be compiled from convergent guidance across the German equivalents of the English style guides used for the EN preset:

- **Duden Ratgeber** (Briefe und E-Mails, Stil-Wörterbuch, Sprachratgeber). Reference for formal German correspondence and accepted register markers.
- **DIN 5008** (Schreib- und Gestaltungsregeln für die Text- und Informationsverarbeitung). Binding standard for German business correspondence formatting and addressing.
- **Bundesregierung Plain-Deutsch initiatives** ("Bürgernahe Sprache", BAMF-Sprachratgeber). Counterpart to plainlanguage.gov for German government writing.
- **Übersetzungsleitfaden der Europäischen Kommission** (DE). Convergent German bureaucratic-formal rules from EU translation practice.
- **Wikipedia DE Schreibwerkstatt / Wikipedia:Schreibwerkstatt**. Convergent encyclopaedic German neutral-tone guidance, including the German-language "Wie schreibe ich gute Artikel" and the German equivalent of the Wikipedia "Signs of AI writing" page.
- **Klartext-Initiative der Universität Hohenheim** (Verständlichkeitsforschung, Hohenheimer Verständlichkeitsindex). Quantitative German readability scoring, German analogue to Flesch-Kincaid.

## Divergence from English preset (do not auto-translate)

These differences are documented well enough to assert now. They explain why the English rules cannot be carried over wholesale.

- **Passive voice is acceptable** in formal German. "Die Tabelle wird erstellt", "Es wird empfohlen, dass..." are idiomatic, not AI tells. The English "active voice as default" rule does not transfer.
- **Nominalstil is idiomatic** in formal German. "Die Durchführung der Konfiguration erfolgt..." is standard register, not bloat. The English "no nominalised verbs" rule does not transfer; in fact the opposite tendency (Verb-Stil) can read as colloquial or under-formal in German specifications.
- **Compound nouns (Komposita) are expected.** "Datenbankzugriffskonfiguration" is one word, not three. Do not break compounds apart in pursuit of Anglo-Saxon brevity.
- **Hedging via Konjunktiv is legitimate.** "Es wäre zu prüfen", "könnte ergänzt werden" are accepted formal-German constructions, not slop tells. The Konjunktiv I and Konjunktiv II carry epistemic and reportative semantics that English modals do not match cleanly.
- **Address mode is Sie / impersonal.** Formal German uses "Sie" for the reader or impersonal constructions ("Man unterscheidet", "Es ist zu beachten"). "Du" is appropriate only for internal team documents or genuinely casual contexts. The English "you" rule maps to "Sie", not to "du".
- **Bandwurmsätze** (long compound sentences) tolerate higher word counts than English. The Plain-Language 15-20-word target does not transfer directly. German formal writing routinely uses 25-35-word sentences without losing clarity, provided the structure is parallel and the Verbklammer holds.

## Likely-to-survive rules from the English preset

Some EN register rules are likely to survive the DE research because they target patterns that show up in both languages with similar AI-tell character. These are candidates, not confirmed:

- No filler intensifiers in German equivalents: "einfach", "ganz einfach", "schlichtweg", "schlicht und einfach" probably warrant the same scepticism as English "simply / easily / just".
- No promotional adjectives without measurable backing: "robust", "umfassend", "leistungsstark", "skalierbar", "elegant" without metric backing are equally hollow.
- No vague behavioural verbs in specifications: "gewährleistet", "ermöglicht", "unterstützt", "bietet" hide the mechanism in German specs just as "ensures / enables / supports / provides" do in English.
- Specification-verb whitelist: German formal documents use "MUSS", "SOLL", "DARF NICHT" with the same RFC-2119-style semantics; treat them as load-bearing.

## Fallback behaviour until the full preset ships

If a user invokes `neutral professional de` before the full research lands:

1. Apply the universal §1 through §30 numbered patterns from SKILL.md.
2. Apply the "Divergence from English preset" rules above as guardrails (do not strip passive, do not break Komposita, do not flatten Nominalstil).
3. Apply the "likely-to-survive" rules with low confidence; flag any rewrites in those areas for review.
4. Note in the response that the German preset is in research stage and that an EN-side preset would have produced a different output.

A short fallback message template for the response:

> Der `neutral professional (de)`-Preset befindet sich in der Recherchephase. Der vollständige Regelsatz wird gerade gegen Duden, DIN 5008, BAMF und vergleichbare Quellen kompiliert. Bis dahin wirken nur die universellen §1 bis §30 Anti-Muster aus SKILL.md sowie ein paar dokumentierte deutsch-spezifische Schutzregeln. Für eine vollständig kalibrierte Überarbeitung empfiehlt sich entweder ein deutsches Schreibmuster als Stilreferenz (Option A) oder das Warten auf den fertigen Preset.

## Open questions for the research phase

- Are there published German-language analogues to the Wikipedia "Signs of AI writing" guide? (Wikipedia:WikiProjekt KI und Wikipedia / Erkennung KI-Einsatz, partially available, needs full extraction.)
- How does the Hohenheimer Verständlichkeitsindex compare with Flesch-Kincaid as a register target? What index value corresponds to "neutral-professional technical German"?
- Are there discipline-specific German style guides that should be acknowledged the way [syq-cmdi/Academic-DeAI](https://github.com/syq-cmdi/Academic-DeAI) is acknowledged in the academic preset?
- What is the German equivalent of Microsoft's Wordiness.yml? Does any community-maintained machine-readable word-substitution list exist?
- Should the DE preset distinguish Bundesdeutsch / Schweizerdeutsch / Österreichisches Deutsch register? (Probably not at first; the technical register is more convergent than colloquial.)

## Maintenance contract for this preset

Until the full research lands, do not add concrete rules to the "Register-specific rules" section. The "Divergence" and "Likely-to-survive" sections are deliberate placeholders that document orientation without pretending to be a binding ruleset. The first contributor who completes the research should:

1. Add a "Register-specific rules" section with explicit citations to Duden, DIN 5008, BAMF, etc., in the same `[bracket-code]` style as the EN preset.
2. Replace the "Likely-to-survive" placeholder section with confirmed rules.
3. Keep the "Divergence" section as an explainer for why this is not a translation of the EN preset.
4. Update the fallback-behaviour section to remove the research-stage notice.
5. Update AGENTS.md to mark the preset as no longer research-stage.
