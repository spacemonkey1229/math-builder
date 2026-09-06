"""
sensitivity_model.py -- The Overlap Send

Graded primary metric (case.json.primary_metric): expected net revenue per campaign
send (reach x conversion rate x average order value, minus total send cost), comparing
Option A (Cast The Net, mail P union L) against Option B (Mail The Middle, mail P
intersect L). Higher expected net revenue is better for Jess, so evaluate() returns
each option's expected net revenue directly -- higher score = better ("higher wins"
convention, same as cases/the-deferred-repair/sensitivity_model.py).

    reach(A) = P + L - (P intersect L)                     (inclusion-exclusion, Appendix A)
    reach(B) = P intersect L                                (Appendix A)
    ENR(option) = reach(option) x conversion_rate(option) x AOV - reach(option) x per_recipient_cost

conversion_rate(A) [S1, Klaviyo 2026 benchmark, broad "campaign" placed-order rate] is a
real, sourced, HIGH-confidence figure -- NOT flexed by default (cited data, stress-tested
by P6 instead). Every other quantity below (list sizes P/L/overlap, per-recipient cost,
the intersection segment's conversion rate, and AOV) is a stated Modeling Assumption --
see case.json.modeling_assumptions[MA1, MA2, MA4, MA5] and RESEARCH_LOG.md; none of these
figures exists as a citable external dataset. FLEX below sweeps exactly these five and
nothing else.

Verified against case.json.balance / FACILITATOR.md's margin arithmetic:
    base   A = $1,741.68  ·  B = $1,987.20  ·  margin 14.1%  (B wins -- matches case.json)
"""

PARAMS = {
    # --- Appendix A, Modeling Assumption MA1 -- CRM list sizes and overlap. Not
    #     published anywhere (no company publishes its own internal CRM data) --
    #     see RESEARCH_LOG.md.
    "p_size": 21400.0,
    "l_size": 38600.0,
    "p_and_l": 6900.0,
    # --- Appendix B, Modeling Assumption MA2 -- flat per-recipient send cost.
    "per_recipient_cost": 0.06,
    # --- Appendix C [S1], sourced, HIGH confidence -- broad ("campaign") placed-order
    #     rate. NOT in FLEX (cited data; P6 stress-tests sources instead).
    "conv_broad": 0.0016,
    # --- Appendix C, Modeling Assumption MA4 -- the case's own load-bearing,
    #     dilemma-flipping dial. No source measures this exact segment; informed
    #     by S1/S2/S3 (see RESEARCH_LOG.md) but authored, not cited.
    "conv_intersection": 0.006,
    # --- Appendix C, Modeling Assumption MA5 -- average order value.
    "aov": 58.0,
}

# Only the five genuine Modeling Assumptions are swept by default (SPEC §2 asks for
# sensitivity to STATED ASSUMPTIONS, not cited measurements). conv_broad is a real,
# sourced Klaviyo figure [S1] -- halving a published benchmark is a different case,
# not a sensitivity test on this case's own authored assumptions. Run with
# --flex-all to sweep conv_broad too.
FLEX = ["p_size", "l_size", "p_and_l", "per_recipient_cost", "conv_intersection", "aov"]


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    union = p["p_size"] + p["l_size"] - p["p_and_l"]
    intersection = p["p_and_l"]
    enr_a = union * p["conv_broad"] * p["aov"] - union * p["per_recipient_cost"]
    enr_b = intersection * p["conv_intersection"] * p["aov"] - intersection * p["per_recipient_cost"]
    return {"A": enr_a, "B": enr_b}


if __name__ == '__main__':
    base = evaluate({})
    a, b = base["A"], base["B"]
    win = "A" if a > b else "B"
    lo, hi = min(a, b), max(a, b)
    margin = 100.0 * (hi - lo) / hi
    print("base A=$%.2f  B=$%.2f  winner=%s  margin=%.1f%%" % (a, b, win, margin))

    print("\n--- +/-50%% flex sweep (FLEX[] only) ---")
    for name in FLEX:
        base_val = PARAMS[name]
        for label, mult in (("-50%", 0.5), ("+50%", 1.5)):
            flexed = evaluate({name: base_val * mult})
            fa, fb = flexed["A"], flexed["B"]
            fwin = "A" if fa > fb else "B"
            flo, fhi = min(fa, fb), max(fa, fb)
            fmargin = 100.0 * (fhi - flo) / fhi if fhi else 0.0
            flip = " <<< FLIPS" if fwin != win else ""
            cap = " (breaks 20% cap)" if fmargin > 20 else ""
            print("  %-20s %-5s -> A=$%.2f B=$%.2f winner=%s margin=%.1f%%%s%s" %
                  (name, label, fa, fb, fwin, fmargin, flip, cap))
