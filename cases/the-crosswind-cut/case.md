Case Study: Crosswind Cut
MS | Math | Case Study | 2026 | Launchpad

## Overview

The corridor advisory refreshes on Jordan Reyes's second monitor and the number in the crosswind
field does not move. Behind the glass, Drone 114 sits on its pad with its rotors folded, waiting on
a configuration Jordan has not yet locked in. The prelaunch checklist has one field still blank:
**motor/prop config.**

Two toolboxes are open on the bench. One holds the high-KV motors and the small, fast props —
the pair Jordan's team calls the sprint rig. The other holds the low-KV motors and the wide,
slow-turning props — the cruise rig. Once ground crew bolts one pair on, that is what Drone 114
flies today. There is no swapping mid-route.

Dispatch pings again: the FAA waiver that lets Swiftwing fly this corridor beyond visual line of
sight is conditioned on staying inside the mapped lateral boundary, published to the meter. Drift
outside it and the flight is a reportable violation, not just a bad delivery. Drop below the
mandatory battery reserve before touchdown and the drone is required to set down wherever it is,
waiver corridor or not.

Jordan pulls up both spec sheets side by side — thrust curves, current draw, the works — and
starts doing the arithmetic that neither toolbox label tells you: how much of each rig's thrust
budget actually points down the corridor once the wind gets paid first.

The cursor blinks over the checklist's empty configuration field.

## Background

Jordan Reyes is a flight-operations engineer at Swiftwing Regional Logistics, a last-mile drone
delivery operator. Jordan is the person on shift responsible for locking in each drone's
motor/propeller configuration before it launches, and for signing off that the choice keeps the
flight inside the operating limits Swiftwing's FAA beyond-visual-line-of-sight waiver requires.
Today's route runs Drone 114 down a mapped delivery corridor that a published crosswind advisory
crosses at close to a right angle to the direction of travel (SEE APPENDIX B).

Two configurations are available for this airframe, and both are drawn from the same
manufacturer's published multirotor propeller/motor performance data rather than a single
marketing number (SEE APPENDIX A):

**Configuration Sparrow** — the high-KV motor paired with the smaller-diameter propeller. It spins
faster and has more raw thrust on tap, at the cost of drawing more current for every pound of
thrust it produces.

**Configuration Albatross** — the low-KV motor paired with the larger-diameter propeller. In calm
air it produces more thrust for every amp the battery gives up, but it has a smaller margin of
surplus thrust left over once some of that thrust has to be spent holding the drone on course
against a crosswind.

Both configurations are bolted to the same airframe, carry the same payload, and fly the same
corridor at the same commanded groundspeed (SEE APPENDIX A) — so the two options differ in exactly
two things: how much total thrust each is capable of producing, and how much current it costs to
produce it.

Two hard constraints apply to either choice. First, the corridor's lateral boundary is fixed by
the waiver: the drone must hold its programmed heading down the corridor centerline, which means
whichever configuration flies today has to devote part of its thrust budget to cancelling the
crosswind's push off that heading before any thrust is "useful" (SEE APPENDIX B). Second,
Swiftwing's flight rules set a mandatory battery reserve that must remain in the pack at touchdown,
computed from the configuration's current draw over the route's flight time (SEE APPENDIX C).
Jordan has to check both configurations against that reserve rule before locking one in.

Where a figure in this case is not a matter of public record, it is stated as an explicit modeling
assumption (SEE APPENDIX D) rather than guessed, and every sourced figure is listed in
(SEE APPENDIX E). The vocabulary and the "how to…" skills this case will ask of you are listed in
**APPENDIX G** — that is where Challenge 1 sends you. Curious about drone delivery operations, KV
ratings, or beyond-visual-line-of-sight waivers beyond what the Dilemma requires? SEE APPENDIX F
for further reading.

## Dilemma

