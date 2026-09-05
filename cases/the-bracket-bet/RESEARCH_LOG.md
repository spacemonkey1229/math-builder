# RESEARCH_LOG.md — The Bracket Bet

Stage 3 (`case-research`) run 2026-09-03. 18 `{{NEEDS_SOURCE}}` tokens enumerated from `case.md`.
One row per token: what was searched, what was found or rejected, and the disposition.

---

**P01 — Devon's planned annual IRA contribution amount (Appendix A)**
Searched: "recommended starter IRA contribution amount early career," Fidelity/Northwestern Mutual
savings-rate guidance. No single published number exists for "what a 24-year-old contributes to an
IRA" — this is inherently a scenario choice. Grounded it instead: BLS median usual weekly earnings
for full-time workers age 16–24 (cpsaat37.htm) — $805/wk (men) / $725/wk (women) for 2025 — average
≈ $765/wk ≈ $39,780/yr, rounded to $40,000 as Devon's assumed entry-level salary anchor. Applied a
conservative early-career savings rate (~7–8%, below Fidelity's "work up to 15%" target, consistent
with Northwestern Mutual's "start with what's feasible, no employer match yet" guidance) →
≈ $3,000/year. **Disposition: SOURCED (derived)**, MEDIUM confidence — the salary anchor is a real
BLS figure but for a slightly broader age band (16–24, not 20–24 exactly) and the savings rate is a
guidance-based choice, not a single published statistic. Both inputs cited; the $3,000 figure itself
is a defensible derivation, not an invention.

**P02 — IRS annual individual contribution limit, under 50 (Appendix A)**
Searched IRS.gov newsroom directly. Found: IRS Newsroom, "401(k) limit increases to $24,500 for
2026, IRA limit increases to $7,500," confirms **$7,500** for 2026 (up from $7,000 in 2025).
Cross-checked against Notice 2025-67 (2026 COLA amounts) referenced in the same release.
**Disposition: SOURCED**, HIGH confidence — primary IRS source, dated, unambiguous.

**P03 — Roth IRA MAGI phase-out, single filer (Appendix A)**
Same IRS Newsroom release: "income phase-out range for taxpayers making contributions to a Roth IRA
is increased to between $153,000 and $168,000 for singles and heads of household" for 2026. Devon's
assumed income (~$40,000, see P01) is far below the floor — full contribution eligibility confirmed.
**Disposition: SOURCED**, HIGH confidence.

**P04 — Days remaining until the election locks in (Appendix A)**
This is explicitly flagged in case-write's own token as "narrative-only," not a researched fact —
there is no real Devon and no real Friday to look up. No external search performed; none is
possible. Set to **4 days** (a work-week's worth of urgency, consistent with "first paycheck posts
Friday"). Not given a `[S#]` marker and not placed in the Sources appendix — doing so would make an
invented number look sourced, which SPEC §5 forbids. Documented plainly in `case.md` as an author's
narrative detail. **Disposition: ASSUMPTION (narrative, non-load-bearing)** — does not appear in any
of D1–D5's computations, so it carries no Sensitivity entry.

**P05 — Devon's current age (Appendix B)**
Already stated in Overview/Background as 24; case-write's own token asks only for confirmation, not
external sourcing. Confirmed: no external source exists or is needed for a fictional protagonist's
stated age. **Disposition: ASSUMPTION (narrative, non-load-bearing)** — carried through as given.

**P06 — Assumed retirement age (Appendix B)**
Searched SSA.gov and corroborating sources. SSA's Full Retirement Age (FRA) is **67** for everyone
born in 1960 or later — which covers Devon (24 in 2026, born ~2002) with no ambiguity or future
phase-in left to resolve; this number is fixed policy, not a projection. Direct fetch of
ssa.gov/faqs/en/questions/KA-01885.html returned HTTP 403 (bot-blocked), but the figure is directly
quoted from SSA's own benefits-planner content in search results and corroborated by Charles Schwab
and the Bipartisan Policy Center. **Disposition: SOURCED**, HIGH confidence — official, stable,
unambiguous.

**P07 — Years of growth this case models (Appendix B)**
Derived: 67 (P06, sourced) − 24 (P05, narrative) = **43 years**. Concept brief target was "near 40";
43 is close enough that no retuning of the ages was needed. **Disposition: SOURCED (derived)**,
HIGH confidence (pure arithmetic on the two inputs above).

**P08 — Assumed average annual rate of return (Appendix B)**
Searched for a real, cited long-run diversified/index benchmark. Multiple aggregator sources agree:
Motley Fool cites **9.98%/year** CAGR for the S&P 500 since 1928; officialdata.org (built on
Shiller-derived historical S&P 500 data, dividends reinvested) independently states **10.22%/year**
since 1928. These are secondary aggregators of primary market data (tier 3), not a government or
exchange primary source (metals/equities long-run series of this kind are not published by a single
primary regulator) — but the two independent figures corroborate each other tightly (9.98% vs.
10.22%), and the ~10% figure is the standard, uncontested number used throughout retirement-planning
literature. Rounded to a clean **10%/year** for modeling — disclosed as a rounding choice, not a
different number. **Disposition: SOURCED**, MEDIUM confidence (reputable aggregators, not primary,
but tightly corroborated and undisputed).

**P09 — Traditional IRA contribution tax treatment (Appendix C)**
IRS.gov (irs.gov/retirement-plans/traditional-iras): "Contributions you make to a traditional IRA
may be fully or partially deductible, depending on your filing status and income." Devon has no
other workplace retirement plan (this is the first plan of any kind), so the workplace-plan phase-out
does not apply — full deduction. **Disposition: SOURCED**, HIGH confidence, primary source.

**P10 — Traditional IRA withdrawal tax treatment (Appendix C)**
IRS.gov, same page: "amounts in your traditional IRA (including earnings and gains) are not taxed
until you take a distribution." IRS Pub 590-B (referenced, not separately fetched) confirms
distributions are taxed as ordinary income. **Disposition: SOURCED**, HIGH confidence.

**P11 — Roth IRA contribution tax treatment (Appendix C)**
IRS.gov (irs.gov/retirement-plans/roth-iras): "You cannot deduct contributions to a Roth IRA" —
made with after-tax dollars. **Disposition: SOURCED**, HIGH confidence, primary source.

**P12 — Roth IRA withdrawal tax treatment (Appendix C)**
Same IRS.gov page: "if you satisfy the requirements, qualified distributions are tax-free" —
contributions and earnings both. **Disposition: SOURCED**, HIGH confidence, primary source.

**P13 — Devon's current marginal federal tax bracket (Appendix D)**
Searched IRS.gov directly for the 2026 inflation-adjusted bracket table (IRS Newsroom, "IRS releases
tax inflation adjustments for tax year 2026, including amendments from the One, Big, Beautiful
Bill"). 2026 single-filer brackets: 10% to $12,400; 12% above $12,400 to $50,400; 22% above $50,400
to $105,700; 24%, 32%, 35%, 37% above that. 2026 standard deduction for single filers: $16,100.
Using Devon's assumed entry-level salary (~$40,000, see P01) minus the standard deduction, taxable
income ≈ $23,900 — squarely inside the 12% bracket. **Disposition: SOURCED**, HIGH confidence,
primary IRS source, current tax year.

*This is the load-bearing finding for the balance-test check below: Devon's real current bracket
is 12%, not the facilitator's originally-floated "10–12% neighborhood" floor of 10%. That matters —
see the Balance-Test Verification section.*

**P14 — Scenario 1, higher future bracket (Appendix D)**
Candidate from `case.json.balance.candidate_rate_scenario_for_research` was "roughly two brackets
higher, historically near 22%." With the current bracket confirmed at 12% (not 10%), the next real
published bracket up is **22%** — a one-bracket jump, not two, but still a fully realistic
"established mid-career salary" trajectory over a ~43-year career (a rise from ~$40k to comfortably
into six figures in nominal terms is unremarkable over four decades, and is *less* aggressive than
assuming a jump to 24% or higher). **Disposition: SOURCED** (the rate itself is a real, currently
published federal bracket; its *selection* as Devon's future scenario is the disclosed Modeling
Assumption — see Modeling Assumptions block), HIGH confidence on the rate, assumption on the
selection.

**P15 — Scenario 2, lower future bracket (Appendix D)**
The originally-floated candidate anchored current bracket at 10%, which would have left no real
published bracket *below* it to use as the required "lower" scenario — an internal contradiction in
the original candidate now resolved by the real current-bracket finding (12%). With current
confirmed at 12%, the real bracket immediately below is **10%**, the actual bottom of the federal
schedule — a realistic "modest retirement income, largely funded by Social Security and a smaller
draw-down" scenario. **Disposition: SOURCED** (rate) / **ASSUMPTION** (selection), same basis as P14.

**P16–P18 — Modeling Assumptions block restating the three brackets (12% / 22% / 10%)**
Same figures as P13–P15, restated in the visible Modeling Assumptions block per SPEC §5 (a stated
scenario assumption must live in the open, not buried in a data table). **Disposition: ASSUMPTION**
(the two future rates) with the current rate carried through as sourced context.

---

## Balance-test verification (the critical check)

Ran the case's own stated model (`case.json.balance.margin_basis`, matching `argument_a`/
`argument_b`): for a pretax contribution `C` invested identically in both accounts and grown to
future value `FV`, after-tax value = `FV × (1 − r_today)` for Roth (tax paid once, up front, at
today's rate) and `FV × (1 − r_future)` for Traditional (tax paid once, at withdrawal, at the future
rate). Using the sourced/derived inputs above — `C = $3,000/yr`, `r = 10%`, `n = 43 years` — the
annuity future value is `FV = 3,000 × [(1.10)^43 − 1] / 0.10 ≈ $1,777,200`.

| Scenario | Future rate | Traditional after-tax | Roth after-tax | Winner | Margin |
|---|---|---|---|---|---|
| 1 — higher | 22% | $1,386,216 | $1,563,936 | Roth (B) | **12.8%** |
| 2 — lower | 10% | $1,599,480 | $1,563,936 | Traditional (A) | **2.3%** |

Both margins are comfortably inside SPEC §2's ~20% cap — no landslide in either direction. Scenario
2's margin (2.3%) is tighter than the 5–10% target (nearly a coin flip, which is arithmetically fine
and pedagogically fine — it is not a landslide, it is the *tightest* possible version of "close").
Scenario 1's margin (12.8%) sits a little above the 5–10% ideal but well under the 20% blocker
threshold. **No retune was needed** — the originally-floated candidate's *direction* (straddle
today's rate, one bracket each way) held up; only its specific anchor (10% vs. 12% for today's rate)
needed correcting once the real bracket table was checked, which is exactly the kind of
constraint-verification this stage exists to do. Had the real numbers instead produced a landslide,
the note in `case.json.balance` and `FACILITATOR.md` already designates the correct lever (Appendix
A's contribution amount or Appendix B's return assumption) rather than the bracket pair — that lever
was not needed here.

## Not used / rejected

- IRS Pub 590-A/590-B PDFs were not directly fetchable in this session (binary parsing failure) —
  relied on IRS.gov's rendered HTML pages instead, which state the same rules in prose and are
  citable in their own right.
- ssa.gov's FAQ page returned HTTP 403 on direct fetch (bot-blocked); the FRA=67 figure is instead
  cited to the search-indexed SSA content plus two independent corroborating secondary sources
  (Schwab, Bipartisan Policy Center), which together clear the "two distinct framings + attempted
  primary fetch" bar in the skill before a NOT FOUND would be declared. Not treated as NOT FOUND
  since the primary content was directly quoted, just not fetchable as a live page in this run.
- Considered citing a specific "20–24" BLS breakout for P01's salary anchor; BLS's published table
  only breaks out 16–24 as a combined band, so the 20–24-specific figure does not exist as a
  standalone published statistic. Used the 16–24 figure as a (slightly conservative, since it
  includes some sub-20 part-time earners) proxy instead, noted as MEDIUM confidence.
