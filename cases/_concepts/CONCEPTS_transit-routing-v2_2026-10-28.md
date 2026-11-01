# Concept sheet v2 — Transit, Routing & Last-Mile Logistics — 2026-10-28

Revision of `CONCEPTS_transit-routing_2026-10-27.md` after R1 round 1. C1 The Spare Bus was DROPPED
(R1a: Route 21 wins under any uniform schedule-awareness share; R1c: metric twin of Reroute Or Wait).
This sheet develops the old **C2 Fixed Or Flex** into a single full concept. Nothing is written under `cases/<id>/`.

**Margin convention (stated once, applied everywhere in this sheet): margin = (winner - loser) / winner, on the primary metric.**
(The v1 sheet divided by the loser; v1's 5.26 % for 2025 is 5.00 % here.)

| # | Title | tier | feasibility | margin (frozen decision year, RY2024) |
|---|---|---|---|---|
| C2 | **Fixed Or Flex** | T4 | HIGH (one public API, recomputed) | **6.48 %** (fixed route over demand-response, base case) |

## Method and data log (fetched and recomputed in Python on 2026-10-28)

| Source | Fetched | What it gave |
|---|---|---|
| NTD "2022 - 2025 NTD Annual Data - Metrics", Socrata `https://data.transportation.gov/resource/ekg5-frzt.json` (filter agency like `%Westmoreland%`, NTD ID 30044) | LIVE, HTTP 200, no key; 8 rows (MB and DR for report years 2022-2025). Dataset `rowsUpdatedAt` 2026-10-14 | `total_operating_expenses`, `vehicle_revenue_hours`, `unlinked_passenger_trips`, `passenger_miles`, `fare_revenues_earned`, `vehicle_revenue_miles`, `agency_voms`, `mode_voms` |
| NTD dataset metadata `https://data.transportation.gov/api/views/ekg5-frzt` | LIVE | Description: only Full Reporters report passenger miles; 2015-2021 metrics live in a different table (not used) |
| WCTA home page `https://www.westmorelandtransit.com` | LIVE (WebFetch summary) | 15 fixed routes incl. Pittsburgh "Flyer" routes 1F, 2F, 3F, 14F; "GO Westmoreland" = Senior Shared-Ride, ADA Complementary Paratransit, Persons with Disabilities Transportation, MATP |
| WCTA Senior Shared-Ride page `https://www.westmorelandtransit.com/senior-shared-ride` | LIVE (WebFetch summary) | Eligibility: Westmoreland County residents 65 or older, proof of age; funded by the Pennsylvania State Lottery; "trips can be taken for any purpose" |
| NTD Glossary `transit.dot.gov/ntd/national-transit-database-ntd-glossary` | **HTTP 403 — UNVERIFIED**, not relied on | Definitions of unlinked trip / DR are paraphrased from general knowledge and flagged UNVERIFIED below |

All tables below were recomputed from the eight raw rows (script in the session scratchpad, not in the project).
The v1 raw rows reproduce to the cent: cost per hour = operating expense / revenue hours for all eight rows.

---

### C2 — Fixed Or Flex   ·   tier T4   ·   score 0.0 on the n <= 2 rule (see skills; a reachable thin pair is claimed below)

**Protagonist.** Teodora Quillen, a service planner at Westmoreland County Transit Authority (Greensburg, PA)
(constructed framing, disclosed: the agency, its two services and every NTD figure are real; Teodora, the board
meeting and the added $100,000 are invented for the case; no real WCTA employee is portrayed).
Name check: `Teodora` and `Quillen` occur nowhere under `cases/` (grep, 0 files each); not Priya / Mara / Okafor / Raman.

**Story.** The board has found $100,000 a year in new operating money and will fund either more fixed-route
bus service (the Greensburg-Pittsburgh Flyers and the local routes) or more GO Westmoreland demand-response service
(the shared-ride vans seniors, riders with disabilities and medical-assistance patients book by phone). The newest
NTD year on her desk is report year 2024. The decision cannot be split and the board wants one number, but the
two services do not count the same kind of ride: a fixed-route trip is a seat on a bus that runs whether or not
you board; a demand-response trip is a van sent for one person. Teodora has until the agenda item is called to decide
which kind of ride the first $100,000 should buy.

**Decision date / frozen data (SPEC §5).** Everything the students see is **NTD report year (RY) 2024 and earlier**
(RY2022-RY2024). RY2025 exists in the dataset but is withheld for the Twist. Modeling Assumption M0: "as of: the
board is assumed to hold the RY2024 NTD metrics as the latest year; no later figure is used at the decision stage."
The date the RY2024 rows were first published is **UNVERIFIED** (the dataset reports only its 2026-10-14 update time);
the case says "the latest year on the desk" and does not name a publication date.

**Dilemma.**
You are Teodora Quillen.
Do you:
A.) Spend the $100,000 on more fixed-route bus service OR
B.) Spend the $100,000 on more GO Westmoreland demand-response service

