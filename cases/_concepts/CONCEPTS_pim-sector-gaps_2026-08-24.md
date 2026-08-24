# Concept sheet — PIM sector-gap batch (business/industry areas underrepresented in the corpus)

Generated 2026-08-24, per `skills/case-brainstorm/SKILL.md`. Target selection: not a single spine
group — the user asked for career/industry areas identified as poorly represented against a
PIM "Universe" investment dashboard of high-conviction structural-power business sectors, plus two
follow-up asks (mid-session) to add **aerospace/space tech, quantum computing, product design
(IDEO-style creative/industrial design), human factors, music theory, and social-media
influencing/SEO/product-placement optimization**. 14 business areas total, each mapped to a
genuine spine-group fit rather than a spine-group-first search. `case-brainstorm` was invoked
manually (the skill isn't in this session's registered-skill list, so its procedure was followed
directly against `readmodel/gap_queue.json` / `standards_spine.json` / `domains.json`).

**Quality rubric applied alongside coverage,** same convention as
`CONCEPTS_formal-logic-vectors-matrices-numbertheory_2026-08-23.md`: `raw` counts only skills
genuinely at spine `n==0` (0.6/term, 1.0/how-to); `bonus` +2.0 only if every remaining gap in the
group closes; `score = (raw + bonus) × availability_factor`. Most of these business-area concepts
land at or near coverage **0.0** — the sectors the user asked about (AI infra, quantum, aerospace,
product design, crypto, human factors) mostly map onto spine groups that are *thin, not zero*
(the true zero-coverage groups left in the spine are mostly lower-level: fractions, place value,
quadrilaterals — a poor thematic fit for these careers). That is an honest, structural mismatch
between "which business sectors are missing" and "which math skills are missing," not a scoring
bug. Where it applies, `QUALITY = Q1+Q2+Q3+Q4` (0–2 each, max 8): **Q1** dilemma sharpness, **Q2**
career/stakes authenticity, **Q3** engagement hook, **Q4** metric integrity (real ratio, not
gameable).

## Ranked

| # | Concept | Business area | Coverage | Quality | Data | Skills closed |
|---|---|---|---|---|---|---|
| C5 | The Cooling Curve | Energy & grid (data-center cooling) | **2.0** | 8/8 | HIGH | 2 genuinely zero |
| C1 | The Compute Lease | AI & semiconductors (cloud/GPU infra) | **1.6** | 8/8 | HIGH | 1 term + 1 how-to zero |
| C13 | The Downbeat Split | Music theory / composition | **1.2** | 8/8 | MEDIUM | 2 how-tos zero (2 groups) |
| C2 | The Alert Curve | Cybersecurity (enterprise SOC) | **1.2** | 7/8 | MEDIUM | 2 how-tos zero |
| C3 | The Bioreactor Bid | Biotech / CRO manufacturing | **0.96** | 6/8 | MEDIUM | 1 term + 1 how-to zero |
| C11 | The Enclosure Call | Product design (industrial/IDEO-style) | **0.72** | 7/8 | MEDIUM | 2 terms zero |
| C9 | The Transfer Window | Aerospace & space tech | **0.0** | 8/8 | HIGH | 0 new / thickens 6 |
| C10 | The Qubit Budget | Quantum computing | **0.0** | 8/8 | HIGH | 0 new / thickens 4 |
| C12 | The Panel Layout | Human factors / ergonomics | **0.0** | 8/8 | HIGH | 0 new / thickens 7 |
| C6 | The Peg Line | Crypto / stablecoin infrastructure | **0.0** | 8/8 | HIGH | 0 new / thickens 8 |
| C14 | The Placement Test | Social-media influencing / SEO / ad-placement optimization | **0.0** | 7/8 | MEDIUM | 0 new / thickens 2 |
| C8 | The Attribution Sample | Ad-tech / performance marketing | **0.0** | 6/8 | MEDIUM | 0 new / thickens 1 |
| C4 | The Fee Ladder | Financial market infrastructure (custody) | **0.0** | 5/8 | MEDIUM | 0 new / thickens 7 |
| C7 | The Approval Graph | Enterprise software / cloud | **0.0** | 4/8 | MEDIUM | 0 new / thickens 8 |

