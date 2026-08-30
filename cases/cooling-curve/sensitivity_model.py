#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Cooling Curve.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the contract
this file follows.

Metric convention: the case's real primary_metric (watts of heat dissipated
per dollar of fin manufacturing cost) is already HIGHER-is-better, matching
the P5 harness's max() convention directly -- no inversion needed (contrast
cases/enclosure-call, whose metric is cost/unit and needs a 1/x flip).

PARAMS = every dial the case's own modeling_assumptions[] states that feeds
D1-D4 (MA1-MA7). MA8 (cost-per-watt benchmark) is a D4 cross-check only, not
an input to the watts-per-dollar comparison itself, so it is fixed/omitted
from FLEX. MA9-MA11 (rack count, cold plates/rack, fins/cold plate) are pure
uniform scaling multipliers applied equally to both options' totals -- they
cancel out of the per-fin watts-per-dollar ratio entirely and cannot flip the
winner by construction, so they are fixed at their case.json values and left
out of FLEX (flexing them would only test arithmetic plumbing, not the case's
real sensitivity). MA12 (mold-order deadline) is decorative, feeds no
calculation at all.

RETUNE 2026-08-29: MA5 (pyramid mold cost) was revised from $12,000 to $7,000
per case.json.balance.margin_note -- grounded in tooling-cost-complexity
benchmarking research (30-50% premium per added mold complexity feature is
realistic, vs. the prior untested 2.4x ratio). This file reflects the
POST-RETUNE case of record.

Verified against cases/cooling-curve/case.json balance{} / derived{}
(computation dated 2026-08-29, post-retune):
    base   Pyramid = 17.50 W/$  ·  Cone = 21.45 W/$  ·  margin 18.4% (B/Cone wins)
    twist  Pyramid = 3.33 W/$   ·  Cone = 4.13 W/$   ·  margin 19.35% (B/Cone still wins)
"""
import math

PARAMS = {
    # --- MA1: heat dissipation rate per unit of exposed fin surface area ----
    "dissipation_w_per_in2": 13.0,
    # --- MA2/MA3: fin base dimensions ----------------------------------------
    "pyramid_base_edge_in": 0.08,      # MA2
    "cone_base_diameter_in": 0.09,     # MA3
    # --- MA4: fin height, both geometries ------------------------------------
    "fin_height_in": 0.2,
    # --- S2 (sourced, fixed -- not flexed by P5, see docstring) -------------
    "material_cost_usd_per_in3": 2.12,
    # --- MA5/MA6: mold cost, retuned 2026-08-29 -------------------------------
    "pyramid_mold_cost_usd": 7000.0,   # MA5 (was 12000.0 pre-retune)
    "cone_mold_cost_usd": 5000.0,      # MA6
    # --- MA7: fins produced per mold before replacement ----------------------
    "fins_per_mold": 300000.0,
    # --- MA9-MA11: deployment scale (fixed -- uniform scalers, see docstring) -
    "gpu_racks": 16.0,                 # MA9
    "cold_plates_per_rack": 72.0,      # MA10
    "fins_per_cold_plate": 48.0,       # MA11
}

# P5 sweeps only these -- the case's own STATED ASSUMPTIONS that actually feed
# the per-fin watts-per-dollar comparison (MA1-MA7). S2 (cited copper price) is
# stress-tested by P6 (data decay) instead. MA9-MA11 are fixed uniform scalers
# (see docstring) and MA8/MA12 feed no D1-D4 calculation at all.
FLEX = [
    "dissipation_w_per_in2",       # MA1
    "pyramid_base_edge_in",        # MA2
    "cone_base_diameter_in",       # MA3
    "fin_height_in",               # MA4
    "pyramid_mold_cost_usd",       # MA5 -- the case's own named most load-bearing dial
    "cone_mold_cost_usd",          # MA6
    "fins_per_mold",               # MA7
]


def _pyramid_geometry(p):
    edge, h = p["pyramid_base_edge_in"], p["fin_height_in"]
    volume = (1.0 / 3.0) * edge ** 2 * h
    slant = math.sqrt(h ** 2 + (edge / 2.0) ** 2)
    # Four triangular faces; base excluded (bonded to the cold plate, not
    # exposed to coolant) -- matches case.json.balance.margin_note exactly.
    surface = 2.0 * edge * slant
    return volume, surface


def _cone_geometry(p):
    d, h = p["cone_base_diameter_in"], p["fin_height_in"]
    r = d / 2.0
    volume = (1.0 / 3.0) * math.pi * r ** 2 * h
    slant = math.sqrt(r ** 2 + h ** 2)
    surface = math.pi * r * slant
    return volume, surface


def _fin_count(p):
    return p["gpu_racks"] * p["cold_plates_per_rack"] * p["fins_per_cold_plate"]


def _watts_per_dollar(volume_in3, surface_in2, mold_cost_usd, fins_per_mold, p):
    material_cost = volume_in3 * p["material_cost_usd_per_in3"]
    mold_amortized_cost = mold_cost_usd / fins_per_mold
    cost_per_fin = material_cost + mold_amortized_cost
    watts_per_fin = surface_in2 * p["dissipation_w_per_in2"]
    return watts_per_fin / cost_per_fin


def _scores(p, fins_per_mold_override=None):
    fpm = fins_per_mold_override if fins_per_mold_override is not None else p["fins_per_mold"]
    py_vol, py_surf = _pyramid_geometry(p)
    co_vol, co_surf = _cone_geometry(p)
    a = _watts_per_dollar(py_vol, py_surf, p["pyramid_mold_cost_usd"], fpm, p)
    b = _watts_per_dollar(co_vol, co_surf, p["cone_mold_cost_usd"], fpm, p)
    return a, b


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    a, b = _scores(p)
    return {"A": a, "B": b}


def evaluate_twist(params):
    """FACILITATOR.md's Twist: re-amortize each mold over the deployment's
    actual fin order (Appendix E: 16 racks x 72 cold plates x 48 fins =
    55,296) instead of MA7's 300,000-fin assumed mold life. Built entirely
    from numbers already in the case (no new figure invented)."""
    p = dict(PARAMS)
    p.update(params or {})
    a, b = _scores(p, fins_per_mold_override=_fin_count(p))
    return {"A": a, "B": b}


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})
    print("base W/$   Pyramid=%.2f  Cone=%.2f  margin=%.2f%%  winner=%s"
          % (base["A"], base["B"],
             100 * (base["B"] - base["A"]) / base["B"],
             "B (Cone)" if base["B"] > base["A"] else "A (Pyramid)"))
    print("twist W/$  Pyramid=%.2f  Cone=%.2f  margin=%.2f%%  winner=%s"
          % (tw["A"], tw["B"],
             100 * (tw["B"] - tw["A"]) / tw["B"],
             "B (Cone)" if tw["B"] > tw["A"] else "A (Pyramid)"))
