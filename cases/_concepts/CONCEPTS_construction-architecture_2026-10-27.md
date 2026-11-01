# CONCEPTS: construction-architecture (Built Environment) - 2026-10-27

Verified concept sheet (data fetched 2026-10-27). Tags: **[CONFIRMED]** fetched and read by me; **[DERIVED]** my own computation from fetched data
(re-run at research); **[UNVERIFIED]** not fetched, must be sourced or disclosed as a Modeling Assumption.

**Target.** Domain `construction-architecture`. Its signature skills are mostly covered, so I targeted the few skills still at `n <= 2` that a
building decision can force (pre-calculus trig terms/how-to). Two of the three concepts are data-led and close few thin skills; flagged honestly.

**Overlap check.** `cases_index.json` + `cases/_concepts/`: existing built-environment cases are `house-plans` (floor-plan cost), `carpenter`
(flooring TCO), `roofline-call` (gable vs hip lumber), `creek-span` (truss steel), `plaza-pavers` / `the-plaza-bid` (paving tessellation),
`the-painted-gallon` (water tower), `the-deep-end` (pool ramp). Grepped concept sheets for overhang, degree day, gutter, cistern, heat pump,
insulation, stair, ramp: no hit other than `the-deep-end` (ramp, different premise). None of C1-C3 reuses a premise above.

---

### C1 - The Overhang Depth   -   score 1.6 ((0.6 term + 1.0 how-to) x 1.0 HIGH)   -   tier T4   -   RECOMMENDED

**Protagonist.** Mara Oyelaran (fictional), a residential designer finishing a south-facing family room for a spec-home builder in Austin.
**Story/framing.** Constructed, disclosed: a real, standard passive-solar detail (roof overhang over south glazing) at a real climate station.
**Dilemma.** A.) Draft a 2-ft overhang OR B.) Draft a 3-ft overhang, over a 5-ft-tall south window whose head sits 0.5 ft below the soffit.
**Primary metric.** Annual "unwanted-sun penalty" in degree-days: sum over months of (shaded fraction x HDD, the winter sun you lose) + (open
fraction x CDD, the summer sun you admit), using the noon profile angle. Lower is better.
**Math.** Noon solar altitude = 90 - |latitude - declination|; shadow drop = depth x tan(altitude); open fraction = 1 - clamp(drop - 0.5, 0, 5)/5.
**Would close (2 skills):**
| id | kind | label |
|---|---|---|
| pre-calculus-tangent-function | term | Tangent Function |
| pre-calculus-how-to-find-the-sine-cosine-and-tangent-of-an-angle-using-the-unit-circle | how-to | How to find the sine, cosine, and tangent of an angle using the unit circle |
Optional extension (n=3, not counted): `pre-calculus-how-to-evaluate-an-inverse-trigonometric-function` (solve for the sun angle that just clears the sill).
**Balance computed [DERIVED], 2 ft (A) vs 3 ft (B), degree-days, lower wins:**
| Station (NCEI 1991-2020 normals) | A 2 ft | B 3 ft | Winner | Margin |
|---|---|---|---|---|
| Miami Intl | 1087 | 605 | B | 79.7% |
| Las Vegas McCarran | 1027 | 920 | B | 11.6% |
| Houston Hobby | 817 | 728 | B | 12.3% |
| New Orleans | 825 | 698 | B | 18.3% |
| San Antonio Intl | 829 | 845 | A | 1.9% |
| **Austin Bergstrom** | 886 | 959 | **A** | **8.3%** |
| Dallas-Ft Worth | 943 | 1117 | A | 18.4% |
| Atlanta | 932 | 1210 | A | 29.8% |
| Denver | 1624 | 2416 | A | 48.8% |
| Chicago O'Hare | 1496 | 2197 | A | 46.8% |
| Seattle-Tacoma | 953 | 1490 | A | 56.4% |
Break-even (equal penalty) falls between San Antonio (A by 1.9%) and Houston (B by 12.3%), roughly 29.6 to 30.2 deg N for this window. Setting the case
at Austin gives A winning by 8.3%; every city 150 miles away flips or runs to 50%+, which is the Socratic hook (same detail, different latitude/HDD:CDD mix).
Sensitivity (window 4 ft tall, head gap 1.0 ft): Austin A by 19.1%, Houston B by 6.9%, San Antonio A by 10.3%, Las Vegas B by 2.5%. Still both-win. Window height and
head gap are student-visible inputs, so the margin moves with a stated assumption (disclose).
**Hidden assumptions to disclose.** Noon-only profile angle (ignores azimuth and hourly sun); mid-month declination via Cooper's formula; HDD and CDD weighted equally per
degree-day (a heat pump or AC COP would reweight; sensitivity table advised); no glass shading coefficient.
**Data feasibility: HIGH.**
- NOAA NCEI Climate Normals 1991-2020 monthly HDD/CDD by station, free JSON API (`ncei.noaa.gov/access/services/data/v1?dataset=normals-monthly-1991-2020&stations=USW00013904&dataTypes=MLY-HTDD-NORMAL,MLY-CLDD-NORMAL&format=json`) [CONFIRMED, fetched 11 stations returned 12 monthly rows each; Austin Bergstrom is USW00013904, lat 30.1831].
- NOAA GML Solar Calculator equations page `gml.noaa.gov/grad/solcalc/calcdetails.html` [CONFIRMED reachable; I used the simpler Cooper declination, so students should cross-check against NOAA's equations and the NOAA online calculator].
Skill-ranking note: 0.6 + 1.0 = 1.6 raw; trig is a pre-calc stretch band so tier T4 (must state noon-only and equal-weight assumptions).

---

### C2 - Up or Out   -   score 0 thin skills closed (thickens covered ones)   -   tier T3

**Protagonist.** Dev Raman (fictional), an Alt-1 filing expediter helping a Queens two-family owner decide how to add about 350 sq ft.
**Story/framing.** Real filing records, constructed owner. Option labels follow the DOB's own "vertical enlargement" and "horizontal enlargement" checkboxes.
**Dilemma.** A.) File a vertical enlargement (add up, build a partial new floor over the existing footprint) OR B.) File a horizontal enlargement (build out into the rear yard).
**Primary metric.** Median declared job cost per square foot of enlargement on comparable signed-off 1-2-3 family Alteration-1 filings (2011 onward), in the owner's size band.
**Balance computed [DERIVED] from `data.cityofnewyork.us/resource/ic3t-wcy2.json`** (DOB Job Application Filings; filters: job_type A1, building_type 1-2-3 FAMILY, job_status_descrp SIGNED OFF, only one of
vertical/horizontal flagged, enlargement_sq_footage 50-5000, initial_cost > 0; costs not inflation-adjusted; pulled 10,141 vertical and 10,706 horizontal rows):
| Enlargement band (sq ft), filings 2011+ | Vertical $/sf (n) | Horizontal $/sf (n) | Winner | Margin |
|---|---|---|---|---|
| 100-300 | 510.1 (272) | 359.2 (892) | Horizontal | 42.0% |
| 200-300 | 477.3 (172) | 332.4 (457) | Horizontal | 43.6% |
| 250-300 | 283.0 (83) | 282.2 (225) | Horizontal | 0.3% |
| **300-450** | 231.5 (257) | 254.0 (557) | **Vertical** | **9.7%** |
| 450-600 | 189.9 (250) | 221.3 (539) | Vertical | 16.5% |
| 600-900 | 125.0 (844) | 196.7 (820) | Vertical | 57.4% |
Bootstrap 95% intervals on the 300-450 medians overlap (vertical 178-296, horizontal 217-303), so the "win" is not statistically separable: this is the discussion, not a flaw. Break-even size is about 300 sq ft; below it
horizontal wins decisively, above it vertical. Whole-pool medians over all sizes are 60.4 (vertical) vs 86.0 (horizontal) $/sf, which is a size-mix artifact (vertical filings are larger); students must catch that (Simpson-style confounding).
Dataset `rowsUpdatedAt` = 2026-10-27 [CONFIRMED live]. Declared costs are applicant-stated, unaudited, and BIS-era dollars (2011-2026 not deflated); disclose.
**Would close (0 skills at n <= 2).** Exercises `statistics-and-probability-median` (n=8), `measurement-how-to-convert-an-amount-with-compound-units` (n=21), `advanced-numbers-how-to-find-the-percent-of-a-number` (n=90), `geometry-how-to-find-the-measure-of-the-perimeter-of-a-polygon` (n=6, a footprint sketch). Flag: coverage-lite; best used as a Domain-diversity / real-data slot rather than a gap-closer.
**Data feasibility: HIGH** (Socrata API, free, no key for these queries, [CONFIRMED]). Weakness: small bins (n 83-260 on the vertical side), noisy self-declared costs. A second check against Census building permit valuation was attempted; the BPS state files give units only [CONFIRMED], not valuation, so there is no second source.

