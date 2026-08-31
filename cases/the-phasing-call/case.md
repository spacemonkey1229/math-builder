Case Study: The Phasing Call
MS | Math | Case Study | 2026 | Adventure

## Overview

Talia Brooks has the tracking readout up on the left monitor and the launch calendar up on the
right, and the cursor has been parked on the same cell for six minutes.

Meridian Launch Systems' mission control room is quiet this late — just the low hum of the
environmental system and, somewhere down the hall, a printer finishing a long job. Talia is the
trajectory analyst who signs the rendezvous profile that goes into the flight plan, and right now
there are two profiles, not one. The first plan on her left monitor is short and steep: launch,
climb, and close on the client's station in a matter of hours, same day. The second plan, on the
right, is patient: launch into a lower parking orbit and let the vehicle spend days catching up,
orbit by orbit, before it ever gets close.

Her phone buzzes, face down on the console. The launch site's weather office, probably, with
tomorrow's hold forecast. She doesn't pick it up yet. She already knows roughly what it will say,
because she asked for exactly this number when she asked for the callback.

What she doesn't know yet, not with numbers she'd sign her name to, is which profile actually
leaves the vehicle in better shape to dock — not just which one gets there faster, but which one
leaves enough reserve, and enough room in the calendar, if tomorrow's launch slips by even a day.
The short profile is unforgiving about exactly when it can lift off. The patient profile is
forgiving about the launch day — but every extra orbit it spends catching up is an orbit spent
eating into the same fixed reserve the short profile barely touches.

Talia pulls the tracking readout and the launch calendar onto one screen, opens a blank sheet
between them, and reaches for her calculator.

## Background

Talia Brooks is the trajectory analyst at Meridian Launch Systems, a small commercial launch
company under contract to fly a cargo vehicle to a client's space station in low Earth orbit. She
is responsible for recommending the rendezvous profile the mission flies once the vehicle reaches
its initial parking orbit — and once she signs off, that profile is what gets written into the
flight plan and the launch-day procedures (SEE APPENDIX A).

Two rendezvous profiles are on the table for this mission, and both start from a parking orbit
below the client's station and are aimed at the same docking port (SEE APPENDIX A).

**The Fast-Track.** A direct, few-orbit rendezvous profile: the vehicle closes on the station in
a small number of orbits, same day, using a rapid sequence of catch-up burns. Reaching the
station quickly leaves the largest possible share of the vehicle's fixed onboard
autonomous-flight/consumables allowance untouched at docking — but the profile only closes cleanly
if the vehicle reaches its parking orbit within a narrow band of initial phase angle relative to
the station, which in turn narrows which calendar days a launch can actually be attempted (SEE
APPENDICES B and D).

**The Phasing Climb.** A multi-orbit parking-orbit phasing rendezvous profile: the vehicle spends
many more orbits — days, not hours — gradually catching up to the station's position before
beginning final approach. Because the vehicle can absorb a much wider range of initial phase
angle by simply flying more or fewer phasing orbits, far more calendar days become viable launch
attempts — but every extra day spent phasing is a day drawn against the same fixed
autonomous-flight/consumables allowance, leaving less reserve at docking (SEE APPENDICES B, C
and D).

The client's station-keeping contract fixes a hard docking deadline and requires the vehicle to
retain a minimum reserve of its autonomous-flight/consumables allowance at the moment of docking,
for contingencies such as a failed first approach (SEE APPENDIX A) — either profile must satisfy
both limits to be flyable at all. Meridian's vehicle has a fixed total autonomous-flight/
consumables allowance regardless of which profile is flown; only how much of it is spent reaching
the station changes between the two profiles (SEE APPENDIX C). Where a figure below is not a
matter of public record, it is stated as an explicit modeling assumption (SEE APPENDIX E) rather
than guessed, and every sourced figure is listed in APPENDIX F. The vocabulary and "how to…"
skills this case asks you to research are listed in **APPENDIX G** — where Challenge 1 sends you.

## Dilemma

