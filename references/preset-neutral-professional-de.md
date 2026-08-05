# Voice preset: `neutral professional` (Deutsch). Draft v0.2.

Loaded by SKILL.md when the user requests "neutral professional de" or "neutrales Deutsch". Apply this preset instead of PERSONALITY AND SOUL. The numbered patterns §1 through §30 in SKILL.md apply where language-independent (knowledge-cutoff disclaimers, sycophantic tone, generic positive conclusions) but are NOT auto-translated into German equivalents. The German-specific rules below replace or override several of them — including the em-dash rule, which inverts for German (see Typografie).

**Status:** Draft v0.2. New in this revision: a Typografie section (deterministically checkable, DE-normative sources), a Struktur/Formatierung section, a Rhythmus section that explicitly refuses to import English sentence-length thresholds, a DE Quick-Check, and the rhetoric/evidence pattern families from `humanizer-de`. Still short of the EN preset in worked examples.

## Voice mode

Sie-Anrede for descriptive and reference content directed at the reader; impersonal "man" / passive constructions for general statements. Du-Anrede only for internal team docs or genuinely casual contexts (specify explicitly). No first-person "ich" or "wir" in formal contexts. Suits technische READMEs, API-Dokumentation, RFCs, interne Spezifikationen, Anbieter-Dokumente, formelle E-Mails.

## Scope: German (de)

Targets German neutral-professional prose. Does not target Bürgersprache / Leichte Sprache (which has its own DIN SPEC 33429 standard and stricter conventions), nor literary or marketing German. The rules below reflect convergent guidance across German-language sources only: Wikipedia:Anzeichen für KI-generierte Inhalte, `marmbiz/humanizer-de`, `severinschweiger/klartext`, the Klartext-Initiative Hohenheim, Duden Rechtschreibregeln, DIN 5008, and German-language reporting on AI tells. English-language studies are cited nowhere as a rule basis; see "Warum keine englischsprachigen Studien" below.

## Divergence from English preset (do not auto-translate)

These differences are firmly established. The English `neutral professional` rules cannot be ported wholesale.

- **Passive voice is acceptable** in formal German. "Die Tabelle wird erstellt", "Es wird empfohlen, dass..." are idiomatic, not AI tells. The English "active voice as default" rule does NOT transfer.
- **Nominalstil is idiomatic** in formal German. "Die Durchführung der Konfiguration erfolgt..." is standard register, not bloat. The English "no nominalised verbs" rule does NOT transfer. Excessive Nominalstil (more than the norm) can still be flagged.
- **Compound nouns (Komposita) are expected.** "Datenbankzugriffskonfiguration" is one word, not three. Do not break compounds apart in pursuit of Anglo-Saxon brevity.
- **Hedging via Konjunktiv is legitimate.** "Es wäre zu prüfen", "könnte ergänzt werden" are accepted formal-German constructions, not slop tells. Single Konjunktiv is fine; stacking ("könnte möglicherweise unter Umständen...") is still the tell.
- **Address mode is Sie / impersonal.** Formal German uses "Sie" or impersonal "man" / "es ist zu beachten". The English "you" rule maps to "Sie", not to "du".
- **Bandwurmsätze tolerate higher word counts.** Plain Language 15-20-word target does not transfer. German formal writing routinely uses 25-35-word sentences. The Hohenheimer Verständlichkeitsindex (HIX) is the correct target instead.
- **The dash rule inverts.** SKILL.md treats the em dash (—) as an overuse tell to be reduced. In German the em dash is not merely overused, it is the wrong glyph: German sets the Gedankenstrich as a Halbgeviertstrich (–) with surrounding spaces. Every "—" in German prose is an English-typography import. *([WP-TYP], [GOL].)*
- **Sentence-length variance thresholds do not transfer.** Numeric burstiness targets published for English prose describe an English corpus. Do not apply them to German. See Rhythmus.

## Register-specific rules

