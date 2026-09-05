# RESEARCH_LOG.md — The Quiet Thief

Stage 3 (`case-research`) run 2026-09-04. 6 `{{NEEDS_SOURCE}}`-class tokens enumerated from the
case's concept (concept brief's "primary_metric" and "sourcing note" §5): one shared retirement
age, one nominal-return figure, one inflation figure, and three scenario constants (ages,
contribution amount, retirement-age delay) resolved as disclosed Modeling Assumptions. One row per
token: what was searched, what was found or rejected, and the disposition.

---

**P01 — Shared target retirement age (Appendix A, Appendix B)**

Searched: "Social Security full retirement age," ssa.gov directly. Found: SSA's Benefits Planner
states full retirement age (FRA) is **67** for anyone born in 1960 or later — a fixed, non-
projected policy figure that applies with no ambiguity to both Priya and Jordan (both well under 60
in the case's present day). This is the identical figure and identical source already used in
`cases/the-bracket-bet/case.json` [S4 there], re-verified independently for this case (fetched
2026-09-04, same content). **Disposition: SOURCED**, HIGH confidence — official, stable,
unambiguous.

**P02 — Long-run average annual nominal rate of return (Appendix C)**

Searched for a real, cited long-run diversified/index benchmark, same search strategy as
`cases/the-bracket-bet`. Two independent aggregators agree closely: The Motley Fool states
**9.98%/year** CAGR for the S&P 500 since 1928 (dividends reinvested); officialdata.org
independently states **10.22%/year** since 1928 (dividends reinvested, "1928 to 2026" per its live
page). Attempted a direct fetch of the primary academic dataset this figure ultimately traces to
(Aswath Damodaran's NYU Stern historical-returns table, `histretSP.html`) to see whether a headline
CAGR was stated there directly — the page instead publishes only raw year-by-year returns with no
summary CAGR/average printed on the page itself, so computing a long-run average directly from that
raw table would require summing/compounding ~98 individual annual return rows by hand, an
error-prone derivation given the row count. Used the two well-attributed secondary aggregators
instead (tier 2/3, not primary, but tightly corroborated and undisputed), exactly as
`cases/the-bracket-bet/case.json`'s S5 already does for the identical claim. Rounded to a clean
**10%/year** for modeling, disclosed as a rounding choice. **Disposition: SOURCED**, MEDIUM
confidence (reputable aggregators, not primary, but tightly corroborated: 9.98% vs. 10.22%).

**P03 — Long-run average annual U.S. inflation rate (Appendix C)**

Searched BLS.gov and Federal Reserve sources directly for a long-run CPI average, since this is the
figure this case is named for and the rubric trap (D5) depends on it being genuinely distinct from
the nominal return. Found the Federal Reserve Bank of Minneapolis's "Consumer Price Index, 1913-"
page, which publishes the CPI-U index (1982-84=100 base) year by year from 1913 to 2025. The page
itself states index values rather than a single headline average-inflation percentage, so the
long-run average annual rate was **derived** from the two endpoint index values: 1913 index = 9.9,
2025 index = 321.9. CAGR = (321.9 / 9.9)^(1/112) − 1 ≈ **3.1%/year**. Cross-checked this derivation
against multiple independent secondary aggregators (usinflationcalculator.com, rateinflation.com,
a general web search synthesizing BLS-based sources) which describe the long-run average since 1913
as "approximately 3.1%–3.2%" — consistent with the derived figure, corroborating it rather than
contradicting it. **Disposition: SOURCED (derived)**, HIGH confidence — the Minneapolis Fed is a
primary, official publisher of this BLS-sourced series (not a third-party aggregator), the
derivation arithmetic is simple and shown in full above, and the result is independently
corroborated.

**P04 — Priya's and Jordan's starting ages (Appendix D, MA1)**

No external source exists or is needed for two fictional protagonists' stated ages — this is a
narrative/scenario constant, not a researchable fact, exactly as Devon's age (24) was treated in
`cases/the-bracket-bet`. Set to Priya 25, Jordan 35 (a clean, round ten-year gap) — the exact
scenario the approved concept brief specifies. **Disposition: ASSUMPTION (narrative, scenario
constant)** — recorded in the visible Modeling Assumptions block (MA1) per SPEC §5, not buried in a
data table.

**P05 — Both savers' monthly contribution amount (Appendix A, Appendix D MA2)**

Considered grounding this in a specific salary-and-savings-rate derivation, as
`cases/the-bracket-bet` did for Devon's $3,000/year IRA contribution (BLS salary anchor × a
savings-rate guideline). Decided against replicating that chain here: this case's pedagogical
point is specifically the *mechanics* of catching up (the interaction of a start-date gap with
compounding and inflation), not what a specific income level can or cannot afford — introducing a
salary anchor would add an unnecessary, unrelated variable without changing any of the case's
actual math (see the MA2 sensitivity note: the dollar figure scales every result proportionally but
does not move the D4 margin or the D5 understatement percentage, both of which are pure ratios).
Set to a common, round **$400/month** figure. **Disposition: ASSUMPTION (scenario constant)**,
disclosed with an explicit sensitivity note establishing it is non-load-bearing for the case's two
key percentages (D4's 13.66% margin, D5's 49.11% understatement).

**P06 — Extended Plan's retirement-age delay length (Appendix B, Appendix D MA3)**

Not a researchable real-world fact — this is the case-design lever used to tune the balance test.
Ran the actual model (see "Balance-test verification" below) at 1-year, 2-year, and 5-year delays
before settling on the final value:

| Delay | Extended Plan months | PMT_B | Margin vs. Bridge Plan (D3 = $817.00) |
|---|---|---|---|
| 1 year | 396 | $758.90 | 7.11% |
| **2 years (chosen)** | **408** | **$705.38** | **13.66%** |
| 5 years | 444 | $568.32 | 30.44% |

A 1-year delay (7.11%) landed below the concept brief's 10–15% target band; a 5-year delay blew well past
SPEC §2's 20% cap into landslide territory. **2 years lands squarely inside the target band**
(13.66%) without engineering the exact percentage — the delay length was chosen by testing
realistic, round candidate values and taking the one that produced a genuine, defensible margin, not
by solving backward for a specific target number. **Disposition: ASSUMPTION (case-design constant)**,
disclosed in `case.json.sensitivity_disclosure[]` as Category D (a deliberate, disclosed case-
balance dial), consistent with the disclosure taxonomy in `skills/case-readiness/SKILL.md`.

---

## Balance-test verification (the critical check)

Ran the case's own stated model (`case.json.balance.margin_basis`, matching `argument_a`/
`argument_b`):

