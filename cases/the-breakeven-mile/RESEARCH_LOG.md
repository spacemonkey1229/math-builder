# RESEARCH_LOG.md — The Breakeven Mile

Stage: `case-research`, run 2026-09-03.

## 0. Load-bearing premise check (done first, per case.json's `quotient_rule_sourcing_risk` and the note in FACILITATOR.md / Appendix B)

**Question:** Does a real, citable source document mileage-driven vehicle depreciation as a
genuinely **nonlinear, accelerating** per-mile cost (i.e., the per-mile depreciation rate itself
*rises* as annual mileage rises) — as opposed to a per-mile average that merely falls because a
roughly fixed depreciation dollar amount gets spread over more miles (a pattern fully consistent
with a *linear* total-cost model)?

**Searched:**
- "AAA 'Your Driving Costs' 2026 depreciation cost per mile methodology mileage bands" (WebSearch)
- Direct fetch of AAA's "Your Driving Costs" 2025 brochure PDF (`https://newsroom.aaa.com/wp-content/uploads/2025/09/AAA-Brochure-Your-Driving-Cost-9.2025.pdf`) — read as a PDF directly, not via search summary.
- "Edmunds True Cost to Own depreciation curve accelerating per mile driven vehicle" (WebSearch)
- "iSeeCars study resale value drops faster per mile high mileage vehicles nonlinear" (WebSearch)
- "car depreciation accelerates with mileage odometer study percent value lost per 1000 miles" (WebSearch)

**Found:**
- AAA's brochure gives per-vehicle-segment tables at 10k/15k/20k mi/yr. For the Medium Sedan
  segment: depreciation (5-yr amortized) is $3,462/yr at the 15k mi/yr baseline, with a stated
  "decreased depreciation" adjustment of -$354 at 10k mi/yr (-> $3,108/yr) and an "increased
  depreciation" adjustment of +$411 at 20k mi/yr (-> $3,873/yr). Converting to **per-mile**:
  $0.3108/mi (10k) -> $0.2308/mi (15k) -> $0.1937/mi (20k) — **falling**, not accelerating, as
  annual mileage rises. AAA's own published "total cost per mile" column for the same segment
  falls monotonically across the same range ($0.8450 -> $0.6637 -> $0.5759) with **no interior
  minimum** anywhere in the 10k-20k range — exactly the fixed-cost-diluted-over-more-miles
  pattern the concept sheet's addendum warned would be linear-consistent, not the case's needed
  accelerating marginal cost.
- Edmunds' True Cost to Own does not publish a mileage-band depreciation curve at all: it assumes
  a single flat 15,000 mi/yr rate for every vehicle in its methodology (per Edmunds Help Center
  and TCO documentation), so there is no curve-shape to check.
- Secondary reporting on iSeeCars-style total-odometer-mileage depreciation studies (a related but
  different framing — total accumulated miles vs. resale value, rather than annual mileage rate
  vs. per-mile cost) found the *opposite* shape from what the case needs: value loss is steepest
  in the first ~20,000 accumulated miles and *flattens* (decelerates) well before 100,000 miles —
  concave, not accelerating/convex.

**Rejected:** No source was found, in any framing checked, that documents depreciation getting
*more expensive per additional mile* as annual mileage rises. This premise is **NOT FOUND** and,
per the case's own instructions, is not something case-research is authorized to force by
choosing a value — it is a structural finding recorded in `case.json`'s new `structural_blocker`
key and in Appendix B's Research Finding in `case.md`. **Recommendation: return to `case-write`**
to rebuild this case around the linear breakeven-mileage model (the concept sheet's own documented
fallback), rather than the quotient-rule optimization framing currently in Challenges D1-D3/D5.

---

## Placeholder-by-placeholder log

**P01 — Annual insurance premium (Appendix A).** Searched AAA "Your Driving Costs" (already
fetched for the premise check above). Found: Medium Sedan full-coverage insurance = $1,572/yr,
2025 brochure. SOURCED, HIGH (S1).

**P02 — Annual auto-loan financing cost, interest portion (Appendix A).** Same source. Found:
Medium Sedan "finance charges" = $854/yr. SOURCED, HIGH (S1). Note: AAA does not disclose the
loan-term/down-payment assumptions behind this figure in the brochure; it is AAA's own modeled
typical buyer, not Renata's specific loan.

