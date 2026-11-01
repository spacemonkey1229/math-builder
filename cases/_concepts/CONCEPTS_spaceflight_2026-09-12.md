# Concept sheet — Spaceflight & Orbital Mechanics (`spaceflight`)

**Target and why (one line).** `readmodel/domains.json`'s `spaceflight` entry is HIGH authoring
priority, HIGH data grade, and carries **0 existing cases** (`existing_cases: []`,
`n_uncovered_signature_skills: 0` — its 13 signature skills are all already covered elsewhere in
the corpus, which just means the domain itself has never been the *frame* for a case, not that it
lacks a real gap to close). Its `math_branches[]` list includes `linear-algebra`, and this project's
own `README.md` names Linear Algebra (44%) as one of the two weakest branches with pre-existing case
coverage — a genuine reason to look here. In practice the legacy spine has no separate
Linear-Algebra domain (`curriculum_tree.json` maps the `linear-algebra` branch to the legacy
`Geometry` domain via `acton_domains: ["Geometry"]`), so "linear-algebra" skills in this corpus live
under Geometry/Transformations and Geometry/Coordinate Plane — I checked both live and used them
where genuinely forced (see C4 below), but did not inflate a case around them just to claim the
branch.

**Scoring note.** A spine-wide sweep this session confirmed zero skills anywhere in the 437-skill
spine sit at true `n==0`; every concept below is scored against `gap_queue.json`'s own thin
convention (`n<=2`), with each skill's live `n` shown so `case-write` knows none of these are
"first case ever" claims. I re-pulled every id, label, and `n` directly from
`readmodel/standards_spine.json` this session (not from `domains.json`'s cached `signature_skills`,
which are mostly already well-covered and would score nothing). One live collision found and
avoided: `cases/the-turbine-channel/case.json` (already in the corpus, oceanography-framed) already
claims all 7 Calculus/Integrals skills — I did not re-propose that group here to avoid two concepts
chasing the same thin group.

| # | Concept | Score | Tier | Group(s) closed |
|---|---|---|---|---|
| C1 | The Conjunction Call | **5.8** | T3 | Advanced Operations / Scientific Notation, Factorial, Absolute Value (5/5 remaining thin) |
| C2 | The Apogee Call | **5.6** | T4 | Calculus / Applications Of Derivatives (1/1 remaining thin) + 3 of 4 Derivatives thin skills |
| C3 | The Constellation Bid | **4.2** | T3 | Pre-Calculus / Trigonometric Functions (3/3 remaining thin) |
| C4 | The Range Safety Call | **2.52** | T2 | Geometry / Transformations (3/3 remaining thin) |

**Recommendation.** Write **C1, The Conjunction Call** first — it closes an entire thin group (all
5 remaining `n<=2` skills in Advanced Operations/Scientific Notation-Factorial-Absolute-Value) with
every skill genuinely forced by real satellite conjunction-assessment math (not decorative), and its
core data source, CelesTrak's SOCRATES Plus service, is confirmed live this session with exactly the
fields the case needs (miss distance, collision probability, time of closest approach). **C2** is the
strongest runner-up and the most rigorous (T4, genuine chain/product-rule derivative work on a real
orbital-decay style model) — write it second. **C3** is a fine third pick — real and clean
(right-ascension/true-anomaly angles are literally unit-circle trigonometry) but its cost data is
only MEDIUM, so treat launch pricing as a stated Modeling Assumption, not a sourced figure. **Kill or
defer C4** for this round: its score (2.52) sits well under Cold Chain's 4.2 calibration anchor, its
data source (FAA AST debris-risk methodology) is an unverified category guess this session, and its
subject matter (debris-footprint casualty risk) needs the SPEC §6 protection-framing rewrite noted
below before it's writable at all.

---

### C1 — The Conjunction Call   ·   score 5.8   ·   tier T3

**Protagonist.** Priya Nakamura, a satellite operations engineer for a small-satellite operator,
personally responsible for signing off on the fleet's collision-avoidance decisions this week.

