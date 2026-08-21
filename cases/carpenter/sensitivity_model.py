#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Carpenter.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. This is that
model, for cases/carpenter.

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):

    PARAMS                             dict[str, number]  every dial the case states
    FLEX                               list[str]          subset of PARAMS probe 5 flexes
    evaluate(params) -> dict           {"A": metric, "B": metric}
    evaluate_twist(params) -> dict     same shape, with the twist's own lens applied

IMPORTANT — metric direction: this case's primary metric is a COST in CAD, so
LOWER is better here.

evaluate() returns the case's graded PRIMARY metric: 15-year total cost of
ownership in CAD, reading Appendix B/C's wear-life and maintenance figures at
face value (one full carpet replacement inside the 15-year horizon, at year
10; hardwood serviced per Appendix F MA3's stated schedule only -- recoat at
year 5, full refinish at year 10, nothing further). This matches
case.json.balance (A=$33,723.93, B=$34,674.14, margin 2.8%, A cheaper).

evaluate_twist() applies the case's Twist: short-term-rental heavy, weekly-
turnover foot traffic roughly halves carpet's effective replacement trigger,
forcing a SECOND full carpet replacement inside the 15-year horizon (year 5
and year 10, instead of just year 10). Hardwood's schedule is unaffected --
solid hardwood is comparatively traffic-resistant; only its finish wears, and
that is already captured by the recoat/refinish schedule in the base case.
This matches case.json.balance's twist reading (A=$39,986.87, B=$34,674.14,
margin 15.3%, B cheaper) -- the winner flips.

Verified against case.md / case.json:
    evaluate({})        A = 33723.93  B = 34674.14   margin (B-A)/A = 2.8%   (A cheaper, base)
    evaluate_twist({})  A = 39986.87  B = 34674.14   margin (A-B)/B = 15.3%  (B cheaper, twist)

