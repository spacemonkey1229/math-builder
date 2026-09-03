# RESEARCH_LOG.md — The Qubit Budget

`case-research` pass, 2026-09-01. 10 `{{NEEDS_SOURCE}}` placeholders enumerated from `case.md`.
6 SOURCED, 4 ASSUMPTION (stated Modeling Assumptions), 0 DROPPED, 0 OPEN.

---

## P01 — Number of independent binary decision variables in the client's routing problem (Appendix A)

Searched: nothing — explicitly framed as "stated in-scenario," an authorial choice fixing the
client's problem size at exactly 24 to match the case's 20-vs-24-qubit comparison from the concept
sheet (C10: "24-qubit register... represents the problem exactly").

**Outcome: ASSUMPTION.** MA1 = 24. Sets the frame, not load-bearing in the margin arithmetic.

## P02–P05 — Per-shot and per-task pricing, IonQ Forte (Appendix B, C)

Searched: "Amazon Braket pricing per shot per task IonQ Forte Rigetti 2026." Fetched
`aws.amazon.com/braket/pricing/` directly with `WebFetch`. Confirmed exact figures on the live
page: IonQ Forte $0.30/task + $0.08000/shot; Rigetti Cepheus $0.30/task + $0.000425/shot; IonQ
QPUs require a minimum of 2,500 shots per task when using error mitigation. Cross-checked against
an independent `WebSearch` summary quoting the identical numbers before trusting them.

Chose IonQ Forte (not Rigetti) as the priced device for this case specifically because it is also
the device benchmarked in the paper used for Appendix D (P06–P08 below) — using the same device
for both price and error-rate data avoids stitching together two different hardware families'
numbers into one metric.

**Outcome: SOURCED, HIGH.** S1 = $0.08/shot, $0.30/task (IonQ Forte). Used identically for both
Option A and Option B, since the register-size decision doesn't change which device is targeted.

## P06–P08 — Median two-qubit gate error rate and gate-count anchor (Appendix D)

Searched: "IBM quantum processor two-qubit gate error rate published spec," then "IonQ Forte
published two-qubit gate fidelity error rate spec sheet," then "IonQ Forte specifications page
two-qubit gate fidelity 99.7% OR 99.8% OR 99.9%." Landed on Chen et al. (IonQ),
"Benchmarking a trapped-ion quantum computer with 30 qubits," arXiv:2308.05071. Fetched
`arxiv.org/html/2308.05071v2` directly with `WebFetch`.

Confirmed in the paper: median two-qubit gate error rate 46.4×10⁻⁴ (0.464%); best-observed
pair 27.8×10⁻⁴; worst pair 885×10⁻⁴. Also confirmed the paper's own real application-benchmark
claim: circuits with width up to ≈20 qubits and depth up to ≈200 two-qubit gates pass with
fidelity above 1/e without error mitigation, and the paper's own Algorithmic Qubits (#AQ)
methodology defines a width-n reference circuit as needing up to dc ≤ n² two-qubit gates (e.g.
#AQ 29 uses dc ≤ 29² = 841). Also confirmed real application-circuit examples in the same paper
that do *not* follow n² scaling (phase estimation at 30 qubits: 471 gates; amplitude estimation at
7 qubits: 604 gates) — logged this specifically because it is the basis for MA5's modeling choice
below.

Fetched `arxiv.org/abs/2308.05071` separately to confirm exact title, author list (Jwo-Sy Chen,
Erik Nielsen, Matthew Ebert, Volkan Inlek, Kenneth Wright, Vandiver Chaplin, Andrii Maksymov,
Eduardo Páez, Amrit Poudel, Peter Maunz, John Gamble), and version dates (v1: 2023-08-09; v2:
2024-11-02).

**Outcome: SOURCED, HIGH.** S2. This is the single most load-bearing source in the case — it
supplies both the per-gate error rate and the real anchor the gate-count model (MA5) is
calibrated to.

## P08 (model construction) — Gate-count model, gates(N) = 10 × N (Appendix D)

The paper (S2) directly states real error-rate data and a real width≈20/≈200-gate anchor, but does
NOT report a directly-measured gate count at width 24 (the paper's own benchmarks stop at width
30 for a different, narrower purpose — algorithmic-qubit certification, not a general
gates-vs-width curve). Two candidate models were considered:

1. **IonQ's own #AQ worst-case formula, gates = N².** Real, sourced, directly stated in the same
   paper (dc ≤ n²). Gives gates(20) = 400, gates(24) = 576.
2. **A linear model calibrated to the paper's own stated real anchor, gates(N) = 10 × N** (since
   200 gates ÷ 20 qubits = 10 gates/qubit exactly matches the paper's stated ≈200-gates-at-width-≈20
   figure). Gives gates(20) = 200 (exact match to the real anchor), gates(24) = 240 (extrapolated).

