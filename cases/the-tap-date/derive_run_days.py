#!/usr/bin/env python3
"""Derive every Tap Date figure from NOAA NCEI GHCN-Daily station USW00014742 (Burlington Intl Airport, VT).

Usage:
  python3 derive_run_days.py --ghcn /path/to/USW00014742.csv --write-compact   # also writes data/burlington_feb_may_tenthsC.csv
  python3 derive_run_days.py                                                    # reads data/burlington_feb_may_tenthsC.csv

Source file: https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/USW00014742.csv
Units in the source are tenths of degrees C. Conversion to F is exact (no rounding); thresholds are compared
with a 1e-9 tolerance so that 32.0 F (0.0 C) counts as >= 32 and <= 32.
A "run day" = Tmax >= tx and Tmin <= tn on a day inside the 42-day window starting on the tap date.
Margin convention: |A - B| / max(A, B).
"""
import csv, os, sys, argparse, datetime as dt, statistics as st, math, json
HERE = os.path.dirname(os.path.abspath(__file__))
COMPACT = os.path.join(HERE, "data", "burlington_feb_may_tenthsC.csv")

def load(path=None):
    D = {}
    if path:
        for r in csv.DictReader(open(path)):
            d = dt.date.fromisoformat(r["DATE"])
            if 1950 <= d.year <= 2026 and (d.month in (2, 3, 4) or (d.month == 5 and d.day <= 15)):
                tx, tn = r["TMAX"].strip(), r["TMIN"].strip()
                D[d] = (int(tx) if tx else None, int(tn) if tn else None)
    else:
        for r in csv.DictReader(open(COMPACT)):
            d = dt.date.fromisoformat(r["DATE"])
            D[d] = (int(r["TMAX"]) if r["TMAX"] else None, int(r["TMIN"]) if r["TMIN"] else None)
    return D

def f_of(tenths_c):
    return tenths_c / 10.0 * 9.0 / 5.0 + 32.0

def run_days(D, year, start, L, tx, tn):
    s = dt.date(year, *start); n = 0; miss = 0
    for i in range(L):
        v = D.get(s + dt.timedelta(i))
        if v is None or v[0] is None or v[1] is None:
            miss += 1; continue
        if f_of(v[0]) >= tx - 1e-9 and f_of(v[1]) <= tn + 1e-9:
            n += 1
    return n, miss

DEFS = {"P": (35, 27), "N": (32, 32), "Q": (35, 32)}   # P primary; N plain freeze-thaw; Q warm day, any frost
A_START, B_START = (2, 20), (3, 1)

def series(D, d, start, y0=1950, y1=2025, L=42):
    tx, tn = DEFS[d]
    return [run_days(D, y, start, L, tx, tn)[0] for y in range(y0, y1 + 1)]

def fit(xs, ys):
    n = len(xs); mx = sum(xs) / n; my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs); sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys)); syy = sum((y - my) ** 2 for y in ys)
    b = sxy / sxx
    return my - b * mx, b, sxy / math.sqrt(sxx * syy)

def margin(a, b):
    return 100.0 * abs(a - b) / max(a, b)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--ghcn"); ap.add_argument("--write-compact", action="store_true")
    a = ap.parse_args()
    D = load(a.ghcn)
    if a.write_compact:
        os.makedirs(os.path.dirname(COMPACT), exist_ok=True)
        with open(COMPACT, "w", newline="") as fh:
            w = csv.writer(fh); w.writerow(["DATE", "TMAX", "TMIN"])
            for d in sorted(D):
                w.writerow([d.isoformat(), "" if D[d][0] is None else D[d][0], "" if D[d][1] is None else D[d][1]])
        print("wrote", COMPACT, len(D), "rows")
    yrs = list(range(1950, 2026))
    print("missing days in any 42-day window 1950-2025:",
          sum(run_days(D, y, s, 42, 35, 27)[1] for y in yrs for s in (A_START, B_START)))
    print("year,PA,PB,NA,NB,QA,QB")
    S = {d: (series(D, d, A_START), series(D, d, B_START)) for d in DEFS}
    for i, y in enumerate(yrs):
        print(y, *[S[d][k][i] for d in DEFS for k in (0, 1)], sep=",")
    recs = {"1950-1979": (1950, 1979), "1976-2005": (1976, 2005), "1991-2020": (1991, 2020), "1996-2025": (1996, 2025),
            "2006-2025": (2006, 2025), "1950-2025": (1950, 2025)}
    for d in DEFS:
        print("DEF", d, DEFS[d])
        for k, (y0, y1) in recs.items():
            ma = st.mean(S[d][0][y0 - 1950:y1 - 1950 + 1]); mb = st.mean(S[d][1][y0 - 1950:y1 - 1950 + 1])
            wa = sum(x > y for x, y in zip(S[d][0][y0 - 1950:y1 - 1950 + 1], S[d][1][y0 - 1950:y1 - 1950 + 1]))
            wb = sum(x < y for x, y in zip(S[d][0][y0 - 1950:y1 - 1950 + 1], S[d][1][y0 - 1950:y1 - 1950 + 1]))
            print(f"  {k}: A {ma:.2f}  B {mb:.2f}  winner {'A' if ma > mb else 'B'} {margin(ma, mb):.1f}%  seasons A>B {wa}  B>A {wb}")
        aa, ab, ar = fit(yrs, S[d][0]); ba, bb, br = fit(yrs, S[d][1])
        print(f"  fit 1950-2025: A y={aa:.3f}+{ab:.5f}x r={ar:.3f}; B y={ba:.3f}+{bb:.5f}x r={br:.3f}; cross {(ba - aa) / (ab - bb):.1f}")
        print("  2026 season:", run_days(D, 2026, A_START, 42, *DEFS[d])[0], run_days(D, 2026, B_START, 42, *DEFS[d])[0])
