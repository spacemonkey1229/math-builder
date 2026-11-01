# Concept sheet — Oceans, Tides & Marine Science (`oceanography`)

**Target and why (one line, per skill's own instruction).** Oceanography is ranked HIGH authoring
priority / HIGH data grade / **0 existing cases** in `readmodel/domain_coverage.json`
(2026-09-01) — the corpus's top domain-authoring gap that also happens to sit on excellent free
government data (NOAA), so it is the highest-leverage next target this session.

**A scoring note that changes how "gap" is read here.** A mechanical sweep of the full
`readmodel/standards_spine.json` run 2026-09-11 (recorded in `cases/flow-state/case.json`'s
`reinforcement_note`) found **zero skills anywhere in the 437-skill spine currently at `n==0`** —
every skill in the corpus now has at least one covering case. I re-ran that sweep independently for
this brief and confirmed it: 0 zero-coverage skills. This means no oceanography concept below can
honestly claim to close a true hole; **the real gap now is thinness** — `readmodel/gap_queue.json`'s
own convention of `n<=2` — and I've scored against that instead, calling out each skill's exact `n`
so `case-write` knows none of these are "first case ever" claims. `domains.json`'s oceanography
entry lists one legacy "uncovered" signature skill, `number-sense-depth` — checked against the live
spine it is at **n=2 (thin, not zero)**, already stale by the time this brief was written, which is
exactly the kind of drift the brief told me to cross-check for.

| # | Concept | Score | Tier | Group(s) fully thin-closed |
|---|---|---|---|---|
| C1 | The Turbine Channel | **7.4** | T4 | Calculus / Integrals (7/7) |
| C2 | The Last Safe Departure | **6.8** | T3 | Number Sense / Measurement And Data (1/1); Measurement / Units (1/1) |
| C3 | The Mooring Choice | **4.8** | T2 | Geometry / Surface Area And Volume (6/6 remaining) |
| C4 | Catch Per Trip | **2.76** | T2 | Statistics And Probability / Displaying Data (3/3 remaining) |

**Recommendation.** Write **C1, The Turbine Channel** first — it is the only concept that closes a
*fully*-thin spine group (all 7 Calculus/Integrals skills sit at n=2, and this case forces all
seven with a genuine physical justification: total tidal-flow volume through a channel is a real
definite integral of a real current-speed curve, not a contrived wrapper). **C2** is the strongest
runner-up and the domain's own headline decision archetype (a harbor pilot's sail-now-or-wait
call) — write it second, not instead, since it closes two different thin groups outright with only
4 scored skills between them (a small, clean case, not inflation). Kill **C4** for this round: its
score is well under Cold Chain's 4.2 calibration anchor and its best data source (NOAA Fisheries'
FOSS portal) returned a 403 when I tried to confirm it live this session — it needs a verified
source before it is worth writing, not just a category guess. **C3** is a fine third pick if a
Geometry-branch case is wanted next, but its data feasibility is MEDIUM, not HIGH, because I could
not confirm a specific buoy/anchor spec document is free and online (only that the category of
document — USCG Aids to Navigation technical manuals — plausibly exists).

---

### C1 — The Turbine Channel   ·   score 7.4   ·   tier T4

**Protagonist.** Dana Okafor, a marine energy siting engineer for a regional utility's tidal-power
pilot program, who has to recommend one channel to the board before the lease-option window closes.

