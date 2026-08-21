#!/usr/bin/env python3
"""
SENSITIVITY MODEL — LeBron vs. Michael.

Tier 2 probe 5 ("flex each STATED ASSUMPTION by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. Contract:

    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            the subset that is an
                                                     author-chosen ASSUMPTION,
                                                     not cited/given data
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     same shape, with the twist (playoffs-only)
                                applied

primary_metric (case.json) is "career regular-season 3-point percentage",
graded balance.margin_basis: LeBron's real career-wide 3PT% (makes/attempts,
Appendix A) vs. Jordan's, per Modeling Assumption 1 ("career percentages are
makes over attempts, career-wide — not the average of each season's own
percentage"). The twist (FACILITATOR.md) swaps in the same computation over
Appendix B's playoff makes/attempts.

FLEX IS DELIBERATELY EMPTY. Every PARAM below is a real, cited, publicly
verifiable box-score total (sources[] S1-S3, cross-checked against
Basketball-Reference / StatMuse, corrected 2026-08-04 — see
case.json.correction_2026_08_04) — not an author-chosen convention with a
range of defensible values. Modeling Assumption 1 itself (career-wide vs.
season-average) is a binary methodological choice the case already commits to
and is the actual subject of D1's forcing question, not a continuous dial;
there is nothing to move it "+/-50%" toward. Per the case-readiness doctrine
("Only FLEX[] is swept by default... cited data is stress-tested by P6
instead"), flexing these make/attempt totals would be testing the accuracy of
the box scores, not the case's assumption -- that is what P6 (data decay) is
for, not P5. This is itself the honest P5 finding for this case: the graded
metric rests entirely on cited data with no author-chosen assumption dial to
stress-test.

Verified against cases/lebron-vs-michael/case.json (derived{} / balance{}):
    base   A = 34.49  ·  B = 32.68  ·  margin  5.54%   (matches case.json margin_pct)
    twist  A = 33.88  ·  B = 33.78                     (matches FACILITATOR.md twist section:
                                                         "LeBron leads it both before ... and after")
"""

PARAMS = {
    # --- Appendix A: career regular-season 3-point makes/attempts, real totals ---
    "lebron_3pt_made": 1979,
    "lebron_3pt_att": 5738,
    "jordan_3pt_made": 581,
    "jordan_3pt_att": 1778,
    # --- Appendix B: career playoff 3-point makes/attempts (Twist), real/reconstructed
    #     per Modeling Assumption 4 -- reconstructed from real per-game-by-season
    #     averages x that season's real games played, summed, rounded ---
    "lebron_po_3pt_made": 435,
    "lebron_po_3pt_att": 1284,
    "jordan_po_3pt_made": 150,
    "jordan_po_3pt_att": 444,
}

# See docstring: no PARAM here is an author-chosen assumption with a defensible
# range of values -- every one is a cited/reconstructed real statistic. FLEX is
# empty on purpose; P5 correctly sweeps 0 dials for this case.
FLEX = []


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    a = 100.0 * p["lebron_3pt_made"] / p["lebron_3pt_att"]
    b = 100.0 * p["jordan_3pt_made"] / p["jordan_3pt_att"]
    return {"A": a, "B": b}


def evaluate_twist(params):
    p = dict(PARAMS)
    p.update(params or {})
    a = 100.0 * p["lebron_po_3pt_made"] / p["lebron_po_3pt_att"]
    b = 100.0 * p["jordan_po_3pt_made"] / p["jordan_po_3pt_att"]
    return {"A": a, "B": b}


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})
    print("base ", {k: round(v, 2) for k, v in base.items()},
          "margin %.2f%%" % (100 * (base["A"] - base["B"]) / base["B"]))
    print("twist", {k: round(v, 2) for k, v in tw.items()})