In addition to the language-independent numbered patterns §1 through §30. Bracket codes resolve to URLs in the Sources block.

### Bedeutungs- und Werbeinflation

- **Keine Bedeutungs-Phrasen.** "steht als Zeugnis", "unterstreicht seine Bedeutung", "tief verwurzelt", "im Herzen von", "Wendepunkt", "Schlüsselmoment", "spielt eine wichtige Rolle". Diese inflationieren beliebige Aspekte als historisch-bedeutsam. *([WP-DE], [HDE].)*
- **Keine Werbesprache.** "reiches kulturelles Erbe", "atemberaubend", "lebendig", "pulsierend", "beeindruckende natürliche Schönheit", "unbedingt besuchen". *([WP-DE], [HDE].)*
- **Keine „sicheren" Positiv-Adjektive.** "innovativ", "praktisch", "vielfältig", "spannend" ohne Beleg. Sie sind risikolos und deshalb inhaltsleer. *([GOL].)*
- **Keine Aufwertungs-Verben.** "auf ein neues Level heben", "eintauchen", "revolutionieren", "neu definieren". *([GOL].)*
- **Keine promotional Adjektive ohne Metrik.** "robust", "umfassend", "leistungsstark", "skalierbar", "elegant" verlangen entweder eine zitierte Kennzahl oder weglassen. *([WP-DE] listet Werbesprache generisch; die Metrik-Forderung ist konvergent mit [HDE].)*
- **Keine dekorativen Metaphern.** "wie ein Leuchtturm im dichten Nebel", "das Herzstück", "roter Faden" als Schmuck ohne Erklärungsleistung. *([GOL].)*

### Mechanische Konnektoren und Argumentationsfloskeln

- **Keine Konnektor-Cluster am Absatzanfang.** "Darüber hinaus", "außerdem", "ferner", "des Weiteren", "zudem", "andererseits" gehäuft als Satz- oder Absatzanfänge. Ein einzelnes "außerdem" ist kein Tell; drei in Folge schon. *([WP-DE], [KT★], [HDE].)*
- **"Jedoch" statt "aber" ist verdächtig.** Ein Text ohne ein einziges "aber" ist fast immer maschinell. AI bevorzugt "jedoch" für jeden Kontrast. *([KT★].)*
- **"Sowohl... als auch... und" Dreiergruppen vermeiden.** Erzwingt Rule-of-three-Struktur, die formelles Deutsch nicht braucht. Auch die reine Adjektiv-Triade zählt: "intuitiv, schnell und effizient". *([WP-DE], [KT★], [GOL].)*
- **"Nicht nur... sondern auch" für Argumentation übernutzt.** Klassische AI-Eskalations-Figur, ebenso "Es ist nicht nur X, es ist auch Y". *([WP-DE], [GOL].)*

### Sprachliche Über-Formalität (DE-spezifisch)

- **Keine archaischen Demonstrative.** "hierbei", "diesbezüglich", "hinsichtlich", "vorgenannt", "obig" sind Amtsdeutsch. In moderner formeller Prosa ersetzen durch "dabei", "dazu", "in Bezug auf", oder Verweis durch Nähe. *([KT★].)*
- **Genitivketten vermeiden.** "im Rahmen der Umsetzung der Strategie der Abteilung" → "bei der Strategieumsetzung der Abteilung" oder Komposita-Auflösung. Max. zwei Genitive in Folge. *([KT★].)*
- **Übermäßige Partizip-I-Konstruktionen.** "gewährleistend", "hervorhebend", "unterstreichend" als satz-anhängende Modifizierer. *([WP-DE].)*
- **Übertriebene Formalität ohne Umgangssprache.** In Blog-/Newsletter-Registern ist das vollständige Fehlen von "halt", "mal", "einfach" selbst ein Tell. In API-Docs gilt das nicht. *([KT★], registerabhängig.)*

### Rhetorik- und Signposting-Floskeln

