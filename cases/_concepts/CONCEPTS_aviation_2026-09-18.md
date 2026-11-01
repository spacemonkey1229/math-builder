# Concept sheet — Aviation & Air Traffic — 2026-09-18

Target domain: `readmodel/domains.json` → `aviation` (cluster "Movement & Logistics"). Spine sweep
(2026-09-18) confirms the whole spine currently has **zero skills at n==0** — the same state
`the-turbine-channel` found on 2026-09-11 — so every concept below is scored on the
reinforcement-carve-out basis (SPEC §8 exception, `skills/case-readiness/SKILL.md` "reinforcement
carve-out on T1-10"): honestly checked for the thinnest reachable group, not a fabricated
`new_coverage[]`. Thinnest aviation-reachable group found: **Pre-Calculus/Vectors — 7/7 skills,
every one at n=3** (`pre-calculus-vector`, `pre-calculus-magnitude-of-a-vector`,
`pre-calculus-unit-vector`, `pre-calculus-dot-product`, and their three how-tos). Secondary:
Geometry/Triangles (Pythagorean Theorem n=6, Hypotenuse n=4) and Measurement/Time (elapsed-time
family, n=3–16).

| # | Title | score | tier | feasibility |
|---|---|---|---|---|
| C1 | **Wind Call** | 8.4 | T4 | HIGH |
| C2 | Holding Pattern | 5.6 | T3 | MEDIUM |
| C3 | Gate Bank | 4.9 | T2 | MEDIUM |

**Recommendation:** Write **C1 — Wind Call**. It closes the entire Pre-Calculus/Vectors group
(the thinnest reachable group for this domain) with a real wind-triangle problem — the textbook
use case for vector addition and the dot product — grounded in real, live-fetchable FAA/NOAA wind
data and a real published aircraft performance sheet. C2 (holding pattern fuel math) and C3 (gate
scheduling) are killed: C2 leans on ATC holding procedures that don't reach Vectors at all (mostly
re-covers already-thick Measurement/Time skills), and C3 is a scheduling case that reinforces
nothing thin.

---

### C1 — Wind Call   ·   score 8.4   ·   tier T4

**Protagonist.** A flight dispatcher at a Part 135 cargo/feeder operator flying Cessna 208B Grand
Caravans, who must lock the dispatch release (altitude, routing, fuel load) before a hard
paperwork cutoff.

**The dilemma.** A.) File the flight at 9,000 ft ("Niner-Thousand") — below the 12,500 ft
supplemental-oxygen threshold OR B.) File at 18,000 ft ("One-Eight-Thousand") — requires
supplemental oxygen under 14 CFR 91.211, but the winds aloft differ.

**Primary metric.** Gallons of Jet-A burned per nautical mile of net progress toward the
destination (ratio).

**Why it's close.** The Caravan's true airspeed (180 kn) dominates either wind vector, so the two
options' fuel-per-mile figures land within roughly 1% of each other once the wind triangle is
solved for each altitude — genuinely close, in the spirit of SPEC §2's own gold-standard example
(Route 1 beating Route 2 by 0.09%). The regulatory cost of Option B (mandatory oxygen) is real and
has to be weighed against a wind advantage that may not be large enough to justify it — that
tension is the whole case.

**Would close (12 skills, 7 how-to / 5 term):**
| id | kind | label |
|---|---|---|
| pre-calculus-vector | term | Vector |
| pre-calculus-magnitude-of-a-vector | term | Magnitude (Of A Vector) |
| pre-calculus-unit-vector | term | Unit Vector |
| pre-calculus-dot-product | term | Dot Product |
| pre-calculus-how-to-find-the-magnitude-and-direction-of-a-vector | how-to | How to find the magnitude and direction of a vector |
| pre-calculus-how-to-add-and-subtract-vectors | how-to | How to add and subtract vectors |
| pre-calculus-how-to-find-the-dot-product-of-two-vectors | how-to | How to find the dot product of two vectors |
| geometry-pythagorean-theorem | term | Pythagorean Theorem |
| geometry-hypotenuse | term | Hypotenuse |
| measurement-how-to-find-elapsed-time | how-to | How to find elapsed time |
| measurement-how-to-convert-an-amount-with-compound-units | how-to | How to convert an amount with compound units |
| statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data | how-to | How to create a scatter plot given a set of data (vector diagram plotted to scale on a coordinate grid) |

**Data feasibility: HIGH.** Named sources I expect to exist and (for brainstorm purposes) have
reason to believe are live: FAA/NOAA `aviationweather.gov` winds-aloft (FB) data API (real,
publicly queryable); AOPA's published Cessna 208B Grand Caravan aircraft fact sheet (cruise TAS,
fuel burn, usable fuel); real published airport coordinates (FAA/Wikipedia) for a great-circle
distance and true-course calculation; 14 CFR 91.211 (eCFR, the actual regulation text). Not
confident about: a full per-altitude cruise fuel-flow chart for this aircraft freely online — the
manufacturer POH PDF is large/paywalled-adjacent on secondary hosts; likely resolves as a stated,
disclosed Modeling Assumption (fuel flow held constant across the two altitudes).

**Sensitivity (SPEC §6).** NONE — a siting/logistics decision, no death/illness/hardship stakes.

**Split risk.** NONE — 12 skills is within the single-case range (SPEC's 8–15 guidance), and every
one is genuinely forced by a named deliverable (see LEARNING_GOALS.md once written).

---

### C2 — Holding Pattern · score 5.6 · tier T3

**Protagonist.** A tower/approach controller deciding whether to hold an inbound regional jet or
clear it straight in, given fuel remaining and a closing weather ceiling.
**Killed because:** the natural math here (elapsed time, rate × time, percent of fuel reserve) all
lands in already-thick spine groups (Measurement/Time is 12–16 deep on its relevant skills) and
never reaches Vectors or any comparably thin group. Real data (BTS delay causes, AWC METAR/TAF)
is available but the skill yield doesn't clear the bar C1 clears.

### C3 — Gate Bank · score 4.9 · tier T2

**Protagonist.** An airport operations planner choosing between adding a fifth gate or re-timing a
departure bank to cut turnaround conflicts.
**Killed because:** the deliverables are almost entirely scheduling arithmetic (elapsed time,
percent) with no natural path to Vectors, Triangles, or any thin group; would mostly re-cover
already-saturated Measurement and Percent skills.

**Next step:** Approve C1, then run case-write on it.
