Case Study: The One-Pass Route
MS | Math | Case Study | 2026 | Adventure

## Overview

Renata Kwan has the district's paper street map taped across the hood of Sweeper 6, its corners
lifting in the diesel exhaust, and a red grease pencil already chewed flat on one end. It is 5:40
in the morning, leaf season starts in two weeks, and the route she inherited last spring has her
trucks doubling back down Larkspur three separate times before the shift ever reaches Birchwood.
The radio on her hip crackles — the division director wants her routing memo by end of day, the
one that decides whether the department pays for a short stretch of new pavement or just keeps
eating the extra diesel every single week. Behind her, Sweeper 6 idles, gutter broom folded up,
waiting on her to draw the line. She traces Larkspur with the pencil, then Birchwood, then the
short dead-end nub off Persimmon that has bothered her for two sweeps running. Somewhere on this
map is the exact reason none of this ever closes into one clean loop, and she is fairly sure she
has finally found it — not a guess this time, a number. She uncaps the pencil, looks up at the
idling truck, and starts counting corners.

## Background

Renata Kwan is the Route Supervisor for the Streets and Sanitation Division of the Department of
Public Works in the city of Talbrook. She is responsible for sweeper-truck routing across
Talbrook's residential neighborhoods and is accountable to the division director for the fuel and
labor cost of every route she designs — including every "deadhead" mile her crews drive over a
street segment they have already swept that same shift (SEE APPENDIX A). She does not control the
city's road-construction budget, but her annual routing memo is what the division director uses to
decide whether that budget funds a new residential connector street this cycle.

This year's memo covers Larkspur Hollow, a real residential neighborhood whose full street network
— every block, every intersection, every dead end — has been mapped as a graph: each intersection
or dead end a vertex, each street segment between two of them an edge. The real network contains
**58** vertices connected by **86** edges, totaling **3.96 miles** of street (SEE APPENDIX A). A
sweeper truck that starts and ends at the same depot corner and drives every street segment exactly
once, with nothing repeated, is only possible if every vertex in that graph touches an even number
of street segments — Euler's theorem, applied literally to pavement (SEE APPENDIX B). Larkspur
Hollow's real intersection layout does not have that property: **48 of its 58 vertices** touch an
odd number of segments, which means a true single-pass route is not merely hard to find — on the
network as it exists today, it is mathematically impossible (SEE APPENDIX B).

Larkspur Hollow's graph is modeled on a real neighborhood's real street layout, not an invented
grid — building it honestly required a few disclosed modeling choices about where the district's
boundary is drawn and how often a route like this really runs (SEE APPENDIX E).

Two responses are on Renata's desk before the memo is due, and the division can only fund one this
cycle. **The As-Is Loop** keeps Larkspur Hollow's street network exactly as it is and instead
computes the specific, calculable minimum amount of already-swept street the route must drive a
second time to close into one continuous loop — no capital request, a fixed and predictable
increase in fuel cost every single week the crew sweeps (SEE APPENDIX C). **The Persimmon
Connector** asks the division to fund a short new stretch of pavement joining two of the network's
vertices, at a one-time construction cost of roughly **$1,600 per linear foot** for an estimated
**302-foot** connector — a change to the graph itself that reduces, though it does not eliminate,
how much repeat mileage every future sweep needs (SEE APPENDICES C AND D). Every sourced figure in
this case is listed in **APPENDIX F**; the vocabulary and "how to…" skills the case will ask of
you are listed in **APPENDIX H** — that is where Challenge 1 sends you. Curious readers can go
further with real, freely available resources on Euler's theorem and the real town Larkspur
Hollow's street network is modeled on (SEE APPENDIX G).

## Dilemma

You are Renata Kwan.
Do you:
A.) Run The As-Is Loop — accept the calculated minimum repeat-mileage route on Larkspur Hollow's
street network exactly as it exists today OR
B.) Petition for The Persimmon Connector — fund a new connector street that shrinks the required
repeat mileage, at a one-time construction cost

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A vertex-degree table for every vertex in the Larkspur Hollow Practice Block (SEE APPENDIX
    C), a real 23-intersection excerpt of the full network small enough to tally by hand: each
    vertex listed with the number of street segments touching it, and each one labeled EVEN or ODD.
    D2. A written Euler-circuit determination for the full Larkspur Hollow network (SEE APPENDIX
    B): state which of the three possible cases applies — an Euler circuit exists, an Euler path
    exists but no circuit, or neither exists — and justify your answer using the specific count of
    odd-degree vertices given there, not just a restatement of the theorem.
    D3. A minimum repeat-mileage route for the Practice Block (SEE APPENDIX C): using the provided
    shortest-connecting-path distance table, pair up every odd-degree vertex from D1 with another
    odd-degree vertex, show every paired distance and how you chose the pairing, then compute the
    resulting deadhead ratio — total miles driven divided by total miles of street actually
    serviced — for one full sweep of the Practice Block. Then compare your Practice Block ratio to
    the full network's official deadhead ratio (SEE APPENDIX C) and explain in words why the two
    numbers are close but not identical.
    D4. A capital-cost-versus-savings comparison for The Persimmon Connector on the full network
    (SEE APPENDIX D): recompute the degree of the two vertices the connector would join, reapply
    the Euler test from D2 to the changed network, and show how much repeat mileage the connector
    removes. Then compare its one-time construction cost against the fuel-cost savings that reduced
    repeat mileage produces every sweep, with the payback period stated in years.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — The Larkspur Hollow Street Network

