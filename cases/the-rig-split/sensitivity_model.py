#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- The Rig Split.

Tier 2 probe 5 ("flex each stated assumption by +-50%; report which flips
the verdict") needs a runnable model of the case's own arithmetic.

CONTRACT -- two public names:

    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

The case's SPEC Section 2 primary metric (case.json.balance.margin_basis) is
blended barrels produced per rig-day, across both basins, for the remainder
of the quarter. Higher is better, so evaluate() returns the metric directly
(no sign flip needed, unlike a cost metric).

Mechanism modeled explicitly (this is the whole point of the case): each
option is really a small 3-variable / 3-equation linear system --
  x = Permian-producing rig-days
  y = Bakken-producing rig-days
  z = idle (relocation) rig-days
solved from the option's own stated constraints. Appendix D's real EIA
per-rig productivity rates (Permian 1,400 bbl/day/rig, Bakken 1,747
bbl/day/rig) convert the solved rig-days into a blended barrels-per-rig-day
number. This script solves that system numerically via NumPy-free Gaussian
elimination on a 3x3 matrix, mirroring the matrix method the case's D1/D2
deliverables require students to do by hand.

FLEX[] sweeps the case's own stated Modeling Assumptions that feed this
metric's arithmetic: MA1 (fleet size / Permian share), MA2 (remaining
quarter days), MA3 (relocation downtime days). MA3 is the case's own
disclosed high-sensitivity assumption -- see case.json.balance.margin_note
and RESEARCH_LOG.md for the hand-derived breakeven (11.92 days).
"""

PARAMS = {
    # --- Appendix A / MA1: fleet size and basin split ------------------------
    "total_rigs": 8.0,
    "permian_rigs": 6.0,
    "bakken_rigs": 2.0,
    # --- Dilemma: rigs the Basin Shift proposes to move -----------------------
    "rigs_moved": 2.0,
    # --- Appendix A / MA2: remaining days left in the quarter ----------------
    "remaining_days": 60.0,
    # --- Appendix A / MA3: relocation downtime per moved rig (days) ----------
    "relocation_downtime_days": 14.0,
    # --- Appendix D: real EIA new-well oil production per rig (bbl/day) ------
    "permian_bbl_per_rig_day": 1400.0,  # S1
    "bakken_bbl_per_rig_day": 1747.0,   # S2
}

# Probe 5 flexes THESE and only these: the case's own stated Modeling
# Assumptions that feed the graded primary metric's arithmetic.
FLEX = [
    "total_rigs",                 # MA1, Appendix A
    "permian_rigs",                # MA1, Appendix A
    "remaining_days",              # MA2, Appendix A
    "relocation_downtime_days",    # MA3, Appendix A -- the case's real fulcrum
]


def _solve_3x3(a, b):
    """Solve a 3x3 linear system a*x = b via Gaussian elimination with
    partial pivoting. a is a 3x3 list-of-lists, b is a length-3 list.
    Returns the solution as a length-3 list. Mirrors the matrix method
    D1/D2 ask students to perform by hand -- no external library used."""
    m = [row[:] + [b[i]] for i, row in enumerate(a)]  # augmented matrix
    n = 3
    for col in range(n):
        # partial pivot
        pivot_row = max(range(col, n), key=lambda r: abs(m[r][col]))
        m[col], m[pivot_row] = m[pivot_row], m[col]
        pivot = m[col][col]
        if abs(pivot) < 1e-12:
            raise ValueError("Singular coefficient matrix -- system has no unique solution.")
        for r in range(n):
            if r == col:
                continue
            factor = m[r][col] / pivot
            for c in range(col, n + 1):
                m[r][c] -= factor * m[col][c]
    return [m[i][n] / m[i][i] for i in range(n)]


def _option_rigdays(p, rigs_moved):
    """Build and solve the 3x3 system (x=Permian rig-days, y=Bakken rig-days,
    z=idle rig-days) for a given number of rigs moved (0 for Hold the Line,
    p['rigs_moved'] for the Basin Shift). Coefficient matrix is identical
    for both options -- only the constant vector b changes -- matching the
    case's D3 observation that both options share one coefficient matrix."""
    d = p["remaining_days"]
    l = p["relocation_downtime_days"]
    permian_remaining = p["permian_rigs"] - rigs_moved
    total_rigday_budget = p["total_rigs"] * d

    a = [
        [1.0, 1.0, 1.0],   # x + y + z = total rig-day budget
        [1.0, 0.0, 0.0],   # x = permian_remaining * d
        [0.0, 0.0, 1.0],   # z = rigs_moved * l
    ]
    b = [
        total_rigday_budget,
        permian_remaining * d,
        rigs_moved * l,
    ]
    x, y, z = _solve_3x3(a, b)
    return {"permian_days": x, "bakken_days": y, "idle_days": z, "total_budget": total_rigday_budget}


