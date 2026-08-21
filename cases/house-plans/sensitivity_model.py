#!/usr/bin/env python3
"""
SENSITIVITY MODEL — House Plans.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py (Cold Chain) for the
worked reference and the exact contract.

CONTRACT — exactly two public names used by the probe, plus a third (evaluate_twist)
because this case ships a twist:

    PARAMS                          dict[str, number]   every dial the case states
    FLEX                            list[str]            the subset that is a genuine
                                                           author-chosen ASSUMPTION
    evaluate(params) -> dict         {"A": metric, "B": metric}  higher is better
    evaluate_twist(params) -> dict   same shape, with the twist applied

Metric: primary_metric per case.json is "total project cost as a percentage of the
true $550,000 spending ceiling, at each floor plan's most upgraded affordable tier
with an optimized amenity package." Higher is better (fuller use of the family's
approved budget), capped implicitly at 100 by construction (the optimizer never
selects a build+amenity combination that exceeds the ceiling).

FLEX SCOPING — this case has almost no discretionary modeling dials, unlike Cold
Chain. Appendix C's "Modeling Assumptions" (MA1: loan is 90% of total cost; MA2:
build+amenities share one ceiling) and Appendix D's tier prices / amenity costs /
Appendix A-B's square footages are all GIVEN scenario data for this fictional
family -- fixed facts of the word problem, not a convention the author had to
invent (contrast Cold Chain's "which villages get priority" allocation policy,
which the case never states and had to be modeled). Flexing the 90%-loan
condition or a price table is "a different case," per the Cold Chain doc's own
"halving a WHO-rated cold life is a different case" rule -- not a sensitivity
test of THIS case's assumptions.

The one genuine author-chosen scenario dial is the TWIST's lumber-cost increase
(FACILITATOR.md: "Lumber prices have jumped 6%") -- a number the case invented to
construct the twist scenario, exactly analogous to Cold Chain's twist_detour_h
(also FLEX-only-for-the-twist). That is the only entry in FLEX.

Verified against cases/house-plans/case.md, case.json.derived and FACILITATOR.md:
    base   A(Farmhouse/Luxury) = 549835.84 (99.9702% of $550,000)
           B(Ranch/Standard)   = 549212.80 (99.8569% of $550,000)
           margin (pct-of-ceiling points) = 0.1133 -> matches case.json margin_pct 0.11
    twist  build costs rise by 6%: Farmhouse Luxury -> 458593.99 (+25958.15... case
           rounds to 25958.15), Ranch Standard -> 482080.37 (+27287.57) -- matches
           case.json.derived twist_* fields; neither tier flips (both still fit
           under $550,000), so the twist visibly shrinks amenity budgets only.
"""
from itertools import combinations

PARAMS = {
    # --- Appendix A / B, given architectural area tabulations ---------------
    "farmhouse_sqft": 2912.0,
    "ranch_sqft": 4494.0,
    # --- Appendix D, price per heated sq ft by tier --------------------------
    "tier_standard": 101.20,
    "tier_plus": 122.63,
    "tier_luxury": 148.57,
    # --- Appendix C, Assumption 1: loan is 90% of total project cost --------
    "loan_amount": 495000.0,
    "loan_pct_of_total": 0.90,
    # --- Appendix D, amenity costs -------------------------------------------
    "amenity_pool": 35000.0,
    "amenity_home_theater": 14530.0,
    "amenity_landscaping": 17250.0,
    "amenity_detached_shop": 23265.0,
    "amenity_putting_green": 17465.0,
    "amenity_sport_court": 32890.0,
    "amenity_custom_gate": 16125.0,
    "amenity_outdoor_kitchen": 8580.0,
    # --- the Twist (FACILITATOR.md): lumber cost increase, as a percent -----
    "twist_lumber_increase_pct": 6.0,
}

# Probe 5 flexes THESE and only these. Everything else in PARAMS is given
# scenario data (a fixed price table, a fixed loan condition, given square
# footage) -- flexing it produces a different case, not a sensitivity test of
# this case's own assumptions. The twist's lumber-increase percent is the one
# number the case invented to construct its own twist scenario.
FLEX = [
    "twist_lumber_increase_pct",   # FACILITATOR.md twist, "lumber prices jumped 6%"
]

AMENITY_KEYS = [
    "amenity_pool",
    "amenity_home_theater",
    "amenity_landscaping",
    "amenity_detached_shop",
    "amenity_putting_green",
    "amenity_sport_court",
    "amenity_custom_gate",
    "amenity_outdoor_kitchen",
]


def _true_ceiling(p):
    # D2: the loan is loan_pct_of_total of the total project cost -> find the whole.
    return p["loan_amount"] / p["loan_pct_of_total"]


def _best_tier_cost(p, sqft, lumber_mult):
    """The most upgraded tier (Luxury > Plus > Standard) whose build cost alone
    fits under the true ceiling, after the twist's lumber multiplier."""
    ceiling = _true_ceiling(p)
    for tier in ("tier_luxury", "tier_plus", "tier_standard"):
        cost = sqft * p[tier] * lumber_mult
        if cost <= ceiling:
            return tier, cost
    # No tier fits (shouldn't happen for either house at stated params).
    return "tier_standard", sqft * p["tier_standard"] * lumber_mult


def _best_amenity_package(p, budget):
    """0/1 knapsack over the 8 amenities: maximise spend without exceeding the
    remaining budget. Small fixed item count (8) -> brute force all subsets,
    exact and unambiguous (matches case.json.derived exactly at base params)."""
    items = [(k, p[k]) for k in AMENITY_KEYS]
    best_total, best_set = 0.0, []
    n = len(items)
    for mask in range(1 << n):
        total = 0.0
        chosen = []
        for i in range(n):
            if mask & (1 << i):
                total += items[i][1]
                chosen.append(items[i][0])
        if total <= budget and total > best_total:
            best_total, best_set = total, chosen
    return best_total, best_set


def _pct_of_ceiling(p, sqft, lumber_mult=1.0):
    ceiling = _true_ceiling(p)
    tier, build_cost = _best_tier_cost(p, sqft, lumber_mult)
    remaining = ceiling - build_cost
    amenity_total, _ = _best_amenity_package(p, remaining)
    total_cost = build_cost + amenity_total
    return 100.0 * total_cost / ceiling


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    a = _pct_of_ceiling(p, p["farmhouse_sqft"], lumber_mult=1.0)
    b = _pct_of_ceiling(p, p["ranch_sqft"], lumber_mult=1.0)
    return {"A": a, "B": b}


def evaluate_twist(params):
    p = dict(PARAMS)
    p.update(params or {})
    mult = 1.0 + p["twist_lumber_increase_pct"] / 100.0
    a = _pct_of_ceiling(p, p["farmhouse_sqft"], lumber_mult=mult)
    b = _pct_of_ceiling(p, p["ranch_sqft"], lumber_mult=mult)
    return {"A": a, "B": b}


if __name__ == "__main__":
    base = evaluate({})
    tw = evaluate_twist({})
    print("base ", {k: round(v, 4) for k, v in base.items()},
          "margin(pts) %.4f" % abs(base["A"] - base["B"]))
    print("twist", {k: round(v, 4) for k, v in tw.items()},
          "margin(pts) %.4f" % abs(tw["A"] - tw["B"]))
