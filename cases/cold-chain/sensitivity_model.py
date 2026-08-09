#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Cold Chain (owned by this case, per MCS-26 / A2).

This is NOT the skill's generic example — it encodes Cold Chain's actual,
current Appendix F, after the 2026-07-31 rewrite that added Assumption 0
(box assignment) and removed the undisclosed allocation convention Tier 2
found. There is no `allocation_village_priority` dial in this file, because
there is no longer a shortfall to allocate: Order A's 4 boxes (3 truck + 1
moto) cover every facility's full stated demand. That is the actual fix —
not a better guess at an unstated rule, but a route plan that makes the
question moot.

CONTRACT — exactly two public names (see skills/case-readiness/scripts/
example_sensitivity_model.py for the full spec this follows):

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     same shape, with the twist applied

Verified against cases/cold-chain/case.md, FACILITATOR.md and case.json:
    base   A = 8200 · B = 7000 · margin 17.1%
    twist  A = 7000 · B = 7000 · exact tie (never below B)
"""
import math

PARAMS = {
    # --- Appendix F, Assumption 1 -------------------------------------------
    "opening_cost_h": 4.0,
    # --- Appendix F, Assumption 2: cold life IS in-spec time ----------------
    "in_spec_fraction": 1.0,
    # --- Appendix A, rated cold life -----------------------------------------
    "cold_life_A_h": 132.3,
    "cold_life_B_h": 138.0,
    # --- Appendix D ------------------------------------------------------------
    "vol_per_dose_cm3": 2.1,
    # --- Appendix A, vaccine capacity ----------------------------------------
    "litres_per_box_A": 6.0,
    "litres_per_box_B": 20.0,
    # --- the Twist (FACILITATOR.md) -------------------------------------------
    "twist_detour_h": 9.0,
}

# Probe 5 flexes these two — the case's actual stated assumptions. cold_life_*_h
# are sourced WHO PQS ratings, not authored assumptions, so they are out of
# scope for this probe (see the docstring note in the reference model) and are
# instead exercised by the data-decay probe (P6).
FLEX = ["opening_cost_h", "in_spec_fraction"]

# --- Appendix F, Assumption 0: box assignment -------------------------------
BOXES_A_TRUCK, BOXES_A_MOTO = 3, 1
BOXES_B_TRUCK = 2

#   stop, facility,        need, cumulative hour, motorcycle-only
CIRCUIT = [
    (1, "Kabira HC III",    2100,  18, False),
    (2, "Nsanja HC II",     1850,  41, False),
    (3, "Mubende HC III",   1600,  67, False),
    (4, "Kitovu HC II",     1450,  96, False),
    (5, "Bulera HC II",     1200, 118, True),
    (6, "Nyamirama HC II",   800, 134, True),
]

# Appendix F, Assumption 1: deduct EVERY planned opening up front. Worst-case
# openings-per-box on the truck leg (3 boxes, 4 stops) is 2 (ceil(4/3)); the
# moto leg (1 box, 2 stops) is exactly 2. Both legs share the same 2-opening
# deduction, matching FACILITATOR.md's ledger.
OPENINGS_PER_BOX = 2


def _capacity(p, boxes, litres):
    return math.floor(boxes * litres * 1000.0 / p["vol_per_dose_cm3"])


def _leg_in_spec(p, boxes, litres, cold_life, stops, detour_h=0.0):
    """Full coverage on this leg (capacity >= demand, verified in evaluate()).
    A stop's doses are in spec if the box's lid opens at or before the
    effective cold life."""
    eff = p["in_spec_fraction"] * cold_life - OPENINGS_PER_BOX * p["opening_cost_h"]
    total = 0.0
    for _, _, need, hour, is_moto in stops:
        h = hour + (detour_h if is_moto else 0.0)
        if h <= eff:
            total += need
    return total


def evaluate(params, detour_h=0.0):
    p = dict(PARAMS)
    p.update(params or {})

    truck_stops = [s for s in CIRCUIT if not s[4]]
    moto_stops = [s for s in CIRCUIT if s[4]]
    truck_demand = sum(s[2] for s in truck_stops)
    moto_demand = sum(s[2] for s in moto_stops)

    # --- Order A: 3 truck boxes + 1 moto box, full coverage on both legs ---
    a_truck_cap = _capacity(p, BOXES_A_TRUCK, p["litres_per_box_A"])
    a_moto_cap = _capacity(p, BOXES_A_MOTO, p["litres_per_box_A"])
    assert a_truck_cap >= truck_demand, (
        "Order A's truck capacity no longer covers full truck demand under "
        "these params -- Assumption 0's route plan assumes full coverage; "
        "if a param flex breaks that, the case's box counts need revisiting, "
        "not a silent partial-delivery guess.")
    assert a_moto_cap >= moto_demand, "same for the moto leg"
    a_in_spec = (_leg_in_spec(p, BOXES_A_TRUCK, p["litres_per_box_A"], p["cold_life_A_h"], truck_stops)
                 + _leg_in_spec(p, BOXES_A_MOTO, p["litres_per_box_A"], p["cold_life_A_h"], moto_stops, detour_h))

    # --- Order B: 2 truck boxes, never attempts the moto leg ---
    b_truck_cap = _capacity(p, BOXES_B_TRUCK, p["litres_per_box_B"])
    assert b_truck_cap >= truck_demand, "Order B's stated capacity no longer covers truck demand"
    b_in_spec = _leg_in_spec(p, BOXES_B_TRUCK, p["litres_per_box_B"], p["cold_life_B_h"], truck_stops)

    return {"A": a_in_spec, "B": b_in_spec}


def evaluate_twist(params):
    p = dict(PARAMS)
    p.update(params or {})
    return evaluate(p, detour_h=p["twist_detour_h"])


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})
    print("base ", {k: round(v) for k, v in base.items()},
          "margin %.1f%%" % (100 * (base["A"] - base["B"]) / base["B"]))
    print("twist", {k: round(v) for k, v in tw.items()},
          "margin %.1f%%" % (100 * (tw["A"] - tw["B"]) / tw["B"]) if tw["B"] else "n/a")

    print("\nFLEX sweep, opening_cost_h in [2..6] (Assumption 1 +/-50% and beyond):")
    for oc in (2.0, 3.0, 4.0, 5.0, 6.0):
        b = evaluate({"opening_cost_h": oc})
        t = evaluate_twist({"opening_cost_h": oc})
        print(f"  opening_cost_h={oc}  base A={b['A']:.0f} B={b['B']:.0f} "
              f"margin={100*(b['A']-b['B'])/b['B']:.1f}%   "
              f"twist A={t['A']:.0f} B={t['B']:.0f} "
              f"margin={100*(t['A']-t['B'])/t['B']:.1f}%")
