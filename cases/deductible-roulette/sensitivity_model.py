"""
sensitivity_model.py -- Deductible Roulette

Graded primary metric (case.json.primary_metric): expected total dollars spent on
auto insurance (premium + probability-weighted deductible exposure) over a three-year
window, comparing The Guarded Lane (A, $500 deductible, higher premium) against The
Long Shot (B, $1,000 deductible, lower premium). Lower expected total cost is better
for Priya, so evaluate() returns the NEGATIVE of each option's expected 3-year total
cost -- higher score = better (same convention as cases/the-deferred-repair).

Each year, Priya is in one of two branches:
  - "clean"     -- no claim yet in this window. That year's claim probability is the
                   Appendix B baseline rate (SOURCED, [S2], NOT flexed by default --
                   cited data, stress-tested by P6 instead).
  - "post-claim" -- a claim has already occurred earlier in the window. That year's
                   claim probability is Appendix C's elevated rate (MA1, the case's
                   one stated Modeling Assumption -- see case.json.modeling_assumptions).

    P(clean entering Year 1)  = 1
    P(clean entering Year 2)  = 1 - base_prob
    P(clean entering Year 3)  = (1 - base_prob) ** 2
    expected deductible payments (in units of "number of deductibles paid") =
        base_prob                                                  (Year 1)
      + (1-base_prob)*base_prob + base_prob*recid_prob             (Year 2)
      + (1-base_prob)**2*base_prob + (1-(1-base_prob)**2)*recid_prob  (Year 3)

expected_3yr_cost(option) = 3 * annual_premium(option)
                           + deductible(option) * expected_deductible_payments

Appendix A's premiums [S1] and the deductible amounts themselves (policy design,
not measurements) are NOT flexed. Appendix B's baseline claim probability [S2] is
SOURCED and NOT flexed by default (cited data -- P6 covers it). Only MA1
(recid_prob, Appendix C) is swept by default, per "only FLEX[] is swept" (SPEC SS2:
sensitivity to STATED ASSUMPTIONS, not cited measurements).

Verified against case.json.balance / case.json.derived:
    base   A = $7,998.42  ·  B = $7,176.83  ·  margin 10.3%  (B wins -- matches case.json)
"""

PARAMS = {
    # --- Appendix A [S1], sourced, certain, every year --------------------
    "premium_A": 2638.0,
    "premium_B": 2336.0,
    "deductible_A": 500.0,
    "deductible_B": 1000.0,
    # --- Appendix B [S2], sourced baseline collision-claim probability ----
    "base_prob": 0.049,
    # --- Appendix C, Modeling Assumption MA1 -- the case's one stated,
    #     dilemma-relevant (though NOT dilemma-flipping at the primary-
    #     metric level -- see sensitivity() below) dial. Not sourced
    #     anywhere as a general-population figure (see RESEARCH_LOG.md).
    "recid_prob": 0.20,
}

# Only MA1's repeat-claim probability is swept by default.
FLEX = ["recid_prob"]


def _expected_deductible_payments(base_prob, recid_prob):
    clean_y1 = 1.0
    clean_y2 = 1.0 - base_prob
    clean_y3 = (1.0 - base_prob) ** 2
    y1 = clean_y1 * base_prob
    y2 = clean_y2 * base_prob + (1.0 - clean_y2) * recid_prob
    y3 = clean_y3 * base_prob + (1.0 - clean_y3) * recid_prob
    return y1 + y2 + y3


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    factor = _expected_deductible_payments(p["base_prob"], p["recid_prob"])
    a_cost = 3 * p["premium_A"] + p["deductible_A"] * factor
    b_cost = 3 * p["premium_B"] + p["deductible_B"] * factor
    # Lower cost is better for Priya -- return negative cost so higher score wins.
    return {"A": -a_cost, "B": -b_cost}


def evaluate_twist(params):
    """The Twist: a claim has ALREADY occurred in Year 1. Recompute the remaining
    Year 2 + Year 3 total cost for each option, using MA1's elevated rate for both
    remaining years (Priya is now in the 'post-claim' branch for the rest of the
    window). This is the Challenge 3 (D4) / FACILITATOR.md twist scenario."""
    p = dict(PARAMS)
    p.update(params or {})
    remaining_years = 2
    a_remaining = remaining_years * p["premium_A"] + remaining_years * p["recid_prob"] * p["deductible_A"]
    b_remaining = remaining_years * p["premium_B"] + remaining_years * p["recid_prob"] * p["deductible_B"]
    return {"A": -a_remaining, "B": -b_remaining}


