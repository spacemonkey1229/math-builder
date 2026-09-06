#!/usr/bin/env python3
"""
Sensitivity model -- The Custom Die.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS                     dict[str, number]   every dial the case STATES
    FLEX                       list[str]           the subset that is an ASSUMPTION
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     optional; same shape, with the twist applied

The case's graded primary metric is square inches of cardboard NET per cubic inch
of Wedge actually shipped, tooling-amortized: for each option, take the net's own
surface area (Appendix D-priced material, NOT the box's interior volume -- that
distinction is the case's own trap), add the one-time die cost converted into an
equivalent quantity of cardboard (dividing the die's dollar cost by the real,
sourced price-per-square-inch, then spreading that across the expected order
volume before the next re-tooling decision), and divide the whole thing by The
Wedge's own fixed volume (27 cubic inches, identical for both options since it's
the same pastry either way).

Because FEWER square inches per cubic inch is the better outcome, evaluate()
returns the *negative* of that figure so the "higher is better" convention still
holds -- the option with the smaller effective footprint legitimately returns the
larger (less negative) number.

Appendix E's three modeling assumptions (MA1 the simple-die cost, MA2 the
complex-die cost, MA3 the amortization volume) ARE the FLEX set -- these are the
values Marcus's team had to choose with no public per-company die quote or a
locked-in order volume to point to. The cardboard price (Appendix D, sourced S1)
and every geometric dimension (Appendix B/C, the case's own stated product and
box design) are NOT flexed -- they are given/cited data, not assumptions, per the
"Only FLEX[] is swept" rule in case-readiness's Tier 2 probe 5.

evaluate_twist() recomputes the same metric after the Twist lands: the "trial"
order volume MA3 stated (12,000 units) turns out to be wrong -- the retail buyer
signed Marcus's employer to a 40,000-unit annual purchase order, not a one-off
run. Spreading either die's cost over a much larger volume favors whichever
option has the smaller *material* footprint once tooling stops dominating -- see
FACILITATOR.md.

Verified against case.json's `derived` block (Appendix D price $2.37/sheet, re-verified 2026-09-06):
    base   A=-4.297996  B=-4.591272   winner A   margin  6.39%  (cheap die still wins at 12,000 units)
    twist  A=-3.943565  B=-3.449219   winner B   margin 12.54%  (fitted wedge wins once volume is 40,000 units)
"""
import math

PARAMS = {
    # --- Appendix B: the bakery's own stated product design, not sourced -----
    "leg1_in": 3.00,
    "leg2_in": 3.00,
    "length_in": 6.00,
    # --- Appendix C: the packaging team's own stated clearance convention ----
    "clearance_in": 0.25,
    # --- Appendix D: sourced (S1) ---------------------------------------------
    "price_per_sheet_usd": 2.37,
    "sheet_area_sqin": 24.0 * 36.0,
    # --- Appendix E: stated modeling assumptions (MA1 / MA2 / MA3) -----------
    "tooling_a_usd": 450.0,
    "tooling_b_usd": 1450.0,
    "order_volume_units": 12000.0,
    # --- Twist: the true order volume once the annual contract lands ---------
    "twist_order_volume_units": 40000.0,
}

# Only the three stated assumptions are swept by Probe 5. The product/box
# geometry and the sourced cardboard price are given/cited data, not
# assumptions the case author chose -- per the "Only FLEX[] is swept" rule
# (case-readiness SKILL.md, Tier 2 P5).
FLEX = [
    "tooling_a_usd",        # Appendix E, MA1
    "tooling_b_usd",        # Appendix E, MA2
    "order_volume_units",   # Appendix E, MA3
]


def _geometry(p):
    leg1, leg2, length, c = p["leg1_in"], p["leg2_in"], p["length_in"], p["clearance_in"]
    vol_product = 0.5 * leg1 * leg2 * length

    # Option A -- rectangular prism, interior = bounding box + clearance
    LA = length + c
    WA = leg1 + c
    DA = leg2 + c
    vol_a = LA * WA * DA
    sa_a = 2 * (LA * WA + LA * DA + WA * DA)

    # Option B -- triangular prism, interior legs/length = product dims + clearance
    l1 = leg1 + c
    l2 = leg2 + c
    Lb = length + c
    hyp = math.sqrt(l1 ** 2 + l2 ** 2)
    vol_b = 0.5 * l1 * l2 * Lb
    sa_b = 2 * (0.5 * l1 * l2) + (l1 + l2 + hyp) * Lb

    price_per_sqin = p["price_per_sheet_usd"] / p["sheet_area_sqin"]

    return {
        "vol_product": vol_product,
        "vol_a": vol_a, "vol_b": vol_b,
        "sa_a": sa_a, "sa_b": sa_b,
        "price_per_sqin": price_per_sqin,
        "hyp_b_in": hyp,
    }


def _metric(p, volume_key):
    g = _geometry(p)
    V = p[volume_key]
    eff_a = g["sa_a"] + p["tooling_a_usd"] / g["price_per_sqin"] / V
    eff_b = g["sa_b"] + p["tooling_b_usd"] / g["price_per_sqin"] / V
    return {
        "A": eff_a / g["vol_product"],
        "B": eff_b / g["vol_product"],
    }


def evaluate(params=None):
    """Graded primary metric: net sq in per cu in, tooling-amortized, negated."""
    p = dict(PARAMS); p.update(params or {})
    m = _metric(p, "order_volume_units")
    return {"A": -m["A"], "B": -m["B"]}


def evaluate_twist(params=None):
    """Same metric, recomputed at the Twist's revealed order volume."""
    p = dict(PARAMS); p.update(params or {})
    m = _metric(p, "twist_order_volume_units")
    return {"A": -m["A"], "B": -m["B"]}


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})

    def _report(d, label):
        lo, hi = min(d, key=d.get), max(d, key=d.get)
        margin = 100 * (d[hi] - d[lo]) / abs(d[lo]) if d[lo] else float('nan')
        print(f"{label:6s} A={d['A']:.6f}  B={d['B']:.6f}  winner={hi}  margin={margin:.2f}%")

    _report(base, "base")
    _report(tw, "twist")
