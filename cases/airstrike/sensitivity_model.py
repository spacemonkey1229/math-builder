#!/usr/bin/env python3
"""
Sensitivity model — Airstrike.

Tier 2 probe 5 ("flex each stated assumption by +-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. This is that
model, built from case.md Appendix A (site coordinates + warhead classes),
Appendix B (population-at-risk table), Appendix C (real, cited hardware
specs), and Appendix D (stated Modeling Assumptions MA1-MA4).

CONTRACT:
    PARAMS                       dict[str, number]   every dial the case states
    FLEX                         list[str]            subset of PARAMS probe 5 perturbs
    evaluate(params) -> dict     {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)       same shape, with the twist (3rd F-16) applied

Metric is total expected population protected (people), higher is better for
both A (Grey Dawn) and B (Desert Sparrow) — the case's balance test compares
these two directly (case.json.balance.margin_basis).

Verified against case.json.derived:
    base (2 jets)   A = 5,158,000  B = 5,918,400   margin (B over A) = 14.7%
    twist (3 jets)  A = 6,810,000  B = 7,126,400   margin (B over A) = 4.6%
"""
import math

UNIT_KM = 10.0            # case.md Appendix A: each grid unit = 10 km
CAMP = (2, -19)

# name -> (x, y, type, warhead_class)
SITES = {
    "ICBM-Alpha":   (6, 9, "ICBM", "5.2MT"),
    "ICBM-Bravo":   (-3, 7.5, "ICBM", "100kt"),
    "ICBM-Charlie": (10, 0, "ICBM", "1MT"),
    "ICBM-Delta":   (-8, -4, "ICBM", "3.1MT"),
    "ICBM-Echo":    (1, -8.5, "ICBM", "50kt"),
    "ICBM-Foxtrot": (-7, -1, "ICBM", "5.2MT"),
    "ICBM-Golf":    (-17, -13, "ICBM", "1MT"),
    "ICBM-Hotel":   (-14, 11, "ICBM", "3.1MT"),
    "ICBM-India":   (13, 12.5, "ICBM", "50kt"),
    "SRBM-Alpha":   (-3, 4, "SRBM", "5.2MT"),
    "SRBM-Bravo":   (10, 4, "SRBM", "100kt"),
    "SRBM-Charlie": (14, -2, "SRBM", "1MT"),
    "SRBM-Delta":   (-17, 7, "SRBM", "3.1MT"),
    "SRBM-Echo":    (-2, 14, "SRBM", "50kt"),
    "SRBM-Foxtrot": (1, -13, "SRBM", "5.2MT"),
}

PARAMS = {
    # --- Appendix C, sourced (S1) --------------------------------------------
    "speed_kmh": 2400.0,
    # --- Appendix D, MA1 -------------------------------------------------------
    "fire_standoff_km": 2.0,
    # --- Background: hard deadline ---------------------------------------------
    "window_min_base": 12.0,
    # --- FACILITATOR.md Twist: 3rd jet launches this many minutes later ---------
    "twist_delay_min": 2.0,
    # --- Appendix D, MA2 (the case's single most load-bearing assumption) -------
    "srbm_intercept_rate": 0.056,
    # --- Appendix B, MA3: population-at-risk per warhead class -----------------
    # 2026-08-13: derived, not assumed. pop = pi*R^2*density, R = 4.8km*(Y/100kt)^(1/3)
    # (Glasstone & Dolan cube-root blast scaling, S4), density = 2716/sq mi (real
    # Census-derived U.S. average across all central cities in 2000, S5 -- corrected
    # 2026-08-18: earlier draft mislabeled this "2020" and "2716.38" [the ".38" was
    # the source's footnote marker, not a decimal]. See Appendix D MA3, QA_REPORT.md.
    "pop_5_2MT": 1_057_614.0,
    "pop_3_1MT": 749_145.0,
    "pop_1MT": 352_364.0,
    "pop_100kt": 75_915.0,
    "pop_50kt": 47_823.0,
}

# Probe 5 flexes THESE and only these — SPEC §2 asks for sensitivity to STATED
# ASSUMPTIONS, not to cited measurements. speed_kmh (S1) and the ICBM/SRBM
# range specs (S2/S3) are cited data, not assumptions, so they are NOT flexed
# here — they'd be a data-decay probe (P6) concern, not a P5 one.
FLEX = [
    "fire_standoff_km",        # MA1 -- negligible effect (see FACILITATOR.md check)
    "srbm_intercept_rate",     # MA2 -- the load-bearing one; can flip the margin's size
    "pop_5_2MT", "pop_3_1MT", "pop_1MT", "pop_100kt", "pop_50kt",   # MA3
    "twist_delay_min",         # scenario construction (FACILITATOR.md Twist)
]

_YIELD_KEY = {"5.2MT": "pop_5_2MT", "3.1MT": "pop_3_1MT", "1MT": "pop_1MT",
              "100kt": "pop_100kt", "50kt": "pop_50kt"}


def _dist_km(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1]) * UNIT_KM


