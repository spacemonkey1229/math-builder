#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Heist.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. This is that
model, for cases/heist.

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):

    PARAMS                             dict[str, number]  every dial the case states
    FLEX                               list[str]          subset of PARAMS probe 5 flexes
    evaluate(params) -> dict           {"A": metric, "B": metric}
    evaluate_twist(params) -> dict     same shape, with the twist's own lens applied

Metric direction: this case's primary metric is a PROBABILITY (percent chance
of a fully successful escape), so HIGHER is better here, same convention as
Cold Chain's in-spec-dose count.

evaluate() returns the case's graded primary metric: each option's building-
exit success chance (the two GIVEN, LOCKED dilemma numbers, 94%/98% -- not a
modeling assumption, not flexed by this probe) multiplied by one shared
getaway-drive survival probability, computed by multiplying together a
survival factor for every stated Appendix C risk factor (road-type-per-mile,
stoplights, stop signs, minutes in the vehicle). Matches case.json.balance
(A=71.85%, B=74.91%, margin 4.26%, B wins).

evaluate_twist() applies the stolen-vehicle Twist from FACILITATOR.md: the
crew loses 3 extra minutes to hot-wiring a second car, so the per-minute risk
factor now applies across minutes_in_vehicle + 3 instead of minutes_in_vehicle.
Matches case.json.derived (A=71.27%, B=74.30%, margin still 4.26%).

STRUCTURAL PROPERTY, load-bearing to how this model should be read: because
Option A and Option B share the identical route and the identical Appendix C
risk factors, every one of PARAMS' route-risk dials multiplies BOTH options'
final percentage by the exact same route-survival factor. That factor cancels
out of the A-vs-B RATIO entirely -- so no flex of any FLEX[] entry, in either
direction, can ever change the winner or the margin_pct. This is verified
below (__main__ prints the full sweep) and is the intended, disclosed finding
of running probe 5 on this case, not a bug in the model: see
case.json.sensitivity_note and FACILITATOR.md's "Data Deep Dive" trap.

Verified against case.md / case.json:
    evaluate({})              A = 71.85%  B = 74.91%   margin (B-A)/A = 4.26%   (B wins)
    evaluate_twist({})        A = 71.27%  B = 74.30%   margin (B-A)/A = 4.26%   (B wins, unchanged)
