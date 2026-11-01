# Concept sheet — Batch C, current-events-anchored (10 cases)

Source: a 2026-09-06 economic-moat/chokepoint scan (9 named business topics with tickers/sectors)
cross-referenced against `standards_spine.json`'s live thin-cluster gap list (2026-09-06 scan,
`uncovered: 0` at that point — no true zero-coverage skills remained, so this batch targets the
highest-severity *thin* (n=1/n=2) clusters instead). A 10th concept was added to round out the
batch, targeting the one full-group thin cluster (Fractions/Addition & Subtraction) not otherwise
covered. **These are concepts only** — nothing here has been through `case-research` or
`case-write`. Business-topic framing is grounded in real, named companies/mechanisms; exact dollar
figures, rates, and technical specs are NOT yet sourced and must be verified in `case-research`
per SPEC.md §5 — never presented as sourced until actually checked.

---

## 1. The Fee Route (Card-Network Settlement Rail vs. Stablecoin Rail)
**Topic gap closed:** Discrete Mathematics / Graph Theory — 8 of 8 skills thin (near-full close
opportunity).
**Narrative.** An AI checkout agent (or the merchant ops team configuring it) must decide, for
each transaction, whether to route payment over the traditional card network (Visa/Mastercard —
real, live 2026-09 tension: AI payment agents are increasingly built to route around 2-3%
interchange fees) or a stablecoin settlement rail (near-zero fee, but no chargeback/fraud-dispute
recourse). Model the payment network as a real graph (banks/processors as nodes, settlement paths
as edges) and reason about path cost vs. path risk.
**Problem.** A) Card rail — higher fee, built-in chargeback protection modeled as a real expected
value. B) Stablecoin rail — near-zero fee, but a real, disclosed dispute/fraud-loss exposure with
no recourse.
**Primary metric.** Net revenue retained per $1,000 processed, after fees and expected
fraud/dispute losses, computed via the shortest-cost path through the settlement graph.
**Rubric.** Trap: choosing the lowest raw fee without weighting the real expected fraud-loss
exposure; must force genuine graph-theory vocabulary (node, edge, path, weighted graph) not just a
verbal cost comparison.
**Margin target.** 8–15%.
**Feasibility.** HIGH — Visa/Mastercard interchange rates are public; stablecoin settlement cost
and card-network fraud-loss rate data are documented by payments-industry sources (Forbes,
Nilson Report, card network 10-Ks).

---

## 2. The Approval Gate (Agentic Enterprise Orchestration Logic)
**Topic gap closed:** Discrete Mathematics / Formal Logic — 8 of 8 skills thin (full close).
**Narrative.** An enterprise ops team (using a platform like Salesforce Agentforce, ServiceNow, or
Microsoft Copilot Studio — real, named 2026 category) must design the actual approval-gate logic
for an AI agent handling customer refunds: which conditions let it auto-approve vs. escalate to a
human. Two competing gate designs look different in prose but may be logically equivalent or
meaningfully different — the case forces building real truth tables.
**Problem.** A) A stricter-sounding compound condition (e.g., "approve only if amount < $50 AND
customer tenure > 1 year"). B) A differently-worded condition that a stakeholder claims is
equivalent but isn't (a De Morgan's-law trap).
**Primary metric.** False-approval rate vs. escalation-workload tradeoff, computed per gate
design via truth table.
**Rubric.** Trap: assuming two logically different compound conditions are equivalent because
they "sound similar," without building the truth table to check.
**Margin target.** 8–15%.
**Feasibility.** HIGH — no exotic sourcing; enterprise AI-agent-gating is a well-documented,
named 2026 product category (Salesforce, ServiceNow, Microsoft all publish real approval-workflow
documentation).

---