1. Real annual rate of return: (1 + 0.10) / (1 + 0.031) − 1 = 1.10 / 1.031 − 1 ≈ **6.6925%**
   (displayed as 6.69%) [S2, S3 combined, D1].
2. Real monthly rate: (1.066925)^(1/12) − 1 ≈ **0.5413%/month**.
3. Priya's real target balance (504 months at $400/month, ordinary annuity):
   FV = 400 × [(1.005413)^504 − 1] / 0.005413 ≈ **$1,048,768.04** (D2).
4. Bridge Plan (384 months): PMT_A = FV × r / [(1+r)^384 − 1] ≈ **$817.00/month** (D3) — about
   2.04× Priya's $400/month.
5. Extended Plan (408 months): PMT_B = FV × r / [(1+r)^408 − 1] ≈ **$705.38/month** (D4) — about
   1.76× Priya's $400/month.
6. Margin: (817.00 − 705.38) / 817.00 × 100 ≈ **13.66%** — comfortably inside the concept brief's
   10–15% target band and well under SPEC §2's 20% cap.
7. Nominal-rate trap (D5): using the nominal 10% rate directly (monthly nominal rate ≈ 0.7974%)
   instead of the derived real rate, in the Bridge Plan's PMT formula (still 384 months):
   PMT_naive ≈ **$415.79/month** — a **49.11%** understatement of the true $817.00 figure.

All figures independently reproduced in `sensitivity_model.py`'s `__main__` block; both match to
the cent. No retune of Appendix A/C's sourced figures was needed — only Appendix D's MA3 delay
length (a disclosed design constant, not a real-world figure) was tested against a few candidate
values to land the margin in-band, exactly the kind of constraint-tuning `skills/PIPELINE.md`'s
"what goes backwards" table describes as the correct lever for an out-of-range margin (here, used
proactively during the initial write/research pass rather than as a later remediation).

## Not used / rejected

- Considered deriving the long-run S&P 500 CAGR directly from Damodaran's own raw
  `histretSP.html` year-by-year table rather than citing secondary aggregators, since that table is
  the primary source those aggregators themselves draw from. Rejected for this pass: the page
  publishes ~98 individual annual-return rows with no on-page summary statistic, and manually
  compounding that many rows introduces real arithmetic-error risk without a spreadsheet tool in
  this session; the two secondary aggregators used instead are the same class of source already
  accepted for the identical claim in `cases/the-bracket-bet/case.json`'s S5, and they corroborate
  each other tightly (9.98% vs. 10.22%).
- Considered grounding Appendix A's $400/month contribution in a specific entry-level salary and
  savings-rate guideline (the approach `cases/the-bracket-bet` used for its own contribution
  figure). Rejected as unnecessary complexity for this case — see P05 above — and disclosed instead
  as a stated Modeling Assumption with an explicit non-load-bearing sensitivity note.
- Considered a Roth/Traditional-style "which account type" dimension to add a second lever to the
  dilemma. Rejected: it would duplicate `cases/the-bracket-bet`'s existing dilemma almost exactly
  and would dilute this case's actual point (the cost of delay under inflation), which does not
  need a tax-treatment axis to be genuinely two-sided.
