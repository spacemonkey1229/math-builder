#!/usr/bin/env python3
"""
Sensitivity model — Grant Reach.

Tier 2 probe 5 flexes each stated assumption by +/-50% and reports which flips
the verdict. Contract: PARAMS, evaluate(params) -> {"A": metric, "B": metric}.
See skills/case-readiness/scripts/example_sensitivity_model.py for the worked
reference this file follows.

Per case.json's balance.margin_basis, the graded metric is NOT the literal
primary_metric (dollars per renewal, degenerate for Order B at $0.00) -- it is
total on-time renewals achieved, which is well-defined for both orders. Higher
is better.

Population is split into three renewal-relevant regions (the "neither" region
never had aid to renew and drops out of both orders):
    pell_only  = pell_total - intersection
    state_only = state_total - intersection
    intersection = state_total * overlap_share (MA3)
Order A mails the full union (all three regions) at the WITH-reminder rate (MA5).
Order B mails only the intersection at MA5; pell_only/state_only get the
NO-reminder rate (MA4).

Verified against case.json.balance / FACILITATOR.md's arithmetic note:
    base  A = 2275.0  ·  B = 1987.9  ·  margin ~12.6%  (matches case.json margin_pct 12.6)
"""

PARAMS = {
    # --- Appendix A [S1]: national Pell recipient rate -- CITED, not an assumption, not in FLEX
    "pell_share": 0.324,
    # --- Modeling Assumption MA1: renewal population size
    "population": 9000.0,
    # --- Modeling Assumption MA2: share of population that is state-grant-eligible
    "state_share": 0.186,
    # --- Modeling Assumption MA3: share of state-eligible students also Pell-eligible
    "overlap_share": 0.80,
    # --- Modeling Assumption MA4: on-time renewal rate, no mailed reminder
    "rate_no_reminder": 0.55,
    # --- Modeling Assumption MA5: on-time renewal rate, with mailed reminder
    "rate_with_reminder": 0.70,
}

# pell_share [S1] is cited national data, not a chosen assumption -- P6 stress-tests
# it, not P5. MA1 (population) is included because it IS a stated Modeling
# Assumption, even though case.json's own MA1 row already predicts it will not
# move the margin (it scales every region proportionally). MA2-MA5 are all
# marked "Sensitive" in case.json.modeling_assumptions[] -- exactly the ones
# SPEC S2 asks P5 to flex.
FLEX = [
    "population",           # MA1
    "state_share",          # MA2
    "overlap_share",        # MA3
    "rate_no_reminder",     # MA4
    "rate_with_reminder",   # MA5
]


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})

    pell_total = p["pell_share"] * p["population"]
    state_total = p["state_share"] * p["population"]
    intersection = state_total * p["overlap_share"]
    pell_only = pell_total - intersection
    state_only = state_total - intersection
    union = pell_only + state_only + intersection

    metric_a = union * p["rate_with_reminder"]
    metric_b = (intersection * p["rate_with_reminder"]
                + (pell_only + state_only) * p["rate_no_reminder"])
    return {"A": metric_a, "B": metric_b}


if __name__ == '__main__':
    base = evaluate({})
    margin = 100 * (base["A"] - base["B"]) / base["B"] if base["B"] else float("nan")
    print("base ", {k: round(v, 4) for k, v in base.items()}, "margin %.2f%%" % margin)
