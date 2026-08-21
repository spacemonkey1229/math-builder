# Research Log — Movie Executive

Stage 3 (`case-research`). This case-write pass shipped with **zero** `{{NEEDS_SOURCE}}`
placeholders in `case.md` because the load-bearing figures are of two kinds, neither of which
takes the placeholder path:

1. **The two films' fictional data** (production budgets, survey sample sizes, sampling methods,
   and the individual respondent rows in Appendix A/B) — these are the case's own given data, the
   same authorial latitude used for Catering's blank order appendix and Archery Camp's Appendix B
   field-range table. They do not describe anything real and are not researchable; case-write
   fixed them directly rather than routing them through `{{NEEDS_SOURCE}}`. See
   `case.json.legacy_conversion_note` for exactly which of these numbers are carried over from the
   original 2021 source document versus newly designed for this conversion (the per-respondent
   scatter rows are new; the sample sizes, sampling methods, budgets, genres, and ratings are the
   source's own stated facts).
2. **Three real, external claims** used as context/inputs for Appendix D and the facilitator-only
   Twist — these WERE researched this stage, below.

## P01 — Average U.S. movie ticket price

**Used for:** Appendix D real-world pricing context (the case does not use this figure as an
input to the revenue projection itself — D4/D5's ticket prices come from the survey data).

- Searched: "National Association of Theatre Owners average US movie ticket price 2024 2025".
  Found conflicting numbers across secondary sources ($10.50-$10.84) with inconsistent years and
  no clear single current-year NATO figure.
- Fetched the Yahoo republication of the IndieWire piece reporting NATO's own annual-report
  number directly: **$10.53 for 2022**, the first NATO/Cinema United had released in three years
  at the time (published March 9, 2023).
- Attempted to reach `natoonline.org` and its successor `cinemaunited.org` directly for a more
  current figure — both returned dead/redirected/404 pages during this research pass (NATO
  rebranded to Cinema United in March 2025, and the data page did not resolve).
- **Outcome: SOURCED, HIGH confidence.** Used the 2022 NATO figure. Confidence was considered for
  a staleness downgrade to MEDIUM, but kept at HIGH because it is NATO's own primary reported
  figure (not a third-party estimate) and is used only as background market context, not as a
  load-bearing calculation input. Recorded as `sources[].S1`.

## P02 — Marketing (P&A) budget as a share of production budget

**Used for:** D6's marketing-budget recommendation.

- Searched: "film marketing P&A budget percentage of production budget rule of thumb industry".
- Fetched thoolie.com's P&A guide directly. Real figures cited there: Get Out (production $4.5M,
  P&A ~$30M, ~6.7x), Paranormal Activity (production $15K, P&A ~$18M), The Nun (production $22M,
  P&A $25-35M) — all real examples of P&A meeting or exceeding production budget for a wide
  release. The article also states a lower-end industry rule of thumb of 20-30% of production
  budget for a baseline marketing allocation.
- Considered a more precise/authoritative source (e.g., MPA annual reports) but could not locate
  a public, dated, primary-source figure giving an exact P&A-to-production ratio in the time
  available — the real industry pattern is genuinely a wide range depending on film type, not a
  single number, which the article itself says explicitly.
- **Outcome: SOURCED, MEDIUM confidence** (industry guide, not a primary trade body; a range, not
  one figure; no explicit publication date on the article). Recorded as `sources[].S2`. Because
  the underlying reality is genuinely a range, D6 asks Heroes to recommend a marketing budget
  *range*, not force a single false-precision number — the case's design follows the source's own
  honesty about the spread, rather than manufacturing precision the source doesn't have.

## P03 — How much statistical correction can recover from a convenience-sample's selection bias

**Used for:** FACILITATOR.md's Twist (facilitator-only; never appears in `case.md`, per SPEC
§7.2's discussion-reveal doctrine).

- Searched: "Pew Research nonprobability convenience sample selection bias correction weighting".
- Fetched/confirmed via search summary of Pew Research Center's "Evaluating Online Nonprobability
  Surveys" (May 2, 2016): across 24 real benchmark comparisons, the best-performing weighting
  method reduced average estimated bias from 8.4 to 6.0 percentage points — roughly 30% of the
  bias corrected, about 70% remaining uncorrectable.
- **Caveat, stated in `sources[].S3.note`:** Pew's study covers online opt-in panels specifically,
  not in-person theater-lobby convenience samples like Flower's Ice's. It is the best available
  real research on the *general principle* (convenience-sample bias is only partially correctable
  by statistics after the fact), which is what the Twist actually teaches — not a claim that Pew
  studied movie surveys.
- **Outcome: SOURCED, HIGH confidence** (primary respected research organization, dated, clear
  methodology, real benchmark count). Recorded as `sources[].S3`.

## Rejected / not pursued

- **`the-numbers.com/market/`** — the original source document's own Appendix D link, and a real,
  well-known box-office data site. Returned HTTP 403 to this session's automated fetch tools
  (likely bot-blocking, not a dead site). Rather than cite a link this pipeline's own P6 data-decay
  probe could not verify as reachable, it was dropped from Appendix D entirely rather than risk an
  unverifiable citation. `cinemaunited.org/data/ticket-price/` (NATO's rebranded successor site)
  returned a live 404 during this pass and was likewise not cited directly — the NATO figure is
  instead sourced through the dated news republication (S1) that quotes it.
- **A precise national "addressable opening-weekend audience for a genre" figure** — searched
  briefly for real per-genre opening-weekend attendance benchmarks; found only aggregate industry
  totals (e.g., total annual domestic admissions, total annual wide-release count) that would
  require a multi-step, low-confidence derivation to reach a single genre-specific number for two
  *fictional* films. Correctly returned **NOT FOUND** and taken to the Modeling Assumption exit
  (SPEC §5) instead of a fragile derivation dressed up as a citation — recorded as `case.json`
  `modeling_assumptions[].MA1`, with its basis stated and its (lack of) effect on the verdict
  disclosed honestly (it cancels out of the revenue-per-dollar ratio between the two films).

## Verification pass

```
placeholders remaining in case.md: 0
citation markers [S#] used in case.md: S1, S2 (Appendix D)
sources[] rows: S1, S2, S3 — all complete (claim/value/org/title/url/accessed/confidence)
LOW-confidence sources: none
```

Next step: `Run case-readiness on movie-producer.`