---

### C3 - The Attic Blanket   -   score 0 thin skills closed   -   tier T3   -   WEAKEST (cost input unverified)

**Protagonist.** Priya Venkataraghavan (fictional), a weatherization contractor quoting two attic upgrades on a 1,600 sq ft ranch.
**Dilemma.** A.) Blow in to R-38 (about 10 inches) OR B.) Blow in to R-60 (about 16 inches), heating with a 2.5-COP heat pump.
**Primary metric.** 30-year cost per square foot of attic floor = installed price + heating electricity (HDD x 24 / R / 3412 BTU per kWh / COP x state residential price x 30).
**Balance computed [DERIVED]** with a premium of R-60 over R-38 of $0.60/sf **[UNVERIFIED, constructed]** and base install $1.00/sf **[UNVERIFIED]**:
Denver B by 6.9%, Chicago B by 10.5%, Minneapolis B by 12.9%, Seattle A by 3.2%, Atlanta A by 14.4%, Boston B by 19.5%, Las Vegas A by 27%, Houston A by 33%.
Break-even near Seattle/Denver HDD (about 4,400-5,800) at that premium; at a $0.90 premium it moves to Chicago-Minneapolis HDD, which shows the case's answer is premium-dependent.
**Data [CONFIRMED]:** NCEI HDD normals (same API as C1), EIA Electric Power Monthly Table 5.6.A state residential price, August 2026 (e.g. TX 15.91, CO 17.17, IL 19.32, WA 14.63, MA 30.48 cents/kWh; `eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a`). **Not confirmed:** the blown-insulation per-inch price (needs a named retailer/contractor price sheet or DOE cost-effective R-value table).
**Would close:** none at n <= 2. Flag: thermal-envelope premise sits near C1 (both use NCEI degree-days); do not run both in one batch.
**Data feasibility: MEDIUM** (energy side HIGH, cost side UNVERIFIED).

---

## Ranking and recommendation

1. **C1 The Overhang Depth** - only concept that closes thin skills (2), HIGH data (NOAA), computed both-win with a clean flip across latitudes; Austin margin 8.3%.
2. **C2 Up or Out** - best real-data story (NYC DOB, updated today, size threshold ~300 sq ft, margin 9.7% at 300-450), but closes no thin skills.
3. **C3 The Attic Blanket** - overlaps C1's data and depends on an unverified cost input; only develop if the install price is sourced.

Recommended pick: **C1** (set at Austin, A 2 ft wins by 8.3%; flips to B at Houston/Las Vegas).
