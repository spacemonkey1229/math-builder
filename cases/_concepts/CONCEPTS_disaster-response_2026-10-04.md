# Concept sheet: disaster-response (2026-10-04)

Produced by `case-brainstorm` under the STRICT cold-solve rule from `REVIEW_BRIEF_non-sports-slots_2026-10-04.md` (four failed sheets: metric lets one option dominate, or answer set by an invented parameter). Every number below was fetched on 2026-10-04 and recomputed in Python before any recommendation. No case folder written.

## Domain choice
`disaster-response` (data grade HIGH in `readmodel/domains.json`; existing cases Wildfire, Airstrike, Food Rationing, none about hurricane evacuation timing or federal logistics). Candidates rejected after checking real data:
- mining-minerals: zero cases, but every unit cost (strip cost, underground cost per tonne, mill cost) would be an invented or paywalled company figure; public filings (Freeport 10-K, Codelco) gave capex and tonnage but no unit costs. Fails the "no invented parameter" rule.
- media-recommendation: `the-cold-start` and Movie Producer / Cinema already cover it.
- transit-routing: real GTFS fetched (NYC MTA M15 local vs M15+ SBS: 234 m vs 670 m stop gap, 90 vs 68-79 min scheduled run time). Cold solve showed the limited-stop option wins for any trip longer than about 1.5 km (break-even about 1.5 km at 4.5 km/h walking; about 2.3 km at an older-adult 0.8 m/s). Typical bus trips are longer, so it is dominated for the average rider. Dropped, not recommended.
- robotics, construction: data MEDIUM, mostly datasheets / permit counts, no real-data metric found.

## Ranking
| Rank | Concept | Anchor event | Passes balance test? |
|---|---|---|---|
| C1 | The Just-in-Time Order | Hurricane Ian, Lee County FL, Sept 26-27 2022 | Yes, conditionally (sign flips inside sourced ranges; model has two structural assumptions, disclosed) |
| C2 | The Sixth Depot | FEMA distribution-centre network, Katrina/Sandy/Ida-era declarations | Yes (sign flips between three real weightings; but pair of candidate sites is constructed) |

Third concept intentionally omitted: nothing else in the domain reached a cold-solved, real-data metric.

---

### C1 - The Just-in-Time Order   ·   score n/a (closes 0 zero-coverage skills; thickens 1 thin skill)   ·   tier T3 (applied probability + time)
**Protagonist.** Fictional composite, "Renata Okafor", deputy emergency manager of a Gulf Coast county of about 760,000 people. (Use a fictional protagonist; real Lee County officials and 57 county deaths make a named real official inappropriate.) Personally at stake: she signs the order, and either way people will second-guess it.
**The dilemma.** A.) Order Zones A, B and C (about 531,000 residents) evacuated Monday 5 pm EDT, 30 h before tropical-storm winds, when the storm is forecast mostly toward Tampa Bay OR B.) Wait one forecast cycle and order Zones A and B (about 382,000) Tuesday 7 am EDT, 16 h before onset (what Lee County did, its "just-in-time" protocol, adopted 2010).
**Primary metric.** Expected cost in person-evacuation-equivalents: (people evacuated unnecessarily) plus lambda x (people not yet cleared when winds arrive, weighted by hit probability), where lambda = (value of statistical life x chance of death if caught) / (cost of evacuating one person).
**Why it's close.** Waiting is cheap if the storm turns away (NHC hurricane-force probability at Fort Myers was only 17% Monday evening) but leaves 16 h against a 13-14 h clearance time for A+B and a 19-20 h clearance for Zone C. Ordering early costs 149,000 extra people (zone C) and about 150,000 more evacuees certain, but zero uncleared people. Which wins turns on how long clearance really takes (two official sources disagree) and on how lethal being uncleared is.

