Case Study: The Phasing Call
MS | Math | Case Study | 2026 | Adventure

## Overview

Talia Brooks has the tracking readout up on the left monitor and the launch calendar up on the
right, and the cursor has been parked on the same cell for six minutes.

Meridian Launch Systems' mission control room is quiet this late — just the low hum of the
environmental system and, somewhere down the hall, a printer finishing a long job. Talia is the
trajectory analyst who signs the rendezvous profile that goes into the flight plan, and right now
there are two profiles, not one. The first plan on her left monitor is short and steep: launch,
climb, and close on the client's station same day. The second plan, on the right, is patient:
launch into a lower parking orbit and let the vehicle spend days catching up, orbit by orbit,
before it ever gets close.

Her phone buzzes, face down on the console. The launch site's weather office, probably, with
tomorrow's hold forecast. She doesn't pick it up yet. She already knows roughly what it will say,
because she asked for exactly this number when she asked for the callback.

What she doesn't know yet, not with numbers she'd sign her name to, is which profile actually
leaves the vehicle in better shape to dock — not just which one gets there faster, but which one
leaves enough reserve, and enough room in the calendar, if tomorrow's launch slips. The short
profile is unforgiving about exactly when it can lift off. The patient profile is forgiving about
the launch day — but every extra orbit spent catching up eats into the same fixed reserve the short
profile barely touches.

Talia pulls the readout and the calendar onto one screen and reaches for her calculator.

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
APPENDICES B and D) — a real, documented engineering constraint on short rendezvous profiles [S1].

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
| Cargo vehicle / launch provider | Meridian's cargo vehicle, modeled on Northrop Grumman's **Cygnus** cargo spacecraft, a real, currently-operating LEO cargo resupply vehicle flown to the ISS (most recently NG-19, August 2023) [S5] |
| Client station's orbital altitude (measured above Earth's surface) | ≈ 400–420 km — the ISS's own real orbit (413 km perigee / 422 km apogee as of the most recent published statistics) [S9] |
| Client station's tracked position at the moment of the rendezvous-profile decision, as reported by ground tracking radar | Bearing 48°, range 210 km from the tracking site (MA1, SEE APPENDIX E) |
| Contracted docking deadline | 96 hours (4 days) after launch (MA2, SEE APPENDIX E) |
| Minimum required autonomous-flight/consumables reserve remaining at docking | 15% of total allowance (MA3, SEE APPENDIX E) |

*Meridian Launch Systems is a scenario construction for this case — there is no real company by
this name. The rendezvous-profile timing figures in Appendix B, however, are anchored to real,
named, operationally-flown spacecraft rendezvous profiles (SEE APPENDIX F).*

## Appendix B — Rendezvous Profile Orbital Elements

Figures below describe each profile's real operational precedent and the modeled orbital elements
this case derives from it.