**Primary metric.** Added unlinked passenger trips per year bought by the $100,000, weighted by a rider-value weight:
`score = (average trips per $100k of that mode) x rho x w`, with
`rho` = marginal effectiveness of an added dollar relative to the mode's average dollar (marginal trips per marginal $ divided by average trips per $),
`w` = value weight of one trip of that mode relative to one fixed-route trip (`w_fixed = 1` by definition, `w_DR = w`).
**Base case: rho_F = rho_D = 1 and w = 1** (the plain NTD average-productivity comparison; each is a labeled assumption, see below).

#### Computed with real data (NTD RY2024, `ekg5-frzt`, recomputed from raw rows)

| | A: Fixed route (MB) | B: Demand response (DR) |
|---|---|---|
| Operating expense | $7,617,684 | $6,265,961 |
| Vehicle revenue hours | 43,758 | 71,297 |
| Unlinked passenger trips | 205,556 | 158,133 |
| Cost per revenue hour | $174.09 | $87.89 |
| Trips per revenue hour | 4.698 | 2.218 |
| **Trips per $100k (average)** | **2,698.4** | **2,523.7** |
| Hours $100k buys | 574.4 h/yr (2.2 h per weekday) | 1,137.8 h/yr (4.4 h per weekday) |
| Passenger-miles per $100k | 34,344 | 28,952 |
| Fare revenue per $ of expense | 0.05027 | 0.05037 |

**Margin on the primary metric (base case): A beats B by (2,698.4 - 2,523.7) / 2,698.4 = 6.48 %.** <= 20 %: yes.

**The history students see (RY2022-RY2024), same convention:**

| Report year | Fixed trips / $100k | DR trips / $100k | Winner | Margin | Signed gap D = DR - fixed |
|---|---|---|---|---|---|
| 2022 | 2,340.4 | 2,803.2 | DR | 16.51 % | +462.8 |
| 2023 | 2,600.4 | 2,760.7 | DR | 5.81 % | +160.3 |
| **2024 (decision year)** | **2,698.4** | **2,523.7** | **Fixed** | **6.48 %** | **-174.7** |

Note on R1a's "flips twice": recomputed, the trips-per-dollar winner flips **once** in 2022-2025 (DR in 2022 and 2023; fixed in 2024 and 2025).
Passenger-miles per $100k also flips once, a year earlier (DR 2022; fixed 2023 on). So the winner depends on the year *and* on the metric; that is the point, but the sheet does not claim two flips.

#### The two services are NOT like-for-like (must appear in Background and in the facilitator notes)

* A fixed-route "unlinked passenger trip" is a boarding; a trip that needs a transfer counts twice. A DR trip is one rider picked up and dropped off by a van, door to door. (Paraphrase of NTD usage; the official glossary page returned 403 — **UNVERIFIED wording**, the case cites the NTD dataset field names only.)
* The DR riders are largely people for whom the fixed route is not an alternative: the Senior Shared-Ride program is open to county residents 65 or older (WCTA page), and the GO Westmoreland family also includes ADA complementary paratransit, Persons with Disabilities Transportation and MATP. The agency does not publish how its DR trips split by program in the NTD metrics table, so the split is **not given and not assumed**; the case treats "who the DR rider is" qualitatively, from the program list, and carries the value difference in the weight `w`.
* The agency average hides the mix: a Pittsburgh Flyer commuter and a local-route rider are one number in "fixed". Average length of trip is similar on paper (12.7 passenger-miles per fixed trip, 11.5 per DR trip, RY2024), but small agencies estimate passenger miles; treat as soft (**UNVERIFIED** how WCTA samples it).
* Consequence: "trips per $100k" is a defensible *first* metric but not a verdict. The case makes the student say how many DR trips equal one fixed trip (the weight `w`) and defend that number as a value judgment, not a data point.

