#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Mainline Margin.

Tier 2 probe 5 ("flex each stated assumption by +-50%; report which flips
the verdict") needs a runnable model of the case's own arithmetic.

CONTRACT — two public names:

    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

REFRAME (2026-09-01) — see RESEARCH_LOG.md's dated addendum for the full
narrative. This case originally graded on a SINGLE blended number: total
annualized cost per acre-inch, NET of the EQIP cost-share reimbursement.
That number is real, but it blends two different things together: (1) true
engineering efficiency (material + energy cost only) and (2) the EQIP
Practice 430 subsidy, which pays PER POUND of pipe installed — i.e. it pays
MORE for the heavier, less-efficient-per-dollar option. Blending them hid a
genuinely interesting structural fact: once you strip the subsidy out, the
"true" efficiency gap between the two pipe options is barely more than a
rounding error (~1.3%), even though the net-of-subsidy gap that shows up on
Denise's actual bid is ~50.3%. Almost the entire graded margin was coming
from the subsidy formula, not from real engineering efficiency.

The case's PRIMARY metric is now (1), the gross/true comparison:
    true annualized cost = (material + labor) / 20-yr pipeline life
                            + annual pump energy cost
                            -- NO reimbursement term --
This isolates real engineering efficiency (pipe cost + pump energy) with
the subsidy formula removed entirely. evaluate() is now computed on THIS
metric, per SPEC's rule that evaluate() must track case.json's
primary_metric / balance.margin_pct.

The net-of-subsidy metric (the original primary metric, EQIP reimbursement
included) is retained as a SECONDARY metric via
evaluate_net_of_subsidy() / evaluate_net_of_subsidy_detail() -- it is what
actually shows up on Denise's bid, and D1/D3/D6 in case.md still ask
students to build it. Nothing about NRCS Code 430 certification (S1, S2),
the Lean Main's ~440.7 GPM certified ceiling, MA1 (440 GPM), or MA3 (88
acres) changed in this reframe -- only which of the two cost comparisons is
graded as primary, and how both are surfaced.

