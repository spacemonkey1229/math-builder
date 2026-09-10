#!/usr/bin/env python3
"""
sensitivity_model.py — Fizzer Order

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):

    PARAMS                          dict[str, number]  every dial the case states
    FLEX                            list[str]          subset Tier 2 probe 5 perturbs +/-50%
    evaluate(params) -> dict        {"A": metric, "B": metric}   LOWER is better here
    evaluate_twist(params) -> dict  same shape (no twist authored for this case; identity)

Metric: dollars per Mini Fizzer actually delivered. Unlike the Cold Chain reference model
(higher is better), THIS case's primary metric is a cost — lower is better, and the case
explicitly reports Option B (Twist Cone) as the winner (case.json.margin_pct = 8.96, B wins).
Tier 2 probe 5 / any caller of this module should compare on that basis: min(A, B) wins.

Verified against cases/fizzer-order/case.md Appendices B-D and FACILITATOR.md:
    base    A = $0.0026116/fizzer   B = $0.0023775/fizzer   margin 8.96%   (matches case.json)
"""
import math

PARAMS = {
    # --- Appendix C, Box Options: Engineering Spec Sheet --------------------
    "peak_base_side_in": 2.60,
    "peak_height_in": 3.50,
    "cone_radius_in": 1.60,
    "cone_height_in": 3.30,
    # --- Appendix B, Mini Fizzer spec ----------------------------------------
    "fizzer_diameter_in": 1.00,
    # --- Appendix C, loose-fill packing figure [S3] --------------------------
    "packing_fraction": 0.64,
    # --- Appendix D, material cost reference [S1] ----------------------------
    "price_per_sqin": 0.00089797,
    # --- Appendix F, shipping carton reference [S4] (used only by D5 helper) -
    "carton_side_in": 12.0,
}

# Probe 5 flexes THESE and only these. FIXED 2026-09-09 (case-readiness Tier 2 P5
# remediation): the box dimensions were previously included here too, on the
# theory that they're "Priya's own team's engineering choice, not a physical
# constant." That reasoning doesn't hold up against SPEC's own FLEX-scoping
# doctrine (skills/case-readiness/SKILL.md, "FLEX[] scoping is the model
# author's responsibility") — Appendix C's dimensions are presented as fixed
# GIVEN engineering-spec data (a concrete table, no hedge language), and
# Appendix E's Modeling Assumptions table is this case's own authoritative
# list of the assumptions "a Hero may challenge in discussion." Only MA1 (the
# 64% loose-packing figure applied identically to both shapes) is on that
# list, and only MA1's row says the D4 margin is sensitive to it. Flexing the
# box dimensions was a scoping error that manufactured false instability
# findings (peak_base_side_in/peak_height_in/cone_radius_in/cone_height_in all
# "flipped" the winner at +/-50%, which is not a real modeling-assumption
# fragility — it's just "a different box would be a different case"). FLEX now
# contains only the one real, case-stated assumption.
FLEX = [
    "packing_fraction",
]


def _pyramid_sa_vol(base_side, height):
    base_area = base_side ** 2
    slant = math.sqrt(height ** 2 + (base_side / 2) ** 2)
    lateral = 2 * base_side * slant
    sa = base_area + lateral
    vol = (1 / 3) * base_area * height
    return sa, vol


def _cone_sa_vol(radius, height):
    base_area = math.pi * radius ** 2
    slant = math.sqrt(height ** 2 + radius ** 2)
    lateral = math.pi * radius * slant
    sa = base_area + lateral
    vol = (1 / 3) * base_area * height
    return sa, vol


def _sphere_vol(diameter):
    r = diameter / 2
    return (4 / 3) * math.pi * r ** 3


def _cost_per_fizzer(sa, vol, p):
    v_sphere = _sphere_vol(p["fizzer_diameter_in"])
    usable_vol = vol * p["packing_fraction"]
    n = math.floor(usable_vol / v_sphere)
    if n <= 0:
        return float("inf")
    cost = sa * p["price_per_sqin"]
    return cost / n


def evaluate(params, detour_h=0.0):
    """Returns {"A": $/fizzer for the Peak Box, "B": $/fizzer for the Twist Cone}.
    LOWER wins for both keys — this case's primary metric is a cost, not a benefit.
    `detour_h` is accepted for interface parity with the reference contract; this
    case has no twist that perturbs it, so it is unused."""
    sa_a, vol_a = _pyramid_sa_vol(params["peak_base_side_in"], params["peak_height_in"])
    sa_b, vol_b = _cone_sa_vol(params["cone_radius_in"], params["cone_height_in"])
    return {
        "A": _cost_per_fizzer(sa_a, vol_a, params),
        "B": _cost_per_fizzer(sa_b, vol_b, params),
    }


def evaluate_twist(params):
    """No twist is authored for this case (see FACILITATOR.md — none declared).
    Provided for contract parity; identical to evaluate()."""
    return evaluate(params)


def margin_pct(result):
    a, b = result["A"], result["B"]
    lo, hi = min(a, b), max(a, b)
    if hi == 0 or math.isinf(hi):
        return float("nan")
    return (hi - lo) / hi * 100


if __name__ == "__main__":
    base = evaluate(PARAMS)
    print("base:", base, "margin_pct:", round(margin_pct(base), 2),
          "winner:", "A" if base["A"] < base["B"] else "B")

    print("\n--- Tier 2 probe 5: +/-50% flex on each FLEX dial ---")
    for key in FLEX:
        for pct, label in ((0.5, "+50%"), (-0.5, "-50%")):
            flexed = dict(PARAMS)
            flexed[key] = PARAMS[key] * (1 + pct)
            if key == "packing_fraction":
                flexed[key] = max(0.01, min(1.0, flexed[key]))
            r = evaluate(flexed)
            winner = "A" if r["A"] < r["B"] else "B"
            base_winner = "A" if base["A"] < base["B"] else "B"
            flip = " <-- FLIPS" if winner != base_winner else ""
            print(f"{key:20s} {label:5s} -> A={r['A']:.6f} B={r['B']:.6f} "
                  f"margin={margin_pct(r):5.2f}%  winner={winner}{flip}")

    print("\n--- Asymmetric check: MA1 (uniform packing_fraction) relaxed ---")
    print("    Peak Box held at the sourced 64% figure; only the Twist Cone's")
    print("    packing fraction is lowered, modelling a real taper penalty.")
    sa_a0, vol_a0 = _pyramid_sa_vol(PARAMS["peak_base_side_in"], PARAMS["peak_height_in"])
    sa_b0, vol_b0 = _cone_sa_vol(PARAMS["cone_radius_in"], PARAMS["cone_height_in"])
    p_a_fixed = dict(PARAMS)
    cost_a_fixed = _cost_per_fizzer(sa_a0, vol_a0, p_a_fixed)
    for cone_pack in (0.64, 0.60, 0.55, 0.50, 0.45, 0.40):
        p_b = dict(PARAMS); p_b["packing_fraction"] = cone_pack
        cost_b = _cost_per_fizzer(sa_b0, vol_b0, p_b)
        winner = "A" if cost_a_fixed < cost_b else "B"
        print(f"    cone packing={cone_pack:.2f} -> A={cost_a_fixed:.6f} "
              f"B={cost_b:.6f}  winner={winner}")
