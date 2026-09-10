"""Sensitivity model for Dice Roll (SPEC §2 balance test, case-readiness Tier 2 probe 5).

Single disclosed formula, no hidden blend. CONTRACT: evaluate(params) -> {"A": metric, "B": metric},
higher wins. The metric is total program cost (mileage + lodging + M&IE + staff time) for 5
visits under each option; lower cost is better, so evaluate() uses the ceiling-collapse transform
used elsewhere in this corpus (Full Reach, Apron Order, Company Front): value = 2*max(costs) -
cost, which preserves ranking and lets the same "higher wins" contract cover a lower-is-better
metric.
"""

PARAMS = {
    "mileage_rate": 0.68,          # S7 -- Colorado state mileage rate, USD/mile, eff. 2026-07-01
    "mie_rate": 68.0,              # S8 -- GSA FY2026 standard CONUS M&IE, USD/day/person
    "lodging_rate": 110.0,         # S8 -- GSA FY2026 standard CONUS lodging, USD/night/person
    "staff_daily_rate": 450.0,     # MA2 -- loaded compliance-monitor daily cost, USD/day
    "overnight_threshold_mi": 150.0,  # MA1 -- one-way miles beyond which an overnight is required
    "n_visits": 5.0,               # MA3 -- site visits this cycle, both options

    # Appendix A one-way miles, Denver to county seat -- Option A's realized 5-county draw
    "a_jefferson_mi": 15.0,
    "a_boulder_mi": 66.0,
    "a_pueblo_mi": 114.0,
    "a_kitcarson_mi": 169.0,
    "a_alamosa_mi": 235.0,

    # Option B's 5-county Front Range Loop (fixed: the 5 nearest counties on the roster)
    "b_jefferson_mi": 15.0,
    "b_douglas_mi": 29.0,
    "b_larimer_mi": 64.0,
    "b_boulder_mi": 66.0,
    "b_elpaso_mi": 69.0,
}

FLEX = ["staff_daily_rate", "overnight_threshold_mi"]
# NOTE: mileage_rate ($0.68/mi) is deliberately NOT in FLEX -- it is a cited, sourced figure
# (S7, Colorado's own state mileage rate as of 2026-07-01), not a stated Modeling Assumption.
# Tier 2's P5 sweeps FLEX because SPEC Sec.2 tests sensitivity to ASSUMPTIONS, not to citations;
# stress-testing a cited value is P6's (data-decay) job, not P5's. Only MA1 (overnight_threshold_mi)
# and MA2 (staff_daily_rate) are genuinely author-chosen assumptions in this case's cost model.


def _visit_cost(one_way_mi, p):
    mileage = p["mileage_rate"] * 2 * one_way_mi
    lodging = p["lodging_rate"] if one_way_mi > p["overnight_threshold_mi"] else 0.0
    return mileage, lodging


def cost_breakdown(p):
    a_keys = ["a_jefferson_mi", "a_boulder_mi", "a_pueblo_mi", "a_kitcarson_mi", "a_alamosa_mi"]
    b_keys = ["b_jefferson_mi", "b_douglas_mi", "b_larimer_mi", "b_boulder_mi", "b_elpaso_mi"]

    a_mileage = a_lodging = 0.0
    for k in a_keys:
        m, l = _visit_cost(p[k], p)
        a_mileage += m; a_lodging += l
    b_mileage = b_lodging = 0.0
    for k in b_keys:
        m, l = _visit_cost(p[k], p)
        b_mileage += m; b_lodging += l

    n = p["n_visits"]
    mie = p["mie_rate"] * n          # identical under both options -- same visit count
    staff = p["staff_daily_rate"] * n  # identical under both options -- same visit count

    a_total = a_mileage + a_lodging + mie + staff
    b_total = b_mileage + b_lodging + mie + staff
    return {
        "mie": mie, "staff": staff,
        "a_mileage": a_mileage, "a_lodging": a_lodging, "A_cost": a_total,
        "b_mileage": b_mileage, "b_lodging": b_lodging, "B_cost": b_total,
    }


def evaluate(p):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. Ceiling-collapse transform."""
    b = cost_breakdown(p)
    a_cost, b_cost = b["A_cost"], b["B_cost"]
    ceiling = 2 * max(a_cost, b_cost)
    return {"A": ceiling - a_cost, "B": ceiling - b_cost}


def evaluate_twist(p):
    """Twist: a new direct state highway bypass opens, cutting Alamosa's round-trip driving
    distance in half -- tests whether a single geography change to one of Option A's far
    counties is enough on its own to flip the cost margin."""
    p2 = dict(p)
    p2["a_alamosa_mi"] = p["a_alamosa_mi"] * 0.5
    return evaluate(p2)


if __name__ == "__main__":
    b = cost_breakdown(PARAMS)
    print(f"Shared per-cycle costs: M&IE=${b['mie']:.2f}  staff=${b['staff']:.2f}")
    print(f"Option A (Statewide Draw): mileage=${b['a_mileage']:.2f} lodging=${b['a_lodging']:.2f} "
          f"total=${b['A_cost']:.2f}")
    print(f"Option B (Front Range Loop): mileage=${b['b_mileage']:.2f} lodging=${b['b_lodging']:.2f} "
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

    tw = evaluate_twist(PARAMS)
    print(f"\nTwist (Alamosa miles halved): {tw}")

    print("\nFLEX sensitivity (+/-50%):")
    for key in FLEX:
        for mult, label in [(0.5, "-50%"), (1.5, "+50%")]:
            p2 = dict(PARAMS); p2[key] = PARAMS[key] * mult
            r = cost_breakdown(p2)
            ch = "A" if r["A_cost"] < r["B_cost"] else "B"
            ot = "B" if ch == "A" else "A"
            v = {"A": r["A_cost"], "B": r["B_cost"]}
            m = (v[ot] - v[ch]) / v[ot] * 100
            print(f"  {key} {label}: A=${r['A_cost']:.2f} B=${r['B_cost']:.2f} cheaper={ch} margin={m:.2f}%")