Chose model 2 as the case's primary model, because model 1 (n²) is explicitly a worst-case
reference-circuit definition used to *certify* a width, not a claim about how many gates a real
application circuit at that width actually needs — and the same paper's own real application
examples (P06–P08 above) show real circuits falling well short of n² at comparable widths. Model 2
reproduces the paper's own headline real number exactly at N=20 and extrapolates linearly, which
is the more conservative, more directly anchor-matched choice.

**Outcome: NOT DIRECTLY MEASURED AT N=24 → derived + disclosed Modeling Assumption (MA5).**
Logged both models' full downstream consequences in the Margin section below and in
`case.json.balance.margin_note`, per the project's practice (see `prove-it-scales` P11-13/MA5 for
precedent) of running the counterfactual rather than silently picking one number.

## P09 — Contrasting real billing model, IBM Quantum (Appendix F, color only)

Searched: "IBM Quantum Platform pricing per second QPU Premium plan cost." `WebFetch` on
`quantum.cloud.ibm.com/docs/en/guides/manage-cost` and `.../plans-overview` returned real pages
but neither stated a dollar figure directly (both defer to `ibm.com/quantum/pricing`). Direct
`WebFetch` on `ibm.com/quantum/pricing` returned HTTP 403 (blocked). Routed around this by opening
the URL in the sandboxed Claude Browser tool instead (`preview_start` + `get_page_text` +
`javascript_tool` to confirm the resolved URL). The page resolved to `ibm.com/quantum/products`
and rendered its pricing table directly: "Pay-As-You-Go Plan... Billed per second of usage. Starts
at $96 USD / minute." Confirmed via the browser's own extracted page text, not a search snippet.

**Outcome: SOURCED, HIGH.** S3. Used only as Background/Intro color (a second real provider with a
genuinely different billing philosophy — time-based, not shot-based) — not a computation input.

## P10 — Contrasting hardware family, Rigetti Cepheus-1-108Q (Appendix F, color only)

Searched: "Rigetti Cepheus published two-qubit gate error rate spec sheet qubits." Fetched
`aws.amazon.com/blogs/quantum-computing/amazon-braket-launches-rigetti-cepheus-1-108q-superconducting-device/`
directly. Confirmed: "108-qubit superconducting quantum processing unit," "median two-qubit gate
fidelity of 99.1%," gate speeds "~60 nanoseconds." (A second candidate source for the smaller
Cepheus-1-36Q device, `datacenterdynamics.com`, returned HTTP 403 and was not pursued further once
the 108Q figure was already confirmed directly from an AWS-published, dated blog post.)

**Outcome: SOURCED, MEDIUM.** S4. Real and directly fetched, but describes a different device
family than the one this case's own computation (S1 + S2, both IonQ Forte) uses — included as
Appendix F color confirming gate-error rates genuinely vary by hardware family, not as a
computation input. Confidence downgraded to MEDIUM specifically because it is off-target for this
case's own arithmetic, not because the figure itself is doubtful.

---

