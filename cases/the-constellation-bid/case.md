# Case Study: Constellation Bid

MS | Math | Case Study | 2026-27 | Launchpad

---

## Overview

Aisha Odom has two spreadsheets open and one launch-slot deposit deadline blinking at the top of her inbox. Solara Orbital's board wants her recommendation in writing by tomorrow morning, and the deposit — nonrefundable — is due the same day she has to send it.

Sixty satellites. Six target orbital planes, sixty degrees apart around the equator, each one needed to close a gap in Solara's coverage map before a competitor files for the same radio spectrum. One path puts all sixty on a single rocket, into a single plane, and lets each satellite burn its own propellant afterward to walk itself around to its assigned plane. The other path books six smaller rockets, one aimed straight at each target plane, so every satellite arrives already exactly where it needs to be.

She pulls up the propellant budget her propulsion lead signed off on last month — a number that looked generous on a slide deck and considerably less generous now that she's staring at how far some of these satellites will actually have to travel. Her cursor sits over the sine key on her calculator. Behind her, the office is empty; everyone else left for the night two hours ago.

Aisha bookmarks the launch-cost quote in one tab, the propulsion budget in the other, and starts working the angles.

---

## Background

Aisha Odom is the constellation architect at Solara Orbital, a small-satellite operator, and she owns the launch-strategy recommendation the board will vote on this week. Solara's sixty-satellite constellation is designed as a Walker-style pattern: six orbital planes, evenly spaced sixty degrees apart in right ascension of ascending node (RAAN — the angle that fixes where a satellite's orbital plane crosses the equator), with ten satellites assigned to each plane.

Two paths are open to her:

**Consolidated Launch** — book one large rocket, carry all sixty satellites to orbit together in a single "seed" plane, and let each satellite that isn't already in its assigned plane spend its own onboard propellant on a plane-change burn to walk itself over (SEE APPENDICES B, C and D).

**Distributed Launch** — book six smaller, dedicated rockets, one flown directly into each of the six target planes, so every satellite is delivered already correctly placed and no satellite ever needs to change planes after launch (SEE APPENDIX E).

Every satellite's assigned position starts as an angle — how far its target plane sits around the equator from wherever it's actually delivered — and Solara's ground-station network reads a satellite's real-time position in orbit the same way: as an angle, whose sine, cosine, and tangent are exactly what a satellite-tracking analyst computes from the unit circle (SEE APPENDIX A). The Consolidated Launch's plane-change burns are expensive in direct proportion to how large that angle is — a small angle costs little propellant, a large one can cost more propellant than a satellite can carry. Each of Solara's satellites has a fixed, board-approved propellant allowance set aside for this kind of maneuver; a satellite that cannot complete its assigned plane change within that allowance never reaches its target plane at all, and does not count toward Solara's finished, deployed constellation (SEE APPENDIX D).

None of the figures in this case describing Solara, Aisha, or this specific sixty-satellite mission are invented outright — every real-world figure is either cited to a real, live source or stated openly as a scenario assumption, with the basis for each assumption disclosed in **APPENDIX F**.

The vocabulary and "how to…" skills this case will ask you to research are listed in **APPENDIX G** — that is where Challenge 1 sends you. Every sourced figure and stated assumption in this case is documented in **APPENDIX H**. If any real-world term in this case (not the math vocabulary) is unfamiliar, **APPENDIX I** explains it in plain English.

She starts working the angles.

---

## Dilemma

You are Aisha Odom.

Do you:

**A.)** Recommend the Consolidated Launch — one rocket, one seed plane, every off-plane satellite walks itself over on its own propellant **OR**

**B.)** Recommend the Distributed Launch — six dedicated rockets, one per target plane, every satellite delivered already correctly placed

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A unit-circle trig table.** For each of the six target planes (Appendix B), find the minimum angular separation from the seed plane, convert that angle to radians, and use the unit circle to find the sine, cosine, and tangent of both the full separation angle and half the separation angle. Show the unit-circle coordinates you used.
- **D2 — An arc-length table.** Using Solara's orbital circumference (Appendix A) and each group's minimum angular separation from D1, find how many kilometers each group of satellites would have to travel around the orbit's own circle to reach its target plane, if it moved along the orbit itself rather than changing planes directly.
- **D3 — A delta-v and propellant feasibility table.** Using the combined plane-change formula in Appendix C and the sine values from D1, compute the velocity change (delta-v) each group's plane-change burn requires. Then, using Appendix D's thruster and mass figures, compute the propellant mass each group's burn would actually cost, and compare it against Appendix D's stated per-satellite propellant allowance. Mark each of the six groups FEASIBLE or NOT FEASIBLE.
- **D4 — A cost-and-coverage decision memo.** Using D3's feasibility results, compute how many of Solara's sixty satellites the Consolidated Launch actually delivers to their correct target plane, and its total launch cost (Appendix E). Compute the Distributed Launch's total launch cost and correctly-placed count. Compute each option's satellites-correctly-placed-per-dollar, state your recommendation, and show the arithmetic.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A — Solara's Orbit and the Unit Circle