## 3. The Yield Die (Leading-Edge Foundry Wafer Economics)
**Topic gap closed:** Advanced Operations / Scientific Notation, Factorial, Absolute Value —
9 of 8 skills thin (near-full close on the Scientific Notation half).
**Narrative.** A chip designer working with a leading-edge foundry (TSMC — real, named, the
central chokepoint of the entire 2026 AI buildout) must choose a die size for a new chip: smaller
die (more chips per wafer, but a higher fraction lost to random defects) vs. larger die (fewer
chips per wafer, but each one covers less defect-prone area proportionally... actually the
opposite — larger die area means MORE defects per die on average). Real transistor counts
(tens of billions) and defect densities (per cm²) force scientific notation throughout.
**Problem.** A) Smaller die — more gross die per wafer, using the wafer-area-divided-by-die-area
formula, but yield-per-die drops as advanced-node defect density is applied. B) Larger die — fewer
gross die per wafer, but a real yield-per-die trade against the same defect density.
**Primary metric.** Net good (yielding) dies per wafer × price per die, computed with every
intermediate figure in scientific notation.
**Rubric.** Trap: comparing gross die count without applying the yield model (a die-size-dependent
function using real defect-density data), overstating the smaller die's advantage.
**Margin target.** 8–14%.
**Feasibility.** MEDIUM-HIGH — semiconductor-industry defect-density and yield-model publications
(IEEE, foundry technical disclosures, industry analyst reports) are real and citable; exact current
TSMC node figures may need to be handled as disclosed, industry-representative assumptions if
proprietary exact figures aren't public.

---

## 4. The Setpoint Call (Industrial Process-Control Optimization)
**Topic gap closed:** Calculus / Derivatives — 7 of 9 skills thin.
**Narrative.** A process engineer at an industrial plant (chemical processing, real-world
"Industrials, energy & defense" chokepoint category) must set a continuous process variable
(temperature, flow rate) to minimize cost or maximize throughput, subject to a real hard safety
constraint. This is a genuine calculus-native optimization problem, not a plugged formula.
**Problem.** A) Optimize the process purely for minimum cost, using an actual derivative of a
real or realistic cost function — but the unconstrained optimum may fall outside a safe operating
range. B) A more conservative fixed setpoint that's provably safe but not cost-optimal.
**Primary metric.** Cost per unit output at the derivative-found optimum (checked against the
safety constraint) vs. a naive fixed setpoint.
**Rubric.** Trap: finding the unconstrained calculus optimum and treating it as final without
checking it against the stated safety/feasibility bound.
**Margin target.** 8–15%.
**Feasibility.** HIGH — process-control cost-optimization is a standard, well-documented
industrial-engineering topic; real or realistic cost-function parameters are available from
industrial-engineering textbooks/case studies.

---

## 5. The Sample Plan (Bioprocess Manufacturing Consumables QC)
**Topic gap closed:** Statistics and Probability / Sampling and Experiments — 5 of 14 skills thin.
**Narrative.** A biologics manufacturing plant (single-use bioreactor consumables — Sartorius,
Thermo Fisher, Cytiva are real, named companies in this space) must decide how many quality-control
samples to pull per production batch, trading inspection cost against the real probability of
shipping a contaminated or out-of-spec batch undetected.
**Problem.** A) Pull fewer QC samples — cheaper, faster batch release, but a higher real
probability of an undetected defect reaching a patient/customer. B) Pull more QC samples — costs
more and delays release, but meaningfully lowers undetected-defect probability, subject to
diminishing returns.
**Primary metric.** Expected total cost (inspection cost + probability-weighted expected recall/
liability cost) per batch, as a function of sample size.
**Rubric.** Trap: assuming defect-detection probability scales linearly with sample size instead
of following the real diminishing-returns curve (hypergeometric/binomial sampling theory).
**Margin target.** 8–12%.
**Feasibility.** MEDIUM — FDA/biopharma quality-control sampling standards (e.g., ANSI/ASQ Z1.4)
are real and public; specific contamination-rate figures likely need to be disclosed, realistic
Modeling Assumptions grounded in published industry QC-failure-rate ranges.

---

## 6. The Schedule Explosion (AI Accelerator Compute Scheduling)
**Topic gap closed:** Advanced Operations / Factorial — part of the same 8-skill cluster as
concept #3, targeting the Factorial half specifically (pair, not duplicate).
**Narrative.** A cloud provider (Nvidia GPU fleets — real, named, the central 2026 AI-compute
chokepoint) must schedule a batch of training jobs across a fixed GPU fleet. The number of
possible job orderings is a factorial that explodes past a small fleet size, forcing the provider
to use an approximation/heuristic instead of true brute-force optimal scheduling.
**Problem.** A) Attempt a "perfect" brute-force schedule search — provably optimal in principle,
but the factorial explosion makes it computationally infeasible past a small job count, which the
case forces the learner to compute directly. B) A greedy/heuristic scheduling rule — computable
in reasonable time, provably suboptimal by a bounded, calculable amount.
**Primary metric.** GPU-hours wasted (idle time) per scheduling strategy, at a realistic fleet/job
scale.
**Rubric.** Trap: assuming "computers are fast" makes brute-force scheduling always feasible,
without actually computing how large the factorial becomes at realistic job counts.
**Margin target.** 8–15%.
**Feasibility.** HIGH — GPU scheduling/job-shop-scheduling computational-complexity facts are
standard computer-science content; no proprietary data needed, since the factorial-explosion point
is a pure math fact.

