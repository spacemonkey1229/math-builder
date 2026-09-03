Case Study: The Course Correction
MS | Math | Case Study | 2026-27 | Launchpad

## Overview

The bridge of the *Coastal Aster* smells like burnt coffee and the diesel that's been idling under
the deck plates since 0400. On the chart plotter, a small turquoise ring marks the data buoy
they're due to reach — sensor package swapped, logger downloaded, back underway — before the front
now stacking up on the western horizon closes the window for good.

Priya Anand has the watch, and the helm order is hers to give.

The current readout beside the plotter has been quietly updating all morning, and it hasn't been
pointing where Priya would like it to. She can already feel the swell starting to build under the
hull, the kind that means the weather desk's forecast is arriving early.

Two courses are chalked on the whiteboard behind her, in the Captain's handwriting from last
night's turnover. One holds the straight bearing to the buoy and nothing else — steady on the
throttle, cheap, simple, exactly what the chart says. The other bends the bow into the current on
purpose, correcting for water Priya can't see moving, burning harder to hold a line the plotter
says is actually shorter.

The radio crackles — the Captain, from his bunk, half awake: *"Whichever one you pick, log your
reasoning. I'll want it at breakfast."*

Priya picks up the parallel rules.

## Background

Priya Anand is the Second Mate aboard the *Coastal Aster*, a 110-foot coastal oceanographic survey
vessel, standing the morning watch on a mooring-turnaround leg of a multi-day research cruise. The
ship is bound for NDBC Data Buoy 44090, a real National Data Buoy Center mooring in Cape Cod Bay,
to swap an instrument package and download logged data before returning to the survey grid. As
Second Mate on watch, Priya has the conn: the helm order for this leg is hers to give and hers to
defend at the watch turnover (SEE APPENDIX A).

The buoy's own current sensor is reporting a real, measured current at the moment Priya takes the
watch — a steady set that has held for the last several readings (SEE APPENDIX B). Two ways of
steering to the buoy are chalked on the bridge whiteboard.

**The True Line** corrects for that measured current before the ship ever leaves its present
heading: Priya works out, by vector subtraction, the exact heading and throttle setting that make
the ship's true course over the water — heading plus current, added as vectors — land exactly on
the shortest real-distance line to the buoy. Holding that corrected heading requires more engine
power than the ship's economical cruising setting, and the *Coastal Aster*'s fuel burn rises
sharply, not gently, as throttle increases past that setting (SEE APPENDIX C).

**The Steady Burn** points the bow directly at the buoy's charted bearing and holds the ship's
economical cruising throttle — the setting that burns the least fuel per hour of any speed the
ship can make. It makes no correction for the current at all. Over the length of the transit, the
uncorrected current pushes the ship's actual track off that bearing, so by the time the ship has
covered the buoy's along-track distance, it is no longer at the buoy — it is off to one side, and
reaching the buoy from there costs a further, un-planned leg (SEE APPENDIX A).

A weather window is closing on this leg specifically: conditions at the buoy are forecast to
deteriorate past what the mooring-turnaround work requires within a fixed number of hours from the
start of the watch (SEE APPENDIX A). The ship's underway fuel is also a real, finite resource
against this week's survey budget — every gallon burned on this one leg is a gallon not available
for the grid work still ahead (SEE APPENDIX C, D). Every sourced figure in this case is listed in
APPENDIX F; where a figure is not a matter of public record, it is stated as an explicit modeling
assumption instead (SEE APPENDIX E). Curious about ocean currents themselves, the real buoy this
case rendezvouses with, or real marine-navigation vocabulary beyond what the Dilemma requires? SEE
APPENDIX G for further reading. The vocabulary and "how to…" skills this case will ask of you are
listed in **APPENDIX H** — that is where Challenge 1 sends you.

## Dilemma

