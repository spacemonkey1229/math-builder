#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- Urban Planner.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. This is that
model, for cases/urban-planner.

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):

    PARAMS                             dict[str, number]  every dial the case states
    FLEX                               list[str]          subset of PARAMS probe 5 flexes
    evaluate(params) -> dict           {"A": metric, "B": metric}
    evaluate_twist(params) -> dict     same shape, with the twist's own lens applied

IMPORTANT -- metric direction: the primary metric is a weighted SUITABILITY
SCORE (0-10ish scale, higher is better), like Cold Chain's in-spec-dose count,
unlike Acton Survey's or Family Trip's cost metrics where lower is better.

evaluate() returns the case's graded PRIMARY metric: the weighted score under
the case's example weighting (case.json.balance.margin_basis / Appendix F MA6).

Verified against case.md / case.json:
    evaluate({})  A = 7.68   B = 8.16   margin (B-A)/A = 6.33% -> B wins (example weighting)
    matches case.json.balance (A=7.68, B=8.16, margin_pct=6.3)

evaluate_twist() models the Guide Notes twist: the northwest half of Hayden
Island turns out to sit mostly within the Columbia River's active floodplain
and levee-protected wetland habitat (a real, documented condition of West
Hayden Island -- see RESEARCH_LOG.md), cutting Site B's already-small
developed-footprint assumption (MA1) in half again. This does not change any
CITED figure (acreage, coordinates, cost data are all unchanged) -- it only
lowers dev_pct_b, the case's own stated assumption, the same kind of move
Acton Survey's twist made to its own MA1.
"""

import math

# ---------------------------------------------------------------------------
# CITED DATA -- never flexed by probe 5 (P6 covers data decay on these instead)
# ---------------------------------------------------------------------------
CITY_HALL = (45.515014, -122.679122)          # S1
SITE_A_COORD = (45.47056, -122.63972)         # S3 (Westmoreland Park)
SITE_B_COORD = (45.61190, -122.67606)         # S4 (Hayden Island)

SITE_A_TOTAL_ACRES = 43.09 + 138.50           # S6 + S7 = 181.59
HAYDEN_TOTAL_ACRES = 1.69 * 640               # S4 (1.69 sq mi -> acres) = 1081.60

REEDWAY_SQFT = 130_000                        # S8
REEDWAY_UNITS = 120                           # S8
DENSITY_UNITS_PER_ACRE = REEDWAY_UNITS / (REEDWAY_SQFT / 43_560)  # derived, ~40.21

TOTAL_BUDGET_USD = 56_300_000                 # S9
N_VILLAGES = 6                                # S10
AVG_VILLAGE_PODS = 49                         # S11
COST_PER_RESIDENT_UNIT_USD = (TOTAL_BUDGET_USD / N_VILLAGES) / AVG_VILLAGE_PODS  # derived, ~191497

IRS_RATE_USD_PER_MILE = 0.725                 # S12


def _local_xy(origin, pt):
    lat0, lon0 = origin
    lat1, lon1 = pt
    y = (lat1 - lat0) * 69.0
    x = (lon1 - lon0) * 69.172 * math.cos(math.radians((lat0 + lat1) / 2))
    return x, y


_xa, _ya = _local_xy(CITY_HALL, SITE_A_COORD)
_xb, _yb = _local_xy(CITY_HALL, SITE_B_COORD)
DIST_A_MI = math.hypot(_xa, _ya)   # ~3.61
DIST_B_MI = math.hypot(_xb, _yb)   # ~6.69

# ---------------------------------------------------------------------------
# STATED ASSUMPTIONS (Appendix F) -- these are what probe 5 flexes
# ---------------------------------------------------------------------------
PARAMS = {
    "dev_pct_a": 0.01,          # MA1, applied to Site A
    "dev_pct_b": 0.01,          # MA1, applied to Site B (MA3 sets the 540.80-ac baseline it multiplies)
    "residents_per_trip": 25.0,  # MA4
    "w_access": 0.40,           # MA6
    "w_capacity": 0.35,         # MA6
    "w_cost": 0.25,             # MA6
}

# Only the case's own STATED assumptions are flexed -- not the real acreage,
# coordinates, density, or cost figures (S1-S12, cited data, stress-tested by
# P6 instead). MA2 (1 resident/unit) and MA5 (flat cost-per-unit rate, a fixed
# ratio of cited data S9/S10/S11) are deliberately excluded from FLEX -- see
# case.json.modeling_assumptions[] for why each is or isn't a scenario dial.
FLEX = [
    "dev_pct_a",
    "dev_pct_b",
    "residents_per_trip",
    "w_access",
    "w_capacity",
    "w_cost",
]


def _capacity(total_acres, dev_pct):
    return total_acres * dev_pct * DENSITY_UNITS_PER_ACRE


def _total_cost(capacity, dist_mi, residents_per_trip):
    buildout = capacity * COST_PER_RESIDENT_UNIT_USD
    trips_per_day = math.ceil(capacity / residents_per_trip) if capacity > 0 else 0
    miles_per_day = trips_per_day * dist_mi * 2  # round trip
    transport = miles_per_day * 365 * IRS_RATE_USD_PER_MILE
    return buildout + transport


def _scores(p):
    cap_a = _capacity(SITE_A_TOTAL_ACRES, p["dev_pct_a"])
    cap_b = _capacity(HAYDEN_TOTAL_ACRES / 2.0, p["dev_pct_b"])  # MA3: northwest half

    cost_a = _total_cost(cap_a, DIST_A_MI, p["residents_per_trip"])
    cost_b = _total_cost(cap_b, DIST_B_MI, p["residents_per_trip"])
    per_res_a = cost_a / cap_a
    per_res_b = cost_b / cap_b

    # Accessibility: smaller distance is better.
    if DIST_A_MI <= DIST_B_MI:
        acc_a, acc_b = 10.0, 10.0 * DIST_A_MI / DIST_B_MI
    else:
        acc_b, acc_a = 10.0, 10.0 * DIST_B_MI / DIST_A_MI

    # Capacity: larger is better.
    if cap_a >= cap_b:
        capsc_a, capsc_b = 10.0, 10.0 * cap_b / cap_a
    else:
        capsc_b, capsc_a = 10.0, 10.0 * cap_a / cap_b

    # Cost-efficiency: smaller cost-per-resident is better.
    if per_res_a <= per_res_b:
        costsc_a, costsc_b = 10.0, 10.0 * per_res_a / per_res_b
    else:
        costsc_b, costsc_a = 10.0, 10.0 * per_res_b / per_res_a

    w_sum = p["w_access"] + p["w_capacity"] + p["w_cost"]
    w_access, w_capacity, w_cost = p["w_access"] / w_sum, p["w_capacity"] / w_sum, p["w_cost"] / w_sum

    score_a = w_access * acc_a + w_capacity * capsc_a + w_cost * costsc_a
    score_b = w_access * acc_b + w_capacity * capsc_b + w_cost * costsc_b
    return score_a, score_b


def evaluate(params=None):
    """Primary graded metric: weighted suitability score (higher is better)."""
    p = dict(PARAMS)
    p.update(params or {})
    score_a, score_b = _scores(p)
    return {"A": score_a, "B": score_b}


def evaluate_twist(params=None):
    """Guide Notes twist: West Hayden Island's real floodplain/wetland-habitat
    status (RESEARCH_LOG.md) halves Site B's already-modest developed-footprint
    assumption, MA1, from 1% to 0.5%. No cited figure changes."""
    p = dict(PARAMS)
    p.update(params or {})
    p["dev_pct_b"] = p["dev_pct_b"] * 0.5
    score_a, score_b = _scores(p)
    return {"A": score_a, "B": score_b}


if __name__ == "__main__":
    base = evaluate({})
    tw = evaluate_twist({})
    base_margin = 100 * (base["B"] - base["A"]) / base["A"]
    tw_margin = 100 * (tw["B"] - tw["A"]) / tw["A"]
    print("dist_a=%.2f mi  dist_b=%.2f mi" % (DIST_A_MI, DIST_B_MI))
    print("density=%.2f units/acre  cost/resident-unit=$%.0f" %
          (DENSITY_UNITS_PER_ACRE, COST_PER_RESIDENT_UNIT_USD))
    print("base   A=%.2f  B=%.2f  (B-A)/A=%.2f%%  -> %s wins" %
          (base["A"], base["B"], base_margin, "B" if base["B"] > base["A"] else "A"))
    print("twist  A=%.2f  B=%.2f  (B-A)/A=%.2f%%  -> %s wins" %
          (tw["A"], tw["B"], tw_margin, "B" if tw["B"] > tw["A"] else "A"))
