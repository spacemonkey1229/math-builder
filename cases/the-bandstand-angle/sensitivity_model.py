#!/usr/bin/env python3
"""
Sensitivity model -- The Bandstand Angle.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     optional; same shape, with the twist applied

evaluate() computes the case's graded primary metric -- total covered square
footage delivered per dollar of frame material + fabrication labor + site-prep
cost -- for each roof-frame option:

  Option A, "The Even Eight": a regular octagon frame. All 8 hip rafters run
  from a vertex to the frame's center at the SAME plan-view distance (the
  circumradius), so all 8 hip rafters are identical in run, rise, and length.
  This buys simple, repeated (batch) fabrication, but the regular shape must
  fit inside the tightest constraint of the buildable envelope, so it covers
  less ground.

  Option B, "The Site Six": an irregular hexagon fit to the corner lot's
  actual boundary. Each of the 6 vertices sits at a DIFFERENT plan-view
  distance from the frame's center, so all 6 hip rafters have different runs,
  rises, and lengths -- no batch pattern, one template and test-fit per piece.
  This buys more covered footprint (it hugs the real boundary instead of the
  worst-case corner a regular shape must clear), at a real fabrication-labor
  and site-prep-mix premium.

Every figure in PARAMS is either sourced (S1 lumber price, S2 carpenter wage)
or a stated Modeling Assumption (MA1 site geometry -- NOT flexed, it is the
scenario itself, not an uncertain dial; MA2 simple-cut time; MA3 custom-cut
premium; MA4/MA5 site-prep rates). Only MA2-MA5 are swept by Probe 5 -- see
FLEX below. MA1's geometry (envelope apothem, hexagon side lengths and vertex
radii, footprint areas, 5 of the hexagon's 6 surveyed interior angles) is
fixed scenario data, exactly like Roofline Call's building footprint: it
defines the two options being compared, not an uncertain quantity to flex.

evaluate_twist() computes the TWIST's different metric: total shop time (setup
+ cutting) before the truss shop's cutoff, in hours, negated so lower time
(better) returns a higher number. The Even Eight's 8 identical hips share one
pattern setup; The Site Six's 6 unique hips each need their own template and
test-fit, because no two are alike. This is a genuinely different metric from
the graded dollar metric -- see FACILITATOR.md.
"""
import math

PARAMS = {
    # --- MA1: constructed site geometry (Appendix B / Appendix E MA1) --------
    # NOT flexed -- this defines the two frame designs being compared, the
    # same way Roofline Call's 24x52 ft footprint was given design, not an
    # assumption with a confidence interval.
    "run_a_ft": 12.988,                       # Option A: identical for all 8 hips
    "side_a_ft": 9.9411,                      # Option A: identical for all 8 sides
    "n_hips_a": 8,
    "footprint_a_sqft": 477.17,

    "runs_b_ft": [14.0, 16.5, 12.0, 15.5, 13.0, 17.0],   # Option B: 6 different hips
    "sides_b_ft": [18.0, 22.5, 15.0, 20.0, 17.5, 24.0],  # Option B: 6 different sides
    "footprint_b_sqft": 510.0,

    "pitch_rise": 6.0, "pitch_run": 12.0,     # 6-in-12, both options (Appendix A)
    "lumber_bf_factor": 2 * 6 / 12,           # board-feet per linear foot, 2x6 stock

    # --- sourced ---------------------------------------------------------------
    "price_per_bf_usd": 0.52135,              # S1: $521.35 / 1000 board-feet
    "wage_usd_per_hr": 29.12,                 # S2: BLS median carpenter wage

    # --- MA2 / MA3: fabrication time assumptions (Appendix E) -----------------
    "simple_cut_min": 10.0,                   # MA2: identical-rafter batch cut
    "custom_premium": 0.45,                   # MA3: custom-cut time premium over MA2

    # --- MA4 / MA5: site-prep grading rate assumptions (Appendix E) -----------
    "site_prep_rate_a": 1.10,                 # MA4: USD per sq ft, Option A
    "site_prep_rate_b": 0.95,                 # MA5: USD per sq ft, Option B

    # --- twist-only: shop scheduling assumptions (FACILITATOR.md only) --------
    "pattern_setup_min": 15.0,                # one-time, Option A only
    "template_setup_min": 20.0,               # per unique piece, Option B only
}

