#!/usr/bin/env python3
"""
Sensitivity model -- The Contrapositive Claim.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips
the verdict"). See skills/case-readiness/scripts/example_sensitivity_model.py.

Primary metric: wrongly-denied claims caught per 100 appeals reviewed, under
each candidate audit standard, computed from Appendix E's 14-row constructed
log (Modeling Assumption MA2):
  - both_catch: rows where a diligent reviewer applying either standard's
    own definition of "flood" catches the misapplication on its face.
  - mirror_only_catch: rows where only the Mirror-Image Standard's explicit
    non-flood-cause check catches an adjuster who reasoned from the
    clause's converse rather than its contrapositive.
  - neither_catch: rows genuinely ambiguous at review time (the twist, row
    14) -- no standard catches these; also includes correctly-denied rows
    (ground truth = flood) which count as 0 catches under both standards.

evaluate() returns each option's catch rate per 100 appeals directly
(higher = better = more wrongly-denied claims caught), matching case.json's
own primary_metric framing.

This model exposes the counts (not a continuous dial) as the swept
"assumption" -- Appendix E's own row classification IS Modeling Assumption
MA2, so FLEX sweeps the row COUNTS by +/-50%, holding the total log size
fixed at 14 (the same scoping the case's own retune history used).
"""

PARAMS = {
    "total_rows": 14.0,
    "both_catch_rows": 6.0,        # rows 3,5,7,9,11,13
    "mirror_only_catch_rows": 1.0,  # row 1
    # correctly-denied + genuinely-ambiguous rows (neither standard catches)
    # = total - both_catch - mirror_only_catch = 14 - 6 - 1 = 7
    # (6 correctly-denied rows 2,4,6,8,10,12 + 1 ambiguous row 14)
}

# Probe 5 flexes the two row-count dials that make up MA2's classification
# (both_catch_rows, mirror_only_catch_rows). total_rows is held fixed at 14
# (the log's own scale, MA2's own stated constant) since flexing it alone
# with no re-classification is not a meaningful sweep of this case's math.
FLEX = [
    "both_catch_rows",
    "mirror_only_catch_rows",
]


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})

    plain_text_catches = p["both_catch_rows"]
    mirror_image_catches = p["both_catch_rows"] + p["mirror_only_catch_rows"]

    rate_a = 100.0 * plain_text_catches / p["total_rows"]
    rate_b = 100.0 * mirror_image_catches / p["total_rows"]

    return {"A": rate_a, "B": rate_b}


if __name__ == '__main__':
    base = evaluate({})
    margin = 100 * (base["B"] - base["A"]) / base["A"]
    print("base  A(Plain-Text)=%.1f/100  B(Mirror-Image)=%.1f/100" % (base["A"], base["B"]),
          "margin %.2f%%" % margin, "-- matches case.json.margin_pct (16.7)")

    for factor, label in ((0.5, "-50%"), (1.5, "+50%")):
        flexed = evaluate({"mirror_only_catch_rows": PARAMS["mirror_only_catch_rows"] * factor})
        m = 100 * (flexed["B"] - flexed["A"]) / flexed["A"]
        print(f"mirror_only_catch_rows {label}", "A=%.1f B=%.1f" % (flexed["A"], flexed["B"]),
              "margin %.2f%%" % m, "winner:", "B" if flexed["B"] > flexed["A"] else "A")

        flexed2 = evaluate({"both_catch_rows": PARAMS["both_catch_rows"] * factor})
        m2 = 100 * (flexed2["B"] - flexed2["A"]) / flexed2["A"]
        print(f"both_catch_rows {label}", "A=%.1f B=%.1f" % (flexed2["A"], flexed2["B"]),
              "margin %.2f%%" % m2, "winner:", "B" if flexed2["B"] > flexed2["A"] else "A")
