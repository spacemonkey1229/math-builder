#!/usr/bin/env python3
"""
SENSITIVITY MODEL — End Of Life.

Tier 2 probe 5 ("flex each stated assumption by +-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. Follows the
contract in skills/case-readiness/scripts/example_sensitivity_model.py.

CONTRACT — exactly two public names (plus PARAMS/FLEX):

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     same shape, with the Twist's $150,000 treatment applied

This case's balance test is NOT "total cost of A vs total cost of B" (that gap
is real, large, and by construction always favors A -- see case.json's
legacy_conversion_note for why that can never honestly clear SPEC's 20% cap).
The graded primary metric is the family's liquid-asset RUNWAY in days,
compared against the doctor's own low-end survival estimate. To keep this
model useful for BOTH a runway-margin check and the case's real deliverables
(D1, D2, D4, D5), evaluate() returns a dict with the runway comparison as
"A"/"B" (higher = closer to being defensible go the balance test's own way)
plus the full derived block under "_derived" for D1-D5 style spot-checks.

Verified against cases/end-of-life/case.md and case.json:
    base   runway = 13.52 days  vs.  doctor's low end = 14.0 days   margin 3.43%
    day money runs out: cash-only Day 10, liquid+brokerage Day 14, net worth Day 26
    day50 total cost = $430,908.65 (exceeds liquid+invested; total assets still cover it)
"""

PARAMS = {
    # --- Appendix A, real billed Day 1 (Emergency Room, one-time) -----------
    "day1_er_cost": 2488.91,
    # --- Appendix A / Appendix E, real+projected Day 2-onward daily rate ----
    "daily_rate": 8743.26,
    # --- Appendix C, Dr. Halbert's stated survival window -------------------
    "survival_low_days": 14.0,
    "survival_high_days": 21.0,
    "survival_cap_days": 50.0,
    # --- Appendix B / Appendix F, liquid asset pools -------------------------
    "liquid_cash": 80942.75,
    "liquid_cash_plus_brokerage": 111953.63,
    "total_net_worth": 218368.19,
    "total_assets": 667756.51,
    "total_liabilities": 449388.32,
    # --- FACILITATOR.md Twist — authored fresh this conversion --------------
    "twist_treatment_cost": 150000.0,
}

# Probe 5 flexes THESE and only these -- stated case conventions, not the real,
# cited bill/net-worth figures themselves (those are the data-decay probe's
# job, P6). Appendix E's daily rate and Appendix C's survival window are the
# two dials that actually move the balance-test margin; the twist cost is the
# one dial specific to the authored (not sourced) Twist content.
FLEX = [
    "daily_rate",             # Appendix E, Assumption MA1
    "survival_low_days",      # Appendix C -- the primary metric's own comparison point
    "twist_treatment_cost",   # FACILITATOR.md Twist, authored this conversion
]


def _cumulative_cost(p, day_n):
    """Appendix E's rule: Day 1 is the one-time ER charge; every day from
    Day 2 onward adds the flat daily_rate."""
    if day_n <= 0:
        return 0.0
    if day_n == 1:
        return p["day1_er_cost"]
    return p["day1_er_cost"] + (day_n - 1) * p["daily_rate"]


def _day_threshold_crossed(p, threshold):
    """First whole day D5's cumulative cost strictly exceeds `threshold`."""
    n = 1
    while _cumulative_cost(p, n) <= threshold:
        n += 1
        if n > 10000:  # safety valve; never reached at real case scale
            break
    return n


