#!/usr/bin/env python3
"""
Sensitivity model — Caribbean Internet Café.

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset that is a genuine ASSUMPTION
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     optional; same shape, with the twist applied

Primary metric: CIC's expected monthly pre-tax operating cash flow (JA$), under Appendix E's
REALISTIC market-research scenario, before any split of profit between David and JTL. Higher is
better. Source of every PARAMS value: cases/caribbean-internet-cafe/case.md, Appendices B-F.

    base   A = 85,045.83   B = 96,983.33   margin 14.0% (B higher)   (matches case.json.balance)

FLEX[] holds ONLY genuine stated assumptions (Appendix F), never cited/given data:
    - market_loan_rate_annual: Appendix F MA1 -- Option A's financing rate is ASSUMED (the case's
      own quoted 25% Jamaican mortgage rate, applied here because CIC's case never quotes an
      independent lender's rate directly). This is the case's single load-bearing dial.
    - weeks_per_month: Appendix F MA3 -- a modeling convention (52/12), not a number the case states
      directly; a different convention is equally defensible.
    - staff_hours_per_week: Appendix F MA4 -- Appendix C's "needs staff on hand for about 90 hours
      a week (an average of two employees on duty at a time)" is ambiguous between a total-hours
      reading (90, used as the base value here) and a coverage-hours-times-headcount reading (180).
      Found during Tier 2 P1 cold-solve, 2026-08-17.
Everything else (equipment costs, JTL's 10% rate, JTL's loan/equity amounts, Appendix C's other
wages/prices/costs, Appendix E's segment size/visit rates) is GIVEN data from the source document,
not an assumption -- excluded from FLEX per the "only sweep stated assumptions" rule. Cited data
is stress-tested by Tier 2 probe 6 (data decay) instead.

NOTE (added 2026-08-17, P2 both-sides-solve fix): the PRIMARY metric this model's evaluate()
computes is CIC's company-level cash flow, BEFORE any split of profit between David and JTL --
matching case.json.primary_metric. A separate, materially different comparison exists and is real:
David's OWN personal take-home once each option's ownership share is applied (100% under A, 50%
under B, per Appendix D) -- Option A wins that comparison by roughly 75%, not Option B. That
comparison is deliberately NOT what evaluate() computes (see case.json.balance.margin_basis for
why), so it is not swept by FLEX here; the fixed figures are recorded in
case.json.derived.david_personal_take_home_A_realistic_jad /
_B_realistic_jad and case.json.balance.personal_take_home_note.
"""

PARAMS = {
    # --- Appendix B: startup equipment (JA$, already converted from US$ at 35:1) --------------
    "equipment_total_jad": 1426000.0,
    # --- Appendix D: other up-front costs (JA$) ------------------------------------------------
    "upfront_legal_license_decor_jad": 120000.0,
    "preopening_advertising_jad": 20000.0,
    "utility_deposit_jad": 7000.0,
    # --- Appendix D: capital available --------------------------------------------------------
    "david_savings_jad": 500000.0,
    "jtl_equity_jad": 500000.0,
    "jtl_loan_jad": 1250000.0,
    "jtl_loan_rate_annual": 0.10,          # GIVEN -- JTL's quoted concessionary rate
    "david_ownership_share_a": 1.0,        # GIVEN -- David keeps 100% under Option A
    "david_ownership_share_b": 0.5,        # GIVEN -- JTL buys 50% equity under Option B (Appendix D)
    # --- Appendix F, MA1: Option A's assumed financing rate (FLEX) -----------------------------
    "market_loan_rate_annual": 0.25,       # ASSUMED -- the case's own quoted Jamaican mortgage rate
    # --- Appendix F, MA3: calendar convention (FLEX) --------------------------------------------
    "weeks_per_month": 52.0 / 12.0,
    # --- Appendix C: fixed monthly costs (JA$) --------------------------------------------------
    "manager_salary_month": 40000.0,
    "lease_month": 30000.0,
    "telephone_utilities_month": 15000.0,
    "internet_link_lease_month": 10000.0,
    "insurance_month": 10000.0,
    "advertising_month": 10000.0,
    "misc_admin_month": 50000.0,
    "staff_hours_per_week": 90.0,
    "staff_wage_per_hour": 40.0,
    # --- Appendix C: pricing and per-visit economics --------------------------------------------
    "computer_pay_share": 0.40,            # GIVEN -- share of customers who pay for computer time
    "computer_rate_per_hour": 120.0,
    "jtl_internet_cost_per_computer_hour": 60.0,
    "avg_hours_per_visit": 1.0,
    "avg_drink_revenue": 140.0,
    "avg_food_revenue": 60.0,
    "avg_drink_cost": 50.0,
    "avg_food_cost": 30.0,
    # --- Appendix E: market research scenarios (share of 20,000-person segment, visits/year) ----
    "segment_size": 20000.0,
    "optimistic_share": 0.50, "optimistic_visits_per_year": 5.0,
    "realistic_share": 0.40, "realistic_visits_per_year": 3.0,
    "pessimistic_share": 0.30, "pessimistic_visits_per_year": 2.0,
    # --- The Twist (FACILITATOR.md): post-broadband demand collapse -----------------------------
    "twist_collapse_fraction": 0.50,       # scenario dial for the twist, applied to pessimistic visits
}

