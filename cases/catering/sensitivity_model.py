#!/usr/bin/env python3
"""
Sensitivity model -- Catering.

Reproduces case.json.derived's own worked figures for both events (wedding =
"A", corporate party = "B") from Appendix A-D's given menu/fee data, and lets
Tier 2 Probe 5 flex the case's two actual modeling_assumptions (MA1, MA2)
+/-50%.

CONTRACT: PARAMS, FLEX, evaluate(params) -> {"A": net_profit, "B": net_profit},
evaluate_twist(params) for the +15-wedding-guest twist (FACILITATOR.md).

WHAT IS AND ISN'T FLEX
  Menu prices/costs, guest counts (110/100), the loan payment, the 3-hour event
  length, the $115/hr rate and 5-hour billed time, and $1.65/mile are all GIVEN
  scenario data -- the case's own fictional facts, the same authorial latitude
  as any case's Appendix B/C/D. They are not something Victorino "estimated";
  they are what the story states his business charges and needs. Halving the
  loan payment is a different case, not a sensitivity test on this one.

  case.json.modeling_assumptions names exactly two things the case itself
  calls out as assumptions rather than given fact:
    MA1 -- the 7% buffer rate/rounding (Appendix C, Assumption 1)
    MA2 -- the two delivery-mileage estimates, explicitly disclosed as
           "reasonable estimates for the area, not routed or sourced"
           (Appendix C, Assumption 2)
  Both are numeric and both are swept here as FLEX. Everything else in PARAMS
  exists so evaluate() can reproduce the case's real arithmetic, not because
  it is a dial P5 should turn.

Verified against cases/catering/case.json.derived (2026-08-19):
    base    A (wedding)   = 897.42   B (corporate) = 760.62   margin 17.99%
    twist   A (wedding)   = 1098.86  (B unchanged -- twist only touches A)
"""
import math

PARAMS = {
    # --- given scenario data (Appendix A) -----------------------------------
    "wedding_guests": 110,
    "corporate_guests": 100,
    "twist_wedding_guests": 125,          # FACILITATOR.md twist: +15 guests
    # --- Appendix B: menu, summed per the three-item plate each guest gets --
    "wedding_price_per_serving": 6.87 + 11.17 + 8.96,     # Little Italy Salad, Four Cheese Lasagna, Tiramisu
    "wedding_cost_per_serving": 3.91 + 5.18 + 5.32,
    "corporate_price_per_serving": 5.32 + 17.47 + 6.51,   # Caesar Salad, Chicken Parmesan, Butterscotch Budino
    "corporate_cost_per_serving": 1.43 + 12.65 + 2.46,
    # --- Appendix C, Assumption 1 (MA1) -- FLEX -----------------------------
    "buffer_pct": 0.07,
    # --- Appendix D: fees ----------------------------------------------------
    "event_hours": 3.0,               # given event length
    "event_fee_rate": 115.0,          # $/hr
    "event_fee_extra_hours": 2.0,     # fixed 1hr prep + 1hr cleanup, always billed
    "delivery_rate": 1.65,            # $/mile round trip
    # --- Appendix C, Assumption 2 (MA2) -- FLEX -----------------------------
    "wedding_miles": 8.0,
    "corporate_miles": 18.0,
    # --- Background: real, disclosed loan payment (not an assumption) ------
    "loan_payment": 950.0,
}

# Only the case's own two named modeling_assumptions are swept by default.
FLEX = [
    "buffer_pct",        # MA1
    "wedding_miles",      # MA2
    "corporate_miles",    # MA2
]


def _servings(guests, buffer_pct):
    return math.ceil(guests * (1.0 + buffer_pct))


def _fees(p, miles):
    event_fee = p["event_fee_rate"] * (p["event_hours"] + p["event_fee_extra_hours"])
    delivery_fee = p["delivery_rate"] * miles
    return event_fee, delivery_fee


def _net_profit(p, guests, price_per_serving, cost_per_serving, miles):
    s = _servings(guests, p["buffer_pct"])
    revenue = s * price_per_serving
    cost = s * cost_per_serving
    event_fee, delivery_fee = _fees(p, miles)
    return revenue - cost - event_fee - delivery_fee


def evaluate(params):
    p = dict(PARAMS); p.update(params or {})
    a = _net_profit(p, p["wedding_guests"], p["wedding_price_per_serving"],
                     p["wedding_cost_per_serving"], p["wedding_miles"])
    b = _net_profit(p, p["corporate_guests"], p["corporate_price_per_serving"],
                     p["corporate_cost_per_serving"], p["corporate_miles"])
    return {"A": a, "B": b}


def evaluate_twist(params):
    """+15 guests to the Beal wedding only (FACILITATOR.md twist); B is untouched."""
    p = dict(PARAMS); p.update(params or {})
    a = _net_profit(p, p["twist_wedding_guests"], p["wedding_price_per_serving"],
                     p["wedding_cost_per_serving"], p["wedding_miles"])
    b = _net_profit(p, p["corporate_guests"], p["corporate_price_per_serving"],
                     p["corporate_cost_per_serving"], p["corporate_miles"])
    return {"A": a, "B": b}


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})
    print("base ", {k: round(v, 2) for k, v in base.items()},
          "margin %.2f%%" % (100 * (base["A"] - base["B"]) / base["B"]))
    print("twist", {k: round(v, 2) for k, v in tw.items()})
