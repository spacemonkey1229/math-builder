# Case Study: The Qubit Budget

MS | Math | Case Study | 2026-27 | Frontier

---

## Overview

Sam Okafor has thirty seconds left on the shared screen before the budget committee moves to the next line item.

The slide behind her shows two boxes, side by side, and nothing else yet. One box is smaller. The other is bigger, and more expensive, and — if the client's own spec sheet is right — the only one that actually solves the client's problem instead of a piece of it. Sam's cursor hovers between them.

She's been the one signing off on register-size calls since she joined Latticeworks eight months ago, but this is the first one with a client contract attached to it, and the first one the CFO is sitting in on. Behind her, on a second monitor turned just far enough away that the room can't read it, sits the cost model she built last night — real vendor pricing, real hardware numbers, nothing made up, and an answer she's still not sure she believes.

Someone in the room clears their throat. The CFO taps her pen once against the table, waiting.

"Twenty qubits," Sam says, "or twenty-four. That's the ask."

She doesn't click either box yet.

---

## Background

Sam Okafor is a Quantum Software Engineer at Latticeworks, a small quantum-computing startup that runs client optimization workloads on rented cloud quantum hardware rather than owning any of its own. This week's client has handed Latticeworks a supply-chain routing problem: for each of 24 candidate warehouse-to-store delivery lanes, decide whether that lane should be active or idle, in a way that minimizes total cost — a standard combinatorial optimization problem with 24 independent binary decision variables (SEE APPENDIX A).

Representing that problem exactly on a quantum computer requires one qubit per decision variable, so the *exact* register size is 24 qubits, with a state space of 2²⁴ basis states — one for every possible combination of active/idle lanes. Latticeworks does not own quantum hardware; every run is billed by a cloud quantum-compute provider, per shot, on rented time (SEE APPENDIX B and APPENDIX C).

Sam has narrowed the register-size decision to two options. **The Near-Term Register** commits to 20 qubits — comfortably inside this quarter's cloud-compute budget, but its 2²⁰ state space can represent only 20 of the client's 24 decision variables at once; the remaining 4 lanes have to be handled by a classical fallback heuristic bolted onto the quantum result (SEE APPENDIX B). **The Full Register** commits to 24 qubits — its state space represents all 24 decision variables exactly, with no classical patchwork required (SEE APPENDIX C).

Every extra qubit does not cost the same amount, and it is not simply "more expensive, but still correct." Real published hardware benchmarks show that the more qubits a circuit uses, the more two-qubit gates a realistic problem-solving circuit on that hardware needs to touch every qubit — and every gate carries its own real, nonzero error rate. Errors compound multiplicatively across a circuit, so a shot's odds of finishing below the error threshold that makes its result trustworthy fall as register size grows (SEE APPENDIX D). Because Latticeworks pays per shot, not per successful shot, a shot that comes back above the error threshold is still billed — it just isn't useful. That is what makes the two options genuinely comparable on the same yardstick: not the price tag on the box, but the real cost of a shot Latticeworks can actually hand the client (SEE APPENDIX E). Every figure in this case is either directly cited to a real, published source or explicitly labeled a scenario assumption (SEE APPENDIX F for the full source list).

*Note: Latticeworks is a scenario construction for this case — there is no real company by this name. The client's 24-lane routing problem is likewise a constructed scenario. The cloud-provider pricing and hardware error-rate figures cited in the appendices are real, published, and independent of Latticeworks' fictional status. The full standards bridge for this case is in Appendix G.*

---

## Dilemma

You are Sam Okafor.

Do you:

**A.)** Commit to **the Near-Term Register** — 20 qubits, cheaper and inside this quarter's budget, but its 2²⁰ state space can't fully represent the client's 24-variable problem, forcing a classical-heuristic approximation on 4 of the lanes **OR**

**B.)** Commit to **the Full Register** — 24 qubits, whose 2²⁴ state space represents the client's problem exactly, but real published hardware error rates compound faster as circuit width grows, and cloud-quantum time is billed per shot regardless of whether that shot lands below the error threshold

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A state-space computation.** Evaluate 2²⁰ and 2²⁴ exactly, then compute the ratio 2²⁴ ÷ 2²⁰ as a single power of 2. Use that ratio to explain, in your own words, exactly what "16× larger state space" means and why it is the 24-qubit register — not the 20-qubit register — that can represent all 24 of the client's decision variables at once.
- **D2 — A circuit gate-count table.** Using Appendix D's gate-count model, compute the number of two-qubit gates a full problem-solving circuit needs at 20 qubits and at 24 qubits.
- **D3 — A below-threshold success-probability computation.** For each register size, evaluate the expression (1 − gate error rate)^(number of two-qubit gates), following order of operations: subtract inside the parentheses first, then apply the exponent. Show your work for both options.
- **D4 — A cost-per-successful-shot table and margin.** Using D3's success probabilities and Appendix E's per-shot price, compute dollars of cloud-quantum compute cost per successfully-completed shot for both options, and the percent margin between them.
- **D5 — A recommendation memo.** State which register size Sam should commit to, defended with D1's exact state-space comparison, D4's cost-per-successful-shot numbers and margin, and Appendix A's fact about what happens to the 4 uncovered lanes under Option A.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

