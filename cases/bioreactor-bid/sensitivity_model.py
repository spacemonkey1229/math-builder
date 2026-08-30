#!/usr/bin/env python3
"""
Sensitivity model — The Bioreactor Bid.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the contract
and worked reference (Cold Chain).

CONTRACT:
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset that is a stated
                                                     Modeling Assumption
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better

The metric returned is the case's actual recommendation logic, not the raw
yield-per-dollar ratio alone: an option that fails the client's minimum total
yield [MA4] or blows the CRO budget cap [MA5] is disqualified and scored 0,
exactly as Wei's Background states ("Wei's recommendation has to clear all
three at once"). This is deliberate -- the case's real dilemma is that the
Wave Bid (B) has the *better* raw yield-per-dollar ratio but is disqualified
by MA4 at the stated base values, so `evaluate()` must be able to reproduce
that disqualification, not just the underlying ratio.

Fixed (not in FLEX[]): vessel geometry and cost figures that are cited data
(sources[] S1-S5), not stated scenario assumptions -- Column's 75% fill of a
sourced 50 L nominal capacity, and both vessels' sourced purchase costs.
Only the Modeling Assumptions (MA1, MA2, MA4, MA5, and MA6/MA7 via their
proxy dials) are swept by default.

Verified against case.md and case.json (2026-08-27 remediation):
    base    A (Column) = 0.0008551  ·  B (Wave) = 0.0  (disqualified by MA4)
            raw yield-per-dollar ratio, ignoring MA4/MA5: A=0.0008551, B=0.0009606
            (a 12.4% margin -- this is case.json.balance.margin_pct)
    MA4 flexed to ~12.5 L (-50%): B becomes feasible and wins outright,
            matching the case's own documented flip band ("below ~17.3 L ...
            Wave wins", case.md Modeling Assumptions / MA4).
"""

# --- Fixed: cited data (sources[] S1-S5), not stated modeling assumptions ---
COLUMN_NOMINAL_L = 50.0          # [S1]
COLUMN_FILL_FRAC = 0.75          # [S5]
COLUMN_VESSEL_COST_USD = 28864.0  # [S2]
WAVE_VESSEL_COST_USD = 8000.0     # [S4]

PARAMS = {
    # --- MA1: Column Bid validation cost -------------------------------------
    "ma1_column_validation_usd": 15000.0,
    # --- MA2: Wave Bid validation cost ----------------------------------------
    "ma2_wave_validation_usd": 10000.0,
    # --- MA4: client's minimum total viable product yield ---------------------
    "ma4_min_yield_l": 25.0,
    # --- MA5: CRO program budget cap ------------------------------------------
    "ma5_budget_cap_usd": 50000.0,
    # --- MA6 proxy: net cumulative yield per liter of working volume, from the
    #     area between Appendix A's feed-rate/uptake-rate curves x the 0.05 L/g
    #     conversion factor. Both are stated Modeling Assumptions (MA6); flexing
    #     this scalar approximates "what if MA6's authored table/conversion
    #     factor were bigger or smaller", per SPEC Sec2 sensitivity to STATED
    #     assumptions, not to a re-derivation of the table itself.
    "yield_scale_l_per_l": 1.0,
    # --- MA7 proxy: Wave Bid's disk-method-integrated working volume, in L.
    #     MA7 is the bag radius profile r(h); flexing the resulting volume
    #     directly is the honest proxy for "what if MA7's authored profile were
    #     flatter/taller", since the profile only ever enters the case's math
    #     through this one derived number (case.json.derived.wave_working_volume_l).
    "wave_working_volume_l": 17.29,
}

# Probe 5 flexes THESE and only these -- the subset that is a stated Modeling
# Assumption, not cited/sourced data (Column's fill level and both vessels'
# purchase costs are sourced, so they are NOT flexed by default; --flex-all
# overrides).
FLEX = [
    "ma1_column_validation_usd",   # MA1
    "ma2_wave_validation_usd",     # MA2
    "ma4_min_yield_l",             # MA4 -- the case's own documented flip dial
    "ma5_budget_cap_usd",          # MA5
    "yield_scale_l_per_l",         # MA6 proxy
    "wave_working_volume_l",       # MA7 proxy
]


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})

    net_yield = p["yield_scale_l_per_l"]
    column_volume_l = COLUMN_NOMINAL_L * COLUMN_FILL_FRAC          # fixed, sourced
    wave_volume_l = p["wave_working_volume_l"]

    column_total_yield_l = net_yield * column_volume_l
    wave_total_yield_l = net_yield * wave_volume_l

    column_cost_usd = COLUMN_VESSEL_COST_USD + p["ma1_column_validation_usd"]
    wave_cost_usd = WAVE_VESSEL_COST_USD + p["ma2_wave_validation_usd"]

    column_feasible = (column_total_yield_l >= p["ma4_min_yield_l"]
                        and column_cost_usd <= p["ma5_budget_cap_usd"])
    wave_feasible = (wave_total_yield_l >= p["ma4_min_yield_l"]
                      and wave_cost_usd <= p["ma5_budget_cap_usd"])

    column_metric = (column_total_yield_l / column_cost_usd) if column_feasible else 0.0
    wave_metric = (wave_total_yield_l / wave_cost_usd) if wave_feasible else 0.0

    return {"A": column_metric, "B": wave_metric}


def raw_ratio(params=None):
    """Not part of the Tier 2 contract -- the un-gated yield-per-dollar ratio
    (ignores MA4/MA5 disqualification), used only to reproduce
    case.json.balance.margin_pct (12.4%) for verification."""
    p = dict(PARAMS)
    p.update(params or {})
    net_yield = p["yield_scale_l_per_l"]
    column_total_yield_l = net_yield * COLUMN_NOMINAL_L * COLUMN_FILL_FRAC
    wave_total_yield_l = net_yield * p["wave_working_volume_l"]
    column_cost_usd = COLUMN_VESSEL_COST_USD + p["ma1_column_validation_usd"]
    wave_cost_usd = WAVE_VESSEL_COST_USD + p["ma2_wave_validation_usd"]
    return {"A": column_total_yield_l / column_cost_usd,
            "B": wave_total_yield_l / wave_cost_usd}


if __name__ == '__main__':
    base = evaluate({})
    raw = raw_ratio({})
    print("base (feasibility-gated) ", {k: round(v, 7) for k, v in base.items()})
    print("raw yield-per-dollar ratio", {k: round(v, 7) for k, v in raw.items()},
          "margin %.1f%%" % (100 * (raw["B"] - raw["A"]) / raw["A"]))
    flipped = evaluate({"ma4_min_yield_l": 12.5})
    print("MA4 flexed to 12.5 L (-50%)", {k: round(v, 7) for k, v in flipped.items()})
