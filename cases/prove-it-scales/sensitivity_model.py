#!/usr/bin/env python3
"""
Sensitivity model -- Prove It Scales.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips
the verdict"). See skills/case-readiness/scripts/example_sensitivity_model.py.

Primary metric (case.json.primary_metric): ms of RollUpCharges runtime per
10,000 billing rollups. The graded margin (case.json.margin_pct=95.8) is
computed at the Shallow depth, under Go (MA7), which does not honor TCO
(S4) -- so evaluate() compares Option A (recursive, TCO-not-honored column)
against Option B (iterative), both DIRECTLY MEASURED figures from S1, not
Modeling Assumptions.

evaluate() returns the NEGATIVE of each option's ms/10,000-rollups (higher =
better = faster), matching this batch's sign convention.

CRITICAL SCOPING NOTE (see case.json.balance.margin_note and the MCS-46
waiver): S1's Shallow-row figures (0.164 ms iterative, 3.94 ms recursive
TCO-not-honored) are DIRECTLY MEASURED benchmark data, not stated Modeling
Assumptions -- there is nothing to flex here without contradicting real,
cited data, which SPEC Sec5 forbids. The only genuine stated Modeling
Assumption that changes WHICH column of Appendix D drives the graded margin
is MA7 (target runtime = Go, which selects the TCO-not-honored column via
S4's real fact). FLEX[] therefore sweeps a single boolean-like toggle
(tco_honored) between the two REAL, MEASURED columns S1 actually reports,
rather than perturbing either measured number by an arbitrary percentage.
"""

PARAMS = {
    # --- Appendix D / S1: directly measured Shallow-row figures (ms/10,000) --
    "iterative_ms": 0.164,
    "recursive_tco_honored_ms": 0.333,
    "recursive_tco_not_honored_ms": 3.94,
    # --- MA7: target runtime selects which recursive column applies ----------
    # 1.0 = Go (does not honor TCO, S4) -- the case's actual stated target.
    # 0.0 = a TCO-honoring runtime (the counterfactual case.json.balance.margin_note checks).
    "tco_not_honored": 1.0,
}

# Only MA7 (via this boolean-like toggle) is a genuine stated Modeling
# Assumption feeding this comparison. The three ms figures themselves are
# directly measured (S1) and are NOT flexed -- perturbing real benchmark
# numbers by +/-50% would contradict SPEC Sec5's "never fabricate a number"
# rule, which is exactly why this case carries an MCS-46 waiver instead of a
# retune.
FLEX = [
    "tco_not_honored",
]


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})

    recursive_ms = (p["recursive_tco_not_honored_ms"] if p["tco_not_honored"] >= 0.5
                     else p["recursive_tco_honored_ms"])

    return {"A": -recursive_ms, "B": -p["iterative_ms"]}


if __name__ == '__main__':
    base = evaluate({})
    a, b = -base["A"], -base["B"]
    margin = 100 * (a - b) / a
    print("base (Go, TCO not honored, MA7=1)  A(recursive)=%.3f ms  B(iterative)=%.3f ms" % (a, b),
          "margin %.1f%%" % margin, "-- matches case.json.margin_pct (95.8)")

    honored = evaluate({"tco_not_honored": 0.0})
    a2, b2 = -honored["A"], -honored["B"]
    margin2 = 100 * (a2 - b2) / a2
    print("MA7 counterfactual (TCO-honoring runtime)  A=%.3f ms  B=%.3f ms" % (a2, b2),
          "margin %.1f%%" % margin2, "-- matches case.json.balance.margin_note's 50.8%% counterfactual")
    print("Winner in both cases: B (iterative) -- confirms the lopsidedness is structural to the")
    print("real S1/S2 benchmark data, not an artifact of the MA7 runtime choice (per the MCS-46 waiver).")
