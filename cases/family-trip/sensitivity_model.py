#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Family Trip.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. This is that
model, for cases/family-trip.

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):

    PARAMS                             dict[str, number]  every dial the case states
    FLEX                               list[str]          subset of PARAMS probe 5 flexes
    evaluate(params) -> dict           {"A": metric, "B": metric}
    evaluate_twist(params) -> dict     same shape, with the twist's own lens applied

IMPORTANT — metric direction: this case's primary metric is a COST in USD, so
LOWER is better here (unlike Cold Chain's in-spec-dose count, where higher is
better). Callers comparing A vs B for "the winner" should take the smaller
value, not the larger one.

evaluate() returns the case's graded PRIMARY metric: fully-loaded total
transportation cost (case.json.primary_metric) -- Option B priced with the
real IRS standard mileage rate, not gas price alone. This matches
case.json.balance (A=$1940.80, B=$1754.88, margin 10.6%).

evaluate_twist() returns the alternate, gas-only lens a Hero produces before
FACILITATOR.md's Twist reframes what "cost of driving" means -- Option A is
unchanged (there is no gas-vs-mileage-rate ambiguity for a plane ticket);
Option B drops to its much cheaper gas-only reading. This is the comparison
that makes driving look like a landslide winner before the Twist (case.json
derived.drive_total_cash_marginal = $602.50 vs A's $1,940.80) -- the reveal
in FACILITATOR.md runs the discussion from evaluate_twist()'s naive reading
back to evaluate()'s fully-loaded one, not the other direction.

Verified against case.md / case.json:
    evaluate({})        A = 1940.80  B = 1754.88   margin (A-B)/B = 10.6%   (fully-loaded; B cheaper)
    evaluate_twist({})  A = 1940.80  B =  602.50   margin (A-B)/B = 222.2%  (gas-only; B is a landslide)
"""

PARAMS = {
    # --- Appendix C / Appendix H, MA1: projected Dec-2026 fare per leg ------
    "fare_per_leg_usd": 237.00,
    # --- Appendix D: only 4 of 6 family members need a paid ticket ----------
    "paying_passengers": 4,
    # --- Appendix D, S6: real federal fee, round trip -----------------------
    "tsa_fee_roundtrip_usd": 11.20,
    # --- Appendix H, MA3: disclosed bag strategy -----------------------------
    "bag_fee_total_usd": 0.00,
    # --- Appendix A, S1: real route distance ---------------------------------
    "roundtrip_miles": 1888,
    # --- Appendix F, S12: real, current federal rate -------------------------
    "irs_mileage_rate_usd": 0.76,
    # --- Appendix F, S11: real, current national average ---------------------
    "gas_price_per_gal_usd": 4.04,
    # --- Appendix B, S2, Appendix H MA5: EPA highway rating ------------------
    "mpg_highway": 27,
    # --- Appendix E / Appendix H, MA2 -----------------------------------------
    "hotel_rate_per_night_usd": 80.00,
    "hotel_rooms": 2,
    "hotel_nights": 2,
}

# Probe 5 flexes THESE and only these -- the case's own STATED assumptions
# (Appendix H), not the cited federal/EPA figures (S2, S6, S12), which are
# stress-tested by the data-decay probe (P6) instead. mpg_highway and
# gas_price_per_gal_usd are included because MA5 (which mileage figure to
# apply) is itself a stated modeling choice, not just the raw EPA/AAA citation.
# FLEX rescoped 2026-08-13: irs_mileage_rate_usd and mpg_highway are both real,
# sourced, published figures (the current IRS standard mileage rate; the
# Odyssey's EPA highway rating, source S2) -- cited measurements, not
# assumptions. MA4's actual assumption is WHICH COSTING METHOD to apply (IRS
# rate vs. gas-only), a categorical choice, not the rate's numeric value --
# flexing the published rate itself is testing citation freshness, P6's job,
# not P5's. fare_per_leg_usd (a projected future fare, MA1) and
# hotel_rate_per_night_usd (a rounded-down estimate off a real comparable,
# MA2) remain -- both are genuine, case-author-chosen estimates.
FLEX = [
    "fare_per_leg_usd",          # Appendix H, MA1
    "hotel_rate_per_night_usd",  # Appendix H, MA2
]


def _fly_total(p):
    fares = p["paying_passengers"] * (2 * p["fare_per_leg_usd"])
    fees = p["paying_passengers"] * p["tsa_fee_roundtrip_usd"]
    return fares + fees + p["bag_fee_total_usd"]


def _hotel_total(p):
    return p["hotel_rooms"] * p["hotel_nights"] * p["hotel_rate_per_night_usd"]


def _drive_fully_loaded(p):
    return p["roundtrip_miles"] * p["irs_mileage_rate_usd"] + _hotel_total(p)


def _drive_gas_only(p):
    gallons = p["roundtrip_miles"] / p["mpg_highway"]
    return gallons * p["gas_price_per_gal_usd"] + _hotel_total(p)


def evaluate(params=None):
    """Primary graded metric: fully-loaded cost (IRS mileage rate for B)."""
    p = dict(PARAMS)
    p.update(params or {})
    return {"A": _fly_total(p), "B": _drive_fully_loaded(p)}


def evaluate_twist(params=None):
    """Naive gas-only lens for B -- the pre-Twist reading (FACILITATOR.md)."""
    p = dict(PARAMS)
    p.update(params or {})
    return {"A": _fly_total(p), "B": _drive_gas_only(p)}


if __name__ == "__main__":
    base = evaluate({})
    tw = evaluate_twist({})
    base_margin = 100 * (base["A"] - base["B"]) / base["B"]
    tw_margin = 100 * (tw["A"] - tw["B"]) / tw["B"]
    print("fully-loaded (evaluate)      A=$%.2f  B=$%.2f  (A-B)/B=%.1f%%  -> %s cheaper" %
          (base["A"], base["B"], base_margin, "B" if base["B"] < base["A"] else "A"))
    print("gas-only, pre-twist (evaluate_twist) A=$%.2f  B=$%.2f  (A-B)/B=%.1f%%  -> %s cheaper" %
          (tw["A"], tw["B"], tw_margin, "B" if tw["B"] < tw["A"] else "A"))
