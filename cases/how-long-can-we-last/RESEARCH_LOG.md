# Research Log — How Long Can We Last

Stage: `case-research`. Four `{{NEEDS_SOURCE}}` placeholders enumerated from the drafted case at
start: (P01) household essential-expense breakdown, (P02) Renata's salaried income, (MA1 component)
Julian's slow-month invoice as a percent of typical, (MA2 component) length/severity of the
household's documented dry spell. Worked in order of load-bearing weight: the essential-expense
baseline first (it sets both fund sizes directly), then Renata's income (sets the monthly
shortfall), then the two freelance-volatility figures last, since both were expected going in to
resolve as disclosed Modeling Assumptions rather than clean citations.

---

## P01 — Household essential monthly expenses

**Placeholder:** `average annual household essential-expense breakdown by category, USD, US, 2024 or most recent`

- Tier-1 attempt: BLS's own "Consumer Expenditures in 2024" news release PDF
  (bls.gov/news.release/archives/cesan_12192025.pdf) — fetched directly but the tool could not
  extract clean text from the PDF's encoding. Rejected as a fetch target, not as a source (same
  underlying data is published as HTML — see below).
- Tier-1 success: BLS's own HTML report, "Consumer Expenditures in 2024"
  (bls.gov/opub/reports/consumer-expenditures/2024/home.htm), fetched directly. Confirmed exact
  category figures: Housing $26,266, Transportation $13,318, Food $10,169, Personal insurance and
  pensions $9,797, Healthcare $6,197, Utilities/fuels/public services $4,736 (total average annual
  expenditure across all categories, including non-essential ones not used here, is $78,535).
  **Found. SOURCED as S1, confidence MEDIUM** (a real, primary, dated BLS national average across
  all U.S. consumer units — used as a proxy for this fictional household's specific essential
  spending; it is not location- or household-size-specific, and no attempt was made to find a
  household-composition-specific breakdown — see note below on the two-earner-household search).
- Considered and rejected: searching for a "two or more earners" household-specific CES table
  (which would likely run higher than the all-consumer-units average, since it excludes single-
  person and retiree households). A direct fetch of the CES tables landing page
  (bls.gov/opub/reports/consumer-expenditures/2024/home.htm) confirmed BLS does publish
  by-number-of-earners breakdowns in its full data tables, but a WebFetch of the summary report
  page did not surface that specific cut, and pursuing the full interactive table was judged not
  worth the effort for a MEDIUM-confidence proxy figure that is disclosed as a national-average
  proxy either way. Noted here so a future pass knows this refinement exists but was not chased.
- **Essential subset chosen:** Housing, Transportation, Food, Personal insurance and pensions,
  Healthcare, and Utilities/fuels/public services, totaling $70,483/year ($5,874/month, rounded).
  Excluded as non-essential: apparel, entertainment, alcohol/tobacco, education, and other
  miscellaneous/cash-contribution categories (together roughly $8,052/year of the $78,535 total),
  disclosed explicitly in case.md Appendix A.

## P02 — Renata's salaried monthly income

**Placeholder:** `median annual wage, home health and personal care aide, USD, US, most recent`

- Chose "home health and personal care aide" specifically (rather than a generic "salaried
  worker" median) so Renata's income is a concrete, checkable, real occupation rather than an
  averaged national wage figure that would be harder for a Hero to sanity-check independently.
- Tier-1 attempt: BLS OEWS occupation page (bls.gov/oes/2023/may/oes311120.htm) — fetched directly,
  returned May 2023 data: median annual wage $33,530. Correct primary source, but not the most
  recent available.
- Tier-1 success (more recent): BLS Occupational Outlook Handbook page for the same occupation
  (bls.gov/ooh/healthcare/home-health-aides-and-personal-care-aides.htm) — fetched directly and
  quoted verbatim: "The median annual wage for home health and personal care aides was $35,800 in
  May 2025." **Found. SOURCED as S2, confidence HIGH** (primary government source, dated,
  unambiguous units, national). Used the more recent May 2025 figure rather than the May 2023 OEWS
  figure found first, since the OOH page is BLS's own more-current restatement of the same series.
- $35,800/12 = $2,983.33/month, rounded to $2,983/month in case.md Appendix B.

## MA1 — Julian's slow-month invoice as a percent of a typical month

**Placeholder (informal, not a literal `{{NEEDS_SOURCE}}` token — flagged during drafting as a
figure needing either a source or a disclosed assumption):** the relationship used in Challenge
3's D2 between Julian's $756 slow-month invoice total and "21% of a typical month."