| Element | Option A — The Fast-Track | Option B — The Phasing Climb |
|---|---|---|
| Real operational precedent | Soyuz's operational **4-orbit, ~6-hour** rendezvous profile, flown since 2013 [S2]; an even faster **2-orbit, ~3-hour "ultrafast"** variant has been flown since 2020 (Soyuz MS-17) [S3] | The classic **34-orbit, ~2-day** Soyuz rendezvous profile flown before 2013 [S4]; still the live, current-day profile for Northrop Grumman's **Cygnus** cargo vehicle (NG-19, August 2023, ≈2.4–2.5 days launch to berthing) [S5] |
| Parking-orbit altitude (below the client station) | 220 km (mean of a 202 × 240 km injection orbit) — this case's real Soyuz-precedent parking/injection orbit [S10] | Same, 220 km — real precedent shows both profiles insert into essentially the same low parking orbit; they differ in how many orbits they let run, not in this altitude [S10] |
| Parking-orbit period (derived from altitude via Kepler's third law) | 88.62 min (the real, measured period of this orbit) [S10] | 88.62 min (same orbit) [S10] |
| Vehicle's angular catch-up rate relative to the station (derived from the two orbital periods) | ≈ 0.187°/min (≈ 11.2°/hour), from 360°×(1/88.62 − 1/92.9) using the station's real period [S9, S10] | ≈ 0.187°/min (≈ 11.2°/hour) — same rate; same underlying orbits (SEE APPENDIX E, MA4) |
| Modeled total transit time, parking orbit to docking | 6 hours [S2] | 2.5 days (60 hours) [S5] |

*Both profiles begin at Appendix A's tracked station position (converted to rectangular in D1) and
are modeled as a constant angular catch-up rate over elapsed time — D3 asks you to verify each
profile's actual closing time directly from its own rectangular equation rather than take it on
faith. Treating each profile's real, multi-burn catch-up sequence as a single constant angular
rate is a stated simplification (MA4, SEE APPENDIX E), not a literal description of every
individual burn — the underlying wait-time/lead-angle relationship this simplification draws on
is real, published orbital-mechanics math [S6].*

## Appendix C — Autonomous-Flight and Consumables Budget Figures

The vehicle's total autonomous-flight/consumables allowance is drawn from the named vehicle's own
real operational limit [S7, S10]. Each profile's reserve remaining at docking is derived
from Appendix B's own modeled transit time against this fixed total allowance — the arithmetic is
yours to show in D4; the source record documents the same computation.

| Quantity | Value |
|---|---|
| Vehicle's total autonomous-flight/consumables allowance (real operational limit) | 4.2 days (100.8 hours) — Soyuz's own published calculated autonomous-flight life (2.2 days rendezvous/docking + 2.0 days undocking/pre-landing reserve) [S10] |
| Reserve remaining at docking, Option A — the Fast-Track | 100.8 − 6 = 94.8 hours remaining (94.0% of total allowance) — arithmetic shown; yours to reproduce in D4 |
| Reserve remaining at docking, Option B — the Phasing Climb | 100.8 − 60 = 40.8 hours remaining (40.5% of total allowance) — arithmetic shown; yours to reproduce in D4 |

## Appendix D — Launch-Window Phase-Angle Reference

Figures below describe how the initial phase angle between the vehicle's launch site and the
client station, at the moment of liftoff, constrains which calendar days a launch can be
attempted under each rendezvous profile.

| Quantity | Value |
|---|---|
| Client station's orbital period | 92.9 minutes — the ISS's own real, published orbital period [S9] |
| Phase angle at liftoff, full possible range | 0° to 360° — the chaser's initial phase (Ф₀), defined as the angle between the chaser's and the station's radius-vectors at the moment of orbital insertion, may be of any value in this range [S8, S10] |
| Phase-angle tolerance band, Option A — the Fast-Track (the narrow band within which a few-orbit rendezvous closes cleanly) | ≈ 30° initial phase angle [S11] |
| Phase-angle tolerance band, Option B — the Phasing Climb (the wide band a multi-orbit phasing rendezvous can absorb) | ≈ 270° initial phase angle [S11] — *see the note under S10/S11 in Appendix F: a real, primary Soyuz operations manual states the classic profile's initial phase "may be of any value," a wider (~360°) claim than the 270° figure used here; both real sources are cited and the discrepancy is disclosed rather than smoothed over.* |
| Days per 30-day launch calendar falling inside each option's phase-angle tolerance band | Derived in D6 from your D5 graphed tolerance bands and the station's orbital period |

## Appendix E — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, each with a real basis named. A Hero may challenge them in discussion — that is a
> legitimate move, APPENDIX G names the skills a Hero would need to test one.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Client station's tracked bearing and range at the moment of the decision | Bearing 48°, range 210 km | No real, named LEO client station of the kind described exists under contract with a company like Meridian; the bearing/range figures are a stated scenario tracking readout, chosen to sit a plausible distance ahead of the vehicle's real parking orbit and to give a non-trivial D1 conversion. | Changes the D1 rectangular coordinate and therefore the specific D3 elapsed-time answer for both profiles equally; does not change which profile wins the D6/D7 ratio, since both profiles close on the same tracked position and the ratio is driven by Appendix B/C/D's real figures, not this one. |
| MA2 | Contracted docking deadline | 96 hours (4 days) after launch | No public contract exists for the fictional Meridian Launch Systems. Anchored directly to Soyuz's real published 4.2-day (100.8-hour) total autonomous-flight allowance (Appendix C, S10): the stated deadline is set at 96 hours, a few hours inside that real hardware limit, the way a real mission-assurance contract would build in slack rather than target the hardware ceiling exactly. | Both profiles' modeled transit times (6 hours and 60 hours) sit well inside 96 hours, so neither option is disqualified by the deadline alone — the binding constraints are the reserve floor (MA3) and the D7 ratio, not this deadline. Only a deadline tightened below ~60 hours would start to threaten the Phasing Climb's flyability. |
| MA3 | Minimum required autonomous-flight/consumables reserve remaining at docking | 15% of total allowance | No public contract term of this kind is published for a real commercial LEO resupply mission; 15% is a stated scenario contingency fraction, chosen in line with typical aerospace mission-assurance contingency-margin conventions, and disclosed as an assumption rather than a sourced figure. | Both profiles clear this floor by a wide margin under this case's real, sourced transit-time figures (Fast-Track ≈ 94% reserve, Phasing Climb ≈ 40% reserve) — this assumption would have to rise above ~40% before it could disqualify the Phasing Climb outright, well above any published contingency convention found during research. |
| MA4 | Each rendezvous profile is modeled as a single constant angular catch-up rate over its full transit, rather than as its real multi-burn sequence | Constant rate, derived from each profile's two orbital periods | Both real profiles this case is modeled on fly a short sequence of discrete burns (an initial phasing burn, one or more correction burns, then final approach), not one continuous rate. Modeling each as a single constant-rate parametric arc is a stated simplification appropriate to this case's Pre-Calculus/Polar-and-Parametric skill target. | Does not affect the D4/D5/D6 reserve-and-flexibility comparison, which is driven by each profile's real, sourced total transit time, not by how that transit time is broken into individual burns. Only affects the D2/D3 algebra, which models one arc instead of several. |

## Appendix F — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | The seminal engineering paper behind the operational short/fast rendezvous profile, establishing that a short phasing strategy requires a precise initial phase angle and recommending it as a combination between direct and two-day rendezvous missions | Confirmed real via ScienceDirect, NASA ADS, and ResearchGate abstracts; frames the short-rendezvous strategy as needing a precisely-constrained initial phase angle. Full text is paywalled — no page-specific numeric figure from this paper is used directly in this case's tables; its role here is establishing the real engineering basis for the Fast-Track/Phasing-Climb trade-off, corroborated numerically by S11 below. | Murtazin, R.F. & Budylov, S.G., "Short rendezvous missions for advanced Russian human spacecraft," *Acta Astronautica* 67 (2010), pp. 900–909 | 2010 | HIGH |
| S2 | Modern operational 4-orbit, ~6-hour Soyuz rendezvous profile, flown since 2013 | "Since 2012, docking of 28 Russian vehicles (18 of them Soyuz crew vehicles) has been accomplished using the 6-hour and 4-orbit rendezvous profile"; a specific flight (Soyuz TMA-13M) is documented completing this 4-orbit profile. NASA's own original "Soyuz Orbital Insertion to Docking Timeline" page (`nasa.gov/mission_pages/station/structure/elements/soyuz/timeline_orbit.html`) could not be reached live at research time (HTTP 404) — Universe Today's coverage is used as the working citation instead. | Universe Today — "Next Soyuz Crew Will Take 6-Hour Fast-Track to Space Station" (`universetoday.com/100536/`) | 2015-12-23 | HIGH |
| S3 | 2-orbit, ~3-hour "ultrafast" Soyuz rendezvous profile, first flown October 2020 (Soyuz MS-17) | "Soyuz MS-17 caught up with the orbiting laboratory in only two orbits (three hours)... docked with the ISS's Rassvet module" — launched 05:45:04 UTC, docked 08:48 UTC, 14 Oct 2020 (3 hr 3 min, a Guinness World Record for fastest crewed trip to the ISS). A later flight (April 2021) was expected to take ~3.5 hours under the same 2-orbit scheme (TASS, quoting RSC Energia ballistics lead Rafail Murtazin). | NASASpaceFlight.com — "Soyuz MS-17 completes 3 hour journey to ISS" (`nasaspaceflight.com/2020/10/soyuz-ms17-ultrafast-journey-to-iss/`) | 2020-10-14 | HIGH |
| S4 | Classic ~2-day (34-orbit) Soyuz rendezvous profile, the standard profile flown before 2013 | "Soyuz (and Progress) fly a standard 34-orbit (2-day) timeline template from launch through docking" — the pre-2013 baseline profile, superseded by (but still available as a fallback to) the faster profiles in S2/S3. 88.62-minute real orbital period × 34 orbits ≈ 50.2 hours ≈ 2.09 days, consistent with the "2-day" figure. | SpaceRef — "The standard Soyuz launch-and-ascent template" (`spaceref.com/status-report/the-standard-soyuz-launch-and-ascent-template/`); corroborated by AmericaSpace's reporting on Soyuz TMA-12M's 2014 two-day rendezvous | undated (SpaceRef); 2014-03-27 (AmericaSpace) | HIGH |
| S5 | Real, currently-flown multi-orbit phasing profile, ~2 to 2.5 days, Northrop Grumman's Cygnus cargo vehicle to the ISS (most recently NG-19, August 2023) | Launch 2 Aug 2023, 00:31:14 UTC. RMS capture 4 Aug 2023, 09:52 UTC (≈2.39 days / 57.4 hours elapsed). Berthing 4 Aug 2023, 12:28 UTC (≈2.50 days / 59.9 hours elapsed). This case models the Phasing Climb's total transit time as 2.5 days (60 hours), using the berthing figure as the "docking" analog. | Space.com — "Cygnus space freighter arrives at space station..."; Wikipedia — "Cygnus NG-19" (cross-checked against both) | 2023-08-04 | HIGH |
| S6 | Phase-angle-dependent phasing-orbit rendezvous duration, and the underlying wait-time/lead-angle/phase-angle relationship | Confirmed live and readable at research time. States the lead-angle relationship α = ω_target × TOF_interceptor, final phase angle φ_f = π − α, and wait time t_wait = (φ_f − φ_i)/(ω_target − ω_interceptor). Worked Example 1 solves a rescue scenario with an interceptor 135° behind the target (φ_i = 135°), computing a lead angle ≈ 80.6° and final phase angle ≈ 99.4° — a real, numeric worked example of exactly this case's underlying phasing math, at a large (135°) initial phase angle, supporting that the Phasing Climb's much wider tolerance band is mathematically well-precedented. | L. George, "Chapter 8 — Rendezvous," *Introduction to Orbital Mechanics* (OER Pressbooks, `oer.pressbooks.pub/lynnanegeorge/chapter/chapter-8-ground-tracks-and-rendezvous/`) | accessed 2026-08-31 | HIGH |
| S7 | Real, named spacecraft's published total autonomous-flight/consumables duration limit, cited as the operational reason the fast rendezvous profile was pursued | "The Soyuz spacecraft can fly autonomously in orbit for only about four days total... the faster rendezvous frees up more fuel, oxygen and other supplies for possible use in an emergency." This qualitative rationale is corroborated with an exact figure (4.2 days) by the primary source S10 below. | Space.com — "Soyuz 'Fast Track': How 1-Day Space Station Trips Work" (Karl Tate) | 2013-05-28 | MEDIUM |
| S8 | Phase angle between an arriving spacecraft and a station under rendezvous ranges from 0° to 360° on a given day, and the time required to reach the station depends on that phase angle | Confirmed by primary source: "The phase (Ф) is defined as the angle between the spacecraft radius-vector and the station radius-vector... The initial phase Ф₀ at the moment of the spacecraft injection may be of any value." This resolved what the original concept sheet flagged as an unconfirmed reference — the actual source is the Soyuz crew manual (S10), not a separate textbook. | Soyuz Crew Operations Manual (SoyCOM), Section 8.2.1 — SEE S10 for full citation | 1999 (manual date); accessed 2026-08-31 | HIGH |
| S9 | International Space Station's real orbital altitude and orbital period, used as this case's client-station orbit | "Perigee: 413 km... Apogee: 422 km... Orbital Period: 92.9 minutes," listed under "Station statistics," current as of 22 December 2022 unless noted otherwise. | Wikipedia — "International Space Station" (`en.wikipedia.org/wiki/International_Space_Station`) | as of 2022-12-22; accessed 2026-08-31 | MEDIUM |
| S10 | Soyuz spacecraft's real published total autonomous-flight/consumables limit, and its real parking/injection orbit altitude and period — this case's anchor for Appendix B/C's fixed budget and orbital elements | Primary NASA-numbered crew operations manual (doc. no. NAS15-10110, "0004AE4b (ROP-19)"). Table 8-1: injection orbit period 88.62 min (±22 s), apogee 240 km (+43/−42 km), perigee 202 km (+7/−23 km) — mean ≈ 220 km. Section 3: "the spacecraft calculated autonomous flight life is 4.2 days. This time period includes rendezvous/docking operations (2.2 days) and undocking, pre-landing operations and time reserve (2 days)." Section 8.2.1 additionally states the classic two-day (34-orbit) profile's initial phase is chosen "within 240 − 30 degrees" to minimize propellant, though the phase itself "may be of any value" — see the disclosed discrepancy against S11's 270° figure, noted in Appendix D. | Soyuz Crew Operations Manual (SoyCOM), hosted at `planet4589.org/space/articles/pao/CrewManual1999.pdf` (Jonathan McDowell's spaceflight document archive) | 1999; accessed 2026-08-31 | HIGH |
| S11 | Phase-angle tolerance figures specifically distinguishing the fast rendezvous profile from the classic two-day profile — the exact numeric figure this case's D5/D6/D7 chain depends on | "An orbital insertion for Soyuz and Progress spacecraft... within the desired fast rendezvous parameter of 30 degrees initial phase angle, is possible," based on "a Russian document describing the new rendezvous profile, which was seen by NASASpaceflight.com" (unnamed original document/author). By contrast, "the traditional two-day method tolerates a much larger 270-degree phase angle." This is the most authoritative numeric phase-angle-tolerance figure located after a genuine, multi-query research attempt (see RESEARCH_LOG.md) — graded MEDIUM because the underlying Russian document is described but not named or independently produced. | NASASpaceFlight.com — "Progress M-16M succesfully tests new fast rendezvous with ISS" (byline Pete Harding) | 2012-08-01; accessed 2026-08-31 | MEDIUM |

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
