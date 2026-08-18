Case Study: Wind Triangle
MS | Math | Case Study | 2026 | Launchpad

## Overview

The plotter on Reza Haddad's second monitor finishes drawing the jet stream across the middle of
the country, and it lands exactly where he did not want it. The coffee beside his keyboard has
gone cold. Somewhere behind him on the dispatch floor a colleague laughs at something on a phone.
Nobody else in the room is looking at his screen.

Meridian 412 pushes back within the hour, and the release cannot go until it carries his
certificate number. Not the captain's. His. If that airplane rolls out at the far end with less
fuel in the tanks than the rules required him to plan for, the letter comes to his desk, and it
comes with his name on it.

He has two flight plans open side by side. One is the route the schedulers assume he will file —
the straight one, the one that looks shortest on the map, the one that runs directly into the
ribbon of wind now glowing across his display. The other bends south, adds miles he will have to
justify to somebody, and slides underneath the worst of it.

The forecast is a forecast. It is the best product the government publishes, and it is still, in
the end, a statement about air that has not happened yet.

The captain's name appears in the crew chat: *Anything I should know before I sign?*

Reza drags the two plans onto one screen and looks at them together for the first time.

## Background

Reza Haddad is a certificated aircraft dispatcher on the domestic desk at Meridian Air. Under the
rules his airline flies by, he and the captain share responsibility for the flight: the captain
commands the aircraft, but the dispatcher signs the release, chooses the route, and computes the
fuel load, and neither of them may depart without the other's agreement. The fuel figure on the
release is Reza's professional judgment, filed under his own certificate.

Meridian 412 is a scheduled transcontinental service from New York Kennedy to San Francisco, flown
westbound in the morning against the prevailing upper-level flow. Two routings are on Reza's
screen (SEE APPENDIX A).

**The Great Circle** follows the short northern track — within a couple of nautical miles of the
shortest distance between the two airports across the curved surface of the earth — and passes
through the forecast core of the jet stream (SEE APPENDIX B).

**The Southern Swing** bends the routing south of the forecast jet core. It is a longer track over
the ground, but the upper-level wind along it is forecast to be far weaker (SEE APPENDIX B).

Both routings are flown by the same aircraft, at the same cruise altitude, at the same true
airspeed and the same cruise fuel flow (SEE APPENDIX C) — so the two options differ in exactly two
things: how far the aircraft flies through the air, and how hard the air pushes back.

Two hard constraints apply to either choice. First, the regulations set a minimum dispatch fuel
load: enough to fly to the destination, then to the most distant filed alternate, then for a fixed
additional period at normal cruising fuel consumption (SEE APPENDIX C). Reza has to compute that
figure for whichever routing he files, and put it on the release. Second, the fuel Meridian buys
is a real cost per gallon, and the difference between two routings is money the airline actually
spends or actually keeps, on every departure, all year (SEE APPENDIX D).

The wind data Reza is planning against is a published forecast for a stated date and valid period,
not a measurement of the flight itself, and Meridian's system pulls the whole corridor's worth of
stations whether a given routing uses them or not (SEE APPENDIX B). Where a figure in this case is
not a matter of public record, it is stated as an explicit modeling assumption (SEE APPENDIX E)
rather than guessed, and every sourced figure is listed in (SEE APPENDIX F). The vocabulary and
the "how to…" skills this case will ask of you are listed in **APPENDIX H** — that is where
Challenge 1 sends you. Curious about the real dispatcher's job, the jet stream itself, or the
aircraft in this case beyond what the Dilemma requires? SEE APPENDIX G for further reading.

## Dilemma

