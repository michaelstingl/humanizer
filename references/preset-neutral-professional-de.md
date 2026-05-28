# Voice preset: `neutral professional` (Deutsch). Early draft v0.1.

Loaded by SKILL.md when the user requests "neutral professional de" or "neutrales Deutsch". Apply this preset instead of PERSONALITY AND SOUL. The numbered patterns §1 through §30 in SKILL.md apply where language-independent (em dashes, knowledge-cutoff disclaimers, sycophantic tone, generic positive conclusions) but are NOT auto-translated into German equivalents. The German-specific rules below replace or override several of them.

**Status:** Early draft v0.1. The primary sources have been identified and the highest-confidence rules are listed. The full convergent rule set (in the same depth as `preset-neutral-professional-en.md`) is not yet compiled. Expect refinement.

## Voice mode

Sie-Anrede for descriptive and reference content directed at the reader; impersonal "man" / passive constructions for general statements. Du-Anrede only for internal team docs or genuinely casual contexts (specify explicitly). No first-person "ich" or "wir" in formal contexts. Suits technische READMEs, API-Dokumentation, RFCs, interne Spezifikationen, Anbieter-Dokumente, formelle E-Mails.

## Scope: German (de)

Targets German neutral-professional prose. Does not target Bürgersprache / Leichte Sprache (which has its own DIN SPEC 33429 standard and stricter conventions), nor literary or marketing German. The rules below reflect convergent guidance across Wikipedia:Anzeichen für KI-generierte Inhalte, the German Wikipedia Schreibwerkstatt, Duden Sprachratgeber, and observed AI-output patterns in formal German technical writing.

## Divergence from English preset (do not auto-translate)

These differences are firmly established. The English `neutral professional` rules cannot be ported wholesale.

- **Passive voice is acceptable** in formal German. "Die Tabelle wird erstellt", "Es wird empfohlen, dass..." are idiomatic, not AI tells. The English "active voice as default" rule does NOT transfer.
- **Nominalstil is idiomatic** in formal German. "Die Durchführung der Konfiguration erfolgt..." is standard register, not bloat. The English "no nominalised verbs" rule does NOT transfer. Excessive Nominalstil (more than the norm) can still be flagged.
- **Compound nouns (Komposita) are expected.** "Datenbankzugriffskonfiguration" is one word, not three. Do not break compounds apart in pursuit of Anglo-Saxon brevity.
- **Hedging via Konjunktiv is legitimate.** "Es wäre zu prüfen", "könnte ergänzt werden" are accepted formal-German constructions, not slop tells. Single Konjunktiv is fine; stacking ("könnte möglicherweise unter Umständen...") is still the tell.
- **Address mode is Sie / impersonal.** Formal German uses "Sie" or impersonal "man" / "es ist zu beachten". The English "you" rule maps to "Sie", not to "du".
- **Bandwurmsätze tolerate higher word counts.** Plain Language 15-20-word target does not transfer. German formal writing routinely uses 25-35-word sentences. The Hohenheimer Verständlichkeitsindex (HIX) is the correct target instead.

## Register-specific rules

In addition to the language-independent numbered patterns §1 through §30. Bracket codes resolve to URLs in the Sources block.

### Bedeutungs- und Werbeinflation

- **Keine Bedeutungs-Phrasen.** "steht als Zeugnis", "unterstreicht seine Bedeutung", "tief verwurzelt", "im Herzen von". Diese inflationieren beliebige Aspekte als historisch-bedeutsam. *([WP-DE].)*
- **Keine Werbesprache.** "reiches kulturelles Erbe", "atemberaubend", "lebendig", "pulsierend", "vibrant". *([WP-DE].)*
- **Keine promotional Adjektive ohne Metrik.** "robust", "umfassend", "leistungsstark", "skalierbar", "elegant" verlangen entweder eine zitierte Kennzahl oder weglassen. *(Übertragung aus EN-Preset; nicht explizit gelistet in [WP-DE], aber konvergent.)*

### Mechanische Konnektoren und Argumentationsfloskeln

