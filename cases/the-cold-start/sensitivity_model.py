#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- The Cold Start.

Tier 2 probe 5 ("flex each stated assumption by +-50%; report which flips
the verdict") needs a runnable model of the case's own arithmetic.

CONTRACT -- two public names:

    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

The case's SPEC Section 2 primary metric (case.json.balance.margin_basis) is
recommendations clicked (specifically, on the premiere, "Halfmoon Bay") per
100 accounts that STARTED signup -- not per account that finished it. Higher
is better for both options, so evaluate() needs no negation (contrast with
the-mainline-margin's cost metric, which does).

Mechanism modeled explicitly (this is the whole point of the case):
Option A (Popularity Path) has zero onboarding friction -- all 100 starters
reach a recommendation shelf -- but the premiere has zero data in the
item-similarity matrix on day one, so only a modeled fraction of reachers
ever click it (ctr_a). Option B (Ratings Gate) requires 10 ratings before
any shelf appears; a modeled fraction of starters abandon that gate
(dropout_b) before ever seeing ANY recommendation, but those who complete it
get real personalization signal, converting at a modeled, much higher rate
(ctr_b_completer).

clicks_per_100(A) = 100 * ctr_a
clicks_per_100(B) = 100 * (1 - dropout_b) * ctr_b_completer

FLEX[] sweeps the case's own three stated Modeling Assumptions that feed
this metric's arithmetic: MA2 (ctr_a), MA3 (dropout_b), MA4
(ctr_b_completer). MA1 (days to launch review) and MA5 (Appendix E's
worked-example matrices) are not swept -- neither feeds the primary metric
at all; both are flagged "None -- flavor/pedagogical only" in
case.json.modeling_assumptions[].
"""

PARAMS = {
    # --- Appendix B / MA2: click-through rate, Option A, among all reachers
    "ctr_a": 0.20,
    # --- Appendix C / MA3: modeled 2026 dropout during the Ratings Gate ----
    "dropout_b": 0.40,
    # --- Appendix C / MA4: click-through rate, Option B, among completers -
    "ctr_b_completer": 0.35,
    # --- Fixed case parameter -------------------------------------------------
    "cohort": 100.0,
}

# Probe 5 flexes THESE and only these: the case's own stated Modeling
# Assumptions that feed the graded primary metric's arithmetic.
FLEX = [
    "ctr_a",             # MA2, Appendix B -- the case's most narratively-invented number
    "dropout_b",         # MA3, Appendix C -- the case's real fulcrum
    "ctr_b_completer",   # MA4, Appendix C
]

# S2's real, measured historical dropout (Rashid et al. 2002, live MovieLens
# experiment: 49/351 = 13.96%) -- NOT the modeled value (dropout_b above),
# kept here only so the counterfactual in case.json's balance.margin_note is
# reproducible from this file.
REAL_HISTORICAL_DROPOUT_S2 = 49.0 / 351.0


def evaluate_detail(params):
    p = dict(PARAMS)
    p.update(params or {})
    cohort = p["cohort"]

    clicks_a = cohort * p["ctr_a"]

    completers_b = cohort * (1.0 - p["dropout_b"])
    clicks_b = completers_b * p["ctr_b_completer"]

    detail_a = {"clicks_per_100": clicks_a}
    detail_b = {
        "completers_per_100": completers_b,
        "clicks_per_100": clicks_b,
    }
    return {"A": clicks_a, "B": clicks_b}, detail_a, detail_b


def evaluate(params):
    """Tier 2 probe 5 contract: evaluate(params) -> {'A': metric, 'B': metric}
    ONLY -- no extra return values. Full diagnostics (completer counts, etc.)
    are in evaluate_detail()."""
    r, _a, _b = evaluate_detail(params)
    return r


def _margin(base):
    win = max(base, key=base.get)
    lo = min(base, key=base.get)
    if base[win] == 0:
        return win, 0.0
    margin = 100.0 * (base[win] - base[lo]) / base[win]
    return win, margin


if __name__ == '__main__':
    base, a, b = evaluate_detail({})
    print("Option A (Popularity Path):", a)
    print("Option B (Ratings Gate):", b)
    win, margin = _margin(base)
    print()
    print("clicks/100 starters  A=%.2f  B=%.2f" % (base["A"], base["B"]))
    print("winner:", win, " margin: %.2f%%" % margin)

    print()
    print("--- Counterfactual: real historical S2 dropout instead of modeled MA3 ---")
    base2, a2, b2 = evaluate_detail({"dropout_b": REAL_HISTORICAL_DROPOUT_S2})
    print("Option A:", a2)
    print("Option B:", b2)
    win2, margin2 = _margin(base2)
    print("clicks/100 starters  A=%.2f  B=%.2f" % (base2["A"], base2["B"]))
    print("winner:", win2, " margin: %.2f%%  (real S2 dropout = %.4f%%)"
          % (margin2, REAL_HISTORICAL_DROPOUT_S2 * 100))

    print()
    print("--- Probe 5: flex each FLEX param by +-50%, report winner/margin ---")
    for key in FLEX:
        for mult, label in ((0.5, "-50%"), (1.5, "+50%")):
            val = PARAMS[key] * mult
            # Clamp rates/probabilities into [0, 1] -- dropout_b and the two
            # CTRs are all modeled as probabilities.
            val = max(0.0, min(1.0, val))
            b3, _a3, _b3 = evaluate_detail({key: val})
            w3, m3 = _margin(b3)
            print("  %-18s %-5s -> %.3f   A=%.2f B=%.2f  winner=%s margin=%.1f%%"
                  % (key, label, val, b3["A"], b3["B"], w3, m3))