You are Reza Haddad.
Do you:
A.) File The Great Circle — the short northern track, straight through the forecast jet core OR
B.) File The Southern Swing — the longer southern track that slides under the strongest wind

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A wind-vector table covering every waypoint on both routings (SEE APPENDIX B): the wind
    at cruise level written first as a magnitude and a direction, and then resolved into east and
    north components, with the full conversion shown for at least one entry.
    D2. A course unit-vector table covering every leg of both routings (SEE APPENDIX A): each
    leg's true course expressed as a unit vector in east and north components, with the
    calculation that shows the resulting vector's magnitude is exactly one.
    D3. A wind-component table: for every leg, the dot product of that leg's wind vector with that
    leg's course unit vector, in knots, under a sign convention you state in writing for headwind
    versus tailwind — with the crosswind component reported alongside it.
    D4. A wind-triangle diagram and ground-speed table for every leg: the true-airspeed vector,
    the wind vector, and the resulting ground vector drawn head to tail and added, with the ground
    speed reported as the magnitude of that sum and the diagram labeled to scale. Note the
    condition that closes the triangle: the aircraft is flown on whatever heading makes the
    resulting ground vector lie **along the leg's course** — it crabs into the wind rather than
    pointing straight down the course line — so the true-airspeed vector is generally not parallel
    to the course unit vector from D2.
    D5. A trip fuel table for both routings (SEE APPENDICES C AND D) — leg time, leg fuel, route
    total, the minimum dispatch fuel required by the reserve rule, and pounds of fuel burned per
    nautical mile of net progress toward the destination — plus a break-even calculation: by what
    percentage would the forecast headwind component along The Great Circle have to be overstated
    for the two routings to cost the same fuel?

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — The Two Routings

Each routing is a chain of published waypoints, each of which is a real airport whose reference
position is published by the FAA and served through the Aviation Weather Center's airport data
service [S1, S2]. Leg distance is the great-circle distance between consecutive waypoints,
computed from those positions on a **spherical earth of radius 3,440.065 nm** (the figure used
throughout this case — a different radius or an ellipsoidal model shifts every distance below by
about a tenth of a percent, in the same direction, and changes no comparison). Leg true course is
the **initial** course of the leg, measured clockwise from true north, and it is held constant for
the whole leg (SEE APPENDIX E, MA5).

**Routing A — The Great Circle**

| Leg | From | To | From position | To position | Leg great-circle distance (nm) | Leg initial true course (°) |
|---|---|---|---|---|---|---|
| A1 | KJFK — New York/John F Kennedy Intl [S1] | KDBQ — Dubuque Rgnl [S2] | 40.6399° N, 73.7787° W [S1] | 42.4020° N, 90.7095° W [S2] | 767.1 | 283.5 |
| A2 | KDBQ — Dubuque Rgnl [S2] | KSLC — Salt Lake City Intl [S2] | 42.4020° N, 90.7095° W [S2] | 40.7884° N, 111.9778° W [S2] | 957.4 | 271.4 |
| A3 | KSLC — Salt Lake City Intl [S2] | KSFO — San Francisco Intl [S2] | 40.7884° N, 111.9778° W [S2] | 37.6188° N, 122.3754° W [S2] | 519.4 | 251.9 |

Routing A total great-circle track: **2,243.9 nm**. Filed track miles after the airway-structure
allowance (SEE APPENDIX E, MA2): **2,266.3 nm**.

**Routing B — The Southern Swing**

| Leg | From | To | From position | To position | Leg great-circle distance (nm) | Leg initial true course (°) |
|---|---|---|---|---|---|---|
| B1 | KJFK — New York/John F Kennedy Intl [S1] | KSGF — Springfield-Branson Ntl [S2] | 40.6399° N, 73.7787° W [S1] | 37.2457° N, 93.3886° W [S2] | 936.0 | 263.8 |
| B2 | KSGF — Springfield-Branson Ntl [S2] | KABQ — Albuquerque Intl Sunport [S1] | 37.2457° N, 93.3886° W [S2] | 35.0389° N, 106.6083° W [S1] | 653.9 | 262.3 |
| B3 | KABQ — Albuquerque Intl Sunport [S1] | KSFO — San Francisco Intl [S2] | 35.0389° N, 106.6083° W [S1] | 37.6188° N, 122.3754° W [S2] | 777.2 | 286.1 |

Routing B total great-circle track: **2,367.2 nm**. Filed track miles after the airway-structure
allowance (SEE APPENDIX E, MA2): **2,402.7 nm**. (The leg figures in the tables above are rounded
to a tenth of a nautical mile; both totals are computed before rounding, so a hand-added column may
differ from the total by a tenth.)

**Straight-line reference.** The direct great-circle distance from KJFK to KSFO, ignoring
waypoints entirely, is **2,241.8 nm**. This is the figure the "net progress" metric in D5 divides
by.

**Other waypoints in Meridian's corridor file.** Meridian's flight-planning system carries the
published position of every station in the transcontinental corridor, not only the ones a given
routing uses. These are also available to Reza:

