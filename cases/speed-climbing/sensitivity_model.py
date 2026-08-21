"""
sensitivity_model.py -- Speed Climbing

Contract (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS   = {...}                       every dial the case STATES
    FLEX     = ["...", "..."]              the subset that is an ASSUMPTION
    def evaluate(params) -> {"A": metric, "B": metric}     # HIGHER IS BETTER
    def evaluate_twist(params) -> {...}                    # optional

Metric convention: the case's real primary_metric (combined team-composite score, in seconds)
is LOWER-is-better. This module negates it internally so evaluate() returns higher-is-better
values, per the tier2_probes.py contract (max() picks the winner).

Only FLEX[] is swept by ±50% by default (only genuine authored assumptions, never the climbers'
actual given climb times -- those are the case's own fixed scenario data, not a research-backed
external figure, so P6/data-decay doesn't apply to them either; they simply aren't a "dial").
The one real assumption this case makes that is quantifiable and disclosed is the facilitator's
own character/leadership rubric's point weights (case.json.balance / FACILITATOR.md) -- Option B's
roster is NOT fixed data, it is the output of this rubric, so flexing the rubric weights is exactly
what SPEC's sensitivity test is for.
"""

# Official (most-recent-month) climb time per athlete -- Appendix B, given case data, not a dial.
OFFICIAL_TIME = {
    "Jesse": 8.41, "Victoria": 8.70, "Gertrude": 8.53, "Emily": 6.99, "Sky": 7.94,
    "Jane": 8.47, "Amara": 9.53, "Leslie": 7.52, "Gigi": 12.52, "Rebecca": 7.01,
    "Ava": 8.58, "Kylie": 8.22,
}

# Character/leadership rubric inputs per athlete -- which stated Coach's-Notes criteria they meet.
# 1 = criterion present per Appendix C, 0 = absent. This is NOT itself a dial; the point VALUES
# assigned to each criterion (PARAMS below) are the dial.
CRITERIA = {
    #            captain mentor trust discipline multiyear nationals culture_pos culture_neg
    "Jesse":    (0,      1,     0,    0,         0,        1,        0,          0),
    "Victoria": (0,      0,     0,    0,         0,        1,        1,          0),
    "Gertrude": (0,      0,     0,    1,         0,        0,        0,          0),
    "Emily":    (0,      0,     0,    1,         0,        1,        0,          1),
    "Sky":      (0,      0,     0,    0,         0,        0,        1,          0),
    "Jane":     (0,      0,     0,    0,         0,        0,        0,          0),
    "Amara":    (0,      0,     0,    0,         0,        0,        1,          0),
    "Leslie":   (0,      0,     1,    1,         1,        0,        0,          0),
    "Gigi":     (0,      0,     0,    0,         0,        0,        0,          0),
    "Rebecca":  (0,      0,     0,    0,         0,        0,        0,          1),
    "Ava":      (1,      1,     0,    1,         1,        1,        0,          0),
    "Kylie":    (1,      1,     0,    0,         1,        1,        0,          0),
}

PARAMS = {
    "captain_pts": 2.0,
    "mentor_pts": 1.0,
    "trust_survey_pts": 2.0,
    "discipline_pts": 1.0,
    "multiyear_pts": 1.0,
    "nationals_pts": 1.0,
    "culture_pos_pts": 1.0,
    "culture_neg_pts": -1.0,
}

# Only the rubric weights are FLEX -- these are the case's own disclosed, author-chosen modeling
# assumption (case.json.modeling_assumptions MA3 / balance.argument_b), not given/cited data.
FLEX = list(PARAMS.keys())


def _character_score(name, params):
    captain, mentor, trust, disc, multi, nat, cpos, cneg = CRITERIA[name]
    return (
        captain * params["captain_pts"]
        + mentor * params["mentor_pts"]
        + trust * params["trust_survey_pts"]
        + disc * params["discipline_pts"]
        + multi * params["multiyear_pts"]
        + nat * params["nationals_pts"]
        + cpos * params["culture_pos_pts"]
        + cneg * params["culture_neg_pts"]
    )


def _team_composite(three_times):
    times = sorted(three_times)
    mean = sum(times) / 3
    median = times[1]
    return mean + median


def _assign_teams(roster_8):
    """Appendix D's alternating-seed rule: rank by official time, 1-2-1-2..., each team's
    slowest-of-four becomes its alternate."""
    ranked = sorted(roster_8, key=lambda n: OFFICIAL_TIME[n])
    team1 = [ranked[i] for i in range(0, 8, 2)]
    team2 = [ranked[i] for i in range(1, 8, 2)]
    def split(team):
        team_sorted = sorted(team, key=lambda n: OFFICIAL_TIME[n])
        competing = team_sorted[:3]
        alternate = team_sorted[3]
        return competing, alternate
    t1_competing, t1_alt = split(team1)
    t2_competing, t2_alt = split(team2)
    return {"team1": (t1_competing, t1_alt), "team2": (t2_competing, t2_alt)}


def _option_a_roster():
    return sorted(OFFICIAL_TIME, key=lambda n: OFFICIAL_TIME[n])[:8]


def _option_b_roster(params):
    scored = sorted(
        OFFICIAL_TIME.keys(),
        key=lambda n: (-_character_score(n, params), OFFICIAL_TIME[n]),
    )
    return scored[:8]


def _combined_composite(roster_8):
    assignment = _assign_teams(roster_8)
    t1_composite = _team_composite([OFFICIAL_TIME[n] for n in assignment["team1"][0]])
    t2_composite = _team_composite([OFFICIAL_TIME[n] for n in assignment["team2"][0]])
    return t1_composite + t2_composite, assignment


def evaluate(params):
    """Returns higher-is-better values (negated seconds, since lower composite = better)."""
    a_roster = _option_a_roster()
    b_roster = _option_b_roster(params)
    a_composite, _ = _combined_composite(a_roster)
    b_composite, _ = _combined_composite(b_roster)
    return {"A": -a_composite, "B": -b_composite}


def evaluate_twist(params):
    """Kylie is removed; each team's own alternate is promoted. Returns higher-is-better values."""
    a_roster = _option_a_roster()
    b_roster = _option_b_roster(params)

    def recompute_after_injury(roster_8):
        assignment = _assign_teams(roster_8)
        new_composites = []
        for team_key in ("team1", "team2"):
            competing, alternate = assignment[team_key]
            if "Kylie" in competing:
                competing = [n for n in competing if n != "Kylie"] + [alternate]
            new_composites.append(_team_composite([OFFICIAL_TIME[n] for n in competing]))
        return sum(new_composites)

    a_new = recompute_after_injury(a_roster)
    b_new = recompute_after_injury(b_roster)
    return {"A": -a_new, "B": -b_new}


if __name__ == "__main__":
    base = evaluate(PARAMS)
    print("Base (higher-is-better, negated seconds):", base)
    print(f"  -> A combined composite = {-base['A']:.4f}s, B combined composite = {-base['B']:.4f}s")
    margin = 100 * (base["A"] - base["B"]) / abs(base["B"])
    print(f"  -> margin (A faster than B) = {margin:.2f}%")

    twist = evaluate_twist(PARAMS)
    print("Twist (higher-is-better, negated seconds):", twist)
    print(f"  -> A combined composite = {-twist['A']:.4f}s, B combined composite = {-twist['B']:.4f}s")
    twist_margin = 100 * (twist["A"] - twist["B"]) / abs(twist["B"])
    print(f"  -> post-twist margin = {twist_margin:.2f}%")