**Recommendation.** Write **C5 (The Cooling Curve)** first — it's the only concept here with both
a real coverage claim *and* a clean HIGH-feasibility, non-gameable ratio metric, and it closes the
last two how-tos (`volume-of-a-pyramid`, `volume-of-a-cone`) that Geometry/Surface Area And Volume
still needs. **C1 (The Compute Lease)** is the strongest second pick — real coverage (Series group),
HIGH data (published cloud GPU rate cards), and directly answers the AI/semiconductors gap that
prompted this batch. **C13 (The Downbeat Split)** is worth a look too: it's the only concept in
this batch that closes real zero-coverage skills in two different Fractions groups at once
(`multiply-two-mixed-numbers`, `divide-a-fraction-by-a-fraction`) through one honestly-motivated
scenario, not two bolted-together problems. After those three, the four zero-coverage-but-
quality-8 concepts (**C9 aerospace, C10 quantum, C12 human factors, C6 crypto**) are peers, not a
ranked ladder — pick whichever business area matters most for corpus diversification; all four
cite real, named, verifiable sources (NASA/JPL trajectory tools, IBM/AWS quantum per-shot pricing,
Fitts's Law / ISO 9241-9, Circle/Tether reserve attestations) and none required inventing a
number. **C7 (The Approval Graph)** is the weakest concept in the batch on quality (4/8) —
workflow-governance as a premise reads dry and the protagonist is generic; if enterprise
software/cloud needs a slot, it should get a sharper hook before `case-write`, not this version
as-is.

Do not write more than 2 of these before a QA checkpoint, same guidance the prior batch's
Recommendation gave and the same pattern that surfaced C4's real margin defect there.

---

### C1 — The Compute Lease   ·   score 1.6   ·   quality 8/8   ·   tier T2
**Protagonist.** Sofia Reyes, Infrastructure Capacity Planner at a mid-size AI cloud/GPU-rental
startup. Personally at stake: she has to recommend a GPU-cluster commitment to the board Friday,
and whichever way it goes, she owns the cost line for the next two years.

**The dilemma.** A.) Sign a 3-year fixed-rate GPU cluster lease — lower cost per GPU-hour, locked
in regardless of demand, so the total committed cost is a simple fixed series OR B.) Buy on-demand
cloud GPU capacity that scales with actual customer growth — higher per-hour rate, but the total
spend tracks a geometric series driven by the company's real month-over-month growth rate, which
could land above or below the fixed lease depending on whether growth compounds as projected.

**Primary metric.** Total infrastructure cost per GPU-hour delivered to paying customers over the
24-month period (a ratio, computed by summing each option's series under a stated growth-rate
range, not a single point estimate).

**Why it's close.** The fixed lease wins if growth compounds close to the projected rate — it
spreads a flat cost over more and more usage. But if growth undershoots, the lease's fixed-payment
series keeps arriving whether or not the GPUs are used, while on-demand's series tracks real
demand exactly, just at a worse per-unit rate. Neither option dominates until the growth-rate
assumption is fixed — which is exactly what the series convergence/divergence math is for.

**Would close (2 skills, 1 how-to / 1 term, both genuinely zero):**
| id | kind | label |
|---|---|---|
| calculus-series | term | Series |
| calculus-how-to-determine-whether-a-series-converges-or-diverges | how-to | How to determine whether a series converges or diverges |

**Already-covered skills it also exercises.** `calculus-sequence` (n=1, reinforced by modeling
monthly usage as a sequence before summing). Deliberately does *not* claim `calculus-taylor-series`
or its how-to — a Taylor expansion isn't a natural tool for a GPU lease cost comparison, and
forcing it would be exactly the "unreachable skill" lie the skill's own rules forbid.

**Data feasibility: HIGH.** Named sources: published cloud GPU on-demand and reserved pricing
(AWS EC2 P5/H100 instance pricing pages, CoreWeave and Lambda Labs published rate cards — all
real, public, dated price lists); realistic demand-growth-rate ranges from hyperscaler public
10-K/investor-deck disclosures on AI infrastructure capex growth.
Sources I am NOT confident about: this specific fictional startup's actual customer growth curve
— stated as a Modeling Assumption anchored to the published industry growth-rate range, not a
literal transferred number.

**Sensitivity (SPEC §6).** None — routine infrastructure-procurement math.

**Split risk.** NONE.

---

### C2 — The Alert Curve   ·   score 1.2   ·   quality 7/8   ·   tier T2
**Protagonist.** Jordan Lee, Tier-2 SOC Analyst at a financial-services company. Personally at
stake: mid-shift, he has to decide whether to wake the on-call incident commander at 2 a.m. — a
false page costs him credibility with the team; a missed real escalation costs a lot more.

