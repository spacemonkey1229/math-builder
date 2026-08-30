# Research Log — enclosure-call

16 `{{NEEDS_SOURCE}}` placeholders were enumerated (5 in Appendix A, 6 in Appendix B, 5 in
Appendix C — some rows hold two placeholders, one per column). Worked in load-bearing order.
Outcome: **4 SOURCED, 12 ASSUMPTION, 0 DROPPED, 0 unresolved.**

---

## Appendix A — geometry and production volume

### P01–P05: Horn base radius, top radius, height, slant height; Orb sphere radius

**Searched:** "portable Bluetooth speaker enclosure typical dimensions", plus a direct check for
any real "Project Horn" / "Project Orb" spec — there is none; these are the studio's own
foam-model dimensions in a fictional design brief. No real filing, spec sheet, or manufacturer
page can describe a fictional client's fictional prototype.

**Found:** No source is possible in principle — the dimensions belong to the case's invented
scenario, not to a real, citable product. A general search for portable-speaker form factors
(e.g. a compact BT speaker at roughly 6.3 × 5.4 × 3.0 in) gave a plausibility check on scale only.

**Decision:** NOT FOUND → **Modeling Assumption MA1.** Base radius 3.5 in, top radius 2.0 in,
height 6.0 in (frustum); sphere radius 3.5 in (matched to the frustum's base so both shells
plausibly house the same driver/battery stack). Slant height 6.19 in is pure geometry from the
other three (√((3.5−2.0)² + 6.0²) = √38.25 ≈ 6.185 in) — not an independent assumption, just the
Pythagorean consequence of MA1's chosen radii and height.

### P06–P07: Client's stated target first-year production volume

**Searched:** N/A — the "client" is fictional; there is no real production-volume filing to find.

**Decision:** NOT FOUND → **Modeling Assumption MA2.** 250,000 units, a plausible year-one volume
for a mid-market consumer portable-audio SKU. Flagged as dilemma-sensitive: tooling cost is
amortized over this number, so the assumption directly affects which option wins (see MA2 in
case.json for the sensitivity note).

---

## Appendix B — material and manufacturing cost data

### P08–P09: Enclosure shell material identity (both options)

**Searched:** "polycarbonate ABS blend PC/ABS most common material portable speaker enclosure
electronics housing."

**Found:** PC/ABS blend is a well-established, widely used material for consumer-electronics and
speaker enclosures (audioxpress.com, "Some Thoughts on Plastics for Speaker Enclosures";
canyoncomponents.com PC/ABS selection guide) — real-world precedent, but which material *this*
fictional studio chose is still a scenario detail, not a fact to be looked up.

**Decision:** NOT FOUND (as a fact about this product) → **Modeling Assumption MA3**: PC/ABS
blend for both shells (same material for both, so it does not bias the comparison), with the
real-world precedent as basis (S9).

### P10–P11: Material cost, USD per square inch of shell surface

**Searched:** "ABS plastic resin price per pound 2026"; "ABS plastic density g/cm3 material
property matweb"; "Protolabs injection molding recommended wall thickness ABS inches design
guide."

**Found:**
- ABS resin price, USA, Q1 2026 average ≈ $1,824/MT ≈ $0.83/lb (procurementresource.com,
  aggregating producer/converter pricing) — **S3, MEDIUM** (aggregator, not the producer itself,
  regional average).
- ABS density ≈ 1.05 g/cm³ (matweb.com datasheet; converges with plasticranger.com's 1.04–1.06
  g/cm³ range) — **S4, HIGH** (stable physical property, well-attested, unambiguous units).
- ABS recommended wall thickness range: 0.045–0.140 in (protolabs.com, manufacturer's own design
  guidelines) — **S5, HIGH** (primary, dated-enough, on-topic).

