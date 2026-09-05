#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Quiet Thief.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own D1-D4 arithmetic: derive a
real (inflation-adjusted) monthly rate of return from the sourced nominal
return and sourced inflation rate (D1), grow Priya's contribution to a real
target balance (D2), then solve backward for the monthly contribution each of
Jordan's two plans requires to reach that same target (D3/D4).

CONTRACT -- exactly two required public names:

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

The primary metric is a REQUIRED MONTHLY CONTRIBUTION -- a cost, where LOWER
is actually better for Jordan. Per the P5 contract ("higher is better"),
evaluate() returns the NEGATED required contribution for each plan, so a
smaller dollar requirement (a plan that's cheaper to fund) correctly scores
higher. This mirrors the negation convention used in
cases/the-deferred-repair and cases/the-breakeven-mile's cost-minimizing
models.

    real_annual   = (1 + nominal) / (1 + inflation) - 1                 (D1)
    real_monthly  = (1 + real_annual)^(1/12) - 1                        (D1)
    FV (Priya)    = C * ((1+r)^n_priya - 1) / r                         (D2)
    PMT(n)        = FV * r / ((1+r)^n - 1)                              (D3/D4)
    A = -PMT(n_bridge_months)     (Jordan's Bridge Plan contribution, negated)
    B = -PMT(n_extended_months)   (Jordan's Extended Plan contribution, negated)

Appendix A/C's contribution amount [MA2], nominal return [S2] and inflation
rate [S3] are either cited data or a disclosed-non-load-bearing scenario
constant -- NOT flexed by default (P6, data decay, covers the two cited rates
instead; see "Only FLEX[] is swept" in skills/case-readiness/SKILL.md's P5
section). MA1 (the two starting ages, fixed narrative constants) is likewise
excluded -- case.json.modeling_assumptions[MA1].sensitivity notes it scales
the case proportionally but is not a free scenario dial being tested here.

MA3 (the Extended Plan's 2-year retirement-age delay) IS the genuine,
disclosed case-design assumption this case asks a reader to weigh -- it is
the one dial that was actually chosen (among several tested candidates, see
RESEARCH_LOG.md) specifically to land the margin inside the case's 10-15%
target band. FLEX sweeps exactly this one dial, consistent with
case.json.sensitivity_disclosure[]'s Category D framing (a disclosed
case-balance constant, not a hidden fragility).

Verified against case.json.balance / FACILITATOR.md (2026-09-04):
    base (MA3=2 years)  Bridge=$816.84/mo  Extended=$705.27/mo  margin=13.66%
"""

PARAMS = {
    # --- Appendix C [S2], sourced long-run average annual nominal return ----
    "nominal_annual_rate": 0.10,
    # --- Appendix C [S3], sourced long-run average annual inflation rate ----
    "inflation_annual_rate": 0.031,
    # --- Appendix A / Modeling Assumption MA2, both savers' monthly ---------
    #     contribution -- disclosed non-load-bearing scenario constant (see
    #     case.json.modeling_assumptions[MA2].sensitivity: scales A and B
    #     proportionally, does not move the margin between them).
    "monthly_contribution_usd": 400.0,
    # --- Appendix A/B / Modeling Assumption MA1, the two starting ages ------
    "priya_start_age": 25,
    "jordan_start_age": 35,
    # --- Appendix A/B [S1], sourced shared target retirement age ------------
    "retirement_age": 67,
    # --- Appendix B / Modeling Assumption MA3, Extended Plan's delay --------
    #     THE genuine disclosed case-design assumption this case asks a
    #     reader to weigh (see case.json.sensitivity_disclosure[], Category D).
    "extended_plan_delay_years": 2,
}

# Probe 5 flexes THIS and only this by default: the one genuinely disclosed
# case-design dial (MA3). The two cited rates (nominal return, inflation) are
# stress-tested by P6 (data decay) instead; the contribution amount and the
# two starting ages are fixed narrative/scenario constants whose own
# case.json sensitivity notes already state they don't move the margin or
# are not free dials being tested here. Run with --flex-all to sweep
# everything anyway.
FLEX = [
    "extended_plan_delay_years",
]


def _real_monthly_rate(p):
    """D1: derive the real annual rate from the two sourced rates, then
    convert to an equivalent monthly rate."""
    real_annual = (1.0 + p["nominal_annual_rate"]) / (1.0 + p["inflation_annual_rate"]) - 1.0
    real_monthly = (1.0 + real_annual) ** (1.0 / 12.0) - 1.0
    return real_monthly


def _future_value(contribution, r, n_months):
    """D2: ordinary-annuity future value of a level monthly contribution."""
    return contribution * (((1.0 + r) ** n_months - 1.0) / r)


def _required_pmt(fv, r, n_months):
    """D3/D4: rearranged annuity formula, solved for the monthly contribution
    required to reach a target future value in n_months."""
    return fv * r / ((1.0 + r) ** n_months - 1.0)


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})

    r = _real_monthly_rate(p)

    n_priya = (p["retirement_age"] - p["priya_start_age"]) * 12
    fv_priya = _future_value(p["monthly_contribution_usd"], r, n_priya)

    n_bridge = (p["retirement_age"] - p["jordan_start_age"]) * 12
    n_extended = (p["retirement_age"] + p["extended_plan_delay_years"] - p["jordan_start_age"]) * 12

    pmt_bridge = _required_pmt(fv_priya, r, n_bridge)
    pmt_extended = _required_pmt(fv_priya, r, n_extended)

    # Negated: this metric is a COST (a required monthly contribution), and
    # the P5 contract expects "higher is better" -- so a cheaper (smaller)
    # required contribution must score higher.
    return {"A": -pmt_bridge, "B": -pmt_extended}


def evaluate_nominal_rate_trap(params=None):
    """D5: the case's own disclosed rubric trap -- recompute the Bridge
    Plan's required contribution using the un-adjusted NOMINAL rate instead
    of the derived real rate. Not part of the probe 5 contract (it isn't a
    second scenario for the A-vs-B dilemma; it's a wrong-methodology
    illustration), provided so case.json.balance's disclosed 49.13%
    understatement figure is independently checkable."""
    p = dict(PARAMS)
    p.update(params or {})
    r_nominal_monthly = (1.0 + p["nominal_annual_rate"]) ** (1.0 / 12.0) - 1.0
    r_real_monthly = _real_monthly_rate(p)

    n_priya = (p["retirement_age"] - p["priya_start_age"]) * 12
    fv_priya = _future_value(p["monthly_contribution_usd"], r_real_monthly, n_priya)

    n_bridge = (p["retirement_age"] - p["jordan_start_age"]) * 12
    pmt_correct = _required_pmt(fv_priya, r_real_monthly, n_bridge)
    pmt_naive = _required_pmt(fv_priya, r_nominal_monthly, n_bridge)

    understatement_pct = (pmt_correct - pmt_naive) / pmt_correct * 100.0
    return {"correct": pmt_correct, "naive": pmt_naive, "understatement_pct": understatement_pct}


if __name__ == '__main__':
    base = evaluate({})
    pmt_a, pmt_b = -base["A"], -base["B"]
    lo, hi = min(pmt_a, pmt_b), max(pmt_a, pmt_b)
    margin = 100.0 * (hi - lo) / hi
    print("base (MA3=2 years)  Bridge=$%.2f/mo  Extended=$%.2f/mo  margin=%.2f%%"
          % (pmt_a, pmt_b, margin))
    assert abs(margin - 13.66) < 0.05, "margin drifted from case.json's recorded 13.66%"

    trap = evaluate_nominal_rate_trap()
    print("\nD5 nominal-rate trap: correct=$%.2f/mo  naive(nominal rate)=$%.2f/mo  understatement=%.2f%%"
          % (trap["correct"], trap["naive"], trap["understatement_pct"]))
    assert abs(trap["understatement_pct"] - 49.13) < 0.1, "D5 understatement drifted from disclosed 49.13%"

    print("\n+/-50%% flex of MA3 (extended_plan_delay_years):")
    for mult, label in ((0.5, "-50%"), (1.5, "+50%")):
        years = PARAMS["extended_plan_delay_years"] * mult
        r = evaluate({"extended_plan_delay_years": years})
        a2, b2 = -r["A"], -r["B"]
        lo2, hi2 = min(a2, b2), max(a2, b2)
        m2 = 100.0 * (hi2 - lo2) / hi2
        print("  delay=%.2f yrs (%s)  Bridge=$%.2f/mo  Extended=$%.2f/mo  margin=%.2f%%"
              % (years, label, a2, b2, m2))

    print("\nWider check -- delay of 1, 2 (base), and 5 years:")
    for years in (1, 2, 5):
        r = evaluate({"extended_plan_delay_years": years})
        a2, b2 = -r["A"], -r["B"]
        lo2, hi2 = min(a2, b2), max(a2, b2)
        m2 = 100.0 * (hi2 - lo2) / hi2
        print("  delay=%d yrs  Bridge=$%.2f/mo  Extended=$%.2f/mo  margin=%.2f%%"
              % (years, a2, b2, m2))
