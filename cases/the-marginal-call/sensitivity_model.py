"""
sensitivity_model.py -- The Marginal Call

Graded primary metric (case.json.primary_metric): net cost per board foot of black
walnut actually SOLD within the planning quarter -- average unit cost, penalized for
the carrying cost of any board footage locked in but not sold this quarter. Lower net
cost is better for Renata, so evaluate() returns the NEGATIVE of each option's net
cost per board foot sold -- higher score = better ("higher wins" convention, matching
cases/the-deferred-repair/sensitivity_model.py).

    C(x)  = F + v*x + k*x^2                          total production cost, board feet x
    A(x)  = C(x) / x                                 raw average cost per board foot
    NC(x) = (C(x) + carry_per_bf * max(0, x - D)) / min(x, D)   net cost per bf SOLD

Appendix A's lumber price, kiln-drying price, and BLS wage feed v [S1]/[S2]/[S3] --
NOT flexed by default (cited data; P6 stress-tests URLs, not values). Appendix A's
fixed cost F (MA1) and overtime coefficient k (MA3), Appendix B's two batch sizes
(MA4, MA5), Appendix C's sellable limit (MA6) and the carrying-cost quarterly
conversion (derived from [S4]'s annual rate) are the case's own stated Modeling
Assumptions -- no public source publishes any of them for a specific mill or shop.
FLEX below sweeps exactly these and nothing else.

Verified against case.json.balance / FACILITATOR.md's margin arithmetic:
    base:  raw A(steady)=$18.50/bf  A(full)=$18.30/bf  (Full Kiln looks cheaper, 1.1%)
           NC(steady)=$18.50/bf  NC(full)=$20.43/bf   margin 9.4%  (Steady Order wins)
"""

PARAMS = {
    # --- Appendix A, sourced/derived: lumber [S1] + kiln-drying [S2] + labor
    #     (BLS wage [S3] / an assumed bf-per-hour rate, MA2) -----------------
    "v": 17.40,
    # --- Appendix A, Modeling Assumption MA1 -- fixed cost per kiln run ----
    "F": 1800.0,
    # --- Appendix A, Modeling Assumption MA3 -- overtime cost coefficient --
    "k": 0.0001,
    # --- Appendix B, Modeling Assumptions MA4 / MA5 -- the two real batch
    #     sizes on the table ---------------------------------------------
    "steady_bf": 2000.0,
    "full_bf": 3000.0,
    # --- Appendix C, Modeling Assumption MA6 -- this quarter's sellable
    #     limit (hotel order + standing accounts) ------------------------
    "sellable_limit": 2700.0,
    # --- Appendix C, derived from [S4]'s ~20%/year benchmark applied at
    #     one-quarter of the annual rate (this case's own arithmetic, not
    #     part of the cited figure) ---------------------------------------
    "carry_rate_q": 0.05,
}

# Only the case's own stated Modeling Assumptions are swept by default (SPEC §2
# asks for sensitivity to STATED ASSUMPTIONS, not to cited measurements). v is
# built from real, cited lumber/kiln/wage figures -- halving it is a different
# case, not a sensitivity test on this case's own authored assumptions. Run
# with --flex-all to additionally sweep v.
FLEX = ["F", "k", "steady_bf", "full_bf", "sellable_limit", "carry_rate_q"]


def _cost(x, p):
    return p["F"] + p["v"] * x + p["k"] * x ** 2


def _net_cost_per_bf_sold(x, p):
    d = p["sellable_limit"]
    sold = min(x, d)
    unsold = max(0.0, x - d)
    carry_per_bf = p["carry_rate_q"] * p["v"]
    total = _cost(x, p) + carry_per_bf * unsold
    return total / sold


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    a_net = _net_cost_per_bf_sold(p["steady_bf"], p)
    b_net = _net_cost_per_bf_sold(p["full_bf"], p)
    # Lower net cost per board foot sold is better for Renata -- return
    # negative so higher score wins, matching this script's convention.
    return {"A": -a_net, "B": -b_net}


def evaluate_twist(params):
    """
    The twist (FACILITATOR.md): the mill confirms the competing national chain's bid
    forces Renata to match a higher price specifically to hold The Full Kiln's slot --
    the larger, deep-discount run the competitor is also bidding on. The Steady
    Order's usual, smaller run is not the batch under competitive pressure and is not
    repriced. This is modeled as a fixed-cost shock (a higher effective run-booking
    price to secure the contested slot) applied ONLY to the Full Kiln evaluation, not
    to Steady Order's -- fixed 2026-09-05 after Tier 2 P4 found the original
    implementation raised F for BOTH options via a shared PARAMS dict, which
    contradicted the twist's own narrative (only the contested, larger run is being
    bid up) and made FACILITATOR.md's "wider margin" claim arithmetically false (the
    old code actually NARROWED the margin, 9.45% -> 8.73%, because a uniform F shock
    helps the smaller batch's raw average cost less in absolute terms but hurts it
    more as a share of its own smaller cost base). Applying the shock only to Full
    Kiln matches both the narrative and FACILITATOR.md's stated conclusion.
    """
    p_a = dict(PARAMS)
    p_a.update(params or {})
    a_net = _net_cost_per_bf_sold(p_a["steady_bf"], p_a)

    p_b = dict(PARAMS)
    p_b.update(params or {})
    p_b["F"] = p_b["F"] * 1.5  # 50% higher fixed run cost, Full Kiln's contested slot only
    b_net = _net_cost_per_bf_sold(p_b["full_bf"], p_b)

    return {"A": -a_net, "B": -b_net}


if __name__ == '__main__':
    import math

    base = evaluate({})
    a_net, b_net = -base["A"], -base["B"]
    win = "A" if a_net < b_net else "B"
    lo, hi = min(a_net, b_net), max(a_net, b_net)
    margin = 100.0 * (hi - lo) / hi
    print("base: NC(A)=$%.4f/bf  NC(B)=$%.4f/bf  winner=%s  margin=%.2f%%" % (a_net, b_net, win, margin))

    p = dict(PARAMS)
    xstar = math.sqrt(p["F"] / p["k"])
    print("x* (raw AC minimizer) = %.2f bf,  A(x*) = $%.4f/bf" % (xstar, _cost(xstar, p) / xstar))
    print("raw A(steady)=$%.4f/bf  raw A(full)=$%.4f/bf" % (
        _cost(p["steady_bf"], p) / p["steady_bf"], _cost(p["full_bf"], p) / p["full_bf"]))

    twist = evaluate_twist({})
    a_t, b_t = -twist["A"], -twist["B"]
    win_t = "A" if a_t < b_t else "B"
    print("twist: NC(A)=$%.4f/bf  NC(B)=$%.4f/bf  winner=%s" % (a_t, b_t, win_t))
