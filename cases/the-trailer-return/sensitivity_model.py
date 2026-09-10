#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Trailer Return.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the verdict") needs a
runnable model of the case's own arithmetic. Contract per
skills/case-readiness/scripts/example_sensitivity_model.py:

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     optional; same shape, with the twist applied

This case reports TWO metrics that can each flip independently, so `evaluate()` returns the
PRIMARY-METRIC verdict (deadhead ratio -- lower is better in the case's own framing, so the
returned score is negated so "higher is better" holds for this contract, matching how case.json's
balance_test.margin_pct is computed). A second helper, `evaluate_dollars()`, reports the raw daily
dollar comparison (also negated so higher-is-better), which is the OTHER lens FACILITATOR.md and
the Twist deliberately keep in tension with the primary metric -- flexing MA4 can move the dollar
verdict's margin without ever moving the primary-metric verdict, which is itself a documented,
disclosed finding (see MA4's sensitivity note in case.json), not a bug in this model.

Verified against cases/the-trailer-return/case.md and case.json:
    base   deadhead ratio: A=1.2069  B=1.1622   margin 3.70%   (matches case.json balance.margin_pct)
    base   daily dollars:  A=10.07   B=124.70   (matches Appendix E)
"""

PARAMS = {
    # --- Appendix A / D: the real, computed graph figures (not stated assumptions -- these are
    #     cited/derived from S3, included here only so probe 5's --flex-all sweep can be run
    #     against them if requested; FLEX below does NOT include these by default) ------------
    "base_mileage": 7.3245,
    "closed_extra_mileage": 1.5155,
    "open_extra_mileage": 1.1882,
    # --- Appendix E: cited figures (S1, S2) ----------------------------------------------------
    "mpg": 5.2392,
    "diesel_price_per_gal": 5.967,
    # --- Appendix F, MA4: the one real stated Modeling Assumption -----------------------------
    "trailer_fee": 115.0,
}

# Probe 5 flexes THESE and only these -- the case's own stated scenario assumption(s), per
# case-readiness doctrine ("sensitivity to STATED ASSUMPTIONS, not to cited measurements").
# mpg and diesel_price_per_gal are cited real-world figures (S1/S2), not scenario assumptions,
# so they are stress-tested by the data-decay probe (P6) instead, not flexed here by default.
FLEX = [
    "trailer_fee",   # Appendix F, MA4 -- the only genuinely stated assumption in this case
]


def _ratio(base, extra):
    return (base + extra) / base


def _fuel_cost(base, extra, mpg, diesel):
    return (base + extra) * (diesel / mpg)


def evaluate(params):
    """Primary-metric verdict: deadhead ratio. Lower ratio is better, so the score returned is
    negated (-ratio) so that, per contract, a HIGHER returned number means a BETTER option."""
    p = params
    ratio_a = _ratio(p["base_mileage"], p["closed_extra_mileage"])
    ratio_b = _ratio(p["base_mileage"], p["open_extra_mileage"])
    return {"A": -ratio_a, "B": -ratio_b}


def evaluate_dollars(params):
    """Secondary lens: raw daily dollar cost. Lower cost is better, so again negated."""
    p = params
    fuel_a = _fuel_cost(p["base_mileage"], p["closed_extra_mileage"], p["mpg"], p["diesel_price_per_gal"])
    fuel_b = _fuel_cost(p["base_mileage"], p["open_extra_mileage"], p["mpg"], p["diesel_price_per_gal"])
    cost_a = fuel_a
    cost_b = fuel_b + p["trailer_fee"]
    return {"A": -cost_a, "B": -cost_b}


def evaluate_twist(params):
    """The Twist (FACILITATOR.md) does not change either metric's arithmetic -- it changes which
    BUDGET LINE the $115/day trailer fee competes against, a qualitative reframing, not a numeric
    one. Both evaluate() and evaluate_dollars() are therefore unchanged under the twist; this
    function exists to satisfy the optional contract slot and to make that "no numeric change"
    finding explicit and checkable rather than silently absent."""
    return evaluate(params), evaluate_dollars(params)


if __name__ == "__main__":
    base_primary = evaluate(PARAMS)
    base_dollars = evaluate_dollars(PARAMS)
    ratio_a, ratio_b = -base_primary["A"], -base_primary["B"]
    cost_a, cost_b = -base_dollars["A"], -base_dollars["B"]
    print(f"PRIMARY METRIC (deadhead ratio, lower=better): A={ratio_a:.4f}  B={ratio_b:.4f}  "
          f"margin={100*(ratio_a-ratio_b)/ratio_a:.2f}%  winner={'B' if ratio_b < ratio_a else 'A'}")
    print(f"DOLLAR LENS (daily cost, lower=better):        A=${cost_a:.2f}  B=${cost_b:.2f}  "
          f"winner={'B' if cost_b < cost_a else 'A'}")

    print("\n--- Flexing MA4 (trailer_fee) +/-50% ---")
    for mult in (0.5, 1.0, 1.5):
        p = dict(PARAMS)
        p["trailer_fee"] = PARAMS["trailer_fee"] * mult
        d = evaluate_dollars(p)
        ca, cb = -d["A"], -d["B"]
        print(f"  trailer_fee x{mult:.1f} (${p['trailer_fee']:.2f}): A=${ca:.2f}  B=${cb:.2f}  "
              f"winner={'B' if cb < ca else 'A'}  (primary-metric winner is unaffected: B, always)")
