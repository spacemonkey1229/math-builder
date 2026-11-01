"""
sensitivity_model.py -- The Culling Volume

Graded primary metric (case.json.primary_metric): total added per-frame engine cost in
milliseconds -- culling-test compute cost across every tested prop, plus wasted-volume
render/overdraw cost -- for a bounding-sphere policy (A) vs. a bounding-capsule policy (B)
applied to three representative long, thin props (Appendix B).

evaluate() contract (skills/case-readiness/SKILL.md's P5 spec): higher wins. Since LOWER
real-dollar-equivalent cost is better here (same "lower is better, so negate" pattern as
cases/the-approval-gate/sensitivity_model.py), evaluate() returns NEGATIVE total cost so a
higher score means a lower real cost.

    cost(option) = tested_props_total x per_test_cost_ms(option)
                 + total_wasted_volume_L(option) x render_cost_per_L

Real, sourced figures (lamppost pole height bounded by [S1]; pipe radius from [S2]) are NOT
flexed by default -- only the case's own stated Modeling Assumptions are (FLEX[] below). See
case.json.modeling_assumptions and RESEARCH_LOG.md for the full sourcing record.

Verified against case.json.balance / FACILITATOR.md's margin arithmetic:
    base   A = 3.063 ms  ·  B = 2.706 ms (winner, lower cost)  ·  margin 13.2%
"""
import math

PARAMS = {
    # --- Appendix B, MA1-MA5 -- prop geometry. Real/cited components noted inline.
    "lamppost_pole_r": 0.075, "lamppost_pole_h": 6.1,          # MA1 (height bounded by [S1])
    "lamppost_cone_r": 0.15, "lamppost_cone_h": 0.3,           # MA2
    "pipe_r": 0.0841375, "pipe_h": 4.0,                        # radius from [S2]; length MA3
    "signpost_r": 0.05, "signpost_h": 2.5,                     # MA4
    "signpost_pyr_s": 0.2, "signpost_pyr_h": 0.15,             # MA5
    # --- Appendix C, MA6 -- scene prop counts (per type, per frame).
    "count_each": 600.0,
    # --- Appendix D, MA7-MA9 -- cost inputs. The three genuinely authored dials.
    "sphere_cost_per_test": 0.0005,     # ms
    "capsule_cost_per_test": 0.0015,    # ms
    "render_cost_per_liter": 0.00000002,  # ms per liter of wasted volume
}

# Only the genuine cost/scale Modeling Assumptions are swept by default (SPEC §2 asks for
# sensitivity to STATED ASSUMPTIONS, not cited measurements). Prop geometry (MA1-MA5) sets
# the shape of the comparison, not a cost dial to flex the same way; count_each (MA6) is
# swept separately below in the __main__ report but omitted from the default FLEX[] because
# it scales both options' totals together and does not test genuine winner-flip risk the way
# the three cost dials do (see case.json.sensitivity_disclosure -- only MA7/MA8/MA9 are
# disclosed Category X).
FLEX = ["sphere_cost_per_test", "capsule_cost_per_test", "render_cost_per_liter"]


def _cyl_vol(r, h):
    return math.pi * r * r * h


def _cone_vol(r, h):
    return (1.0 / 3.0) * math.pi * r * r * h


def _pyr_vol(s, h):
    return (1.0 / 3.0) * s * s * h


def _sphere_vol(r):
    return (4.0 / 3.0) * math.pi * r ** 3


def _prop_stats(p, key):
    """Returns (real_vol_m3, height_m, max_radius_m) for one of the three props."""
    if key == "lamppost":
        vol = _cyl_vol(p["lamppost_pole_r"], p["lamppost_pole_h"]) + \
            _cone_vol(p["lamppost_cone_r"], p["lamppost_cone_h"])
        height = p["lamppost_pole_h"] + p["lamppost_cone_h"]
        maxr = max(p["lamppost_pole_r"], p["lamppost_cone_r"])
    elif key == "pipe":
        vol = _cyl_vol(p["pipe_r"], p["pipe_h"])
        height = p["pipe_h"]
        maxr = p["pipe_r"]
    else:  # signpost
        vol = _cyl_vol(p["signpost_r"], p["signpost_h"]) + \
            _pyr_vol(p["signpost_pyr_s"], p["signpost_pyr_h"])
        height = p["signpost_h"] + p["signpost_pyr_h"]
        maxr = max(p["signpost_r"], p["signpost_pyr_s"] / math.sqrt(2))
    return vol, height, maxr


