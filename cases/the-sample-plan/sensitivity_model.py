"""
sensitivity_model.py -- The Sample Plan

Graded primary metric (case.json.primary_metric): expected total cost per production lot
(certain destructive-testing cost + probability-weighted expected cost of an undetected
out-of-spec escape), comparing The Lean Draw (A, ANSI/ASQ Z1.4 General Inspection Level II,
n=50) against The Deep Draw (B, Level III, n=80). Lower expected total cost is better for
Renata, so evaluate() returns the NEGATIVE of each option's expected cost -- higher score =
better (same convention as cases/deductible-roulette).

Model, per option:
  escape_probability(n)  = (1 - defect_fraction) ** n
      -- the probability that a fully out-of-spec lot (every unit checked against a "c=0"
      acceptance rule, [S2]) still passes all n destructively-tested units and ships
      undetected. defect_fraction (MA1) is the case's one PRIMARY-metric assumption: the
      fraction of individual units that are actually defective inside a lot that IS
      out-of-spec. Sourced sample sizes n and per-unit test cost are NOT flexed -- policy
      design / standard-table values, not measurements (same convention as
      deductible-roulette's premiums/deductibles).

  expected_total_cost(option) = n * unit_test_cost
                               + lot_occurrence_prob * escape_probability(n) * cost_of_escape

lot_occurrence_prob is SOURCED ([S3], 2.3%, large-scale-facility batch contamination rate) and
is NOT flexed by default in the PRIMARY metric -- cited data, stress-tested by P6 instead, per
"only FLEX[] is swept" (SPEC SS2: sensitivity to STATED ASSUMPTIONS, not cited measurements).

evaluate_twist() is the Challenge 3 (D4) / Twist scenario: Lot 4471 has been flagged by a
supplier deviation notice, so the SOURCED population-average lot_occurrence_prob (2.3%) no
longer applies -- MA2 (a stated, moderate multiple of the baseline) is substituted instead.
This is the parameter genuinely swept for the twist.

Verified against case.json.balance / case.json.derived:
    base   A = $21,580.02  ·  B = $24,248.40  ·  margin 11.0%  (A wins -- matches case.json)
    twist  A = $36,187.00  ·  B = $31,082.78  ·  margin 14.11% (B wins -- matches case.json)
"""

PARAMS = {
    # --- Appendix A/B [S1], sourced sample sizes and policy-design cost, not flexed --------
    "n_A": 50,
    "n_B": 80,
    "unit_test_cost": 250.0,
    # --- Appendix C, sourced baseline lot-occurrence probability [S3] ----------------------
    "lot_occurrence_prob": 0.023,
    # --- Appendix C, sourced-derived cost of an undetected escape [S3] ---------------------
    "cost_of_escape": 1_400_000.0,
    # --- Appendix C, Modeling Assumption MA1 -- the case's one PRIMARY-metric dial. Not
    #     sourced anywhere as a unit-level figure (see RESEARCH_LOG.md).
    "defect_fraction": 0.025,
    # --- Appendix C, Modeling Assumption MA2 -- used ONLY in evaluate_twist(), substituted
    #     for lot_occurrence_prob under the supplier-deviation-notice scenario.
    "deviation_lot_occurrence_prob": 0.06,
}

# Only MA1 (defect_fraction) is swept by default for the PRIMARY metric.
FLEX = ["defect_fraction"]


def _escape_prob(defect_fraction, n):
    return (1.0 - defect_fraction) ** n


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    eA = _escape_prob(p["defect_fraction"], p["n_A"])
    eB = _escape_prob(p["defect_fraction"], p["n_B"])
    a_cost = p["n_A"] * p["unit_test_cost"] + p["lot_occurrence_prob"] * eA * p["cost_of_escape"]
    b_cost = p["n_B"] * p["unit_test_cost"] + p["lot_occurrence_prob"] * eB * p["cost_of_escape"]
    # Lower cost is better for Renata -- return negative cost so higher score wins.
    return {"A": -a_cost, "B": -b_cost}