- **Keine Konnektor-Cluster am Absatzanfang.** "Darüber hinaus", "außerdem", "ferner", "des Weiteren", "zudem" gehäuft als Satz- oder Absatzanfänge. Ein einzelnes "außerdem" ist kein Tell; drei in Folge schon. *([WP-DE], [KT★].)*
- **"Jedoch" statt "aber" ist verdächtig.** Ein Text ohne ein einziges "aber" ist fast immer maschinell. AI bevorzugt "jedoch" für jeden Kontrast. *([KT★].)*
- **"Sowohl... als auch... und" Dreiergruppen vermeiden.** Erzwingt Rule-of-three-Struktur, die formelles Deutsch nicht braucht. *([WP-DE], [KT★].)*
- **"Nicht nur... sondern auch" für Argumentation übernutzt.** Klassische AI-Eskalations-Figur. *([WP-DE].)*

### Sprachliche Über-Formalität (DE-spezifisch)

- **Keine archaischen Demonstrative.** "hierbei", "diesbezüglich", "hinsichtlich", "vorgenannt", "obig" sind Amtsdeutsch. In moderner formeller Prosa ersetzen durch "dabei", "dazu", "in Bezug auf", oder Verweis durch Nähe. *([KT★].)*
- **Genitivketten vermeiden.** "im Rahmen der Umsetzung der Strategie der Abteilung" → "bei der Strategieumsetzung der Abteilung" oder Komposita-Auflösung. Max. zwei Genitive in Folge. *([KT★].)*
- **Übermäßige Partizip-I-Konstruktionen.** "gewährleistend", "hervorhebend", "unterstreichend" als satz-anhängende Modifizierer. *([WP-DE].)*
- **Übertriebene Formalität ohne Umgangssprache.** In Blog-/Newsletter-Registern ist das vollständige Fehlen von "halt", "mal", "einfach" selbst ein Tell. In API-Docs gilt das nicht. *([KT★], registerabhängig.)*

### Chatbot-Artifacts (DE-Übersetzungen)

- **Keine kollaborativen Service-Floskeln.** "Natürlich!", "Selbstverständlich!", "Ich hoffe, das hilft", "Lassen Sie mich wissen, ob...", "Gerne erweitere ich...". Direkt aus dem Englischen übersetzt, klingen in deutscher Prosa fremd. *([WP-DE].)*
- **Keine formulaischen Schlüsse.** "Zusammenfassend", "Abschließend lässt sich sagen", Sektionstitel "Fazit" am Ende generischer Abschnitte. *([WP-DE].)*
- **Keine selbstgenerierten Disclaimer.** "Soweit mir bekannt", "auf Grundlage verfügbarer Informationen". *([WP-DE].)*

### Spezifikationen und API-Dokumente

- **Keine schwammigen Verhaltensverben.** "gewährleistet", "ermöglicht", "unterstützt", "bietet", "stellt sicher" maskieren in API-Docs und Spezifikationen die tatsächliche Mechanik. Ersetzen durch konkrete Operation und Fehlermodus. "Der Dienst gewährleistet Konsistenz" → "Der Dienst verwendet Zwei-Phasen-Commit; Schreibvorgänge werden bei fehlendem Quorum abgelehnt." *(Übertragung aus EN-Preset, konvergent.)*
- **Spezifikations-Verben behalten.** "MUSS", "SOLL", "DARF NICHT" (deutsche RFC-2119-Konvention) tragen Vertragssemantik, nicht "muss vielleicht" oder "sollte eventuell". Genauso "gibt zurück", "lehnt ab", "akzeptiert". *([RFC-2119].)*

### Hedging und Modal-Stacking

- **Einzelner Konjunktiv ist legitim.** "Es wäre zu prüfen", "könnte ergänzt werden" sind formeller DE-Standard.
- **Modal-Stacking ist der Tell.** "Könnte möglicherweise ermöglichen", "kann unter Umständen unterstützen", "wäre eventuell zu erwägen". Ein einzelnes Modal oder ein einzelnes Hedge-Adverb ist fein; Stapelung asserts nichts. *(Übertragung aus EN-Preset.)*

## Quantitative target: HIX

