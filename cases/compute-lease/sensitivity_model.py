#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Compute Lease.

Tier 2 probe 5 ("flex each stated assumption by +-50%; report which flips the
verdict") needs a runnable model of the case's own D2/D4 arithmetic.

CONTRACT — exactly two public names:

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

`evaluate()` returns the Mid-scenario (the case's own graded scenario, per
`case.json.balance.margin_basis`) cost per GPU-hour delivered for each option,
NEGATED, so that "higher is better" holds even though the case's own metric
is a cost (lower is better) -- same convention as cases/fret-board and
cases/enclosure-call's models, noted there for the same reason.

FLEX is scoped to the case's stated Modeling Assumptions only (MA1, MA2) --
per this project's doctrine, sensitivity to STATED ASSUMPTIONS is what P5
tests; sensitivity to cited/sourced data (S1/S2's rates, S3/S4/S5's growth
rates) is instead stress-tested by P6 (data decay), not P5. Run with
--flex-all to sweep everything (including the sourced dials) anyway.

Verified against case.json / case.md (2026-08-30 retune):
    base (Mid, 1.7%/month)   LL = $7.57/GPU-hr   OT = $6.88/GPU-hr
                             Open Tap wins, margin 9.1%   (matches case.json.balance.margin_pct)
"""

PARAMS = {
    # --- Appendix A / Modeling Assumptions -----------------------------------
    "n_gpus": 512.0,                    # MA1 -- Long Lock committed cluster size
    "starting_demand_gpu_hrs": 120000.0,  # MA2 -- Kestrel's month-0 GPU-hour demand
    # --- Appendix B, sourced (S2) --------------------------------------------
    "ll_rate_per_gpu_hr": 2.97,
    # --- Appendix C, sourced (S1) --------------------------------------------
    "ot_rate_per_gpu_hr": 6.88,
    # --- Appendix D, sourced (S3), the case's own graded scenario ------------
    "mid_growth_pct_month": 1.7,
    # --- fixed structural constants (not assumptions; SPEC/board-stated) -----
    "hours_per_month": 730.0,
    "n_months": 24,
}

# Probe 5 flexes THESE and only these by default: the two stated Modeling
# Assumptions. The rates and the growth rate are cited/sourced data (S1, S2,
# S3), stress-tested by P6 (data decay) instead of P5 -- flexing a sourced
# AWS list price or a DigitalOcean-reported growth rate by +-50% is not a
# sensitivity test of the case's own assumptions, it is a different case.
FLEX = [
    "n_gpus",                   # MA1
    "starting_demand_gpu_hrs",  # MA2
]


def _sum_demand(d0, r_pct_month, n_months):
    r = r_pct_month / 100.0
    if r == 0:
        return d0 * n_months
    return d0 * (((1 + r) ** n_months - 1) / r)


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})

    ll_total_cost = p["ll_rate_per_gpu_hr"] * p["n_gpus"] * p["hours_per_month"] * p["n_months"]
    sum_demand = _sum_demand(p["starting_demand_gpu_hrs"], p["mid_growth_pct_month"], int(p["n_months"]))

    ll_cost_per_hr = ll_total_cost / sum_demand
    ot_cost_per_hr = p["ot_rate_per_gpu_hr"]  # constant under this case's reading (cost = rate x hours)

    # Negate: lower cost per GPU-hour is better, but the harness convention is
    # higher-is-better, matching cases/fret-board and cases/enclosure-call.
    return {"A": -ll_cost_per_hr, "B": -ot_cost_per_hr}


def crossover_growth_pct_month(params=None):
    """Solve for the monthly growth rate at which A (Long Lock) and B (Open
    Tap) tie -- i.e. D5. Not part of the probe 5 contract; provided for
    convenience / cross-checking against case.json.derived."""
    p = dict(PARAMS)
    p.update(params or {})
    ll_total_cost = p["ll_rate_per_gpu_hr"] * p["n_gpus"] * p["hours_per_month"] * p["n_months"]
    target = p["ot_rate_per_gpu_hr"]

    lo, hi = 0.0001, 50.0
    for _ in range(80):
        mid = (lo + hi) / 2
        sd = _sum_demand(p["starting_demand_gpu_hrs"], mid, int(p["n_months"]))
        cost = ll_total_cost / sd
        # cost decreases as mid increases (more demand spreads the fixed cost further)
        if cost > target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


if __name__ == '__main__':
    base = evaluate({})
    ll, ot = -base["A"], -base["B"]
    winner = "B (Open Tap)" if ot < ll else "A (Long Lock)"
    loser_cost, winner_cost = max(ll, ot), min(ll, ot)
    margin = 100.0 * (loser_cost - winner_cost) / loser_cost
    print("base  LL/hr=$%.2f  OT/hr=$%.2f  winner=%s  margin=%.1f%%" % (ll, ot, winner, margin))
    print("D5 crossover (mid growth pct/month) = %.3f" % crossover_growth_pct_month())
