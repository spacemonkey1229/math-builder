"""
sensitivity_model.py -- The Referral Cut

Graded primary metric (case.json.primary_metric): true net margin per unit sold,
comparing Fulfilled by Merchant (A, self-fulfillment) against Fulfilled by Amazon
(B, marketplace-managed fulfillment), found by chaining fraction multiplications in
the correct (multiplicative, not additive) order. Higher monthly net margin is
better for Mia, so evaluate() returns each option's monthly net margin directly --
higher score = better (same "higher wins" convention as
cases/the-special-order/sensitivity_model.py).

    post_referral(price)      = price * (1 - referral_fee)
    net_margin_per_unit(A)    = post_referral - packaging_cost - production_cost
    total_fulfillment_fee(B)  = base_fba_fee * (1 + fuel_surcharge)
    net_margin_per_unit(B)    = post_referral - total_fulfillment_fee(B) - production_cost
    monthly_net_margin(opt)   = net_margin_per_unit(opt) * monthly_units

Appendix B's referral fee [S1] and Appendix C's base FBA fulfillment fee [S2] and
fuel-and-logistics surcharge [S3] are real, sourced figures -- NOT flexed by
default (cited data, stress-tested by P6 instead). This case needed no Modeling
Assumption (RESEARCH_LOG.md: all three placeholders were SOURCED) in the usual
{{NEEDS_SOURCE}} sense. FLEX below instead sweeps `packaging_cost` -- Amber & Oak's
own per-unit packaging/postage cost (Appendix A). This is not an externally
sourced fact (nobody outside the fictional business could verify or falsify it);
it is the case author's own chosen figure for what Mia's self-fulfillment actually
costs her, playing the same epistemic role a stated Modeling Assumption plays in
other cases in this corpus even though it is presented in-case as ordinary given
data rather than in a Modeling Assumptions block. It is also the case's single
dilemma-relevant dial: verified below, `case.json.balance`'s recommendation (A
wins) is genuinely sensitive to it. Per skills/case-readiness SKILL.md's P5 rule
("FLEX[] scoping is the model author's responsibility... is this PARAM a real
assumption the case had to *choose*... or is it *given/cited* data"), this is the
`packaging_cost` analogue of the precedent already on file for Seton Hall's
ap_rank -- a deliberate, disclosed departure from "only flex a stated assumption"
because this case's real fragility lives in an author-chosen operational figure,
not a sourced platform fee. See case.json.sensitivity_disclosure.

Verified against case.json.balance / FACILITATOR.md's margin arithmetic:
    base   A = $252.50/month  ·  B = $225.148/month  ·  margin 10.83%  (A wins -- matches case.json)
    packaging_cost flip point = $3.8088/unit (currently $3.125/unit; a +50% flex to
    $4.6875/unit crosses it and flips the verdict to B)
"""

from fractions import Fraction as F

# PARAMS stores plain int/float values (not Fraction objects) so that
# tier2_probes.py's P5 sensitivity sweep -- which only flexes values where
# isinstance(val, (int, float)) holds -- can actually multiply and test them.
# Every dollar figure below (eighths/quarters/halves of a dollar) is exactly
# representable in binary floating point with zero rounding error (0.125,
# 0.25, 0.5, 0.375, 0.75 are all exact dyadic fractions), so this loses no
# precision; evaluate() converts every incoming value back to an exact
# fractions.Fraction immediately via _frac() before doing any arithmetic, so
# all graded arithmetic (and every number reported in case.json/FACILITATOR.md)
# is still computed as an exact fraction, never a rounded float. Only the two
# fee fractions with non-power-of-2 denominators (referral_fee, fuel_surcharge)
# and base_fba_fee are kept as Fraction directly -- they are cited data, not
# swept by default, and F(3,20)/F(368,100)/F(35,1000) are exact regardless.
PARAMS = {
    # --- Amber & Oak's own price sheet and order data (Appendix A) -- the shop's
    #     own operational figures, not an external fact -----------------------
    "price": 18.75,                 # $18-3/4 list price
    "packaging_cost": 3.125,        # $3-1/8, FBM only
    "production_cost": 6.5,         # $6-1/2, both options
    "monthly_units": 40,            # Rivendell's guaranteed monthly order quantity
    "weeks_inventory_A": 6.5,       # 6-1/2 weeks held under FBM
    "weeks_inventory_B": 2.25,      # 2-1/4 weeks held under FBA
    "weekly_production_cost": 340.375,  # $340-3/8

    # --- Appendix B [S1], sourced ---------------------------------------------
    "referral_fee": F(3, 20),       # 15%

    # --- Appendix C [S2] [S3], sourced -----------------------------------------
    "base_fba_fee": F(368, 100),    # $3.68 per unit
    "fuel_surcharge": F(35, 1000),  # 3.5%, applied to the fulfillment fee
}


