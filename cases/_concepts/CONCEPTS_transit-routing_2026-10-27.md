# Concept sheet — Transit, Routing & Last-Mile Logistics — 2026-10-27

Target domain: `readmodel/domains.json` -> `transit-routing` (cluster "Movement & Logistics",
authoring_priority HIGH, `n_uncovered_signature_skills` 0). Spine sweep: no skill sits at
`n == 0` any more, so each concept is scored on the reinforcement carve-out basis (SPEC §8
exception, same basis as `CONCEPTS_aviation_2026-09-18.md`). "Closes" below means: the
thinnest reachable spine skills (n <= 2 where honestly reachable), with n stated. Thin groups
reachable from this domain: **Fractions / Division Of Fractions** (n = 1-2 across the group),
**Geometry / Triangles** (Triangle Inequality Theorem n = 2), **Statistics / Probability**
(permutation family n = 2, not used here).

Avoided premises (checked in `readmodel/cases_index.json` and `cases/_concepts/`): the-breakeven-mile
(car vs rideshare linear breakeven), the-hub-choice (airline route graph), the-fee-route
(settlement graph), the-missing-hub (friend-circle degree stats), the-one-pass-route (street
sweeper deadhead), reroute-wait (Line 20 bridge closure: detour vs transfer), the-trailer-return,
navigation, travel-planner; and the dropped concept recorded in `CONCEPTS_disaster-response_2026-10-04.md`
(NYC M15 local vs SBS stop spacing — dominated beyond 1.5 km).

| # | Title | score | tier | feasibility | computed margin |
|---|---|---|---|---|---|
| C1 | **The Spare Bus** | 2.0 | T3 | HIGH | 10.7 % (Route 21 over 39) |
| C2 | **Fixed Or Flex** | 0.0 (carve-out; ranked on data + ambiguity) | T4 | HIGH | 5.3 % (fixed route over demand-response) |
| C3 | **The Walk-Up Stop** | 0.6 | T2 | HIGH | 2.0 % (stop at the door vs stop on the corridor) |

**Recommendation: write C1 — The Spare Bus.** It is the only concept that closes n = 2 skills with
how-to weight (both Division-Of-Fractions how-tos), the real feeds confirm the fleet-size identity
it teaches (buses = cycle / headway; observed concurrent buses 6.1 and 2.9 vs formula 6.2 and 3.0), and its
metric flips on a stated, defensible assumption. C2 is the strongest ambiguity case (the winner changed
twice in four real years) and is the pick if the pipeline wants a T4. C3 is the lightest, a good T2 backfill.

## Method and data log (everything below was fetched and recomputed in code on 2026-10-27)

| Source | Fetched | What it gave |
|---|---|---|
| MBTA GTFS static `https://cdn.mbta.com/MBTA_GTFS.zip` | LIVE, HTTP 200, 22.1 MB, `feed_info`: "Fall 2026 ... version D", valid 2026-10-20 to 2026-12-12 | `trips`, `stop_times`, `blocks`, `stops` for Tue 2026-10-27 (13,050 bus trips) |
| MBTA Bus Ridership by Trip, Season, Route, Line, and Stop (ArcGIS Hub item `8daf4a33925a4df59183f860826d29ee`, `.../sharing/rest/content/items/<id>/data`) | LIVE, 73 MB zip, read `..._Fall_2025.csv` | Fall 2025 weekday boardings per route (sum of `Boardings` where Day Type = Wkdy) |
| Boston Region MPO feature service `cmp_network_2024_transit_mbta_bus_fall_2023_ridership` (ArcGIS FeatureServer layer 0) | LIVE, 653 route-pattern rows | Fall 2023 `boardings_weekday`, used as a cross-check |
| NTD Annual Data - Metrics 2022-2025, Socrata `data.transportation.gov/resource/ekg5-frzt.json` | LIVE (JSON API, no key) | opex, unlinked trips, revenue hours, passenger miles by agency / mode / year |
| OpenStreetMap Overpass API (`overpass-api.de/api/interpreter`) | LIVE | coordinates of public parks, libraries, community centres |
| gtfs.org, transit.land (homepages) | HTTP 200 (homepage only; no Transitland feed API was exercised) | spec / feed directory references |
| Citi Bike GBFS `gbfs.citibikenyc.com/gbfs/en/station_information.json` | LIVE (2,521 stations) | fetched, not used in a concept |
| bts.gov | HTTP 403 to curl | **UNVERIFIED** — not used |

