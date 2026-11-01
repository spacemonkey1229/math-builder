#!/usr/bin/env python3
"""
Sensitivity model -- The Trophy and the Table.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS, FLEX, evaluate(params) -> {"A": metric, "B": metric}  (higher is better),
    evaluate_twist(params) -> same shape with the twist applied.

Metric: expected 2025/26 Premier League points for the club.
A = Keep the manager.  B = Replace the manager.

Structure (all of it stated in the case):
  * The 2024/25 table (Appendix B, official) is fitted by least squares with the
    club's own row LEFT OUT (the "outlier-check" model of record, D3).
  * L = that fitted line at the club's goal difference; r = club's points minus L.
  * Option A (keep):    E_A = L - a * |r|   (a = share of the shortfall that repeats next season)
  * Option B (replace): E_B = L - d         (d = one-season reset cost, points; the case does not
    fix it: students choose a range, the case suggests 0 to 4, and this model evaluates the
    midpoint 2 as a test point. The real question is the BREAK-EVEN d* = a * |r|.)
  * a is DERIVED from ten Wikipedia season tables (Appendix E): pooled next-season-on-this-season
    residual slope 0.109, 95% range about -0.05 to 0.27. The case uses 0.11. d is an unsourced
    range the student chooses (MA2).

TWIST (facilitator only): no club in the ten seasons missed the line by as much as this club, so
the room is asked to suppose this club's miss is the sticky kind: a_twist = 0.27, the top of the
Appendix E range. A what-if, not a measured fact.

FLEX scoping: the table, goal differences and points are cited official data (stress-tested by
P6, not swept). Only MA1 and MA2 are assumptions.
"""
import math

# Appendix B -- official final 2024/25 Premier League table (goal difference, points)
TABLE = [
    ("Liverpool", 45, 84), ("Arsenal", 35, 74), ("Manchester City", 28, 71),
    ("Chelsea", 21, 69), ("Newcastle United", 21, 66), ("Aston Villa", 7, 66),
    ("Nottingham Forest", 12, 65), ("Brighton & Hove Albion", 7, 61),
    ("AFC Bournemouth", 12, 56), ("Brentford", 9, 56), ("Fulham", 0, 54),
    ("Crystal Palace", 0, 53), ("Everton", -2, 48), ("West Ham United", -16, 43),
    ("Manchester United", -10, 42), ("Wolverhampton Wanderers", -15, 42),
    ("Tottenham Hotspur", -1, 38), ("Leicester City", -47, 25),
    ("Ipswich Town", -46, 22), ("Southampton", -60, 12),
]
CLUB = "Tottenham Hotspur"


def fit(rows):
    n = len(rows)
    mx = sum(r[1] for r in rows) / n
    my = sum(r[2] for r in rows) / n
    sxx = sum((r[1] - mx) ** 2 for r in rows)
    sxy = sum((r[1] - mx) * (r[2] - my) for r in rows)
    b = sxy / sxx
    a = my - b * mx
    res = [r[2] - (a + b * r[1]) for r in rows]
    sse = sum(e * e for e in res)
    sst = sum((r[2] - my) ** 2 for r in rows)
    return {"intercept": a, "slope": b, "r2": 1 - sse / sst,
            "resid_sd": math.sqrt(sse / (n - 2)), "resid": res}


FULL = fit(TABLE)
OTHERS = [r for r in TABLE if r[0] != CLUB]
LOO = fit(OTHERS)
_club = [r for r in TABLE if r[0] == CLUB][0]
CLUB_GD, CLUB_PTS = _club[1], _club[2]
L = LOO["intercept"] + LOO["slope"] * CLUB_GD        # model-of-record prediction
R = CLUB_PTS - L                                       # residual (negative)

PARAMS = {
    "a": 0.11,        # MA1: share of the shortfall that repeats next season (DERIVED, Appendix E: pooled 0.109)
    "d": 2.0,         # MA2 TEST POINT: midpoint of the 0-4 point range the case asks students to consider. NOT a case claim: the student chooses; this is only the evaluation point for the balance test.
    "a_twist": 0.27,  # TWIST ONLY: top of the Appendix E range for the repeat share
}
FLEX = ["a", "d"]


def _metrics(a, d):
    return {"A": L - a * abs(R), "B": L - d}


def evaluate(params=None):
    p = dict(PARAMS); p.update(params or {})
    return _metrics(p["a"], p["d"])


def evaluate_twist(params=None):
    p = dict(PARAMS); p.update(params or {})
    return _metrics(p["a_twist"], p["d"])


def _margin(m):
    lo, hi = min(m.values()), max(m.values())
    w = "A" if m["A"] > m["B"] else ("B" if m["B"] > m["A"] else "TIE")
    return w, 100.0 * (hi - lo) / lo


if __name__ == "__main__":
    print("FULL fit", {k: round(v, 4) for k, v in FULL.items() if k != "resid"})
    print("LOO  fit", {k: round(v, 4) for k, v in LOO.items() if k != "resid"})
    full_pred = FULL["intercept"] + FULL["slope"] * CLUB_GD
    print("club full-fit pred %.3f resid %.3f z %.3f" % (full_pred, CLUB_PTS - full_pred,
          (CLUB_PTS - full_pred) / FULL["resid_sd"]))
    print("club LOO pred %.3f resid %.3f z %.3f" % (L, R, R / LOO["resid_sd"]))
    names = [r[0] for r in TABLE]
    order = sorted(zip(FULL["resid"], names))
    print("lowest full-fit residuals", [(round(x, 2), n) for x, n in order[:3]],
          "highest", [(round(x, 2), n) for x, n in order[-2:]])
    b = evaluate(); t = evaluate_twist()
    print("BASE ", {k: round(v, 2) for k, v in b.items()}, "%s %.2f%%" % _margin(b))
    print("TWIST", {k: round(v, 2) for k, v in t.items()}, "%s %.2f%%" % _margin(t))
    print("break-even a* = d/|r| = %.4f" % (PARAMS["d"] / abs(R)))
    base_w = _margin(b)[0]
    print("\n--- FLEX +-50% ---")
    for n in FLEX:
        for f, lab in ((1.5, "+50%"), (0.5, "-50%")):
            p = dict(PARAMS); p[n] *= f
            w, m = _margin(evaluate(p))
            print(f"{n:3s} {lab} value={p[n]:.3f} winner={w} margin={m:6.2f}%"
                  + (" <-- FLIP" if w != base_w else "") + (" <-- CAP BREACH" if m > 20 else ""))
