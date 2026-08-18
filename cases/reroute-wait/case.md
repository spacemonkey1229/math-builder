Case Study: Reroute Or Wait
MS | Math | Case Study | 2026 | Adventure

## Overview

Nadia Ferreiro has the whole east wall of the planning room covered in butcher paper, and the
marker in her hand has gone dry. The line she keeps redrawing is Line Twenty — the bus that runs
from the far west suburbs, straight down Burnside, over the river, and out to the far east end of
the county. On the paper it is one continuous stroke. Soon it will not be, because the bridge it
crosses is coming down to be replaced, and it is not coming back for years.

Her manager stops in the doorway with a coat over one arm and does not sit down. Riders' committee
is Thursday. Somebody is going to stand up at that meeting and ask what happens to their bus, and
whatever Nadia says will be the answer they hold her to. Two service plans are pinned side by side
behind her: one keeps the line whole and sends every bus the long way around; the other cuts the
line in half at the water and lets riders make the crossing themselves. She has a printout of the
timetable, a printout of last spring's ridership counts, and the sinking feeling that both plans
are defensible and that she is the one who has to pick.

Her manager says the word "Thursday" again, more gently, and leaves. Nadia caps the dead marker,
looks at the two sheets, and reaches for the one on the left.

## Background

Nadia Ferreiro is a service planner at TriMet, the transit agency for the Portland, Oregon metro
region. She is responsible for writing the service plan that will run one bus line — Line
20-Burnside/Stark — for the duration of a multi-year bridge closure. She does not control the
construction schedule and she does not get more buses; she controls only how the buses she already
has are routed and how often they run. Her recommendation goes to the riders' committee and then
to the agency's service planning board.

The closure is real and already recommended. Multnomah County's Earthquake Ready Burnside Bridge
project will fully close the Burnside Bridge and detour traffic to neighbouring bridges while the
existing bridge is demolished and replaced [S6] (SEE APPENDIX F; SEE APPENDIX H for further reading
on why the county calls the new bridge "earthquake ready"). Line 20 crosses the Willamette
River on that bridge, on the segment between its downtown timepoint and its first east-side
timepoint (SEE APPENDIX A, APPENDIX B). Every other segment of Line 20 is untouched.

Two service plans are on the wall.

**The Long Way Round** — keep Line 20 as one through line and detour every bus around the closure
over the next bridge north. Nobody transfers. But the detour lengthens the round trip, and with a
fixed bus assignment a longer round trip buys a wider headway: under this plan Line 20 runs every
twenty minutes instead of every fifteen, for everybody, all day, for the whole closure
(SEE APPENDIX E, APPENDIX G MA1).

**The Clean Break** — split Line 20 into a west line and an east line that each stop at their own
side of the river. Neither half's running time changes and both halves keep the fifteen-minute
headway they have today [S2]. Riders who never cross the river do not lose a minute. Riders who do
cross must get themselves across on the light rail line and pick up the other half of Line 20 on
the far side (SEE APPENDIX C, APPENDIX E).

Nadia's metric is **total added rider-minutes per weekday** — the sum, across every Line 20 rider,
of the minutes the plan costs them. That total is what she has to defend on Thursday. Computing it
means treating the corridor as a network of stops joined by timed segments and asking, for each
trip, what the fastest way through that network actually is under each plan (SEE APPENDIX A,
APPENDIX B, APPENDIX C).

The ridership counts she has are real published agency counts, and they are richer than this
decision needs (SEE APPENDIX D). Part of the work is deciding which of them bear on the question.
Every figure in this case is either sourced in APPENDIX F or stated as an explicit modeling
assumption in APPENDIX G. The vocabulary and the "how to…" skills this case will ask of you are
listed in APPENDIX I — that is where Challenge 1 sends you. (SEE APPENDIX H for further reading
on the real bridge project and the earthquake risk behind it.)

## Dilemma

