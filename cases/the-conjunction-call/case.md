# Case Study: Conjunction Call

MS | Math | Case Study | 2026-27 | Launchpad

---

## Overview

Priya Nakamura has the conjunction-screening report — the daily printout of every orbiting object predicted to pass close to her satellite — open in one window and a half-written de-orbit order open in the other, and she has been toggling between them for twenty minutes without touching either. The mission control room is quiet this late — just the hum of the server racks and the soft click of Deshawn's keyboard two desks over, still fighting yesterday's backlog of data radioed down from orbit.

Aurora-7 has been hers since launch: four years of ocean-color data — satellite readings of light bouncing off the sea's surface, used to track algae blooms and water clarity — nobody else is collecting at this resolution, four years of late nights, and, as of this morning's fuel reading, not much propellant left to show for it. The season is starting: certain months bring more tracked fragments crossing Aurora-7's altitude band, the same way Earth passes through denser patches of comet debris at the same time every year, producing predictable meteor-shower peaks — and the fuel gauge is not going to get any fuller.

Her manager wants an answer before the next shift takes over at 6:00 a.m.: de-orbit Aurora-7 now, clean and certain, or let her keep flying through the season and hope the numbers hold up if a close call gets real. Priya has run the screening report twice already. Both times she closed the laptop before finishing the last table.

She opens it a third time, pulls the propellant readout up next to it, and starts typing.

---

## Background

Priya Nakamura is a satellite operations engineer at Meridian Orbital, a small-satellite operator, and she is personally responsible for signing off on Aurora-7's collision-avoidance decisions this week. Aurora-7 is aging and low on propellant, but its sensor package is still fully functional and still under contract to deliver ocean-color data through the end of the season.

Two paths are open to her: **De-Orbit Now**, which ends Aurora-7's data collection immediately but with zero further fuel risk, and **Fly The Season**, which keeps Aurora-7 collecting data through the debris-conjunction season and spends reserve propellant on real avoidance maneuvers if and when a tracked object's predicted approach actually crosses the industry's real collision-probability threshold (SEE APPENDIX A).

Meridian's disposal policy — consistent with standard orbital-debris-mitigation practice — requires every satellite to retain enough propellant to complete a controlled end-of-mission de-orbit burn (a deliberate final engine firing that lowers a satellite's orbit until it re-enters the atmosphere and burns up, instead of drifting as space debris for decades), whichever day that burn actually happens (SEE APPENDIX D). There is nothing physical to picture here at all — no tank-within-a-tank, no valve, no partition. It is pure bookkeeping: Aurora-7's flight computer reports one single number (kilograms of propellant remaining, Appendix D), and Priya's mission-control procedures are a rule about that number, exactly like a line item in a budget spreadsheet — "do not authorize any command that would make this number drop below 0.0100." Nothing in the hardware enforces it; the rule is entirely in what commands the humans and software agree to send. That reserved amount cannot be spent on anything else, including an avoidance maneuver, without leaving Aurora-7 unable to comply with the disposal requirement it will eventually have to meet regardless of which option Priya picks today.

CelesTrak's SOCRATES Plus service screens every active payload against the full tracked-object catalog three times a day, propagating each object's orbit forward a week and reporting every predicted approach that comes within 5 km at closest approach — minimum range, relative speed, time of closest approach, and the maximum predicted collision probability for the pair (SEE APPENDIX A). Aurora-7's own conjunction log for the coming 45-day season is in Appendix C. Appendix B lays out how many objects share Aurora-7's altitude band and what that means for how many pairwise close-approach checks the screening system actually has to run. Appendix D covers Aurora-7's thruster and the propellant math that turns a maneuver's required velocity change into a mass of propellant spent. None of Appendix B, C, or D's figures for this specific fictional fleet are publicly published, so each is a stated scenario assumption, grounded in a real basis (SEE APPENDIX E).

The vocabulary and the "how to…" skills this case will ask you to research are listed in **APPENDIX F** — that is where Challenge 1 sends you. Every sourced figure and stated assumption in this case is documented in **APPENDIX I**. If any real-world term in this case (not the math vocabulary) is unfamiliar, **APPENDIX H** explains it in plain English.

She starts typing.

---

## Dilemma

You are Priya Nakamura.

Do you:

**A.)** De-Orbit Now — end Aurora-7's data collection immediately, with a guaranteed-compliant disposal burn and zero further fuel risk **OR**

