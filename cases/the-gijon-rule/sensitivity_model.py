#!/usr/bin/env python3
"""
Sensitivity model -- The Gijon Rule.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS, FLEX, evaluate(params) -> {"A": metric, "B": metric}  (higher is better),
    evaluate_twist(params).

Primary metric (case.json.primary_metric), LOWER is better for the committee:
    the "collusion ceiling" = the larger of two shares of the (cap+1)^2 Algeria-Chile
    result cells: the share in which a 1-0 West Germany win still sends BOTH West Germany
    and Austria through, and the share for the highest-scoring one-goal win the window
    allows ((cap)-(cap-1), i.e. 6-5 at cap 6).  Cells are an illustrative count,
    NOT probabilities.  evaluate() returns the NEGATED ceiling so "higher wins" holds (same
    negate pattern as cases/the-culling-volume).  NOTE: because the values are negative, the
    generic P5 margin arithmetic is not meaningful; the true margins are printed by __main__.

Option A = simultaneous kickoffs only; the 1982 ladder is unchanged:
           points, goal difference, goals scored.
Option B = simultaneous kickoffs plus goals scored BEFORE goal difference:
           points, goals scored, goal difference.
"Safe" = West Germany and Austria are the top two AND the ladder resolves the 2nd/3rd boundary
(an unresolved tie, which the 1982 rules settled by lot, is NOT counted as safe).

Fixed givens (cited, NOT in FLEX): the four 1982 Group 2 results played before the final day,
2 points per win (3 tested in the case, found to change nothing), the six groups' final tables.
Assumption (FLEX): `cap`, the 0..cap goal window for each match -- an enumeration choice, MA1.
"""
import itertools

# Group 2 results played before the last two matches (S1): (home, away, home_goals, away_goals)
# W = West Germany, A = Austria, G = Algeria, C = Chile
PRIOR = [("W", "G", 1, 2), ("C", "A", 0, 1), ("W", "C", 4, 1), ("G", "A", 0, 2)]

PARAMS = {"cap": 6, "points_win": 2}
FLEX = ["cap"]            # points_win is a tested rule variant, not a flexed assumption


def _table(results, win):
    T = {t: [0, 0, 0] for t in "WAGC"}          # points, goals for, goals against
    for h, a, hg, ag in results:
        for t, gf, ga in ((h, hg, ag), (a, ag, hg)):
            T[t][1] += gf
            T[t][2] += ga
            T[t][0] += win if gf > ga else (1 if gf == ga else 0)
    return T


def top2(alg_chile, wg_aut, ladder="A", win=2):
    """Return frozenset of the two advancing teams, or None if the 2nd/3rd place tie is unresolved."""
    T = _table(PRIOR + [("G", "C") + tuple(alg_chile), ("W", "A") + tuple(wg_aut)], win)

    def key(t):
        p, gf, ga = T[t]
        return (p, gf - ga, gf) if ladder == "A" else (p, gf, gf - ga)
    order = sorted(T, key=key, reverse=True)
    if key(order[1]) == key(order[2]):
        return None
    return frozenset(order[:2])


def safe_cells(wg_aut, cap, ladder="A", win=2, only_alg_not_winning=False, narrow_alg_win=False):
    cells = [(a, c) for a in range(cap + 1) for c in range(cap + 1)
             if not (only_alg_not_winning and a > c)
             and not (narrow_alg_win and not (1 <= a - c <= 2))]
    ok = [cell for cell in cells if top2(cell, wg_aut, ladder, win) == frozenset("WA")]
    return ok, len(cells)


def benchmark_scorelines(cap):
    return [(1, 0), (cap, cap - 1)]


def ceiling(ladder, cap, win=2, twist=False, narrow=False):
    best = 0.0
    for sl in benchmark_scorelines(cap):
        ok, n = safe_cells(sl, cap, ladder, win, only_alg_not_winning=twist, narrow_alg_win=narrow)
        best = max(best, len(ok) / n)
    return best


