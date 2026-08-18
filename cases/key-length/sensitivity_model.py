"""Sensitivity model for Key Length (SPEC section 2 balance test, case-readiness Tier 2 probe 5).

Primary metric: distance from Elena's target training-difficulty (sqrt(N)) -- lower distance wins.
CONTRACT: evaluate(params) -> {"A": metric, "B": metric}, higher wins, so this uses the same
ceiling-collapse transform verified in Plaza Pavers/Company Front/Vent Cap/Apron Order/Survey Corner.
"""
import math

PARAMS = {
    "candidate_a": 143.0,       # Appendix C -- 11 x 13
    "candidate_b": 323.0,       # Appendix C -- 17 x 19 (base case, pre-twist)
    "target_base": 15.05,       # fixed reference, never flexed
    "calib_buffer": 0.15,       # Appendix D MA1 -- FLEX target (15.05+0.15 = 15.2 base target)
}

FLEX = ["calib_buffer"]


def distances(p):
    target = p["target_base"] + p["calib_buffer"]
    sqrt_a = math.sqrt(p["candidate_a"])
    sqrt_b = math.sqrt(p["candidate_b"])
    return {"target": target, "sqrt_a": sqrt_a, "sqrt_b": sqrt_b,
            "dev_a": abs(sqrt_a - target), "dev_b": abs(sqrt_b - target)}


def evaluate(p):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. Ceiling-collapse transform, same
    pattern verified in every prior case: value = 2*worse - dev."""
    d = distances(p)
    dev_a, dev_b = d["dev_a"], d["dev_b"]
    ceiling = 2 * max(dev_a, dev_b)
    return {"A": ceiling - dev_a, "B": ceiling - dev_b}


def evaluate_twist(p):
    """Twist: a bug in the practice key-generator's random seed is found; re-running Candidate B's
    generation with the corrected seed produces 391 (17x23) instead of 323 (17x19) -- a real,
    disclosed scenario (stated in FACILITATOR.md), touching only candidate_b."""
    p2 = dict(p)
    p2["candidate_b"] = 391.0
    return evaluate(p2)


if __name__ == "__main__":
    d = distances(PARAMS)
    print(f"target={d['target']:.3f}  sqrtA={d['sqrt_a']:.3f} devA={d['dev_a']:.3f}  "
          f"sqrtB={d['sqrt_b']:.3f} devB={d['dev_b']:.3f}")
    winner = "A" if d["dev_a"] < d["dev_b"] else "B"
    other = "B" if winner == "A" else "A"
    devs = {"A": d["dev_a"], "B": d["dev_b"]}
    margin = (devs[other] - devs[winner]) / devs[other] * 100
    print(f"Winner: {winner}   margin: {margin:.2f}%")

    ev = evaluate(PARAMS)
    ev_margin = (max(ev.values()) - min(ev.values())) / min(ev.values()) * 100
    print(f"\nCONTRACT evaluate(): {ev}  (margin check: {ev_margin:.2f}%)")
    assert abs(ev_margin - margin) < 0.01

    dt = distances({**PARAMS, "candidate_b": 391.0})
    twinner = "A" if dt["dev_a"] < dt["dev_b"] else "B"
    tother = "B" if twinner == "A" else "A"
    tdevs = {"A": dt["dev_a"], "B": dt["dev_b"]}
    tmargin = (tdevs[tother] - tdevs[twinner]) / tdevs[tother] * 100
    print(f"\nTwist (Candidate B corrected to 391): sqrtB={dt['sqrt_b']:.3f} devB={dt['dev_b']:.3f}  "
          f"winner={twinner} margin={tmargin:.2f}%")

    for mult, label in [(0.5, "-50%"), (1.5, "+50%")]:
        p2 = dict(PARAMS); p2["calib_buffer"] = PARAMS["calib_buffer"] * mult
        d2 = distances(p2)
        w2 = "A" if d2["dev_a"] < d2["dev_b"] else "B"
        o2 = "B" if w2 == "A" else "A"
        v2 = {"A": d2["dev_a"], "B": d2["dev_b"]}
        m2 = (v2[o2] - v2[w2]) / v2[o2] * 100
        print(f"  calib_buffer {label} (target={d2['target']:.3f}): devA={d2['dev_a']:.3f} "
              f"devB={d2['dev_b']:.3f} winner={w2} margin={m2:.2f}%")