You are Jordan Reyes.
Do you:
A.) Bolt on **Configuration Sparrow** — the high-KV motor and small propeller OR
B.) Bolt on **Configuration Albatross** — the low-KV motor and large propeller

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A thrust-and-current table for each configuration, drawn from the manufacturer performance
    data in Appendix A: the total available thrust each configuration can produce at the throttle
    setting used for today's route, and the current draw at that same setting.
    D2. A crosswind-cancellation vector diagram for each configuration: the crosswind vector (SEE
    APPENDIX B), the delivery-heading unit vector, and the corrective thrust vector each
    configuration must supply to cancel the crosswind and hold the corridor centerline — with the
    full vector subtraction shown for at least one configuration.
    D3. A net forward-progress thrust table for each configuration: the dot product of that
    configuration's total available thrust vector with the delivery-heading unit vector, after the
    crosswind-cancellation component from D2 has been subtracted out — reported in the same units
    for both configurations.
    D4. A thrust-per-amp comparison table showing, for each configuration, (i) the manufacturer's
    advertised calm-air thrust-per-amp figure and (ii) the net-forward-progress-thrust-per-amp
    figure computed from D3, divided by the current draw from D1 — with your arithmetic shown for
    both rows, so the pitch can address whether the two rankings agree or disagree.
    D5. A battery-reserve check for each configuration: using the current draw from D1 and the
    reserve rule in Appendix C, the percentage of the mandatory reserve remaining in the pack at
    touchdown on today's route.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — The Two Configurations

Performance figures for both configurations are drawn from the same manufacturer's published
multirotor propeller/motor combination test data (T-Motor, `uav-en.tmotor.com/Multirotor/Propellers`),
which reports thrust, current draw, and RPM across a range of throttle settings for each
motor/propeller pairing, rather than a single headline number.

| | Configuration Sparrow (high-KV / small prop) | Configuration Albatross (low-KV / large prop) |
|---|---|---|
| Motor KV rating | 400 KV [S1] | 340 KV [S2] |
| Propeller diameter and pitch | 15 in × 5 in pitch (T-Motor P15×5 CF) [S1] | 18 in × 6.1 in pitch (T-Motor P18×6.1 CF) [S2] |
| RPM at the route's commanded throttle setting (90% throttle) | 7,180 rpm [S1] | 5,842 rpm [S2] |
| Thrust at that RPM (per motor, kgf) | 2.782 kgf (2,782 g) [S1] | 3.909 kgf (3,909 g) [S2] |
| Current draw at that RPM (per motor, A) | 20.60 A [S1] | 29.46 A [S2] |
| Advertised calm-air thrust-per-amp (g/A) | 238.3 g/A — derived: 672 g ÷ 2.82 A at T-Motor's lowest published throttle point (40%), the closest published stand-in for a headline "calm-air" efficiency figure [S1] | 264.9 g/A — derived: 996 g ÷ 3.76 A at 40% throttle [S2] |
| Number of motors on the airframe | 4 (quadcopter) — SEE APPENDIX D, MA3 | (same airframe) |
| Commanded groundspeed down the corridor | 33.5 mph — SEE APPENDIX D, MA4 | (same route) |

## Appendix B — Flight Corridor and Crosswind

The delivery corridor is a mapped, waiver-approved lateral boundary that Drone 114 must stay
inside for the length of today's route. The corridor's programmed heading and today's crosswind
advisory are given below.