| Waypoint | Position |
|---|---|
| KBUF — Buffalo Niagara Intl [S1] | 42.9404° N, 78.7306° W [S1] |
| KDEN — Denver Intl [S1] | 39.8617° N, 104.6732° W [S1] |
| KMEM — Memphis Intl [S2] | 35.0424° N, 89.9767° W [S2] |
| KLIT — Little Rock/Bill and Hillary Clinton Ntl [S1] | 34.7294° N, 92.2248° W [S1] |
| KLAX — Los Angeles Intl [S1] | 33.9425° N, 118.4080° W [S1] |

## Appendix B — Upper-Level Winds

Wind is reported the way meteorology reports it: the direction the wind is blowing **from**, in
degrees clockwise from true north, and its speed in knots. A wind "from 300 at 78" is blowing out
of the north-west at seventy-eight knots — which is to say the air itself is moving *toward* 120°.

The figures below are taken verbatim from the National Weather Service's Winds and Temperatures
Aloft Forecast, product **FBUS33 KWNO / FD3US3**, issued **12 August 2026 at 2001Z**, *data based
on 121800Z*, *valid 130600Z, for use 0300–1200Z* [S3]. The raw coded group is reproduced exactly
as the product publishes it, in the 34,000 ft column.

**How to read the coded group.** The first two digits are the wind direction in tens of degrees
true; the next two are the wind speed in knots; the last two are the temperature in degrees
Celsius (negative above 24,000 ft, so the sign is not printed). `307843` is therefore a wind from
300° at 78 knots, temperature −43 °C.

| Waypoint | Used by routing | Raw coded group at 34,000 ft [S3] | Wind direction (° true, FROM) | Wind speed (kt) | Temp (°C) |
|---|---|---|---|---|---|
| KJFK | — | `287047` | 280 | 70 | −47 |
| KBUF | — | `317547` | 310 | 75 | −47 |
| KDBQ | A | `307843` | 300 | 78 | −43 |
| KDEN | — | `211141` | 210 | 11 | −41 |
| KSLC | A | `204244` | 200 | 42 | −44 |
| KSGF | B | `341441` | 340 | 14 | −41 |
| KMEM | — | `351741` | 350 | 17 | −41 |
| KLIT | — | `030741` | 030 | 07 | −41 |
| KABQ | B | `280940` | 280 | 09 | −40 |
| KSFO | A and B | `151345` | 150 | 13 | −45 |

**How Meridian's flight-planning system applies these to a leg.** Each leg is assigned the wind at
the waypoint at its **far end** — the one the aircraft is flying toward, not the one it is leaving,
so leg A1 (KJFK→KDBQ) takes KDBQ's wind — and that single wind
vector is treated as constant for the whole leg. This is a simplification the case states openly;
a real system interpolates continuously (SEE APPENDIX E, MA3). Rows marked "—" in the second
column are stations Meridian's system pulled for this corridor that neither filed routing
currently uses.

## Appendix C — Aircraft, Performance, and the Fuel Rule

| | Value |
|---|---|
| Aircraft type flown by Meridian 412 | Boeing 737-800 (ICAO type designator B738) [S4] |
| Cruise Mach number and certified ceiling | Mach 0.79; ceiling FL410 [S4] |
| Planned cruise altitude | FL340 (34,000 ft) — the level whose winds are published in Appendix B |
| Planned true airspeed in cruise | **460 kt** [S4] |
| Cruise fuel flow, total aircraft | **40.1 kg/minute = 2,406 kg/h = 5,304.3 lb/h** [S5] (pounds figure derived at 1 kg = 2.20462 lb) |
| Minimum dispatch fuel — the reserve rule | Enough fuel to (a) fly to the airport to which it is dispatched, (b) fly to and land at the most distant alternate airport where one is required, and (c) fly thereafter for **45 minutes** at normal cruising fuel consumption [S6] |
| Filed alternate for KSFO | KLAX — Los Angeles Intl, **293.3 nm** from KSFO on an initial true course of **137.6°** (computed from the positions in Appendix A) |
| How the alternate leg is planned | Against the **KSFO** wind from Appendix B — the only wind published anywhere near the destination — and with **no** airway-structure allowance, because a diversion is flown direct rather than on a filed airway routing |

## Appendix D — What The Fuel Costs

