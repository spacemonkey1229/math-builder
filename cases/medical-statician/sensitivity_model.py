#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Medical Statistician.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. This is that
model, for cases/medical-statician.

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):

    PARAMS                             dict[str, number]  every dial the case states
    FLEX                               list[str]          subset of PARAMS probe 5 flexes
    evaluate(params) -> dict           {"A": metric, "B": metric}
    evaluate_twist(params) -> dict     same shape, with the twist's own lens applied

IMPORTANT -- metric direction: this case's primary metric is a MARGIN OF ERROR
in percent (case.json.primary_metric), so LOWER is better here (like Family
Trip's cost-in-USD metric, unlike Cold Chain's in-spec-dose count where higher
is better). Callers comparing A vs B for "the winner" should take the SMALLER
value, not the larger one -- tier2_probes.py's own max()-based "winner" label
will therefore print the more EXPENSIVE/less-precise option as "winner"; that
label is a script convention, not a claim about which option is actually
better. See case.json.balance for the real-world-correct direction (B wins on
this metric; A's real advantage is regulatory, not numeric, see FACILITATOR.md).

evaluate() returns the case's graded PRIMARY metric: margin of error (%) at
95% confidence, at the maximum sample size each option can afford within the
shared $493,000 recruitment-and-dosing budget (case.json.balance.margin_basis).
This matches case.json.balance (A=3.53%, B=3.06%, margin (A-B)/B = 15.5%).

evaluate_twist() returns the same numeric metric, unchanged -- the Twist
(FACILITATOR.md: FDA CVM's GFI #266 real-world-data guidance) does not alter
either option's sample size, cost, or margin of error. It changes what the
margin-of-error numbers are WORTH to an FDA reviewer, not what they ARE. A
sensitivity model that moved the numbers on the twist would misrepresent what
actually happens in the room -- the Twist is a regulatory-interpretation
reveal, not a new figure. evaluate_twist exists here only to satisfy the
optional contract slot and to document that fact explicitly for probe 4.

Verified against case.md / case.json:
    evaluate({})        A = 3.53   B = 3.06   margin (A-B)/B = 15.5%   (MOE percent; B smaller/more precise)
    evaluate_twist({})  A = 3.53   B = 3.06   identical -- the twist does not move this metric
"""
import math

PARAMS = {
    # --- Appendix A: Bansky's fixed research budget, preserved from the legacy
    #     source. GIVEN scenario data, not an assumption -- not in FLEX. ------
    "total_budget_usd": 600000.0,
    "design_cost_usd": 23000.0,
    "analysis_cost_usd": 84000.0,
    # --- Appendix A: drug dosing cost, preserved from the legacy source. -----
    "dose_cost_per_week_usd": 15.0,
    "treatment_weeks": 26,
    # --- Appendix G, MA1/MA2: the case's own disclosed recruitment-cost
    #     assumptions, built on Appendix D's real cited benchmark range. ------
    "recruit_cost_a_usd": 250.0,
    "recruit_cost_b_usd": 90.0,
    # --- Appendix G, MA3: conservative default when no prior estimate exists.
    "proportion_p": 0.5,
    # --- Appendix E, S6: the standard z-score for 95% confidence. A real,
    #     cited mathematical constant, not an assumption -- not in FLEX. ------
    "z_score_95": 1.96,
}

# Only the genuine, case-author-chosen dials -- not the preserved legacy budget
# figures (given scenario data) and not the z-score (a cited mathematical
# constant). Halving a cited figure is a different case, not a sensitivity
# test; P6 (data decay) covers citation freshness instead.
FLEX = [
    "recruit_cost_a_usd",   # Appendix G, MA1
    "recruit_cost_b_usd",   # Appendix G, MA2
    "proportion_p",         # Appendix G, MA3
]


def _max_n(shared_budget, per_subject_recruit_cost, drug_cost):
    cost_per_subject = per_subject_recruit_cost + drug_cost
    if cost_per_subject <= 0:
        return 1
    n = math.floor(shared_budget / cost_per_subject)
    return max(n, 1)


def _moe_pct(z, p, n):
    p = min(max(p, 0.0), 1.0)
    return z * math.sqrt(p * (1 - p) / n) * 100.0


def evaluate(params=None):
    p = dict(PARAMS)
    p.update(params or {})
    shared_budget = p["total_budget_usd"] - p["design_cost_usd"] - p["analysis_cost_usd"]
    drug_cost = p["dose_cost_per_week_usd"] * p["treatment_weeks"]

    n_a = _max_n(shared_budget, p["recruit_cost_a_usd"], drug_cost)
    n_b = _max_n(shared_budget, p["recruit_cost_b_usd"], drug_cost)

    moe_a = _moe_pct(p["z_score_95"], p["proportion_p"], n_a)
    moe_b = _moe_pct(p["z_score_95"], p["proportion_p"], n_b)
    return {"A": moe_a, "B": moe_b}


def evaluate_twist(params=None):
    # The Twist (GFI #266 real-world-data reveal) is a regulatory-interpretation
    # reveal, not a new figure -- it does not change either option's affordable
    # sample size or margin of error. Returned unchanged, deliberately.
    return evaluate(params)


if __name__ == "__main__":
    base = evaluate({})
    tw = evaluate_twist({})
    print("base ", {k: round(v, 2) for k, v in base.items()},
          "margin %.1f%%" % (100 * (base["A"] - base["B"]) / base["B"]))
    print("twist", {k: round(v, 2) for k, v in tw.items()}, "(unchanged by design)")