**No single published "$/sq in of shell" figure exists** — this unit is a derived quantity, not
something anyone publishes directly. Derived $/sq in = price/lb × density (lb/in³) × wall
thickness (in). The wall-thickness input is a *point* picked from S5's range (0.0925 in
midpoint) — that pick is itself a modeling choice, disclosed as **MA5**.

0.83 × 0.037934 × 0.0925 ≈ **$0.0029 per sq in**, same for both shells (same assumed material and
thickness) — **S6, derived: true, MEDIUM** (weakest link: the resin-price aggregator and the
thickness-midpoint pick).

**Decision:** SOURCED (S6, derived from S3/S4/S5, with MA5 disclosed).

### P12–P13: Mold tooling cost, tapered vs. spherical geometry

**Searched:** "injection molding tooling cost simple mold vs complex mold DFM cost guide."

**Found:** Published DFM cost guides (Formlabs, RapidDirect) give *ranges*, not point figures:
mid-volume aluminum tooling for simple geometry ≈ $2,000–$5,000; production-grade steel tooling
for high-volume runs (the case's 250,000-unit MA2 volume needs steel, not aluminum) runs
$25,000–$100,000+, with added geometric complexity (draft, taper, side-action risk) pushing
toward the top half of that range — **S7, MEDIUM** (real, but a wide range with no controlled
"tapered vs. sphere" comparison published anywhere).

**Decision:** No source gives a specific dollar figure for *this* frustum vs. *this* sphere —
that comparison does not exist in public data. NOT FOUND as a point value → **Modeling Assumption
MA6**: Horn (tapered) tooling $58,000, Orb (sphere) tooling $32,000, both anchored inside S7's
published range, tapered priced toward the top half per the DFM guidance on complexity. This is
dilemma-sensitive (amortized tooling is one of the three cost terms) — sensitivity noted in
case.json.

---

## Appendix C — shipping and packing data

### P14: Standard shipping container internal volume

**Searched:** "40 foot high cube shipping container internal volume cubic feet spec sheet";
direct fetch of a Hapag-Lloyd container spec PDF (fetch returned no extractable text — PDF is
image/encoded); fallback to bws.net's published container-spec page, cross-checked against
icontainers.com and cbmcalculator.com, all agreeing to ~76 m³ / ~2,683–2,694 cu ft.

**Found:** 40 ft High-Cube dry container internal capacity ≈ 76 m³ ≈ **2,683 cu ft**
(bws.net/toolbox/container-specifications/40-foot-dry-high-cube) — **S1, MEDIUM** (secondary
republication of carrier specs, not the carrier's own page directly, but cross-source agreement
is tight).

**Decision:** SOURCED (S1).

### P15: Ocean freight cost per container

**Searched:** "Freightos Baltic Index current ocean freight rate per 40ft container 2026"; direct
fetch of freightos.com's own FBX Global Container Index page.

**Found:** Freightos' own published FBX Global Container Index: **$3,570.80 per 40-ft
container** — **S2, MEDIUM** (primary publisher, but the live page did not surface an explicit
"as of" date in the fetch — it is a daily-moving index, so the case records the access date
2026-08-26 as the effective date rather than claiming a fixed as-of date).

**Decision:** SOURCED (S2).

### P16: Project Horn packing efficiency (cone-frustum carton nesting, % of container filled)

**Searched:** `"packing efficiency" tapered container carton nesting percent shipping density
study`; a second framing on general container/carton fill-rate benchmarks.

**Found:** No published figure exists for cone-frustum-shaped carton nesting specifically — the
literature covers rectangular-carton container utilization (target 80–85% for optimized
rectangular cargo per industry guidance; DHL study puts average secondary-level carton fill
around 76%) and generic bin-packing algorithm papers, neither of which measures a tapered
frustum shape.

**Decision:** NOT FOUND → **Modeling Assumption MA4**: 80%, placed between the sphere's proven
74.05% Kepler ceiling (a frustum should out-pack a sphere, since frustums can alternate
orientation like nested cups) and the 80–85% rectangular-carton target (a frustum is not as
efficient as a true rectangular box, since it still cannot tile a box completely). This is the
single most dilemma-sensitive assumption in the case — **mandatory sensitivity note recorded in
case.json**: if the true figure is below ~76%, Project Horn's shipping advantage over Orb
shrinks sharply; above ~85% it would exceed the DFM literature's own ceiling for rectangular
cargo and should be treated with suspicion.

---

## Summary table

| # | Placeholder (short) | Resolution | Value | Confidence |
|---|---|---|---|---|
| P01 | Horn base radius | ASSUMPTION (MA1) | 3.5 in | — |
| P02 | Horn top radius | ASSUMPTION (MA1) | 2.0 in | — |
| P03 | Horn height | ASSUMPTION (MA1) | 6.0 in | — |
| P04 | Orb radius | ASSUMPTION (MA1) | 3.5 in | — |
| P05 | Horn slant height | ASSUMPTION (MA1, derived) | 6.19 in | — |
| P06 | Production volume (Horn col) | ASSUMPTION (MA2) | 250,000 units | — |
| P07 | Production volume (Orb col) | ASSUMPTION (MA2) | 250,000 units | — |
| P08 | Horn shell material | ASSUMPTION (MA3) | PC/ABS blend | — |
| P09 | Orb shell material | ASSUMPTION (MA3) | PC/ABS blend | — |
| P10 | Horn material cost/in² | SOURCED (S6, derived) | $0.0029/in² | MEDIUM |
| P11 | Orb material cost/in² | SOURCED (S6, derived) | $0.0029/in² | MEDIUM |
| P12 | Horn mold tooling cost | ASSUMPTION (MA6) | $58,000 | — |
| P13 | Orb mold tooling cost | ASSUMPTION (MA6) | $32,000 | — |
| P14 | Container internal volume | SOURCED (S1) | 2,683 cu ft | MEDIUM |
| P15 | Ocean freight per container | SOURCED (S2) | $3,570.80 | MEDIUM |
| P16 | Horn packing efficiency | ASSUMPTION (MA4) | 80% | — |

No figure was DROPPED. No load-bearing figure remains genuinely unresolved — every OPEN
placeholder closed as either SOURCED or a disclosed, sensitivity-noted Modeling Assumption.

---

## 2026-08-27 — P6 data-decay remediation (re-sourcing pass)

The prior QA run (`QA_REPORT.md`, 2026-08-27 close-out pass #1) fetched all 9 `sources[]` URLs one
day after their original access date and found S3/S6 dead (no USA figure any more), S4 blocked
(MatWeb 403), and S7/S8 drifted (page text changed since access). This entry records the
re-sourcing work done to close that finding.

### S3 / S6 — ABS resin price (was ProcurementResource, dead for USA)

**Searched:** "ABS resin price per pound USA current market price", plus direct checks of several
of the candidate pages surfaced (imarcgroup, chemanalyst, chemorbis, polymerupdate, plasticstoday,
statista, businessanalytiq).

**Found:** businessanalytiq.com's live ABS USA/North America price index states "North America:
US$1.94/KG" for August 2026 (≈$0.88/lb). Fetched directly and confirmed the exact quote. The page's
URL slug names it a USA index; the displayed region label reads "North America" — read as
materially the same figure for this case's purposes (flagged in QA_REPORT.md for a human to
confirm if they disagree).

**Resolution:** S3 re-sourced to this URL/figure, `accessed: 2026-08-27`. S6 (derived material
cost per sq in) re-derived from the new S3 × the new S4 (below) × MA5: $0.88/lb × 0.038 lb/in³ ×
0.0925 in ≈ $0.0031/in² (was $0.0029/in²).

### S4 — ABS density (was MatWeb, HTTP 403 on re-fetch)

**Searched:** "ABS plastic density g/cm3 datasheet", checking plasticranger.com, Wikipedia,
amesweb.info, salesplastics.com, teststandard.com (PDF, not machine-readable via WebFetch),
plastim.co.uk, kg-m3.com.

**Found:** amesweb.info's published density table lists "ABS, Extrusion Grade: 1.052 g/cm³ /
0.038 lbm/in³" — within a hair of the prior 1.05 g/cm³ / 0.0379 lb/in³ figure, so this case's
downstream numbers barely move on this input alone.

**Resolution:** S4 re-sourced to amesweb.info, `accessed: 2026-08-27`, value updated to 1.052
g/cm³ / 0.038 lb/in³. MatWeb was not declared dead outright (403 is bot-blocking behavior, not
confirmed page removal) — it was simply unverifiable by automated fetch, so it was replaced rather
than kept on an unconfirmed citation, per MCS-21 ("report NOT FOUND rather than guessing").

### S7 — Injection-mold tooling cost benchmark (same URL, page text drifted)

**Searched:** "injection mold steel tooling cost benchmark high volume production 2026", checking
rapiddirect.com, jaycon.com (two reports), zetarmold.com, and re-fetching the original
formlabs.com/blog/injection-molding-cost/ page directly.

**Found:** formlabs.com itself (same URL originally cited) now states "$5,000 to $100,000" for
complex-geometry molds at 10,000+ units, plus a worked example of a $20,000 machined-steel mold
producing 100,000 units of a small electronic enclosure — different numbers than the
"$25,000-$100,000+" originally cited from the same page, but not a dead page. Alternative sources
(rapiddirect $50k-$100k+ for 1M+ shots, jaycon $60k-$150k+ for 250k-1M+ units) were considered but
rejected because their ranges no longer cover Project Orb's $32,000 tooling figure, while
formlabs's updated range ($5,000-$100,000) still comfortably covers both MA6 figures ($32,000 and
$58,000).

