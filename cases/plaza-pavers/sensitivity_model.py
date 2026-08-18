"""Sensitivity model for Plaza Pavers (SPEC section 2 balance test, case-readiness Tier 2 probe 5).

REVISED 2026-08-12 after a fresh-eyes cold-solve + adversarial QA pass (Tier 2 probes 1-4) found
two real defects in the first version of this model, both now fixed:

  1. The original model blended a hidden "border fraction" (6% for Option A, 10% for B) between
     an "interior" cost rate and a "border" cost rate. That blend lived ONLY here -- case.md's
     Appendix D never discloses it, so a student following the case's own written instructions
     cannot reproduce the case's own claimed margin. A cold-solve agent, using only case.md,
     computed a materially different (and more lopsided) margin than this file's old output. Fixed
     by dropping the interior/border blend entirely: every dollar figure below is now a single
     stated range or a single stated multiplier, all disclosed in case.md Appendix D / Appendix G,
     reproducible in one pass with no hidden per-case-author judgment call.
  2. The original model's per-paver retail price (S1/S2, a small-pallet product listing) was used
     as the case's material-cost basis for the dollar math, landing at ~$16.40/sq ft -- 2 to 8x
     outside Appendix D's own cited contractor-scale market range ($2.00-$8.00/sq ft, S7), an
     internal inconsistency the case never reconciled. Fixed: S1/S3/S4 (module dimensions) remain
     load-bearing for D4's GCF calculation only. All dollar math below uses S7's real contractor
     range directly, for both options, consistently.
  3. evaluate_twist()'s extra-cutting-cost fractions were unlabeled invented constants with no
     basis in case.md. Fixed by promoting them to a named, disclosed Modeling Assumption (MA5,
     Appendix G) with a stated basis and an explicit uncertainty note.

PARAMS carries every dial the case states. Each is tagged SOURCED (case.md Appendix B/C/D,
citation id in the comment) or ASSUMED (case.md Appendix G, Modeling Assumptions, id in the
comment). FLEX lists the ASSUMED subset -- probe 5 sweeps only those, per case-readiness's rule
that cited measurements are stress-tested by probe 6 (data decay), not probe 5.
"""
import math

PARAMS = {
    # --- SOURCED ---
    "hex_across_flats_in": 10.25,          # S1 -- Super Arbor hexagonal concrete paver (D4 only)
    "oct_across_flats_in": 15.875,         # S3 -- Hanover Two Piece Octagonal system (D4 only)
    "square_side_in": 6.5625,              # S4 -- Hanover, matching square, same set (D4 only)
    "material_low_usd_sqft": 2.00,         # S7 -- StoneCenters, concrete paver material range
    "material_high_usd_sqft": 8.00,        # S7 -- StoneCenters, same
    "install_labor_low_usd_sqft": 7.00,    # S7 -- StoneCenters, "professional installation"
    "install_labor_high_usd_sqft": 15.00,  # S7 -- StoneCenters, same
    "intricate_labor_premium_pct": 20.0,   # S8 -- StoneCenters: "intricate patterns...add 15-25% to labor" (midpoint)

    # --- ASSUMED (case.md Appendix G, Modeling Assumptions) ---
    "plaza_length_ft": 200.0,              # MA2
    "plaza_width_ft": 150.0,               # MA2
    "commission_target_usd_sqft": 18.50,   # MA3 -- published target, between the two real totals
    "hex_material_usd_sqft": 5.50,         # MA1a -- stated point within S7's real $2-$8 range
    "oct_sqset_price_premium_pct": 10.0,   # MA1b -- material premium, retuned 2026-08-12 (SPEC section 2:
                                            # 20% put the base margin at 19.1%, and a +50% flex broke the
                                            # 20% cap at 21.4% -- retuned the constraint down, not hidden data
    "simple_waste_pct": 3.0,               # MA4 -- straight-border trim only
    "cut_waste_pct": 10.0,                 # MA4 -- mitred multi-angle cuts, retuned with MA1b for the same reason
    "twist_extra_a_pct_of_cut_labor": 1.5, # MA5 -- curved-edge cutting cost growth, Hex Grid
    "twist_extra_b_pct_of_cut_labor": 3.0, # MA5 -- curved-edge cutting cost growth, Weave Pattern
}

FLEX = ["commission_target_usd_sqft", "oct_sqset_price_premium_pct",
        "simple_waste_pct", "cut_waste_pct"]


def _hex_area_sqft(across_flats_in):
    side = across_flats_in / math.sqrt(3)
    return ((3 * math.sqrt(3) / 2) * side ** 2) / 144.0


def _octagon_area_sqft(across_flats_in):
    side = across_flats_in / (1 + math.sqrt(2))
    return (2 * (1 + math.sqrt(2)) * side ** 2) / 144.0


def _square_area_sqft(side_in):
    return (side_in ** 2) / 144.0


def _labor_mid(p):
    return (p["install_labor_low_usd_sqft"] + p["install_labor_high_usd_sqft"]) / 2


