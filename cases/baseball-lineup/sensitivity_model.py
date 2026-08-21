#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Baseball Lineup.

CONTRACT — exactly two required public names, plus an optional third:

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     optional; same shape, with the twist applied

Every entry in PARAMS must correspond to something the case STATES -- a
modelling assumption, a rated figure, a convention. Do not put an authorial
fudge factor in here.

WHAT IS AND ISN'T A DIAL IN THIS CASE, AND WHY.

Unlike Cold Chain (opening cost, cold life, a detour) this case's raw inputs
-- all 15 players' plate-appearance splits in Appendix A -- are GIVEN data,
not an authorial scenario choice. There is no "what if the roster were
different" dial to turn; that would be a different case, not a sensitivity
test on this one, exactly per the FLEX-scoping doctrine in
skills/case-readiness/SKILL.md P5. Appendix A is stress-tested by P6 (data
decay), not by P5.

Appendix C ("Modeling Assumptions") states exactly two things that ARE
genuine author-chosen conventions, not given data:

  Assumption 1 -- AB excludes walks. This is presented as "the real baseball
  convention," i.e. a citation of an external rule, not an authorial choice
  -- so it is not swept either (there is also no defensible "half of true/
  false" for a boolean definitional convention; ±50% has no meaning here).

  Assumption 2 -- rounding.
    (a) batting figures round to a fixed number of decimal places
        (avg_round_decimals = 3), and
    (b) any margin between two lineups' AVG/SLG is computed from the
        ALREADY-ROUNDED figures, not the raw unrounded ratio
        (margin_from_rounded, a 0/1 dial, domain-clamped like Cold Chain's
        allocation_village_priority).

Those two are FLEX. Both are real, both are things the case explicitly had
to choose (a different author could have picked 2 or 4 decimal places, or
computed margin from the raw ratio -- case.json.derived._note flags the
±0.1-point difference this makes), and both are dials this file can actually
turn ±50% and re-measure.

base()    -- primary_metric: combined batting average (case.json primary_metric)
twist()   -- the Paul twist: the SAME Appendix A data, scored by slugging
             percentage (total bases / AB) instead of batting average. This
             is not a scenario perturbation (nothing about the ROSTER
             changes) -- it is a second, real lens on the same fixed data,
             which is exactly how the case's own twist works (FACILITATOR.md
             "Twist" section: no new data arrives, Paul just asks whether
             anyone counted the home runs).

Verified against cases/baseball-lineup/case.json.derived:
    base   A(AVG) = 0.514  B(AVG) = 0.475   margin  8.2%   (matches case.json)
    twist  A(SLG) = 0.917  B(SLG) = 0.958   Venicia leads  (matches FACILITATOR.md)
