# Case Study: The Hub Choice

MS | Math | Case Study | 2026 | Adventure

---

## Overview

Marcus Feld has one line left on the spreadsheet, and finance needs it filled by Friday.

He's been staring at the same regional route map for three days — six little airport dots scattered across upstate New York, a handful of thin lines connecting some of them, and a lot of open space between the rest. The budget memo on his second monitor says it plainly: one new route this fiscal year. Not two. The board already trimmed his ask once.

Two sticky notes are stuck to the side of his monitor, one pink, one yellow. The pink one says *BGM ↔ ART — direct*. The yellow one says *ART ↔ Cortland — new*. He's rewritten each of them twice.

His ops director stops by his desk on her way to the parking garage, coat already on. "Whichever one you pick," she says, "you're presenting it Monday. Both of them poll fine with the crew. Just don't make me explain a route nobody flies." She doesn't wait for an answer.

Marcus pulls both folders out from under his keyboard — one thick with call-volume printouts from the airports that already have his airline's planes on the ramp, one thin, with a county population report and a hand-drawn line on a road atlas. He sets them side by side. The cursor blinks in the empty subject line of the Monday deck.

---

## Background

Marcus Feld is the network planning manager at Finger Lakes Regional Air, a small regional carrier operating a fleet of one aircraft type out of a network of airports across the Finger Lakes and North Country regions of New York. He is accountable to the airline's board for how the year's single approved route-expansion budget is spent, and for defending that choice in front of the operations committee (SEE APPENDIX F).

The airline's current network serves 6 small regional airports, each connected to at least one other by an existing scheduled route, so that every airport in the network can reach every other one by some combination of flights (SEE APPENDIX A). Before costing anything, Marcus's team first has to know how many *possible* nonstop city-pairs a network of 6 airports could ever support — a number that turns out to be far larger than the 5 routes the airline actually flies today, and it is that gap that explains why only one new route gets funded this year, not all of them (SEE APPENDIX A).

Marcus is choosing between exactly two already-scoped route proposals, both flyable with the airline's existing aircraft type and both costed by finance (SEE APPENDIX E):

**Route A — The Hub Link:** a new direct flight between two of the airline's already-served regional hub airports, Greater Binghamton Airport (BGM) and Watertown International Airport (ART). Today, a traveler moving between these two airports has no direct flight — the only way to fly between them uses the airline's existing network, connecting through two intermediate stops (SEE APPENDIX A), which turns out to take far longer than simply driving. In practice, nearly everyone who makes this trip today drives instead (SEE APPENDIX B, APPENDIX C). Both airports already have Marcus's planes, gate space, and ground crew on-site — the route adds a new edge between two points his airline already touches.

**Route B — The New City Link:** a new direct flight connecting the ART hub to a small city currently outside the airline's network entirely — Cortland, NY, home to Cortland County Airport, which today has no scheduled commercial air service of any kind (SEE APPENDIX B, APPENDIX D). This route adds a new vertex to the network, not just a new edge between two existing ones. Today, anyone traveling between the ART hub area and Cortland drives the entire way.

Both routes use the same aircraft type at the same published operating cost per flight hour (SEE APPENDIX E), so the deciding factor is not which route is cheaper to fly — it's which route returns more travel-time saved for the region, per dollar the airline commits to flying it. That number depends on how many people would actually use each new route and how much time each one saves them over driving, the realistic alternative both routes compete against today (SEE APPENDIX B, C, D).

The vocabulary and "how to…" skills this case will ask you to research are listed in **APPENDIX G** — that is where Challenge 1 sends you. Every figure in this case is either cited to a real public source or stated as a modeling assumption, in **APPENDIX H**.

The Monday deck is due in four days.

---

## Dilemma

You are Marcus Feld.

Do you:

**A.)** Fund Route A — a new direct flight between two already-served hub airports, Greater Binghamton (BGM) and Watertown International (ART) **OR**

