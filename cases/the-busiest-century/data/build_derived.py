#!/usr/bin/env python3
"""
Build the derived, de-identified extract for "The Busiest Century" from p3k14c release 2025.07
(Zenodo 10.5281/zenodo.16394072, file inst/p3k14c_scrubbed_fuzzed.csv, data CC0, attribution
requested) and the IntCal20 curve (Reimer et al. 2020, intcal.org/curves/intcal20.14c).

Usage:  python3 build_derived.py <p3k14c_scrubbed_fuzzed.csv> <intcal20.14c> <outdir>

Pipeline (fixed BEFORE any result was looked at):
  scope   : Country == USA, Province == New Mexico, SiteID present,
            100 < Age < 8000 (14C BP), 0 < Error < 300, Material not BONE or TEETH
  calibr. : IntCal20, normal likelihood, curve error added in quadrature,
            density(t) ~ exp(-(age - mu(t))^2 / (2 v(t))) / sqrt(v(t)), v = err^2 + curve_err^2,
            1-calendar-year grid, 0..12000 cal BP, each date normalised to total probability 1
  bins    : 100 calendar years, aligned so a bin starts at a multiple of 100 cal BP (BP = before 1950 CE)
  dates   : summed probability = sum over dates of the date's probability inside the bin
  sites   : expected number of sites with at least one date in the bin
            = sum over sites of [1 - product over the site's dates of (1 - p_date_in_bin)]
Writes de-identified outputs only: no SiteID, SiteName, LabID, coordinates or reference text.
Site and date numbers are random; the mapping to the database's SiteIDs is NOT written anywhere.
"""
import sys, numpy as np, pandas as pd

def load_curve(path):
    rows = []
    for l in open(path, encoding="utf8"):
        if l.startswith("#") or not l.strip():
            continue
        p = l.strip().split(",")
        rows.append((float(p[0]), float(p[1]), float(p[2])))
    return np.array(sorted(rows))

GRID = np.arange(0, 12001)

def calibrate(ages, errs, curve):
    mu = np.interp(GRID, curve[:, 0], curve[:, 1])
    sg = np.interp(GRID, curve[:, 0], curve[:, 2])
    P = np.zeros((len(ages), len(GRID)))
    for i, (a, e) in enumerate(zip(ages, errs)):
        v = e * e + sg * sg
        p = np.exp(-0.5 * (a - mu) ** 2 / v) / np.sqrt(v)
        P[i] = p / p.sum()
    return P

def binsum(P, w, off):
    G = P.shape[1]
    edges = np.arange(off, G, w)
    cs = np.concatenate([np.zeros((P.shape[0], 1)), np.cumsum(P, axis=1)], axis=1)
    return edges, cs[:, np.clip(edges + w, 0, G)] - cs[:, np.clip(edges, 0, G)]

def measures(M, sid):
    D = M.sum(0)
    S = np.zeros(M.shape[1])
    for s in pd.unique(sid):
        S += 1 - np.prod(1 - M[sid == s], axis=0)
    return D, S

def main(csv, curvep, out):
    df = pd.read_csv(csv, low_memory=False)
    nm = df[(df.Country == "USA") & (df.Province == "New Mexico")]
    q = nm[nm.SiteID.notna() & (nm.Age > 100) & (nm.Age < 8000) & (nm.Error > 0) & (nm.Error < 300)].copy()
    n_before = len(q)
    excl = q.Material.fillna("").str.upper().isin(["BONE", "TEETH"])
    q = q[~excl].reset_index(drop=True)
    print("NM rows", len(nm), "| in scope before material rule", n_before, "| excluded BONE/TEETH", int(excl.sum()),
          "| kept", len(q), "| sites", q.SiteID.nunique())
    P = calibrate(q.Age.values, q.Error.values, load_curve(curvep))
    # anonymise: random site and date numbers, no mapping saved
    rng = np.random.default_rng(1950)
    sites = pd.unique(q.SiteID)
    perm = rng.permutation(len(sites)) + 1
    smap = dict(zip(sites, perm))
    q["site_no"] = q.SiteID.map(smap)
    q["date_no"] = rng.permutation(len(q)) + 1
    q["material"] = q.Material.fillna("unknown").str.lower()
    edges, M = binsum(P, 100, 0)
    keep = [i for i in range(len(edges)) if edges[i] <= 8900]
    out_df = pd.DataFrame({"date_no": q.date_no, "site_no": q.site_no, "age_14c_bp": q.Age.astype(int),
                           "error_14c": q.Error.astype(int), "material": q.material})
    for i in keep:
        out_df["c%04d" % edges[i]] = np.round(M[:, i], 5)
    out_df = out_df.sort_values(["site_no", "date_no"]).reset_index(drop=True)
    out_df.to_csv(out + "/derived_dates_by_century.csv", index=False, float_format="%.5g")
    sid = q.site_no.values
    D, S = measures(M, sid)
    e5, M5 = binsum(P, 100, 50)
    D5, S5 = measures(M5, sid)
    tab = pd.DataFrame({"bin_start": edges[keep], "dates": D[keep], "sites": S[keep]})
    tab5 = pd.DataFrame({"bin_start": e5[:len(keep)], "dates": D5[:len(keep)], "sites": S5[:len(keep)]})
    tab.to_csv(out + "/_century_table_offset0.csv", index=False)
    tab5.to_csv(out + "/_century_table_offset50.csv", index=False)
    cnt = pd.Series(sid).value_counts()
    cnt.value_counts().sort_index().rename_axis("dates_at_site").reset_index(name="n_sites").to_csv(
        out + "/_dates_per_site_frequency.csv", index=False)
    # single-year collapse rules
    cdf = np.cumsum(P, axis=1)
    pts = {"median": (cdf < 0.5).sum(1), "mean": (P * GRID).sum(1).round().astype(int), "mode": P.argmax(1)}
    rows = []
    for nm_, pt in pts.items():
        b = (pt // 100) * 100
        d = pd.Series(b).value_counts()
        s = pd.DataFrame({"b": b, "s": sid}).drop_duplicates().groupby("b").size()
        for k in range(len(edges[keep])):
            pass
        rows.append((nm_, d, s))
    pd.to_pickle(rows, out + "/_collapse.pkl")
    # model-support rows for sensitivity_model.py: ALL NM rows with a SiteID (no scope filters), masses at 700 and 1200
    allr = nm[nm.SiteID.notna() & (nm.Age > 0) & (nm.Error > 0)].reset_index(drop=True)
    P2 = calibrate(allr.Age.values, allr.Error.values, load_curve(curvep))
    _, M2 = binsum(P2, 100, 0)
    sm = dict(zip(pd.unique(allr.SiteID), rng.permutation(allr.SiteID.nunique()) + 1))
    sup = pd.DataFrame({"site_no": allr.SiteID.map(sm), "age": allr.Age.astype(int), "err": allr.Error.astype(int),
                        "material": allr.Material.fillna("unknown").str.lower(), "m700": np.round(M2[:, 7], 6),
                        "m1200": np.round(M2[:, 12], 6)})
    sup.to_csv(out + "/_sensitivity_rows.csv", index=False)
    print("done")

if __name__ == "__main__":
    main(*sys.argv[1:4])
