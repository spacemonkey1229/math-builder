#!/usr/bin/env python3
"""
Sensitivity model — Conjunction Call.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. Contract per
skills/case-readiness/scripts/example_sensitivity_model.py:

    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     same shape, with the twist applied

The case's real decision is a feasibility check, not a smooth ratio: Option B
(Fly The Season) is only genuinely available if the propellant required for
this season's real threshold-crossing maneuvers fits inside what's left after
reserving the mandatory disposal minimum. So the metric returned for B is the
season's stated data-collection value (45 days) if that check passes, and a
value below Option A's certain-but-empty outcome (0) if it does not -- a real
flip, not a smoothly degrading number, which matches how the case's own
Twist is built to work.

isp_s (S3, cited) and g0 (a physical constant) are NOT in FLEX -- SPEC Section 2
asks for sensitivity to STATED ASSUMPTIONS, not cited measurements or physical
constants. Cited data is stress-tested by the data-decay probe (P6) instead.
"""

PARAMS = {
    # --- Appendix D, cited (S3) -- NOT flexed ---------------------------------
    "isp_s": 2150.0,
    "g0": 9.80665,
    # --- Appendix D / Appendix E, stated assumptions --------------------------
    "wet_mass_kg": 12.0,             # MA3
    "reserve_propellant_kg": 0.024,  # MA4 -- the single most load-bearing dial
    "disposal_reserve_kg": 0.0100,   # MA5
    # --- Appendix C, MA2 -- total delta-v of the events that cross the real
    #     threshold (E2 3.5 + E4 6.0 + E5 7.0 + E6 4.5 = 21.0 m/s) ------------
    "total_maneuver_dv_ms": 21.0,
    # --- the Twist (FACILITATOR.md): a 7th event's delta-v, added on top -----
    "twist_dv_ms": 5.5,
    # --- season length, stated in Background/Overview -------------------------
    "season_days": 45.0,
}

# Probe 5 flexes THESE and only these -- the case's real stated assumptions.
# isp_s and g0 are excluded: one is a cited manufacturer spec, the other is a
# physical constant, neither is a scenario dial the case author chose.
FLEX = [
    "wet_mass_kg",              # MA3
    "reserve_propellant_kg",    # MA4
    "disposal_reserve_kg",      # MA5
    "total_maneuver_dv_ms",     # MA2 (aggregate of the 4 maneuvering events)
]


def _kg_per_ms(p):
    v_e = p["isp_s"] * p["g0"]
    return p["wet_mass_kg"] / v_e


def _feasible(p, extra_dv=0.0):
    required = (p["total_maneuver_dv_ms"] + extra_dv) * _kg_per_ms(p)
    available = p["reserve_propellant_kg"] - p["disposal_reserve_kg"]
    return available - required   # >= 0 means feasible


def evaluate(params):
    p = dict(PARAMS); p.update(params or {})
    leftover = _feasible(p)
    a = 0.0  # De-Orbit Now: certain, zero additional data days, zero fuel risk
    b = p["season_days"] if leftover >= 0 else -1.0  # infeasible is worse than A
    return {"A": a, "B": b, "_leftover_kg": leftover}


def evaluate_twist(params):
    p = dict(PARAMS); p.update(params or {})
    leftover = _feasible(p, extra_dv=p["twist_dv_ms"])
    a = 0.0
    b = p["season_days"] if leftover >= 0 else -1.0
    return {"A": a, "B": b, "_leftover_kg": leftover}


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})
    print("base ", {k: (round(v, 6) if isinstance(v, float) else v) for k, v in base.items()})
    print("twist", {k: (round(v, 6) if isinstance(v, float) else v) for k, v in tw.items()})