**The dilemma.** A.) Site the turbine array in the Narrows — a narrow, fast tidal channel with high
peak current speed but a short, sharply-peaked flow window each cycle OR B.) site it in the Reach —
a wider, slower channel with a longer, flatter flow window. (Matches `domains.json` oceanography's
own decision archetype #2: "Site the tidal turbine in the fast narrow channel or the slower but
deeper one.")

**Primary metric.** Kilowatt-hours of generation potential per cubic meter of water actually moved
through the channel's cross-section per tidal cycle (a ratio, not a total — a channel that moves
more total water isn't better if it takes more water to make each kWh).

**Why it's close.** NOAA current-meter records give current speed at discrete times through a tidal
cycle, not a formula — an engineer has to fit a smooth curve (this case uses a fitted polynomial to
each channel's real 6-minute-interval speed data, which is exactly where a power-rule antiderivative
applies honestly) and integrate it to get total volumetric flow. The Narrows' curve is tall and
narrow (high peak speed, short duration); the Reach's is short and wide (lower peak, long duration).
Which one delivers more *water per unit of turbine footprint* is genuinely not obvious until the two
definite integrals are computed and compared — that's the case.

**Would close (7 skills, 3 how-to / 4 term, all currently n=2, all of Calculus/Integrals):**

| id | kind | label | n |
|---|---|---|---|
| calculus-antiderivative | term | Antiderivative | 2 |
| calculus-definite-integral | term | Definite Integral | 2 |
| calculus-indefinite-integral | term | Indefinite Integral | 2 |
| calculus-riemann-sum | term | Riemann Sum | 2 |
| calculus-how-to-find-an-antiderivative-using-the-power-rule | how-to | How to find an antiderivative using the power rule | 2 |
| calculus-how-to-evaluate-a-definite-integral-using-the-fundamental-theorem-of-calculus | how-to | How to evaluate a definite integral using the Fundamental Theorem of Calculus | 2 |
| calculus-how-to-approximate-area-under-a-curve-using-a-riemann-sum | how-to | How to approximate area under a curve using a Riemann sum | 2 |

**Already-covered skills it also exercises.** `measurement-how-to-convert-an-amount-with-compound-units`
(n=18, converting m³/s flow and kW into a per-cycle kWh figure); `statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data`
(n=9, plotting the raw current-speed readings before fitting the curve).

**Data feasibility: HIGH.** Named sources I checked live this session:
- NOAA Tides & Currents (`https://tidesandcurrents.noaa.gov/`) — confirmed live; publishes real
  current-speed predictions and observed current-meter data per station, including PORTS® real-time
  current feeds at exactly the kind of channel/inlet this case needs.
- NOAA National Data Buoy Center (`https://www.ndbc.noaa.gov/`) — confirmed live; cross-check /
  supplementary station data if the primary current station lacks a long-enough record.

Not confident about: a specific *named* proposed turbine-lease channel with public current data at
both a "narrow" and "wide" site in one place — `case-research` will likely need to pick two real
NOAA current stations that happen to fit the narrow/wide contrast, disclosed as the site selection,
not invented data.

**Sensitivity (SPEC §6).** None required — a siting/business decision, no personal stakes.

**Split risk.** None — 7 skills, one coherent deliverable arc (fit curve → integrate two ways →
compare).

---

### C2 — The Last Safe Departure   ·   score 6.8   ·   tier T3

**Protagonist.** Marisol Vega, a harbor pilot licensed for a container port, who boards the ship and
is personally liable if it grounds.

**The dilemma.** A.) Depart at the next marginal high tide (in a few hours) with the ship exactly as
loaded OR B.) hold the ship at berth roughly half a lunar day for the next, taller spring tide —
missing the just-in-time delivery window the customer's contract specifies. (This is `domains.json`
oceanography's own decision archetype #1, verbatim.)

**Primary metric.** Under-keel clearance as a fraction of draft (clearance ÷ draft, not clearance in
raw feet) — the standard way pilots actually express a safety margin, because the same clearance in
feet means something different on a small coastal vessel than a deep-draft containership.

**Why it's close.** Charted depth plus predicted tide height minus the ship's draft minus "squat"
(a vessel sinks slightly deeper when moving fast in shallow water) gives clearance; option A's tide
is barely enough on paper, option B is comfortably enough but costs the contract. The case also
needs cargo/ballast: how many cubic meters of ballast would have to be pumped out to lighten the
ship enough to sail early instead of waiting — turning "wait or lighten" into an actual volume
calculation, not just a schedule choice.

**Would close (2 skills, both term, both currently the sole remaining thin skill in their group):**

