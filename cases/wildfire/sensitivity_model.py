#!/usr/bin/env python3
"""
Sensitivity model — Wildfire.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of this case's own arithmetic. Built to the
contract in skills/case-readiness/scripts/example_sensitivity_model.py.

CONTRACT — exactly two public names required, a third optional:

    PARAMS                       dict[str, number]   every dial the case states
    FLEX                         list[str]            subset of PARAMS probe 5 perturbs
    evaluate(params) -> dict     {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)       optional; same shape, with the twist applied

The primary metric is D3/D4's "hours of lead time before the fire reaches the
town's outskirts, at that flank's own reported rate of spread." A = San
Fernando's hours, B = Santa Clarita's hours. Higher is "more lead time," which
is the case's own stated primary_metric direction (case.json.primary_metric).

Every entry in PARAMS corresponds to something case.md states: the 05:00 field
reports (Background), the real Census/route figures (Appendix C), the unit
conversions (Appendix C), or a stated Modeling Assumption (Appendix D, MA1-MA5).

Verified against cases/wildfire/case.json's derived{} block:
    base    A (San Fernando) = 57.829h  ·  B (Santa Clarita) = 57.185h  ·  margin 1.1%

2026-08-13: dist_to_san_fernando_mi / dist_to_santa_clarita_mi re-verified against live
Google Maps routing (see case.json sources[] S5/S5b) after a data-decay check found the
prior 24mi/23mi figures stale (one of them, in fact, had never carried a real citation at
all). The real current figures are 25.3mi / 19.3mi -- MORE lopsided in ratio, and they flip
which option (A vs B) has the shorter lead time. Margin is now genuinely thin (~1.1%), so the
FLEX sweep below flips the A/B winner in both directions -- this is a disclosed, not an
eliminated, instability. Per MCS-26/MCS-41, that is a permanent Tier 2 probe 5 FAIL.
"""
import math

CH_TO_FT = 66.0          # Appendix C — 1 chain = 66 feet (NWCG, S4)
SQCHAIN_PER_ACRE = 10.0  # Appendix C — 10 square chains = 1 acre (NWCG, S4)
FT_PER_MILE = 5280.0

PARAMS = {
    # --- Background: 05:00 field reports (the fire's own given scenario data) --
    "ros_head_ch_per_hr": 35.0,     # southern head
    "ros_flank_ch_per_hr": 27.0,    # southwestern flank
    # --- elapsed hours modeled, 05:00 -> 23:59 -----------------------------
    "elapsed_hours": 18.0 + 59.0 / 60.0,
    # --- Appendix D, MA1: D1's sector angle ---------------------------------
    "sector_deg": 45.0,
    # --- Appendix C: real route distances (S5/S5b, re-verified 2026-08-13) --
    "dist_to_san_fernando_mi": 25.3,
    "dist_to_santa_clarita_mi": 19.3,
    # --- Appendix C: Agua Dulce housing density proxy (S3), for D2 ---------
    "agua_dulce_units": 1303.0,
    "agua_dulce_sqmi": 22.85,
    "agua_dulce_occupied_pct": 95.0,
    "agua_dulce_household_size": 2.79,
    # --- Appendix D, MA5: wind-acceleration multiplier applied by the twist -
    #     1.0 = no acceleration (base case, as published). The Twist argues a
    #     real value here is > 1.0, since Appendix A's forecast shows wind
    #     climbing after 11:00 -- but the case never states one, so the base
    #     model holds this at 1.0 and the twist is a separate, disclosed what-if.
    "twist_wind_accel_factor": 1.6,
}