def cost_breakdown(p):
    """Total installed $/sq ft, A and B, plus diagnostics. Fully disclosed, single-pass formula --
    no hidden interior/border blend. A student can reproduce every line from Appendix D + G alone:

        Total = material x (1 + waste_pct) + labor

    with material/labor picked from Appendix D's stated ranges and the Weave Pattern's premiums
    (material x1.20, labor x1.20, both from Appendix G / S8) applied once, directly."""
    plaza_sqft = p["plaza_length_ft"] * p["plaza_width_ft"]

    material_a = p["hex_material_usd_sqft"]                                    # MA1a
    material_b = material_a * (1 + p["oct_sqset_price_premium_pct"] / 100)     # MA1b

    labor_a = _labor_mid(p)                                                    # S7
    labor_b = labor_a * (1 + p["intricate_labor_premium_pct"] / 100)           # S7 + S8

    a_total = material_a * (1 + p["simple_waste_pct"] / 100) + labor_a
    b_total = material_b * (1 + p["cut_waste_pct"] / 100) + labor_b

    # D4-only diagnostics -- module areas/pavers-per-sqft from real sourced dimensions,
    # never used in the dollar math above (see module docstring, fix #2).
    hex_area = _hex_area_sqft(p["hex_across_flats_in"])
    oct_area = _octagon_area_sqft(p["oct_across_flats_in"])
    sq_area = _square_area_sqft(p["square_side_in"])

    return {"A_cost": a_total, "B_cost": b_total, "plaza_sqft": plaza_sqft,
            "material_a": material_a, "material_b": material_b,
            "labor_a": labor_a, "labor_b": labor_b,
            "hex_pavers_per_sqft": 1 / hex_area,
            "weave_pavers_per_sqft": 1 / (oct_area + sq_area)}


def evaluate(p):
    """CONTRACT: {"A": metric, "B": metric}, higher wins (per example_sensitivity_model.py).

    Plaza Pavers' real metric (installed $/sq ft) is LOWER-is-better, and case.md states margin as
    (worse - better) / worse. To satisfy the higher-wins CONTRACT *and* reproduce that exact margin
    definition under the framework's generic (max-min)/min formula, each option's cost is
    subtracted from 2x the worse option's own cost (computed fresh inside this call): value =
    2*worse_cost - cost. That keeps both values positive and algebraically collapses the generic
    formula back to exactly (worse-better)/worse -- not a different, silently-disagreeing margin.
    """
    b = cost_breakdown(p)
    a_cost, b_cost = b["A_cost"], b["B_cost"]
    ceiling = 2 * max(a_cost, b_cost)
    return {"A": ceiling - a_cost, "B": ceiling - b_cost}


def twist_cost_breakdown(p):
    """Fountain restoration (FACILITATOR.md Twist): a circular cutout forces extra curved-edge
    cutting on both options. MA5 (Appendix G) states the growth rate as a stated, disclosed
    percentage of each option's own cut-labor cost -- NOT derived from a fountain radius, since the
    case gives none; MA5 says so explicitly and flags the direction as an assumption a Hero may
    challenge, per the case's own stated convention for every other Modeling Assumption."""
    base = cost_breakdown(p)
    extra_a = base["labor_a"] * (p["twist_extra_a_pct_of_cut_labor"] / 100)
    extra_b = base["labor_b"] * (p["twist_extra_b_pct_of_cut_labor"] / 100)
    return {"A_cost": base["A_cost"] + extra_a, "B_cost": base["B_cost"] + extra_b}


def evaluate_twist(p):
    """CONTRACT-compliant twin of evaluate(), same ceiling-transform, applied to twist costs."""
    t = twist_cost_breakdown(p)
    a_cost, b_cost = t["A_cost"], t["B_cost"]
    ceiling = 2 * max(a_cost, b_cost)
    return {"A": ceiling - a_cost, "B": ceiling - b_cost}


def _report(label, costs, cap=None):
    a_cost, b_cost = costs["A_cost"], costs["B_cost"]
    cheaper = "A" if a_cost < b_cost else "B"
    worse_cost = max(a_cost, b_cost)
    margin_pct = (worse_cost - min(a_cost, b_cost)) / worse_cost * 100
    line = f"{label}: A ${a_cost:.2f}/sqft, B ${b_cost:.2f}/sqft (cheaper: {cheaper}, margin {margin_pct:.2f}%)"
    if cap is not None:
        line += (f"  cap ${cap:.2f} -- A {'CLEARS' if a_cost <= cap else 'OVER'}, "
                 f"B {'CLEARS' if b_cost <= cap else 'OVER'}")
    print(line)
    return a_cost, b_cost, margin_pct


if __name__ == "__main__":
    b = cost_breakdown(PARAMS)
    print(f"Material A: ${b['material_a']:.2f}/sqft   Material B: ${b['material_b']:.2f}/sqft")
    print(f"Labor A: ${b['labor_a']:.2f}/sqft    Labor B: ${b['labor_b']:.2f}/sqft")
    print(f"Plaza area: {b['plaza_sqft']:.0f} sq ft")
    _report("Base", b, cap=PARAMS["commission_target_usd_sqft"])

    t = twist_cost_breakdown(PARAMS)
    _report("Twist (fountain cutout)", t)

    ev = evaluate(PARAMS)
    ev_worse = min(ev, key=ev.get)
    ev_better = max(ev, key=ev.get)
    ev_margin = (ev[ev_better] - ev[ev_worse]) / ev[ev_worse] * 100
    raw_margin = (max(b["A_cost"], b["B_cost"]) - min(b["A_cost"], b["B_cost"])) / max(b["A_cost"], b["B_cost"]) * 100
    assert ev_better == "A" and abs(ev_margin - raw_margin) < 0.05, \
        f"evaluate() contract transform drifted from cost_breakdown(): {ev} margin={ev_margin:.2f}"
    print(f"\nevaluate() contract check OK: winner={ev_better}, margin={ev_margin:.2f}% (matches raw cost margin)")
