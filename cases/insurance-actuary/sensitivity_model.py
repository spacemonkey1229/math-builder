#!/usr/bin/env python3
"""
Sensitivity model — Insurance Actuary.

CONTRACT (skills/case-readiness/scripts/tier2_probes.py, Probe 5):
    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  HIGHER IS BETTER

The case's primary metric is a *cost* (lower Ĉ/vehicle is better), so `evaluate`
reports the IMPROVEMENT each option buys relative to making no change at all —
i.e. (today's full-book blended rate) minus (the option's remaining-book blended
rate). A bigger improvement is better, satisfying the "higher is better" contract
without inverting the case's own stated metric.

DATA — Appendix A. Quarterly car-years of exposure and Ĉ claims incurred,
2016Q1-2018Q4, by driver-age class, summed across all 9 Vehicle-Size x Risk
sub-classes within each age class. Reproduced from the bundled workbook
`Safetylife Insurance Data.xlsx`, sheet "Claims Data" (the case's own given
data — not an external citation; see RESEARCH_LOG.md).

THE ONE STATED ASSUMPTION — Appendix A, "How the 2019 figures were forecast":
each age class's 2019 quarterly run-rate is projected by fitting a least-
squares line to its 12 known quarters (2016Q1-2018Q4) and extending that line
through 2019Q1-2019Q4. The case states this outright: nothing in Safetylife's
data says the 2016-2018 trend will continue into 2019 — that continuation is
an authorial modeling choice, not a fact. `trend_continuation` is the dial:
1.0 reproduces the case's own published forecast (the trend continues exactly
as observed); 0.0 assumes the trend flattens at the 2018Q4 run-rate; 2.0
assumes the observed trend doubles. Probe 5 flexes this dial +/-50% around 1.0.
"""

QUARTERS = list(range(12))          # 2016Q1 .. 2018Q4, t = 0..11
FORECAST_QUARTERS = [12, 13, 14, 15]  # 2019Q1 .. 2019Q4

# --- Appendix A, quarterly car-years of exposure ---------------------------
EXP_YOUNG = [53224.0, 53964.0, 54437.0, 54579.0, 54628.0, 55068.0,
             55350.0, 55434.0, 55398.0, 55845.0, 55893.0, 55663.0]
EXP_MIDDLE = [243097.0, 246563.0, 248653.0, 248837.0, 248659.0, 251021.0,
              252627.0, 252603.0, 251896.0, 254642.0, 255698.0, 254725.0]
EXP_SENIOR = [153595.0, 155917.0, 156935.0, 156630.0, 157007.0, 158745.0,
              159307.0, 158747.0, 158804.0, 160483.0, 160414.0, 159012.0]

# --- Appendix A, quarterly Ĉ claims incurred (all 5 coverages summed) ------
AMT_YOUNG = [100693118.0, 113976755.0, 113589075.0, 114712887.0, 115801146.0,
             108722060.0, 120817896.0, 114173843.0, 120102268.0, 106321090.0,
             120104053.0, 116356882.0]
AMT_MIDDLE = [417593876.0, 381249897.0, 431307164.0, 421605301.0, 427651000.0,
              416800035.0, 443943267.0, 454576808.0, 460875438.0, 442558679.0,
              450445898.0, 478618020.0]
AMT_SENIOR = [279911613.0, 295039075.0, 302607475.0, 320671193.0, 305867859.0,
              324291581.0, 323332576.0, 313956811.0, 331356790.0, 321135663.0,
              325741157.0, 316956571.0]

PARAMS = {
    # Appendix A — "How the 2019 figures were forecast." The case's ONE
    # stated modeling assumption: the 2016-2018 linear trend continues,
    # unscaled, into 2019.
    "trend_continuation": 1.0,
}

FLEX = ["trend_continuation"]


def _linreg(y):
    n = len(y)
    xbar = sum(QUARTERS) / n
    ybar = sum(y) / n
    num = sum((QUARTERS[i] - xbar) * (y[i] - ybar) for i in range(n))
    den = sum((QUARTERS[i] - xbar) ** 2 for i in range(n))
    slope = num / den
    intercept = ybar - slope * xbar
    return slope, intercept


def _forecast_2019(y, trend_continuation):
    slope, intercept = _linreg(y)
    scaled_slope = slope * trend_continuation
    # Anchor the scaled line through the same fitted mean point (xbar, ybar)
    # so trend_continuation=0 forecasts "flat at the fitted 2016-2018 average
    # trajectory's current level," not a discontinuous jump.
    xbar = sum(QUARTERS) / len(QUARTERS)
    ybar = sum(y) / len(y)
    scaled_intercept = ybar - scaled_slope * xbar
    return sum(scaled_intercept + scaled_slope * t for t in FORECAST_QUARTERS)


def _class_forecast(trend_continuation):
    out = {}
    for name, exp, amt in (("Young", EXP_YOUNG, AMT_YOUNG),
                            ("Middle", EXP_MIDDLE, AMT_MIDDLE),
                            ("Senior", EXP_SENIOR, AMT_SENIOR)):
        fe = _forecast_2019(exp, trend_continuation)
        fa = _forecast_2019(amt, trend_continuation)
        out[name] = (fe, fa)
    return out


RATE_SCALE = 1_000_000.0   # arbitrary constant; only ratios between A and B matter


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    fc = _class_forecast(p["trend_continuation"])
    y_exp, y_amt = fc["Young"]
    m_exp, m_amt = fc["Middle"]
    s_exp, s_amt = fc["Senior"]

    # Option A: discontinue Young -> remaining book is Middle + Senior
    a_rate = (m_amt + s_amt) / (m_exp + s_exp)
    # Option B: discontinue Senior -> remaining book is Young + Middle
    b_rate = (y_amt + m_amt) / (y_exp + m_exp)

    # The case's own primary metric (Ĉ/vehicle) is LOWER-is-better. Probe 5's
    # contract requires HIGHER-is-better, so report the reciprocal, scaled by
    # a constant so the numbers are a readable size. For a margin this thin
    # (~2%), a reciprocal's percent margin is numerically almost identical to
    # the original rate's percent margin (and always points the same
    # direction), so this is a faithful higher-is-better restatement of the
    # same comparison, not a different metric.
    return {"A": RATE_SCALE / a_rate, "B": RATE_SCALE / b_rate}


if __name__ == '__main__':
    base = evaluate({})
    print("base", {k: round(v, 2) for k, v in base.items()})
    lo = evaluate({"trend_continuation": 0.5})
    hi = evaluate({"trend_continuation": 1.5})
    print("trend x0.5", {k: round(v, 2) for k, v in lo.items()})
    print("trend x1.5", {k: round(v, 2) for k, v in hi.items()})
