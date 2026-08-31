Case Study: The Transfer Window
MS | Math | Case Study | 2026 | Adventure

## Overview

Talia Brooks has two trajectory files open side by side, and the cursor has been sitting on the
same blinking line for eleven minutes.

Meridian Launch Systems' mission control room is quiet this late — just the low hum of the
environmental system and, somewhere down the hall, someone's keyboard going in short bursts. Talia
is the trajectory analyst who signs the transfer-orbit design that goes into the customer's
contract, and right now there are two designs, not one. The first plot on her left monitor climbs
steeply and gets there fast — a hard, direct burn that puts the payload on orbit in days, if the
propellant budget holds. The second plot, on the right, drifts out in a long, patient spiral that
sips propellant instead of gulping it — and takes weeks longer to arrive.

Her inbox has a message from the payload customer's program manager, still unread, subject line
starting with "RE: delivery date —". She hasn't opened it. She already knows roughly what it says,
because she asked for exactly this kind of pressure when she requested the meeting that produced
it.

What she doesn't know yet, not with numbers she'd sign her name to, is which trajectory actually
delivers more usable payload for every day the customer has to wait. The steep burn eats into the
mass budget before the payload ever separates from the kick stage. The long drift protects that
mass — but every extra day in transit is a day the payload spends soaking in the belts.

Talia pulls both plots onto one screen, opens a blank sheet between them, and reaches for her
calculator.

## Background

Talia Brooks is the trajectory analyst at Meridian Launch Systems, a small commercial launch
company that flies rideshare payloads to geostationary orbit using an expendable kick stage. She
is responsible for recommending the transfer-orbit design that the mission uses once the payload
separates from the launch vehicle's upper stage in low Earth parking orbit — and once she signs
off, that design is what gets written into the customer's delivery contract (SEE APPENDIX A).

Two kick-stage trajectory designs are on the table for this mission, and both start from the same
parking orbit and are aimed at the same target geostationary orbit radius (SEE APPENDIX A).

**The Direct Burn.** A high-thrust, direct parametric transfer trajectory: the kick stage's
chemical engine fires hard early in the transfer, putting the payload on an aggressive, shorter-
period transfer ellipse that reaches the target orbit radius in far less time. That thrust isn't
free — a higher fraction of the kick stage's total launch mass has to be propellant, which is mass
that does not get delivered as payload (SEE APPENDICES B and C).

**The Patient Drift.** A low-thrust, extended-coast parametric transfer trajectory: the kick
stage's electric propulsion system fires gently over a much longer transfer, tracing a larger,
longer-period transfer ellipse to the same target orbit radius. Because electric propulsion is far
more propellant-efficient than the chemical burn, a smaller fraction of launch mass has to be
propellant, and more of it survives as deliverable payload — but the payload spends far more days
in transit, and a meaningful share of that transit crosses Earth's Van Allen radiation belts (SEE
APPENDICES B and D).

The payload customer's contract fixes a maximum acceptable delivery window and a maximum
acceptable cumulative radiation dose the payload's electronics are rated to survive in transit
(SEE APPENDIX A) — either option must fall inside both limits to be flyable at all. Meridian's
kick stage has a fixed total wet mass and a fixed dry (structure-plus-engine) mass regardless of
which trajectory is flown; only the propellant load and the resulting deliverable payload mass
change between the two designs (SEE APPENDIX C). Where a figure below is not a matter of public
record, it is stated as an explicit modeling assumption (SEE APPENDIX E) rather than guessed, and
every sourced figure is listed in APPENDIX F. The vocabulary and "how to…" skills this case asks
you to research are listed in **APPENDIX G** — where Challenge 1 sends you.

## Dilemma

You are Talia Brooks.
Do you:
A.) Recommend **the Direct Burn** — the high-thrust, direct parametric transfer trajectory that
reaches the target orbit fastest OR
B.) Recommend **the Patient Drift** — the low-thrust, extended-coast parametric transfer
trajectory that preserves the most deliverable payload mass

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A pair of parametric position equations, x(E) and y(E), for each trajectory option (the
    Direct Burn and the Patient Drift), using each option's stated semi-major axis and
    eccentricity from Appendix B, with the parameter identified by name and explained in plain
    terms (what it represents physically, and what values it ranges over for one full transfer).
    D2. For each option, the rectangular (Cartesian) equation of the trajectory's path, found by
    eliminating the parameter from that option's D1 equations, showing every algebraic step —
    followed by a solved check, using that rectangular equation, of the point where each
    trajectory actually reaches Appendix A's target orbit radius, with your algebra shown in full.
    D3. A propellant-mass-fraction and deliverable-payload-mass calculation for each option, using
    the kick stage's fixed total wet mass and dry mass and each option's stated propellant load
    from Appendix C, with every percent calculated shown as arithmetic, not just stated as a
    result.
    D4. A single primary-metric comparison table — kilograms of deliverable payload per day of
    transit time, for both options — built from your D2 transit-time figures and your D3
    deliverable-payload-mass figures, with the division shown for each option.
    D5. A cumulative radiation-dose estimate for each option's payload, using Appendix D's
    dose-rate reference and each option's own transit time (from D2) and belt-crossing duration,
    with your unit conversions shown explicitly and both results compared against Appendix A's
    stated payload radiation tolerance limit.
    D6. A recommendation to the payload customer, defended using your D4 and D5 results, stating
    plainly what would have to change about the transfer design for your recommendation to flip.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — Mission Parameters and Contract Constraints

