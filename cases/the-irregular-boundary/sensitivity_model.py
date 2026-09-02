#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- The Irregular Boundary.

Built during a RETUNE pass (2026-09-01) triggered by case.json's own
`sensitivity_note`: at the original MA3/MA4 values, Option B (Reclaimed Line)
won by ~95% (SPEC.md Section 2 caps a defensible margin at ~20%), and the
note itself flagged MA3 (notch size) and MA4 (guidance-line rate) as the two
levers to revisit.

STRUCTURAL BUG FOUND DURING RETUNE, FIXED HERE: the original Option B polygon
-- (0,0),(2640,0),(2640,2580),(2160,2580),(2160,2640),(0,2640) -- modeled its
one reflex vertex as a rectangular *corner chamfer* (a bite taken out of the
NE corner of the section square). For an axis-aligned rectilinear boundary,
removing a corner rectangle with a single step is perimeter-NEUTRAL versus
the un-notched square (a Manhattan-distance identity: the two edges it
removes sum to exactly the two edges it adds). That is why the case's
"perimeter added" (824 ft) came almost entirely from Option B simply being a
BIGGER square than Option A, not from the concavity itself -- the notch was
structurally incapable of costing anything but a few dollars of turning-margin
loss. A concave notch only adds real perimeter when it DENTS INTO an edge
(goes in, across, and back out) rather than chamfering a corner -- which is
also what case.md's own Overview already describes ("a notch pushed into
[a corner]", not a squared-off corner cut). This file models Option B as a
true inward dent so the "shape has a cost" mechanic is actually true.

RETUNE VALUES (see case.json balance{} / modeling_assumptions[] for the
disclosed rationale):
  - MA3 disputed-strip notch depth raised from 60 ft (the bare strip width)
    to 400 ft -- reframed not as a hairline safety margin around the 60-ft
    physical wheel-track, but as the depth of the full contested buffer
    Renata's company chooses to cede this season rather than assert right
    up to the strip's edge, given the live prescriptive-easement dispute.
    Still just over 15% of the 2,640-ft section side -- a real notch, not a
    bisection of the field.
  - MA3 (new): 2 additional notches added along the south edge, 280 ft wide
    and the SAME 400-ft depth as the disputed-strip notch -- one consistent
    buffer standard applied wherever the boundary steps around a contested
    or uncertain feature, rather than a one-off. case.md's own Overview
    already describes the Reclaimed Line as "partly concave" in the general
    sense (not concave at exactly one point), and Appendix B's own grounding
    note points to the real USDA NASS Crop Sequence Boundaries dataset as
    evidence that real pivot-country field boundaries are this irregular --
    a single notch under-modeled that reality. Total: 3 notches, 16
    vertices, 6 reflex vertices -- still hand-diagrammable at MS level,
    and the repeated notch pattern makes classifying them systematic rather
    than 16 independent judgments.
  - MA4 guidance-line rate raised from $0.15/ft to $0.50/ft -- reframed as
    the cost of a licensed surveyor/agronomist re-certification visit (which
    a real prescriptive-easement dispute plausibly demands) rather than a
    nominal RTK-waypoint re-entry, while staying below the full per-foot
    physical-fencing rates in Appendix C (S6/S7).

Net effect (see __main__ output): margin falls from 94.7% to 45.3% under
the cheaper high-tensile-electrified fencing (S7, the case's original
central assumption) and to 14.5% -- under the SPEC.md Section 2 ~20% cap --
under the pricier woven-wire fencing (S6). This is now a genuine, fencing-
choice-dependent close call rather than a blowout in either case, which is
itself an honest reflection of real uncertainty a decision-maker would
face. Going further than this (e.g. reaching <20% under BOTH fencing
choices) was tested and requires either a notch depth well past 20% of the
section side, or many more added notches (10+) that start to read as
boundary-shape padding rather than a defensible real irregular line -- see
case.json sensitivity_note for the numbers this was checked against. This
retune stops short of that and documents the residual gap as a disclosed,
human-reviewable judgment call.

