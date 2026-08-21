# Navigation — Research Log

Navigation's premise is set in **Modus City, a fictional city** (source docx, `Portfolio13_Modus03.jpg`).
Nearly every quantitative fact the case needs — the route's segment distances, road types, posted
speed limits, stop-sign counts and turn-timing penalties, and the $10,000+ fine/license-loss
penalty — is fictional scenario canon Filberto is stated to already know, the fictional analogue of
"given data" rather than a claim about the real world. Per `skills/case-write/SKILL.md`'s
placeholder discipline, none of these needed a `{{NEEDS_SOURCE}}` placeholder: they are not
presented as real, externally-checkable facts, so SPEC §5's "cited or a declared assumption" rule
does not apply to them the way it would to a real city's real speed limits.

Two things in the case genuinely needed real-world grounding, and both are placed as sourced
figures in `case.md` Appendix E:

| Placeholder | What was needed | Outcome |
|---|---|---|
| P01 | A real dollar figure for "one year of Filberto's income," to price D4's license-loss exposure (Appendix D, MA1) | **SOURCED** — O*NET OnLine, reporting 2025 BLS wage data for Taxi Drivers (53-3054.00): median annual wage $42,100. `https://www.onetonline.org/link/summary/53-3054.00`. Fetched directly, 2026-08-20. HIGH confidence: BLS-sourced, dated, unambiguous units, directly the figure needed. |
| P02 | Real-world grounding that Modus City's $10,000+ camera-enforced penalty is a plausible, if severe, *kind* of consequence — supplemental context per SPEC §1.6, not load-bearing in any calculation | **SOURCED (context only)** — SpeedingCost.com's national average calculator: $150-$300 for an ordinary 10-mph-over highway violation including court fees, updated June 2026. `https://speedingcost.com/`. Fetched directly, 2026-08-20. MEDIUM confidence: a calculator/aggregator site with an explicit "estimates are for educational purposes only" disclaimer, used only for comparison, never as an input to Appendix C or D's arithmetic. |

## What was searched and rejected

- **BLS's own Occupational Outlook Handbook page** (`bls.gov/ooh/transportation-and-material-moving/taxi-drivers-and-chauffeurs.htm`)
  was the first-choice tier-1 primary source for the taxi-wage figure. A WebSearch snippet reported
  $36,220 (May 2024) from this page, but a direct `WebFetch` of the URL returned HTTP 403 (bot-blocked)
  and could not be independently confirmed by fetch. Re-sourced to O*NET OnLine instead, which
  fetched successfully and republishes more recent (2025) BLS wage data with clear attribution and
  a directly quoted figure ($42,100). The ~$5,900 difference between the two years/sources is noted
  here rather than silently reconciled — Appendix D's MA1 already frames the $42,100 figure as a
  conservative *floor* (one year, not Filberto's full remaining career), so a few thousand dollars
  of drift in the base annual figure does not change the case's qualitative argument.
- **Visual Capitalist's "Mapped: Speeding Ticket Costs by State"** was the first-choice source for
  the real-world speeding-ticket grounding figure (a well-known, frequently cited data
  visualization piece). Direct `WebFetch` returned HTTP 403 (bot-blocked). Re-sourced to
  SpeedingCost.com, which fetched successfully; downgraded to MEDIUM confidence accordingly, and
  kept explicitly non-load-bearing (P02 above) since it is a calculator site, not a primary
  publisher.
- No attempt was made to source real driving-time or real street-level data for "Modus City,"
  because Modus City is explicitly fictional (the source docx's own map is a stock neighborhood-map
  template, not a real place) — treating any of its streets, distances, or drive times as
  real-world claims requiring citation would be a category error, not a research gap.

## Verification

```
placeholders remaining in case.md: 0
citation markers with no source row: none ([S1], [S2] both resolve — used narratively in
  Appendix E rather than inline [S1]/[S2] markers elsewhere in the document, since neither figure
  appears as a bare number anywhere else in case.md)
source rows never cited: none
LOW-confidence sources: none
```

`modeling_assumptions[]` (case.json): MA1 (license-loss duration) — the only stated scenario
assumption in this case; see `case.md` Appendix D.

Next step: `case-readiness` — run the preflight linter, Tier 1, then Tier 2's six probes.
