#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- The Course Correction.

Tier 2 probe 5 ("flex each stated assumption by +-50%; report which flips
the verdict") needs a runnable model of the case's own arithmetic.

CONTRACT -- two public names:

    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

The case's SPEC Section 2 primary metric (case.json.balance.margin_basis) is
fuel cost (USD) per nautical mile of NET PROGRESS toward the rendezvous
point (NDBC Buoy 44090). That is a COST -- lower is better -- but the
probe's contract is "higher is better", so evaluate() returns the NEGATIVE
of the cost.

Mechanism modeled explicitly (this is the whole point of the case):
Option A (The True Line) steers a heading found by vector SUBTRACTION
(Heading = DesiredResultant - Current) so the resultant velocity lands
exactly on the course line -- net progress rate equals the full resultant
magnitude, no wasted distance, but the required boat speed through the
water is a little above the ship's economical throttle, so fuel burn/hr
is interpolated from Appendix C's real speed/fuel table (MA3).
Option B (The Steady Burn) holds the uncorrected heading at the ship's
economical throttle; the resultant velocity (heading + current, added by
vector ADDITION) drifts off the course line. Net progress is found by a
DOT PRODUCT of the resultant against the course unit vector (along-track
component); the perpendicular (cross-track) component accumulates a real
offset that must be closed with an extra correction leg (MA4), lengthening
the real distance sailed for the same net progress.

FLEX[] sweeps the case's own stated Modeling Assumptions: MA1 (distance/
course), MA2 (weather-window hours -- feeds Option A's required
speed-over-ground), and the fuel-consumption interpolation is re-derived
every call from PARAMS, not swept separately (see MA3 note below).
"""

import math

GAL_PER_KT_KTS = 51.4444  # cm/s per knot, i.e. 1 kt = 51.4444 cm/s

PARAMS = {
    # --- Appendix A / MA1: rendezvous geometry ---------------------------
    "distance_nm": 27.0,
    "course_deg": 250.0,
    # --- Appendix A / MA2: weather window ---------------------------------
    "window_hr": 3.0,
    # --- Appendix B: measured current at NDBC 44090 (S1) -------------------
    "current_speed_cm_s": 27.0,
    "current_toward_deg": 340.0,
    # --- Appendix C: Coastal Aster speed/fuel curve (S2, R/V-class data) --
    "boat_speed_b_kt": 8.5,       # economical throttle, Option B
    "fuel_pt_lo_kt": 8.5, "fuel_pt_lo_gph": 19.0,
    "fuel_pt_mid_kt": 9.5, "fuel_pt_mid_gph": 32.0,
    "fuel_pt_hi_kt": 11.5, "fuel_pt_hi_gph": 60.0,
    # --- Appendix D: diesel price (S3) --------------------------------------
    "price_per_gal": 5.599,
}

# Probe 5 flexes THESE and only these: the case's own stated Modeling
# Assumptions that feed the graded primary metric's arithmetic. MA3
# (interpolation method) and MA4 (final-leg simplification) are structural
# modeling choices, not continuously-flexible numbers, so they are not
# swept the same way -- MA3's effect is exercised automatically any time
# distance_nm/window_hr changes the required boat speed, and MA4 is
# discussed qualitatively in RESEARCH_LOG.md.
FLEX = [
    "distance_nm",   # MA1
    "course_deg",    # MA1
    "window_hr",     # MA2
]


def _vec(mag, deg):
    r = math.radians(deg)
    return mag * math.sin(r), mag * math.cos(r)


def _dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def _interp_fuel_gph(v_kt, p):
    pts = sorted([
        (p["fuel_pt_lo_kt"], p["fuel_pt_lo_gph"]),
        (p["fuel_pt_mid_kt"], p["fuel_pt_mid_gph"]),
        (p["fuel_pt_hi_kt"], p["fuel_pt_hi_gph"]),
    ])
    if v_kt <= pts[0][0]:
        (v1, f1), (v2, f2) = pts[0], pts[1]
    elif v_kt >= pts[-1][0]:
        (v1, f1), (v2, f2) = pts[-2], pts[-1]
    else:
        v1 = f1 = v2 = f2 = None
        for i in range(len(pts) - 1):
            if pts[i][0] <= v_kt <= pts[i + 1][0]:
                (v1, f1), (v2, f2) = pts[i], pts[i + 1]
                break
    slope = (f2 - f1) / (v2 - v1)
    return f1 + slope * (v_kt - v1)


def evaluate_detail(params):
    p = dict(PARAMS)
    p.update(params or {})

    D = p["distance_nm"]
    theta = p["course_deg"]
    T_window = p["window_hr"]
    Vc = p["current_speed_cm_s"] / GAL_PER_KT_KTS
    current_vec = _vec(Vc, p["current_toward_deg"])
    u = _vec(1.0, theta)
    u_perp = (math.cos(math.radians(theta)), -math.sin(math.radians(theta)))
    price = p["price_per_gal"]

    # ---- Option A: The True Line (corrected heading) ----------------------
    R_required = D / T_window
    Ru = (R_required * u[0], R_required * u[1])
    H = (Ru[0] - current_vec[0], Ru[1] - current_vec[1])
    boat_speed_a = math.hypot(H[0], H[1])
    fuel_rate_a = _interp_fuel_gph(boat_speed_a, p)
    time_a = D / R_required
    fuel_a = fuel_rate_a * time_a
    cost_a = fuel_a * price
    metric_a = cost_a / D
    meets_window_a = time_a <= T_window

    # ---- Option B: The Steady Burn (uncorrected heading) -------------------
    boat_speed_b = p["boat_speed_b_kt"]
    heading_vec_b = _vec(boat_speed_b, theta)
    resultant_b = (heading_vec_b[0] + current_vec[0], heading_vec_b[1] + current_vec[1])
    along_b = _dot(resultant_b, u)
    cross_b = _dot(resultant_b, u_perp)
    t1 = D / along_b
    cross_offset = cross_b * t1
    extra_leg = abs(cross_offset)
    t_extra = extra_leg / boat_speed_b
    total_time_b = t1 + t_extra
    engine_distance_b = boat_speed_b * total_time_b
    fuel_rate_b = p["fuel_pt_lo_gph"]  # economical throttle -- lowest published point
    fuel_b = fuel_rate_b * total_time_b
    cost_b = fuel_b * price
    metric_b = cost_b / D
    meets_window_b = total_time_b <= T_window

    detail_a = {
        "boat_speed_kt": boat_speed_a, "fuel_rate_gph": fuel_rate_a,
        "time_hr": time_a, "fuel_gal": fuel_a, "cost_usd": cost_a,
        "metric_usd_per_nm": metric_a, "meets_window": meets_window_a,
    }
    detail_b = {
        "boat_speed_kt": boat_speed_b, "fuel_rate_gph": fuel_rate_b,
        "resultant_speed_kt": math.hypot(*resultant_b), "along_track_kt": along_b,
        "cross_track_kt": cross_b, "t1_hr": t1, "cross_offset_nm": cross_offset,
        "t_extra_hr": t_extra, "time_hr": total_time_b,
        "engine_distance_nm": engine_distance_b, "fuel_gal": fuel_b,
        "cost_usd": cost_b, "metric_usd_per_nm": metric_b, "meets_window": meets_window_b,
    }
    # Lower cost/nm is better; evaluate()'s contract is "higher is better",
    # so return the NEGATIVE of the cost/nm.
    return {"A": -metric_a, "B": -metric_b}, detail_a, detail_b


def evaluate(params):
    """Tier 2 probe 5 contract: evaluate(params) -> {'A': metric, 'B': metric}
    ONLY -- full diagnostics (per-option breakdown) are in evaluate_detail()."""
    r, _a, _b = evaluate_detail(params)
    return r


if __name__ == '__main__':
    base, a, b = evaluate_detail({})
    win = max(base, key=base.get)
    lo = min(base, key=base.get)
    win_cost, lo_cost = -base[win], -base[lo]
    margin = 100.0 * (lo_cost - win_cost) / lo_cost
    print("Option A (The True Line):")
    for k, v in a.items():
        print(f"  {k}: {v}")
    print("Option B (The Steady Burn):")
    for k, v in b.items():
        print(f"  {k}: {v}")
    print()
    print("cost/nm  A=%.4f  B=%.4f" % (-base["A"], -base["B"]))
    print("winner (cheaper $/nm):", win, " margin: %.2f%%" % margin)

    print("\n--- FLEX sweep (+-50% one at a time) ---")
    for key in FLEX:
        base_val = PARAMS[key]
        for pct in (-0.5, -0.25, 0.25, 0.5):
            trial = dict(PARAMS)
            trial[key] = base_val * (1 + pct) if key != "course_deg" else base_val + pct * 90.0
            r, da, db = evaluate_detail(trial)
            w = max(r, key=r.get)
            l_ = min(r, key=r.get)
            m = 100.0 * (-r[l_] - (-r[w])) / (-r[l_]) if -r[l_] != 0 else float('nan')
            flag = "" if w == win else "  <-- WINNER FLIPS"
            print(f"  {key} {pct:+.0%} (-> {trial[key]:.3f}): winner={w} margin={m:.2f}%{flag}")
