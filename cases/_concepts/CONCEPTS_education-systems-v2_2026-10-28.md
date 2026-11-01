# CONCEPTS: education-systems v2 (Civic Life, Law & Learning) - 2026-10-28

Revision of C1 "The Fifth Coach" after R1 round 1 (R1a REVISE minor, R1b GO, R1c GO minor). Single concept. Tags: **[CONFIRMED]** = fetched this session; **[DERIVED]** = recomputed in Python this session from fetched rows; **[UNVERIFIED]** = not fetched, must be labeled a Modeling Assumption or cut.

**Margin convention (stated once, used everywhere).** Margin = (winner's value - loser's value) / winner's value, on the primary metric. SPEC 20% test applies to this number.

### The Fifth Coach   ·   tier T3   ·   thin skills closed: 2

**Protagonist.** Odette Hargrove (fictional; no hit for "Odette" or "Hargrove" anywhere under `cases/`), literacy director for Bellevue Public Schools, Nebraska. Constructed framing: the district, school names, enrollments and meal-eligibility counts are real federal data (Urban Institute Education Data Portal, CCD directory, portal year 2021). The "one more reading-coach slot", the two-school shortlist and the cost structure are invented and disclosed as Modeling Assumptions. No such decision is claimed to have happened.

**How the shortlist is defined (new, fixes a hidden option).** Four elementary schools already have a coach: the four with the most students who qualify for meals, which is the same four by count (Birchcrest 226, Betz 195, Belleaire 184, Avery 178) and by percent. Of the 11 remaining Bellevue elementary schools, the school board has narrowed the fifth coach to the two its two competing equity rules pick: the **highest share** of students who qualify (Central, 81 of 172 = 47.1%) and the **highest number** (Wake Robin, 135 of 506 = 26.7%). I checked all 11 [DERIVED]: those really are the max-share and max-count schools (next: Twin Ridge 46.2%; Peter Sarpy 131). **Twin Ridge (117 of 253, 46.2%) beats both finalists on the whole-program ratio for every r from 98 to 2,223** (Twin Ridge 170.29 vs Central 166.03 vs Wake Robin 165.76 FRL per $1M at r=750; Twin Ridge leads the better finalist by 2.5%). SPEC 1.4 requires a binary fork, so the case keeps the board's two rules as the fork and surfaces Twin Ridge as a deliberate discussion point (see Socratic points and Still open) rather than hiding it. It is not a fourth option the student may choose in the pitch.

**The dilemma.** You are Odette Hargrove. Do you:
A.) Place the fifth coach and program at Central Elementary (172 pupils, 81 who qualify for meals, the highest share) OR
B.) Place it at Wake Robin Elementary (506 pupils, 135 who qualify for meals, the highest number)?

**Primary metric (stated objective).** The **whole-program ratio**: students who qualify for meals served by the five-school program, per program dollar. Cost of the program = f per school (coach salary and benefits, fixed) + v per enrolled pupil (materials, assessments). Only free parameter: r = f / v, in "pupils' worth of materials". Ratio = (783 + F) / (5r + 1,282 + E) per v-dollar, where F and E are the new school's qualifying and enrolled counts.

**Why the whole-program ratio and not the marginal one (made a Socratic point, not hidden).** The board funds and reports one program, so the accountable number is what the five-school program delivers per dollar. A competing reading judges only the new school: F / (r + E), the "marginal swap". The two rules disagree on r in (329, 778):

| r range | Marginal swap (new school alone) | Whole-program ratio |
|---|---|---|
| r < 329 | Central | Central |
| 329 < r < 778 | Wake Robin | **Central** |
| r > 778 | Wake Robin | Wake Robin |

