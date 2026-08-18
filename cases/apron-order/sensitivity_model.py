"""Sensitivity model for Apron Order (SPEC section 2 balance test, case-readiness Tier 2 probe 5).

Single disclosed formula, no hidden blend. CONTRACT: evaluate(params) -> {"A": metric, "B": metric},
higher wins -- metric is total job cost (lower is better), so evaluate() uses the same
ceiling-collapse transform verified in Plaza Pavers/Company Front/Vent Cap.
"""

PARAMS = {
    "price_per_yd": 3.60,        # S1
    "batch_n": 40.0,              # Appendix D
    "yd_per_apron_a": 1.25,       # Appendix C (1 1/4)
    "yd_per_apron_b": 7.0 / 6.0,  # Appendix C (1 1/6)
    "min_per_apron_a": 3.0,       # Appendix C
    "min_per_apron_b": 6.0,       # Appendix C
    "wage_per_hr": 16.00,         # MA1
}

FLEX = ["wage_per_hr"]


def cost_breakdown(p):
    material_a = p["yd_per_apron_a"] * p["batch_n"] * p["price_per_yd"]
    material_b = p["yd_per_apron_b"] * p["batch_n"] * p["price_per_yd"]
    labor_a = p["batch_n"] * p["min_per_apron_a"] * (p["wage_per_hr"] / 60.0)
    labor_b = p["batch_n"] * p["min_per_apron_b"] * (p["wage_per_hr"] / 60.0)
    return {
        "material_a": material_a, "material_b": material_b,
        "labor_a": labor_a, "labor_b": labor_b,
        "A_cost": material_a + labor_a, "B_cost": material_b + labor_b,
    }


def evaluate(p):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. Ceiling-collapse transform, same
    pattern verified in Plaza Pavers/Company Front/Vent Cap: value = 2*worse - cost."""
    b = cost_breakdown(p)
    a_cost, b_cost = b["A_cost"], b["B_cost"]
    ceiling = 2 * max(a_cost, b_cost)
    return {"A": ceiling - a_cost, "B": ceiling - b_cost}


def evaluate_twist(p):
    """Twist: a directional/napped print forces an extra 1/8 yd/apron on Option A (cut-on-fold)
    only -- a real cutting-room concern (MA3), not touching Option B or the labor line."""
    p2 = dict(p)
    p2["yd_per_apron_a"] = p["yd_per_apron_a"] + 0.125
    return evaluate(p2)


if __name__ == "__main__":
    b = cost_breakdown(PARAMS)
    print(f"Option A (Cut on the Fold): material=${b['material_a']:.2f} labor=${b['labor_a']:.2f} "
          f"total=${b['A_cost']:.2f}")
    print(f"Option B (Cut Open):        material=${b['material_b']:.2f} labor=${b['labor_b']:.2f} "
          f"total=${b['B_cost']:.2f}")
    cheaper = "A" if b["A_cost"] < b["B_cost"] else "B"
    other = "B" if cheaper == "A" else "A"
    costs = {"A": b["A_cost"], "B": b["B_cost"]}
    margin = (costs[other] - costs[cheaper]) / costs[other] * 100
    print(f"Cheaper: {cheaper}   margin: {margin:.2f}%")

    ev = evaluate(PARAMS)
    ev_margin = (max(ev.values()) - min(ev.values())) / min(ev.values()) * 100
    print(f"\nCONTRACT evaluate(): {ev}  (margin check: {ev_margin:.2f}%)")
    assert abs(ev_margin - margin) < 0.01

    t = cost_breakdown({**PARAMS, "yd_per_apron_a": PARAMS["yd_per_apron_a"] + 0.125})
    tcheaper = "A" if t["A_cost"] < t["B_cost"] else "B"
    tother = "B" if tcheaper == "A" else "A"
    tcosts = {"A": t["A_cost"], "B": t["B_cost"]}
    tmargin = (tcosts[tother] - tcosts[tcheaper]) / tcosts[tother] * 100
    print(f"\nTwist (+1/8 yd/apron, Option A): A=${t['A_cost']:.2f} B=${t['B_cost']:.2f} "
          f"cheaper={tcheaper} margin={tmargin:.2f}%")

    for mult, label in [(0.5, "-50%"), (1.5, "+50%")]:
        p2 = dict(PARAMS); p2["wage_per_hr"] = PARAMS["wage_per_hr"] * mult
        r = cost_breakdown(p2)
        ch = "A" if r["A_cost"] < r["B_cost"] else "B"
        ot = "B" if ch == "A" else "A"
        v = {"A": r["A_cost"], "B": r["B_cost"]}
        m = (v[ot] - v[ch]) / v[ot] * 100
        print(f"  wage {label}: A=${r['A_cost']:.2f} B=${r['B_cost']:.2f} cheaper={ch} margin={m:.2f}%")
