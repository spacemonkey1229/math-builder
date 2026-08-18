"""Sensitivity model for Survey Corner (SPEC section 2 balance test, case-readiness Tier 2 probe 5).

Primary metric: angular deviation (degrees) between each candidate pin's actual corner angle and
the plat's expected angle -- lower deviation wins. CONTRACT: evaluate(params) -> {"A": metric,
"B": metric}, higher wins, so this uses the same ceiling-collapse transform verified in Plaza
Pavers/Company Front/Vent Cap/Apron Order (A = Pin 1, B = Pin 2).
"""

PARAMS = {
    "right_angle_deg": 90.0,  # fixed reference, never flexed
    "nw_excess_deg": 3.0,     # Appendix B -- NW corner angle expressed as excess past square
                               # (93 deg = 90 + 3); MA1's real recording/rounding uncertainty
                               # scales with this excess, not with the whole 93 deg angle --
                               # see FACILITATOR.md's sensitivity note for why.
    "pin1_raw": 88.5,     # Appendix C -- Pin 1 total-station backsight-to-shot angle
    "pin2_raw": 89.0,     # Appendix C -- Pin 2 total-station backsight-to-shot angle
}

FLEX = ["nw_excess_deg"]


def deviations(p):
    nw_angle = p["right_angle_deg"] + p["nw_excess_deg"]
    expected = 180.0 - nw_angle
    actual_a = 180.0 - p["pin1_raw"]
    actual_b = 180.0 - p["pin2_raw"]
    return {
        "nw_angle": nw_angle, "expected": expected, "actual_a": actual_a, "actual_b": actual_b,
        "dev_a": abs(actual_a - expected), "dev_b": abs(actual_b - expected),
    }


def evaluate(p):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. Ceiling-collapse transform, same
    pattern verified in Plaza Pavers/Company Front/Vent Cap/Apron Order: value = 2*worse - dev."""
    d = deviations(p)
    dev_a, dev_b = d["dev_a"], d["dev_b"]
    ceiling = 2 * max(dev_a, dev_b)
    return {"A": ceiling - dev_a, "B": ceiling - dev_b}


def evaluate_twist(p):
    """Twist: re-checking the data-logger export reveals Pin 2's total-station reading was
    mis-transcribed -- the raw field notes said 89.0 deg, the logger export says 88.3 deg. A
    real, disclosed scenario (MA3-equivalent, stated in FACILITATOR.md), touching only pin2_raw."""
    p2 = dict(p)
    p2["pin2_raw"] = 88.3
    return evaluate(p2)


if __name__ == "__main__":
    d = deviations(PARAMS)
    print(f"expected={d['expected']:.2f}  Pin1 actual={d['actual_a']:.2f} dev={d['dev_a']:.2f}  "
          f"Pin2 actual={d['actual_b']:.2f} dev={d['dev_b']:.2f}")
    winner = "A" if d["dev_a"] < d["dev_b"] else "B"
    other = "B" if winner == "A" else "A"
    devs = {"A": d["dev_a"], "B": d["dev_b"]}
    margin = (devs[other] - devs[winner]) / devs[other] * 100
    print(f"Winner: {winner}   margin: {margin:.2f}%")

    ev = evaluate(PARAMS)
    ev_margin = (max(ev.values()) - min(ev.values())) / min(ev.values()) * 100
    print(f"\nCONTRACT evaluate(): {ev}  (margin check: {ev_margin:.2f}%)")
    assert abs(ev_margin - margin) < 0.01

    dt = deviations({**PARAMS, "pin2_raw": 88.3})
    twinner = "A" if dt["dev_a"] < dt["dev_b"] else "B"
    tother = "B" if twinner == "A" else "A"
    tdevs = {"A": dt["dev_a"], "B": dt["dev_b"]}
    tmargin = (tdevs[tother] - tdevs[twinner]) / tdevs[tother] * 100
    print(f"\nTwist (Pin 2 raw corrected to 88.3): Pin1 dev={dt['dev_a']:.2f} "
          f"Pin2 dev={dt['dev_b']:.2f}  winner={twinner} margin={tmargin:.2f}%")

    for mult, label in [(0.5, "-50%"), (1.5, "+50%")]:
        p2 = dict(PARAMS); p2["nw_excess_deg"] = PARAMS["nw_excess_deg"] * mult
        d2 = deviations(p2)
        w2 = "A" if d2["dev_a"] < d2["dev_b"] else "B"
        o2 = "B" if w2 == "A" else "A"
        v2 = {"A": d2["dev_a"], "B": d2["dev_b"]}
        m2 = (v2[o2] - v2[w2]) / v2[o2] * 100
        print(f"  nw_excess_deg {label} (nw_angle={d2['nw_angle']:.1f}): Pin1 dev={d2['dev_a']:.2f} "
              f"Pin2 dev={d2['dev_b']:.2f} winner={w2} margin={m2:.2f}%")
