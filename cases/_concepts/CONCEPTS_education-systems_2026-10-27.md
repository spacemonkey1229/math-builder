# CONCEPTS: education-systems (Civic Life, Law & Learning) - 2026-10-27

Verified concept sheet. Tags: **[CONFIRMED]** = fetched and read by me this session; **[DERIVED]** = my own computation in code from fetched data (every number below was recomputed, none from memory); **[UNVERIFIED]** = not fetched, cut or disclose before use.

**Target.** Domain `education-systems` (`readmodel/domains.json`). Its signature skills are almost all well covered, so there are no zero-coverage holes to attack. I scored only skills at n <= 3 ("thin"); weights per SKILL.md (how-to 1.0, term 0.6). Scores are small; rank leans on closed thin skills first, then data and story.

**Overlap check.** `cases_index.json` and `cases/_concepts/`: existing education-adjacent cases are `college-admissions`, `placement-test`, `driving-age`, `the-trophy-and-the-table`, `psychologist`, `seton-hall`, `acton-survey`, plus the grep hit `CONCEPTS_agriculture-food_2026-10-27.md` (Nebraska pivot field; unrelated). None uses school-level targeting, school-closure siting, or institution-pair payback. Closest: `college-admissions` (admission rule); C3 below is about net cost versus earnings of two enrolled-student outcomes, not admission.

| Rank | Concept | Score | Data | Tier |
|---|---|---|---|---|
| C1 | The Fifth Coach | 2.0 | HIGH | T3 |
| C2 | The Quiet Closure | 0.0 (thickens n=4) | HIGH | T3 |
| C3 | The Payback Pair | 0.0 | HIGH (one UNVERIFIED field) | T3 |

**Recommendation.** Pick **C1** (The Fifth Coach). It closes two thin how-to skills, is the only one with a clean algebraic break-even (f/v = 778), keeps both options winning across a whole plausible range, and its data is one free, keyless, fetched API. **C2** is the best data story (the winner flips between years in six real years of data) and is a strong second, geometry-flavoured pick. **C3** is the most relatable to students but has the thinnest margin (0.65%) and no thin skills.

Common portals fetched (all [CONFIRMED]):
- **Urban Institute Education Data Portal API**, no key: `https://educationdata.urban.org/api/v1/schools/ccd/directory/{year}/?fips=31` (1,098 Nebraska schools for 2021; fields include enrollment, latitude, longitude, free_or_reduced_price_lunch, lunch_program, title_i_status). Docs page `https://educationdata.urban.org/documentation/` returns 200. Data Explorer `https://educationdata.urban.org/data-explorer/` returns 200.
- **College Scorecard API** (api.data.gov, DEMO_KEY): `https://api.data.gov/ed/collegescorecard/v1/schools.json?api_key=DEMO_KEY&school.state=MD&school.ownership=1&fields=...` returned 30 Maryland public institutions. DEMO_KEY hit `OVER_RATE_LIMIT` after about 30 calls/hour, so students will want a free personal key (the key is free at api.data.gov, [UNVERIFIED] signup page). Human-facing `collegescorecard.ed.gov/data/` was not fetched; the `/data/documentation/` URL I tried returned 404, so cite the API URL, not that page.

---