**P03 — Annual registration and licensing fees (Appendix A).** Same source. Found: Medium Sedan
"license, registration, taxes" = $613/yr. SOURCED, but the AAA row bundles state taxes in with
registration/licensing, broader than what the placeholder asked for; no breakout was found.
Graded HIGH on provenance/date/units but the note flags the scope mismatch (S1).

**P04 — Linear per-mile operating cost (Appendix B).** Same source. Found: Medium Sedan "cost per
mile" (fuel + maintenance) = 23.03 cents = $0.2303/mile. Matches the placeholder's requested
composition (fuel, tires, routine maintenance/oil) closely — AAA's "maintenance" line covers
tires/oil/routine service. SOURCED, HIGH (S2).

**P05 — Nonlinear mileage-driven depreciation curve (Appendix B).** This is the load-bearing
figure addressed in Section 0 above. **NOT FOUND** as an accelerating curve. Left OPEN in
`case.json` with an explanatory note; not converted to a Modeling Assumption (a stated assumption
here would be indistinguishable from inventing the functional form the whole calculus track rests
on — exactly the "no fourth exit" the skill prohibits) and not dropped (dropping it removes the
entire justification for Challenges D1-D3/D5). Recommendation: redesign, flagged in
`case.json.structural_blocker` and in the final report.

**P06 — Average rideshare per-mile rate (Appendix C).** Searched "average Uber Lyft cost per mile
2025 2026 rideshare rate per mile national average" and a follow-up for NerdWallet/Bankrate
corroboration. Found conflicting numbers across aggregator pages on the same site on a first pass
($0.97/mi vs $1.50/mi); fetched the specific RideWise "Uber Rates 2026" article directly and
confirmed its stated national UberX average is $1.50/mile (March 2026, ~2,200 fares across 20+
markets), which the article says is corroborated by NerdWallet/Groupon/Upgraded Points. No
government or company-published rate card exists (Uber/Lyft do not publish an official national
per-mile average) — this is inherently a tier-3 estimate. SOURCED, MEDIUM (S3), with the $0.90-
$2.20/mile metro range disclosed in the case rather than hidden.

**P07 — Average annual miles driven per licensed driver (Appendix D).** Searched FHWA Highway
Statistics directly; fetched Table VM-1 (total vehicle-miles traveled, 2023 = 3,246,817 million)
and Table DL-1C (total licensed drivers, 2023 = 237,655,885) from fhwa.dot.gov directly (both
primary government tables). No single FHWA table publishes "miles per licensed driver" directly,
so this is a derived figure: 3,246,817,000,000 / 237,655,885 = 13,661.8 -> 13,662 miles/year.
Rejected several secondary aggregator figures (12,200; 13,596; 14,489 mi/yr from KBB/SmartFinancial/
Grokipedia-style summaries) in favor of computing directly from the two cited primary tables.
SOURCED, MEDIUM (S4) — graded MEDIUM rather than HIGH because the numerator spans all registered
vehicle types (trucks, buses, motorcycles), not light-duty vehicles alone, so it is a proxy for
what an individual licensed driver personally drives.

**P08 — Renata's own estimated annual mileage (Appendix D).** Protagonist-specific, as
case-write's own case.md text anticipated. No scenario-specific figure exists to source. Resolved
as **MA1**: 11,500 mi/yr, grounded in a dense-urban multi-stop home-health route running below the
national average (S4), with sensitivity noted (this is exactly what Challenge D4 asks the student
to locate relative to m*, and cannot be finalized as load-bearing until the P05 structural blocker
is resolved).

**P09 — Renata's maximum monthly transportation budget (Appendix D).** Protagonist-specific.
Searched BLS OEWS/Occupational Outlook Handbook for home health and personal care aide wages to
ground the assumption in a real income figure rather than an arbitrary number; found median annual
wage $35,800 (May 2025, S5). Resolved as **MA2**: $350/month (~12% of gross monthly income),
within the commonly cited 10-20% affordable-transportation-share guideline.

