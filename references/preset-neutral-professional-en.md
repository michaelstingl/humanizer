# Voice preset: `neutral professional` (English)

Loaded by SKILL.md when the user requests "neutral professional", "neutral professional en", or equivalent. Apply this preset instead of PERSONALITY AND SOUL. The numbered patterns §1 through §30 in SKILL.md still apply unchanged; this preset only shifts register and voice.

## Voice mode

Third-person for descriptive and reference content; second-person ("you") for instructional and procedural content (install steps, how-to). No first-person ("I", "we") in either mode. No folksy asides, no one-word sentences for effect. Sentence length still varied, rhythm even rather than punchy. Suits technical READMEs, API documentation, RFCs, project descriptions, internal write-ups, vendor-facing prose. Do not inject opinions or mixed feelings. Keep claims sourced or hedged honestly, never both ("studies show" without a study is still an AI tell).

## Scope: English (en)

The rules below derive from convergent guidance across the Google developer documentation style guide, Microsoft Writing Style Guide, Apple Style Guide, IBM Style Guide, GOV.UK Content Design Guide, GitLab Documentation Style Guide, Plain Language Action and Information Network guidelines, and the Chicago Manual of Style. They do not apply to German, French, Spanish, or other languages where formal-writing conventions differ significantly (e.g., German tolerates passive voice and nominalised constructions that English style guides reject). For non-English text, request a language-specific preset or fall back to the default voice with explicit language instruction.

## Register-specific rules

In addition to the numbered patterns §1 through §30. Each rule cites the style guide(s) it was drawn from; bracket codes resolve to URLs in the Sources block below. For non-native English writers: when in doubt between a formal-sounding word and a common one, the common word almost always wins in this register. Plain Language guidance applies more strictly here than in academic or marketing writing.

- **Active voice as default.** "The button can be clicked" → "Click the button." Passive is acceptable only when the agent is genuinely unknown or irrelevant. *(Convergent across [G], [MS], [Apple], [IBM], [GOV], [GL], [PL], [CMS], [MC].)*
- **Present tense.** "The function will return..." → "The function returns..." Future tense ("will") is reserved for genuinely future events, not for describing current behaviour. *([G], [IBM].)*
- **No filler intensifiers.** Drop "simply", "easily", "just", "straightforward", "merely". They imply triviality and add no information. *([G], [RH].)*
- **No "utilize" / "leverage" / "facilitate".** Use "use", or name the specific action. "We leverage X" → "X does Y." *([MS], [GL].)*
- **No vague behavioural verbs in specifications.** "ensures", "supports", "enables", "provides", "handles" hide the mechanism. Replace with the actual operation and its failure mode. "The service ensures consistency" → "The service uses two-phase commit; writes are rejected if quorum is not reached." *([BB].)*
- **No hedge-stacked modal predictions.** "could potentially enable" / "may help to facilitate" assert nothing. Either commit to a claim or omit it. A single modal or single hedge is fine; stacking them is the tell. *([CB].)*
- **No nominalised verbs.** "perform a restart" → "restart". "make a decision about" → "decide". "give consideration to" → "consider". *([Apple].)*
- **No Latin abbreviations in body prose.** "e.g." → "for example", "i.e." → "that is", "etc." → name the missing items or drop them. (Acceptable inside parenthetical asides and citations.) *([GOV], [GL].)*
- **One idea per sentence; short sentences over long ones.** Aim for 15-20 words on average, hard cap around 25. Two clauses joined by "and" are usually two sentences. Plain Language targets a Flesch-Kincaid Grade Level around 8 for general technical audiences. *([MC], [PL].)*
- **No promotional adjectives without measurable backing.** "robust", "comprehensive", "powerful", "seamless", "scalable", "elegant" require either a cited metric or omission. "A scalable system" → "Tested at 10,000 requests per second" or just remove the adjective. *(Convergent consensus across style guides; no single source bans these by name. Documented as recurring AI tell in [BB] and [CB].)*
- **Use common words over fancy synonyms.** When two words mean the same thing, prefer the everyday word. This matters extra for non-native English writers: Latinate verbs ("utilize", "terminate", "subsequent") feel natural to German, French, and Spanish speakers but read as formal or distant in English. The Anglo-Saxon synonym is almost always shorter and clearer.

  The seven highest-frequency AI-tell pairs:

  | Avoid          | Prefer        |
  |----------------|---------------|
  | utilize        | use           |
  | leverage       | use           |
  | facilitate     | help, allow   |
  | demonstrate    | show          |
  | subsequent     | later, next   |
  | additional     | more, extra   |
  | brittle        | fragile       |

  This is an illustrative starter set, not the full catalog. For comprehensive lists, fetch one of the canonical sources directly:

  ```bash
  # Microsoft Wordiness pack: about 80 substitution pairs in YAML
  curl -s https://raw.githubusercontent.com/errata-ai/Microsoft/main/Microsoft/Wordiness.yml

  # Plain Language simple-words page: HTML, parseable
  curl -s https://www.plainlanguage.gov/guidelines/words/use-simple-words-phrases/
  ```

  Prefer a raw fetch over a small-model summariser. The YAML structure is the value, and a paraphrase loses entries. If the runtime only offers an HTTP-fetch-via-LLM tool (for example WebFetch in Claude Code), instruct it to return the file verbatim, or skip it and use shell.

  Pull the lists into context once per session for tasks that need them. Do not commit a copy to the skill. The upstream lists drift, and a stale embedded copy is worse than a fresh fetch.

  Exception: keep the original word when the common synonym means something different. Two classes to watch for:

  1. **Domain nouns** carrying specific technical meaning: "hash", "salt", "quorum", "commit", "fork", "rebase". "Scramble", "spice", "majority", "save", "branch", and "redo" do not mean the same thing.
  2. **Specification verbs** carrying obligation, contract, or condition semantics: "requires", "must", "shall", "returns", "raises", "accepts", "rejects". These are not formal synonyms for "needs", "has to", or "gives back". They encode the contract of an API or protocol. RFC 2119 defines "MUST", "SHALL", "SHOULD", and "MAY" as load-bearing terms; treat their lower-case cousins the same way in specifications.

  The rule targets formal-sounding general vocabulary, not load-bearing technical or contractual terms. *([PL], [MS], [Kobak], [RFC 2119].)*