def average(ladder, cap, win=2, narrow=False, twist=False):
    vals = []
    for sl in benchmark_scorelines(cap):
        ok, n = safe_cells(sl, cap, ladder, win, only_alg_not_winning=twist, narrow_alg_win=narrow)
        vals.append(len(ok) / n)
    return sum(vals) / len(vals)


def evaluate(params=None):
    p = dict(PARAMS); p.update(params or {})
    cap = int(round(p["cap"]))
    return {"A": -ceiling("A", cap, p["points_win"]), "B": -ceiling("B", cap, p["points_win"])}


def evaluate_twist(params=None):
    """Late information: both benches learn the Algeria-Chile match ended as a narrow Algeria win
    (by one or two goals; the as-played 3-2 is one).  Only those cells remain (11 of 49 at cap 6),
    and percents are re-based on the surviving cells (Appendix C counting rule).  The ceilings tie;
    the AVERAGE (see average()) separates the options sharply."""
    p = dict(PARAMS); p.update(params or {})
    cap = int(round(p["cap"]))
    return {"A": -ceiling("A", cap, p["points_win"], narrow=True),
            "B": -ceiling("B", cap, p["points_win"], narrow=True)}


# ---- Appendix D: final tables of every 1982 first-round group (S1, S4-S8): (W, D, L, GF, GA)
GROUPS = {
    1: {"POL": (1, 2, 0, 5, 1), "ITA": (0, 3, 0, 2, 2), "CMR": (0, 3, 0, 1, 1), "PER": (0, 2, 1, 2, 6)},
    2: {"FRG": (2, 0, 1, 6, 3), "AUT": (2, 0, 1, 3, 1), "ALG": (2, 0, 1, 5, 5), "CHI": (0, 0, 3, 3, 8)},
    3: {"BEL": (2, 1, 0, 3, 1), "ARG": (2, 0, 1, 6, 2), "HUN": (1, 1, 1, 12, 6), "SLV": (0, 0, 3, 1, 13)},
    4: {"ENG": (3, 0, 0, 6, 1), "FRA": (1, 1, 1, 6, 5), "TCH": (0, 2, 1, 2, 4), "KUW": (0, 1, 2, 2, 6)},
    5: {"NIR": (1, 2, 0, 2, 1), "ESP": (1, 1, 1, 3, 3), "YUG": (1, 1, 1, 2, 2), "HON": (0, 2, 1, 2, 3)},
    6: {"BRA": (3, 0, 0, 10, 2), "URS": (1, 1, 1, 6, 4), "SCO": (1, 1, 1, 8, 8), "NZL": (0, 0, 3, 2, 12)},
}


def group_top2(rows, ladder):
    def key(t):
        w, d, l, gf, ga = rows[t]
        pts = 2 * w + d
        return (pts, gf - ga, gf) if ladder == "A" else (pts, gf, gf - ga)
    order = sorted(rows, key=key, reverse=True)
    resolved = key(order[1]) != key(order[2])
    return set(order[:2]), resolved


def group_changes():
    changed = {}
    for g, rows in GROUPS.items():
        a, ra = group_top2(rows, "A")
        b, rb = group_top2(rows, "B")
        assert ra and rb
        if a != b:
            changed[g] = (sorted(a - b), sorted(b - a))
    return changed


def _summary(sl, cap=6):
    out = {}
    for lad in "AB":
        ok, n = safe_cells(sl, cap, lad)
        out[lad] = (len(ok), n, sum(1 for a, c in ok if a > c))
    return out