**The dilemma.** A.) Escalate now, because the raw alert count this hour is already above
threshold OR B.) Hold one more sampling interval and compute the actual instantaneous rate of
change of the alert-rate function — a composite of traffic volume and threat score — to confirm
it's truly accelerating before waking anyone.

**Primary metric.** Confirmed real incidents per false escalation triggered (a ratio comparing
threshold-only escalation against derivative-confirmed escalation).

**Why it's close.** A raw count above threshold is fast but noisy — a traffic spike alone can
trip it. Waiting for the derivative to confirm real acceleration cuts false escalations, but the
wait itself has a cost: a real attack given one more interval to run is a real attack that ran
longer. Neither policy is free.

**Would close (2 how-tos, both genuinely zero):**
| id | kind | label |
|---|---|---|
| calculus-how-to-use-the-chain-rule-to-differentiate-a-composite-function | how-to | How to use the chain rule to differentiate a composite function |
| calculus-how-to-use-the-product-rule-to-differentiate-a-product-of-functions | how-to | How to use the product rule to differentiate a product of functions |

**Already-covered skills it also exercises.** `calculus-tangent-line` and `calculus-differentiable`
(both n=2, reinforced via reading the tangent line's slope as the instantaneous escalation rate).
Deliberately does not also claim the quotient rule — one composite-function example (traffic
volume × threat score) carries the case; stacking a second unrelated composite function just to
claim a third how-to would be skill-stuffing.

**Data feasibility: MEDIUM.** The composite alert-rate function itself is a stated scenario, but
its scale is anchored to real, named, published incident-response benchmark reports (IBM Cost of
a Data Breach report's mean-time-to-detect figures; Verizon DBIR alert-volume statistics) — the
category exists and is public, but the exact function is necessarily a Modeling Assumption, which
is why this is MEDIUM and not HIGH.

**Sensitivity (SPEC §6).** Financial-services SOC framing — keep it about the escalation-policy
decision, never a real breach or named institution. Routine register, comparable to Key Length.

**Split risk.** NONE.

---

### C3 — The Bioreactor Bid   ·   score 0.96   ·   quality 6/8   ·   tier T2
**Protagonist.** Wei Zhang, Bioprocess Engineer at a contract manufacturing organization (CRO)
scaling up a client's cell-culture batch. Personally at stake: his vessel recommendation is the
line item the client's program budget lives or dies on for this production run.

**The dilemma.** A.) Use a standard cylindrical stirred-tank bioreactor — well-characterized
volume, cheaper, but mixing efficiency caps the achievable cell density OR B.) Use a wave/rocking
bioreactor whose flexible bag forms a curved profile — better mixing, higher potential yield, but
its true working volume at the target fill level has to be computed via the disk method from the
bag's cross-sectional profile (a solid of revolution), not a simple cylinder formula.

**Primary metric.** Liters of viable product yielded per dollar of vessel cost (a ratio built from
the net cumulative yield — the area between the batch's feed-rate and uptake-rate curves — divided
by each vessel's total cost).

**Why it's close.** Option B's better mixing genuinely raises yield per the growth-kinetics
curve, but its vessel and validation cost is higher and its usable volume is smaller once you
integrate the actual bag profile rather than assume full nominal capacity — the two effects pull
in opposite directions on the same ratio.

**Would close (2 skills, 1 how-to / 1 term, both genuinely zero):**
| id | kind | label |
|---|---|---|
| calculus-volume-of-revolution | term | Volume Of Revolution |
| calculus-how-to-find-the-volume-of-a-solid-of-revolution-using-the-disk-method | how-to | How to find the volume of a solid of revolution using the disk method |

**Already-covered skills it also exercises.** `calculus-area-between-two-curves` and its how-to
(both n=1, reinforced by computing net cumulative yield as the area between the feed and uptake
curves) — genuinely load-bearing, not a stretch, since that's literally what "net yield over the
batch" means.

**Data feasibility: MEDIUM.** Real, named sources: published bioreactor vendor spec sheets
(Sartorius and Cytiva both publish wave-bioreactor technical datasheets with bag profile and
capacity curves) and standard Monod-kinetics-style growth curves from peer-reviewed bioprocess
literature. Not confident about: a specific CRO's per-run cost — anchored to published CDMO
industry pricing-benchmark surveys (e.g., BioPlan Associates) as a stated Modeling Assumption,
not a hard citation.

**Sensitivity (SPEC §6).** None.

**Split risk.** NONE.

---

### C4 — The Fee Ladder   ·   score 0.0   ·   quality 5/8   ·   tier T2
**Protagonist.** Marcus Alvarez, Securities Settlement Operations Analyst at a custody bank.
Personally at stake: sales needs a fee quote today for a new institutional client, and he's the
one who has to defend whatever number goes out.

**The dilemma.** A.) Quote a simplified flat effective rate, derived by converting the bank's true
recursive tiered-fee schedule (each tier's charge depends on the balance remaining after the prior
tier's fee) into a single closed-form explicit rate — fast, quotable on the call, but an
approximation OR B.) Compute the actual fee tier-by-tier using the real recursive schedule — exact,
defensible, but takes real analyst time the sales deadline doesn't have.

