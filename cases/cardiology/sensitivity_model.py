#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Cardiology.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic.

CONTRACT — exactly two-plus public names (see
skills/case-readiness/scripts/example_sensitivity_model.py for the worked
reference, Cold Chain):

    PARAMS                     dict[str, number]   every dial the case STATES
    FLEX                       list[str]            the subset that is a genuine
                                                      author-chosen ASSUMPTION
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     optional; same shape, with the twist applied

Case's own graded primary_metric (case.json) is "5-year survival rate (%), in
percentage points -- the real, close number the STICH trial's own primary 2011
report gives." A = MT, B = CABG. Higher survival is better.

WHAT IS CITED vs WHAT IS FLEX -- this is the load-bearing modeling call for
this case:

  - The mortality/survival percentages (5-year AND 10-year) are the real STICH
    trial's own published results (case.json sources S1/S2, Velazquez et al.
    NEJM 2011 and 2016). They are CITED DATA, not an author assumption -- the
    case did not choose them, the trial did. Per SKILL.md P5's own rule
    ("Only FLEX[] is swept... halving a WHO-rated cold life is a different
    case, not a sensitivity test"), these do NOT belong in FLEX. P6 (data
    decay) is what stress-tests cited figures, not P5.
  - Appendix C's cost figures (MT $450/mo; CABG one-time $85,000 + $150/mo
    follow-up) are explicitly and repeatedly flagged in case.md and case.json
    as "a disclosed, stated modeling convention, not sourced from the trial."
    That is exactly the SPEC §2 "genuine author-chosen assumption" P5 exists
    to flex. They go in FLEX.

The consequence, and the actual P5 finding: the case's own margin_basis
(case.json balance.margin_basis) states plainly that the graded primary
metric is the survival-rate gap, and that the $67,000 cost gap, while real
and central to D3/D4, "is not the graded primary metric." Because evaluate()
below reproduces exactly that graded metric (survival rate only), flexing the
only real FLEX[] params (the cost dials) by construction cannot move A or B
at all -- they are not inputs to the win/loss computation. See QA_REPORT.md
for how this is reported: not a script bug, a fact about the case's own
declared scoring rule.

Verified against cases/cardiology/case.md and case.json derived{}:
    base (5yr)  A(MT)=59.0  B(CABG)=64.0   margin 5.0 points   (matches case.json)
    twist(10yr) A(MT)=33.9  B(CABG)=41.1   margin 7.2 points   (matches FACILITATOR.md)
"""

PARAMS = {
    # --- Appendix A / case.json sources S1 -- CITED, real STICH trial data --
    "mt_5yr_mortality_pct": 41.0,
    "cabg_5yr_mortality_pct": 36.0,
    # --- Appendix A / case.json sources S2 -- CITED, real STICHES extension -
    "mt_10yr_mortality_pct": 66.1,
    "cabg_10yr_mortality_pct": 58.9,
    # --- Appendix C / Assumption 2 -- DISCLOSED MODELING CONVENTION ---------
    "mt_monthly_cost": 450.0,
    "cabg_surgery_cost": 85000.0,
    "cabg_monthly_followup": 150.0,
}

# Only the disclosed cost convention is a genuine author-chosen assumption.
# The mortality/survival figures are real cited trial data (P6's job, not P5's)
# -- see the docstring above for why they are deliberately excluded here.
FLEX = [
    "mt_monthly_cost",          # Appendix C / Assumption 2
    "cabg_surgery_cost",        # Appendix C / Assumption 2
    "cabg_monthly_followup",    # Appendix C / Assumption 2
]


def _survival(mortality_pct):
    return 100.0 - mortality_pct


def evaluate(params):
    """Graded primary metric: 5-year survival rate (%). Higher is better."""
    p = dict(PARAMS)
    p.update(params or {})
    a = _survival(p["mt_5yr_mortality_pct"])
    b = _survival(p["cabg_5yr_mortality_pct"])
    return {"A": a, "B": b}


def evaluate_twist(params):
    """The twist: the real 10-year STICHES extension data (FACILITATOR.md)."""
    p = dict(PARAMS)
    p.update(params or {})
    a = _survival(p["mt_10yr_mortality_pct"])
    b = _survival(p["cabg_10yr_mortality_pct"])
    return {"A": a, "B": b}


def cost_5yr(params):
    """Not part of the graded win/loss metric -- disclosed context only
    (D3/D4, and the qualitative balance.argument_a/argument_b text). Exposed
    here for completeness/debugging, not swept by evaluate()."""
    p = dict(PARAMS)
    p.update(params or {})
    mt = p["mt_monthly_cost"] * 12 * 5
    cabg = p["cabg_surgery_cost"] + p["cabg_monthly_followup"] * 12 * 5
    return {"A": mt, "B": cabg}


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})
    cost = cost_5yr({})
    print("base (5yr) ", {k: round(v, 1) for k, v in base.items()},
          "margin %.1f pts" % (base["B"] - base["A"]))
    print("twist(10yr)", {k: round(v, 1) for k, v in tw.items()},
          "margin %.1f pts" % (tw["B"] - tw["A"]))
    print("cost (5yr, context only)", {k: round(v) for k, v in cost.items()})