| id | kind | label | n | group closed |
|---|---|---|---|---|
| number-sense-depth | term | Depth | 2 | Number Sense / Measurement And Data — 1/1 remaining thin skill |
| measurement-volume | term | Volume | 2 | Measurement / Units — 1/1 remaining thin skill |

**Also exercises (thin but not yet fully closing their group — 2 more skills, both n=2, Pre-Calculus
/ Trigonometric Functions, 2 of that group's 3 remaining thin skills):**

| id | kind | label | n |
|---|---|---|---|
| pre-calculus-unit-circle | term | Unit Circle | 2 |
| pre-calculus-how-to-find-the-sine-cosine-and-tangent-of-an-angle-using-the-unit-circle | how-to | How to find the sine, cosine, and tangent of an angle using the unit circle | 2 |

(The tide's phase angle at the departure hour is read off the unit circle to justify why the two
named tide times give different heights — genuinely forced, not decorative. The group's third thin
skill, `tangent-function`, is deliberately **not** claimed: nothing in an under-keel-clearance
calculation forces a tangent, and claiming it would be exactly the "vocabulary stuffing" the parent
skill warns against.)

**Already-covered skills it also exercises.** `pre-calculus-sine-function` / `amplitude` /
`period-of-a-function` (n=3 each — the tide-height model itself); `measurement-how-to-convert-an-amount-with-compound-units`
(n=18); `measurement-how-to-find-elapsed-time` (n=12, time between the two tide options).

**Data feasibility: HIGH.** Named sources checked live this session:
- NOAA Tides & Currents (`https://tidesandcurrents.noaa.gov/`) — confirmed live; publishes official
  high/low tide predictions years in advance for any U.S. port station, exactly the "marginal vs.
  spring tide" numbers this case needs.
- NOAA Office of Coast Survey (`https://nauticalcharts.noaa.gov/`) — confirmed live; provides free
  electronic navigational charts with charted depths (soundings) for the same port.

Not confident about: a real named ship's draft, squat coefficient, and ballast tank capacity —
`domains.json` already flags this (vessel specs for a *named* ship are commercial/AIS-reseller data)
— `case-research` should build the case around a stated, disclosed vessel spec (a common containership
class) rather than a real named vessel.

**Sensitivity (SPEC §6).** None required — professional liability stakes, not personal hardship.

**Split risk.** None — 4 scored skills plus reinforcement, well under the 8–15 range.

---

### C3 — The Mooring Choice   ·   score 4.8   ·   tier T2

**Protagonist.** Theo Marsh, a coastal engineer at a state ports authority, designing a mooring
system for a new offshore data buoy.

**The dilemma.** A.) The Spar Design — a tall cylindrical buoy body with a conical nose (cutwater)
to shed waves, moored to a cast-concrete pyramidal sinker OR B.) The Spherical Design — a compact
spherical buoy, moored to the same style of pyramidal sinker. Both need the sinker sized for the
same holding force; only the buoy body shape differs.

**Primary metric.** Net buoyant lift (buoyancy minus anchor weight) per dollar of material — steel
and concrete are priced by volume/surface area, buoyancy is a volume, so the honest comparison is a
ratio, not "which buoy is bigger."

**Why it's close.** A sphere has less surface area (and so less steel and less bio-fouling/corrosion
exposure) per unit of enclosed volume than a cylinder-with-cone — that favors B. But the spar's
cylindrical body is easier and cheaper to fabricate and mount instruments on flat sides, which is a
real, named trade-off the case can state as a constraint rather than a number. The pyramidal sinker
is shared by both options, so its volume/weight is computed once and applied to each.

**Would close (6 skills, all how-to, all currently n=2 — all of Geometry/Surface Area And Volume's
remaining thin skills):**