**Primary metric.** Fee-quote error, as a percentage of the true recursively-computed annual fee.

**Would close (0 skills at true zero — the group has none; thickens the entire Proof And
Recursion group from n≈1 toward n≈2, via a genuine recursive-to-explicit conversion, not a
contrived one):** `discrete-mathematics-recursive-formula`,
`discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence`,
`discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula`.

**Data feasibility: MEDIUM.** Real custody fee-schedule *structures* are publicly disclosed in
fund prospectus/N-CSR filings on SEC EDGAR (fee tables genuinely show tiered custody charges), but
a specific recursive schedule for this fictional client is a stated Modeling Assumption anchored
to those real disclosed rate magnitudes.

**Sensitivity (SPEC §6).** None.

**Split risk.** NONE.

---

### C5 — The Cooling Curve   ·   score 2.0   ·   quality 8/8   ·   tier T2
**Protagonist.** Advait Rao, Facilities Engineer at a hyperscale AI data center. Personally at
stake: the GPU racks going in next quarter run hotter than anything the site has cooled before,
and his cold-plate fin recommendation is what keeps them from throttling.

**The dilemma.** A.) Spec a pyramidal fin array for the liquid cold plates — more surface area per
unit of material, better heat dissipation, but a more complex (costlier) mold OR B.) Spec simple
conical standoff fins — cheaper and faster to manufacture at the volumes this build needs, but
less surface area per fin, dissipating less heat per dollar of material.

**Primary metric.** Watts of heat dissipated per dollar of fin manufacturing cost.

**Why it's close.** The pyramidal design's extra surface area is real and directly improves
cooling — but it isn't free, and at data-center scale (tens of thousands of fins) even a modest
per-unit cost gap compounds fast. Whichever design wins on watts-per-dollar depends on both
shapes' actual surface area, not on which "sounds" like it cools better.

**Would close (2 how-tos, both genuinely zero):**
| id | kind | label |
|---|---|---|
| geometry-how-to-find-the-volume-of-a-pyramid | how-to | How to find the volume of a pyramid |
| geometry-how-to-find-the-volume-of-a-cone | how-to | How to find the volume of a cone |

**Already-covered skills it also exercises.** `geometry-surface-area` (n=3) — the actual decision
metric is a surface-area-per-cost computation, reinforcing the group's core term while closing the
two how-tos above via the material-volume side of the cost calculation.

**Data feasibility: HIGH.** Named sources: ASHRAE TC9.9 data-center thermal guidelines (the real,
published industry standard for data-center cooling); liquid-cooling cold-plate vendor technical
datasheets (CoolIT Systems, Vertiv both publish real spec sheets with fin geometry and heat-
dissipation figures); Uptime Institute cost-per-watt cooling infrastructure benchmarks.
Sources I am NOT confident about: an exact manufacturing cost for these two specific fin
geometries at this exact volume — stated as a Modeling Assumption anchored to the published
benchmark ranges.

**Sensitivity (SPEC §6).** None — routine facilities-engineering math.

**Split risk.** NONE.

---

### C6 — The Peg Line   ·   score 0.0   ·   quality 8/8   ·   tier T2
**Protagonist.** Priya Nathan, Treasury/Reserves Analyst at a regulated stablecoin issuer.
Personally at stake: she has to recommend a reserve-composition change before the next monthly
attestation report goes out under her name.

**The dilemma.** A.) Rebalance reserves toward more short-term Treasury bills — very small peg
deviation risk, keeping the absolute distance between market price and $1.00 tiny, but earning
less interest income OR B.) Rebalance toward a slightly longer-duration bond mix — meaningfully
more yield for the issuer, but a historically larger absolute peg deviation during rate-volatility
weeks.

