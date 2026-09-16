---
name: case-context
description: "Source and place the real-world (non-math) explanatory content a case needs to be readable by a student with zero background in its setting — a story glossary of 2-4 real-world terms, at least one real visual (a photo/diagram with traceable provenance, or a hand-drawn SVG when no real image clears the bar), and a one-line why-this-methodology note per deliverable. Use when the user says \"add context to the case\", \"source some background material\", \"this case needs explaining\", \"find an image for the case\", \"the terms aren't explained\", or after case-research reports all numeric placeholders closed. Runs after case-research, before case-readiness. Never touches a load-bearing numeric figure — that stays case-research's job."
---

# case-context — real-world explanation, sourced like everything else

Stage between `case-research` and `case-readiness`. `case-research` sources every number the case's
*math* needs. This skill sources everything the case's *setting* needs — the vocabulary, the
picture, the "why this order of operations" reasoning — so a student with no background in
harbor piloting, contact tracing, or hardwood milling can still follow the story. Tier 2's P7
probe (MCS-48) checks the result; this skill is what produces it, so authoring stops relying on a
QA probe catching an absence a month after publish.

> The corpus-wide fix this project's own QA history keeps re-discovering (STORY_GLOSSARY on
> apron-order, then retrofitted onto lebron-vs-michael, tide-window, six-degrees-of-exposure,
> the-special-order, flow-state, gerrymandering — six separate after-the-fact repairs in one
> project) is proof this needs to be a pipeline stage, not a QA finding.

## Inputs

- `cases/<id>/case.md` and `cases/<id>/case.json` with `sources[]`/`needs_source[]` closed by
  `case-research`.
- Tools: `WebSearch` and `WebFetch` (load via ToolSearch if deferred).

## Outputs

- `cases/<id>/case.json` — `sources[]` gains 2-4 new context/visual entries (same schema as a
  data source: `id`, `claim`, `org`, `title`, `url`, `accessed`, `confidence`, `note`), plus a new
  `context_glossary[]` array: `[{term, desc, link, source_id}]`.
- `cases/<id>/case.md` — the chosen terms appear, in-context, somewhere in Overview/Background/
  Dilemma/Challenges/Appendices (not invented as a standalone vocabulary list divorced from the
  narrative), and a short "Context Sources" note naming what was added and why.