You are Priya Anand.
Do you:
A.) Steer **The True Line** — the vector-corrected heading, burning more fuel per hour to hold the shortest real-distance track OR
B.) Steer **The Steady Burn** — the uncorrected direct heading, burning less fuel per hour but drifting off the line as the current pushes the ship over the transit

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A current-vector table (SEE APPENDIX B): the measured current at Buoy 44090 written first
    as a magnitude and a direction, then resolved into east and north components, with the full
    conversion shown.
    D2. A course unit-vector table (SEE APPENDIX A): the desired course to the buoy expressed as a
    unit vector in east and north components, with the calculation that shows the resulting
    vector's magnitude is exactly one — plus each option's heading vector, expressed as that
    option's boat speed through the water times a heading unit vector.
    D3. A resultant-velocity table for The Steady Burn: the vector sum of its heading vector and
    the current vector, reported as a speed and a bearing — then, using a dot product against the
    course unit vector from D2, split that resultant into its along-track component (progress
    toward the buoy) and its cross-track component (drift off the line), under a sign convention
    you state in writing.
    D4. A vector diagram for each option, drawn to scale and labeled: heading vector, current
    vector, and resultant vector, added head to tail. For The True Line, show that the resultant
    lies exactly along the course line from D2 and label the correction (crab) angle between the
    heading vector and the course. For The Steady Burn, show the resultant's drift away from the
    course line and label the drift angle.
    D5. A fuel-cost table for both options (SEE APPENDICES C AND D): engine hours, fuel burned,
    dollar cost, and dollars of fuel cost per nautical mile of *net progress* toward the buoy —
    plus a statement, defended with D3's along-track component, of whether each option makes the
    weather window in Appendix A.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — The Rendezvous Geometry

| Quantity | Value |
|---|---|
| Rendezvous point | NDBC Data Buoy 44090, Cape Cod Bay, MA — 41.840° N, 70.329° W [S1] |
| Distance from the *Coastal Aster*'s position to Buoy 44090 at the start of the watch | 27.0 nm [MA1] |
| True course (bearing) from the ship's position to Buoy 44090 | 250.0° T [MA1] |
| Hours remaining in the closing weather window, from the start of the watch | 3.0 hr [MA2] |
| The Steady Burn's heading (uncorrected — pointed directly at the charted bearing) | 250.0° T |
| The True Line's required speed-over-ground along the course line, to close the full 27.0 nm inside the weather window | 27.0 nm ÷ 3.0 hr = **9.000 kt** |

*Note: the* Coastal Aster *is a scenario construction for this case, styled on a real coastal
research-vessel class (SEE APPENDIX C) — there is no real vessel by this name. NDBC Data Buoy
44090 is real; its position above is the buoy's own published station coordinates [S1].*

## Appendix B — The Measured Current at Buoy 44090

NDBC reports ocean current direction as the direction the current is flowing **toward** (the
opposite convention from how NDBC reports wind, which is reported as the direction it blows
**from**) [S4]. Current speed is reported in centimeters per second.

| Quantity | Value |
|---|---|
| Station | NDBC 44090 — Cape Cod Bay, MA [S1] |
| Depth of reading (shallowest bin) | 1 meter [S1] |
| Observation time | 2026-09-01, 21:30 UTC [S1] |
| Current direction (toward) | 340° T [S1] |
| Current speed | 27 cm/s [S1] |
| Current speed, converted to knots | 27 cm/s ÷ 51.4444 cm/s per kt = **0.5248 kt** (1 kt = 1 nm/hr = 1,852 m/hr = 51.4444 cm/s) |

**How to read this table for D1.** A current "toward 340 at 0.5248 kt" is a vector of magnitude
0.5248 kt pointed on a bearing of 340° true. Resolved into east/north components (east =
magnitude × sin(bearing), north = magnitude × cos(bearing)): east ≈ **−0.1795 kt**, north ≈
**+0.4932 kt** — a westward-and-north-flowing set.

## Appendix C — Vessel Speed and Fuel Consumption

The *Coastal Aster* is styled on a real coastal research-vessel class, using the published
speed/fuel-consumption figures of a real 110-foot fisheries research vessel of that class [S2].

| Speed through the water (kt) | RPM | Fuel consumption (gal/hr) |
|---|---|---|
| 8.5 | 1250 | 19 [S2] |
| 9.5 | 1460 | 32 [S2] |
| ~11.5 (near top speed) | — | 60 [S2] |