The full real street-network graph for the Larkspur Hollow neighborhood: every intersection and
dead end as a vertex (labeled I1–I58), every street segment between two of them as an edge, with
the length of each segment. Depot corner: **I1** (Smolian Circle).

| | Value |
|---|---|
| Vertices (intersections and dead ends) | **58** [S3, derived] |
| Edges (street segments) | **86** [S3, derived] |
| Total street mileage (sum of every edge length) | **3.9597 mi** [S3, derived] |

**Full vertex list** (label, cross streets, degree, even/odd — degree and even/odd columns are
reproduced from Appendix B so this table stands alone):

| Label | Cross streets | Degree | Even/Odd |
|---|---|---|---|
| I1 | Smolian Circle | 3 | ODD |
| I2 | Forest Street & Smolian Circle | 3 | ODD |
| I3 | Grayton Street & Smolian Circle | 3 | ODD |
| I4 | Butler Street & Smolian Circle | 3 | ODD |
| I5 | Butler Street & Pensacola Street | 4 | EVEN |
| I6 | Butler Street & Grayton Street & Odessa Street | 5 | ODD |
| I7 | Quincy Circle & Seaside Avenue | 3 | ODD |
| I8 | East Ruskin Street & Seaside Avenue | 4 | EVEN |
| I9 | Forest Street & Seaside Avenue | 3 | ODD |
| I10 | Grayton Street & Natchez Street | 3 | ODD |
| I11 | East County Highway 30A & Natchez Street | 3 | ODD |
| I12 | Roberts Way & West Grove Avenue | 2 | EVEN |
| I13 | Savannah Street & West Grove Avenue | 4 | EVEN |
| I14 | East Ruskin Street & West Grove Avenue | 3 | ODD |
| I15 | East County Highway 30A & Savannah Street | 3 | ODD |
| I16 | East County Highway 30A & West Ruskin Street | 3 | ODD |
| I17 | Forest Street & Savannah Street | 3 | ODD |
| I18 | Grayton Street & Pensacola Street | 4 | EVEN |
| I19 | Forest Street & Grayton Street | 2 | EVEN |
| I20 | Quincy Circle & Seaside Avenue | 3 | ODD |
| I21 | Quincy Circle & Ruskin Place | 3 | ODD |
| I22 | East County Highway 30A & Quincy Circle | 3 | ODD |
| I23 | East County Highway 30A & Roberts Way | 2 | EVEN |
| I24 | East County Highway 30A & Tupelo Street | 3 | ODD |
| I25 | Forest Street & Tupelo Street | 3 | ODD |
| I26 | East County Highway 30A & Rosewalk Alley | 3 | ODD |
| I27 | East County Highway 30A & East Ruskin Street | 3 | ODD |
| I28 | East County Highway 30A & Quincy Circle | 3 | ODD |
| I29 | Central Square & East County Highway 30A | 3 | ODD |
| I30 | Central Square & East County Highway 30A | 3 | ODD |
| I31 | East County Highway 30A & Pensacola Street | 3 | ODD |
| I32 | East County Highway 30A & Odessa Street | 3 | ODD |
| I33 | Rosewalk Alley | 1 | ODD |
| I34 | Forest Street & Pensacola Street | 3 | ODD |
| I35 | East Ruskin Street & Ruskin Place | 3 | ODD |
| I36 | Forest Street & Ruskin Place | 3 | ODD |
| I37 | Ruskin Place & West Ruskin Street | 3 | ODD |
| I38 | Forest Street & Odessa Street | 4 | EVEN |
| I39 | Forest Street | 3 | ODD |
| I40 | Forest Street & Venice Circle | 3 | ODD |
| I41 | Forest Street & Seaside Avenue | 3 | ODD |
| I42 | Forest Street | 3 | ODD |
| I43 | Forest Street & Venice Circle | 2 | EVEN |
| I44 | Venice Circle & Wakulla Lane | 3 | ODD |
| I45 | Venice Circle & Wakulla Lane | 3 | ODD |
| I46 | (unnamed lane) & West Grove Avenue | 3 | ODD |
| I47 | (unnamed lane) & West Grove Avenue | 3 | ODD |
| I48 | (unnamed lane) & Tupelo Street | 3 | ODD |
| I49 | (unnamed lane) & Tupelo Street | 3 | ODD |
| I50 | Odessa Street (dead end) | 1 | ODD |
| I51 | East Ruskin Street & Seaside Avenue | 4 | EVEN |
| I52 | Forest Street & Ruskin Place | 3 | ODD |
| I53 | Quincy Circle & Smolian Circle | 3 | ODD |
| I54 | Quincy Circle & Smolian Circle | 3 | ODD |
| I55 | Smolian Circle & West Ruskin Street | 3 | ODD |
| I56 | Smolian Circle & West Ruskin Street | 3 | ODD |
| I57 | Ruskin Place & Smolian Circle | 3 | ODD |
| I58 | East County Highway 30A (district-boundary vertex) | 1 | ODD |

