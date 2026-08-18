"""Sensitivity model for Vent Cap (SPEC section 2 balance test, case-readiness Tier 2 probe 5).

Every dial is disclosed in case.md Appendix C/D/E -- single-pass formula, no hidden blend
(lesson applied from Plaza Pavers). CONTRACT: evaluate(params) -> {"A": metric, "B": metric},
higher wins -- this case's metric is total job cost (lower is better), so evaluate() returns
NEGATIVE-of-cost shifted by a per-run ceiling, same pattern as Plaza Pavers' fix, so the generic
(max-min)/min formula collapses to exactly this case's own (worse-better)/worse margin.
"""
import math

PARAMS = {
    "sheet_price": 68.39,        # S3
    "batch_n": 70.0,              # Appendix C
    "caps_per_sheet_a": 14.0,     # MA2 -- authored nesting result
    "caps_per_sheet_b": 12.0,     # MA2
    "seams_per_cap_a": 4.0,       # Appendix D, geometric fact (4 faces -> 4 seams)
    "seams_per_cap_b": 3.0,       # Appendix D (one seam pre-closed by the fold)
    "weld_cost_per_seam": 3.00,   # MA1
}

FLEX = ["weld_cost_per_seam"]


def cost_breakdown(p):
    sheets_a = math.ceil(p["batch_n"] / p["caps_per_sheet_a"])
    sheets_b = math.ceil(p["batch_n"] / p["caps_per_sheet_b"])
    material_a = sheets_a * p["sheet_price"]
    material_b = sheets_b * p["sheet_price"]
    labor_a = p["batch_n"] * p["seams_per_cap_a"] * p["weld_cost_per_seam"]
    labor_b = p["batch_n"] * p["seams_per_cap_b"] * p["weld_cost_per_seam"]
    return {
        "sheets_a": sheets_a, "sheets_b": sheets_b,
        "material_a": material_a, "material_b": material_b,
        "labor_a": labor_a, "labor_b": labor_b,
        "A_cost": material_a + labor_a, "B_cost": material_b + labor_b,
    }


def evaluate(p):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. Same ceiling-collapse transform as
    Plaza Pavers' evaluate(): value = 2*worse_cost - cost, which keeps both positive and reduces
    the generic (max-min)/min formula to exactly (worse-better)/worse -- this case's own margin
    definition, not a silently-different one."""
    b = cost_breakdown(p)
    a_cost, b_cost = b["A_cost"], b["B_cost"]
    ceiling = 2 * max(a_cost, b_cost)
    return {"A": ceiling - a_cost, "B": ceiling - b_cost}


def evaluate_twist(p):
    """Twist: a steel tariff spikes sheet price by 40% (MA3). Only the material line is affected;
    labor is untouched."""
    p2 = dict(p)
    p2["sheet_price"] = p["sheet_price"] * 1.40
    return evaluate(p2)


if __name__ == "__main__":
    b = cost_breakdown(PARAMS)
    print(f"Option A (4-Panel Cut): {b['sheets_a']:.0f} sheets (${b['material_a']:.2f}) + "
          f"{PARAMS['batch_n']:.0f}x{PARAMS['seams_per_cap_a']:.0f} seams (${b['labor_a']:.2f}) "
          f"= ${b['A_cost']:.2f}")
    print(f"Option B (3-Panel Fold): {b['sheets_b']:.0f} sheets (${b['material_b']:.2f}) + "
          f"{PARAMS['batch_n']:.0f}x{PARAMS['seams_per_cap_b']:.0f} seams (${b['labor_b']:.2f}) "
          f"= ${b['B_cost']:.2f}")
    cheaper = "A" if b["A_cost"] < b["B_cost"] else "B"
    other = "B" if cheaper == "A" else "A"
    costs = {"A": b["A_cost"], "B": b["B_cost"]}
    margin = (costs[other] - costs[cheaper]) / costs[other] * 100
    print(f"Cheaper: {cheaper}   margin: {margin:.2f}%")

    ev = evaluate(PARAMS)
    ev_margin = (max(ev.values()) - min(ev.values())) / min(ev.values()) * 100
    print(f"\nCONTRACT evaluate(): {ev}  (margin check: {ev_margin:.2f}%)")
    assert abs(ev_margin - margin) < 0.01

    t = cost_breakdown({**PARAMS, "sheet_price": PARAMS["sheet_price"] * 1.40})
    tcheaper = "A" if t["A_cost"] < t["B_cost"] else "B"
    tother = "B" if tcheaper == "A" else "A"
    tcosts = {"A": t["A_cost"], "B": t["B_cost"]}
    tmargin = (tcosts[tother] - tcosts[tcheaper]) / tcosts[tother] * 100
    print(f"\nTwist (+40% steel price): A=${t['A_cost']:.2f} B=${t['B_cost']:.2f} "
          f"cheaper={tcheaper} margin={tmargin:.2f}%")

    for mult, label in [(0.5, "-50%"), (1.5, "+50%")]:
        p2 = dict(PARAMS); p2["weld_cost_per_seam"] = PARAMS["weld_cost_per_seam"] * mult
        r = cost_breakdown(p2)
        ch = "A" if r["A_cost"] < r["B_cost"] else "B"
        ot = "B" if ch == "A" else "A"
        v = {"A": r["A_cost"], "B": r["B_cost"]}
        m = (v[ot] - v[ch]) / v[ot] * 100
        print(f"  weld_cost {label}: A=${r['A_cost']:.2f} B=${r['B_cost']:.2f} cheaper={ch} margin={m:.2f}%")