**Real data (all fetched, free):**
| Input | Value | Source |
|---|---|---|
| Zone populations (2010 Census) A / B / C / D / E | 153,117 / 228,608 / 149,281 / 36,061 / 38,168 | Lee County "Evacuation Clearance Times" page, leegov.com |
| County clearance times (h) A / B / C / D / E | 10-10.5 / 13-14 / 19-20 / 27.5-32.5 / 35.5-40.5 | same page (definition: order issued until last evacuee leaves zone or reaches shelter) |
| Conflicting figure | "36 hours to evacuate a Zone A population of 375,078"; up to 41 h in county, up to 89 h out of region | WUSF/WGCU article citing SWFRPC. **UNVERIFIED which table/scenario this is; do not mix with the county page without checking the SWFRPC Vol 1 Ch VI / Vol 4 PDFs** |
| Tropical-storm-wind onset, Fort Myers area | about 0300 UTC 28 Sep (11 pm EDT Tue 27 Sep) | NHC Tropical Cyclone Report AL092022 (Hurricane Warning 0900 UTC 27 Sep "about 18 h before onset on the barrier islands"; Tropical Storm Warning 2100 UTC 26 Sep "about 30 h before") |
| Lee County order timeline | 7:00 am Tue: Zone A + part of B; 8:45 am: all A and B; 1:45 pm: add part of C; 6:30 pm: "seek shelter by 8 pm"; landfall 3:05 pm Wed 28 Sep | Lee County Hurricane Ian After-Action Report (Aug 2023), pp 9-10, 17 |
| NHC hurricane-force (64 kt) cumulative probability, Fort Myers, by advisory | Adv 14 (Mon 1500Z) 14%; Adv 15 (Mon 2100Z) 17%; Adv 16 (Tue 0300Z) 21%; Adv 17 (Tue 0900Z) 25%; Adv 18 (Tue 1500Z) 39%; Adv 19 (Tue 2100Z) 55%; Adv 20 (Wed 0300Z) 81% | NHC archive `al092022.wndprb.NNN.shtml`, public domain |
| Same, Tampa | 36% (Adv 15), 49% (Adv 16), 35% (Adv 19), 16% (Adv 25) | same |
| Final outcome | Landfall Cayo Costa, category 4; 156 US deaths, 66 direct, surge 41 deaths of which 36 in Lee County; 10-15 ft inundation Fort Myers Beach; Storm Surge Warning north of Englewood did not verify | NHC TCR |
| Hillsborough ordered about 300,000 evacuated Monday | WUSF 2022-09-26 (Pinellas Zone A order 6 pm Mon) |
| Cost of evacuating | median household $211 (voluntary) / $292 (mandatory); Harvey Coastal Bend about $1,200 per household; about $88-350 per day in older storms | Whitehead 2003 (UNCG), Rice/Smith evacuation-cost papers; per-person conversion needs household size about 2.5 (**UNVERIFIED**) |
| Value of statistical life | $13.2M (2023$), $13.7M (2024$) | US DOT guidance (Federal Register 2024-04-18) |

**Cold solve (script `ian_solve.py`, `ian_grid.py` in the session scratchpad; reproduced here).**
Timing: slack = onset minus order time = 30.0 h (A, Mon 2100Z), 16.0 h (B, Tue 1100Z), 9.25 h for a Zone C order at Tue 1745Z.
Model: cost_A = N_ABC + h x lambda x uncleared_A, cost_B = q x N_AB + h x N_C + h x lambda x (uncleared_AB + uncleared_C). Uncleared fraction = max(0, 1 - slack / clearance) (linear departure). h = 0.17 (NHC, Adv 15). q = chance that waiting still ends in an order (q = h if forecasts fully resolve; q = 1 if waiting never changes the decision). s = multiplier on county clearance times (s = 1 county page; s = 3.6 is the ratio of the SWFRPC 36 h to the county 10 h Zone A figure).
Break-even lambda (B better below it):

| s \ q | 0.17 | 0.30 | 0.50 | 1.00 |
|---|---|---|---|---|
| 1.0 | 33 | 29 | 24 | 9 |
| 2.0 | 13 | 11 | 9 | 4 |
| 3.6 | 15 | 14 | 11 | 4 |