**The dilemma.** A.) De-orbit the aging, low-fuel satellite now, ending its remaining useful data
collection early OR B.) keep it flying through the current debris-conjunction season, spending its
last reserve propellant on a collision-avoidance maneuver if a close approach materializes. (This is
`domains.json` spaceflight's own decision archetype #3, verbatim.)

**Primary metric.** Expected remaining data-collection days protected per kilogram of reserve
propellant spent (a ratio — total data days isn't the question, since option A trivially has zero
maneuver cost; the question is whether the *protected* days per kg justify the fuel).

**Why it's close.** De-orbiting now is certain and cheap but throws away paid-for, still-working
sensor time. Waiting keeps the satellite earning, but the debris field it shares an altitude band
with has dozens of tracked objects, and evaluating real risk means counting every *pairwise*
close-approach possibility among them (a combinatorics problem, not a single number), comparing tiny
probability figures given in scientific notation against a fixed risk threshold, and measuring how
far a predicted miss distance deviates from that threshold in absolute terms. The math is what turns
"space is big, it'll probably be fine" into an actual defensible number.

**Would close (5 skills, 2 how-to / 3 term, all currently n=2, all of Advanced Operations/Scientific
Notation-Factorial-Absolute-Value's remaining thin skills):**

| id | kind | label | n |
|---|---|---|---|
| advanced-operations-standard-notation | term | Standard Notation | 2 |
| advanced-operations-factorial | term | Factorial | 2 |
| advanced-operations-absolute-value | term | Absolute Value | 2 |
| advanced-operations-how-to-write-a-number-in-standard-notation-given-its-scientific-notation | how-to | How to write a number in standard notation given its scientific notation | 2 |
| advanced-operations-how-to-evaluate-a-factorial-expression | how-to | How to evaluate a factorial expression | 2 |

**Already-covered skills it also exercises.** `advanced-operations-scientific-notation` (n=4 — miss
probabilities and mass figures are natively reported in scientific notation, e.g. 3.2×10⁻⁴);
`advanced-operations-how-to-write-a-number-in-scientific-notation-given-its-standard-notation` (n=4);
`measurement-how-to-convert-an-amount-with-compound-units` (n=18, kg of propellant per m/s of
delta-v for the avoidance burn).

**Data feasibility: HIGH.** Named source I checked live this session:
- CelesTrak SOCRATES Plus (`https://celestrak.org/SOCRATES/`) — confirmed live; publishes
  three-times-daily conjunction screening of every active payload against the full tracked-object
  catalog, with minimum distance, maximum collision probability, time of closest approach, relative
  speed, and NORAD catalog numbers for both objects — exactly the fields this case needs.

Not confident about: a specific *named* small-satellite operator's actual remaining fuel budget and
per-maneuver propellant cost — those will be a disclosed, stated scenario assumption built around a
real small-sat propulsion system's published specific-impulse figure, not an invented number.

**Sensitivity (SPEC §6).** None required — an engineering/operations decision about hardware and
data value, not personal or human-casualty stakes.

**Split risk.** None — 5 scored skills plus reinforcement, well under the 8–15 range; one coherent
deliverable arc (count conjunctions → screen probabilities → compare against threshold → decide).

---

### C2 — The Apogee Call   ·   score 5.6   ·   tier T4

**Protagonist.** Marcus Webb, a mission design engineer at a small launch-services company, who has
to recommend one transfer-orbit plan to a satellite customer before the week's trajectory-design
review.

**The dilemma.** A.) Transfer Orbit Alpha — a faster, higher-thrust ellipse that reaches a higher
apogee sooner but burns more propellant OR B.) Transfer Orbit Beta — a slower, lower-thrust ellipse
that reaches a lower apogee, coasts longer, and needs a larger circularization burn once it arrives.

**Primary metric.** Useful payload mass delivered to the target circular orbit per kilogram of total
mission propellant (a ratio — total delta-v isn't the question, since a bigger rocket trivially wins
on totals; the question is what each option costs per kilogram actually delivered).

**Why it's close.** Each transfer orbit's altitude as a function of time is a real, physically
motivated composite function (altitude climbs, decelerates near apogee, and the *rate* at which it
climbs is itself changing) — finding the instantaneous climb rate at a given moment requires the
chain rule (the altitude function is composed with a time-scaling term specific to each orbit's
period), and finding the rate at which the climb rate itself is changing near the turnover point
uses the product rule (velocity is genuinely a product of a radius term and an angular-rate term in
this model). The apogee itself — the point Alpha and Beta trade off — is a local maximum found the
same way an economist finds a maximum profit: by testing where the derivative is zero. A tangent
line at the current tracked position is what mission control actually uses for a short-horizon
"are we tracking the model" check before committing to the circularization burn.

**Would close (4 skills, 3 how-to / 1 term):**