**B.)** Fund Route B — a new direct flight connecting the ART hub to Cortland, NY, a city with no current scheduled commercial air service

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A network map and city-pair count: list every airport in Finger Lakes Regional Air's current network as a labeled vertex, connect the 5 routes it actually flies as labeled edges, then use the binomial coefficient to compute the total number of unique city-pairs (possible nonstop routes) that 6-airport network could ever support, and compare that count to the 5 routes it actually operates (Appendix A).
    D2. A route-time comparison table: for Route A, the total time (flight legs plus stops) of the fastest path through the airline's EXISTING weighted route network from BGM to ART, compared with straight-line driving and with the proposed new direct flight; for Route B, driving time compared with the proposed new direct flight (Appendix A, B, C, D).
    D3. A weekly time-saved calculation for each route: estimated weekly travelers on that route multiplied by the minutes each one saves flying direct compared to driving (today's realistic alternative for both), giving total weekly person-minutes saved (Appendix C, D).
    D4. A cost-per-benefit table: each route's annual operating cost (Appendix E) divided into its annual person-minutes saved (from D3, annualized), giving minutes of travel time saved per dollar of route cost for A and for B.
    D5. A one-page recommendation memo that opens by citing your D1 city-pair count to explain why the airline cannot simply fund every possible route, then states your recommendation using your D4 figures.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

### Appendix A — Finger Lakes Regional Air's Current Network

The airline's current network of regional airports (vertices) and the routes it already flies among them (edges), with each edge's one-way flight time.

| Airport | Code |
|---|---|
| Ithaca Tompkins International | ITH |
| Elmira Corning Regional | ELM |
| Greater Binghamton | BGM |
| Watertown International | ART |
| Massena International | MSS |
| Ogdensburg International | OGS |

| Existing route (edge) | One-way distance (mi) | One-way flight time (air only, min) |
|---|---|---|
| ITH ↔ ELM | 31.8 | 9.0 |
| ELM ↔ BGM | 46.8 | 13.2 |
| BGM ↔ MSS | 196.8 | 55.5 |
| MSS ↔ OGS | 35.1 | 9.9 |
| OGS ↔ ART | 55.0 | 15.5 |

**Airports in the network (n):** 6
**Routes the airline actually flies today (edges shown above):** 5

The network is connected — every airport can reach every other by some sequence of existing flights — but the 5 routes shown above are only some of the nonstop city-pairs a 6-airport network could support. Most pairs, including BGM↔ART, have no direct flight and must either connect through the existing network or use another mode of travel (SEE APPENDIX C). D1 asks you to compute exactly how many total city-pairs a 6-airport network could ever support, using the binomial coefficient — that count is not given here.

### Appendix B — Airport and City Locations

Published coordinates for each airport/city in this case, used to compute the great-circle distances above and in Appendices C and D.

| Location | Code | Latitude | Longitude |
|---|---|---|---|
| Greater Binghamton Airport | BGM | 42.20861° N | 75.97972° W |
| Watertown International Airport | ART | 43.99194° N | 76.02056° W |
| Cortland County Airport | N03 | 42.59250° N | 76.21472° W |
| Ithaca Tompkins International | ITH | 42.49139° N | 76.45861° W |
| Elmira Corning Regional | ELM | 42.16000° N | 76.89167° W |
| Massena International | MSS | 44.93583° N | 74.84556° W |
| Ogdensburg International | OGS | 44.68194° N | 75.46556° W |

| Route | Great-circle distance (statute miles, derived from coordinates above) [S1]–[S7] |
|---|---|
| BGM ↔ ART (Route A) | 123.2 |
| ART ↔ Cortland (Route B) | 97.2 |

### Appendix C — Route A: Today's Alternatives vs. the New Direct Flight

| | Value |
|---|---|
| Driving time, BGM to ART (today's realistic alternative) [S8] | 135 min (2 h 15 min) |
| Flying via the EXISTING network (BGM→MSS→OGS→ART, 2 connections) — air time only | 80.9 min, plus ground time at 2 extra stops (see Appendix F, MA1) — over 4 hours door-to-door, which is why almost no one flies this way today |
| Cruise speed of Finger Lakes Regional Air's aircraft type (Cessna Grand Caravan EX) [S9] | 185 knots true airspeed ≈ 212.9 mph |
| New Route A direct flight time = 123.2 mi ÷ 212.9 mph + ground-time overhead (Appendix F, MA1) | 34.7 min air time + 45 min ground overhead = 79.7 min |
| Time saved per traveler vs. driving (135 − 79.7) | 55.3 min |
| Estimated weekly travelers who would use a new BGM↔ART nonstop (Appendix F, MA2) | 25 |

### Appendix D — Route B: Today's Alternative vs. the New Direct Flight

| | Value |
|---|---|
| Driving time, ART to Cortland (today's only option — no commercial air service exists) [S8] | 110 min (1 h 50 min) |
| New Route B direct flight time = 97.2 mi ÷ 212.9 mph + ground-time overhead (Appendix F, MA1) | 27.4 min air time + 45 min ground overhead = 72.4 min |
| Time saved per traveler vs. driving (110 − 72.4) | 37.6 min |
| Cortland County, NY population (2024) [S10] | 46,246 |
| Estimated weekly travelers who would use a new ART↔Cortland nonstop (Appendix F, MA2) | 25 |

### Appendix E — Route Operating Costs

| | Value |
|---|---|
| Aircraft type flown on both routes | Cessna Grand Caravan EX (single-engine turboprop, standard 9-passenger configuration) [S9][S11] |
| Published operating cost per flight hour, this aircraft type (450 annual hours, $9/gal fuel basis) [S12] | $1,601 |
| Scheduled flights per week, each route (Appendix F, MA3) | 6 (3 round trips) |
| Annual block hours flown, Route A = (34.7 min ÷ 60) × 6 flights/week × 52 weeks | 180.6 hours |
| Annual block hours flown, Route B = (27.4 min ÷ 60) × 6 flights/week × 52 weeks | 142.4 hours |
| Annual operating cost, Route A = 180.6 hr × $1,601/hr | $289,145 |
| Annual operating cost, Route B = 142.4 hr × $1,601/hr | $228,024 |

### Appendix F — Modeling Assumptions

> These figures are **not sourced from a real record of this fictional airline**. They are stated
> scenario assumptions chosen by the case author, or real public data applied by analogy to this
> fictional network. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis |
|---|---|---|---|
| MA1 | Ground-time overhead added to every flight leg's air time (boarding, taxi, deplaning at a small regional airport with no dedicated jet-bridge or long security line) | 45 minutes, applied identically to Route A and Route B | No public per-flight ground-time figure exists for this fictional airline's specific small airports. 45 minutes is a stated scenario value chosen within the range commonly recommended for arrival ahead of a small regional/commuter departure. The answer is sensitive to this value — recompute D2–D4 with it at roughly half and roughly 1.5× this value and compare (see `sensitivity_model.py`). |
| MA2 | Estimated weekly travelers on a brand-new route, applied identically to Route A and Route B | 25 travelers/week each | No booking history exists for either fictional route. Rather than guess two different numbers, the case applies the SAME weekly-ridership scenario value to both proposals, since nothing in the sourced data (Appendix B–D) distinguishes how many people would actually show up — only how much time each rider would save and what it costs to fly them. Loosely anchored below Watertown International's real ~22,000 annual (≈423/week, all-destination) 2023 enplanement total [S13], since a single new route would only ever capture a modest slice of a hub's total traffic. This is a genuinely debatable modeling choice — a Hero may argue the two routes deserve different ridership estimates, and defending or challenging that choice is itself part of the pitch. (No formula converts population or enplanements into a ridership number — 25/week is a stated scenario value, not a computed one; the population and enplanement figures are given only as rough plausibility checks on that value, not as its derivation.) |
| MA3 | Scheduled flights per week, each route | 6 (3 round trips/week) | A stated scenario frequency, consistent with how many real small Essential Air Service routes to comparably sized New York communities operate on a several-times-weekly schedule rather than daily [S14]. Not swept in the robustness check — a fixed scheduling choice, not a research uncertainty. |

### Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Vertex
- Edge
- Graph (Vertices And Edges)
- Weighted Graph
- Binomial Coefficient
- Fundamental Counting Principle

**"How to…" questions**

- How to find the shortest path between two vertices in a weighted graph
- How to compute a binomial coefficient

### Appendix H — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Greater Binghamton Airport (BGM) coordinates | 42.20861° N, 75.97972° W | Wikipedia — "Greater Binghamton Airport" ([link](https://en.wikipedia.org/wiki/Greater_Binghamton_Airport)) | accessed 2026-09-18 | HIGH |
| S2 | Watertown International Airport (ART) coordinates | 43.99194° N, 76.02056° W | Wikipedia — "Watertown International Airport" ([link](https://en.wikipedia.org/wiki/Watertown_International_Airport)) | accessed 2026-09-18 | HIGH |
| S3 | Cortland County Airport (N03) coordinates | 42.59250° N, 76.21472° W | Wikipedia — "Cortland County Airport" ([link](https://en.wikipedia.org/wiki/Cortland_County_Airport)) | accessed 2026-09-18 | HIGH |
| S4 | Ithaca Tompkins International Airport (ITH) coordinates | 42.49139° N, 76.45861° W | Wikipedia — "Ithaca Tompkins International Airport" ([link](https://en.wikipedia.org/wiki/Ithaca_Tompkins_International_Airport)) | accessed 2026-09-18 | HIGH |
| S5 | Elmira Corning Regional Airport (ELM) coordinates | 42.16000° N, 76.89167° W | Wikipedia — "Elmira Corning Regional Airport" ([link](https://en.wikipedia.org/wiki/Elmira_Corning_Regional_Airport)) | accessed 2026-09-18 | HIGH |
| S6 | Massena International Airport (MSS) coordinates | 44.93583° N, 74.84556° W | Wikipedia — "Massena International Airport" ([link](https://en.wikipedia.org/wiki/Massena_International_Airport)) | accessed 2026-09-18 | HIGH |
| S7 | Ogdensburg International Airport (OGS) coordinates | 44.68194° N, 75.46556° W | Wikipedia — "Ogdensburg International Airport" ([link](https://en.wikipedia.org/wiki/Ogdensburg_International_Airport)) | accessed 2026-09-18 | HIGH |
| S8 | Driving times, BGM↔ART and ART↔Cortland | 135 min (145 mi); 110 min (103.5 mi) | Travelmath driving time/distance calculators ([BGM↔ART](https://www.travelmath.com/driving-time/from/Binghamton,+NY/to/Watertown,+NY), [ART↔Cortland](https://www.travelmath.com/driving-time/from/Watertown,+NY/to/Cortland,+NY)) | accessed 2026-09-18 | MEDIUM (aggregator site, not a primary mapping API; times corroborated within a few minutes across multiple search results) |
| S9 | Cessna Grand Caravan EX maximum cruise speed | 185 knots true airspeed (≈213 mph) | Textron Aviation — "Grand Caravan EX Turboprop" official specifications page ([link](https://cessna.txtav.com/en/turboprop/grand-caravan-ex)) | accessed 2026-09-18 | HIGH (manufacturer primary source) |
| S10 | Cortland County, NY population | 46,246 (2024, ACS 5-year estimate) | U.S. Census Bureau QuickFacts — "Cortland County, New York" ([link](https://www.census.gov/quickfacts/fact/table/cortlandcountynewyork/PST045224)) | accessed 2026-09-18 | HIGH |
| S11 | Cessna Grand Caravan EX standard passenger configuration | 9 passengers | AeroCorner — "Cessna Grand Caravan EX" ([link](https://aerocorner.com/aircraft/cessna-grand-caravan-ex/)) | accessed 2026-09-18 | MEDIUM (aviation enthusiast/industry reference site, not the manufacturer directly) |
| S12 | Cessna Caravan 208B Grand EX operating cost per flight hour | $1,601/hour (450 annual owner-operated hours, $9/gal fuel basis) | Aircraft Cost Calculator — "Cessna Caravan 208B Grand EX" ([link](https://www.aircraftcostcalculator.com/AircraftOperatingCosts/501/Cessna+Caravan+208B+Grand+EX)) | accessed 2026-09-18 | MEDIUM (industry cost-estimation tool; figure obtained via search result summary of the page, not a direct fetch, because the page blocked direct retrieval — figure is internally consistent with the same tool's non-EX Caravan estimate of $1,536/hr under identical assumptions) |
| S13 | Watertown International Airport (ART) 2023 annual enplanements | more than 22,000 | NY.gov Regional Economic Development Councils — "Governor Hochul Announces Major Construction Underway to Enhance Passenger Experience at North Country Airports" ([link](https://regionalcouncils.ny.gov/press-release/governor-hochul-announces-major-construction-underway-enhance-passenger-experience)) | accessed 2026-09-18 | MEDIUM (government press release, not the FAA's own enplanement table directly) |
| S14 | Essential Air Service eligibility threshold and typical small-community route frequency | Communities must average ≥10 enplanements/service day (≈3,650/year) to remain EAS-eligible unless >175 driving miles from a hub | U.S. GAO — "Commercial Aviation: Trends in Air Service to Small Communities," GAO-24-106681 ([link](https://www.gao.gov/products/gao-24-106681)) | accessed 2026-09-18 | HIGH (federal audit report) |

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
