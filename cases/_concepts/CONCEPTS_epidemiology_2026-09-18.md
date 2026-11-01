# Concept sheet — Epidemiology & Public Health

Target picked by reading `readmodel/domains.json`'s `epidemiology` entry directly (no existing
concept sheet covers this domain at the right coverage level). The domain's own
`signature_skills[]`/`uncovered_signature_skills` list is **stale for gap-finding purposes** —
every one of its 8 signature skills was checked live against `readmodel/standards_spine.json` on
2026-09-18 and all 8 are already well covered (n=4 to n=29; see table below). Chasing the
signature list would reinforce an already-thick group, not close a real gap.

Instead, the domain's own `math_branches[]` field lists `calculus` as a genuine branch this domain
reaches (epidemiologists fit growth curves and reason about rates of change — "computes attack
rates... fits exponential growth to early case counts" per the domain's own `careers[]` entry).
Cross-checking `Calculus/Derivatives` and `Calculus/Applications Of Derivatives` against the live
spine found a cluster of skills sitting at genuine n=1/n=2 (thin-to-bare) that a real
epidemiological decision naturally forces: differentiating a fitted exponential case-count curve.

**Signature skills checked and ruled out (all already well covered, not chased):**
| id | n |
|---|---|
| statistics-and-probability-population | 11 |
| statistics-and-probability-sample-size | 9 |
| statistics-and-probability-conditional-probability | 5 |
| statistics-and-probability-how-to-determine-the-probability-of-conditional-events | 5 |
| advanced-numbers-how-to-find-a-whole-given-the-percent-and-the-part-of-the-whole | 4 |
| advanced-operations-how-to-evaluate-an-exponential-expression | 8 |
| statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data | 10 |
| measurement-ratio | 29 |

**Genuinely thin calculus cluster targeted instead (live spine read, 2026-09-18):**
| id | kind | n | covered_by |
|---|---|---|---|
| calculus-how-to-use-the-chain-rule-to-differentiate-a-composite-function | how-to | 1 | The Alert Curve |
| calculus-how-to-use-the-product-rule-to-differentiate-a-product-of-functions | how-to | 2 | The Alert Curve, The Setpoint Call |
| calculus-how-to-use-the-quotient-rule-to-differentiate-a-quotient-of-functions | how-to | 1 | The Marginal Call |
| calculus-how-to-find-the-equation-of-a-tangent-line-at-a-point | how-to | 2 | The Curve's Turn, The Sunset Ramp |
| calculus-local-maximum | term | 2 | The Curve's Turn, The Optimal Can |

(`calculus-tangent-line` and `calculus-differentiable` are separate ids already used by other
cases like `The Alert Curve` and are not claimed here — `calculus-how-to-find-the-equation-of-a-tangent-line-at-a-point`
is the distinct "how-to" id used below.)

| Concept | Score | Tier | Verdict |
|---|---|---|---|
| **C1 — The Surge Trigger** | **4.6** | T4 | **Chosen** |
| C2 — The Coverage Curve | 3.2 | T3 | Weaker: mostly reinforces already-thicker exponential/percent skills |
| C3 — The Cold-Chain Refit | 2.8 | T3 | Weaker: overlaps existing "Cold Chain" case's own territory |

**Recommendation.** Write **C1 — The Surge Trigger**. It forces a genuinely non-trivial,
5-skill thin cluster (4 how-to + 1 term, none above n=2) through real derivative work a vaccine-
allocation planner would actually do — differentiating a fitted case-count curve to decide when to
redeploy a scarce mobile unit — and the real, citable growth-rate research anchoring it (an actual
published early-outbreak doubling time) keeps the math grounded rather than invented. C2 and C3
were killed: C2 mostly re-exercises `advanced-operations-how-to-evaluate-an-exponential-expression`
(already n=8, not a real gap), and C3 risks stepping on the existing "Cold Chain" case's own
vaccine-logistics territory without adding a new skill.

---

### C1 — The Surge Trigger   ·   score 4.6   ·   tier T4

**Protagonist.** Dr. Renata Cho, county epidemiologist and vaccine/mobile-unit allocation planner
at a mid-size county health department. Personally at stake: she owns the call on when to redeploy
the department's one mobile vaccination-and-testing unit, and has to defend the timing math to her
director the same day.

**The dilemma.** A.) Redeploy the moment the *modeled true infection curve's* growth rate crosses
threshold (found by differentiating a fitted exponential model via the chain rule) OR B.) Redeploy
only once the *observed reported-case curve's* growth rate crosses threshold (found by
differentiating a reported-cases-times-capture-rate model via the product rule) — the only signal
actually visible in real time, since true infections are never directly observable.