- **Keine Überredungs-Formeln.** "Im Kern", "letztlich geht es darum", "die entscheidende Frage ist". Sie kündigen Tiefe an, die der Satz nicht liefert. *([HDE].)*
- **Kein Signposting an den Leser.** "Schauen wir uns an", "werfen wir einen Blick auf", "im Folgenden betrachten wir". Der Abschnittstitel leistet das bereits. *([HDE].)*
- **Kein "In der heutigen ...-Welt"-Einstieg.** "In der heutigen digitalen Welt", "in einer zunehmend vernetzten Zeit". Reiner Aufwärmabsatz ohne Aussage. *([HDE].)*
- **Keine Aphorismen als Absatzschluss.** Der abrundende Merksatz ("Qualität entsteht nicht zufällig.") ist eine Modellgewohnheit, kein Argument. *([HDE].)*
- **Keine redaktionellen Selbstkommentare.** "es ist wichtig zu bemerken", "es ist bemerkenswert", "keine Betrachtung wäre vollständig ohne". *([WP-DE], [HDE].)*

### Argumentation und Belege

- **Keine vagen Quellenverweise.** "Branchenberichte zeigen", "Beobachter gehen davon aus", "Studien belegen" ohne Nennung. Entweder Quelle benennen oder Behauptung streichen. *([WP-DE], [HDE].)*
- **Keine erfundene Ich-Erfahrung.** "In meiner Praxis hat sich gezeigt", "wir haben oft erlebt" in Texten, hinter denen keine solche Erfahrung steht. *([HDE].)*
- **Keine Verantwortungs-Verschleierung.** "Es wurde entschieden", "es kam zu Verzögerungen", wo ein Akteur benennbar ist. Achtung: Das ist kein generelles Passiv-Verbot – formelles Deutsch darf passiv sein. Der Tell ist das Verschwinden des Handelnden, nicht die Passivform. *([HDE]; abgegrenzt gegen die Divergence-Regel oben.)*
- **Keine Konditional-Stapelung.** "Sofern verfügbar und soweit anwendbar, könnte gegebenenfalls..." Jede Bedingung einzeln oder streichen. *([HDE].)*

### Chatbot-Artifacts (DE-Übersetzungen)

- **Keine kollaborativen Service-Floskeln.** "Natürlich!", "Selbstverständlich!", "Ich hoffe, das hilft", "Lassen Sie mich wissen, ob...", "Gerne erweitere ich...". Direkt aus dem Englischen übersetzt, klingen in deutscher Prosa fremd. *([WP-DE], [HDE].)*
- **Keine Lob-Eröffnung.** "Wunderbare Frage", "Sie treffen damit den Kern", "sehr guter Punkt". *([GOL].)*
- **Keine formulaischen Schlüsse.** "Zusammenfassend", "Abschließend lässt sich sagen", "Insgesamt", Sektionstitel "Fazit" am Ende generischer Abschnitte. *([WP-DE], [HDE].)*
- **Keine selbstgenerierten Disclaimer.** "Soweit mir bekannt", "auf Grundlage verfügbarer Informationen". *([WP-DE].)*
- **Kein Brief-Duktus in Sachtexten.** Anrede- und Grußformeln in Dokumenten, die keine Korrespondenz sind. *([HDE].)*

### Spezifikationen und API-Dokumente