*The 8.5 kt / 19 gal/hr setting is the ship's economical cruising throttle — the lowest fuel burn
of any speed in this table. Fuel consumption between the published points is not a straight
percent-for-percent trade with speed: raising speed from 8.5 to 9.5 kt (+11.8%) raises fuel burn
from 19 to 32 gal/hr (+68.4%); raising it again to ~11.5 kt (+21.1%) raises fuel burn to 60 gal/hr
(+87.5%). A speed between two published points uses the straight-line (linear) interpolation
between them — see Appendix E, MA3.*

## Appendix D — Fuel Price

| Quantity | Value |
|---|---|
| Diesel price used for this case | $5.599 per US gallon — U.S. No. 2 Diesel Retail Price, weekly series, week ending **2026-08-31** [S3] |
| "As of" cutoff for the price | 2026-08-31, the most recent week carrying a published value in the series at the time this case was written. Every dollar figure in this case is frozen at this same cutoff. |

## Appendix E — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, each with a real basis named below. A Hero may challenge them in discussion — that is a
> legitimate move, and APPENDIX H names the skills a Hero would need to test one.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | The *Coastal Aster*'s distance and bearing to Buoy 44090 at the start of the watch | 27.0 nm, on a true course of 250.0° | The *Coastal Aster* is fictional, so no real ship position exists to source; chosen to put the buoy a realistic few hours' steaming away and to place the measured current (Appendix B) at a working angle across the course — neither dead ahead nor dead abeam — so that both a real along-track effect and a real cross-track effect show up in the vector math. | **HIGH on distance, MODERATE on bearing** (`sensitivity_model.py`). The distance, paired with MA2, sets Option A's required speed-over-ground (27.0 nm ÷ 3.0 hr = 9.000 kt) — the single most load-bearing derived number in the case, since it decides which part of Appendix C's fuel curve Option A has to buy. Flexing distance alone ±25%/±50% (holding the window fixed) flips the cheaper-per-nm winner from B to A outside roughly −20% to +20% around the stated value. Flexing the bearing alone ±25°/±50° (holding distance and window fixed) does **not** flip the winner in that tested range — it moves margin_pct between about 3% and 28% by changing how much of the current's effect is along-track versus cross-track. |
| MA2 | Hours remaining in the closing weather window | 3.0 hr | Matches the Overview's "front now stacking up on the western horizon" framing — a stated scenario deadline, the same kind of narrative constraint Wind Triangle and other cases in this project use for a closing operational window. | **HIGH** (`sensitivity_model.py`). Enters Option A's required speed-over-ground inversely (9.0 kt = 27.0 nm ÷ window_hr). Loosening the window (+25%/+50%) flips the $/nm winner to Option A (a looser deadline lets Option A throttle down); tightening it (−25%/−50%) keeps Option B ahead on $/nm by a wider margin (57.6%–71.7%) while making Option B's schedule miss worse. The 3.0 hr base case sits close to the flip boundary on the loosening side — a genuinely sensitive constraint, disclosed rather than hidden. |
| MA3 | Fuel consumption at a boat speed between two published Appendix C data points is found by straight-line (linear) interpolation | Applied to The True Line's required ~9.015 kt setting | No published data point exists at exactly the speed The True Line's correction requires; linear interpolation between the two nearest real, sourced points (8.5 kt/19 gal/hr and 9.5 kt/32 gal/hr) is the most conservative estimate available without inventing a new curve shape. | **LOW-MODERATE.** The required speed (9.015 kt) sits only 1.6% of the way from the 8.5 kt anchor toward the 9.5 kt anchor, so the interpolated fuel rate (25.70 gal/hr) is close to the low end regardless of curve shape. A convex (accelerating) curve between the two real points — plausible, since the jump from 9.5 kt to ~11.5 kt in Appendix C is itself convex — would raise the interpolated rate by at most a few gal/hr here, changing metric_A by a few percent, not enough on its own to close the 16.9-point gap to Option B. |
| MA4 | On The Steady Burn, the final short leg from the current-drifted position to the buoy is sailed at the same 8.5 kt economical throttle, and the current's effect on that short final leg is not separately modeled | Applied to The Steady Burn's D5 fuel total | A simplification stated openly, matching how Wind Triangle holds one wind vector constant per leg rather than modeling continuous drift — the final leg is short enough (1.67 nm out of a 27.0 nm transit, about 6% of the total path) that re-solving the vector triangle for it changes the total by a small fraction of a gallon. | **LOW.** The un-modeled leg is under 2 nm out of 27 nm; even a full re-solve of that leg under the same current changes Option B's total time/fuel, and therefore margin_pct, by well under one percentage point. |

