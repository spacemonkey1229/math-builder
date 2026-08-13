#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- Airplane Manufacturer.

Tier 2 probe 5 ("flex each stated assumption by +-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. This file is
that model for cases/airplane-manufacturer.

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     same shape, with the twist applied

A = turbine disks, B = inlet O-rings (matches case.json options).

Metric = D8 cutting efficiency -- this case's actual graded `primary_metric` /
`balance.margin_basis` (case.json), NOT weekly gross profit. D8 is minutes of
laser cutting time per square meter of finished part, LOWER is better; since
this contract requires "higher is better", evaluate() returns the inverse
(square meters of finished part per minute of laser time) so A/B compare the
same direction the contract expects. Weekly gross profit is real, disclosed,
and far larger (~679%, driven by the O-ring's bending cost and sale-price gap)
but is explicitly NOT the graded balance metric per case.json's
legacy_conversion_note/sensitivity_note -- see run_weekly_profit_check() below
for that number, kept for facilitator reference only.

Every entry in PARAMS corresponds to something case.md or case.json states: a
given scenario figure (Background/Appendix A/B/C) or a disclosed Modeling
Assumption (MA1-MA4). Nothing here is an authorial fudge factor.

Verified against cases/airplane-manufacturer/case.json `derived{}`:
    base (D8)      A (disk) min/m^2 = 2.53 -> 0.3953 m^2/min
                   B (O-ring) min/m^2 = 2.92 -> 0.3425 m^2/min
                   margin_pct (B->A) = 15.4%  (matches balance.margin_pct)
    base (profit, reference only) A weekly_profit = $1,394,241.61
                   B weekly_profit = $178,890.42   margin_pct (B->A) = 679.4%
    twist  A (disk) 10-day units = 4,760 (< 5,000, bonus NOT met)
           B (O-ring) 10-day units = 1,302 (< 5,000, bonus NOT met)

Independently verified finding (2026-08-13 QA pass): under the FLEX sweep
below, both disk_overall_h_in and disk_hole_d_in at +-50% flip the D8 winner
(B ends up "more efficient" than A) -- this is a real Tier 2 finding, and
MA1/MA2's sensitivity notes plus FACILITATOR.md have been corrected to
disclose it rather than claim (as an earlier draft wrongly did) that
sensitivity on these dials "does not change which option wins."
"""
import math

IN = 0.0254  # meters per inch

PARAMS = {
    # --- Background -----------------------------------------------------
    "sheet_w_m": 7.0,
    "sheet_h_m": 5.0,
    "aluminum_cost_per_m2": 76.80,
    "scrap_resale_per_m2": 23.45,
    "wage_per_hr_per_employee": 45.00,
    "employees_running_machine": 2,
    "hours_per_day": 20.0,
    "days_per_week": 5.0,
    # --- Appendix A -------------------------------------------------------
    "machine_cost": 136500.0,
    "cut_speed_m_per_min": 3.0,
    "load_time_min": 35.0,
    # --- Appendix B: O-ring -------------------------------------------------
    "oring_outer_d_in": 72.0,
    "oring_inner_d_in": 54.0,
    "oring_sell_price": 5498.00,
    "oring_bend_cost": 4870.00,
    # --- Appendix C + Modeling Assumptions: turbine disk ---------------------
    "disk_square_side_in": 28.0,
    "disk_overall_h_in": 36.0,          # MA1 basis
    "disk_teeth_per_side": 3,
    "disk_hole_d_in": 9.0,               # MA2 -- proprietary, one-time-exception estimate, 2026-08-13 (was 10.0)
    "disk_sell_price": 657.00,
    # --- Twist (Appendix D) ---------------------------------------------------
    "twist_bonus_per_part": 114.00,
    "twist_bonus_flat": 200000.00,
    "twist_target_units": 5000,
    "twist_sprint_days": 10,
    "twist_hours_per_day": 20.0,
}

# Probe 5 flexes THESE and only these -- the case's own disclosed Modeling
# Assumptions (MA1/MA2/MA4-equivalent dials) plus the twist's sprint length.
# Cited/given scenario figures (sell prices, machine cost, wage, sheet size)
# are stress-tested by the data-decay probe (P6) instead, per the reference
# contract's convention.
# FLEX rescoped 2026-08-13: disk_overall_h_in (36in) is the source sketch's own
# verbatim labeled dimension (case.md Appendix C) -- a cited measurement, not an
# assumption. MA1's real assumption is the tooth-SHAPE reconciliation choice
# (isosceles vs. the sketch's inconsistent "true equilateral" claim), a
# categorical modeling decision, not a continuous dial -- flexing the raw cited
# dimension +-50% tests measurement uncertainty on a real sketch label, which
# P5 doctrine assigns to citation/P6 territory, not this probe. disk_hole_d_in
# (MA2, genuinely unstated in the source) and wage_per_hr_per_employee (MA4, a
# genuine loading-convention assumption) remain -- both are real modeling
# choices the case had to make. twist_sprint_days (the twist's own construction)
# remains too.
FLEX = [
    "disk_hole_d_in",           # MA2: unstated hole diameter
    "wage_per_hr_per_employee", # MA4: fully-loaded wage assumption
    "twist_sprint_days",        # scenario construction (Appendix D)
]


def _oring(p):
    outer_d_m = p["oring_outer_d_in"] * IN
    inner_d_m = p["oring_inner_d_in"] * IN
    cut_path_m = math.pi * (outer_d_m + inner_d_m)
    cut_time_min = cut_path_m / p["cut_speed_m_per_min"]
    net_area_m2 = math.pi * ((outer_d_m / 2) ** 2 - (inner_d_m / 2) ** 2)
    bbox_m = outer_d_m
    per_row = math.floor(p["sheet_w_m"] / bbox_m)
    per_col = math.floor(p["sheet_h_m"] / bbox_m)
    per_sheet = max(1, per_row * per_col)
    return dict(cut_path_m=cut_path_m, cut_time_min=cut_time_min,
                net_area_m2=net_area_m2, per_sheet=per_sheet,
                sell_price=p["oring_sell_price"], bend_cost=p["oring_bend_cost"])


def _disk(p):
    side_m = p["disk_square_side_in"] * IN
    n = p["disk_teeth_per_side"]
    tooth_base_m = side_m / n
    # MA1: tooth height derived from (overall_height - square_side) / 2
    tooth_height_m = max(0.0, ((p["disk_overall_h_in"] - p["disk_square_side_in"]) / 2)) * IN
    tooth_slant_m = math.sqrt((tooth_base_m / 2) ** 2 + tooth_height_m ** 2)
    teeth_total = 4 * n
    perimeter_teeth_m = teeth_total * 2 * tooth_slant_m
    hole_d_m = p["disk_hole_d_in"] * IN
    cut_path_m = perimeter_teeth_m + math.pi * hole_d_m
    cut_time_min = cut_path_m / p["cut_speed_m_per_min"]
    tooth_area_m2 = 0.5 * tooth_base_m * tooth_height_m
    net_area_m2 = side_m ** 2 + teeth_total * tooth_area_m2 - math.pi * (hole_d_m / 2) ** 2
    bbox_m = p["disk_overall_h_in"] * IN
    per_row = math.floor(p["sheet_w_m"] / bbox_m)
    per_col = math.floor(p["sheet_h_m"] / bbox_m)
    per_sheet = max(1, per_row * per_col)
    return dict(cut_path_m=cut_path_m, cut_time_min=cut_time_min,
                net_area_m2=net_area_m2, per_sheet=per_sheet,
                sell_price=p["disk_sell_price"], bend_cost=0.0)


def _per_sheet_economics(p, part):
    sheet_area_m2 = p["sheet_w_m"] * p["sheet_h_m"]
    sheet_cost = sheet_area_m2 * p["aluminum_cost_per_m2"]
    total_cut_time = part["per_sheet"] * part["cut_time_min"]
    cycle_time_min = p["load_time_min"] + total_cut_time
    scrap_area = max(0.0, sheet_area_m2 - part["per_sheet"] * part["net_area_m2"])
    scrap_value = scrap_area * p["scrap_resale_per_m2"]
    net_material_cost = sheet_cost - scrap_value
    material_cost_per_part = net_material_cost / part["per_sheet"]
    wage_hr_total = p["wage_per_hr_per_employee"] * p["employees_running_machine"]
    labor_cost_sheet = (cycle_time_min / 60.0) * wage_hr_total
    labor_cost_per_part = labor_cost_sheet / part["per_sheet"]
    total_cost_per_part = material_cost_per_part + labor_cost_per_part + part["bend_cost"]
    profit_per_part = part["sell_price"] - total_cost_per_part
    return dict(cycle_time_min=cycle_time_min,
                total_cost_per_part=total_cost_per_part,
                profit_per_part=profit_per_part)


def _weekly(p, part, econ):
    week_min = p["hours_per_day"] * p["days_per_week"] * 60.0
    sheets_per_week = math.floor(week_min / econ["cycle_time_min"])
    parts_per_week = sheets_per_week * part["per_sheet"]
    weekly_profit = parts_per_week * econ["profit_per_part"]
    return dict(sheets_per_week=sheets_per_week, parts_per_week=parts_per_week,
                weekly_profit=weekly_profit)


def evaluate(params=None):
    """D8 cutting efficiency for each option -- the case's actual graded
    balance metric (case.json primary_metric / balance.margin_basis).

    D8 = cut_time_min / net_area_m2 (minutes of laser time per square meter),
    LOWER is better. This contract requires "higher is better", so we return
    the inverse (net_area_m2 / cut_time_min -- square meters of finished part
    cut per minute of laser time). A = turbine disks, B = O-rings.
    """
    p = dict(PARAMS); p.update(params or {})
    disk = _disk(p); oring = _oring(p)
    disk_efficiency = disk["net_area_m2"] / disk["cut_time_min"]
    oring_efficiency = oring["net_area_m2"] / oring["cut_time_min"]
    return {"A": disk_efficiency, "B": oring_efficiency}


def run_weekly_profit_check(params=None):
    """Weekly gross profit (USD) for each option -- NOT the graded balance
    metric (see module docstring). Kept as a separate, explicitly-named
    function (not `evaluate`) so Tier 2 probe 5 grades against D8, the real
    primary_metric, while this larger, separately-disclosed gap stays
    available for facilitator reference and for the FACILITATOR.md/case.json
    disclosure that documents it. A = turbine disks, B = O-rings."""
    p = dict(PARAMS); p.update(params or {})
    disk = _disk(p); oring = _oring(p)
    disk_econ = _per_sheet_economics(p, disk)
    oring_econ = _per_sheet_economics(p, oring)
    disk_week = _weekly(p, disk, disk_econ)
    oring_week = _weekly(p, oring, oring_econ)
    return {"A": disk_week["weekly_profit"], "B": oring_week["weekly_profit"]}


def evaluate_twist(params=None):
    """Units producible in the Twist's sprint window, and whether the >5,000
    bonus threshold is met. Returns {"A": units, "B": units} -- NOT profit,
    since the Twist's own question is a feasibility question, not a profit
    question. Facilitators should read this alongside evaluate()'s profit
    numbers, not in place of them."""
    p = dict(PARAMS); p.update(params or {})
    disk = _disk(p); oring = _oring(p)
    disk_econ = _per_sheet_economics(p, disk)
    oring_econ = _per_sheet_economics(p, oring)
    sprint_min = p["twist_hours_per_day"] * 60.0 * p["twist_sprint_days"]
    disk_sheets = math.floor(sprint_min / disk_econ["cycle_time_min"])
    oring_sheets = math.floor(sprint_min / oring_econ["cycle_time_min"])
    disk_units = disk_sheets * disk["per_sheet"]
    oring_units = oring_sheets * oring["per_sheet"]
    return {"A": disk_units, "B": oring_units,
            "A_meets_bonus": disk_units > p["twist_target_units"],
            "B_meets_bonus": oring_units > p["twist_target_units"]}


if __name__ == '__main__':
    base = evaluate({})
    margin = 100 * (base["A"] - base["B"]) / base["B"]
    print("base (D8 efficiency, m^2/min) ", {k: round(v, 4) for k, v in base.items()},
          "margin(A over B) %.1f%%" % margin)
    profit = run_weekly_profit_check({})
    profit_margin = 100 * (profit["A"] - profit["B"]) / profit["B"]
    print("base (weekly profit, reference only) ", {k: round(v, 2) for k, v in profit.items()},
          "margin(A over B) %.1f%%" % profit_margin)
    tw = evaluate_twist({})
    print("twist", tw)

    print("\n--- FLEX sweep (+-50% on each stated dial) ---")
    for key in FLEX:
        for mult, label in ((0.5, "-50%"), (1.5, "+50%")):
            flexed = dict(PARAMS)
            flexed[key] = PARAMS[key] * mult
            b = evaluate(flexed)
            m = 100 * (b["A"] - b["B"]) / b["B"] if b["B"] else float("inf")
            tw2 = evaluate_twist(flexed)
            print(f"  {key:28s} {label:5s} -> margin {m:7.1f}%  "
                  f"twist A={tw2['A']:5d}(bonus={tw2['A_meets_bonus']}) "
                  f"B={tw2['B']:5d}(bonus={tw2['B_meets_bonus']})")
