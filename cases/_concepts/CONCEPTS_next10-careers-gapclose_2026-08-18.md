# Next 10 Case Concepts — gap-driven, career-weighted

Target selection: the 10 spine groups with the highest zero-coverage counts that do not already
have a concept or in-flight case against them (excludes `redrawing-lines`/precalc-calc-discrete
concepts C9/C12 already in the pipeline). Every protagonist below is a **working professional**,
by design — see the companion assessment (career/profession distribution) for why: 5 of the last
6 legacy conversions used a family or an individual with no professional role, and this batch
corrects that ratio deliberately, per instruction to weight careers and professions.

| # | Concept | Target group(s) | Career | Skills closed | Feasibility | Score |
|---|---|---|---|---|---|---|
| C1 | Grant Reach | Discrete Math / Set Theory (8/8 zero) | Financial Aid Outreach Coordinator | 8 (2 how-to / 6 term) | HIGH | 7.6 |
| C2 | The Contrapositive Claim | Discrete Math / Formal Logic (7/8 zero) | Insurance Claims Auditor | 7 (2 how-to / 5 term) | MEDIUM | 5.0 |
| C3 | The Multiplier Recruit | Pre-Calculus / Matrices (7/7 zero) | Regional Economic Development Analyst | 7 (3 how-to / 4 term) | HIGH | 7.4 |
| C4 | The Fan Formation | Pre-Calculus / Polar And Parametric (6/6 zero) | Drone Show Flight Programmer | 6 (3 how-to / 3 term) | HIGH | 6.8 |
| C5 | The Reserve Asymptote | Pre-Calculus / Introduction To Limits (5/5) + Calculus / Limits And Continuity (6/6) | Actuarial Analyst | 11 (4 how-to / 7 term) | HIGH | 12.2 |
| C6 | The Tracker's Angle | Pre-Calculus / Trigonometric Identities (5/5 zero) | Solar Installation Design Engineer | 5 (3 how-to / 2 term) | HIGH | 6.2 |
| C7 | The Roofline Call | Geometry / Fundamentals Of Geometry (8 zero / 24) | Residential Architectural Drafter | 8 (0 how-to / 8 term) | MEDIUM | 4.8 |
| C8 | The Irregular Boundary | Geometry / Quadrilaterals And Polygons (5 zero / 22) | Precision-Ag GIS Land-Use Analyst | 5 (0 how-to / 5 term) | MEDIUM | 3.0 |
| C9 | Prove It Scales | Discrete Math / Proof And Recursion (4/7 zero) | Software / Algorithm Engineer | 4 (1 how-to / 3 term) | MEDIUM | 2.8 |
| C10 | The Cheap Approximation | Calculus / Series (4/5 zero) | Embedded Systems / Firmware Engineer | 4 (2 how-to / 2 term) | MEDIUM | 3.2 |

**Recommendation.** Write **C5 (The Reserve Asymptote)** first — it is the single highest-value
concept in the current pipeline including everything already in `_concepts/`: it closes two full
spine groups (11 skills, both zero-coverage, HIGH feasibility off SOA/CDC public mortality and
reserve tables) in one case, and Actuarial Analyst is a career with zero prior representation in
the corpus. Write **C1 (Grant Reach)** and **C3 (The Multiplier Recruit)** next — both HIGH
feasibility, both close a full group, both untapped careers (financial aid, regional econ dev).
Hold **C8** and **C9** — MEDIUM feasibility on both and the smallest raw scores in the batch;
revisit once `case-research` confirms a source for one of the HIGH-graded concepts above, since a
confirmed source sometimes turns up adjacent data for the MEDIUM ones too.

---