### C1 - The Fifth Coach   ·   score 2.0   ·   tier T3
**Protagonist.** Renata Cole (fictional), literacy director for Bellevue Public Schools, Nebraska. Constructed framing: the district, school names, enrollments and free-and-reduced-lunch (FRL) counts are real federal data; the "one more reading-coach slot" decision and the program cost structure are invented and must be disclosed as such. No such decision is claimed to have happened.
**The dilemma.** Four elementary schools already have a coach (the four with the most low-income students, whether ranked by percent or by count). Do you:
A.) Place the fifth coach and program at Central Elementary (smaller, 47% FRL), OR
B.) Place it at Wake Robin Elementary (much larger, 27% FRL but more FRL students in absolute terms)?
**Primary metric.** FRL students served per program dollar for the whole five-school program, cost = f per school (coach salary, fixed) + v per enrolled pupil (materials, assessments). The only free parameter is r = f/v, expressed in "pupils' worth of variable cost".
**Why it's close (both options win somewhere) [DERIVED].**
- Core four (identical in A and B): Betz 293 enrolled / 195 FRL, Birchcrest 360/226, Belleaire 299/184, Avery 330/178 = 1,282 pupils, 783 FRL.
- Central Elementary (NCESSCH 310381001506): 172 enrolled, 81 FRL (47.1%). Wake Robin (310381001518): 506 enrolled, 135 FRL (26.7%).
- Whole-program tie at **r = 778**. A wins when r < 778, B wins when r > 778. Margin of A over B: +15.74% at r=0, +10.21% at r=100, +6.93% at r=200, +4.26% at r=329, +1.18% at r=600, then B wins: -1.01% at r=1,000, -3.14% at r=2,000.
- The marginal swap alone ties at r = 329 (81 x (r+506) = 135 x (r+172)); the data check across years: 329 (2021), 258 (2022), 279 (2018), 132 (2019), 168 (2020). So the tipping point moves, but Central wins on the marginal swap at any r below the tipping point, and Wake Robin above it.
- Margin <= 20% at every r tested. A realistic r is a stated assumption: if a coach costs $90,000 and materials are $120 per pupil, r = 750, essentially at the tie (the $90,000 and $120 are illustrative inputs for students to replace, [UNVERIFIED], not sourced).
**Would close (2 thin skills, both how-to):**
| id | kind | n | label |
|---|---|---|---|
| advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-both-sides | how-to | 3 | Solve the tie: 81(r+506)=135(r+172), then the five-school version |
| statistics-and-probability-how-to-write-a-linear-equation-given-a-graph-of-a-line-of-a-set-of-d | how-to | 3 | Write cost = f + v x enrollment for a school from two program price quotes; compare slopes |
**Already-covered skills it also exercises.** `advanced-numbers-how-to-find-the-percent-of-a-number` (FRL share; n=90), unit rate / ratio comparison of FRL per dollar, ranking by percent versus count.
**Data feasibility: HIGH.** Source [CONFIRMED]: Urban Institute portal, CCD school directory 2021, Nebraska. All 15 Bellevue elementary schools have nonempty FRL counts, percent FRL ranges 15.8% to 66.6%, and `lunch_program` = 0 for all 15 in 2021, which is consistent with FRL being a real count here and not a community-wide free-meals flag; the exact meaning of the `lunch_program` code is [UNVERIFIED], so check the CCD codebook before saying it in the case. Grand Island, Lincoln and Omaha had missing or program-flag-distorted FRL in 2022 (Omaha 62 of 62 missing), so **use Bellevue 2021**, not those districts or years. Also state FRL is a proxy for family income and is undercounted wherever the community-eligibility option is in use.
**Sensitivity (SPEC §6).** Poverty labelling: describe pupils as "students who qualify for meals", never rank schools as "bad". Name a real school only as a data point. No individual teachers or children.
**Split risk.** NONE (2 thin skills claimed, well under 15).
**Balance-test note.** Not dominated: A wins on concentration and on lower fixed cost per pupil served; B wins on absolute count when coaches are the expensive part. The strongest argument for A is "more of each coach's day lands on a student who needs it"; the strongest for B is "one coach, one hundred thirty-five children". Margin <= 20% across the plausible range, tie at r=778.

---