"""

# --- Appendix A: every player on the roster, not just the 18 chosen ----------
PLAYERS = {
    "Abraham":   dict(BB=10, S=14, D=5, T=3, HR=0,  O=22),
    "Adams":     dict(BB=5,  S=8,  D=1, T=3, HR=1,  O=34),
    "Chow":      dict(BB=22, S=16, D=6, T=3, HR=1,  O=18),
    "Dasante":   dict(BB=3,  S=10, D=4, T=2, HR=6,  O=31),
    "Fredricks": dict(BB=5,  S=9,  D=0, T=3, HR=2,  O=35),
    "Graham":    dict(BB=10, S=16, D=5, T=4, HR=0,  O=20),
    "Harper":    dict(BB=9,  S=13, D=6, T=4, HR=0,  O=23),
    "Jacoby":    dict(BB=9,  S=17, D=6, T=2, HR=7,  O=20),
    "Jordan":    dict(BB=4,  S=11, D=2, T=2, HR=9,  O=28),
    "Poppins":   dict(BB=4,  S=3,  D=5, T=8, HR=14, O=42),
    "Sabathia":  dict(BB=10, S=12, D=7, T=4, HR=0,  O=22),
    "Swensen":   dict(BB=10, S=18, D=5, T=4, HR=2,  O=17),
    "Tranjier":  dict(BB=6,  S=11, D=0, T=2, HR=11, O=32),
    "Yoder":     dict(BB=12, S=15, D=5, T=4, HR=2,  O=18),
    "Young":     dict(BB=3,  S=8,  D=0, T=3, HR=2,  O=39),
}

# Appendix B: the two submitted lineups.
ASH = ["Swensen", "Jacoby", "Tranjier", "Chow", "Yoder", "Adams", "Sabathia", "Abraham", "Harper"]
VENICIA = ["Chow", "Sabathia", "Abraham", "Tranjier", "Poppins", "Yoder", "Fredricks", "Graham", "Jordan"]

PARAMS = {
    # --- Appendix C, Assumption 2(a) -----------------------------------------
    "avg_round_decimals": 3.0,
    # --- Appendix C, Assumption 2(b): margin computed from rounded figures,
    #     not the raw ratio. Domain is {0, 1}; a flexed value is clamped and
    #     rounded to the nearer endpoint, same convention as Cold Chain's
    #     allocation_village_priority. 1.0 = case's actual stated convention.
    "margin_from_rounded": 1.0,
}

# Only these two are genuine author-chosen conventions (Appendix C,
# Assumption 2). AB-excludes-walks (Assumption 1) is a cited external
# convention, not an authorial dial -- not swept, per the same FLEX-scoping
# doctrine that keeps Appendix A's player stats out of PARAMS entirely.
FLEX = [
    "avg_round_decimals",
    "margin_from_rounded",
]


def _hits(p):
    return p["S"] + p["D"] + p["T"] + p["HR"]


def _ab(p):
    return _hits(p) + p["O"]


def _tb(p):
    return p["S"] + 2 * p["D"] + 3 * p["T"] + 4 * p["HR"]


def _combined(names):
    h = sum(_hits(PLAYERS[n]) for n in names)
    ab = sum(_ab(PLAYERS[n]) for n in names)
    tb = sum(_tb(PLAYERS[n]) for n in names)
    return h, ab, tb


def _round_decimals(p):
    # avg_round_decimals is stated as an integer place value (Appendix C says
    # "three decimal places"). Flexing ±50% of 3 gives 1.5/4.5; round to the
    # nearest whole decimal place and floor at 0 (can't round to negative
    # places).
    d = p["avg_round_decimals"]
    return max(0, round(d))


def _use_rounded_margin(p):
    v = max(0.0, min(1.0, p["margin_from_rounded"]))
    return v >= 0.5


def _metric(names, p, use_slg):
    h, ab, tb = _combined(names)
    decimals = _round_decimals(p)
    raw = (tb if use_slg else h) / ab
    return round(raw, decimals)


def evaluate(params):
    """Primary metric per case.json: combined batting average. Higher wins."""
    p = dict(PARAMS)
    p.update(params or {})
    return {
        "A": _metric(ASH, p, use_slg=False),
        "B": _metric(VENICIA, p, use_slg=False),
    }


def evaluate_twist(params):
    """Paul's question: the same fixed Appendix A data, scored by slugging
    percentage (total bases / AB) instead of batting average. No new data
    arrives -- this is a second lens on the same numbers, matching how the
    case's own twist is written (FACILITATOR.md, "Twist" section)."""
    p = dict(PARAMS)
    p.update(params or {})
    return {
        "A": _metric(ASH, p, use_slg=True),
        "B": _metric(VENICIA, p, use_slg=True),
    }


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})
    b_margin = 100.0 * (base["A"] - base["B"]) / base["B"]
    t_lo = min(tw, key=tw.get)
    t_hi = max(tw, key=tw.get)
    t_margin = 100.0 * (tw[t_hi] - tw[t_lo]) / tw[t_lo]
    print("base ", base, "margin %.1f%% (Ash leads)" % b_margin)
    print("twist", tw, "margin %.1f%% (%s leads)" % (t_margin, t_hi))