**B.)** Fly The Season — keep Aurora-7 collecting data through the debris-conjunction season, spending reserve propellant on real avoidance maneuvers only when a conjunction's predicted collision probability actually crosses the industry threshold

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A conjunction-count table.** Using a factorial-based combination formula, compute the total number of unique pairwise close-approach checks required to screen every object that shares Aurora-7's altitude band this season (Appendix B), and how many of those pairs directly involve Aurora-7 herself. Show the factorial expression before you simplify it.
- **D2 — A probability-notation screening table.** For each of the six conjunction events in Appendix C, convert the reported maximum collision probability between scientific notation and standard (decimal) notation, and compute the absolute-value margin between each event's probability and the real industry maneuver threshold (Appendix A), expressed in scientific notation.
- **D3 — A propellant-budget table.** Using Aurora-7's thruster's real specific impulse (Appendix D) and its stated wet mass, derive the kilograms of propellant required per meter/second of delta-v, then compute the total propellant cost of performing an avoidance maneuver for every event your Challenge D2 table shows crossing the real threshold.
- **D4 — A decision memo.** Compare Option A's certain outcome (zero additional data days, a guaranteed-compliant disposal burn spent now) against Option B's outcome computed from D1–D3 (a season of data collection, a real propellant cost for this season's real threshold-crossing maneuvers, and the propellant Aurora-7 must still have left over afterward to complete the same disposal burn required in Appendix D). State your recommendation and show the arithmetic that supports it.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A — Conjunction Screening: How It Really Works

**CelesTrak's SOCRATES Plus** is a real, live, publicly available conjunction-screening service — a "conjunction," in this orbital sense, just means two tracked objects are predicted to pass unusually close to each other, not the grammar term. Three times a day, it takes the position of every tracked object in orbit and calculates ("propagates") where each one's own orbital path will carry it forward one week — the same kind of forward calculation you'd use to predict where a thrown ball will be a second from now, just applied to an object circling the Earth — and reports every predicted pair of objects whose closest approach comes within 5 km of each other. For each flagged pair it reports: the minimum predicted range (how close they actually get), the time of closest approach, the relative speed, and the maximum predicted collision probability (Pc) — a computed percent chance, built from how precisely each object's position is actually known, that the two paths result in an impact [S4].

Real satellite operators do not maneuver for every reported conjunction — most predicted approaches carry a vanishingly small collision probability. NASA's own Conjunction Assessment and Risk Analysis (CARA) program uses a baseline maneuver-decision threshold of **Pc ≥ 1 × 10⁻⁴** (a 1-in-10,000 chance of collision): below that, no action is recommended; at or above it, a mitigation maneuver is recommended [S1]. NASA further notes that a well-executed mitigation maneuver is expected to reduce a flagged event's collision probability by about 1.5 orders of magnitude (a 10¹·⁵-fold, roughly 32-times, reduction — "order of magnitude" means a power of 10), down to roughly **3.1 × 10⁻⁶** [S1] — worth knowing, but not itself something this case's Challenges ask you to use.

| Quantity | Value |
|---|---|
| SOCRATES screening range (objects closer than this at closest approach get reported at all) | 5 km [S4] |
| SOCRATES screening frequency | 3 times per day [S4] |
| SOCRATES forward propagation window | 7 days [S4] |
| Real industry collision-probability maneuver threshold (Pc) | 1 × 10⁻⁴ [S1] |

---

## Appendix B — Aurora-7's Screening Population

Meridian Orbital does not publish, and no public catalog publishes, a single "number of objects sharing this specific satellite's altitude band" figure broken out per satellite — SOCRATES screens the full catalog (the running list of every known human-made object in orbit, updated by ground radar and telescopes), not a per-shell subset (SEE APPENDIX A). This case fixes a stated scenario count for Aurora-7's specific ~525-kilometer-high "sun-synchronous" orbital band (an orbit shaped so the satellite passes over any given point on Earth at the same local time every day — useful for comparing images day to day, and common enough that many satellites cluster in this same narrow altitude range) (MA1, Appendix E), grounded in the real scale of today's tracked-object catalog: **46,875 objects are currently tracked and cataloged across all of Earth orbit** [S2].

| Quantity | Value |
|---|---|
| Total objects tracked and cataloged, all of Earth orbit | 46,875 [S2] |
| Objects sharing Aurora-7's specific altitude band this season, screened as potential conjunction partners (including Aurora-7 herself) | 36 [MA1] |

*Challenge D1 asks you to find, using a factorial-based combination formula, how many unique pairs can be formed from these 36 objects — and, separately, how many of those pairs involve Aurora-7 specifically.*

---

## Appendix C — Aurora-7's Conjunction Log, 45-Day Season

The six-event log below is a stated scenario dataset (MA2, Appendix E) for Aurora-7's specific 45-day debris season, formatted the way a real SOCRATES Plus report is formatted [S4]. It is not a live feed record pulled for a real, named satellite.

| Event | Day of season | Object pair | Predicted min. range (km) | Maximum predicted Pc | Avoidance Δv if maneuvered (m/s) |
|---|---|---|---|---|---|
| E1 | 3 | Aurora-7 / Debris 41-119 | 2.8 | 2.7 × 10⁻⁵ | — |
| E2 | 9 | Aurora-7 / Debris 33-882 | 0.6 | 3.4 × 10⁻⁴ | 3.5 |
| E3 | 15 | Aurora-7 / Debris 08-207 | 1.4 | 8.1 × 10⁻⁵ | — |
| E4 | 22 | Aurora-7 / Debris 51-644 | 0.9 | 1.9 × 10⁻⁴ | 6.0 |
| E5 | 30 | Aurora-7 / Debris 19-355 | 0.4 | 5.2 × 10⁻⁴ | 7.0 |
| E6 | 41 | Aurora-7 / Debris 27-908 | 1.1 | 1.1 × 10⁻⁴ | 4.5 |

*"Debris ##-###" designators above are fictional, styled on the real NORAD-catalog-number format SOCRATES actually uses — they are not real catalog numbers. "Avoidance Δv if maneuvered" is left blank for any event your Challenge D2 table shows does not cross the real 1 × 10⁻⁴ threshold in Appendix A; those events require no maneuver at all, by the same real decision rule every operator actually uses.*

---

## Appendix D — Aurora-7's Thruster and Propellant Budget

Aurora-7 flies a Busek BIT-3 RF ion thruster — "RF" (radio-frequency) refers to how it energizes its propellant, and "ion thruster" means it produces thrust electrically rather than by burning chemical fuel. You do not need to know how it works internally: for this case's math, treat it as a black box fully described by the two numbers in the table below (specific impulse and thrust) — a real, flight-proven small-satellite propulsion system [S3].

| Quantity | Value |
|---|---|
| Specific impulse (Isp), rated maximum — a standard measure of how efficiently a thruster turns propellant into thrust; a higher number means more push per kilogram spent | 2,150 s [S3] |
| Thrust, rated maximum — the actual push force the thruster produces | 1.1 mN [S3] |
| Standard gravity (g₀), a fixed physical constant used to convert Isp (measured in seconds) into a velocity | 9.80665 m/s² |
| Aurora-7 stated wet mass — the spacecraft's mass including whatever propellant is still on board (as opposed to "dry mass," which would not count it) | 12.0 kg [MA3] |
| Aurora-7 remaining reserve propellant, start of season | 0.024 kg [MA4] |
| Minimum propellant Meridian's disposal policy requires Aurora-7 to retain for its own controlled end-of-mission de-orbit burn, whenever that burn happens | 0.0100 kg [MA5] |

*Isp is measured in seconds because of how it is defined: exhaust velocity (how fast the thruster expels propellant out the back, in meters/second) equals Isp × g₀. Challenge D3 asks you to compute that exhaust velocity directly from the two rows above, then use dimensional reasoning — the same kind Challenge 1's "how to convert an amount with compound units" resource explains — to combine it with Aurora-7's wet mass into kilograms of propellant per meter/second of delta-v (Δv — engineers' standard way of measuring "how big" a maneuver is, meaning the total change in the spacecraft's velocity it requires, regardless of the spacecraft's mass), and apply it to every maneuver Challenge D2 shows is really required.*

---

## Appendix E — Modeling Assumptions

> These figures are **not sourced** as direct external citations. They are stated scenario assumptions, each grounded in a real basis described below. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Number of tracked objects sharing Aurora-7's specific altitude band this season, screened as potential conjunction partners | 36 (including Aurora-7) | No public catalog reports a single "objects sharing this specific satellite's shell" count broken out per satellite — SOCRATES screens the entire tracked catalog against itself, not a per-shell subset (Appendix A). A mid-inclination, ~525 km sun-synchronous shell is realistically one of the more congested LEO bands relative to the real 46,875-object catalog [S2], and dozens of objects sharing a single narrow altitude band over a 45-day window is a realistic order of magnitude for that congestion — not a specific real satellite's real, publicly reported count. | This sets the size of the screening table in Challenge D1. It does not change the risk of any individual conjunction in Appendix C, which is evaluated on its own reported probability regardless of how many other objects share the shell. |
| MA2 | Aurora-7's six-event conjunction log for this season (Appendix C) | See Appendix C table | A specific 45-day conjunction history for a specific fictional satellite has no real-world source to look up — it is inherently a scenario construction, styled on the real report format SOCRATES actually produces (Appendix A) rather than pulled from a live feed for a real, named satellite. | The case's answer is sensitive to this data — different reported probabilities and required Δv values would change how much propellant Option B actually costs. This is disclosed here rather than hidden in the table. |
| MA3 | Aurora-7's wet mass, used to convert delta-v into a mass of propellant spent | 12.0 kg | Consistent with the mass class of small satellites the BIT-3 thruster is actually designed and flight-qualified for — the manufacturer's own published reference platform is a 14 kg 6U CubeSat [S3]; Aurora-7 is stated as a slightly lighter 6U-class bus. | The propellant-per-maneuver figures in Challenge D3 scale directly with this number; a heavier or lighter stated bus mass would change them proportionally. |
| MA4 | Aurora-7's remaining reserve propellant at the start of the season | 0.024 kg | Not publicly reported for any real, specific satellite's current fuel state — this is the case's own stated "aging, low-fuel" scenario detail, fixed at a small fraction of a plausible original tank load for a thruster system in this thrust class late in a multi-year mission. | This is the single most dilemma-relevant assumption in the case: it is the total pool of propellant Option B has to work with, for both this season's real threshold-crossing maneuvers and the disposal reserve in MA5. The case's answer is directly sensitive to this value. |
| MA5 | Minimum propellant Meridian's disposal policy requires Aurora-7 to retain for its own end-of-mission de-orbit burn | 0.0100 kg | Consistent with standard orbital-debris-mitigation practice, which requires an operator to be able to complete a controlled disposal maneuver at end of mission — no public figure exists for Aurora-7 specifically since Aurora-7 is fictional, so this case fixes a stated policy minimum. This reserve applies identically under both options: Option A spends it now, Option B defers it to the end of the season. | The case's answer is directly sensitive to this value, in the same pool as MA4. |

*No other figure in this case required a Modeling Assumption — see `RESEARCH_LOG.md` for the full source-by-source trail.*

---

## Appendix F — "How To…" Math Questions To Research

**Vocabulary terms**

- Standard Notation
- Factorial
- Absolute Value
- Scientific Notation

**"How to…" questions**

- How to write a number in standard notation given its scientific notation
- How to evaluate a factorial expression
- How to write a number in scientific notation given its standard notation
- How to convert an amount with compound units

---

## Appendix H — Plain-English Notes on Real-World Terms

This appendix explains real-world (non-math) terms and mechanisms used elsewhere in the case, for anyone unfamiliar with satellite operations. It does not affect any Challenge.

| Term | Plain-English explanation |
|---|---|
| Conjunction / conjunction event | The term satellite operators use for two tracked objects predicted to pass unusually close together — not the grammar term. |
| SOCRATES / SOCRATES Plus | A real, free, public report that lists every predicted close approach between orbiting objects, refreshed three times a day. |
| Propagate an orbit forward | Using the physics of orbital motion to calculate where an object will be at a future time — the same kind of calculation as predicting where a thrown ball will land, just applied to a satellite. |
| Closest approach / time of closest approach (TCA) / minimum range / relative speed | The single moment two objects' predicted paths come nearest each other, when that moment happens, how close they get, and how fast they're moving relative to one another at that instant. |
| Collision probability (Pc) | A computed percent chance of impact, built from the two objects' predicted paths and how precisely those paths are actually known (tracking is never perfectly exact). |
| Maneuver / avoidance maneuver | A short engine burn that nudges a satellite's path just enough to miss the other object. |
| Debris season / debris-conjunction season | A period when tracked fragments happen to cross a satellite's orbital path more often — similar to how certain months bring more meteor showers. |
| De-orbit / de-orbit burn / disposal burn | A deliberate final engine firing that lowers a satellite's orbit until it re-enters the atmosphere and burns up, instead of drifting for decades as space debris. |
| Reserve / reserved propellant | Not a separate, physically walled-off tank — a flight-rule commitment not to spend that portion of the one shared propellant supply on anything except its designated purpose. |
| Tracked-object catalog | The running, continuously updated list of every known human-made object in orbit, maintained using ground-based radar and telescopes. |
| Sun-synchronous orbit / altitude band / LEO (low Earth orbit) | LEO is the region of space closest to Earth where most satellites (including the ISS) fly; a sun-synchronous orbit is shaped so a satellite crosses any given point on Earth at the same local time each day; an "altitude band" is a narrow range of orbital heights that many satellites in similar orbits share. |
| Delta-v (Δv) | Engineers' standard way of measuring "how big" a maneuver is: the total change in velocity required, independent of the spacecraft's actual mass. |
| Specific impulse (Isp) | A standard measure of how efficiently a thruster converts propellant into thrust — a higher number means more push per kilogram of propellant spent. |
| Exhaust velocity | How fast a thruster expels propellant out the back; directly related to Isp. |
| Wet mass / dry mass | Wet mass counts a spacecraft together with whatever propellant remains on board; dry mass would not include it. |
| Ion thruster | A small electric engine that produces thrust by accelerating a stream of charged propellant particles, rather than burning chemical fuel the way a traditional rocket engine does. |
| Ocean-color data | Satellite measurements of light reflected by the ocean's surface, used to track algae blooms, water clarity, and marine-ecosystem health. |
| 6U CubeSat | A small, standardized satellite built from six 10 cm cube-shaped units stacked together (about the size of a shoebox) — a common, inexpensive small-satellite size class. |
| Gimbal | A mechanical mount that lets a thruster pivot slightly, so small aiming corrections don't require turning the entire spacecraft — background detail; no Challenge in this case uses it. |
| NORAD catalog number | The unique ID number the U.S. military's Space Surveillance Network assigns to every tracked object in orbit, the same way every car has a unique VIN — background detail only. |
| Input power (W) | How much electrical power the thruster draws while firing — background detail; not something any Challenge in this case calculates with. |
| Why screening is a "pairs" problem | Any two objects, not just Aurora-7 and one piece of debris, could in principle pass close to each other — so a thorough screening system has to check every possible pair among the tracked population, not just pairs involving one satellite. That is exactly why Challenge D1's combination count matters. |

---

## Appendix I — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Real industry collision-probability threshold for recommending an avoidance maneuver, and the real post-maneuver risk-reduction target | Pc ≥ 1 × 10⁻⁴ threshold; ~3.1 × 10⁻⁶ post-maneuver target | NASA Conjunction Assessment and Risk Analysis (CARA) program, [CARA FAQ / NPR Handbook](https://www.nasa.gov/wp-content/uploads/2025/03/cara-faq-npr-handbook-2025.pdf) | accessed 2026-09-17 | HIGH |
| S2 | Total number of tracked, cataloged objects in Earth orbit | 46,875 objects | ESA Space Debris Office, [DISCOSweb Space Environment Statistics](https://sdup.esoc.esa.int/discosweb/statistics/) | data as of 2026-07-31, accessed 2026-09-17 | HIGH |
| S3 | Busek BIT-3 RF ion thruster real specifications | Isp up to 2,150 s; thrust up to 1.1 mN; dry mass 1.40 kg w/ gimbal; input power 56–75 W; reference platform up to 2.39 km/s Δv for a 14 kg 6U CubeSat | Busek Co. Inc., [BIT-3 RF Ion Thruster product page](https://www.busek.com/bit3) | accessed 2026-09-17 | HIGH |
| S4 | CelesTrak SOCRATES Plus conjunction-screening methodology | Screens 3×/day; 7-day forward propagation; reports every predicted approach within 5 km at closest approach, with minimum range, time of closest approach, relative speed, and maximum Pc | CelesTrak, [SOCRATES Plus](https://celestrak.org/SOCRATES/) | accessed 2026-09-17 | HIGH |

*Modeling Assumptions MA1–MA5 are documented in Appendix E, not repeated here. Full search trail, rejected sources, and derivation arithmetic: `RESEARCH_LOG.md`.*

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
