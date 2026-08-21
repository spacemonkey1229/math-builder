#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Insurance.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. This is that
model, for cases/insurance.

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):

    PARAMS                             dict[str, number]  every dial the case states
    FLEX                               list[str]          subset of PARAMS probe 5 flexes
    evaluate(params) -> dict           {"A": metric, "B": metric}
    evaluate_twist(params) -> dict     same shape, with the twist's own lens applied

IMPORTANT — metric direction: this case's primary metric is each plan's own
stated family out-of-pocket MAXIMUM in USD, so LOWER is better (same
convention as Family Trip's cost metric, opposite of Cold Chain's dose count).
Callers comparing A vs B for "the winner" should take the smaller value.

evaluate() returns the case's graded PRIMARY metric: each plan's own real,
stated, sourced family out-of-pocket maximum (case.json.primary_metric) --
Option A (HDHP) $12,800, Option B (Navigator Gold 2000) $12,000. This matches
case.json.balance (margin 6.7%, B lower/better). Deliberately, this metric
does NOT depend on any of this case's Modeling Assumptions -- it is read
directly from Appendix A/C's sourced plan terms -- so it is expected to be
completely stable under every FLEX sweep (see sensitivity_note in case.json).

evaluate_twist() returns a DIFFERENT, but connected, view: the REALIZED total
annual cost (premium + actual out-of-pocket) for each plan under the twist
scenario (Tiffany is pregnant this year), built from the family's real 2021
care pattern plus Navigator Gold 2000's own real SBC pregnancy example. This
is genuinely sensitive to the case's real Modeling Assumptions (MA1/MA3/MA4)
-- it is what the Twist actually recomputes live with the room. It is
intentionally a different unit (realized dollars, not a fixed cap) from
evaluate()'s fixed-cap metric: the twist does not change either plan's
*contractual* out-of-pocket maximum, it changes how much of that maximum
actually gets spent, which is the whole point of the reveal (see
case.json.balance.twist_effect).

Verified against case.md / case.json:
    evaluate({})        A = 12800.00  B = 12000.00   margin (A-B)/B =  6.7%   (fixed caps; B lower)
    evaluate_twist({})  A = 10351.41  B = 15066.00   margin (B-A)/A = 45.5%   (realized $ w/ pregnancy; A lower)

