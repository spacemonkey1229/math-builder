#!/usr/bin/env python3
"""
Sensitivity model -- Perimeter Protocol.

Tier 2 probe 5 flexes each stated assumption by +/-50% and reports which flips
the verdict. Contract: PARAMS, FLEX, evaluate(params) -> {"A": metric, "B": metric}.
See skills/case-readiness/scripts/example_sensitivity_model.py for the worked
reference this file follows.

Per case.json's primary_metric / balance.margin_basis, the graded metric is
true-threats-blocked-per-false-positive for each rule set. Higher is better.

The Traffic Sample (Appendix C, Modeling Assumption MA2) is modeled here as
eight category counts -- one true-threat count and one false-count for each of
the four (p, q) truth combinations -- instead of as four raw totals, because
the raw totals are NOT independent: Rule Set A (p OR q) structurally blocks a
SUPERSET of what Rule Set B (p AND q) blocks. Modeling by category makes that
containment automatic under any flex, exactly like the real rule sets:
    Rule A blocks: (p&q) + (p&~q) + (~p&q)   categories
    Rule B blocks: (p&q)                      category only
so ttA >= ttB and fpA >= fpB always hold, for any nonnegative category counts.

Base counts read off Table C-1 (case.md Appendix C):
    p&q    (rows 1-6):   4 true threats, 2 false
    p&~q   (rows 7-11):  3 true threats, 2 false
    ~p&q   (rows 12-16): 3 true threats, 2 false
    ~p&~q  (rows 17-20): 1 true threat,  3 false  (neither rule ever blocks this
                                                     category -- included for
                                                     completeness, not used below)

Verified against case.json.balance / FACILITATOR.md's arithmetic note:
    base  A = 10/6 = 1.6667  ·  B = 4/2 = 2.0  ·  margin (2.0-1.6667)/2.0 = 16.7%
    (matches case.json margin_pct 16.7)

MA1 (the 20-analyst-hour weekend pool) and MA3 (15 minutes/false-positive) are
both stated, sensitive assumptions, but neither one enters the primary metric
at all -- they only govern whether each rule set's total triage time fits the
fixed pool (D5's capacity-fit check), which this case's `balance.margin_basis`
does not use as the graded comparison. They are included in PARAMS/FLEX for
completeness and capacity_fit(), but flexing them alone cannot move the
primary-metric winner -- that is a real, disclosable finding, not a bug in
this model.
"""

PARAMS = {
    # --- Modeling Assumption MA2 (Traffic Sample, Appendix C / Table C-1) ---
    # p AND q category (rows 1-6)
    "n_pq_true": 4.0,
    "n_pq_false": 2.0,
    # p AND NOT q category (rows 7-11)
    "n_p_notq_true": 3.0,
    "n_p_notq_false": 2.0,
    # NOT p AND q category (rows 12-16)
    "n_notp_q_true": 3.0,
    "n_notp_q_false": 2.0,
    # --- Modeling Assumption MA1: weekend analyst-hour pool ---
    "pool_minutes": 1200.0,   # 20 hours x 60
    # --- Modeling Assumption MA3: minutes to triage one false positive ---
    "min_per_fp": 15.0,
}

# All three sensitive Modeling Assumptions (MA1, MA2 as its six category
# counts, MA3) are in FLEX -- MA2's counts are what SPEC S2 means by "the
# assumption this case had to choose": no public per-hospital firewall log
# exists, so the mix of watchlist-only/unpatched-only/both/neither traffic and
# how much of each is a genuine threat was hand-built, exactly like grant-reach's
# 9,000-student population. pell_share-style CITED data does not appear in this
# case -- every number in Appendix C is the stated assumption itself, not a
# citation P6 should stress-test instead.
FLEX = [
    "n_pq_true", "n_pq_false",
    "n_p_notq_true", "n_p_notq_false",
    "n_notp_q_true", "n_notp_q_false",
    "pool_minutes",
    "min_per_fp",
]


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})

    tt_a = p["n_pq_true"] + p["n_p_notq_true"] + p["n_notp_q_true"]
    fp_a = p["n_pq_false"] + p["n_p_notq_false"] + p["n_notp_q_false"]
    tt_b = p["n_pq_true"]
    fp_b = p["n_pq_false"]

    ratio_a = tt_a / fp_a if fp_a else float("inf")
    ratio_b = tt_b / fp_b if fp_b else float("inf")
    return {"A": ratio_a, "B": ratio_b}


def evaluate_twist(params):
    """The twist: Rule Set A's raw threats-blocked count is guaranteed >= Rule
    Set B's by the OR/AND containment, for ANY nonnegative category counts --
    it is a fact of the logic, not something the Traffic Sample could ever
    overturn. Returns the raw counts so the containment can be checked
    directly, alongside the same ratio metric evaluate() returns."""
    p = dict(PARAMS)
    p.update(params or {})

    tt_a = p["n_pq_true"] + p["n_p_notq_true"] + p["n_notp_q_true"]
    fp_a = p["n_pq_false"] + p["n_p_notq_false"] + p["n_notp_q_false"]
    tt_b = p["n_pq_true"]
    fp_b = p["n_pq_false"]

    out = evaluate(params)
    out["raw_containment_holds"] = (tt_a >= tt_b) and (fp_a >= fp_b)
    out["tt_a"], out["fp_a"], out["tt_b"], out["fp_b"] = tt_a, fp_a, tt_b, fp_b
    return out


def capacity_fit(params):
    """Not part of the P5 metric contract -- a secondary check for D5's
    'does this fit the fixed 20-hour pool' question, driven by MA1/MA3."""
    p = dict(PARAMS)
    p.update(params or {})
    fp_a = p["n_pq_false"] + p["n_p_notq_false"] + p["n_notp_q_false"]
    fp_b = p["n_pq_false"]
    minutes_a = fp_a * p["min_per_fp"]
    minutes_b = fp_b * p["min_per_fp"]
    return {
        "minutes_a": minutes_a, "minutes_b": minutes_b,
        "fits_a": minutes_a <= p["pool_minutes"],
        "fits_b": minutes_b <= p["pool_minutes"],
    }


if __name__ == '__main__':
    base = evaluate({})
    lo = min(base, key=base.get)
    hi = max(base, key=base.get)
    margin = 100 * (base[hi] - base[lo]) / base[hi] if base[hi] else float("nan")
    print("base ", {k: round(v, 4) for k, v in base.items()}, "margin %.2f%%" % margin)
    print("twist", evaluate_twist({}))
    print("capacity", capacity_fit({}))
