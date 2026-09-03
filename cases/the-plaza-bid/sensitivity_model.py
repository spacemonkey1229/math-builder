#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- The Plaza Bid.

Tier 2 probe 5 ("flex each stated assumption by +-50%; report which flips
the verdict") needs a runnable model of the case's own arithmetic.

CONTRACT -- two public names:

    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

The case's SPEC Section 2 primary metric (case.json.balance.margin_basis) is
total installed cost per square foot of the plaza: material cost (purchased
sheet coverage x listed price per sq ft) plus labor cost (plaza area x labor
rate, including any pattern-specific premium), all divided by the plaza's
1,350 sq ft.

Total installed cost/sq ft is a COST -- lower is better -- but the probe's
contract is "higher is better", so evaluate() returns the NEGATIVE of the
cost per square foot.

Mechanism modeled explicitly (this is the whole point of the case):
Option A's (hexagon) manufactured sheet (11.625in x 10.25in, S1) does NOT
evenly divide the plaza's whole-foot dimensions, so its sheet-grid rounds up
in both directions and buys real waste (Appendix E). Option B's (octagon +
square) manufactured sheet is exactly 12in x 12in (S2), a perfect 1 sq ft
square that divides any whole-foot plaza dimension with zero grid-rounding
waste. That structural asymmetry is real and geometric, not a modeling
artifact -- it survives regardless of price/labor-rate assumptions. What
DOES flip the winner is MA4, the hexagon labor premium (Appendix F) -- see
__main__ for the sweep.

