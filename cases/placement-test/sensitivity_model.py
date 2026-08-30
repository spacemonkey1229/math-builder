#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Placement Test.

Tier 2 probe 5: flex each stated assumption by +/-50% and report which flips
the verdict. Contract: PARAMS, evaluate(params) -> {"A": metric, "B": metric}.
No evaluate_twist() -- this case's Twist is N/A (see FACILITATOR.md).

The case's primary metric is statistically attributable conversions per
dollar of ad spend. Both options draw from the same total budget (MA2). The
Straight Cut spends it all on 1 variant; the Full Rotation splits it evenly
across 6 variants, but any variant whose split spend falls below the
Appendix C minimum-viable-spend threshold ($/variant, derived from MA3 x the
platform's conversion-count minimum over the MA1-week window) is excluded
from Option B's attributable-conversions total -- its data is not
statistically trustworthy and cannot be counted, per this case's own
margin_basis rule.

Verified against case.json.derived / FACILITATOR.md's Facilitator-only
numbers section:
    base   A = 80000.0  B = 80000.0   margin 0.0%  (exact tie, matches case.json margin_pct)

2026-08-30 retune: total_budget raised from $30,000 to $60,000 (see
case.json.balance.margin_note for the full rationale). At $30,000 the tie sat
EXACTLY on the Appendix C threshold with zero slack -- a +50% flex on either
weeks_remaining (MA1) or cost_per_conversion (MA3) alone was enough to push
the per-variant threshold above Full Rotation's fixed $5,000/variant split
and flip the recommendation to A for all six variants simultaneously (they
are excluded together, since every variant gets an identical split spend).
At $60,000, Full Rotation's split is $10,000/variant -- double the base
$5,000/variant threshold -- and re-running this flex sweep below confirms
NONE of the five stated assumptions flips the recommendation on its own
within a +/-50% move, including total_budget's own -50% flex (which lands
exactly back on the old $30,000 boundary and still clears, not falls below).
"""

PARAMS = {
    # --- Appendix A / E, MA1 --------------------------------------------------
    "weeks_remaining": 5.0,
    # --- Appendix B / E, MA2 (load-bearing; the case's own documented flip dial)
    "total_budget": 60000.0,
    # --- Appendix C / E, MA3 (load-bearing; the other documented flip dial) ---
    "cost_per_conversion": 20.0,
    # --- Appendix D / E, MA4/MA5 -- apply identically to both options, so the
    #     case's own sensitivity note says these cannot independently flip it.
    "conversion_rate": 0.02,
    "cpm": 15.0,
    # --- structural constants the case states, not modeling dials -------------
    "variants_a": 1,
    "variants_b": 6,
    "meta_min_events_per_week": 50.0,   # Appendix C / S2 -- cited, not flexed (P6 covers it)
}

# SPEC §2 sensitivity is about STATED ASSUMPTIONS, not cited measurements.
# MA1 (weeks_remaining) changes D1's permutation magnitude AND feeds directly
# into Appendix C's threshold formula (_threshold_per_variant below), so it
# IS part of the graded verdict's mechanism. At the pre-2026-08-30 $30,000
# budget, a +50% flex (5 -> 7.5 weeks) raised the threshold from $5,000 to
# $7,500/variant, which Full Rotation's then-fixed $5,000/variant split no
# longer cleared, flipping the recommendation to A. After the 2026-08-30
# retune to $60,000 ($10,000/variant), that same +50% flex still only raises
# the threshold to $7,500/variant -- Full Rotation now clears it with real
# slack ($2,500/variant, 33% above the threshold) instead of flipping.
# meta_min_events_per_week is cited data (S2), not an assumption -- excluded
# from FLEX, consistent with "cited data is stress-tested by P6 instead."
FLEX = [
    "weeks_remaining",       # MA1
    "total_budget",          # MA2 -- the case's own documented load-bearing dial
    "cost_per_conversion",   # MA3 -- the case's own documented load-bearing dial
    "conversion_rate",       # MA4 -- applies identically to both options per the case
    "cpm",                   # MA5 -- applies identically to both options per the case
]


def _threshold_per_variant(p):
    """Appendix C: derived minimum-viable spend per variant over the test
    window = (Meta's min events/week x weeks) x assumed cost/conversion."""
    events_over_window = p["meta_min_events_per_week"] * p["weeks_remaining"]
    return events_over_window * p["cost_per_conversion"]


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    conv_per_dollar = (1000.0 / p["cpm"]) * p["conversion_rate"]
    threshold = _threshold_per_variant(p)

    # Option A: all budget on 1 variant. Its spend is the whole budget, which
    # by construction (the case never lets total_budget go below a single
    # variant's own threshold in any realistic flex) clears the bar.
    a_spend = p["total_budget"] / p["variants_a"]
    a_conversions = a_spend * conv_per_dollar if a_spend >= threshold else 0.0

    # Option B: split the identical budget across variants_b. Any variant
    # whose split spend misses the threshold contributes zero attributable
    # conversions -- excluded, not silently counted, per margin_basis.
    b_spend_per_variant = p["total_budget"] / p["variants_b"]
    if b_spend_per_variant >= threshold:
        b_conversions = p["total_budget"] * conv_per_dollar
    else:
        b_conversions = 0.0

    return {"A": a_conversions, "B": b_conversions}


if __name__ == '__main__':
    base = evaluate({})
    lo = min(base, key=base.get)
    denom = base[lo] or 1
    margin = 100.0 * (max(base.values()) - min(base.values())) / denom
    print("base ", {k: round(v, 2) for k, v in base.items()}, "margin %.1f%%" % margin)
    print("threshold/variant:", _threshold_per_variant(PARAMS))
