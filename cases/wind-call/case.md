# Case Study: Wind Call

MS | Math | Case Study | 2026-27 | Launchpad

---

## Overview

Renata Alvarez has four minutes before the dispatch release locks, and the printer is still warming up. Through the trailer window she can see the Caravan idling on the ramp, prop already turning, the cargo door still cranked open while the ramp agent finishes strapping the last pallet. Her headset crackles — the captain, asking for the release altitude so he can brief it before taxi. She doesn't answer yet.

Two number pads sit open on her second monitor, one behind the other, each one a completed wind triangle she built by hand herself twenty minutes ago rather than trust the scheduling software's canned estimate for a route this close to a decision. One triangle is for the low cruise. The other is for the high one. She already knows what the high option means operationally — the portable oxygen bottle has to come out of the hangar locker, get weighed, get logged, and the captain has to brief the crew on how to breathe through it before engine start, all inside a shrinking window. She built both triangles anyway, because "operationally simpler" and "numerically better" are not obviously the same flight today.

Her coffee has gone cold in the two hours she's been staring at these numbers. The captain's voice comes through again, quieter this time: "Renata, gate's closing. What have you got?"

She pulls both printouts toward her.

---

## Background

Renata Alvarez is the flight dispatcher of record for Highline Air Cargo, a Part 135 (the federal rulebook for commuter and on-demand charter/cargo operators, stricter than the rules for private flying) cargo and feeder operator flying Cessna 208B Grand Caravans. For every flight she releases, she is the person of record who signs the dispatch release — the single paperwork package that bundles the route, the cruise altitude, and exactly how much fuel to load — and she is accountable if that fuel load turns out to be wrong.

Today's flight is a single leg from Denver Centennial Airport (KAPA) to Wichita Dwight D. Eisenhower National Airport (KICT) (SEE APPENDIX A). The aircraft, weather, and cargo load are fixed; the only open decision is the cruise altitude Renata files on the release, because the winds aloft — and therefore the fuel burned to complete the flight — differ by altitude (SEE APPENDIX C).

Two altitudes are under consideration, and Renata has nicknamed them the way the crew will hear them read back over the radio:

- **Niner-Thousand** — cruise at 9,000 feet MSL. Below 12,500 feet, no supplemental oxygen is required for the crew under federal regulation (SEE APPENDIX D).
- **One-Eight-Thousand** — cruise at 18,000 feet MSL. Above 12,500 feet, federal regulation requires the required minimum flight crew to be provided with and use supplemental oxygen for any portion of the flight above that altitude lasting more than 30 minutes — and above 14,000 feet, oxygen is required regardless of duration (SEE APPENDIX D). The Caravan's cabin is unpressurized, so "above 12,500 feet" here means the whole cruise segment, not just part of it.

The aircraft's true airspeed (its speed through the air mass itself, before wind) and fuel-flow rate (gallons burned per hour at a given power setting) are fixed by its published performance figures and do not change with the altitude decision on their own (SEE APPENDIX B) — what changes the outcome is how the wind at each altitude combines, as a vector, with the aircraft's airspeed vector to produce the actual groundspeed the aircraft will fly. A higher groundspeed means less time in the air, and less time in the air means less fuel burned, for the exact same distance covered. Because the manufacturer does not publish a complete fuel-flow chart broken out by altitude, this case holds fuel-flow rate constant across both options as a stated, disclosed assumption (SEE APPENDIX E) rather than inventing a second, uncited number.

The dispatch release locks in four minutes, when the captain begins his pre-taxi checklist. After that, altitude cannot be changed without re-running the entire weight-and-balance and fuel package from scratch, which would blow the delivery window for tonight's cargo.

The vocabulary and the "how to…" skills this case will ask you to research are listed in **APPENDIX F** — that is where Challenge 1 sends you. Every sourced figure and stated assumption in this case is documented in **APPENDIX G**.

Renata picks up the headset.

---

## Dilemma

You are Renata Alvarez.

Do you:

**A.)** File **Niner-Thousand** — cruise at 9,000 feet, no supplemental oxygen required **OR**

