#!/usr/bin/env python3
"""
Sensitivity model -- Travel Planner.

Tier 2 probe 5 flexes each stated modeling assumption by +-50% and reports
whether the cheaper plan flips. CONTRACT: PARAMS, evaluate(params) -> {"A","B"}.

A = Plan A (Wizarding World) grand total, B = Plan B (Disney Classic) grand
total, in USD. Lower is "cheaper" but the harness's generic margin/winner
convention just compares the two numbers -- matches case.json.balance exactly
(base A=2601.65, B=2817.36, margin 8.29%).
"""

PARAMS = {
    # Appendix A/C -- family-wide list price per activity day, for the
    # Betteridges' actual 6-person mix of adult/child/free-admission ages
    # (2 adults, Cassy 10, Maria 8, Jimmy Jr 6, Henrietta 2-free per MA1).
    # Not flexed: these are Appendix C's real, sourced per-gate ticket
    # prices applied to a fixed, given family roster, not authorial
    # estimates -- matching case.json.sensitivity_disclosure[]'s scope
    # (only plan_b_hotel_rate is a genuine disclosed modeling assumption).
    "universal_1day_family_list": 533.00,   # 3 Universal days -> x3 below
    "zoo_1day_family_list": 370.00,
    "disneyland_2day_family_list": 1635.00,
    "legoland_1day_family_list": 345.00,
    # Background -- Gina's firm's standing discount tiers.
    "tier_2pct": 0.02,
    "tier_6pct": 0.06,
    # Background -- Priceline hotel discount.
    "hotel_discount": 0.085,
    # Background -- agency fee, % of combined discounted hotel+ticket total.
    "agency_fee_pct": 0.04,
    # Appendix D -- nightly rates.
    "plan_a_hotel_rate": 139.00,
    # Appendix E, MA4: the single largest modeling assumption -- the top of
    # a real $102-$210/night cited range, since Plan B needs the specific
    # divided-suite room type. See sensitivity_disclosure[] in case.json.
    "plan_b_hotel_rate": 210.00,
}

# Only MA4's dial is flexed -- the ticket list prices and discount/fee
# percentages are Background's own fixed, sourced deal terms (Appendix C/F),
# not scenario assumptions; flexing them would be the FLEX-scoping error the
# pipeline's doctrine warns against (case.json.sensitivity_disclosure[] only
# names plan_b_hotel_rate as unstable, and P6 confirms the ticket prices and
# fee percentages are all directly sourced, not authorial choices).
FLEX = ["plan_b_hotel_rate"]

PLAN_A_NIGHTS = 5
PLAN_B_NIGHTS = 4


def evaluate(params):
    p = dict(PARAMS); p.update(params or {})

    # Plan A: 3 Universal days (family total/day, 6% tier per MA2) + 1 Zoo day (2% tier)
    universal_total = 3 * p["universal_1day_family_list"] * (1 - p["tier_6pct"])
    zoo_total = p["zoo_1day_family_list"] * (1 - p["tier_2pct"])
    a_tickets = universal_total + zoo_total
    a_hotel = PLAN_A_NIGHTS * p["plan_a_hotel_rate"] * (1 - p["hotel_discount"])
    a_subtotal = a_tickets + a_hotel
    a_total = a_subtotal * (1 + p["agency_fee_pct"])

    # Plan B: Disneyland 2-day (family total, 2% tier) + LEGOLAND 1-day (2% tier)
    disneyland_total = p["disneyland_2day_family_list"] * (1 - p["tier_2pct"])
    legoland_total = p["legoland_1day_family_list"] * (1 - p["tier_2pct"])
    b_tickets = disneyland_total + legoland_total
    b_hotel = PLAN_B_NIGHTS * p["plan_b_hotel_rate"] * (1 - p["hotel_discount"])
    b_subtotal = b_tickets + b_hotel
    b_total = b_subtotal * (1 + p["agency_fee_pct"])

    return {"A": a_total, "B": b_total}


if __name__ == '__main__':
    base = evaluate({})
    margin = 100 * (max(base.values()) - min(base.values())) / min(base.values())
    print("base", {k: round(v, 2) for k, v in base.items()}, "margin %.2f%%" % margin)
