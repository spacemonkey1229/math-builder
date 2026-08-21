#!/usr/bin/env python3
"""
Sensitivity model -- Fast Food.

Reproduces case.json.derived's own worked figures for both franchises (Subway =
"A", Papa John's = "B") from Appendix A/B/C's cited/assumed data, and lets
Tier 2 Probe 5 flex the case's real modeling assumptions +/-50%.

CONTRACT: PARAMS, FLEX, evaluate(params) -> {"A": roi_pct, "B": roi_pct}
(higher is better -- the case's primary_metric is first-year ROI, a percent,
not a raw dollar figure, so evaluate() returns percent, matching
case.json.primary_metric literally), evaluate_twist(params) for the Idaho
minimum-wage twist (FACILITATOR.md): labor cost rises from 30% to 34% of
revenue for both options.

WHAT IS AND ISN'T FLEX
  Both franchises' franchise fees, investment ranges, royalty/ad-fund/marketing
  rates (S1-S4, S6-S9) are real, officially-published figures -- GIVEN, cited
  data, not assumptions. The $806,000 combined capital ceiling is given
  scenario data about the fictional Reynolds/investor group, not something
  anyone estimated. None of these belong in FLEX; P6 (data decay) covers the
  cited figures instead.

  case.json.modeling_assumptions names exactly three things the case calls
  out as assumptions rather than given/cited fact:
    MA1 -- Day-1 employee headcount (non-numeric to the dollar math; not in
           PARAMS/FLEX at all, since evaluate() never uses it)
    MA2 -- monthly fixed operating costs (rent+utilities+insurance) for each
           franchise: subway_fixed_monthly, papa_fixed_monthly
    MA3 -- which AUV quartile represents Papa John's first-year revenue:
           papa_auv (the case uses the real, disclosed bottom-quartile figure,
           not the system median -- this is THE load-bearing choice keeping
           the case's margin under SPEC Section 2's 20% cap)
  case.json.sensitivity_disclosure also flags the food-cost-percentage choice
  (S12/S13) as a real judgment call (a specific point picked within a real,
  cited range, not the range's own midpoint) -- included in FLEX as
  subway_food_pct / papa_food_pct for the same reason.

Verified against cases/fast-food/case.json.derived (2026-08-20):
    base  A (Subway) ROI = 23.24%   B (Papa John's) ROI = 26.22%   margin 12.82%
    twist A ROI = 17.80%   B ROI = 22.12%   margin 24.26% (winner unchanged, margin widens past cap)
"""

PARAMS = {
    # --- given/cited scenario data (Appendix A) -----------------------------
    "subway_investment_mid": 367940.0,
    "papa_investment_mid": 585876.0,
    "subway_royalty_pct": 0.08,
    "subway_ad_pct": 0.045,
    "papa_royalty_pct": 0.05,
    "papa_marketing_pct": 0.06,
    "labor_pct": 0.30,   # S11, given industry benchmark applied identically to both
    # --- Appendix B: AUV (Subway's single estimate is given; Papa John's is FLEX via MA3) ---
    "subway_auv": 500000.0,
    "papa_auv": 600000.0,          # MA3 -- FLEX
    # --- Appendix B: food cost, a real judgment call within a cited range (FLEX) ------------
    "subway_food_pct": 0.32,
    "papa_food_pct": 0.25,
    # --- Appendix C, MA2 -- FLEX ---------------------------------------------
    "subway_fixed_monthly": 3500.0,
    "papa_fixed_monthly": 4200.0,
    # --- FACILITATOR.md twist: Idaho minimum wage hike ------------------------
    "twist_labor_pct": 0.34,
}

# Only the case's own real, disclosed modeling choices are swept by default.
FLEX = [
    "papa_auv",             # MA3
    "subway_fixed_monthly",  # MA2
    "papa_fixed_monthly",    # MA2
    "subway_food_pct",       # sensitivity_disclosure
    "papa_food_pct",         # sensitivity_disclosure
]


def _roi(revenue, pct_sum, fixed_monthly, investment_mid):
    variable_cost = revenue * pct_sum
    total_cost = variable_cost + fixed_monthly * 12
    net_profit = revenue - total_cost
    return 100.0 * net_profit / investment_mid


def evaluate(params):
    p = dict(PARAMS); p.update(params or {})
    sub_pct = p["subway_royalty_pct"] + p["subway_ad_pct"] + p["subway_food_pct"] + p["labor_pct"]
    pj_pct = p["papa_royalty_pct"] + p["papa_marketing_pct"] + p["papa_food_pct"] + p["labor_pct"]
    a = _roi(p["subway_auv"], sub_pct, p["subway_fixed_monthly"], p["subway_investment_mid"])
    b = _roi(p["papa_auv"], pj_pct, p["papa_fixed_monthly"], p["papa_investment_mid"])
    return {"A": a, "B": b}


def evaluate_twist(params):
    """Idaho minimum wage hike: labor cost rises to twist_labor_pct (34%) for both options."""
    p = dict(PARAMS); p.update(params or {})
    sub_pct = p["subway_royalty_pct"] + p["subway_ad_pct"] + p["subway_food_pct"] + p["twist_labor_pct"]
    pj_pct = p["papa_royalty_pct"] + p["papa_marketing_pct"] + p["papa_food_pct"] + p["twist_labor_pct"]
    a = _roi(p["subway_auv"], sub_pct, p["subway_fixed_monthly"], p["subway_investment_mid"])
    b = _roi(p["papa_auv"], pj_pct, p["papa_fixed_monthly"], p["papa_investment_mid"])
    return {"A": a, "B": b}


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})
    m = 100 * (base["B"] - base["A"]) / base["A"]
    mt = 100 * (tw["B"] - tw["A"]) / tw["A"]
    print("base ", {k: round(v, 2) for k, v in base.items()}, "margin %.2f%%" % m)
    print("twist", {k: round(v, 2) for k, v in tw.items()}, "margin %.2f%%" % mt)
