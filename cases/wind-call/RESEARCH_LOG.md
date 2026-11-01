# Research Log — Wind Call

Every placeholder from the case-write pass, what was searched, what was found, and the full
arithmetic chain from raw sourced figures to the case's published numbers.

## Placeholders and resolution

| # | Placeholder | Searched | Found | Resolution |
|---|---|---|---|---|
| P01 | Cessna 208B cruise TAS, fuel flow, usable fuel, ceiling | (1) Manufacturer POH PDF (caravannation.com/208BG1000POH.pdf) — fetched, exceeded WebFetch's 10 MB content limit, abandoned. (2) General web search for "Cessna Caravan 208B gph fuel burn FL200 knots specifications" — surfaced several secondary sources with inconsistent figures (50–62 gph range). (3) Direct fetch of AOPA's published Aircraft Fact Sheet. | AOPA fact sheet: TAS 180 kn at 1,750 rpm/6,000 ft representative cruise; fuel flow 415 lb/hr (62 gal/hr); usable fuel 332 gal; service ceiling 25,000 ft (certified). | SOURCED — S1, HIGH confidence (primary aviation-association fact sheet, single internally-consistent figure set, dated aircraft variant named). |
| P02 | Winds aloft at 9,000 ft and 18,000 ft along the route | (1) General search for how to read FAA FB/FD winds-aloft codes (background only). (2) Direct fetch of `aviationweather.gov/api/data/windtemp?region=us&level=low&fcst=6&layout=off` — live API, returned real coded groups for DEN, GLD, ICT, GCK stations. | GLD (Goodland, KS — closest station to the KAPA-KICT great-circle route) raw groups: 9,000 ft = `2227+09`; 18,000 ft = `2320-15`. Decoded per the standard FD/FB format (2-digit direction/10, 2-digit speed in kt, signed 2-digit temp in C, sign omitted and implicitly negative above 24,000 ft): 9,000 ft = 220° true / 27 kt / +9°C; 18,000 ft = 230° true / 20 kt / −15°C. | SOURCED — S2, HIGH confidence, live-fetched primary FAA/NOAA product. **This is a forecast product that reissues on a 6-hour cycle** — fixed as an explicit "as of" cutoff (2026-09-18 fetch) per SPEC §5, and the case states this cutoff in Appendix C so the figures are never presented as a live-updating value. |
| P03 | Departure/destination airport coordinates | Web search for KAPA and KICT coordinates; cross-checked against Wikipedia infobox values (themselves sourced to FAA Form 5010). | KAPA 39.57000°N, 104.84944°W; KICT 37.65000°N, 97.43306°W. | SOURCED — S3, S4, HIGH confidence. |
| P04 | Great-circle distance and true course between the two airports | Not separately published anywhere for this specific pair; computed directly from S3/S4 using the standard haversine distance formula and initial-bearing (forward-azimuth) formula, Earth radius 3,440.065 nm. | 366.4 nm; true course 106.0° (see arithmetic below). | DERIVED from S3+S4 — not a citation of a third source, but a geometric calculation from two real, sourced coordinate pairs. Marked `derived: true`-equivalent in case.json's Appendix A note. |
| P05 | 14 CFR 91.211 supplemental-oxygen requirement text | Web search for exact regulation text; confirmed against eCFR (the authoritative current text of the Code of Federal Regulations). | §91.211(a)(2): oxygen required above 12,500 ft MSL for flight segments over 30 min. §91.211(a)(3): oxygen required continuously above 14,000 ft MSL. | SOURCED — S5, HIGH confidence, primary regulatory text. |
| P06 | Per-altitude (9,000 ft vs. 18,000 ft) cruise fuel-flow chart | (1) Manufacturer POH PDF — same size-limit failure as P01. (2) Two additional search framings for a summarized cruise-performance table by altitude — found only single-point figures (the same 415 lb/hr representative value, or informal forum posts with no provenance, rejected per the LOW-confidence rule). | No freely-fetchable, complete per-altitude chart. | **NOT FOUND.** Resolved as **MA1** — stated Modeling Assumption holding fuel flow constant at 62.0 gal/hr across both altitudes, rather than inventing a second uncited number. Redesign was considered (dropping the altitude-fuel-flow linkage entirely) but rejected: the case's real dilemma is specifically about how wind, not fuel-flow-by-altitude, changes the outcome, so holding fuel flow constant is the more honest simplification, not a workaround. |

## Full arithmetic: from sourced figures to the published numbers

