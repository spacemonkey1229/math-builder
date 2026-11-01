# Concept sheet — Observational Astronomy (`astronomy`)

**Target and why (one line, per skill's own instruction).** Astronomy is HIGH authoring priority /
HIGH data grade / **0 existing cases** in `readmodel/domains.json` — the single domain in the
`Space & Sky` cluster with zero corpus presence and (per its own `data_availability` note) "arguably
the single most open science on the internet," so it is the highest-leverage next target this
session.

**A staleness check and a scoring note, both confirmed live 2026-09-12.** `domains.json`'s astronomy
entry lists exactly one `uncovered_signature_skills` entry —
`geometry-how-to-find-the-volume-of-a-sphere` — implying it is the domain's only true zero-coverage
skill. I checked it live against `readmodel/standards_spine.json`: it is at **n=2** right now (thin,
not zero), consistent with this session's earlier spine-wide sweep (`cases/flow-state/case.json`,
`cases/the-turbine-channel/case.json`) that found **zero skills anywhere in the 437-skill spine at
true n==0**. `domains.json` is stale here exactly the way the brief warned — I did not trust the
`signature_skills[]`/`uncovered_signature_skills[]` lists and instead pulled every id fresh from the
live spine (table below). All four concepts are scored against `gap_queue.json`'s own `n<=2` "thin"
convention, and none claims to close a zero.

| id (checked live) | kind | n | note |
|---|---|---|---|
| geometry-how-to-find-the-volume-of-a-sphere | how-to | 2 | thin, not zero — `domains.json` claim is stale |
| geometry-similar | term | 2 | thin |
| geometry-angle | term | 3 | not thin |
| geometry-degree | term | 3 | not thin |
| geometry-sphere | term | 4 | not thin |
| advanced-operations-scientific-notation | term | 4 | not thin |
| advanced-operations-how-to-write-a-number-in-scientific-notation-given-its-standard-notation | how-to | 4 | not thin |
| measurement-how-to-convert-an-amount-from-one-unit-to-another-unit | how-to | 17 | not thin |
| statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data | how-to | 9 | not thin |
| statistics-and-probability-outlier | term | 3 | not thin |
| number-sense-how-to-compare-two-or-more-values | how-to | 52 | not thin |
| pre-calculus-radian | term | 4 | not thin |
| pre-calculus-reference-angle | term | 3 | not thin |

| # | Concept | Score | Tier | Group(s) fully thin-closed |
|---|---|---|---|---|
| C1 | The Clear-Sky Dome | **8.6** | T2/T3 | Geometry / Surface Area And Volume (6/6 remaining thin) |
| C2 | The Survey Slot | **6.8** | T3 | Statistics And Probability / Probability (4/4 remaining thin) |
| C3 | The Marginal Detection | **4.6** | T2 | Statistics And Probability / Displaying Data (3/3 remaining thin) |
| C4 | The Parallax Baseline | **1.8** | T3 | none fully closed |

**Recommendation.** Write **C1, The Clear-Sky Dome** first — it closes every remaining thin skill
in Geometry/Surface Area And Volume (6/6) with a real observatory-enclosure architecture (cylindrical
drum, hemispherical dome cap, conical slit windscreen, pyramidal pier footing) and pairs it with real
ESO Paranal astroclimate data, matching `domains.json`'s own siting archetype. **C2, The Survey Slot**
is the strongest runner-up and the domain's own headline decision archetype verbatim (4-hour slot: one
transit candidate vs. a 12-field survey) — write it second; it fully closes the Probability group's
remaining thin set with a genuinely forced combinatorics argument (field-selection combinations
against a fixed slot). **C3** is a fine third pick — smaller but honest, no stretch skills. **Kill C4
for this round**: its score (1.8) sits well under Cold Chain's 4.2 calibration anchor because a
faithful parallax model only cleanly forces 3 of Geometry/Triangles' 6 remaining thin skills without
closing the group; it would need a materially different framing (or merging with a second thin group)
before it is worth writing.

---

### C1 — The Clear-Sky Dome   ·   score 8.6   ·   tier T2/T3

**Protagonist.** Kwame Osei, site-selection engineer for a university consortium's new robotic
survey telescope, who has to sign one land-lease recommendation before the option window on both
parcels expires.

**The dilemma.** A.) Build on the high desert plateau parcel — the best clear-sky fraction on
record, but the elevation and wind load require a reinforced dome enclosure (thicker cylindrical
drum wall, a wind-rated conical slit cover, and a heavier pyramidal pier footing) OR B.) build on
the lower, more sheltered parcel — noticeably fewer clear nights per year on record, but a standard
lightweight dome (thinner drum, no reinforced footing).

