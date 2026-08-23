#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Robotics Engineer.

Tier 2 probe 5 ("flex each stated assumption by ±50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. Contract is the
two public names described in skills/case-readiness/scripts/
example_sensitivity_model.py (the Cold Chain reference): PARAMS, evaluate(),
and optionally evaluate_twist().

primary_metric is TOTAL TRAVEL TIME (minutes) for Ultron to recover both
remaining containers -- lower is better. evaluate() returns {"A": ..., "B": ...}
per the "higher is better" contract, so both route times are returned negated
(-minutes); the route with the smaller total time has the larger (less
negative) metric, exactly like Cold Chain's dose counts, and margin_pct math
downstream (100*(winner-loser)/loser) still reads correctly off these values.

Verified against case.json.derived:
    base   A (route C-A-B) = -20.896 min   B (route C-B-A) = -20.135 min
           B wins (route C-B-A is faster) -- case.json margin_pct 3.78%
    twist  A = -20.896 min   B = -29.456 min
           A now wins -- case.json.derived.twist_margin_pct 40.96%

NOTE ON MARGIN FORMULAS (pre-existing, not part of this twist redesign): case.json's own
margin_pct convention divides by the WINNER's magnitude -- 100*(winner-loser)/abs(winner) -- while
this file's `__main__` block below (and the Cold Chain reference model it was copied from) divides
by the LOSER's -- 100*(winner-loser)/abs(loser). The two formulas agree on which side wins and by
roughly how much, but print different percentages (e.g. running this file prints "3.64%"/"29.06%"
for base/twist, not the 3.78%/40.96% quoted above from case.json). This discrepancy predates the
2026-08-22 twist redesign -- the base-case mismatch (3.64 vs 3.78) was already present before this
edit -- so it is noted here rather than silently "fixed" by changing either convention.

2026-08-22 TWIST REDESIGN (case-readiness P4 remediation, see QA_REPORT.md): the original twist
blocked the direct A-B leg and rerouted through C's position. Both route orders (C-A-B and C-B-A)
traverse the A-B leg exactly once, so adding a constant detour to that shared leg shifts both
routes' total time by the same amount -- the absolute gap, and therefore the winner, is
algebraically invariant to any A-B detour of any size. That is a real structural property of this
geometry (Tier 2, 2026-08-19 finding), not something P5/flex could ever have caught, and it made
the original twist a true no-op on the winner regardless of the detour's magnitude.

The redesigned twist blocks the direct C-B corridor instead. Route C-A-B never travels the C-B leg
at all (it goes C->A->B) -- so blocking C-B affects ONLY route C-B-A, which uses it directly. This
is a genuine asymmetry the original A-B version didn't have, and it is what lets the twist actually
flip the winner: with DETOUR_EXTRA_M added only to the C-B leg, route C-B-A's total time rises from
20.135 to 29.456 minutes while route C-A-B's is entirely untouched at 20.896 -- A overtakes B.

FLEX[] IS DELIBERATELY EMPTY -- this is itself the P5 finding, not an
oversight. Every numeric quantity in this case is either:
  (a) real/given data the case states as fact and cites/measures directly
      (the three site coordinates, read off the drone map in Appendix A;
      Ultron's 0.06 mph rough-terrain speed, a stated Background design spec;
      Container B's 93%/1.2%-per-hour integrity reading, Appendix B) -- P6
      (data decay) is the right probe for these, not P5; or
  (b) a genuinely BINARY modeling convention with no continuous numeric dial
      to flex ±50% (Appendix C's Assumption 1 -- treat the whole field as
      uniform rough terrain, no locally-faster shortcut modeled; Assumption 2
      -- straight-line legs, no mid-route climb pause in the time calc).
There is no author-chosen numeric fudge factor anywhere in this case's
arithmetic analogous to Cold Chain's `opening_cost_h` or
`allocation_village_priority` -- nothing the author picked as an estimate or
scenario dial that isn't either a cited fact or a yes/no convention. Putting
any of (a) into FLEX would be exactly the FLEX-scoping error the skill
warns against (flexing cited data produces theatre, not a real sensitivity
test); putting (b) into FLEX is not meaningful because there's no magnitude
to flex -- Assumption 1/2 are either on or off, not variable.

PARAMS still lists every dial the case states, for completeness and so
`--flex-all` can sweep them if a reviewer wants that theatre disclosed
explicitly.
"""
import math

PARAMS = {
    # --- Appendix A, drone-survey coordinates (meters) ------------------------
    "site_A_x": 28.0, "site_A_y": 25.0,
    "site_B_x": 33.0, "site_B_y": 4.0,
    "site_C_x": 27.0, "site_C_y": 13.0,
    # --- Background, Ultron's stated design speed over rough terrain ---------
    "rough_terrain_speed_mph": 0.06,
    # --- Appendix B, Container B's DOD integrity reading ----------------------
    "container_B_integrity_pct": 93.0,
    "container_B_decay_pct_per_hr": 1.2,
    # --- Twist, real surveyed detour distance around the debris field blocking
    # the direct C-B corridor (facilitator-only reveal; given/disclosed fact,
    # not an author estimate -- see FLEX note below) ---------------------------
    "twist_cb_detour_extra_m": 15.0,
}

MPH_TO_M_PER_HR = 1609.34

# No genuine author-chosen numeric assumption exists in this case distinct
# from cited/given data -- see docstring. P5 therefore sweeps zero dials by
# design, not by omission.
FLEX = []


def _dist(p, s1, s2):
    x1, y1 = p[f"site_{s1}_x"], p[f"site_{s1}_y"]
    x2, y2 = p[f"site_{s2}_x"], p[f"site_{s2}_y"]
    return math.hypot(x2 - x1, y2 - y1)


def _core(params):
    p = dict(PARAMS); p.update(params or {})
    speed_m_per_hr = p["rough_terrain_speed_mph"] * MPH_TO_M_PER_HR
    d_ca = _dist(p, "C", "A")
    d_cb = _dist(p, "C", "B")
    d_ab = _dist(p, "A", "B")
    return p, speed_m_per_hr, d_ca, d_cb, d_ab


def evaluate(params, cb_leg_extra_m=0.0):
    """cb_leg_extra_m: extra distance added to the C<->B leg specifically (used by
    the twist, where the direct C-B corridor is blocked). Route C-A-B never
    travels the C-B leg directly -- it goes C->A->B -- so this extra distance
    affects ONLY route C-B-A. That asymmetry is deliberate: it is what lets the
    twist actually change the winner (see evaluate_twist's docstring)."""
    p, speed, d_ca, d_cb, d_ab = _core(params)
    cb_effective = d_cb + cb_leg_extra_m

    route_C_A_B_m = d_ca + d_ab            # unaffected by a C-B leg detour
    route_C_B_A_m = cb_effective + d_ab
    time_C_A_B_min = route_C_A_B_m / speed * 60.0
    time_C_B_A_min = route_C_B_A_m / speed * 60.0

    # higher-is-better contract: negate the time (lower time -> larger metric)
    return {"A": -time_C_A_B_min, "B": -time_C_B_A_min}


def evaluate_twist(params):
    """Secondary explosion blocks the direct C-B corridor (not A-B). Ultron takes
    a real, surveyed detour of PARAMS['twist_cb_detour_extra_m'] around the
    debris field to still reach B directly from C.

    This only affects route C-B-A, the one order that travels the C-B leg
    directly -- route C-A-B goes C->A->B and never touches C-B at all, so it is
    completely unaffected. That is the structural difference from the original
    (2026-08-19) version of this twist, which blocked the shared A-B leg: both
    route orders travel A-B exactly once, so any A-B detour shifts both routes'
    total time equally and can never change the winner -- an algebraic
    invariant of the geometry, not a modeling choice. Blocking C-B instead
    breaks that symmetry and lets the twist genuinely flip the verdict."""
    p = dict(PARAMS); p.update(params or {})
    detour_extra_m = p["twist_cb_detour_extra_m"]
    return evaluate(p, cb_leg_extra_m=detour_extra_m)


def container_B_integrity(params, elapsed_hr):
    p = dict(PARAMS); p.update(params or {})
    return p["container_B_integrity_pct"] - p["container_B_decay_pct_per_hr"] * elapsed_hr


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})

    def margin(d):
        win = max(d, key=d.get); lo = min(d, key=d.get)
        return win, 100.0 * (d[win] - d[lo]) / abs(d[lo])

    bw, bm = margin(base)
    tw_w, tw_m = margin(tw)
    print("base ", {k: round(-v, 3) for k, v in base.items()}, "minutes; winner", bw,
          "margin %.2f%%" % bm)
    print("twist", {k: round(-v, 3) for k, v in tw.items()}, "minutes; winner", tw_w,
          "margin %.2f%%" % tw_m)

    p, speed, d_ca, d_cb, d_ab = _core({})
    print("dist C-A %.3f  C-B %.3f  A-B %.3f  (m)" % (d_ca, d_cb, d_ab))
    t_via_A_first = (d_ca + d_ab) / speed * 60.0  # elapsed to reach B via A-first
    t_via_B_first = d_cb / speed * 60.0           # elapsed to reach B via B-first
    print("B integrity via A-first: %.3f%%  via B-first: %.3f%%" % (
        container_B_integrity({}, t_via_A_first / 60.0),
        container_B_integrity({}, t_via_B_first / 60.0)))