---

## 7. The Referral Cut (Marketplace Seller-Access Fee Stack)
**Topic gap closed:** Fractions / Multiplication of Fractions — 7 of 4 skills thin (near-full
close).
**Narrative.** A third-party seller on a major marketplace (Amazon, Shopify, or Etsy — real, named
"third-party marketplace seller-access gate" category) compares two fulfillment paths, each with
a different referral-fee fraction and a different fraction of inventory value tied up in the
fulfillment method, to find true net margin per unit.
**Problem.** A) Self-fulfillment — lower referral-fee fraction, but a larger fraction of capital
tied up in held inventory. B) Marketplace-managed fulfillment (e.g., FBA-style) — higher referral/
fulfillment-fee fraction taken off the top, but less capital tied up and faster access to the
platform's premium placement/demand-aggregation gate.
**Primary metric.** Net margin per unit sold, computed by chaining fraction multiplications
(price × (1 − fee fraction) × (1 − further fee fraction)) in the correct order.
**Rubric.** Trap: multiplying sequential percentage/fraction cuts as if they were additive
(subtracting fee fractions from 1 and summing) instead of correctly compounding them
multiplicatively.
**Margin target.** 8–15%.
**Feasibility.** HIGH — Amazon/Shopify referral-fee and fulfillment-fee schedules are real,
public, and precisely documented on their own seller-help pages.

---

## 8. The Vein-to-Vein Window (Cell & Gene Therapy Manufacturing Limit)
**Topic gap closed:** Calculus / Limits and Continuity — 6 of 6 skills thin (full close).
**Narrative.** A hospital logistics coordinator manages a personalized cell therapy (CAR-T —
real, named "cell & gene therapy manufacturing/administration" category) that has a hard
"vein-to-vein" time limit: cells collected from a patient must be manufactured, shipped back, and
re-administered before a strict biological expiration window, or the dose becomes unusable. This
is a literal, real-world instance of a hard limit, not a metaphor.
**Problem.** A) A faster but costlier manufacturing/shipping path that keeps the dose safely
inside the viability window with margin to spare. B) A slower, cheaper path that is only viable if
nothing goes wrong — modeled as a function of elapsed time approaching the hard cutoff limit, where
viability doesn't fade gradually but drops sharply at the boundary.
**Primary metric.** Probability the dose remains viable at re-administration, modeled via the
behavior of a viability function as elapsed time approaches the hard limit.
**Rubric.** Trap: treating the viability window as a soft average/typical case ("it's usually
fine") instead of recognizing the real discontinuity at the hard cutoff — a delay that's "only
a little over" the limit isn't "a little less viable," it can be a cliff-edge failure.
**Margin target.** 6–10% — the case's tension is inherently about margin-for-error inside a fixed
window, not a large dollar swing.
**Feasibility.** MEDIUM — the real biological/logistics "vein-to-vein time" concept for CAR-T
therapies is documented in medical/pharma-logistics literature (real published typical windows);
exact per-patient/per-manufacturer figures will likely need disclosed Modeling Assumptions grounded
in published typical ranges.

---

## 9. The Equivalent Ledger (Deterministic System-of-Record Verification)
**Topic gap closed:** Basic Operations / Factoring — 7 of 6 skills thin (near-full close).
**Narrative.** An enterprise engineering team maintains a core "system of record" (a ledger/ERP
reconciliation engine — real, named "deterministic system-of-record action rail" category, a live
2026 tension as companies bolt probabilistic AI onto systems that must stay perfectly
deterministic) and must verify that an AI-rewritten version of a legacy reconciliation formula is
*exactly* mathematically equivalent to the original — not just "usually matching" on test data.
**Problem.** A) Trust the AI-rewritten formula because it matches on a sample of test transactions
— fast, but only probabilistic confidence. B) Actually factor both the original and rewritten
expressions to prove structural equivalence — slower, but the only real guarantee a deterministic
system of record can rely on.
**Primary metric.** Whether the two formulas are provably equivalent (factor to the identical
expression) vs. merely coincidentally matching on the tested sample values.
**Rubric.** Trap: confirming "equivalence" by testing a handful of sample values and finding they
match, without actually factoring both expressions to prove they're structurally the same
function (a classic incomplete-proof trap).
**Margin target.** 5–10% — the point of this case is a binary provable/not-provable outcome, not a
dollar-margin dilemma; margin here can be framed around the cost difference between the two
verification approaches (time cost of proof vs. residual risk of relying on sampling).
**Feasibility.** HIGH — no proprietary data needed; the mathematical content (factoring to prove
function equivalence) is self-contained, and the enterprise "AI rewriting legacy deterministic
code" framing is a well-documented 2026 industry conversation (no specific real company's exact
code needs citing, since the case can use a realistic, disclosed constructed formula).

