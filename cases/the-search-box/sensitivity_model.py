#!/usr/bin/env python3
"""
Sensitivity model — The Search Box.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the contract
and worked reference (Cold Chain).

CONTRACT:
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset that is a stated
                                                     Modeling Assumption
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better

The metric returned is each option's estimated probability of detection (POD)
per flight-hour — case.md's own D5 decision-table quantity and
case.json.balance's primary metric — reproducing the same D1-D5 chain
FACILITATOR.md and case.json.balance.computed_2026-08-30 record:

    E(t)   = growth_rate_kt * elapsed_time_hr            (50%-containment radius)
    R      = search_factor * E(t)                         (search radius)
    area   = (2 * R) ** 2                                  (D3's rectangular box,
                                                             side 2R, centered on
                                                             the drifted datum)
    C      = (sweep_width_nm * search_speed_kt * search_endurance_hr) / area
    POD    = 1 - e^(-C)                                    (S5, Normal Search
                                                             Conditions)
    POS    = POD * POC                                     (POC = probability of
                                                             containment, Appendix E)
    metric = POS / search_endurance_hr                     (POD per flight-hour,
                                                             case.json.balance.
                                                             computed_2026-08-30.
                                                             option_*.POD_per_flighthour)

Fixed (not in FLEX[]): elapsed_time_hr (MA2), search_endurance_hr (MA3),
sweep_width_nm/search_speed_kt (S1/S2, sourced), search_factor (S10's fs=1.1,
a fixed methodology constant, not a per-case assumption), growth_rate_A_kt
(S3's sourced 0.35 kt/hr leeway standard error), and poc_B_pct (S8's sourced
64.75% single-point-datum POC). None of these are stated as flippable in
case.json.modeling_assumptions (MA1-MA11 all carry "flippable": false, and the
sourced figures are cited data, not assumptions -- SPEC Sec2 sensitivity is
for STATED ASSUMPTIONS, not for re-litigating a cited measurement).

FLEX[] carries exactly the two dials case.json marks "flippable": true --
MA12 (Option B's un-sourced search-radius growth-rate constant) and MA13
(Option A's un-sourced divergent-datum POC) -- the same two Appendix F itself
already calls out in prose as able to flip the recommendation.

Verified against case.json.balance.computed_2026-08-30 (2026-08-31):
    base    A (Windward)     = 0.1447   B (Set-and-Drift) = 0.1704
            (POD_per_flighthour, both options POD-saturated ~1.0; matches
            case.json to 4 decimal places)
"""
import math

# --- Fixed: cited data (sources[] S1, S2, S3's growth-rate figure, S8, S10) or
#     a non-flippable Modeling Assumption (case.json marks MA1-MA11 all
#     "flippable": false) -----------------------------------------------------
ELAPSED_TIME_HR = 2.5          # MA2, flippable: false
SEARCH_ENDURANCE_HR = 3.8      # MA3 (net of S6's 85% rule), flippable: false
SWEEP_WIDTH_NM = 0.4           # S2, sourced
SEARCH_SPEED_KT = 90.0         # S1, sourced
SEARCH_FACTOR = 1.1            # S10, fixed methodology constant (fs)

PARAMS = {
    # --- Option A (Windward Datum / wind-driven leeway model) ---------------
    "growth_rate_A_kt": 0.35,      # S3 — sourced leeway-speed standard error
    "poc_A_pct": 0.55,             # MA13 — NOT sourced (flippable: true)
    # --- Option B (Set-and-Drift Datum / current-driven model) --------------
    "growth_rate_B_kt": 0.45,      # MA12 — NOT sourced (flippable: true)
    "poc_B_pct": 0.6475,           # S8 — sourced single-point-datum POC
}

# Probe 5 flexes THESE and only these -- the two dials case.json itself marks
# "flippable": true (MA12, MA13). Every other Appendix C/D/E figure is either
# cited (S1/S2/S3/S8/S10) or a Modeling Assumption the case itself records as
# non-flippable (MA1-MA11, all box-location-only or shared-by-both-options
# scalars per case.json). --flex-all overrides this scoping.
FLEX = [
    "poc_A_pct",        # MA13 — Windward Datum's assumed POC
    "growth_rate_B_kt",  # MA12 — Set-and-Drift's search-radius growth rate
]


def _pod_per_flighthour(growth_rate_kt, poc_pct):
    e_t = growth_rate_kt * ELAPSED_TIME_HR
    r = SEARCH_FACTOR * e_t
    area = (2.0 * r) ** 2
    if area <= 0:
        return 0.0
    c = (SWEEP_WIDTH_NM * SEARCH_SPEED_KT * SEARCH_ENDURANCE_HR) / area
    pod = 1.0 - math.exp(-c)
    pos = pod * poc_pct
    return pos / SEARCH_ENDURANCE_HR


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    a = _pod_per_flighthour(p["growth_rate_A_kt"], p["poc_A_pct"])
    b = _pod_per_flighthour(p["growth_rate_B_kt"], p["poc_B_pct"])
    return {"A": a, "B": b}


if __name__ == '__main__':
    base = evaluate({})
    print("base", {k: round(v, 4) for k, v in base.items()},
          "margin(win-denom) %.2f%%" % (100 * (base["B"] - base["A"]) / base["B"]))

    # MA12 +/-50%
    for mult, label in ((0.5, "-50%"), (1.5, "+50%")):
        r = evaluate({"growth_rate_B_kt": PARAMS["growth_rate_B_kt"] * mult})
        print("MA12 growth_rate_B_kt %s -> %.6f" % (label, PARAMS["growth_rate_B_kt"] * mult),
              {k: round(v, 4) for k, v in r.items()}, "winner", max(r, key=r.get))

    # MA13 +/-50%
    for mult, label in ((0.5, "-50%"), (1.5, "+50%")):
        v = min(1.0, PARAMS["poc_A_pct"] * mult)
        r = evaluate({"poc_A_pct": v})
        print("MA13 poc_A_pct %s -> %.6f" % (label, v),
              {k: round(v2, 4) for k, v2 in r.items()}, "winner", max(r, key=r.get))

    # bisection: find the MA12 growth-rate-B threshold where the winner flips
    lo, hi = 1e-6, PARAMS["growth_rate_B_kt"]
    for _ in range(60):
        mid = (lo + hi) / 2
        r = evaluate({"growth_rate_B_kt": mid})
        if r["B"] > r["A"]:
            hi = mid
        else:
            lo = mid
    print("MA12 flip threshold (growth_rate_B_kt, holding MA13 fixed): ~%.4f kt" % hi)

    # bisection: find the MA13 poc_A threshold where the winner flips
    lo, hi = PARAMS["poc_A_pct"], 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        r = evaluate({"poc_A_pct": mid})
        if r["A"] > r["B"]:
            hi = mid
        else:
            lo = mid
    print("MA13 flip threshold (poc_A_pct, holding MA12 fixed): ~%.4f (%.1f%%)" % (hi, hi * 100))
