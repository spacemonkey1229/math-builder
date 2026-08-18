#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Foreign Travel.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the reference
shape this file follows.

CONTRACT:
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            subset of PARAMS Tier 2 flexes
    evaluate(params) -> dict   {"A": metric, "B": metric}   HIGHER = better here
                                means CHEAPER (lower total cost) -- so evaluate()
                                returns the NEGATIVE of each option's total cost,
                                to satisfy the "higher is better" contract while
                                keeping the real dollar totals easy to read off
                                in derived_totals() below.
    evaluate_twist(params)     same shape, with the Twist's own perturbation
                                applied (see below -- the Twist here does not
                                change either option's dollar total at all,
                                which is itself the point of this case's Twist).

evaluate() models the case's actual GRADED primary_metric (case.json
`primary_metric` / `balance.margin_pct` = 12.25): total transportation cost in
USD for both sisters together, Option A (car) vs Option B (rail), built from
every cited appendix line item (case.json `sources[]` S1-S30) plus the three
genuine Modeling Assumptions (MA1 fuel economy, MA3 metro ride count, MA4
Channel-crossing baseline) that FLEX actually perturbs.

Per skills/case-readiness/SKILL.md's P5 doctrine ("Only FLEX[] is swept... sensitivity
to stated assumptions, not to cited measurements"), FLEX contains ONLY the three
genuine assumptions -- every appendix price, every driving distance, and both
exchange rates are cited data (case.json sources[] S1-S30), never flexed here.
"""

PARAMS = {
    # ---- CITED DATA (never flexed -- see sources[] in case.json) ----------
    "gbp_usd": 1.35,
    "eur_usd": 1.16,
    "rental_gbp_per_day": 20.00,        # S1 -- refreshed 2026-08-18, official gatwickairport.com "Car Hire from £20/day"
    "rental_days": 9,
    "uk_petrol_gbp_per_l": 1.612,
    "eu_petrol_eur_per_l": 1.79,
    "uk_leg_miles": 84 + 67,            # Gatwick-Dover proxy + Canterbury-Gatwick return
    "eu_leg_miles": 185 + 316 + 228 + 130 + 176,  # Calais-Paris, Paris-Ams, Ams-Groningen RT, Ams-Brussels, Brussels-Canterbury
    "london_bundle_gbp_per_day": 52.30,  # £21.80 parking (S23, refreshed) + £30.50 CC/ULEZ (S21)
    "london_days": 2,
    "paris_bundle_eur_per_day": 30.00,   # S24
    "paris_days": 2,
    "critair_eur": 4.51,                 # S22 -- refreshed 2026-08-18, real foreign-vehicle (int'l postage) price
    "eurostar_ldn_par_gbp": 79.00,       # S13, per person
    "thalys_par_ams_eur": 124.72,        # S14 -- refreshed 2026-08-19, seat61's claimed EUR55-EUR135 band
                                          # does not exist on the live page (only EUR35 "several months
                                          # ahead" and EUR149 "on the day" appear); EUR35 does not match this
                                          # case's own "several weeks (not months) ahead" booking framing
                                          # (case.md Appendix B), so real figure taken from a live
                                          # thetrainline.com advance-fare quote ($144.68) converted at the
                                          # case's own EUR/USD rate
    "ns_ams_gro_eur_oneway": 33.30,      # S15 -- refreshed 2026-08-18, real NS.nl fare is EUR not USD
    "ns_ams_bru_eur": 45.00,             # S16, per person
    "eurostar_bru_ldn_gbp": 52.00,       # S17 -- refreshed 2026-08-19, real one-way fare (seat61: "£52
                                          # one-way or £78 return") -- this leg is one-way in the itinerary,
                                          # case had wrongly used the £78 RETURN fare as a one-way price
    "natrail_ldn_cant_gbp": 16.20,       # S18, per person
    "ldn_underground_gbp": 3.10,         # S19, per ride
    "paris_metro_eur": 2.55,             # S20, per ride
    "travelers": 2,

    # ---- GENUINE MODELING ASSUMPTIONS (Appendix A/C/D of case.md) ---------
    "rental_mpg_imperial": 40.0,          # MA1 -- Appendix A, Modeling Assumption A1
    "metro_rides_per_person_per_day": 6,  # MA3 -- Appendix C, Modeling Assumption C1
    "ferry_crossing_gbp_each_way": 120.00,  # MA4 -- Appendix D, Modeling Assumption D1; falls within
                                             # the real GBP-denominated band re-sourced 2026-08-19 (S26,
                                             # aferry.com/en-gb: cars "£80 to £193 one way") after the
                                             # directferries.com USD-only page could not support a GBP claim
}

# Probe 5 flexes THESE and only these -- the three genuine, stated Modeling
# Assumptions (case.md Appendix A/C/D; case.json modeling_assumptions[] MA1/
# MA3/MA4). Every other PARAMS key is cited appendix data (prices, distances,
# exchange rates) and is stress-tested by probe 6 (data decay) instead, per
# skills/case-readiness/SKILL.md's P5 doctrine -- "cited data is stress-tested
# by P6 instead."
FLEX = [
    "rental_mpg_imperial",
    "metro_rides_per_person_per_day",
    "ferry_crossing_gbp_each_way",
]

L_PER_IMPERIAL_GALLON = 4.546


def _option_a_usd(p):
    """Option A (car) total cost in USD, for both travelers sharing one car.

    IMPORTANT: case.md's Appendix C header is explicit -- "Getting around
    inside London and Paris (both options use this)" -- and the Overview
    states it flatly too ("Both sisters agree...inside the cities of London
    and Paris, they'll get around by metro/subway, not by car"). The metro
    fares (MA3 ride count x S19/S20 fares) are therefore a real cost on
    BOTH options, not just Option B: an Option-A traveler still buys metro
    tickets for in-city sightseeing while the rented car sits idle (which is
    exactly why the idle-car zone fees below exist in the first place). A
    2026-08-19-and-earlier version of this function omitted the metro line
    from Option A entirely -- a real modeling bug, not a rounding issue --
    which silently made the car look cheaper than it really is. Fixed here.
    """
    rental_gbp = p["rental_gbp_per_day"] * p["rental_days"]

    uk_fuel_l = (p["uk_leg_miles"] / p["rental_mpg_imperial"]) * L_PER_IMPERIAL_GALLON
    eu_fuel_l = (p["eu_leg_miles"] / p["rental_mpg_imperial"]) * L_PER_IMPERIAL_GALLON
    uk_fuel_gbp = uk_fuel_l * p["uk_petrol_gbp_per_l"]
    eu_fuel_eur = eu_fuel_l * p["eu_petrol_eur_per_l"]

    crossings_gbp = p["ferry_crossing_gbp_each_way"] * 2  # outbound + return crossing

    london_gbp = p["london_bundle_gbp_per_day"] * p["london_days"]
    paris_eur = p["paris_bundle_eur_per_day"] * p["paris_days"]

    # City metro costs -- identical formula to Option B's, per Appendix C:
    # both options pay for in-city metro travel regardless of intercity mode.
    metro_gbp = (p["ldn_underground_gbp"] * p["metro_rides_per_person_per_day"]
                 * p["london_days"] * p["travelers"])
    metro_eur = (p["paris_metro_eur"] * p["metro_rides_per_person_per_day"]
                 * p["paris_days"] * p["travelers"])

    total_gbp = rental_gbp + uk_fuel_gbp + crossings_gbp + london_gbp + metro_gbp
    total_eur = eu_fuel_eur + paris_eur + p["critair_eur"] + metro_eur

    return total_gbp * p["gbp_usd"] + total_eur * p["eur_usd"]


def _option_b_usd(p):
    """Option B (rail) total cost in USD, for both travelers (every ticket x2)."""
    t = p["travelers"]

    gbp_total = (
        p["eurostar_ldn_par_gbp"] * t
        + p["eurostar_bru_ldn_gbp"] * t
        + p["natrail_ldn_cant_gbp"] * t
        + p["ldn_underground_gbp"] * p["metro_rides_per_person_per_day"] * p["london_days"] * t
    )
    # NS Amsterdam-Groningen is a round trip (there and back), quoted in EUR (S15, refreshed 2026-08-18)
    eur_total = (
        p["thalys_par_ams_eur"] * t
        + p["ns_ams_bru_eur"] * t
        + p["ns_ams_gro_eur_oneway"] * 2 * t
        + p["paris_metro_eur"] * p["metro_rides_per_person_per_day"] * p["paris_days"] * t
    )

    return gbp_total * p["gbp_usd"] + eur_total * p["eur_usd"]


def derived_totals(params=None):
    """Convenience: the real dollar totals, not negated -- for reporting/printing."""
    p = dict(PARAMS)
    p.update(params or {})
    a = _option_a_usd(p)
    b = _option_b_usd(p)
    return {"A_usd": a, "B_usd": b, "margin_pct_a_over_b": 100 * (a - b) / b}


def evaluate(params, detour_h=0.0):
    """The case's actual graded primary_metric: total transportation cost in
    USD, Option A (car) vs Option B (rail), for both sisters together.
    Contract requires HIGHER = BETTER, so this returns the *negative* of each
    option's dollar total (cheaper = higher/better)."""
    p = dict(PARAMS)
    p.update(params or {})
    return {"A": -_option_a_usd(p), "B": -_option_b_usd(p)}


def evaluate_twist(params):
    """The Twist (constant UK-Europe time offset across the March 28 clock
    change) is a TIME-mechanics finding, not a cost finding -- by design, it
    changes neither option's dollar total. This function returns the same
    values as evaluate() to make that explicit and mechanically checkable:
    Tier 2 probe 4 should confirm the twist leaves the cost verdict and
    margin completely unmoved, because the case's twist is about D2 (the
    itinerary), not D1 (the cost table)."""
    return evaluate(params)


if __name__ == '__main__':
    base = derived_totals({})
    print("base totals:", {k: round(v, 2) for k, v in base.items()})
    ev = evaluate({})
    print("evaluate() (negated, higher=better):", {k: round(v, 2) for k, v in ev.items()})

    print("\nFLEX sweep (+/-50%):")
    for key in FLEX:
        base_val = PARAMS[key]
        for pct, label in [(0.5, "-50%"), (1.5, "+50%")]:
            flexed = dict(PARAMS)
            flexed[key] = base_val * pct
            t = derived_totals(flexed)
            winner = "A (car)" if t["A_usd"] < t["B_usd"] else "B (rail)"
            print(f"  {key} {label} ({base_val} -> {round(flexed[key], 3)}): "
                  f"A=${t['A_usd']:.2f} B=${t['B_usd']:.2f} "
                  f"margin={t['margin_pct_a_over_b']:.2f}%  winner={winner}")

    tw = evaluate_twist({})
    print("\nevaluate_twist() -- should equal evaluate() exactly (twist affects D2 time math, not D1 cost):")
    print("  ", {k: round(v, 2) for k, v in tw.items()}, "  MATCH" if tw == ev else "  MISMATCH")
