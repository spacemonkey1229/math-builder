#!/usr/bin/env python3
"""Facilitator-side checks computed from derived_dates_by_century.csv alone (no raw database needed).
Usage: python3 check_figures.py   (run from anywhere)"""
import os, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__))
x = pd.read_csv(os.path.join(H, "derived_dates_by_century.csv"))
cols = [c for c in x.columns if c[0] == "c" and c[1:].isdigit()]
start = np.array([int(c[1:]) for c in cols])
cnt = x.site_no.value_counts()

def meas(sub):
    D = sub[cols].sum().values
    S = sum((1 - (1 - g[cols]).prod()).values for _, g in sub.groupby("site_no"))
    return D, S

def top(v, n=3):
    o = np.argsort(-v, kind="stable")[:n]
    return [(int(start[i]), round(float(v[i]), 1)) for i in o]

def show(name, sub):
    D, S = meas(sub)
    print(f"{name}: dates={len(sub)} sites={sub.site_no.nunique()} | dates top {top(D)} | sites top {top(S)} "
          f"| D700 {D[7]:.1f} D1200 {D[12]:.1f} S700 {S[7]:.1f} S1200 {S[12]:.1f}")

show("all", x)
for k in (1, 5, 10):
    show(f"drop {k} heaviest", x[~x.site_no.isin(cnt.index[:k])])
    print("   dates at dropped sites:", int(cnt.iloc[:k].sum()), cnt.iloc[:k].tolist())
for m in (5, 10):
    show(f"sites with >= {m} dates", x[x.site_no.isin(cnt.index[cnt >= m])])
show("sites with exactly 1 date", x[x.site_no.isin(cnt.index[cnt == 1])])
t700 = x.groupby("site_no")["c0700"].sum().sort_values(ascending=False)
t1200 = x.groupby("site_no")["c1200"].sum().sort_values(ascending=False)
print("heaviest contributor to Dates 700: %.1f (%.1f%% of the century); to Dates 1200: %.1f (%.1f%%)" % (
    t700.iloc[0], 100 * t700.iloc[0] / t700.sum(), t1200.iloc[0], 100 * t1200.iloc[0] / t1200.sum()))
# cluster bootstrap over sites
sites = x.site_no.unique()
DM = np.array([x[x.site_no == s][cols].sum().values for s in sites])
SM = np.array([(1 - (1 - x[x.site_no == s][cols]).prod()).values for s in sites])
rng = np.random.default_rng(20261028); B = 2000; wd = ws = 0
for _ in range(B):
    i = rng.integers(0, len(sites), len(sites)); d = DM[i].sum(0); s = SM[i].sum(0)
    wd += d[7] > d[12]; ws += s[12] > s[7]
print("bootstrap (B=2000, seed 20261028): P(Dates 700 > 1200) = %.3f ; P(Sites 1200 > 700) = %.3f" % (wd / B, ws / B))
D, S = meas(x)
print("plateau: dates 600-1200 min/max = %.3f ; 1-date sites = %d of %d" % (D[6:13].min() / D.max(), (cnt == 1).sum(), len(cnt)))