---

### C1 — The Spare Bus   ·   score 2.0   ·   tier T3

**Protagonist.** Mateo Alvarez, a service planner at the MBTA (constructed framing, disclosed: the
agency, routes, schedules and ridership are real; the character and the "one spare bus" are invented
for the case). 

**Story.** A garage ends the fall pick with exactly one spare bus and the planner may add it to one route
before winter. Which route should get it?

**Dilemma.**
You are Mateo Alvarez.
Do you:
A.) Add the spare bus to Route 39 (Forest Hills - Back Bay, the busy "Frequent Bus" corridor) OR
B.) Add the spare bus to Route 21 (Ashmont - Forest Hills, the thin local with 20-minute headways)

**Primary metric.** Rider-minutes of average waiting time saved per weekday from the added bus
(ratio-style, one bus on each side): `weekday boardings x (H_old - H_new) / 2`, where headway
`H = cycle time / buses` (random-arrival wait is half the headway; the assumption is stated).

**Computed with real data (recomputed in code).**

| | Route 39 | Route 21 |
|---|---|---|
| Round-trip cycle (median, GTFS, 10:00-14:00 blocks) | 87 min | 59 min |
| Observed midday headway (trips 10:00-14:00 / 4 h) | 14.1 min | 20.0 min |
| cycle / headway (fleet identity) | 6.16 buses | 2.95 buses |
| Buses used (rounded; bus-block concurrency check) | 6 (observed 6.1) | 3 (observed 2.9) |
| Headway cycle / N -> cycle / (N+1) | 14.50 -> 12.43 min | 19.67 -> 14.75 min |
| Fall 2025 weekday boardings | 8,840 | 4,169 |
| **Rider-minutes saved / weekday** | **9,156** | **10,248** |

Margin: B beats A by **10.66 %** (Fall 2025). With the Fall 2023 ridership cross-check the margin is
**4.58 %** (9,552 vs 10,010). So neither option dominates — the answer is a close call and moves with the ridership vintage.

**Where each side wins (threshold).** A (Route 39) wins if fewer than **89.3 %** of Route 21's riders
arrive at random — i.e. if more than ~11 % of its riders already time their trips to the schedule (very
plausible at a 20-minute headway; the half-the-headway rule is only strong for frequent service). Equivalent
ridership thresholds: Route 21 would need to carry fewer than **3,724** weekday boardings (it carries 4,169),
or Route 39 more than **9,895** (it carries 8,840). B wins under the plain textbook assumption; A wins under
the schedule-aware assumption. Margin at base <= 20 %: yes (10.7 %).

**Strongest case for A.** The bus lands where the crowd is: 8,840 riders, each of whom gets a 2-minute
shorter headway; if even a modest share of Route 21's riders plan around the timetable, A is the better buy.
**Strongest case for B.** Dropping a 20-minute headway to 15 saves ~5 minutes of headway per wait; rider-minutes
saved still exceed Route 39's by ~1,100 per weekday under the standard assumption.

**Would close (n shown; both how-to):**

| id | kind | n | label |
|---|---|---|---|
| fractions-how-to-divide-a-whole-number-by-a-fraction | how-to | 2 | How to divide a whole number by a fraction (cycle 1.45 h / headway 1/4 h -> buses) |
| fractions-how-to-divide-a-fraction-by-a-whole-number | how-to | 2 | How to divide a fraction by a whole number (cycle in hours / N buses -> headway) |

Supporting (already thick, not counted): `measurement-how-to-convert-between-units-of-time`,
`measurement-how-to-find-elapsed-time`, `number-sense-how-to-compare-two-or-more-values`.
Score = (2 x 1.0) x 1.0 (HIGH) = 2.0. No group bonus (Division Of Fractions has more thin skills left).