**Full edge list** (86 segments):

| Segment | Street | Length (mi) |
|---|---|---|
| I46–I48 | (unnamed lane) | 0.0035 |
| I47–I49 | (unnamed lane) | 0.0073 |
| I48–I47 | (unnamed lane) | 0.0106 |
| I49–I46 | (unnamed lane) | 0.0073 |
| I4–I5 | Butler Street | 0.0442 |
| I5–I6 | Butler Street | 0.0452 |
| I29–I30 | Central Square | 0.1453 |
| I11–I58 | East County Highway 30A | 0.1004 |
| I15–I27 | East County Highway 30A | 0.0445 |
| I16–I31 | East County Highway 30A | 0.0453 |
| I22–I16 | East County Highway 30A | 0.0435 |
| I23–I26 | East County Highway 30A | 0.0342 |
| I24–I15 | East County Highway 30A | 0.0445 |
| I26–I24 | East County Highway 30A | 0.0238 |
| I27–I28 | East County Highway 30A | 0.0442 |
| I28–I29 | East County Highway 30A | 0.0282 |
| I29–I30 | East County Highway 30A | 0.0665 |
| I30–I22 | East County Highway 30A | 0.0285 |
| I31–I32 | East County Highway 30A | 0.0447 |
| I32–I11 | East County Highway 30A | 0.0452 |
| I8–I51 | East Ruskin Street | 0.0071 |
| I14–I8 | East Ruskin Street | 0.0236 |
| I27–I14 | East Ruskin Street | 0.0860 |
| I51–I35 | East Ruskin Street | 0.0658 |
| I2–I39 | Forest Street | 0.0256 |
| I9–I17 | Forest Street | 0.0200 |
| I17–I40 | Forest Street | 0.0084 |
| I19–I38 | Forest Street | 0.0748 |
| I25–I43 | Forest Street | 0.0129 |
| I34–I2 | Forest Street | 0.0682 |
| I36–I42 | Forest Street | 0.0539 |
| I38–I34 | Forest Street | 0.0451 |
| I39–I52 | Forest Street | 0.0523 |
| I40–I25 | Forest Street | 0.0237 |
| I41–I9 | Forest Street | 0.0071 |
| I42–I41 | Forest Street | 0.0648 |
| I42–I39 | Forest Street | 0.1620 |
| I52–I36 | Forest Street | 0.0515 |
| I6–I18 | Grayton Street | 0.0450 |
| I10–I6 | Grayton Street | 0.0456 |
| I18–I3 | Grayton Street | 0.0451 |
| I19–I10 | Grayton Street | 0.0345 |
| I10–I11 | Natchez Street | 0.0786 |
| I6–I38 | Odessa Street | 0.0393 |
| I32–I6 | Odessa Street | 0.0785 |
| I38–I50 | Odessa Street | 0.0102 |
| I5–I34 | Pensacola Street | 0.0388 |
| I18–I5 | Pensacola Street | 0.0164 |
| I31–I18 | Pensacola Street | 0.0783 |
| I7–I20 | Quincy Circle | 0.0072 |
| I20–I21 | Quincy Circle | 0.0226 |
| I21–I53 | Quincy Circle | 0.0463 |
| I28–I7 | Quincy Circle | 0.0650 |
| I53–I54 | Quincy Circle | 0.0620 |
| I54–I22 | Quincy Circle | 0.0376 |
| I12–I23 | Roberts Way | 0.0909 |
| I26–I33 | Rosewalk Alley | 0.0198 |
| I21–I35 | Ruskin Place | 0.0453 |
| I35–I36 | Ruskin Place | 0.0421 |
| I37–I52 | Ruskin Place | 0.0421 |
| I57–I37 | Ruskin Place | 0.0335 |
| I13–I17 | Savannah Street | 0.0576 |
| I15–I13 | Savannah Street | 0.0860 |
| I7–I8 | Seaside Avenue | 0.0603 |
| I8–I9 | Seaside Avenue | 0.0577 |
| I41–I51 | Seaside Avenue | 0.0575 |
| I51–I20 | Seaside Avenue | 0.0604 |
| I1–I2 | Smolian Circle | 0.0278 |
| I1–I4 | Smolian Circle | 0.0272 |
| I3–I55 | Smolian Circle | 0.0189 |
| I4–I3 | Smolian Circle | 0.0297 |
| I53–I57 | Smolian Circle | 0.0199 |
| I55–I54 | Smolian Circle | 0.0428 |
| I56–I1 | Smolian Circle | 0.0510 |
| I57–I56 | Smolian Circle | 0.0219 |
| I24–I49 | Tupelo Street | 0.0813 |
| I25–I48 | Tupelo Street | 0.0647 |
| I43–I44 | Venice Circle | 0.0457 |
| I44–I45 | Venice Circle | 0.0262 |
| I45–I40 | Venice Circle | 0.0285 |
| I44–I45 | Wakulla Lane | 0.1473 |
| I12–I46 | West Grove Avenue | 0.0277 |
| I13–I47 | West Grove Avenue | 0.0398 |
| I14–I13 | West Grove Avenue | 0.0440 |
| I37–I56 | West Ruskin Street | 0.0297 |
| I55–I16 | West Ruskin Street | 0.0723 |