| id | kind | label | n |
|---|---|---|---|
| geometry-how-to-find-the-surface-area-of-a-cylinder | how-to | How to find the surface area of a cylinder | 2 |
| geometry-how-to-find-the-volume-of-a-cylinder | how-to | How to find the volume of a cylinder | 2 |
| geometry-how-to-find-the-volume-of-a-cone | how-to | How to find the volume of a cone | 2 |
| geometry-how-to-find-the-volume-of-a-sphere | how-to | How to find the volume of a sphere | 2 |
| geometry-how-to-find-the-surface-area-of-a-pyramid | how-to | How to find the surface area of a pyramid | 2 |
| geometry-how-to-find-the-volume-of-a-pyramid | how-to | How to find the volume of a pyramid | 2 |

**Already-covered skills it also exercises.** `geometry-how-to-find-the-surface-area-of-a-prism` /
`how-to-find-the-volume-of-a-prism` (n=3 each, if the sinker is modeled as a stepped/prism base
instead of a pure pyramid — a `case-write` framing choice, not scored here either way).

**Data feasibility: MEDIUM.** I was not able to name and confirm one specific free spec document
this session (I did not find and check a live URL for a buoy/sinker manufacturer or USCG technical
manual before writing this sheet, per the "don't web-search during brainstorm unless verifying"
norm — this one genuinely needs that check before it can be graded HIGH). The category is plausible:
USCG Aids to Navigation technical manuals and NOAA/IOOS buoy engineering specs are usually public.
Not confident about: exact dimensions and concrete/steel unit costs — likely Modeling Assumptions.

**Sensitivity (SPEC §6).** None required.

**Split risk.** None — 6 skills, one coherent mooring-system deliverable.

---

### C4 — Catch Per Trip   ·   score 2.76   ·   tier T2

**Protagonist.** Renata Silva, a regional fisheries manager, deciding between two survey protocols
before recommending a quota change to the council.

**The dilemma.** A.) Trust the trawl-survey time series (longer history, more variable catch counts)
OR B.) trust the newer acoustic-survey time series (shorter history, less variable, but not yet
long enough to be sure it isn't missing a seasonal pattern the trawl survey shows).

**Primary metric.** Catches per standardized trip (already a ratio in fisheries science — this case
does not invent it) compared across the two survey methods and across two candidate model shapes.

**Why it's close.** A box-and-whisker plot of each survey's catch-per-trip distribution shows B has
tighter variability (fewer outlier trips) — a case for trusting it more. But a scatter plot of
catch-per-trip against water temperature shows a pattern that looks non-linear for the longer trawl
record and only looks linear for the acoustic record because it's too short to show the turn — the
case turns on recognizing that difference, not on which survey "looks nicer."

**Would close (3 skills, 1 how-to / 2 term, all currently thin — all of Displaying Data's remaining
thin skills):**

| id | kind | label | n |
|---|---|---|---|
| statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data | how-to | How to create a box and whisker plot given a set of data | 1 |
| statistics-and-probability-non-linear | term | Non-linear | 2 |
| statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data | how-to | How to draw a line of best fit given a set of data | 2 |

**Already-covered skills it also exercises.** `statistics-and-probability-scatter-plot` /
`how-to-create-a-scatter-plot-given-a-set-of-data` (n=9 each); `statistics-and-probability-correlation`
(n=3).

**Data feasibility: MEDIUM.** I attempted to confirm a specific NOAA Fisheries data source live this
session: `https://www.fisheries.noaa.gov/foss` (the Fisheries One Stop Shop landings/catch data
tool) returned **HTTP 403 Forbidden** when fetched — I could not verify it live, so I am not grading
this HIGH. The parent site, `https://www.fisheries.noaa.gov/`, is confirmed live and does describe
public "Research Surveys" and "Population Assessments" data as a general offering, which is why this
isn't graded LOW either. Not confident about: whether a specific two-survey-method comparison
dataset (trawl vs. acoustic, same species, overlapping years) is actually publicly downloadable in
one place, or would need assembling from several NOAA regional science center pages.

**Sensitivity (SPEC §6).** None required.

**Split risk.** None — 3 skills, small, single deliverable arc.