**Primary metric.** Basis points of peg deviation (an absolute-value quantity) tolerated per
dollar of extra annual yield earned.

**Why it's close.** More yield is real money for the issuer, and the deviation risk is real but
usually small and short-lived — the case forces pricing exactly how much deviation is "worth" one
more dollar of yield, using the reserve totals (tens of billions of dollars — genuinely
scientific-notation scale) and the peg deviation (an absolute-value comparison against $1.00) side
by side.

**Would close (0 skills at true zero — the group has none; thickens Scientific Notation/Factorial/
Absolute Value from n≈1-2 toward n≈2-3):** `advanced-operations-scientific-notation` (reserve
totals), `advanced-operations-absolute-value` and
`advanced-operations-how-to-evaluate-an-absolute-value-expression` (peg deviation, genuinely
load-bearing — |price − $1.00| *is* the deviation metric, not a stretch).

**Data feasibility: HIGH.** Named, real, live sources: Circle's (USDC) and Tether's published
monthly reserve attestation reports (real, publicly filed, independently attested, disclosing
reserve composition and dollar totals in the billions); public stablecoin peg-price history from
CoinGecko/CoinMarketCap for real historical deviation data during known volatility events.

**Sensitivity (SPEC §6).** Keep this about the treasury-allocation decision, never about a named
real depeg incident's harm to holders — routine treasury-management register, not a crisis
narrative.

**Split risk.** NONE.

---

### C7 — The Approval Graph   ·   score 0.0   ·   quality 4/8   ·   tier T1/T2
**Protagonist.** Chloe Whitfield, Platform Engineer at a mid-size SaaS company. Personally at
stake: her redesign of the compliance-approval workflow ships next sprint, and the support-ticket
volume the week after tells everyone whether it worked.

**The dilemma.** A.) Keep approvals as a strictly sequential chain (a simple path graph) — easy to
reason about, but any one blocked approver stalls the whole chain OR B.) Allow parallel approval
paths with a required cycle-check before shipping — faster on average, but the workflow graph must
be proven cycle-free first.

**Primary metric.** Average approval turnaround hours per submitted request, computed as a
weighted shortest path across each graph design.

**Would close (0 skills at true zero — thickens Graph Theory from n≈1-3 toward n≈2-4):**
`discrete-mathematics-weighted-graph`,
`discrete-mathematics-how-to-find-the-shortest-path-between-two-vertices-in-a-weighted-graph`,
`discrete-mathematics-how-to-determine-whether-a-graph-has-an-euler-path-or-circuit` (the
cycle-check, genuinely load-bearing for option B's validity, not decorative).

**Data feasibility: MEDIUM.** The graph-topology math needs no citation. Realistic approval-
turnaround benchmarks exist in published SaaS workflow-vendor case studies (ServiceNow, Asana),
but not one single citable dataset — expect a stated Modeling Assumption anchored to the published
benchmark range.

**Sensitivity (SPEC §6).** None.

**Split risk.** NONE — but flagged as the weakest concept in this batch on quality (see
Recommendation): the premise reads dry and the protagonist is generic. Needs a sharper hook (a
real deadline, a real cost of the stall) before `case-write`.

---

### C8 — The Attribution Sample   ·   score 0.0   ·   quality 6/8   ·   tier T2
**Protagonist.** Derek Okafor, Performance Marketing Analyst at an ad-tech install-attribution
platform. Personally at stake: the weekly attribution report he ships to a mobile-game client is
the number that decides which channels get next month's ad budget.

**The dilemma.** A.) Simple random sample a subset of ad clicks to verify true installs — cheap,
fast, but risks missing a small, high-value channel if it's a small share of total clicks OR B.)
Stratified sample by ad-placement channel before verifying — catches every channel's true install
rate including rare ones, but costs more analyst time and delays the report.

**Primary metric.** Attribution error (percentage points) per analyst-hour spent verifying.

**Would close (0 skills at true zero — thickens Sampling And Experiments' one genuinely thin
skill):** `statistics-and-probability-multistage-sampling` (n=1), plus already-covered
`-stratified-sampling` and `-simple-random-sampling` as the case's actual comparison.