Solara's constellation flies at a 550 km circular altitude — the same altitude SpaceX's own first operational Starlink shell was approved to fly at by the U.S. Federal Communications Commission [S1], a real, representative altitude for a modern low-Earth-orbit small-satellite constellation.

| Quantity | Value |
|---|---|
| Orbital altitude | 550 km [MA1, grounded in S1] |
| Earth's mean radius | 6,371 km (standard reference value) |
| Orbital radius (altitude + Earth radius) | 6,921 km |
| Earth's standard gravitational parameter (μ) — a fixed physical constant relating orbital radius to orbital speed | 398,600.4418 km³/s² (standard reference value) |

A satellite's position within its orbital plane, and one orbital plane's position relative to another, is described the same way any angle on a unit circle is described: as a rotation, whose horizontal and vertical coordinates on a circle of radius 1 are exactly the angle's cosine and sine. A ground-station analyst tracking one of Solara's satellites as it rises over the horizon reads its elevation angle the same way — using the tangent of the angle between the satellite's line of sight and the ground. Challenges D1–D3 ask you to use the unit circle to find the sine, cosine, and tangent of the angles this case's plane-change geometry actually produces.

*Orbital speed — the constant speed a satellite in this circular orbit travels at — is found from the vis-viva relationship for a circular orbit, v = √(μ ÷ r), using the radius and gravitational parameter above; the orbital circumference used in Challenge D2 is 2πr. Both are given here so you can verify your own D1–D2 arithmetic:*

| Derived quantity | Value |
|---|---|
| Orbital speed (v) | 7,589.0 m/s |
| Orbital circumference (2πr) | 43,486.5 km |

---

## Appendix B — Solara's Six Target Planes

Solara's sixty satellites launch toward a single "seed" plane and are assigned, ten each, to six target planes evenly spaced 60° apart in RAAN around the equator.

| Target plane | RAAN offset from the seed plane | Satellites assigned |
|---|---|---|
| Plane 0 (the seed plane itself) | 0° | 10 |
| Plane 1 | 60° | 10 |
| Plane 2 | 120° | 10 |
| Plane 3 | 180° | 10 |
| Plane 4 | 240° | 10 |
| Plane 5 | 300° | 10 |

*A plane-change burn can always be flown the shorter way around the circle, so the burn a Plane 4 or Plane 5 satellite actually needs is sized to the smaller of the stated offset and 360° minus that offset — not the full stated number. Challenge D1 asks you to find that minimum angular separation for all six planes before doing anything else with it.*

---

## Appendix C — The Plane-Change Maneuver

