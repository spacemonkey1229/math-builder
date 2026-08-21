#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Movie Executive.

CONTRACT (case-readiness Tier 2, probe 5) — exactly two public names, per
skills/case-readiness/scripts/example_sensitivity_model.py:

    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     same shape, with FACILITATOR.md's Twist applied

`primary_metric` = projected opening-weekend box office revenue per dollar of
production budget, for each film:

    revenue   = top2box_fraction * addressable_audience * top2box_mean_price
    metric    = revenue / production_budget

`top2box_fraction`, `top2box_mean_price`, `production_budget`, and each
film's sample size are the case's own GIVEN data (Appendix A/B's survey
tables and stated budgets) — real assumptions the case had to choose, they
are not. They are held fixed and are NOT in FLEX[], per the doctrine in
skills/case-readiness/SKILL.md ("Only FLEX[] is swept by default... cited
data is stress-tested by P6 instead").

Only two dials are genuine STATED assumptions:
  - `addressable_audience` (Appendix E, MA1) — the national addressable
    opening-weekend audience. Flexing this scales both films' projected
    revenue equally; it cancels out of the A/B ratio and should NOT flip
    the verdict. A sensitivity probe that finds it flips the verdict would
    itself be a modeling bug — see the assertion in __main__.
  - `twist_correction_retained_fraction` — the share of Flower's Ice's
    "excess" definite-buyer rate over Waves' that FACILITATOR.md's Twist
    treats as trustworthy signal rather than convenience-sample selection
    bias. Grounded in sources[].S3 (Pew Research Center's finding that the
    best correction techniques recovered ~30% of a nonprobability sample's
    bias) but applied here as a stylized scenario construction for THIS
    twist, the same way Cold Chain's reference model flexes its own
    `twist_detour_h` — so it is treated as a scenario dial, in FLEX[], not
    as cited data P6 alone covers.

Verified against cases/movie-producer/case.json and FACILITATOR.md:
    base   A = 0.2654  ·  B = 0.2332  ·  margin 13.8%   (A ahead)
    twist  A = 0.2654  ·  B ~= 0.1954  ·  margin ~36%   (A ahead, decisively)
"""

PARAMS = {
    # --- Appendix A: Waves In The Tales (given survey + budget data) --------
    "waves_n": 15,
    "waves_top2box_n": 4,
    "waves_top2box_price": 8.0,
    "budget_a": 64_300_000,
    # --- Appendix B: The Flower's Ice (given survey + budget data) ----------
    "flower_n": 23,
    "flower_top2box_n": 8,
    "flower_top2box_price": 8.625,
    "budget_b": 102_900_000,
    # --- Appendix E, MA1: the one real stated assumption ---------------------
    "addressable_audience": 8_000_000,
    # --- the Twist (FACILITATOR.md), grounded in sources[].S3 ---------------
    "twist_correction_retained_fraction": 0.30,
}

# Probe 5 flexes THESE and only these. Sample sizes, top-2-box counts/prices,
# and production budgets are the case's own given data, not assumptions —
# halving Waves' n=15 would be a different case, not a sensitivity test.
FLEX = [
    "addressable_audience",                 # Appendix E, MA1
    "twist_correction_retained_fraction",   # scenario construction (FACILITATOR.md Twist)
]


def _top2box_fracs(p):
    return p["waves_top2box_n"] / p["waves_n"], p["flower_top2box_n"] / p["flower_n"]


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    a_frac, b_frac = _top2box_fracs(p)
    rev_a = a_frac * p["addressable_audience"] * p["waves_top2box_price"]
    rev_b = b_frac * p["addressable_audience"] * p["flower_top2box_price"]
    return {"A": rev_a / p["budget_a"], "B": rev_b / p["budget_b"]}


def evaluate_twist(params):
    p = dict(PARAMS)
    p.update(params or {})
    a_frac, b_frac = _top2box_fracs(p)
    excess = b_frac - a_frac
    trusted_excess = p["twist_correction_retained_fraction"] * excess
    adj_b_frac = a_frac + trusted_excess
    rev_a = a_frac * p["addressable_audience"] * p["waves_top2box_price"]
    rev_b = adj_b_frac * p["addressable_audience"] * p["flower_top2box_price"]
    return {"A": rev_a / p["budget_a"], "B": rev_b / p["budget_b"]}


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})
    m_base = 100 * (base["A"] - base["B"]) / base["B"]
    m_tw = 100 * (tw["A"] - tw["B"]) / tw["B"]
    print("base ", {k: round(v, 4) for k, v in base.items()}, "margin %.2f%%" % m_base)
    print("twist", {k: round(v, 4) for k, v in tw.items()}, "margin %.2f%%" % m_tw)

    # Sanity check the docstring's own claim: addressable_audience must NOT
    # move the winner (it scales both films equally and cancels in the ratio).
    half = evaluate({"addressable_audience": PARAMS["addressable_audience"] * 0.5})
    double = evaluate({"addressable_audience": PARAMS["addressable_audience"] * 2.0})
    assert (half["A"] > half["B"]) == (base["A"] > base["B"]), "addressable_audience flipped the winner"
    assert (double["A"] > double["B"]) == (base["A"] > base["B"]), "addressable_audience flipped the winner"
    print("addressable_audience confirmed non-flip-driving at 0.5x and 2.0x")
