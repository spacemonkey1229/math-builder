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

### C2 — STRENGTHENED research pass (2026-08-31)

**What changed and why.** The original concept named source *categories* ("state DOI reports,
NAIC data") without verifying a specific, citable instance of either, and asserted the
converse/contrapositive confusion as a plausible-sounding but unconfirmed premise. This pass ran
real web research against all four weak points. Net result: Data Richness moves from an assumed
MEDIUM to a verified HIGH — real, named, per-company annual figures exist and are dramatic enough
to build a metric on directly, rather than needing a Modeling Assumption to bridge a gap. The
logic-confusion premise is now grounded in genuine legal terminology (though not in an
insurance-specific documented incident), and the stakes are sharpened with a real, load-bearing
analogy from adjacent (non-insurance-line) litigation.

**1. Real state DOI data — found, specific, strong.** The California Department of Insurance
publishes an annual *Consumer Complaint Study* with a "justified complaint ratio" (justified
complaints per 100,000 policy exposures) for the 50 largest homeowners insurers, broken out by
individual company for the three most recent years. The 2025 study
([2025-Consumer-Complaint-Study-Home.pdf](https://www.insurance.ca.gov/01-consumers/120-company/03-concmplt/upload/2025-Consumer-Complaint-Study-Home.pdf))
gives real per-carrier figures, e.g.:
- State Farm General Insurance Company: 1.4 (2022) → 1.6 (2023) → **11.9 (2024)**, on an exposure
  base of 2,139,816 policies (254 justified complaints in 2024 vs. 37 in 2023).
- Farmers Insurance Exchange: 4.5 (2022) → 24.0 (2023) → **40.2 (2024)**.
- Mid-Century Insurance Company: 4.5 (2022) → 31.8 (2023) → **51.4 (2024)**.
- By contrast, USAA General Indemnity: 2.0 (2022) → 1.4 (2023) → 0.6 (2024).

That is a real, dramatic, unexplained-in-the-report year-over-year jump for several major
California homeowners carriers into 2024 — exactly the kind of number an auditor would be
assigned to investigate, and it is specific enough to hand a student as a real table rather than
an invented one. (A California DOI market-conduct/complaint-study series for auto and other lines
also exists at the same URL root, confirming the source category generalizes.)

**2. Real NAIC data — found, real, program confirmed but figure not yet pulled.** The NAIC's
*Market Conduct Annual Statement* (MCAS) program is real and current: 51 jurisdictions
participated in the 2024 data year, and NAIC publishes yearly "MCAS Annual Statement Ratios"
scorecards (confirmed for 2023 and 2025 vintages at content.naic.org) with named ratios —
complaints received directly from consumers per 1,000 policies in force, and total complaints to
claims opened, by state and line of business. This confirms the source is real and citable at the
scorecard level; a specific carrier-year figure from the MCAS scorecard itself should still be
pulled at write-time (the PDF did not render cleanly via automated fetch) and cited directly
rather than assumed. Recommend using the CA DOI homeowners table above as the primary dataset
(cleaner, company-named, already verified) and citing MCAS as the secondary/context source, per
SPEC's real-source preference.

**3. The converse/inverse confusion premise — partially grounded, still needs an honest caveat.**
I could not find a documented real-world case of an insurance adjuster or auditor specifically
confusing a conditional's converse with its contrapositive in an insurance-law CLE article or bar
journal. What I did confirm: the specific error the case turns on has real, standard names in
logic and law — "affirming the consequent" (the converse error) and "denying the antecedent" (the
inverse error) — and these exact fallacy names are recognized and cited in real appellate opinions
(e.g., the Ninth Circuit's discussion in *Carver v. Lehman*, No. 06-35176, cites "denying the
antecedent" by name as a specific reasoning error). That confirms the underlying logical error is
a real, formally recognized category that courts already use this exact vocabulary for — it is
not a contrived textbook distinction — but the case write-up should present the adjusters'
converse-vs-contrapositive mistake as a **stated, clearly-labeled scenario premise** (plausible
and logically well-formed, consistent with how real insurance clauses get misread) rather than as
a documented historical incident. This is a narrower, more honest claim than the original concept
implied, and should be written that way in the case's Modeling Assumptions.

**4. Sharpened stakes — a real, higher-stakes analog exists, one line of business over.** Two real,
well-documented cases show what "wrongly denying claims under the wrong logical standard, at
scale" actually costs when nobody catches it — both in health insurance, not property/auto, but
directly on point as the *stakes analogy* for Marisol's decision:
- **Cigna's PxDx system**: ProPublica's investigation (confirmed, and cited in ongoing House
  Energy & Commerce Committee scrutiny) found Cigna medical directors denied roughly 300,000
  claims over two months using an automated review process, spending an average of 1.2 seconds
  per claim — later the subject of multiple class-action lawsuits.
- **UnitedHealth's nH Predict**: a federal lawsuit (partially allowed to proceed; UnitedHealth
  was ordered to produce discovery documents) alleges the algorithm had roughly a 90% error rate
  on appealed denials — i.e., nine of ten denials that were appealed got overturned, meaning the
  wrong standard was being applied systematically and at volume before anyone caught it.
- On the pure litigation-exposure side, first-party bad-faith claim handling is a real, named
  California cause of action (California Civil Jury Instructions CACI No. 2332, "Bad Faith (First
  Party) — Failure to Properly Investigate Claim") with real precedent (e.g. *Hangarter v.
  Provident*, 9th Cir.) — this is the real legal mechanism by which a wrong audit standard, if it
  causes a pattern of wrongful denials, turns into carrier liability beyond the individual claim.

Use these as the "why the stakes are real" framing text in the case narrative (not as the
data the metric is computed from, and not as the scenario's line of business — keep the scenario
itself property/auto per the original sensitivity note) — i.e., "this is the property/auto
version of a mistake that, in health insurance, has already produced a 90%-error-rate AI system
and a 300,000-claim automated-denial program now under federal investigation." That reframes
Marisol's choice from "pick the faster audit standard" to "pick the standard that would have
caught this before regulators or plaintiffs' counsel did."

**Re-scored rubric (4-axis, /5 each, /20 total):**

| Axis | Before | After | Why it moved |
|---|---|---|---|
| Skill Fit | 4.5 | 4.5 | Unchanged — 7/8 zero-coverage Formal Logic skills at n=1 is still the strongest fit in this batch; research didn't touch skill mapping. |
| Narrative Pull | 4.0 | 4.5 | The real State Farm General / Farmers / Mid-Century 2024 complaint-ratio spikes give Marisol a concrete, dated, "something changed and I have to find out what" hook instead of a generic audit-standard choice; the Cigna/UnitedHealth stakes analogy sharpens why her recommendation actually matters. |
| Data Richness | 3.5 | 4.5 | The weakest axis, now the most improved: a real, named, per-carrier, multi-year complaint-ratio table (CA DOI 2025 study) replaces the vague "these reports exist" claim, and is dramatic enough to build the primary metric on directly. NAIC MCAS confirmed as real and citable at the program/scorecard level but not yet pulled to a specific figure — that's the one remaining piece of legwork before case-write, so I'm not claiming a full 5. |
| Dilemma Tension | 4.0 | 4.0 | Unchanged on the core mechanic (literal clause vs. contrapositive is still the tension), but now better supported: the honest caveat on axis 3 (no documented insurance-specific converse/contrapositive incident, only the real formally-named fallacy) keeps this from over-claiming, while the real bad-faith litigation mechanism (CACI 2332) gives the "wrong standard" side of the dilemma genuine teeth. |
| **Total** | **16/20** | **17.5/20** | |

**Bottom line.** Feasibility should move from MEDIUM to HIGH for Data Richness purposes: there is
now a real, specific, citable, dramatic dataset (CA DOI 2025 homeowners complaint study) available
to build the case's primary metric on, with NAIC MCAS as a confirmed-real secondary source still
needing one more figure pulled at write-time. The logic-confusion premise should be written up as
a labeled scenario assumption, not an implied documented fact — a narrower but more honest claim
than the original sheet made.

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

**Status: STRENGTHENED (research addendum, 2026-08-31) — original writeup above superseded by the
version below.** Original scored 12.5/20 (Skill Fit 3.5 / Narrative Pull 3 / Data Richness 3 /
Dilemma Tension 3) and was flagged by its own author as the batch's weakest, "kept for career
weighting, write last." A dedicated research pass (real sources below) found a sharper hook, a
second genuinely real cost axis, and specific named figures the original writeup lacked. Re-
scored 17/20 (below). Original protagonist, skills, and Data Richness label are retained above
for historical record; do not delete.

#### C8 (revised) — The Irregular Boundary, strengthened

**Protagonist.** Renata Suh, precision-ag GIS land-use analyst for a farm-management company
operating corn/soybean quarter-sections in Nebraska pivot-irrigation country. She is finalizing
the planted-boundary map for one 160-acre quarter-section (the standard U.S. Public Land Survey
System unit these fields are laid out on) ahead of a lease-renewal deadline: the landlord's bank
wants a locked planted-acreage figure to set next year's cash rent, and a neighboring farm's
center-pivot "tail" has been swinging across the disputed corner of this property line for
several seasons — under Nebraska's prescriptive-easement rule (10 years of open, continuous,
adverse use ripens into a legal right; Neb. Rev. Stat. §34-301 governs actions to establish lost
or disputed boundaries/corners), this is the season to settle the boundary on paper before that
clock matters. The deadline and the neighbor dispute raise the stakes past a routine mapping task.

**The dilemma.** A.) Draw a standard convex rectangular planted block sized to the pivot's basic
circle, cede the corners as unplanted, and stay clear of the disputed pivot-tail strip entirely
(simplest GPS guidance line, no new fencing, and — because the boundary never touches the
disputed strip — no risk of validating the neighbor's crossing) OR B.) Draw an irregular,
partly concave boundary that reclaims the corner acreage *and* asserts the property line right up
to the disputed strip (more usable acres and forces the boundary question now), at the cost of a
longer, more complex guidance line/fence and — per real agricultural-engineering research on
harvester path planning — extra crop loss at each concave notch where the combine's turning
margin has to double-cut.

**Primary metric.** Net dollars per acre gained: (usable planted acres reclaimed × per-acre crop
margin) minus (guidance-line/fencing cost per added foot of perimeter) minus (harvest turning-
margin crop loss at each concave notch, per acre gained).

**Why it's genuinely close (two real cost axes, not one).** A circle pivot inscribed in a
160-acre quarter-section leaves up to 24 acres (about 15% of the field) unwatered/unplanted in
the corners — a real, commonly cited precision-ag figure (sourced below). Commercial "corner
systems" (swing arms) exist to reclaim 17–25 of those acres, but they require burying a guidance
wire around the field's irregular perimeter and are proven out mainly on high-value crops like
potatoes ($2,000–3,000/acre) — for corn or soybeans, with far thinner per-acre margins, the same
reclaimed-acreage math is genuinely close rather than an obvious win. On top of that perimeter
cost, a 2019 peer-reviewed robot-combine path-planning study (Rahman et al., cited below) shows
concave field boundaries force extra double-cut turning margin at each reflex (concave) vertex —
a second, independent real cost that a purely "more area vs. more perimeter" framing misses. The
concave vertices are exactly where both costs stack, which is what makes identifying convex vs.
concave and locating the polygon's vertices mathematically load-bearing rather than decorative.

**Target skills (unchanged, still 5 term, 0 how-to):** geometry-convex, geometry-concave,
geometry-irregular-polygon, geometry-quadrilateral, geometry-parallelogram — now load-bearing
because the case requires the analyst to locate the specific reflex (concave) vertex on the
boundary polygon, since that vertex is where the extra perimeter cost and the extra turning-
margin crop loss both occur simultaneously.

**Real named sources found:**
- FCSAmerica / AgCountry / Frontier Farm Credit, "Don't Cut Corners on Reporting Pivot Acres, Use
  Precision" (farm-credit learning-center article) and Edible Geography, "Squaring the Circle" —
  both cite the real, specific figure that a center-pivot circle inscribed in a 160-acre quarter-
  section leaves up to 24 acres (about 15%) unwatered in the corners, and that corner swing-arm
  systems add roughly 17–25 acres per corner but are economically justified mainly for high-value
  crops (potatoes at $2,000–3,000/acre), per historical account of Robert Daugherty's corner-arm
  solution and current corner-leasing practice (e.g., the Bunderson family leasing 8–10-acre
  corners from neighbors).
- General center-pivot capital cost range, $400–$1,000/acre (excluding land/water development),
  as compiled via Michigan State University Extension's published irrigation-cost worksheets.
- Iowa State University Extension, Ag Decision Maker File B1-75, "Estimated Costs for Livestock
  Fencing" (revised December 2024, extension.iastate.edu/agdm) — a real, current, publicly
  published per-foot fencing cost comparison (woven wire, barbed wire, high-tensile
  non-electric/electrified) for a quarter-mile (1,320 ft) perimeter, with labor valued at
  $20.00/hour from Iowa's own custom-rate survey (AgDM File A3-12). Table values themselves need
  a direct PDF pull at case-write time (WebFetch was blocked by the server at research time); the
  publication and its cost basis are confirmed real and current.
- GPS guidance/RTK system costs, $1,500 (visual guidance) to $35,000 (automatic RTK steering),
  and USDA Economic Research Service (Amber Waves, 2016, "Cost Savings from Precision Agriculture
  Technologies on U.S. Corn Farms") figures of roughly $15/acre annual savings and about a 2.5%
  profit increase from guidance adoption, with 1–2 year payback above 1,000 acres — real,
  citable numbers for the guidance-line side of the cost.
- USDA NASS Crop Sequence Boundaries (CSB) dataset, developed with USDA's Economic Research
  Service — real, public, satellite-derived field-boundary polygons for corn, soybeans, cotton,
  and wheat nationwide (explicitly crop boundaries, not ownership/tax parcels — a caveat to state
  plainly if used to ground the scenario's field shape in a real location).
- Rahman, M.M. et al. (2019), "Optimum harvesting area of convex and concave polygon field for
  path planning of robot combine harvester," *Intelligent Service Robotics* (also archived via
  Hokkaido University HUSCAP repository) — a real peer-reviewed paper establishing that concave
  field boundaries require extra double-cut turning margin near boundary vertices (using
  RTK-GPS at ±2 cm accuracy), the real engineering basis for the case's second cost axis.
- Nebraska prescriptive-easement law: Neb. Rev. Stat. §34-301 (action to establish lost or
  disputed boundaries/corners); the 10-year open/continuous/adverse-use rule for prescriptive
  easements (see Mueller v. Bohannon, Neb. Sup. Ct. 1999, and a Baird Holm LLP summary of a
  Nebraska Supreme Court prescriptive-easement affirmance in Otoe County); and a 2025 Nebraska
  agricultural-law firm bulletin specifically addressing pivot-tail crossings and field-road
  easements as a live boundary-dispute risk for pivot-irrigated corners — real legal grounding
  for the deadline/dispute stakes in the protagonist's situation.
- Nebraska Department of Agricultural Economics (UNL), 2026 Nebraska Farmland Values and Cash
  Rental Rates preliminary report — real annual state survey documenting center-pivot irrigated
  cropland value and rental-rate trends, usable to ground the lease-renewal stakes in a real,
  current market context (exact per-acre dollar figures await the June 2026 final report; the
  preliminary report gives only percentage changes).

**Sensitivity (SPEC §6).** NONE — routine agricultural land-use and property-boundary math; the
neighbor/easement angle stays civil/property law, not a protected-subject or personal-conflict
narrative.
**Split risk.** NONE — still 5 skills, one group, clean fit; strengthening added narrative/data
depth, not scope.

**Re-scored rubric (0–5 each):**
| Axis | Before | After | Why |
|---|---|---|---|
| Skill Fit | 3.5 | 4.5 | The concave-vertex identification is now the exact point where both real cost axes (perimeter cost, turning-margin crop loss) coincide — vocabulary is mechanically load-bearing, not just descriptive labeling of the field's shape. |
| Narrative Pull | 3 | 4 | Replaced a generic "lay out a field" task with a dated, higher-stakes hook: a lease-renewal deadline plus a real, legally grounded neighbor boundary dispute (Nebraska prescriptive-easement statute and case law), not just routine planning. |
| Data Richness | 3 | 4.5 | Added multiple real, specific, named figures: the 24-acre/15% quarter-section corner-waste figure, corner-system acreage/cost economics, a named current extension fencing-cost publication, USDA ERS guidance-cost savings figures, a real peer-reviewed harvester path-planning paper, and real Nebraska statute/case law — up from three generic source categories with no concrete numbers. |
| Dilemma Tension | 3 | 4 | The original was a single axis (more acreage vs. more perimeter cost). The revision adds a second, independent real cost (harvest turning-margin crop loss at concave notches, from Rahman et al. 2019) plus a legal-risk axis (settling vs. not settling the disputed boundary), making the two options genuinely comparable rather than one clearly better. |
| **Total** | **12.5/20** | **17/20** | |

**Still not confident about (flag honestly for case-write):** the exact ISU B1-75 per-foot dollar
figures (publication confirmed real and current, but the table itself needs a direct pull, not
just search snippets); the specific dollar-per-acre Nebraska farmland value for this case's
fictional quarter-section (2026 report is preliminary/percentage-only; the June 2026 final report
should have real per-acre numbers by the time this case is written); and the fictional
neighbor-dispute's specific facts, which stay a clearly labeled Modeling Assumption anchored to
the real Nebraska statute and case law cited above, not a claim that this exact dispute occurred.

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

> **STRENGTHENED 2026-08-31 — original C9 above is SUPERSEDED by the addendum below.**
> Research pass raised Narrative Pull, Data Richness, and Dilemma Tension with real, citable
> sources (no invented numbers). Original kept above for the record; do not re-read it as current.

### C9 (addendum) — Prove It Scales, strengthened   ·   research note 2026-08-31

**What changed and why.** The original concept's protagonist/company were generic ("a
data-infrastructure company"), its performance numbers were an unanchored Modeling Assumption,
and its tension ("recursive is provably correct but costs more") was true but not sharp — real
benchmark data shows the actual cost gap swings from ~2x to >1,000x depending on one variable
(does the runtime honor tail-call optimization), which is a far better engine for a "how big a
gap justifies which choice" case than a flat "recursion is slower" framing.

**1. Data Richness — real sources found.**
- **Real, reproducible benchmark numbers (Go), with the TCO-dependence built in:** Felipe Dutra
  Tine e Silva, ["Iterative vs Recursive vs Tail-Recursive in
  Golang"](https://medium.com/@felipedutratine/iterative-vs-recursive-vs-tail-recursive-in-golang-c196ca5fd489)
  reports measured Fibonacci benchmarks: **iterative 16.4 ns/op, tail-recursive 33.3 ns/op,
  plain (non-tail) recursive 394 ns/op**. That is a ~2x gap when the recursive form is written so
  the compiler can optimize the tail call, vs. a ~24x gap when it can't. This is the real number
  the case's "how close is this, really" question can be built around.
- **Real extreme-case benchmark (same shape, bigger gap):** the public repo
  [pope/go_recursive_benchmark](https://github.com/pope/go_recursive_benchmark) benchmarks a
  naive exponential-recursion Fibonacci at **~312,238,250 ns/op** against a restructured
  tail-call version at **~35.36 ns/op** — roughly an 8.8-million-times difference, on Go/ARM64,
  methodology and code visible in the repo. Useful as the "what happens if you get the recursive
  form wrong in a way that isn't tail-callable at all" data point — i.e., the downside case the
  engineer is trying to avoid by rewriting iteratively in the first place.
- **A real, named, on-point production incident — recursive code, billing, wrong numbers:**
  Oren Eini (Ayende Rahien, founder of RavenDB — a real database/data-infrastructure company),
  ["Production postmortem: Your math is wrong, recursion doesn't work this
  way"](https://ayende.com/blog/197637-A/production-postmortem-your-math-is-wrong-recursion-doesnt-work-this-way).
  A recursive map-reduce **billing aggregation** function (aggregating Users, Credits, and
  Charges) silently violated its own inductive assumption — it assumed every invocation would
  receive a document carrying a `Name` property, which failed once intermediate (already-reduced)
  results were fed back into it recursively across cluster nodes. The result: customer billing
  totals diverged by node, with one account showing **-67,343 vs. +67,329** — a real, cited,
  numeric example of exactly the failure mode "prove it by induction" is supposed to catch (the
  bug *is* an unverified inductive step: the function's behavior on the base case did not
  generalize to arbitrary recursive invocations). This is a much stronger, more specific anchor
  than a generic "billing-critical code" line — it is a real incident at a real data-infra
  company, and it makes the induction proof's practical payoff concrete rather than abstract.

**2. Narrative Pull — sharper real-world hook.**
- **AWS's formal-methods engineering culture** (Newcombe, Rath, Zhang, Munteanu, Brooker,
  Deardeuff, ["How Amazon Web Services Uses Formal
  Methods"](https://cacm.acm.org/research/how-amazon-web-services-uses-formal-methods/), CACM
  2015): AWS engineers used TLA+ formal specification to catch subtle correctness bugs in
  DynamoDB and S3 before they shipped; one DynamoDB engineer is quoted saying he'd have used it
  from the start had he known about it, finding it more reliable and less time-consuming than his
  informal proofs. Real, named, citable culture of "prove it, don't just argue it informally" at
  exactly the kind of company (cloud data infrastructure) this protagonist works at.
- **seL4 microkernel** (Klein et al.; DARPA HACMS program): the first general-purpose OS kernel
  with a machine-checked, end-to-end proof of functional correctness, later embedded in
  safety-critical systems including Boeing's Unmanned Little Bird helicopter — a professional
  red team hired to hack it in live flight failed. A real, extreme illustration of "how much does
  proof-grade correctness matter" at the high end of the spectrum, useful as a contrast point
  (Devon's stakes are lower than a flying helicopter, but the same proof technique is the one
  seL4 used) rather than as the case's own setting.
- **Recommended protagonist/company sharpening:** keep Devon Achebe as a software/algorithm
  engineer, but at a company whose core product *is* billing/usage aggregation for other
  businesses (a metering/usage-billing platform, the commercial descendant of what RavenDB's
  postmortem was about) rather than a generic "data-infrastructure company." That framing turns
  "is this function billing-critical" from a throwaway line into the entire premise, and lets the
  case openly reference the real failure mode (an unverified inductive step in a recursive
  aggregation function) as the reason correctness proof is on the table at all — without
  claiming Devon's company IS RavenDB.

**3. Dilemma Tension — the real nuance found.**
Naive framing ("recursive is provably correct but slower, iterative is faster but only
informally argued") is true but flat. The real benchmark data complicates it usefully:
- When the recursive function is written so the compiler/runtime can apply tail-call
  optimization, the real gap is small (~2x in the Go numbers above — some functional-language
  runtimes with reliable TCO, e.g. Scala/F#/Elixir, get even closer to iteration's cost).
- When it isn't (or the runtime doesn't guarantee TCO — notably, V8/JavaScript dropped TCO
  support entirely, and most mainstream imperative-language compilers don't guarantee it either),
  the gap is large: ~24x in a modest case, and easily 1,000x+ if the recursive structure is not
  tail-callable at all (the 8.8-million-times case above is the extreme end).
- **This means the real decision Devon faces isn't "recursive vs. iterative" in the abstract —
  it's "can I trust this specific runtime to actually apply TCO to this specific function, and if
  I can't (or won't, because that's an unwritten compiler behavior rather than a language
  guarantee), is the provable-correctness win worth accepting the large, not the small, gap."**
  That is a genuinely closer, more realistic engineering call than "recursion just costs more,"
  and it gives the case a clean secondary lever (which language/runtime is this shipping to,
  and does its spec actually guarantee TCO) without adding new target skills.

**Revised dilemma (drop-in replacement for "The dilemma" and "Why it's close" above).**
A.) Ship the recursive implementation — matches the mathematical definition, proven correct for
every input by induction (base case + inductive step), but its runtime cost depends on whether
the target language/runtime reliably applies tail-call optimization to it OR B.) ship the
iterative rewrite — guaranteed flat, low per-call cost regardless of runtime, but its correctness
argument is informal (a walkthrough, not a proof), and Devon's team has already shipped one real
bug of exactly this shape (an unverified assumption that held at the top level but not on
recursive re-invocation) once before. Primary metric unchanged (ms per 10,000 calls at three
input sizes) but now explicitly bifurcated: with-TCO cost vs. without-TCO cost, both anchored to
the real Go benchmark ratios above rather than an unanchored assumption.

**Re-scored 4-axis rubric.**

| Axis | Before | After | Why |
|---|---|---|---|
| Skill Fit | 4 | 4 | Unchanged — if anything more tightly earned: the RavenDB incident *is* a failed inductive step, so the induction/base-case/inductive-step skills now map onto a real failure mode instead of an abstract proof exercise. |
| Narrative Pull | 3.5 | 4.5 | Generic "data-infrastructure company" replaced with a real, named engineering culture (AWS TLA+ on DynamoDB/S3), a real extreme case (seL4/DARPA HACMS) for contrast, and a recommended protagonist framing (usage-billing platform) anchored to a real incident rather than invented flavor text. |
| Data Richness | 3.5 | 4.5 | Two independent real, checkable benchmark sources with actual ns/op numbers (16.4 / 33.3 / 394; and 312,238,250 / 35.36), replacing "a stated Modeling Assumption anchored to a cited public benchmark's real ratio" with the ratios themselves, plus a real production incident with real cited financial figures (-67,343 vs +67,329). |
| Dilemma Tension | 3.5 | 4.0 | The real data reveals the actual crux is runtime-dependent (TCO honored or not), which is a sharper, more realistic engineering judgment call than "recursive costs more" — closer to a genuine toss-up in the TCO-honored case, genuinely lopsided in the non-TCO case, and the *which one applies here* question is itself the skill-relevant tension. |
| **Total** | **14.5/20** | **17.5/20** | |

**Feasibility note.** Still MEDIUM, not HIGH — the *shape* of the tradeoff is now backed by real,
named, checkable sources (a marked improvement over the original's unanchored assumption), but
Devon's own company's traffic volume remains a stated Modeling Assumption by necessity (as with
any fictional protagonist). Recommend anchoring that assumption explicitly to the Go benchmark
ratios above (2x with TCO / 24x+ without) rather than picking an arbitrary number, and citing the
Ayende/RavenDB postmortem and the AWS TLA+ paper directly in FACILITATOR.md as real-world
grounding for why a data-infra company would care about a proof at all.

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