**Data feasibility: MEDIUM.** Sampling methodology needs no citation. Realistic install-
attribution/fraud-rate benchmarks are published in real industry reports (AppsFlyer's and
Adjust's annual "State of App Marketing" fraud-benchmark reports), but a specific channel-by-
channel install-rate table for this scenario is a stated Modeling Assumption anchored to those
published ranges.

**Sensitivity (SPEC §6).** None.

**Split risk.** NONE.

---

### C9 — The Transfer Window   ·   score 0.0   ·   quality 8/8   ·   tier T2
**Protagonist.** Talia Brooks, Trajectory Analyst at a small commercial launch company.
Personally at stake: the transfer-orbit design she signs off on this week is what the payload
customer's contract locks in.

**The dilemma.** A.) A direct, higher-thrust parametric burn trajectory — shorter transit time,
but a higher propellant mass fraction, which eats directly into deliverable payload mass OR B.) A
slower, lower-thrust parametric coast trajectory — less fuel burned, more payload mass available,
but a longer transit exposes the payload to more cumulative radiation.

**Primary metric.** Kilograms of payload deliverable per day of transit time.

**Why it's close.** More thrust delivers the payload faster, which is real value to a customer on
a schedule — but every kilogram of extra propellant is a kilogram the payload doesn't get, and the
tradeoff isn't linear once you actually parametrize position over time for both trajectories and
check where each one reaches the target orbit radius.

**Would close (0 skills at true zero — thickens Polar And Parametric from n=1 toward n=2, the
first case in this corpus to touch the group at all beyond its single existing entry):**
`pre-calculus-parametric-equation`, `pre-calculus-parameter`,
`pre-calculus-how-to-eliminate-the-parameter-to-find-a-rectangular-equation` (used exactly as
intended — eliminating the parameter to find where the trajectory crosses the target orbit
radius, not decorative).

**Data feasibility: HIGH.** Named, real, live sources: NASA JPL's public Trajectory Browser and
Horizons system (real, queryable orbital mechanics data); published smallsat/launch-provider
payload-vs-delta-v tradeoff tables (Rocket Lab and SpaceX both publish public payload user's
guides with real mass-fraction figures).

**Sensitivity (SPEC §6).** None — routine mission-design math, comparable in register to Wind
Triangle or Navigation.

**Split risk.** NONE.

---

### C10 — The Qubit Budget   ·   score 0.0   ·   quality 8/8   ·   tier T2
**Protagonist.** Sam Okafor, Quantum Software Engineer at a quantum-computing startup.
Personally at stake: this week's cloud-quantum-compute budget request is hers to defend, and the
register-size call determines whether the client's problem is exactly represented or
approximated.

**The dilemma.** A.) Commit budget to a 20-qubit register — cheaper, fits comfortably in the
near-term budget, but its 2²⁰ state space can't fully represent the client's problem, forcing an
approximation OR B.) Commit to a 24-qubit register — its 2²⁴ state space (16× larger) represents
the problem exactly, but real hardware error rates compound faster as qubit count rises, and
cloud-quantum time is billed per shot.

**Primary metric.** Dollars of cloud-quantum compute cost per successfully-completed (below-
error-threshold) shot.

**Why it's close.** The 24-qubit register is exact, which is real value — but the exponential
state-space growth (2²⁰ vs 2²⁴) drives both cost and error rate up together, so "more qubits" and
"better result per dollar" are not automatically the same claim once the per-shot billing and the
real published error-rate-vs-qubit-count curve are both priced in.

**Would close (0 skills at true zero — thickens Exponents from n=1-3 toward n=2-4, genuinely
load-bearing since 2²⁰ vs 2²⁴ *is* the state-space comparison the decision turns on, opens
`quantum-computing`, a domain not yet in `readmodel/domains.json`):**
`advanced-operations-base`, `advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-with-exponents-order`.

**Data feasibility: HIGH.** Named, real, live sources: IBM Quantum and Amazon Braket published
per-shot cloud-quantum-compute pricing (real, public rate cards); IBM's published quantum-volume
and gate-error-rate benchmarks by qubit count (real, publicly documented hardware specs).

**Sensitivity (SPEC §6).** None.

**Split risk.** NONE.

---

### C11 — The Enclosure Call   ·   score 0.72   ·   quality 7/8   ·   tier T2
**Protagonist.** Nina Odom, Industrial Designer at a consumer-product design studio (IDEO-style
consultancy), pitching enclosure form for a client's new portable speaker. Personally at stake:
whichever shape she recommends in Friday's client review is the one that gets tooled — a reversal
after tooling starts is a real budget line she'd have to explain.