| Quantity | Value |
|---|---|
| Launch vehicle / kick stage | Meridian's kick stage, modeled on Firefly Aerospace's Sherpa orbital transfer vehicle line (the chemical-bipropellant **Sherpa-LTC** and electric-propulsion **Sherpa-LTE** variants) [S1] |
| Parking orbit radius (measured from Earth's center) | 6,878 km (500 km altitude [S2][S3] + Earth's equatorial radius, 6,378 km [S5]) |
| Target orbit radius (geostationary, measured from Earth's center) | 42,164 km (35,786 km altitude [S4] + Earth's equatorial radius, 6,378 km [S5]) |
| Customer's maximum acceptable delivery window | 240 days (MA1, SEE APPENDIX E) |
| Payload's rated cumulative radiation-dose tolerance | 20,000 rad (20 krad-Si) [S10] |

*Meridian Launch Systems is a scenario construction for this case — there is no real company by
this name. The parking-orbit and target-orbit radii, however, are real orbital-mechanics
constants, and the kick stage named above is a real, currently-offered product whose own published
mission profile anchors this case's mass and delta-v figures (SEE APPENDIX C).*

## Appendix B — Trajectory Orbital Elements

Figures below describe each option's transfer ellipse — the path the kick stage actually flies
between the parking orbit and the target orbit. NASA JPL's Trajectory Browser and Horizons system
(SEE APPENDIX G) models interplanetary trajectories between solar-system bodies and does not
produce Earth-centric parking-orbit-to-GEO transfer figures, so it is **not** the source of the
numbers below. Instead, the Direct Burn's semi-major axis, eccentricity, delta-v, and idealized
transit time are computed directly from Appendix A's real parking-orbit and target-orbit radii and
Earth's real gravitational parameter, using the standard two-body Hohmann-transfer equations [S6]
[S12]. Each option's specific impulse and (for the Patient Drift) delta-v come from the named
kick stage's real published engine specifications [S3][S7].

| Element | Option A — The Direct Burn | Option B — The Patient Drift |
|---|---|---|
| Propulsion type | Chemical bipropellant, high thrust | Electric (Hall-effect), low thrust |
| Transfer-ellipse semi-major axis (km) | 24,521 km [S12] | 24,521 km (MA2, SEE APPENDIX E) |
| Transfer-ellipse eccentricity | 0.7195 [S12] | 0.7195 (MA2, SEE APPENDIX E) |
| Delta-v budget for this transfer (km/s) | 3.82 km/s [S12] | 6.0 km/s [S3] |
| Propulsion specific impulse, Isp (s) | 290 s [S7] | 1,400 s [S3] |
| Modeled total transit time (days) | 0.221 days (5.3 hr) [S12] | 180 days (MA3, SEE APPENDIX E) |

*Both trajectories begin at Appendix A's parking-orbit radius and are designed to reach Appendix
A's target orbit radius at transfer-ellipse apoapsis — D2 asks you to verify this directly from
each option's own rectangular equation rather than take it on faith. Because both options start
and end at the same two real orbital radii, the two-body transfer ellipse connecting those radii
is geometrically identical for both (same semi-major axis and eccentricity, [S12]) — what differs
between the Direct Burn and the Patient Drift is not the shape of the ellipse but how it is flown:
a near-instantaneous chemical burn versus a continuous low-thrust spiral. A real continuous
low-thrust transfer does not actually trace a single Keplerian ellipse at all; treating the Patient
Drift as flying this same ellipse, only far more slowly, is a stated simplification (MA2, SEE
APPENDIX E), not a literal description of low-thrust orbital dynamics.*

## Appendix C — Propellant and Payload Mass Figures