| | Value |
|---|---|
| Jet fuel price | **$3.403 per US gallon** — U.S. Gulf Coast Kerosene-Type Jet Fuel Spot Price FOB, monthly series, **July 2026** [S7] |
| "As of" cutoff for the price | **July 2026**, the most recent month carrying a published value in the series. The series' own release date is 12 August 2026 and its August 2026 cell was still empty on that date, so no part-month value exists to use and none is used anywhere in this case. Every dollar figure in this case is frozen at this same cutoff. |
| Density used to convert pounds of fuel to gallons | See Appendix E, MA4 |
| Departures per year used to annualise the difference | See Appendix E, MA1 |

## Appendix E — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, each with a real basis named below. A Hero may challenge them in discussion — that is a
> legitimate move, and APPENDIX H names the skills a Hero would need to test one.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Meridian's frequency on this city pair, used only to annualise the per-flight difference | **2 departures per day, 365 days a year (730 departures)** | Meridian Air is fictional; no schedule for it can exist publicly. Two daily frequencies is an ordinary mainline transcontinental pattern. | Scales the annual dollar figure linearly. **Cannot change which routing wins** — it multiplies both routings by the same number. |
| MA2 | Airway-structure allowance: the percentage by which filed track miles exceed the great-circle distance, because real routings follow published airways and fixes rather than an exact great circle | **+1.0% on the northern corridor (Routing A), +1.5% on the southern corridor (Routing B)** | A real, well-known effect with no published per-corridor figure. The southern corridor is given the larger allowance on the reasoning that it offers fewer direct routings and more weather deviation. **That direction is asserted, not measured, and a Hero may reasonably argue the opposite.** | Directly load-bearing, and the single largest stated lever in the case. Flexing each value ±50%, one at a time, leaves the gap between the two routings between 0.95% and 2.40% on the primary metric; taking both to their opposite extremes at once widens that band to 0.46%–2.88%. No setting inside that range changes which routing comes out ahead. Reversing the two values **widens** the gap rather than narrowing it, to 2.64%. |
| MA3 | One wind vector per leg, taken at the leg's downwind-end waypoint and held constant along the whole leg | **Applied to all six legs** | A real flight-planning system samples the forecast grid continuously. Holding one published point wind per leg is what makes this case computable by hand. | Direction of error: it **understates** how much the wind varies along a long leg. It hits Routing A's 957.4 nm KDBQ→KSLC leg and Routing B's 936.0 nm KJFK→KSGF leg hardest, and those two legs are roughly the same length — so the simplification does not obviously favour one routing over the other. |
| MA4 | Density of Jet A used to convert pounds of fuel to US gallons | **6.7 lb per US gallon** | The planning density used throughout US aviation. The governing specification (ASTM D1655) is behind a paywall and no US-government page stating a pounds-per-gallon figure was located and fetched for this case — so this is declared as an assumption rather than cited (see `RESEARCH_LOG.md`, P71). | Affects **only** the dollar figure, and affects both routings identically. **Cannot change which routing wins.** |
| MA5 | Leg geometry: each leg's length is the great-circle distance between its endpoints, while its true course is the **initial** great-circle course of that leg, held constant from end to end | **Applied to all six legs of both routings, and to the KSFO→KLAX alternate leg** | A great circle's true course changes continuously along the leg: on the 957.4 nm KDBQ→KSLC leg it runs from 271.4° where the leg begins to 257.2° where it ends. Holding the initial course constant is the standard hand-planning simplification, and it is what makes a single dot product per leg meaningful at all. Note that a track flown on a genuinely constant true course is a rhumb line, which on these legs is longer than the great circle by roughly a tenth of a percent — so the two halves of this assumption pull very slightly against each other. | Load-bearing on every along-course and crosswind component in D3 and D4, and the least conservative assumption stated here. Re-solving the whole case instead on the mean of each leg's initial and final course, on its final course, or on true rhumb-line courses with rhumb-line distances, moves the gap on the primary metric by well under a percentage point in each case and changes which routing comes out ahead in none of them. |

## Appendix F — Sources

