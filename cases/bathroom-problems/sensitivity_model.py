#!/usr/bin/env python3
"""
Sensitivity model -- Bathroom Problems.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS                     dict[str, number]   every dial the case STATES
    FLEX                       list[str]           the subset that is an ASSUMPTION
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     same shape, with the Twist (Grandma Polly and
                                Grandpa Ben moving in) applied

Metric = "useful minutes delivered" -- for each family member, the smaller of
their assigned bathroom slot and their real stated need (Appendix A), summed
across the family. Higher = more of the shared 70-minute window actually goes
toward something a family member needed, instead of being wasted on someone
who didn't need that much time. Matches case.md's D4.

Verified against case.json's balance/derived block:
    base   A = 63.5  ·  B = 70.0  ·  margin 10.24%
    twist  A = 66.0  ·  B = 70.0  ·  margin 6.06%  (still favors B, margin compresses)
"""

# --- Appendix A: each family member's own stated total daily bathroom need,
#     in minutes. Given scenario data (S1), NOT an assumption. ---
NEEDS = {
    "will":    28.0,
    "marta":   47.0,
    "heather": 57.0,
    "nick":    35.0,
    "rulon":   25.0,
    "george":   8.0,
    "olivia":  24.0,
    "thomas":   3.0,
}

PARAMS = {
    # --- Appendix D: the shared morning window, in minutes. Derived from the
    #     given wake time (6:45) + Modeling Assumption MA1 (devotional placed
    #     first thing) + Appendix A's own latest leave-by time (8:00 AM). ---
    "window_minutes": 70.0,
    **{f"{k}_need": v for k, v in NEEDS.items()},
}

# Probe 5 flexes THIS and only this. SPEC section 2 asks for sensitivity to
# STATED ASSUMPTIONS, not to cited/given data: the eight individual need
# figures are the family's own tracked data (Appendix A, S1), not a case-author
# modeling choice -- flexing those would be disputing given data, which P6
# (not P5) is the probe for. MA1 (case.md's Modeling Assumptions block) is the
# one genuine author dial: exactly WHEN the devotional happens, which sets how
# large the shared window is.
FLEX = ["window_minutes"]


def _useful_a(window, needs):
    n = len(needs)
    flat = window / n
    return sum(min(flat, v) for v in needs.values())


def _useful_b(window, needs):
    # Proportional allocation: alloc_i = need_i * window / total_need.
    # Because total_need always exceeds window in this case, alloc_i < need_i
    # for every person, so "useful minutes" (min(alloc, need)) always equals
    # the full allocation -- the whole window is useful under Option B.
    return window


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    needs = {k: p[f"{k}_need"] for k in NEEDS}
    window = p["window_minutes"]
    return {"A": _useful_a(window, needs), "B": _useful_b(window, needs)}


def evaluate_twist(params):
    """The Twist: Grandma Polly and Grandpa Ben move in to help with repairs,
    adding two more adults who need the bathroom every morning.

    Modeled by adding two more family members to the pool (25 min/day each --
    a disclosed, facilitator-side estimate; see FACILITATOR.md MA2, not
    printed in case.md since the Twist is withheld from the student packet
    until the discussion). The shared window is unchanged -- the household's
    morning deadlines don't move, only the number of people sharing them.
    """
    p = dict(PARAMS)
    p.update(params or {})
    needs = {k: p[f"{k}_need"] for k in NEEDS}
    needs["grandma_polly"] = p.get("grandma_polly_need", 25.0)
    needs["grandpa_ben"] = p.get("grandpa_ben_need", 25.0)
    window = p["window_minutes"]
    return {"A": _useful_a(window, needs), "B": _useful_b(window, needs)}


if __name__ == "__main__":
    base = evaluate({})
    tw = evaluate_twist({})
    margin = 100 * (base["B"] - base["A"]) / base["A"]
    margin_tw = 100 * (tw["B"] - tw["A"]) / tw["A"]
    print("base ", {k: round(v, 3) for k, v in base.items()}, "margin %.2f%%" % margin)
    print("twist", {k: round(v, 3) for k, v in tw.items()}, "margin %.2f%%" % margin_tw)
    for w in (35.0, 105.0):
        b = evaluate({"window_minutes": w})
        m = 100 * (b["B"] - b["A"]) / b["A"]
        print(f"flex window={w}", {k: round(v, 3) for k, v in b.items()}, "margin %.2f%%" % m)
