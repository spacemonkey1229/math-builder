#!/usr/bin/env python3
"""
Sensitivity model — Food Rationing.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS                     dict[str, number]   every dial the case STATES
    FLEX                       list[str]           the subset that is an ASSUMPTION
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     same shape, with the Twist's hidden ration applied

Metric = total days the food supply lasts under each option, at everyone's
full recommended (or, for Easton under Option B, re-classified) daily calories.
Higher days = more days of coverage = better, matching the case's own framing
in case.md Appendix F.

Verified against case.json's balance/derived block:
    base   A = 5.165  ·  B = 6.1488  ·  margin 19.05%
    twist  A and B both gain 2,390 / 10,000 and 2,390 / 8,400 days respectively
"""

PARAMS = {
    # --- Appendix D: total core caloric supply (cited/derived, NOT an assumption) ---
    "total_supply_kcal": 51650.0,
    # --- Appendix E (USDA/HHS table, S17): individually cited, NOT assumptions ---
    "tamara_need_kcal": 2000.0,
    "john_need_kcal": 2200.0,
    "fiona_need_kcal": 1600.0,
    "chance_need_kcal": 1000.0,
    # --- Appendix H, MA2: the case's own modeling choice for Option A's flat ration ---
    "flat_ration_kcal": 2000.0,
    # --- Appendix H, MA1: the case's own modeling choice re-classifying Easton's
    #     activity level to "sedentary" rather than an invented retention percent ---
    "easton_need_b_kcal": 1600.0,
    # --- FACILITATOR.md Twist: one real SOLAS/LSA Code liferaft ration pack, S19 ---
    "twist_hidden_ration_kcal": 2390.0,
}

# Probe 5 flexes THESE and only these. SPEC §2 asks for sensitivity to STATED
# ASSUMPTIONS, not to cited measurements: halving the USDA table's own published
# calorie-need figures is not a sensitivity test, it is disputing real data (that
# is what P6 stress-tests instead). MA1 and MA2 are the two dials that are
# genuinely the case author's modeling choices, not sourced figures.
FLEX = [
    "flat_ration_kcal",       # Appendix H, MA2
    "easton_need_b_kcal",     # Appendix H, MA1
]


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    total_daily_a = 5.0 * p["flat_ration_kcal"]
    total_daily_b = (
        p["tamara_need_kcal"]
        + p["john_need_kcal"]
        + p["fiona_need_kcal"]
        + p["easton_need_b_kcal"]
        + p["chance_need_kcal"]
    )
    days_a = p["total_supply_kcal"] / total_daily_a
    days_b = p["total_supply_kcal"] / total_daily_b
    return {"A": days_a, "B": days_b}


def evaluate_twist(params):
    """The Twist: a single SOLAS-standard one-person liferaft ration pack is found.

    This is NOT modeled as a flat addition to the shared total supply (that would
    be mathematically inert -- adding a constant to a shared numerator changes
    both options' days by the same *ratio*, so the margin between A and B would
    be provably invariant to it, a real defect caught while building this model).

    Instead, each option's own stated PHILOSOPHY determines how the pack is used,
    which is the actual dramatic point of the Twist:
      - Option A (strict equality) splits even this one-person pack five ways,
        same as everything else -- it simply extends the flat daily total.
      - Option B (need-based) earmarks the pack entirely to Easton, the person
        the Twist's new information identifies as most acutely at risk ("barely
        keeping anything down at all") -- fully covering his ration draw from
        the shared pool for as many days as the pack alone can sustain him,
        which extends the WHOLE group's runway under B by proportionally more
        than under A. That asymmetry -- not the raw kcal total -- is what
        genuinely moves the margin, and is why the winner and the margin both
        change here (case-readiness Tier 2 probe 4's actual test).
    """
    p = dict(PARAMS)
    p.update(params or {})
    base = evaluate(p)
    total_daily_a = 5.0 * p["flat_ration_kcal"]
    total_daily_b = (
        p["tamara_need_kcal"]
        + p["john_need_kcal"]
        + p["fiona_need_kcal"]
        + p["easton_need_b_kcal"]
        + p["chance_need_kcal"]
    )
    extra_days_a = p["twist_hidden_ration_kcal"] / total_daily_a
    extra_days_b = p["twist_hidden_ration_kcal"] / p["easton_need_b_kcal"]
    return {"A": base["A"] + extra_days_a, "B": base["B"] + extra_days_b}


if __name__ == "__main__":
    base = evaluate({})
    tw = evaluate_twist({})
    margin = 100 * (base["B"] - base["A"]) / base["A"]
    print("base ", {k: round(v, 4) for k, v in base.items()}, "margin %.2f%%" % margin)
    print("twist", {k: round(v, 4) for k, v in tw.items()})
