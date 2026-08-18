#!/usr/bin/env python3
"""
SENSITIVITY MODEL — College Admissions.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the reference
shape this file follows.

CONTRACT:
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            subset of PARAMS Tier 2 flexes
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher = stronger applicant
    evaluate_twist(params)     same shape, with D5's school-size-normalized headcount

`evaluate()` models the case's actual GRADED primary_metric (case.json
`primary_metric` / `balance.margin_pct` = 2.7%): each applicant's SAT
Composite score, given verbatim in their own application file (Appendix C/D).
Both scores are cited application data, not a stated assumption -- per
skills/case-readiness/SKILL.md's P5 doctrine ("sensitivity to stated
assumptions, not to cited measurements"), neither belongs in FLEX. This
metric is stable by construction: there is no assumption anywhere in its
computation to perturb.

`evaluate_twist()` models D5's disclosed secondary comparison -- each
applicant's stated class-rank percentile converted into a raw headcount of
classmates who rank above them, using their high school's enrollment. Tisha's
enrollment is given directly in her application (3,200). Harrison's is NOT
given -- his application states only "Public" with no size -- so this case
substitutes a real, sourced national-average public-high-school enrollment
(case.json MA2, Appendix B, ~649 students) as a genuine stated assumption.
THAT substitution is the one real dial probe 5 flexes.

Verified against case.json.derived:
    base   A = tisha_sat_composite    = 1480
           B = harrison_sat_composite = 1520
           margin = 100*(B-A)/A = 2.7%   (matches derived.sat_gap_pct_of_lower_score)
    twist  tisha_est_students_ranked_above    = 96   (0.03 * 3200)
           harrison_est_students_ranked_above = 45   (0.07 * 649, national-avg assumption)
"""

PARAMS = {
    # --- Appendix C/D: each applicant's own stated SAT Composite score ------
    #     cited application data, not a stated assumption -- never flexed.
    "tisha_sat_composite": 1480,
    "harrison_sat_composite": 1520,

    # --- Appendix C: Tisha's stated class-rank percentile and her school's
    #     stated enrollment (given directly in her application) --------------
    "tisha_class_rank_pct": 0.03,
    "tisha_hs_enrollment": 3200,

    # --- Appendix D: Harrison's stated class-rank percentile (given) --------
    "harrison_class_rank_pct": 0.07,
    # --- ASSUMPTION (case.json MA2). Harrison's application does not state
    #     his high school's enrollment. This case substitutes the U.S.
    #     national average public high school enrollment (Appendix B,
    #     ~649 students, sourced from NCES-derived figures S5/S6) as a
    #     genuine, disclosed stand-in -- NOT a claimed fact about Harrison's
    #     actual school. This is the one real dial probe 5 exists to flex.
    "harrison_hs_enrollment_assumed": 649,
}

# Probe 5 flexes THIS and only this. tisha_sat_composite/harrison_sat_composite
# are each applicant's own stated application data (cited, fixed -- stress-
# tested by probe 6's source-decay check, not probe 5's assumption-flex).
# tisha_class_rank_pct/harrison_class_rank_pct and tisha_hs_enrollment are
# likewise given, stated figures from each application, not assumptions.
# harrison_hs_enrollment_assumed is the case's one genuine unstated-and-
# substituted number (case.json MA2) -- the honest sensitivity dial.
FLEX = [
    "harrison_hs_enrollment_assumed",
]


def evaluate(params, detour_h=0.0):
    """The case's actual graded primary_metric: SAT Composite score, Tisha
    (A) vs Harrison (B) -- case.json `primary_metric` / `balance.margin_pct`
    = 2.7%, `derived.sat_gap_pct_of_lower_score`. Stable by construction:
    both inputs are cited application data, not a flexible assumption."""
    p = dict(PARAMS)
    p.update(params or {})
    return {"A": p["tisha_sat_composite"], "B": p["harrison_sat_composite"]}


def evaluate_twist(params):
    """NOT the graded primary_metric. D5's disclosed secondary comparison:
    for each applicant, the number of classmates who do NOT rank above them
    (school size minus the estimated headcount ranked above) -- higher is a
    stronger showing. Harrison's school size is a stated assumption
    (harrison_hs_enrollment_assumed); Tisha's is given."""
    p = dict(PARAMS)
    p.update(params or {})
    tisha_above = p["tisha_class_rank_pct"] * p["tisha_hs_enrollment"]
    harrison_above = p["harrison_class_rank_pct"] * p["harrison_hs_enrollment_assumed"]
    tisha_below = p["tisha_hs_enrollment"] - tisha_above
    harrison_below = p["harrison_hs_enrollment_assumed"] - harrison_above
    return {"A": tisha_below, "B": harrison_below,
            "tisha_students_above": tisha_above,
            "harrison_students_above": harrison_above}


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})
    margin = 100 * (base["B"] - base["A"]) / base["A"]
    print("base (graded primary_metric)", base, "  margin = %.1f%% of A" % margin)
    print("twist (D5 disclosed headcount comparison; NOT the graded metric)",
          {k: round(v, 2) for k, v in tw.items()})

    print("\nProbe 5 flex sweep on harrison_hs_enrollment_assumed (base 649):")
    for pct in (-0.5, -0.25, 0.0, 0.25, 0.5):
        flexed = 649 * (1 + pct)
        r = evaluate_twist({"harrison_hs_enrollment_assumed": flexed})
        print("  flex %+.0f%%  enrollment=%.1f  tisha_above=%.1f  harrison_above=%.1f  "
              "%s has fewer students above them"
              % (pct * 100, flexed, r["tisha_students_above"], r["harrison_students_above"],
                 "Tisha" if r["tisha_students_above"] < r["harrison_students_above"] else "Harrison"))
