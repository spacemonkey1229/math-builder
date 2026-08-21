#!/usr/bin/env python3
"""
Sensitivity model — Player Of The Year.

Tier 2 probe 5 flexes each of this case's own stated modeling assumptions by
±50% and reports whether the winner flips. CONTRACT: PARAMS, evaluate(params).

Metric returned for "A" and "B" is each methodology's own top-finalist
composite score (CompositeA / CompositeB) — the case's own primary_metric.
Since the two methodologies are not directly comparable in absolute units
(one is an average z-score, the other a role-z times a multiplier), the
"winner" that matters is which methodology's OWN margin (top1 - top2) is
larger relative to top2 — that is what argument_a/argument_b and margin_pct
in case.json describe (A's race is a 1.74% coin flip, B's is a decisive
24.1%). evaluate() reports both methodologies' own top score and their own
runner-up gap so probe 5 can check whether either race's ranking changes.
"""

# Appendix A -- per-player raw stats. NR (not ranked) is None.
PLAYERS = {
    "Betsy Torres":     dict(pos="OH",  hit=None,  kills=3.91, aces=0.44, blocks=0.65, assists=None, digs=None, rpi=4),
    "Nicole Peterson":  dict(pos="MB",  hit=0.430, kills=3.41, aces=0.01, blocks=1.43, assists=None, digs=None, rpi=2),
    "Stephanie Roberts":dict(pos="RS",  hit=0.254, kills=4.75, aces=0.19, blocks=0.72, assists=None, digs=None, rpi=13),
    "Shawna Capellen":  dict(pos="OH",  hit=0.276, kills=5.19, aces=0.31, blocks=0.49, assists=None, digs=None, rpi=23),
    "Lauren Bates":     dict(pos="L/DS",hit=None,  kills=None, aces=None, blocks=None, assists=None, digs=4.35, rpi=2),
    "Julia Bergmann":   dict(pos="OH",  hit=0.284, kills=4.44, aces=0.32, blocks=0.60, assists=None, digs=None, rpi=5),
    "Mastana Brambilla":dict(pos="OH",  hit=0.286, kills=4.34, aces=0.21, blocks=0.44, assists=None, digs=None, rpi=5),
    "Anna DeFluer":     dict(pos="OH",  hit=None,  kills=3.27, aces=None, blocks=None, assists=None, digs=None, rpi=1),
    "Tori Dent":        dict(pos="S",   hit=None,  kills=None, aces=None, blocks=None, assists=10.74, digs=None, rpi=1),
    "Samantha Drechsel":dict(pos="OH",  hit=None,  kills=3.48, aces=0.27, blocks=0.57, assists=None, digs=None, rpi=16),
    "Sydney Hilley":    dict(pos="S",   hit=None,  kills=None, aces=None, blocks=None, assists=11.95, digs=None, rpi=2),
    "Mac May":          dict(pos="OH",  hit=0.268, kills=4.85, aces=0.39, blocks=0.45, assists=None, digs=None, rpi=17),
    "Yossiana Pressley":dict(pos="OH",  hit=0.280, kills=4.53, aces=0.15, blocks=0.55, assists=None, digs=None, rpi=6),
    "Anna Stevenson":   dict(pos="MB",  hit=0.427, kills=2.79, aces=None, blocks=1.35, assists=None, digs=None, rpi=1),
}

# Appendix B -- national reference population (cited data, not flexed by P5).
NATIONAL = {
    "hit":     (0.356, 0.033),
    "kills":   (2.333, 0.784),
    "blocks":  (1.084, 0.130),
    "assists": (9.997, 0.756),
    "digs":    (4.617, 0.426),
    "aces":    (0.405, 0.061),
}

ROLE_CATEGORIES = {
    "OH": ["kills", "hit", "aces"],
    "RS": ["kills", "hit", "aces"],
    "MB": ["blocks", "hit", "kills"],
    "S":  ["assists"],
    "L/DS": ["digs"],
}

PARAMS = {
    # Appendix E, MA1: an unranked category scores at league average, not
    # penalized. Flexing this away from 0 tests whether the "no penalty"
    # convention (vs. a small penalty for not ranking at all) matters. This
    # is the only assumption that touches Methodology A's own top-2 margin
    # (the metric evaluate() returns, matching case.json's declared
    # margin_pct), so it is the only dial in FLEX -- see evaluate()'s
    # docstring-comment for why.
    "unranked_z_penalty": 0.0,
    # Appendix D, MA3: Methodology B's team-success multiplier -- max bonus
    # a #1-RPI team's players receive. Real, stated, and used by
    # _composite_b (kept here and exercised by __main__/tests below), but
    # NOT in FLEX: it has zero effect on Methodology A's top-2 margin, the
    # metric this probe checks, so flexing it here would be the FLEX-scoping
    # error the pipeline's own doctrine warns against (testing a param the
    # returned metric never uses). Methodology B's own internal margin
    # (Hilley vs. Peterson, 24.1%) is disclosed directly in
    # case.json.balance.argument_b instead of re-derived here.
    "team_mult_max_bonus": 0.5,
    # Appendix D, MA3: the RPI rank beyond which no bonus applies. Same
    # scoping note as team_mult_max_bonus above.
    "team_mult_cutoff_rpi": 50,
}

FLEX = ["unranked_z_penalty"]


def _z(value, cat, unranked_penalty):
    if value is None:
        return -abs(unranked_penalty) if unranked_penalty else 0.0
    mean, sd = NATIONAL[cat]
    return (value - mean) / sd


def _composite_a(p, stats):
    cats = ["kills", "aces", "blocks", "assists", "digs"]
    zs = [_z(stats[c], c, p["unranked_z_penalty"]) for c in cats]
    return sum(zs) / len(zs)


def _team_mult(rpi, p):
    if rpi > p["team_mult_cutoff_rpi"]:
        return 1.0
    span = p["team_mult_cutoff_rpi"] - 1
    return 1 + p["team_mult_max_bonus"] * (1 - (rpi - 1) / span)


def _composite_b(p, stats):
    cats = ROLE_CATEGORIES[stats["pos"]]
    zs = [_z(stats[c], c, p["unranked_z_penalty"]) for c in cats]
    role_z = sum(zs) / len(zs)
    return role_z * _team_mult(stats["rpi"], p)


def evaluate(params):
    p = dict(PARAMS); p.update(params or {})
    scores_a = {name: _composite_a(p, s) for name, s in PLAYERS.items()}
    scores_b = {name: _composite_b(p, s) for name, s in PLAYERS.items()}
    rank_a = sorted(scores_a.items(), key=lambda kv: -kv[1])
    # case.json's declared primary balance metric (margin_pct = 1.74%) IS
    # Methodology A's own #1-vs-#2 gap (Stevenson vs. Hilley, both scored
    # under Methodology A) -- not a comparison between Methodology A's
    # outcome and Methodology B's outcome. The two methodologies' composites
    # live on incommensurate scales (an averaged z-score vs. a role-z times a
    # team-success multiplier) and are never meant to be compared to each
    # other on one shared axis; the case's own balance test is entirely
    # about how FRAGILE Methodology A's verdict is on its own terms. "A" and
    # "B" below are therefore Stevenson's and Hilley's scores, both computed
    # under Methodology A -- reproducing margin_pct exactly.
    a_name, a_score = rank_a[0]
    b_name, b_score = rank_a[1]
    return {"A": a_score, "B": b_score}


if __name__ == '__main__':
    print("base", {k: round(v, 4) for k, v in evaluate({}).items()})
    print("margin_pct", round(100 * (evaluate({})["A"] - evaluate({})["B"]) / evaluate({})["B"], 2))