You are Nadia Ferreiro.
Do you:
A.) Run The Long Way Round — keep Line 20 whole, detour every bus around the closed bridge, and accept a wider headway on the same fleet OR
B.) Run The Clean Break — split Line 20 at the river, hold both halves to today's headway, and send every crossing rider through a transfer

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A drawn network graph of the corridor: every stop and station in Appendix A as a
    labelled vertex, every segment between two of them as an edge, and every edge labelled with
    its running time in whole minutes — which you must get by finding the elapsed time between
    the two printed clock times for that segment in Appendix B, not by measuring the map. Print
    the vertex count and the edge count next to the drawing.
    D2. A cycle-and-cut inventory of that same graph: write out the vertices of one cycle in
    your graph, in order, returning to where you started; then list every edge that lies on no
    cycle at all, and for each one state which two pieces the network breaks into if that edge
    is removed. Finish with one sentence saying why Option A is even available for the closed
    bridge segment and would not be available for at least one other edge you listed.
    D3. A shortest-path table for the five trips in Appendix C. For each trip give the shortest
    path as a sequence of vertices and its total weight in minutes, three times: on today's
    network, on the Option A network, and on the Option B network. Show the comparison work that
    proves the path you chose is the shortest, not just the one you noticed first.
    D4. A rider-minutes ledger: using the ridership figures in Appendix D and the counting method
    stated in Appendix E, compute the total added rider-minutes per weekday under Option A and
    under Option B, with waiting minutes and in-vehicle minutes shown on separate lines before
    the total. Then convert each weekday total into rider-hours per weekday, and into rider-hours
    over the whole closure, and state which plan you are recommending and by what margin.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — The Corridor Network

The stops and stations this decision runs through, and which published service serves each one.

| Vertex | Name | Served by |
|---|---|---|
| BTC | Beaverton Transit Center | Line 20 [S2]; MAX Blue Line [S3]; MAX Red Line [S4] |
| STC | Sunset Transit Center | Line 20 [S2]; MAX Blue Line [S3]; MAX Red Line [S4] |
| OSG | W Burnside & SW Osage | Line 20 [S2] |
| W18 | W Burnside & SW 18th | Line 20 [S2] |
| W5 | W Burnside & SW 5th | Line 20 [S2] |
| PSN | Pioneer Square North MAX Station | MAX Blue Line [S3]; MAX Red Line [S4] |
| RQ | Rose Quarter Transit Center | MAX Blue Line [S3]; MAX Red Line [S4]; Line 77-Broadway/Halsey [S10] |
| E12 | E Burnside & SE 12th Ave | Line 20 [S2] |
| CHV | E Burnside & SE Cesar Chavez Blvd | Line 20 [S2] |
| E82 | E Burnside & SE 82nd | Line 20 [S2] |
| S122 | SE Stark & 122nd | Line 20 [S2] |
| S185 | SE Stark & 185th | Line 20 [S2] |
| MHCC | NE Kane & 29th (MHCC) | Line 20 [S2] |
| GCT | NE Kelly & 8th (Gresham Central TC) | Line 20 [S2] |

**Scope of the graph.** The edges of this case's graph are exactly the segments listed in
APPENDIX B, and no others. Several of these vertices are also served by lines and rail segments
outside that list — that is real, and it is context, not an edge. If two services connect the same
pair of vertices, the graph keeps one edge and uses the faster published running time.

**The two connections that are not Line 20 bus segments.**
- **W5 to PSN** is a walking connection: 600 feet of downtown sidewalk (SEE APPENDIX G,
  MA3), walked at the standard pedestrian design speed [S8].
- **RQ to E12** is the street segment Option B's east half would be extended over to reach the
  transit centre. Its running time is stated in APPENDIX G, MA4.

**The closed edge.** The Burnside Bridge carries the Line 20 segment between W5 and E12. That is
the edge the county's project removes [S6] (SEE APPENDIX F).

## Appendix B — Published Weekday Running Times

Clock times as printed in the agency's own published weekday schedules. Each row is one vehicle,
read left to right. **The running time of a segment is the elapsed time between the two printed
times at its ends — you compute it; this appendix does not print it.** Trip 1's running times
govern every edge weight used in this case (the agency's own later trips pad a couple of segments
by a minute or two for schedule recovery — use Trip 1's times consistently rather than mixing
trips).

**Line 20-Burnside/Stark, weekday, to Portland and Gresham Central Transit Center** [S2]