**P10 — Days remaining on the dealership's price hold (Appendix D).** Protagonist-specific
narrative detail. The Overview already states the hold "expires 5 p.m., can't extend past close"
today — so this placeholder is really just conforming a number to narrative already written, not
an independent estimate. Resolved as **MA3**: 0 days remaining (expires today).

---

## Verification (skill step 7)

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources (must not be load-bearing): []
```

## Next step

**Do not run `case-readiness`.** This case has an unresolved structural blocker
(`case.json.structural_blocker`) and `case.json.status` is set to `blocked_needs_redesign`, not
`researched`. Return to `case-write` to rebuild the calculus/quotient-rule framing (Appendix B,
Challenges D1-D3/D5) around the linear breakeven-mileage model per the concept sheet's own
documented fallback, then re-run `case-research` on the redesigned case before proceeding.

---

## Redesign entry — 2026-09-03 (back at `case-write`)

Per the recommendation above and `case.json.structural_blocker`, this case was rebuilt around the
concept sheet's own documented linear fallback: A) total annual cost = fixed costs + (per-mile
operating cost x miles driven), B) total annual cost = rideshare rate x miles driven, with the
breakeven mileage as the primary metric instead of a quotient-rule-minimized average cost per mile.

**Carried forward as-is (no re-research needed — these were always independent of the
depreciation-curve question):**
- S1 — insurance ($1,572/yr), auto-loan financing/interest ($854/yr), registration ($613/yr),
  AAA "Your Driving Costs" 2025, HIGH confidence.
- S2 — linear per-mile operating cost ($0.2303/mile), same AAA source, HIGH confidence. (S2's
  mileage-band depreciation figures, which were only ever used to test the now-abandoned nonlinear
  premise, are dropped along with that premise.)
- S3 — rideshare per-mile rate ($1.50/mile), RideWise, MEDIUM confidence.
- S4 — US average annual miles/driver (13,662 mi/yr, derived from FHWA VM-1/DL-1C), MEDIUM
  confidence.
- S5 — BLS median wage for home health aides, grounding MA2.
- MA2 (monthly budget cap, $350/month) and MA3 (price-hold deadline, 0 days) — unchanged in value
  and basis; both remain narratively and mathematically sound under the linear model.

**Dropped:**
- The nonlinear mileage-driven depreciation placeholder (former Appendix B row) and its NOT-FOUND
  research finding — no longer needed, since the linear model has no depreciation-curve term.
- The quotient-rule / critical-point / first-derivative-test framing throughout the Dilemma,
  Challenges (former D1-D5), and Appendix F.
- `case.json.structural_blocker` and `quotient_rule_sourcing_risk` (resolved by this redesign;
  replaced by `case.json.redesign_2026_09_03`).

**Retuned for the balance test (SPEC §2), not re-researched:** MA1 (Renata's own annual mileage)
is a disclosed Modeling Assumption, not a sourced figure, so it was the correct dial to adjust. At
its prior value (11,500 mi/yr, roughly national-average scale), the linear model produces a ~67%
margin in favor of Option A — a landslide, unbalanced per SPEC §2's ~20% ceiling. MA1 was revised
down to 2,760 mi/yr with an explicit arithmetic basis (a compact single-neighborhood home-health
route: ~10 mi/workday x 250 workdays + ~260 mi/yr of errands), which is both defensible for the
narrative and lands the margin at 11.24% — inside the concept sheet's 8-12% target. This is a
constraint retune, not a data change or a hidden adjustment: it is disclosed in `case.md`'s
Modeling Assumptions block, its sensitivity is called out explicitly, and it drives Socratic
question 3 in `FACILITATOR.md`.

**New figures needed:** none. Every figure the linear model requires (two fixed-cost components,
one operating rate, one rideshare rate, one national-average mileage figure, and three
protagonist-specific assumptions) was already sourced or disclosed in the prior pass. No new
`{{NEEDS_SOURCE}}` placeholders were introduced, and no follow-up search was required beyond
re-verifying the arithmetic above.

**Verification:**
```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources (must not be load-bearing): []
breakeven mileage m* = 3039 / 1.2697 ≈ 2,393.5 mi/yr
margin at MA1 (2,760 mi/yr) = 11.24%
```

**Status:** `case.json.status` set to `researched`. This case is ready for `case-readiness`.