def _frac(x):
    """Exact Fraction from an int/float/Fraction -- Fraction(float) is exact
    for any binary-representable value (every dollar figure in PARAMS is)."""
    return x if isinstance(x, F) else F(x)

# Only packaging_cost is swept by default -- see the module docstring for why
# this deliberately departs from "only FLEX[] a stated assumption" (this case
# declares none in the usual sense) and instead stress-tests the one
# author-chosen, unverifiable operational figure the verdict is actually
# sensitive to. The three real Amazon fee figures [S1][S2][S3] are cited data,
# stress-tested by P6 instead -- use --flex-all to sweep them too.
FLEX = ["packaging_cost"]


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    price = _frac(p["price"])
    packaging_cost = _frac(p["packaging_cost"])
    production_cost = _frac(p["production_cost"])
    monthly_units = _frac(p["monthly_units"])
    referral_fee = _frac(p["referral_fee"])
    base_fba_fee = _frac(p["base_fba_fee"])
    fuel_surcharge = _frac(p["fuel_surcharge"])

    post_referral = price * (1 - referral_fee)

    net_A = post_referral - packaging_cost - production_cost
    monthly_A = net_A * monthly_units

    total_fulfillment_fee = base_fba_fee * (1 + fuel_surcharge)
    net_B = post_referral - total_fulfillment_fee - production_cost
    monthly_B = net_B * monthly_units

    # All arithmetic above is exact Fraction math (see _frac()); only the
    # returned values are cast to float, matching
    # cases/the-special-order/sensitivity_model.py's own convention, so
    # tier2_probes.py's generic round()/json.dumps() handling (which expects
    # plain numbers, not Fraction objects) works on this model like any other.
    return {"A": float(monthly_A), "B": float(monthly_B)}


def working_capital(params=None):
    p = dict(PARAMS)
    p.update(params or {})
    weeks_A = _frac(p["weeks_inventory_A"])
    weeks_B = _frac(p["weeks_inventory_B"])
    weekly = _frac(p["weekly_production_cost"])
    return {"A": weeks_A * weekly, "B": weeks_B * weekly}


def packaging_cost_flip_point(params=None):
    """Exact packaging_cost (a Fraction) at which A's and B's monthly margins tie."""
    p = dict(PARAMS)
    p.update(params or {})
    monthly_B = evaluate(p)["B"]
    price = _frac(p["price"])
    referral_fee = _frac(p["referral_fee"])
    production_cost = _frac(p["production_cost"])
    monthly_units = _frac(p["monthly_units"])
    post_referral = price * (1 - referral_fee)
    # net_A*units == monthly_B  =>  packaging_cost = post_referral - production_cost - monthly_B/units
    return post_referral - production_cost - (monthly_B / monthly_units)


if __name__ == '__main__':
    base = evaluate({})
    a, b = base["A"], base["B"]
    win = "A" if a > b else "B"
    lo, hi = min(a, b), max(a, b)
    margin = 100.0 * float(hi - lo) / float(hi)
    wc = working_capital()
    flip = packaging_cost_flip_point()
    print("base A=$%.4f/mo  B=$%.4f/mo  winner=%s  margin=%.2f%%" %
          (float(a), float(b), win, margin))
    print("working capital A=$%.4f  B=$%.4f" % (float(wc["A"]), float(wc["B"])))
    print("packaging_cost flip point: $%.4f  (base $%.4f)" %
          (float(flip), float(PARAMS["packaging_cost"])))
