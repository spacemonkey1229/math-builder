"""Sensitivity model for Six Degrees of Exposure (SPEC section 2 balance test,
case-readiness Tier 2 probe 5).

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):
    PARAMS   -- every dial the case STATES
    FLEX     -- the subset that is a genuine, author-chosen ASSUMPTION
    evaluate(params) -> {"A": metric, "B": metric}, higher wins
    (no evaluate_twist(): this case has no twist -- see FACILITATOR.md, which
    ships a trap [per-head vs per-budget] and a sensitivity note, not a twist)

Option A (Operation Hub Sweep) = total edge-weight eliminated by vaccinating
the traced network's real, fixed top-50-by-degree set (Appendix B).
Option B (Operation Wide Net) = *expected* edge-weight eliminated by
vaccinating a uniformly-random 500-person subset of the same 1,899-person
network (Appendix A), found by the counting argument in FACILITATOR.md:
for any fixed edge (i, j), P(neither endpoint is drawn) =
[(n_total-n_wide)(n_total-n_wide-1)] / [n_total(n_total-1)], the same for
every edge regardless of its own weight -- so the expected weight touched is
just total_weight * (1 - that probability).

WHAT IS AND ISN'T IN FLEX -- read this before adding a dial.
Appendix E lists three modeling assumptions (MA1-MA3). Only MA3 (the two
operation headcounts, 50 and 500) is a numeric dial this file can honestly
sweep:
  - MA1 (which real network stands in for Calloway County's own graph) is
    categorical, not a number -- it cannot be flexed +/-50%, and swapping the
    dataset is a different case, not a sensitivity test on this one.
  - MA2 (edge weight = contact-event count, not some other proxy) is, by the
    case's own text, load-bearing to interpretation but NOT to the arithmetic
    -- flexing it changes nothing evaluate() computes, so it is not a
    meaningful dial either.
  - MA3 (n_hub=50, n_wide=500) is the one place the case chose a number
    rather than deriving or citing it (Appendix D's real per-dose costs do
    NOT, at their sourced values, split one shared budget into exactly 50 and
    500 -- see Appendix D's own "discrepancy this case does not hide"). That
    makes it a genuine assumption, not given/cited data -- P6 (data decay)
    covers S1/S2/S3 instead.

n_wide is fully in FLEX: Wide Net's expected-weight formula is exact
closed-form for ANY n_wide from 0 to n_total, so a +/-50% sweep (250 / 750)
is a real, honestly-computable answer.

n_hub is NOT swept, and that is a data-availability limit, not a scoping
choice made for convenience. Appendix B publishes the exact top-50 ranked
list and its exact eliminated weight (27,643, from 5,859 distinct edges) --
but it does not publish the full 13,838-edge list, so there is no way to
compute the exact weight eliminated by a *different*-sized hub set (25 or 75)
without the raw graph this case does not ship. Recomputing it from degree
sums alone would double-count shared edges between top-ranked individuals and
is exactly the kind of fabricated derived number MCS-21/SPEC Sec5 forbid.
hub_weight_50 is therefore treated as a fixed, sourced quantity (S3-derived,
already computed and disclosed in case.md), the same way the reference
model's BOXES_A/BOXES_B counts are structural givens, not PARAMS to flex.

Verified against case.md/case.json:
    base   A = 27643.0  B = 27366.7   margin (A-B)/A ~= 1.0%   (matches case.json margin_pct)
"""

PARAMS = {
    # --- Appendix A, S3 (cited/derived network structure -- NOT flexed) -----
    "n_total": 1899,
    "total_weight": 59835.0,
    # --- Appendix B, S3-derived (the case's own real top-50 result --
    #     NOT flexed; see the module docstring for why it can't be) ----------
    "hub_weight_50": 27643.0,
    # --- Appendix E, MA3 (the one genuine, author-chosen assumption) -------
    "n_hub": 50,
    "n_wide": 500,
}

# Only n_wide is a numeric assumption this case's published data can honestly
# support sweeping. See the module docstring for n_hub's exclusion.
FLEX = ["n_wide"]


def _wide_expected_weight(n_total, total_weight, n_wide):
    """Expected total edge-weight touched by a uniform-random n_wide-person
    draw from an n_total-person network, via the counting argument in
    FACILITATOR.md: P(a given edge survives untouched) is the same for every
    edge regardless of its own weight, so E[weight touched] = total_weight *
    (1 - P(survives))."""
    n_wide = max(0, min(n_total, n_wide))
    if n_total < 2 or n_wide >= n_total:
        return float(total_weight)
    p_survive = ((n_total - n_wide) * (n_total - n_wide - 1)) / (n_total * (n_total - 1))
    return total_weight * (1.0 - p_survive)


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    a = p["hub_weight_50"]
    b = _wide_expected_weight(p["n_total"], p["total_weight"], p["n_wide"])
    return {"A": a, "B": b}


if __name__ == "__main__":
    base = evaluate({})
    margin = 100 * (base["A"] - base["B"]) / base["A"]
    print("base ", {k: round(v, 1) for k, v in base.items()}, "margin %.2f%%" % margin)

    for mult, label in [(0.5, "-50%"), (1.5, "+50%")]:
        n_wide2 = round(PARAMS["n_wide"] * mult)
        r = evaluate({"n_wide": n_wide2})
        winner = "A" if r["A"] > r["B"] else ("B" if r["B"] > r["A"] else "TIE")
        print(f"  n_wide {label:6s} (n_wide={n_wide2:4d}) -> A={r['A']:.1f} B={r['B']:.1f} winner={winner}")
