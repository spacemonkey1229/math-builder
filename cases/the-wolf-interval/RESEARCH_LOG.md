# RESEARCH_LOG — The Wolf Interval

One row per placeholder opened by case-write.

| # | Placeholder | Searched | Found | Outcome |
|---|---|---|---|---|
| P01 | Pure perfect fifth ratio (3/2) and pure octave ratio (2/1) | Direct WebFetch of Wikipedia's "Pythagorean comma" article (a tier-2 republication of a standard, universally-agreed mathematical definition — not a disputed or measured quantity, so no tier-1 "primary publisher" search was needed the way a market price would require). | Page states the derivation explicitly: the comma is defined from "twelve justly tuned perfect fifths" (3:2 each) compared to "seven octaves" (2:1 each), ratio 3^12/2^19 = 531441/524288, ~23.46 cents. | **SOURCED** as S1, confidence HIGH. Definitions are unambiguous and dated to the access day (2026-09-17). |
| P02 | 1200×log2(ratio) cents formula | Same fetch as P01 — the cents formula and the comma's cents value are stated on the same page. | "Measured in cents, the interval spans approximately 23.46 cents." | **SOURCED** as S1 (folded into the same source row; it is the same claim, not a separate fact needing a separate source id). |
| P03 | 12-tone equal temperament semitone ratio (2^(1/12)) and equal-tempered fifth ratio (2^(7/12), ~700 cents) | Direct WebFetch of Wikipedia's "Equal temperament" article. | Page states the semitone ratio is the 12th root of 2 (~1.05946), the equal-tempered fifth is 2^(7/12) ≈ 1.498 = 700 cents, versus the pure 3:2 fifth's 701.96 cents — a 1.96-cent difference. | **SOURCED** as S2, confidence HIGH. |
| P04 | Pythagorean comma's size in cents, independently checked | Not searched further — this is this case's own arithmetic (Appendix B), not a separate lookup. Cross-checked two ways: (a) direct calculation, `1200 * log2(531441/524288)` = 23.460010384649014, matching S1's stated ~23.46 cents; (b) S2's independently-stated "~1.96 cents narrower per fifth" × 12 fifths = 23.52 cents (small rounding drift from stating a per-fifth figure to 2 decimals, consistent with S1's more precise total). | Both independent sources agree with the case's own direct calculation, within the rounding each source itself displays. | **VERIFIED**, not a separate source id — this is the case's own derived arithmetic from S1/S2's definitions, shown in full in Appendix A/B, `derived: true` in spirit (case.json marks the underlying S1/S2 rows `derived: false` since they are definitional, and treats the comma/per-key averages as this case's own shown arithmetic rather than a third citable claim). |

## What was NOT researched, and why

- **The Cantilena Consort, the Fenice, and the season repertoire (Appendix C).** This is a
  constructed scenario, not a claim about a real ensemble, a real instrument, or a real concert
  season — SPEC §5's "never fabricate a number" targets real-world facts a case claims are true;
  it does not require a citation for a fictional business's own invented calendar, the same way
  Fermenter's Rosa Delgado or Cold Chain's clinic route needed no citation for their own fictional
  specifics. No number in Appendix C is presented as sourced or verifiable, and the case says so
  explicitly in Appendix C's closing note.
- **A real historical harpsichord customer, shop, or specific historical wolf-interval placement
  convention.** Per the original concept sheet's own scoping note, this stays a constructed
  scenario on purpose. The only numbers that needed sourcing were the mathematical/definitional
  ratios (S1, S2) — the concept's own "Data feasibility: HIGH" call was correct: the core math
  needs no external dataset, only agreed-on definitions.
- **A specific enharmonic location for the "wolf" fifth** (e.g. whether it lands at G#-D#/Ab-Eb or
  elsewhere) was considered and deliberately NOT stated as a specific fact, because real
  historical builders placed it differently depending on the instrument and repertoire — stating
  one specific location as fact would be exactly the kind of plausible-but-unverifiable claim SPEC
  §5 prohibits. Appendix B states only what is provable: it is whichever fifth closes the loop
  back to D, without over-specifying its enharmonic spelling. (Flagged by the P1 cold-solve dry
  run, 2026-09-17 — see QA_REPORT.md.)

## Zero `{{NEEDS_SOURCE}}` remain

Verified 2026-09-17: `grep -c '{{NEEDS_SOURCE' cases/the-wolf-interval/case.md` returns 0. All four
opened placeholders resolved to SOURCED; none were dropped or converted to a Modeling Assumption —
this case needed neither, since every load-bearing figure is a citable mathematical definition, not
a disputed or unmeasurable real-world quantity.

Next step: `Run case-readiness on the-wolf-interval.`