Plausible lambda from sourced inputs: pi = P(death | uncleared, hit) of 1.2e-4 to 3.1e-4 (Ian's 36 Lee surge deaths over 115k-305k residents who stayed in A+B; the stay fraction is an **assumption**), c = $85-$480 per person, VSL $13.2M, so lambda runs from about 3.3 to about 48. This range straddles every break-even above except the q = 1 column. Result on the sourced (pi, c) grid, share of 9 cells where waiting (B) wins: s=1.0: 8/9, 7/9, 7/9, 4/9 (q = .17/.30/.50/1.0); s=2.0: 4/9, 4/9, 4/9, 1/9; s=3.6: 5/9, 5/9, 4/9, 1/9.
Reading: **neither option dominates.** With county-published clearance times and any real information value from waiting (q below 1), waiting wins most cells. If the clearance times are about twice the county's own table, or if waiting rarely changes the decision, ordering early wins most cells. The sign of B minus A flips inside the plausible range.

**Honest weaknesses.** (1) 64-kt wind probability at a city is a proxy for surge risk to Zones A-C; the NHC probabilistic storm-surge product is the better input and was not fetched. (2) q and linear clearance are modelling choices; the case should expose them as sliders with the sourced range, not hide them. (3) The 10-14 h county figures vs 36-41 h regional figure must be resolved from the SWFRPC PDFs before writing (flagged). (4) Hindsight: use only forecasts and numbers available at each decision time.
**Would exercise (thin skills in bold):** `measurement-how-to-find-elapsed-time` (n=12), `measurement-how-to-add-and-subtract-time` (n=16), **`measurement-how-to-find-the-start-or-end-time-given-the-start-or-end-and-the-elapsed-time` (n=3)** (latest order time = onset minus clearance), `statistics-and-probability-how-to-determine-the-probability-of-a-single-event` (n=14), `advanced-numbers-how-to-find-the-percent-of-a-number` (n=89), `number-sense-how-to-compare-two-or-more-values`, `measurement-how-to-convert-an-amount-with-compound-units` (n=20). All ids verified in `standards_spine.json`.
**Data feasibility: HIGH.** NHC advisory/probability archive and TCR (US public domain), Lee County pages (public), AAR (public PDF). Not confident: SWFRPC clearance table, per-person evacuation cost, share who stayed.
**Sensitivity (SPEC §6).** FLAG: real storm with 150+ deaths and criticism of real local officials. Use fictional protagonist, frame as protection (people cleared), no casualty imagery, facilitator note that real deaths occurred.
**Split risk.** NONE. **Overlap.** Wildfire / Airstrike are different hazards; no hurricane case in corpus.
**Verified story.** Lee County's JIT protocol, the Tue 7 am order, TS onset and the Tampa-vs-Fort Myers forecast shift are confirmed from NHC TCR + Lee AAR + WUSF. County manager's "timing just wasn't right" quote is from WUSF (secondhand, UNVERIFIED against a primary transcript).

---

### C2 - The Sixth Depot   ·   score n/a (thickens 1 thin skill)   ·   tier T3
**Protagonist.** Fictional "Marcus Bell", logistics planner at a federal emergency agency, who must recommend where to put a sixth continental distribution centre. Personally at stake: his name is on the memo, and the first test comes in hurricane season.
**The dilemma.** A.) Build in Kansas City, MO (central, best all-hazard reach) OR B.) Build in Jackson, MS (Gulf-adjacent, best hurricane reach).
**Primary metric.** Average straight-line miles from the nearest depot to a disaster county, weighted by what the planner decides counts (declarations, residents, or federal dollars), plus the share of weight farther than 400 miles (about one long driving day).
**Why it's close.** Kansas City cuts miles for the many tornado, flood and winter-storm declarations; Jackson cuts miles for the few huge hurricane disasters that carry most federal dollars. Which weighting is right is the actual argument.

**Real data (fetched, free):**
- OpenFEMA `DisasterDeclarationsSummaries` v2 (70,430 rows, county-level FIPS, incident type, dates) and `FemaWebDisasterSummaries` v1 (per-disaster PA and IHP dollars; only 2,843 of 4,036 rows have PA dollars, newest disasters lag, e.g. Harvey shows only $4.7B, **UNVERIFIED vs published totals**). OpenFEMA data is public domain / free, no key.
- Census 2023 Gazetteer county centroids (public), Census 2020 county population estimates (public).
- Existing FEMA depots from fema.gov Distribution Warehouse listing: Atlanta GA, Fort Worth TX, Frederick MD, Cumberland MD, Moffett Field CA (plus Hawaii, Guam, Puerto Rico, excluded; CONUS counties only). Coordinates are approximate city/base lat-lon (**UNVERIFIED to the metre; only matters at the mile scale**).