**Distance and course (Appendix A), from S3 + S4:**

```
lat1, lon1 = 39.57000, -104.84944   (KAPA)
lat2, lon2 = 37.65000,  -97.43306   (KICT)
R = 3440.065 nm (mean Earth radius in nautical miles)

haversine:
  a = sin²(Δφ/2) + cos(φ1)·cos(φ2)·sin²(Δλ/2)
  c = 2·atan2(√a, √(1−a))
  distance = R·c = 366.4 nm

initial bearing (true course):
  y = sin(Δλ)·cos(φ2)
  x = cos(φ1)·sin(φ2) − sin(φ1)·cos(φ2)·cos(Δλ)
  bearing = atan2(y, x) normalized to [0°, 360°) = 106.0°
```

**Wind triangle at each altitude, from S1 + S2 + Appendix A:**

For each altitude, the wind vector (from S2) is converted from "blowing-from" convention to a
standard math vector (blowing-toward, standard compass-to-Cartesian conversion), then decomposed
against the unit vector along the 106.0° true course using the dot product:

```
course = 106.0°;  unit_course = (sin(106.0°), cos(106.0°)) = (0.961, −0.276)

9,000 ft wind: from 220° / 27 kt → vector components (17.355, 20.683) [E, N]
  wind_along_course (dot product)  = 17.355(0.961) + 20.683(−0.276) = 10.98 kt  (tailwind component)
  wind_cross_course                = −24.67 kt
  wind-correction angle = asin(wind_cross / TAS) = asin(−24.67/180) = −7.9°
  resultant groundspeed = TAS·cos(WCA) + wind_along = 180·cos(7.9°) + 10.98 = 189.3 kn
  heading to fly = course − WCA = 106.0° − (−7.9°) = 113.9°

18,000 ft wind: from 230° / 20 kt → vector components (15.321, 12.856) [E, N]
  wind_along_course = 15.321(0.961) + 12.856(−0.276) = 11.18 kt  (tailwind component)
  wind_cross_course = −16.58 kt
  wind-correction angle = asin(−16.58/180) = −5.3°
  resultant groundspeed = 180·cos(5.3°) + 11.18 = 190.4 kn
  heading to fly = 106.0° − (−5.3°) = 111.3°
```

**Time and fuel (Appendix B, MA1), from the groundspeeds above:**

```
9,000 ft:  time = 366.4 nm / 189.3 kn = 1.9357 hr = 116.1 min
           fuel = 1.9357 hr × 62.0 gal/hr = 120.0 gal
           gal/nm = 120.0 / 366.4 = 0.3276

18,000 ft: time = 366.4 nm / 190.4 kn = 1.9242 hr = 115.5 min
           fuel = 1.9242 hr × 62.0 gal/hr = 119.3 gal
           gal/nm = 119.3 / 366.4 = 0.3256

margin_pct = |0.3276 − 0.3256| / max(0.3276, 0.3256) × 100 = 0.60%
winner = B (One-Eight-Thousand)
```

Both totals (120.0 gal and 119.3 gal) are well under the aircraft's 332-gallon usable fuel
capacity (S1), so fuel range is not itself a binding constraint in this case — it is included in
Appendix B for completeness and as a plausibility check a sharp Hero might reach for.

## Rejected sources

- Several general-web fuel-burn figures for the Caravan in the 50–55 gph range (from charter/jet
  brokerage marketing pages, not primary aircraft-performance documents) were found and **not
  used** — no stated power setting or altitude, inconsistent with each other, and none as
  well-attributed as the AOPA fact sheet's single internally-consistent figure set.
- The manufacturer's full G1000 POH PDF (`caravannation.com/208BG1000POH.pdf`) is a real, primary,
  freely-hosted document, but exceeded this research pass's tool size limit (10 MB) both times it
  was attempted. Not rejected as unreliable — simply not fetchable in this pass. Recorded as
  `not_found[]` in case.json rather than silently worked around.

## Supplemental appendix materials

No additional appendix (map, Desmos graph, etc.) beyond the five sourced appendices was judged
necessary — the case's own Appendix A distance/course derivation and Appendix C wind table are the
load-bearing visuals, and D1's own vector-diagram deliverable is where a Hero produces the visual
representation, not something the case should pre-supply.

## Verification sweep (per case-research §7 script)

- Placeholders remaining in case.md: 0.
- Citation markers `[S1]`–`[S5]` all resolve to a `sources[]` row; no source row is uncited.
- No source graded LOW.
- `status` → `researched`.
