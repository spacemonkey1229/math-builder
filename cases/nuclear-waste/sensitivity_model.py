#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- Nuclear Waste.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. This file is
that model for `cases/nuclear-waste`.

CONTRACT -- exactly two/three public names (see example_sensitivity_model.py):

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     optional; same shape, with the twist applied

IMPORTANT, CASE-SPECIFIC FINDING (read before trusting a P5 "PASS"):

The case's GRADED PRIMARY METRIC is `primary_metric: "safety rating (out of 5)"`
(case.json), and `balance.margin_basis` states explicitly this is safety rating,
not cost. Both companies' safety ratings (4.8 and 4.5) are DIRECTLY STATED,
narrative facts in the case (Background, Appendix A/B) -- they are not derived
from any modeling assumption. There is no formula, no packing convention, no
capacity convention that feeds into the 4.8-vs-4.5 comparison at all.

Consequently `evaluate()` -- which must return the graded metric -- is
independent of every entry in FLEX by construction. Flexing FLEX params +/-50%
cannot move the graded verdict, not because the case is provably robust, but
because the graded metric is raw given data with no assumption in its causal
path. This is reported to QA as a finding (see QA_REPORT.md P5), not silently
treated as "case passed sensitivity cleanly."

The two disclosed modeling assumptions (Appendix D / case.json.modeling_assumptions
MA1, MA2) DO drive D1 (rods/container), D3 (max capacity, storage revenue) and D6
(barrel lining cost) -- i.e. they drive the disclosed COST/CAPACITY context, which
is exactly what the case's own `legacy_conversion_note` says was deliberately kept
out of the graded metric because it produces an unbalanceable (268%) gap. The model
below implements those D1/D3/D6 calculations too (as `context_costs()`), so a human
reader can see exactly how far the disclosed-context numbers move under +/-50% flex,
even though that movement never touches `evaluate()`'s A/B.

Verified against cases/nuclear-waste/case.json `derived{}`:
    rod_volume_cuft            0.053973
    barrel_volume_cuft         49.48
    rods_per_barrel            916
    crate_volume_cuft          125
    rods_per_crate             2315
    barrels_needed             273
    crates_needed               108
    isolation_total_first_year_cost   432527.55
    nustorage_total_first_year_cost   117424.08
    isolation_max_barrels      103529
    nustorage_max_crates        20223
    barrel_surface_area_sqft    80.11
    total_lining_cost_all_barrels  273376.74
    safety_margin_pct (A vs B)     6.67
"""
import math

SQFT_PER_ACRE = 43560.0

PARAMS = {
    # --- Appendix C: fuel rod -------------------------------------------------
    "rod_length_in": 19.0,
    "rod_diameter_in": 2.5,
    # --- Appendix A: Isolation barrel ------------------------------------------
    "barrel_height_ft": 7.0,
    "barrel_diameter_ft": 3.0,
    "isolation_usable_acres": 16.8,
    "isolation_transport_per_barrel": 164.92,
    "isolation_storage_per_barrel_yr": 1419.43,
    "isolation_lining_rate_per_sqft": 12.5,
    "safety_rating_isolation": 4.8,
    # --- Appendix B: NuStorage crate -------------------------------------------
    "crate_side_ft": 5.0,
    "nustorage_stack_factor": 3,
    "nustorage_sqft": 168539.0,
    "nustorage_transport_per_crate": 103.57,
    "nustorage_storage_per_crate_yr": 983.69,
    "safety_rating_nustorage": 4.5,
    # --- Background: the order --------------------------------------------------
    "rods_needed": 250000,
    # --- Appendix D, MA1: rods-per-container by volume, no packing loss --------
    # 1.0 = the case's stated convention (no packing inefficiency modeled).
    # A genuine author-chosen simplification, not cited/given data -- FLEX.
    "packing_efficiency": 1.0,
    # --- Appendix D, MA2: site filled edge-to-edge, no aisles/buffers ----------
    # 1.0 = the case's stated convention (whole usable area counted as storage).
    # A genuine author-chosen simplification, not cited/given data -- FLEX.
    "site_fill_efficiency": 1.0,
}

# Probe 5 flexes THESE and only these. SPEC Section 2 asks for sensitivity to
# STATED ASSUMPTIONS, not to cited/given measurements: the rod/barrel/crate
# dimensions, costs, acreage, and BOTH safety ratings are narrative facts the
# case simply states (Appendix A/B/C) -- flexing those is a different case, not
# a sensitivity test, and P6 (data decay) is the probe for cited data anyway.
# Only MA1 and MA2 (Appendix D) are conventions the case's author actually chose.
FLEX = [
    "packing_efficiency",     # Appendix D, Assumption 1 (MA1)
    "site_fill_efficiency",   # Appendix D, Assumption 2 (MA2)
]


def _rod_volume_cuft(p):
    r_ft = (p["rod_diameter_in"] / 2.0) / 12.0
    h_ft = p["rod_length_in"] / 12.0
    return math.pi * r_ft ** 2 * h_ft


def _barrel_volume_cuft(p):
    r = p["barrel_diameter_ft"] / 2.0
    return math.pi * r ** 2 * p["barrel_height_ft"]


def _barrel_footprint_sqft(p):
    r = p["barrel_diameter_ft"] / 2.0
    return math.pi * r ** 2


def _barrel_surface_area_sqft(p):
    r = p["barrel_diameter_ft"] / 2.0
    return 2 * math.pi * r ** 2 + 2 * math.pi * r * p["barrel_height_ft"]


def _crate_volume_cuft(p):
    return p["crate_side_ft"] ** 3


def _crate_footprint_sqft(p):
    return p["crate_side_ft"] ** 2


def d1_rods_per_container(p):
    """D1 -- how many rods fit in one container (MA1: volume ratio, floor)."""
    rod_v = _rod_volume_cuft(p)
    eff = max(0.0, p["packing_efficiency"])
    rods_per_barrel = math.floor(eff * _barrel_volume_cuft(p) / rod_v)
    rods_per_crate = math.floor(eff * _crate_volume_cuft(p) / rod_v)
    return rods_per_barrel, rods_per_crate


def d2_order_cost(p, rods_per_barrel, rods_per_crate):
    """D2 -- transport + storage cost for the full 250,000-rod order."""
    barrels_needed = math.ceil(p["rods_needed"] / rods_per_barrel)
    crates_needed = math.ceil(p["rods_needed"] / rods_per_crate)
    iso_cost = (barrels_needed * p["isolation_transport_per_barrel"]
                + barrels_needed * p["isolation_storage_per_barrel_yr"])
    nu_cost = (crates_needed * p["nustorage_transport_per_crate"]
               + crates_needed * p["nustorage_storage_per_crate_yr"])
    return barrels_needed, crates_needed, iso_cost, nu_cost


def d3_max_capacity(p):
    """D3 -- each facility's max container count and storage revenue at max (MA2)."""
    eff = max(0.0, p["site_fill_efficiency"])
    iso_usable_sqft = p["isolation_usable_acres"] * SQFT_PER_ACRE
    iso_max_barrels = math.floor(eff * iso_usable_sqft / _barrel_footprint_sqft(p))
    nu_max_crates = math.floor(eff * p["nustorage_sqft"] / _crate_footprint_sqft(p)) * p["nustorage_stack_factor"]
    iso_revenue = iso_max_barrels * p["isolation_storage_per_barrel_yr"]
    nu_revenue = nu_max_crates * p["nustorage_storage_per_crate_yr"]
    return iso_max_barrels, nu_max_crates, iso_revenue, nu_revenue