- Searched for a population-level "freelancer's worst month is what percent of a typical month"
  statistic. Found only secondary/aggregator content (e.g., a "planwith.ai" blog post attributing a
  ~30% high-month-vs-low-month figure to JPMorgan Chase Institute research) that could not be
  independently verified against JPMC's own published materials via direct fetch — **rejected**,
  per this project's rule to never cite a figure whose provenance cannot be confirmed by fetching
  the actual primary source.
- Verified instead, by direct fetch of JPMorgan Chase Institute's own report page
  (jpmorganchase.com/institute/all-topics/labor-markets-and-workforce/report-paychecks-paydays-and-
  the-online-platform-economy): non-salaried/hourly workers see a typical month-to-month earnings
  change of 9%, with a swing of at least 21% occurring in roughly 1 of every 4 months. This is a
  real, primary, directly-verified figure — **but it describes swing *size* (a change relative to
  a worker's own trailing average), not "this month's income is X% of a typical month."** A 21%
  *decrease* swing would mean that month is 79% of typical, not 21% of typical — using the raw 21%
  figure as "percent of typical" would have misrepresented what JPMC actually measured.
- **Disposition: ASSUMPTION**, not a direct citation. Recorded as Modeling Assumption MA1 in
  case.json and case.md Appendix D: Julian's specific $756-is-21%-of-typical relationship is this
  case's own household record, chosen to give Challenge 3's D2 a clean, calculable whole
  ($756 ÷ 0.21 = $3,600 exactly). JPMC's real 21% swing-frequency figure [S4] is disclosed as
  informing the choice of percentage (it establishes 21% as a real, documented magnitude of
  volatility for this population) without claiming it is the source of this specific household's
  specific number. This is deliberately disclosed rather than silently presented as sourced.

## MA2 — Length and severity of the household's documented dry spell

**Placeholder (informal):** how long, and how severely, Julian's freelance income realistically
stops — the number that sets Fund B's entire size.

- Searched for a multi-month, consecutive-month severity distribution for freelance/self-employed
  income specifically (e.g., "typical length of a freelancer's slow season," "consecutive months
  of zero self-employment income survey data"). **Not found** as a single clean published
  statistic — this is a real, structural data gap: population surveys (Fed SHED, BLS CPS) capture
  whether income varies month to month, and platform-specific big-data studies (JPMC) capture
  single-month swing magnitude and annual participation-month counts, but none of the sources
  reviewed publish a "how long does a bad stretch last, and how severe" joint distribution for
  freelance/1099 workers.
- Two real, directly-verified findings used as supporting basis instead (both fetched directly from
  primary sources, not summarized secondhand):
  - Federal Reserve, "Report on the Economic Well-Being of U.S. Households in 2024 — Income and
    Expenses" (federalreserve.gov, published May 2025, fetched directly): "Fifty-nine percent of
    self-employed adults said their income varied from month to month… Excluding those who did gig
    activities, adults who were self-employed still were more likely to report their income varied
    from month to month (56 percent) compared with those who worked for someone else (26 percent)."
    **Found. SOURCED as S3, confidence HIGH.** Used the 56%/26% (excluding gig work) figures since
    Julian is a project-based freelance consultant, not a gig-platform worker — establishes that
    persistent month-to-month variability, not a one-off bad month, is the norm for this
    population.
  - JPMorgan Chase Institute, same report as MA1 above: "the majority of these [platform] participants
    work for online platforms for three or fewer months in a year" — directional support that many
    non-salaried earners go multiple consecutive months per year with little or no income from a
    given income source. Already recorded as S4.
- **Disposition: ASSUMPTION.** Neither source specifies an exact consecutive-month "income fully
  stops" duration, so this case exits via a stated Modeling Assumption (MA2 in case.json/case.md
  Appendix D), not a citation: 7 consecutive months at $0 freelance income, chosen as a scenario
  that is (a) long enough to be a genuine worst case for a household that has "hit the famous
  number" and stopped worrying, and (b) shorter than the full-year extreme JPMC's participation-
  month finding would technically permit, kept deliberately conservative rather than maximally
  severe. This is the single assumption Tier 2 P5 will flex ±50% — see `sensitivity_model.py`.
- Redesign considered and rejected: reframing the case around a single very-bad month (using
  JPMC's 21%-swing figure directly, not needing MA2 at all) was considered, but produces a shortfall
  far too small in dollar terms to make the flat "3 months of expenses" rule fail against it under
  any duration a Hero would find realistic (the residual gap between essential expenses and
  Renata's fixed income, $2,891/month, means a fund of $17,622 survives more than 6 months of even
  total Julian income loss on its own — a multi-month dry spell, not a single bad month, is what
  makes this a genuine sizing decision rather than a foregone conclusion). This is why the case is
  built around a *documented multi-month dry spell* rather than a single-month swing.

---

## Verification

Ran the skill's verification script after all edits (adapted for this case's four placeholders,
which resolve to two SOURCED table figures and two disclosed ASSUMPTIONs rather than six SOURCED
figures as in `the-two-offers`):

- Placeholders remaining OPEN in case.md: **0**
- Citation markers with no matching Sources row: **none**
- Source rows never cited in text: **none**
- LOW-confidence sources: **none** (no LOW-confidence figure was used at all, let alone
  load-bearing)
- All 4 `sources[]` entries in case.json carry claim, value, units, org, title, url, accessed, and
  confidence.
- Both `modeling_assumptions[]` entries (MA1, MA2) are visible in case.md Appendix D with a basis
  and a sensitivity column, per SPEC §5 and the case-write skill's placeholder-discipline rule —
  neither is buried in a data table as though it were sourced.

## Balance/margin note for the next stage

Computing the two fund sizes with the sourced/assumed figures:

- Essential monthly expenses: $5,874 (S1). Renata's income: $2,983 (S2). Normal-month surplus with
  Julian's derived $3,600 typical income: $2,983 + $3,600 − $5,874 = $709/month.
- Fund A (Rule-of-Thumb) = 3 × $5,874 = $17,622.
- Fund B (Real-Stretch) = 7 × ($5,874 − $2,983) = 7 × $2,891 = $20,237 (MA2's 7-month, $0-income
  dry spell).
- Fund A's actual coverage against the $2,891/month shortfall: $17,622 ÷ $2,891 = 6.10 months —
  87.1% of the 7-month documented stretch.
- margin_pct = ($20,237 − $17,622) / $17,622 × 100 = **14.84%**, inside the SPEC §2 20% cap and
  inside the 10-15% target range given in the original concept sheet.
- Flagging for whoever runs `case-readiness`: MA2 (the 7-month/$0 dry spell) is the load-bearing
  assumption for the entire balance test — Fund B's size, the margin, and Option A's "87.1%, not
  100%" finding all scale directly with it. A `sensitivity_model.py` flexing MA2's duration ±50%
  (5.5 to 10.5 months) is the natural Tier 2 P5 test and should be built before that probe runs.

---

## Correction — 2026-09-04, found during Tier 2 P6 (data decay)

Running P6's direct-fetch verification against S4's own cited URL surfaced a real sourcing defect
in this log and in the original S4 entry: **the "9% typical swing, with at least 21% occurring in
roughly 1 of every 4 months" figure, originally attributed above to JPMorgan Chase Institute's
"Paychecks, Paydays, and the Online Platform Economy" report, could not be re-verified on that
report's own page.** A direct fetch of the exact cited URL on 2026-09-04, asked to quote every
sentence containing a percent figure about month-to-month income volatility, returned seven real,
verbatim quotes from the page — none of them the "9%/21%, 1-in-4-months" figure. A second, more
targeted web search for the exact phrase also failed to locate it on any JPMC page. **Disposition:
this figure is being treated as unverifiable and has been removed from case.json/case.md and
replaced.** This is exactly the kind of error the pipeline's sourcing discipline exists to catch —
recorded here rather than corrected silently.

Replacement figures, both verified by direct fetch on 2026-09-04 and now recorded as S4 and S5 in
case.json/case.md Appendix F:

- **S4 (replaces the old S4 claim; same JPMC "Paychecks, Paydays" URL, correctly quoted this
  time):** "The vast majority of people aged 18-24, individuals in the bottom income quintile, and
  people living in the West experienced on average more than a 30 percent month-to-month change in
  total income." Used inside MA1 as directional support for "a swing in the low tens of percent is
  a realistic magnitude," not as the source of the specific 21% figure (which remains this case's
  own chosen value for D2, as already disclosed).
- **S5 (new source, a different JPMC report):** JPMorgan Chase Institute's 2018 "The Online
  Platform Economy" report page, fetched directly, states: "Among those who generated earnings
  through transportation platforms at any point in a year, 58 percent had earnings in just three or
  fewer months of that year." This is a more precise, directly-verified version of the "most
  online-platform earners are active 3 or fewer months per year" claim the original MA2 basis
  attributed (imprecisely, and to the wrong URL) to the Paychecks-Paydays report — now correctly
  cited to its actual source and given its exact reported figure (58% of transportation-platform
  earners specifically, not "most" platform earners generally).

`case.json.modeling_assumptions` (MA1, MA2), `case.json.sensitivity_disclosure[0].justification`,
and `case.md` Appendices D and F were all updated to match. No other figure in this case (S1, S2,
S3) was affected — each was independently re-verified by direct fetch during the same P6 pass and
confirmed accurate on first check.
