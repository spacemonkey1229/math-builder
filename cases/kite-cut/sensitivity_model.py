#!/usr/bin/env python3
"""
Sensitivity model — Kite Cut.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           subset of PARAMS Tier 2 probe 5 perturbs
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

evaluate() computes the case's graded primary metric -- total material cost per kite -- for
each frame option, from Appendix A's stated geometry (crossing points), Appendix B's sourced
pricing (fabric $7.95/yd @ 60in wide [S5]; fiberglass rod $3.75/48in [S2]), and Appendix E's
three stated modeling assumptions (MA1 tail-length multiplier, MA2 tail width, MA3 the Option-B
cutting-layout efficiency). Because LOWER material cost is better, evaluate() returns the
*negative* of the per-kite cost so the "higher is better" convention still holds.

Verified against case.json's `derived` block:
    base   A = -12.005  B = -12.270   margin  2.21%  (A wins, cheaper total material cost)
"""
import math

PARAMS = {
    # --- Appendix A: the shop's own stated design (not sourced; geometry only) --
    "height_in": 36.0,
    "width_in": 36.0,
    "crossing_pct_a": 0.50,   # The True Diamond -- crossing bisects the spine
    "crossing_pct_b": 0.19,   # The Eddy Flyer -- sourced (S3)
    # --- Appendix B: sourced pricing -------------------------------------------
    "fabric_price_per_yd_usd": 7.95,   # S5
    "fabric_roll_width_in": 60.0,      # S5
    "rod_price_usd": 3.75,             # S2
    "rods_per_kite": 2,
    # --- Appendix D: the festival's own order size ------------------------------
    "run_size": 250,
    # --- Appendix E: stated modeling assumptions ---------------------------------
    "tail_len_mult": 4.0,      # MA1 -- multiple of kite height
    "tail_width_in": 4.0,      # MA2
    "b_layout_waste_mult": 2.0,  # MA3 -- Option B's fabric use as a multiple of raw sail area
                                  # (1.0 = same as Option A's zero-waste pairing;
                                  #  2.0 = fully individually-boxed, this case's stated value)
}

# Only the three stated assumptions are swept by Probe 5. The geometry/pricing/run-size dials
# above are given/cited data, not assumptions the case author chose.
FLEX = [
    "tail_len_mult",        # Appendix E, MA1
    "tail_width_in",        # Appendix E, MA2
    "b_layout_waste_mult",  # Appendix E, MA3 -- the case's most sensitive dial
]


def _geometry(p):
    H, W = p["height_in"], p["width_in"]
    # Sail area is identical for both options: Area = d1 x d2 / 2, independent of crossing point,
    # as long as the diagonals are perpendicular (true by construction in both options).
    sail_area = H * W / 2.0

    fabric_price_per_sqin = p["fabric_price_per_yd_usd"] / (36.0 * p["fabric_roll_width_in"])

    # Option A: proven zero-waste parallelogram pairing (D3) -- fabric used = raw sail area.
    a_sail_fabric = sail_area
    # Option B: MA3's stated layout efficiency, relative to Option A's zero-waste case.
    b_sail_fabric = sail_area * p["b_layout_waste_mult"]

    # Tail (Option A only; Option B is tailless per S3/S4).
    tail_len = p["tail_len_mult"] * H
    tail_area = tail_len * p["tail_width_in"]

    a_total_fabric = a_sail_fabric + tail_area
    b_total_fabric = b_sail_fabric

    a_fabric_cost = a_total_fabric * fabric_price_per_sqin
    b_fabric_cost = b_total_fabric * fabric_price_per_sqin

    rod_cost = p["rods_per_kite"] * p["rod_price_usd"]  # identical for both options

    a_total_cost = a_fabric_cost + rod_cost
    b_total_cost = b_fabric_cost + rod_cost

    return {
        "sail_area": sail_area,
        "a_total_fabric": a_total_fabric, "b_total_fabric": b_total_fabric,
        "a_fabric_cost": a_fabric_cost, "b_fabric_cost": b_fabric_cost,
        "rod_cost": rod_cost,
        "a_total_cost": a_total_cost, "b_total_cost": b_total_cost,
    }


def evaluate(params=None):
    """Graded primary metric: total material cost per kite, negated (higher = better)."""
    p = dict(PARAMS); p.update(params or {})
    g = _geometry(p)
    return {"A": -g["a_total_cost"], "B": -g["b_total_cost"]}


def evaluate_twist(params=None):
    """Optional what-if, not a scripted narrative Twist (FACILITATOR.md declares
    Twist: N/A for this case). Applies a single override -- a shop that researches
    and finds a more efficient interlocking cut for Option B's kite-shaped panels,
    cutting its layout waste multiplier from the stated 2.0x down to 1.5x -- and
    recomputes both totals the same way evaluate() does. This is exactly the kind
    of research move Appendix H and MA3's own sensitivity note point a Hero toward;
    it is surfaced in the Interactive HTML as an optional "what if" toggle, not a
    gated narrative reveal."""
    p = dict(PARAMS); p.update(params or {})
    p["b_layout_waste_mult"] = 1.5
    return evaluate(p)


if __name__ == '__main__':
    base = evaluate({})

    def _report(d, label):
        lo, hi = min(d, key=d.get), max(d, key=d.get)
        margin = 100 * (d[hi] - d[lo]) / abs(d[lo]) if d[lo] else float('nan')
        print(f"{label:6s} A={d['A']:.4f}  B={d['B']:.4f}  winner={hi}  margin={margin:.2f}%")

    _report(base, "base")

    g = _geometry(PARAMS)
    print(f"sail_area={g['sail_area']:.2f} sqin  a_fabric={g['a_total_fabric']:.2f}  "
          f"b_fabric={g['b_total_fabric']:.2f}")
    print(f"a_total_cost=${g['a_total_cost']:.3f}/kite  b_total_cost=${g['b_total_cost']:.3f}/kite")
    print(f"run_total_a=${g['a_total_cost']*PARAMS['run_size']:.2f}  "
          f"run_total_b=${g['b_total_cost']*PARAMS['run_size']:.2f}")

    # Probe: how far would MA3 (b_layout_waste_mult) have to move for B to win?
    # B wins at low multipliers (less waste), loses at high ones -- find the crossover.
    lo, hi = 1.0, 3.0
    for i in range(200):
        mid = (lo + hi) / 2.0
        r = evaluate({"b_layout_waste_mult": mid})
        if r["B"] > r["A"]:
            lo = mid   # B still winning here -- push the search window up
        else:
            hi = mid   # A winning here -- push the search window down
    print(f"MA3 flip point (b_layout_waste_mult): ~{lo:.4f} "
          f"(stated case value is 2.0 -- B needs a layout using <= {lo:.2f}x raw sail area to win)")