**Data feasibility — HIGH.** GTFS zip (public, no key), ridership CSV and feature service (public), all fetched
and parsed. Students open `trips.txt` / `stop_times.txt` in a spreadsheet. Caveats to disclose: the GTFS is
Fall 2026, ridership Fall 2025 (vintage gap, shown as a sensitivity); cycle time from block data includes
layover; the metric assumes midday headway holds all day and random-arrival waiting.

---

### C2 — Fixed Or Flex   ·   score 0.0 (carve-out)   ·   tier T4

**Protagonist.** Dana Whitfield, a service planner at Westmoreland County Transit Authority (PA)
(constructed framing, disclosed; the agency and NTD numbers are real, the character and the added
$100,000 are invented).

**Story.** The board approves $100,000 in new operating money. The authority runs both a fixed-route bus
and a county demand-response (shared-ride) service, and each year the NTD reports cost per trip for both.
Which service gets the money?

**Dilemma.**
You are Dana Whitfield.
Do you:
A.) Spend the $100,000 on more fixed-route bus hours OR
B.) Spend the $100,000 on more demand-response (dial-a-ride) hours

**Primary metric.** Added unlinked passenger trips per $100,000 of added service hours
(`hours = $ / cost-per-hour`, `trips = hours x passengers-per-hour`).

**Computed with real data (NTD 2022-2025, `ekg5-frzt`, recomputed from raw opex / trips / hours).**

| Year | Fixed route trips per $100k | Demand response trips per $100k | Winner | Margin |
|---|---|---|---|---|
| 2022 | 2,340.4 | 2,803.2 | DR | 19.77 % |
| 2023 | 2,600.4 | 2,760.7 | DR | 6.17 % |
| 2024 | 2,698.4 | 2,523.7 | Fixed | 6.92 % |
| **2025** | **2,473.0** | **2,349.4** | **Fixed** | **5.26 %** |

2025 build-up: fixed route $8,267,834 / 44,819 h = $184.47/h at 4.562 trips/h -> 542.1 h -> 2,473 trips;
DR $6,981,124 / 76,918 h = $90.76/h at 2.132 trips/h -> 1,101.8 h -> 2,349 trips.

**Where each side wins (threshold).** The winner **flipped twice in four real years**. At 2025 prices
A wins only if new fixed-route hours carry at least **95.0 %** of today's average productivity (rho* = 0.950;
new hours are rarely as productive as the average, so B is the live challenger); equivalently DR would need
2.244 trips/h (it is 2.132) to tie. Cost per passenger-mile points the other way in 2022 (fixed $3.54 vs DR
$2.99) and agrees with fixed in 2025 ($3.33 vs $3.80): picking the metric is part of the argument. Margin
<= 20 % in every year.

**Strongest case for A.** Fixed route is cheaper per trip in the two most recent years, serves ~204,000 trips
a year, and wins on passenger-miles by 14 % in 2025.
**Strongest case for B.** Marginal fixed-route hours are the least productive ones (evenings, outer
branches), DR productivity fell in 2024 and 2025 (2.33 -> 2.22 -> 2.13 trips/h) so there may be slack to refill, and DR won 2022 and 2023.

**Would close (reinforcement — nothing reachable at n <= 2):**

| id | kind | n | label |
|---|---|---|---|
| advanced-numbers-how-to-find-a-whole-given-the-percent-and-the-part-of-the-whole | how-to | 4 | How to find a whole given the percent and the part (rho* style: 95 % of average) |
| advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-both-sides | how-to | 3 | How to solve a multi-step equation with a variable on both sides (set trips-per-dollar equal, solve for the unknown productivity) |

Honesty note: the second skill is only reached if the case is written with productivity unknown on both
sides of the equality; a plain solve-for-rho is a one-step equation. Score 0.0 under the n <= 2 rule.

**Data feasibility — HIGH.** NTD Socrata JSON API, public, no key, fetched and recomputed; four annual rows per mode.
Caveats to disclose: DR in PA is largely shared-ride for seniors / persons with disabilities, so the trips are
not like-for-like; "added hours at average productivity" is an assumption (T4 requirement: stated and defended);
NTD reporting quality varies by agency (small agencies swing wildly year to year — Westmoreland was chosen
because its four years are stable and internally consistent: cost/hr ties out to opex / revenue hours to the cent).

