#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Archery Camp.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the reference
shape this file follows.

CONTRACT:
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            subset of PARAMS Tier 2 flexes
    evaluate(params) -> dict   {"A": metric, "B": metric}   HIGHER = better.
    evaluate_twist(params)     same shape, with the registration-surge Twist applied.

evaluate() models the case's actual GRADED primary_metric (case.json
`primary_metric` / `balance.margin_pct` = 9.92): per-participant charge needed
to cover total camp cost at the planned attendance, Option A (fields A,B,C,G,H)
vs Option B (fields D,E,F,J). Real-world "better" here is CHEAPER (lower
per-participant charge), which is LOWER-is-better. To satisfy the contract's
"higher is better" while keeping the underlying dollar figures easy to read,
evaluate() uses the same ceiling-collapse transform verified in
Plaza Pavers/Company Front/Vent Cap/Apron Order: metric = 2*worse - cost.

Every entry in PARAMS is either a cited/given fact (Appendix A field rental
rates, Appendix B ranges-per-field, Appendix C's per-range capacity and
counselor-minimum, the $26.30/attendee equipment rate, the $145/counselor/day
rate, the board's $110 target, the twist's stated 160-registration surge) or
the one genuine, author-chosen Modeling Assumption the case actually declares
a number for: Appendix C Assumption 1's 140-planned-attendance planning
figure (case.json modeling_assumptions MA1). Appendix C Assumption 2 (a
field's range count is fixed regardless of actual attendance; no partial
refunds) is a real stated convention too, but it is not a numeric dial — it is
already baked into how `_option_cost` below computes rental and counselor
cost (from RENTED ranges, never from headcount), so there is nothing to flex.

FLEX = ["planned_attendance"] only. Per SPEC §2 / this skill's P5 doctrine,
only a genuine ASSUMPTION is swept, not cited data — flexing the Simplot rate
sheet or the $26.30 equipment rate would test the model's honesty, not the
case's. `planned_attendance` is the sole numeric assumption the case's own
Appendix C names as an assumption.