**The dilemma.** A.) A cone-frustum-shaped enclosure — the client's audio engineer wants it for
acoustic dispersion, but the tapered mold costs more per unit and nests less efficiently for
shipping OR B.) A spherical enclosure — the design team's preferred signature shape for shelf
appeal, but spheres are the classic worst case for container packing density, driving per-unit
shipping cost up.

**Primary metric.** Total cost per unit at the client's target production volume — materials plus
mold tooling plus shipping, computed from each shape's actual surface area (material use) and
packing efficiency (shipping density).

**Why it's close.** Neither shape wins outright: the frustum's simpler shipping stacking is offset
by its costlier tapered mold, while the sphere's cheaper mold is offset by real, well-known
sphere-packing shipping waste — which one comes out ahead on total per-unit cost depends on the
actual numbers, not on which shape "looks" more efficient.

**Would close (2 terms, both genuinely zero — the two shapes the case's own dilemma requires,
not a third shape bolted on to inflate the count):**
| id | kind | label |
|---|---|---|
| geometry-cone | term | Cone |
| geometry-sphere | term | Sphere |

**Already-covered skills it also exercises.** `geometry-3-dimensional` (n=4),
`geometry-how-to-name-a-3-d-shape` (n=1) — both genuinely reinforced in comparing the two forms.

**Data feasibility: MEDIUM.** Sphere-packing efficiency (~74% maximum, per the well-known
Kepler-conjecture result) and cone/frustum geometry need no citation. Injection-molding tooling-
cost benchmark ranges are published in industrial-design/manufacturing trade press (real DFM
cost-guide publications); ocean-freight per-container shipping cost is available from published
indices (Freightos Baltic Index). Not confident about: this specific client's exact production
volume or per-unit shipping cost — stated Modeling Assumptions anchored to those published ranges.

**Sensitivity (SPEC §6).** None.

**Split risk.** NONE.

---

### C12 — The Panel Layout   ·   score 0.0   ·   quality 8/8   ·   tier T2
**Protagonist.** Marcus Feld, Human Factors Engineer at a medical-device company. Personally at
stake: his control-panel layout sign-off ships to the next hardware revision, and a miss-rate
problem discovered after tooling is a recall-review conversation with his name on it.

**The dilemma.** A.) A larger critical button placed close to the resting hand position — a lower
predicted movement time and miss rate, but it eats panel space needed for other required controls
OR B.) A smaller button placed farther away — frees panel space for the other controls, but
carries a measurably higher predicted movement time and miss rate.

**Primary metric.** Seconds of predicted task-completion time per successful actuation, across the
full control sequence — not just the one button, which is what forces a genuine whole-panel
optimization rather than an easy single pick.

**Why it's close.** The larger/closer button is safer in isolation, which is real — but panel
space is a fixed constraint, and taking it from another control has its own movement-time cost
elsewhere in the same sequence. The layout that minimizes total task time isn't obvious until the
whole panel's critical points are found and classified.

**Would close (0 skills at true zero — thickens Applications Of Derivatives from n=2 toward n=3,
using Fitts's Law, a real, well-established, citable human-factors model, not an invented
function):** `calculus-critical-point`, `calculus-how-to-find-critical-points-of-a-function`,
`calculus-how-to-use-the-first-derivative-test-to-classify-a-critical-point`,
`calculus-how-to-solve-an-optimization-problem-using-derivatives` — all genuinely load-bearing:
finding and classifying the panel-time function's critical point *is* the layout decision.

**Data feasibility: HIGH.** Named, real sources: Fitts's Law itself (Paul Fitts, 1954 — the
standard predictive model for pointing/target-acquisition movement time, still in active use);
ISO 9241-9, the published international standard for evaluating pointing-device performance using
Fitts's Law, which documents real coefficient values from peer-reviewed test studies.

**Sensitivity (SPEC §6).** Medical-device framing — keep this about the layout-optimization
decision, never about an actual patient-harm incident. Routine engineering register.

**Split risk.** NONE.

---

### C13 — The Downbeat Split   ·   score 1.2   ·   quality 8/8   ·   tier T2
**Protagonist.** Elena Cross, staff arranger at a commercial audio production house. Personally at
stake: her cue for a client's ad spot has to land inside an exact broadcast time slot, and she's
the one in the booth when the ensemble runs it.

