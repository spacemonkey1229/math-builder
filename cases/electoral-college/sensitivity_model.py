#!/usr/bin/env python3
"""
sensitivity_model.py — Electoral College

Facilitator/QA tool only. Computes, for both locked strategies (A: Big-Prize, greedy descending-EV
among states Farnsworth currently leads; B: Margin, greedy ascending-current-gap among the same
states), the total projected electoral votes securable within the fixed $3,000,000 remaining
travel budget under the case's stated mechanics (Appendix E). Never shown to students.

CONTRACT (skills/case-readiness Tier 2 probe 5):
    PARAMS                     dict[str, number]   every dial the case STATES
    FLEX                       list[str]            the subset that is a stated ASSUMPTION
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     optional; same shape, with the Ohio twist applied
"""

# Appendix C contested-state data: (state, EV, peaken_pct, farnsworth_pct, undecided_pct)
CONTESTED = [
    ("Alaska", 3, 37, 45, 18), ("Arizona", 11, 39, 46, 15), ("Arkansas", 6, 24, 57, 19),
    ("California", 54, 54, 30, 16), ("Colorado", 10, 42, 38, 20), ("Florida", 30, 34, 45, 21),
    ("Georgia", 16, 40, 47, 13), ("Idaho", 4, 26, 55, 19), ("Illinois", 19, 43, 34, 23),
    ("Indiana", 11, 29, 48, 23), ("Iowa", 6, 40, 48, 12), ("Kansas", 6, 31, 47, 22),
    ("Kentucky", 8, 26, 55, 19), ("Maryland", 10, 56, 30, 14), ("Massachusetts", 11, 43, 21, 36),
    ("Michigan", 15, 40, 45, 15), ("Minnesota", 10, 45, 42, 13), ("Missouri", 10, 39, 52, 9),
    ("Montana", 4, 28, 49, 23), ("Nebraska", 5, 31, 47, 22), ("Nevada", 6, 45, 47, 8),
    ("New Hampshire", 4, 46, 37, 17), ("New Mexico", 5, 49, 41, 10), ("New York", 28, 46, 36, 18),
    ("North Carolina", 16, 37, 43, 20), ("North Dakota", 3, 17, 54, 29), ("Ohio", 17, 38, 50, 12),
    ("Oklahoma", 7, 27, 55, 18), ("Pennsylvania", 19, 43, 43, 14), ("South Dakota", 3, 28, 50, 22),
    ("Tennessee", 11, 29, 54, 17), ("Texas", 40, 39, 45, 16), ("Virginia", 13, 49, 43, 8),
    ("Washington", 12, 52, 38, 10), ("West Virginia", 4, 23, 59, 18), ("Wisconsin", 10, 41, 45, 14),
    ("Wyoming", 3, 15, 68, 17),
]

LOCKED_PEAKEN_EV = 50          # Appendix B, 9 states
LOCKED_FARNSWORTH_EV = 38      # Appendix B, 5 states
ALREADY_LEANING_PEAKEN_EV = sum(ev for _, ev, p, f, u in CONTESTED if p > f)  # banked, no visit
BASE_EV = LOCKED_PEAKEN_EV + ALREADY_LEANING_PEAKEN_EV

# --- every dial the case STATES (Appendix E, Appendix F Modeling Assumptions) --------------------
PARAMS = {
    "flat_fee": 500_000,        # MA2 — Appendix E, flat per-state travel setup cost
    "half_day_cost": 200_000,   # MA2 — Appendix E, cost per half-day visit
    "swing_rate": 2,            # MA3 — Appendix E, undecided-pool swing per half-day, percentage points
    "budget": 3_000_000,        # Appendix E, remaining travel budget (real: MA1's derived total)
    "indiana_twist_delta": 4,   # the Twist — 4 pts move from Indiana's undecided into Farnsworth
}

# Probe 5 flexes THESE and only these — the case's own stated Modeling Assumptions (MA2, MA3).
# flat_fee, budget and indiana_twist_delta are not flexed here: flat_fee/budget are part of the
# same MA1/MA2 pair but budget is the case's hard constraint (flexing it is a different case, not
# a sensitivity test on an assumption), and indiana_twist_delta is the Twist's own stated
# correction, only applied by evaluate_twist(), not by the ±50% assumption flex.
FLEX = ["half_day_cost", "swing_rate"]


def half_days_to_flip(peaken, farnsworth, undecided, swing_rate):
    """Minimum half-days so peaken_pct + swing*x > farnsworth_pct, capped by the undecided pool.
    Returns None if not flippable within the undecided ceiling. NOTE: gap == 0 (an exact tie,
    e.g. Pennsylvania 43/43) still needs 1 half-day -- a tie is not a win, D2 requires the
    projection to strictly EXCEED Farnsworth's share. Only gap < 0 (already strictly ahead) is a
    free win."""
    gap = farnsworth - peaken
    if gap < 0:
        return 0
    x = 0
    while True:
        x += 1
        if x * swing_rate > undecided:
            return None
        if peaken + x * swing_rate > farnsworth:
            return x