**How Appendix A was built.** [S3] Larkspur Hollow's street network is modeled on the real street
layout of the town of Seaside, Florida, pulled directly from OpenStreetMap (SEE APPENDIX E, MA1).
The raw geometry was collapsed into a graph the same way a real GIS routing tool does: every node
where two or more differently-named streets meet, and every dead end, becomes a vertex; every
uninterrupted run of the same-named street between two such vertices, however many shape points it
takes to draw its curve, becomes a single edge whose length is the summed real-world distance along
that curve (computed with the great-circle/haversine formula from the raw GPS coordinates, not a
straight-line guess). Three OSM way segments that leave Seaside's built area and run for over a
fifth of a mile toward neighboring, unmapped communities were excluded as outside Renata's assigned
route district (SEE APPENDIX E, MA2); one small, disconnected two-node fragment with no path back to
the rest of the network was also excluded.

## Appendix B — Vertex Degree Table and Euler Determination

The degree of every vertex is given in Appendix A's vertex list. This appendix states the
theorem-level summary D2 asks you to justify.

| | Value |
|---|---|
| Number of odd-degree vertices | **48** [S3, derived] |
| Number of even-degree vertices | **10** [S3, derived] |
| Euler's theorem outcome for this network | **Neither an Euler circuit nor an Euler path exists.** A graph has an Euler circuit only if every vertex has even degree (0 odd vertices), and an Euler path (but no circuit) only if exactly 2 vertices have odd degree. Larkspur Hollow has 48 odd-degree vertices — far more than 2 — so neither special case applies, and *some* repeated driving is unavoidable no matter how the route is planned [S3, derived]. |

## Appendix C — Larkspur Hollow Practice Block, and the Official As-Is Loop Numbers

**Part 1 — The Practice Block (for D1 and D3).** A real, connected, 23-vertex excerpt of the full
network — the Smolian Circle / Quincy Circle loop and its immediate connections — small enough to
tally and pair by hand. Vertices where a named street exits this excerpt toward the rest of the
real network (SEE APPENDIX A) are treated as this excerpt's own edge for practice purposes; they
are not necessarily true physical dead ends in the full network.

Practice Block vertices (label, corresponding full-network label):

| Practice label | Full-network label | Practice-Block degree |
|---|---|---|
| P1 | I1 | 3 |
| P2 | I2 | 2 |
| P3 | I3 | 2 |
| P4 | I4 | 2 |
| P5 | I7 | 2 |
| P6 | I16 | 2 |
| P7 | I20 | 2 |
| P8 | I21 | 3 |
| P9 | I22 | 3 |
| P10 | I27 | 1 |
| P11 | I28 | 3 |
| P12 | I29 | 3 |
| P13 | I30 | 3 |
| P14 | I35 | 2 |
| P15 | I36 | 2 |
| P16 | I37 | 3 |
| P17 | I39 | 2 |
| P18 | I52 | 3 |
| P19 | I53 | 3 |
| P20 | I54 | 3 |
| P21 | I55 | 3 |
| P22 | I56 | 3 |
| P23 | I57 | 3 |

Practice Block edges (29 segments):

