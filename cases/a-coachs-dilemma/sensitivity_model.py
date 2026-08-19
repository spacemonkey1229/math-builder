#!/usr/bin/env python3
"""
SENSITIVITY MODEL — A Coach's Dilemma (2026-08-18 content replacement).

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the reference
shape this file follows. This authoring pass ran Tier 1 self-check only (per
explicit instruction not to run Tier 2 probes) -- this file is provided so a
future, human-triggered Tier 2 run has a working model to flex, and so the
hand-check already recorded in case.json.balance.stability (removing MA3
pushes the margin to 23.1%, over the SPEC Section 2 20% cap) is reproducible.

CONTRACT:
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            subset of PARAMS Tier 2 flexes
    evaluate(params) -> dict   {"A": metric, "B": metric}  points CONCEDED by
                                Houston -- LOWER is better for Houston, unlike
                                the old case's "higher is safer" convention.

`evaluate()` models case.json's graded primary_metric / balance.margin_pct
(9.7%): the corrected expected points Houston concedes per defensive
possession, Hack-a-Jordan (A) vs. Play It Straight (B), after Appendix D's
two disclosed real-anchored costs (MA2 live-ball-rebound risk, MA3
transition-suppression cost) are added to A. Matches
case.json.derived.realistic_ev_a_points (1.0145) and .clippers_ppp (1.124).
"""

PARAMS = {
    # --- Appendix B / source S1: DeAndre Jordan's real 2014-15 regular-season
    #     free-throw percentage -- the "book" number knowable before Game 4.
    "jordan_season_ft_pct": 0.397,
    # --- Appendix B / source S3: Clippers' real 2014-15 team points per
    #     possession (Offensive Rating / 100).
    "clippers_ppp": 1.124,
    # --- Appendix D MA2: real-anchored offensive-rebound rate on a missed
    #     free throw (source S5, 2015-16 season, MEDIUM confidence -- nearest
    #     available public figure, season gap disclosed).
    "oreb_rate_on_missed_ft": 0.104,
    # --- Appendix D MA3: disclosed, unsourced-as-precise-fact transition-
    #     suppression cost Houston pays (only under Option A) by fouling
    #     instead of forcing a live-ball stop. Conservative low end of a
    #     found-but-not-primary real range (~0.15-0.3 pts/poss). THIS IS THE
    #     LOAD-BEARING DIAL -- removing it breaks the 20% cap (see __main__).
    "transition_suppression_cost": 0.15,
    # --- Appendix D MA4: disclosed, unsourced-as-precise-fact backup-center
    #     defensive drop-off, in points per 100 possessions. Feeds
    #     evaluate_roster(), not evaluate() -- D4's foul-budget risk is a
    #     real, deliberately SEPARATE axis from the graded per-possession
    #     metric (case.json.balance.margin_basis is explicit about this).
    "backup_center_delta_per100": 8.0,
}

# Probe 5 flexes the two dials that are NOT a real, cited, load-bearing
# measurement (jordan_season_ft_pct and clippers_ppp are real Appendix B/S1/S3
# figures -- cited data belongs to Tier 2 probe 6, not probe 5, same doctrine
# the old version of this case's own sensitivity_model.py already established
# and skills/case-readiness/SKILL.md's P5 section documents). oreb_rate is a
# real-anchored MEDIUM-confidence figure (S5) used inside a Modeling
# Assumption, not a stated scenario constant on its own -- flexed here anyway
# since MA2's arithmetic treats it as a dial, matching the doctrine that a
# Modeling Assumption's OWN chosen constants (not the cited figures feeding
# them) are probe 5's real subject.
FLEX = [
    "transition_suppression_cost",
    "backup_center_delta_per100",
]


def evaluate(params=None):
    """The case's graded primary_metric: points Houston CONCEDES per
    possession -- LOWER is better for Houston. Option A = Hack-a-Jordan
    (realistic, corrected model, Appendix D's MA2+MA3 applied). Option B =
    Play It Straight (Clippers' real points-per-possession, unchanged)."""
    p = dict(PARAMS)
    p.update(params or {})
    ft = p["jordan_season_ft_pct"]
    naive_a = 2 * ft
    ma2_extra = (1 - ft) * p["oreb_rate_on_missed_ft"] * p["clippers_ppp"]
    realistic_a = naive_a + ma2_extra + p["transition_suppression_cost"]
    return {"A": realistic_a, "B": p["clippers_ppp"]}


def evaluate_roster(params=None):
    """D4's separate roster-exhaustion axis -- NOT the graded primary_metric.
    Returns the Clippers' points-per-possession once Houston's primary center
    is off the floor (foul trouble/disqualified), under Appendix D's MA4."""
    p = dict(PARAMS)
    p.update(params or {})
    return p["clippers_ppp"] + p["backup_center_delta_per100"] / 100.0


def margin_pct(result):
    """Percent margin of B over A, matching case.json.balance.margin_basis'
    convention: (B - A) / B, since B (Play It Straight, Clippers' real PPP)
    is the higher/worse-for-Houston number when A wins."""
    return 100.0 * (result["B"] - result["A"]) / result["B"]


if __name__ == '__main__':
    base = evaluate()
    print("base (graded primary_metric)", {k: round(v, 4) for k, v in base.items()},
          "  margin = %.2f%% (favors A / Hack-a-Jordan if positive)" % margin_pct(base))

    naive = evaluate({"transition_suppression_cost": 0.0, "oreb_rate_on_missed_ft": 0.0})
    print("naive D2 (no MA2/MA3 costs)", {k: round(v, 4) for k, v in naive.items()},
          "  margin = %.2f%%" % margin_pct(naive))

    no_trans = evaluate({"transition_suppression_cost": 0.0})
    print("MA3 removed entirely       ", {k: round(v, 4) for k, v in no_trans.items()},
          "  margin = %.2f%%  <-- BREAKS the SPEC Sec.2 20%% cap" % margin_pct(no_trans))

    print("\nFLEX sweep (+/-50%):")
    for key in FLEX:
        for mult, label in ((0.5, "-50%"), (1.5, "+50%")):
            flexed = evaluate({key: PARAMS[key] * mult})
            m = margin_pct(flexed)
            flip = " <-- FLIPS (B now favored)" if m < 0 else ""
            print(f"  {key} {label}: A={flexed['A']:.4f} B={flexed['B']:.4f} margin={m:.2f}%{flip}"
                  + ("  OVER 20% CAP" if abs(m) > 20 else ""))

    print("\nD4 roster-exhaustion axis (separate from the graded metric):")
    print("  Clippers PPP with primary center IN: ", round(PARAMS["clippers_ppp"], 4))
    print("  Clippers PPP with backup center IN:  ", round(evaluate_roster(), 4))