**Primary metric.** Total expected cost of the trigger design (a flat verification-protocol cost
for acting on an unconfirmed modeled signal, vs. a late-detection cost sized by how much bigger
that day's case count has grown by the time the reported signal finally fires) — lower cost wins.

**Why it's close.** The true-curve trigger (A) fires earlier and is mathematically the "right"
signal, but relies on an assumption-laden back-calculation (an unconfirmed model) that the
department's own policy requires a costly verification protocol before acting on. The
reported-curve trigger (B) is the only signal directly observable in real time, but declining
testing capture during a surge (a real, documented operational pattern) makes it structurally lag
the true signal — and, because the reported curve has its own local maximum where the true curve
has none, a room that assumes "the reported curve is just the true curve, delayed" will miss that
the shapes genuinely diverge, not just shift in time.

**Would close (5 skills, 4 how-to / 1 term):**
| id | kind | label |
|---|---|---|
| calculus-how-to-use-the-chain-rule-to-differentiate-a-composite-function | how-to | How to use the chain rule to differentiate a composite function |
| calculus-how-to-use-the-product-rule-to-differentiate-a-product-of-functions | how-to | How to use the product rule to differentiate a product of functions |
| calculus-how-to-use-the-quotient-rule-to-differentiate-a-quotient-of-functions | how-to | How to use the quotient rule to differentiate a quotient of functions |
| calculus-how-to-find-the-equation-of-a-tangent-line-at-a-point | how-to | How to find the equation of a tangent line at a point |
| calculus-local-maximum | term | Local Maximum |

**Already-covered skills it also exercises.** `advanced-operations-how-to-evaluate-an-exponential-expression`
(evaluating the fitted exponential model at specific days), general algebraic equation-solving for
the trigger days.

**Data feasibility: HIGH.** Named sources I expect to exist and later confirmed live: a real,
peer-reviewed early-outbreak growth-rate/doubling-time figure (Li et al., NEJM 2020, independently
confirmed via CDC's *Emerging Infectious Diseases* journal); a real published outpatient-visit
economic-burden figure for a respiratory illness (industry-aggregated, informing the case's
per-case cost assumption); real published mobile-clinic operating-cost data (Mobile Health Map).
Sources I am NOT confident about: no source publishes any specific (fictional) county's own daily
case counts, testing-capture-rate curve, or internal trigger-threshold policy — these are stated
Modeling Assumptions by construction, the same pattern this corpus already uses for `Cold Chain`
and `The Approval Gate`.

**Sensitivity (SPEC §6).** NONE — ordinary workplace/operational pressure (a public-health
resource-allocation timing call), no illness/death/family-hardship framing forced onto a
specific person. Per SPEC §6, framed as *protection* (getting the mobile vaccination/testing
unit to the neighborhood that needs it) rather than *destruction*.

**Split risk.** NONE — 5 skills is within the honest single-case range (SPEC's own "no single case
should require the reader to track more than 15" per case-brainstorm's coverage-inflation guard).

---

### C2 — The Coverage Curve · score 3.2 · tier T3 (killed)

A vaccination-clinic staffing case comparing linear vs. percent-based dose-wastage models.
Would mostly reinforce `advanced-operations-how-to-evaluate-an-exponential-expression` (already
n=8) and `advanced-numbers-how-to-find-a-whole-given-the-percent-and-the-part-of-the-whole`
(already n=4) — not a real gap close. Killed in favor of C1.

### C3 — The Cold-Chain Refit · score 2.8 · tier T3 (killed)

A second cold-chain/vaccine-spoilage geometry case. Risks direct overlap with the existing `Cold
Chain` case's own territory (dose-wastage, cold-chain logistics) without reaching a genuinely new
skill cluster. Killed in favor of C1.