| id | Claim | Value | Source | Accessed | Confidence |
|---|---|---|---|---|---|
| S1 | Published airport reference positions for KJFK, KABQ, KLAX, KBUF, KDEN, KLIT | latitude/longitude in decimal degrees, as tabulated in Appendix A | NOAA/NWS Aviation Weather Center, Airport Data API ([link](https://aviationweather.gov/api/data/airport?ids=KJFK,KBUF,KDEN,KLAX,KLIT,KABQ,KONT&format=json)) | 2026-08-12 | HIGH |
| S2 | Published airport reference positions for KSFO, KDBQ, KSLC, KSGF, KMEM | latitude/longitude in decimal degrees, as tabulated in Appendix A | NOAA/NWS Aviation Weather Center, Airport Data API ([link](https://aviationweather.gov/api/data/airport?ids=KSFO,KDBQ,KMEM,KSLC,KCLE,KGLD,KSGF,KELP,KRNO,KFAT,KELY,KFMN,KALS,KGCK,KOAK,KSJC&format=json)) | 2026-08-12 | HIGH |
| S3 | Forecast wind direction and speed at 34,000 ft at each waypoint | the coded groups reproduced verbatim in Appendix B | NWS Aviation Weather Center, Winds and Temperatures Aloft Forecast **FBUS33 KWNO / FD3US3**, issued 122001Z, data based on 121800Z, valid 130600Z — retrieved from the Iowa Environmental Mesonet's permanent NWS text-product archive ([link](https://mesonet.agron.iastate.edu/wx/afos/p.php?pil=FD3US3&e=202608122001)) | 2026-08-12 | HIGH — the archive permalink above pins the **122001Z** issuance and was re-fetched at QA; all ten coded groups in Appendix B were confirmed against it. Note that `FD3US3` is a rolling product: an archive query that does not pin the issuance returns whichever forecast is current, whose winds are entirely different figures |
| S4 | Boeing 737-800 cruise true airspeed, cruise Mach number, certified ceiling | TAS 460 kt; Mach 0.79; FL410 | EUROCONTROL Aircraft Performance Database, type B738 ([link](https://learningzone.eurocontrol.int/ilp/customs/ATCPFDB/details.aspx?ICAO=B738)) | 2026-08-12 | HIGH |
| S5 | En-route fuel burn rate for a narrow-body jet | 40.1 kg per minute | EUROCONTROL, *Standard Inputs for Economic Analyses*, Release 10.0.1, Table 6.1 "Average fuel burn rates (kg/minute)", column "En route"; stated data source EUROCONTROL BADA and PRISME ([link](https://ansperformance.eu/economics/cba/standard-inputs/latest/chapters/rate_of_fuel_burn.html)) | 2026-08-12 | MEDIUM — this is the published **average for the narrow-body segment** (which the source names as including the B738), not a type-specific figure for the 737-800. It is used identically for both routings, so it scales the size of the answer and cannot change which routing wins. |
| S6 | The US domestic airline minimum dispatch fuel requirement | destination + most distant alternate + 45 minutes at normal cruising fuel consumption | 14 CFR § 121.639, *Fuel supply: All domestic operations*, Electronic Code of Federal Regulations ([link](https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-14?chapter=I&subchapter=G&part=121&subpart=U&section=121.639)) | 2026-08-12 | HIGH — independently confirmed by a second fetch of the same section at Cornell LII ([link](https://www.law.cornell.edu/cfr/text/14/121.639)) |
| S7 | Jet fuel price | $3.403 per US gallon, July 2026 | U.S. Energy Information Administration, *U.S. Gulf Coast Kerosene-Type Jet Fuel Spot Price FOB (Dollars per Gallon)*, monthly series, release date 12 August 2026 ([link](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=pet&s=eer_epjk_pf4_rgc_dpg&f=M)) | 2026-08-12 | HIGH — a live series; the "as of" cutoff stated in Appendix D applies to every dollar figure in this case, and the incomplete August 2026 month is deliberately not used |
| S8 | Documented magnitude of individual-case wind-speed error in jet-stream-level numerical weather prediction analyses and short-range forecasts | up to ±10 m/s (≈19.4 kt), concentrated in upper-level ridges above the tropopause; mean bias over the full campaign only −0.15 to −0.41 m/s | Schäfler, Harvey, Methven, Doyle, Rahm, Reitebuch, Weiler & Witschas, *"Observation of Jet Stream Winds during NAWDEX and Characterization of Systematic Meteorological Analysis Errors,"* **Monthly Weather Review** 148(7), 2889–2907, American Meteorological Society, 2020 ([link](https://doi.org/10.1175/MWR-D-19-0229.1)) | 2026-08-17 | MEDIUM — a peer-reviewed verification study of jet-stream winds using airborne Doppler lidar, dropsondes, and ground-based radar against ECMWF and UK Met Office analyses/short-range forecasts over the North Atlantic. It is **not** a verification of the specific NWS FBUS33/FD3US3 product cited in S3, and its campaign (NAWDEX, autumn 2016) is a different jet and a different forecast system — so its exact figure is not a claim about this case's own forecast error. It is offered only as real, published evidence of the general magnitude of error documented in jet-stream-level wind analysis and forecasting. |

## Appendix G — Learn More

These are real, currently-live resources for a Hero who wants to go beyond what the Dilemma
requires — none of them is needed to complete a Challenge, and none is a source for a figure used
anywhere else in this case (those are listed separately in Appendix F).

- [Aircraft dispatcher — Wikipedia](https://en.wikipedia.org/wiki/Aircraft_dispatcher). An overview
  of the real profession Reza Haddad works in, including the joint dispatcher/captain
  responsibility for a flight described in the Background section above.
- [Jet stream — Wikipedia](https://en.wikipedia.org/wiki/Jet_stream). An explanation of what a jet
  stream physically is and why it speeds up eastbound flights and slows down westbound ones like
  Meridian 412.
- [Aviation Weather Center](https://aviationweather.gov/). The live National Weather Service site
  that publishes the same kind of winds-aloft forecast data used in Appendix B — a Hero can look up
  today's actual jet-stream forecast here.
- [Dot product — Wikipedia](https://en.wikipedia.org/wiki/Dot_product). A fuller explanation of the
  operation behind D3's wind-component calculation, including how it measures the part of one
  vector that points in the direction of another.
- [Boeing 737 Next Generation — Wikipedia](https://en.wikipedia.org/wiki/Boeing_737_Next_Generation).
  Background on the aircraft family that includes the 737-800 flown on Meridian 412 (SEE APPENDIX
  C).

## Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Vector
- Magnitude (Of A Vector)
- Unit Vector
- Dot Product
- Pythagorean Theorem
- Right Triangle

**"How to…" questions**

- How to find the magnitude and direction of a vector
- How to add and subtract vectors
- How to find the dot product of two vectors
- How to convert an amount with compound units
- How to find the percent of a number

<!-- FACILITATOR ONLY -->

## Balance argument (facilitator only — never shipped to students)

**Argument for A (The Great Circle).** The extra track miles on The Southern Swing are certain and
are paid on every leg; the wind saving that is meant to pay for them exists only in a forecast.
Routing A's filed track is 2,266.3 nm against Routing B's 2,402.7 nm — 136.4 nm, or 6.0%, of extra
distance that Routing B has to earn back purely on wind. The amount of forecast error that erases
Routing B's whole advantage is a uniform **7.2 kt per leg** — a **20.5%** overstatement of Routing
A's along-course headwind components — and that figure is not an assertion, it is now evidenced:
published verification research on jet-stream-level winds finds individual-case wind-speed errors
up to **±10 m/s (≈19.4 kt)** in numerical weather prediction analyses and short-range forecasts,
concentrated in upper-level ridges above the tropopause — the same structure that produces this
case's own strongest forecast winds [S8]. That study verifies a different jet (North Atlantic) and
a different forecast system (ECMWF/Met Office, not the NWS FD product this case cites), so it is
not a direct measurement of this issuance's error — but it is real, peer-reviewed evidence that
errors several times the case's 7.2 kt/leg break-even are a documented, non-exotic feature of
jet-stream-level wind analysis and forecasting, not a rare tail event. Argument A's claim is
therefore not that Routing B's saving is fake, but that a 472.8 lb / 1.67% margin sits inside a
noise band this large, and a single 12-hour-old forecast issuance is not solid enough ground to
spend 136 certain nm chasing a number that small.

**Argument for B (The Southern Swing).** Under the wind field the National Weather Service
actually published for this date and valid period, the along-course headwind component at KDBQ is
−74.8 kt, which drops Routing A's ground speed on its first leg to 384.7 kt against a 460 kt true
airspeed. Routing B never sees an along-course headwind worse than −8.6 kt and picks up a +9.4 kt
tailwind component on its final leg. Trip fuel comes out at **27,756.2 lb for Routing B against
28,228.9 lb for Routing A** — Routing B is 472.8 lb cheaper, 1.67% on the primary metric, despite
flying 136.4 nm further. Fuel is bought by the hour, not by the mile. The published forecast is
also the product a dispatcher is required to plan against; declining to use it because it might be
wrong is not a defensible dispatch position, it is a refusal to plan.

**Margin.** `margin_pct` = **1.67**, computed in `sensitivity_model.py` from Appendix A's sourced
positions, Appendix B's sourced winds, and Appendix C's sourced performance figures, with MA2's
stated allowance applied. Every step is reproducible by hand from the case document alone.
Confirmed stable under a ±50% flex of every stated Modeling Assumption — Routing B stays cheaper
across the whole sweep, margin 0.95%–2.40% one dial at a time and 0.46%–2.88% at the joint corners
of MA2's two dials (Tier 2 probe 5). It is stable under MA5's alternatives too: on mean-of-initial-
and-final courses the margin is 2.01%, on final courses 2.27%, on true rhumb-line courses and
distances 2.06%, and Routing B is cheaper in every one. **The verdict is genuinely fragile to the
cited wind data**, which is exactly what D5's break-even measures and is disclosed as the case's own
headline finding rather than hidden.

**Which plan is actually exposed to the forecast — hand this over if the room reaches for
"certainty".** Argument A's instinct is that the shorter track is the *safe* plan because its miles
are certain while its rival's saving is only forecast. On this case's own numbers that instinct is
backwards, and a guide should not let it stand unexamined. Scaling the **whole** published wind
field from 0× to 1.5× moves Routing A's trip fuel by **3,489 lb (+12.4%)** and Routing B's by
**86 lb (+0.3%)**: Routing A's cost is the one that depends on the forecast, because Routing A is
the routing with the large winds in it. Routing A becomes the cheaper plan only below about **0.80×**
— that is, only if the entire field is overstated by roughly a fifth, and only in that direction; a
symmetric error of the same size in the other direction makes Routing A worse still. So the honest
form of Argument A is not "B's benefit is uncertain" — that claims A is the lower-variance choice,
and it is not — but "**the margin is smaller than the documented noise floor of jet-stream wind
analysis [S8], so a single forecast issuance is not solid enough evidence to spend 136 certain miles
chasing a 472.8 lb saving**." A Hero who reaches for "safer" or "certainty" should be asked which
routing the exposure actually lands on — it is A — and then asked to defend the narrower,
noise-floor version of the argument instead, which does not depend on that claim being true.

**The twist's flip is itself conditional — disclose it if pushed.** At the low end of MA2's ±50%
range for the southern corridor (0.75% instead of 1.5%) the Memphis re-route does **not** reverse
the verdict: Routing B stays cheaper by 0.10%. The flip holds for every southern allowance from
about 1.0% upward, and it holds under all of MA5's course conventions, but at the thinnest of them
it is only 0.08%. The twist is a real reversal, not a robust one, and the Guide Notes say so in the
same words.

**The trap.** A Hero will compare the two routings on the wind's raw published speed — "the
northern winds are 78 and 42 knots and the southern winds are 14 and 9, so the northern route is
obviously worse" — and never take the component along the course. That reasoning reaches the right
answer for the wrong reason, and it falls apart at KSLC, where a 42 kt wind contributes only
−13.4 kt along the course and 39.8 kt across it. The second half of the same trap is comparing the
routings on distance flown rather than time aloft, which produces a confident recommendation for
Routing A with tables and arithmetic behind it.

**The third trap, and the one that produces the most convincing wrong answer: the FROM/TOWARD sign
inversion.** Appendix B states that wind is reported as the direction it blows *from*, so a wind
from 300° is a vector pointing toward 120°. A Hero who resolves `300/78` into components without
that 180° reversal gets every along-course component with its sign flipped — Routing A's KDBQ leg
reads **+74.8 kt of tailwind** instead of −74.8 kt of headwind, its first-leg ground speed comes out
near 534 kt instead of 384.7 kt, and Routing A wins by a wide and entirely spurious margin. This
error is invisible to the diagnostic for the first trap: a sign-inverted D3 table has the *right*
magnitudes, so its headwind column does not equal the wind-speed column. The tell is different — a
D3 table whose signs say the jet stream is helping a westbound flight. Ask any room that recommends
Routing A on ground speed to say out loud which way the air is moving at KDBQ.

**Sensitivity note (SPEC §6).** None required — the stakes are commercial and professional (a fuel
bill, a dispatcher's certificate), not personal loss or family hardship. Both routings are legal
and safe; nothing in the case asks a Hero to trade safety for money.