def evaluate_twist(params):
    """The Twist: Lot 4471 has been flagged by a supplier deviation notice. Recompute each
    option's expected cost using MA2 (deviation_lot_occurrence_prob) in place of the sourced
    population-average lot_occurrence_prob -- this is the Challenge 3 (D4) scenario."""
    p = dict(PARAMS)
    p.update(params or {})
    eA = _escape_prob(p["defect_fraction"], p["n_A"])
    eB = _escape_prob(p["defect_fraction"], p["n_B"])
    a_cost = p["n_A"] * p["unit_test_cost"] + p["deviation_lot_occurrence_prob"] * eA * p["cost_of_escape"]
    b_cost = p["n_B"] * p["unit_test_cost"] + p["deviation_lot_occurrence_prob"] * eB * p["cost_of_escape"]
    return {"A": -a_cost, "B": -b_cost}


def _summarize(result):
    a_cost, b_cost = -result["A"], -result["B"]
    win = "A" if a_cost < b_cost else ("B" if b_cost < a_cost else "TIE")
    lo, hi = min(a_cost, b_cost), max(a_cost, b_cost)
    margin = 0.0 if hi == 0 else 100.0 * (hi - lo) / hi
    return a_cost, b_cost, win, margin


if __name__ == "__main__":
    a_cost, b_cost, win, margin = _summarize(evaluate({}))
    print("PRIMARY  base A=$%.2f  B=$%.2f  winner=%s  margin=%.2f%%" % (a_cost, b_cost, win, margin))

    for flex_pct, label in [(1.5, "+50%%"), (0.5, "-50%%")]:
        flexed = dict(PARAMS)
        flexed["defect_fraction"] = PARAMS["defect_fraction"] * flex_pct
        a2, b2, win2, margin2 = _summarize(evaluate(flexed))
        print("PRIMARY  defect_fraction %s (%.4f)  A=$%.2f  B=$%.2f  winner=%s  margin=%.2f%%  flip=%s"
              % (label, flexed["defect_fraction"], a2, b2, win2, margin2, win2 != win))

    # Binary-search whether ANY defect_fraction in [0,1] flips the PRIMARY metric.
    lo, hi = 0.0, 1.0
    if _summarize(evaluate({"defect_fraction": hi}))[2] == win and _summarize(evaluate({"defect_fraction": lo}))[2] == win:
        print("PRIMARY  no flip found for defect_fraction anywhere in [0.00, 1.00] -- winner stays %s" % win)
    else:
        for _ in range(60):
            mid = (lo + hi) / 2.0
            if _summarize(evaluate({"defect_fraction": mid}))[2] == win:
                lo = mid
            else:
                hi = mid
        print("PRIMARY  flip threshold: defect_fraction ~= %.4f (%.1f%%)" % (hi, hi * 100))

    at, bt, wint, margint = _summarize(evaluate_twist({}))
    print("TWIST    (supplier deviation notice, MA2=%.1f%%) A=$%.2f  B=$%.2f  winner=%s  margin=%.2f%%"
          % (PARAMS["deviation_lot_occurrence_prob"] * 100, at, bt, wint, margint))

    # Binary-search the lot-occurrence probability that flips the TWIST scenario, holding
    # defect_fraction (MA1) fixed at its base value. Sweeps the SUBSTITUTED probability
    # itself (not defect_fraction) since that is the parameter the Twist scenario actually
    # varies -- MA2 replaces the sourced baseline for one specific, flagged lot.
    lo, hi = PARAMS["lot_occurrence_prob"], 1.0

    def twist_total(occurrence_prob):
        eA = _escape_prob(PARAMS["defect_fraction"], PARAMS["n_A"])
        eB = _escape_prob(PARAMS["defect_fraction"], PARAMS["n_B"])
        a_cost = PARAMS["n_A"] * PARAMS["unit_test_cost"] + occurrence_prob * eA * PARAMS["cost_of_escape"]
        b_cost = PARAMS["n_B"] * PARAMS["unit_test_cost"] + occurrence_prob * eB * PARAMS["cost_of_escape"]
        return a_cost, b_cost

    base_a, base_b = twist_total(lo)
    base_win = "A" if base_a < base_b else "B"
    hi_a, hi_b = twist_total(hi)
    hi_win = "A" if hi_a < hi_b else "B"
    if hi_win == base_win:
        print("TWIST    no flip found for lot-occurrence probability in [%.3f, 1.00]" % lo)
    else:
        for _ in range(60):
            mid = (lo + hi) / 2.0
            ma, mb = twist_total(mid)
            mwin = "A" if ma < mb else "B"
            if mwin == base_win:
                lo = mid
            else:
                hi = mid
        print("TWIST    flip threshold: lot-occurrence probability ~= %.4f (%.2f%%)" % (hi, hi * 100))