FLEX[] sweeps the case's own stated Modeling Assumptions that feed this
metric's arithmetic: MA1 (design flow), MA2 (run length), MA4 (labor rate),
MA5 (annual operating hours). MA3 (acreage) and MA7 (fuel type) are not
swept: MA3 only sets the basis MA1 was derived from and does not itself
enter the per-acre-inch cost arithmetic; MA7 is a scenario choice (fuel
type), not a continuously-flexible number.
"""

import math

PARAMS = {
    # --- Appendix A / MA1: mainline design flow rate (GPM) ------------------
    "design_flow_gpm": 440.0,
    # --- Appendix A / MA2: total mainline run length (ft) --------------------
    "run_length_ft": 1320.0,
    # --- Appendix A / MA4: installation labor rate (USD/ft) ------------------
    "labor_rate_per_ft": 25.00,
    # --- Appendix A / MA5: annual system operating hours (hr/yr) -------------
    "annual_hours": 1200.0,
    # --- Appendix B: Option A (Lean Main) spec ------------------------------
    "diameter_in_a": 6.0,
    "weight_lb_per_ft_a": 2.40,
    "material_cost_per_ft_a": 5.10,
    # --- Appendix C: Option B (Margin Main) spec ------------------------------
    "diameter_in_b": 8.0,
    "weight_lb_per_ft_b": 4.16,
    "material_cost_per_ft_b": 7.30,
    # --- Appendix D: NRCS Code 430 --------------------------------------------
    "hw_c": 150.0,               # Hazen-Williams roughness coefficient (S3)
    "velocity_ceiling_fps": 5.0,  # S1
    # --- Appendix E: EQIP terms ------------------------------------------------
    "eqip_rate_per_lb": 4.22,     # S5
    # --- Appendix F: pump energy -----------------------------------------------
    "pump_efficiency": 0.75,      # S10 (BHP formula denominator constant is fixed at 3960)
    "whp_hr_per_kwh_electric": 0.885,  # S9
    "price_per_kwh": 0.0917,      # S12
    # --- Fixed case parameters ---------------------------------------------------
    "pipeline_life_years": 20.0,   # Code 430's own stated minimum expected life
}

# Probe 5 flexes THESE and only these: the case's own stated Modeling
# Assumptions that feed the graded primary metric's arithmetic.
FLEX = [
    "design_flow_gpm",       # MA1, Appendix A -- the case's real fulcrum
    "run_length_ft",         # MA2, Appendix A
    "labor_rate_per_ft",     # MA4, Appendix A
    "annual_hours",          # MA5, Appendix A
]

GPM_PER_CFS = 448.8325
GAL_PER_ACRE_INCH = 27154.28


def _velocity_fps(gpm, diameter_in):
    q_cfs = gpm / GPM_PER_CFS
    d_ft = diameter_in / 12.0
    area_sqft = math.pi / 4.0 * d_ft ** 2
    return q_cfs / area_sqft


def _friction_loss_ft(gpm, diameter_in, hw_c, length_ft):
    q_cfs = gpm / GPM_PER_CFS
    d_ft = diameter_in / 12.0
    return 4.732 * (q_cfs / hw_c) ** 1.85 * (length_ft / d_ft ** 4.87)


def _annual_energy_cost(gpm, head_ft, p):
    whp = (gpm * head_ft) / 3960.0
    annual_whp_hr = whp * p["annual_hours"]
    kwh = annual_whp_hr / p["whp_hr_per_kwh_electric"]
    return kwh * p["price_per_kwh"]


def _option_breakdown(gpm, diameter_in, weight_lb_per_ft, material_cost_per_ft, p):
    """Shared per-option arithmetic. Returns both the TRUE (gross,
    subsidy-free) and NET-OF-SUBSIDY (EQIP-included) annualized cost, plus
    the certification/velocity facts D4 needs. Neither number here changes
    Code 430's certification math -- only how the cost comparison is framed."""
    length = p["run_length_ft"]
    installed_cost = (material_cost_per_ft + p["labor_rate_per_ft"]) * length
    weight_lb = weight_lb_per_ft * length
    velocity = _velocity_fps(gpm, diameter_in)
    certified = velocity <= p["velocity_ceiling_fps"]
    reimbursement = weight_lb * p["eqip_rate_per_lb"] if certified else 0.0

    head_ft = _friction_loss_ft(gpm, diameter_in, p["hw_c"], length)
    energy_cost = _annual_energy_cost(gpm, head_ft, p)

    # PRIMARY metric: true/gross cost -- material + labor + energy ONLY,
    # subsidy formula removed entirely. Isolates real engineering efficiency.
    true_annualized_capital = installed_cost / p["pipeline_life_years"]
    true_total_annual_cost = true_annualized_capital + energy_cost

    # SECONDARY metric: net-of-subsidy -- what actually shows up on
    # Denise's bid, EQIP reimbursement included (and forfeited on failed
    # certification, per Appendix E's all-or-nothing rule).
    net_capital = installed_cost - reimbursement
    net_annualized_capital = net_capital / p["pipeline_life_years"]
    net_total_annual_cost = net_annualized_capital + energy_cost

    annual_gallons = gpm * 60.0 * p["annual_hours"]
    acre_inches = annual_gallons / GAL_PER_ACRE_INCH

    return {
        "certified": certified,
        "velocity_fps": velocity,
        "installed_cost": installed_cost,
        "reimbursement": reimbursement,
        "head_ft": head_ft,
        "energy_cost": energy_cost,
        "acre_inches": acre_inches,
        # true / gross (PRIMARY)
        "true_annualized_capital": true_annualized_capital,
        "true_total_annual_cost": true_total_annual_cost,
        "true_cost_per_acre_inch": true_total_annual_cost / acre_inches,
        # net-of-subsidy (SECONDARY)
        "net_capital": net_capital,
        "net_annualized_capital": net_annualized_capital,
        "net_total_annual_cost": net_total_annual_cost,
        "net_cost_per_acre_inch": net_total_annual_cost / acre_inches,
    }


