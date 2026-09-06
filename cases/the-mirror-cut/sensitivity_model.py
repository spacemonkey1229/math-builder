#!/usr/bin/env python3
"""
Sensitivity model -- The Mirror Cut.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     optional; same shape, with the twist applied

Option A = The Mirror Cut (mirrored/nested layout).
Option B = The Straight Run (simple, repeated layout).

evaluate() computes the case's graded primary metric -- net cost per finished
part (material cost + machine-time cost combined) -- for each layout, from:
  - Appendix B: the bracket's own stated coordinate geometry (not an
    assumption -- the part is Sam's own stated design, exactly like Roofline
    Call's footprint/pitch).
  - Appendix C: sourced sheet size, sheet weight-per-area and steel price
    (S1, S2).
  - Appendix D: sourced cutting speed and pierce-time ranges, and the sourced
    material-yield improvement of mirrored nesting (S3, S4, S6), combined
    with a machine rate built from two sourced hourly figures (S5, S7).
  - Appendix E: two stated Modeling Assumptions (MA1 pierce-count multiplier,
    MA2 cutting-speed multiplier) that make the Mirrored layout's machine
    time cost MORE per part than the Straight Run's, even though the
    Mirrored layout uses LESS material per part. Because higher net cost is
    worse, evaluate() returns the *negative* of net cost per part so the
    "higher is better" convention holds.

Because a competitor's naive read of the sourced 10-15% material-yield
number would predict a similarly large NET savings, the graded metric
deliberately does NOT simply track that number -- MA1/MA2 tax the mirrored
layout's machine time, eroding (but not reversing) the material win. That
erosion, not a full flip, is the case's real trap: yield percent is not the
same thing as net-cost-per-part percent.

evaluate_twist() computes the metric a supervisor would actually care about
once the customer's inspection contract is factored in: a mirrored,
tightly-nested layout carries a higher rejected-part rate from heat-affected-
zone distortion (a real, sourced, general phenomenon -- see Appendix F. The
specific reject-rate values are themselves a third Modeling Assumption, MA3,
because no public per-shop reject-rate study exists for this exact
geometry). Good-part cost = raw cost / (1 - reject_rate). Same sign
convention: lower is better, so the function returns the negative.
"""
import math

PARAMS = {
    # --- Appendix B: the bracket's own stated coordinate design, not an
    #     assumption (Sam's own part, like Roofline Call's footprint/pitch) -
    "vA_x": 0.0, "vA_y": 0.0,
    "vB_x": 6.0, "vB_y": 0.0,
    "vC_x": 4.5, "vC_y": 4.0,
    "vD_x": 1.5, "vD_y": 4.0,
    # --- Appendix C: sourced sheet + price -----------------------------
    "sheet_width_in": 48.0,
    "sheet_length_in": 120.0,
    "slot_margin_in": 0.25,          # kerf/handling spacing added per side
    "weight_per_sqin_lb": 2.448 / 144.0,   # S1 speedymetals.com, 16ga CRS
    "price_per_lb_usd": 2.94,              # S1 speedymetals.com, 16ga CRS
    # --- Appendix D: sourced cutting/piercing + yield ------------------
    "cut_speed_in_per_min_simple": 25.0 * 39.3701,  # S3 stylecnc.com (25 m/min)
    "pierce_time_s": 0.3,                            # S4 kasulaser.com (low end)
    "yield_gain": 0.12,                              # S6 sltl.com (10-15%, picked 12%)
    "wage_usd_per_hr": 22.94,                        # S5 BLS OOH (May 2025)
    "machine_op_usd_per_hr": 7.00,                   # S7 arcuscnc.com (O2/CS, 6kW)
    # --- Appendix E: stated modeling assumptions (MA1 / MA2 / MA3) -----
    "mirrored_pierce_mult": 2.0,     # MA1: pierces per part, mirrored vs 1 simple
    "mirrored_speed_mult": 0.70,     # MA2: mirrored cut speed as a fraction of simple
    "reject_rate_simple": 0.01,      # MA3: Straight Run reject rate
    "reject_rate_mirrored": 0.04,    # MA3: Mirror Cut reject rate
}

# Only the three stated assumptions are swept by Probe 5. The coordinates,
# sheet/price/speed/wage/yield dials above are the part's own stated design
# or given/cited data, not assumptions the case author chose -- per the
# "Only FLEX[] is swept" rule (case-readiness SKILL.md, Tier 2 P5).
FLEX = [
    "mirrored_pierce_mult",   # Appendix E, MA1
    "mirrored_speed_mult",    # Appendix E, MA2
    "reject_rate_simple",     # Appendix E, MA3 (twist only)
    "reject_rate_mirrored",   # Appendix E, MA3 (twist only)
]