## Appendix A: The Client's Routing Problem & Latticeworks' Constraints

| Quantity | Value |
|---|---|
| Number of independent binary decision variables in the client's routing problem (one per candidate delivery lane) | 24 [MA1] |
| Minimum qubits required to represent the full problem exactly (1 qubit per decision variable) | 24 [computed from MA1] |
| This quarter's cloud-quantum compute budget ceiling | Comfortably covers the 20-qubit option; does not comfortably cover the 24-qubit option at the shot volumes in Appendix E [MA2] |
| What happens to lanes not covered by the quantum register, under the Near-Term Register (Option A) | The uncovered 4 lanes are decided by a classical fallback heuristic run alongside the quantum result, not by the quantum circuit itself [MA3] |
| Days until Sam must submit a register-size recommendation to the budget committee | 2 days [MA4] |

*Note: Latticeworks and its client are scenario constructions for this case — see Background.*

---

## Appendix B: Option A — The Near-Term Register (20 Qubits)

| Spec | Value |
|---|---|
| Register size | 20 qubits |
| State space (basis states) | 2²⁰ = 1,048,576 [computed] |
| Coverage of the client's 24-variable problem | 20 of 24 decision variables represented exactly; 4 lanes handled by a classical heuristic (Appendix A) |
| Cloud provider / device | IonQ Forte, accessed via Amazon Braket [S1] |
| Per-shot price | $0.08 [S1] |
| Per-task price | $0.30 [S1] |

---

## Appendix C: Option B — The Full Register (24 Qubits)

| Spec | Value |
|---|---|
| Register size | 24 qubits |
| State space (basis states) | 2²⁴ = 16,777,216 [computed] — exactly 2²⁴ ÷ 2²⁰ = 2⁴ = **16×** the 20-qubit state space [computed] |
| Coverage of the client's 24-variable problem | All 24 decision variables represented exactly; no classical fallback needed |
| Cloud provider / device | IonQ Forte, accessed via Amazon Braket (same device and pricing as Option A) [S1] |
| Per-shot price | $0.08 [S1] |
| Per-task price | $0.30 [S1] |

---

## Appendix D: IonQ Forte — Published Hardware Error Data & Gate-Count Model

| Quantity | Value |
|---|---|
| Median measured two-qubit gate error rate, IonQ Forte (30-qubit trapped-ion system) | 46.4 × 10⁻⁴ = **0.464%** per two-qubit gate [S2] |
| Real published anchor: at circuit width ≈20 qubits, IonQ Forte sustains application-oriented circuits of up to ≈200 two-qubit gates before measured fidelity drops below the 1/e (≈36.8%) threshold that IonQ's own "Algorithmic Qubits" (#AQ) benchmark uses to define a passing circuit | ≈200 two-qubit gates at width ≈20 [S2] |
| Gate-count model used in this case, calibrated to the real anchor above (200 gates ÷ 20 qubits = 10 gates/qubit) | gates(N) = 10 × N two-qubit gates, for a register of N qubits [MA5, calibrated to S2] |
| Gate count at 20 qubits (Option A), from the model | 10 × 20 = **200** two-qubit gates — matches the real anchor exactly [S2] |
| Gate count at 24 qubits (Option B), from the model | 10 × 24 = **240** two-qubit gates [MA5] |

*Note on the gate-count model (MA5): IonQ's own #AQ benchmark methodology defines a passing reference circuit at width n as needing up to n² two-qubit gates (so 20² = 400, 24² = 576) — but that n² figure describes IonQ's own synthetic worst-case benchmark circuits, not necessarily a real application circuit. The same published paper's own real application-circuit examples show gate counts well below n² at comparable widths (SEE APPENDIX F, S2). This case therefore uses the simpler, directly-calibrated linear model above (10 gates/qubit, matched exactly to the paper's own stated real anchor at width ≈20) rather than the n² worst-case formula. See the Modeling Assumptions block for the sensitivity of the margin to this modeling choice — it is not small.*

---

## Appendix E: Cost Per Successfully-Completed Shot

| Step | Option A (20 qubits) | Option B (24 qubits) |
|---|---|---|
| Two-qubit gates in the circuit (Appendix D) | 200 | 240 |
| Below-threshold success probability: (1 − 0.00464)^(gates) | (1 − 0.00464)²⁰⁰ ≈ **0.3945** [computed] | (1 − 0.00464)²⁴⁰ ≈ **0.3275** [computed] |
| Per-shot price (Appendix B/C) | $0.08 [S1] | $0.08 [S1] |
| Dollars per successfully-completed shot = price ÷ success probability | $0.08 ÷ 0.3945 ≈ **$0.2028** | $0.08 ÷ 0.3275 ≈ **$0.2443** |
| Same, scaled to cost per 1,000 successful shots | ≈ **$202.79** | ≈ **$244.26** |

