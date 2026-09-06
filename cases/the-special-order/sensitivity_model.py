"""
sensitivity_model.py -- The Special Order

Graded primary metric (case.json.primary_metric): true material cost per finished cabinet
door, accounting for milling waste, comparing Standard Stock (A, self-mill from standard
nominal hardwood) against The Special Order (B, mill-supplied pre-milled exact-width
hardwood). Lower cost per door is better for Grace, so evaluate() returns the NEGATIVE of
each option's cost per door -- higher score = better, matching this script's "higher wins"
convention (same convention as cases/the-deferred-repair/sensitivity_model.py).

    cost_per_door(A) = (net_width + joint_allow + kerf_allow) * length_in * thickness_in / 144
                        * pieces_per_door * price_A_per_bf
                        (constant regardless of batch size -- Standard Stock has no minimum)

    cost_per_door(B) = max(moq_bf, needed_bf(n)) * price_B_per_bf / n
                        where needed_bf(n) = net_width * length_in * thickness_in / 144
                                             * pieces_per_door * n

Appendix B's jointing allowance [S1], kerf allowance [S2], and hard maple base price [S3],
and Appendix C's custom-milling upcharge [S4] and lead time [S5] are real, sourced figures --
NOT flexed by default (cited data, stress-tested by P6 instead). Appendix E's minimum order
quantity (MA1) is the case's own disclosed Modeling Assumption -- no source publishes a
minimum specific to a small custom exact-width dimensioning run (RESEARCH_LOG.md,
case.json.modeling_assumptions[MA1]). This is the load-bearing, dilemma-relevant dial the
case names explicitly: case.json.modeling_assumptions[MA1].sensitivity states that raising
the assumed minimum pushes the breakeven batch size up and can flip the recommendation for
this exact job's 24-door batch. FLEX below sweeps exactly this one dial and nothing else.

Verified against case.json.balance / FACILITATOR.md's margin arithmetic:
    base   A = $12.7358/door  ·  B = $11.6750/door  ·  margin 8.33%  (B wins -- matches case.json)
    breakeven batch size = 23 doors (this job's batch of 24 doors clears it by one door)
"""

from fractions import Fraction as F

PARAMS = {
    # --- Appendix A, the shop's own cut-list specification (not an external fact) ----
    "net_width_in": F(7, 4),        # 1-3/4 in
    "length_in": 24,                # 2 ft per stile/rail piece
    "thickness_in": 1,              # nominal 4/4
    "pieces_per_door": 4,           # 2 stiles + 2 rails
    "doors": 24,                    # this job's batch size

    # --- Appendix B [S1] [S2], sourced milling allowances, Standard Stock only -------
    "joint_allow_in": F(1, 4),
    "kerf_allow_in": F(1, 8),

    # --- Appendix B [S3] / Appendix C [S3][S4], sourced prices, USD per board foot ---
    "price_A_per_bf": 8.99,
    "price_B_per_bf": 9.34,

    # --- Appendix E, Modeling Assumption MA1 -- the case's own load-bearing,
    #     dilemma-relevant dial. Not sourced anywhere (see RESEARCH_LOG.md);
    #     chosen near the low end of the real range found (0 to 500 board feet
    #     across adjacent custom-milling/wholesale services) so this job's
    #     24-door batch clears the resulting breakeven threshold by exactly
    #     one door (23 doors), landing the margin at 8.33%, inside SPEC §2's
    #     5-10% target band.
    "moq_bf": 30.0,
}

# Only MA1's minimum order quantity is swept by default (SPEC §2 asks for
# sensitivity to STATED ASSUMPTIONS, not to cited measurements). The milling
# allowances, prices, and cut-list geometry are either sourced figures or the
# shop's own fixed job specification -- flexing them is a different case, not
# a sensitivity test on this case's own authored assumption. Run with
# --flex-all to sweep the sourced figures too.
FLEX = ["moq_bf"]


def _bf_per_piece(width_in, p):
    return width_in * p["length_in"] * p["thickness_in"] / F(144)


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    n = p["doors"]

    rough_width = p["net_width_in"] + p["joint_allow_in"] + p["kerf_allow_in"]
    bf_per_door_A = _bf_per_piece(rough_width, p) * p["pieces_per_door"]
    bf_total_A = bf_per_door_A * n
    cost_A = float(bf_total_A) * p["price_A_per_bf"]
    cost_per_door_A = cost_A / n

    bf_per_door_B = _bf_per_piece(p["net_width_in"], p) * p["pieces_per_door"]
    bf_needed_B = bf_per_door_B * n
    bf_bought_B = max(float(p["moq_bf"]), float(bf_needed_B))
    cost_B = bf_bought_B * p["price_B_per_bf"]
    cost_per_door_B = cost_B / n

    # Lower cost is better for Grace -- return negative cost so higher score
    # wins, matching this script's "higher is better" convention.
    return {"A": -cost_per_door_A, "B": -cost_per_door_B}


def breakeven_batch_size(params=None, max_n=200):
    """Smallest integer n (doors) where B's cost/door first drops below A's."""
    p = dict(PARAMS)
    p.update(params or {})
    for n in range(1, max_n + 1):
        pp = dict(p)
        pp["doors"] = n
        r = evaluate(pp)
        if -r["B"] < -r["A"]:
            return n
    return None


if __name__ == '__main__':
    base = evaluate({})
    a_cost, b_cost = -base["A"], -base["B"]
    win = "A" if a_cost < b_cost else "B"
    lo, hi = min(a_cost, b_cost), max(a_cost, b_cost)
    margin = 100.0 * (hi - lo) / hi
    be = breakeven_batch_size()
    print("base A=$%.4f/door  B=$%.4f/door  winner=%s  margin=%.2f%%  breakeven=%s doors" %
          (a_cost, b_cost, win, margin, be))
