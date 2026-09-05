"""Sensitivity model for The Two Offers (SPEC section 2 balance test, case-readiness Tier 2
probe 5). CONTRACT: evaluate(params) -> {"A": metric, "B": metric}, higher wins. Metric is
cumulative net value V(t) at the reference tenure t=24 months (case.json's margin reference).

Single disclosed formula, no hidden blend:
    V_A(t) = (base_A/12 - commute_month) * t + bonus_A
    V_B(t) = (base_B/12 + match_A_pct*base_B/12) * t + bonus_B     [match already USD/mo below]
"""

PARAMS = {
    "base_A": 96250.0,        # Appendix A, S1
    "bonus_A": 8663.0,        # Appendix A, S1-D1 (derived)
    "commute_month": 520.0,   # Appendix A, MA1 -- the case's ONLY stated modeling assumption
    "base_B": 80000.0,        # Appendix B, S3
    "bonus_B": 12000.0,       # Appendix B, S3-D1 (derived)
    "match_month_B": 313.33,  # Appendix B, S4-D1 (derived, $80,000 x 4.7% / 12)
    "reference_tenure_months": 24.0,
}

# Probe 5 flexes THIS and only this -- SPEC §2 asks for sensitivity to STATED ASSUMPTIONS, not
# to cited measurements. MA1 (commuting + parking cost) is the case's single modeling
# assumption; every other figure in PARAMS is a cited source (S1, S2, S3, S4), stress-tested
# instead by the data-decay probe (P6), not this one.
FLEX = ["commute_month"]


def net_monthly(p):
    net_A = p["base_A"] / 12.0 - p["commute_month"]
    net_B = p["base_B"] / 12.0 + p["match_month_B"]
    return net_A, net_B


def crossover_months(p):
    net_A, net_B = net_monthly(p)
    return (p["bonus_B"] - p["bonus_A"]) / (net_A - net_B)


def evaluate(p):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. Metric = cumulative net value at the
    reference tenure (24 months)."""
    net_A, net_B = net_monthly(p)
    t = p["reference_tenure_months"]
    return {
        "A": net_A * t + p["bonus_A"],
        "B": net_B * t + p["bonus_B"],
    }


def evaluate_twist(p):
    """Twist: N/A for this case (see FACILITATOR.md) -- no separate twist scenario to evaluate.
    Provided only so callers expecting the optional hook do not fail; returns evaluate(p)."""
    return evaluate(p)


if __name__ == "__main__":
    net_A, net_B = net_monthly(PARAMS)
    print(f"Net monthly value: A=${net_A:.2f}  B=${net_B:.2f}")
    t_cross = crossover_months(PARAMS)
    print(f"Crossover: t={t_cross:.2f} months")

    ev = evaluate(PARAMS)
    winner = "A" if ev["A"] > ev["B"] else "B"
    other = "B" if winner == "A" else "A"
    margin = (ev[winner] - ev[other]) / ev[other] * 100
    print(f"\nAt t={PARAMS['reference_tenure_months']:.0f} months: A=${ev['A']:.2f} B=${ev['B']:.2f} "
          f"winner={winner} margin={margin:.2f}%")
    assert abs(margin - 5.1) < 0.05, "margin drifted from case.json's recorded 5.1%"

    print("\nFlexing MA1 (commute_month) by +/-50%:")
    for mult, label in [(0.5, "-50%"), (1.5, "+50%")]:
        p2 = dict(PARAMS)
        p2["commute_month"] = PARAMS["commute_month"] * mult
        e2 = evaluate(p2)
        w2 = "A" if e2["A"] > e2["B"] else "B"
        o2 = "B" if w2 == "A" else "A"
        m2 = (e2[w2] - e2[o2]) / e2[o2] * 100
        tc2 = crossover_months(p2)
        print(f"  commute_month={p2['commute_month']:.2f} ({label}): A=${e2['A']:.2f} "
              f"B=${e2['B']:.2f} winner={w2} margin={m2:.2f}% crossover={tc2:.2f}mo")

    print("\nFlexing MA1 by +/-100% (0 and 2x) for a wider check:")
    for mult, label in [(0.0, "0 (no commute cost)"), (2.0, "+100%")]:
        p2 = dict(PARAMS)
        p2["commute_month"] = PARAMS["commute_month"] * mult
        e2 = evaluate(p2)
        w2 = "A" if e2["A"] > e2["B"] else "B"
        o2 = "B" if w2 == "A" else "A"
        m2 = (e2[w2] - e2[o2]) / e2[o2] * 100
        tc2 = crossover_months(p2)
        print(f"  commute_month={p2['commute_month']:.2f} ({label}): A=${e2['A']:.2f} "
              f"B=${e2['B']:.2f} winner={w2} margin={m2:.2f}% crossover={tc2:.2f}mo")