"""

PARAMS = {
    # --- Dilemma: GIVEN, LOCKED exit figures -- NOT modeling assumptions,
    # NOT in FLEX. These are the case's fixed scenario parameters (Four's own
    # scouted numbers) -- see cases/_concepts/LEGACY_DILEMMA_LOCKS_2026-08-20.md.
    "exit_a_success_pct": 94.0,
    "exit_b_success_pct": 98.0,
    "exit_a_seconds": 17,
    "exit_b_seconds": 29,
    "post_alarm_window_seconds": 30,

    # --- Appendix A, S3: real route, real total distance/time ----------------
    "route_total_miles": 8.9,
    "route_total_minutes": 21,

    # --- Appendix C, MA1: this case's own road-type segmentation of the real
    # 8.9-mile route (Google reports one combined distance, not a category
    # breakdown) ---------------------------------------------------------------
    "city_miles": 2.0,
    "highway_miles": 6.4,
    "neighborhood_miles": 0.5,

    # --- Appendix C: per-mile risk by road type (Four's disclosed model,
    # reused verbatim from the original source) -------------------------------
    "city_risk_per_mile": 0.0029,
    "highway_risk_per_mile": 0.012,
    "neighborhood_risk_per_mile": 0.0008,

    # --- Appendix C, MA2/MA3/MA4: stoplight/stop-sign counts and their risk --
    "n_stoplights": 7,
    "stoplight_risk_each": 0.0165,
    "n_stopsigns": 3,
    "stopsign_risk_each": 0.004,

    # --- Appendix C, MA5: per-minute-in-vehicle risk --------------------------
    "minute_risk_each": 0.0027,

    # --- Twist: stolen second vehicle, hot-wired without keys -----------------
    "twist_extra_minutes": 3,

    # --- Appendix B/C, MA6: police-station-proximity bump. Disclosed as NOT
    # applying to the base route (D4's real finding, S4) -- included here so a
    # Hero's alternate-route "what if" exploration has a real number to use. --
    "station_proximity_bump": 0.0,
}

# Probe 5 flexes THESE and only these -- the case's own STATED assumptions
# (Appendix C, none of which is a cited real-world measurement; all are
# Four's disclosed professional judgment reused from the original source),
# not the two GIVEN dilemma parameters (exit_a_success_pct, exit_b_success_pct)
# and not the real, sourced route distance/time (S3), which is stress-tested
# by the data-decay probe (P6) instead, not P5.
FLEX = [
    "city_risk_per_mile",
    "highway_risk_per_mile",
    "neighborhood_risk_per_mile",
    "n_stoplights",
    "stoplight_risk_each",
    "n_stopsigns",
    "stopsign_risk_each",
    "minute_risk_each",
]


def _route_survival(p, minutes):
    s = (1 - p["city_risk_per_mile"]) ** p["city_miles"]
    s *= (1 - p["highway_risk_per_mile"]) ** p["highway_miles"]
    s *= (1 - p["neighborhood_risk_per_mile"]) ** p["neighborhood_miles"]
    s *= (1 - p["stoplight_risk_each"]) ** p["n_stoplights"]
    s *= (1 - p["stopsign_risk_each"]) ** p["n_stopsigns"]
    s *= (1 - p["minute_risk_each"]) ** minutes
    s *= (1 - p["station_proximity_bump"])
    return s


def evaluate(params=None):
    """Primary graded metric: combined P(full successful escape), by option."""
    p = dict(PARAMS)
    p.update(params or {})
    route = _route_survival(p, p["route_total_minutes"])
    return {
        "A": 100 * (p["exit_a_success_pct"] / 100) * route,
        "B": 100 * (p["exit_b_success_pct"] / 100) * route,
    }


def evaluate_twist(params=None):
    """Post-twist lens: +3 minutes in the vehicle (stolen second car)."""
    p = dict(PARAMS)
    p.update(params or {})
    minutes = p["route_total_minutes"] + p["twist_extra_minutes"]
    route = _route_survival(p, minutes)
    return {
        "A": 100 * (p["exit_a_success_pct"] / 100) * route,
        "B": 100 * (p["exit_b_success_pct"] / 100) * route,
    }


def _margin(res):
    lo, hi = min(res, key=res.get), max(res, key=res.get)
    return hi, 100 * (res[hi] - res[lo]) / res[lo]


if __name__ == "__main__":
    base = evaluate({})
    tw = evaluate_twist({})
    bw, bm = _margin(base)
    tww, twm = _margin(tw)
    print("base    A=%.2f%%  B=%.2f%%  margin=%.2f%%  -> %s wins" % (base["A"], base["B"], bm, bw))
    print("twist   A=%.2f%%  B=%.2f%%  margin=%.2f%%  -> %s wins" % (tw["A"], tw["B"], twm, tww))

    print("\n--- FLEX sweep (+/-50%), base case ---")
    for key in FLEX:
        for direction, mult in (("-50%", 0.5), ("+50%", 1.5)):
            flexed = evaluate({key: PARAMS[key] * mult})
            w, m = _margin(flexed)
            flip = " *** FLIP ***" if w != bw else ""
            print("  %-24s %-5s -> A=%.2f%% B=%.2f%% margin=%.2f%% winner=%s%s" %
                  (key, direction, flexed["A"], flexed["B"], m, w, flip))
    print("\nExpected result: no FLEX[] entry ever changes the winner or the margin -- see")
    print("case.json.sensitivity_note. Only exit_a_success_pct/exit_b_success_pct (GIVEN,")
    print("locked, not in FLEX) can move the winner.")
