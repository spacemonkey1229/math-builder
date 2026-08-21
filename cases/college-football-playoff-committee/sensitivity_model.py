#!/usr/bin/env python3
"""
Sensitivity model -- College Football Playoff Committee.

Tier 2 probe 5 flexes each stated modeling assumption (Appendix F) by +-50%
and reports whether the winner flips. CONTRACT: PARAMS, evaluate(params).

A = Oklahoma's Composite Selection Score, B = Michigan's Composite Selection
Score (higher wins -- SPEC's standard "A vs B on one shared metric" shape,
matches case.json.balance exactly: base A~66.08, B~73.79, margin ~11.67%).
"""

# Appendix B -- AP voting points (out of the confirmed max, 63 x 25 = 1575)
OKLAHOMA_AP = 1382
MICHIGAN_AP = 1048
AP_MAX = 63 * 25  # MA2: confirmed by Georgia's 1,575 = 63 x 25

# Appendix C -- SRS (Simple Rating System)
OKLAHOMA_SRS = 11.52
MICHIGAN_SRS = 21.02
SRS_CEILING = 25.94  # MA3: Georgia's SRS, the highest of the full ~130-team dataset

PARAMS = {
    # MA2: denominator for the Human% score.
    "ap_max": AP_MAX,
    # MA3: denominator for the Machine% score -- the ceiling team's SRS.
    "srs_ceiling": SRS_CEILING,
    # MA4: weight given to the Human score in the 50/50 composite (the
    # single most load-bearing assumption per Appendix F/case.json.
    # human_weight=0.5 is the case's stated unweighted mean;
    # machine_weight is always 1 - human_weight.
    "human_weight": 0.5,
}

FLEX = ["ap_max", "srs_ceiling", "human_weight"]


def _composite(ap_points, srs, p):
    human_pct = 100 * ap_points / p["ap_max"]
    machine_pct = 100 * srs / p["srs_ceiling"]
    return p["human_weight"] * human_pct + (1 - p["human_weight"]) * machine_pct


def evaluate(params):
    p = dict(PARAMS); p.update(params or {})
    a = _composite(OKLAHOMA_AP, OKLAHOMA_SRS, p)
    b = _composite(MICHIGAN_AP, MICHIGAN_SRS, p)
    return {"A": a, "B": b}


if __name__ == '__main__':
    base = evaluate({})
    margin = 100 * (max(base.values()) - min(base.values())) / min(base.values())
    print("base", {k: round(v, 2) for k, v in base.items()}, "margin %.2f%%" % margin)
