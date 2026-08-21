#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- Acton Survey.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. This is that
model, for cases/acton-survey.

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):

    PARAMS                             dict[str, number]  every dial the case states
    FLEX                               list[str]          subset of PARAMS probe 5 flexes
    evaluate(params) -> dict           {"A": metric, "B": metric}
    evaluate_twist(params) -> dict     same shape, with the twist's own lens applied

IMPORTANT -- metric direction: this case's primary metric is a TIME COST in
hours, so LOWER is better here (like Family Trip's cost metric, unlike Cold
Chain's in-spec-dose count where higher is better). Callers comparing A vs B
for "the winner" should take the smaller value.

evaluate() returns the case's graded PRIMARY metric: total call time in hours
(case.json.primary_metric). Option B always reaches all 50 real campuses
(stratified, by construction). Option A reaches an EXPECTED number of
campuses, computed exactly via the hypergeometric distribution (Appendix C)
over the real 50-campus size list (Appendix B) -- not an estimate.

Verified against case.md / case.json:
    evaluate({})  A = 51.23 h   B = 53.92 h   margin (B-A)/A = 5.25% -> A cheaper (fewer hours)
    matches case.json.balance (A=51.23, B=53.92, margin_pct=5.3)

evaluate_twist() models the Guide Notes twist: guide-coordination calls run
at the TOP of the case's own stated 15-20 minute bracket (Appendix A) --
20 min instead of MA1's chosen low end of 15 -- because "every guide wants
to talk shop before they hand the phone over." This stays inside the case's
own declared 15-20-minute-per-call fact (Appendix A / Background) rather than
contradicting it; the twist only changes WHICH point in that already-stated
range MA1 uses, the same kind of move MA1 itself makes. It does not change
which figures are real (Appendix B's campus sizes are unchanged); it only
raises the coordination_call_min PARAM from 15 to 20.
"""

from math import comb

# Real, complete 2021 campus-size list (case.md Appendix B) -- 50 campuses,
# 1,420 learners. This is CITED DATA (S1), not an assumption -- it is never
# flexed by probe 5. Only the case's own STATED assumptions (MA1, MA2) are
# in FLEX, per the "Only FLEX[] is swept" rule (skills/case-readiness/SKILL.md).
CAMPUS_SIZES = (
    [168, 168, 168, 108] +
    [60, 60, 60, 60] +
    [28] +
    [24, 24, 24, 24] +
    [12] * 37
)
TOTAL_POPULATION = sum(CAMPUS_SIZES)  # 1420
assert TOTAL_POPULATION == 1420
assert len(CAMPUS_SIZES) == 50

PARAMS = {
    # --- Background / Appendix A: Jeff & Xander's stated target -------------
    "sample_fraction": 0.10,             # -> n = round(0.10 * 1420) = 142
    # --- Appendix D, MA2: chosen point within the real 15-20 min range ------
    "learner_call_min": 17.5,
    # --- Appendix D, MA1: stated modeling assumption, no public figure ------
    "coordination_call_min": 15.0,
}

# Probe 5 flexes THESE and only these -- the case's own STATED assumptions
# (Appendix E: MA1, MA2), not the real, complete campus roster (S1, cited
# data, CAMPUS_SIZES above -- stress-tested by P6 instead, not P5).
# sample_fraction is included because "interview 10% of the population" is
# itself a scenario decision Jeff and Xander made, not an external citation.
FLEX = [
    "coordination_call_min",   # Appendix E, MA1
    "learner_call_min",        # Appendix E, MA2
    "sample_fraction",         # Background -- Jeff & Xander's stated target
]


def _sample_size(p):
    return round(p["sample_fraction"] * TOTAL_POPULATION)


def _expected_campuses_reached(n):
    """Exact hypergeometric expectation: 50 - sum_i P(zero from campus i)."""
    N = TOTAL_POPULATION
    if n <= 0:
        return 0.0
    if n >= N:
        return float(len(CAMPUS_SIZES))
    expected_shutout = 0.0
    for Ni in CAMPUS_SIZES:
        if N - Ni < n:
            p_zero = 0.0  # can't avoid drawing from this campus at all
        else:
            p_zero = comb(N - Ni, n) / comb(N, n)
        expected_shutout += p_zero
    return len(CAMPUS_SIZES) - expected_shutout


def _hours(n, campuses_reached, p):
    learner_minutes = n * p["learner_call_min"]
    coordination_minutes = campuses_reached * p["coordination_call_min"]
    return (learner_minutes + coordination_minutes) / 60.0


def evaluate(params=None):
    """Primary graded metric: total call-time hours (lower is better)."""
    p = dict(PARAMS)
    p.update(params or {})
    n = _sample_size(p)
    reached_a = _expected_campuses_reached(n)
    reached_b = len(CAMPUS_SIZES)  # stratified always reaches all 50, by construction
    return {
        "A": _hours(n, reached_a, p),
        "B": _hours(n, reached_b, p),
    }


def evaluate_twist(params=None):
    """Guide Notes twist: coordination calls run at the TOP of the case's own
    stated 15-20 minute bracket (20 min), not a fabricated value outside it."""
    p = dict(PARAMS)
    p.update(params or {})
    p["coordination_call_min"] = 20.0
    return evaluate(p)


if __name__ == "__main__":
    base = evaluate({})
    tw = evaluate_twist({})
    base_margin = 100 * (base["B"] - base["A"]) / base["A"]
    tw_margin = 100 * (tw["B"] - tw["A"]) / tw["A"]
    n = _sample_size(PARAMS)
    reached_a = _expected_campuses_reached(n)
    print("sample size n = %d, expected campuses reached under A = %.3f of %d (%.1f%% shutout)" %
          (n, reached_a, len(CAMPUS_SIZES), 100 * (len(CAMPUS_SIZES) - reached_a) / len(CAMPUS_SIZES)))
    print("base            A=%.2fh  B=%.2fh  (B-A)/A=%.2f%%  -> %s wins (fewer hours)" %
          (base["A"], base["B"], base_margin, "A" if base["A"] < base["B"] else "B"))
    print("twist (20min coord) A=%.2fh  B=%.2fh  (B-A)/A=%.2f%%  -> %s wins (fewer hours)" %
          (tw["A"], tw["B"], tw_margin, "A" if tw["A"] < tw["B"] else "B"))