FLEX[] sweeps the case's own stated Modeling Assumptions that feed this
metric's arithmetic: MA3 (base labor rate) and MA4 (hexagon labor premium).
Tile prices (S1, S2) and the install waste allowance (S3) are real, directly
cited figures, not modeling assumptions, but are still exposed as PARAMS so
a facilitator can stress-test them too. MA1 (plaza dimensions) is not swept
by FLEX because changing it changes the sheet-grid rounding itself (a
structural, not continuous, effect) -- see plaza_length_ft/plaza_width_ft
for manual stress-testing instead.
"""

import math

PARAMS = {
    # --- Appendix A / MA1: plaza dimensions (ft) ------------------------------
    "plaza_length_ft": 45.0,
    "plaza_width_ft": 30.0,
    # --- Appendix C / S1: Option A (Hexagon) sheet spec -----------------------
    "hex_sheet_w_in": 11.625,
    "hex_sheet_h_in": 10.25,
    "hex_coverage_per_sheet_sqft": 0.81,
    "hex_price_per_sqft": 6.59,
    # --- Appendix D / S2: Option B (Octagon + Square) sheet spec --------------
    "oct_sheet_side_in": 12.0,
    "oct_coverage_per_sheet_sqft": 1.00,
    "oct_price_per_sqft": 9.69,
    # --- Appendix E / S3: installation waste allowance -------------------------
    "install_waste_factor": 0.10,
    # --- Appendix F / MA3, MA4: labor ------------------------------------------
    "base_labor_rate_per_sqft": 9.00,
    "hex_labor_premium": 0.15,
}

# Probe 5 flexes THESE and only these: the case's own stated Modeling
# Assumptions that feed the graded primary metric's arithmetic.
FLEX = [
    "base_labor_rate_per_sqft",   # MA3, Appendix F
    "hex_labor_premium",          # MA4, Appendix F -- the case's real fulcrum
]


def _ceil_clean(x, tol=1e-6):
    """math.ceil with a small tolerance so binary floating-point noise (e.g.
    1350 * 1.10 == 1485.0000000000002 in IEEE754) doesn't round an exact
    integer result up to the next integer."""
    r = round(x, 6)
    return math.ceil(r - tol) if abs(r - round(r)) < tol else math.ceil(r)


def _sheets_needed(plaza_length_ft, plaza_width_ft, sheet_w_ft, sheet_h_ft):
    cols = _ceil_clean(plaza_length_ft / sheet_w_ft)
    rows = _ceil_clean(plaza_width_ft / sheet_h_ft)
    return cols * rows


def _option_cost_per_sqft(p, sheet_w_in, sheet_h_in, coverage_per_sheet, price_per_sqft, labor_rate):
    plaza_area = p["plaza_length_ft"] * p["plaza_width_ft"]
    sheet_w_ft = sheet_w_in / 12.0
    sheet_h_ft = sheet_h_in / 12.0
    grid_sheets = _sheets_needed(p["plaza_length_ft"], p["plaza_width_ft"], sheet_w_ft, sheet_h_ft)
    sheets_to_buy = _ceil_clean(grid_sheets * (1.0 + p["install_waste_factor"]))
    purchased_coverage = sheets_to_buy * coverage_per_sheet
    material_cost = purchased_coverage * price_per_sqft
    labor_cost = plaza_area * labor_rate
    total_cost = material_cost + labor_cost
    waste_pct = 100.0 * (purchased_coverage - plaza_area) / purchased_coverage
    return {
        "grid_sheets": grid_sheets,
        "sheets_to_buy": sheets_to_buy,
        "purchased_coverage_sqft": purchased_coverage,
        "waste_pct": waste_pct,
        "material_cost": material_cost,
        "labor_cost": labor_cost,
        "total_cost": total_cost,
        "cost_per_sqft": total_cost / plaza_area,
    }


def evaluate_detail(params):
    p = dict(PARAMS)
    p.update(params or {})
    labor_rate_a = p["base_labor_rate_per_sqft"] * (1.0 + p["hex_labor_premium"])
    labor_rate_b = p["base_labor_rate_per_sqft"]
    a = _option_cost_per_sqft(p, p["hex_sheet_w_in"], p["hex_sheet_h_in"],
                               p["hex_coverage_per_sheet_sqft"], p["hex_price_per_sqft"], labor_rate_a)
    b = _option_cost_per_sqft(p, p["oct_sheet_side_in"], p["oct_sheet_side_in"],
                               p["oct_coverage_per_sheet_sqft"], p["oct_price_per_sqft"], labor_rate_b)
    # Lower cost/sq ft is better; evaluate()'s contract is "higher is
    # better", so return the negated cost/sq ft.
    return {"A": -a["cost_per_sqft"], "B": -b["cost_per_sqft"]}, a, b


def evaluate(params):
    """Tier 2 probe 5 contract: evaluate(params) -> {'A': metric, 'B': metric}
    ONLY -- no extra return values. Full diagnostics (per-option breakdown)
    are in evaluate_detail()."""
    r, _a, _b = evaluate_detail(params)
    return r


if __name__ == '__main__':
    base, a, b = evaluate_detail({})
    win = max(base, key=base.get)
    lo = min(base, key=base.get)
    win_cost, lo_cost = -base[win], -base[lo]
    margin = 100.0 * (lo_cost - win_cost) / lo_cost
    print("Option A (Hexagon):")
    for k, v in a.items():
        print(f"  {k}: {v}")
    print("Option B (Octagon + Square):")
    for k, v in b.items():
        print(f"  {k}: {v}")
    print()
    print("cost/sq ft  A=%.4f  B=%.4f" % (-base["A"], -base["B"]))
    print("winner:", win, " margin: %.2f%%" % margin)

    print()
    print("--- MA4 sweep (hexagon labor premium) ---")
    for premium in [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50]:
        r = evaluate({"hex_labor_premium": premium})
        w = max(r, key=r.get)
        m = 100.0 * (min(-r["A"], -r["B"]) - max(-r["A"], -r["B"])) * -1
        cost_a, cost_b = -r["A"], -r["B"]
        m = 100.0 * abs(cost_a - cost_b) / max(cost_a, cost_b)
        print(f"  premium={premium:+.0%}  A=${cost_a:.2f}/sqft  B=${cost_b:.2f}/sqft  winner={w}  margin={m:.1f}%")

    print()
    print("--- MA3 sweep (base labor rate, $/sq ft) ---")
    for rate in [3.0, 6.0, 9.0, 12.0, 15.0]:
        r = evaluate({"base_labor_rate_per_sqft": rate})
        w = max(r, key=r.get)
        cost_a, cost_b = -r["A"], -r["B"]
        m = 100.0 * abs(cost_a - cost_b) / max(cost_a, cost_b)
        print(f"  base_rate=${rate:.2f}/sqft  A=${cost_a:.2f}/sqft  B=${cost_b:.2f}/sqft  winner={w}  margin={m:.1f}%")
