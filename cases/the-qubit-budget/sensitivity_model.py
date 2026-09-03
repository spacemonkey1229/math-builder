#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Qubit Budget.

Tier 2 probe 5 ("flex each stated assumption by +-50%; report which flips
the verdict") needs a runnable model of the case's own arithmetic.

CONTRACT — two public names:

    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

The case's SPEC Section 2 primary metric (case.json.balance.margin_basis) is
dollars of cloud-quantum compute cost per successfully-completed (below-
error-threshold) shot, for a 20-qubit register (A) vs. a 24-qubit register
(B) solving the same client routing problem on the same priced device
(IonQ Forte via Amazon Braket).

Dollars-per-successful-shot is a COST -- lower is better -- but the probe's
contract is "higher is better", so evaluate() returns the NEGATIVE of the
cost.

Mechanism modeled explicitly (this is the whole point of the case):
  1. A register of N qubits needs gates(N) two-qubit gates to run the
     client's problem-solving circuit (Appendix D's calibrated model,
     gates(N) = gates_per_qubit * N, MA5).
  2. Each two-qubit gate has a real, published error rate (S2). Errors
     compound multiplicatively across the circuit: below-threshold success
     probability F(N) = (1 - gate_error_rate) ** gates(N).
  3. Latticeworks pays a fixed per-shot price regardless of whether the
     shot lands below threshold, so dollars per SUCCESSFUL shot is
     price_per_shot / F(N).

STRUCTURAL FINDING (see RESEARCH_LOG.md "Margin" section): price_per_shot
and price_per_task are IDENTICAL for both options in this case, so they
cancel completely out of the margin and the winner. They are kept in
PARAMS/evaluate() for realism (so evaluate_detail() reports real dollar
figures), but they are deliberately NOT included in FLEX[] -- sweeping them
would misleadingly suggest they're a sensitivity dimension when they
provably aren't. FLEX[] instead sweeps the two parameters that actually
determine the margin and the winner: gate_error_rate (S2) and
gates_per_qubit (MA5's calibrated slope, the single most margin-determining
modeling choice in the case -- see the n^2 counterfactual in
RESEARCH_LOG.md, which corresponds to gates_per_qubit effectively varying
with N rather than being constant; this linear model is the case's stated
approximation of that real alternative).

Register sizes (n_a=20, n_b=24) are the case's own fixed dilemma, not a
modeling assumption -- not swept.
"""

PARAMS = {
    # --- Appendix B / C: register sizes (the case's own fixed dilemma) -----
    "n_a": 20.0,
    "n_b": 24.0,
    # --- Appendix D / S2: real median two-qubit gate error rate, IonQ Forte
    "gate_error_rate": 0.00464,
    # --- Appendix D / MA5: calibrated gate-count model slope (gates/qubit) -
    "gates_per_qubit": 10.0,
    # --- Appendix B / C / S1: Amazon Braket pricing, IonQ Forte -------------
    "price_per_shot": 0.08,
    "price_per_task": 0.30,
    "shots_per_task": 2500.0,  # S1: IonQ's own stated minimum shots/task with error mitigation
}

# Probe 5 flexes THESE and only these: the two real levers that actually
# move margin_pct and can flip the winner. price_per_shot/price_per_task are
# deliberately excluded -- see module docstring; they cancel out completely.
FLEX = [
    "gate_error_rate",   # S2 -- the case's real fulcrum
    "gates_per_qubit",   # MA5 -- the single most margin-determining modeling choice
]


def _success_probability(n_qubits, p):
    gates = p["gates_per_qubit"] * n_qubits
    return (1.0 - p["gate_error_rate"]) ** gates


def _cost_per_successful_shot(n_qubits, p):
    f = _success_probability(n_qubits, p)
    effective_price = p["price_per_shot"] + (p["price_per_task"] / p["shots_per_task"])
    return {
        "gates": p["gates_per_qubit"] * n_qubits,
        "success_probability": f,
        "cost_per_successful_shot": effective_price / f,
    }


def evaluate_detail(params):
    p = dict(PARAMS)
    p.update(params or {})
    a = _cost_per_successful_shot(p["n_a"], p)
    b = _cost_per_successful_shot(p["n_b"], p)
    # Lower cost/successful-shot is better; evaluate()'s contract is "higher
    # is better", so return the negated cost.
    return {"A": -a["cost_per_successful_shot"], "B": -b["cost_per_successful_shot"]}, a, b


def evaluate(params):
    """Tier 2 probe 5 contract: evaluate(params) -> {'A': metric, 'B': metric}
    ONLY -- no extra return values, since the probe's own max()/min() over
    the return value would otherwise break on a 3-tuple. Full diagnostics
    (per-option breakdown) are in evaluate_detail()."""
    r, _a, _b = evaluate_detail(params)
    return r


if __name__ == '__main__':
    base, a, b = evaluate_detail({})
    win = max(base, key=base.get)  # higher (less negative) evaluate() value wins
    lo = min(base, key=base.get)
    win_cost, lo_cost = -base[win], -base[lo]  # back to actual USD/successful-shot cost
    margin = 100.0 * (lo_cost - win_cost) / lo_cost  # % the loser costs MORE than the winner
    print("Option A (20-qubit Near-Term Register):")
    for k, v in a.items():
        print(f"  {k}: {v}")
    print("Option B (24-qubit Full Register):")
    for k, v in b.items():
        print(f"  {k}: {v}")
    print()
    print("cost/successful shot  A=%.6f  B=%.6f" % (-base["A"], -base["B"]))
    print("winner:", win, " margin: %.2f%%" % margin)

    # Counterfactual named in the Twist / RESEARCH_LOG.md: IonQ's own #AQ
    # worst-case gate-count formula, gates = N^2, instead of the calibrated
    # linear model. Approximated here by setting gates_per_qubit = N (so
    # gates_per_qubit * N = N^2) separately for each option, since this
    # model's FLEX contract assumes one shared slope -- reported as a
    # one-off diagnostic, not a FLEX sweep point.
    import math
    n_a, n_b = PARAMS["n_a"], PARAMS["n_b"]
    e = PARAMS["gate_error_rate"]
    f_a2 = (1 - e) ** (n_a ** 2)
    f_b2 = (1 - e) ** (n_b ** 2)
    price = PARAMS["price_per_shot"]
    cost_a2 = price / f_a2
    cost_b2 = price / f_b2
    margin2 = 100.0 * (cost_b2 - cost_a2) / cost_b2
    print()
    print("Counterfactual (n^2 gate-count model, IonQ's own #AQ formula):")
    print("  cost/successful shot  A=%.6f  B=%.6f  margin=%.2f%%" % (cost_a2, cost_b2, margin2))
