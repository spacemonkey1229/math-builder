"""Sensitivity model for Field Watch (SPEC section 2 balance test, case-readiness Tier 2 probe 5).

Primary metric: days of safety buffer between a model's predicted threshold-crossing day and the
claim filing deadline -- higher buffer wins. Unlike prior cases' cost/deviation metrics, buffer is
naturally "higher is better", so evaluate() returns it directly with no ceiling-collapse transform.
CONTRACT: evaluate(params) -> {"A": metric, "B": metric}, higher wins (A = Model A, B = Model B).
"""

PARAMS = {
    "p1_day": 3.0, "p1_ndvi": 0.72,     # Appendix B -- Pass 1
    "p2_day": 8.0, "p2_ndvi": 0.62,     # Appendix B -- Pass 2
    "p3_day": 13.0, "p3_ndvi": 0.51,    # Appendix B -- Pass 3
    "base_threshold": 0.37,             # fixed reference, never flexed
    "calib_margin": 0.03,               # Appendix D/F MA1 -- FLEX target (0.37+0.03 = 0.40 base)
    "deadline": 26.0,                   # Appendix D -- claim filing deadline
}

FLEX = ["calib_margin"]


def models(p):
    slope_a = (p["p2_ndvi"] - p["p1_ndvi"]) / (p["p2_day"] - p["p1_day"])
    slope_b = (p["p3_ndvi"] - p["p2_ndvi"]) / (p["p3_day"] - p["p2_day"])
    threshold = p["base_threshold"] + p["calib_margin"]
    day_a = p["p1_day"] + (threshold - p["p1_ndvi"]) / slope_a
    day_b = p["p2_day"] + (threshold - p["p2_ndvi"]) / slope_b
    buf_a = p["deadline"] - day_a
    buf_b = p["deadline"] - day_b
    return {"slope_a": slope_a, "slope_b": slope_b, "threshold": threshold,
            "day_a": day_a, "day_b": day_b, "buf_a": buf_a, "buf_b": buf_b}


def evaluate(p):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. Buffer is already higher-is-better,
    no transform needed."""
    m = models(p)
    return {"A": m["buf_a"], "B": m["buf_b"]}


def evaluate_twist(p):
    """Twist: a sensor recalibration correction reveals Pass 3's NDVI was under-reported --
    the raw reading said 0.51, the corrected value is 0.54 (a real, disclosed scenario, stated
    in FACILITATOR.md), touching only Model B's second anchor point."""
    p2 = dict(p)
    p2["p3_ndvi"] = 0.54
    return evaluate(p2)


if __name__ == "__main__":
    m = models(PARAMS)
    print(f"slopeA={m['slope_a']:.4f} slopeB={m['slope_b']:.4f} threshold={m['threshold']:.3f}")
    print(f"dayA={m['day_a']:.2f} dayB={m['day_b']:.2f}  bufA={m['buf_a']:.2f} bufB={m['buf_b']:.2f}")
    winner = "A" if m["buf_a"] > m["buf_b"] else "B"
    other = "B" if winner == "A" else "A"
    bufs = {"A": m["buf_a"], "B": m["buf_b"]}
    margin = (bufs[winner] - bufs[other]) / bufs[other] * 100
    print(f"Winner: {winner}   margin: {margin:.2f}%")

    ev = evaluate(PARAMS)
    ev_margin = (max(ev.values()) - min(ev.values())) / min(ev.values()) * 100
    print(f"\nCONTRACT evaluate(): {ev}  (margin check: {ev_margin:.2f}%)")
    assert abs(ev_margin - margin) < 0.01

    mt = models({**PARAMS, "p3_ndvi": 0.54})
    tbufs = {"A": mt["buf_a"], "B": mt["buf_b"]}
    twinner = max(tbufs, key=tbufs.get); tother = min(tbufs, key=tbufs.get)
    tmargin = (tbufs[twinner] - tbufs[tother]) / tbufs[tother] * 100
    print(f"\nTwist (Pass 3 NDVI corrected to 0.54): slopeB={mt['slope_b']:.4f} dayB={mt['day_b']:.2f} "
          f"bufA={mt['buf_a']:.2f} bufB={mt['buf_b']:.2f}  winner={twinner} margin={tmargin:.2f}%")

    for mult, label in [(0.5, "-50%"), (1.5, "+50%")]:
        p2 = dict(PARAMS); p2["calib_margin"] = PARAMS["calib_margin"] * mult
        m2 = models(p2)
        b2 = {"A": m2["buf_a"], "B": m2["buf_b"]}
        w2 = max(b2, key=b2.get); o2 = min(b2, key=b2.get)
        mg2 = (b2[w2] - b2[o2]) / b2[o2] * 100
        print(f"  calib_margin {label} (threshold={m2['threshold']:.3f}): bufA={m2['buf_a']:.2f} "
              f"bufB={m2['buf_b']:.2f} winner={w2} margin={mg2:.2f}%")