def _leg_time_min(p, dist_km):
    flight_km = max(dist_km - p["fire_standoff_km"], 0.0)
    return flight_km / (p["speed_kmh"] / 60.0)


def _pop_value(p, name, discount_srbm=True):
    x, y, typ, wh = SITES[name]
    v = p[_YIELD_KEY[wh]]
    if typ == "SRBM" and discount_srbm:
        v = v * (1.0 - p["srbm_intercept_rate"])
    return v


def _nearest_neighbor_route(p, start, candidates, time_budget_min):
    """Greedy nearest-neighbor route from `start` through `candidates` (a dict
    of name -> site tuple), stopping when the next leg would exceed the
    remaining time budget. Returns (destroyed_names, remaining_names)."""
    pos = start
    t = 0.0
    remaining = dict(candidates)
    destroyed = []
    while remaining:
        best_name, best_d = None, None
        for name, (x, y, typ, wh) in remaining.items():
            d = _dist_km(pos, (x, y))
            if best_d is None or d < best_d:
                best_d, best_name = d, name
        leg_t = _leg_time_min(p, best_d)
        if t + leg_t > time_budget_min + 1e-9:
            break
        t += leg_t
        destroyed.append(best_name)
        pos = (remaining[best_name][0], remaining[best_name][1])
        del remaining[best_name]
    return destroyed, remaining


def _grey_dawn_2jet(p):
    icbm = {k: v for k, v in SITES.items() if v[2] == "ICBM"}
    srbm = {k: v for k, v in SITES.items() if v[2] == "SRBM"}
    west_icbm = {k: v for k, v in icbm.items() if v[0] < 0}
    east_icbm = {k: v for k, v in icbm.items() if v[0] >= 0}
    west_srbm = {k: v for k, v in srbm.items() if v[0] < 0}
    east_srbm = {k: v for k, v in srbm.items() if v[0] >= 0}

    budget = p["window_min_base"]
    destroyed = []
    for icbm_half, srbm_half in ((west_icbm, west_srbm), (east_icbm, east_srbm)):
        icbm_hit, _ = _nearest_neighbor_route(p, CAMP, icbm_half, budget)
        t_used = sum(_leg_time_min(p, _dist_km(
            CAMP if i == 0 else (icbm_half[icbm_hit[i - 1]][0], icbm_half[icbm_hit[i - 1]][1]),
            (icbm_half[n][0], icbm_half[n][1])
        )) for i, n in enumerate(icbm_hit))
        last_pos = CAMP if not icbm_hit else (icbm_half[icbm_hit[-1]][0], icbm_half[icbm_hit[-1]][1])
        srbm_hit, _ = _nearest_neighbor_route(p, last_pos, srbm_half, budget - t_used)
        destroyed += icbm_hit + srbm_hit
    return destroyed


def _desert_sparrow_2jet(p):
    west_all = {k: v for k, v in SITES.items() if v[0] < 0}
    east_all = {k: v for k, v in SITES.items() if v[0] >= 0}
    destroyed = []
    for half in (west_all, east_all):
        hit, _ = _nearest_neighbor_route(p, CAMP, half, p["window_min_base"])
        destroyed += hit
    return destroyed


def evaluate(params=None):
    p = dict(PARAMS)
    p.update(params or {})
    a_destroyed = _grey_dawn_2jet(p)
    b_destroyed = _desert_sparrow_2jet(p)
    a = sum(_pop_value(p, n) for n in a_destroyed)
    b = sum(_pop_value(p, n) for n in b_destroyed)
    return {"A": a, "B": b}


def evaluate_twist(params=None):
    """3rd F-16 becomes available after `twist_delay_min` minutes, giving it a
    shorter window. It mops up whatever each operation's 2-jet route left
    live, using the same nearest-neighbor rule."""
    p = dict(PARAMS)
    p.update(params or {})
    twist_budget = p["window_min_base"] - p["twist_delay_min"]

    a_destroyed = _grey_dawn_2jet(p)
    a_left = {k: v for k, v in SITES.items() if k not in a_destroyed}
    a_third, _ = _nearest_neighbor_route(p, CAMP, a_left, twist_budget)
    a_all = a_destroyed + a_third

    b_destroyed = _desert_sparrow_2jet(p)
    b_left = {k: v for k, v in SITES.items() if k not in b_destroyed}
    b_third, _ = _nearest_neighbor_route(p, CAMP, b_left, twist_budget)
    b_all = b_destroyed + b_third

    a = sum(_pop_value(p, n) for n in a_all)
    b = sum(_pop_value(p, n) for n in b_all)
    return {"A": a, "B": b}


if __name__ == '__main__':
    base = evaluate()
    tw = evaluate_twist()
    margin_base = 100 * (base["B"] - base["A"]) / base["A"]
    margin_tw = 100 * (tw["B"] - tw["A"]) / tw["A"]
    print("base ", {k: round(v) for k, v in base.items()}, "margin(B over A) %.1f%%" % margin_base)
    print("twist", {k: round(v) for k, v in tw.items()}, "margin(B over A) %.1f%%" % margin_tw)