---

### C3 — The Walk-Up Stop   ·   score 0.6   ·   tier T2

**Protagonist.** Jordan, a student who finishes at the Tobin Community Center in Mission Hill, Boston
every afternoon (constructed framing, disclosed; the building, stops and timetables are real, Jordan is invented
and no real person is portrayed).

**Story.** Two real stops can get Jordan to Nubian Station. One is 73 m from the door with a single route.
The other is 474 m away with seven routes and a bus almost every two minutes.

**Dilemma.**
You are Jordan.
Do you:
A.) Walk to the nearest stop, Tremont St @ Sewall St (Route 66 only) OR
B.) Walk to the corridor stop, Malcolm X Blvd @ King St (Routes 15, 19, 23, 28, 44, 45, 66)

**Primary metric.** Expected door-to-door minutes to Nubian Station, averaged over weekday departure hours
7:00-20:00: `walk + average wait (random arrival, next scheduled trip) + scheduled in-vehicle minutes`.
Walk = straight-line distance x 1.3 street-detour factor / 80 m per min (both disclosed assumptions).

**Computed with real data (GTFS Tue 2026-10-27; origin coordinates from OSM way 29871661).**

| | A: Tremont @ Sewall | B: Malcolm X @ King |
|---|---|---|
| Straight-line distance from door | 73 m | 474 m |
| Walk at 1.3 / 80 m/min | 1.2 min | 7.7 min |
| Weekday departures per hour (typical) | 6 | 25-34 |
| Average wait / in-vehicle | ~4.4 / ~9.7 min | ~1.2 / ~6.5 min |
| **Average door-to-door** | **15.06 min** | **15.36 min** |

Margin: A is **2.0 %** faster. Neither dominates: A wins 8 of the 13 hourly windows, B wins 5.
No third stop within 1 km dominates both (checked all stops with service to Nubian).

**Where each side wins (threshold).** The decision flips at a walking speed of **83.9 m/min = 5.03 km/h**
(a brisk adult pace): slower walkers should take A, faster walkers B. Sensitivity (recomputed): detour 1.0 at
80 m/min -> B wins by 8.9 %; 1.3 at 60 m/min -> A wins by 16.0 %; 1.5 at 80 m/min -> A wins by 8.6 %;
1.3 at 100 m/min -> B wins by 7.3 %. Riders who check the schedule (wait removed) favour A:
25 % schedule-aware -> A 13.99 vs B 15.05 min. Margin at base <= 20 %: yes (2.0 %).

**Strongest case for A.** Almost no walking, and a rider who knows the Route 66 times loses almost nothing.
**Strongest case for B.** With a bus every two minutes and a 3-minute-shorter ride, B wins as soon as the
rider walks briskly or ignores the timetable.

**Would close (counted n <= 2 only; second skill noted):**

| id | kind | n | label |
|---|---|---|---|
| geometry-triangle-inequality-theorem | term | 2 | Triangle Inequality Theorem (the L-shaped walk vs the straight line justifies the detour factor) |
| geometry-how-to-find-the-distance-between-two-coordinate-pairs-on-a-coordinate-plane | how-to | 4 | How to find the distance between two coordinate pairs (stop and door coordinates) — reinforcement |

Score = 0.6 x 1.0 = 0.6.

**Data feasibility — HIGH.** GTFS zip as above, plus OSM Overpass for the building coordinates (both fetched).
Caveats to disclose: scheduled, not real-time, times; detour factor and walking speed are assumptions the Hero
must state; Route 66 stop times are for trips that reach Nubian.

---

Reproduction notes: GTFS service on Tue 2026-10-27 selected from `calendar.txt` / `calendar_dates.txt`; bus
`route_type == 3`; cycle = start-to-start of the second trip in the same block on the same route, 10:00-14:00,
median; N = round(cycle / headway). C2 and C3 numbers computed directly from NTD rows and `stop_times.txt`
as described above. All scripts and raw pulls are in the session scratchpad, not in the project.
