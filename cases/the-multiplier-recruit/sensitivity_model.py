#!/usr/bin/env python3
"""
Sensitivity model — The Multiplier Recruit.

Tier 2 probe 5 flexes each stated assumption by +/-50% and reports which flips
the verdict. Contract: PARAMS, evaluate(params) -> {"A": metric, "B": metric}.
See skills/case-readiness/scripts/example_sensitivity_model.py for the worked
reference this file follows.

The case's primary metric is total regional jobs supported (direct + indirect,
solved via x = (I-A)^-1 d) per $10,000 of incentive spent. Higher is better.

Verified against case.json.balance / FACILITATOR.md's facilitator-only
arithmetic note:
    base  A = 4.5624  ·  B = 3.9572  ·  margin ~13.27%  (matches case.json margin_pct 13.3)
"""

PARAMS = {
    # --- Appendix E, MA1: Calder County's regional technical coefficient matrix A
    "a11": 0.20,   # Sector 1 (Mfg) buying from Sector 1
    "a12": 0.05,   # Sector 1 buying from Sector 2
    "a21": 0.08,   # Sector 2 (Trade/Trans/Whse) buying from Sector 1
    "a22": 0.10,   # Sector 2 buying from Sector 2
    # --- Appendix E, MA2: flat incentive rate, $ per net new direct job
    "rate_per_job": 3000.0,
    # --- Appendix E, MA3: each employer's direct-jobs headcount
    "jobs_A": 140.0,   # Meridian Forgeworks (The Anvil Bid)
    "jobs_B": 310.0,   # Cascade Distribution (The Waypoint Bid)
}

# All three of the case's stated assumptions (MA1-MA3) carry needs_source status
# "ASSUMPTION" (not sourced) -- SPEC #2 asks for sensitivity to stated
# assumptions, and all three are exactly that, not cited measurements. Cited
# real-world data (the BEA RIMS II calibration examples, the Florida QTI rate
# used as MA2's real-world anchor) is stress-tested by P6 instead, not swept
# here.
FLEX = [
    "a11", "a12", "a21", "a22",   # MA1
    "rate_per_job",               # MA2
    "jobs_A", "jobs_B",           # MA3
]


def _solve(p, d1, d2):
    """Solve x = (I - A)^-1 d for a 2x2 system, by hand (Cramer's rule)."""
    a11, a12, a21, a22 = p["a11"], p["a12"], p["a21"], p["a22"]
    m11, m12 = 1.0 - a11, -a12
    m21, m22 = -a21, 1.0 - a22
    det = m11 * m22 - m12 * m21
    if det == 0:
        return None
    inv11, inv12 = m22 / det, -m12 / det
    inv21, inv22 = -m21 / det, m11 / det
    x1 = inv11 * d1 + inv12 * d2
    x2 = inv21 * d1 + inv22 * d2
    return x1, x2


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})

    xa = _solve(p, p["jobs_A"], 0.0)
    xb = _solve(p, 0.0, p["jobs_B"])
    if xa is None or xb is None:
        # (I - A) singular -- the system has no solution at this flex point.
        return {"A": float("-inf"), "B": float("-inf")}

    total_a = sum(xa)
    total_b = sum(xb)
    incentive_a = p["jobs_A"] * p["rate_per_job"]
    incentive_b = p["jobs_B"] * p["rate_per_job"]

    metric_a = total_a / (incentive_a / 10000.0) if incentive_a else float("-inf")
    metric_b = total_b / (incentive_b / 10000.0) if incentive_b else float("-inf")
    return {"A": metric_a, "B": metric_b}


if __name__ == '__main__':
    base = evaluate({})
    margin = 100 * (base["A"] - base["B"]) / base["B"] if base["B"] else float("nan")
    print("base ", {k: round(v, 4) for k, v in base.items()}, "margin %.2f%%" % margin)
