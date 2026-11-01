"""
sensitivity_model.py -- The Setpoint Call

Graded primary metric (case.json.primary_metric): total cost per bottle over the life
of the new co-packing contract, comparing the calculus-optimal line speed (reachable
only after a guarding retrofit) against the line's current rated safe-speed ceiling.
Lower total cost per bottle is better for Marisol, so evaluate() returns the NEGATIVE
of each option's total cost per bottle ("higher wins" convention, matching
cases/the-marginal-call/sensitivity_model.py).

    CR(r)  = a + b*r                     cost rate to run Line 3, USD/min, speed r bpm
    MPU(r) = 1/r + d                     time per bottle, min/bottle
    TC(r)  = CR(r) * MPU(r)              total cost per bottle, USD/bottle
    r*     = sqrt(a / (b*d))             the calculus optimum (TC'(r)=0, TC''(r)>0)

    Option A (Guarding Upgrade): TC(r*) + U / Q      -- retrofit cost amortized over Q
    Option B (Rated Cap):        TC(r_cap)           -- no retrofit, capped at r_cap

Appendix A's *a* (labor+burden [S1]/[S2]/MA2 + baseline utility MA1) is a derived/cited
quantity, not flexed by default (same rule as cases/the-marginal-call's v). Appendix
A's incremental cost rate *b* (MA3) and downstream handling time *d* (MA4), Appendix
B's rated ceiling r_cap (MA5), and Appendix C's retrofit cost U (MA6) and contract
volume Q (MA7) are this case's own stated Modeling Assumptions -- no public source
publishes any of them for a specific bottling line or a one-off safety retrofit. FLEX
below sweeps exactly these and nothing else.

Verified against case.json.balance / FACILITATOR.md's margin arithmetic:
    base:  r* = 335.41 bpm   TC(r*) = $0.023767/bottle
           TC(r_cap=150)     = $0.025600/bottle
           total(A) = TC(r*) + U/Q = $0.028167/bottle
           total(B) = TC(r_cap)    = $0.025600/bottle
           margin = 9.11%  (Rated Cap / Option B wins)
"""
import math

PARAMS = {
    # --- Appendix A, sourced/derived: BLS/O*NET wage [S1] x labor burden
    #     multiplier ([S2], MA2) + baseline utility draw (MA1) -------------
    "a": 0.90,
    # --- Appendix A, Modeling Assumption MA3 -- incremental cost rate -----
    "b": 0.0004,
    # --- Appendix A, Modeling Assumption MA4 -- fixed downstream handling
    #     time per bottle ----------------------------------------------
    "d": 0.02,
    # --- Appendix B, Modeling Assumption MA5 -- Line 3's current rated
    #     maximum safe operating speed ------------------------------------
    "r_cap": 150.0,
    # --- Appendix C, Modeling Assumption MA6 -- guarding/interlock
    #     retrofit cost, USD, one-time -------------------------------------
    "U": 44000.0,
    # --- Appendix C, Modeling Assumption MA7 -- total contract volume on
    #     Line 3, bottles --------------------------------------------------
    "Q": 10_000_000.0,
}

# Only the case's own stated Modeling Assumptions are swept by default (SPEC §2 asks
# for sensitivity to STATED ASSUMPTIONS, not to cited measurements). "a" is built from
# real, cited wage/burden/electricity figures -- halving it is a different case, not a
# sensitivity test on this case's own authored assumptions. Run with --flex-all to
# additionally sweep a.
FLEX = ["b", "d", "r_cap", "U", "Q"]


def _r_star(p):
    return math.sqrt(p["a"] / (p["b"] * p["d"]))


def _tc(r, p):
    cr = p["a"] + p["b"] * r
    mpu = 1.0 / r + p["d"]
    return cr * mpu


def _totals(p):
    r_star = _r_star(p)
    total_a = _tc(r_star, p) + p["U"] / p["Q"]
    total_b = _tc(p["r_cap"], p)
    return total_a, total_b, r_star


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    total_a, total_b, _ = _totals(p)
    # Lower total cost per bottle is better for Marisol -- return negative so
    # higher score wins, matching this script's convention.
    return {"A": -total_a, "B": -total_b}


def evaluate_twist(params):
    """
    The twist (FACILITATOR.md): corporate confirms the sports-drink brand has
    exercised a guaranteed volume-renewal option, tripling the contract's total
    bottle commitment on Line 3 (MA7: 10,000,000 -> 30,000,000 bottles). This
    applies ONLY to Option A's amortization base -- The Guarding Upgrade's
    retrofit cost is spread over however many bottles the contract actually
    runs, which is exactly the number that just changed. It does not touch
    Option B's arithmetic at all: The Rated Cap pays no retrofit cost, so it has
    nothing to amortize and TC(r_cap) is a pure per-bottle rate, unaffected by
    total contract volume. Modeled as tripling Q for Option A's evaluation only,
    not via a shared PARAMS mutation, so the twist's own scoping (only the
    amortized side of the comparison moves) cannot silently leak into Option B
    the way cases/the-marginal-call's original (buggy) evaluate_twist() once did.
    """
    p_a = dict(PARAMS)
    p_a.update(params or {})
    p_a["Q"] = p_a["Q"] * 3.0  # confirmed volume-renewal option, Option A's amortization base only
    r_star = _r_star(p_a)
    total_a = _tc(r_star, p_a) + p_a["U"] / p_a["Q"]

    p_b = dict(PARAMS)
    p_b.update(params or {})
    total_b = _tc(p_b["r_cap"], p_b)

    return {"A": -total_a, "B": -total_b}


if __name__ == '__main__':
    base = evaluate({})
    a_tc, b_tc = -base["A"], -base["B"]
    win = "A" if a_tc < b_tc else "B"
    lo, hi = min(a_tc, b_tc), max(a_tc, b_tc)
    margin = 100.0 * (hi - lo) / hi
    print("base: total(A)=$%.6f/bottle  total(B)=$%.6f/bottle  winner=%s  margin=%.2f%%" % (a_tc, b_tc, win, margin))

    p = dict(PARAMS)
    r_star = _r_star(p)
    print("r* (calculus optimum) = %.2f bpm   TC(r*) = $%.6f/bottle" % (r_star, _tc(r_star, p)))
    print("TC(r_cap=%.0f bpm) = $%.6f/bottle" % (p["r_cap"], _tc(p["r_cap"], p)))
    print("U/Q = $%.6f/bottle (Option A's amortized retrofit cost)" % (p["U"] / p["Q"]))

    twist = evaluate_twist({})
    a_t, b_t = -twist["A"], -twist["B"]
    win_t = "A" if a_t < b_t else "B"
    lo_t, hi_t = min(a_t, b_t), max(a_t, b_t)
    margin_t = 100.0 * (hi_t - lo_t) / hi_t
    print("twist: total(A)=$%.6f/bottle  total(B)=$%.6f/bottle  winner=%s  margin=%.2f%%" % (a_t, b_t, win_t, margin_t))
