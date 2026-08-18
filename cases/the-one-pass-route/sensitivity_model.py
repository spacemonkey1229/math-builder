#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- The One-Pass Route.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. Contract per
skills/case-readiness/scripts/example_sensitivity_model.py:

    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            the STATED-ASSUMPTION subset
    evaluate(params) -> dict   {"A": metric, "B": metric}   HIGHER metric wins
    evaluate_twist(params)     N/A -- this case has no twist (no evaluate_twist
                                is defined; FACILITATOR.md's "trap" is the
                                dollars-vs-ratio tension baked into the case
                                from the start, not a reveal partway through)

This case's stated primary_metric is the deadhead ratio (total miles driven /
total miles of street actually serviced, for one full sweep). Like
The Optimal Can, that metric's natural comparison isn't "bigger number wins"
for both sides -- The As-Is Loop (A) has no lever to pull, it simply *is* what
the network's topology forces. So evaluate() expresses A's position as a fixed
0 and B's position as its improvement over A on the primary metric (ratio_A -
ratio_B, positive = the connector genuinely lowers the ratio), keeping the
shared "higher is better" shape without inventing a third, oppositely-signed
quantity.

FLEX-scoping (SKILL.md's 2026-08-13 note): PARAMS holds every number case.md
states, sourced or assumed. FLEX holds ONLY the one genuine, numerically
flexible stated assumption this case has -- MA3, sweep frequency (Appendix E).
It deliberately does NOT flex:
  - base_mileage_mi, repeat_mileage_asis_mi, connector_length_mi/ft,
    repeat_mileage_connector_mi -- all [S3, derived]: real OpenStreetMap
    street-network data and this case's own exact graph-theory computation
    (minimum-weight T-join matching), not an assumption the author chose.
    Flexing the underlying network topology is not "sensitivity to an
    assumption," it is a different neighborhood -- MA1's own sensitivity note
    says as much. P6 (data decay) covers this data instead.
  - fuel_efficiency_mpg [S1] and diesel_price_usd_per_gal [S2] -- cited
    external figures (a disclosed refuse-truck mpg proxy, and a live EIA
    price series), not scenario dials the case invented.
  - construction_cost_per_ft_usd [S5] -- a cited, disclosed-proxy municipal
    figure, not an assumption; its two-source discrepancy ($1,600 vs. $345/ft)
    is itself a P6-style data-quality question, not a P5 assumption flex, and
    FACILITATOR.md's own "second-order trap" already establishes the
    conclusion is insensitive to which one is used.
  - MA2 (the 0.2-mile district-boundary exclusion threshold) is a genuine
    stated modeling assumption (Appendix E) but is NOT flexible here: it
    determines which raw OSM way segments get collapsed into vertices/edges
    in the first place, and this case ships only the final, already-collapsed
    58-vertex/86-edge graph (Appendix A), not the pre-exclusion raw pull.
    Re-deriving the graph under a different threshold would require rerunning
    the Overpass fetch and vertex-collapse pipeline, which is outside what a
    sensitivity_model.py can honestly do with the numbers case.md states. This
    is a real, disclosed limitation, not an oversight -- flagged here rather
    than faked with a fabricated multiplier.
  - MA1 (using Seaside, FL as the real-network stand-in for Talbrook) is not
    a numeric dial at all; there is nothing to flex by +/-50%.

MA3 (sweep_frequency_per_year) is included precisely because Appendix E's own
sensitivity column makes a falsifiable claim about it: "it does not change the
deadhead ratio itself, which is a per-sweep, frequency-independent quantity."
evaluate() below proves that claim true by construction -- sweep frequency
never enters the ratio computation at all, only the (non-primary-metric)
dollar-savings/payback figures computed by the helper functions. A genuine
P5 run on this case is therefore expected to find ZERO instability from
flexing MA3: that is not a bug in the model, it is the case's own disclosed
finding, reproduced mechanically.

Verified against cases/the-one-pass-route/case.json (Appendix C Part 2,
Appendix D, balance.margin_pct):
    ratio_A (As-Is Loop)          1.2285   (matches Appendix C, Part 2)
    ratio_B (Persimmon Connector) 1.2050   (matches Appendix D)
    margin_pct                    1.9      (matches balance.margin_pct)
    annual fuel-cost savings      $0.14/yr (matches Appendix D)
    payback period                ~3.35 million years (matches Appendix D)
"""

PARAMS = {
    # --- Appendix A [S3, derived]: real network, base street mileage --------
    "base_mileage_mi": 3.9597,
    # --- Appendix C, Part 2 [S3, derived]: minimum repeat mileage, As-Is ----
    "repeat_mileage_asis_mi": 0.9046,
    # --- Appendix D [S3, derived]: Persimmon Connector length ---------------
    "connector_length_ft": 302.0,
    # --- Appendix D [S3, derived]: minimum repeat mileage, with connector ---
    "repeat_mileage_connector_mi": 0.8236,
    # --- Appendix C, Part 2 [S1]: proxy sweeper-truck fuel efficiency -------
    "fuel_efficiency_mpg": 5.2,
    # --- Appendix C, Part 2 [S2]: US average diesel price --------------------
    "diesel_price_usd_per_gal": 5.257,
    # --- Appendix C, Part 2 / Appendix E, MA3: sweep frequency --------------
    "sweep_frequency_per_year": 6.0,
    # --- Appendix D [S5]: construction cost per linear foot -----------------
    "construction_cost_per_ft_usd": 1600.0,
}

# Probe 5 flexes THESE and only these. SPEC section 2 asks for sensitivity to
# STATED ASSUMPTIONS, not to cited measurements or to the case's own sourced
# graph data -- see the long note above for why every other PARAMS entry is
# excluded. MA3 is this case's one genuinely flexible stated assumption.
FLEX = [
    "sweep_frequency_per_year",   # MA3 -- Appendix E
]


def _ratios(p):
    """Deadhead ratio for each option: total miles driven / total miles of
    street actually serviced, for one full sweep (case.md's primary_metric).
    Returns (ratio_A, ratio_B, total_A, total_B, new_base_mileage_mi)."""
    total_a = p["base_mileage_mi"] + p["repeat_mileage_asis_mi"]
    ratio_a = total_a / p["base_mileage_mi"]

    connector_length_mi = p["connector_length_ft"] / 5280.0
    new_base_mileage_mi = p["base_mileage_mi"] + connector_length_mi
    total_b = new_base_mileage_mi + p["repeat_mileage_connector_mi"]
    ratio_b = total_b / new_base_mileage_mi

    return ratio_a, ratio_b, total_a, total_b, new_base_mileage_mi


def evaluate(params=None):
    """{"A": 0.0, "B": ratio_A - ratio_B}. Higher is better. A is always
    exactly 0 -- The As-Is Loop is not a lever anyone pulls, it is simply what
    the existing network's topology forces. B > 0 means the connector lowers
    the deadhead ratio (verdict favors The Persimmon Connector on the stated
    primary metric); B < 0 would mean the connector makes the ratio worse.
    sweep_frequency_per_year deliberately never appears in this computation --
    see the module docstring; that is this case's own disclosed finding, not
    an omission."""
    p = dict(PARAMS)
    p.update(params or {})
    ratio_a, ratio_b, _, _, _ = _ratios(p)
    return {"A": 0.0, "B": ratio_a - ratio_b}


def annual_fuel_savings_usd(params=None):
    """The dollar-side figure Appendix D reports (not the primary metric, but
    the number the case's whole trap turns on). Uses sweep_frequency_per_year,
    unlike evaluate() above."""
    p = dict(PARAMS)
    p.update(params or {})
    _, _, total_a, total_b, _ = _ratios(p)
    miles_saved_per_sweep = total_a - total_b
    annual_miles_saved = miles_saved_per_sweep * p["sweep_frequency_per_year"]
    gallons_saved = annual_miles_saved / p["fuel_efficiency_mpg"]
    return gallons_saved * p["diesel_price_usd_per_gal"]


def payback_years(params=None):
    p = dict(PARAMS)
    p.update(params or {})
    cost = p["connector_length_ft"] * p["construction_cost_per_ft_usd"]
    savings = annual_fuel_savings_usd(p)
    return cost / savings if savings else float("inf")


if __name__ == "__main__":
    p = dict(PARAMS)
    ratio_a, ratio_b, total_a, total_b, new_base = _ratios(p)
    margin = 100.0 * (ratio_a - ratio_b) / ratio_a
    savings = annual_fuel_savings_usd(p)
    payback = payback_years(p)

    print("ratio_A %.4f  ratio_B %.4f  margin_pct %.4f%%" % (ratio_a, ratio_b, margin))
    print("annual_fuel_savings_usd %.4f  payback_years %.1f" % (savings, payback))

    base = evaluate({})
    print("evaluate() ->", base, " winner:", "A" if base["A"] >= base["B"] else "B")

    # Sanity check against case.json's stated figures (rounded the same way).
    assert round(ratio_a, 4) == 1.2285, ratio_a
    assert round(ratio_b, 4) == 1.2050, ratio_b
    assert round(margin, 1) == 1.9, margin
    assert round(savings, 2) == 0.14, savings
    assert 3_000_000 < payback < 3_700_000, payback

    # MA3's own disclosed claim, proven mechanically: sweep frequency cannot
    # move the primary-metric verdict at all, in either flex direction.
    for freq in (p["sweep_frequency_per_year"] * 0.5, p["sweep_frequency_per_year"] * 1.5):
        flexed = evaluate({"sweep_frequency_per_year": freq})
        assert flexed == base, (freq, flexed, base)

    print("All checks passed.")
