#!/usr/bin/env python3
"""Reproduce every number in Up or Out from the live NYC Open Data API (dataset ic3t-wcy2).
Run: python3 data_pull.py [outdir]   (default: ./_pull, not committed). Pull used by the case: 2026-10-28.
Cleaning order (row counts printed): exactly-one-flag -> enlargement 50-5000 sq ft -> cost > 0 ->
pre-filed >= 2011 -> keep first doc per job -> $/sq ft within 20-2000.
Outputs clean.json and prints the 9-size table, expected costs and margin (gap / lower value)."""
import json, os, sys, statistics as st, urllib.parse, urllib.request
OUT = sys.argv[1] if len(sys.argv) > 1 else "_pull"; os.makedirs(OUT, exist_ok=True)
BASE = "https://data.cityofnewyork.us/resource/ic3t-wcy2.json"
SEL = "job__,doc__,borough,pre__filing_date,job_status_descrp,initial_cost,horizontal_enlrgmt,vertical_enlrgmt,enlargement_sq_footage,building_type,job_type"
WHERE = "job_type='A1' AND building_type='1-2-3 FAMILY' AND job_status_descrp='SIGNED OFF'"
rows, off = [], 0
while True:
    q = urllib.parse.urlencode({"$select": SEL, "$where": WHERE, "$order": "job__,doc__", "$limit": 50000, "$offset": off})
    d = json.load(urllib.request.urlopen(BASE + "?" + q, timeout=180)); rows += d
    if len(d) < 50000: break
    off += 50000
print("raw rows", len(rows))
out = []
for r in rows:
    h = r.get("horizontal_enlrgmt", "").strip().upper() == "Y"; v = r.get("vertical_enlrgmt", "").strip().upper() == "Y"
    if h == v: continue
    try: sf = float(r["enlargement_sq_footage"]); c = float(str(r["initial_cost"]).replace("$", "").replace(",", ""))
    except Exception: continue
    out.append(dict(r, opt="H" if h else "V", sf=sf, cost=c))
print("one flag", len(out))
out = [r for r in out if 50 <= r["sf"] <= 5000]; print("50-5000 sf", len(out))
out = [r for r in out if r["cost"] > 0]; print("cost>0", len(out))
out = [r for r in out if int(r["pre__filing_date"][-4:]) >= 2011]; print("prefiled>=2011", len(out))
seen, o2 = set(), []
for r in sorted(out, key=lambda r: (r["job__"], r["doc__"])):
    if r["job__"] in seen: continue
    seen.add(r["job__"]); o2.append(r)
print("first doc per job", len(o2))
out = [dict(r, ppsf=r["cost"] / r["sf"]) for r in o2 if 20 <= r["cost"] / r["sf"] <= 2000]; print("ppsf 20-2000", len(out))
json.dump(out, open(os.path.join(OUT, "clean.json"), "w"))
SIZES = list(range(250, 451, 25))
def med(o, s, hw=50): return st.median(r["ppsf"] for r in out if r["opt"] == o and s - hw <= r["sf"] <= s + hw)
cv = [s * med("V", s) for s in SIZES]; ch = [s * med("H", s) for s in SIZES]
for s, a, b in zip(SIZES, cv, ch): print(s, round(med("V", s), 1), round(med("H", s), 1), round(a), round(b))
ev, eh = st.mean(cv), st.mean(ch); print("expected cost V", round(ev), "H", round(eh), "margin %", round(100 * abs(ev - eh) / min(ev, eh), 1))
