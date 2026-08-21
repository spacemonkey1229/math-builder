#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Psychologist.

CONTRACT — exactly two required public names, plus an optional third:

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     optional; same shape, with the twist applied

Every entry in PARAMS must correspond to something the case STATES -- a
modelling assumption, a rated figure, a convention. Do not put an authorial
fudge factor in here.

WHAT IS AND ISN'T A DIAL IN THIS CASE, AND WHY.

Appendix B's 27 applicants x 5 raw scores are GIVEN data (the case's own fixed
fictional dataset, carried over from the legacy source spreadsheet) -- there is
no "what if the applicant pool were different" dial to turn; that would be a
different case, not a sensitivity test on this one, per the FLEX-scoping
doctrine in skills/case-readiness/SKILL.md P5. Appendix B is stress-tested by
P6 (data decay on the two real-world sourced claims, S1/S2), not by P5.

Appendix C ("Modeling Assumptions") states two genuine author-chosen
conventions, not given data:

  MA1 -- normalization basis: each raw score is scaled to a percent of the
  BEST SCORE ACHIEVED IN THIS YEAR'S POOL for that category (not a fixed
  external maximum). This is a real, stated authorial choice -- but it is a
  categorical choice of *basis* (this year's pool max vs. some external
  ceiling), not a continuous number with a natural +/-50% flex (the same
  reason Baseball Lineup's Assumption 1, "AB excludes walks," was excluded
  from FLEX -- a boolean/categorical convention has no defensible half). Not
  swept here; category_pool_max below is fixed, taken directly from Appendix B.

  MA2 -- weighting: the five categories count equally (1/5 each) toward the
  composite score, per the case's stated default-weighting justification
  [S2]. This IS a continuous dial: `typing_weight` lets the case ask "what if
  typing speed counted for more (or less) than an equal fifth?" while the
  other four categories stay weighted at 1.0 each. This is FLEX.

base()  -- primary_metric: composite score (case.json.primary_metric) for the
           two NAMED, FIXED rosters in the Dilemma -- Standout Slate (Sophia,
           Spencer, Riley) and Balanced Slate (Sophia, Tyler, Brigitte). This
           mirrors Baseball Lineup's pattern: the twist does not change WHO
           is being compared here, it changes withdrawal below instead.