#### Labeled inputs (Modeling Assumptions; none is NTD data)

| # | Input | Base | Range students argue over | Status |
|---|---|---|---|---|
| M0 | Decision date | RY2024 latest | n/a | Scenario assumption (frozen) |
| M1 | $100,000 recurring per year, indivisible | $100,000 | n/a | Scenario assumption (invented) |
| M2 | Marginal cost of an added hour = that mode's average cost per hour | $174.09 / $87.89 | marginal cost is usually below average cost (fixed overhead already paid) | Scenario assumption; folded into `rho` |
| M3 | `rho_F` = fixed-route marginal effectiveness (added hours are evenings, weekends, outer branches) | 1.00 | 0.80-1.05 | Scenario assumption |
| M4 | `rho_D` = DR marginal effectiveness (extra van-hours only create trips if there is unmet demand) | 1.00 | 0.3-1.1 | Scenario assumption; NTD has no denial / unmet-demand count |
| M5 | `w` = value weight of a DR trip vs a fixed trip (captive-rider share) | 1.00 | 0.8-1.5 | **Value judgment of the board, not data** |
| M6 | Stake scale: one rider using a service on 260 weekdays with a round trip = 520 trips a year | 520 | n/a | Arithmetic convention |

**People stake (labeled inputs, constructed illustrations).** At the base case the $100,000 buys about
2,698 / 520 = **5.2 weekday round-trip riders' worth of fixed-route trips**, or 2,524 / 520 = **4.9 riders' worth of DR trips**.
Concretely (constructed personas, not WCTA customers): A funds, say, one more evening run that lets a shift worker ride home on the
Flyer instead of finding a car; B funds, say, the extra van-hours that let a 78-year-old Senior Shared-Ride rider get a same-week dialysis-day or
grocery slot. Who goes without is the other group: the fixed-route commuter keeps today's last bus, the DR rider keeps today's booking wait.
The case does not say which loss is worse; the weight `w` is where the student has to.

#### Where each side wins (threshold) — a decision map, not one number

A wins iff `2,698.4 x rho_F > 2,523.7 x rho_D x w`, i.e. iff **`rho_F / (rho_D x w) > 0.9352`**.

* Break-even fixed-route effectiveness (rho_D = 1, w = 1): **rho_F* = 2,523.7 / 2,698.4 = 0.9352** — fixed-route hours may be up to **6.5 % less productive than today's average** and A still ties. Below that B wins. (The assumption on rho: this is the *break-even-productivity* rule; new hours are assumed to produce the same marginal-to-average share as stated, and the case names that share rho.)
* Equivalent in trips per hour: B ties A when each DR van-hour carries **2.372** trips (RY2024 average 2.218, +6.9 %); A ties B when each fixed bus-hour carries **4.393** (average 4.698, -6.5 %).
* Weight form (rho_F = rho_D = 1): B wins once a DR trip counts for more than **w* = 1.069** fixed trips.
* A sample of the map (x = rho_F / rho_D):

| w (value of a DR trip) | A wins if x is above | At x = 1, winner and margin |
|---|---|---|
| 0.8 | 0.748 | A by 25.18 % (outside 20 %; shown to mark the edge of the plausible range) |
| 1.0 | 0.935 | A by 6.48 % |
| 1.2 | 1.122 | B by 10.90 % |
| 1.5 | 1.403 | B by 28.72 % (outside 20 %; edge) |

The balanced zone (|margin| <= 20 %) is roughly `0.8 < w < 1.4` at x = 1: it is the **board's stated weight and the stated marginal-effectiveness ratio**, not the NTD table, that settle the case.
* At w = 1 and rho_D = 1, margin by rho_F: 1.00 -> A 6.48 %; 0.95 -> A 1.55 %; 0.935 -> tie (B by 0.03 %); 0.90 -> B 3.77 %; 0.85 -> B 9.12 %; 0.80 -> B 14.46 %.
* Passenger-miles lens (competing metric, same convention): A by (34,344 - 28,952) / 34,344 = **15.70 %**; B's break-even on this lens is rho_F* = 0.843. Fare recovery is a dead heat (DR higher by 0.21 %). The student must say which metric the board is funding.

