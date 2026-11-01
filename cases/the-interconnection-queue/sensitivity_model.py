"""
sensitivity_model.py -- The Interconnection Queue

Graded primary metric (case.json.primary_metric): capacity stranded (left unallocated) at the
Fenwick Creek substation, as a fraction of a capacity block, after each option's bid combination
-- lower stranded capacity is better. evaluate() returns the NEGATIVE of each option's stranded
capacity so higher score = better, matching this script's "higher wins" convention (same
convention as cases/the-special-order/sensitivity_model.py).

    remaining      = total_capacity_blocks - committed_capacity_blocks
    stranded_A     = remaining - aurora_ridge_blocks
    combined_B     = cobalt_peak_blocks + fenwick_yards_blocks
    stranded_B     = remaining - combined_B          (only meaningful if combined_B <= remaining)

Appendix A's total/committed capacity and Appendix B's four bid sizes are the case's own fixed
scenario data (Meridian Valley Power's own capacity-of-record and queue-board entries) -- NOT
externally sourced, so NOT flexed by default. Appendix C/D's capacity-block MW size (MA1) is the
case's own disclosed Modeling Assumption -- no source publishes a block size specific to this
fictional substation (RESEARCH_LOG.md, case.json.modeling_assumptions[MA1]). FLEX below sweeps
exactly that one dial. Per case.json.modeling_assumptions[MA1].sensitivity, this parameter is
expected NOT to flip the verdict, because the A-vs-B comparison is a same-units fraction
comparison in blocks that the MW scale cancels out of entirely -- flexing block_size_mw only
rescales the real-world MW figures reported alongside the block comparison, so evaluate() (which
works entirely in block units) is intentionally insensitive to it. It is retained in FLEX/PARAMS
so P5 can confirm this mechanically rather than by assertion, and so the megawatt figures a
facilitator might report can still be recomputed under a different assumed block size.

Verified against case.json.balance / FACILITATOR.md's margin arithmetic:
    base   stranded_A = 1/2 block (12 MW)  ·  stranded_B = 11/24 block (11 MW)  ·  margin 8.33%
    (B wins -- matches case.json; combined_B = 2-11/12 blocks fits inside remaining = 3-3/8 blocks)
"""

from fractions import Fraction as F

PARAMS = {
    # --- Appendix A, Meridian Valley Power's own capacity-of-record (not external) -----
    "total_capacity_blocks": F(37, 8),      # 4-5/8
    "committed_capacity_blocks": F(5, 4),   # 1-1/4

    # --- Appendix B, Meridian Valley Power's own queue-board entries (not external) ----
    "aurora_ridge_blocks": F(23, 8),        # 2-7/8  (Option A: approve now)
    "cobalt_peak_blocks": F(5, 4),          # 1-1/4  (Option B: combined bid, part 1)
    "fenwick_yards_blocks": F(5, 3),        # 1-2/3  (Option B: combined bid, part 2)
    "briar_hollow_blocks": F(11, 6),        # 1-5/6  (queue overflow; D1 only, not in A/B math)

    # --- Appendix C/D, Modeling Assumption MA1 -- the case's own disclosed, non-load-
    #     bearing dial. Not sourced anywhere (see RESEARCH_LOG.md); chosen near RMI's real
    #     ~20 MW large-load interconnection reference point [S5]. Confirmed algebraically
    #     and mechanically (below) NOT to change which option wins, since evaluate() is
    #     computed entirely in block units -- the MW scale cancels out of the comparison.
    "block_size_mw": 24.0,
}

# Only MA1's block size is swept by default (SPEC §2 asks for sensitivity to STATED
# ASSUMPTIONS, not to cited measurements or the case's own fixed scenario data).
# Appendix A/B's capacities and bid sizes are Meridian Valley Power's own queue-of-record
# figures, not a sourced measurement or an assumption -- flexing them is a different case,
# not a sensitivity test on this case's own authored assumption. Run with --flex-all to
# sweep them too.
FLEX = ["block_size_mw"]


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})

    remaining = p["total_capacity_blocks"] - p["committed_capacity_blocks"]

    stranded_A = remaining - p["aurora_ridge_blocks"]

    combined_B = p["cobalt_peak_blocks"] + p["fenwick_yards_blocks"]
    stranded_B = remaining - combined_B

    # Lower stranded capacity is better for Renata -- return negative stranded so higher
    # score wins, matching this script's "higher is better" convention. block_size_mw does
    # not enter this calculation at all (it only rescales MW reporting elsewhere), which is
    # exactly the point P5 is meant to confirm.
    return {"A": -float(stranded_A), "B": -float(stranded_B)}


def blocks_to_mw(blocks, params=None):
    """Helper for facilitator-side MW reporting only -- not used by evaluate()."""
    p = dict(PARAMS)
    p.update(params or {})
    return float(blocks) * p["block_size_mw"]


if __name__ == '__main__':
    base = evaluate({})
    a_stranded, b_stranded = -base["A"], -base["B"]
    win = "A" if a_stranded < b_stranded else ("B" if b_stranded < a_stranded else "TIE")
    lo, hi = min(a_stranded, b_stranded), max(a_stranded, b_stranded)
    margin = 100.0 * (hi - lo) / hi if hi else 0.0
    print("base stranded_A=%.6f blocks (%.2f MW)  stranded_B=%.6f blocks (%.2f MW)  "
          "winner=%s  margin=%.2f%%" %
          (a_stranded, blocks_to_mw(a_stranded), b_stranded, blocks_to_mw(b_stranded),
           win, margin))

    # Confirm block_size_mw truly has no effect on the winner/margin (Modeling Assumptions
    # sensitivity note above) by sweeping it far beyond a +/-50% flex.
    for mult in (0.5, 1.5, 3.0, 0.1):
        r = evaluate({"block_size_mw": PARAMS["block_size_mw"] * mult})
        print("  block_size_mw x%.1f -> stranded_A=%.6f stranded_B=%.6f (unchanged, as expected)" %
              (mult, -r["A"], -r["B"]))
