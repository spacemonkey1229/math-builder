"""Sensitivity model for The Tap Date (SPEC section 2, case-readiness Tier 2 probe 5).

CONTRACT: evaluate(params) -> {"A": metric, "B": metric}, higher wins.
Metric = mean run days over the judging record (default 1996-2025), A = Feb 20 start, B = Mar 1 start.
A run day = daily high >= 32 + tmax_margin F and daily low <= 32 - tmin_margin F, counted inside a window of
window_len days from the tap date. The Primary Rule is tmax_margin 3, tmin_margin 5 (35 F / 27 F), window 42.
Expressing the thresholds as margins from freezing makes a +/-50% flex meaningful (a +/-50% flex of the
raw 35 F or 27 F would be 17.5-52.5 F, which is not a sensible weather rule).

FLEX (what probe 5 sweeps): the three stated assumptions MA1 (window_len), MA2 (tmax_margin, tmin_margin).
The judging record is a scope choice fixed before results (MA5) and is varied separately in the main block,
as is the Plain Freeze-Thaw rule (margins 0 and 0, MA3). The weather data are cited (probe 6 covers them).

Data: data/burlington_feb_may_tenthsC.csv (NOAA NCEI GHCN-Daily USW00014742, tenths of C), made by
derive_run_days.py. evaluate_twist(): the 2026 season, which is facilitator-only, post-decision.
"""
import os, csv, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__))
_D = {}
for _r in csv.DictReader(open(os.path.join(HERE, "data", "burlington_feb_may_tenthsC.csv"))):
    _D[dt.date.fromisoformat(_r["DATE"])] = (int(_r["TMAX"]) if _r["TMAX"] else None, int(_r["TMIN"]) if _r["TMIN"] else None)

PARAMS = {
    "window_len": 42.0,        # MA1: productive life of a tap hole, days
    "tmax_margin": 3.0,        # MA2: day's high must be at least 32 + this (F)  -> 35
    "tmin_margin": 5.0,        # MA2: night's low must be at most 32 - this (F)  -> 27
    "record_start": 1996.0,    # MA5: scope fixed before results (not flexed)
    "record_end": 2025.0,
}
FLEX = ["window_len", "tmax_margin", "tmin_margin"]


def _f(t):
    return t / 10.0 * 9.0 / 5.0 + 32.0


def _season(year, start, p):
    s = dt.date(year, *start); n = 0
    L = int(round(p["window_len"]))
    for i in range(L):
        v = _D.get(s + dt.timedelta(i))
        if v and v[0] is not None and v[1] is not None and _f(v[0]) >= 32 + p["tmax_margin"] - 1e-9 and _f(v[1]) <= 32 - p["tmin_margin"] + 1e-9:
            n += 1
    return n


def _mean(start, p, y0=None, y1=None):
    y0 = int(y0 or p["record_start"]); y1 = int(y1 or p["record_end"])
    v = [_season(y, start, p) for y in range(y0, y1 + 1)]
    return sum(v) / len(v)


def evaluate(params):
    p = dict(PARAMS); p.update(params or {})
    return {"A": _mean((2, 20), p), "B": _mean((3, 1), p)}


def evaluate_twist(params):
    """The 2026 season (facilitator-only, post-decision) under the same rule."""
    p = dict(PARAMS); p.update(params or {})
    return {"A": float(_season(2026, (2, 20), p)), "B": float(_season(2026, (3, 1), p))}


def margin_pct(r):
    hi, lo = max(r.values()), min(r.values())
    return 100.0 * (hi - lo) / hi          # |A-B| / larger (the case's convention)


if __name__ == "__main__":
    base = evaluate({}); print("base", {k: round(v, 2) for k, v in base.items()}, "winner", max(base, key=base.get), "margin %.1f%%" % margin_pct(base))
    tw = evaluate_twist({}); print("twist 2026", tw)
    for name in FLEX:
        for mult in (0.5, 1.5):
            r = evaluate({name: PARAMS[name] * mult}); w = max(r, key=r.get)
            print(f"{name:12s} x{mult}: value {PARAMS[name]*mult:5.1f}  A {r['A']:.2f} B {r['B']:.2f} winner {w if r['A']!=r['B'] else 'TIE'} margin {margin_pct(r):5.1f}%  twist {evaluate_twist({name: PARAMS[name]*mult})}")
    print("-- Plain Freeze-Thaw (margins 0,0):", {k: round(v, 2) for k, v in evaluate({"tmax_margin": 0, "tmin_margin": 0}).items()})
    print("-- Warm Day Any Frost (3,0):", {k: round(v, 2) for k, v in evaluate({"tmin_margin": 0}).items()})
    for lab, (a, b) in {"1950-1979": (1950, 1979), "1991-2020": (1991, 2020), "1950-2025": (1950, 2025)}.items():
        r = evaluate({"record_start": a, "record_end": b}); print(lab, {k: round(v, 2) for k, v in r.items()}, "margin %.1f%%" % margin_pct(r))