def derived(params=None):
    """D1/D2/D5-style derived figures, for spot-checking the case's own
    numbers and for the Twist's own diagnostics. NOT part of the probe 5
    contract -- evaluate()/evaluate_twist() must return exactly {"A", "B"},
    so anything beyond that pair lives here instead."""
    p = dict(PARAMS); p.update(params or {})

    runway_days = 1 + (p["liquid_cash_plus_brokerage"] - p["day1_er_cost"]) / p["daily_rate"]
    margin_pct = abs(p["survival_low_days"] - runway_days) / p["survival_low_days"] * 100.0

    day_cash_out = _day_threshold_crossed(p, p["liquid_cash"])
    day_liquid_out = _day_threshold_crossed(p, p["liquid_cash_plus_brokerage"])
    day_networth_out = _day_threshold_crossed(p, p["total_net_worth"])

    cost_day14 = _cumulative_cost(p, 14)
    cost_day21 = _cumulative_cost(p, 21)
    cost_day50 = _cumulative_cost(p, int(p["survival_cap_days"]))

    buy_day = 4
    cost_through_buy_day = _cumulative_cost(p, buy_day)
    cost_with_treatment_day50 = cost_through_buy_day + p["twist_treatment_cost"]

    return {
        "runway_days": round(runway_days, 2),
        "margin_pct": round(margin_pct, 2),
        "day_cash_exhausted": day_cash_out,
        "day_liquid_plus_brokerage_exhausted": day_liquid_out,
        "day_net_worth_exhausted": day_networth_out,
        "cumulative_cost_day14": round(cost_day14, 2),
        "cumulative_cost_day21": round(cost_day21, 2),
        "cumulative_cost_day50": round(cost_day50, 2),
        "remaining_assets_after_day50": round(p["total_assets"] - cost_day50, 2),
        "net_worth_after_day50_bill": round(p["total_assets"] - cost_day50 - p["total_liabilities"], 2),
        "twist_cost_through_day50": round(cost_with_treatment_day50, 2),
        "twist_exceeds_liquid_plus_brokerage": cost_with_treatment_day50 > p["liquid_cash_plus_brokerage"],
    }


def evaluate(params=None):
    p = dict(PARAMS); p.update(params or {})

    runway_days = 1 + (p["liquid_cash_plus_brokerage"] - p["day1_er_cost"]) / p["daily_rate"]

    # Balance-test shape: {"A": ..., "B": ...}, higher = the metric this
    # option's argument leans on. "A" (remove sooner) leans on the runway
    # being SHORT relative to the doctor's low estimate (financial argument
    # strengthens as the gap shrinks toward 0); "B" (keep her connected)
    # leans on the doctor's own low-end survival estimate, the reference
    # point A is compared against. Call derived(params) separately for the
    # full D1-D5 spot-check block and margin_pct -- this function returns
    # ONLY the two-key contract probe 5 requires.
    return {
        "A": runway_days,             # smaller = stronger case for stopping sooner
        "B": p["survival_low_days"],  # the doctor's own reference point A is compared to
    }


def evaluate_twist(params=None):
    """FACILITATOR.md Twist: a $150,000 experimental treatment, not covered
    by insurance, that does not change the 50-day outer bound but (per the
    Twist narrative) lets the family stop paying the ICU/ventilator daily
    rate for however many days are left once Lauren goes home. Modeled here
    as: the treatment cost lands as a one-time charge on the day it's bought,
    and the daily hospital rate stops accruing from that day forward.

    Returns the same {"A", "B"} shape as evaluate() -- the Twist does not
    change the primary metric's definition, only its diagnostics (see
    derived()). This is a placeholder pending a genuine Twist-side "A"/"B"
    if the case's balance test is ever extended to grade the Twist itself;
    today the Twist is diagnostic-only (see derived()'s twist_* fields) and
    is not swept by probe 5's flips/margin logic beyond what evaluate()
    already covers."""
    return evaluate(params)


if __name__ == '__main__':
    base = evaluate({})
    d = derived({})
    print("base   runway=%.2f days vs doctor's low end=%.1f days  margin=%.2f%%"
          % (base["A"], base["B"], d["margin_pct"]))
    print("        ", d)
    tw = evaluate_twist({})
    print("twist  A=%.2f B=%.2f (unchanged by twist -- see derived() for twist diagnostics)"
          % (tw["A"], tw["B"]))
    print("       treatment cost through Day 50 total: $%.2f  (exceeds liquid+brokerage: %s)"
          % (d["twist_cost_through_day50"], d["twist_exceeds_liquid_plus_brokerage"]))