CORRECTION (2026-08-20, caught by Tier 2 probe 1 cold-solve): an earlier
version of this model added an undocumented THIRD hardwood service event (a
second recoat at year 15) that Appendix F's MA3 text never states ("recoat at
year 5... full refinish at year 10" -- no third event). A fresh cold-solve
subagent, working from the student packet alone, correctly used only the two
stated events and reached B=$34,674.14, not the model's then-B=$36,100.89.
Fixed here by removing the undisclosed year-15 recoat so the model matches
what the case document actually says (hardwood_recoat_years=(5,) only).
"""

PARAMS = {
    # --- Appendix A / Appendix F, MA1: room square footage -------------------
    "sqft_chz": 690,     # carpet/hardwood zone (bedrooms + living room)
    "sqft_tile": 330,    # tile zone (kitchen, dining, store, bathrooms)

    # --- Appendix B, S1/S4: carpet, USD/sq ft --------------------------------
    "carpet_material_psf": 3.25,
    "carpet_install_psf": 3.25,

    # --- Appendix B, S2/S5: hardwood, USD/sq ft ------------------------------
    "hardwood_material_psf": 8.00,
    "hardwood_install_psf": 6.96,

    # --- Appendix B, S3/S6: tile, USD/sq ft (same both options) -------------
    "tile_material_psf": 4.50,
    "tile_install_psf": 13.80,

    # --- Appendix D, given business term -------------------------------------
    "delivery_fee_pct": 0.026,
    # --- Appendix D, S12: live Bank of Canada rate ---------------------------
    "usd_to_cad": 1.3785,

    # --- Appendix C, S10/S11: routine maintenance, USD/sq ft/service --------
    "carpet_clean_psf_yr": 0.50,
    "tile_service_psf": 2.50,
    "tile_service_interval_yrs": 3,

    # --- Appendix F, MA2: which end of the 8-10yr carpet wear-life range ----
    # base reading: one full replacement, at this year. Flexing this dial
    # ±50% (probe 5) changes how many trigger-multiples fall inside the
    # horizon (see _n_events below).
    "carpet_replace_trigger_years": 10,
    # twist reading: short-term-rental heavy traffic roughly halves the
    # trigger, so replacements land at these explicit years instead.
    "carpet_replace_years_twist": (5, 10),

    # --- Appendix C, S8/S9; Appendix F, MA3: hardwood service schedule ------
    # explicit years, not a divisibility loop: a refinish REPLACES the recoat
    # that would otherwise fall in the same year.
    "hardwood_recoat_psf": 1.50,
    "hardwood_recoat_years": (5,),
    "hardwood_refinish_psf": 5.00,
    "hardwood_refinish_years": (10,),

    "horizon_years": 15,
}

# Probe 5 flexes THESE and only these -- the case's own STATED assumptions
# (Appendix F), not the cited 2026 cost/wear-life figures (S1-S12), which are
# stress-tested by the data-decay probe (P6) instead. sqft_chz is MA1 (a
# floor plan adapted for a fictional flat, not a real property record).
# carpet_replace_trigger_years is MA2 -- a genuine case-author choice of which
# end of the sourced 8-10 year range triggers a full replacement inside the
# 15-year horizon.
FLEX = [
    "sqft_chz",                       # Appendix F, MA1
    "carpet_replace_trigger_years",   # Appendix F, MA2
]


def _tile_totals(p):
    mat = p["sqft_tile"] * p["tile_material_psf"]
    lab = p["sqft_tile"] * p["tile_install_psf"]
    return mat, lab


def _initial_cad(p, mat_psf, inst_psf):
    zone_mat = p["sqft_chz"] * mat_psf
    zone_lab = p["sqft_chz"] * inst_psf
    tile_mat, tile_lab = _tile_totals(p)
    total_mat = zone_mat + tile_mat
    total_lab = zone_lab + tile_lab
    delivery = total_mat * p["delivery_fee_pct"]
    total_usd = total_mat + total_lab + delivery
    return total_usd * p["usd_to_cad"], total_mat


def _carpet_replace_cost_usd(p):
    mat = p["sqft_chz"] * p["carpet_material_psf"]
    lab = p["sqft_chz"] * p["carpet_install_psf"]
    delivery = mat * p["delivery_fee_pct"]
    return mat + lab + delivery


def _n_carpet_replacements(p, horizon, twist):
    """How many full carpet replacements land inside the horizon.

    Base reading: multiples of the stated trigger year, strictly before the
    horizon's own end (a replacement due exactly on the last day buys no
    additional service life within the window being costed).
    Twist reading: the case's explicit twist schedule (heavy short-term-rental
    traffic roughly halves the effective trigger).
    """
    if twist:
        return sum(1 for y in p["carpet_replace_years_twist"] if y < horizon)
    trigger = p["carpet_replace_trigger_years"]
    n = 0
    t = trigger
    while t < horizon:
        n += 1
        t += trigger
    return n


def _option_a_cad(p, twist=False):
    initial_cad, _ = _initial_cad(p, p["carpet_material_psf"], p["carpet_install_psf"])
    horizon = p["horizon_years"]
    clean_usd = p["carpet_clean_psf_yr"] * p["sqft_chz"] * horizon
    n_tile = int(horizon // p["tile_service_interval_yrs"])
    tile_usd = p["tile_service_psf"] * p["sqft_tile"] * n_tile
    n_replace = _n_carpet_replacements(p, horizon, twist)
    replace_usd = _carpet_replace_cost_usd(p) * n_replace
    maint_usd = clean_usd + tile_usd + replace_usd
    return initial_cad + maint_usd * p["usd_to_cad"]


def _option_b_cad(p, twist=False):
    initial_cad, _ = _initial_cad(p, p["hardwood_material_psf"], p["hardwood_install_psf"])
    horizon = p["horizon_years"]
    n_tile = int(horizon // p["tile_service_interval_yrs"])
    tile_usd = p["tile_service_psf"] * p["sqft_tile"] * n_tile
    # hardwood service events: explicit years (a refinish year replaces any
    # recoat that would otherwise coincide with it -- see hardwood_recoat_years
    # / hardwood_refinish_years, which are already disjoint by construction).
    recoat_usd = p["sqft_chz"] * p["hardwood_recoat_psf"]
    refinish_usd = p["sqft_chz"] * p["hardwood_refinish_psf"]
    n_recoats = sum(1 for y in p["hardwood_recoat_years"] if y <= horizon)
    n_refinishes = sum(1 for y in p["hardwood_refinish_years"] if y <= horizon)
    hardwood_usd = recoat_usd * n_recoats + refinish_usd * n_refinishes
    maint_usd = tile_usd + hardwood_usd
    return initial_cad + maint_usd * p["usd_to_cad"]


def evaluate(params=None):
    """Primary graded metric: 15-yr total cost of ownership, base (no twist)."""
    p = dict(PARAMS)
    p.update(params or {})
    return {"A": round(_option_a_cad(p, twist=False), 2), "B": round(_option_b_cad(p, twist=False), 2)}


def evaluate_twist(params=None):
    """Twist lens: short-term-rental heavy traffic roughly halves carpet's
    effective replacement trigger, forcing a second full replacement inside
    the 15-year horizon. Hardwood unaffected."""
    p = dict(PARAMS)
    p.update(params or {})
    return {"A": round(_option_a_cad(p, twist=True), 2), "B": round(_option_b_cad(p, twist=False), 2)}


if __name__ == "__main__":
    base = evaluate({})
    tw = evaluate_twist({})
    base_margin = 100 * (base["B"] - base["A"]) / base["A"]
    tw_margin = 100 * (tw["A"] - tw["B"]) / tw["B"]
    print("base (evaluate)         A=$%.2f  B=$%.2f  (B-A)/A=%.1f%%  -> %s cheaper" %
          (base["A"], base["B"], base_margin, "A" if base["A"] < base["B"] else "B"))
    print("twist (evaluate_twist)  A=$%.2f  B=$%.2f  (A-B)/B=%.1f%%  -> %s cheaper" %
          (tw["A"], tw["B"], tw_margin, "B" if tw["B"] < tw["A"] else "A"))
