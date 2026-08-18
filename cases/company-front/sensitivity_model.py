"""Sensitivity model for Company Front (SPEC section 2 balance test, case-readiness Tier 2 probe 5).

Every dial is disclosed in case.md Appendix B/C/D/E -- no hidden interior/border-style blend
(lesson learned from Plaza Pavers' first draft). PARAMS/FLEX/evaluate()/evaluate_twist() follow
the case-readiness CONTRACT: evaluate(params) -> {"A": metric, "B": metric}, higher wins.

This case's real metric (Option A's required step size, in/step) is LOWER-is-better and compared
against a real ceiling (30 in/step), not directly against Option B (rotating about a compact
formation's own center is structurally always cheaper -- see RESEARCH_LOG.md). The CONTRACT still
needs two comparable "higher is better" values, so both options' values are expressed as ceiling
headroom: value = 30 - required_step_size. Higher headroom = safer = "wins" under the CONTRACT's
own convention, and the case's own real margin_pct (Option A's headroom as % of the 30 in/step
ceiling) is recovered directly from value_A / 30 * 100 -- not a different, silently-diverging
number.
"""
import math

STEP_IN = 22.5          # S2 -- the "8-to-5" comfort standard, also 1 grid-spacing unit's basis
AGGRESSIVE_CEILING_IN = 30.0   # S2 -- the "6-to-5" aggressive ceiling

MARKERS_STEPS = [(x, y) for x in (-4, 0, 4) for y in (-4, 0, 4)]  # Appendix B, authored formation

PARAMS = {
    "grid_spacing_steps": 4.0,          # Appendix B
    "scale_factor": 4.4,                # MA1
    "counts": 16.0,                     # MA2
    "aggressive_ceiling_in": AGGRESSIVE_CEILING_IN,  # S2
}

FLEX = ["scale_factor", "counts"]


def _markers_in(p):
    s = p["grid_spacing_steps"] * STEP_IN
    return [(x / 4.0 * s, y / 4.0 * s) for x, y in MARKERS_STEPS]


def _dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def max_travel_dilation(p):
    S = p["scale_factor"]
    return max(_dist(m, (m[0] * S, m[1] * S)) for m in _markers_in(p))


def max_travel_rotation90(p):
    # (x,y) -> (-y,x), a 90-degree rotation about the formation's own center
    return max(_dist(m, (-m[1], m[0])) for m in _markers_in(p))


def max_travel_rotation180(p):
    return max(_dist(m, (-m[0], -m[1])) for m in _markers_in(p))


def cost_breakdown(p):
    """Real, disclosed step-size figures. D2/D3's actual worked answers."""
    step_a = max_travel_dilation(p) / p["counts"]
    step_b = max_travel_rotation90(p) / p["counts"]
    step_180 = max_travel_rotation180(p) / p["counts"]
    return {"step_a_in": step_a, "step_b_in": step_b, "step_180_in": step_180}


def evaluate(p):
    """CONTRACT: {"A": metric, "B": metric}, higher wins (per example_sensitivity_model.py).

    This case's real dilemma is NOT "A vs B on the same metric" -- rotating a compact formation
    about its own center is structurally always cheaper than a large dilation (see RESEARCH_LOG.md
    and cost_breakdown()'s three real numbers), so a literal A-vs-B comparison would trivially and
    permanently favor B, the same non-comparison Tide Window hit with its clearance-vs-policy-floor
    shape. The real tension is how close Option A's required step size comes to the real 30 in/step
    ceiling -- so, matching Tide Window's resolution, "B" in this CONTRACT-shaped return is the
    ceiling itself, not Option A's Mirror-Turn dilemma-partner (whose own real, separately reported
    number lives in cost_breakdown()['step_b_in'] and is never at risk of exceeding anything).
    Higher wins: if Option A's step size ever exceeds the ceiling, A > B and the generic probe-5
    winner flips from "ceiling holds" to "Option A" -- a correct, meaningful flip for this case,
    not an artifact.
    """
    b = cost_breakdown(p)
    return {"A": b["step_a_in"], "B": p["aggressive_ceiling_in"]}


def evaluate_twist(p):
    """Twist: a late music edit cuts the transition from 16 counts to 14. Only Option A is
    re-evaluated in FACILITATOR.md (Option B has so much headroom the cut doesn't matter), but
    both are returned for the CONTRACT's sake."""
    p2 = dict(p)
    p2["counts"] = 14.0
    return evaluate(p2)


if __name__ == "__main__":
    b = cost_breakdown(PARAMS)
    print(f"Option A (Expand): {b['step_a_in']:.2f} in/step  "
          f"({'CLEARS' if b['step_a_in'] <= AGGRESSIVE_CEILING_IN else 'EXCEEDS'} the {AGGRESSIVE_CEILING_IN}in ceiling)")
    print(f"Option B (Mirror Turn): {b['step_b_in']:.2f} in/step")
    print(f"180-rotation (ruled out): {b['step_180_in']:.2f} in/step")
    headroom_pct = (AGGRESSIVE_CEILING_IN - b['step_a_in']) / AGGRESSIVE_CEILING_IN * 100
    print(f"Option A headroom under aggressive ceiling: {headroom_pct:.2f}%  (this case's margin_pct)")

    ev = evaluate(PARAMS)
    print(f"\nCONTRACT evaluate(): {ev}")
    assert ev["A"] < ev["B"], "Option A's step size should be under the ceiling (B)"
    contract_margin = (ev["B"] - ev["A"]) / ev["B"] * 100
    print(f"CONTRACT-formula margin ((B-A)/B): {contract_margin:.2f}%  (matches headroom_pct above by construction)")

    twist = cost_breakdown({**PARAMS, "counts": 14.0})
    print(f"\nTwist (14 counts): Option A {twist['step_a_in']:.2f} in/step "
          f"({'EXCEEDS' if twist['step_a_in'] > AGGRESSIVE_CEILING_IN else 'still clears'} the ceiling)")

    # sensitivity sweep preview
    for name in FLEX:
        for mult, label in [(0.5, "-50%"), (1.5, "+50%")]:
            p2 = dict(PARAMS); p2[name] = PARAMS[name] * mult
            r = cost_breakdown(p2)
            print(f"  {name:20s} {label:6s} -> Option A {r['step_a_in']:.2f} in/step")