| Segment | Street | Length (mi) |
|---|---|---|
| P1–P2 | Smolian Circle | 0.0278 |
| P1–P4 | Smolian Circle | 0.0272 |
| P4–P3 | Smolian Circle | 0.0297 |
| P3–P21 | Smolian Circle | 0.0189 |
| P21–P20 | Smolian Circle | 0.0428 |
| P22–P1 | Smolian Circle | 0.0510 |
| P19–P23 | Smolian Circle | 0.0199 |
| P23–P22 | Smolian Circle | 0.0219 |
| P2–P17 | Forest Street | 0.0256 |
| P17–P18 | Forest Street | 0.0523 |
| P18–P15 | Forest Street | 0.0515 |
| P8–P14 | Ruskin Place | 0.0453 |
| P14–P15 | Ruskin Place | 0.0421 |
| P16–P18 | Ruskin Place | 0.0421 |
| P23–P16 | Ruskin Place | 0.0335 |
| P16–P22 | West Ruskin Street | 0.0297 |
| P21–P6 | West Ruskin Street | 0.0723 |
| P10–P11 | East County Highway 30A | 0.0442 |
| P11–P12 | East County Highway 30A | 0.0282 |
| P12–P13 | East County Highway 30A | 0.0665 |
| P13–P9 | East County Highway 30A | 0.0285 |
| P9–P6 | East County Highway 30A | 0.0435 |
| P12–P13 | Central Square | 0.1453 |
| P5–P7 | Quincy Circle | 0.0072 |
| P7–P8 | Quincy Circle | 0.0226 |
| P8–P19 | Quincy Circle | 0.0463 |
| P11–P5 | Quincy Circle | 0.0650 |
| P19–P20 | Quincy Circle | 0.0620 |
| P20–P9 | Quincy Circle | 0.0376 |