def _wasted_liters(p, key):
    """Returns (wasted_sphere_L, wasted_capsule_L) for one prop instance."""
    vol, height, maxr = _prop_stats(p, key)
    sphere_r = height / 2.0
    sph_vol = _sphere_vol(sphere_r)
    cap_vol = _cyl_vol(maxr, height) + _sphere_vol(maxr)
    return (sph_vol - vol) * 1000.0, (cap_vol - vol) * 1000.0


def costs(params=None):
    """Convenience for reporting: returns real positive cost dict + intermediate totals."""
    p = dict(PARAMS)
    p.update(params or {})
    total_wasted_a = 0.0
    total_wasted_b = 0.0
    for key in ("lamppost", "pipe", "signpost"):
        wa, wb = _wasted_liters(p, key)
        total_wasted_a += wa * p["count_each"]
        total_wasted_b += wb * p["count_each"]
    n_total = p["count_each"] * 3.0
    cpu_a = n_total * p["sphere_cost_per_test"]
    cpu_b = n_total * p["capsule_cost_per_test"]
    render_a = total_wasted_a * p["render_cost_per_liter"]
    render_b = total_wasted_b * p["render_cost_per_liter"]
    cost_a = cpu_a + render_a
    cost_b = cpu_b + render_b
    return {"A": cost_a, "B": cost_b, "cpu_a": cpu_a, "cpu_b": cpu_b,
            "render_a": render_a, "render_b": render_b,
            "wasted_a_L": total_wasted_a, "wasted_b_L": total_wasted_b,
            "n_total": n_total}


def evaluate(params):
    """higher-wins contract: return NEGATIVE cost so lower real cost -> higher score."""
    c = costs(params or {})
    return {"A": -c["A"], "B": -c["B"]}


def evaluate_twist(params):
    """No withheld-information twist -- the 'twist' is structural (revealing MA9 has no
    real source), not new data. Returns the same evaluate() result unmodified so Tier 2 P4's
    machine recomputation has a defined, harmless no-op to compare against."""
    return evaluate(params)


if __name__ == '__main__':
    base = costs({})
    a, b = base["A"], base["B"]
    win = "A" if a < b else "B"
    lo, hi = min(a, b), max(a, b)
    margin = 100.0 * (hi - lo) / lo if lo else 0.0
    print("base A=$%.3fms  B=$%.3fms  winner(lower cost)=%s  margin=%.1f%%" % (a, b, win, margin))
    print("  cpu_a=%.3f cpu_b=%.3f  render_a=%.3f render_b=%.3f" %
          (base["cpu_a"], base["cpu_b"], base["render_a"], base["render_b"]))
    print("  wasted_a_L=%.1f  wasted_b_L=%.1f" % (base["wasted_a_L"], base["wasted_b_L"]))

    print("\n--- +/-50%% flex sweep (FLEX[] only) ---")
    for name in FLEX:
        base_val = PARAMS[name]
        for label, mult in (("-50%", 0.5), ("+50%", 1.5)):
            flexed = costs({name: base_val * mult})
            fa, fb = flexed["A"], flexed["B"]
            fwin = "A" if fa < fb else "B"
            flo, fhi = min(fa, fb), max(fa, fb)
            fmargin = 100.0 * (fhi - flo) / flo if flo else 0.0
            flip = " <<< FLIPS" if fwin != win else ""
            cap = " (breaks 20% cap)" if fmargin > 20 else ""
            print("  %-24s %-5s -> A=%.3f B=%.3f winner=%s margin=%.1f%%%s%s" %
                  (name, label, fa, fb, fwin, fmargin, flip, cap))

    print("\n--- qualitative check: count_each (MA6), scales both options together ---")
    for mult, label in ((0.5, "-50%"), (1.5, "+50%")):
        flexed = costs({"count_each": PARAMS["count_each"] * mult})
        fa, fb = flexed["A"], flexed["B"]
        fwin = "A" if fa < fb else "B"
        flo, fhi = min(fa, fb), max(fa, fb)
        fmargin = 100.0 * (fhi - flo) / flo if flo else 0.0
        print("  count_each %-5s -> A=%.3f B=%.3f winner=%s margin=%.1f%%" %
              (label, fa, fb, fwin, fmargin))
