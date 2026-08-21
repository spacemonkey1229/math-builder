#!/usr/bin/env python3
"""
Sensitivity model — The Reserve Asymptote.

Tier 2 probe 5 flexes each stated assumption by +/-50% and reports which flips
the verdict. Contract: PARAMS, evaluate(params) -> {"A": metric, "B": metric}.
See skills/case-readiness/scripts/example_sensitivity_model.py for the worked
reference this file follows.

This case's dilemma is not "which number is bigger" -- it is which filed
methodology is defensible. The metric returned here is the blended dollars of
reserve required per $1,000 of face value, negated (so a smaller/cheaper
reserve reads as a "higher" metric, keeping this file's evaluate() consistent
with the project's higher-is-better convention). The case's actual argument
for the Full Table is *not* that it produces a bigger blended number -- it's
that the Smooth Curve's blended number understates the true single-cohort
exposure. Probe 5 measures whether the aggregate comparison (which option is
cheaper in blended terms) is stable under flex, and separately reports the
single-cohort gap so a human adjudicator can see both.

Verified against case.json.balance.computed_values:
    base  A (Smooth Curve)= $208.36/1000 face  ·  B (Full Table) = $210.41/1000 face
    blended margin ~0.97%; age-100 single-cohort gap = $652.73/1000 face (188%)
"""

# --- Appendix C: the Full Table's real, published qx values, ages 90-99, and
# the "100 and over" closure convention (qx = 1). This is CITED data (Appendix
# C / source S1), not a stated assumption -- it is NOT flexed here (P6 data
# decay stress-tests cited sources instead; see "Only FLEX[] is swept" rule).
FULL_TABLE_QX = {
    90: 0.148104, 91: 0.164457, 92: 0.181983, 93: 0.200630, 94: 0.220320,
    95: 0.240942, 96: 0.262361, 97: 0.284411, 98: 0.306908, 99: 0.329650,
    100: 1.000000,   # "100 and over" open-group closure
}

# --- Appendix D: contract counts by attained age, EXCEPT the age-100-and-over
# cohort, which is exposed as a flexible PARAM below (MA2's own sensitivity
# note calls out exactly this cohort's relative size as the load-bearing dial).
OTHER_AGE_CONTRACTS = {
    90: 112, 91: 95, 92: 80, 93: 65, 94: 52,
    95: 41, 96: 31, 97: 23, 98: 16, 99: 11,
}

PARAMS = {
    # --- Appendix F, MA1: the Smooth Curve's calibrated formula parameters
    #     C_A(x) = 1000 - k * b^(x-90)
    "k": 851.8963,
    "b": 0.973722,
    # --- Appendix F, MA2: size of the age-100-and-over cohort in Highline's
    #     in-force block -- the single most sensitive dial per the case's own
    #     stated sensitivity note.
    "age100_contracts": 8.0,
}

FLEX = [
    "k", "b",                 # MA1 -- the Smooth Curve's own calibration
    "age100_contracts",       # MA2 -- the boundary cohort's size
]


def _C_A(x, k, b):
    """Smooth Curve: dollars of reserve per $1,000 face at attained age x."""
    return 1000.0 - k * (b ** (x - 90))


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    k, b = p["k"], p["b"]
    age100 = max(0.0, p["age100_contracts"])

    total_contracts = sum(OTHER_AGE_CONTRACTS.values()) + age100
    reserve_a = 0.0
    reserve_b = 0.0
    for age, n in OTHER_AGE_CONTRACTS.items():
        reserve_a += n * _C_A(age, k, b)
        reserve_b += n * (1000.0 * FULL_TABLE_QX[age])
    reserve_a += age100 * _C_A(100, k, b)
    reserve_b += age100 * (1000.0 * FULL_TABLE_QX[100])

    blended_a = reserve_a / total_contracts if total_contracts else float("-inf")
    blended_b = reserve_b / total_contracts if total_contracts else float("-inf")

    # Higher-is-better convention: negate the blended cost so "A wins" means
    # "A is the cheaper blended methodology," matching how this project's
    # other sensitivity models report a winner.
    return {"A": -blended_a, "B": -blended_b}


def single_cohort_gap(params):
    """Non-metric diagnostic: the age-100 dollar gap and relative %, for a
    human adjudicator comparing against the aggregate-margin verdict above."""
    p = dict(PARAMS)
    p.update(params or {})
    k, b = p["k"], p["b"]
    ca100 = _C_A(100, k, b)
    cb100 = 1000.0 * FULL_TABLE_QX[100]
    gap = cb100 - ca100
    rel_pct = 100.0 * gap / ca100 if ca100 else float("inf")
    return {"C_A_100": ca100, "C_B_100": cb100, "gap": gap, "relative_pct": rel_pct}


if __name__ == '__main__':
    base = evaluate({})
    blended_a, blended_b = -base["A"], -base["B"]
    margin = 100 * abs(blended_a - blended_b) / min(blended_a, blended_b)
    print("base blended  A=$%.2f  B=$%.2f  margin %.2f%%" % (blended_a, blended_b, margin))
    print("single-cohort ", single_cohort_gap({}))