| | Value |
|---|---|
| Delivery corridor heading (° from the crosswind's line of travel) | SEE APPENDIX D, MA2 |
| Crosswind speed | SEE APPENDIX D, MA1 |
| Route length down the corridor | 4 mi — SEE APPENDIX D, MA5 |

**How the wind is resolved.** The crosswind is treated as a single vector, constant along the
whole corridor, with a component perpendicular to the corridor heading (the part that pushes the
drone off centerline) and a component along the corridor heading (the part that helps or hurts
groundspeed directly). Cancelling the perpendicular component is what consumes part of each
configuration's thrust budget before any thrust counts as forward progress.

## Appendix C — Battery and Reserve Rule

| | Value |
|---|---|
| Battery pack capacity | 22,000 mAh (22 Ah), 6S — SEE APPENDIX D, MA6 |
| Mandatory reserve at touchdown | 25% of pack capacity — SEE APPENDIX D, MA7 |
| Nominal pack voltage | 22.2 V nominal (6S LiPo) [S1][S2] |

## Appendix D — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, each with a real basis named below. A Hero may challenge them in discussion — that is a
> legitimate move, and APPENDIX G names the skills a Hero would need to test one.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Crosswind speed for today's corridor, since no public source names a specific reading for a fictional corridor | 15 mph | No public source names a wind reading for a fictional delivery corridor. 15 mph is well below the National Weather Service's own threshold for issuing a Wind Advisory (sustained 31–39 mph) [S3], so it represents an ordinary, sub-advisory crosswind a regional UAS operator would manage routinely rather than an extreme event. It is also below the general "Level 6" wind-resistance benchmark (~27–31 mph) commonly cited across the small-UAS industry as a serviceable operating ceiling [S4]. | Common to both configurations (sets the wind-correction angle), so it does not change the ranking between the two configurations, only its magnitude. |
| MA2 | Angle between the corridor heading and the crosswind's line of travel | 80° | Chosen to make the crosswind's course-perpendicular component dominant (sin 80° ≈ 0.985 of the wind vector), consistent with the Background's description of the wind crossing "close to a right angle" — an oblique angle close to, but deliberately not exactly, 90°, so the figure reads as a modeled scenario angle rather than an engineered-looking round number. | Common to both configurations, so it does not change the ranking between them, only its magnitude. |
| MA3 | Number of motors on Drone 114's airframe | 4 (quadcopter) | No public airframe spec exists for the fictional Drone 114. Quadcopter is the most common multirotor layout for medium-lift regional last-mile delivery platforms in this thrust class (comparable in scale to real short-hop multirotor delivery services such as Flytrex [S6]). | Does not change the ranking between the two configurations — motor count scales both configurations' total thrust and total current identically, so it cancels out of the per-amp ratio. |
| MA4 | Drone 114's commanded cruise groundspeed | 33.5 mph (15 m/s) | No public speed spec exists for the fictional Drone 114. 33.5 mph matches the DJI FlyCart 30's published maximum automatic-flight cruising speed [S5] — the closest real, publicly specified cruise speed for a pure multirotor (non-fixed-wing) delivery drone, as opposed to the much faster VTOL fixed-wing-hybrid platforms (Zipline, Wing, Amazon Prime Air) whose wing-borne cruise physics do not apply to a rotor-only airframe like Drone 114's. | Does not flip the ranking between configurations — groundspeed sets the wind-correction angle, which is identical for both configurations and so cancels out of the per-amp ratio. It does affect the D5 reserve-check flight time. |
| MA5 | Length of today's delivery corridor | 4 mi | No public route spec exists for the fictional Swiftwing corridor. 4 mi matches Flytrex's published delivery radius for its Sky2 multirotor delivery drone [S6] — a comparable real short-hop, non-fixed-wing delivery operation, chosen over the much longer VTOL fixed-wing delivery ranges (Zipline, Wing, Amazon) for the same non-comparability reason as MA4, and consistent with the flight endurance the MN5008-class current draw and MA6's battery capacity actually support. | Feeds the D5 reserve check only; does not enter the D3/D4 per-amp comparison between configurations. |
| MA6 | Drone 114's battery pack capacity | 22,000 mAh (22 Ah), 6S | No public battery spec exists for the fictional Drone 114 — capacity is an airframe-level choice, not a motor spec, so T-Motor's own datasheets (Appendix A) do not name one. 22,000 mAh sits within the commonly available 16,000–24,000 mAh 6S range used with this thrust class of motor; T-Motor's own Antigravity MN-series line (including the MN5008 combos in Appendix A) is marketed toward agricultural/industrial multirotor platforms that typically carry packs in this range [S7]. | Feeds the D5 reserve check only; does not enter the D3/D4 per-amp comparison between configurations. |
| MA7 | Swiftwing's mandatory battery reserve at touchdown | 25% of pack capacity | No public reserve rule exists for the fictional Swiftwing. Modeled on manned aviation's VFR fuel-reserve principle — 14 CFR § 91.151 requires at least 30 minutes' additional fuel at normal cruising speed beyond the point of intended landing for day VFR flight [S8] — with Swiftwing adopting an analogous fixed-fraction battery-energy reserve. 25% falls within the 20–30% battery-reserve range commonly cited as small-UAS operating practice. | Feeds the D5 reserve check only; does not enter the D3/D4 per-amp comparison between configurations. |

## Appendix E — Sources

| id | Claim | Value | Source | Accessed | Confidence |
|---|---|---|---|---|---|
| S1 | MN5008 KV400 Antigravity motor + T-Motor P15×5" CF propeller combo performance data (KV, thrust, current, RPM by throttle) and rated voltage | KV400, 6S rated, see Appendix A table | T-Motor — [MN5008 KV400 Antigravity product/spec page](https://store.tmotor.com/product/mn5008-kv400-motor-antigravity-type.html) | 2026-08-30 | HIGH |
| S2 | MN5008 KV340 Antigravity motor + T-Motor P18×6.1" CF propeller combo performance data (KV, thrust, current, RPM by throttle) and rated voltage | KV340, 6S rated, see Appendix A table | T-Motor — [MN5008 KV340 Antigravity product/spec page](https://store.tmotor.com/product/mn5008-kv340-motor-antigravity-type.html) | 2026-08-30 | HIGH |
| S3 | NWS Wind Advisory issuance threshold | Sustained 31–39 mph, or gusts 46–57 mph | National Weather Service (Burlington, VT WFO) — [Watch/Warning/Advisory Threshold Reference](https://www.weather.gov/btv/wwa_reference) | 2026-08-30 | HIGH |
| S4 | General small-UAS "Level 6" wind-resistance industry benchmark | ~27–31 mph (12–14 m/s) | Drone-industry trade coverage (aggregated benchmark, not manufacturer-specific) — [Drone Wind Resistance Level Explained](https://www.jouav.com/blog/drone-wind-resistance-levels.html) | 2026-08-30 | MEDIUM |
| S5 | DJI FlyCart 30 maximum automatic-flight cruising speed | 15 m/s (33.5 mph); max manual-flight speed 20 m/s (44.7 mph) | DJI — [30 Things to Know About DJI FlyCart 30](https://enterprise-insights.dji.com/blog/30-things-to-know-about-dji-flycart30), cross-checked against [DJI FlyCart 30 official specs](https://www.dji.com/flycart-30/specs) | 2026-08-30 | HIGH |
| S6 | Flytrex Sky2 delivery-drone range | Up to 4 mi delivery radius | Trade press reporting Flytrex's published spec — [Flytrex Launches New Drone in North Texas](https://dallasinnovates.com/flytrex-launches-new-drone-in-north-texas-that-can-deliver-industry-leading-food-orders/) | 2026-08-30 | MEDIUM |
| S7 | Representative 6S agricultural/industrial multirotor battery pack capacity | 22,000 mAh, 6S | Commercial battery listing for agriculture-drone use — [Agriculture drone Battery and charger 22000mah 6S](https://robocraftstore.com/product/agriculture-drone-battery-and-charger-22000mah-6s/) | 2026-08-30 | MEDIUM |
| S8 | 14 CFR § 91.151 VFR day fuel-reserve requirement | 30 minutes' additional fuel at normal cruising speed beyond the point of intended landing (day VFR) | Cornell Law School, Legal Information Institute — [14 CFR § 91.151](https://www.law.cornell.edu/cfr/text/14/91.151) | 2026-08-30 | HIGH |

## Appendix F — Learn More

These are real, currently-live resources for a Hero who wants to go beyond what the Dilemma
requires — none of them is needed to complete a Challenge, and none is a source for a figure used
anywhere else in this case (those are listed separately in Appendix E).

- [KV rating (motors) — Wikipedia](https://en.wikipedia.org/wiki/Brushless_DC_electric_motor). An
  explanation of how a brushless motor's KV rating relates speed to voltage, and why a high-KV
  motor paired with a small propeller behaves differently from a low-KV motor on a large one.
- [Unmanned aerial vehicle — Wikipedia](https://en.wikipedia.org/wiki/Unmanned_aerial_vehicle).
  Background on multirotor drone platforms of the kind Drone 114 represents.
- [Federal Aviation Administration — Beyond Visual Line of Sight (BVLOS)](https://www.faa.gov/uas/advanced_operations/beyond_visual_line_of_sight_bvlos).
  The real regulatory framework behind the waiver referenced in the Background section above.
- [Dot product — Wikipedia](https://en.wikipedia.org/wiki/Dot_product). A fuller explanation of the
  operation behind D3's net-forward-progress-thrust calculation.
- [Vector (mathematics and physics) — Wikipedia](https://en.wikipedia.org/wiki/Euclidean_vector).
  Background on vector magnitude, direction, and components used throughout D2 and D3.

## Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Vector
- Magnitude (Of A Vector)
- Unit Vector
- Dot Product
- Variable

**"How to…" questions**

- How to find the magnitude and direction of a vector
- How to add and subtract vectors
- How to find the dot product of two vectors
- How to find the percent of a number

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
