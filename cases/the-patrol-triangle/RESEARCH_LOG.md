# Research Log: Patrol Triangle

One row per placeholder from `case-write`, in load-bearing order.

## P01 — Reserve total area (Appendix A)

**Searched:** "Ol Pejeta Conservancy total area acres square kilometers official"; direct fetch of `en.wikipedia.org/wiki/Ol_Pejeta_Conservancy`; direct fetch attempt of `olpejetaconservancy.org/who-we-are/` (404) and the homepage (no area figure present on the page as crawled).

**Found:** 360 km² (90,000 acres / 140 sq mi), stated on Wikipedia and reportedly matching the conservancy's own official site per search-engine summary, though a direct fetch of an official page stating the figure in hand was not achieved this session.

**Decision:** SOURCED as S1, confidence MEDIUM (not HIGH — no single primary document was directly fetched and confirmed to contain the figure, even though it is well-corroborated across independent sources and not contested).

## P02 — Real patrol-team density standard (Appendix A)

**Searched:** "Ol Pejeta Conservancy number of rangers anti-poaching patrol vehicle speed limit km/h"; direct fetch of the Wikipedia article's "Poaching and security" section.

**Found:** "There is a coverage rate of one rhino patrol team to 14 square kilometres (1,400 ha)." Also found in the same section: "a fence attendant for every 7 kilometres of fence" — considered as an alternative grounding figure but not used, since this case's staffing deliverable (D2) is about sector-area coverage, not fence length.

**Decision:** SOURCED as S2, confidence MEDIUM (Wikipedia flags this section as needing additional citation).

## P03 — Shared maximum patrol speed (Appendix A)

**Searched:** "Kenya Wildlife Service national park speed limit km/h game drive rules"; direct fetch attempt of `kws.go.ke/oldweb/content/park-rules` (failed — TLS certificate error); direct fetch of `masaimara.travel/nairobi-national-park-entry-fees.php` as a fallback.

**Found:** "The speed limit in the parks is 50km/h and 25km/h in the Nyerere Park." (Nyerere National Park is in Tanzania, not Kenya — the source conflates two countries' parks, which is exactly why this figure is graded MEDIUM.) A search-engine summary separately reported Masai Mara National Reserve and Nairobi National Park speed caps in the 40 km/h range from other pages not directly fetched.

**Decision:** SOURCED as S3, confidence MEDIUM. Rejected the idea of using a patrol-specific speed (no such figure is publicly published for anti-poaching vehicles specifically, as opposed to tourist game-drive vehicles) — recorded in `not_found[]`. Applied identically to both options, so it cannot itself be the source of the case's balance.

## P04 — Ranger workforce scale (Appendix A, context only)

**Searched:** Same query as P02; direct fetch of `savetherhino.org/programmes/kenya-ol-pejeta-conservancy/`.

**Found:** "There are more than 150 rangers at Ol Pejeta working to protect the wildlife, including rhinos."

**Decision:** SOURCED as S4, confidence MEDIUM. Used purely as scale context in Appendix A so the case's derived team counts (16–18) read as a realistic subset of a real workforce — not load-bearing for any deliverable or the primary metric, and not cited anywhere else in the case.

## P05 — Perimeter Loop standard sector geometry (Appendix B)

**Searched:** No real reserve publishes exact vertex coordinates for a boundary patrol sector — this was never expected to be sourceable, and wasn't searched for as a fact-finding exercise beyond confirming (via general geography/GIS knowledge) that a long, narrow, boundary-hugging patrol sector on a reserve of this scale is a realistic shape.

**Decision:** NOT FOUND (as expected — this is a design choice, not a discoverable fact). Resolved as MA1 (side lengths 18/11/9 km, chosen to be scalene and obtuse) and MA2 (6 sectors ring the reserve), both disclosed Modeling Assumptions with full basis and sensitivity in Appendix E and `case.json.modeling_assumptions`.

## P06 — Interior Web standard sector geometry (Appendix C)

Same reasoning as P05. Resolved as MA3 (equilateral, side 5.7 km — deliberately sized close to S2's real 14 km²-per-team density standard) and MA4 (8 sectors, deliberately leaving real interior gaps).

## P07 — Outpost network distances and relay-route offsets (Appendix D)

Same reasoning as P05/P06 — no real reserve publishes its internal ranger-outpost GPS network. Resolved as MA5 (the three pairwise distances, deliberately constructed to fail the Triangle Inequality Theorem as the point of Challenge D5a) and MA6 (the relay-route legs, deliberately a clean 6-8-10 right triangle for Challenge D5b).

## Arithmetic trail (for QA and the guide)

```
Option A (Perimeter Loop), sides 18, 11, 9 km:
  Triangle inequality: 9 + 11 = 20 > 18  ✓ valid triangle
  Angle opposite 18 km side: cos(C) = (11² + 9² − 18²) / (2·11·9) = −122/198 = −0.6162 → C ≈ 128.04° → OBTUSE
  All three sides different → SCALENE
  Heron's formula: s = (18+11+9)/2 = 19; Area = √(19·1·8·10) = √1520 ≈ 38.99 km²
  Response distance = longest side = 18 km; time = 18/50 × 60 = 21.6 min
  Ratio = 21.6 / 38.99 = 0.5540 min/km²
  Teams per sector = ceil(38.99/14) = ceil(2.785) = 3; 6 sectors × 3 = 18 teams
  Total area = 6 × 38.99 = 233.92 km² (64.98% of 360 km²)

Option B (Interior Web), equilateral side 5.7 km:
  All sides equal → EQUILATERAL; all angles 60° → ACUTE
  Area = (√3/4)·5.7² = 0.4330 × 32.49 ≈ 14.07 km²
  Response distance = one side length = 5.7 km (equilateral triangle: no interior point exceeds
    one side length from any vertex); time = 5.7/50 × 60 = 6.84 min
  Ratio = 6.84 / 14.07 = 0.4862 min/km²
  Teams per sector = ceil(14.07/14) = ceil(1.005) = 2; 8 sectors × 2 = 16 teams
  Total area = 8 × 14.07 = 112.55 km² (31.26% of 360 km²)

Margin: (0.5540 − 0.4862) / 0.4862 × 100 = 13.95%  →  B wins (margin computed relative to the
  winning option's own value, matching sensitivity_model.py's efficiency-framed convention)

D5(a) — Outpost network: 6.0 + 6.5 = 12.5 < 13.0 → FAILS the Triangle Inequality Theorem;
  the three reported distances cannot form a real triangle.
D5(b) — Relay route: legs 6 km (east–west) and 8 km (north–south); hypotenuse = √(6²+8²) = √100 = 10 km.
```

## Verification sweep

```
placeholders remaining: 0
citation markers with no source row: none (S1-S4 all cited and all appear in case.md)
source rows never cited in text: none
INCOMPLETE source rows: none (all of claim/value/units/org/title/url/accessed/confidence present)
LOW-confidence sources: none (S1-S4 all MEDIUM)
```

Next step: run `case-readiness` on `the-patrol-triangle`.
