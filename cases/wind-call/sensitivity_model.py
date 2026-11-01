#!/usr/bin/env python3
"""
Sensitivity model — Wind Call.

CONTRACT — exactly two public names used by Tier 2 probe 5:
    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better

No evaluate_twist() — this case has no twist (facilitator.has_twist = false,
FACILITATOR.md's "Twist: N/A" section).

The case's own primary metric (gallons of Jet-A burned per nautical mile) is a
COST metric — lower is better. To match the "higher is better" convention this
script's contract expects, `evaluate()` returns nautical miles flown per gallon
burned (the reciprocal) — a monotonic transform of the same ratio, so the winner
and the relative margin are identical either way, just expressed as efficiency
instead of cost.

Verified against case.json.balance (2026-09-18):
    base   A (Niner-Thousand)     = 366.4 / 120.0 = 3.0533 nm/gal
           B (One-Eight-Thousand) = 366.4 / 119.3 = 3.0713 nm/gal
    winner B, margin_pct = |3.0713-3.0533| / max(...) * 100 = 0.59% ~ case.json's 0.6% (rounding)
"""
import math

DIST_NM = 366.4
COURSE_DEG = 106.0
TAS_KT = 180.0

# Real, live-fetched winds aloft (case.json sources S2) -- NOT in PARAMS/FLEX.
# Per skills/case-readiness/SKILL.md's P5 "FLEX[] scoping" rule: only STATED
# ASSUMPTIONS are swept by probe 5, never cited measurements. This case's own
# case.json.sensitivity_disclosure[] documents the cited wind data's fragility
# separately, precisely because it is real data, not an author's assumption.
WIND_A_FROM_DEG, WIND_A_SPEED_KT, ALT_A_FT = 220.0, 27.0, 9000
WIND_B_FROM_DEG, WIND_B_SPEED_KT, ALT_B_FT = 230.0, 20.0, 18000

PARAMS = {
    # Appendix E, MA1 -- the only stated Modeling Assumption in this case.
    # Held identical across both altitude options (same as Turbine Channel's
    # MA2 conversion factor), so flexing it moves BOTH options' absolute fuel
    # totals together and cannot, by construction, flip which option wins --
    # that is a real, correctly-disclosed finding, not a bug in this model.
    "fuel_gph": 62.0,
}

FLEX = ["fuel_gph"]


def _wind_triangle(course_deg, tas, wind_from_deg, wind_speed):
    wind_to = math.radians((wind_from_deg + 180.0) % 360.0)
    wx = wind_speed * math.sin(wind_to)
    wy = wind_speed * math.cos(wind_to)
    course = math.radians(course_deg)
    cx, cy = math.sin(course), math.cos(course)
    wind_along = wx * cx + wy * cy
    wind_cross = wx * cy - wy * cx
    wca = math.asin(max(-1.0, min(1.0, wind_cross / tas)))
    gs = tas * math.cos(wca) + wind_along
    heading = math.degrees(course - wca) % 360.0
    return {"gs": gs, "heading": heading, "wind_along": wind_along, "wca_deg": math.degrees(wca)}


def _nm_per_gal(params, wind_from_deg, wind_speed):
    r = _wind_triangle(COURSE_DEG, TAS_KT, wind_from_deg, wind_speed)
    time_hr = DIST_NM / r["gs"]
    fuel_gal = time_hr * params["fuel_gph"]
    return DIST_NM / fuel_gal


def evaluate(params):
    return {
        "A": _nm_per_gal(params, WIND_A_FROM_DEG, WIND_A_SPEED_KT),
        "B": _nm_per_gal(params, WIND_B_FROM_DEG, WIND_B_SPEED_KT),
    }


if __name__ == "__main__":
    base = evaluate(PARAMS)
    winner = "A" if base["A"] > base["B"] else ("B" if base["B"] > base["A"] else "TIE")
    lo, hi = min(base.values()), max(base.values())
    margin = 0.0 if hi == 0 else abs(base["A"] - base["B"]) / hi * 100
    print("base", base, "winner", winner, "margin_pct", round(margin, 2))
    for pname in FLEX:
        for mult, label in ((0.5, "-50%"), (1.5, "+50%")):
            p = dict(PARAMS)
            p[pname] = PARAMS[pname] * mult
            r = evaluate(p)
            w = "A" if r["A"] > r["B"] else ("B" if r["B"] > r["A"] else "TIE")
            print(f"  flex {pname} {label}: {r}  winner={w}  (base winner={winner})")