def _summarize(result):
    a_cost, b_cost = -result["A"], -result["B"]
    win = "A" if a_cost < b_cost else ("B" if b_cost < a_cost else "TIE")
    lo, hi = min(a_cost, b_cost), max(a_cost, b_cost)
    margin = 0.0 if hi == 0 else 100.0 * (hi - lo) / hi
    return a_cost, b_cost, win, margin


if __name__ == '__main__':
    a_cost, b_cost, win, margin = _summarize(evaluate({}))
    print("PRIMARY  base A=$%.2f  B=$%.2f  winner=%s  margin=%.1f%%" % (a_cost, b_cost, win, margin))

    for flex_pct, label in [(1.5, "+50%%"), (0.5, "-50%%")]:
        flexed = dict(PARAMS)
        flexed["recid_prob"] = PARAMS["recid_prob"] * flex_pct
        a2, b2, win2, margin2 = _summarize(evaluate(flexed))
        print("PRIMARY  recid_prob %s (%.3f)  A=$%.2f  B=$%.2f  winner=%s  margin=%.1f%%  flip=%s"
              % (label, flexed["recid_prob"], a2, b2, win2, margin2, win2 != win))

    # Binary-search the recid_prob value that flips the PRIMARY metric from B to A.
    lo, hi = PARAMS["recid_prob"], 1.0
    if _summarize(evaluate({"recid_prob": hi}))[2] != "A":
        print("PRIMARY  no flip found for recid_prob in [%.2f, 1.00]" % lo)
    else:
        for _ in range(60):
            mid = (lo + hi) / 2.0
            if _summarize(evaluate({"recid_prob": mid}))[2] == "A":
                hi = mid
            else:
                lo = mid
        print("PRIMARY  flip threshold: recid_prob ~= %.4f (%.1f%%)" % (hi, hi * 100))

    at, bt, wint, margint = _summarize(evaluate_twist({}))
    print("TWIST    (claim already occurred, Y1) remaining A=$%.2f  B=$%.2f  winner=%s  margin=%.1f%%"
          % (at, bt, wint, margint))
    for flex_pct, label in [(1.5, "+50%%"), (0.5, "-50%%")]:
        flexed = dict(PARAMS)
        flexed["recid_prob"] = PARAMS["recid_prob"] * flex_pct
        at2, bt2, wint2, margint2 = _summarize(evaluate_twist(flexed))
        print("TWIST    recid_prob %s (%.3f)  A=$%.2f  B=$%.2f  winner=%s  margin=%.1f%%  flip=%s"
              % (label, flexed["recid_prob"], at2, bt2, wint2, margint2, wint2 != wint))

    # Binary-search the recid_prob value that flips the TWIST scenario (D4:
    # remaining Years 2-3 after a Year-1 claim) from B to A. UNLIKE the primary
    # metric above, this one DOES flip -- recid_prob applies UNDILUTED to both
    # remaining years here (no "still clean" branch dilutes it, since a claim has
    # already happened by construction), so it can outweigh the smaller 2-year
    # premium gap. Found 2026-09-04 via an adversarial Tier 2 P4 review after an
    # earlier pass of this file only bisected the primary metric and wrongly
    # implied (via case.json.derived.flip_threshold = null) that NO metric in
    # this case is sensitive to recid_prob -- true for evaluate(), false for
    # evaluate_twist(). See case.json.derived.twist_flip_threshold and
    # FACILITATOR.md's Twist section, both corrected to state this explicitly.
    lo, hi = PARAMS["recid_prob"], 1.0
    if _summarize(evaluate_twist({"recid_prob": hi}))[2] != "A":
        print("TWIST    no flip found for recid_prob in [%.2f, 1.00]" % lo)
    else:
        for _ in range(60):
            mid = (lo + hi) / 2.0
            if _summarize(evaluate_twist({"recid_prob": mid}))[2] == "A":
                hi = mid
            else:
                lo = mid
        print("TWIST    flip threshold: recid_prob ~= %.4f (%.1f%%)" % (hi, hi * 100))