| id | kind | label | n | group |
|---|---|---|---|---|
| calculus-how-to-use-the-chain-rule-to-differentiate-a-composite-function | how-to | How to use the chain rule to differentiate a composite function | 1 | Derivatives |
| calculus-how-to-use-the-product-rule-to-differentiate-a-product-of-functions | how-to | How to use the product rule to differentiate a product of functions | 2 | Derivatives |
| calculus-how-to-find-the-equation-of-a-tangent-line-at-a-point | how-to | How to find the equation of a tangent line at a point | 2 | Derivatives |
| calculus-local-maximum | term | Local Maximum | 2 | Applications Of Derivatives — 1/1 remaining thin skill, fully closed |

**Honestly not claimed.** `calculus-how-to-use-the-quotient-rule-to-differentiate-a-quotient-of-functions`
(n=1, also thin in the same Derivatives group) is deliberately left off this list — nothing in this
altitude/velocity model genuinely requires dividing two functions of the same variable, and forcing
one in would be exactly the "coverage-inflation" the parent skill warns against. `case-write` may
find a genuine quotient-rule moment (e.g. specific-orbital-energy rate); if so it's a bonus, not a
claim made here.

**Already-covered skills it also exercises.** `calculus-derivative` (n=5); `calculus-instantaneous-rate-of-change`
(n=4); `calculus-tangent-line` (n=3); `calculus-how-to-find-a-derivative-using-the-power-rule` (n=5);
`calculus-how-to-find-critical-points-of-a-function` / `how-to-use-the-first-derivative-test-to-classify-a-critical-point`
(n=5 each, used to actually classify the apogee as a maximum).

**Data feasibility: HIGH.** Named sources checked live this session:
- JPL Horizons (`https://ssd.jpl.nasa.gov/horizons/`) — confirmed live; provides free public,
  highly accurate ephemerides for spacecraft, including transfer-trajectory-style orbital data, via
  web, command-line, or API access.
- CelesTrak (`https://celestrak.org/`, confirmed live via its `/SOCRATES/` subpage this session) —
  publishes current orbital elements (TLEs) for tracked objects, from which period and altitude are
  directly derivable.

Not confident about: a real, named commercial transfer-orbit trade study with both options' exact
thrust profiles disclosed (proprietary) — `case-research` should build the altitude-vs-time model
from public orbital-mechanics formulas applied to real orbital elements, disclosed as the modeling
choice, not sourced from a leaked internal document.

**Sensitivity (SPEC §6).** None required — a commercial engineering trade-off, no personal stakes.

**Split risk.** None — 4 scored skills across two adjacent, physically-linked groups (finding the
apogee is the same computation that produces the climb-rate answer); one coherent deliverable arc.

---

### C3 — The Constellation Bid   ·   score 4.2   ·   tier T3

**Protagonist.** Aisha Odom, a satellite constellation architect at a small-sat operator, who has to
recommend one launch strategy to the board before the launch-slot deposit is due.