def evaluate_detail(params):
    """PRIMARY metric detail: true/gross cost per acre-inch (no EQIP
    reimbursement). Lower cost/acre-inch is better; evaluate()'s contract is
    "higher is better", so the returned dict negates the cost."""
    p = dict(PARAMS)
    p.update(params or {})
    gpm = p["design_flow_gpm"]
    a = _option_breakdown(gpm, p["diameter_in_a"], p["weight_lb_per_ft_a"], p["material_cost_per_ft_a"], p)
    b = _option_breakdown(gpm, p["diameter_in_b"], p["weight_lb_per_ft_b"], p["material_cost_per_ft_b"], p)
    return {"A": -a["true_cost_per_acre_inch"], "B": -b["true_cost_per_acre_inch"]}, a, b


def evaluate(params):
    """Tier 2 probe 5 contract: evaluate(params) -> {'A': metric, 'B': metric}
    ONLY -- no extra return values, since the probe's own max()/min() over
    the return value would otherwise break on a 3-tuple. Computed on the
    PRIMARY metric (true/gross cost per acre-inch, no EQIP reimbursement).
    Full diagnostics (per-option breakdown, both metrics) are in
    evaluate_detail() / evaluate_net_of_subsidy_detail()."""
    r, _a, _b = evaluate_detail(params)
    return r


def evaluate_net_of_subsidy_detail(params):
    """SECONDARY metric detail: net-of-subsidy cost per acre-inch (EQIP
    reimbursement included, forfeited on failed certification). This was
    the case's sole primary metric before the 2026-09-01 reframe; it is
    what actually shows up on Denise's bid, and remains what D1-D3/D6 ask
    students to build."""
    p = dict(PARAMS)
    p.update(params or {})
    gpm = p["design_flow_gpm"]
    a = _option_breakdown(gpm, p["diameter_in_a"], p["weight_lb_per_ft_a"], p["material_cost_per_ft_a"], p)
    b = _option_breakdown(gpm, p["diameter_in_b"], p["weight_lb_per_ft_b"], p["material_cost_per_ft_b"], p)
    return {"A": -a["net_cost_per_acre_inch"], "B": -b["net_cost_per_acre_inch"]}, a, b


def evaluate_net_of_subsidy(params):
    r, _a, _b = evaluate_net_of_subsidy_detail(params)
    return r


def _margin(base):
    win = max(base, key=base.get)
    lo = min(base, key=base.get)
    win_cost, lo_cost = -base[win], -base[lo]
    margin = 100.0 * (lo_cost - win_cost) / win_cost
    return win, margin, win_cost, lo_cost


if __name__ == '__main__':
    true_base, a, b = evaluate_detail({})
    net_base, _a2, _b2 = evaluate_net_of_subsidy_detail({})

    print("Option A (Lean Main):")
    for k, v in a.items():
        print(f"  {k}: {v}")
    print("Option B (Margin Main):")
    for k, v in b.items():
        print(f"  {k}: {v}")
    print()

    win, margin, win_cost, lo_cost = _margin(true_base)
    print("[PRIMARY] true (subsidy-free) cost/acre-inch  A=%.4f  B=%.4f" % (-true_base["A"], -true_base["B"]))
    print("[PRIMARY] true winner:", win, " margin: %.2f%%" % margin)

    win2, margin2, win_cost2, lo_cost2 = _margin(net_base)
    print("[SECONDARY] net-of-subsidy cost/acre-inch  A=%.4f  B=%.4f" % (-net_base["A"], -net_base["B"]))
    print("[SECONDARY] net-of-subsidy winner:", win2, " margin: %.2f%%" % margin2)

    print()
    print("Subsidy-formula effect on the margin: %.2f points (net %.2f%% - true %.2f%%)"
          % (margin2 - margin, margin2, margin))

    # Certified-max-flow check for the Lean Main (6 in), independent of MA1:
    # solve velocity_fps(gpm, 6) == 5.0 for gpm.
    ceiling = PARAMS["velocity_ceiling_fps"]
    d_ft = PARAMS["diameter_in_a"] / 12.0
    area = math.pi / 4.0 * d_ft ** 2
    max_q_cfs = ceiling * area
    max_gpm = max_q_cfs * GPM_PER_CFS
    print("Lean Main certified max flow: %.2f GPM" % max_gpm)
