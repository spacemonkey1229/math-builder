#!/usr/bin/env python3
"""
Sensitivity model -- The Busiest Century.

Contract per skills/case-readiness/scripts/example_sensitivity_model.py:
    PARAMS, FLEX, evaluate(params) -> {"A","B"} (higher is better), evaluate_twist(params).

Metric: blended headline score of an option's century,
    score = (1 - s) * (dates in the century / dates in the better of the two centuries)
          +      s  * (sites in the century / sites in the better of the two centuries)
A = the Dates Wall century (700-799 cal BP at base), B = the Sites Wall century (1200-1299 cal BP).
At base the "better of the two" equals the largest value anywhere in Appendix B for each reading.
Margin convention: (winner - loser) / winner.

Data: data/sensitivity_rows.csv = every New Mexico row with a SiteID in p3k14c release 2025.07
(Zenodo 10.5281/zenodo.16394072), WITHOUT the scope rules applied, with the probability mass each
IntCal20-calibrated date puts in the 700-799 and 1200-1299 cal BP centuries. Site numbers are random.
This lets the scope thresholds (M1) be flexed in BOTH directions.

FLEX = the stated assumptions a student may challenge: the weight s (M5) and the three numeric scope
thresholds (M1). Cited database values are not flexed (P6 covers cited data). BONE/TEETH are excluded
(M1) and are not flexed.
"""
import csv, os
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROWS = []
with open(os.path.join(_HERE, "data", "sensitivity_rows.csv"), encoding="utf8") as _f:
    for _r in csv.DictReader(_f):
        _ROWS.append((int(_r["site_no"]), int(_r["age"]), int(_r["err"]), _r["material"],
                      float(_r["m700"]), float(_r["m1200"])))
_SITE = np.array([r[0] for r in _ROWS])
_AGE = np.array([r[1] for r in _ROWS])
_ERR = np.array([r[2] for r in _ROWS])
_MAT = np.array([r[3] for r in _ROWS])
_M7 = np.array([r[4] for r in _ROWS])
_M12 = np.array([r[5] for r in _ROWS])

PARAMS = {
    # --- stated assumptions (Appendix E) -- the dials FLEX sweeps -------------
    "s": 0.50,          # M5 weight on the sites reading
    "age_min": 100.0,   # M1 lower limit of 14C age (exclusive)
    "age_max": 8000.0,  # M1 upper limit of 14C age (exclusive)
    "err_max": 300.0,   # M1 ceiling on 14C error (exclusive)
    # --- twist only (not flexed) -------------------------------------------------
    "n_drop": 0.0,         # Twist part 1: set aside the n most heavily dated sites
    "min_dates": 0.0,      # Twist part 2: keep only sites with at least this many dates
}
FLEX = ["s", "age_min", "age_max", "err_max"]


def _centuries(p):
    keep = (_AGE > p["age_min"]) & (_AGE < p["age_max"]) & (_ERR > 0) & (_ERR < p["err_max"]) \
        & ~np.isin(_MAT, ["bone", "teeth"])
    sites, counts = np.unique(_SITE[keep], return_counts=True)
    n = int(round(p["n_drop"]))
    if n > 0:
        drop = sites[np.argsort(-counts, kind="stable")[:n]]
        keep &= ~np.isin(_SITE, drop)
    md = int(round(p["min_dates"]))
    if md > 0:
        sites2, counts2 = np.unique(_SITE[keep], return_counts=True)
        keep &= np.isin(_SITE, sites2[counts2 >= md])
    d7, d12 = _M7[keep].sum(), _M12[keep].sum()
    s7 = s12 = 0.0
    for s in np.unique(_SITE[keep]):
        m = (_SITE == s) & keep
        s7 += 1 - np.prod(1 - _M7[m]); s12 += 1 - np.prod(1 - _M12[m])
    return float(d7), float(d12), float(s7), float(s12)


def evaluate(params):
    p = dict(PARAMS); p.update(params or {})
    d7, d12, s7, s12 = _centuries(p)
    dm, sm = max(d7, d12), max(s7, s12)
    s = p["s"]
    a = (1 - s) * d7 / dm + s * s7 / sm
    b = (1 - s) * d12 / dm + s * s12 / sm
    return {"A": float(a), "B": float(b)}


def evaluate_twist_part1(params):
    """Twist part 1 (threatens A): the single most heavily dated site is set aside."""
    p = dict(PARAMS); p.update(params or {}); p["n_drop"] = 1
    return evaluate(p)


def evaluate_twist(params):
    """Twist part 2 (threatens B, the base winner): keep only the sites with at least 10 dates
    (same release, withheld analysis). Part 1 is evaluate_twist_part1."""
    p = dict(PARAMS); p.update(params or {}); p["min_dates"] = 10
    return evaluate(p)


if __name__ == "__main__":
    for name, f in (("base", evaluate), ("twist part 1 (heaviest site set aside)", evaluate_twist_part1),
                    ("twist part 2 (sites with 10+ dates only)", evaluate_twist)):
        r = f({})
        hi, lo = max(r.values()), min(r.values())
        print(name, {k: round(v, 4) for k, v in r.items()}, "margin (gap/winner) %.2f%%" % (100 * (hi - lo) / hi))
    print("centuries base :", [round(float(x), 1) for x in _centuries(PARAMS)])
    t = dict(PARAMS); t["min_dates"] = 10
    print("centuries twist part 2:", [round(float(x), 1) for x in _centuries(t)])
    for k in FLEX:
        for f in (0.5, 1.5):
            r = evaluate({k: PARAMS[k] * f}); hi, lo = max(r.values()), min(r.values())
            print(k, f, "A %.4f B %.4f" % (r["A"], r["B"]), "winner", max(r, key=r.get), "margin %.2f%%" % (100 * (hi - lo) / hi))