def evaluate_detail(params):
    p = dict(PARAMS)
    p.update(params or {})

    rd_a = _option_rigdays(p, p["rigs_moved"])   # Basin Shift
    rd_b = _option_rigdays(p, 0.0)                # Hold the Line

    barrels_a = p["permian_bbl_per_rig_day"] * rd_a["permian_days"] + p["bakken_bbl_per_rig_day"] * rd_a["bakken_days"]
    barrels_b = p["permian_bbl_per_rig_day"] * rd_b["permian_days"] + p["bakken_bbl_per_rig_day"] * rd_b["bakken_days"]

    blended_a = barrels_a / rd_a["total_budget"]
    blended_b = barrels_b / rd_b["total_budget"]

    detail_a = dict(rd_a, barrels=barrels_a, blended_bbl_per_rigday=blended_a)
    detail_b = dict(rd_b, barrels=barrels_b, blended_bbl_per_rigday=blended_b)
    return {"A": blended_a, "B": blended_b}, detail_a, detail_b


def evaluate(params):
    """Tier 2 probe 5 contract: evaluate(params) -> {'A': metric, 'B': metric}
    ONLY -- no extra return values. Full diagnostics (per-option breakdown)
    are in evaluate_detail(). Higher is better (blended bbl/rig-day), no
    sign flip needed."""
    r, _a, _b = evaluate_detail(params)
    return r


def breakeven_downtime_days(params=None):
    """Solve for the relocation-downtime value (days) at which the two
    options tie exactly, holding every other parameter fixed. Closed form:
    (D - L) * rB = D * rP  =>  L* = D * (1 - rP/rB)."""
    p = dict(PARAMS)
    p.update(params or {})
    d = p["remaining_days"]
    rp = p["permian_bbl_per_rig_day"]
    rb = p["bakken_bbl_per_rig_day"]
    return d * (1.0 - rp / rb)


if __name__ == '__main__':
    base, a, b = evaluate_detail({})
    win = max(base, key=base.get)
    lo = min(base, key=base.get)
    margin = 100.0 * (base[win] - base[lo]) / base[win]

    print("Option A (Basin Shift):")
    for k, v in a.items():
        print(f"  {k}: {v}")
    print("Option B (Hold the Line):")
    for k, v in b.items():
        print(f"  {k}: {v}")
    print()
    print("blended bbl/rig-day  A=%.4f  B=%.4f" % (base["A"], base["B"]))
    print("winner:", win, " margin: %.4f%%" % margin)
    print("breakeven relocation-downtime days (all else held at PARAMS): %.4f" % breakeven_downtime_days())

    print()
    print("--- Probe 5: flex each FLEX param by +-50%, report winner ---")
    for key in FLEX:
        base_val = PARAMS[key]
        for pct in (-0.5, -0.25, 0.25, 0.5):
            trial_val = base_val * (1.0 + pct)
            try:
                r = evaluate({key: trial_val})
            except ValueError as e:
                print(f"  {key} {pct:+.0%} -> {trial_val:.3f}: INVALID ({e})")
                continue
            trial_win = max(r, key=r.get)
            flip = " <-- FLIPS WINNER" if trial_win != win else ""
            print(f"  {key} {pct:+.0%} -> {trial_val:.3f}: A={r['A']:.2f} B={r['B']:.2f} winner={trial_win}{flip}")