**Richer decision shape (answering the cross-cutting requirement).** The decision is a *region*, not one break-even:
three labeled quantities (`rho_F`, `rho_D`, `w`) collapse to one ratio `x* = 0.9352 w`, but they are three different arguments
(how productive added hours are, whether the DR side has unmet demand, how much a rider's alternative matters), and the metric-choice
argument (trips vs passenger-miles vs fare recovery) sits on top. An allocation split (say 60/40) was tested and rejected: with
average-productivity inputs a split is always between the two endpoints, so it adds no decision unless a diminishing-returns curve is
assumed, and that curve would be invented (Hard line §5). It is listed under "Still open" as a possible Appendix extension only.

**Strongest case for A.** Fixed route is the cheaper way to buy a trip at the average (6.48 % in RY2024, and fixed gained every year: 2,340 -> 2,600 -> 2,698), it carries passenger-miles at 15.70 % more per dollar, it serves 205,556 trips against 158,133, and the
signed gap has moved toward fixed every year (+462.8, +160.3, -174.7), so a planner who trusts the direction of travel puts the money where
the trend is going.
**Strongest case for B.** Marginal fixed-route hours are the least productive ones (late evenings, outer branches), so rho_F below 0.935 is
easy to defend, which alone flips the case; DR trips are door-to-door for riders who cannot board a fixed route, so a DR trip may deserve
w > 1.07; and DR won RY2022 and RY2023.

#### Deliverables (what the student must produce) and spine skills they genuinely force

1. **Build-up table** for both options: hours bought (`100,000 / cost per hour`), trips (`hours x trips per hour`), trips per $100k, margin with the stated convention. (Unit rates, percent difference.)
2. **Break-even** for rho_F (set `2,698.4 x rho_F = 2,523.7` and solve) and the break-even trips per hour for each mode; written sentence on what share of today's productivity new fixed-route hours must keep. (One-step equation; percent-of-a-number; "find a whole given the percent and the part" in reverse: 93.5 % of 4.698 = 4.393.)
3. **Rider weight:** state `w`, justify it from the program list (who is eligible for what), compute `w*`, and place the board's choice on the map.
4. **Signed-gap trend (forces the negative-number skills).** Compute D = DR - fixed trips per $100k for 2022, 2023, 2024 (+462.8, +160.3, **-174.7**). Average annual change = (-174.7 - 462.8) / 2 = **-318.8** (a negative divided by a positive). Project RY2025 and RY2026 under that "keeps its pace" assumption: -174.7 + (-318.8) = **-493.5** (add and multiply with a negative: 2 years x -318.8 = -637.5, so RY2026 = **-812.2**). State whether two data points support a trend (they do not prove one).
5. **Metric panel:** one sentence on whether the board should fund trips, passenger-miles or fare recovery, and what `unlinked` hides (transfers).
6. **Recommendation memo (the dilemma):** one of A / B, the `rho_F`, `rho_D`, `w` the choice rests on, and one result that would change it.

**Would close (Spine ids exist: checked in `readmodel/standards_spine.json`):**

| id | kind | n | role |
|---|---|---|---|
| `advanced-numbers-how-to-divide-with-negative-numbers` | how-to | **2** | Deliverable 4 (average annual change of a falling signed gap, -637.5 / 2) and Twist item (-1,094 trips / +1,061 hours) |
| `advanced-numbers-how-to-multiply-with-negative-numbers` | how-to | **2** | Deliverable 4 (2 x -318.8 = -637.5 for the RY2026 projection) and Twist item |
| `advanced-numbers-how-to-find-a-whole-given-the-percent-and-the-part-of-the-whole` | how-to | 4 | Reinforcement: break-even trips per hour (93.5 % of today's 4.698 is 4.393) |
| `measurement-how-to-find-a-missing-amount-in-a-proportion` | how-to | 13 | Reinforcement: hours bought and trips for a given $ |

**Thin-skill honesty.** The earlier sheet could reach nothing at n <= 2. This revision makes two real n = 2 skills
(`how to multiply with negative numbers`, `how to divide with negative numbers`) forced by Deliverable 4: the signed gap D is negative in the decision year, the
average change is negative, and the projection needs a negative times a positive. They are not decorative: delete Deliverable 4 and the trend argument disappears.
Honest limit: they are *forced by one deliverable*, not by the dilemma itself; a student can choose A or B without the trend. The Twist then makes them load-bearing
(the marginal trips-per-hour for fixed route is a negative number). If R1a judges them too thin to count as "genuinely forced", the fallback is a
**reinforcement carve-out** and the note to write is: *"Reinforcement carve-out. No spine skill with n <= 2 is forced by the dilemma itself. The case reinforces
n = 4 (find a whole given the percent and the part) and n = 13 (missing amount in a proportion), and adds the negative-number pair at n = 2 only through the
trend and Twist deliverables."* The `missing data element given the mean` (n = 1) skill was deliberately **not** claimed: the drill-choreography and
agriculture-food sheets in this same wave already claim it.
Score under SPEC §8 (`2 skills x 1.0 x HIGH`) = 2.0 if the pair is accepted; 0.0 if treated as carve-out.

**Tier T4.** Requires stated and defended assumptions (rho_F, rho_D, w), a break-even with a sign, and incomplete data by design
(NTD has no denial counts, no program split, no marginal-cost split).

**Twist (post-decision data, SPEC §7.2; NOT shown at the decision stage).** At about the 15-minute mark, reveal RY2025:

| | Fixed (MB) RY2025 | DR RY2025 |
|---|---|---|
| Operating expense | $8,267,834 | $6,981,124 |
| Revenue hours | 44,819 | 76,918 |
| Unlinked trips | 204,462 | 164,014 |
| Trips per $100k | 2,473.0 | 2,349.4 |

* The winner is still fixed route, but the margin shrinks to **(2,473.0 - 2,349.4) / 2,473.0 = 5.00 %**, and rho_F* rises to 0.950. The "keeps its pace" projection predicted a signed gap of **-493.5** (fixed ahead by 18.3 %); the actual gap is **-123.6** (5.00 %). The trend position is invalidated.
* From RY2024 to RY2025, fixed-route hours grew 1,061 and trips fell 1,094: **-1,094 / 1,061 = -1.03 trips per added hour** (marginal effectiveness about -0.06 of average per dollar, since expense rose $650,150). DR hours grew 5,621 and trips grew 5,881: **+1.05 trips per added hour** (about 0.33 of average per dollar). So neither mode's added hours behaved like the average hour; the "added hours come in at the average" position (A's base case) and "DR has slack that new hours fill" (B's base case) both break. Neither makes the other obviously correct: DR's marginal trips per $ (822) are far above fixed's (-168), yet both numbers are one year, agency-wide, not attributable to any $100,000 decision (hours and trips moved for many reasons, and 2022-2024 were post-COVID recovery years).
* Follow-up question: "What just broke in your model? Were you wrong, or just missing information?"
* Facilitator caution: if students compute RY2022->2023 and RY2023->2024 hour-by-hour increments in the first 15 minutes, they get DR 3.15 then 0.16 trips per added hour (fixed 40.8 then 29.3, mostly recovery). That swing is itself the discussion: two or three increments are not an estimate of rho.

**Facilitator note (SPEC §6).** The DR service includes older riders and people with disabilities, and medical-assistance trips. The case compares service per dollar;
it must not be framed as whose life is worth more. The weight `w` is a value judgment and the facilitator should invite students to defend any value,
including 1.0, and to say who is being asked to go without. Mention that transit cost per trip is not a measure of a rider's worth.

**Data feasibility — HIGH.** One public JSON API, no key, every figure fetched and recomputed. Caveats to disclose in the case: (i) DR and fixed are not like-for-like (above);
(ii) average productivity is not marginal productivity; (iii) small agencies estimate passenger miles and report noisy year-to-year figures (Westmoreland's four years
are internally consistent, cost per hour ties out to the cent); (iv) 2022-2024 are post-COVID recovery years; (v) the RY2022 row names the agency "Westmoreland County , dba: Westmoreland County Transit Authority" — match on `ntd_id = 30044`, not name.

---

## Fixes applied (R1 round 1 -> this sheet)

| Reviewer finding | Fix |
|---|---|
| R1a: DROP C1; recompute NTD for C2 | C1 removed; C2 recomputed from eight raw rows: 2022 DR 2,803.2 vs fixed 2,340.4; 2023 2,760.7 vs 2,600.4; 2024 fixed 2,698.4 vs DR 2,523.7; 2025 fixed 2,473.0 vs DR 2,349.4 (all trips per $100k, confirmed). |
| R1a: "winner flips twice" | Recomputed: once for trips per $100k (between 2023 and 2024), once for passenger-miles per $ (between 2022 and 2023). Stated honestly; no "twice" claim. |
| R1a: state DR vs fixed are not like-for-like | Dedicated section; the difference is carried by the weight `w`, with program eligibility from the WCTA pages; official NTD glossary 403 and flagged UNVERIFIED. |
| R1a: state rho* / break-even-productivity assumption | M3 and the threshold block: rho_F* = 0.9352 at rho_D = 1 and w = 1; marginal cost = average cost (M2) folded into rho. |
| R1a: thin n <= 2 skill | Two n = 2 negative-number skills are forced by Deliverable 4; fallback reinforcement note written. `missing data element` (n = 1) deliberately not claimed (collides with drill and agriculture sheets). |
| R1c: people / rider stake | Labeled constructed stake: 5.2 vs 4.9 riders' worth of trips, personas for who gains and who goes without, weight `w` as an explicit value judgment, facilitator note. |
| Cross-cutting: decision date frozen | M0: RY2024 is the decision year; RY2025 and the marginal analysis are Twist only; history RY2022-RY2023 is Background. |
| Cross-cutting: margin convention | Gap / winner everywhere (v1's 5.26 % becomes 5.00 %); one margin per option set: 6.48 %. |
| Cross-cutting: richer decision shape | Region on (rho_F / rho_D, w) plus a metric-choice panel (trips vs passenger-miles vs fare recovery); split allocation tested and rejected as dominated without invented curves. |
| Cross-cutting: protagonist name | Teodora Quillen; neither word found in `cases/`. |
| Cross-cutting: endings | The story ends on the agenda item being called; no buzzing phone. |
| Cross-cutting: as-of dates / facilitator notes | M0 and data log; SPEC §6 note included. |
| Spine ids | All four ids confirmed present in `readmodel/standards_spine.json` (negative multiply n = 2, divide n = 2, find-a-whole n = 4, missing-amount proportion n = 13). |

## Still open / UNVERIFIED

1. **UNVERIFIED:** NTD glossary definition of "unlinked passenger trip" and "demand response" (page returned 403); the case should quote the NTD data-table field names only until a copy is fetched.
2. **UNVERIFIED:** the date RY2024 rows were first published on data.transportation.gov (only the dataset's 2026-10-14 update time is known). The case avoids naming a publication date.
3. **UNVERIFIED:** how Westmoreland estimates passenger miles (NTD allows sampling); the passenger-miles lens is soft.
4. **UNVERIFIED:** WCTA program shares of DR trips (senior / ADA / disability / MATP); not in the NTD table. Not assumed.
5. Fare structure and the Senior Free Transit Program terms were not retrievable from the WCTA home page; not used.
6. Whether R1a accepts the negative-number pair as "genuinely forced" (otherwise carve-out note above applies; tier and score move to 0.0).
7. The pre-2022 NTD years (2015-2021 Metrics table) were not fetched; adding RY2019 would give a pre-COVID baseline and could change the story of the flip (a possible v3 extension, not needed for balance).
8. Optional Appendix extension: a split allocation with a diminishing-returns curve for fixed route; omitted because the curve would be invented.
9. Facilitator risk: students who compute year-over-year hour/trip increments early pre-empt part of the Twist (note under Twist).

Reproduction: `ekg5-frzt` rows for `ntd_id = 30044`; trips per $100k = `unlinked_passenger_trips / total_operating_expenses x 100,000`; hours bought = `100,000 / (total_operating_expenses / vehicle_revenue_hours)`; margin = (winner - loser) / winner.