A helper, baseline_total(), is also provided (not part of the probe contract)
for the no-pregnancy realized-cost reading used in case.md D2's answer key.
"""

PARAMS = {
    # --- Appendix A, S1: friend's HDHP plan, given, unverifiable origin -----
    "hdhp_premium_monthly": 125.00,
    "hdhp_family_deductible": 6300.00,
    "hdhp_family_oop_max": 12800.00,
    # --- Appendix G, MA1: not given by the source, a stated scenario dial ---
    "hdhp_coinsurance_rate": 0.20,
    # --- Appendix A/C, S2/S3: real, sourced marketplace plan ----------------
    "gold_premium_monthly_net": 694.00,
    "gold_family_oop_max": 12000.00,
    "gold_pcp_copay": 20.00,
    "gold_specialist_copay": 40.00,
    "gold_chiro_copay": 20.00,
    "gold_rx_tier1_copay": 15.00,
    "gold_urgent_care_copay": 20.00,
    # --- Appendix D: the family's real, given 2021 recurring care pattern ---
    "pcp_visits": 10,          # Neri 4 (quarterly) + Tiffany 3 + Greg 3
    "specialist_visits": 4,    # Neri's urologist, quarterly
    "chiro_visits": 12,        # Greg, monthly
    "vcug_count": 2,           # Neri, biannual
    "rx_refills": 12,          # Neri, monthly
    # --- Appendix D, D3: mean-projected from the family's real 2020 record --
    "urgent_care_visits": 2,
    "er_visits": 1,
    # --- Appendix E, MA3/MA4: reference costs for services with no copay ----
    # (used only on the HDHP side, and on the Gold side only for the
    # coinsurance-eligible imaging/ER lines -- copay lines use the flat
    # copay amounts above regardless of the underlying bill)
    "pcp_reference_cost": 150.00,
    "specialist_reference_cost": 215.00,
    "vcug_reference_cost": 500.00,
    "urgent_care_reference_cost": 180.00,
    "er_reference_cost": 748.00,           # S7, real 2021 federal figure -- cited, not flexed
    # --- Appendix D: the family's own real, given cash prices ---------------
    "chiro_cash_cost": 134.00,             # real, given -- cited, not flexed
    "rx_cash_cost": 23.42,                 # real, given -- cited, not flexed
    # --- Appendix C, S3: Navigator Gold 2000's own real SBC coverage example
    "pregnancy_total_cost": 12700.00,      # real, cited -- not flexed
    "pregnancy_oop_gold": 4170.00,         # real, cited -- not flexed
}

# Probe 5 flexes THESE and only these -- the case's own STATED assumptions
# (Appendix G), not the cited/given data (S1-S8, or the family's own reported
# cash prices), which are stress-tested by the data-decay probe (P6) instead.
# hdhp_coinsurance_rate (MA1) is a pure scenario dial the source never states.
# The four *_reference_cost params (MA3/MA4) are disclosed proxies chosen
# because no dated, Idaho-specific figure exists for these services --
# genuine case-author estimates, not measurements. er_reference_cost is
# EXCLUDED from FLEX even though it looks similar: it is a real, cited 2021
# federal statistic (S7), not an assumption -- its own dating/proxy caveat is
# P6's job, not P5's.
FLEX = [
    "hdhp_coinsurance_rate",       # Appendix G, MA1
    "pcp_reference_cost",          # Appendix G, MA3
    "specialist_reference_cost",   # Appendix G, MA3
    "vcug_reference_cost",         # Appendix G, MA4
    "urgent_care_reference_cost",  # Appendix G, MA4
]


def _hdhp_preinsurance_allowed(p, include_pregnancy=False):
    total = (
        p["pcp_visits"] * p["pcp_reference_cost"]
        + p["specialist_visits"] * p["specialist_reference_cost"]
        + p["chiro_visits"] * p["chiro_cash_cost"]
        + p["rx_refills"] * p["rx_cash_cost"]
        + p["vcug_count"] * p["vcug_reference_cost"]
        + p["urgent_care_visits"] * p["urgent_care_reference_cost"]
        + p["er_visits"] * p["er_reference_cost"]
    )
    if include_pregnancy:
        total += p["pregnancy_total_cost"]
    return total


def _hdhp_oop(p, include_pregnancy=False):
    x = _hdhp_preinsurance_allowed(p, include_pregnancy)
    ded = p["hdhp_family_deductible"]
    if x <= ded:
        oop = x
    else:
        oop = ded + p["hdhp_coinsurance_rate"] * (x - ded)
    return min(oop, p["hdhp_family_oop_max"])


def _gold_oop(p, include_pregnancy=False):
    copays = (
        p["pcp_visits"] * p["gold_pcp_copay"]
        + p["specialist_visits"] * p["gold_specialist_copay"]
        + p["chiro_visits"] * p["gold_chiro_copay"]
        + p["rx_refills"] * p["gold_rx_tier1_copay"]
        + p["urgent_care_visits"] * p["gold_urgent_care_copay"]
    )
    # VCUG and ER are coinsurance-eligible (subject to deductible); this case
    # models neither family member as having already met their individual
    # deductible from any other spending, so both are paid in full (deductible
    # not met) at the reference cost -- see case.md Appendix C/G.
    vcug_and_er = p["vcug_count"] * p["vcug_reference_cost"] + p["er_visits"] * p["er_reference_cost"]
    oop = copays + vcug_and_er
    if include_pregnancy:
        oop += p["pregnancy_oop_gold"]
    return min(oop, p["gold_family_oop_max"])


def evaluate(params=None):
    """Primary graded metric: each plan's own fixed, sourced out-of-pocket maximum."""
    p = dict(PARAMS)
    p.update(params or {})
    return {"A": p["hdhp_family_oop_max"], "B": p["gold_family_oop_max"]}


def evaluate_twist(params=None):
    """Realized total annual cost (premium + OOP) under the twist (pregnancy this year)."""
    p = dict(PARAMS)
    p.update(params or {})
    a_total = p["hdhp_premium_monthly"] * 12 + _hdhp_oop(p, include_pregnancy=True)
    b_total = p["gold_premium_monthly_net"] * 12 + _gold_oop(p, include_pregnancy=True)
    return {"A": a_total, "B": b_total}


def baseline_total(params=None):
    """Not part of the probe contract -- the no-pregnancy realized-cost reading (case.md D2)."""
    p = dict(PARAMS)
    p.update(params or {})
    a_total = p["hdhp_premium_monthly"] * 12 + _hdhp_oop(p, include_pregnancy=False)
    b_total = p["gold_premium_monthly_net"] * 12 + _gold_oop(p, include_pregnancy=False)
    return {"A": a_total, "B": b_total}


if __name__ == "__main__":
    base = evaluate({})
    tw = evaluate_twist({})
    bl = baseline_total({})
    base_margin = 100 * (base["A"] - base["B"]) / base["B"]
    tw_margin = 100 * (tw["B"] - tw["A"]) / tw["A"]
    bl_margin = 100 * (bl["B"] - bl["A"]) / bl["A"]
    print("primary metric (evaluate, fixed caps)   A=$%.2f  B=$%.2f  (A-B)/B=%.1f%%  -> %s lower" %
          (base["A"], base["B"], base_margin, "B" if base["B"] < base["A"] else "A"))
    print("baseline realized total (no pregnancy)  A=$%.2f  B=$%.2f  (B-A)/A=%.1f%%  -> %s lower" %
          (bl["A"], bl["B"], bl_margin, "A" if bl["A"] < bl["B"] else "B"))
    print("twist realized total (with pregnancy)   A=$%.2f  B=$%.2f  (B-A)/A=%.1f%%  -> %s lower" %
          (tw["A"], tw["B"], tw_margin, "A" if tw["A"] < tw["B"] else "B"))
