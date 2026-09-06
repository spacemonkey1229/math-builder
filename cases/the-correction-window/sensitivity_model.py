"""
sensitivity_model.py — The Correction Window

Graded primary metric (case.json.primary_metric): (1 - error_rate) / total_compute_budget_ms,
for each build, over Mara's 90-second canyon transit at the flight computer's 8 kHz correction
loop rate. Higher is better (more successful, in-tolerance corrections per millisecond of
flight-computer time spent on the sin(theta) approximation) -- matches this script's "higher
wins" convention (same convention as cases/the-deferred-repair/sensitivity_model.py).

    ops_per_correction(A) = 3   (theta^2, theta^3 = theta^2*theta, FMA: theta - theta^3/6)
    ops_per_correction(B) = 5   (the same 3, plus theta^5 = theta^3*theta^2,
                                  plus a second FMA adding theta^5/120)
    cycle_time_ns = 1e9 / clock_hz                                            [S1, sourced]
    -- both op counts assume single-cycle multiply/add/FMA on the Cortex-M4    [S2, sourced]

    total_cycles = transit_s * 1000 / loop_period_ms                          [S3, sourced]
    total_compute_budget_ms(option) = total_cycles * ops_per_correction[option]
                                       * cycle_time_ns / 1e6

    error_rate(option) = sum of MA1 band-weights whose exact |sin(theta) - poly(theta)|
                          exceeds MA2's tolerance, for that option's polynomial

Appendix A's clock speed [S1] and single-cycle-instruction fact [S2] and the 8 kHz loop-rate
practice [S3] are real, sourced figures -- NOT flexed by default (cited data, stress-tested by
P6 instead). Appendix E's gust-tilt band weights (MA1) and the correction-error tolerance (MA2)
are the case's own disclosed Modeling Assumptions -- no source publishes either for any real or
fictional canyon (RESEARCH_LOG.md, case.json.modeling_assumptions). These are the load-bearing,
dilemma-relevant dials the case names explicitly. FLEX below sweeps exactly these and nothing
else. Canyon transit time is deliberately NOT flexed: it multiplies both builds' total compute
cost equally and cancels out of the metric(A)/metric(B) RATIO entirely (see note in
evaluate()), so it can never move the margin or the winner -- it is a plain scenario constraint,
not a Modeling Assumption.

Verified against case.json.balance / FACILITATOR.md's margin arithmetic (project convention,
per skills/case-readiness/scripts/tier2_probes.py: margin_pct = 100*(winner-loser)/loser):
    base   A = 0.052111/ms  ·  B = 0.046667/ms  ·  margin 11.7%  (A wins -- matches case.json)
"""

import math

PARAMS = {
    # --- Appendix A [S1]/[S2]/[S3], sourced -------------------------------------
    "clock_hz": 168_000_000.0,     # STM32F405 Cortex-M4 max clock [S1]
    "loop_hz": 8000.0,             # correction-loop rate [S3]
    "transit_s": 90.0,             # stated scenario constraint (not an MA -- cancels in the ratio)
    "ops_A": 3,                    # derived operation count, Build 3 (theta - theta^3/6)
    "ops_B": 5,                    # derived operation count, Build 5 (theta - theta^3/6 + theta^5/120)

    # --- Appendix E, Modeling Assumption MA1 -- gust-tilt band weights ----------
    # Representative angles (degrees): 10, 20, 30, 40, 50. Must sum to 1.0.
    "gust_10": 0.40,
    "gust_20": 0.27,
    "gust_30": 0.20,
    "gust_40": 0.10,
    "gust_50": 0.03,

    # --- Appendix E, Modeling Assumption MA2 ------------------------------------
    "tolerance": 0.0003,
}

# Only MA1's five band weights and MA2's tolerance are swept by default (SPEC §2 asks
# for sensitivity to STATED ASSUMPTIONS, not cited measurements). clock_hz/loop_hz are
# real sourced figures [S1]/[S3] -- halving a datasheet clock speed is a different
# case, not a sensitivity test on this case's own authored assumption. transit_s is
# deliberately excluded even though it is a free dial: see the module docstring --
# it cancels out of the metric(A)/metric(B) ratio and can never move the margin.
FLEX = ["gust_10", "gust_20", "gust_30", "gust_40", "gust_50", "tolerance"]

_ANGLES_DEG = [10, 20, 30, 40, 50]


def _poly_errors(theta_deg):
    """Exact |sin(theta) - polynomial(theta)| for both builds at one angle (degrees)."""
    theta = math.radians(theta_deg)
    true_sin = math.sin(theta)
    poly_a = theta - theta**3 / 6.0
    poly_b = theta - theta**3 / 6.0 + theta**5 / 120.0
    return abs(true_sin - poly_a), abs(true_sin - poly_b)


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})

    cycle_time_ns = 1e9 / p["clock_hz"]
    loop_period_ms = 1000.0 / p["loop_hz"]
    total_cycles = (p["transit_s"] * 1000.0) / loop_period_ms

    cost_ms_A = total_cycles * p["ops_A"] * cycle_time_ns / 1e6
    cost_ms_B = total_cycles * p["ops_B"] * cycle_time_ns / 1e6

    weights = {d: p[f"gust_{d}"] for d in _ANGLES_DEG}
    err_rate_A, err_rate_B = 0.0, 0.0
    for deg, w in weights.items():
        err_a, err_b = _poly_errors(deg)
        if err_a > p["tolerance"]:
            err_rate_A += w
        if err_b > p["tolerance"]:
            err_rate_B += w

    metric_A = (1.0 - err_rate_A) / cost_ms_A
    metric_B = (1.0 - err_rate_B) / cost_ms_B
    return {"A": metric_A, "B": metric_B}


if __name__ == '__main__':
    base = evaluate({})
    a, b = base["A"], base["B"]
    win = "A" if a > b else ("B" if b > a else "TIE")
    lo, hi = min(a, b), max(a, b)
    # Project convention (tier2_probes.py): margin_pct = 100*(winner-loser)/loser.
    margin = 100.0 * (hi - lo) / lo if lo else 0.0
    print("base A=%.6f/ms  B=%.6f/ms  winner=%s  margin=%.1f%%" % (a, b, win, margin))
    print("(gust weights sum to %.4f -- should be 1.0000)" % sum(PARAMS[f"gust_{d}"] for d in _ANGLES_DEG))