*D4 asks you to compute the percent margin between these two cost-per-successful-shot figures yourself — that comparison is not worked out here.*

---

## Appendix F: Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Amazon Braket per-shot and per-task pricing for the IonQ Forte QPU | $0.08/shot, $0.30/task | Amazon Web Services — [Amazon Braket Pricing](https://aws.amazon.com/braket/pricing/) | Accessed 2026-09-01 | HIGH |
| S2 | Median two-qubit gate error rate on IonQ Forte, and the real published circuit-width-vs-sustainable-gate-count anchor (≈200 two-qubit gates at width ≈20 before fidelity crosses the 1/e #AQ threshold; #AQ definition dc ≤ n²) | Median error 46.4×10⁻⁴ (0.464%); ≈200 two-qubit gates at width ≈20 | Chen, Nielsen, Ebert, Inlek, Wright, Chaplin, Maksymov, Páez, Poudel, Maunz, Gamble (IonQ) — ["Benchmarking a trapped-ion quantum computer with 30 qubits"](https://arxiv.org/abs/2308.05071), arXiv:2308.05071v2 | 2024-11-02 (v2) | HIGH |
| S3 | Contrasting cloud-quantum billing model: IBM Quantum bills by QPU time, not by shot | Pay-As-You-Go Plan: "Pay for the quantum computer access you use. Billed per second of usage. Starts at $96 USD / minute" | IBM — [IBM Quantum Computing: Products and services / pricing plans](https://www.ibm.com/quantum/products) | Accessed 2026-09-01 | HIGH |
| S4 | Real published two-qubit gate fidelity for a different superconducting-qubit cloud QPU family, used only as color confirming that gate error rates on real, currently-offered hardware vary by device family, not as a load-bearing figure in this case's own computation | Median two-qubit gate fidelity 99.1% (108-qubit device) | Amazon Web Services — [Amazon Braket launches Rigetti Cepheus-1-108Q superconducting device](https://aws.amazon.com/blogs/quantum-computing/amazon-braket-launches-rigetti-cepheus-1-108q-superconducting-device/) | Accessed 2026-09-01 | MEDIUM — real and directly fetched, but describes a different device family (Rigetti, not IonQ) than the one this case's own computation uses; included as background color, not as a computation input |

*Unit note: "1/e" in Appendix D/S2 refers to a fidelity of 1/e ≈ 0.368 (36.8%), the specific threshold IonQ's own Algorithmic Qubits (#AQ) benchmark uses to define whether a circuit of a given width and gate count "passes."*

---

## Modeling Assumptions

> These figures are either pure scenario flavor (the fictional Latticeworks' own budget and deadline) or a stated, disclosed modeling choice used to bridge from the one real published data point (S2's width-≈20, ≈200-gate anchor) to the 24-qubit case S2 does not directly measure. A Hero may challenge any of them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Number of independent binary decision variables in the client's routing problem | 24 | Scenario construction — chosen to match the case's 20-vs-24-qubit register comparison exactly. | Sets the frame (this is why 24 qubits is "exact"), but is not itself part of the margin arithmetic. |
| MA2 | Whether this quarter's budget comfortably covers each option | Covers A; does not comfortably cover B | Narrative framing matching the Overview and Dilemma — not a specific dollar figure, so not load-bearing on the margin computation. | None — flavor/framing only. |
| MA3 | What happens to the 4 lanes the 20-qubit register can't cover | Classical fallback heuristic | Standard real-world practice when a quantum register is smaller than a problem's variable count (hybrid quantum-classical decomposition) — not a specific sourced technique, stated as scenario detail. | Does not enter the margin arithmetic; it is the *qualitative* cost of Option A the numbers don't capture (see Balance argument). |
| MA4 | Days until Sam's recommendation is due | 2 days | Matches the Overview's "thirty seconds left on the shared screen" urgency framing. | None — flavor only. |
| MA5 | Gate-count model: gates(N) = 10 × N two-qubit gates | 200 gates at N=20 (exact match to S2's real anchor); 240 gates at N=24 (extrapolated) | Calibrated so the model exactly reproduces S2's own stated real anchor (≈200 two-qubit gates sustainable at width ≈20 before crossing the 1/e threshold), then extended linearly to N=24. | **HIGH — this is the single most margin-determining modeling choice in the case.** Using IonQ's own #AQ worst-case formula (gates = N²) instead of this calibrated linear model would put gates at 400 (N=20) and 576 (N=24) instead of 200 and 240 — same winner, but a substantially wider, much less close race. See D4 for your own computed margin under each model. |

---

### Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Exponent (also Power)
- Base

**"How to…" questions**

- How to evaluate an exponential expression
- How to evaluate an expression with multiple operations with exponents (Order Of Operations)

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