### C2 - The Quiet Closure   ·   score 0.0 (thickens n=4)   ·   tier T3
**Protagonist.** Marcus Ibarra (fictional), facilities planner for a mid-sized suburban Nebraska district. Constructed framing: real enrollment and coordinates of two real Westside Community Schools (Omaha, NE) elementary schools, a hypothetical budget-forced closure that is NOT a real proposal (I did not search for one; [UNVERIFIED] whether any such proposal has ever existed). Disclose this prominently; name the schools only as data points.
**The dilemma.** One of two nearby schools has to close and its students move to the nearest remaining school. Do you:
A.) Close Hillside Elementary (about 370 students, nearest alternative 0.50 mi away) OR
B.) Close Rockbrook Elementary (about 280 students, nearest alternative 0.70 mi away)?
**Primary metric.** Added student-miles of travel per day (enrollment x straight-line distance to the nearest remaining elementary school, one-way; double it for the round trip; lower is better). Assumption: each school's students live at the school's coordinates (a T4-style modelling assumption the student must state; real attendance zones are not in the data). Straight-line is multiplied equally in both options, so it cannot change which is smaller.
**Why it's close (the winner flips by year in real data) [DERIVED].** Hillside (NCESSCH 317866001711) and Rockbrook (317866001716), nearest-remaining-school distance via haversine on CCD coordinates:
| year | Hillside n x d | Rockbrook n x d | closing Hillside costs vs Rockbrook | cheaper to close |
|---|---|---|---|---|
| 2017 | 414 x 0.500 = 207.1 | 292 x 0.698 = 203.9 | +1.5% | Rockbrook |
| 2018 | 390 x 0.500 = 195.1 | 280 x 0.678 = 189.9 | +2.7% | Rockbrook |
| 2019 | 380 x 0.500 = 190.1 | 283 x 0.698 = 197.6 | -3.8% | Hillside |
| 2020 | 379 x 0.500 = 189.6 | 273 x 0.698 = 190.6 | -0.6% | Hillside |
| 2021 | 368 x 0.500 = 184.1 | 283 x 0.698 = 197.6 | -6.9% | Hillside |
| 2022 | 372 x 0.500 = 186.1 | 275 x 0.698 = 192.0 | -3.1% | Hillside |
Break-even for 2021: Hillside would need 395 students (versus 368), or Rockbrook would need 264 (versus 283), to tie. Margin never exceeds 6.9%. The tension: a bigger school with a short hop versus a smaller school with a long hop, and enrollment drifts year to year. Receiving-school loads differ too (Hillside's students would go to Westbrook, 549 enrolled in 2021; Rockbrook's to Prairie Lane, 271), a discussion point since capacity is not in the data.
**Would close (0 thin skills; thickens one n=4):**
| id | kind | n | label |
|---|---|---|---|
| geometry-how-to-find-the-distance-between-two-coordinate-pairs-on-a-coordinate-plane | how-to | 4 | Distance formula from latitude/longitude pairs (convert to a local grid first) |
**Already-covered skills it also exercises.** Pythagorean theorem (n=6), weighted comparison, percent difference, reading a six-year table. Honest scoring: this concept does not close a thin skill (n=4, outside the n<=3 bar), so its score is 0.0; it earns its place on geometry and on a real flip.
**Data feasibility: HIGH.** Source [CONFIRMED]: Urban Institute portal, CCD school directory for Nebraska, years 2017 to 2022 (1,116 / 1,111 / 1,107 / 1,096 / 1,098 / 1,104 rows), fields enrollment, latitude, longitude, school_status, school_type, grade range. Each year's nearest-neighbor distance was recomputed in code from the fetched rows. Not available: school capacities, attendance boundaries, bus routes, closure cost savings, so the case is a single-metric siting problem and must not claim to model total closure savings.
**Sensitivity (SPEC §6).** School closure is emotionally loaded for real communities. Use "reassignment" language, keep to the disclosed hypothetical, no named teachers or families, note this is geometry, not an evaluation of either school.
**Split risk.** NONE.
**Balance-test note.** Not dominated: A wins in 4 of 6 years, B wins in 2 of 6; the leader flips on a 2% to 7% swing and the enrollment trend (Hillside shrinking from 414 to 372, Rockbrook roughly flat) is itself the argument. Margin <= 7% in every year.

