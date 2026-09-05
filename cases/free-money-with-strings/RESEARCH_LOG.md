# Research Log — Free Money, With Strings

Stage: `case-research`. Eight `{{NEEDS_SOURCE}}` placeholders enumerated from `case.md` at start.
Worked in order of load-bearing weight: the salary first (it scales every dollar amount in the
case), then the match rate/cap (defines the whole dilemma mechanism), then the Stack & Grow
contribution rate, then the loan figures (balance/rate), then the IRS limit (reference only, not
load-bearing), then the market-growth assumption (MA1) last, since it was expected to resolve to
an assumption rather than a fact.

---

## P01 — Entry-level "Junior Systems Analyst" annual base salary

**Placeholder:** `entry-level "Junior Systems Analyst" or nearest comparable IT/business-analyst role, annual base salary, USD, national median, 2026 or most recent`

- Searched several adjacent titles ("entry level systems analyst," "junior business analyst,"
  "entry level business systems analyst") since "Junior Systems Analyst" itself is not a
  standardized job-board title. Salary.com's "Entry Level Systems Analyst" page returned
  $72,744/yr average (25th pct $66,015, 75th pct $76,790), dated September 1, 2026. Other titles
  returned a wide scatter ($51,125 for "Junior Business Analyst" with <1 year experience up to
  $90,989 for "Entry Level Business Analyst" on Glassdoor/Built In) — rejected in favor of the
  title closest to the case's own "Systems Analyst" framing, from a single consistent source
  rather than mixing titles across sources.
- **Found. SOURCED as S1, confidence MEDIUM** (real, dated national compensation aggregator; a
  proxy for the case's fictional exact title).

## P02 / P03 — Employer 401(k) match rate and match cap

**Placeholders:** `representative/most-common employer 401(k) match rate...` and `...match cap...`

- Tier-1 attempt: searched for Vanguard's current (25th edition, 2026, covering 2025 data) "How
  America Saves" report directly — it publishes an *average match rate* (4.7% of pay, already used
  by `cases/the-two-offers`), but a direct WebFetch of its press release confirmed it does **not**
  publish a formula-prevalence breakdown (e.g., "X% of plans use 50%-up-to-6%"). Rejected for this
  specific claim.
- Tier-1 attempt: fetched the Vanguard PDF "Are employers optimizing their 401(k) match?" directly
  — the fetch tool could not extract readable text from the PDF (binary/compressed content).
  Rejected as unusable this session.
- Tier-2 attempt: ASPPA-Net's "What Are the Most Common Matching Formulas?" (2021), which reports
  and attributes Vanguard "How America Saves" 2020 plan-year data directly: "50 cents on the dollar
  on the first 6% of pay" was the single most common exact formula, offered by about 1 in 6 plans
  (16%) and covering 14% of participants. **Found. SOURCED as S2, confidence MEDIUM.**
- Checked for a fresher formula-prevalence breakdown before accepting the 2020 data: searched PSCA
  (Plan Sponsor Council of America)'s 2025 coverage and directly fetched their December 2025 article
  on matching contributions and vesting — it reports plan-level stats (81.3% of plans match; average
  maximum match 4.7%; 3.4% of payroll spent on matching) from the PSCA 68th Annual Survey (2024 data)
  but does **not** break out formula prevalence either. No fresher breakdown was found. Disclosed
  this explicitly in `case.json.sources[S2].note` and in case.md's Appendix E rather than silently
  using 2020 data as if it were current.

## P04 — "Stack & Grow" contribution rate (retirement savings benchmark)

**Placeholder:** `widely publicized recommended total retirement-savings rate as a percent of income (including any employer match)...`

- Searched directly for Fidelity's well-known "save 15%" guideline. WebFetch of Fidelity's own
  "Retirement Guidelines" page confirmed the exact recommendation: "aim to save at least 15% of
  your pre-tax income (including any employer match) a year over the course of your working life,"
  with stated assumptions (starting age 25, retirement age 67, 45% income-replacement target,
  1.5% real wage growth) and an explicit note that this 15% figure includes any employer match —
  exactly the modeling property this case's Stack & Grow strategy needed. **Found on first
  attempt. SOURCED as S3, confidence HIGH** (primary source: the guidance-issuing institution
  itself, not a third-party republication).

## P05 — IRS 401(k) employee elective deferral limit

**Placeholder:** `IRS annual 401(k) employee elective deferral contribution limit, USD, current year`

- Direct WebFetch of the IRS's own "Retirement Topics — 401(k) and Profit-Sharing Plan Contribution
  Limits" page. Confirmed: "$24,500 in 2026, subject to cost-of-living adjustments." **Found on
  first attempt. SOURCED as S4, confidence HIGH** (primary government source). Confirmed this
  figure stays non-load-bearing: even Stack & Grow's 15% of the sourced salary ($10,911.60/yr) is
  well under this limit, so it never enters the D1-D4 calculations as a binding constraint — kept
  in Appendix A for reference/verification only, per case-write's "no decorative constraints" rule
  it is explicitly labeled "shown for reference only."

