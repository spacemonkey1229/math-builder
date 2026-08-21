#!/usr/bin/env python3
"""
Sensitivity model — Roofline Call.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     optional; same shape, with the twist applied

evaluate() computes the case's graded primary metric — board-feet of framing
lumber per square foot of enclosed attic space — for each roof option, from the
footprint, pitch, lumber size, and spacing stated in Appendix B (none of which
are modeling assumptions; they are the drafter's own stated design). Because
FEWER board-feet per square foot is the better outcome, evaluate() returns the
*negative* of that figure so the "higher is better" convention still holds:
Option B (fewer board-feet/sq ft) legitimately returns a higher number.

Appendix E's two modeling assumptions (MA1 the simple-cut time, MA2 the
compound-cut multiplier) do NOT enter this calculation at all — the primary
metric is pure geometry. That is itself the Tier 2 probe 5 finding: flexing
MA1/MA2 cannot move the graded verdict, by construction. They matter only to
the case's SUPPLEMENTARY total-cost figure, which is what the Twist reveals.

evaluate_twist() computes that supplementary figure — total cost (material +
labor, using Appendix C's real lumber price and Appendix E's cut-time
assumptions) instead of pure board-feet — because the Twist is literally the
shop's labor ledger landing on Colton's desk after he already committed to the
board-feet answer. The metric changes on purpose: that is the twist's whole
point (see FACILITATOR.md). Same sign convention: lower cost is better, so the
function returns the negative.

Verified against case.json's `derived` block:
    base   A = -1.2023  B = -1.0242   margin  17.39%  (B wins, less lumber)
    twist  A = -956.50  B = -997.02   margin   4.24%  (A wins, less total cost)
"""
import math

PARAMS = {
    # --- Appendix B: the drafter's own stated design, not an assumption ------
    "width_ft": 24.0,
    "length_ft": 52.0,
    "pitch_rise": 6.0,
    "pitch_run": 12.0,
    "spacing_in": 16.0,
    "lumber_bf_factor": 2 * 8 / 12,   # board-feet per linear foot, 2x8 stock
    # --- Appendix C: sourced (S2) ---------------------------------------------
    "price_per_bf_usd": 0.53615,
    # --- Appendix E: stated modeling assumptions (MA1 / MA2) -----------------
    "simple_cut_min": 4.0,
    "compound_mult": 3.0,
    "wage_usd_per_hr": 28.51,        # sourced (S3); not itself flexed
}

# Only the two stated assumptions are swept by Probe 5. The geometry/pricing/
# wage dials above are given/cited data, not assumptions the case author chose
# — per the "Only FLEX[] is swept" rule (case-readiness SKILL.md, Tier 2 P5).
FLEX = [
    "simple_cut_min",     # Appendix E, MA1
    "compound_mult",      # Appendix E, MA2
]


def _geometry(p):
    W, L = p["width_ft"], p["length_ft"]
    run = W / 2.0
    rise = run * (p["pitch_rise"] / p["pitch_run"])
    common_len = math.sqrt(run ** 2 + rise ** 2)
    spacing_ft = p["spacing_in"] / 12.0
    attic_sqft = W * L

    # Gable
    ridge_g = L
    commons_per_side_g = int(ridge_g * 12 / p["spacing_in"]) + 1
    common_total_g = commons_per_side_g * 2 * common_len
    len_total_g = common_total_g + ridge_g  # + ridge board

    # Hip
    ridge_h = L - W
    commons_per_side_h = int(ridge_h * 12 / p["spacing_in"]) + 1
    common_total_h = commons_per_side_h * 2 * common_len
    hip_run = run * math.sqrt(2)
    hip_len = math.sqrt(hip_run ** 2 + rise ** 2)
    hips_total = 4 * hip_len
    unit_len = common_len / run
    decrement = spacing_ft * unit_len
    n_jacks_per_side = int(run * 12 / p["spacing_in"])
    jack_total = decrement * (n_jacks_per_side * (n_jacks_per_side + 1) / 2) * 4
    len_total_h = common_total_h + hips_total + jack_total + ridge_h  # + ridge board

    bf_a = len_total_g * p["lumber_bf_factor"]
    bf_b = len_total_h * p["lumber_bf_factor"]

    return {
        "attic_sqft": attic_sqft,
        "bf_a": bf_a, "bf_b": bf_b,
        "bf_per_sqft_a": bf_a / attic_sqft, "bf_per_sqft_b": bf_b / attic_sqft,
        "commons_per_side_g": commons_per_side_g,
        "commons_per_side_h": commons_per_side_h,
        "n_hip_members": 4,
        "n_jack_members": n_jacks_per_side * 4,
    }


def evaluate(params=None):
    """Graded primary metric: board-feet per sq ft, negated (higher = better)."""
    p = dict(PARAMS); p.update(params or {})
    g = _geometry(p)
    return {"A": -g["bf_per_sqft_a"], "B": -g["bf_per_sqft_b"]}


def evaluate_twist(params=None):
    """Supplementary metric revealed by the Twist: total cost, negated."""
    p = dict(PARAMS); p.update(params or {})
    g = _geometry(p)
    mat_a = g["bf_a"] * p["price_per_bf_usd"]
    mat_b = g["bf_b"] * p["price_per_bf_usd"]
    simple_cost = p["simple_cut_min"] / 60.0 * p["wage_usd_per_hr"]
    compound_cost = simple_cost * p["compound_mult"]
    labor_a = g["commons_per_side_g"] * 2 * simple_cost
    labor_b = (g["commons_per_side_h"] * 2 * simple_cost
               + g["n_hip_members"] * compound_cost
               + g["n_jack_members"] * compound_cost)
    total_a = mat_a + labor_a
    total_b = mat_b + labor_b
    return {"A": -total_a, "B": -total_b}


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})

    def _report(d, label):
        lo, hi = min(d, key=d.get), max(d, key=d.get)
        margin = 100 * (d[hi] - d[lo]) / abs(d[lo]) if d[lo] else float('nan')
        print(f"{label:6s} A={d['A']:.4f}  B={d['B']:.4f}  winner={hi}  margin={margin:.2f}%")

    _report(base, "base")
    _report(tw, "twist")