---

### C3 - The Payback Pair   ·   score 0.0   ·   tier T3
**Protagonist.** Imani Okafor (fictional), a 27-year-old returning student in Maryland weighing two public universities (adult, not a minor; no real person). Constructed framing: the person is invented; the institution figures are the federal College Scorecard values for the two named public universities.
**The dilemma.** Do you:
A.) Enroll at Morgan State University (lower net cost per graduate) OR
B.) Enroll at Frostburg State University (higher median earnings)?
**Primary metric.** Years of 10-year-median earnings needed to repay the expected net cost per completer = (4 x average annual net price / completion rate) / median earnings 10 years after entry; lower is better.
**Why it's close [DERIVED], Scorecard values fetched today:**
| | Morgan State (id 163453) | Frostburg State (id 162584) |
|---|---|---|
| average annual net price (public) | $14,653 | $16,768 |
| completion rate (4-yr, 150%) | 41.57% | 44.93% |
| expected net cost per completer (4 x price / rate) | $140,996 | $149,281 |
| median earnings 10 yr after entry | $56,585 | $60,300 |
| payback ratio | 2.4918 | 2.4756 |
- Frostburg wins the primary metric by **0.65%** (cost per completer 5.55% higher, earnings 6.57% higher, cancelling). Morgan would tie at a completion rate of 41.84% (observed 41.57%, a 0.27-point gap, well inside cohort noise); Frostburg would tie if its completion rate fell to 44.64%.
- Robustness (both options win under defensible metric choices): using 6-year earnings (Morgan $46,106, Frostburg $47,727), Morgan wins (3.058 vs 3.128, 2.2%). Using the Scorecard "suppressed" completion rate (Morgan 41.22%, Frostburg 47.29%), Frostburg wins by 6.4% (2.5129 vs 2.3521). The 4, 5 and 6-year program lengths scale both sides equally and do not change the order. Median debt of completers is also in the data (Morgan $25,500, Frostburg $17,959), a third variable that favors Frostburg, kept out of the primary metric for balance.
**Would close (0 thin skills).** Candidate skills (no thin match, so honest score 0): `advanced-numbers-how-to-find-the-percent-of-a-number` (n=90, percent cost difference), ratio/unit-rate comparison, break-even completion rate by rearranging the payback formula. If a T4 version is wanted, add confidence-interval-on-a-proportion using the cohort size (see below), which could pull in the thin statistics skills.
**Data feasibility: HIGH.** Source [CONFIRMED]: College Scorecard API (api.data.gov), fields `latest.cost.avg_net_price.public`, `latest.completion.completion_rate_4yr_150nt`, `latest.completion.rate_suppressed.overall`, `latest.earnings.10_yrs_after_entry.median`, `latest.earnings.6_yrs_after_entry.median`, `latest.aid.median_debt.completers.overall`, all returned for these two institutions. Scorecard cohort size (`latest.completion.completion_cohort_4yr_150nt`) exists as a field (I confirmed it on Montgomery College: 1,552 for a 2-year cohort), but I was rate-limited before pulling it for these two, so the cohort sizes and the data vintage year are [UNVERIFIED]. The 4-year-completion rate describes first-time full-time students only; this limitation must appear in the case. Selection effects (who each school admits) mean the payback ratio is not a causal "value-add".
**Sensitivity (SPEC §6).** Morgan State is a historically Black university; present both institutions with equal respect, never as a ranking of worth, and do not let the case imply differing earnings are due to a school's students.
**Split risk.** NONE.
**Balance-test note.** The 0.65% margin is the Robotics-gold-standard tight (0.09%) class, and it flips with a defensible metric choice (6-year earnings, suppressed completion). Primary risk is that the margin is so small it reads as a tie; the case should state the tie completion rate and make students argue which input they trust.