def _cost_to_flip(row, p):
    name, ev, peaken, farnsworth, undecided = row
    x = half_days_to_flip(peaken, farnsworth, undecided, p["swing_rate"])
    if x is None:
        return None
    return p["flat_fee"] + x * p["half_day_cost"], x, ev


def _run(order_key, p, contested):
    candidates = [r for r in contested if r[3] >= r[2]]  # Farnsworth leads OR exactly tied (needs 1 visit)
    candidates.sort(key=order_key)
    spent, ev_won = 0, 0
    for row in candidates:
        r = _cost_to_flip(row, p)
        if r is None:
            continue
        cost, _half_days, ev = r
        if spent + cost <= p["budget"]:
            spent += cost
            ev_won += ev
    return BASE_EV + ev_won, spent


def evaluate(params, contested=None):
    """Strategy A (Big-Prize, descending EV) vs Strategy B (Margin, ascending current gap)."""
    p = dict(PARAMS)
    p.update(params or {})
    rows = contested if contested is not None else CONTESTED
    a_total, _a_spent = _run(lambda r: -r[1], p, rows)
    b_total, _b_spent = _run(lambda r: (r[3] - r[2]), p, rows)
    return {"A": a_total, "B": b_total}


def evaluate_twist(params):
    """The Twist (FACILITATOR.md): a follow-up verification round finds that `indiana_twist_delta`
    points of Indiana's previously counted "undecided" voters had already committed to Farnsworth.
    Indiana's row is corrected from (peaken 29, farnsworth 48, undecided 23) to
    (peaken 29, farnsworth 52, undecided 19) -- still summing to 100.

    Before the twist: Indiana's 19-point gap needs exactly 10 half-days (20 points of movement,
    within the original 23-point undecided ceiling) -- mathematically REACHABLE, if expensive
    ($2,500,000 -- more than the entire remaining travel budget, so never actually chosen, but
    reachable in principle, which is what D2 asks Heroes to check).

    After the twist: the gap widens to 23 points while the ceiling shrinks to 19, so closing it
    would need 24 points of movement against only a 19-point ceiling -- no number of half-days
    can do it. Indiana flips from mathematically reachable to mathematically IMPOSSIBLE.

    Neither verified strategy (Big-Prize: Texas+Florida; Margin literal: Pennsylvania+Nevada+
    Wisconsin) ever used Indiana, so the twist should not move the winner or the margin -- it
    punishes only a Hero who was quietly counting on Indiana as a backup, which is the point."""
    p = dict(PARAMS)
    p.update(params or {})
    delta = p.get("indiana_twist_delta", PARAMS["indiana_twist_delta"])
    twisted = [
        (n, ev, pk, fw + delta, u - delta) if n == "Indiana" else (n, ev, pk, fw, u)
        for n, ev, pk, fw, u in CONTESTED
    ]
    return evaluate(p, contested=twisted)


if __name__ == "__main__":
    print(f"Already-leaning-Peaken contested EV (no visit needed): {ALREADY_LEANING_PEAKEN_EV}")
    print(f"BASE_EV (locked + already-leaning-Peaken) = {BASE_EV}")
    print(f"Sum check (37 contested + 9 + 5 locked): "
          f"{sum(r[1] for r in CONTESTED) + LOCKED_PEAKEN_EV + LOCKED_FARNSWORTH_EV} (should be 538)")

    base = evaluate({})
    margin = 100 * abs(base["A"] - base["B"]) / max(base["A"], base["B"])
    print(f"\nbase   A={base['A']}  B={base['B']}  margin={margin:.2f}%  "
          f"({'A wins' if base['A'] > base['B'] else 'B wins' if base['B'] > base['A'] else 'TIE'})")

    tw = evaluate_twist({})
    tmargin = 100 * abs(tw["A"] - tw["B"]) / max(tw["A"], tw["B"])
    print(f"twist  A={tw['A']}  B={tw['B']}  margin={tmargin:.2f}%")

    indiana = next(r for r in CONTESTED if r[0] == "Indiana")
    _n, _ev, ipk, ifw, iund = indiana
    before = half_days_to_flip(ipk, ifw, iund, PARAMS["swing_rate"])
    delta = PARAMS["indiana_twist_delta"]
    after = half_days_to_flip(ipk, ifw + delta, iund - delta, PARAMS["swing_rate"])
    print(f"\nIndiana twist check: before x={before} half-days (REACHABLE)  "
          f"after x={after} half-days ({'REACHABLE' if after is not None else 'IMPOSSIBLE'})")
    assert before is not None and after is None, "twist must flip Indiana from reachable to impossible"

    print("\n=== +/-50% SENSITIVITY FLEX (FLEX[] only) ===")
    for name in FLEX:
        base_val = PARAMS[name]
        for mult, label in ((0.5, "-50%"), (1.5, "+50%")):
            flexed = {name: base_val * mult}
            r = evaluate(flexed)
            m = 100 * abs(r["A"] - r["B"]) / max(r["A"], r["B"])
            winner = 'A wins' if r['A'] > r['B'] else 'B wins' if r['B'] > r['A'] else 'TIE'
            print(f"  {name} {label} ({flexed[name]:,.1f}): A={r['A']}  B={r['B']}  "
                  f"margin={m:.2f}%  {winner}")