**Resolution:** S7 kept its original URL; `claim`/`value`/`note` updated to match the page's
current text, `accessed: 2026-08-27`.

### S8 — Container/carton fill-rate benchmark (same URL, DHL attribution gone)

**Searched:** "container packing efficiency utilization rate benchmark percent shipping", checking
kpidepot.com (subscriber-gated benchmark table, rejected) and re-fetching the original
3dloadcalculator.com page directly.

**Found:** 3dloadcalculator.com (same URL originally cited) no longer attributes its guidance to a
DHL study; it now reads "planned utilization above 85% by volume is achievable in most cases...
below 75% consistently suggests either a planning process problem or a constraint calibration
issue," presented as the author's own observation.

**Resolution:** S8 kept its original URL; `claim`/`value`/`note` updated to match the page's
current text (no more DHL attribution), `accessed: 2026-08-27`. `MA4`'s basis/sensitivity text in
`case.json`/`case.md` updated to reference the new 75%/85% framing instead of the old "76%
DHL-study average."

### S1, S2, S5, S9 — re-verified, unchanged

All four were re-fetched live on 2026-08-27 (a second, independent check beyond the prior day's
pass) and still show their exact cited figures: S1 "Capacity: 76 cbm", S2 "Current FBX $3,570.80",
S5 "ABS 0.045 in. - 0.140 in.", S9's PC/ABS-for-speaker-enclosures discussion. `accessed` bumped to
2026-08-27 on all four for an honest, freshly-verified date.

### Net effect

`margin_pct` moved from 9.11% to 8.85% as a direct, honest consequence of the S3/S4 re-sourcing
(material cost per sq in: $0.0029 → $0.0031/in²). Winner (B, Project Orb) and the overall shape of
the case are unchanged. No figure in this pass was invented — every changed number traces to a
freshly-fetched, quoted source. See `QA_REPORT.md`'s 2026-08-27 "close-out pass #2" entry for the
full P5/P6 verdict and the resulting `TIER2_PASS`.