def d6_lining_cost(p, barrels_needed):
    """D6 -- one barrel's surface area, and total lining cost for the order."""
    sa = _barrel_surface_area_sqft(p)
    per_barrel = sa * p["isolation_lining_rate_per_sqft"]
    return sa, per_barrel, per_barrel * barrels_needed


def context_costs(params=None):
    """Everything D1/D2/D3/D6 compute -- the disclosed COST/CAPACITY context that
    the case deliberately keeps OUT of the graded metric (see module docstring).
    Not used by evaluate(); exposed so P5 can report how far the context numbers
    move under a FLEX sweep even though the graded verdict never moves."""
    p = dict(PARAMS)
    p.update(params or {})
    rods_per_barrel, rods_per_crate = d1_rods_per_container(p)
    barrels_needed, crates_needed, iso_cost, nu_cost = d2_order_cost(p, rods_per_barrel, rods_per_crate)
    iso_max_barrels, nu_max_crates, iso_rev, nu_rev = d3_max_capacity(p)
    sa, per_barrel_lining, total_lining = d6_lining_cost(p, barrels_needed)
    return {
        "rods_per_barrel": rods_per_barrel,
        "rods_per_crate": rods_per_crate,
        "barrels_needed": barrels_needed,
        "crates_needed": crates_needed,
        "isolation_total_first_year_cost": iso_cost,
        "nustorage_total_first_year_cost": nu_cost,
        "isolation_max_barrels": iso_max_barrels,
        "nustorage_max_crates": nu_max_crates,
        "isolation_max_annual_storage_revenue": iso_rev,
        "nustorage_max_annual_storage_revenue": nu_rev,
        "barrel_surface_area_sqft": sa,
        "barrel_lining_cost": per_barrel_lining,
        "total_lining_cost_all_barrels": total_lining,
    }


def evaluate(params=None):
    """D4/balance_test -- the GRADED metric: safety rating out of 5, per company.
    Directly-stated data (Background, Appendix A/B). Independent of FLEX -- see
    module docstring for why that is itself a Tier-2 finding, not a bug here."""
    p = dict(PARAMS)
    p.update(params or {})
    return {"A": p["safety_rating_isolation"], "B": p["safety_rating_nustorage"]}


# evaluate_twist() deliberately NOT implemented. FACILITATOR.md is explicit that
# the rail-route twist is "deliberately qualitative, not a new number to plug
# in" -- the case states no numeric dial (a distance, a population count, a
# risk weight) that the twist would flex. Fabricating one to satisfy the
# contract's optional third name would be modeling a case the author did not
# write. P4 is therefore adjudicated by reading (see QA_REPORT.md), not by
# mechanical recomputation.


if __name__ == '__main__':
    base = evaluate({})
    margin = 100 * (base["A"] - base["B"]) / base["B"]
    print("evaluate() base:", base, "margin %.2f%%" % margin)
    ctx = context_costs({})
    for k in ("rods_per_barrel", "rods_per_crate", "barrels_needed", "crates_needed",
              "isolation_total_first_year_cost", "nustorage_total_first_year_cost",
              "isolation_max_barrels", "nustorage_max_crates",
              "barrel_surface_area_sqft", "barrel_lining_cost", "total_lining_cost_all_barrels"):
        print(f"  {k} = {ctx[k]}")