### C1 — Grant Reach   ·   score 7.6   ·   tier T2
**Protagonist.** Deja Whitfield, financial aid outreach coordinator at a mid-size public
university. Her office's mailing budget is fixed; she has to decide who gets a printed reminder
packet before the FAFSA renewal deadline.
**The dilemma.** A.) Mail packets to every student in the *union* of "Pell-eligible" and
"state-grant-eligible" (broad reach, higher cost) OR B.) Mail only to the *intersection* — students
eligible for both (narrower reach, funded entirely by the state-grant admin allowance, no
university budget spent).
**Primary metric.** Dollars of university budget spent per student who actually renews aid on time.
**Why it's close.** The union reaches more students and probably nets more renewals in absolute
terms, but every one of those extra mailers comes out of the university's own budget; the
intersection is free (state grant funds cover it) but reaches a visibly smaller set — the
question is whether the union's extra reach is worth its extra cost per renewal, not whether more
mail is better.
**Would close (8 skills, 2 how-to / 6 term):**
| id | kind | label |
|---|---|---|
| discrete-mathematics-set | term | Set |
| discrete-mathematics-subset | term | Subset |
| discrete-mathematics-union | term | Union |
| discrete-mathematics-intersection | term | Intersection |
| discrete-mathematics-empty-set | term | Empty Set |
| discrete-mathematics-venn-diagram | term | Venn Diagram |
| discrete-mathematics-how-to-find-the-union-and-intersection-of-two-sets | how-to | How to find the union and intersection of two sets |
| discrete-mathematics-how-to-represent-a-set-relationship-using-a-venn-diagram | how-to | How to represent a set relationship using a Venn diagram |
**Data feasibility: HIGH.** Named sources: U.S. Dept. of Education Federal Pell Grant end-of-year
reports (income-eligibility bands and headcounts by state); individual state grant agency
published eligibility income thresholds (most state grant agencies publish these, e.g., a state
higher-ed finance authority's award-year eligibility table); USPS commercial mail rate table for
the per-piece cost. Not confident about: renewal-rate-by-outreach-method — that will likely need
a stated Modeling Assumption tied to a published higher-ed-marketing benchmark.
**Sensitivity (SPEC §6).** NONE — routine administrative operations math, no protected-subject
sensitivity.
**Split risk.** NONE — 8 skills, one group, clean fit.

### C2 — The Contrapositive Claim   ·   score 5.0   ·   tier T2
**Protagonist.** Marisol Aguon, senior claims auditor at a mid-size property insurer. She
reviews denied claims flagged for appeal and has to decide which review standard the appeals
team should apply going forward.
**The dilemma.** A.) Apply the policy's conditional clause literally as written ("if damage was
caused by flood, coverage is denied") OR B.) Apply its contrapositive as the audit standard
("if coverage was not denied, damage was not caused by flood") to catch clauses adjusters
misapplied in the other direction.
**Primary metric.** Wrongly-denied claims caught per 100 appeals reviewed, under each standard.
**Why it's close.** The literal reading is faster to apply and matches what adjusters were
trained on, but a conditional and its contrapositive are logically equivalent while its converse
and inverse are not — the case turns on whether the appeals team has actually been applying the
converse (a common, real error) instead of the true contrapositive, and how much that costs to
find versus how much it costs to keep training front-line adjusters on the distinction.
**Would close (7 skills, 2 how-to / 5 term):**
| id | kind | label |
|---|---|---|
| discrete-mathematics-conjunction | term | Conjunction |
| discrete-mathematics-disjunction | term | Disjunction |
| discrete-mathematics-negation | term | Negation |
| discrete-mathematics-conditional-statement | term | Conditional Statement |
| discrete-mathematics-truth-table | term | Truth Table |
| discrete-mathematics-how-to-construct-a-truth-table-for-a-compound-statement | how-to | How to construct a truth table for a compound statement |
| discrete-mathematics-how-to-determine-the-converse-inverse-and-contrapositive-of-a-conditional-statement | how-to | How to determine the converse, inverse, and contrapositive of a conditional statement |
**Data feasibility: MEDIUM.** Named sources: state Departments of Insurance publish annual
consumer complaint/appeal-outcome ratios by carrier (many DOI market conduct reports are public);
NAIC market conduct annual statement data. Not confident about: a real carrier's internal
literal-vs-contrapositive audit hit-rate — that number does not exist publicly and will need a
stated Modeling Assumption anchored to the DOI appeal-overturn-rate base.
**Sensitivity (SPEC §6).** LOW — insurance claim denial is mildly sensitive; keep the scenario
property/auto, not health or life, to stay clear of SPEC §6's higher-sensitivity categories.
**Split risk.** NONE.