twist() -- Sophia (the #1 applicant on both original rankings) withdraws.
           Both slates are recomputed from the REMAINING 26 applicants using
           the SAME single-best / composite rules. This is the case's actual
           Twist (FACILITATOR.md): new information arrives, nothing about the
           scoring formula changes.

Verified against cases/psychologist/case.json.derived:
    base   A(comp) = 72.311  B(comp) = 79.037   margin 9.3%  (Balanced Slate leads)
    twist  A(comp, Spencer/Riley/Tyler) = 68.538   B(comp, Tyler/Brigitte/Riley) = 74.042
           margin 8.03% (Balanced Slate still leads) -- winner does not flip, but the
           twist changes WHO is being argued about: 2 of 3 seats become shared,
           the real fight narrows to Spencer vs. Brigitte for one seat.
"""

# --- Appendix B: every applicant, raw scores (Text Only, Text+Audio x3,
#     Audio+Text, Audio+Visual, Typing WPM). Age is omitted -- it is not a
#     dial or an input to either ranking (Appendix C, MA3). ------------------
APPLICANTS = {
    "Owen":     (8, 7, 9, 7, 48),
    "Caleb":    (10, 10, 9, 13, 34),
    "Amalia":   (9, 6, 8, 10, 44),
    "Brigitte": (12, 11, 12, 15, 32),
    "Sophia":   (16, 15, 13, 18, 28),
    "Sophie":   (9, 11, 8, 9, 23),
    "Lauryn":   (5, 9, 12, 13, 29),
    "Zach":     (10, 11, 8, 9, 45),
    "Tyler":    (12, 11, 10, 13, 52),
    "Reagan":   (9, 13, 9, 13, 41),
    "McKenna":  (7, 6, 6, 10, 42),
    "Amelia":   (6, 6, 7, 8, 43),
    "Berlyn":   (9, 10, 12, 14, 21),
    "Roselyn":  (7, 9, 9, 12, 30),
    "Spencer":  (9, 7, 5, 9, 56),
    "Ellie":    (13, 5, 8, 11, 29),
    "James":    (7, 8, 8, 9, 34),
    "Ivy":      (7, 9, 8, 15, 23),
    "Andrew":   (8, 9, 11, 11, 46),
    "Isaac":    (8, 6, 8, 11, 41),
    "Cru":      (3, 4, 4, 6, 35),
    "Allissa":  (14, 9, 11, 13, 38),
    "Gabi":     (8, 12, 11, 12, 39),
    "Ibby":     (6, 8, 6, 10, 45),
    "Lily":     (6, 4, 4, 11, 41),
    "Lilya":    (6, 7, 9, 10, 37),
    "Riley":    (12, 7, 15, 13, 38),
}

# The Dilemma's two named, fixed rosters (base scenario, Sophia included).
STANDOUT_SLATE = ["Sophia", "Spencer", "Riley"]
BALANCED_SLATE = ["Sophia", "Tyler", "Brigitte"]

# Post-twist rosters: same single-best / composite rules, re-run on the 26
# applicants remaining once Sophia withdraws. (Not a PARAM -- this is what the
# Twist reveals, not a dial a Hero or a facilitator turns.)
TWIST_STANDOUT_SLATE = ["Spencer", "Riley", "Tyler"]
TWIST_BALANCED_SLATE = ["Tyler", "Brigitte", "Riley"]

PARAMS = {
    # --- Appendix C, MA2: equal weighting is the case's stated default;
    #     1.0 means typing counts the same as each of the four memory tests.
    "typing_weight": 1.0,
}

# Only MA2's weighting dial is a genuine, continuously-flexible authorial
# choice. MA1 (normalization basis) is a real stated assumption too, but it
# is categorical, not continuous -- no defensible "+/-50%" of "use this
# year's pool max" exists, the same reason Baseball Lineup's AB-excludes-
# walks convention was excluded from FLEX.
FLEX = [
    "typing_weight",
]


def _category_pool_max():
    """Appendix B's bottom row: the best raw score any applicant achieved in
    each category. Fixed given data (MA1's normalization basis), not a dial."""
    maxes = [0, 0, 0, 0, 0]
    for scores in APPLICANTS.values():
        for i, v in enumerate(scores):
            maxes[i] = max(maxes[i], v)
    return maxes


CATEGORY_POOL_MAX = _category_pool_max()  # [16, 15, 15, 18, 56]


def _normalized(name):
    """Each of the applicant's 5 raw scores as a percent of this category's
    pool max (Appendix C, MA1)."""
    scores = APPLICANTS[name]
    return [100.0 * s / m for s, m in zip(scores, CATEGORY_POOL_MAX)]


def _composite(name, p):
    """Composite score: weighted mean of the 5 normalized categories.
    Weights are [1, 1, 1, 1, typing_weight] / their sum (Appendix C, MA2)."""
    pcts = _normalized(name)
    weights = [1.0, 1.0, 1.0, 1.0, max(0.0, p["typing_weight"])]
    return sum(pi * wi for pi, wi in zip(pcts, weights)) / sum(weights)


def _roster_composite_avg(names, p):
    return sum(_composite(n, p) for n in names) / len(names)


def evaluate(params):
    """Primary metric per case.json: composite score, averaged across each
    named roster's 3 admits. Higher wins."""
    p = dict(PARAMS)
    p.update(params or {})
    return {
        "A": round(_roster_composite_avg(STANDOUT_SLATE, p), 3),
        "B": round(_roster_composite_avg(BALANCED_SLATE, p), 3),
    }


def evaluate_twist(params):
    """The Twist: Sophia withdraws. Same scoring rules, same weight params,
    rosters recomputed from the remaining 26 applicants (FACILITATOR.md)."""
    p = dict(PARAMS)
    p.update(params or {})
    return {
        "A": round(_roster_composite_avg(TWIST_STANDOUT_SLATE, p), 3),
        "B": round(_roster_composite_avg(TWIST_BALANCED_SLATE, p), 3),
    }


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})
    b_margin = 100.0 * (base["B"] - base["A"]) / base["A"]
    t_margin = 100.0 * (tw["B"] - tw["A"]) / tw["A"]
    print("base ", base, "margin %.2f%% (Balanced Slate leads)" % b_margin)
    print("twist", tw, "margin %.2f%% (Balanced Slate leads)" % t_margin)

    # Peak-metric counter-argument (not the primary metric, but used in
    # case.json.balance.argument_a / .derived) -- average single-best score.
    def _best(name):
        return max(_normalized(name))

    def _roster_best_avg(names):
        return sum(_best(n) for n in names) / len(names)

    print("standout best_avg", round(_roster_best_avg(STANDOUT_SLATE), 3),
          "balanced best_avg", round(_roster_best_avg(BALANCED_SLATE), 3))
    print("twist standout best_avg", round(_roster_best_avg(TWIST_STANDOUT_SLATE), 3),
          "twist balanced best_avg", round(_roster_best_avg(TWIST_BALANCED_SLATE), 3))
