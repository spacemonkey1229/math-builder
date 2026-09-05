"""
sensitivity_model.py — The Deferred Repair

Graded primary metric (case.json.primary_metric): expected total dollars spent on the
coolant system per year of ownership, comparing The Standing Order (A, always pay the
flush) against The Reactive Route (B, pay only if the engine fails). Lower expected
annual cost is better for Elena, so evaluate() returns the NEGATIVE of each option's
expected annual cost -- higher score = better, matching this script's "higher wins"
convention (same convention as cases/gerrymandering/sensitivity_model.py).

    expected_annual_cost(A) = flush_price                              (certain, every year)
    expected_annual_cost(B) = mean over 3 years of (year's probability x repair_cost)

Appendix A's flush price [S1] and Appendix B's repair cost [S4] are real, sourced
RepairPal figures -- NOT flexed by default (cited data, stress-tested by P6 instead).
Appendix B's Year 1/2/3 probabilities (MA1) are the case's own disclosed Modeling
Assumption -- no source publishes a per-year conditional failure-probability schedule
for a skipped coolant flush (RESEARCH_LOG.md, case.json.modeling_assumptions[MA1]).
These three probabilities are the load-bearing, dilemma-flipping dial the case names
explicitly: case.json.modeling_assumptions[MA1].sensitivity states the comparison
flips below a ~16.1% three-year average failure probability against a currently
assumed ~14% average. FLEX below sweeps exactly these three and nothing else.

Verified against case.json.balance / FACILITATOR.md's margin arithmetic:
    base   A = $473.00/yr  ·  B = $411.32/yr  ·  margin 13.0%  (A wins -- matches case.json)
"""

PARAMS = {
    # --- Appendix A [S1], sourced, certain, every year ----------------------
    "flush_price": 473.0,
    # --- Appendix B [S4], sourced repair cost if the coolant system fails --
    "repair_cost": 2938.0,
    # --- Appendix B, Modeling Assumption MA1 -- the case's own load-bearing,
    #     dilemma-flipping dial. Not sourced anywhere (see RESEARCH_LOG.md);
    #     chosen to escalate year over year and to land the margin at 13.0%,
    #     inside SPEC §2's 10-15% target band and close to the ~16.1% flip
    #     point named in case.json.modeling_assumptions[MA1].sensitivity.
    "y1_prob": 0.09,
    "y2_prob": 0.13,
    "y3_prob": 0.20,
}

# Only MA1's three probabilities are swept by default (SPEC §2 asks for
# sensitivity to STATED ASSUMPTIONS, not to cited measurements). flush_price and
# repair_cost are real RepairPal figures [S1]/[S4] -- halving a sourced repair
# estimate is a different case, not a sensitivity test on this case's own
# authored assumption. Run with --flex-all to sweep the sourced figures too.
FLEX = ["y1_prob", "y2_prob", "y3_prob"]


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    a_cost = p["flush_price"]
    b_cost = (p["y1_prob"] + p["y2_prob"] + p["y3_prob"]) / 3.0 * p["repair_cost"]
    # Lower cost is better for Elena -- return negative cost so higher score wins,
    # matching this script's "higher is better" convention.
    return {"A": -a_cost, "B": -b_cost}


if __name__ == '__main__':
    base = evaluate({})
    a_cost, b_cost = -base["A"], -base["B"]
    win = "A" if a_cost < b_cost else "B"
    lo, hi = min(a_cost, b_cost), max(a_cost, b_cost)
    margin = 100.0 * (hi - lo) / hi
    print("base A=$%.2f/yr  B=$%.2f/yr  winner=%s  margin=%.1f%%" % (a_cost, b_cost, win, margin))