### C3 — The Multiplier Recruit   ·   score 7.4   ·   tier T2
**Protagonist.** Ben Okafor, regional economic development analyst for a county industrial
development authority. He has one incentive package to offer and two employers competing for it.
**The dilemma.** A.) Recruit Employer A (a component manufacturer with heavy local supplier
purchasing) OR B.) Recruit Employer B (a logistics/distribution center with fewer local supplier
ties but more direct jobs).
**Primary metric.** Total regional jobs supported per $1 of incentive, computed by solving the
region's input-output relationships (a system of linear equations) via matrix methods, using each
employer's direct-jobs and local-purchasing profile as the input vector.
**Why it's close.** Employer B creates more direct jobs per dollar, but Employer A's spending
ripples further through the regional supply chain (a higher output multiplier) — you cannot see
which wins without actually solving the system, which is the point of using a matrix instead of
just adding up direct jobs.
**Would close (7 skills, 3 how-to / 4 term):**
| id | kind | label |
|---|---|---|
| pre-calculus-matrix | term | Matrix |
| pre-calculus-matrix-dimension | term | Matrix Dimension |
| pre-calculus-determinant | term | Determinant |
| pre-calculus-identity-matrix | term | Identity Matrix |
| pre-calculus-how-to-add-and-multiply-matrices | how-to | How to add and multiply matrices |
| pre-calculus-how-to-find-the-determinant-of-a-2x2-matrix | how-to | How to find the determinant of a 2x2 matrix |
| pre-calculus-how-to-solve-a-system-of-equations-using-a-matrix | how-to | How to solve a system of equations using a matrix |
**Data feasibility: HIGH.** Named sources: U.S. Bureau of Economic Analysis RIMS II regional
input-output multipliers (published, purchasable table of output/employment multipliers by
region and industry — the standard real-world tool this exact job uses); BEA/Census County
Business Patterns for baseline employment. Not confident about: the specific incentive-dollar
figure — that will be a stated Modeling Assumption anchored to a real published state/county
incentive program size.
**Sensitivity (SPEC §6).** NONE.
**Split risk.** NONE — 7 skills, one group.

### C4 — The Fan Formation — OBSOLETE (was: score 6.8 · tier T2)
**Status: superseded, do not write.** Pre-Calculus / Polar And Parametric (this concept's entire
target group, 6/6 skills) was independently closed 2026-08-20 by **`Feedback`**
(`cases/feedback/`), written from a separate, later concept pass
(`cases/_concepts/CONCEPTS_polar-parametric_2026-08-19.md`, concept C1) that scored the same
group and reached the same 6.8 ceiling at HIGH feasibility. Every skill below is now `n=1` in
`standards_spine.json` — writing this concept as scoped would close zero new coverage. Kept here
only as a historical record of the concept; removed from the concepting board.
**Protagonist.** Priya Ondelacy, flight choreography programmer for a commercial drone light-show
company. She is programming the finale formation for a paid show and has one battery-life budget
per drone.
**The dilemma.** A.) Program the finale as a polar "fan" expansion (each drone's path defined by
a polar equation r(θ) sweeping outward from center stage) OR B.) Program it as a parametric
"ribbon" sweep (x(t), y(t) tracing a moving spiral band across the sky).
**Primary metric.** Seconds of flight time consumed per drone to complete the formation, given
each drone's fixed max speed and battery budget.
**Why it's close.** The polar fan is shorter in raw path length for drones near the center but
forces the outer-ring drones into a much longer arc at the same angular speed; the parametric
ribbon evens out path length across drones but requires converting back to rectangular waypoints
for the flight controller, adding a small fixed overhead per drone — which one drains the fleet's
battery budget faster is not obvious until you compute both paths.
**Would close (6 skills, 3 how-to / 3 term):**
| id | kind | label |
|---|---|---|
| pre-calculus-polar-coordinate | term | Polar Coordinate |
| pre-calculus-parametric-equation | term | Parametric Equation |
| pre-calculus-parameter | term | Parameter |
| pre-calculus-how-to-convert-a-point-between-rectangular-and-polar-coordinates | how-to | How to convert a point between rectangular and polar coordinates |
| pre-calculus-how-to-graph-a-polar-equation | how-to | How to graph a polar equation |
| pre-calculus-how-to-eliminate-the-parameter-to-find-a-rectangular-equation | how-to | How to eliminate the parameter to find a rectangular equation |
**Data feasibility: HIGH.** Named sources: published consumer/commercial drone show specs (e.g.,
Intel Shooting Star / other manufacturers publish max speed, flight time, and battery capacity
spec sheets); FAA Part 107 / drone show operator public filings sometimes disclose formation
drone counts. Not confident about: the exact finale formation geometry of a real show — that is
modeled, clearly labeled as such.
**Sensitivity (SPEC §6).** NONE.
**Split risk.** NONE.