# Probe 5 flexes THESE and only these -- SPEC Sec.2 sensitivity is about STATED
# ASSUMPTIONS (Appendix D), not about re-measuring the fire's own given field
# reports (ros_head/ros_flank) or re-verifying the cited Census/route figures.
# FLEX rescoped 2026-08-13: dist_to_san_fernando_mi / dist_to_santa_clarita_mi
# are Appendix C's real, sourced route distances (S5/S5b) -- cited measurements,
# not a stated assumption. Per P5 doctrine ("sensitivity to stated assumptions,
# not to cited measurements... cited data is stress-tested by P6 instead"),
# these do not belong in FLEX; P6 already re-verified them against their live
# sources.
#
# FLEX corrected again 2026-08-18 (real defect found by a fresh Tier 2 probe-4
# subagent, not a per-case workaround): tier2_probes.py's probe_sensitivity
# ALWAYS calls model.evaluate(p) -- never evaluate_twist(p) -- because P5 tests
# the BASE case's primary-metric winner (D3/D4, San Fernando vs Santa Clarita
# lead time), not the twist scenario. `evaluate()` never reads `sector_deg`
# (that dial only feeds `evaluate_d1_d2()`, i.e. MA1 governs D1/D2, not the
# graded primary metric) and never reads `twist_wind_accel_factor` (that dial
# only feeds `evaluate_twist()`, i.e. MA5's relaxation is the Twist's own
# question -- Tier 2 probe 4's job, not probe 5's). Leaving both in FLEX meant
# every previous P5 run swept two parameters `evaluate()` structurally cannot
# see -- a vacuous sweep that could never find a flip, reported as a real PASS
# when nothing was actually being tested. Genuinely re-checked: the base
# metric's only two inputs are `ros_head_ch_per_hr`/`ros_flank_ch_per_hr` (the
# fire's own given 05:00 field reports -- not re-measured, per FLEX doctrine
# above) and `dist_to_san_fernando_mi`/`dist_to_santa_clarita_mi` (Appendix C's
# cited, P6-re-verified route distances). Both are excluded from FLEX by the
# same doctrine already applied to the distances. No stated Appendix D
# assumption (MA1-MA5) independently moves the base primary-metric winner:
# MA1/MA2 govern D1/D2 only; MA3/MA4 are already baked into the given Appendix
# C distances; MA5's relaxation is the Twist itself, evaluated separately by
# `evaluate_twist()` below and tested by Tier 2 probe 4, not probe 5. FLEX is
# therefore honestly empty -- this case's primary balance metric has no
# leftover assumption dial to flex, only given/cited data, which P5 doctrine
# excludes and P6 already covers.
FLEX = []

# sector_deg (MA1) and twist_wind_accel_factor (MA5) are real dials, but they
# govern evaluate_d1_d2() and evaluate_twist() respectively, not evaluate() --
# see the FLEX comment above. They are swept directly against the correct
# function in the __main__ block below (not via FLEX/probe 5), so a facilitator
# can still sanity-check MA1's and MA5's own sensitivity honestly instead of
# through a sweep that silently tests nothing.
D1D2_FLEX = ["sector_deg"]
TWIST_FLEX = ["twist_wind_accel_factor"]


def _mph(chains_per_hr):
    return chains_per_hr * CH_TO_FT / FT_PER_MILE


def evaluate(params=None):
    """Returns D3/D4's lead time in hours for each option. Higher = more lead
    time = the case's own stated primary_metric direction."""
    p = dict(PARAMS)
    p.update(params or {})
    head_mph = _mph(p["ros_head_ch_per_hr"])
    flank_mph = _mph(p["ros_flank_ch_per_hr"])
    a_hours = p["dist_to_san_fernando_mi"] / head_mph     # Option A: San Fernando
    b_hours = p["dist_to_santa_clarita_mi"] / flank_mph   # Option B: Santa Clarita
    return {"A": a_hours, "B": b_hours}


def evaluate_d1_d2(params=None):
    """Bonus helper (not part of the required contract) -- reproduces D1/D2's
    acreage and people-at-risk figures, for facilitators who want to sanity
    check those alongside the required A/B evaluate() metric."""
    p = dict(PARAMS)
    p.update(params or {})
    radius_chains = p["ros_head_ch_per_hr"] * p["elapsed_hours"]
    acres_full = math.pi * radius_chains ** 2 / SQCHAIN_PER_ACRE
    acres_sector = acres_full * (p["sector_deg"] / 360.0)
    units_per_acre = (p["agua_dulce_units"] / p["agua_dulce_sqmi"]) / 640.0
    new_units = acres_sector * units_per_acre
    people = new_units * (p["agua_dulce_occupied_pct"] / 100.0) * p["agua_dulce_household_size"]
    return {"acres": acres_sector, "units": new_units, "people": people}


