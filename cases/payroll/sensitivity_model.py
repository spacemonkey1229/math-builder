#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- Payroll.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. This is that
model for cases/payroll.

CONTRACT -- exactly two-plus public names (per
skills/case-readiness/scripts/example_sensitivity_model.py):

    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            subset of PARAMS keys probe 5 perturbs
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     same shape, with the twist's own perturbation applied

For Payroll, "higher is better" on the primary metric (dollars removed from the
$20,000 shortfall) is deliberately near-identical for A and B by construction
(margin_pct = 0.0 -- see case.json.balance). The metric this model actually
exposes as a *tiebreaker* -- and the one the Twist changes -- is each option's
NET first-year dollar benefit once the twist's disclosed revenue-at-risk
assumption (MA3) is applied to whichever employee was let go under Option A.

Verified against cases/payroll/case.json and FACILITATOR.md:
    base (Option A = Tiago, no twist)   A = 20000.0  ·  B = 20000.0  ·  margin 0.0%
    base (Option A = Irene, no twist)   A = 20000.0  ·  B = 20000.0  ·  margin 0.0%
    twist (Option A = Irene)            A = 950.0    ·  B = 20000.0  ·  A well below B
    twist (Option A = Tiago)            A = 20000.0  ·  B = 20000.0  ·  unchanged (matches
                                         FACILITATOR.md: the twist only touches the Irene branch)
"""

PARAMS = {
    # --- Appendix C, H2-2019 projected pay, the five employees the Dilemma is about ---
    "martha_h2": 22500.0,
    "paul_h2": 21000.0,
    "christina_h2": 28000.0,
    "tiago_h2": 20000.0,
    "irene_h2": 20000.0,
    # --- Background: the target shortfall Francesca must close ---
    "shortfall_target": 20000.0,
    # --- Appendix B: 2019 H1 actual revenue, base for the Twist's revenue-at-risk figure ---
    "revenue_2019_h1": 127000.0,
    # --- Twist (FACILITATOR.md), disclosed scenario assumption MA3, not a cited real figure ---
    "twist_customer_revenue_share": 0.15,
    # --- which employee Option A lets go: "tiago" or "irene" are the two that close the
    #     $20,000 target exactly; any other name still runs but will show an over/under-shoot ---
    "option_a_employee": "irene",
}

# FLEX rescoped 2026-08-13: shortfall_target was previously flexed on the theory
# that "no external citation exists, so it's fair game" -- but that reasoning
# doesn't hold up: shortfall_target isn't an author-chosen assumption filling an
# ambiguity, it's Francesca's actual given business target (Background), a fixed
# fact of the scenario, not something the case is uncertain about. Worse,
# evaluate() DEFINES b_removed = target directly, so flexing target alone doesn't
# even model "what if the shortfall were different" honestly -- it just breaks
# the two options' shared anchor and produces a comparison artifact, not a real
# finding (confirmed: the "instability" it produced was solely this modeling
# artifact). twist_customer_revenue_share (MA3) stays -- it IS a genuine,
# explicitly-disclosed scenario assumption with no external source.
FLEX = [
    "twist_customer_revenue_share", # Twist, MA3
]

EMPLOYEES = ("martha", "paul", "christina", "tiago", "irene")


def _pool(params):
    """The five-employee remaining-payroll pool Option B's percent is computed over
    (Appendix C total, $111,500 at base values) -- Francesca is excluded per MA2."""
    return sum(params[f"{e}_h2"] for e in EMPLOYEES)


def evaluate(params):
    """Base case, no twist applied. Both options are constructed to close the
    stated shortfall_target exactly (Option A via whichever single employee's H2
    pay is chosen; Option B via the flat percent of the pool). Returns dollars
    removed from the target for each option -- by design, equal at base values
    unless option_a_employee's own H2 pay differs from shortfall_target."""
    target = params["shortfall_target"]
    emp = params["option_a_employee"]
    a_removed = params[f"{emp}_h2"]
    # Option B is defined to hit the target exactly (that's what "the flat percent
    # that removes exactly $target" means) -- it is a design constraint of the case,
    # not something that can miss, so it always returns target itself.
    b_removed = target
    return {"A": round(a_removed, 2), "B": round(b_removed, 2)}


def evaluate_twist(params):
    """Twist applied: if Option A's chosen employee is Irene, her remaining H2 pay
    saved is offset by the disclosed revenue-at-risk figure (MA3). Every other
    choice of employee (including Tiago) is untouched by the twist, matching
    FACILITATOR.md's 'nothing about Tiago's situation is touched by this twist.'
    Option B is never affected by the twist -- it never singles out an employee."""
    base = evaluate(params)
    emp = params["option_a_employee"]
    if emp == "irene":
        revenue_at_risk = params["revenue_2019_h1"] * params["twist_customer_revenue_share"]
        base["A"] = round(base["A"] - revenue_at_risk, 2)
    return base


if __name__ == "__main__":
    print("base, Option A = irene:", evaluate(PARAMS))
    twisted = dict(PARAMS)
    print("twist, Option A = irene:", evaluate_twist(twisted))
    tiago_params = dict(PARAMS, option_a_employee="tiago")
    print("base, Option A = tiago:", evaluate(tiago_params))
    print("twist, Option A = tiago:", evaluate_twist(tiago_params))
    print("five-employee pool ($111,500 expected):", _pool(PARAMS))