The kick stage's total wet mass is drawn from the named vehicle's own published specifications
(SEE APPENDIX G). No public dry-mass figure exists for a single bus flying both a chemical and an
electric mode at this delta-v/Isp combination, so dry mass is a stated Modeling Assumption
(MA4, SEE APPENDIX E). Each option's propellant mass is derived from Appendix B's own sourced
delta-v and Isp figures against the sourced wet mass, using the rocket equation — the arithmetic
is yours to show in D3; the source record documents the same computation.

| Quantity | Option A — The Direct Burn | Option B — The Patient Drift |
|---|---|---|
| Kick stage total wet mass (kg) | 180 kg [S2] | *(same vehicle — see Option A column)* |
| Kick stage dry mass (kg) | 30 kg (MA4, SEE APPENDIX E) | *(same vehicle — see Option A column)* |
| Propellant mass required for this transfer (kg) | 133.0 kg [S13] | 63.7 kg [S13] |

## Appendix D — Van Allen Belt Radiation Dose Reference

Figures below describe the radiation environment a GEO-transfer payload passes through while
crossing Earth's Van Allen radiation belts. No single, dated, primary dose-rate figure could be
sourced for this exact scenario — real published values ranged from roughly 200 to 3,700 rad per
year depending on shielding thickness and orbital region, a genuinely shielding-dependent figure
rather than one settled number — so the dose rate below is a stated Modeling Assumption (MA5, SEE
APPENDIX E). The belt-crossing fractions are derived from real, published Van Allen belt altitude
ranges [S11] measured against Appendix A's own real parking-orbit and target-orbit radii.

| Quantity | Value |
|---|---|
| Average cumulative radiation dose rate while actively crossing the belts (rad per day) | 50 rad/day (MA5, SEE APPENDIX E) |
| Fraction of the Direct Burn's total transit time spent actively crossing the belts | 48% [S14] |
| Fraction of the Patient Drift's total transit time spent actively crossing the belts | 48% [S14] |

## Appendix E — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, each with a real basis named. A Hero may challenge them in discussion — that is a
> legitimate move, APPENDIX G names the skills a Hero would need to test one.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Payload customer's maximum acceptable delivery window | 240 days | No public contract exists for the fictional Meridian Launch Systems. Anchored to real commercial precedent: satellite operators today routinely accept ~6-month (180-day) all-electric GTO-to-GEO transfers [S8], so 240 days gives both options real, plausible headroom above the Patient Drift's own modeled 180-day transit. | Below 180 days, the Patient Drift becomes contractually unflyable outright regardless of the kg/day metric. Above roughly 200 days it never binds either option. |
| MA2 | Both options are modeled using the same geometric transfer ellipse | a = 24,521 km, e = 0.7195 for both | Both options genuinely start at the same real parking-orbit radius and are targeted to reach the same real GEO radius at apoapsis — the two-body ellipse connecting two fixed radii is geometrically unique. A real low-thrust electric transfer does not actually trace one Keplerian ellipse; modeling the Patient Drift as flying this same ellipse very slowly is a stated simplification. | Does not affect the D3/D4/D5 mass-and-time economics, which are driven by delta-v, Isp, and transit time, not ellipse shape. Only affects the D1/D2 algebra, which becomes the same curve for both options under this assumption. |
| MA3 | Patient Drift's modeled total transit time | 180 days | Anchored to real commercial ~6-month all-electric GTO-GEO transfers [S8] and to a real peer-reviewed finding that electric orbit-raising transits can run up to 200 days [S9]. | The single most consequential assumption in the case. Halving it would roughly double the Patient Drift's kg/day figure — but even doubling it would not close the ~160x gap to the Direct Burn's kg/day figure. |
| MA4 | Kick stage dry (structure + engine + avionics) mass, fixed across both propulsion modes | 30 kg | No public figure exists for a single bus flying both a chemical and an electric mode at this delta-v/Isp combination — the real vehicles this case is modeled on are, in reality, separately-massed vehicles. 30 kg is roughly 17% of the sourced 180 kg wet mass, a plausible structure-plus-avionics-plus-engine fraction for a small orbital transfer vehicle. | Major lever. At dry mass ≥ 47.0 kg, the Direct Burn's deliverable payload mass drops to zero or negative (infeasible). Below that, raising dry mass shrinks both options' payload roughly linearly, narrowing but not closing the kg/day gap. |
| MA5 | Average radiation dose rate while actively within Van Allen belt-radius territory | 50 rad/day | No single dated, primary, apples-to-apples dose-rate figure could be found for this scenario. Real published figures for related contexts ranged roughly 200–3,700 rad/year depending on shielding and orbital region — a genuinely shielding-dependent figure, not one settled number. 50 rad/day is a stated round mid-range value. | Patient Drift's cumulative dose scales directly with this rate: at 50 rad/day it totals about 4,320 rad (well under the 20,000 rad tolerance); at roughly 5x this rate (~250 rad/day) it would approach the tolerance ceiling and could flip the radiation check from pass to fail without changing the kg/day comparison. |

