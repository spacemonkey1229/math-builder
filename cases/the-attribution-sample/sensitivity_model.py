#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Attribution Sample.

Tier 2 probe 5 ("flex each stated assumption by +-50%; report which flips
the verdict") needs a runnable model of the case's own arithmetic.

CONTRACT — two public names:

    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

The case's SPEC Section 2 primary metric (case.json.balance.margin_basis) is
pooled (whole-report) attribution-error standard error, in percentage points,
divided by total analyst-hours spent verifying (setup + per-click
verification). Lower pp/hour is BETTER (less error per hour of analyst time),
but the probe's contract is "higher is better", so evaluate() returns the
NEGATIVE of that ratio.

Mechanism modeled explicitly (this is the whole point of the case):
Option A (Pooled Random Sample) draws one simple random sample of n=400
clicks from the pooled stream; each channel's EXPECTED sample count is
proportional to its click-volume share, so the small Influencer/Affiliate
channel (2% share) gets an expected n of only 8 -- a standard error of
sqrt(p(1-p)/n) that is nearly useless for a budget decision. Option B
(Channel-Stratified Sample) guarantees a minimum floor sample in that same
small channel, at the cost of more setup time and more total verification
minutes (since the small channel's per-click verification is also the
slowest, per MA12).

FLEX[] sweeps the case's own stated Modeling Assumptions that feed this
metric's arithmetic: MA4 (channel shares -- the Affiliate share specifically),
MA5 (Option A total sample size), MA6/MA8 (setup times), MA7 (Option B's
floor size), and MA12's four per-click verification times. MA1-MA3 (deadline
framing, hours budget, total population) are not swept: MA1/MA3 are flavor
only and never enter the ratio; MA2 (the 13-hour weekend budget) is a
feasibility ceiling checked separately, not an input to the ratio itself.
MA9-MA11 (per-channel true-install rates) ARE swept, since they set each
channel's p(1-p) variance term.
"""

import math

PARAMS = {
    # --- Appendix A / MA4: channel shares of total weekly clicks -----------
    "share_san": 0.62,
    "share_dsp": 0.26,
    "share_owned": 0.10,
    "share_affiliate": 0.02,
    # --- Appendix D / MA9-MA11: true-install rate by channel (S3 for Owned) -
    "p_san": 0.95,
    "p_dsp": 0.85,
    "p_owned": 0.89,      # S3, real sourced figure (89% = 1 - 11% fraud)
    "p_affiliate": 0.85,
    # --- Appendix E / MA12: per-click verification time (minutes) ----------
    "time_san": 1.0,
    "time_dsp": 2.0,
    "time_owned": 2.0,
    "time_affiliate": 5.0,
    # --- Appendix B / MA5-MA6: Option A spec --------------------------------
    "n_total_a": 400.0,
    "setup_hours_a": 0.5,
    # --- Appendix C / MA7-MA8: Option B spec --------------------------------
    "floor_affiliate_b": 40.0,
    "setup_hours_b": 1.4,
    # --- Appendix A / MA2: weekend verification-hours budget (feasibility) -
    "hours_budget": 13.0,
}

# Probe 5 flexes THESE and only these: the case's own stated Modeling
# Assumptions that feed the graded primary metric's arithmetic.
FLEX = [
    "share_affiliate",     # MA4, Appendix A -- the case's real fulcrum
    "n_total_a",            # MA5, Appendix B
    "setup_hours_a",         # MA6, Appendix B
    "floor_affiliate_b",      # MA7, Appendix C
    "setup_hours_b",           # MA8, Appendix C
    "time_affiliate",          # MA12, Appendix E
    "p_affiliate",               # MA11, Appendix D
]

CHANNELS = ["san", "dsp", "owned", "affiliate"]


def _se(p, n):
    if n <= 0:
        return float("inf")
    # Clamp p into a valid probability range so a +-50% FLEX sweep on
    # p_affiliate (base 0.85) can't push p above 1.0 and blow up sqrt().
    p = min(max(p, 0.001), 0.999)
    return math.sqrt(p * (1.0 - p) / n)


def _option_a_allocation(p):
    n_total = p["n_total_a"]
    shares = {c: p[f"share_{c}"] for c in CHANNELS}
    return {c: shares[c] * n_total for c in CHANNELS}


def _option_b_allocation(p):
    floor = p["floor_affiliate_b"]
    remaining = p["n_total_a"] - floor  # same total sample size as A
    other = [c for c in CHANNELS if c != "affiliate"]
    weight_sum = sum(p[f"share_{c}"] for c in other)
    alloc = {"affiliate": floor}
    for c in other:
        alloc[c] = remaining * p[f"share_{c}"] / weight_sum
    return alloc


def _pooled_se(alloc, p):
    total = 0.0
    for c in CHANNELS:
        w = p[f"share_{c}"]
        pc = min(max(p[f"p_{c}"], 0.001), 0.999)
        n = alloc[c]
        total += w * w * pc * (1.0 - pc) / n
    return math.sqrt(total)


def _verification_hours(alloc, p):
    minutes = sum(alloc[c] * p[f"time_{c}"] for c in CHANNELS)
    return minutes / 60.0


def evaluate_detail(params):
    p = dict(PARAMS)
    p.update(params or {})

    alloc_a = _option_a_allocation(p)
    alloc_b = _option_b_allocation(p)

    se_a = _pooled_se(alloc_a, p)
    se_b = _pooled_se(alloc_b, p)

    hours_a = _verification_hours(alloc_a, p) + p["setup_hours_a"]
    hours_b = _verification_hours(alloc_b, p) + p["setup_hours_b"]

    ratio_a = se_a * 100.0 / hours_a  # pp per hour
    ratio_b = se_b * 100.0 / hours_b

    detail_a = {
        "allocation": alloc_a,
        "channel_se_pp": {c: _se(p[f"p_{c}"], alloc_a[c]) * 100.0 for c in CHANNELS},
        "pooled_se_pp": se_a * 100.0,
        "hours": hours_a,
        "ratio_pp_per_hour": ratio_a,
        "fits_budget": hours_a <= p["hours_budget"],
    }
    detail_b = {
        "allocation": alloc_b,
        "channel_se_pp": {c: _se(p[f"p_{c}"], alloc_b[c]) * 100.0 for c in CHANNELS},
        "pooled_se_pp": se_b * 100.0,
        "hours": hours_b,
        "ratio_pp_per_hour": ratio_b,
        "fits_budget": hours_b <= p["hours_budget"],
    }

    # Lower pp/hour is better; evaluate()'s contract is "higher is better",
    # so return the negated ratio.
    return {"A": -ratio_a, "B": -ratio_b}, detail_a, detail_b


def evaluate(params):
    """Tier 2 probe 5 contract: evaluate(params) -> {'A': metric, 'B': metric}
    ONLY -- no extra return values, since the probe's own max()/min() over
    the return value would otherwise break on a 3-tuple. Full diagnostics
    (per-channel breakdown, hours, budget fit) are in evaluate_detail()."""
    r, _a, _b = evaluate_detail(params)
    return r


if __name__ == "__main__":
    base, a, b = evaluate_detail({})
    win = max(base, key=base.get)  # higher (less negative) evaluate() value wins
    lo = min(base, key=base.get)
    win_ratio, lo_ratio = -base[win], -base[lo]  # back to actual pp/hour
    margin = 100.0 * (lo_ratio - win_ratio) / lo_ratio  # % the loser costs MORE pp/hr than the winner

    print("Option A (Pooled Random Sample):")
    for k, v in a.items():
        print(f"  {k}: {v}")
    print("Option B (Channel-Stratified Sample):")
    for k, v in b.items():
        print(f"  {k}: {v}")
    print()
    print("ratio (pp/hr)  A=%.4f  B=%.4f" % (-base["A"], -base["B"]))
    print("winner:", win, " margin: %.2f%%" % margin)

    # Sweep FLEX at +-50% one at a time, report which flips the winner.
    print()
    print("--- FLEX sweep (+-50%) ---")
    for key in FLEX:
        base_val = PARAMS[key]
        for mult, label in [(0.5, "-50%"), (1.5, "+50%")]:
            trial, _, _ = evaluate_detail({key: base_val * mult})
            trial_win = max(trial, key=trial.get)
            flipped = trial_win != win
            print(f"  {key} {label} ({base_val} -> {base_val*mult:.4g}): winner={trial_win}"
                  f"{'  *** FLIPS ***' if flipped else ''}")