### C5 — The Reserve Asymptote   ·   score 12.2   ·   tier T3
**Protagonist.** Harlan Voss, actuarial analyst at a regional life insurer, pricing a new
long-duration annuity product ahead of a filing deadline.
**The dilemma.** A.) Price reserves using a closed-form formula that assumes the claims-cost
function approaches its long-run asymptote smoothly (cheaper to compute, standard industry
shortcut) OR B.) Price reserves using the full piecewise mortality-table function, checking it
for continuity at each age-band boundary where the table's assumptions change.
**Primary metric.** Dollars of reserve required per $1,000 of face value, under each pricing
method.
**Why it's close.** The asymptotic shortcut is faster and matches what junior actuaries are
taught first, but it silently assumes the claims-cost function is continuous everywhere — if the
real mortality table has a discontinuity at an age-band boundary (which published SOA tables
sometimes do, by construction), the shortcut misprices reserves right at that boundary; the case
turns on finding the limit both ways and checking continuity at the boundary the shortcut assumes
away.
**Would close (11 skills, 4 how-to / 7 term):**
| id | kind | label |
|---|---|---|
| pre-calculus-limit | term | Limit |
| pre-calculus-asymptote | term | Asymptote |
| pre-calculus-continuity-informal | term | Continuity (Informal) |
| pre-calculus-how-to-estimate-a-limit-from-a-table-or-graph | how-to | How to estimate a limit from a table or graph |
| pre-calculus-how-to-identify-a-vertical-or-horizontal-asymptote-from-a-function-s-equation | how-to | How to identify a vertical or horizontal asymptote from a function's equation |
| calculus-limit | term | Limit |
| calculus-one-sided-limit | term | One-Sided Limit |
| calculus-continuity | term | Continuity |
| calculus-discontinuity | term | Discontinuity |
| calculus-how-to-evaluate-a-limit-algebraically | how-to | How to evaluate a limit algebraically |
| calculus-how-to-determine-whether-a-function-is-continuous-at-a-point | how-to | How to determine whether a function is continuous at a point |
**Data feasibility: HIGH.** Named sources: Society of Actuaries published mortality tables (e.g.,
the SOA's publicly released base tables); CDC National Vital Statistics life tables (fully
public, standard actuarial teaching source); a published annuity reserve-methodology primer (SOA
study notes are public). Not confident about: a specific carrier's own filed reserve number —
that stays a Modeling Assumption built from the public tables, clearly labeled.
**Sensitivity (SPEC §6).** LOW — mortality tables reference life expectancy in the aggregate,
actuarially standard and not framed around any individual; keep it that way in the write-up.
**Split risk.** NONE at 11 skills — it is at the top of the "honest 8-15" range specifically
*because* it is one coherent decision (price this reserve) that happens to require both the
precalc on-ramp and the calculus formalization; do not split it, the precalc half alone under-
motivates a protagonist and the calculus half alone re-teaches limits from nothing.

### C6 — The Tracker's Angle — OBSOLETE (was: score 6.2 · tier T2)
**Status: superseded, do not write.** Pre-Calculus / Trigonometric Identities (this concept's
entire target group, 5/5 skills) was independently closed 2026-08-20 by **`Deluge Gun`**
(`cases/deluge-gun/`), written from a separate, later concept pass
(`cases/_concepts/CONCEPTS_trig-identities_2026-08-19.md`) that scored the same group and reached
the same 6.2 ceiling at HIGH feasibility. Every skill below is now `n=1` in
`standards_spine.json` — writing this concept as scoped would close zero new coverage. Kept here
only as a historical record of the concept; removed from the concepting board.
**Protagonist.** Ysabel Nkemelu, solar installation design engineer at a residential/commercial
solar contractor, bidding a rooftop-vs-tracker system for a warehouse client.
**The dilemma.** A.) Install a fixed-tilt array at the site's optimal static angle OR B.) Install
a single-axis tracker that adjusts angle through the day, verified against the trig identity that
relates the panel's instantaneous angle of incidence to the sun's changing elevation angle.
**Primary metric.** kWh produced per kW installed per year (a standard solar-industry ratio).
**Why it's close.** The tracker produces more energy per panel but costs more per watt installed
and adds a moving part to maintain; verifying the Pythagorean identity correctly in the
angle-of-incidence formula is what lets the engineer trust the tracker's modeled gain instead of
just taking the manufacturer's marketing number.
**Would close (5 skills, 3 how-to / 2 term):**
| id | kind | label |
|---|---|---|
| pre-calculus-pythagorean-identity | term | Pythagorean Identity |
| pre-calculus-inverse-trigonometric-function | term | Inverse Trigonometric Function |
| pre-calculus-how-to-verify-a-trigonometric-identity | how-to | How to verify a trigonometric identity |
| pre-calculus-how-to-solve-a-trigonometric-equation-over-a-given-interval | how-to | How to solve a trigonometric equation over a given interval |
| pre-calculus-how-to-evaluate-an-inverse-trigonometric-function | how-to | How to evaluate an inverse trigonometric function |
**Data feasibility: HIGH.** Named sources: NREL PVWatts published output-per-kW data by system
type (fixed-tilt vs. tracking) and region; NREL's own published fixed-tilt-vs-tracker cost
premium studies. Not confident about: the specific warehouse's roof geometry — modeled, labeled.
**Sensitivity (SPEC §6).** NONE.
**Split risk.** NONE.