Marginal tie: 81(r+506) = 135(r+172) gives r = 329 exactly. Whole-program tie: 864(5r+1,788) = 918(5r+1,454) gives r = 778 exactly [DERIVED]. In the middle band Wake Robin looks better standing alone (at r=750: 135/1,256 = 0.1075 vs 81/922 = 0.0879) but the program does better with Central, because Wake Robin adds 334 more pupils' worth of materials to a shared denominator while the added qualifying students (54) do not buy that much. Students must decide which objective they would defend to a board and say why; the case states the program ratio as the primary metric so the answer is checkable, and a student may argue for another objective but must name it. A second honest objection: the options do not cost the same (B costs more), so an equal-budget view is also defensible (see Socratic points).

**Margins (program ratio, gap/winner) [DERIVED].** Positive = Central (A) leads.
| r | Central FRL per $1M of v-units* | Wake Robin | Margin | Winner |
|---|---|---|---|---|
| 0 | 594.22 | 513.42 | 13.60% | A |
| 100 | 442.17 | 401.22 | 9.26% | A |
| 200 | 352.08 | 329.27 | 6.48% | A |
| 329 | 278.80 | 267.40 | 4.09% | A |
| 387 (low end of range) | 254.94 | 246.58 | 3.28% | A |
| 500 | 218.51 | 214.09 | 2.03% | A |
| 600 | 193.98 | 191.73 | 1.16% | A |
| 750 (illustrative) | 166.03 | 165.76 | **0.16%** | A |
| 778 | 161.68 | 161.68 | 0.00% | tie |
| 800 | 158.42 | 158.60 | 0.12% | B |
| 1,000 | 133.87 | 135.24 | 1.01% | B |
| 1,084 (high end of range) | 125.69 | 127.36 | 1.31% | B |
| 2,000 | 75.43 | 77.88 | 3.14% | B |
*Ratio x 1,000,000 with v = 1 (so "per $1M" holds when v = $1); in the case use FRL per $1,000 of actual cost.

**Break-even.** r* = 778 for the whole-program ratio (A wins below, B above). Range of plausible r from the Modeling Assumptions: **387 to 1,084** (below), so both options win somewhere inside the plausible range: Central by up to 3.3% at the low end, Wake Robin by up to 1.3% at the high end. **At the illustrative inputs ($90,000 coach, $120 per pupil), r = 750 and Central leads by only 0.16%** (864 / $624,480 = 1.3836 vs 918 / $664,560 = 1.3814 qualifying students per $1,000). That is a near-tie, and the case must NOT present it as a finding that Central is better; it is the reason the answer depends on the inputs students choose. Maximum margin anywhere tested (r=0) is 13.60%, under the 20% test.

