#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Pier Wheel.

Reference contract: skills/case-readiness/scripts/example_sensitivity_model.py.

Both options share the same real, sourced rotation period (30 min, Appendix A/B, S1/S5) and the
same functional form h(t) = D - R*cos(w*t), D = R + boarding_clearance_m, w = 2*pi/period_min.
R (radius = diameter/2) is a real, cited figure for each option (S2, S4) and is NOT flexed here --
cited measurements are stress-tested by the data-decay probe (P6), not the sensitivity probe (P5),
same convention cases/cold-chain and cases/tide-window's own models use for their cited figures.

evaluate() returns each option's PRIMARY METRIC score: qualifying sunset-view minutes delivered
per operating hour, per meter of wheel diameter (case.json.balance.margin_basis). Higher wins.

FLEX = the case's two stated Modeling Assumptions (Appendix E): the qualifying sightline height
(MA1, load-bearing) and the boarding-platform clearance (MA2, applied identically to both options,
low sensitivity by construction).

Verified against cases/pier-wheel/case.json.balance and FACILITATOR.md:
    base   A ~= 0.21197 qualifying-min/hr/m   B ~= 0.19696 qualifying-min/hr/m
           margin_pct = 100*(A-B)/A ~= 7.08%  (matches case.json.margin_pct)
    raw (non-primary, context only) qualifying min/hr:  A ~= 25.44   B ~= 31.22  (B +18.5%)
"""
import math

PARAMS = {
    # --- Appendix A, S1/S2: real, cited (not flexed) -------------------------
    "diameter_A_m": 120.0,
    "period_A_min": 30.0,
    # --- Appendix B, S4/S5: real, cited (not flexed) --------------------------
    "diameter_B_m": 158.5,
    "period_B_min": 30.0,
    # --- Appendix E, MA1: the load-bearing stated assumption -----------------
    "qualifying_height_m": 76.2,
    # --- Appendix E, MA2: applied identically to both options ----------------
    "boarding_clearance_m": 2.0,
}

# Probe 5 flexes exactly the case's own stated Modeling Assumptions (Appendix E), per SPEC
# section 2 -- not the cited diameters/periods, which are real measurements, not authored
# scenario magnitudes.
FLEX = ["qualifying_height_m", "boarding_clearance_m"]


def _dwell_minutes(radius_m, period_min, boarding_clearance_m, qualifying_height_m):
    """Minutes within one rotation that h(t) = D - R*cos(wt) is >= qualifying_height_m."""
    D = radius_m + boarding_clearance_m
    w = 2 * math.pi / period_min
    rhs = (D - qualifying_height_m) / radius_m
    rhs = max(-1.0, min(1.0, rhs))          # clamp: always-above or never-above cases
    ang = math.acos(rhs)                    # principal value in [0, pi]
    t1 = ang / w
    t2 = (2 * math.pi - ang) / w
    return max(0.0, t2 - t1)


def _score(diameter_m, period_min, p):
    radius_m = diameter_m / 2.0
    dwell = _dwell_minutes(radius_m, period_min, p["boarding_clearance_m"], p["qualifying_height_m"])
    rotations_per_hr = 60.0 / period_min
    qualifying_min_per_hr = dwell * rotations_per_hr
    per_meter = qualifying_min_per_hr / diameter_m
    return qualifying_min_per_hr, per_meter


def evaluate(params=None):
    """Returns the PRIMARY METRIC: qualifying min/hr per meter of diameter. Higher wins."""
    p = dict(PARAMS); p.update(params or {})
    _, per_m_a = _score(p["diameter_A_m"], p["period_A_min"], p)
    _, per_m_b = _score(p["diameter_B_m"], p["period_B_min"], p)
    return {"A": per_m_a, "B": per_m_b}


def evaluate_twist(params=None):
    """No twist authored for this case (FACILITATOR.md: Twist N/A, justified).
    Returns the same primary metric unperturbed, for interface parity."""
    return evaluate(params)


def raw_minutes(params=None):
    """CONTEXT metric (not graded): raw qualifying minutes/hour, unweighted by diameter.
    This is the number the case's own trap expects a Hero to stop at (FACILITATOR.md)."""
    p = dict(PARAMS); p.update(params or {})
    raw_a, _ = _score(p["diameter_A_m"], p["period_A_min"], p)
    raw_b, _ = _score(p["diameter_B_m"], p["period_B_min"], p)
    return {"A": raw_a, "B": raw_b}


if __name__ == '__main__':
    base = evaluate()
    print("primary metric (qualifying min/hr per meter of diameter):",
          {k: round(v, 5) for k, v in base.items()},
          "margin A-over-B %.2f%%" % (100 * (base["A"] - base["B"]) / base["A"]))
    raw = raw_minutes()
    print("context: raw qualifying min/hr:", {k: round(v, 2) for k, v in raw.items()},
          "B-over-A %.2f%%" % (100 * (raw["B"] - raw["A"]) / raw["B"]))

    # find the qualifying_height_m that flips the primary metric's winner
    lo, hi = 30.0, 130.0
    for _ in range(60):
        mid = (lo + hi) / 2
        r = evaluate({"qualifying_height_m": mid})
        if r["A"] > r["B"]:
            lo = mid
        else:
            hi = mid
    print("qualifying_height_m that flips the winner: ~%.2f m (base case uses 76.2 m)" % lo)