You are Talia Brooks.
Do you:
A.) Recommend **the Fast-Track** — the direct, few-orbit rendezvous profile that reaches the
station fastest and preserves the most autonomous-flight/consumables reserve OR
B.) Recommend **the Phasing Climb** — the multi-orbit parking-orbit phasing profile that tolerates
the widest range of launch-day phase angles

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A conversion of the client station's tracked position (Appendix A) from the polar
    coordinate its tracking radar reports — a bearing and range from the tracking site — into a
    rectangular coordinate, with your conversion work shown in full.
    D2. A pair of parametric position equations, x(t) and y(t), for each rendezvous profile (the
    Fast-Track and the Phasing Climb), using each profile's stated angular catch-up rate from
    Appendix B, with the parameter identified by name and explained in plain terms (what it
    represents physically, and what values it ranges over for each profile's full rendezvous).
    D3. For each profile, the rectangular (Cartesian) equation of the vehicle's closing path,
    found by eliminating the parameter from that profile's D2 equations, showing every algebraic
    step — followed by a solved check, using that rectangular equation, of the elapsed time at
    which each profile actually reaches the station's D1 rectangular position, with your algebra
    shown in full.
    D4. An autonomous-flight/consumables-reserve calculation for each profile: what percent of
    Appendix C's fixed total allowance is used up by the time each profile reaches docking (using
    your D3 elapsed-transit-time figures), and what percent remains as reserve.
    D5. A graphed polar boundary for each profile's phase-angle tolerance band (Appendix D): using
    the 0°-360° phase-angle circle centered on the moment of liftoff, graph each profile's
    workable phase-angle band as a polar equation, stating that equation explicitly, so the two
    bands' relative widths are visible on a single polar plot.
    D6. A launch-window calendar calculation for each profile: using your D5 graphed phase-angle
    bands and the station's orbital period from Appendix D, how many days in a 30-day launch
    calendar fall inside each profile's workable phase-angle window, with your arithmetic shown.
    D7. A single primary-metric comparison table — hours of reserve margin remaining at docking
    (from D4) per calendar day of launch-window flexibility (from D6) — built for both profiles,
    with the division shown for each.
    D8. A recommendation to Meridian's launch director, defended using your D7 result, stating
    plainly what would have to change about either profile for your recommendation to flip.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — Mission Parameters and Contract Constraints

| Quantity | Value |
|---|---|
| Cargo vehicle / launch provider | Meridian's cargo vehicle, modeled on {{NEEDS_SOURCE: a real, named, currently-operating LEO cargo resupply vehicle used as this case's modeling anchor, e.g. Cygnus or Cargo Dragon}} |
| Client station's orbital altitude (measured above Earth's surface) | {{NEEDS_SOURCE: a real, named LEO station or ISS-analog altitude, km}} |
| Client station's tracked position at the moment of the rendezvous-profile decision, as reported by ground tracking radar | Bearing {{NEEDS_SOURCE: a stated scenario bearing, degrees}}, range {{NEEDS_SOURCE: a stated scenario range, km}} from the tracking site (MA1, SEE APPENDIX E) |
| Contracted docking deadline | {{NEEDS_SOURCE: a stated scenario contract deadline, hours or days after launch}} (MA2, SEE APPENDIX E) |
| Minimum required autonomous-flight/consumables reserve remaining at docking | {{NEEDS_SOURCE: a stated scenario minimum reserve, percent of total allowance}} (MA3, SEE APPENDIX E) |

*Meridian Launch Systems is a scenario construction for this case — there is no real company by
this name. The rendezvous-profile timing figures in Appendix B, however, are anchored to real,
named, operationally-flown spacecraft rendezvous profiles (SEE APPENDIX F).*

## Appendix B — Rendezvous Profile Orbital Elements

Figures below describe each profile's real operational precedent and the modeled orbital elements
this case derives from it.

