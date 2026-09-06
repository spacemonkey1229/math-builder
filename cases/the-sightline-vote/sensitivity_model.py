#!/usr/bin/env python3
"""
Sensitivity model -- The Sightline Vote.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     optional; same shape, with the twist applied

evaluate() computes the case's graded primary metric -- sightline safety score
per dollar of construction cost -- for each option.

Safety score = sin(intersection angle in degrees), the acute angle each design
produces (Appendix B, MA3): Option A is a full 90-degree perpendicular
crossing (score 1.0, the maximum); Option B's connector lane is parallel to
the platted 1880s lot line, so by the Corresponding Angles relationship it
meets Kellner Avenue at the SAME 75-degree angle the lot line does (Appendix
A/D4) -- this is real, derived geometry, not an assumption, and is NOT swept
by this probe.

Total cost = MA1 (shared base reconstruction, identical for both options) +
MA2 (land acquisition, Option A only) + each option's own curb-and-gutter
footage at the sourced $21/ft rate (S3). MA1 and MA2 are the case's two
stated Modeling Assumptions (Appendix D) and are the only entries in FLEX[]
per the "Only FLEX[] is swept" rule -- the angle values, the curb footage,
and the $21/ft rate are given/cited/derived data, not assumptions the case
author chose freely.

Because higher safety-score-per-dollar is the better outcome and the
convention here is already "higher is better" (unlike roofline-call's
board-feet metric, which needed negating), evaluate() returns the score
directly.

Verified against case.json's `derived` block:
    base: A = 2.0581e-6  B = 2.3579e-6   margin 14.56% (B wins)
"""
import math

PARAMS = {
    # --- Appendix A: Dana's own stated site design, not an assumption --------
    "current_acute_deg": 50.0,
    "lot_line_angle_deg": 75.0,        # given angle for D4's parallel/transversal calc
    "optionA_angle_deg": 90.0,         # The Squared Corner: full perpendicular realignment
    "curb_ramp_given_deg": 35.0,       # ADA ramp angle to Kellner Ave curb, Option A NE corner
    "curb_a_ft": 280.0,                # Option A's own new curb-and-gutter footage
    "curb_b_ft": 460.0,                # Option B's own new curb-and-gutter footage
    # --- Appendix C / Appendix E: sourced (S3) --------------------------------
    "curb_rate_usd_per_ft": 21.0,
    # --- Appendix D: stated modeling assumptions (MA1 / MA2) ------------------
    "base_cost_usd": 400000.0,
    "land_cost_usd": 80000.0,
    # --- Twist-only parameter (Facilitator use; not in case.md) ---------------
    "grant_share": 0.60,               # HSIP-style grant reimburses this share of cost
    "grant_min_angle_deg": 85.0,       # ...but only for a design reaching this angle or more
}

# Only the two stated assumptions are swept by Probe 5. The site geometry,
# curb footage, and sourced construction rate above are given/derived/cited
# data, not assumptions the case author chose -- per the "Only FLEX[] is
# swept" rule (case-readiness SKILL.md, Tier 2 P5).
FLEX = [
    "base_cost_usd",   # Appendix D, MA1
    "land_cost_usd",   # Appendix D, MA2
]


def _optionB_angle_deg(p):
    """Option B's connector lane is parallel to the platted lot line, so by
    the Corresponding Angles relationship it crosses the transversal
    (Kellner Avenue) at the same angle the lot line does. Real geometry, not
    an assumption -- never in FLEX[]."""
    return p["lot_line_angle_deg"]


def _costs(p):
    total_a = p["base_cost_usd"] + p["land_cost_usd"] + p["curb_a_ft"] * p["curb_rate_usd_per_ft"]
    total_b = p["base_cost_usd"] + 0.0 + p["curb_b_ft"] * p["curb_rate_usd_per_ft"]
    return total_a, total_b


def evaluate(params=None):
    """Graded primary metric: sightline safety score per dollar (higher = better)."""
    p = dict(PARAMS); p.update(params or {})
    sin_a = math.sin(math.radians(p["optionA_angle_deg"]))
    sin_b = math.sin(math.radians(_optionB_angle_deg(p)))
    total_a, total_b = _costs(p)
    return {"A": sin_a / total_a, "B": sin_b / total_b}


def evaluate_twist(params=None):
    """Twist (Facilitator-only, not in case.md): a state HSIP-style safety
    grant reimburses `grant_share` of construction cost, but only for a
    design that reaches at least `grant_min_angle_deg`. Option A (90 deg)
    qualifies; Option B (75 deg) does not. Recomputes safety-score-per-NET-
    dollar after the grant."""
    p = dict(PARAMS); p.update(params or {})
    sin_a = math.sin(math.radians(p["optionA_angle_deg"]))
    sin_b = math.sin(math.radians(_optionB_angle_deg(p)))
    total_a, total_b = _costs(p)
    net_a = total_a * (1.0 - p["grant_share"]) if p["optionA_angle_deg"] >= p["grant_min_angle_deg"] else total_a
    net_b = total_b * (1.0 - p["grant_share"]) if _optionB_angle_deg(p) >= p["grant_min_angle_deg"] else total_b
    return {"A": sin_a / net_a, "B": sin_b / net_b}


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})

    def _report(d, label):
        lo, hi = min(d, key=d.get), max(d, key=d.get)
        margin = 100 * (d[hi] - d[lo]) / d[lo] if d[lo] else float('nan')
        print(f"{label:6s} A={d['A']:.6e}  B={d['B']:.6e}  winner={hi}  margin={margin:.2f}%")

    _report(base, "base")
    _report(tw, "twist")

    print("\n-- Probe 5 manual flex check (each assumption alone, +/-50%) --")
    for key in FLEX:
        for mult in (0.5, 1.5):
            flexed = dict(PARAMS)
            flexed[key] = PARAMS[key] * mult
            d = evaluate(flexed)
            lo, hi = min(d, key=d.get), max(d, key=d.get)
            margin = 100 * (d[hi] - d[lo]) / d[lo] if d[lo] else float('nan')
            print(f"  {key} x{mult}: winner={hi} margin={margin:.2f}%")