# Only the assumptions the case author actually chose are swept -- the site
# geometry (MA1) is the scenario itself, and price_per_bf_usd/wage_usd_per_hr
# are sourced (S1/S2), stress-tested by Probe 6 (data decay) instead.
FLEX = [
    "simple_cut_min",      # Appendix E, MA2
    "custom_premium",      # Appendix E, MA3
    "site_prep_rate_a",    # Appendix E, MA4
    "site_prep_rate_b",    # Appendix E, MA5
]


def _hip_length(run_ft, p):
    rise = run_ft * (p["pitch_rise"] / p["pitch_run"])
    return math.sqrt(run_ft ** 2 + rise ** 2)


def _frame_totals(p):
    # Option A: 8 identical hips
    hip_len_a = _hip_length(p["run_a_ft"], p)
    hips_total_a = p["n_hips_a"] * hip_len_a
    perim_a = p["n_hips_a"] * p["side_a_ft"]
    len_total_a = hips_total_a + perim_a
    bf_a = len_total_a * p["lumber_bf_factor"]

    # Option B: 6 different hips
    hip_lens_b = [_hip_length(r, p) for r in p["runs_b_ft"]]
    hips_total_b = sum(hip_lens_b)
    perim_b = sum(p["sides_b_ft"])
    len_total_b = hips_total_b + perim_b
    bf_b = len_total_b * p["lumber_bf_factor"]

    return {
        "hip_len_a": hip_len_a, "hips_total_a": hips_total_a, "perim_a": perim_a,
        "len_total_a": len_total_a, "bf_a": bf_a,
        "hip_lens_b": hip_lens_b, "hips_total_b": hips_total_b, "perim_b": perim_b,
        "len_total_b": len_total_b, "bf_b": bf_b,
    }


def evaluate(params=None):
    """Graded primary metric: covered sq ft per dollar of frame + site prep."""
    p = dict(PARAMS); p.update(params or {})
    g = _frame_totals(p)

    material_a = g["bf_a"] * p["price_per_bf_usd"]
    material_b = g["bf_b"] * p["price_per_bf_usd"]

    simple_cost = p["simple_cut_min"] / 60.0 * p["wage_usd_per_hr"]
    custom_cost = simple_cost * (1 + p["custom_premium"])
    labor_a = p["n_hips_a"] * simple_cost
    labor_b = len(p["runs_b_ft"]) * custom_cost

    site_prep_a = p["footprint_a_sqft"] * p["site_prep_rate_a"]
    site_prep_b = p["footprint_b_sqft"] * p["site_prep_rate_b"]

    total_a = material_a + labor_a + site_prep_a
    total_b = material_b + labor_b + site_prep_b

    return {"A": p["footprint_a_sqft"] / total_a, "B": p["footprint_b_sqft"] / total_b}


def evaluate_twist(params=None):
    """Twist metric: total shop setup+cut time in hours, negated (lower=better)."""
    p = dict(PARAMS); p.update(params or {})
    simple_cost_min = p["simple_cut_min"]
    custom_cost_min = simple_cost_min * (1 + p["custom_premium"])

    time_a_min = p["pattern_setup_min"] + p["n_hips_a"] * simple_cost_min
    n_b = len(p["runs_b_ft"])
    time_b_min = n_b * p["template_setup_min"] + n_b * custom_cost_min

    return {"A": -(time_a_min / 60.0), "B": -(time_b_min / 60.0)}


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})

    def _report(d, label):
        lo, hi = min(d, key=d.get), max(d, key=d.get)
        margin = 100 * (d[hi] - d[lo]) / abs(d[lo]) if d[lo] else float('nan')
        print(f"{label:6s} A={d['A']:.4f}  B={d['B']:.4f}  winner={hi}  margin={margin:.2f}%")

    _report(base, "base")
    _report(tw, "twist")

    g = _frame_totals(PARAMS)
    print("\n--- detail ---")
    print("hip_len_a", round(g["hip_len_a"], 4), "x", PARAMS["n_hips_a"], "=", round(g["hips_total_a"], 2))
    print("perim_a", round(g["perim_a"], 2))
    print("len_total_a", round(g["len_total_a"], 2), "bf_a", round(g["bf_a"], 2))
    print("hip_lens_b", [round(x, 4) for x in g["hip_lens_b"]])
    print("hips_total_b", round(g["hips_total_b"], 2))
    print("perim_b", round(g["perim_b"], 2))
    print("len_total_b", round(g["len_total_b"], 2), "bf_b", round(g["bf_b"], 2))