---

## 10. The Interconnection Queue (Grid Capacity Allocation for AI Datacenters)
**Topic gap closed:** Fractions / Addition and Subtraction of Fractions — 8 of 4 skills thin
(full close — every skill in the group sits at n=1 today).
**Narrative.** A regional utility manages a substation's grid interconnection queue — a real,
widely-reported 2026 bottleneck on new AI datacenter capacity, where fractional shares of
remaining substation capacity are allocated across competing datacenter/industrial bids with
different fractional capacity needs and unlike "denominators" (different units of the same total
capacity pool expressed as different fractions of it).
**Problem.** A) Approve a bid needing a fraction of the substation's remaining capacity now, even
though it leaves an awkward remaining fraction that may not cleanly fit any other pending bid.
B) Hold the queue slot open, hoping a better-fitting combination of smaller fractional bids arrives
— requiring real fraction addition/subtraction with unlike denominators to check what actually
remains after each combination.
**Primary metric.** Remaining allocatable capacity fraction after each bid combination, and
whether a given project's fractional need can still be met from what's left.
**Rubric.** Trap: adding/subtracting fraction numerators directly without finding a common
denominator first, over- or under-allocating the substation's real capacity.
**Margin target.** 8–15%.
**Feasibility.** HIGH — grid interconnection queue bottlenecks for datacenters are extensively,
publicly reported (utility filings, DOE/FERC data, trade press) in 2026; exact regional capacity
figures can be grounded in real, disclosed utility interconnection-queue reporting.

---

## Summary table

| # | Concept | Skill gap group | Gap severity (of total) | Feasibility |
|---|---|---|---|---|
| 1 | The Fee Route | Discrete Math / Graph Theory | 8 of 8 thin | HIGH |
| 2 | The Approval Gate | Discrete Math / Formal Logic | 8 of 8 thin (full close) | HIGH |
| 3 | The Yield Die | Advanced Ops / Scientific Notation | 9 of 8 thin (near-full) | MEDIUM-HIGH |
| 4 | The Setpoint Call | Calculus / Derivatives | 7 of 9 thin | HIGH |
| 5 | The Sample Plan | Statistics / Sampling and Experiments | 5 of 14 thin | MEDIUM |
| 6 | The Schedule Explosion | Advanced Ops / Factorial | (shares cluster with #3) | HIGH |
| 7 | The Referral Cut | Fractions / Multiplication of Fractions | 7 of 4 thin (near-full) | HIGH |
| 8 | The Vein-to-Vein Window | Calculus / Limits and Continuity | 6 of 6 thin (full close) | MEDIUM |
| 9 | The Equivalent Ledger | Basic Operations / Factoring | 7 of 6 thin (near-full) | HIGH |
| 10 | The Interconnection Queue | Fractions / Addition & Subtraction | 8 of 4 thin (full close) | HIGH |

None of these 10 have been through `case-research` or `case-write`. Recommended write order:
#2, #7, #10 first (full/near-full closes, HIGH feasibility, no exotic sourcing) — then #1, #4, #6,
#9 (HIGH feasibility) — then #3, #5, #8 (MEDIUM/MEDIUM-HIGH feasibility, need real source checks
during `case-research` before committing to exact technical figures).