**Modeling Assumptions block (label, do not source as fact).**
1. **Coach cost f.** Proxy only: BLS Occupational Outlook Handbook, Instructional Coordinators: median annual wage **$77,440 (May 2025)**, 10th-90th percentile $47,980 to $121,670 [CONFIRMED by WebFetch of bls.gov/ooh/education-training-and-library/instructional-coordinators.htm on 2026-10-28; page last modified 2026-08-27; read via a summarizing fetch, so re-check the figures on the page before publication]. Instructional coordinators are not identical to reading coaches, and the benefits load (assumed 1.0x to 1.4x salary, giving f of $77,440 to $108,416) is **[UNVERIFIED]**. The illustrative $90,000 is an assumption students may replace.
2. **Materials per pupil v.** Assumed range $100 to $200 per pupil per year; the illustrative value is $120. **[UNVERIFIED]**: no NCES figure fetched; a literacy program's per-pupil materials and assessment cost is not a federal statistic. State as a scenario input.
3. **r range 387 to 1,084** follows from items 1 and 2 (77,440 / 200 and 108,416 / 100). If a student uses a different f or v the range moves; the break-even does not.
4. **Shortlist** (Central vs Wake Robin) and the "same cost structure at both schools" are scenario assumptions.
5. **As-of date.** All enrollment and meal-eligibility counts are the Urban Institute CCD directory rows for portal year 2021, fetched 2026-10-28. The mapping of "year 2021" to a school year is **[UNVERIFIED]** (the portal's labeling convention was not confirmed); say "portal year 2021" in the case. Do not mix in other years or the 2022 data (see Data).

**Data (as-of, re-fetched and recomputed 2026-10-28) [CONFIRMED + DERIVED].** Source: `https://educationdata.urban.org/api/v1/schools/ccd/directory/2021/?fips=31` (no key; 1,098 Nebraska schools; Bellevue Public Schools has 15 elementary schools, grade span to 6).
| School | NCESSCH | Enrolled | Qualify for meals (FRL) | Share |
|---|---|---|---|---|
| Betz | 310381001504 | 293 | 195 | 66.6% |
| Birchcrest | 310381001505 | 360 | 226 | 62.8% |
| Belleaire | 310381001500 | 299 | 184 | 61.5% |
| Avery | 310381001499 | 330 | 178 | 53.9% |
| **Core four (identical in A and B)** | | **1,282** | **783** | 61.1% |
| Central | 310381001506 | 172 | 81 | 47.1% |
| Wake Robin | 310381001518 | 506 | 135 | 26.7% |
| Twin Ridge (discussion point) | 310381001517 | 253 | 117 | 46.2% |
Plus-Central program: 1,454 pupils, 864 qualify; plus-Wake Robin: 1,788 pupils, 918 qualify. Counts reproduce the v1 values exactly.

**`lunch_program` code verified (fix c).** Portal variable list (`educationdata.urban.org/documentation/data/api-endpoint-varlist.json`, endpoint 24, field `lunch_program`, label "National School Lunch Program (NSLP) status") [CONFIRMED]: 0 = "No"; 1 = participating without any Provision or the CEP; 2 = under the Community Eligibility Provision (CEP); 3, 4, 5 = Provision 1, 2, 3; -1 = missing. **All 15 Bellevue elementaries are coded 0 in 2021, which the portal defines as "No", yet every one reports a free-or-reduced count.** (Statewide, 444 of 1,098 Nebraska rows are 0, 528 are 1, 50 are 2, 61 are 4.) So v1's claim that 0 means "not a community-wide free-meals school" is only half right: 0 rules out CEP and the Provisions (the counts are individual applications, not a blanket flag), but the literal code "No" conflicts with reported counts and the reason is not documented in the portal. Case wording: "reported free-or-reduced-price meal eligibility counts"; disclose the code oddity in a source note; do not describe the counts as "NSLP participants". Meal-eligibility counts are a proxy for family income and are an undercount where applications are not collected.

**Pedagogy.** Would close (2 thin skills, both how-to):
| id | kind | n | what the deliverable forces |
|---|---|---|---|
| advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-both-sides | how-to | 3 | Solve 81(r+506) = 135(r+172) for the marginal tie and 864(5r+1,788) = 918(5r+1,454) for the program tie |
| statistics-and-probability-how-to-write-a-linear-equation-given-a-graph-of-a-line-of-a-set-of-d | how-to | 3 | Write cost = 5f + v(1,282 + E) for each option and compare the two cost lines |
Also exercised (already covered, not claimed): percent of a number (qualifying share, n=90), ratio and unit rate (students per $1,000), margin as gap over winner. Tier T3 (T4 if students must also defend the objective and the r range, which the stated assumptions block makes natural).

**Socratic points (SPEC 7.3 seeds).**
1. Which number does a board report: the program's ratio or the new school's own? Show that they disagree for r in (329, 778) and ask which is easier to defend, and what each one ignores.
2. At r = 750 the program ratio says Central by 0.16%. Should a 0.16% lead decide anything? What would it take (new data, a better v) to decide?
3. B costs $40,080 more than A at the illustrative inputs ($664,560 vs $624,480). Does an equal-budget view change the answer?
4. A student finds Twin Ridge and notices it beats both. The board's two rules framed the fork. What does that say about rules like "most students" and "highest share" as selection tools?
5. "Share" versus "number": whose day does the coach actually reach?

**Facilitator note (SPEC 6, meals eligibility).** Family-income and meal-eligibility data: say "students who qualify for free or reduced-price meals", never "poor kids" or "bad schools". **Never rank or criticize the schools.** Real school names are data points only; the comparison is about where one extra program slot adds the most per dollar, not about the quality of a school, its teachers or its families. No individual child or teacher is named. Flag for the discussion lead that some students may live in qualifying households.

**Sensitivity / evidence notes.** Meal-eligibility counts depend on families applying; pandemic-era meal waivers around 2020-22 may have changed how schools collected applications (an inference, **[UNVERIFIED]** for Bellevue). Grand Island, Lincoln and Omaha 2022 rows had missing or distorted counts (Omaha 62 of 62 missing, from the v1 pull), so the case stays on Bellevue portal year 2021.

**Data feasibility: HIGH.** One free keyless API. Students can re-pull the rows themselves with the URL above. Not available: coach salaries by school, materials prices, school budgets.

**Ending (not the phone-buzz ending).** Odette writes one number on the whiteboard, r, circles it, and caps the marker before the principals come in; the case ends before the board's vote.

**Balance-test note.** A (Central): the largest share of the building is reached by each coach, and the program ratio is higher whenever coach cost is below 778 pupils' worth of materials. B (Wake Robin): the most children served in absolute terms, and the ratio is higher once coach cost is above 778; it also serves 54 more qualifying students. Margin never exceeds 3.3% across the plausible range 387 to 1,084 and is 0.16% at the illustrative inputs; max 13.60% at r=0. Not dominated.

### Fixes applied
| # | Reviewer item | Fix in v2 |
|---|---|---|
| a | R1a: marginal vs program narrative wrong in (329, 778) | Objective stated as the whole-program ratio with reasons; table showing where marginal and program rules disagree; made a Socratic point; r given as range 387-1,084; illustrative r=750 gives Central +0.16%, labeled a near-tie, not a finding |
| b | Label coach salary and materials cost | Modeling Assumptions block: BLS median $77,440 (May 2025, p10-p90 $47,980-$121,670) as a proxy, benefits load and v range [UNVERIFIED] |
| c | Verify `lunch_program` | Fetched portal variable list: 0 = "No", 2 = CEP, etc.; all 15 are 0 despite reported counts; wording and disclosure specified |
| d | School names data-only, no ranking | Facilitator note per SPEC 6 ("students who qualify for meals"); never rank or criticize schools |
| e | Bellevue 2021 as-of data | Re-fetched 2026-10-28 and recomputed; Central 172/81, Wake Robin 506/135, core four 293/195, 360/226, 299/184, 330/178 all reproduced |
| f | Margin convention | Gap / winner, stated once, applied to every margin |
| g | Protagonist name | Odette Hargrove: zero hits for "Odette" and "Hargrove" under `cases/`; Priya, Mara, Okafor, Raman avoided |
| h | Richer decision | Kept binary (SPEC 1.4) but added a deliberate marginal-vs-whole-program objective argument, a cost-difference (equal-budget) argument, and a surfaced Twin Ridge discussion point; shortlist defined by two equity rules instead of left unexplained |
| - | Ending | New ending (whiteboard, marker cap), not phone-buzz |

### Still open
- **Twin Ridge beats both finalists** on the program ratio for r in (98, 2,223) (+2.5% over the better finalist at r=750). The fork stays binary by board motion; R1a/R1c should say whether surfacing it as a discussion point is enough or the pair should change (for example Twin Ridge vs Wake Robin, where the tie is r=2,223, outside the plausible range, so that fork would fail the both-win-somewhere test).
- [UNVERIFIED] benefits load (1.0x-1.4x), materials per pupil v ($100-$200, illustrative $120), mapping of Urban portal "year 2021" to a school year, pandemic waiver effect on Bellevue's application counts.
- The BLS wage figures came through a summarizing fetch (bls.gov direct HTML returned 403 to curl, API rate-limited); confirm on the page before publishing. Instructional coordinator is a proxy occupation.
- `lunch_program` = 0 ("No") with nonzero counts is an undocumented portal oddity; cause not determined.
- Old marginal-tie values by year in v1 (329/258/279/132/168) were not recomputed here; drop them from the case.