**Shortest-connecting-path distances between every odd-degree Practice Block vertex** (P1, P8, P9,
P10, P11, P12, P13, P16, P18, P19, P20, P21, P22, P23 — 14 vertices; distances in miles, computed
along the Practice Block's own streets) [S3, derived]:

| | P1 | P8 | P9 | P10 | P11 | P12 | P13 | P16 | P18 | P19 | P20 | P21 | P22 | P23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **P1** | — | 0.1390 | 0.1562 | 0.2779 | 0.2337 | 0.2512 | 0.1847 | 0.0806 | 0.1056 | 0.0928 | 0.1186 | 0.0758 | 0.0510 | 0.0729 |
| **P8** | 0.1390 | — | 0.1458 | 0.1388 | 0.0947 | 0.1229 | 0.1744 | 0.0997 | 0.1388 | 0.0463 | 0.1083 | 0.1510 | 0.0881 | 0.0662 |
| **P9** | 0.1562 | 0.1458 | — | 0.1674 | 0.1233 | 0.0951 | 0.0285 | 0.1530 | 0.1951 | 0.0996 | 0.0376 | 0.0804 | 0.1414 | 0.1195 |
| **P10** | 0.2779 | 0.1388 | 0.1674 | — | 0.0442 | 0.0724 | 0.1389 | 0.2385 | 0.2776 | 0.1851 | 0.2050 | 0.2478 | 0.2269 | 0.2050 |
| **P11** | 0.2337 | 0.0947 | 0.1233 | 0.0442 | — | 0.0282 | 0.0947 | 0.1943 | 0.2335 | 0.1409 | 0.1608 | 0.2036 | 0.1827 | 0.1608 |
| **P12** | 0.2512 | 0.1229 | 0.0951 | 0.0724 | 0.0282 | — | 0.0665 | 0.2225 | 0.2617 | 0.1691 | 0.1326 | 0.1754 | 0.2109 | 0.1890 |
| **P13** | 0.1847 | 0.1744 | 0.0285 | 0.1389 | 0.0947 | 0.0665 | — | 0.1815 | 0.2236 | 0.1281 | 0.0661 | 0.1089 | 0.1699 | 0.1480 |
| **P16** | 0.0806 | 0.0997 | 0.1530 | 0.2385 | 0.1943 | 0.2225 | 0.1815 | — | 0.0421 | 0.0534 | 0.1154 | 0.1564 | 0.0297 | 0.0335 |
| **P18** | 0.1056 | 0.1388 | 0.1951 | 0.2776 | 0.2335 | 0.2617 | 0.2236 | 0.0421 | — | 0.0955 | 0.1575 | 0.1814 | 0.0718 | 0.0756 |
| **P19** | 0.0928 | 0.0463 | 0.0996 | 0.1851 | 0.1409 | 0.1691 | 0.1281 | 0.0534 | 0.0955 | — | 0.0620 | 0.1048 | 0.0418 | 0.0199 |
| **P20** | 0.1186 | 0.1083 | 0.0376 | 0.2050 | 0.1608 | 0.1326 | 0.0661 | 0.1154 | 0.1575 | 0.0620 | — | 0.0428 | 0.1038 | 0.0819 |
| **P21** | 0.0758 | 0.1510 | 0.0804 | 0.2478 | 0.2036 | 0.1754 | 0.1089 | 0.1564 | 0.1814 | 0.1048 | 0.0428 | — | 0.1268 | 0.1247 |
| **P22** | 0.0510 | 0.0881 | 0.1414 | 0.2269 | 0.1827 | 0.2109 | 0.1699 | 0.0297 | 0.0718 | 0.0418 | 0.1038 | 0.1268 | — | 0.0219 |
| **P23** | 0.0729 | 0.0662 | 0.1195 | 0.2050 | 0.1608 | 0.1890 | 0.1480 | 0.0335 | 0.0756 | 0.0199 | 0.0819 | 0.1247 | 0.0219 | — |

**Part 2 — The official As-Is Loop numbers (full network, for D2, D3's comparison step, and D4).**
These are computed the same way — shortest-path pairing of all 48 odd-degree vertices — but over
the full 58-vertex network, using a minimum-weight matching algorithm rather than hand pairing
(the full working is in RESEARCH_LOG.md):

| | Value |
|---|---|
| Minimum total repeat mileage, full network (optimal pairing of all 48 odd vertices) | **0.9046 mi** [S3, derived] |
| Total miles driven, one full sweep (3.9597 + 0.9046) | **4.8643 mi** [S3, derived] |
| **Official deadhead ratio, The As-Is Loop** | **1.2285** (4.8643 ÷ 3.9597) [S3, derived] |
| Sweeper truck fuel efficiency (proxy, SEE APPENDIX F, S1) | **5.2 miles per gallon** [S1] |
| Diesel fuel price | **$5.257 per gallon** [S2] |
| Sweep frequency | **6 sweeps per year** (SEE APPENDIX E, MA3) [S4] |

## Appendix D — The Persimmon Connector: Cost and Savings Data

| | Value |
|---|---|
| Identified vertex pair the connector would join | **I16** (East County Highway 30A & West Ruskin Street) and **I54** (Quincy Circle & Smolian Circle) — the closest pair of currently-unconnected odd-degree vertices whose connection meaningfully improves the network [S3, derived] |
| Estimated connector length | **302 feet** (0.0572 mi), straight-line distance between I16 and I54 [S3, derived] |
| Construction cost per linear foot, new local residential street | **$1,600** (full reconstruction, including paving, drainage, and base) [S5] |
| Total estimated one-time construction cost | **$483,200** (302 ft × $1,600/ft) [S5, derived] |
| Recomputed degree of I16 and I54 after the connector is built | Both rise from **3 (ODD)** to **4 (EVEN)** [S3, derived] |
| New total street mileage (3.9597 + 0.0572) | **4.0169 mi** [S3, derived] |
| New odd-degree vertex count | **46** (down from 48) [S3, derived] |
| New minimum total repeat mileage (optimal pairing of remaining 46 odd vertices) | **0.8236 mi** [S3, derived] |
| New total miles driven, one full sweep (4.0169 + 0.8236) | **4.8405 mi** [S3, derived] |
| **New deadhead ratio, with the connector** | **1.2050** (4.8405 ÷ 4.0169) [S3, derived] |
| Absolute miles driven saved per sweep (4.8643 − 4.8405) | **0.0238 mi** [S3, derived] |
| Annual miles saved (0.0238 mi × 6 sweeps/year) | **0.1428 mi/year** [derived] |
| Annual gallons saved (0.1428 ÷ 5.2 mpg) | **0.0275 gal/year** [derived] |
| **Annual fuel-cost savings** (0.0275 gal × $5.257) | **$0.14/year** [derived] |
| **Payback period** ($483,200 ÷ $0.14/year) | **≈ 3.35 million years** [derived] |
| Reference construction-cost figure (lower bound, dated) | **$345/linear foot** avg ($315–$375 range), State of Michigan Treasury subdivision-cost schedule, 2003 dollars, unadjusted for inflation — implies **$104,190** total and a payback of **≈ 722,000 years** [S6, derived] |

**A discrepancy this case does not hide.** However the construction-cost estimate is sourced, the
payback period is not close to any real capital-planning horizon (typically 20–40 years for
municipal infrastructure) — it is off by roughly five orders of magnitude. On a pure fuel-cost
basis, The Persimmon Connector is not a defensible capital request. D4 asks you to compute this
yourself and reckon with it: the connector genuinely, measurably lowers the deadhead ratio (compare
Appendix C's official figure against this appendix's recomputed figure), which is this case's
stated primary metric — but "measurably better on the primary metric" and "worth building" are not
the same question, and this case does not resolve that tension for you.

## Appendix E — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | The Larkspur Hollow street network's identity | Modeled using the real, public street layout of the town of Seaside, Florida (OpenStreetMap contributors, ODbL license) as a structural stand-in for the fictional city of Talbrook's Larkspur Hollow neighborhood | Talbrook is fictional, so no real street-network data exists for it. Seaside is a real, small, densely-platted town with a real, irregular, non-grid street layout — exactly the kind of authentic vertex-degree irregularity a hand-drawn or invented grid could not honestly provide, and its full network is public and directly downloadable. | The entire case — the 48 odd-degree count, the deadhead ratio, the connector's effect — depends on this specific real network's actual topology. A different real neighborhood would give different numbers and could change which vertices are the best connector candidates, though the qualitative finding (most real street networks have many odd-degree vertices, and a single new connector helps only marginally) is a general graph-theory fact, not an artifact of this one network. |
| MA2 | District boundary treatment | Three OSM way segments that extend more than 0.2 miles beyond Seaside's built area toward neighboring, separately-mapped communities were excluded from the graph, along with one small disconnected fragment | OpenStreetMap draws some streets (notably East County Highway 30A, Forest Street, and West Grove Avenue) as single continuous ways that run well past any sensible neighborhood boundary. Including their full real length would mean Renata's "neighborhood" route actually extends over a mile into unrelated communities, which the case's own Background does not describe. The excluded segments are real pavement — they are just outside Larkspur Hollow's assigned route district, the same way any real route supervisor's district has a boundary drawn somewhere. | Vertices where an excluded segment used to continue (I11, I2, I40 in the underlying data) are treated as this district's own edge, not as literal physical dead ends — the street continues in reality, just outside Renata's assignment. This does not change the odd/even count of any vertex that remains in-district; it only removes mileage and dead-end status that were never really Renata's to route. |
| MA3 | Sweep frequency | Fixed at **6 sweeps per year** | Talbrook is fictional and has no real published sweeping schedule. The City of Austin, Texas's Resource Recovery Department publicly states residential streets are swept "up to six times a year" (SEE APPENDIX F, S4) — a real US municipal program's stated maximum, adopted here as Larkspur Hollow's assumed annual frequency. | Sweep frequency is a linear multiplier on every dollar figure in Appendix D — halving it to 3/year would halve the (already astronomical) annual savings and double the payback period; it does not change the deadhead ratio itself, which is a per-sweep, frequency-independent quantity. |

## Appendix F — Sources

| # | Claim | Value | Source | Accessed | Confidence |
|---|---|---|---|---|---|
| S1 | Fuel efficiency of a heavy-duty municipal service vehicle in a stop-and-go urban duty cycle, used as a proxy for a street-sweeper truck | 5.2 miles per gasoline-gallon-equivalent (refuse-truck category) | U.S. Department of Energy, Alternative Fuels Data Center, "Average Fuel Economy by Major Vehicle Category," sourced from Federal Highway Administration *Highway Statistics 2024* (Table VM-1). [afdc.energy.gov/data/10310](https://afdc.energy.gov/data/10310) | 2026-08-13 | MEDIUM — primary federal data series, but no street-sweeper-specific mpg figure is publicly published; refuse trucks are the closest published vocational-truck category (similar weight class, similar low-speed stop-and-go duty cycle). Units are gasoline-gallon-equivalent, applied here directly to diesel gallons as a working approximation; this is a disclosed proxy, not a sweeper-specific measurement. |
| S2 | U.S. average retail on-highway diesel fuel price | $5.257 per gallon | U.S. Energy Information Administration, "Gasoline and Diesel Fuel Update," U.S. average, week of August 10, 2026. [eia.gov/petroleum/gasdiesel/](https://www.eia.gov/petroleum/gasdiesel/) | 2026-08-13 | HIGH — primary federal statistical agency, weekly-dated series, directly fetched. |
| S3 | Larkspur Hollow's street-network graph: raw geometry, vertex/edge structure, degree distribution, minimum-repeat-mileage matchings, and the Persimmon Connector's computed effect | 58 vertices, 86 edges, 3.9597 mi total (base network); see Appendices A–D for full derived figures | OpenStreetMap contributors, Seaside, Florida street data, retrieved via the Overpass API, [overpass-api.de](https://overpass-api.de/) (query region: administrative boundary of Seaside, FL, per Nominatim). Data © OpenStreetMap contributors, [ODbL 1.0](https://www.openstreetmap.org/copyright). | 2026-08-13 | HIGH — primary, directly-queried real street-network data. All graph derivations (vertex/edge collapsing, degree counts, minimum-weight odd-vertex matching, connector candidate search) are this case's own computation, not a figure printed on any source page — full methodology and code logic in RESEARCH_LOG.md. |
| S4 | Residential street-sweeping frequency for a real US municipal program | "up to six times a year" | City of Austin, Texas, Austin Resource Recovery, "Street Sweeping" program page. [austintexas.gov/resource-recovery/programs/street-sweeping](https://www.austintexas.gov/resource-recovery/programs/street-sweeping) | 2026-08-13 | HIGH — primary municipal government source, current program page. Adopted for the fictional Talbrook as a stated Modeling Assumption (SEE APPENDIX E, MA3), since Austin's own figure is not literally Talbrook's. |
| S5 | Cost per linear foot of full municipal road reconstruction (paving, drainage, base, and other essential road functions), as recommended by a city engineer | $1,600 per linear foot | City of Fate, Texas, staff memorandum to the Honorable Mayor & City Council, "Street Replacement Plan," dated November 13, 2024 (Michael Kovacs, City Manager; Omar Williams, Assistant to the City Manager). [fatetx.gov/AgendaCenter/ViewFile/Item/11449?fileID=40396](https://www.fatetx.gov/AgendaCenter/ViewFile/Item/11449?fileID=40396) | 2026-08-13 | MEDIUM — primary municipal government document, recently dated, City-Engineer-recommended figure. Used here as a proxy: the source figure is for full reconstruction of an existing 12-foot-lane road (a maintenance/replacement project), not new construction of a short local connector on previously unpaved land, and no public per-linear-foot figure specific to a short new local residential connector could be located with comparable provenance. Likely an overestimate for Larkspur Hollow's small connector, which the case discloses rather than hides. |
| S6 | Cost per linear foot of a complete new residential subdivision street (grading, base, paving, curb and gutter, in an ordinary level subdivision) | $315–$375 per linear foot (avg. $345), 2003 dollars | State of Michigan Department of Treasury, "Subdivision Development Costs," Underwriting Investment Program manual, Section UIP 16, ©2003. | 2026-08-13 | MEDIUM — primary state-government reference document, exactly on-target for a new local subdivision street, but dated (2003, unadjusted for over two decades of construction-cost inflation) and no current equivalent with the same specificity could be located. Presented as a disclosed lower-bound reference alongside S5, not as the primary planning figure. |

## Appendix G — Learn More

Real, currently-live resources for students who want to go beyond this case's required standards
— none of these are required reading for any Challenge, and none change the numbers in Appendices
A–F.

- [Seven Bridges of Königsberg (Wikipedia)](https://en.wikipedia.org/wiki/Seven_Bridges_of_K%C3%B6nigsberg)
  — the real 1736 puzzle Leonhard Euler solved, and the origin of the even/odd-degree theorem
  Appendix B applies to Larkspur Hollow.
- [Route inspection problem (Wikipedia)](https://en.wikipedia.org/wiki/Route_inspection_problem)
  — also called the Chinese postman problem, the general theory (beyond this case's practice-block
  scope) of finding the minimum-repeat route on a graph that isn't fully even-degree.
- [Eulerian Circuit (Wolfram MathWorld)](https://mathworld.wolfram.com/EulerianCircuit.html) — a
  concise reference definition of an Eulerian circuit from a widely used online mathematics
  encyclopedia.
- [Seaside, Florida (Wikipedia)](https://en.wikipedia.org/wiki/Seaside,_Florida) — the real
  Florida Panhandle town, a pioneering "New Urbanism" planned community, whose actual street
  layout Larkspur Hollow's graph is built from (SEE APPENDIX A).

## Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Vertex
- Path
- Cycle

**"How to…" questions**

- How to determine whether a graph has an Euler path or circuit

<!-- FACILITATOR ONLY -->

## Balance argument (facilitator only — never shipped to students)

**Argument for A (The As-Is Loop).** No capital request, no construction risk, and the numbers are
fully known today: a deadhead ratio of 1.2285, a fixed and predictable extra 0.9046 miles of
repeat driving every sweep. On the only lens that has a real dollar figure attached — fuel cost —
The Persimmon Connector is not close: at these sourced rates, its payback period is on the order of
millions of years, not the 20–40-year horizon any real capital budget uses.

**Argument for B (The Persimmon Connector).** The connector is a genuine, measurable improvement on
the case's own stated primary metric: deadhead ratio drops from 1.2285 to 1.2050, a real 1.9%
improvement, in the same family as this project's own gold-standard close-margin case (SPEC §2, the
0.09%-margin Robotics Engineering exemplar). It also permanently removes two odd-degree vertices
from the network — a structural fix, not a one-time workaround — meaning every future sweep,
indefinitely, benefits from it, not just this year's.

**Margin.** `margin_pct` = **1.9** (computed on the stated primary metric, deadhead ratio: (1.2285 −
1.2050) ÷ 1.2285 ≈ 1.9%). `margin_basis`: compare The As-Is Loop's official deadhead ratio (Appendix
C, Part 2) against the deadhead ratio after The Persimmon Connector is built (Appendix D), both
computed the same way over the same full 58-vertex network.

**The trap.** The case's stated primary metric (deadhead ratio) says B wins, by a margin squarely
in this project's own "close and defensible" range. A Hero who computes only that number will
confidently recommend The Persimmon Connector. But Appendix D's dollar figures, computed from the
same underlying data, show the connector's real payback period is not merely long — it is longer
than recorded human history, several times over. The two lenses do not just disagree in degree;
they point in opposite directions almost totally. The real discussion question is not "which
calculation is correct" — both are, on their own terms — it is "which quantity should decide a
real capital request: the metric the case is titled around, or the dollar reality underneath it."

**Sensitivity note (SPEC §6).** None required — this case involves no illness, death, money stress,
or family-hardship subject matter beyond an ordinary municipal budget memo.
