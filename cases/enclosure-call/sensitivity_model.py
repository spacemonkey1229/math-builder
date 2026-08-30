#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Enclosure Call.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the contract
this file follows.

Metric convention: the case's real primary_metric (total cost per unit) is
LOWER-is-better, but the P5 harness (tier2_probes.py) picks a winner with
max(). So evaluate() returns 1 / total_cost_per_unit for each option -- a
positive, monotonically-decreasing-in-cost score where higher is still better,
same ordering as the case's actual winner (lower cost). margin_pct printed by
the harness is therefore on this inverted scale, not literally
case.json's own "(loser-winner)/winner" cost-margin definition -- read it as a
relative-gap indicator, not as a restatement of the 8.85% figure in case.json.margin_pct.

PARAMS = every dial the case's own modeling_assumptions[] states (MA1, MA2,
MA4, MA5, MA6). MA3 (material, identical for both options) is not a numeric
dial and cancels out of the comparison, so it is omitted.

FIXED / NOT FLEXED (cited data, stress-tested by P6 instead, not by P5):
  - resin price (S3), ABS density (S4) -- feed material cost, but are cited
    market/physical figures, not something the case chose.
  - container internal volume (S1), ocean freight spot rate (S2).
  - Project Orb's packing efficiency, 74.05% -- the Kepler-conjecture sphere-
    packing ceiling. This is a proven mathematical fact the case explicitly
    calls "real, well-known," not an authored assumption, so it stays out of
    FLEX (only Project Horn's packing efficiency, MA4, is an authored pick).

Verified against cases/enclosure-call/case.json derived{} (computation dated
2026-08-27, post P5/P6 remediation -- resin price and ABS density re-sourced,
see RESEARCH_LOG.md):
    base   Horn = $0.8621/unit  ·  Orb = $0.7920/unit  ·  margin 8.85% (B/Orb wins)
    twist  Horn = $0.8621/unit  ·  Orb = $0.9720/unit  ·  margin 12.75% (A/Horn wins)
"""
import math

PARAMS = {
    # --- MA1: Project Horn frustum dimensions & Project Orb sphere radius ---
    "horn_base_r_in": 3.5,
    "horn_top_r_in": 2.0,
    "horn_height_in": 6.0,
    "orb_r_in": 3.5,
    # --- MA2: client's target first-year production volume -----------------
    "target_volume_units": 250000,
    # --- MA4: Project Horn's packing efficiency inside a shipping container -
    #     The single most dilemma-sensitive assumption per case.json's own
    #     sensitivity_note / MA4.sensitivity.
    "horn_packing_efficiency": 0.80,
    # --- MA5: wall thickness picked to derive S6 (material $/sq in) ---------
    "wall_thickness_in": 0.0925,
    # --- MA6: mold tooling cost, both options --------------------------------
    "horn_tooling_cost_usd": 58000.0,
    "orb_tooling_cost_usd": 32000.0,

    # --- FIXED / cited (S1-S4) -- not flexed by P5, see docstring -----------
    # (updated 2026-08-27 P6 re-source: S3 -> BusinessAnalytiq $1.94/kg North
    # America Aug-2026 = $0.88/lb; S4 -> AmesWeb 1.052 g/cm3 extrusion-grade
    # ABS = 0.038 lb/in3; see RESEARCH_LOG.md)
    "resin_price_usd_per_lb": 0.88,          # S3
    "abs_density_lb_per_in3": 0.038,         # S4
    "container_volume_cu_ft": 2683.0,        # S1
    "container_freight_cost_usd": 3570.80,   # S2
    "orb_packing_efficiency": 0.7405,        # Kepler-conjecture ceiling (fact, not MA)

    # --- The Twist (FACILITATOR.md only, illustrative, never in case.md) ----
    "twist_recert_cost_usd": 45000.0,
}

# P5 sweeps only these -- the case's own STATED ASSUMPTIONS (MA1, MA2, MA4,
# MA5, MA6). Cited/fixed figures above are stress-tested by P6 (data decay)
# instead, per the "Only FLEX[] is swept" rule in skills/case-readiness/SKILL.md.
FLEX = [
    "horn_base_r_in",          # MA1
    "horn_top_r_in",           # MA1
    "horn_height_in",          # MA1
    "orb_r_in",                # MA1
    "target_volume_units",     # MA2
    "horn_packing_efficiency", # MA4 -- the case's own named most-sensitive dial
    "wall_thickness_in",       # MA5
    "horn_tooling_cost_usd",   # MA6
    "orb_tooling_cost_usd",    # MA6
]

CU_IN_PER_CU_FT = 1728.0


def _horn_geometry(p):
    R, r, h = p["horn_base_r_in"], p["horn_top_r_in"], p["horn_height_in"]
    slant = math.sqrt((R - r) ** 2 + h ** 2)
    surface = math.pi * (R + r) * slant + math.pi * R ** 2 + math.pi * r ** 2
    volume_cu_in = (math.pi * h / 3.0) * (R ** 2 + R * r + r ** 2)
    return surface, volume_cu_in / CU_IN_PER_CU_FT


def _orb_geometry(p):
    r = p["orb_r_in"]
    surface = 4.0 * math.pi * r ** 2
    volume_cu_in = (4.0 / 3.0) * math.pi * r ** 3
    return surface, volume_cu_in / CU_IN_PER_CU_FT


def _total_cost_per_unit(surface_sq_in, volume_cu_ft, packing_eff, tooling_cost, p):
    # Rounded to 4 decimals to match S6 (case.json sources[]), which is
    # itself published/used downstream at that rounded precision ("$0.0029
    # per sq in"), not as an unrounded intermediate.
    material_cost_per_sqin = round(p["resin_price_usd_per_lb"] * p["abs_density_lb_per_in3"]
                                    * p["wall_thickness_in"], 4)
    material = surface_sq_in * material_cost_per_sqin
    tooling = tooling_cost / p["target_volume_units"]
    units_per_container = (p["container_volume_cu_ft"] * packing_eff) / volume_cu_ft
    shipping = p["container_freight_cost_usd"] / units_per_container
    return material + tooling + shipping


def _costs(p):
    horn_surface, horn_vol = _horn_geometry(p)
    orb_surface, orb_vol = _orb_geometry(p)
    horn_cost = _total_cost_per_unit(horn_surface, horn_vol, p["horn_packing_efficiency"],
                                      p["horn_tooling_cost_usd"], p)
    orb_cost = _total_cost_per_unit(orb_surface, orb_vol, p["orb_packing_efficiency"],
                                     p["orb_tooling_cost_usd"], p)
    return horn_cost, orb_cost


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    horn_cost, orb_cost = _costs(p)
    # Invert: higher score = lower cost = better, matching the harness's max()
    # convention while preserving the case's real (lower-is-better) ordering.
    return {"A": 1.0 / horn_cost, "B": 1.0 / orb_cost}


def evaluate_twist(params):
    """FACILITATOR.md's Twist: a $45,000 acoustic-recertification cost lands
    on Project Orb only, amortized over the target volume ($0.18/unit at the
    base MA2 value). Illustrative-only per FACILITATOR.md -- never sourced,
    never in case.md/balance -- so it is applied here, not folded into PARAMS
    used by the base evaluate()."""
    p = dict(PARAMS)
    p.update(params or {})
    horn_cost, orb_cost = _costs(p)
    orb_cost_with_recert = orb_cost + (p["twist_recert_cost_usd"] / p["target_volume_units"])
    return {"A": 1.0 / horn_cost, "B": 1.0 / orb_cost_with_recert}


if __name__ == '__main__':
    p = dict(PARAMS)
    horn_cost, orb_cost = _costs(p)
    base = evaluate({})
    tw = evaluate_twist({})
    print("base $/unit  Horn=%.4f  Orb=%.4f  margin(Orb ref)=%.2f%%  winner=%s"
          % (horn_cost, orb_cost, 100 * (horn_cost - orb_cost) / orb_cost,
             "B (Orb)" if orb_cost < horn_cost else "A (Horn)"))
    orb_with_recert = orb_cost + p["twist_recert_cost_usd"] / p["target_volume_units"]
    print("twist $/unit Horn=%.4f  Orb+recert=%.4f  margin(Horn ref)=%.2f%%  winner=%s"
          % (horn_cost, orb_with_recert, 100 * (orb_with_recert - horn_cost) / horn_cost,
             "A (Horn)" if horn_cost < orb_with_recert else "B (Orb)"))
    print("inverted scores base :", {k: round(v, 4) for k, v in base.items()})
    print("inverted scores twist:", {k: round(v, 4) for k, v in tw.items()})
