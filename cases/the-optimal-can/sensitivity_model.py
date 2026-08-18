#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Optimal Can.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. Contract per
skills/case-readiness/scripts/example_sensitivity_model.py:

    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            the STATED-ASSUMPTION subset
    evaluate(params) -> dict   {"A": metric, "B": metric}   HIGHER metric wins
    evaluate_twist(params)     not applicable -- this case has no twist (see
                                FACILITATOR.md, "Twist: N/A")

The case's primary_metric is a payback-period comparison against a ceiling, not
a plain "bigger number wins" metric, so this model expresses A's and B's
positions as **annual net material savings relative to the amount required to
clear the payback ceiling** (dollars over/under the bar). That keeps the shape
"higher is better" the same way every other case's evaluate() does, without
introducing a third quantity ("months") whose "lower is better" polarity would
break the shared probe harness.  A's "savings" is by definition 0 -- it retools
nothing and spends nothing -- so B's surplus/shortfall against the same
required-savings bar is what decides the case, exactly as balance_test says.

PARAMS holds every number case.md states, sourced or assumed. FLEX holds only
the four genuine Modeling Assumptions (MA1-MA4) -- the sheet thickness, the
retooling cost, the annual volume, and the payback ceiling. It deliberately
does NOT flex the sourced figures: the CMI standard diameter [S1], the 3104-H19
density [S2], or the aluminum spot price [S3] -- those are cited/given data,
not assumptions the case chose, and P6 (data decay) covers them instead.

Verified against cases/the-optimal-can/case.json:
    base   A=0.00  B=281268.82  (required 300000.00)   shortfall_pct 6.244
    -> Hold The Line (A) wins: B's surplus is negative, A's is exactly 0.
"""
import math

PARAMS = {
    # --- Appendix A: fixed fill volume, a definitional conversion, not sourced
    #     or assumed -- included here as a given constant both shapes share.
    "fixed_volume_in3": 21.65625,
    # --- Appendix A, Appendix E [S1]: CMI standard body outside diameter -----
    "r_std_in": 1.301,
    # --- Appendix B, Appendix E [S2]: density of 3104-H19 aluminum sheet -----
    "density_lb_in3": 0.0983,
    # --- Appendix B, Appendix E [S3]: current aluminum spot price -----------
    "price_usd_per_lb": 2.42,
    # --- Appendix B, Appendix D [MA1]: can-body sheet thickness -------------
    "sheet_thickness_in": 0.0043,
    # --- Appendix A/C, Appendix D [MA2]: retooling cost ----------------------
    "retool_cost_usd": 600000.0,
    # --- Appendix C, Appendix D [MA3]: Ridgeline's annual can volume --------
    "annual_can_volume": 300000000,
    # --- Appendix C, Appendix D [MA4]: capital-approval payback ceiling -----
    "ceiling_months": 24.0,
}

# Probe 5 flexes THESE and only these. SPEC section 2 asks for sensitivity to
# STATED ASSUMPTIONS, not to cited measurements: halving the CMI standard
# diameter or the sourced density/price is not a sensitivity test, it is a
# different case. The sourced figures (r_std_in, density_lb_in3,
# price_usd_per_lb, fixed_volume_in3) are cited/given data and are stress-
# tested by the data-decay probe (P6) instead, never by this list.
FLEX = [
    "sheet_thickness_in",   # MA1 -- Appendix D
    "retool_cost_usd",      # MA2 -- Appendix D
    "annual_can_volume",    # MA3 -- Appendix D
    "ceiling_months",       # MA4 -- Appendix D (the threshold itself)
]


def _std_geometry(p):
    """Hold The Line: the industry-standard radius, height and surface area
    at the fixed fill volume (case.md Appendix A, the student's own D1 work)."""
    r = p["r_std_in"]
    h = p["fixed_volume_in3"] / (math.pi * r ** 2)
    s = 2 * math.pi * r ** 2 + 2 * math.pi * r * h
    return r, h, s


def _opt_geometry(p):
    """The Slim Retool: the calculus-optimal radius/height/surface area for a
    closed cylinder of the same fixed volume (case.md D1/D2 -- r* = (V/2pi)^(1/3),
    h* = V/(pi r*^2))."""
    r = (p["fixed_volume_in3"] / (2 * math.pi)) ** (1.0 / 3.0)
    h = p["fixed_volume_in3"] / (math.pi * r ** 2)
    s = 2 * math.pi * r ** 2 + 2 * math.pi * r * h
    return r, h, s


def _cost_per_can(p, surface_area_in2):
    weight_lb = surface_area_in2 * p["sheet_thickness_in"] * p["density_lb_in3"]
    return weight_lb * p["price_usd_per_lb"]


def evaluate(params=None):
    """{"A": annual surplus/shortfall vs. the payback bar for Hold The Line,
    "B": annual surplus/shortfall vs. the payback bar for The Slim Retool}.
    Higher is better. A is always exactly 0 -- it retools nothing, so it has
    no bar to clear and no savings to report. B is the annual material
    savings minus the annual savings required to clear the ceiling in
    exactly ceiling_months; B > 0 means B clears the bar (verdict flips to
    The Slim Retool), B < 0 means Hold The Line wins, matching case.json's
    stated balance_test/derived figures at the base-case params."""
    p = dict(PARAMS)
    p.update(params or {})

    _, _, s_std = _std_geometry(p)
    _, _, s_opt = _opt_geometry(p)

    cost_std = _cost_per_can(p, s_std)
    cost_opt = _cost_per_can(p, s_opt)
    savings_per_can = cost_std - cost_opt

    annual_savings = savings_per_can * p["annual_can_volume"]
    required_annual_savings = p["retool_cost_usd"] / (p["ceiling_months"] / 12.0)

    a = 0.0
    b = annual_savings - required_annual_savings
    return {"A": a, "B": b}


if __name__ == "__main__":
    p = dict(PARAMS)
    _, h_std, s_std = _std_geometry(p)
    r_opt, h_opt, s_opt = _opt_geometry(p)
    cost_std = _cost_per_can(p, s_std)
    cost_opt = _cost_per_can(p, s_opt)
    savings_per_can = cost_std - cost_opt
    annual_savings = savings_per_can * p["annual_can_volume"]
    required = p["retool_cost_usd"] / (p["ceiling_months"] / 12.0)
    payback_months = p["retool_cost_usd"] / annual_savings * 12.0
    shortfall_pct = (required - annual_savings) / required * 100.0

    print("h_std %.4f  S_std %.4f  r_opt %.4f  h_opt %.4f  S_opt %.4f"
          % (h_std, s_std, r_opt, h_opt, s_opt))
    print("cost_std %.6f  cost_opt %.6f  savings/can %.6f"
          % (cost_std, cost_opt, savings_per_can))
    print("annual_savings %.2f  required %.2f  payback_months %.3f  shortfall_pct %.3f"
          % (annual_savings, required, payback_months, shortfall_pct))
    base = evaluate({})
    print("evaluate() ->", base, " winner:", "A" if base["A"] >= base["B"] else "B")
