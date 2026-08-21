#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Pets.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. This is that
model, for cases/pets.

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):

    PARAMS                             dict[str, number]  every dial the case states
    FLEX                               list[str]          subset of PARAMS probe 5 flexes
    evaluate(params) -> dict           {"A": metric, "B": metric}
    evaluate_twist(params) -> dict     same shape, with the twist's own lens applied

IMPORTANT -- metric direction: this case's primary metric is a COST in USD per
year, so LOWER is better here (like Family Trip, unlike Cold Chain's in-spec
dose count). Callers comparing A vs B for "the winner" should take the smaller
value, not the larger one.

evaluate() returns the case's graded PRIMARY metric: total lifetime cost of
ownership (including Mom's required insurance every year) divided by expected
lifespan (case.json.primary_metric). This matches case.json.balance
(A=$2,935.62/yr, B=$2,515.00/yr, margin 16.7%).

evaluate_twist() returns the alternate, naive lens a Hero produces before
FACILITATOR.md's Twist reframes the comparison: the two pets' RAW lifetime
totals, un-normalized by lifespan. This is the comparison that makes the dog
look overwhelmingly (51.7%) more expensive before the Twist reveals that a
Beagle is simply expected to be alive three more years than a Scottish Fold
(case.json.derived.raw_lifetime_gap_pct) -- the reveal in FACILITATOR.md runs
the discussion from evaluate_twist()'s naive reading back to evaluate()'s
per-year one, not the other direction.

Verified against case.md / case.json:
    evaluate({})        A = 2935.62  B = 2515.00   margin (A-B)/B = 16.7%   (per year; B cheaper)
    evaluate_twist({})  A = 38163.00 B = 25150.00   margin (A-B)/B = 51.7%  (raw lifetime; B looks like a landslide)
"""

PARAMS = {
    # --- Appendix A / Appendix E, MA1: Beagle purchase price (breeder midpoint)
    "purchase_a_usd": 1250.00,
    # --- Appendix A / Appendix E, MA2: Beagle one-time setup cost (midpoint) --
    "setup_a_usd": 955.00,
    # --- Appendix A / Appendix E, MA3: Beagle ongoing annual cost, no insurance
    "annual_noins_a_usd": 2166.00,
    # --- Appendix D / Appendix E, MA4: Beagle annual insurance premium --------
    "insurance_a_usd": 600.00,
    # --- Appendix A / Appendix E, MA5: Beagle expected lifespan, years --------
    "lifespan_a_years": 13,
    # --- Appendix B / Appendix E, MA6: Scottish Fold purchase price (midpoint)
    "purchase_b_usd": 1750.00,
    # --- Appendix B / Appendix E, MA7: Scottish Fold one-time setup (midpoint)
    "setup_b_usd": 1050.00,
    # --- Appendix B / Appendix E, MA8: Fold ongoing annual cost, no insurance -
    "annual_noins_b_usd": 1875.00,
    # --- Appendix D / Appendix E, MA9: Fold annual insurance premium ----------
    #     (a direct cited POINT figure, S4's "$30/month" -- not a range midpoint)
    "insurance_b_usd": 360.00,
    # --- Appendix C / Appendix E, MA10: Scottish Fold expected lifespan -------
    "lifespan_b_years": 10,
}

# Probe 5 flexes THESE and only these -- the case's own STATED assumptions
# (Appendix E's midpoint-of-a-cited-range choices and the two lifespan
# figures), not directly-cited point figures. insurance_b_usd is excluded:
# it is S4's own cited point figure ("$30/month"), not an author-chosen
# midpoint -- stress-tested by the data-decay probe (P6) instead, per the
# same FLEX-scoping rule Family Trip's model documents.
FLEX = [
    "purchase_a_usd",       # Appendix E, MA1
    "setup_a_usd",          # Appendix E, MA2
    "annual_noins_a_usd",   # Appendix E, MA3
    "insurance_a_usd",      # Appendix E, MA4
    "lifespan_a_years",     # Appendix E, MA5
    "purchase_b_usd",       # Appendix E, MA6
    "setup_b_usd",          # Appendix E, MA7
    "annual_noins_b_usd",   # Appendix E, MA8
    "lifespan_b_years",     # Appendix E, MA10
]


def _day1(p, side):
    return p[f"purchase_{side}_usd"] + p[f"setup_{side}_usd"]


def _annual_total(p, side):
    return p[f"annual_noins_{side}_usd"] + p[f"insurance_{side}_usd"]


def _lifetime(p, side):
    return _day1(p, side) + _annual_total(p, side) * p[f"lifespan_{side}_years"]


def _per_year(p, side):
    lifespan = p[f"lifespan_{side}_years"]
    if lifespan <= 0:
        return float("inf")
    return _lifetime(p, side) / lifespan


def evaluate(params=None):
    """Primary graded metric: lifetime cost of ownership per year of expected
    lifespan, insurance included every year."""
    p = dict(PARAMS)
    p.update(params or {})
    return {"A": _per_year(p, "a"), "B": _per_year(p, "b")}


def evaluate_twist(params=None):
    """Naive, un-normalized lens -- the pre-Twist reading (FACILITATOR.md):
    raw lifetime totals, ignoring that the two pets don't live the same
    number of years."""
    p = dict(PARAMS)
    p.update(params or {})
    return {"A": _lifetime(p, "a"), "B": _lifetime(p, "b")}


if __name__ == "__main__":
    base = evaluate({})
    tw = evaluate_twist({})
    base_margin = 100 * (base["A"] - base["B"]) / base["B"]
    tw_margin = 100 * (tw["A"] - tw["B"]) / tw["B"]
    print("per-year (evaluate)            A=$%.2f  B=$%.2f  (A-B)/B=%.1f%%  -> %s cheaper" %
          (base["A"], base["B"], base_margin, "B" if base["B"] < base["A"] else "A"))
    print("raw lifetime, pre-twist (evaluate_twist) A=$%.2f  B=$%.2f  (A-B)/B=%.1f%%  -> %s cheaper" %
          (tw["A"], tw["B"], tw_margin, "B" if tw["B"] < tw["A"] else "A"))