## Appendix F — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Kick stage product line is real and currently offered | Sherpa-LTC / Sherpa-LTE (Firefly Aerospace, ex-Spaceflight Inc.) | SpaceNews — [Firefly Aerospace acquires Spaceflight Inc.](https://spacenews.com/firefly-aerospace-acquires-spaceflight-inc/) | 2023-06 | HIGH |
| S2 | Sherpa-LTC wet mass and parking orbit | 180 kg; 500 km SSO | Gunter's Space Page — [Sherpa-LTC 1, 2](https://space.skyrocket.de/doc_sdat/sherpa-ltc.htm) | 2022 | MEDIUM |
| S3 | Sherpa-LTE Isp, delta-v, and parking orbit | up to 1,400 s Isp; over 6 km/s delta-v; 500 km SSO | Gunter's Space Page — [Sherpa-LTE](https://space.skyrocket.de/doc_sdat/sherpa-lte.htm) | 2022 | MEDIUM |
| S4 | Geostationary orbit altitude | 35,786 km | NASA Earthdata — [Orbits](https://www.earthdata.nasa.gov/learn/earth-observation-data-basics/orbits) | 2026 | HIGH |
| S5 | Earth's equatorial radius (WGS-84) | 6,378.137 km | Wikipedia — [Earth radius](https://en.wikipedia.org/wiki/Earth_radius) | 2026 | MEDIUM |
| S6 | Earth's standard gravitational parameter | 398,600.4418 km³/s² | NASA JPL NAIF — [geophysical.ker](https://naif.jpl.nasa.gov/pub/naif/pds/wgc/test/geophysical.ker) | 2026 | HIGH |
| S7 | Ocelot bipropellant engine (Sherpa-LTC's chemical engine) Isp | 290 s | Benchmark Space Systems — [Qualification Testing of a High-Performance 22N Bipropellant Thruster](https://www.benchmarkspacesystems.com/news/qualification-testing-22n-thruster) | 2024-07-01 | HIGH |
| S8 | Commercial all-electric GTO-GEO transfer duration precedent | ~6 months | eoPortal — [All-Electric](https://www.eoportal.org/other-space-activities/all-electric) | 2026 | MEDIUM |
| S9 | Electric orbit-raising transit time and its documented radiation-exposure risk | up to 200 days | Royal Astronomical Society, reporting Lozinski et al. 2019, *Space Weather*, DOI 10.1029/2019SW002213 — [Space weather causes years of radiation damage to satellites using electric propulsion](https://ras.ac.uk/news-and-press/news/space-weather-causes-years-radiation-damage-satellites-using-electric) | 2019 | HIGH |
| S10 | Commercial smallsat bus total-ionizing-dose radiation tolerance | 20,000 rad (20 krad-Si) | NanoAvionics — [M6P nano-satellite bus radiation tolerance](https://nanoavionics.com/blog/all-of-the-m6p-nano-satellite-bus-subsystems-proved-to-be-radiation-tolerant-to-20krad-after-the-successful-tests/) | 2018-08-28 | MEDIUM |
| S11 | Van Allen belt altitude ranges | inner belt 6,000–12,000 km; outer belt 25,000–45,000 km | ESA — [Earth's plasmasphere and the Van Allen belts](https://sci.esa.int/web/cluster/-/52831-earth-plasmasphere-and-the-van-allen-belts) | 2026 | HIGH |
| S12 | Direct Burn semi-major axis, eccentricity, delta-v, and idealized transit time (derived) | a=24,521 km; e=0.7195; Δv=3.82 km/s; t=0.221 days | Computed from S4–S6 via the standard Hohmann-transfer equations | 2026-08-31 | HIGH |
| S13 | Propellant mass for each option (derived) | Direct Burn 133.0 kg; Patient Drift 63.7 kg | Computed via the rocket equation from Appendix B's delta-v/Isp and Appendix C's wet mass | 2026-08-31 | HIGH |
| S14 | Belt-crossing fraction of the LEO–GEO radial climb (derived) | 48% | Computed from S11's belt altitudes against Appendix A's real radii | 2026-08-31 | MEDIUM |

## Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Parametric Equation
- Parameter
- Percent

**"How to…" questions**

- How to eliminate the parameter to find a rectangular equation
- How to find the percent of a number
- How to divide decimal numbers
- How to convert an amount with compound units

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
