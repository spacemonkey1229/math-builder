#!/usr/bin/env python3
"""
SENSITIVITY MODEL — A Coach's Dilemma.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the reference
shape this file follows.

CONTRACT:
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            subset of PARAMS Tier 2 flexes
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher = safer for Memphis
    evaluate_twist(params)     same shape, with the Twist's rebound risk applied

`evaluate()` models the case's actual GRADED primary_metric (case.json
`primary_metric` / `balance.margin_pct` = 7.3pp): the single-shot make
probability comparison Coach Cavenaugh is really weighing in the moment --
the fouled player's season free-throw percentage (A) vs. the defended
shooter's season three-point percentage (B), the same D1/D2/D4-anchored
figures case.json's `derived` block reports (base A=54.1%, B=46.8%, margin
15.6% of B -- matches `derived.single_shot_margin_pct_of_charmers`). Earlier
drafts of this file modeled the *corrected* compound-probability comparison
(1 - p^2 vs 1 - 3pt%) instead -- a real, useful number for the D3/D4
narrative, but NOT what case.json declares as the graded primary_metric, and
its base margin (32.9%) does not even match case.json's own stated 7.3pp/
15.6% margin. Probe 5 must test sensitivity of the metric the case is
actually graded and balanced on, so `evaluate()` was corrected to match it.
The compound (corrected) comparison is preserved below as `evaluate_twist()`
for the Twist's own accounting (D3's p^2 sequence, stressed by the Twist's
live-ball rebound risk) -- it is a different, deliberately non-comparable
metric space and is not exercised by probe 5's flex sweep.

Verified against case.json.derived (Appendix C, real fictional-dataset numbers):
    base   A = fouled_player_ft_pct = 0.541 (54.1%)
           B = defended_shooter_3pt_pct = 0.4679 (46.8%)
           margin = 100*(A-B)/B = 15.6%   (matches derived.single_shot_margin_pct_of_charmers)
"""

PARAMS = {
    # --- Appendix C: Diego Imor, season free-throw percentage ---------------
    #     the player Memphis's coach chooses to foul in the base case
    "fouled_player_ft_pct": 0.541,
    # --- Appendix C: Cooper Charmers, season three-point percentage ---------
    #     Kansas's most dangerous three-point shooter among the 8 who played
    "defended_shooter_3pt_pct": 0.4679,
    # --- UNSTATED. The case explicitly does NOT give a number for how often
    #     Kansas converts an offensive rebound off a missed front-end free
    #     throw into points (FACILITATOR.md's Twist names this as a real,
    #     unquantified gap in the model -- there is no real data source for
    #     it in this fictional dataset). This dial exists so Tier 2 can
    #     measure how sensitive the Twist's conclusion is to that missing
    #     number, exactly the "exception that proves the rule" pattern in
    #     example_sensitivity_model.py's own allocation_village_priority.
    #     Domain is [0, 1]; default is a deliberately modest placeholder,
    #     NOT a claimed case fact.
    "twist_rebound_risk": 0.10,
}

# Probe 5 flexes THESE and only these -- all three are either a stated
# Appendix C figure (which player gets fouled / which shooter is defended,
# both coaching CHOICES the case explicitly asks the student to reason
# about in D2) or the unstated Twist dial flagged above. Cited box-score
# data itself is not flexed here (this is a fictional dataset, not a cited
# real-world measurement -- see case.json.legacy_conversion_note).
# NOTE: twist_rebound_risk does not affect evaluate() (it only affects
# evaluate_twist(), below) -- it stays in FLEX because it is still a real
# stated dial of the case, just not one this particular metric depends on;
# flexing it here is a documented no-op, the same pattern the reference
# model (example_sensitivity_model.py's twist_detour_h) already uses.
# FLEX rescoped 2026-08-13: fouled_player_ft_pct and defended_shooter_3pt_pct are
# Appendix C's given season statistics (this case's own fictional-but-fixed
# dataset, verified byte-identical to the source workbooks) -- not a stated
# assumption. Per skills/case-readiness/SKILL.md's P5 doctrine ("sensitivity to
# stated assumptions, not to cited measurements... cited data is stress-tested
# by P6 instead"), these do not belong in FLEX any more than Cold Chain's own
# cited cold-box thermal ratings do. MA2 (using season% as the game-probability
# convention) is the real assumption here, and it is not itself a numeric dial.
# Only twist_rebound_risk is a genuine unstated assumption (no real data source
# exists for it; built expressly for this sensitivity test).
FLEX = [
    "twist_rebound_risk",
]


def evaluate(params, detour_h=0.0):
    """The case's actual graded primary_metric: single-shot make probability,
    A (fouled player's FT%) vs B (defended shooter's 3PT%) -- case.json
    `primary_metric` / `balance.margin_pct` = 7.3pp, `derived.
    single_shot_margin_pct_of_charmers` = 15.6%."""
    p = dict(PARAMS)
    p.update(params or {})
    return {"A": p["fouled_player_ft_pct"], "B": p["defended_shooter_3pt_pct"]}


def evaluate_twist(params):
    """NOT the graded primary_metric -- this is the corrected, compound
    (p^2) comparison D3/D4 reveal, stressed further by the Twist's live-ball
    rebound risk. Kept for the Twist's own accounting; probe 5's flex sweep
    exercises evaluate() above, not this function."""
    p = dict(PARAMS)
    p.update(params or {})
    ft = p["fouled_player_ft_pct"]
    miss_first = 1 - ft
    # Twist: a missed front-end free throw is a live ball -- Kansas can
    # rebound it and still score. This adds an extra, unquantified risk
    # path on top of the clean p^2 sequence.
    a_bad_prob = ft ** 2 + miss_first * p["twist_rebound_risk"]
    b_loss_prob = p["defended_shooter_3pt_pct"]
    return {"A": 1 - a_bad_prob, "B": 1 - b_loss_prob}


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})
    print("base (graded primary_metric)", {k: round(v, 4) for k, v in base.items()},
          "  margin = %.1f%% of B" % (100 * (base["A"] - base["B"]) / base["B"]))
    print("twist (corrected, compound comparison; NOT the graded metric)",
          {k: round(v, 4) for k, v in tw.items()})

    # Compound "corrected" comparison -- D3/D4's reveal, not the graded metric
    imor = PARAMS["fouled_player_ft_pct"] * 100
    charmers = PARAMS["defended_shooter_3pt_pct"] * 100
    print("compound comparison: fouled-player one-and-one%% = %.1f%%  vs  "
          "defended-shooter 3PT%% = %.1f%%" % (imor ** 2 / 100, charmers))