## Appendix F — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Measured ocean current, direction and speed, at NDBC Data Buoy 44090 (Cape Cod Bay, MA, 41.840° N, 70.329° W), shallowest depth bin | Direction (toward) 340° T; speed 27 cm/s; observed 2026-09-01, 21:30 UTC, at 1 m depth | NOAA National Data Buoy Center, real-time ADCP data file for station 44090 ([link](https://www.ndbc.noaa.gov/data/realtime2/44090.adcp)); station location confirmed at the [station page](https://www.ndbc.noaa.gov/station_page.php?station=44090) | 2026-09-01 | HIGH — live, directly fetched real-time federal ocean-observation data, re-confirmed at the station page for location |
| S2 | Speed/fuel-consumption figures for a real 110-foot coastal fisheries research vessel | 8.5 kt (1250 RPM) = 19 gal/hr; 9.5 kt (1460 RPM) = 32 gal/hr; ~11.5 kt (near top speed) = 60 gal/hr | Alaska Department of Fish and Game, "Medeia cuts fuel consumption 30 percent," Wildlife News ([link](https://www.adfg.alaska.gov/index.cfm?adfg=wildlifenews.view_article&articles_id=413)) | 2008-12 | MEDIUM — real, named, government-published vessel-operations figures for the R/V Medeia, a genuine 110-ft state fisheries research vessel; used as the sourced speed/fuel basis for the fictional *Coastal Aster*'s "coastal research-vessel class" spec (the case does not claim the *Coastal Aster* is the Medeia). Article is 2008-dated; no more recent public fuel-curve figure for a comparable vessel class was found (see RESEARCH_LOG.md) |
| S3 | U.S. retail diesel fuel price | $5.599 per US gallon, week ending 2026-08-31 | U.S. Energy Information Administration, *U.S. No. 2 Diesel Retail Prices*, weekly series ([link](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=pet&s=emd_epd2d_pte_nus_dpg&f=w)) | 2026-08-31 | HIGH — live federal price series, most recent published week at time of writing; on-highway/retail diesel used as a proxy for this vessel's marine diesel price, since no marine-specific bunker price at this small a vessel scale is publicly quoted (see RESEARCH_LOG.md) |
| S4 | Whether NDBC reports ocean current direction as the direction the current flows *from* or *toward* | Toward — "The direction the ocean current is flowing toward. 0-360 degrees, 360 is due north, 0 means no measurable current." | NOAA National Data Buoy Center, *Nonstandard Meteorological/Ocean Data Measurement Descriptions* ([link](https://www.ndbc.noaa.gov/faq/measdes.shtml)) | current page | HIGH — official NDBC documentation, confirms the convention is the opposite of how the agency reports wind direction |

## Appendix G — Learn More

These are real, currently-live resources for a Hero who wants to go beyond what the Dilemma
requires — none of them is needed to complete a Challenge, and none is a source for a figure used
anywhere else in this case (those are listed separately in Appendix F).

- [National Data Buoy Center](https://www.ndbc.noaa.gov/). The live NOAA site this case's current
  reading (Appendix B) comes from — a Hero can look up today's actual conditions at Buoy 44090, or
  any other real buoy, here.
- [Ocean current — Wikipedia](https://en.wikipedia.org/wiki/Ocean_current). An overview of what
  drives ocean currents and why they vary in speed and direction the way Appendix B's single
  reading does.
- [Dead reckoning — Wikipedia](https://en.wikipedia.org/wiki/Dead_reckoning). Background on the
  real navigation method this case's two options are variations on, including the real maritime
  term for what Appendix A/D3 ask you to compute: "set and drift."
- [Dot product — Wikipedia](https://en.wikipedia.org/wiki/Dot_product). A fuller explanation of the
  operation behind D3's along-track/cross-track split, including how a dot product with a unit
  vector gives the scalar projection of one vector onto another's direction.

## Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Vector
- Magnitude (Of A Vector)
- Unit Vector
- Dot Product

**"How to…" questions**

- How to find the magnitude and direction of a vector
- How to add and subtract vectors
- How to find the dot product of two vectors

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