**B.)** File **One-Eight-Thousand** — cruise at 18,000 feet, supplemental oxygen required for the whole flight

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A wind-triangle vector diagram** for each altitude option, drawn to scale on a labeled coordinate grid: the true-airspeed vector, the wind vector, and the resultant ground-velocity vector, each with its magnitude and direction (compass heading) labeled.
- **D2 — A wind-component table** for each altitude: the headwind/tailwind component and the crosswind component of the wind vector relative to the flight's true course, found using the dot product of the wind vector and the unit vector along the course, shown as work.
- **D3 — A groundspeed and heading table** for each altitude: the resultant groundspeed (magnitude of the resultant vector) and the wind-correction-angle heading the pilot must actually fly, with the right-triangle relationship you used to find each, shown as work.
- **D4 — A flight-time and fuel-burn table** for each altitude: the elapsed flight time computed from the route distance and your Challenge D3 groundspeed, and the total fuel burned for the flight, with every unit conversion shown step by step.
- **D5 — A gallons-per-nautical-mile comparison** for the two altitudes, using your Challenge D4 totals, stated alongside a one-paragraph note on how the Appendix D oxygen requirement factors into your recommendation even though it isn't part of the numeric ratio itself.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A — Route Geometry

| Quantity | Value |
|---|---|
| Departure airport | Denver Centennial Airport (KAPA), 39.57000° N, 104.84944° W [S3] |
| Destination airport | Wichita Dwight D. Eisenhower National Airport (KICT), 37.65000° N, 97.43306° W [S4] |
| Great-circle distance, KAPA to KICT | 366.4 nautical miles [S3, S4, derived] |
| True course, KAPA to KICT | 106.0° true (measured clockwise from true north) [S3, S4, derived] |

*Distance and true course are derived directly from the published coordinates above using the standard great-circle (spherical law of cosines / haversine) distance and initial-bearing formulas — not separately published anywhere, but a straightforward geometric calculation from two real, sourced coordinate pairs. Full arithmetic in `RESEARCH_LOG.md`.*

---

## Appendix B — Aircraft Performance: Cessna 208B Grand Caravan

| Quantity | Value |
|---|---|
| True airspeed at representative cruise power | 180 knots [S1] |
| Fuel flow at representative cruise power | 415 pounds per hour = 62.0 gallons per hour, Jet-A [S1] |
| Usable fuel capacity | 332 gallons [S1] |
| Certified service ceiling | 25,000 feet [S1] |

*"Representative cruise power" here means the single throttle/propeller setting (1,750 rpm) the manufacturer's own fact sheet uses as its standard example cruise condition — the setting a pilot would normally fly at, not a maximum or minimum. This case treats the 62.0 gallons-per-hour fuel-flow figure as constant across both altitude options considered in this case (SEE APPENDIX E, MA1) — a stated simplification, not a separately published per-altitude figure.*

---

## Appendix C — Winds Aloft

Real winds-aloft forecast (FD/FB product), Goodland, Kansas station (GLD) — chosen because it sits close to the KAPA–KICT route (SEE APPENDIX A). Reported as: wind direction the wind is blowing **from** (degrees true, nearest 10°), and wind speed in knots.

| Cruise altitude | Wind (from / speed) |
|---|---|
| 9,000 ft | 220° true / 27 knots [S2] |
| 18,000 ft | 230° true / 20 knots [S2] |

*This is a live forecast product: the government agency that publishes it recalculates and reissues a fresh version every six hours, the same way a weather app refreshes. **As of cutoff: this table reflects the forecast cycle fetched 2026-09-18. Every calculation in this case uses these two values and no others — treat them as the flight's actual forecast winds for the purposes of this case, the same way Renata would treat the forecast she pulled minutes before the release locked.** Source data and the decode method are in Appendix G / RESEARCH_LOG.md.*

---

## Appendix D — Regulatory Constraint: Supplemental Oxygen

> **14 CFR § 91.211(a)(2)** — no person may operate a civil aircraft at cabin pressure altitudes above 12,500 feet (MSL) up to and including 14,000 feet (MSL) unless the required minimum flight crew is provided with and uses supplemental oxygen for that part of the flight at those altitudes that is of more than 30 minutes duration; and **§ 91.211(a)(3)** — above 14,000 feet (MSL), the required minimum flight crew must be provided with and use supplemental oxygen during the entire flight time at those altitudes. [S5]

