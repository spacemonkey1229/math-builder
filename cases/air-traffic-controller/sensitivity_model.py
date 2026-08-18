#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- Air Traffic Controller.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the reference
shape this file follows.

CONTRACT:
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            subset of PARAMS Tier 2 flexes
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher = more fuel remaining

`evaluate()` models the case's actual GRADED primary_metric (case.json
`primary_metric` / `balance.margin_pct` = 5.6%): gallons of fuel remaining in
the tank at touchdown for Option A (return to OGG) vs. Option B (divert to
SFO), matching case.json's `derived.rem_a_gal` / `derived.rem_b_gal`.

No evaluate_twist() is shipped. The Twist (organs in transit needing a
same-night connection through SFO, see FACILITATOR.md) is a values-weighting
device, not a recomputation -- it introduces no new numeric parameter and
changes none of D1-D5's given data (see FACILITATOR.md's Twist Soundness
Check). There is nothing for an evaluate_twist() to recompute; the Twist
changes what the fuel numbers are *worth* to the decision, not what they
*are*.

FLEX SCOPING (case-readiness.md's P5 doctrine: "sensitivity to stated
assumptions, not to cited measurements"): dist_ogg_mi, dist_sfo_mi,
tank_capacity_gal, prefail_speed_mph, prefail_burn_rate_gal_per_hr, and the
Appendix E leak-flow readings are this case's own GIVEN scenario data (a
fictional flight's stated facts, or -- for the SFO distance -- computed from
real, sourced coordinates: case.json sources S1-S3). None of those are
flexed here. The ONE genuine stated assumption is MA1: modeling the
post-failure leak as a constant rate equal to the rounded mean of Appendix
E's plateaued readings (3.7 gal/mi), rather than the true, still-partially-
unknown behavior of a real fuel leak over 1,200+ more miles. That choice --
not the underlying table -- is what FLEX exercises.

Verified against case.json.derived:
    base   A (OGG)  = rem_a_gal = 933.2 gal
           B (SFO)  = rem_b_gal = 881.4 gal
           margin = 100*|A-B|/max(A,B) = 5.55%  (matches derived.margin_pct)
"""

PARAMS = {
    # --- Appendix A: given distances (fictional flight's own stated facts;
    #     the SFO figure is computed from real, sourced airport coordinates
    #     via the great-circle method -- see case.json sources S1-S3) -------
    "dist_ogg_mi": 1200.0,
    "dist_sfo_mi": 1214.0,
    # --- Appendix F: given aircraft/fuel data --------------------------------
    "tank_capacity_gal": 6875.0,
    "prefail_speed_mph": 542.0,
    "prefail_burn_rate_gal_per_hr": 4.88 * 139,   # 4.88 gal/seat/hr x 139 seats
    # --- MA1: the ONE genuine modeled assumption -- the post-failure leak
    #     rate is modeled as a constant equal to the rounded mean of
    #     Appendix E's plateaued readings (5 m 05 s onward: 3.71, 3.75,
    #     3.73, 3.76 -> mean 3.7375 -> rounded 3.7 gal/mi). This is a
    #     modeling CHOICE, not a cited fact -- the leak's true behavior
    #     over the remaining 1,200+ miles is not directly observable from
    #     the ~7 minutes of readings the instrument panel actually shows. --
    "steady_leak_rate_gal_per_mi": 3.7,
}

# Probe 5 flexes ONLY the modeled leak rate -- the case's one real stated
# assumption. Distances and the given aircraft/fuel figures are not flexed
# here; they are cited/given data, stress-tested by probe 6 instead.
FLEX = [
    "steady_leak_rate_gal_per_mi",
]


def _prefail_burn_gal(p):
    # NOTE: pre-failure burn depends on how far the aircraft flew BEFORE the
    # failure at its PRE-failure speed. Per MA2, this case treats "current
    # position" as the point of failure -- so the pre-failure flight covered
    # the SAME ground distance as the Option A return leg (dist_ogg_mi),
    # flown at the pre-failure speed, before the engine failed.
    t_hr = p["dist_ogg_mi"] / p["prefail_speed_mph"]
    return p["prefail_burn_rate_gal_per_hr"] * t_hr


def evaluate(params=None):
    """The case's actual graded primary_metric: gallons of fuel remaining in
    the tank at touchdown -- case.json `primary_metric` / `balance.margin_pct`
    = 5.6%, `derived.rem_a_gal` / `derived.rem_b_gal`."""
    p = dict(PARAMS)
    p.update(params or {})

    prefail_burn = _prefail_burn_gal(p)
    rate = p["steady_leak_rate_gal_per_mi"]

    burn_a = prefail_burn + rate * p["dist_ogg_mi"]
    burn_b = prefail_burn + rate * p["dist_sfo_mi"]

    rem_a = p["tank_capacity_gal"] - burn_a
    rem_b = p["tank_capacity_gal"] - burn_b

    return {"A": rem_a, "B": rem_b}


if __name__ == '__main__':
    base = evaluate({})
    a, b = base["A"], base["B"]
    winner = "A" if a > b else ("B" if b > a else "TIE")
    margin = 100 * abs(a - b) / max(a, b) if max(a, b) else 0.0
    print("base (graded primary_metric)", {k: round(v, 1) for k, v in base.items()},
          "  winner=%s  margin=%.2f%%" % (winner, margin))

    print("\n--- Probe 5: flex steady_leak_rate_gal_per_mi by +/-50% ---")
    for pct in (-0.5, 0.5):
        flexed = dict(PARAMS)
        flexed["steady_leak_rate_gal_per_mi"] = PARAMS["steady_leak_rate_gal_per_mi"] * (1 + pct)
        r = evaluate(flexed)
        fa, fb = r["A"], r["B"]
        fwinner = "A" if fa > fb else ("B" if fb > fa else "TIE")
        fmargin = 100 * abs(fa - fb) / max(fa, fb) if max(fa, fb) else 0.0
        flips = fwinner != winner
        caveat = ""
        if fa < 0 or fb < 0:
            caveat = ("  CAVEAT: at least one option's fuel-remaining figure is NEGATIVE at "
                      "this flex -- that option cannot physically reach its destination on the "
                      "modeled fuel; 'winner'/'margin' at this flex describe which option runs "
                      "dry LESS badly, not a safe arrival. Do not read this margin%% as a real "
                      "percentage of anything (same class of formula artifact as SKILL.md's "
                      "Seton Hall zero-baseline note).")
        print("  rate=%.4f gal/mi (%+.0f%%): A=%.1f B=%.1f winner=%s margin=%.2f%% %s%s"
              % (flexed["steady_leak_rate_gal_per_mi"], pct * 100, fa, fb, fwinner,
                 fmargin, "FLIPS" if flips else "stable", caveat))