**Primary metric.** Usable clear-sky observing hours per year, per dollar of dome-and-pier
construction cost — a ratio, because the plateau site's extra clear nights are only a win if they
are not entirely eaten by the cost of the reinforced structure needed to survive there.

**Why it's close.** The plateau's historical astroclimate record (real DIMM-seeing and cloud-cover
statistics of exactly this kind are what ESO's Paranal Astronomical Site Monitor publishes) gives it
materially more usable nights per year — but its dome needs more steel (surface area of the
cylindrical drum and of the pyramidal footing's faces) and more material volume (the cylinder, the
hemispherical dome cap, and the pier) than the sheltered site's lighter structure, and clear nights
still have to be modeled as a run of independent yes/no events across a season to project next
year's usable-night count honestly rather than just repeating last year's total. Whether the extra
clear-sky access is worth the extra material is genuinely not obvious until both ratios are computed.
**Disclosure:** bundling a hemispherical dome cap, a conical windscreen, and a pyramidal pier footing
onto one enclosure is a deliberate composite (real large-dome enclosures do combine cylindrical walls
with a hemispherical cap, and real observatory piers do sit on stepped/pyramidal footings) chosen
specifically to close the full remaining-thin set of one spine group — `case-write` should confirm
against a real enclosure reference (an SPIE dome-design paper or manufacturer spec) that all four
solids are load-bearing to the deliverable, not decorative.

**Would close (7 skills, 6 how-to / 1 term, all currently thin, closing 6/6 remaining thin in
Geometry/Surface Area And Volume):**

| id | kind | label | n |
|---|---|---|---|
| geometry-how-to-find-the-surface-area-of-a-cylinder | how-to | How to find the surface area of a cylinder | 2 |
| geometry-how-to-find-the-volume-of-a-cylinder | how-to | How to find the volume of a cylinder | 2 |
| geometry-how-to-find-the-volume-of-a-sphere | how-to | How to find the volume of a sphere | 2 |
| geometry-how-to-find-the-volume-of-a-cone | how-to | How to find the volume of a cone | 2 |
| geometry-how-to-find-the-surface-area-of-a-pyramid | how-to | How to find the surface area of a pyramid | 2 |
| geometry-how-to-find-the-volume-of-a-pyramid | how-to | How to find the volume of a pyramid | 2 |
| statistics-and-probability-independent-event | term | Independent Event | 2 |

**Already-covered skills it also exercises.** `geometry-surface-area` / `geometry-volume` (n=8, n=5
— vocabulary anchors); `geometry-how-to-find-the-surface-area-of-a-prism` /
`how-to-find-the-volume-of-a-prism` (n=3 each, if the pier is instead framed as a stepped prism);
`measurement-how-to-convert-an-amount-from-one-unit-to-another-unit` (n=17, converting site
elevation/material units).

**Data feasibility: MEDIUM.** Named sources checked live this session:
- ESO Paranal Astroclimate / Astronomical Site Monitor (`https://www.eso.org/gen-fac/pubs/astclim/paranal/`)
  — confirmed live; publishes real historical DIMM seeing, cloud cover, humidity and wind statistics
  for a real high-altitude site, with an ASM database and API for the "usable nights" side of the
  ratio. This half is HIGH.
- Mauna Kea Weather Center (attempted `mkwc.ifa.hawaii.edu`) — connection failed this session; not
  usable as a named source without a working URL. Paranal replaces it above.

Not confident about: a specific, live, free dome-enclosure or pier-footing spec/cost document — I did
not find and check one this session. The category (SPIE dome-engineering papers, telescope-enclosure
manufacturer spec sheets) plausibly exists, which is why this is graded MEDIUM overall rather than
LOW, but `case-research` needs to land a real one before the construction-cost side of the ratio is
anything but a stated Modeling Assumption.

**Sensitivity (SPEC §6).** None required — a siting/capital-expenditure decision, no personal stakes.

**Split risk.** None on skill count (7, well under 15) — the only risk is the composite-solid
disclosure above, which is a plausibility risk, not a scope risk.

---

### C2 — The Survey Slot   ·   score 6.8   ·   tier T3

**Protagonist.** Renee Okafor, the telescope-time allocation scheduler for a university robotic
observatory's exoplanet program, who has one open 4-hour slot before the moon rises too bright to
use and must submit her recommendation to the allocation committee tonight.

**The dilemma.** A.) Dedicate the full slot to re-observing one specific candidate transit with a
known predicted window (`domains.json`'s own archetype #1, verbatim: "point the 4-hour slot at the
one candidate exoplanet transit") OR B.) split the slot across a 12-field shallow survey looking for
new, as-yet-undetected shallow transits.

**Primary metric.** Expected number of confirmed transit detections per hour of telescope time — a
ratio, because option A's single high-confidence target and option B's twelve low-probability fields
are not comparable as raw counts.

**Why it's close.** Option A's transit is a near-certain single event (one field, one already-known
signal) but yields at most one confirmation regardless of how the 4 hours are spent. Option B treats
each of the 12 fields as an independent trial with its own small detection probability, so the
compound-event probability of at least one new detection can rival — or fall short of — option A's
near-certainty depending on the per-field rate, which is exactly the kind of thing that looks
obviously one-sided until it's computed. Because the survey slot can only realistically follow up a
handful of the 12 flagged fields afterward given downlink/battery budget, the scheduler also has to
show *how many* different follow-up subsets are even possible — this is where the combinatorics
becomes load-bearing rather than decorative: it is the argument for why exhaustive follow-up is
infeasible and ranking-by-expected-value is the real strategy.

**Would close (6 skills, 2 how-to / 4 term, closing 4/4 remaining thin in Statistics And
Probability/Probability):**

| id | kind | label | n |
|---|---|---|---|
| statistics-and-probability-independent-event | term | Independent Event | 2 |
| statistics-and-probability-permutation | term | Permutation | 2 |
| statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination | how-to | How to determine the number of outcomes of a combination | 2 |
| statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-permutation | how-to | How to determine the number of outcomes of a permutation | 2 |
| advanced-operations-standard-notation | term | Standard Notation | 2 |
| advanced-operations-how-to-write-a-number-in-standard-notation-given-its-scientific-notation | how-to | How to write a number in standard notation given its scientific notation | 2 |

**Already-covered skills it also exercises.** `statistics-and-probability-how-to-determine-the-
probability-of-a-compound-event` (n=7, the core "at least one detection among 12" calculation);
`statistics-and-probability-theoretical-probability` / `experimental-probability` (n=4 each);
`advanced-operations-scientific-notation` (n=4, transit-depth values in the archive's raw
scientific-notation form before conversion to standard notation for the report table).

**Data feasibility: HIGH.** Named source checked live this session:
- NASA Exoplanet Archive (`https://exoplanetarchive.ipac.caltech.edu/`) — confirmed live this
  session; hosts data on over 6,000 confirmed planets plus a dedicated Transiting Planets table and
  Transit & Ephemeris Service, with period, radius and transit-depth fields exportable as CSV
  (including in scientific notation), across multiple real survey missions (TESS, Kepler, K2) that
  each publish per-field candidate counts — exactly what a 12-field shallow-survey scenario needs.

Not confident about: the exact per-field detection-probability figure for a *hypothetical* new
12-field survey (as opposed to a completed mission's realized yield) — `case-research` will likely
need to derive a stated per-field rate from a real completed survey's realized candidate-per-field
statistics, disclosed as the modeling basis, not invented.

**Sensitivity (SPEC §6).** None required.

**Split risk.** None — 6 scored skills plus 3 reinforcement, one coherent scheduling-decision arc.

---

### C3 — The Marginal Detection   ·   score 4.6   ·   tier T2

**Protagonist.** Ingrid Solberg, an exoplanet-survey lead reviewing an overnight pipeline flag: one
candidate's transit signal just cleared 3-sigma significance, barely.

**The dilemma.** A.) Spend tomorrow's follow-up slot re-observing the marginal 3-sigma candidate to
try to firm it up OR B.) abandon it and spend the slot on a fresh, unexamined target instead
(`domains.json`'s own archetype #3, verbatim).

**Primary metric.** Signal depth as a multiple of the baseline noise's spread (the light curve's
dip size ÷ its own out-of-transit scatter) — a ratio, not a raw flux drop, because a "big" dip in a
noisy star's data can be less significant than a small dip in a quiet one.