*"Cabin pressure altitude" is the altitude the air inside the cabin effectively feels like to a person breathing it — in a pressurized airliner it stays low even at high true altitude, but the Caravan's cabin is unpressurized, so its cabin pressure altitude simply equals the aircraft's actual altitude. A cruise segment at 18,000 feet is entirely above 14,000 feet, so this case treats Option B as requiring oxygen use for the whole cruise segment, and Option A (9,000 feet, below 12,500 feet) as requiring none.*

---

## Appendix E — Modeling Assumptions

> These figures are **not sourced** as direct external citations. They are stated scenario assumptions, each grounded in a real basis described below. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Fuel-flow rate is the same at 18,000 ft as at 9,000 ft | 62.0 gallons per hour, both altitudes | The manufacturer's full Pilot's Operating Handbook cruise-performance chart (which would list fuel flow by pressure altitude and power setting) is not available as a freely-fetchable primary document within the size this case's research could pull; the only clean, citable published figure found is AOPA's single representative cruise fuel-flow value [S1]. This case applies that one figure to both altitudes rather than inventing a second, uncited number for 18,000 ft. | This is a real simplification, not a free assumption — real turboprop engines commonly show some fuel-flow variation with altitude and power setting. Because the case's own numeric margin between the two options is quite thin, a Hero who argues that a real per-altitude fuel-flow difference could matter to the comparison is raising a legitimate, defensible point. |

*No other figure in this case required a Modeling Assumption — see `RESEARCH_LOG.md` for the full source-by-source trail.*

---

## Appendix F — "How To…" Math Questions To Research

**Vocabulary terms**

- Vector
- Magnitude (Of A Vector)
- Unit Vector
- Dot Product
- Pythagorean Theorem
- Hypotenuse

**"How to…" questions**

- How to find the magnitude and direction of a vector
- How to add and subtract vectors
- How to find the dot product of two vectors
- How to find elapsed time
- How to convert an amount with compound units

---

## Appendix G — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Cessna 208B Grand Caravan cruise performance | TAS 180 kn; fuel flow 415 lb/hr (62.0 gal/hr Jet-A); usable fuel 332 gal; service ceiling 25,000 ft | AOPA Aircraft Fact Sheet, "Cessna 208B Grand Caravan" ([link](https://www.aopa.org/go-fly/aircraft-and-ownership/aircraft-fact-sheets/cessna-208b-grand-caravan)) | accessed 2026-09-18 | HIGH |
| S2 | Winds aloft, Goodland KS (GLD) station | 9,000 ft: 220°/27 kt; 18,000 ft: 230°/20 kt | NOAA/FAA Aviation Weather Center, live Winds/Temps Aloft (FD) data API ([data](https://aviationweather.gov/api/data/windtemp?region=us&level=low&fcst=6&layout=off)) | fetched 2026-09-18 | HIGH |
| S3 | Denver Centennial Airport (KAPA) coordinates | 39.57000° N, 104.84944° W | Wikipedia, "Centennial Airport" (citing FAA Form 5010 airport data) ([link](https://en.wikipedia.org/wiki/Centennial_Airport)) | accessed 2026-09-18 | HIGH |
| S4 | Wichita Dwight D. Eisenhower National Airport (KICT) coordinates | 37.65000° N, 97.43306° W | Wikipedia, "Wichita Dwight D. Eisenhower National Airport" (citing FAA Form 5010 airport data) ([link](https://en.wikipedia.org/wiki/Wichita_Dwight_D._Eisenhower_National_Airport)) | accessed 2026-09-18 | HIGH |
| S5 | Supplemental oxygen requirement | 14 CFR § 91.211(a)(2)-(3) | Electronic Code of Federal Regulations (eCFR), Title 14, Part 91, §91.211 ([link](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-91/subpart-C/section-91.211)) | accessed 2026-09-18 | HIGH |

*Modeling Assumption MA1 is documented in Appendix E, not repeated here. Full search trail and derivation arithmetic: `RESEARCH_LOG.md`.*

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