## Sources

- [G] [Google Developer Documentation Style Guide](https://developers.google.com/style)
- [MS] [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)
- [Apple] [Apple Style Guide](https://support.apple.com/guide/applestyleguide/welcome/web)
- [IBM] [IBM Style (public mirror)](https://stylepedia.net/style/)
- [GOV] [GOV.UK Content Design Guide](https://www.gov.uk/guidance/content-design)
- [GL] [GitLab Documentation Style Guide](https://docs.gitlab.com/development/documentation/styleguide/)
- [PL] [Federal Plain Language Guidelines (plainlanguage.gov)](https://plainlanguage.gov/guidelines/)
- [CMS] [Chicago Manual of Style](https://www.chicagomanualofstyle.org/)
- [MC] [Mailchimp Content Style Guide](https://styleguide.mailchimp.com/)
- [RH] [Red Hat Supplementary Style Guide](https://redhat-documentation.github.io/supplementary-style-guide/)
- [BB] [AI-Written Specifications: When the Documentation Looks Great but It's Wrong (Byborg Engineering, Medium)](https://medium.com/byborg-engineering/ai-written-specifications-when-the-documentation-looks-great-but-its-wrong-a0ae0c689480)
- [CB] [conorbronsdon/avoid-ai-writing SKILL.md](https://github.com/conorbronsdon/avoid-ai-writing/blob/main/SKILL.md)
- [Kobak] [Kobak et al., "Delving into ChatGPT usage in academic writing", Science Advances / arXiv:2406.07016](https://arxiv.org/abs/2406.07016v5). Measured a sudden, large increase in formal vocabulary ("delves", "underscores", "showcasing", "crucial") in PubMed abstracts after ChatGPT's release. Empirical basis for the common-words-over-fancy-synonyms rule.
- [RFC 2119] [Bradner, "Key words for use in RFCs to Indicate Requirement Levels", IETF RFC 2119 (1997)](https://datatracker.ietf.org/doc/html/rfc2119). Defines "MUST", "SHALL", "SHOULD", "MAY" as load-bearing specification terms. Cited in the common-words rule's exception for specification verbs.

## Example transformation

> AI default (PERSONALITY AND SOUL): "I looked around in May 2026 and didn't find anything quite like it. Forgettable."
>
> Neutral preset: "A May 2026 search of public material did not surface a comparable pattern. The approach is not memorable in isolation."