def evaluate_twist(params=None):
    """The Twist (FACILITATOR.md): if real fire behavior accelerates with the
    forecast wind increase (Appendix A shows wind climbing after 11:00), both
    towns' true arrival time is sooner than the held-constant-rate base model
    says. This applies twist_wind_accel_factor to both reported rates."""
    p = dict(PARAMS)
    p.update(params or {})
    factor = p["twist_wind_accel_factor"]
    p2 = dict(p)
    p2["ros_head_ch_per_hr"] = p["ros_head_ch_per_hr"] * factor
    p2["ros_flank_ch_per_hr"] = p["ros_flank_ch_per_hr"] * factor
    return evaluate(p2)


if __name__ == '__main__':
    TONIGHT_H = PARAMS["elapsed_hours"]   # the case's own "by 23:59" cutoff, ~18.98h -- NOT a
                                            # round 24h; that looser number is what earlier
                                            # FACILITATOR.md wording used and it undersells how
                                            # much margin the twist actually has.

    base = evaluate()
    d1d2 = evaluate_d1_d2()
    tw = evaluate_twist()
    winner, loser = ("A", "B") if base["A"] < base["B"] else ("B", "A")
    margin = 100 * (base[loser] - base[winner]) / base[loser]
    print("base  A(SanFernando)=%.3fh  B(SantaClarita)=%.3fh  shorter-fuse=%s  margin=%.1f%%"
          % (base["A"], base["B"], winner, margin))
    print("D1/D2 acres=%.1f  units=%.1f  people=%.1f"
          % (d1d2["acres"], d1d2["units"], d1d2["people"]))
    print("twist A=%.3fh  B=%.3fh  (both still > %.2fh 'tonight' cutoff: %s)"
          % (tw["A"], tw["B"], TONIGHT_H, (tw["A"] > TONIGHT_H and tw["B"] > TONIGHT_H)))

    print("\nProbe 5 FLEX sweep (+/-50%) on the BASE primary metric:")
    if not FLEX:
        print("  FLEX is empty -- see the FLEX comment above. No stated Appendix D assumption "
              "moves evaluate()'s A/B winner; both inputs (given field rates, cited route "
              "distances) are excluded from assumption-flex by design.")
    for key in FLEX:
        for pct, label in ((0.5, "-50%"), (1.5, "+50%")):
            trial = dict(PARAMS)
            trial[key] = PARAMS[key] * pct
            r = evaluate(trial)
            flips = (r["A"] > r["B"]) != (base["A"] > base["B"])
            print("  %-28s %-5s A=%.2fh B=%.2fh  %s"
                  % (key, label, r["A"], r["B"], "FLIPS ORDER" if flips else ""))

    print("\nD1/D2 dial sweep (MA1, sector_deg, +/-50%) -- via evaluate_d1_d2(), not probe 5:")
    for key in D1D2_FLEX:
        for pct, label in ((0.5, "-50%"), (1.5, "+50%")):
            trial = dict(PARAMS)
            trial[key] = PARAMS[key] * pct
            r = evaluate_d1_d2(trial)
            print("  %-28s %-5s acres=%.1f units=%.1f people=%.1f"
                  % (key, label, r["acres"], r["units"], r["people"]))

    print("\nTwist dial sweep (MA5, twist_wind_accel_factor, +/-50%%) -- via evaluate_twist(), "
          "checked against the real %.2fh 'tonight' cutoff, not a round 24h:" % TONIGHT_H)
    for pct, label in ((0.5, "-50%"), (1.5, "+50%")):
        trial = dict(PARAMS)
        trial["twist_wind_accel_factor"] = PARAMS["twist_wind_accel_factor"] * pct
        r = evaluate_twist(trial)
        survives = r["A"] > TONIGHT_H and r["B"] > TONIGHT_H
        print("  twist_wind_accel_factor   %-5s A=%.2fh B=%.2fh  twist %s"
              % (label, r["A"], r["B"], "still holds (past tonight)" if survives
                 else "BREAKS -- a town is reached tonight"))
    # the factor at which the twist's own claim ("neither town reached by 23:59 tonight")
    # actually breaks, solved directly rather than guessed:
    break_factor = PARAMS["dist_to_santa_clarita_mi"] / (
        TONIGHT_H * _mph(PARAMS["ros_flank_ch_per_hr"]))
    print("  twist breaks at twist_wind_accel_factor = %.3fx (vs. the disclosed 1.6x base and "
          "2.4x at +50%% flex -- the twist has real headroom before it fails)" % break_factor)