Changing which orbital plane a satellite flies in — without changing its altitude or speed — costs a single burn whose required velocity change (delta-v, written Δv, engineers' standard measure of "how big" a maneuver is) depends only on the satellite's orbital speed and the angle between its current plane and its target plane. For two planes crossing at an angle Δθ, the required delta-v for a single combined-maneuver burn is:

**Δv = 2 × v × sin(Δθ ÷ 2)**

where v is the satellite's orbital speed (Appendix A) [S2]. This is the standard, real combined-plane-change formula used throughout astrodynamics for a single-burn plane rotation; this case applies it to Solara's RAAN-change "walk" as the case's own stated simplification of that same geometry (MA2 — SEE APPENDIX F). Note what this formula implies on its own, before any propellant math: because sin grows with the angle, a 180° plane change costs a full 2v of delta-v — twice the satellite's entire orbital speed — while a small angle costs comparatively little. Challenge D3 asks you to compute Δv for each of Appendix B's six groups using the minimum angular separations you found in D1.

---

## Appendix D — Thruster, Propellant, and the Walk Budget

Solara's satellites fly a Busek BIT-3 RF ion thruster — "RF" (radio-frequency) refers to how it energizes its propellant; "ion thruster" means it produces thrust electrically. For this case's math, it is fully described by its specific impulse (Isp) below — a real, flight-proven small-satellite propulsion system [S3].

| Quantity | Value |
|---|---|
| Specific impulse (Isp), rated maximum — a standard measure of how efficiently a thruster turns propellant into thrust; higher means more push per kilogram spent | 2,150 s [S3] |
| Standard gravity (g₀) — a fixed physical constant used to convert Isp into a velocity | 9.80665 m/s² |
| Satellite wet mass — mass including whatever propellant is still on board | 15.0 kg [MA3] |
| Per-satellite propellant allowance reserved for the post-launch plane-change walk | 4.0 kg [MA4] |

*Propellant cost per unit of delta-v is found from Isp and wet mass the same way Challenge 1's "how to convert an amount with compound units" resource explains: exhaust velocity = Isp × g₀, and (for this case's linear approximation) propellant mass required ≈ Δv × (wet mass ÷ exhaust velocity). Challenge D3 asks you to apply this to each of Appendix B's six groups and compare the result against the 4.0 kg allowance above. A group whose required propellant exceeds 4.0 kg is NOT FEASIBLE — those satellites remain in the seed plane and do not count as correctly placed in Challenge D4.*

---

## Appendix E — Launch Costs

**Consolidated Launch.** All sixty satellites launch together on a single rideshare-class rocket. SpaceX's published Falcon 9 Transporter rideshare pricing to sun-synchronous orbit, as of February 2026, is a flat $350,000 covering the first 50 kg, plus $7,000 for every kilogram beyond that [S4].

**Distributed Launch.** Each of the six target planes is served by its own dedicated Rocket Lab Electron launch. Electron's published list price is $7.5 million per dedicated launch, for up to 300 kg to low Earth orbit [S5] — comfortably more than the 150 kg (ten satellites) any one Electron launch in this case would carry.

| Quantity | Value |
|---|---|
| Satellite wet mass (Appendix D) | 15.0 kg |
| Total constellation mass (60 satellites) | 900.0 kg |
| Consolidated Launch: rideshare base price, first 50 kg | $350,000 [S4] |
| Consolidated Launch: rideshare price, per kg beyond 50 kg | $7,000/kg [S4] |
| Distributed Launch: list price per dedicated Electron launch (up to 300 kg) | $7,500,000 [S5] |
| Distributed Launch: number of dedicated launches required (one per target plane) | 6 |

*Challenge D4 asks you to total the Consolidated Launch's rideshare cost across the full 900 kg constellation, total the Distributed Launch's cost across all six dedicated launches, and divide each option's correctly-placed-satellite count (Challenge D3) by its total cost.*

---

## Appendix F — Modeling Assumptions

> These figures are **not sourced** as direct external citations. They are stated scenario assumptions, each grounded in a real basis described below. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Solara's constellation altitude | 550 km | Solara is a fictional operator, so no real altitude filing exists for it specifically. 550 km matches the real altitude the FCC approved for SpaceX's first operational Starlink shell [S1] — a real, representative modern small-satellite constellation altitude, not an arbitrary number. | Altitude sets orbital speed (Appendix A), which scales every Δv in Challenge D3 directly. A materially higher or lower altitude would change which of the six groups are feasible. |
| MA2 | Modeling a RAAN (plane) change using the single-burn combined plane-change formula (Appendix C) | Δv = 2 × v × sin(Δθ/2) | This is the real, standard formula for a single-burn plane rotation at fixed altitude and speed [S2]. Real operational RAAN changes are usually achieved differently in practice — over weeks or months, using the natural drift caused by Earth's oblateness (J2 perturbation) rather than one large burn — but that slow-drift approach has no simple closed-form angle-to-cost relationship suitable for this case's math and would not exercise unit-circle trigonometry at all. This case adopts the standard single-burn formula as its own stated simplification of the real geometry. | This choice does not change *which* angle is cheapest or most expensive to reach — sin(Δθ/2) still grows with Δθ under either model — but it does change the exact propellant numbers in Challenge D3, and therefore which groups clear the 4.0 kg allowance in Appendix D. |
| MA3 | Satellite wet mass | 15.0 kg | Consistent with the mass class the BIT-3 thruster is actually designed and flight-qualified for — the manufacturer's own published reference platform is a 14 kg 6U CubeSat [S3]; Solara's satellite is stated as a slightly heavier 6U-class bus to accommodate the larger propellant allowance in MA4. | Every propellant figure in Challenge D3 scales directly and linearly with this value. |
| MA4 | Per-satellite propellant allowance reserved for the post-launch plane-change walk | 4.0 kg | Not publicly reported for any real satellite bus, since Solara is fictional — this is the case's own stated engineering-budget scenario, set aggressively high (about 27% of wet mass) specifically so the walk is genuinely possible for at least the smallest required angle, testing whether it remains possible for larger ones. | **This is the single most dilemma-relevant assumption in the case.** It is the exact line the feasibility check in Challenge D3 is measured against; a larger allowance lets more of the six groups succeed, a smaller one lets fewer. The case's correctly-placed count for Option A, and therefore its whole primary metric, is directly sensitive to this value. |