**The dilemma.** A.) Launch all 60 satellites on one large rocket into a single orbital plane, then
have each satellite spend its own propellant walking to its final plane OR B.) launch on six smaller
rockets, one per target plane, so every satellite arrives already in its assigned plane. (This is
`domains.json` spaceflight's own decision archetype #1, verbatim.)

**Primary metric.** Constellation coverage (satellites correctly placed in their target plane) per
dollar of total launch cost (a ratio — Option A's single rocket is cheaper per kilogram launched,
but "launched" isn't "correctly placed," so raw launch cost alone can't settle it).

**Why it's close.** Every satellite's position within its orbital plane is described by an angle
(true anomaly) measured the same way any angle on a unit circle is measured — sine and cosine give
its coordinates in the plane, and the tangent function is what a ground-station analyst uses to work
out a satellite's elevation angle as it comes over the horizon. Option A requires computing, for each
of six target planes, how far around the unit circle a satellite must effectively "walk" using its
own fuel, which costs mass; Option B needs no such walk but costs more per kilogram at launch. Which
wins depends on exactly how much of that walking angle is required — not obvious until it's measured.

**Would close (3 skills, 1 how-to / 2 term, all currently n=2, all of Trigonometric Functions'
remaining thin skills):**

| id | kind | label | n |
|---|---|---|---|
| pre-calculus-unit-circle | term | Unit Circle | 2 |
| pre-calculus-tangent-function | term | Tangent Function | 2 |
| pre-calculus-how-to-find-the-sine-cosine-and-tangent-of-an-angle-using-the-unit-circle | how-to | How to find the sine, cosine, and tangent of an angle using the unit circle | 2 |

**Already-covered skills it also exercises.** `pre-calculus-sine-function` / `pre-calculus-cosine-function`
(n=3/4); `pre-calculus-radian` / `how-to-convert-between-degrees-and-radians` (n=4 each — orbital
angles are natively given in degrees or radians and need converting); `geometry-circumference` /
`geometry-how-to-find-the-measure-of-the-circumference-of-a-circle` (already-covered spaceflight
signature skills, orbital-plane geometry).

**Data feasibility: HIGH for the trigonometry/orbital-angle side, MEDIUM for launch cost.** Named
sources checked live this session:
- CelesTrak (`https://celestrak.org/`, confirmed live) — publishes current TLEs, from which
  right-ascension-of-ascending-node and true-anomaly angles for real satellites are directly
  computable — this is what genuinely drives the trig skills above.
- GCAT (`https://planet4589.org/space/gcat/`) — confirmed live this session; free public catalog
  (CC-BY licensed) of every launch with payload data.

Not confident about: a specific, current, published per-launch price for a rideshare vs. dedicated
small-sat launch — I attempted to confirm SpaceX's and Rocket Lab's public pricing pages live this
session and both failed to load cleanly (a stale/incorrect SpaceX PDF URL, a 403 from Rocket Lab's
site). `case-research` should use a stated, dated list-price figure with an explicit "as of" capture
date per SPEC §5, not a number pulled from this brief.

**Sensitivity (SPEC §6).** None required.

**Split risk.** None — 3 scored skills, small, single deliverable arc.

---

### C4 — The Range Safety Call   ·   score 2.52   ·   tier T2   ·   NOT RECOMMENDED THIS ROUND

**Protagonist.** Dana Ruiz, a launch range safety analyst, who must clear one of two proposed launch
azimuths before a scheduled launch window.

**The dilemma.** A.) Launch Azimuth North — a corridor whose debris-dispersion footprint, if the
vehicle fails, is a wide ellipse over a mostly unpopulated stretch of ocean OR B.) Launch Azimuth
South — a narrower footprint (safer-looking by area alone) that clips the edge of a populated coastal
zone.

**Primary metric.** *(Needs a §6 rewrite before this is writable — see below.)*

**Would close (3 skills, 2 term / 1 how-to, all currently n=2, all of Geometry/Transformations'
remaining thin skills):**

| id | kind | label | n |
|---|---|---|---|
| geometry-congruent | term | Congruent | 2 |
| geometry-similar | term | Similar | 2 |
| geometry-how-to-reflect-a-figure-across-the-y-axis | how-to | How to reflect a figure across the Y-Axis | 2 |

**Why the forcing is weaker than C1–C3.** A debris footprint scaled by a different failure-dispersion
factor is genuinely a similar ellipse; two footprints from a shared launch-pad geometry but mirrored
azimuths are a genuine reflection. But this is a thinner physical justification than C1–C3's, and
"congruent" specifically is not obviously forced (two footprints are rarely identical in this
scenario) — flagging that risk honestly rather than asserting it's solid.

**Data feasibility: MEDIUM.** I did not confirm a specific live source this session (only described
the category, per the brainstorm norm of not over-claiming). FAA AST publishes launch/reentry debris
risk methodology publicly and US Census provides population density; neither was checked live this
session, so this stays MEDIUM until `case-research` verifies a specific document.

**Sensitivity (SPEC §6): REQUIRED, and the concept needs reframing before it's written.** As
currently framed ("expected casualties," `domains.json`'s own career description for this role) this
is exactly the "optimize human death tolls as an abstract quantity" pattern SPEC §6 warns against.
Before this concept is writable it needs the same reframe SPEC recommends for Airstrike-adjacent
material: state the metric as *population kept clear of the footprint per dollar of trajectory
adjustment* (protection) rather than expected casualties (destruction), and it still needs a
facilitator sensitivity note for the discussion lead.

**Split risk.** None — 3 skills, small.

**Recommendation for this one specifically.** Defer. Verify a real FAA AST source and rewrite the
metric to a protection framing before treating this as a real candidate; it scores under the Cold
Chain 4.2 anchor as written and touches sensitive subject matter without the required rewrite.
