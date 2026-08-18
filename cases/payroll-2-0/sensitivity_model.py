#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- Payroll 2.0.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. This is that
model for cases/payroll-2-0.

CONTRACT -- exactly the four public names (per
skills/case-readiness/scripts/example_sensitivity_model.py):

    PARAMS                     dict[str, number/str]   every dial the case states
    FLEX                       list[str]                subset of PARAMS keys probe 5 perturbs
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     same shape, with the twist's own perturbation applied

Primary metric: dollars removed from the $25,000 remaining-2019-payroll shortfall
target (case.json.primary_metric). Higher is better -- both options are meant to
close the gap; whichever removes more of it "wins" on this narrow metric (the
case's real tension is who bears the $25,000+, per FACILITATOR.md, not which
option removes more dollars).

Verified against cases/payroll-2-0/case.json and FACILITATOR.md:
    base (Option A = Christina, no twist)    A = 26450.0  ·  B = 25000.0  ·  margin 5.8%
    twist (Option A = Christina)             A = 20710.0  ·  B = 25000.0  ·  A now well below B
    base (Option A = any other employee)     A < 25000.0 (undershoots) regardless of twist --
                                              the twist is scoped to the Christina branch only,
                                              matching FACILITATOR.md ("untouched by this twist").
"""

PARAMS = {
    # --- Appendix C, H2-2019 projected pay, the five employees the Dilemma is about ---
    "martha_h2": 23400.0,
    "paul_h2": 20500.0,
    "christina_h2": 26450.0,
    "tiago_h2": 18500.0,
    "irene_h2": 23400.0,
    # --- Background: the target shortfall Francesca must close ---
    "shortfall_target": 25000.0,
    # --- Appendix B: 2017/2018 revenue, base for the Twist's at-risk-growth figure ---
    "revenue_2017": 261000.0,
    "revenue_2018": 275000.0,
    # --- Twist (FACILITATOR.md), disclosed scenario assumption: Christina's stated 41% share
    #     of 2018 NEW SALES (Appendix A) is assumed representative of her share of 2017->2018
    #     REVENUE GROWTH specifically -- the case never states this identity, it is the
    #     author's own modeling choice under missing data (no per-salesperson growth
    #     breakdown exists), so this is the one genuine FLEX dial in this model. ---
    "christina_growth_attribution_pct": 0.41,
    # --- which employee Option A lets go: "christina" is the only one whose remaining pay
    #     alone closes the $25,000 target; any other name still runs but will show an
    #     undershoot, matching FACILITATOR.md's Trap ---
    "option_a_employee": "christina",
}

# Only the Twist's attribution assumption is a genuine author-chosen dial (a real estimate
# filling a real gap in the given data -- no per-salesperson breakdown of REVENUE GROWTH
# exists anywhere in the source, only the 2018 new-sales split). Every dollar figure in
# PARAMS above it (employee pay, revenue, shortfall_target) is the case's own given/cited
# data (Appendix B/C, carried forward from the legacy source workbook, see
# case.json.legacy_conversion_note) -- not swept by probe 5 by default, per
# skills/case-readiness/SKILL.md ("Only FLEX[] is swept... Cited data is stress-tested by
# P6 instead").
FLEX = [
    "christina_growth_attribution_pct",  # Twist assumption
]

EMPLOYEES = ("martha", "paul", "christina", "tiago", "irene")


def _pool(params):
    """The five-employee remaining-payroll pool Option B's percent is computed over
    (Appendix C total, $112,250 at base values) -- Francesca is excluded per
    case.json.modeling_assumptions MA2."""
    return sum(params[f"{e}_h2"] for e in EMPLOYEES)


def evaluate(params):
    """Base case, no twist applied. Option A removes whichever employee's own H2 pay is
    chosen (option_a_employee); Option B is defined to hit shortfall_target exactly (the
    flat percent cut that removes exactly $25,000, by construction of what "Even Keel"
    means). Returns dollars removed from the target for each option."""
    target = params["shortfall_target"]
    emp = params["option_a_employee"]
    a_removed = params[f"{emp}_h2"]
    b_removed = target
    return {"A": round(a_removed, 2), "B": round(b_removed, 2)}


def evaluate_twist(params):
    """Twist applied: if Option A's chosen employee is Christina, her remaining H2 pay
    saved is offset by the disclosed at-risk-growth figure (her stated 41% new-sales share,
    assumed representative of her share of 2017->2018 revenue growth). Every other choice of
    employee is untouched by the twist, matching FACILITATOR.md ('untouched by this twist')."""
    base = evaluate(params)
    emp = params["option_a_employee"]
    if emp == "christina":
        growth = params["revenue_2018"] - params["revenue_2017"]
        at_risk = growth * params["christina_growth_attribution_pct"]
        base["A"] = round(base["A"] - at_risk, 2)
    return base


if __name__ == "__main__":
    print("base, Option A = christina:", evaluate(PARAMS))
    print("twist, Option A = christina:", evaluate_twist(dict(PARAMS)))
    martha_params = dict(PARAMS, option_a_employee="martha")
    print("base, Option A = martha:", evaluate(martha_params))
    print("twist, Option A = martha (should be unaffected):", evaluate_twist(martha_params))
    print("five-employee pool ($112,250 expected):", _pool(PARAMS))
    print("pct cut needed for B ($25,000 / pool):", round(100 * PARAMS["shortfall_target"] / _pool(PARAMS), 4))