**The dilemma.** A.) Arrange the passage with straight subdivisions — a run of mixed-number note
values (e.g., dotted-quarter phrases) multiplied out to a total duration — simple to read, fast to
rehearse, but the total lands a hair off the exact target slot, forcing a small tempo compromise
OR B.) Arrange with a syncopated subdivision — splitting a beat by dividing a fraction by a
fraction to hit the exact target duration precisely — but the uneven subdivision is harder for the
ensemble to sight-read, adding real rehearsal time before the take is clean.

**Primary metric.** Rehearsal minutes required per second of timing accuracy gained (a ratio — the
straight version isn't "wrong," it's cheaper per second of precision it doesn't buy).

**Why it's close.** The straight subdivision is genuinely easier and cheaper in session time, and
close enough that many cues would ship with it — but a broadcast slot is exact, and the syncopated
version's extra precision has a real, billable rehearsal cost, not a free upgrade. Whether the
precision is worth the extra minutes depends on the actual numbers, not on which one "sounds"
harder.

**Would close (2 how-tos, both genuinely zero, across two spine groups):**
| id | kind | label |
|---|---|---|
| fractions-how-to-multiply-two-mixed-numbers | how-to | How to multiply two mixed numbers |
| fractions-how-to-divide-a-fraction-by-a-fraction | how-to | How to divide a fraction by a fraction |

**Already-covered skills it also exercises.** `fractions-how-to-multiply-a-fraction-and-a-mixed-number`
and `fractions-how-to-divide-fractions-and-mixed-numbers` (both n=1) — genuinely reinforced while
building the total-duration and subdivision computations, not padding.

**Data feasibility: MEDIUM.** The rhythm/duration math needs no citation. Real, named source for
the cost side: American Federation of Musicians (AFM) published session-rate scales (real, public
union rate cards for session time) anchor a realistic per-minute rehearsal cost. Not confident
about: this specific cue's exact timing-error tolerance for the client's broadcast slot — stated
as a Modeling Assumption, same pattern as every other constrained-deadline case in this corpus.

**Sensitivity (SPEC §6).** None.

**Split risk.** NONE — two skills from two related Fractions groups, closed by one honestly-
motivated scenario (total duration, then subdivision), not two problems stitched together.

---

### C14 — The Placement Test   ·   score 0.0   ·   quality 7/8   ·   tier T2
**Protagonist.** Jaylen Ortiz, Social Media/Influencer Marketing Strategist at a mid-size
direct-to-consumer brand. Personally at stake: this week's paid-placement test plan is what next
quarter's ad budget gets allocated against, and he's presenting the recommendation Monday.

**The dilemma.** A.) Run a single fixed placement — the product mention airs at one fixed point in
the sponsored video for the whole campaign window — cheap, simple, but tests only one hypothesis
about what drives conversion OR B.) Run a full multi-variant test cycling through several possible
placement orderings (early/mid/late mention combined with two call-to-action styles — a real
permutation space) — captures far more signal about what actually drives conversion, but splits
the same fixed ad-spend budget across every variant, thinning the statistical confidence each one
gets.

**Primary metric.** Statistically attributable conversions per dollar of ad spend, comparing the
single-placement plan against the full permutation-space test.

**Why it's close.** The multi-variant test is real information the single placement can't provide
— but each additional variant divides a fixed budget thinner, and a variant that gets too little
spend produces a conversion-rate estimate too noisy to act on. More permutations tested isn't
automatically more useful once the budget-per-variant is priced in.

**Would close (0 skills at true zero — thickens Statistics And Probability/Probability's two
genuinely thin skills):** `statistics-and-probability-permutation` and
`statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-permutation` (both n=1),
used exactly as intended — the number of distinct placement/CTA orderings *is* the permutation
computation the budget-split decision turns on.

**Data feasibility: MEDIUM.** The combinatorics math needs no citation. Realistic paid-social
conversion-rate and CPM benchmarks are published in real industry reports (Meta and Google Ads
publish benchmark reports; IAB and eMarketer publish industry-wide benchmark figures) — the
category is public, but no single source gives this exact scenario's numbers, so the campaign's
specific conversion figures are a stated Modeling Assumption anchored to those published ranges.

**Sensitivity (SPEC §6).** None — routine marketing-analytics math.

**Split risk.** NONE.

---

## Next step

`Approve a concept, then run case-write on it.` Suggested order per the Recommendation above:
**C5 → C1 → C13 → (pick one of C9/C10/C12/C6 for corpus diversification)**. Say which to write
first, or approve the whole ordered batch and each will move through `case-write` →
`case-research` → `case-readiness` in sequence.