def _part_geometry(p):
    """Perimeter and area of the bracket outline from its own stated
    coordinates (Appendix B) -- shoelace area, edge-length perimeter."""
    pts = [(p["vA_x"], p["vA_y"]), (p["vB_x"], p["vB_y"]),
           (p["vC_x"], p["vC_y"]), (p["vD_x"], p["vD_y"])]
    area2 = 0.0
    perim = 0.0
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        area2 += x1 * y2 - x2 * y1
        perim += math.hypot(x2 - x1, y2 - y1)
    area = abs(area2) / 2.0
    width = max(x for x, _ in pts) - min(x for x, _ in pts)
    height = max(y for _, y in pts) - min(y for _, y in pts)
    return {"area_sqin": area, "perimeter_in": perim,
            "bbox_w_in": width, "bbox_h_in": height}


def _nesting(p):
    g = _part_geometry(p)
    slot_w = g["bbox_w_in"] + p["slot_margin_in"]
    slot_h = g["bbox_h_in"] + p["slot_margin_in"]
    cols = math.floor(p["sheet_width_in"] / slot_w)
    rows = math.floor(p["sheet_length_in"] / slot_h)
    parts_simple = cols * rows
    parts_mirrored = math.floor(parts_simple * (1.0 + p["yield_gain"]))

    sheet_area = p["sheet_width_in"] * p["sheet_length_in"]
    sheet_weight_lb = sheet_area * p["weight_per_sqin_lb"]
    sheet_material_cost = sheet_weight_lb * p["price_per_lb_usd"]

    return {
        "geom": g,
        "parts_simple": parts_simple,
        "parts_mirrored": parts_mirrored,
        "sheet_material_cost_usd": sheet_material_cost,
        "mat_cost_per_part_simple": sheet_material_cost / parts_simple,
        "mat_cost_per_part_mirrored": sheet_material_cost / parts_mirrored,
    }


def _machine_cost_per_part(p, g, pierce_mult, speed_mult):
    rate_usd_per_s = (p["wage_usd_per_hr"] + p["machine_op_usd_per_hr"]) / 3600.0
    speed_in_per_s = (p["cut_speed_in_per_min_simple"] * speed_mult) / 60.0
    cut_time_s = g["perimeter_in"] / speed_in_per_s
    pierce_time_s = p["pierce_time_s"] * pierce_mult
    total_time_s = cut_time_s + pierce_time_s
    return total_time_s * rate_usd_per_s


def evaluate(params=None):
    """Graded primary metric: net cost per finished part (material +
    machine time), negated (higher = better). A = Mirror Cut, B = Straight
    Run."""
    p = dict(PARAMS); p.update(params or {})
    n = _nesting(p)
    g = n["geom"]

    labor_b = _machine_cost_per_part(p, g, pierce_mult=1.0, speed_mult=1.0)
    labor_a = _machine_cost_per_part(p, g, pierce_mult=p["mirrored_pierce_mult"],
                                      speed_mult=p["mirrored_speed_mult"])

    net_b = n["mat_cost_per_part_simple"] + labor_b
    net_a = n["mat_cost_per_part_mirrored"] + labor_a

    return {"A": -net_a, "B": -net_b}


def evaluate_twist(params=None):
    """Supplementary metric revealed by the twist: net cost per GOOD part,
    once each layout's reject rate (MA3, heat-distortion risk) is applied.
    Same sign convention: lower cost is better, so the function returns the
    negative."""
    p = dict(PARAMS); p.update(params or {})
    base = evaluate(p)
    net_a = -base["A"]
    net_b = -base["B"]
    good_a = net_a / (1.0 - p["reject_rate_mirrored"])
    good_b = net_b / (1.0 - p["reject_rate_simple"])
    return {"A": -good_a, "B": -good_b}


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})

    def _report(d, label):
        lo, hi = min(d, key=d.get), max(d, key=d.get)
        margin = 100 * (d[hi] - d[lo]) / abs(d[lo]) if d[lo] else float('nan')
        print(f"{label:6s} A={d['A']:.5f}  B={d['B']:.5f}  winner={hi}  margin={margin:.3f}%")

    _report(base, "base")
    _report(tw, "twist")

    n = _nesting(PARAMS)
    g = n["geom"]
    print("\n--- diagnostics ---")
    print("area_sqin", round(g["area_sqin"], 4), "perimeter_in", round(g["perimeter_in"], 4))
    print("parts_simple", n["parts_simple"], "parts_mirrored", n["parts_mirrored"])
    print("sheet_material_cost_usd", round(n["sheet_material_cost_usd"], 4))
    print("mat/part simple", round(n["mat_cost_per_part_simple"], 5),
          "mat/part mirrored", round(n["mat_cost_per_part_mirrored"], 5))