### C7 — The Roofline Call   ·   score 4.8   ·   tier T2
**Protagonist.** Colton Marsh, residential architectural drafter at a small design-build firm,
finalizing a roof framing plan a client needs signed off this week.
**The dilemma.** A.) Draft a gable roof (two planes meeting at a ridge, mostly right and acute
framing angles) OR B.) Draft a hip roof (four planes, adds obtuse and complementary angle cuts at
the hips) for the same footprint.
**Primary metric.** Board-feet of framing lumber per square foot of enclosed attic space.
**Why it's close.** The hip roof reads as the "nicer" option on the elevation drawing and sheds
wind better, but every hip cut is an angle a framer has to mark and cut individually — the
drafter has to actually work through the vertex and angle relationships at each hip line to know
whether the extra lumber and labor is worth the wind performance, not just eyeball it.
**Would close (8 skills, 0 how-to / 8 term):**
| id | kind | label |
|---|---|---|
| geometry-ray | term | Ray |
| geometry-vertex | term | Vertex |
| geometry-acute-angle | term | Acute Angle |
| geometry-obtuse-angle | term | Obtuse Angle |
| geometry-parallel-lines | term | Parallel Lines |
| geometry-perpendicular-lines | term | Perpendicular Lines |
| geometry-complementary-angles | term | Complementary Angles |
| geometry-adjacent-angles | term | Adjacent Angles |
**Data feasibility: MEDIUM.** Named sources: published lumber framing span/waste-factor tables
from a lumber trade association (e.g., APA/Engineered Wood Association span tables are public);
regional lumber price indices (published by trade press). Not confident about: a specific labor
cost differential between gable and hip framing — likely a stated Modeling Assumption.
**Sensitivity (SPEC §6).** NONE.
**Split risk.** NONE — all-term concept (no how-tos), by nature of what's left uncovered in this
group; flagged honestly rather than padded with a how-to the case wouldn't really force.

### C8 — The Irregular Boundary   ·   score 3.0   ·   tier T1
**Protagonist.** Renata Suh, precision-agriculture GIS land-use analyst for a farm-management
company, laying out a new field's planted boundary.
**The dilemma.** A.) Plant a standard convex rectangular block sized to the center-pivot
irrigation radius (simple, some corner acreage unused) OR B.) Plant an irregular, partly concave
boundary that follows the property line and an easement notch, using every plantable acre.
**Primary metric.** Usable planted acres per dollar of boundary-fencing/guidance-line cost.
**Why it's close.** The irregular boundary captures more acreage but costs more in GPS guidance
setup and fencing perimeter per acre gained, since a concave boundary has more perimeter for the
same area than a convex one — the analyst has to weigh acreage gained against the extra boundary
cost, not just "more land is more land."
**Would close (5 skills, 0 how-to / 5 term):**
| id | kind | label |
|---|---|---|
| geometry-convex | term | Convex |
| geometry-concave | term | Concave |
| geometry-irregular-polygon | term | Irregular Polygon |
| geometry-quadrilateral | term | Quadrilateral |
| geometry-parallelogram | term | Parallelogram |
**Data feasibility: MEDIUM.** Named sources: USDA NASS Cropland Data Layer and county GIS parcel
data (both public); published center-pivot irrigation equipment radius specs; agricultural
fencing cost-per-foot data (extension-service published). Not confident about: a specific
easement scenario — modeled, labeled.
**Sensitivity (SPEC §6).** NONE.
**Split risk.** NONE — lowest raw score in the batch (all-term, small group); kept in this batch
for the career weighting (agriculture is otherwise unrepresented in the corpus) but ranked to
write last.

