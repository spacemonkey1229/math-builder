#!/usr/bin/env python3
"""The Retirement State -- reproducible pull + derivation (run 2026-10-28).

    python3 data_pull.py            # recompute everything from the saved data/ snapshot
    python3 data_pull.py --fetch    # re-download the three snapshots first, then recompute

Sources (all U.S. federal public data):
  S1  NCHS Leading Causes of Death, data.cdc.gov bi63-dtpu  (deaths, age-adjusted death rate; year, state)
  S2  Census Bureau Vintage 2019 state totals, nst-est2019-alldata.csv  (July 1 resident population estimate)
  S3  Census Bureau Vintage 2018 state age/sex/race file, sc-est2018-alldata6.csv (residents aged 65+, July 1 2017;
      17 MB, so only the derived per-state 65+ counts are kept in data/age65_2017_v2018.csv)
  S4  CDC provisional COVID-19 deaths by jurisdiction, data.cdc.gov mpx5-t7tu (Twist only)

Margin convention (stated once, used everywhere): gap divided by the WINNER's value, where the
"winner" is the state with the higher rate (the state the Fund would target on that basis).
"""
import csv, json, os, sys, statistics, itertools, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "data")
URLS = {
    "nchs_all_causes_2010_2017.json":
        "https://data.cdc.gov/resource/bi63-dtpu.json?$limit=50000&$where=cause_name='All causes' AND year>=2010",
    "nst-est2019-alldata.csv":
        "https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/national/totals/nst-est2019-alldata.csv",
    "_sc-est2018-alldata6.csv":
        "https://www2.census.gov/programs-surveys/popest/datasets/2010-2018/state/asrh/sc-est2018-alldata6.csv",
    "covid_mpx5-t7tu_cumulative.json":
        "https://data.cdc.gov/resource/mpx5-t7tu.json?$limit=50000&$where=jurisdiction_residence in('Florida','Georgia','United States') AND data_period_start='2020-01-01T00:00:00.000'",
}