| Element | Option A — The Fast-Track | Option B — The Phasing Climb |
|---|---|---|
| Real operational precedent | {{NEEDS_SOURCE: a real, named, currently- or recently-flown few-orbit fast rendezvous profile, with its orbit count and total transit time}} | {{NEEDS_SOURCE: a real, named, currently- or recently-flown multi-orbit phasing rendezvous profile, with its orbit count and total transit time}} |
| Parking-orbit altitude (below the client station) | {{NEEDS_SOURCE: a stated scenario parking-orbit altitude, km}} | {{NEEDS_SOURCE: same or a lower stated scenario parking-orbit altitude, km}} |
| Parking-orbit period (derived from altitude via Kepler's third law) | {{NEEDS_SOURCE: derived, minutes}} | {{NEEDS_SOURCE: derived, minutes}} |
| Vehicle's angular catch-up rate relative to the station (derived from the two orbital periods) | {{NEEDS_SOURCE: derived, degrees per minute}} | {{NEEDS_SOURCE: derived, degrees per minute}} |
| Modeled total transit time, parking orbit to docking | {{NEEDS_SOURCE: modeled from the real precedent above, hours}} | {{NEEDS_SOURCE: modeled from the real precedent above, days}} |

*Both profiles begin at Appendix A's tracked station position (converted to rectangular in D1) and
are modeled as a constant angular catch-up rate over elapsed time — D3 asks you to verify each
profile's actual closing time directly from its own rectangular equation rather than take it on
faith. Treating each profile's real, multi-burn catch-up sequence as a single constant angular
rate is a stated simplification (MA4, SEE APPENDIX E), not a literal description of every
individual burn.*

## Appendix C — Autonomous-Flight and Consumables Budget Figures

The vehicle's total autonomous-flight/consumables allowance is drawn from the named vehicle's own
real operational limit (SEE APPENDIX F). Each profile's reserve remaining at docking is derived
from Appendix B's own modeled transit time against this fixed total allowance — the arithmetic is
yours to show in D4; the source record documents the same computation.

| Quantity | Value |
|---|---|
| Vehicle's total autonomous-flight/consumables allowance (real operational limit) | {{NEEDS_SOURCE: a real, named spacecraft's published total autonomous-flight duration limit, days or hours}} |
| Reserve remaining at docking, Option A — the Fast-Track | {{NEEDS_SOURCE: derived from Appendix B's modeled transit time}} |
| Reserve remaining at docking, Option B — the Phasing Climb | {{NEEDS_SOURCE: derived from Appendix B's modeled transit time}} |

## Appendix D — Launch-Window Phase-Angle Reference

Figures below describe how the initial phase angle between the vehicle's launch site and the
client station, at the moment of liftoff, constrains which calendar days a launch can be
attempted under each rendezvous profile.

| Quantity | Value |
|---|---|
| Client station's orbital period | {{NEEDS_SOURCE: derived from Appendix A's altitude, minutes}} |
| Phase angle at liftoff, full possible range | 0° to 360° [S — a real, named orbital-mechanics reference documenting this range for ISS-class rendezvous, SEE APPENDIX F] |
| Phase-angle tolerance band, Option A — the Fast-Track (the narrow band within which a few-orbit rendezvous closes cleanly) | {{NEEDS_SOURCE: a real, named source's stated or derivable phase-angle tolerance for a fast/few-orbit rendezvous profile, degrees}} |
| Phase-angle tolerance band, Option B — the Phasing Climb (the wide band a multi-orbit phasing rendezvous can absorb) | {{NEEDS_SOURCE: a real, named source's stated or derivable phase-angle tolerance for a multi-orbit phasing rendezvous profile, degrees}} |
| Days per 30-day launch calendar falling inside each option's phase-angle tolerance band | Derived in D6 from your D5 graphed tolerance bands and the station's orbital period |

## Appendix E — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, each with a real basis named. A Hero may challenge them in discussion — that is a
> legitimate move, APPENDIX G names the skills a Hero would need to test one.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Client station's tracked bearing and range at the moment of the decision | {{NEEDS_SOURCE: stated scenario values}} | No real, named LEO client station of the kind described exists under contract with a company like Meridian; the bearing/range figures are a stated scenario tracking readout, chosen to sit a plausible distance ahead of the vehicle's real parking orbit. | Changes the D1 rectangular coordinate and therefore the specific D3 elapsed-time answer for both profiles equally; does not change which profile wins the D6 ratio, since both profiles close on the same tracked position. |
| MA2 | Contracted docking deadline | {{NEEDS_SOURCE: stated scenario value}} | No public contract exists for the fictional Meridian Launch Systems. Anchored to real commercial LEO resupply precedent (SEE APPENDIX F) so both profiles have real, plausible headroom to be flyable at all. | Sensitivity to be confirmed once Appendix B's real transit-time figures are sourced. |
| MA3 | Minimum required autonomous-flight/consumables reserve remaining at docking | {{NEEDS_SOURCE: stated scenario value}} | No public contract term of this kind is published for a real commercial LEO resupply mission; anchored to the real, named vehicle's own total allowance (Appendix C) so the stated minimum sits at a plausible fraction of that real total. | Sensitivity to be confirmed once Appendix C's real total-allowance figure is sourced. |
| MA4 | Each rendezvous profile is modeled as a single constant angular catch-up rate over its full transit, rather than as its real multi-burn sequence | Constant rate, derived from each profile's two orbital periods | Both real profiles this case is modeled on fly a short sequence of discrete burns (an initial phasing burn, one or more correction burns, then final approach), not one continuous rate. Modeling each as a single constant-rate parametric arc is a stated simplification appropriate to this case's Pre-Calculus/Polar-and-Parametric skill target. | Does not affect the D4/D5/D6 reserve-and-flexibility comparison, which is driven by each profile's real, sourced total transit time, not by how that transit time is broken into individual burns. Only affects the D2/D3 algebra, which models one arc instead of several. |

## Appendix F — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | The seminal engineering paper behind the operational short/fast rendezvous profile, establishing that a short phasing strategy requires a precise initial phase angle and recommending it as a combination between direct and two-day rendezvous missions | {{NEEDS_SOURCE: exact page range and any numeric figures to be pulled directly from the paper at case-research time}} | Murtazin, R.F. & Budylov, S.G., "Short rendezvous missions for advanced Russian human spacecraft," *Acta Astronautica* 67 (2010), pp. 900–909 | 2010 | HIGH |
| S2 | Modern operational 4-orbit, ~6-hour Soyuz rendezvous profile, flown since 2013 | {{NEEDS_SOURCE: exact figures}} | NASA — "Soyuz Orbital Insertion to Docking Timeline" | {{NEEDS_SOURCE: access date}} | HIGH |
| S3 | 2-orbit, ~3-hour "ultrafast" Soyuz rendezvous profile, first flown October 2020 (Soyuz MS-17) | {{NEEDS_SOURCE: exact figures}} | NASASpaceFlight.com — reporting on Soyuz MS-17's ultrafast rendezvous | 2020-10 | HIGH |
| S4 | Classic ~2-day (34-orbit) Soyuz rendezvous profile, the standard profile flown before 2013 | {{NEEDS_SOURCE: exact figures}} | Space.com — "Soyuz 'Fast Track': How 1-Day Space Station Trips Work"; CBS News/Spaceflight Now archived reporting, "Soyuz on track for revised two-day station rendezvous" | {{NEEDS_SOURCE: access dates}} | HIGH |
| S5 | Real, currently-flown multi-orbit phasing profile, ~2 to 2.5 days, Northrop Grumman's Cygnus cargo vehicle to the ISS (most recently NG-19, August 2023) | {{NEEDS_SOURCE: exact figures}} | NASASpaceFlight.com and AmericaSpace — reporting on Cygnus NG-19's rendezvous timeline | 2023-08 | HIGH |
| S6 | Phase-angle-dependent phasing-orbit rendezvous duration, and the underlying wait-time/lead-angle/phase-angle relationship | {{NEEDS_SOURCE: exact equations and any stated day-range figures}} | L. George, "Chapter 8 — Rendezvous," *Introduction to Orbital Mechanics* (OER Pressbooks) | {{NEEDS_SOURCE: access date}} | HIGH |
| S7 | Real, named spacecraft's published total autonomous-flight/consumables duration limit, cited as the operational reason the fast rendezvous profile was pursued | {{NEEDS_SOURCE: exact figure and vehicle}} | Space.com — "Soyuz 'Fast Track': How 1-Day Space Station Trips Work" | {{NEEDS_SOURCE: access date}} | MEDIUM |
| S8 | Phase angle between an arriving spacecraft and a station under rendezvous ranges from 0° to 360° on a given day, and the time required to reach the station depends on that phase angle | {{NEEDS_SOURCE: exact source document and any stated day-range figures}} | {{NEEDS_SOURCE: a real, named orbital-mechanics reference to be confirmed at case-research time}} | {{NEEDS_SOURCE: access date}} | MEDIUM |

## Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Polar Coordinate
- Parametric Equation
- Parameter
- Percent

**"How to…" questions**

- How to convert a point between rectangular and polar coordinates
- How to graph a polar equation
- How to eliminate the parameter to find a rectangular equation
- How to find the percent of a number
- How to convert an amount with compound units

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
