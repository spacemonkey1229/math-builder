# Research Log — Acton Survey

4 open placeholders from `case-write`. All 4 resolved: 3 SOURCED, 1 ASSUMPTION. Zero remain OPEN.

## P01 — Appendix B campus roster summary table

**Searched:** N/A — this is real, complete internal data already in hand, not something to
web-search. Computed directly from `source/Y2/Session 5/Acton Survey/2021 Learners At Campuses
With At Least Two Studios_ ID Numbers, Gender, Age and Location.xlsx` (1,420 rows, one per
learner, real 2021 Journey Tracker export).

**Method:** Python (`openpyxl`) read all 1,420 rows, grouped by the `Acton Campus` column
(50 distinct campuses), counted learners per campus, computed each campus's percent of the total
1,420, then computed the stratified proportional allocation `n_i = round(142 * N_i / 1420)` for
each campus. Raw floor-rounding of all 50 shares summed to 134, 8 short of the 142 target — the
**largest-remainder method** (S3) was applied: the 13 campuses (the arithmetic actually required
distributing 13, not 8 — floors from `int()` truncation differ slightly from naive floor-rounding
of the displayed percentages) with the largest fractional remainder each received one additional
learner, until the total reached exactly 142. Verified: `sum(alloc.values()) == 142`.

**Found:** Full 50-campus table, reproduced in `case.md` Appendix B. Campus sizes range 12–168;
37 of the 50 campuses (74%) have only 12 learners each — this is real and it is the whole reason
the case's dilemma is genuinely load-bearing.

**Outcome:** SOURCED — S1, HIGH confidence (real, complete population data; internal roster, not
independently re-verifiable via a public URL, same treatment as `cases/family-trip`'s own
screen-captured historical source data).

## P02 — Hypergeometric distribution citation

**Searched:** (1) "hypergeometric distribution NIST engineering statistics handbook definition
sampling without replacement" — NIST's own ITL handbook did not surface a direct hypergeometric
page in this search pass (found only a 1997 NIST DATAPLOT software-manual PDF, not a clean
citable reference for a student appendix); (2) "site:itl.nist.gov hypergeometric distribution" —
same result, no clean NIST page. Fell back to tier-2: a well-attributed open educational
statistics text.

**Found:** Statistics LibreTexts, "5.5: Hypergeometric Distribution" (Rachel Webb, Portland State
University, *Mostly Harmless Statistics*). Fetched and confirmed the page states the formula
P(X=x) = aCx·bC(n−x) / NCn, mathematically identical to `case.md` Appendix C's
P(zero) = C(N−N_i, n)/C(N, n) with x=0.

**Outcome:** SOURCED — S2, HIGH confidence (named author, institutional OER, formula verified by
direct fetch, not just a search snippet).

## P03 — Largest-remainder / Hamilton apportionment citation

**Searched:** "largest remainder method Hamilton apportionment definition explanation."

**Found:** Mathematics LibreTexts, "Section 7.12: Apportionment – Hamilton's Method" (Orange Coast
College, *Math in Plain Sight*). Fetched and confirmed: "Assign each group its lower quota...
Distribute the remaining seats/items, one at a time, to the groups with the largest fractional
parts... until all seats/items are assigned" — matches the procedure applied to Appendix B exactly.
Real historical note: first proposed by Alexander Hamilton in 1792, used for the actual U.S. House
of Representatives 1852–1900.

**Outcome:** SOURCED — S3, HIGH confidence (named institutional OER, formula/procedure verified by
direct fetch).

## P04 — Guide-coordination call length

**Searched:** (1) "average length school administrative scheduling phone call minutes" — no
citable public figure for this specific internal step; the closest tangential real precedent found
was "Friday Fifteens," a documented 15-minute superintendent-principal check-in practice (Edutopia),
which is suggestive but not a defensible direct citation for an Acton guide-scheduling call.
(2) No second framing found anything closer to a public, dated, on-point figure.

**Outcome:** **NOT FOUND — Modeling Assumption (MA1).** No public data exists for the duration of
an internal school-network scheduling call of this specific kind; genuinely no primary or secondary
source addresses it. Declared as a stated Modeling Assumption at **15 minutes**, anchored to the
low end of the case's own real, stated 15–20 minute learner-call bracket (Appendix A) — a
coordination call has no interview content, only logistics, and is realistically shorter than a
full learner interview. Placed in a visible `Modeling Assumptions` block (Appendix E, MA1), not
buried in the Appendix D table as though it were sourced. Sensitivity: flexed ±50% (and the
Guide Notes twist pushes it to the top of the case's own stated 15–20 minute bracket, 20 minutes,
rather than past it) in `sensitivity_model.py` — the primary-metric winner (Option A) never flips
under any tested flex; only the margin size moves. Reported honestly, not forced to flip.

## Supplemental: sample-fraction convention (not a placeholder, but checked)

Also searched "survey sample size rule of thumb 10 percent of population finite population
methodology" to sanity-check the case's own stated 10% target. Found a real, commonly cited rule
of thumb (tools4dev.org, echoing several survey-methodology sources): "A good maximum sample size
is usually around 10% of the population, as long as this does not exceed 1,000." This is consistent
with, though not the sole justification for, Jeff and Xander's stated 142-learner (10%) target —
which `case.md` presents as their own scenario decision (like a stated budget), not an externally
sourced fact, so no `{{NEEDS_SOURCE}}` placeholder was created for it at write time.

## Verification

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources (must not be load-bearing): []
```

Next step: run `case-readiness` on `acton-survey`.