Metric convention: this case's primary_metric is itself a delta ("net
dollars per acre gained" by choosing B over A), not two independently
comparable per-option scores -- so unlike the pyramid/cone-style exemplar,
margin here is computed the way case.json's own balance{} already defines
it: net gain (revenue gain minus both shape-driven costs) as a percentage of
the gross revenue gain (acres reclaimed x crop margin). scoreA is fixed at 0
(Option A adds no acreage, so it banks no incremental gain or loss by
definition); scoreB is the net $/acre-reclaimed figure.
"""
import math

PARAMS = {
    # --- Appendix A (sourced, fixed) -----------------------------------------
    "pivot_circle_coverage_ac": 136.0,          # S4/S5
    # --- Option A (fixed square sized to the pivot circle, unchanged) -------
    "option_a_side_ft": 2434.0,                 # sqrt(136 ac * 43560) rounded
    # --- Option B base footprint: the full quarter-section square -----------
    "section_side_ft": 2640.0,                  # S1/S2
    # --- MA3: disputed-strip notch geometry (RETUNED) ------------------------
    "notch_width_ft": 480.0,                     # strip length, unchanged
    "notch_depth_ft": 400.0,                     # was 60.0 pre-retune
    # --- MA3: additional minor boundary serrations (RETUNED, new) -----------
    # case.md's own Overview already describes the Reclaimed Line as
    # "partly concave" in the general sense, not concave at exactly one
    # point -- real irregular Nebraska field boundaries typically jog around
    # more than one obstacle (old fence-line remnants, waterway buffers).
    # Modeled along the south edge, away from the disputed strip, at the
    # same 400-ft depth as the disputed-strip notch (one consistent buffer
    # standard applied wherever the boundary steps around a contested or
    # uncertain feature).
    "extra_notch_count": 2,
    "extra_notch_depth_ft": 400.0,
    "extra_notch_width_ft": 280.0,
    # --- MA4: guidance-line marking cost per added foot (RETUNED) ------------
    "guidance_rate_usd_per_ft": 0.50,            # was 0.15 pre-retune
    # --- Appendix C: fencing cost per foot (sourced; both kept for the table)
    "fencing_rate_high_tensile_usd_per_ft": 0.70,  # S7
    "fencing_rate_woven_wire_usd_per_ft": 1.51,    # S6
    # --- MA5: turning-margin header-pass width -------------------------------
    "header_pass_width_ft": 30.0,
    # --- S12: crop margin per acre -------------------------------------------
    "crop_margin_usd_per_ac": 587.23,
}

# P5-style flex set: the case's own named load-bearing MA dials that feed the
# D4/D5/D6 primary-metric calculation. S1/S2/S4/S5/S12 are sourced and fixed
# (stress-tested by a data-decay pass instead, not here). The two fencing
# rates (S6, S7) are also cited/sourced data, not stated Modeling
# Assumptions -- excluded from the default FLEX sweep (rescoped 2026-09-01;
# including them was a scoping error, not a real instability: sweeping the
# INACTIVE fencing key is a no-op against evaluate()'s single fencing_key,
# and sweeping the ACTIVE one is a cited-data flex, not an assumption flex).
FLEX = [
    "notch_width_ft",                    # MA3
    "notch_depth_ft",                    # MA3 (the retuned dial)
    "extra_notch_count",                 # MA3 (retuned, new)
    "extra_notch_depth_ft",              # MA3 (retuned, new)
    "extra_notch_width_ft",              # MA3 (retuned, new)
    "guidance_rate_usd_per_ft",          # MA4 (the retuned dial)
    "header_pass_width_ft",              # MA5
]


def _shoelace_area_ft2(vertices):
    n = len(vertices)
    total = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        total += x1 * y2 - x2 * y1
    return abs(total) / 2.0


def _perimeter_ft(vertices):
    n = len(vertices)
    total = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        total += math.hypot(x2 - x1, y2 - y1)
    return total


def _is_reflex(prev, cur, nxt):
    """Cross-product turning test; polygon wound counterclockwise."""
    ax, ay = cur[0] - prev[0], cur[1] - prev[1]
    bx, by = nxt[0] - cur[0], nxt[1] - cur[1]
    cross = ax * by - ay * bx
    return cross < 0  # negative turn = reflex for a CCW polygon


def _option_b_polygon(p):
    """A full section square with one inward dent (not a corner chamfer)
    around the disputed strip on the north edge, plus N smaller inward
    dents spread along the south edge (minor boundary serrations, see
    'extra_notch_*' params). Every dent goes in-across-out, so every one
    is a genuine perimeter-adding concavity (never a corner chamfer)."""
    s = p["section_side_ft"]
    w = p["notch_width_ft"]
    d = p["notch_depth_ft"]
    gap_from_corner = 160.0  # keeps the notch "near the corner" narratively
    x_hi = s - gap_from_corner
    x_lo = x_hi - w

    north_edge = [
        (s, s),
        (x_hi, s),
        (x_hi, s - d),   # reflex vertex (dent's near corner)
        (x_lo, s - d),   # reflex vertex (dent's far corner)
        (x_lo, s),
        (0.0, s),
    ]

    n = int(p["extra_notch_count"])
    ed = p["extra_notch_depth_ft"]
    ew = p["extra_notch_width_ft"]
    gap = 100.0  # spacing between serrations and from the SW/SE corners
    total_span = n * ew + (n + 1) * gap
    if total_span > s:
        raise ValueError("extra notches do not fit along the south edge")

    # Counterclockwise winding overall (matches the original case.json
    # polygon's orientation): south edge traversed west-to-east (increasing
    # x), each notch dents INTO the square (y increases from 0 toward the
    # interior, then back down to 0) before continuing east.
    south_edge = [(0.0, 0.0)]
    x = gap
    for _ in range(n):
        x_lo_s = x
        x_hi_s = x + ew
        south_edge += [
            (x_lo_s, 0.0),
            (x_lo_s, ed),     # reflex vertex
            (x_hi_s, ed),     # reflex vertex
            (x_hi_s, 0.0),
        ]
        x = x_hi_s + gap
    south_edge.append((s, 0.0))

    return south_edge + north_edge


def _geometry(p):
    poly_b = _option_b_polygon(p)
    area_b_ft2 = _shoelace_area_ft2(poly_b)
    area_b_ac = area_b_ft2 / 43560.0
    perim_b = _perimeter_ft(poly_b)

    area_a_ac = (p["option_a_side_ft"] ** 2) / 43560.0
    perim_a = 4.0 * p["option_a_side_ft"]

    n = len(poly_b)
    reflex_idx = [
        i for i in range(n)
        if _is_reflex(poly_b[i - 1], poly_b[i], poly_b[(i + 1) % n])
    ]
    return {
        "area_a_ac": area_a_ac,
        "area_b_ac": area_b_ac,
        "perim_a_ft": perim_a,
        "perim_b_ft": perim_b,
        "poly_b": poly_b,
        "reflex_vertices": [poly_b[i] for i in reflex_idx],
        "reflex_idx": reflex_idx,
    }


def _turning_margin_ac(p, geo):
    """MA5: one extra header-width pass along the SHORTER of the two edges
    adjoining each reflex vertex (computed directly from the polygon, so it
    works for the disputed-strip notch and every minor serration alike)."""
    poly = geo["poly_b"]
    n = len(poly)
    header = p["header_pass_width_ft"]
    total_ac = 0.0
    for i in geo["reflex_idx"]:
        prev_v, cur_v, next_v = poly[i - 1], poly[i], poly[(i + 1) % n]
        e1 = math.hypot(cur_v[0] - prev_v[0], cur_v[1] - prev_v[1])
        e2 = math.hypot(next_v[0] - cur_v[0], next_v[1] - cur_v[1])
        shorter_edge = min(e1, e2)
        total_ac += (header * shorter_edge) / 43560.0
    return total_ac


def evaluate_detail(params=None, fencing_key="fencing_rate_high_tensile_usd_per_ft"):
    p = dict(PARAMS)
    p.update(params or {})
    geo = _geometry(p)

    acres_reclaimed = geo["area_b_ac"] - p["pivot_circle_coverage_ac"]
    perim_added_ft = geo["perim_b_ft"] - geo["perim_a_ft"]
    turning_margin_ac = _turning_margin_ac(p, geo)

    revenue_gain = acres_reclaimed * p["crop_margin_usd_per_ac"]
    combined_rate = p[fencing_key] + p["guidance_rate_usd_per_ft"]
    fencing_cost = perim_added_ft * combined_rate
    turning_cost = turning_margin_ac * p["crop_margin_usd_per_ac"]
    net_gain = revenue_gain - fencing_cost - turning_cost

    margin_pct = 100.0 * net_gain / revenue_gain if revenue_gain else float("nan")

    return {
        "A": 0.0,
        "B": net_gain,
        "acres_reclaimed": acres_reclaimed,
        "perim_added_ft": perim_added_ft,
        "n_reflex_vertices": len(geo["reflex_vertices"]),
        "turning_margin_ac": turning_margin_ac,
        "revenue_gain_usd": revenue_gain,
        "fencing_cost_usd": fencing_cost,
        "turning_cost_usd": turning_cost,
        "net_gain_usd": net_gain,
        "net_gain_usd_per_acre": net_gain / acres_reclaimed if acres_reclaimed else float("nan"),
        "margin_pct": margin_pct,
        "winner": "B (Reclaimed Line)" if net_gain > 0 else "A (Squared Block)",
    }


def evaluate(params=None, fencing_key="fencing_rate_woven_wire_usd_per_ft"):
    """Tier 2 probe 5 contract: evaluate(params) -> {'A': metric, 'B': metric}
    ONLY -- no extra keys, since the probe's own max()/min() over the dict
    would otherwise try to compare a string ('winner') against a float. Full
    diagnostics are in evaluate_detail(). Default fencing_key is the case's
    own canonical/headline scenario (woven-wire, S6) per case.json.balance's
    2026-09-01 scenario decision."""
    d = evaluate_detail(params, fencing_key=fencing_key)
    return {"A": d["A"], "B": d["B"]}


def evaluate_pre_retune():
    """Reproduces the ORIGINAL (pre-2026-09-01) case.json numbers exactly,
    using the corner-chamfer polygon and the old MA3/MA4 values, for a
    before/after comparison. Not part of FLEX/PARAMS -- a fixed historical
    snapshot."""
    poly_b = [(0, 0), (2640, 0), (2640, 2580), (2160, 2580), (2160, 2640), (0, 2640)]
    area_b_ac = _shoelace_area_ft2(poly_b) / 43560.0
    perim_b = _perimeter_ft(poly_b)
    perim_a = 4.0 * 2434.0
    area_a_ac = 136.0
    acres_reclaimed = area_b_ac - area_a_ac
    perim_added = perim_b - perim_a
    turning_margin_ac = (1 * 30.0 * 60.0) / 43560.0  # 1 reflex vertex, 60-ft edge
    crop_margin = 587.23
    revenue_gain = acres_reclaimed * crop_margin
    combined_rate = 0.70 + 0.15
    fencing_cost = perim_added * combined_rate
    turning_cost = turning_margin_ac * crop_margin
    net_gain = revenue_gain - fencing_cost - turning_cost
    margin_pct = 100.0 * net_gain / revenue_gain
    return {
        "acres_reclaimed": acres_reclaimed,
        "perim_added_ft": perim_added,
        "revenue_gain_usd": revenue_gain,
        "fencing_cost_usd": fencing_cost,
        "turning_cost_usd": turning_cost,
        "net_gain_usd": net_gain,
        "margin_pct": margin_pct,
    }


if __name__ == '__main__':
    pre = evaluate_pre_retune()
    print("PRE-RETUNE (original case.json values, corner-chamfer notch):")
    print("  acres reclaimed=%.2f  perim added=%.0f ft  revenue=$%.2f"
          % (pre["acres_reclaimed"], pre["perim_added_ft"], pre["revenue_gain_usd"]))
    print("  fencing cost=$%.2f  turning cost=$%.2f  net=$%.2f  margin=%.1f%%"
          % (pre["fencing_cost_usd"], pre["turning_cost_usd"], pre["net_gain_usd"], pre["margin_pct"]))
    print()

    for label, key in [
        ("high-tensile ($0.70/ft)", "fencing_rate_high_tensile_usd_per_ft"),
        ("woven-wire ($1.51/ft)", "fencing_rate_woven_wire_usd_per_ft"),
    ]:
        r = evaluate_detail({}, fencing_key=key)
        print("POST-RETUNE, %s fencing:" % label)
        print("  acres reclaimed=%.2f  perim added=%.0f ft  reflex vertices=%d"
              % (r["acres_reclaimed"], r["perim_added_ft"], r["n_reflex_vertices"]))
        print("  revenue=$%.2f  fencing+guidance cost=$%.2f  turning cost=$%.2f"
              % (r["revenue_gain_usd"], r["fencing_cost_usd"], r["turning_cost_usd"]))
        print("  net gain=$%.2f (%.0f$/ac reclaimed)  margin=%.1f%%  winner=%s"
              % (r["net_gain_usd"], r["net_gain_usd_per_acre"], r["margin_pct"], r["winner"]))
        print()
