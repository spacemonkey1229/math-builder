#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Pattern Rights.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of this case's own arithmetic. Contract per
skills/case-readiness/scripts/example_sensitivity_model.py:

    PARAMS                     dict[str, number]   every dial the case STATES
    FLEX                       list[str]            the subset that is an ASSUMPTION
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     optional; NOT provided here -- see note below

PRIMARY METRIC (case.json.primary_metric): total printed yards producible
from one engraved cylinder, per dollar of one-time engraving setup cost
("yards per dollar of setup cost"). evaluate() returns exactly that for each
option, A = The Straight Set, B = The Half-Drop. Higher is better.

WHY NO evaluate_twist(). This case's "Twist" (FACILITATOR.md) is not a change
of assumption or a scenario perturbation -- it is a sequencing move. Heroes
compute D1/D2 (configuration counts, capsule counts) first, see The Half-Drop
"win" on those numbers, and only then are told to compute D4 (yards per
dollar), which reverses the recommendation. evaluate() already computes the
real primary metric D4 represents; there is no second, twisted arithmetic to
model -- the "twist" is which deliverable a Hero was looking at, not a change
to any input. Tier 2 P4 (twist integrity) is answered directly by this file's
docstring and by FACILITATOR.md, not by a second evaluate_twist() branch.

FLEX-SCOPING (2026-08-13 doctrine note). Only genuine, case-chosen
assumptions belong in FLEX -- never cited/given data (P6 covers that). Here:
  - screen_life_m (Appendix D, MA1) IS an assumption: the case's own source
    [S3] gives a 30,000-50,000 meter RANGE, not a scheme-specific figure, and
    the case chose the conservative low end. A stated choice among a sourced
    range -- flex it.
  - setup_cost_straight_usd / setup_cost_half_drop_usd (Appendix D, MA2) ARE
    assumptions: no current, scheme-specific engraving price exists anywhere
    (RESEARCH_LOG.md P05/P06 -- both NOT FOUND), so both dollar figures are
    stated scenario values, not sourced data. This is the case's single most
    load-bearing dial per Appendix D's own sensitivity note.
  - fabric_width_in (54", Appendix B) is NOT flexed: it is sourced to [S1]
    and corroborated across three independent commercial listings -- real,
    cited data, not a choice the case made. P6 (data decay) stress-tests it.
  - column_width_in / column_height_in (18"/27", Appendix A) are NOT flexed:
    they are the artwork's own fixed given dimensions, identical for both
    schemes by construction, not an assumption either scheme's design chose.
  - colorways (4) and capsule_k (2) are NOT flexed: fixed licensing terms
    stated in Appendix A ("Licensing terms fixed for both schemes"), not a
    dial this case had to estimate.
  - The structural choice-counts (half_drop_mirror_states = 2, i.e. each
    Half-Drop column may run mirrored or as-drawn) and the floral-element
    counts per true tile (6 / 12) are NOT flexed either: they follow directly
    from Appendix A's stated geometry (a half-drop's true tile is 2x one
    column's width, corrected and sourced at S5 -- see RESEARCH_LOG.md), not
    from an estimate the case chose among alternatives.

Verified against cases/pattern-rights/case.json.derived (2026-08-15):
    base   A = 50.47 yd/$  ·  B = 43.74 yd/$  ·  margin 13.3% (A wins)
    D1     config counts:   A = 4   B = 8
    D2     capsule counts:  A = C(6,2) = 15   B = C(12,2) = 66
    D3     pigeonhole:      A = 5   B = 9   (actual run: 131,232 units)
"""
import math
from itertools import combinations

INCH_PER_M = 39.3701          # exact conversion factor used throughout case.json.derived

PARAMS = {
    # --- Appendix A: licensing terms fixed for both schemes (given, not flexed)
    "colorways": 4,
    "capsule_k": 2,
    "column_width_in": 18,
    "column_height_in": 27,
    # --- Appendix A: structural choice-count / true-tile geometry (given, not flexed)
    "half_drop_mirror_states": 2,       # independent mirror-or-as-drawn choice per Half-Drop column
    "floral_elements_straight": 6,      # floral elements per Straight Set true repeating tile
    "floral_elements_half_drop": 12,    # floral elements per Half-Drop true repeating tile (2x, see S5)
    # --- Appendix B: real printable fabric width (sourced S1, not flexed)
    "fabric_width_in": 54,
    # --- Appendix D, MA1: which end of the sourced 30,000-50,000 m range (ASSUMPTION, flexed)
    "screen_life_m": 30000,
    # --- Appendix D, MA2: one-time engraving setup cost per scheme (ASSUMPTION, flexed)
    "setup_cost_straight_usd": 650.0,
    "setup_cost_half_drop_usd": 750.0,
}

# Probe 5 flexes THESE and only these -- see the FLEX-SCOPING note above.
FLEX = [
    "screen_life_m",                # Appendix D, MA1
    "setup_cost_straight_usd",      # Appendix D, MA2
    "setup_cost_half_drop_usd",     # Appendix D, MA2
]


def config_counts(p=None):
    """D1 -- Fundamental Counting Principle. Straight Set: colorways only
    (no independent mirror stage). Half-Drop: colorways x mirror-state."""
    p = dict(PARAMS) if p is None else {**PARAMS, **p}
    a = p["colorways"] * 1
    b = p["colorways"] * p["half_drop_mirror_states"]
    return {"A": a, "B": b}


def capsule_counts(p=None):
    """D2 -- binomial coefficient C(n, k) of floral elements per true tile."""
    p = dict(PARAMS) if p is None else {**PARAMS, **p}
    k = p["capsule_k"]
    a = math.comb(p["floral_elements_straight"], k)
    b = math.comb(p["floral_elements_half_drop"], k)
    return {"A": a, "B": b}


def pigeonhole_thresholds(p=None):
    """D3 -- Pigeonhole Principle: configuration count + 1 pigeons guarantees
    a repeat, for each scheme."""
    cc = config_counts(p)
    return {"A": cc["A"] + 1, "B": cc["B"] + 1}


def yardage(p=None):
    """Shared D4(a) geometry: repeat units across width x repeat units along
    one engraving's rated run -- identical for both schemes (same cylinder
    circumference, same screen life)."""
    p = dict(PARAMS) if p is None else {**PARAMS, **p}
    repeats_across = math.floor(p["fabric_width_in"] / p["column_width_in"])
    screen_life_in = p["screen_life_m"] * INCH_PER_M
    screen_life_yards = screen_life_in / 36.0
    repeats_along = math.floor(screen_life_in / p["column_height_in"])
    total_units = repeats_across * repeats_along
    return {
        "repeats_across": repeats_across,
        "repeats_along": repeats_along,
        "total_repeat_units": total_units,
        "screen_life_yards": screen_life_yards,
    }


def evaluate(params=None):
    """D4(a) -- primary metric: yards per dollar of one-time engraving setup
    cost. Both schemes share identical total yardage from one engraving; the
    only difference is setup cost. Higher is better."""
    p = dict(PARAMS); p.update(params or {})
    yd = yardage(p)
    a = yd["screen_life_yards"] / p["setup_cost_straight_usd"]
    b = yd["screen_life_yards"] / p["setup_cost_half_drop_usd"]
    return {"A": a, "B": b}


def evaluate_capsule_per_dollar(params=None):
    """D4(b) -- secondary figure: capsule-variant count per dollar of setup
    cost. Not the primary metric; included because the case's own D4 asks
    for it alongside D4(a)."""
    p = dict(PARAMS); p.update(params or {})
    cap = capsule_counts(p)
    return {
        "A": cap["A"] / p["setup_cost_straight_usd"],
        "B": cap["B"] / p["setup_cost_half_drop_usd"],
    }


def margin_pct(result):
    """Matches case.json's own margin convention: 100 * (winner - loser) /
    winner (NOT / loser) -- verified this is the formula that reproduces the
    case's recorded 13.3% from 50.47 vs 43.74 yards/$."""
    a, b = result["A"], result["B"]
    hi, lo = (a, b) if a >= b else (b, a)
    if hi == 0:
        return 0.0
    return 100.0 * (hi - lo) / hi