Use the Hohenheimer Verständlichkeitsindex (HIX) instead of Flesch-Kincaid Grade Level for German targets. HIX ist eine 0-20-Skala, gebaut auf vier deutschen Lesbarkeitsformeln (Amstad, Wiener Sachtextformel, SMOG-Deutsch, Lix) plus deutschspezifische Parameter (Nominalisierungsrate, Anteil Sätze >20 Wörter, etc.).

| HIX-Score | Vergleich |
|-----------|-----------|
| 0-4 | Dissertation (politikwissenschaftlich) |
| 5-9 | Fachpresse, Wissenschaftsmagazine |
| 10-14 | **Qualitätszeitung. Target für neutral-professional.** |
| 15-17 | Wochenmagazine, breite Sachbücher |
| 18-20 | Boulevard, Bild-Zeitung |

Validation tool: TextLab ([klartext.uni-hohenheim.de/klartext_textlab](https://klartext.uni-hohenheim.de/klartext_textlab)). *([HIX], [KT-INIT].)*

## Sources

- [WP-DE] [Wikipedia:Anzeichen für KI-generierte Inhalte](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte). German counterpart to en:Wikipedia:Signs of AI writing. Import September 2025, actively maintained. Primary source for German AI-tell patterns.
- [KT] / [KT★] [severinschweiger/klartext](https://github.com/severinschweiger/klartext). Claude skill specifically for German AI-pattern removal. 36 patterns, 7 marked deutschspezifisch (★). Mai 2026. The ★ marker in this document points at klartext's German-only rules.
- [TX] [LangeVC/txtHumanizer](https://github.com/LangeVC/txtHumanizer). Drei-Stufen-Workflow für deutschsprachige Texte (ANALYSE → RECOMMEND → FINETUNE). Evidenzbasiert auf Wikipedia KI-Erkennung v1.35. Apache 2.0. Capacium-installable.
- [DG] [Mineorey/deutsche-goethe](https://github.com/Mineorey/deutsche-goethe). German text humanizer for Claude Code. März 2026. Less feature-rich than the above.
- [HIX] [Hohenheimer Verständlichkeitsindex (HIX)](https://klartext.uni-hohenheim.de/hix). Composite German readability index, 0-20 scale. Drop-in replacement for Flesch-Kincaid in German contexts.
- [KT-INIT] [Klartext-Initiative Universität Hohenheim](https://klartext.uni-hohenheim.de/). Research home of HIX + TextLab tool. Prof. Dr. Frank Brettschneider.
- [DIN-LS] [DIN SPEC 33429:2025-03 (Leichte Sprache)](https://www.dinmedia.de/en/technical-rule/din-spec-33429/387728031). First unified DIN for plain German. Targets accessibility, not neutral-professional, but its sentence-length and active-construction rules transfer in spirit. Frei zugänglich.
- [DIN-5008] [DIN 5008:2020](https://www.dinmedia.de/en/topics/din-5008). German business correspondence standard. Structural (anschrift, betreff, datum, salutations), not stylistic. Useful for formal-letter format, not for AI-tell detection.
- [Duden] [Duden Sprachratgeber](https://www.duden.de/sprachwissen/sprachratgeber). Editorial articles on German style, grammar, formality. Reference for "what correct formal German looks like", no AI-specific guidance.
- [Bund-LS] [Bundesregierung Leichte Sprache](https://www.bundesregierung.de/breg-de/leichte-sprache). German government plain-language portal. Accessibility focus; transfers in spirit to anti-verbosity rules.
- [RFC-2119] [Bradner, IETF RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119). MUST/SHALL/SHOULD/MAY as load-bearing terms. German equivalents (MUSS/SOLL/DARF NICHT) inherit the contract semantics.

## Lessons beyond pattern content

What the three observed German skills do differently from the English humanizer, worth considering for our own future iterations:

### From klartext: Quick-Check pre-flight

Klartext opens with "Quick-Check mit den 10 lautesten Signalen. Wenn drei oder mehr zutreffen, ist der Text fast sicher KI-generiert." A triage step before the full rewrite. Saves the full Pattern-Pass when the input is genuinely human.

Adoption candidate: add a Quick-Check section to SKILL.md (language-independent) so the model can short-circuit when there's nothing to fix. The 10 signals would draw from the most reliable §1-§30 tells.

### From txtHumanizer: Three-stage workflow

ANALYSE → RECOMMEND → FINETUNE. More explicit than blader's "draft → audit → final":
- ANALYSE: diagnose specific tells with line references
- RECOMMEND: present rewrite options (not commit yet)
- FINETUNE: apply chosen rewrites

Adoption candidate: optional richer workflow for long texts where the user wants to see the diagnosis before the rewrite lands.

### From klartext: Target audience specificity

Klartext's description explicitly names target use-cases: "Blog-Posts, Newsletter, Landing-Pages, Social-Media-Content, Produktbeschreibungen". Our EN preset says "technical READMEs, API documentation, RFCs, project descriptions, internal write-ups, vendor-facing prose". Both are concrete; both work.

Lesson: keep concrete-use-case lists in preset descriptions. They guide invocation and prevent misuse.

### From klartext: Inline language markers vs file split

Klartext keeps universal patterns and German-specific patterns in one file, marking the latter with ★. Our skill splits into SKILL.md (universal) + `references/preset-<lang>.md` (per-language). Trade-off:
- Klartext-Stil: one read, everything visible, denser
- Our Stil: progressive disclosure, scales to N languages, requires routing step

Both are defensible. Our architecture is right when N >= 2 languages exist; klartext-style stays cleaner for N = 1.

### From txtHumanizer: Explicit versioning of the rule basis

txtHumanizer ties itself to "Wikipedia KI-Erkennung v1.35", a specific snapshot. Our skill ties to blader/humanizer v2.7.0 plus our feature/voice-presets branch. Per-preset versioning is missing; this DE file declares "v0.1" in its title, which is a start. As preset rules evolve, version each file independently.

## Open questions for the next research round

- Wikipedia:DE has been "import-and-adapt" from EN since September 2025. Has the DE community diverged in any direction the EN page does not cover? (Spot-check L modifications in May 2026 against equivalent EN.)
- Does Duden Mentor expose its rule set, or is it closed? If open, can specific rules be extracted as ground truth for borderline German formal-vocabulary choices?
- HIX target of 10-14 for neutral-professional: is this empirically validated against German technical documentation, or only against journalism / political comms? Need to find HIX-scored corpus of technical docs.
- No German equivalent of Kobak et al. (corpus shift study) was found. Could be commissioned (or scoped as a research grant for an applied-linguistics group; Hohenheim or Mannheim ideal).
- No German Vale style pack exists. Building one (errata-ai/German equivalent) would be a substantial community contribution. Out of scope here, but worth tracking.
- klartext markets itself for blog/marketing register; this preset targets technical-doc register. The Wikipedia:DE patterns are encyclopaedic. How do these three registers reconcile?

## Maintenance contract for this preset

- This file is treated as the authoritative DE preset definition. SKILL.md routing points here.
- Versioning: bump the v0.X version in the title line when register-specific rules change. v0.1 = current baseline.
- New patterns added to Wikipedia:DE should be reviewed and adopted where they fit the neutral-professional register (skip patterns that are encyclopaedic-only).
- Pattern additions from klartext or txtHumanizer should be cited with the right bracket-code and only added if the source explicitly marks them as German-specific or if the test case demonstrates the rule is not a 1:1 translation of an EN rule.
- The "Lessons beyond pattern content" section is the place to capture process-level learnings from observed German skills. Do not put them in the rules section; the rules section is for what to apply to text.

## Fallback behaviour

If a user invokes `neutral professional de` and the rewrite engages unfamiliar German patterns this draft does not yet cover:

1. Apply the rules above and the universal §1 through §30 from SKILL.md.
2. Apply the Divergence section as a guardrail (do not strip passive, do not break Komposita, do not flatten Nominalstil).
3. If the text deals with a genre this preset has not been calibrated for (Behördensprache, juristische Texte, wissenschaftliche Publikationen), flag in the response that the preset is calibrated for technical-doc register and the user may want a different preset or sample.

Until v1.0: indicate "v0.1 draft" in the response when applying this preset, so the user knows the rule set is still evolving.
