#!/usr/bin/env python3
"""
SENSITIVITY MODEL — AirBnb Or Landlord.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. This is that
model, for cases/airbnb-or-landlord.

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):

    PARAMS                             dict[str, number]  every dial the case STATES
    FLEX     list[str]                 subset of PARAMS probe 5 flexes
    evaluate(params) -> dict           {"A": metric, "B": metric}     higher is better
    evaluate_twist(params) -> dict     same shape, with the twist's own lens applied

evaluate() returns the case's graded PRIMARY metric: estimated annual net rental
profit in USD (case.json.primary_metric). Higher is better for both options here
(unlike Family Trip's cost metric, where lower was better).

This matches case.json.balance (A=$14,112.50, B=$16,724.60, margin 18.5%, B wins).

evaluate_twist() applies FACILITATOR.md's Twist lens: it does NOT change either
dollar total (the Twist never disputes the arithmetic) -- it returns the same
two profit figures alongside an explicit per-hour value of Option A's 116 hours
of the Daltons' own unpaid cleaning labor, which is the number the discussion
actually turns on. Included here so a caller can see the Twist doesn't move the
winner, exactly as case.json.qa records it.

Verified against case.md / case.json:
    evaluate({})        A = 14112.50  B = 16724.60   margin (B-A)/A = 18.5%   (B wins)
    evaluate_twist({})  same A/B; extra key "a_labor_hours" = 116
"""

PARAMS = {
    # --- Appendix B/S1: real, current Boise Airbnb market -------------------
    "occupancy_rate_pct": 47.8,
    "adr_usd": 195.00,
    # --- Appendix F, MA2: case-author-chosen average stay length ------------
    "avg_stay_nights": 3,
    # --- Background: Daltons' own fixed cleaning economics -------------------
    "cleaning_fee_usd": 65.00,
    "cleaning_materials_cost_usd": 25.00,
    "cleaning_hours_per_turnover": 2,
    # --- Appendix D/S4: real, current Airbnb host-only fee -------------------
    "airbnb_host_fee_rate_pct": 15.5,
    # --- Appendix A: Daltons' own fixed home costs ----------------------------
    "mortgage_monthly_usd": 1092.00,
    "utilities_monthly_usd": 225.00,
    "maintenance_annual_usd": 490.00,
    # --- Appendix C/S2: real, current Boise 3BR long-term rental market ------
    "unfurnished_baseline_monthly_usd": 2197.00,
    # --- Appendix F, MA1: case-author-chosen furnished premium ---------------
    "furnished_premium_pct": 15.0,
}

# Probe 5 flexes THESE and only these -- the case's own STATED assumptions
# (Appendix F), not the cited market/federal figures (S1-S4), which are
# stress-tested by the data-decay probe (P6) instead. occupancy_rate_pct,
# adr_usd, airbnb_host_fee_rate_pct, and unfurnished_baseline_monthly_usd are
# all real, sourced, dated market figures -- cited measurements, not scenario
# dials the case author picked. avg_stay_nights (MA2) and furnished_premium_pct
# (MA1) are both genuine, case-author-chosen estimates within a real range.
FLEX = [
    "avg_stay_nights",          # Appendix F, MA2
    "furnished_premium_pct",    # Appendix F, MA1
]


def _airbnb_annual_profit(p):
    nights = round(365 * (p["occupancy_rate_pct"] / 100.0))
    gross_nightly = nights * p["adr_usd"]
    bookings = int(nights // p["avg_stay_nights"]) if p["avg_stay_nights"] > 0 else 0
    cleaning_fee_rev = bookings * p["cleaning_fee_usd"]
    gross_booking_rev = gross_nightly + cleaning_fee_rev
    host_fee = gross_booking_rev * (p["airbnb_host_fee_rate_pct"] / 100.0)
    net_payout = gross_booking_rev - host_fee
    cleaning_cost = bookings * p["cleaning_materials_cost_usd"]
    utilities_annual = p["utilities_monthly_usd"] * 12
    mortgage_annual = p["mortgage_monthly_usd"] * 12
    profit = (net_payout - cleaning_cost - utilities_annual - mortgage_annual
              - p["maintenance_annual_usd"])
    return profit, bookings, nights


def _traditional_annual_profit(p):
    furnished_rent = p["unfurnished_baseline_monthly_usd"] * (1 + p["furnished_premium_pct"] / 100.0)
    gross_annual_rent = furnished_rent * 12
    mortgage_annual = p["mortgage_monthly_usd"] * 12
    profit = gross_annual_rent - mortgage_annual - p["maintenance_annual_usd"]
    return profit


def evaluate(params=None):
    """Primary graded metric: estimated annual net rental profit, USD. Higher wins."""
    p = dict(PARAMS)
    p.update(params or {})
    a, _, _ = _airbnb_annual_profit(p)
    b = _traditional_annual_profit(p)
    return {"A": a, "B": b}


def evaluate_twist(params=None):
    """Same two dollar totals -- the Twist reframes what 'profit' means, doesn't move it."""
    p = dict(PARAMS)
    p.update(params or {})
    a, bookings, nights = _airbnb_annual_profit(p)
    b = _traditional_annual_profit(p)
    labor_hours = bookings * p["cleaning_hours_per_turnover"]
    return {"A": a, "B": b, "a_labor_hours": labor_hours}


if __name__ == "__main__":
    base = evaluate({})
    tw = evaluate_twist({})
    margin = 100 * (base["B"] - base["A"]) / base["A"]
    print("estimated annual net profit (evaluate)  A=$%.2f  B=$%.2f  (B-A)/A=%.1f%%  -> %s wins" %
          (base["A"], base["B"], margin, "B" if base["B"] > base["A"] else "A"))
    print("twist lens (evaluate_twist)             A=$%.2f  B=$%.2f  a_labor_hours=%d" %
          (tw["A"], tw["B"], tw["a_labor_hours"]))
