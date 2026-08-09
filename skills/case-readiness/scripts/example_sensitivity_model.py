#!/usr/bin/env python3
"""
REFERENCE SENSITIVITY MODEL — Cold Chain.

Tier 2 probe 5 ("flex each stated assumption by ±50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic.  A case ships one
at `cases/<id>/sensitivity_model.py`.  This file is the worked example authors
copy; it is deliberately kept inside the skill so it can be executed and diffed
without touching a published case.

CONTRACT — exactly two public names:

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     optional; same shape, with the twist applied

Every entry in PARAMS must correspond to something the case STATES — a modelling
assumption, a rated figure, a convention.  Do not put an authorial fudge factor
in here; if a dial is not in the case, the sensitivity result is about your model
and not about the case.

`allocation_village_priority` is the exception that proves the rule, and it is
the reason this file exists: Cold Chain's published numbers (7,771 in spec, and
6,571 after the twist) are only reproducible if the two motorcycle villages are
served at FULL need and the four truck facilities absorb the entire 429-dose
shortfall.  The case never says that.  Flex this dial and the twist's punchline
moves.  A dial the case does not state is itself a Tier 2 finding.

Verified against cases/cold-chain/case.md and FACILITATOR.md:
    base      A = 7771  ·  B = 7000  ·  margin 11.0%     (matches case.json)
    twist     A = 6571  ·  B = 7000  ·  A below B        (matches FACILITATOR.md)
"""
import math

PARAMS = {
    # --- Appendix F, Assumption 1 -------------------------------------------
    "opening_cost_h": 4.0,
    # --- Appendix F, Assumption 2: cold life IS in-spec time -----------------
    #     Flexing this below 1.0 is the +8/+10 conflation the case was rebuilt
    #     to avoid (QA_REPORT B5).  It is the single most load-bearing dial.
    "in_spec_fraction": 1.0,
    # --- Appendix A, rated cold life ----------------------------------------
    "cold_life_A_h": 132.3,
    "cold_life_B_h": 138.0,
    # --- Appendix D ----------------------------------------------------------
    "vol_per_dose_cm3": 2.1,
    # --- Appendix A, vaccine capacity ---------------------------------------
    "litres_per_box_A": 6.0,
    "litres_per_box_B": 20.0,
    # --- the Twist (FACILITATOR.md) -----------------------------------------
    "twist_detour_h": 9.0,
    # --- UNSTATED. See the docstring.  Domain is [0, 1]; values outside are
    #     clamped, so a +50% flex on a dial already at 1.0 is a no-op by design.
    "allocation_village_priority": 1.0,
}

# Probe 5 flexes THESE and only these.  SPEC §2 asks for sensitivity to STATED
# ASSUMPTIONS, not to cited measurements: halving a WHO-rated cold life is not a
# sensitivity test, it is a different case.  Cited data is stress-tested by the
# data-decay probe (P6) instead.  Run with --flex-all to sweep everything anyway.
FLEX = [
    "opening_cost_h",                 # Appendix F, Assumption 1
    "in_spec_fraction",               # Appendix F, Assumption 2
    "twist_detour_h",                 # scenario construction (FACILITATOR.md)
    "allocation_village_priority",    # unstated convention — the finding
]

BOXES_A, BOXES_B = 3, 2

#   stop, facility,        need, cumulative hour, motorcycle-only
CIRCUIT = [
    (1, "Kabira HC III",    2100,  18, False),
    (2, "Nsanja HC II",     1850,  41, False),
    (3, "Mubende HC III",   1600,  67, False),
    (4, "Kitovu HC II",     1450,  96, False),
    (5, "Bulera HC II",     1200, 118, True),
    (6, "Nyamirama HC II",   800, 134, True),
]

# Appendix F says: deduct EVERY planned opening up front, before the trip.
OPENINGS_PER_BOX = 2


def _capacity(p, boxes, litres):
    return math.floor(boxes * litres * 1000.0 / p["vol_per_dose_cm3"])


def _allocate(cap, stops, village_priority):
    """Split `cap` doses across `stops`.  village_priority=1.0 reserves the
    motorcycle villages' full need before the truck facilities get anything."""
    village_priority = max(0.0, min(1.0, village_priority))     # domain is [0, 1]
    villages = [s for s in stops if s[4]]
    trucks = [s for s in stops if not s[4]]
    v_need = sum(s[2] for s in villages)
    t_need = sum(s[2] for s in trucks)
    reserved = min(cap, v_need * village_priority)
    t_alloc = min(t_need, cap - reserved)
    leftover = cap - reserved - t_alloc
    v_total = min(v_need, reserved + leftover)
    out = {}
    for s in trucks:
        out[s[0]] = (t_alloc * s[2] / t_need) if t_need else 0.0
    for s in villages:
        out[s[0]] = (v_total * s[2] / v_need) if v_need else 0.0
    return out


def _in_spec(p, boxes, litres, cold_life, stops, detour_h=0.0):
    """Boxes are loaded two stops each, in circuit order.  A stop is in spec if
    the box's lid opens at or before its remaining cold life."""
    cap = _capacity(p, boxes, litres)
    alloc = _allocate(cap, stops, p["allocation_village_priority"])
    eff = p["in_spec_fraction"] * cold_life - OPENINGS_PER_BOX * p["opening_cost_h"]
    total = 0.0
    for i, s in enumerate(stops):
        hour = s[3] + (detour_h if s[4] else 0.0)
        if hour <= eff:
            total += alloc[s[0]]
    return total


def evaluate(params, detour_h=0.0):
    p = dict(PARAMS); p.update(params or {})
    a = _in_spec(p, BOXES_A, p["litres_per_box_A"], p["cold_life_A_h"], CIRCUIT, detour_h)
    # Order B cannot reach the two motorcycle facilities at all.
    truck_only = [s for s in CIRCUIT if not s[4]]
    b = _in_spec(p, BOXES_B, p["litres_per_box_B"], p["cold_life_B_h"], truck_only, detour_h)
    return {"A": a, "B": b}


def evaluate_twist(params):
    p = dict(PARAMS); p.update(params or {})
    return evaluate(p, detour_h=p["twist_detour_h"])


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})
    print("base ", {k: round(v) for k, v in base.items()},
          "margin %.1f%%" % (100 * (base["A"] - base["B"]) / base["B"]))
    print("twist", {k: round(v) for k, v in tw.items()})
