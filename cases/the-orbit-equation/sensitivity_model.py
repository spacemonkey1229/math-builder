#!/usr/bin/env python3
"""
Sensitivity model -- The Orbit Equation.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset that is an ASSUMPTION
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     same shape, with the twist applied

Metric: average percent-of-frame the boss occupies, per millisecond of
per-frame camera-path computation. A = The Fixed-Radius Orbit,
B = The Variable-Radius Push-In.

FLEX scoping: the 8 sampled orbit angles (0,45,...,315 degrees) are the
case's own fixed sampling convention, not an assumption -- not flexed.
MA1 (clipping radius) gates a pass/fail wall-clearance CHECK, not this
continuous ratio metric -- evaluate()'s dict does not depend on it at all,
so sweeping it here would be a silent no-op on the metric; it is reported
separately via clip_clearance()/CAVEAT in __main__ instead, the same
treatment case-readiness/SKILL.md prescribes for a metric-vs-constraint
mismatch. MA2 (framing constant k) multiplies both rigs' frame
percentages by the same factor and is included in FLEX to let the sweep
itself demonstrate the invariance (see docstring note in __main__), not
because it is expected to move the margin.
"""

import math

PARAMS = {
    # --- Appendix B: governing equations -------------------------------
    "r_A": 18.0,                 # game-units, constant radius, Option A
    "r0_B": 18.0,                # game-units, base radius, Option B
    "amplitude_B": 6.0,          # game-units, push-in amplitude (Appendix E, MA6)
    # --- Appendix C: arena constraint (NOT in FLEX -- see docstring) ---
    "clip_radius": 8.5,          # game-units (Appendix E, MA1)
    # --- Appendix D: framing + cost -------------------------------------
    "framing_k": 300.0,          # Appendix E, MA2
    "cost_A": 0.020,             # ms/frame (Appendix E, MA3)
    "cost_B": 0.022,             # ms/frame (Appendix E, MA4)
}

FLEX = [
    "cost_A",        # MA3
    "cost_B",        # MA4
    "amplitude_B",   # MA6 -- the Twist is exactly this dial's +50% flex
    "framing_k",     # MA2 -- included to demonstrate the invariance, see __main__
]

ANGLES_DEG = [0, 45, 90, 135, 180, 225, 270, 315]


def _r_B(theta_deg, r0, a):
    return r0 - a * math.cos(math.radians(theta_deg))


def _avg_frame_pct(k, r_values):
    return sum(k / r for r in r_values) / len(r_values)


def _diagnostics(params=None):
    """Full diagnostic dict (frame percentages, min radius, clip clearance) --
    NOT the Tier-2 probe 5 contract shape. tier2_probes.py's probe_sensitivity
    does `min(base, key=base.get)` / `max(base, key=base.get)` over EVERY key
    evaluate() returns, on the assumption the dict is exactly {"A", "B"} --
    an extra diagnostic key (e.g. clip_clearance_B, which is numerically
    smaller than either metric) would get silently picked up as a fake
    'option' and produce nonsense margins. evaluate()/evaluate_twist() below
    therefore return ONLY {"A", "B"}, per the case-readiness contract; use
    this function (or the CLI output below) for the extra diagnostics."""
    p = dict(PARAMS)
    p.update(params or {})
    frame_A = p["framing_k"] / p["r_A"]  # constant at every angle
    r_B_values = [_r_B(t, p["r0_B"], p["amplitude_B"]) for t in ANGLES_DEG]
    frame_B = _avg_frame_pct(p["framing_k"], r_B_values)
    a_metric = frame_A / p["cost_A"]
    b_metric = frame_B / p["cost_B"]
    min_r_B = min(r_B_values)
    return {
        "A": a_metric, "B": b_metric,
        "frame_pct_A": frame_A, "frame_pct_B": frame_B,
        "min_r_B": min_r_B, "clip_clearance_B": min_r_B - p["clip_radius"],
    }


def evaluate(params=None):
    d = _diagnostics(params)
    return {"A": d["A"], "B": d["B"]}


def evaluate_twist(params=None):
    """The animation team widens the push-in for more drama: amplitude_B
    goes from 6 to 9 game-units (a +50% flex of MA6). No other parameter
    changes -- cost_B stays the same because the governing equation's
    complexity (one extra cosine + subtraction) is unchanged by the
    amplitude value."""
    p = dict(PARAMS)
    p.update(params or {})
    p["amplitude_B"] = 9.0
    return evaluate(p)


if __name__ == "__main__":
    base = _diagnostics()
    tw = _diagnostics({"amplitude_B": 9.0})

    def margin(m):
        lo, hi = min(m["A"], m["B"]), max(m["A"], m["B"])
        winner = "A" if m["A"] > m["B"] else ("B" if m["B"] > m["A"] else "TIE")
        return winner, 100.0 * (hi - lo) / lo

    w, m = margin(base)
    print("BASE ", {k: round(v, 3) for k, v in base.items()}, "winner", w, "margin %.2f%%" % m)
    w2, m2 = margin(tw)
    print("TWIST", {k: round(v, 3) for k, v in tw.items()}, "winner", w2, "margin %.2f%%" % m2)

    print("\n--- FLEX +-50% sweep ---")
    base_winner = margin(base)[0]
    for name in FLEX:
        for factor, label in ((1.5, "+50%"), (0.5, "-50%")):
            p = dict(PARAMS)
            p[name] = p[name] * factor
            r = evaluate(p)
            w3, m3 = margin(r)
            flip = " <-- FLIP" if w3 != base_winner else ""
            breach = " <-- CAP BREACH (>20%)" if m3 > 20.0 else ""
            print(f"{name:14s} {label:5s} winner={w3} margin={m3:7.2f}%{flip}{breach}")

    print("\n--- MA1 clipping-radius CAVEAT (not a continuous-metric FLEX; see docstring) ---")
    for factor, label in ((1.5, "+50%"), (0.5, "-50%")):
        clip = PARAMS["clip_radius"] * factor
        clears_base = base["min_r_B"] - clip
        print(f"clip_radius {label:5s} -> {clip:.2f}  base-case clearance = {clears_base:+.2f} "
              f"({'CLEARS' if clears_base > 0 else 'FAILS CLIPPING CHECK'})")

    print("\n--- framing_k invariance check ---")
    p = dict(PARAMS); p["framing_k"] = PARAMS["framing_k"] * 1.5
    r = evaluate(p)
    print("base margin: %.4f%%   +50%% framing_k margin: %.4f%%  (should match)" %
          (margin(base)[1], margin(r)[1]))