**Why it's close.** The out-of-transit baseline in real light-curve data (both AAVSO's variable-star
photometry and the Exoplanet Archive's light curves show this) is rarely flat — it drifts, and that
drift is often visibly non-linear rather than a straight trend, so fitting a naive straight
line-of-best-fit and reading the residual dip against it can overstate or understate the
significance depending on where in the drift the transit fell. A box-and-whisker plot of the
baseline's own scatter gives a defensible, distribution-based read on "how big is normal noise here"
that a single sigma number can hide. Whether the marginal detection is worth the slot turns on
which of those two reads — the naive fit or the distribution-aware one — the team trusts.

**Would close (3 skills, 2 how-to / 1 term, closing 3/3 remaining thin in Statistics And
Probability/Displaying Data):**

| id | kind | label | n |
|---|---|---|---|
| statistics-and-probability-non-linear | term | Non-linear | 2 |
| statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data | how-to | How to draw a line of best fit given a set of data | 2 |
| statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data | how-to | How to create a box and whisker plot given a set of data | 1 |

**Already-covered skills it also exercises.** `statistics-and-probability-outlier` (n=3);
`statistics-and-probability-scatter-plot` / `how-to-create-a-scatter-plot-given-a-set-of-data` (n=9
each, plotting the raw flux time series); `statistics-and-probability-correlation` /
`how-to-identify-correlation-given-a-scatter-plot-or-set-of-data` (n=3 each); `statistics-and-
probability-quartiles` (n=3, feeds the box-and-whisker).