**Cold solve (`fema_solve*.py`).** Sample: 40,079 county-declaration records, major disasters (DR) only, CONUS, 2000-2025, COVID ("Biological") excluded. Mean miles to nearest depot, existing network alone: 371 (count), 321 (population), 308 (federal $).

| Weighting (2000-25) | Kansas City | Jackson MS | New Orleans | Mobile | Winner |
|---|---|---|---|---|---|
| declarations (count) | 279 (17% >400 mi) | 350 | 357 | 359 | Kansas City by 71 mi |
| residents of declared counties | 289 (23%) | 309 | 310 | 310 | Kansas City by 20 mi |
| federal PA+IHP $ | 285 (16%) | 258 (15%) | 259 | 272 | **Jackson by 27 mi** |

Same ordering holds for 2010-25 and 2015-25 windows (e.g. 2015-25 $: KC 282 vs Jackson 267). By hazard (count-weighted, base 256 hurricane): hurricane/tropical records Jackson 207 vs KC 256; severe storm/tornado KC 273 vs Jackson 372; flood KC 356 vs Jackson 508.
Break-even mix: weighting that is a blend of $ share and another measure, Jackson wins when the dollar share exceeds 73% (blended with count) or 43% (blended with population); for New Orleans 76% / 45%; Mobile never a close winner (86% / 61%). **The sign flips in the interior of the weighting range, not by an invented parameter.**
Robustness check that matters pedagogically: the top 5 dollar-weighted disasters (Katrina 18.9B, Sandy 15.9B, Ida 4.9B, a 2001 "Fires and Explosions" record 4.7B, Harvey 4.7B) are 32% of all dollars. Dropping them, Jackson loses its $ edge (Jackson 288 vs KC 285). So the Gulf case rests on a handful of catastrophes. A good student finding, and a true tension (plan for the typical event or the catastrophic one).
**Honest weaknesses.** (1) Straight-line miles, not drive time; fine for ranking, say so. (2) The candidate pair is constructed (no known real FEMA decision between these two sites). Disclose; anchor the story on Katrina's well-documented supply failures (UNVERIFIED which specific articles to cite; verify against DHS OIG / House Select Committee Katrina report before writing). (3) Dollar allocation split equally across a disaster's counties is crude. (4) Distance is a proxy for time-to-first-delivery, not for need.
**Would exercise:** **`geometry-how-to-find-the-distance-between-two-coordinate-pairs-on-a-coordinate-plane` (n=4, thin)** (students convert lat/lon to a plane approximation with the cos(latitude) scaling, or use the Pythagorean theorem on a local grid), `geometry-coordinate-plane`, `geometry-pythagorean-theorem`, `statistics-and-probability-how-to-find-the-mean-of-a-set-of-data`, `advanced-numbers-how-to-find-the-percent-of-a-number`, `number-sense-how-to-compare-two-or-more-values`. All ids verified.
**Data feasibility: HIGH.** Specific free documents: OpenFEMA DDS and FemaWebDisasterSummaries, Census Gazetteer, Census population estimates.
**Sensitivity (SPEC §6).** NONE (logistics); mention real disasters respectfully.
**Split risk.** NONE.

---

## Recommendation and verdict
Write C1 first, with C2 as the second. Neither is perfect.
- **C1 passes the balance test, conditionally.** Using only sourced ranges, the sign of B minus A flips (lambda break-even 4-33 sits inside the plausible 3-48), and the answer genuinely depends on two real, checkable things: whether county clearance times are right (two official sources disagree) and how much waiting buys. It does depend on two modelling choices (q, linear clearance), which must be shown as adjustable, and the SWFRPC table must be reconciled before writing.
- **C2 passes more cleanly on parameters** (all inputs are fetched data; the flip comes from three legitimate weightings) but its dilemma pair is constructed, and a reviewer may call the real tension a values question (typical vs catastrophic events), which is acceptable if the case says so.
- Neither is "decorative math": C1 forces elapsed-time arithmetic and a probability-weighted comparison; C2 forces distance computation and weighted means.
- Neither closes any zero-coverage skill (the domain has 0 uncovered signature skills), so ranking here is by balance and data quality, not gap score.