FLEX = [
    "market_loan_rate_annual",   # Appendix F MA1 -- the case's one genuine, load-bearing assumption
    "weeks_per_month",           # Appendix F MA3 -- calendar-conversion convention
    "staff_hours_per_week",      # Appendix F MA4 -- total-hours vs. coverage-hours ambiguity
]


def _fixed_costs_month(p):
    staff_wage_month = p["staff_hours_per_week"] * p["staff_wage_per_hour"] * p["weeks_per_month"]
    return (p["manager_salary_month"] + p["lease_month"] + p["telephone_utilities_month"]
            + p["internet_link_lease_month"] + p["insurance_month"] + p["advertising_month"]
            + p["misc_admin_month"] + staff_wage_month)


def _contribution_margin_per_visit(p):
    fb = (p["avg_drink_revenue"] - p["avg_drink_cost"]) + (p["avg_food_revenue"] - p["avg_food_cost"])
    computer = p["computer_pay_share"] * (p["computer_rate_per_hour"]
                                           - p["jtl_internet_cost_per_computer_hour"]) * p["avg_hours_per_visit"]
    return fb + computer


def _psi(p):
    return (p["equipment_total_jad"] + p["upfront_legal_license_decor_jad"]
            + p["preopening_advertising_jad"] + p["utility_deposit_jad"])


def _interest_month_A(p):
    shortfall = _psi(p) - p["david_savings_jad"]
    return shortfall * p["market_loan_rate_annual"] / 12.0


def _interest_month_B(p):
    return p["jtl_loan_jad"] * p["jtl_loan_rate_annual"] / 12.0


def _cushion_A(p):
    """Total capital raised minus PSI -- Option A raises exactly its shortfall, by construction."""
    shortfall = _psi(p) - p["david_savings_jad"]
    raised = p["david_savings_jad"] + shortfall
    return raised - _psi(p)


def _cushion_B(p):
    raised = p["david_savings_jad"] + p["jtl_equity_jad"] + p["jtl_loan_jad"]
    return raised - _psi(p)


def _visits_per_month(p, share, visits_per_year):
    return p["segment_size"] * share * visits_per_year / 12.0


def _net_cash_flow_month(p, visits_per_month):
    contribution = visits_per_month * _contribution_margin_per_visit(p)
    fixed = _fixed_costs_month(p)
    return {
        "A": contribution - fixed - _interest_month_A(p),
        "B": contribution - fixed - _interest_month_B(p),
    }


def breakeven_visits(p):
    """Diagnostic (used by D4/D5), not the graded primary metric."""
    fixed = _fixed_costs_month(p)
    cm = _contribution_margin_per_visit(p)
    return {
        "A": (fixed + _interest_month_A(p)) / cm,
        "B": (fixed + _interest_month_B(p)) / cm,
    }


def evaluate(params):
    """Primary metric: expected monthly pre-tax operating cash flow (JA$) under the REALISTIC
    scenario. Higher is better."""
    p = dict(PARAMS); p.update(params or {})
    visits = _visits_per_month(p, p["realistic_share"], p["realistic_visits_per_year"])
    return _net_cash_flow_month(p, visits)


def david_personal_take_home(params=None):
    """NOT the graded primary metric (see module docstring / case.json.balance.margin_basis).
    Applies each option's stated ownership share (100% David under A, 50% David / 50% JTL under
    B, Appendix D) to the same realistic-scenario company cash flow evaluate() computes. Recorded
    here so this comparison is runnable, checkable, and never silently omitted -- found during
    Tier 2 P2 both-sides-solve, 2026-08-17."""
    cf = evaluate(params)
    p = dict(PARAMS); p.update(params or {})
    return {
        "A": cf["A"] * p.get("david_ownership_share_a", 1.0),
        "B": cf["B"] * p.get("david_ownership_share_b", 0.5),
    }


def evaluate_twist(params):
    """The Twist: a post-broadband demand collapse, modeled as a fraction of the PESSIMISTIC
    scenario's visit rate. Same metric (monthly net cash flow, JA$), applied to the collapsed
    scenario -- shows both options losing money, and (via _cushion_A/_cushion_B, reported
    alongside, not folded into this dict) that Option A has zero working-capital cushion to
    absorb it while Option B has a real one."""
    p = dict(PARAMS); p.update(params or {})
    pess_visits = _visits_per_month(p, p["pessimistic_share"], p["pessimistic_visits_per_year"])
    twist_visits = pess_visits * p["twist_collapse_fraction"]
    return _net_cash_flow_month(p, twist_visits)


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})
    be = breakeven_visits(PARAMS)
    dph = david_personal_take_home({})
    print("base cash flow (realistic)  ", {k: round(v, 2) for k, v in base.items()},
          "margin %.2f%%" % (100 * (base["B"] - base["A"]) / base["A"]))
    print("twist cash flow (collapsed)  ", {k: round(v, 2) for k, v in tw.items()})
    print("break-even visits/month      ", {k: round(v, 1) for k, v in be.items()},
          "A vs B gap %.2f%%" % (100 * (be["A"] - be["B"]) / be["B"]))
    print("cushion A/B (JA$)            ", round(_cushion_A(PARAMS), 2), round(_cushion_B(PARAMS), 2))
    print("David's personal take-home   ", {k: round(v, 2) for k, v in dph.items()},
          "-- A ahead of B by %.1f%% (NOT the graded metric; see module docstring)"
          % (100 * (dph["A"] - dph["B"]) / dph["B"]))
