"""Sensitivity model for The Weekly Rate (SPEC §2 balance test, case-readiness Tier 2 probe 5).

CONTRACT: evaluate(params) -> {"A": metric, "B": metric}, higher wins. The metric is total cost
to Dara over her stated decision horizon; lower cost is better, so evaluate() uses the
ceiling-collapse transform used elsewhere in this corpus (Dice Roll, Full Reach, Apron Order):
value = 2*max(costs) - cost, which preserves ranking and lets the same "higher wins" contract
cover a lower-is-better metric.
"""

PARAMS = {
    "purchase_price": 2299.0,          # S2 -- RadRunner 3 Plus MSRP, USD
    "battery_wh": 672.0,               # S2 -- battery capacity, Wh
    "charging_range_low_mi": 25.0,     # MA2 -- low end of S2's stated 25-45 mi range, chosen
    "electricity_rate": 0.1834,        # S3 -- EIA average residential price, USD/kWh, June 2026
    "weekly_mileage": 200.0,           # MA1 -- Dara's assumed weekly mileage
    "annual_maintenance_cost": 900.0,  # MA3 -- Dara's assumed self-maintenance cost if she owns, USD/yr
    "subscription_weekly_rate": 39.0,  # S1 -- Zoomo Standard Plan, USD/week
    "decision_horizon_weeks": 91.0,    # MA4 -- Dara's stated 21-month program length, in weeks
}

# Only genuinely author-chosen assumptions are swept by Tier 2 probe 5. subscription_weekly_rate
# and purchase_price are cited figures (S1, S2), not stated assumptions -- P6 (data decay), not
# P5, is the right probe for those. battery_wh and electricity_rate are likewise cited (S2, S3).
FLEX = ["decision_horizon_weeks", "annual_maintenance_cost", "charging_range_low_mi"]


def _weekly_slopes(p):
    """Returns (A_weekly_slope, B_weekly_slope) -- the per-week rate each option adds after any
    one-time purchase cost. Both options pay the same charging-electricity line, so it appears in
    both slopes identically (it does not, by itself, create or remove any margin)."""
    eff_wh_per_mi = p["battery_wh"] / p["charging_range_low_mi"]
    charging_cost_wk = eff_wh_per_mi * p["weekly_mileage"] / 1000.0 * p["electricity_rate"]
    maintenance_wk = p["annual_maintenance_cost"] / 52.0
    a_slope = maintenance_wk + charging_cost_wk
    b_slope = p["subscription_weekly_rate"] + charging_cost_wk
    return a_slope, b_slope, charging_cost_wk, maintenance_wk


def cost_breakdown(p, weeks=None):
    w = p["decision_horizon_weeks"] if weeks is None else weeks
    a_slope, b_slope, charging_wk, maint_wk = _weekly_slopes(p)
    a_total = p["purchase_price"] + a_slope * w
    b_total = b_slope * w
    breakeven = p["purchase_price"] / (b_slope - a_slope)
    return {
        "charging_cost_per_week": charging_wk, "maintenance_cost_per_week": maint_wk,
        "a_slope": a_slope, "b_slope": b_slope,
        "A_cost": a_total, "B_cost": b_total, "breakeven_weeks": breakeven, "weeks": w,
    }


def evaluate(p):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. Ceiling-collapse transform."""
    b = cost_breakdown(p)
    a_cost, b_cost = b["A_cost"], b["B_cost"]
    ceiling = 2 * max(a_cost, b_cost)
    return {"A": ceiling - a_cost, "B": ceiling - b_cost}


def evaluate_twist(p):
    """Twist: Zoomo's own documented pricing history (S5a -- its Flex Plan rose from $39/week to
    $49/week, ~26%, in exchange for expanded coverage) repeats itself on the Standard Plan,
    partway through Dara's 91-week horizon (weeks 1-40 at the base rate, weeks 41-91 at a 26%
    higher rate). Tests whether a single, realistically-grounded rate change to Option B alone is
    enough to flip the recommendation the base case reached."""
    w_before = 40.0
    w_after = max(p["decision_horizon_weeks"] - w_before, 0.0)
    _, b_slope_before, _, _ = _weekly_slopes(p)
    p2 = dict(p)
    p2["subscription_weekly_rate"] = p["subscription_weekly_rate"] * 1.26
    _, b_slope_after, _, _ = _weekly_slopes(p2)

    a_slope, _, _, _ = _weekly_slopes(p)
    a_total = p["purchase_price"] + a_slope * p["decision_horizon_weeks"]
    b_total = b_slope_before * w_before + b_slope_after * w_after

    ceiling = 2 * max(a_total, b_total)
    return {"A": ceiling - a_total, "B": ceiling - b_total}


if __name__ == "__main__":
    b = cost_breakdown(PARAMS)
    print(f"charging=${b['charging_cost_per_week']:.4f}/wk  maintenance=${b['maintenance_cost_per_week']:.4f}/wk")
    print(f"A slope=${b['a_slope']:.4f}/wk   B slope=${b['b_slope']:.4f}/wk")
    print(f"Breakeven: {b['breakeven_weeks']:.2f} weeks")
    print(f"At {b['weeks']:.0f} weeks: A=${b['A_cost']:.2f}  B=${b['B_cost']:.2f}")

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
    tw_cheaper = "A" if tw["A"] > tw["B"] else "B"
    tw_margin = (max(tw.values()) - min(tw.values())) / min(tw.values()) * 100
    print(f"\nTwist (26% rate hike after week 40): {tw}  cheaper={tw_cheaper}  margin={tw_margin:.2f}%")

    print("\nFLEX sensitivity (+/-50%):")
    for key in FLEX:
        for mult, label in [(0.5, "-50%"), (1.5, "+50%")]:
            p2 = dict(PARAMS); p2[key] = PARAMS[key] * mult
            r = cost_breakdown(p2)
            ch = "A" if r["A_cost"] < r["B_cost"] else "B"
            ot = "B" if ch == "A" else "A"
            v = {"A": r["A_cost"], "B": r["B_cost"]}
            m = (v[ot] - v[ch]) / v[ot] * 100
            flip = " <-- FLIPS WINNER" if ch != cheaper else ""
            cap = " <-- OVER 20% CAP" if m > 20 else ""
            print(f"  {key} {label}: A=${r['A_cost']:.2f} B=${r['B_cost']:.2f} cheaper={ch} margin={m:.2f}%{flip}{cap}")