| Trip | BTC | STC | OSG | W18 | W5 | E12 | CHV | E82 | S122 | S185 | MHCC | GCT |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 12:35pm | 12:51pm | 1:08pm | 1:12pm | 1:18pm | 1:24pm | 1:32pm | 1:40pm | 1:53pm | 2:07pm | 2:23pm | 2:35pm |
| 2 | 12:50pm | 1:06pm | 1:23pm | 1:27pm | 1:33pm | 1:39pm | 1:47pm | 1:55pm | 2:08pm | 2:22pm | 2:38pm | 2:50pm |
| 3 | 1:05pm | 1:21pm | 1:38pm | 1:42pm | 1:48pm | 1:54pm | 2:02pm | 2:10pm | 2:24pm | 2:39pm | 2:55pm | 3:07pm |

**MAX Blue Line, weekday, westbound, midday** [S3]

| Trip | RQ | PSN |
|---|---|---|
| 1 | 11:50am | 11:59am |
| 2 | 12:05pm | 12:14pm |
| 3 | 12:20pm | 12:29pm |
| 4 | 12:35pm | 12:44pm |
| 5 | 12:50pm | 12:59pm |

**MAX Red Line, weekday, westbound, midday** [S4]

| Trip | RQ | PSN |
|---|---|---|
| 1 | 12:28pm | 12:37pm |
| 2 | 12:43pm | 12:52pm |
| 3 | 12:58pm | 1:07pm |

**Published headways**

| Service | Weekday midday headway |
|---|---|
| Line 20-Burnside/Stark | Read it off the three trip rows above [S2] |
| MAX Blue Line | Read it off the five trip rows above [S3]; the agency also publishes "MAX Light Rail runs every 15 minutes or less most of the day, every day." [S5] |
| MAX Red Line | Read it off the three trip rows above [S4]; same published statement [S5] |

## Appendix C — The Five Trips

Five Line 20 trips a rider might make. Trips are named by the vertex codes in APPENDIX A.

| Trip | From | To | Crosses the closed edge? |
|---|---|---|---|
| T1 | S122 | E12 | |
| T2 | W18 | W5 | |
| T3 | CHV | W5 | |
| T4 | GCT | OSG | |
| T5 | E82 | PSN | |

*(The right-hand column is yours to fill — it is part of D2 and D3, not given.)*

## Appendix D — Published Ridership

**Line 20-Burnside/Stark, weekday** [S1]

| Measure | Value |
|---|---|
| Boarding rides, weekday | 9,530 |
| Rides per revenue hour | 35.2 |
| Rides per vehicle hour | 28.5 |
| Cost per ride | $5.01 |
| Passenger miles, weekday | 32,726 |
| Passenger miles per revenue mile | 9.0 |
| Average trip length, miles | 3.4 |

**Neighbouring bus lines in the same report, weekday** [S1]

| Route | Boarding rides | Passenger miles | Avg. trip length, mi | Cost per ride |
|---|---|---|---|---|
| 12-Barbur/Sandy Blvd | 5,560 | 19,603 | 3.5 | $5.47 |
| 15-Belmont/NW 23rd | 5,030 | 10,922 | 2.2 | $5.22 |
| 19-Woodstock/Glisan | 2,500 | 7,750 | 3.1 | $7.12 |
| 77-Broadway/Halsey | 3,610 | 10,898 | 3.0 | $5.81 |

**MAX station counts near the crossing, weekday** [S7]

| Station | Ons | Offs | Total |
|---|---|---|---|
| Pioneer Square North | 2,028 | 823 | 2,851 |
| Rose Quarter TC | 2,324 | 2,327 | 4,651 |
| Old Town/Chinatown | 766 | 857 | 1,623 |
| Skidmore Fountain | 531 | 537 | 1,068 |
| Convention Center | 1,255 | 1,077 | 2,332 |

## Appendix E — The Two Service Plans, And How To Count Rider-Minutes

**Option A — The Long Way Round.** One through line. Every bus detours around the closed edge.
Every rider whose fastest trip used the closed edge now rides the detour instead, at the extra
in-vehicle cost stated in APPENDIX G, MA2. Because the round trip is longer and the bus assignment
is fixed, the headway widens for **every** Line 20 rider whether they cross the river or not: from
the published headway in APPENDIX B to the wider headway stated in APPENDIX G, MA1. Added waiting
time per rider is half the increase in headway.

**Option B — The Clean Break.** Two lines, each keeping today's running times and today's headway
[S2]. A rider who does not cross the closed edge is charged nothing. A rider who does cross rides
the east half to Rose Quarter Transit Center (APPENDIX G, MA4), waits for a train, rides across on
the light rail segment in APPENDIX B, walks from Pioneer Square North to W Burnside & SW 5th
(APPENDIX G, MA3), waits for the west half, and no longer spends the minutes the direct Burnside
Bridge segment used to take.

