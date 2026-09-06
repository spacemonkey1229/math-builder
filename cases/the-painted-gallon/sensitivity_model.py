"""
sensitivity_model.py -- The Painted Gallon

Graded primary metric (case.json.primary_metric): total 60-year lifecycle cost
(construction plus scheduled recoating) per gallon of storage capacity, comparing
the Spheroid (A) against the Multi-Column (B), both built to the town's required
capacity. Lower cost per gallon is better, so evaluate() returns the NEGATIVE of
each option's cost per gallon -- higher score = better, matching this script's
"higher wins" convention (same convention as cases/the-deferred-repair/sensitivity_model.py).

Every rate below is DERIVED from real, sourced figures (case.json.sources S5, S7, S8,
S11, S13, S14 -- the real 2019 Black & Veatch / Tnemec Company data for the City of
Lawrence, Kansas):

    spheroid_build_rate    = S7 / S5   = 2,048,000 / 16,500  = $124.12 / sq ft
    spheroid_maint_rate    = S8 / S5   =   376,000 / 16,500  =  $22.79 / sq ft (60-yr NPV)
    multicolumn_build_rate = S13 / S11 = 1,595,000 / 29,100  =  $54.81 / sq ft
    multicolumn_maint_rate = S14 / S11 =   490,000 / 29,100  =  $16.84 / sq ft (60-yr NPV)

These four rates are CITED DATA (derived from real sourced dollar and area figures),
not the case's own stated assumption -- they are NOT swept by default (SPEC §2 asks
for sensitivity to stated ASSUMPTIONS, not cited measurements; P6 stress-tests cited
data instead).

The one real, disclosed Modeling Assumption in this case is MA2 -- the town's required
storage capacity, fixed at 750,000 gallons because no source publishes a capacity
specific to this fictional town. FLEX below sweeps exactly that, and nothing else.
Surface area is modeled as scaling with capacity^(2/3) (similar solids: area scales
with the 2/3 power of volume) around the real calibration point of 750,000 gallons,
so the model reproduces the real S5/S11 areas exactly at the case's stated capacity.

Verified against case.json.balance / FACILITATOR.md's margin arithmetic:
    base   A = $3.23/gal  ·  B = $2.78/gal  ·  margin 14.0%  (B wins -- matches case.json)

SCOPE NOTE (added 2026-09-06, Tier 2 twist-integrity probe finding): this model's capacity sweep
(FLEX = ["capacity_gal"], run at +/-50%) tests ONLY the dollar cost-per-gallon metric (S5-S16,
Appendix D). It says nothing about, and should never be cited as evidence for, the SEPARATE
fabricator-competition claim in case.json's balance.argument_a (source S17, case.md Appendix G) --
that claim is sourced specifically "at 0.5-0.75 MG capacity" per the real memo, and this case's
required capacity (750,000 gal = 0.75 MG) sits at the edge of that sourced range. Do NOT extend the
"the recommendation is stable across a wide capacity range" finding below to Appendix G's fabricator
counts -- that would be citing a dollar-cost invariance result as support for an unrelated,
narrower-scoped sourced claim. See case.md Appendix G's "Scope note" and FACILITATOR.md Socratic
Question 7.
"""

CAPACITY_REF_GAL = 750000.0

PARAMS = {
    # --- The case's one real, disclosed assumption (MA2) --------------------
    "capacity_gal": 750000.0,
    # --- Derived from real sourced figures (S5/S7/S8/S11/S13/S14) -- CITED,
    #     not flexed by default ------------------------------------------------
    "spheroid_build_rate": 124.12,      # USD per sq ft, derived S7/S5
    "spheroid_maint_rate": 22.79,       # USD per sq ft, 60-yr NPV, derived S8/S5
    "multicolumn_build_rate": 54.81,    # USD per sq ft, derived S13/S11
    "multicolumn_maint_rate": 16.84,    # USD per sq ft, 60-yr NPV, derived S14/S11
    # --- Real areas at the calibration capacity (S5, S11) --------------------
    "spheroid_area_ref": 16500.0,
    "multicolumn_area_ref": 29100.0,
}

# Only the case's own stated assumption (required capacity, MA2) is swept by
# default. The four build/maintenance rates and the two reference areas are
# derived from real, cited dollar and area figures -- halving a real fabricator
# quote is a different case, not a sensitivity test on this case's own authored
# assumption. Run with --flex-all to sweep those too.
FLEX = ["capacity_gal"]


def _area(area_ref, capacity_gal):
    # Similar solids: surface area scales with volume^(2/3). Calibrated so the
    # model reproduces the real S5/S11 area exactly at CAPACITY_REF_GAL.
    return area_ref * (capacity_gal / CAPACITY_REF_GAL) ** (2.0 / 3.0)


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    cap = p["capacity_gal"]

    sp_area = _area(p["spheroid_area_ref"], cap)
    mc_area = _area(p["multicolumn_area_ref"], cap)

    a_total = sp_area * (p["spheroid_build_rate"] + p["spheroid_maint_rate"])
    b_total = mc_area * (p["multicolumn_build_rate"] + p["multicolumn_maint_rate"])

    a_cost_per_gal = a_total / cap
    b_cost_per_gal = b_total / cap

    # Lower cost per gallon is better -- return negative so higher score wins.
    return {"A": -a_cost_per_gal, "B": -b_cost_per_gal}


if __name__ == '__main__':
    for flex_pct in (-50, 0, 50):
        cap = CAPACITY_REF_GAL * (1 + flex_pct / 100.0)
        base = evaluate({"capacity_gal": cap})
        a_cost, b_cost = -base["A"], -base["B"]
        win = "A" if a_cost < b_cost else "B"
        lo, hi = min(a_cost, b_cost), max(a_cost, b_cost)
        margin = 100.0 * (hi - lo) / hi
        print("capacity flex %+4d%% (%.0f gal)  A=$%.2f/gal  B=$%.2f/gal  winner=%s  margin=%.1f%%"
              % (flex_pct, cap, a_cost, b_cost, win, margin))