if __name__ == '__main__':
    base = evaluate({})
    print("D1 config counts       ", config_counts())
    print("D2 capsule counts (k=2)", capsule_counts())
    print("D3 pigeonhole thresholds", pigeonhole_thresholds())
    yd = yardage()
    print("D4(a) yardage geometry  ", yd)
    print("D4(a) primary metric    ", {k: round(v, 2) for k, v in base.items()},
          "margin %.1f%%" % margin_pct(base))
    print("D4(b) capsule/$ (secondary)", {k: round(v, 4) for k, v in evaluate_capsule_per_dollar().items()})

    # Self-check against case.json.derived, recorded 2026-08-15.
    expect = {
        "config_count_straight_set": config_counts()["A"], "config_count_half_drop": config_counts()["B"],
        "capsule_count_straight_set": capsule_counts()["A"], "capsule_count_half_drop": capsule_counts()["B"],
        "pigeonhole_threshold_straight_set": pigeonhole_thresholds()["A"],
        "pigeonhole_threshold_half_drop": pigeonhole_thresholds()["B"],
        "repeats_across_width": yd["repeats_across"], "repeats_along_length": yd["repeats_along"],
        "total_repeat_units_per_engraving": yd["total_repeat_units"],
    }
    checks = {
        "config_count_straight_set": 4, "config_count_half_drop": 8,
        "capsule_count_straight_set": 15, "capsule_count_half_drop": 66,
        "pigeonhole_threshold_straight_set": 5, "pigeonhole_threshold_half_drop": 9,
        "repeats_across_width": 3, "repeats_along_length": 43744,
        "total_repeat_units_per_engraving": 131232,
    }
    assert expect == checks, f"MISMATCH vs case.json.derived: {expect} != {checks}"
    assert round(base["A"], 2) == 50.47 and round(base["B"], 2) == 43.74
    assert round(margin_pct(base), 1) == 13.3
    print("\nAll figures reproduce case.json.derived / balance_test exactly.")