- **Keine schwammigen Verhaltensverben.** "gewährleistet", "ermöglicht", "unterstützt", "bietet", "stellt sicher" maskieren in API-Docs und Spezifikationen die tatsächliche Mechanik. Ersetzen durch konkrete Operation und Fehlermodus. "Der Dienst gewährleistet Konsistenz" → "Der Dienst verwendet Zwei-Phasen-Commit; Schreibvorgänge werden bei fehlendem Quorum abgelehnt." *(Konvergent mit [HDE]-Kategorie „Argumentation & Belege"; im EN-Preset über [BB] belegt.)*
- **Spezifikations-Verben behalten.** "MUSS", "SOLL", "DARF NICHT" (deutsche RFC-2119-Konvention) tragen Vertragssemantik, nicht "muss vielleicht" oder "sollte eventuell". Genauso "gibt zurück", "lehnt ab", "akzeptiert". *([RFC-2119].)*

### Hedging und Modal-Stacking

- **Einzelner Konjunktiv ist legitim.** "Es wäre zu prüfen", "könnte ergänzt werden" sind formeller DE-Standard.
- **Modal-Stacking ist der Tell.** "Könnte möglicherweise ermöglichen", "kann unter Umständen unterstützen", "wäre eventuell zu erwägen". Ein einzelnes Modal oder ein einzelnes Hedge-Adverb ist fein; Stapelung asserts nichts. *(Deckungsgleich mit [HDE] „Konditional-Stapelung".)*

## Typografie (DE-normativ, deterministisch prüfbar)

Diese Regeln sind der wertvollste Teil des Presets, weil sie ohne Modell-Urteil prüfbar sind: ein Zeichen ist richtig oder falsch. Sie sind außerdem stabil – Wortlisten veralten mit jeder Modellgeneration, Typografie-Normen nicht.

- **Gedankenstrich ist der Halbgeviertstrich (–) mit Spatien**, nicht der Geviertstrich (—). "Der Termin – ein Donnerstag – passt." Der Geviertstrich ist englische Setzung. Prüfung: kein U+2014 in deutschem Text. *([WP-TYP], [Duden-GS], [DIN-5008].)*
- **Gedankenstrich-Häufung ist zusätzlich ein Tell.** Auch mit korrektem Glyph: Modelle setzen den Gedankenstrich deutlich häufiger als menschliche Schreiber. Wo ein Komma, Semikolon oder Punkt trägt, diesen nehmen. *([GOL].)*
- **Deutsche Anführungszeichen „…"** (99 unten, 66 oben) oder Guillemets »…«, nicht die englischen "…". Prüfung: kein U+201C/U+201D-Paar in englischer Reihenfolge. *([Duden-AZ].)*
- **Typografischer Apostroph (’), nicht der Schreibmaschinen-Ersatz (').** *([Duden-AP].)*
- **Ein Leerzeichen nach dem Satzpunkt, nicht zwei.** Doppelte Leerzeichen sind US-Schreibmaschinen-Konvention. *([KOR].)*
- **Geschütztes Leerzeichen vor Einheiten und in Abkürzungen.** "50 %", "12 kg", "z. B.", "d. h." Das fehlende Spatium in "z.B." und das fehlende Leerzeichen in "50%" sind beides Anglizismen. *([DIN-5008].)*
- **Keine englische Title-Case in Überschriften.** "Konfiguration Der Datenbank" ist aus dem Englischen kopiert; deutsche Überschriften folgen der normalen Groß-/Kleinschreibung. *([HDE].)*
- **Standard-Aufzählungszeichen, keine Emojis und keine "•"-Ersatzzeichen vor Überschriften.** *([WP-DE], [KOR].)*
- **Bis-Strich ist ebenfalls der Halbgeviertstrich, ohne Spatien.** "2024–2026", "10–15 Stunden". *([DIN-5008].)*

## Struktur und Formatierung

- **Keine Drei-Drei-Drei-Architektur.** Drei Einleitungssätze, drei Hauptpunkte mit je drei Unterpunkten, dreigliedriger Schluss. Diese Symmetrie entsteht organisch fast nie. *([KOR].)*
- **Keine Fünfergruppen bei Aufzählungen als Default.** Die Listenlänge soll aus dem Inhalt kommen, nicht aus einer Modellgewohnheit. *([GOL].)*
- **Keine gleich langen Listenpunkte.** Exakt parallele Item-Längen sind ein Generierungsartefakt. *([KOR].)*
- **Kein „Zusammenfassend"-Absatz pro Abschnitt.** Ein Fazit am Ende des Dokuments kann sinnvoll sein; eines pro Sektion ist Füllmaterial. *([KOR], [WP-DE].)*
- **Keine Fettschrift-Inflation.** Hervorhebung einzelner Begriffe ist zulässig; ganze Sätze oder jeder erste Halbsatz einer Listenzeile fett ist ein Tell. *([WP-DE], [HDE].)*
- **Keine Pseudo-Listen.** Aufzählungszeichen für Inhalte, die ein zusammenhängender Absatz sind. *([HDE].)*
- **Keine Markdown-Syntax in Zielformaten, die sie nicht kennen** (Wikitext, DOCX, Plain-Text-Mails). *([WP-DE], [HDE].)*

## Rhythmus

Satzlängen-Varianz ist ein belastbares Signal – aber die veröffentlichten Zahlenwerte stammen aus englischsprachigen Korpora und gelten hier nicht.

- **Satzlängen variieren lassen.** Gleichförmige Satzlängen über einen ganzen Abschnitt sind ein Tell. Das ist qualitativ anzuwenden, nicht gegen einen importierten Schwellenwert. *([KOR] nennt einen Variationskoeffizienten unter 0,4 als verdächtig, beruft sich dafür aber auf eine englischsprachige Untersuchung; die Zahl ist für formelles Deutsch nicht validiert und wird hier bewusst nicht als Zielwert gesetzt.)*
- **Als deutschsprachiger Ersatzmaßstab dient HIX**, der unter anderem den Anteil der Sätze über 20 Wörter und die Nominalisierungsrate als Parameter führt – beides deutschspezifisch kalibriert. *([HIX], [KT-INIT].)*
- **Formelles Deutsch darf lang sein.** 25–35 Wörter sind normal. Wer deutsche Sätze auf englisches Plain-Language-Maß kürzt, produziert einen anderen Fehler, nicht weniger KI-Geruch.

## Quick-Check (DE)

Vor dem vollen Pattern-Pass. Die ersten vier sind mechanisch prüfbar und deshalb zuerst zu prüfen. Drei oder mehr Treffer: Text mit hoher Wahrscheinlichkeit maschinell.

1. Enthält der Text ein "—" (Geviertstrich)?
2. Englische Anführungszeichen "…" statt „…"?
3. "z.B." ohne Spatium oder "50%" ohne Leerzeichen?
4. Doppelte Leerzeichen nach Satzpunkten?
5. Drei oder mehr Konnektoren wie "darüber hinaus" / "zudem" / "ferner" als Satzanfänge?
6. Kein einziges "aber" im ganzen Text, aber mehrere "jedoch"?
7. Ein "Zusammenfassend"- oder "Fazit"-Absatz pro Abschnitt?
8. Adjektiv-Dreiergruppen oder "nicht nur … sondern auch"?
9. Gleich lange Listenpunkte oder Drei-Drei-Drei-Struktur?
10. Werbe- oder Bedeutungsphrasen ohne Beleg ("innovativ", "steht als Zeugnis", "im Herzen von")?

*(Quick-Check-Idee übernommen von [KT]; Signalauswahl aus [WP-DE], [HDE], [GOL], [KOR] und den Typografie-Normen.)*

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

## Warum keine englischsprachigen Studien als Regelbasis

Das EN-Preset stützt seine Wortlisten-Regel auf Kobak et al. (Korpus-Verschiebung in englischen PubMed-Abstracts). Für Deutsch existiert keine äquivalente Untersuchung. Naheliegende englischsprachige Ersatzquellen – etwa Arbeiten zu Burstiness und Satzlängen-Varianz – messen englische Prosa und liefern Zahlenwerte, die an englischen Satzlängen-Normen hängen. Sie in ein DE-Preset zu übernehmen wäre derselbe Fehler wie die Übernahme der Aktiv-statt-Passiv-Regel: formal plausibel, sprachlich falsch. Deshalb gilt hier: qualitative Regel ja, importierter Schwellenwert nein. Die Lücke ist als offene Frage dokumentiert, nicht überdeckt.

## Sources

- [WP-DE] [Wikipedia:Anzeichen für KI-generierte Inhalte](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte). German counterpart to en:Wikipedia:Signs of AI writing. Import September 2025, actively maintained. Primary source for German AI-tell patterns.
- [HDE] [marmbiz/humanizer-de](https://github.com/marmbiz/humanizer-de). German AI Text Humanizer für Claude Code und Codex, Version 5.15.0 (Stand August 2026). 72 deutsche Muster in 10 Kategorien, davon ca. 15 als deterministische Python-Linter (`humanizer_audit.py`, `evidence_lint.py`, `rhythm_lint.py`), optionale spaCy-Syntaxanalyse, Evidence-Gate zum Schutz von Zahlen, Namen und Belegen. Fork von blader/humanizer, eigenständig weiterentwickelt; Musterkatalog aus [WP-DE] abgeleitet, nicht aus dem Englischen übersetzt. Ausführlichste bekannte DE-Quelle.
- [GOL] [KI-Texte erkennen: Auf diese Merkmale müsst ihr achten (Golem Karrierewelt)](https://karrierewelt.golem.de/blogs/karriere-ratgeber/ki-texte-erkennen-auf-diese-merkmale-musst-ihr-achten). Deutschsprachiger Praxisartikel. Belegt unter anderem die Gedankenstrich-Häufung, „sichere" Positiv-Adjektive, Aufwertungs-Verben, Dreiergruppen, Fünfer-Listen und Lob-Eröffnungen.
- [KOR] [KI-Texte erkennen: Merkmale & Checkliste (korrektur.de)](https://korrektur.de/ki-texte-erkennen-merkmale-checkliste). Deutschsprachige Checkliste, Sekundärquelle. Liefert die strukturellen und typografischen Merkmale (Drei-Drei-Drei, gleich lange Listenpunkte, doppelte Leerzeichen, falsche Strich- und Anführungszeichen). Der dort genannte Varianz-Schwellenwert 0,4 stammt aus einer englischsprachigen Untersuchung und wird in diesem Preset nicht als Zielwert übernommen.
- [KT] / [KT★] [severinschweiger/klartext](https://github.com/severinschweiger/klartext). Claude skill specifically for German AI-pattern removal. 36 patterns, 7 marked deutschspezifisch (★). Mai 2026. The ★ marker in this document points at klartext's German-only rules. Quelle der Quick-Check-Idee.
- [TX] [LangeVC/txtHumanizer](https://github.com/LangeVC/txtHumanizer). Drei-Stufen-Workflow für deutschsprachige Texte (ANALYSE → RECOMMEND → FINETUNE). Evidenzbasiert auf Wikipedia KI-Erkennung v1.35. Apache 2.0.
- [DG] [Mineorey/deutsche-goethe](https://github.com/Mineorey/deutsche-goethe). German text humanizer for Claude Code. März 2026. Less feature-rich than the above.
- [MM] [Humanizer (Deutsch): Claude-Skill für menschlichere KI-Texte – Martin Möller](https://martin-moeller.biz/en/lab/ai/claude-humanizer-skill-german). Projektdokumentation zu [HDE] durch den Autor: Entstehung als blader-Fork, eigenes Versionsschema, Zielregister.
- [WP-TYP] [Wikipedia: Halbgeviertstrich](https://de.wikipedia.org/wiki/Halbgeviertstrich). Belegt, dass der deutsche Gedankenstrich ein Halbgeviertstrich mit umgebenden Leerzeichen ist, während englische Setzung den längeren Geviertstrich verwendet.
- [Duden-GS] [Duden Rechtschreibregeln: Gedankenstrich](https://www.duden.de/sprachwissen/rechtschreibregeln/gedankenstrich). Funktion des Gedankenstrichs (Wechsel von Erwartung, Thema, Sprecher, Satzbau). Deckt die Funktion ab, nicht die Glyphenwahl – dafür [WP-TYP] und [DIN-5008].
- [Duden-AZ] [Duden Rechtschreibregeln: Anführungszeichen](https://www.duden.de/sprachwissen/rechtschreibregeln/anfuehrungszeichen). Deutsche Anführungszeichen „…" (unten/oben), halbe Anführungszeichen für Verschachtelung.
- [Duden-AP] [Duden Rechtschreibregeln: Apostroph](https://www.duden.de/sprachwissen/rechtschreibregeln/apostroph). Apostroph-Regeln, Auslassungen, Namen.
- [DIN-5008] [DIN 5008:2020](https://www.dinmedia.de/en/topics/din-5008). German business correspondence standard. Normativ für Spatien in Abkürzungen ("z. B."), Leerzeichen vor Einheiten und Prozentzeichen, Bis-Strich ohne Spatien, Gedankenstrich mit Spatien.
- [HIX] [Hohenheimer Verständlichkeitsindex (HIX)](https://klartext.uni-hohenheim.de/hix). Composite German readability index, 0-20 scale. Drop-in replacement for Flesch-Kincaid in German contexts.
- [KT-INIT] [Klartext-Initiative Universität Hohenheim](https://klartext.uni-hohenheim.de/). Research home of HIX + TextLab tool. Prof. Dr. Frank Brettschneider.
- [DIN-LS] [DIN SPEC 33429:2025-03 (Leichte Sprache)](https://www.dinmedia.de/en/technical-rule/din-spec-33429/387728031). First unified DIN for plain German. Targets accessibility, not neutral-professional, but its sentence-length and active-construction rules transfer in spirit.
- [Duden] [Duden Sprachratgeber](https://www.duden.de/sprachwissen/sprachratgeber). Editorial articles on German style, grammar, formality. Reference for "what correct formal German looks like", no AI-specific guidance.
- [Bund-LS] [Bundesregierung Leichte Sprache](https://www.bundesregierung.de/breg-de/leichte-sprache). German government plain-language portal. Accessibility focus; transfers in spirit to anti-verbosity rules.
- [RFC-2119] [Bradner, IETF RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119). MUST/SHALL/SHOULD/MAY as load-bearing terms. German equivalents (MUSS/SOLL/DARF NICHT) inherit the contract semantics.

## Lessons beyond pattern content

What the observed German skills do differently from the English humanizer, worth considering for our own future iterations:

### From klartext: Quick-Check pre-flight

Klartext opens with "Quick-Check mit den 10 lautesten Signalen. Wenn drei oder mehr zutreffen, ist der Text fast sicher KI-generiert." A triage step before the full rewrite. Adopted in this preset as the DE Quick-Check section, with the mechanical typography checks pulled to the front.

Adoption candidate for SKILL.md: a language-independent Quick-Check so the model can short-circuit when there's nothing to fix.

### From humanizer-de: deterministic linters over model judgement

`humanizer-de` runs roughly a fifth of its patterns as Python linters instead of prompting the model to spot them. Typography, unicode artifacts and rhythm are exactly the class of check where a script beats a judgement call: no false-positive drift, no context cost, reproducible across runs.

Adoption candidate: a small script per mechanical rule (dash glyph, quote glyph, double space, missing narrow space) that the skill can run before the prose pass. Higher value than extending the word lists further.

### From humanizer-de: Evidence-Gate

Facts, numbers, names and sources are frozen before rewriting, so a humanising pass cannot bend evidence. Our skill has no equivalent guard and relies on instruction alone.

Adoption candidate: an explicit "do not touch" enumeration extracted from the input before rewrite, checked after.

### From txtHumanizer: Three-stage workflow

ANALYSE → RECOMMEND → FINETUNE. More explicit than blader's "draft → audit → final": diagnose with line references, present rewrite options, then apply.

Adoption candidate: optional richer workflow for long texts where the user wants to see the diagnosis before the rewrite lands.

### From klartext: Target audience specificity

Klartext names its use-cases explicitly ("Blog-Posts, Newsletter, Landing-Pages, Social-Media-Content, Produktbeschreibungen"). Keep concrete use-case lists in preset descriptions; they guide invocation and prevent misuse.

### From klartext: Inline language markers vs file split

Klartext keeps universal and German-specific patterns in one file, marking the latter with ★. Our skill splits into SKILL.md (universal) + `references/preset-<lang>.md`. Klartext-style is denser for one language; the split scales to N languages. Both defensible.

### From humanizer-de: aggressive version numbering

`humanizer-de` sits at 5.15.0 while our DE preset is at v0.2. Their scheme signals an actively iterated rule catalog with a changelog per revision. Per-preset semantic versioning plus a short changelog block would make drift visible.

## Open questions for the next research round

- No German equivalent of Kobak et al. (corpus shift study) exists. Until one does, DE vocabulary rules rest on editorial guidance rather than measured corpus shift. Candidate for an applied-linguistics collaboration (Hohenheim, Mannheim, IDS).
- Is there a German-language burstiness or sentence-length-variance study? If yes, it replaces the deliberately unset threshold in the Rhythmus section. If no, the qualitative rule stays and the gap stays documented.
- HIX target of 10-14 for neutral-professional: empirically validated against German technical documentation, or only against journalism and political comms? Need a HIX-scored corpus of technical docs.
- `humanizer-de` has 72 patterns; this preset covers a subset. Which of the remaining ones are genuinely register-relevant for technical prose rather than encyclopaedic or marketing-specific? Full diff pending.
- Wikipedia:DE has been "import-and-adapt" from EN since September 2025. Has the DE community diverged in a direction the EN page does not cover? Spot-check 2026 revisions against the EN equivalent.
- No German Vale style pack exists. Building one (errata-ai equivalent) would be a substantial community contribution and would give the mechanical rules a standard runner. Out of scope here, worth tracking.
- Register reconciliation: klartext targets blog/marketing, this preset targets technical docs, Wikipedia:DE is encyclopaedic, `humanizer-de` spans several. Where the three disagree, which wins for neutral-professional?

## Maintenance contract for this preset

- This file is treated as the authoritative DE preset definition. SKILL.md routing points here.
- Versioning: bump the v0.X version in the title line when register-specific rules change. v0.1 = initial draft, v0.2 = typography, structure, rhythm, Quick-Check, evidence/rhetoric families.
- Every rule carries a bracket code. A rule without a source does not go in. Where a rule is transferred rather than sourced, the transfer is named as such in the citation.
- German rules take German sources. English-language studies may inform structure or method, but are not cited as a rule basis for German prose; see "Warum keine englischsprachigen Studien".
- New patterns added to Wikipedia:DE or `humanizer-de` should be reviewed and adopted where they fit the neutral-professional register (skip patterns that are encyclopaedic-only or marketing-only).
- The "Lessons beyond pattern content" section is the place to capture process-level learnings from observed German skills. Do not put them in the rules section; the rules section is for what to apply to text.

## Fallback behaviour

If a user invokes `neutral professional de` and the rewrite engages unfamiliar German patterns this draft does not yet cover:

1. Apply the rules above and the universal §1 through §30 from SKILL.md.
2. Apply the Divergence section as a guardrail (do not strip passive, do not break Komposita, do not flatten Nominalstil, do not import English sentence-length targets, and remember the dash rule inverts).
3. If the text deals with a genre this preset has not been calibrated for (Behördensprache, juristische Texte, wissenschaftliche Publikationen), flag in the response that the preset is calibrated for technical-doc register and the user may want a different preset or sample.

Until v1.0: indicate "v0.2 draft" in the response when applying this preset, so the user knows the rule set is still evolving.