**Average waiting time.** For a service running on a fixed headway, this case charges a rider an
average wait of half that headway. Where two light rail lines serve the same pair of stations on
the same published headway [S3, S4], they are treated as one service at half that headway.

**Counting the riders who cross.** The published counts in APPENDIX D give total boardings and
average trip length for the whole line, not an origin-and-destination table. This case therefore
estimates the share of Line 20 trips that cross any one interior point of the route as **the
average trip length divided by the route's one-way length** — the standard result for trips
scattered uniformly along a line. The route's one-way length is not published directly and must be
derived from APPENDIX D and APPENDIX B:

```
revenue hours  = boarding rides / rides per revenue hour
revenue miles  = passenger miles / passenger miles per revenue mile
average speed  = revenue miles / revenue hours
route length   = average speed x one-way running time from the timetable
```

The limits of this estimate are stated in APPENDIX G, MA6.

**The ledger.** Added rider-minutes per weekday under each option is the sum, over every rider
group, of the number of riders in that group times the minutes that option costs each of them.
Report waiting minutes and in-vehicle minutes on separate lines before totalling.

## Appendix F — Sources

| id | Claim | Value | Source | Accessed | Confidence |
|---|---|---|---|---|---|
| S1 | Route 20-Burnside/Stark weekday boarding rides, passenger miles, rides per revenue hour, passenger miles per revenue mile, average trip length, cost per ride; and the same fields for routes 12, 15, 19, 77 | see Appendix D | TriMet Service Performance and Analysis, "Route Ridership Report — Weekdays, Spring 2024" (report production date 06/27/2024) ([link](https://trimet.org/about/pdf/route/2024spring/route_ridership_report_(sorted_by_route)_weekday.pdf)) | 2026-08-12 | HIGH |
| S2 | Line 20-Burnside/Stark weekday timepoints and printed clock times, eastbound to Portland and Gresham Central TC | see Appendix B | TriMet, "20-Burnside/Stark Weekday To Portland and Gresham Central Transit Center" ([link](https://trimet.org/schedules/w/t1020_1.htm)) | 2026-08-12 | HIGH |
| S3 | MAX Blue Line weekday westbound printed clock times at Rose Quarter TC and Pioneer Square North; Beaverton TC and Sunset TC served | see Appendix B | TriMet, "MAX Blue Line Weekday Westbound to Portland City Center and Hillsboro" ([link](https://trimet.org/schedules/w/t1100_1.htm)) | 2026-08-12 | HIGH |
| S4 | MAX Red Line weekday westbound printed clock times at Rose Quarter TC and Pioneer Square North; Beaverton TC and Sunset TC served | see Appendix B | TriMet, "MAX Red Line Weekday To Portland City Center and Hillsboro" ([link](https://trimet.org/schedules/w/t1090_1.htm)) | 2026-08-12 | HIGH |
| S5 | Published MAX service frequency statement | "MAX Light Rail runs every 15 minutes or less most of the day, every day." | TriMet, "MAX Blue Line Map and Schedule" ([link](https://trimet.org/schedules/maxblueline.htm)) | 2026-08-12 | MEDIUM — "or less" is a floor, not a single figure; the exact midday headway used by this case is read off the printed trip rows in S3/S4, not off this sentence |
| S6 | Recommended construction traffic option for the Burnside Bridge replacement | "full closure" of the Burnside Bridge with traffic diverted to neighbouring bridges; construction "scheduled to start in 2024 and last four to five years" | Multnomah County, "Earthquake Ready Burnside Bridge: Recommended Traffic Option During Construction" ([link](https://multco.us/info/earthquake-ready-burnside-bridge-recommended-traffic-option-during-construction)) | 2026-08-12 | MEDIUM — the page is the county's own, but its printed start year has not been refreshed; see APPENDIX G, MA5 for the cutoff this case applies |
| S7 | Weekday ons, offs and totals at MAX stations near the crossing | see Appendix D | TriMet, "MAX Light Rail Passenger Census — Spring 2025" ([link](https://trimet.org/about/pdf/census/2025spring/max_station_passenger_census_report.pdf)) | 2026-08-12 | HIGH |
| S8 | Pedestrian design walking speed | 3.5 feet per second | Manual on Uniform Traffic Control Devices, Section 4I.06 paragraph 7, "Pedestrian Intervals and Signal Phases" ([link](https://up.codes/s/pedestrian-intervals-and-signal-phases)) | 2026-08-12 | MEDIUM — a faithful republication of the federal standard's text rather than the federal publication itself |
| S9 | Precedent for a multi-week loss of light rail across the Steel Bridge, and the shuttle frequency used when it happened | closure "August 2-29" 2020, four weeks; "All MAX lines — Blue, Green, Orange, Red and Yellow" disrupted; "Shuttle buses will depart about every two to five minutes"; the bridge described as "the nucleus of the MAX system with more than 620 trains crossing it every day" | TriMet press release, "TriMet announces four-week closure of Steel Bridge for major MAX improvements," carried by Mass Transit ([link](https://www.masstransitmag.com/rail/infrastructure/press-release/21145538/trimet-trimet-announces-four-week-closure-of-steel-bridge-for-major-max-improvements)) | 2026-08-12 | MEDIUM — trade press carrying an agency press release verbatim; used only for a later discussion point, not for any figure in Appendices A–E |
| S10 | Line 77-Broadway/Halsey serves Rose Quarter Transit Center | timepoint present in the published weekday schedule | TriMet, "77-Broadway/Halsey Weekday To Montgomery Park" ([link](https://trimet.org/schedules/w/t1077_1.htm)) | 2026-08-12 | HIGH |

**A figure this case deliberately does not use.** Several transit-blog and trip-planner pages
publish "route length" figures for TriMet bus lines with no stated methodology and no agency
attribution. None of them is used here. The route's one-way length is instead *derived* in
APPENDIX E from four figures the agency does publish (S1, S2), so a Hero can check every step.

## Appendix G — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, each with a real basis named below. A Hero may challenge any of them in discussion —
> that is a legitimate move, and it is what APPENDIX I's shortest-path skill equips you to do.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Option A's headway | **20 minutes**, up from the published 15 [S2] | This is part of Option A's *definition*, not a measurement: the plan is "detour every bus and hold the fleet fixed." A longer round trip on a fixed fleet buys a wider headway, and 20 minutes is the next standard clock-face step above 15. A different plan — buying more buses — is a different option and is not on the wall. | Not swept in the ±50% sensitivity run, because it is a plan parameter rather than an uncertain quantity. It is nevertheless one of the largest levers in the case, and a Hero who challenges it is challenging what Option A *is*, not what it costs. |
| MA2 | Option A's extra in-vehicle time for a crossing rider | **2.5 minutes** on top of the closed segment's own published running time | Derived from the case's own sourced pace, not guessed: the detour returns to the same route on both banks and adds roughly six tenths of a mile of running to a segment the timetable already covers in 6 minutes over about a mile and a half [S2]. At that segment's own published pace the extra distance is about 2.4 minutes; the case states 2.5. | Flex it ±50% and check what it does to the primary metric. |
| MA3 | Walking distance, Pioneer Square North to W Burnside & SW 5th | **600 feet** | Three downtown Portland blocks. Converted to minutes at the standard pedestrian design speed [S8]. | Flex it ±50% and check what it does to the primary metric. |
| MA4 | Running time of Option B's east-half extension, E Burnside & SE 12th to Rose Quarter Transit Center | **8 minutes** | About one mile of inner-eastside city street. Line 20's own published segment from E Burnside & SE 12th to E Burnside & Cesar Chavez covers a comparable distance in 8 minutes [S2], so the case uses the line's own pace rather than an outside estimate. **This is the most consequential assumption in the case, and it is an assumption, not a measurement.** Recompute the primary metric with this figure halved and again with it raised by half before you recommend anything — and say what you find, including whether the recommendation survives both. A Hero who wants to overturn the recommendation should attack this distance first. |
| MA5 | Case data cutoff, and closure length | Ridership frozen at the **Spring 2024** route report [S1] and the **Spring 2025** station census [S7]; schedules and headways frozen as **retrieved 2026-08-12** [S2, S3, S4]; closure length taken as **five years — 1,300 weekdays** at 260 weekdays a year | TriMet's schedules and counts keep moving, and the county's own project page has not refreshed its printed start year [S6]. Every figure in this case is therefore pinned to the vintage named beside it, and no figure is refreshed independently of the others. Five years is the top of the county's own printed "four to five years" range [S6]. | The closure length scales both options' totals identically and cannot change which plan wins; it changes only the size of the number Nadia reads out on Thursday. |
| MA6 | The crossing-share method | share of trips crossing an interior point = average trip length ÷ route one-way length | The standard result for trips scattered uniformly along a line. It is an estimate, and it has a known direction of error here: the closed edge sits nearer the middle of the route than the ends, and it sits in the densest part of the corridor, so the true crossing share is probably **higher** than this method returns — which pushes against the plan this case's arithmetic ends up favouring, not toward it. | The method is stated rather than swept: the numbers it consumes are all sourced. Challenging the method is the strongest single move a Hero can make in discussion. |

## Appendix H — Learn More

This case is built from real published sources (SEE APPENDIX F). These links go beyond what the
math requires — they are for a Hero who wants to understand the real bridge project and the real
risk it responds to.

- [Earthquake Ready Burnside Bridge — project overview](https://multco.us/earthquake-ready-burnside-bridge) — Multnomah County's own project page explaining why the current Burnside Bridge is being replaced with one built to stay usable immediately after a major earthquake.
- [Frequently Asked Questions: EQRB](https://multco.us/info/frequently-asked-questions-eqrb) — the county's own FAQ on the project's importance, funding, design decisions, and timeline.
- [Cascadia Subduction Zone Earthquake Simulation](https://multco.us/info/cascadia-subduction-zone-earthquake-simulation) — a short animation from Multnomah County showing what could happen to the existing Burnside Bridge in a magnitude 8+ Cascadia Subduction Zone earthquake, the hazard the new bridge is designed to survive.
- [TriMet 20-Burnside/Stark weekday schedule](https://trimet.org/schedules/w/t1020_1.htm) — the live, current version of the same public schedule this case's Appendix B running times were read from, so you can see how the real published line looks today.

## Appendix I — "How To…" Math Questions To Research

**Vocabulary terms**

- Graph (Vertices And Edges)
- Vertex
- Edge
- Path
- Cycle
- Weighted Graph

**"How to…" questions**

- How to find the shortest path between two vertices in a weighted graph
- How to find elapsed time
- How to convert between units of time

<!-- FACILITATOR ONLY -->

## Balance argument

**Argument for A (The Long Way Round).** The line stays whole. Nobody is asked to stand on a
platform in January with a bag of groceries waiting for a second vehicle, and the published counts
say the number of people who would have to do that is small: the line's own average trip is 3.4
miles on a route the same report's figures derive to just under 27 miles, so only about an eighth
of Line 20's 9,530 weekday boardings cross the river at all. A plan that charges those riders a
transfer charges them a lot — more than twenty minutes each, once waiting at both ends is counted.
Option A charges every crossing rider only the detour, and it charges everyone else two and a half
minutes of extra wait, which is the smallest per-person number anywhere in this case.

**Argument for B (The Clean Break).** Two and a half minutes times *everybody* is not a small
number, and that is the whole trick of Option A: it looks cheap per person because it is spread
across 9,530 riders who mostly never go near the bridge. Option B charges nothing at all to the
seven riders in eight who never cross. Both halves keep the frequency they have today, the
schedule is honest, and the cost lands on the people the closure actually affects. Option B's
whole cost sits in one number — the 25.1-minute transfer penalty — and that number is built on a
stated assumption, not a measurement: shorten the east-half extension from 8 minutes to 4 and
Option B wins outright (APPENDIX G, MA4). Option B's cost is also the one that shrinks if the
crossing share turns out lower than the stated method returns.

**Margin.** Option A costs **26,840.7** added rider-minutes per weekday; Option B costs
**30,285.8**. Option A wins by **11.38%** on the primary metric — inside SPEC §2's 20% cap, and
close enough that the room has a real argument. Computed in `sensitivity_model.py` from Appendix
B/D's sourced figures and Appendix G's stated assumptions; every step is reproducible by hand from
this document alone. **This margin is not fully stable across every stated assumption** — Appendix
G MA4 names which one and asks you to recompute the primary metric under it before you recommend
anything. Say what you find, and whether your recommendation survives it.