if __name__ == "__main__":
    base = evaluate(); tw = evaluate_twist()
    print("BASE  A ceiling %.4f  B ceiling %.4f  (lower is better)" % (-base["A"], -base["B"]))
    ca, cb = -base["A"], -base["B"]
    print("      true margin (B ceiling vs A ceiling): %.2f%%  -> A wins (lower ceiling)" % (100 * (cb - ca) / ca))
    print("TWIST (narrow Algeria win, 11 cells) A ceiling %.4f  B ceiling %.4f" % (-tw["A"], -tw["B"]))
    print("      averages: A %.4f B %.4f" % (average("A", 6, narrow=True), average("B", 6, narrow=True)))
    print("BASE averages: A %.4f B %.4f" % (average("A", 6), average("B", 6)))
    print("Algeria-not-winning follow-up (28 cells): ceilings A %.2f B %.2f; Algeria-won (21 cells): ceilings A %.4f B %.4f" % (
        ceiling("A", 6, twist=True), ceiling("B", 6, twist=True),
        max(len([1 for a, c in safe_cells(s, 6, "A")[0] if a > c]) / 21 for s in [(1, 0), (6, 5)]),
        max(len([1 for a, c in safe_cells(s, 6, "B")[0] if a > c]) / 21 for s in [(1, 0), (6, 5)])))
    assert abs(ceiling("A", 6, narrow=True) - 1.0) < 1e-9 and abs(ceiling("B", 6, narrow=True) - 1.0) < 1e-9
    assert abs(average("B", 6, narrow=True) - 6 / 11) < 1e-9

    s10, s65 = _summary((1, 0)), _summary((6, 5))
    print("\n1-0 safe cells  A %s  B %s   (count, of, Algeria-win cells)" % (s10["A"], s10["B"]))
    print("6-5 safe cells  A %s  B %s" % (s65["A"], s65["B"]))
    assert s10["A"][0] == 39 and s10["A"][2] == 11 and s10["B"][0] == 29 and s10["B"][2] == 1
    assert s65["A"][0] == 42 and s65["B"][0] == 45
    # best scoreline over ALL 49 scorelines
    for lad in "AB":
        best = max(((len(safe_cells((w, u), 6, lad)[0]), (w, u)) for w in range(7) for u in range(7)))
        print("best scoreline under %s: %s safe in %d of 49" % (lad, best[1], best[0]))
    # B-safe cells are a subset of A-safe cells for 1-0
    okA = set(safe_cells((1, 0), 6, "A")[0]); okB = set(safe_cells((1, 0), 6, "B")[0])
    print("1-0: B-safe subset of A-safe:", okB <= okA, " only-A:", len(okA - okB), " both:", len(okA & okB))

    # 1982 as played (Algeria-Chile 3-2): who advances for each WG-Austria scoreline
    print("\nAs played (Algeria 3-2 Chile), WG-Austria scorelines that send WG + Austria through:")
    for lad in "AB":
        print(" ", lad, [(w, u) for w in range(7) for u in range(7) if top2((3, 2), (w, u), lad) == frozenset("WA")])
    print("  5-2 under A ->", top2((3, 2), (5, 2), "A"), "  6-3 under A ->", sorted(top2((3, 2), (6, 3), "A")))
    print("  1-0 as played under B ->", sorted(top2((3, 2), (1, 0), "B")))

    # 3-point rule: any difference anywhere in 7^4 cells under either ladder?
    diff = sum(top2((a, c), (w, u), l, 2) != top2((a, c), (w, u), l, 3)
               for l in "AB" for a in range(7) for c in range(7) for w in range(7) for u in range(7))
    print("\n3-point rule changes the advancing pair in %d of %d (cell x scoreline x ladder) combinations" % (diff, 2 * 7 ** 4))
    assert diff == 0

    ch = group_changes()
    print("\nOption B on the six first-round groups; groups whose advancing pair changes:", ch)
    assert 2 in ch and ch[2] == (["AUT"], ["ALG"])      # Group 2 itself, as actually played
    assert [g for g in ch if g != 2] == [6] and ch[6] == (["URS"], ["SCO"])   # the other five groups

    print("\n--- FLEX cap +-50% ---")
    for cap in (3, 6, 9):
        ea, eb = ceiling("A", cap), ceiling("B", cap)
        n = (cap + 1) ** 2
        print("cap %d (%d cells): A %.4f B %.4f  %s" % (cap, n, ea, eb,
              "TIE" if ea == eb else "A lower by %.2f%%" % (100 * (eb - ea) / ea)))