*No other figure in this case required a Modeling Assumption — see `RESEARCH_LOG.md` for the full source-by-source trail.*

---

## Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Unit Circle
- Tangent Function
- Sine Function
- Cosine Function
- Radian
- Circumference
- Ratio

**"How to…" questions**

- How to find the sine, cosine, and tangent of an angle using the unit circle
- How to convert between degrees and radians
- How to find the measure of the circumference of a circle

---

## Appendix H — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Real altitude the FCC approved for SpaceX's first operational Starlink shell | 550 km | Spaceflight Now, ["FCC approves SpaceX's plan to operate Starlink satellites at lower altitude"](https://spaceflightnow.com/2019/04/30/fcc-approves-spacexs-plan-to-operate-starlink-satellites-at-lower-altitude/) | published 2019-04-30, accessed 2026-09-18 | HIGH |
| S2 | Standard single-burn combined plane-change delta-v formula, Δv = 2 × v × sin(Δθ/2) | formula | Standard astrodynamics relation for a single-burn orbital-plane rotation at constant speed, as codified in mission-design references such as Vallado's *Fundamentals of Astrodynamics and Applications* | standard reference relation, accessed 2026-09-18 | HIGH |
| S3 | Busek BIT-3 RF ion thruster real specifications | Isp up to 2,150 s; reference platform up to 2.39 km/s delta-v for a 14 kg 6U CubeSat | Busek Co. Inc., [BIT-3 RF Ion Thruster product page](https://www.busek.com/bit3) | accessed 2026-09-18 | HIGH |
| S4 | Current SpaceX Falcon 9 Transporter rideshare pricing to sun-synchronous orbit | $350,000 for the first 50 kg, plus $7,000 per kg beyond | New Space Economy, ["SpaceX Rideshare Pricing as of February 2026"](https://newspaceeconomy.ca/2026/02/27/spacex-rideshare-pricing-as-of-february-2026-what-it-costs-whats-included-and-how-buyers-budget-a-mission/) | published 2026-02-27, accessed 2026-09-18 | MEDIUM |
| S5 | Rocket Lab Electron dedicated launch list price and LEO payload capacity | $7.5 million per launch; 300 kg to LEO | SpaceNexus, ["Electron: Launch Cost, Next Launch, Specs & Record (2026)"](https://spacenexus.us/rockets/electron) | accessed 2026-09-18 | MEDIUM |

*A direct fetch of SpaceX's own `spacex.com/rideshare` page was attempted this session and returned no extractable pricing text (a JavaScript-rendered page); S4 is the best available live, dated secondary source reporting SpaceX's own published figures, consistent with `cases/_concepts/CONCEPTS_spaceflight_2026-09-12.md`'s own note that both SpaceX's and Rocket Lab's primary pricing pages failed to load cleanly in that same session. Modeling Assumptions MA1–MA4 are documented in Appendix F, not repeated here. Full search trail, rejected sources, and derivation arithmetic: `RESEARCH_LOG.md`.*

---

## Appendix I — Plain-English Notes on Real-World Terms

This appendix explains real-world (non-math) terms and mechanisms used elsewhere in the case, for anyone unfamiliar with satellite operations. It does not affect any Challenge.

**Picturing the "walk" — what a plane-change burn actually looks like.** Picture Earth from above the North Pole. Each of the six target orbital planes is a giant circular path, tilted at its own angle around the equator, like six hula-hoops all balanced on the same center point but each rotated to a different angle. A satellite flying in one hoop stays in that hoop's circle forever unless something pushes it out. A plane-change burn is a single, short engine firing — not a gradual drift — that gives the satellite a sideways shove big enough to swing its entire circular path over until it lines up with a different hoop.

*Why does one short push re-tilt the entire loop, instead of just nudging the satellite sideways within the loop it's already in?* Because a circular orbit is not a fixed track the satellite rides on — it is nothing more than the one and only circular path that gravity produces, starting from wherever the satellite is right now and however fast it is moving in whatever direction *right now*. A satellite always keeps flying in whatever circle is consistent with its current position and its current velocity's direction. The instant a short sideways burn tips that velocity's direction, the satellite is still at the same point, moving at the same speed — but the *only* circle consistent with that new direction is a differently-tilted hoop. From that instant on, gravity simply keeps holding it onto the new hoop, exactly the way it was holding it onto the old one a moment before. Nothing is "gradually bent" — the satellite was never on a fixed track to begin with, so redirecting its velocity for an instant is the same thing as reassigning which hoop it belongs to.

The size of that shove (delta-v) is exactly what Challenge D3 computes: a small angle between hoops needs a small shove, a big angle needs a shove so large it can cost more propellant than the satellite can carry — which is exactly why some of Solara's satellites cannot complete the walk at all (Appendix D).

| Term | Plain-English explanation |
|---|---|
| RAAN (right ascension of ascending node) | The specific angle, measured around the equator, that marks where a satellite's orbital circle crosses from the southern half of its path to the northern half. Two satellites with different RAAN values are flying in differently-tilted "hoops" even if everything else about their orbits is identical — RAAN is simply the number that says which way a given hoop is rotated. |
| Ascending node | The single point where an orbit crosses the equator heading north; RAAN is the angle to that specific point. |
| Vis-viva relationship (v = √(μ ÷ r)) | The standard formula connecting a satellite's orbital speed to its orbital radius: the higher up a satellite flies, the slower it has to travel to stay in a stable circular path, because gravity is weaker and needs less speed to balance it. |
| Standard gravitational parameter (μ) | A single fixed number that captures how strongly Earth's gravity pulls at a given distance — it is Earth's mass multiplied by the universal gravitational constant, bundled into one constant so orbit formulas don't need to carry both separately. Its unit (km³/s²) is just what falls out of the vis-viva formula's algebra when radius is in km and speed is in km/s — nobody needs to picture "cubic kilometers per second squared" directly, any more than a driver needs to picture what a "mile per gallon" physically looks like to use it. |
| Specific impulse (Isp) | A standard measure of how efficiently a thruster converts propellant into thrust — a higher number means more push per kilogram of propellant spent, the same way miles-per-gallon measures a car engine's efficiency. |
| Exhaust velocity | How fast a thruster expels propellant out the back; directly related to Isp (exhaust velocity = Isp × g₀). |
| Ion thruster | A small electric engine that produces thrust by accelerating a stream of charged propellant particles, rather than burning chemical fuel the way a traditional rocket engine does. |
| J2 perturbation / oblateness-driven drift | Earth is not a perfect sphere — it bulges slightly at the equator — and that bulge's extra gravity slowly rotates every satellite's orbital plane over time, for free, without using any propellant. Real operators often use this slow, months-long natural drift instead of a direct burn to change planes; this case's Appendix C explicitly uses the direct-burn method instead, as a disclosed simplification (MA2). |
| Sun-synchronous orbit | An orbit shaped so a satellite crosses any given point on Earth at the same local time every day — useful for comparing images day to day, and one reason SpaceX's rideshare missions are commonly priced specifically "to sun-synchronous orbit." |
| Rideshare vs. dedicated launch | A rideshare mission splits one rocket's total capacity across many different customers' satellites, which is cheaper per kilogram because the fixed cost of the rocket itself is shared; a dedicated launch reserves an entire rocket for one customer, which costs more per kilogram but lets that customer choose exactly which orbital plane the rocket flies to. |
| Walker-style constellation | A standard way of arranging a constellation's satellites into evenly-spaced orbital planes (here, six planes 60° apart) so that satellites are spread out for continuous coverage rather than clustered together. |
| Launch-slot deposit | A payment an operator puts down to reserve a spot on a specific future rocket launch, typically nonrefundable once paid. |
| Radio spectrum filing | Before operating a satellite, an operator must register which specific radio frequencies it will use with an international regulator, so two different satellite systems don't broadcast on top of each other; filing and actually launching satellites into the registered orbit both matter for keeping the claim, which is why "a competitor filing for the same spectrum" is a real competitive threat, not just a legal formality. |

---

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