def fetch():
    os.makedirs(D, exist_ok=True)
    for name, url in URLS.items():
        u = urllib.request.quote(url, safe=":/?&=$'(),")
        with urllib.request.urlopen(u, timeout=300) as r:
            open(os.path.join(D, name), "wb").write(r.read())
        print("fetched", name)
    # reduce the 17 MB age file to per-state 65+ counts (both sexes, all origins, all races, July 1 2017)
    tot, o65 = {}, {}
    for r in csv.DictReader(open(os.path.join(D, "_sc-est2018-alldata6.csv"))):
        if r["SEX"] != "0" or r["ORIGIN"] != "0":
            continue
        n, a, v = r["NAME"], int(r["AGE"]), int(r["POPESTIMATE2017"])
        tot[n] = tot.get(n, 0) + v
        if a >= 65:
            o65[n] = o65.get(n, 0) + v
    with open(os.path.join(D, "age65_2017_v2018.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["NAME", "POP_2017_V2018", "POP65PLUS_2017_V2018"])
        for n in sorted(o65):
            w.writerow([n, tot[n], o65[n]])
    os.remove(os.path.join(D, "_sc-est2018-alldata6.csv"))


def load():
    rows = json.load(open(os.path.join(D, "nchs_all_causes_2010_2017.json")))
    deaths, aadr = {}, {}
    for r in rows:
        y, s = int(r["year"]), r["state"]
        deaths[(s, y)] = int(r["deaths"])
        aadr[(s, y)] = float(r["aadr"])
    pop = {}
    for r in csv.DictReader(open(os.path.join(D, "nst-est2019-alldata.csv"), encoding="latin-1")):
        for y in range(2010, 2020):
            pop[(r["NAME"], y)] = int(r["POPESTIMATE%d" % y])
    return deaths, aadr, pop


def p65():
    out = {}
    for r in csv.DictReader(open(os.path.join(D, "age65_2017_v2018.csv"))):
        t, o = int(r["POP_2017_V2018"]), int(r["POP65PLUS_2017_V2018"])
        out[r["NAME"]] = (o, t, 100.0 * o / t)
    us_t = sum(v[1] for k, v in out.items())
    us_o = sum(v[0] for k, v in out.items())
    out["United States"] = (us_o, us_t, 100.0 * us_o / us_t)
    return out


def crude(d, p):
    return 1e5 * d / p


def margin(a, b):
    """gap / winner, winner = larger value."""
    hi, lo = max(a, b), min(a, b)
    return 100.0 * (hi - lo) / hi


def main():
    if "--fetch" in sys.argv:
        fetch()
    deaths, aadr, pop = load()
    states = sorted({s for (s, y) in deaths if s != "United States"})
    out = {}
    Y = 2017
    for s in states + ["United States"]:
        pass
    C = {s: crude(deaths[(s, Y)], pop[(s, Y)]) for s in states + ["United States"]}
    A = {s: aadr[(s, Y)] for s in states + ["United States"]}
    US_C, US_A = C["United States"], A["United States"]
    print("U.S. 2017: deaths %d pop %d crude %.2f aadr %.1f" % (deaths[("United States", Y)], pop[("United States", Y)], US_C, US_A))
    for s in ("Florida", "Georgia"):
        print(s, "deaths", deaths[(s, Y)], "pop", pop[(s, Y)], "crude %.2f" % C[s], "aadr", A[s],
              "vsUS crude %+.2f%%" % (100 * (C[s] - US_C) / US_C), "vsUS aadr %+.2f%%" % (100 * (A[s] - US_A) / US_A),
              "ratio %.4f" % (C[s] / A[s]))
    fl, ga = "Florida", "Georgia"
    print("crude margin FL-GA gap/winner %.2f%%  gap/loser %.2f%%" % (margin(C[fl], C[ga]), 100 * (C[fl] - C[ga]) / C[ga]))
    print("aadr  margin GA-FL gap/winner %.2f%%  gap/loser %.2f%%" % (margin(A[fl], A[ga]), 100 * (A[ga] - A[fl]) / A[fl]))
    print("raw counts FL/GA %.3f  FL ahead gap/winner %.2f%%" % (deaths[(fl, Y)] / deaths[(ga, Y)], margin(deaths[(fl, Y)], deaths[(ga, Y)])))
    # ranks among 50 + DC (1 = highest rate)
    def rank(d, s):
        return 1 + sum(1 for t in states if d[t] > d[s])
    print("n jurisdictions", len(states))
    for s in (fl, ga):
        print(s, "rank crude", rank(C, s), "rank aadr", rank(A, s))
    # robustness 2010-2017
    for y in range(2010, 2018):
        cf, cg = crude(deaths[(fl, y)], pop[(fl, y)]), crude(deaths[(ga, y)], pop[(ga, y)])
        print(y, "FL crude %.1f GA crude %.1f (%.1f%%) | FL aadr %.1f GA aadr %.1f (%.1f%%)" % (
            cf, cg, margin(cf, cg), aadr[(fl, y)], aadr[(ga, y)], margin(aadr[(fl, y)], aadr[(ga, y)])))
    # pairs
    pairs = list(itertools.combinations(states, 2))
    rev = []
    for a, b in pairs:
        if (C[a] - C[b]) * (A[a] - A[b]) < 0:
            rev.append((a, b, margin(C[a], C[b]), margin(A[a], A[b])))
    both20 = [r for r in rev if r[2] < 20 and r[3] < 20]
    print("pairs", len(pairs), "reverse", len(rev), "reverse & both margins <20%%", len(both20))
    big = [s for s in states if pop[(s, Y)] >= 10_000_000]
    print("states >=10M (2017):", [(s, pop[(s, Y)]) for s in big])
    bigpairs = [r for r in rev if r[0] in big and r[1] in big]
    print("reversing pairs with both >=10M:")
    for r in sorted(bigpairs, key=lambda r: -(pop[(r[0], Y)] + pop[(r[1], Y)])):
        print("   %-14s %-14s crude-margin %.1f%% aadr-margin %.1f%% %s" % (r[0], r[1], r[2], r[3], "BOTH<20" if r[2] < 20 and r[3] < 20 else ""))
    # Southeast per Census South Atlantic / East South Central?  record the three Southeast >=10M states
    se = ["Florida", "Georgia", "North Carolina"]
    for a, b in itertools.combinations(se, 2):
        print("SE pair", a, b, "crude %.1f %.1f aadr %.1f %.1f reverse=%s" % (C[a], C[b], A[a], A[b], (C[a] - C[b]) * (A[a] - A[b]) < 0))
    # 65+ shares
    sh = p65()
    for s in (fl, ga, "United States"):
        print(s, "65+ share 2017 (V2018 civ) %.2f%% (%d of %d)" % (sh[s][2], sh[s][0], sh[s][1]))
    r = sorted(((sh[s][2], s) for s in states), reverse=True)
    print("65+ share rank FL", [i for i, (v, s) in enumerate(r, 1) if s == fl][0], "GA", [i for i, (v, s) in enumerate(r, 1) if s == ga][0])
    # box plot five-number summaries (median of halves) on the 51 values
    def five(v):
        v = sorted(v)
        n = len(v)
        med = statistics.median(v)
        lo = v[: n // 2]
        hi = v[(n + 1) // 2:]
        q1, q3 = statistics.median(lo), statistics.median(hi)
        iqr = q3 - q1
        lf, uf = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        outs = [x for x in v if x < lf or x > uf]
        return dict(n=n, min=v[0], q1=q1, med=med, q3=q3, max=v[-1], iqr=iqr, lf=lf, uf=uf, outs=outs)
    cr = {s: round(C[s], 1) for s in states}
    print("crude (1dp) five:", five(list(cr.values())))
    print("aadr five:", five([A[s] for s in states]))
    print("crude ranges FL/GA positions: FL", cr[fl], "GA", cr[ga])
    # twist
    tw = json.load(open(os.path.join(D, "covid_mpx5-t7tu_cumulative.json")))
    print("twist rows", len(tw))
    for r in sorted(tw, key=lambda r: r["data_period_end"])[-3:]:
        print(r)


def tables():
    """Emit the Appendix C / D markdown and data/derived.json (facilitator-only reference values)."""
    deaths, aadr, pop = load()
    states = sorted({s for (s, y) in deaths if s != "United States"})
    Y = 2017
    C = {s: crude(deaths[(s, Y)], pop[(s, Y)]) for s in states + ["United States"]}
    A = {s: aadr[(s, Y)] for s in states + ["United States"]}
    sh = p65()
    lines = ["| Jurisdiction | Crude death rate (derived) | Age-adjusted death rate |", "|---|---|---|"]
    for s in states:
        if s in ("Florida", "Georgia"):
            lines.append("| %s | use your own value from D1 | %.1f |" % (s, A[s]))
        else:
            lines.append("| %s | %.1f | %.1f |" % (s, C[s], A[s]))
    open(os.path.join(D, "appendix_c.md"), "w").write("\n".join(lines) + "\n")
    ly = ["| Year | Florida crude (derived) | Georgia crude (derived) | Florida age-adjusted | Georgia age-adjusted |", "|---|---|---|---|---|"]
    for y in range(2010, 2017):
        ly.append("| %d | %.1f | %.1f | %.1f | %.1f |" % (y, crude(deaths[("Florida", y)], pop[("Florida", y)]),
                  crude(deaths[("Georgia", y)], pop[("Georgia", y)]), aadr[("Florida", y)], aadr[("Georgia", y)]))
    open(os.path.join(D, "appendix_d.md"), "w").write("\n".join(ly) + "\n")
    print("wrote appendix_c.md, appendix_d.md")


if __name__ == "__main__":
    if "--tables" in sys.argv:
        tables()
    else:
        main()