### C9 — Prove It Scales   ·   score 2.8   ·   tier T1
**Protagonist.** Devon Achebe, software/algorithm engineer at a data-infrastructure company,
choosing which implementation of a core function ships in the next release.
**The dilemma.** A.) Ship the recursive implementation (shorter, matches the mathematical
definition, proven correct by induction) OR B.) Ship the iterative rewrite (longer, avoids stack
growth, behavior at scale is argued informally rather than proven).
**Primary metric.** Milliseconds of runtime per 10,000 calls, measured at three input sizes.
**Why it's close.** The recursive version is provably correct for every input by mathematical
induction — base case plus inductive step — which is a real engineering asset when the function
touches billing-critical code, but it costs measurably more per call at the sizes this system
actually sees; the case turns on whether the provable-correctness guarantee is worth the runtime
cost at this specific traffic volume.
**Would close (4 skills, 1 how-to / 3 term):**
| id | kind | label |
|---|---|---|
| discrete-mathematics-mathematical-induction | term | Mathematical Induction |
| discrete-mathematics-base-case | term | Base Case |
| discrete-mathematics-inductive-step | term | Inductive Step |
| discrete-mathematics-how-to-prove-a-statement-using-mathematical-induction | how-to | How to prove a statement using mathematical induction |
**Data feasibility: MEDIUM.** Named sources: published algorithmic-complexity benchmarking
methodology (e.g., well-known language-runtime benchmark suites publish recursive-vs-iterative
timing comparisons for canonical functions like factorial/Fibonacci — real, citable numbers
exist for the *shape* of the tradeoff). Not confident about: this specific fictional company's
own traffic volume and runtime numbers — stated Modeling Assumption, anchored to a cited public
benchmark's real ratio.
**Sensitivity (SPEC §6).** NONE.
**Split risk.** NONE — smallest concept in the batch by design; the remaining 3 skills in this
7-skill group (recursive definition, recursive case, closed-form vs recursive formula) are
already thin, not zero, so a future case could thicken them without re-closing what this one
closes.

### C10 — The Cheap Approximation   ·   score 3.2   ·   tier T2
**Protagonist.** Naomi Kessler, embedded systems/firmware engineer at a sensor manufacturer,
choosing how a low-power temperature sensor converts a raw reading to degrees on-chip.
**The dilemma.** A.) Compute a 2nd-order Taylor series approximation of the sensor's nonlinear
response curve, evaluated on-chip in a few CPU cycles OR B.) Store the full nonlinear curve as a
lookup table in flash memory and interpolate.
**Primary metric.** Degrees of error at the calibration curve's extremes, per microsecond of
compute time spent.
**Why it's close.** The Taylor approximation is dramatically cheaper to compute and needs no
flash storage, which matters on a coin-cell-powered part, but a low-order Taylor series drifts
from the true curve away from the point it was expanded around — whether that drift stays inside
the sensor's rated accuracy spec at the temperature extremes is exactly what the engineer has to
check before shipping it.
**Would close (4 skills, 2 how-to / 2 term):**
| id | kind | label |
|---|---|---|
| calculus-series | term | Series |
| calculus-taylor-series | term | Taylor Series |
| calculus-how-to-determine-whether-a-series-converges-or-diverges | how-to | How to determine whether a series converges or diverges |
| calculus-how-to-find-the-taylor-series-of-a-function-at-a-point | how-to | How to find the Taylor series of a function at a point |
**Data feasibility: MEDIUM.** Named sources: published thermistor Steinhart-Hart datasheets
(these are genuinely nonlinear resistance-to-temperature curves engineers really do approximate
this way — real manufacturer datasheets publish the curve and accuracy spec). Not confident
about: the exact on-chip cycle counts for a specific microcontroller — likely a stated Modeling
Assumption anchored to a published datasheet's cycle-timing table.
**Sensitivity (SPEC §6).** NONE.
**Split risk.** NONE.

## Already-covered skills note

None of these ten concepts were checked against `standards_spine.json`'s already-covered (`n>0`)
skills in their groups for a "why it's well-rounded" list — that pass belongs to `case-write` when
a concept here is picked, per the skill's own contract (concept sheets name the *new* coverage
only). Flagging so the human picking a concept knows that step is still ahead of them.
