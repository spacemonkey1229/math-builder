#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Medical Transport.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. This is that
model, for cases/medical-transport.

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):

    PARAMS                             dict[str, number]  every dial the case states
    FLEX                               list[str]          subset of PARAMS probe 5 flexes
    evaluate(params) -> dict           {"A": metric, "B": metric}
    evaluate_twist(params) -> dict     same shape, with the twist's own lens applied

IMPORTANT — metric direction: this case's primary metric is a COST in USD
(total annual operating cost per vehicle), so LOWER is better here (unlike
Cold Chain's in-spec-dose count, where higher is better). Callers comparing
A vs B for "the winner" should take the smaller value, not the larger one.

evaluate() returns the case's graded PRIMARY metric: total annual operating
cost per vehicle (fuel + expected ticket fines + expected insurance
surcharge), matching case.json.balance (A=$8,319.97, B=$9,756.24, margin
17.26%, A cheaper).

evaluate_twist() applies the FACILITATOR.md Twist's lens: instead of pricing
Option B's ticket/surcharge cost at the *expected* (mean) ticket count, it
prices a *worst-plausible* vehicle at ticket_count_worst_case (a stated
scenario dial, default 5 -- one more than Inland's own 4-ticket covered cap)
to show how a fleet-wide policy decision looks different from an average
vehicle's expected cost.

Verified against case.md / case.json:
    evaluate({})        A = 8319.97  B = 9756.24   margin (B-A)/A = 17.26%  (A cheaper)
    evaluate_twist({})  A = 8319.97  B = 10646.09   -- the worst-plausible vehicle
                         (5 tickets/year) still leaves A cheaper, but narrows
                         nothing -- it *widens* the gap, which is itself the
                         point: a policy defended on the average vehicle looks
                         safer than the worst-plausible one actually is.
"""

PARAMS = {
    # --- Appendix B, S1: EPA base fuel economy -------------------------------
    "epa_city_mpg": 26.0,
    "epa_hwy_mpg": 38.0,
    # --- Appendix B, S2: mpg penalty per 5 mph over 50 (multiplicative) ------
    "mpg_penalty_per_5mph_over_50": 0.07,
    # --- Appendix C: fleet daily miles by road type --------------------------
    "miles_city": 110.0,
    "miles_hwy": 142.0,
    "miles_fwy": 352.0,
    "fleet_size": 5,
    # --- Appendix D: posted limits and the two policy speeds -----------------
    "limit_city": 35.0, "limit_hwy": 55.0, "limit_fwy": 65.0,
    "speed_city_A": 35.0, "speed_hwy_A": 55.0, "speed_fwy_A": 65.0,
    "speed_city_B": 45.0, "speed_hwy_B": 65.0, "speed_fwy_B": 75.0,
    # --- Appendix D/G, S5/S6: Oregon presumptive fines by class --------------
    "fine_class_d_usd": 115.0,   # city, highway 10-over (posted <65)
    "fine_class_c_usd": 165.0,   # freeway 10-over (posted >=65, bumped a class)
    # --- Appendix E: Inland's own insurance policy ----------------------------
    "insurance_base_usd": 1453.0,
    "insurance_surcharge_per_ticket_usd": 164.95,
    "covered_tickets_cap": 4,
    # --- Appendix G, S11: current Oregon gas price ----------------------------
    "gas_price_per_gal_usd": 4.7593,
    # --- Modeling Assumptions MA1/MA2 (Appendix, disclosed, unsourced) -------
    "pullover_probability": 0.25,          # MA1
    "annual_exposures_per_vehicle": 8.0,   # MA2
    # --- Twist scenario dial: a "worst-plausible" vehicle's ticket count -----
    "ticket_count_worst_case": 5.0,
    # --- Appendix C: shift structure (2026-08-20 delivery-capacity fix) ------
    "shift_hours": 8.0,
    "break_hours": 0.5,
    # --- Appendix A: given average deliveries/day per hospital (demand, not
    # a function of speed -- see capacity_check() below) --------------------
    "avg_deliveries_randall": 8.4,
    "avg_deliveries_hillsboro": 7.6,
    "avg_deliveries_eugene": 2.7,
    "avg_deliveries_astoria": 1.8,
    "roundtrip_hours_randall_A": 0.45, "roundtrip_hours_randall_B": 0.35,
    "roundtrip_hours_hillsboro_A": 1.44, "roundtrip_hours_hillsboro_B": 1.18,
    "roundtrip_hours_eugene_A": 3.91, "roundtrip_hours_eugene_B": 3.36,
    "roundtrip_hours_astoria_A": 3.59, "roundtrip_hours_astoria_B": 3.03,
}

# Probe 5 flexes THESE and only these -- the case's own STATED, UNSOURCED
# assumptions (MA1, MA2), not the cited Oregon statutes, EPA rating, or AAA gas
# price, which are real, published figures stress-tested by the data-decay
# probe (P6) instead. Both MA1 and MA2 are genuine, case-author-chosen
# estimates with no attributable public source (see case.json.legacy_
# conversion_note and RESEARCH_LOG.md) -- exactly the category SPEC section 2
# sensitivity testing targets.
FLEX = [
    "pullover_probability",           # MA1
    "annual_exposures_per_vehicle",   # MA2
]


def _mpg(speed, base, p):
    if speed <= 50:
        return base
    increments = (speed - 50) / 5.0
    return base * ((1 - p["mpg_penalty_per_5mph_over_50"]) ** increments)


def _fuel_cost_per_vehicle_year(speeds, p):
    gal_city = p["miles_city"] / _mpg(speeds["city"], p["epa_city_mpg"], p)
    gal_hwy = p["miles_hwy"] / _mpg(speeds["hwy"], p["epa_hwy_mpg"], p)
    gal_fwy = p["miles_fwy"] / _mpg(speeds["fwy"], p["epa_hwy_mpg"], p)
    fleet_gal_day = gal_city + gal_hwy + gal_fwy
    fleet_usd_day = fleet_gal_day * p["gas_price_per_gal_usd"]
    return (fleet_usd_day / p["fleet_size"]) * 365


def _expected_ticket_cost_per_vehicle_year(p, ticket_count=None):
    """Option B only -- Option A never exceeds the limit, so its ticket risk
    is zero by construction. `ticket_count`, if given, overrides the
    expected-value ticket count (used by evaluate_twist for the worst-case
    lens); otherwise it is derived from MA1 x MA2."""
    if ticket_count is None:
        ticket_count = p["pullover_probability"] * p["annual_exposures_per_vehicle"]
    avg_fine = (p["fine_class_d_usd"] + p["fine_class_d_usd"] + p["fine_class_c_usd"]) / 3.0
    fines = ticket_count * avg_fine
    surcharge = ticket_count * p["insurance_surcharge_per_ticket_usd"]
    return fines + surcharge


def evaluate(params=None):
    """Primary graded metric: total annual operating cost per vehicle
    (fuel + expected ticket fines + expected insurance surcharge). LOWER is
    better -- this is a cost metric, not a benefit metric."""
    p = dict(PARAMS)
    p.update(params or {})
    speeds_A = {"city": p["speed_city_A"], "hwy": p["speed_hwy_A"], "fwy": p["speed_fwy_A"]}
    speeds_B = {"city": p["speed_city_B"], "hwy": p["speed_hwy_B"], "fwy": p["speed_fwy_B"]}
    cost_A = p["insurance_base_usd"] + _fuel_cost_per_vehicle_year(speeds_A, p)
    cost_B = (p["insurance_base_usd"] + _fuel_cost_per_vehicle_year(speeds_B, p)
              + _expected_ticket_cost_per_vehicle_year(p))
    return {"A": cost_A, "B": cost_B}


def evaluate_twist(params=None):
    """FACILITATOR.md's Twist: Option B priced at a worst-plausible vehicle's
    ticket count (ticket_count_worst_case) instead of the fleet-average
    expected value -- the average-vs-variance reveal."""
    p = dict(PARAMS)
    p.update(params or {})
    speeds_A = {"city": p["speed_city_A"], "hwy": p["speed_hwy_A"], "fwy": p["speed_fwy_A"]}
    speeds_B = {"city": p["speed_city_B"], "hwy": p["speed_hwy_B"], "fwy": p["speed_fwy_B"]}
    cost_A = p["insurance_base_usd"] + _fuel_cost_per_vehicle_year(speeds_A, p)
    cost_B = (p["insurance_base_usd"] + _fuel_cost_per_vehicle_year(speeds_B, p)
              + _expected_ticket_cost_per_vehicle_year(p, ticket_count=p["ticket_count_worst_case"]))
    return {"A": cost_A, "B": cost_B}


def capacity_check(params=None):
    """2026-08-20 fix (Tier 2 P2 finding): checks whether fleet drive-time
    capacity, computed from Appendix C's own shift/break rules, is ever the
    binding constraint on Appendix A's given average-deliveries-per-day
    figures -- for either option. Also computes the one real per-route
    exception: how many round trips a SINGLE vehicle dedicated only to the
    Eugene route can complete per day under each option, versus Eugene's own
    average demand. This is informational (not part of evaluate()'s cost
    metric) -- it backs case.json derived{} and balance.argument_b."""
    p = dict(PARAMS)
    p.update(params or {})
    shift_hours_after_break = p["shift_hours"] - p["break_hours"]
    fleet_hours_day = p["fleet_size"] * 2 * shift_hours_after_break  # 2 shifts/day

    def hours_used(opt):
        return (p["avg_deliveries_randall"] * p[f"roundtrip_hours_randall_{opt}"]
                + p["avg_deliveries_hillsboro"] * p[f"roundtrip_hours_hillsboro_{opt}"]
                + p["avg_deliveries_eugene"] * p[f"roundtrip_hours_eugene_{opt}"]
                + p["avg_deliveries_astoria"] * p[f"roundtrip_hours_astoria_{opt}"])

    hours_A, hours_B = hours_used("A"), hours_used("B")

    def eugene_daily_ceiling(opt):
        per_shift = int(shift_hours_after_break // p[f"roundtrip_hours_eugene_{opt}"])
        return per_shift * 2  # 2 shifts/day, same dedicated vehicle

    eugene_ceiling_A, eugene_ceiling_B = eugene_daily_ceiling("A"), eugene_daily_ceiling("B")
    return {
        "fleet_hours_day": fleet_hours_day,
        "hours_used_A": hours_A, "hours_used_B": hours_B,
        "utilization_pct_A": 100 * hours_A / fleet_hours_day,
        "utilization_pct_B": 100 * hours_B / fleet_hours_day,
        "eugene_ceiling_per_vehicle_day_A": eugene_ceiling_A,
        "eugene_ceiling_per_vehicle_day_B": eugene_ceiling_B,
        "eugene_single_vehicle_covers_demand_A": eugene_ceiling_A >= p["avg_deliveries_eugene"],
        "eugene_single_vehicle_covers_demand_B": eugene_ceiling_B >= p["avg_deliveries_eugene"],
    }


if __name__ == "__main__":
    base = evaluate({})
    tw = evaluate_twist({})
    base_margin = 100 * (base["B"] - base["A"]) / base["A"]
    print("expected-value (evaluate)        A=$%.2f  B=$%.2f  (B-A)/A=%.2f%%  -> %s cheaper" %
          (base["A"], base["B"], base_margin, "A" if base["A"] < base["B"] else "B"))
    print("worst-plausible-vehicle (evaluate_twist) A=$%.2f  B=$%.2f  -> %s cheaper" %
          (tw["A"], tw["B"], "A" if tw["A"] < tw["B"] else "B"))

    cap = capacity_check({})
    print("\ncapacity_check: fleet capacity = %.1f vehicle-hr/day" % cap["fleet_hours_day"])
    print("  Option A: %.2f hr used (%.1f%% utilized)" % (cap["hours_used_A"], cap["utilization_pct_A"]))
    print("  Option B: %.2f hr used (%.1f%% utilized)" % (cap["hours_used_B"], cap["utilization_pct_B"]))
    print("  Eugene single-vehicle daily ceiling: A=%d/day (covers demand: %s)  B=%d/day (covers demand: %s)" %
          (cap["eugene_ceiling_per_vehicle_day_A"], cap["eugene_single_vehicle_covers_demand_A"],
           cap["eugene_ceiling_per_vehicle_day_B"], cap["eugene_single_vehicle_covers_demand_B"]))