- The published HTML's `STORY_GLOSSARY` object, its `.sterm` wiring, and any `<figure>` — hand-
  placed to match `case.json.context_glossary[]`/`sources[]` until a templated generator exists
  (there isn't one yet; see "Known gap" below).

---

## Confidence tiers — reuse case-research's rubric, don't invent a stricter one

This was a real, live mistake (caught 2026-09-16): treating "reputable outlet republishes an
image with a named attribution" as *disqualifying* rather than as exactly what
`skills/case-research/SKILL.md`'s own Tier 3 = MEDIUM already covers. **The rubric is the same
one case-research already uses** — there is no separate, stricter bar for context/visual
material:

| Tier | Source class | Grade | Usable for context/visual? |
|---|---|---|---|
| 1-2 | Primary publisher, or an institution republishing it with attribution | HIGH | Yes |
| 3 | Reputable journalism/outlet naming a real source (incl. Wikimedia Commons with a real uploader and file history) | MEDIUM | **Yes** — this is the normal case, not an edge case |
| 4 | Undated blog/forum/AI-summary with no traceable provenance | LOW | Only as explicitly-labeled decorative noise; never for a claim a student is meant to rely on |

The one real distinction that matters: **is this material load-bearing for the graded math, or
is it illustrative/explanatory?** A LOW-confidence figure may never carry a constraint or a
dilemma-flipping quantity (case-research's rule, unchanged). A MEDIUM-confidence *image or
glossary term* is completely normal — most of this corpus's existing STORY_GLOSSARY links are
MEDIUM-tier Wikipedia pages, and that's fine, because nothing about "a term is explained" is a
graded quantity. Don't apply data-figure strictness to a sentence that just tells a 14-year-old
what a "kerf" is.

## The "fit" test — which 2-4 terms/visuals actually make the cut

Sourcing something real is necessary but not sufficient. A glossary of correct-but-irrelevant
trivia is as useless as no glossary. A candidate term or image is a **fit** only if it clears all
four:

1. **It's already in the case.** The term appears verbatim somewhere in `case.md`'s own
   Overview/Background/Dilemma/Challenges/Appendices, or a visual would illustrate a scene,
   object, or mechanism the case's own narrative describes. Do not import a generic "fun fact"
   about the setting that the case never actually mentions — that's decoration, not
   accessibility.
2. **It would stop a genuinely fresh reader.** Ask, term by term: would someone with zero
   background in this setting (not zero math background — zero *setting* background) need to
   look this up to follow the sentence it's in? If a plainer synonym already sits next to it in
   the sentence, or context makes the meaning obvious, it doesn't need a glossary entry — adding
   one anyway just clutters the card. This is literally Tier 2 P7's own test
   (`skills/case-readiness/scripts/tier2_probes.py`, `probe_accessibility`); running that probe's
   prompt yourself, in character as a zero-context reader, before publishing is the actual
   fit-check, not a proxy for it.
3. **It doesn't leak the case.** No context term, image caption, or diagram may state or imply a
   verdict, margin, or computed result — same no-answer-leak rule that already governs every other
   part of the case.
4. **It's real and cited**, at minimum MEDIUM confidence per the table above. Never fabricate a
   definition or invent a citation to clear the 2-4 minimum — an honest 1 beats a padded 3.

If fewer than 2 terms clear all four bars, ship fewer than 2 and say so in the Context Sources
note — the same "an honest hole beats a fabricated fill" principle `case-research` already
applies to numeric placeholders. If a case's setting is already fully self-explanatory (rare, but
real — a case set in a school cafeteria needs no glossary), record that explicitly rather than
padding.

## Visual sourcing, specifically

Prefer, in order:

1. A real photo or diagram with traceable provenance (a named photographer/creator, a real
   institution, or Wikimedia Commons with real file history and an explicit license) —
   Tier 1-3/HIGH-MEDIUM per the table above. Embed as `<figure><img src="..."><figcaption>...
   credit + license...</figcaption></figure>`, matching the pattern already in
   `cases/tide-window/published/` and `cases/lebron-vs-michael/published/`.
2. A hand-drawn, self-contained inline SVG when no real image clears the bar for this specific
   case, or when a diagram needs to show this case's own invented numbers (which a real photo
   obviously can't) — matching `cases/roofline-call/` and `cases/the-trailer-return/`'s
   convention. An invented illustrative example (not this case's real numbers) is fine and should
   say so in a caption, same as `cases/gerrymandering/`'s Appendix B population chart.
3. Nothing, with a note explaining why (a genuinely abstract topic with no natural visual) — never
   force a decorative image that adds nothing.

A found real image with the *wrong* license (all-rights-reserved stock photography, a paywalled
outlet's own uncredited graphic) is not usable regardless of how well it illustrates the point —
license is a hard gate the confidence tier does not override.

## Known gap — no templated generator yet

As of 2026-09-16, `STORY_GLOSSARY`/`.sterm`/`<figure>` placement in `published/*.html` is still
hand-authored per case (by whoever runs this skill), not generated from `case.json.
context_glossary[]` by `case-publish`. Until that generator exists, this skill's author is
responsible for keeping the published HTML in sync with `case.json` by hand, and
`tier1_structural.py --case <id>` (T1-21 for the glossary mechanism, T1-20 for visual presence)
is the only thing standing between "recorded in case.json" and "actually reaches the student." A
future improvement: teach `case-publish` to render `context_glossary[]` into the HTML directly,
the same way it already renders `sources[]` into the Sources appendix table, closing this gap for
good.
