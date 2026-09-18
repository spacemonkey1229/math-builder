#!/usr/bin/env python3
"""
Sensitivity model — Patrol Triangle.

Tier 2 probe 5 ("flex each stated assumption by ±50%; report which flips the
verdict"). CONTRACT: PARAMS, evaluate(params) -> {"A": metric, "B": metric},
higher is better.

This case's real primary metric (minutes of response time per km² covered) is
LOWER-is-better. To satisfy the "higher is better" contract without inverting
the case's own math, evaluate() returns each option's EFFICIENCY — square
kilometers covered per minute of worst-case response time (area / time) — the
reciprocal of the case's own ratio. Higher efficiency is better under either
framing, and the winner (A vs B) is identical either way: efficiency and
minutes-per-km² simply rank the two options in opposite numeric direction, not
opposite winner.

Only the two triangles' own side lengths (MA1, MA3 — the case's actual stated
Modeling Assumptions) are in FLEX[]. The shared patrol speed (S3, a real cited
figure) and the sector counts (MA2/MA4, which affect only total coverage, not
the per-sector ratio the primary metric is built from) are PARAMS but are
deliberately left out of FLEX[] — per the "only flex stated ASSUMPTIONS, not
cited measurements or non-dilemma-relevant dials" rule.

Verified against case.md / FACILITATOR.md:
    base   A_efficiency = 38.99/21.6 = 1.8051 km^2/min
           B_efficiency = 14.07/6.84 = 2.0567 km^2/min
           margin = (2.0567-1.8051)/2.0567*100 = 13.95%   (matches case.json.balance.margin_pct)
"""
import math

PARAMS = {
    # --- Appendix B / Appendix E, MA1: Perimeter Loop standard sector --------
    "side_a_long_km": 18.0,     # boundary-hugging side; sets both area and response distance
    "side_a_mid_km": 11.0,
    "side_a_short_km": 9.0,
    # --- Appendix C / Appendix E, MA3: Interior Web standard sector ----------
    "side_b_km": 5.7,           # equilateral; sets both area and response distance
    # --- Appendix A, S3: shared patrol speed (cited, not an assumption) -----
    "patrol_speed_kmh": 50.0,
    # --- Appendix E, MA2 / MA4: sector counts (affect total coverage only,
    #     not the per-sector primary-metric ratio) -------------------------
    "n_sectors_a": 6.0,
    "n_sectors_b": 8.0,
}

# SPEC §2 sensitivity is about STATED ASSUMPTIONS, not cited data or dials that
# don't touch the primary metric. patrol_speed_kmh is real and cited (S3),
# applied identically to both options — flexing it cannot change the winner,
# only both options' absolute times together, so it is excluded on the same
# logic as example_sensitivity_model.py's "cited data belongs to P6" rule.
# n_sectors_a/b affect total-area coverage (D2) only, never the per-sector
# ratio the primary metric (D4) is computed from, so they are also excluded.
FLEX = ["side_a_long_km", "side_a_mid_km", "side_a_short_km", "side_b_km"]


def _heron_area(a, b, c):
    """Area of a triangle from three side lengths. Raises ValueError (a
    negative-radicand math domain error) if the three lengths do not satisfy
    the Triangle Inequality Theorem — an invalid triangle is a real, honest
    failure mode for a ±50% flex on one side while holding the other two
    fixed, not a bug to paper over."""
    s = (a + b + c) / 2.0
    disc = s * (s - a) * (s - b) * (s - c)
    if disc <= 0:
        raise ValueError(f"sides {a},{b},{c} do not form a valid triangle "
                          f"(Triangle Inequality Theorem fails or triangle is degenerate)")
    return math.sqrt(disc)


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})

    # Option A — Perimeter Loop: scalene triangle, response distance = longest side
    a1, a2, a3 = p["side_a_long_km"], p["side_a_mid_km"], p["side_a_short_km"]
    area_a = _heron_area(a1, a2, a3)
    dist_a = max(a1, a2, a3)
    time_a = dist_a / p["patrol_speed_kmh"] * 60.0
    eff_a = area_a / time_a

    # Option B — Interior Web: equilateral triangle, response distance = one side
    side_b = p["side_b_km"]
    area_b = (math.sqrt(3) / 4.0) * side_b ** 2
    dist_b = side_b
    time_b = dist_b / p["patrol_speed_kmh"] * 60.0
    eff_b = area_b / time_b

    return {"A": eff_a, "B": eff_b}


if __name__ == '__main__':
    base = evaluate({})
    ratio_a = 1.0 / base["A"]
    ratio_b = 1.0 / base["B"]
    margin = 100 * (max(base.values()) - min(base.values())) / min(base.values())
    print("base efficiency (km^2/min)", {k: round(v, 4) for k, v in base.items()},
          "margin %.2f%%" % margin, "winner", max(base, key=base.get))
    print("as case-facing ratio (min/km^2): A=%.4f B=%.4f" % (ratio_a, ratio_b))