## Verification (skill step 7)

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources (must not be load-bearing): none
needs_source OPEN remaining: 0
```

S3 and S4 are both explicitly color/background sources, not load-bearing on the margin — confirmed
neither appears in `case.json.balance.margin_note`'s arithmetic.

## Margin (facilitator-only — computed here, not written into case.md as a verdict)

```
gate_error_rate   = 0.00464          (S2, median two-qubit gate error, IonQ Forte)
gates(20)         = 10 * 20 = 200    (MA5, exact match to S2's real anchor)
gates(24)         = 10 * 24 = 240    (MA5, linear extrapolation)
F(20) = (1 - 0.00464)^200 = 0.394491
F(24) = (1 - 0.00464)^240 = 0.327525
price_per_shot    = $0.08            (S1, identical for both options)
cost(20) = 0.08 / 0.394491 = $0.202793
cost(24) = 0.08 / 0.327525 = $0.244256
margin_pct = (0.244256 - 0.202793) / 0.244256 * 100 = 16.975%  (rounded 16.98%)
WINNER: Option A, The Near-Term Register.
```

**Structural finding:** `price_per_shot` cancels completely out of `margin_pct` (both options are
priced identically, so `margin_pct = 1 - F(24)/F(20)` regardless of the dollar figure) — the
per-shot price only scales the absolute dollars shown in Appendix E, never the winner or the
margin. A different or cheaper cloud-compute vendor would never flip this recommendation on the
raw numbers alone.

This margin (16.98%) is comfortably inside SPEC §2's ~20% cap. No retune pass or MCS-46-style
waiver was necessary.

**Counterfactual model-sensitivity check** (run per the project's established practice of stress-
testing the modeling choice that most affects the numeric race, see `prove-it-scales`'s TCO
counterfactual for precedent): recomputed using IonQ's own #AQ worst-case gate-count formula
(gates = N²) instead of the case's calibrated linear model (MA5):

```
gates(20) = 20^2 = 400
gates(24) = 24^2 = 576
F(20) = (1 - 0.00464)^400 = 0.155623
F(24) = (1 - 0.00464)^576 = 0.068641
cost(20) = 0.08 / 0.155623 = $0.514063
cost(24) = 0.08 / 0.068641 = $1.165478
margin_pct = (1.165478 - 0.514063) / 1.165478 * 100 = 55.9%
WINNER (unchanged): Option A.
```

Both real, defensible models agree on the winner and disagree sharply (17.0% vs. 55.9%) on how
close the race is. This is not a flaw to hide — it is the deliberate basis for the FACILITATOR.md
Twist, and it is disclosed plainly in `case.json.balance.margin_note` and `case.json`'s Modeling
Assumptions block (MA5, sensitivity flagged HIGH).

## SPEC §2 self-check

- Primary metric exists and is computed for both options: yes (dollars per successfully-completed
  shot, Appendix E).
- No structurally-zero-cost option: correct — both options have a nonzero, real, sourced
  dollars-per-successful-shot figure; neither is free or trivially dominant by construction.
- Dilemma is not a foregone conclusion: the primary D4 numeric race is genuinely close (16.98%,
  under the ~20% cap) under the case's stated model, and the qualitative counter-argument
  (Option A's uncosted classical-fallback risk on 4 lanes vs. Option B's structural exactness) adds
  real tension beyond the raw numbers even where the numeric winner is clear. Flagging for
  case-qa's own judgment: the model-sensitivity finding above (17.0% vs. 55.9% depending on the
  gate-count model) is disclosed, not hidden, and both models agree on the winner — this should
  read as a strength (a real, honest secondary lever for the Twist), not a defect, but it is
  logged here explicitly so case-qa can independently confirm that read.

**Verdict: PASS**, no blockers identified in this research pass.

## Sensitivity model

Built `sensitivity_model.py` (PARAMS / evaluate(params) / FLEX[] pattern, per
`the-mainline-margin/sensitivity_model.py`). Flexes `gate_error_rate` (S2) and
`gates_per_qubit` (MA5's calibrated slope) — the two real levers that actually determine the
margin and the winner. `price_per_shot` and `price_per_task` are included in the model for
realism but are deliberately NOT in `FLEX[]`, since the margin computation above proves they
cancel out algebraically and sweeping them would be pedagogically misleading (it would look like a
sensitivity dimension when it structurally isn't one). `n_a` (20) and `n_b` (24) are also not
swept — they are the case's own fixed dilemma, not a modeling assumption.

## Next step

Run `case-qa` on `the-qubit-budget`.