## P06 — Average federal student loan balance, bachelor's degree recipients

**Placeholder:** `average federal student loan balance held by a bachelor's degree recipient, USD, national, most recent`

- Direct WebFetch of Education Data Initiative's "Average Debt for a Bachelor's Degree" page.
  Reports "$28,613 in federal education loans" for bachelor's-degree borrowers, updated
  2025-11-24, covering AY 2025-26. Chose this over EDI's related "$35,639 average of all education
  loans" figure (also on the same page) because $28,613 is specifically the *federal*-loan figure,
  matching the case's own "Federal Direct Unsubsidized Loan" framing in Appendix B exactly — mixing
  a federal-loan interest rate (S6) with an all-loan-types balance figure would have understated the
  loan's true weighted rate. **Found. SOURCED as S5, confidence MEDIUM** (a well-established,
  frequently-cited education-finance data aggregator, not a primary government release; this is
  disclosed rather than presented as government data).

## P07 — Federal Direct Unsubsidized Loan interest rate, undergraduate

**Placeholder:** `current federal Direct Unsubsidized Loan interest rate for undergraduate borrowers, percent, with the exact "as of" date range`

- Direct WebFetch of Federal Student Aid's (U.S. Dept. of Education) official electronic
  announcement: "Interest Rates for Direct Loans First Disbursed Between July 1, 2025 and June 30,
  2026." Confirmed: 6.39% for undergraduate Direct Unsubsidized Loans, fixed for the life of any
  loan disbursed in that window, derived from the 10-year Treasury note high yield (4.342%) plus a
  2.05% statutory add-on. **Found on first attempt. SOURCED as S6, confidence HIGH** (primary
  government source).

## P08 — MA1: assumed average annual investment growth rate

**Placeholder:** `assumed average annual investment growth rate, percent, to apply to 401(k) balances over a multi-year horizon...`

- This placeholder was expected to resolve as an ASSUMPTION, not a sourced fact — no one can cite
  a "true" future market return. The research task was to find a defensible, real historical figure
  to ground the assumption's basis, per case-write's own note in Appendix C.
- Searched for the S&P 500's long-run historical average annual return. Multiple aggregators
  (OfficialData.org, Trade That Swing, Slickcharts, others) converge on approximately 10-10.6%
  nominal (including reinvested dividends) since 1926, or roughly 7% real (inflation-adjusted).
  Direct WebFetch of OfficialData.org's "S&P 500 Returns since 1926" calculator confirmed 10.47%
  per year nominal, 1926-2026.
- **Exit chosen: (1) Stated Modeling Assumption (MA1), grounded in a real cited figure.** Rounded
  10.47% down to a clean 10% for the modeling calculation — disclosed explicitly in both case.md's
  Appendix C and `case.json.modeling_assumptions[MA1]` as an assumption about the *future*, not a
  guarantee, with the 10.47% historical figure cited as S7 for its basis only. This mirrors
  SPEC §5's requirement that a case never present a plausible number as though it were a fact:
  the case states outright that no one can know a real future return in advance.

---

## Verification

Ran the skill's verification script after all edits:
- Placeholders remaining in case.md: **0**
- Citation markers with no matching Sources row: **none**
- Source rows never cited in text: **none**
- LOW-confidence sources: **none** (no LOW-confidence figure was used at all, let alone
  load-bearing)
- All 7 `sources[]` entries in case.json carry claim, value, units, org, title, url, accessed, and
  confidence.

## Balance/margin note for the next stage

Computing the ten-year future value of each strategy's annuity streams with the sourced figures
(FV_annuity(PMT, r, n) = PMT × [(1+r)^n − 1] / r):

- Both strategies' shared 6%-of-salary + match stream: ($4,364.64 + $2,182.32) = $6,546.96/yr,
  compounded at MA1's assumed 10%/yr for 10 years → $104,341.68.
- Match & Move's extra 9%-of-salary redirected to the loan ($6,546.96/yr), compounded at the
  loan's guaranteed 6.39%/yr (MA3) for 10 years → $87,891.05. **Total A = $192,232.73.**
- Stack & Grow's full 15%-of-salary + match stream: ($10,911.60 + $2,182.32) = $13,093.92/yr,
  compounded at MA1's assumed 10%/yr for 10 years → **Total B = $208,683.36.**
- **Margin: Stack & Grow (B) wins by $16,450.63, or 8.56%** — real, computed, well inside the
  SPEC §2 20% cap, and the case stays genuinely two-sided because Match & Move's return is
  *guaranteed* (6.39%, contractual) while Stack & Grow's is *assumed* (10%, historical average, not
  promised) — a Hero who distrusts the market assumption has a live, quantitative reason to prefer
  Match & Move even though it loses under the case's own stated assumption. Flagging this for
  `case-readiness`: Tier 2 P5 (assumption sensitivity) should confirm how far MA1 would have to
  fall before Match & Move's guaranteed-return argument actually wins outright.