Verified against cases/archery-camp/case.json `derived{}`:
    option_a: rental $1,449.00, ranges 13, capacity 156, counselors 26,
              counselor pay $11,310.00, equip $3,682.00, total $16,441.00,
              per-participant $117.44
    option_b: rental $1,341.00, ranges 15, capacity 180, counselors 30,
              counselor pay $13,050.00, equip $3,682.00, total $18,073.00,
              per-participant $129.09
    D5: option_a fixed cost $12,759.00; 12759 + 26.30x = 110x -> x = 152.44
        -> 153 whole attendees (exceeds Karen's own 150-person ceiling)
    twist: total demand 300; option_a shortfall 144; option_b shortfall 120
"""

PARAMS = {
    # ---- CITED / GIVEN DATA (never flexed) -- Appendix A field rental rates --
    "rate_A": 99.00, "rate_B": 91.00, "rate_C": 114.00, "rate_D": 114.00,
    "rate_E": 107.00, "rate_F": 112.00, "rate_G": 87.00, "rate_H": 92.00,
    "rate_J": 114.00,
    # ---- CITED / GIVEN DATA -- Appendix B ranges per field --------------------
    "ranges_A": 3, "ranges_B": 2, "ranges_C": 4, "ranges_D": 4, "ranges_E": 3,
    "ranges_F": 4, "ranges_G": 2, "ranges_H": 2, "ranges_J": 4,
    # ---- CITED / GIVEN DATA -- Background / Appendix B operating rules -------
    "camp_days": 3,
    "counselors_per_range": 2,          # Background: "at least 2 counselors" per range
    "campers_per_range": 12,            # Background / Appendix B
    "counselor_pay_per_day": 145.00,    # Background
    "equip_cost_per_attendee": 26.30,   # Background
    "board_target_per_participant": 110.00,  # Background: board's real goal
    # ---- Twist (FACILITATOR.md) -- stated scenario figure --------------------
    "registration_surge": 160,
    # ---- THE ONE GENUINE ASSUMPTION (Appendix C, Assumption 1) ---------------
    "planned_attendance": 140,
}

# Only the genuine stated ASSUMPTION is swept -- see docstring.
FLEX = ["planned_attendance"]

OPTION_A_FIELDS = ["A", "B", "C", "G", "H"]
OPTION_B_FIELDS = ["D", "E", "F", "J"]


def _option_cost(p, fields):
    daily_rental = sum(p[f"rate_{f}"] for f in fields)
    total_rental = daily_rental * p["camp_days"]
    ranges = sum(p[f"ranges_{f}"] for f in fields)
    counselors = ranges * p["counselors_per_range"]
    counselor_cost = counselors * p["counselor_pay_per_day"] * p["camp_days"]
    equip_cost = p["equip_cost_per_attendee"] * p["planned_attendance"]
    total_cost = total_rental + counselor_cost + equip_cost
    per_participant = total_cost / p["planned_attendance"]
    max_capacity = ranges * p["campers_per_range"]
    fixed_cost = total_rental + counselor_cost   # independent of headcount (Assumption 2)
    return {
        "ranges": ranges, "counselors": counselors, "max_capacity": max_capacity,
        "total_rental": total_rental, "counselor_cost": counselor_cost,
        "equip_cost": equip_cost, "total_cost": total_cost,
        "per_participant": per_participant, "fixed_cost": fixed_cost,
    }


def evaluate(params=None):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. Ceiling-collapse
    transform (Plaza Pavers/Company Front/Vent Cap/Apron Order pattern):
    metric = 2*worse - cost, over the per-participant charge."""
    p = dict(PARAMS); p.update(params or {})
    a = _option_cost(p, OPTION_A_FIELDS)["per_participant"]
    b = _option_cost(p, OPTION_B_FIELDS)["per_participant"]
    ceiling = 2 * max(a, b)
    return {"A": ceiling - a, "B": ceiling - b}


def evaluate_twist(params=None):
    """The Twist (FACILITATOR.md: a 160-registration surge) is a CAPACITY
    finding, not a cost finding -- Assumption 1 already fixed the cost model
    at the planned attendance, and the surge does not reopen that calculation
    (nothing in the case says Karen re-bills at the higher headcount). So
    this function does NOT recompute per_participant; it returns campers
    actually served out of total post-surge demand (higher = better = fewer
    kids turned away), which is what FACILITATOR.md's own computed numbers
    (case.json derived.twist_option_a_shortfall / twist_option_b_shortfall)
    are built from. Reframing the decision from a cost question to a
    capacity question IS the twist's mechanism -- see QA_REPORT.md P4."""
    p = dict(PARAMS); p.update(params or {})
    demand = p["planned_attendance"] + p["registration_surge"]
    cap_a = _option_cost(p, OPTION_A_FIELDS)["max_capacity"]
    cap_b = _option_cost(p, OPTION_B_FIELDS)["max_capacity"]
    return {"A": min(cap_a, demand), "B": min(cap_b, demand)}


def solve_d5_target_attendance(params=None):
    """D5: minimum whole attendance for Option A to hit board_target_per_participant,
    from Option A's own fixed cost (rental + counselor pay) and the equipment rate.
    fixed_cost + equip*x = target*x  ->  x = fixed_cost / (target - equip)."""
    p = dict(PARAMS); p.update(params or {})
    fixed_cost = _option_cost(p, OPTION_A_FIELDS)["fixed_cost"]
    target = p["board_target_per_participant"]
    equip = p["equip_cost_per_attendee"]
    exact = fixed_cost / (target - equip)
    import math
    return exact, math.ceil(exact)


if __name__ == '__main__':
    a = _option_cost(PARAMS, OPTION_A_FIELDS)
    b = _option_cost(PARAMS, OPTION_B_FIELDS)
    print("Option A:", {k: round(v, 2) for k, v in a.items()})
    print("Option B:", {k: round(v, 2) for k, v in b.items()})
    margin = 100 * (b["per_participant"] - a["per_participant"]) / a["per_participant"]
    print(f"case-style margin (B over A): {margin:.2f}%  (case.json margin_pct = 9.92)")

    exact, rounded = solve_d5_target_attendance()
    print(f"D5: exact={exact:.2f} -> rounded up={rounded} (case.json derived = 152.44 -> 153)")

    ev = evaluate({})
    print("evaluate() (ceiling-collapse, higher=better):", {k: round(v, 2) for k, v in ev.items()})

    tw = evaluate_twist({})
    print("evaluate_twist() (campers served, higher=better):", tw)
