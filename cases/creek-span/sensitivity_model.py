#!/usr/bin/env python3
"""
Sensitivity model — Creek Span.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     optional; same shape, with the twist applied

evaluate() computes the case's graded primary metric -- total fabricated steel
cost per foot of the 24-ft span -- for each truss option, from Appendix A
(angle weights), Appendix B (the drafter's own stated truss geometry -- span,
panel count, panel length; not a modeling assumption), Appendix D (steel
price), Appendix E (the takeoff quantities) and Appendix F's one modeling
assumption (MA1, gusset-joint labor hours). Because LOWER cost per foot is the
better outcome, evaluate() returns the *negative* of that figure so the
"higher is better" convention still holds: whichever option is cheaper
legitimately returns the higher (less negative) number.

MA1 (gusset-joint labor hours) is the only stated assumption and the only
dial FLEX sweeps -- it is also the case's single largest lever, because it is
the one cost driver that scales directly with The Low Line's two extra
panel-point connections (9 vs. 7). Material cost is close to a wash between
the two options (Option B's heavier chord steel very nearly offsets the
diagonal steel it saves by reusing salvage) -- that is itself a finding worth
surfacing in discussion, not a coincidence to smooth over.

evaluate_twist() models the Twist named in FACILITATOR.md: the shop's
fabrication sub proposes combining two of The Low Line's nine panel points
into one doubled field connection, cutting its effective joint count from 9
to 8. This does not flip the winner at the stated MA1 value -- it narrows the
margin substantially, which is the point: a Hero who declared "A wins
comfortably" has to reckon with how fragile that comfort was.

Verified against case.json's `derived` block:
    base   A = -21.22  B = -24.91   margin  17.39%  (A wins, cheaper per foot)
    twist  A = -21.22  B = -23.02   margin   8.50%  (A still wins, margin narrows)
"""

PARAMS = {
    # --- Appendix B: the drafter's own stated truss geometry, not an assumption
    "span_ft": 24.0,
    "chordA_len_ft": 40.0,
    "chordB_len_ft": 42.0,
    "diagA_new_ft": 48.0,     # all-new diagonal steel, The Warren Line
    "diagB_new_ft": 14.0,     # two sway braces only, The Low Line
    "jointsA": 7,
    "jointsB": 9,
    # --- Appendix A: sourced angle weights (S1, S2, S3) -----------------------
    "chordA_wpf": 4.89,       # L3x3x1/4
    "chordB_wpf": 7.17,       # L3x3x3/8
    "diag_wpf": 3.21,         # L2x2x1/4, both options' new-cut members
    # --- Appendix D: sourced steel price (S4) ---------------------------------
    "price_usd_per_lb": 0.55,
    # --- Appendix F: the one stated modeling assumption (MA1), and the wage
    #     that prices it (S5) -----------------------------------------------
    "gusset_hours_per_joint": 1.5,
    "wage_usd_per_hr": 30.18,
    # --- the Twist (FACILITATOR.md): two of B's joints combine into one -------
    "twist_jointsB": 8,
}

# Only the one stated assumption is swept by Probe 5. Geometry, angle weights,
# steel price and wage are given/cited data, not an assumption the case author
# chose -- per the "Only FLEX[] is swept" rule (case-readiness SKILL.md, Tier 2 P5).
FLEX = [
    "gusset_hours_per_joint",     # Appendix F, MA1
]


def _cost(p, chord_len, chord_wpf, diag_new_ft, joints):
    material = (chord_len * chord_wpf + diag_new_ft * p["diag_wpf"]) * p["price_usd_per_lb"]
    labor = joints * p["gusset_hours_per_joint"] * p["wage_usd_per_hr"]
    total = material + labor
    return total, material, labor


def evaluate(params=None):
    """Graded primary metric: total fabricated cost per foot of span, negated
    (higher = better, i.e. cheaper)."""
    p = dict(PARAMS); p.update(params or {})
    totA, _, _ = _cost(p, p["chordA_len_ft"], p["chordA_wpf"], p["diagA_new_ft"], p["jointsA"])
    totB, _, _ = _cost(p, p["chordB_len_ft"], p["chordB_wpf"], p["diagB_new_ft"], p["jointsB"])
    return {"A": -(totA / p["span_ft"]), "B": -(totB / p["span_ft"])}


def evaluate_twist(params=None):
    """The Twist: The Low Line's joint count drops from 9 to 8 (two panel
    points combined into one doubled field connection)."""
    p = dict(PARAMS); p.update(params or {})
    totA, _, _ = _cost(p, p["chordA_len_ft"], p["chordA_wpf"], p["diagA_new_ft"], p["jointsA"])
    totB, _, _ = _cost(p, p["chordB_len_ft"], p["chordB_wpf"], p["diagB_new_ft"], p["twist_jointsB"])
    return {"A": -(totA / p["span_ft"]), "B": -(totB / p["span_ft"])}


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})

    def _report(d, label):
        lo, hi = min(d, key=d.get), max(d, key=d.get)
        margin = 100 * (d[hi] - d[lo]) / abs(d[lo]) if d[lo] else float('nan')
        print(f"{label:6s} A={d['A']:.4f}  B={d['B']:.4f}  winner={hi}  margin={margin:.2f}%")

    _report(base, "base")
    _report(tw, "twist")

    print("\nFlex sweep (Probe 5, +/-50% on MA1):")
    for mult in (0.5, 1.5):
        flexed = evaluate({"gusset_hours_per_joint": PARAMS["gusset_hours_per_joint"] * mult})
        lo, hi = min(flexed, key=flexed.get), max(flexed, key=flexed.get)
        margin = 100 * (flexed[hi] - flexed[lo]) / abs(flexed[lo])
        print(f"  x{mult:.1f}  A={flexed['A']:.4f}  B={flexed['B']:.4f}  winner={hi}  margin={margin:.2f}%")