**Data feasibility: HIGH.** Named sources checked live this session:
- AAVSO (`https://aavso.org/`) — confirmed live this session (74M+ submitted observations, 10.4M
  variable-star database, a light-curve generator tool); real photometric time series with visible
  baseline drift are exactly what this case's noise-distribution argument needs.
- NASA Exoplanet Archive (`https://exoplanetarchive.ipac.caltech.edu/`) — confirmed live (see C2);
  its per-target light curves are the other candidate source for the marginal-detection data itself.

Not confident about: a specific *already-flagged* 3-sigma marginal candidate's raw light curve being
posted in one place — `case-research` will likely need to construct the "marginal" framing around a
real target's real light curve rather than a documented borderline case.

**Sensitivity (SPEC §6).** None required.

**Split risk.** None — 3 scored skills, small, single deliverable arc.

---

### C4 — The Parallax Baseline   ·   score 1.8   ·   tier T3

**Protagonist.** Marcus Villanueva, an astrometry calibration lead at a small college observatory,
deciding how to spend the department's one guaranteed observing semester on distance measurements
for a target list.

**The dilemma.** A.) Run a single-observatory six-month baseline (Earth's own orbital diameter,
cheap, fast, standard precision) OR B.) coordinate a synthetic longer baseline with a partner
observatory's simultaneous data (more scheduling and data-sharing overhead, better precision for the
more distant half of the target list).

**Primary metric.** Distance uncertainty as a percentage of the measured distance — a ratio, since
raw parallax angle sizes are not comparable target-to-target the way a percent uncertainty is.

**Why it's close.** The standard classroom parallax model treats Earth-Sun-star as a right triangle
(right angle at the Sun, the 1 AU Earth-Sun distance as one leg, the star's distance as the other),
which only works because the parallax angle is small enough that the triangle stays valid — checking
that against the triangle inequality theorem is a real, non-decorative step once the two baseline
options produce two different triangle shapes (both scalene, since none of the three real-world
lengths involved are ever equal) with very different angle sizes. Whether the longer, coordinated
baseline's precision gain is worth its overhead genuinely depends on computing both triangles, not
assuming the longer one always wins.

**Would close (3 skills, all term, closing 3/6 remaining thin in Geometry/Triangles — does not close
the group):**

| id | kind | label | n |
|---|---|---|---|
| geometry-scalene-triangle | term | Scalene Triangle | 2 |
| geometry-triangle-inequality-theorem | term | Triangle Inequality Theorem | 2 |
| geometry-leg | term | Leg | 2 |

**Already-covered skills it also exercises.** `geometry-right-triangle` (n=5); `geometry-hypotenuse`
(n=4); `pre-calculus-radian` / `pre-calculus-reference-angle` (n=4, n=3 — converting the parallax
angle from arcseconds to radians for the small-angle model); `advanced-operations-scientific-
notation` (n=4, distances in km vs. parsecs).

**Data feasibility: HIGH.** Named source checked live this session:
- ESA Gaia Data Release 3 / Gaia Archive (`https://www.cosmos.esa.int/web/gaia/data-release-3`,
  archive at `archives.esac.esa.int/gaia`) — confirmed live this session; publishes real parallax
  measurements with uncertainties for over a billion stars, exactly the raw numbers a real
  short-vs-long-baseline precision comparison needs.

Not confident about: the coordination/overhead cost of a real cross-observatory baseline campaign —
that side of the decision will need to be a stated Modeling Assumption, not a sourced figure.

**Sensitivity (SPEC §6).** None required.

**Split risk.** Low score is a coverage problem, not a scope problem — recommend not writing as-is;
it would need to be paired with a second thin group (e.g. merged with C2's Probability closure, or
reframed to also force `geometry-acute-triangle` / `geometry-obtuse-triangle` by classifying the two
baseline options' triangle shapes) before it clears the Cold Chain 4.2 anchor.
