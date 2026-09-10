# Research Log — Kite Cut

`case-research` pass, 2026-09-09. Every figure below was searched, fetched, and confirmed live
before use (MCS-21 — no URL from memory). This case was authored and researched in one combined
pass; this log documents both what was needed and what was found/rejected.

## P01 — Typical diamond-kite height (general context for the shop's own 36 in choice)

- Searched: "Eddy kite plans dimensions spine spreader bow diamond kite standard size".
- Fetched: `https://en.wikipedia.org/wiki/Diamond_kite` — confirmed: "Diamond kites vary in size,
  though most are less than 1 metre (3 ft) in height."
- Also found (not used as the primary cite): my-best-kite.com's Eddy page describes a 36 in × 36
  in "basic Eddy kite design" and notes original meteorological Eddy kites reached almost 9 ft —
  consistent with "sizes vary a lot." Wikipedia's more general, more citable statement was used.
- Outcome: **SOURCED** → S1. Used only as background context; the shop's actual 36 in × 36 in
  choice is a scenario design decision, not itself a placeholder needing a source (same treatment
  as a building footprint in a prior case).

## P02 — Spar (fiberglass rod) price and length

- Searched: "fiberglass kite spar rod price per piece kite building supply".
- Fetched: `https://www.flymarketkites.com/fiberglass-tubes` (catalog) then
  `https://www.flymarketkites.com/fiberglass-tubes/125-solid-fiberglass-rod` (product page).
- Found: 0.125 in solid fiberglass rod, offered in 48 in and 72 in lengths, "from $3.75."
- The exact price for each individual length isn't broken out in the fetched page content — this
  is disclosed as a MEDIUM-confidence caveat in Appendix F/S2 rather than treated as exact.
- Rejected: did not use a heavier-gauge rod (e.g. 0.156 in, ~$4.10) since 0.125 in is a
  commonly-stocked size for a kite this size and keeps both options' spar cost identical, which is
  the honest result (spar length is the same 72 in total for both options regardless of crossing
  point — only the crossing point moves, not the stick lengths).
- Outcome: **SOURCED** → S2.

## P03 — Eddy kite crossing-point proportion

- Searched: "Eddy kite plans dimensions spine spreader bow diamond kite standard size"; also
  "'Eddy kite' tailless stability bowed spar diamond kite needs tail".
- Fetched: `https://www.my-best-kite.com/eddy-kite.html` — confirmed: spreader crosses "19 percent
  of the way down from the nose" on the original Eddy design (a "modern variation" at 25% is also
  mentioned but not used — this case uses the historic original proportion, matching the
  Background's framing of it as the design Priya found in her grandfather's kite-history binder).
- Outcome: **SOURCED** → S3. MEDIUM confidence — a hobbyist kite-history reference, not Eddy's own
  1890s documentation, but specific and internally consistent with S4.

## P04 — Whether traditional diamond kites need a tail, and Eddy kites don't

- Searched: "'Eddy kite' tailless stability bowed spar diamond kite needs tail".
- Fetched: `https://intothewind.com/kites/diamond-kites.html` — confirmed verbatim: "Typical
  diamond-shaped kites need a tail to help with stability."
- Corroborated by my-best-kite.com (S3): the original Eddy kite had "no tail — very handy for kite
  trains" and by Wikipedia's "Bowed kite" article (search snippet): "Eddy added a bow in the cross
  spar in lieu of a tail in order to introduce the requisite stability."
- Outcome: **SOURCED** → S4. HIGH confidence — a specialty kite retailer's own product/education
  copy, consistent across three independent pages.

## P05 — Ripstop nylon fabric price and roll width

- Searched: "ripstop nylon fabric price per yard kite making supplier".
- Fetched: `https://www.emmakites.com/products/40d-ripstop-nylon-fabric-pu-coating-by-the-yard` —
  confirmed: $7.95 per yard, "1.7 yards / 60 inch / 1.52 Meter" width (60 in).
- Rejected: a heavier 70D PU3000 waterproof option ($8.95/yd) and a 1.2 oz silnylon option
  ($12.95/yd) from the same retailer — 40D ripstop is the standard, lightest, cheapest kite-sail
  weight and keeps the comparison from being muddied by a fabric-grade choice that isn't part of
  either option's actual design difference.
- Outcome: **SOURCED** → S5. HIGH confidence — primary retailer listing.

## P06 — Kite tail length guidance

- Searched: "kite tail length rule of thumb how long should a kite tail be times height".
- Fetched: `https://kitekits.com/blogs/kites-in-the-sky-blog/114240899-does-your-kite-need-a-tail`
  — confirmed: "I like to start with adding about 3-4 times the height of the kite."
- Fetched: `https://www.kitesoar.com/articles/03-using-kite-tails-for-stability.shtml` —
  confirmed: "A useful starting point for a small diamond kite is a tail several times the height
  of the kite," with no exact multiplier given, and explicit guidance that the right length is
  found by testing, not a fixed formula.
- No source gives one single fixed ratio — this is exactly the "range exists, no fixed spec"
  case the Modeling Assumptions process is for.
- Outcome: **NOT a fixed sourceable figure → Modeling Assumption**, MA1 (4× height = 144 in),
  basis cited to S6/S7, sensitivity disclosed in Appendix E.

## P07 — Tail strip width

- Searched: general kite-tail-material searches (P06) surfaced ribbon/crepe-paper/streamer tail
  construction generically, but no source gives a standard width for a giveaway-kite tail cut from
  fabric.
- Outcome: **NOT FOUND → Modeling Assumption**, MA2 (4 in craft strip width), no real basis beyond
  "a common, easy-to-cut craft width" — disclosed honestly as unsourced in Appendix E.

## P08 — Fabric-cutting-layout efficiency for the Eddy (kite-shaped) sail

- This is not a figure that exists in any public source — it's the case's own geometric modeling
  choice, verified independently by hand (see below), not searched for.
- Verified by direct coordinate geometry (not sourced, shown here for the record): placing the
  rhombus's four vertices at N(0,36), R(18,18), T(0,0), L(−18,18) and rotating a second copy 180°
  about the midpoint of edge T–L produces a combined boundary that collapses from a hexagon to a
  true 4-sided parallelogram (three pairs of vertices become collinear) with area exactly 1,296 sq
  in = 2 × 648 sq in — a provable, zero-waste result. Repeating the identical construction on the
  kite's vertices N(0,36), R(18,29.16), T(0,0), L(−18,29.16) (crossing at 19%, not 50%) does
  **not** collapse to 4 sides — it stays a genuine 6-vertex hexagon, because the kite lacks the
  rhombus's point symmetry about its center. This is the real mathematical basis for MA3: the
  rhombus's D3 result is exact, provable geometry; the kite's "no equivalent zero-waste pairing in
  this simple construction" is also exact — but a *more complex* interlocking layout might still
  achieve better-than-bounding-box efficiency for the kite shape, which is exactly what MA3's
  stated value (a simple, individually-boxed layout, not a researched optimum) leaves open.
- Outcome: **Modeling Assumption**, MA3 (2.0× raw sail area, i.e. individually-boxed with no
  pairing), sensitivity computed directly in `sensitivity_model.py` (flip point ≈1.89×).

## Verification pass

```
placeholders remaining in case.md: 0
citation markers with no source row: none
source rows never cited in text: none
```

All 7 sources (S1–S7) are HIGH or MEDIUM confidence; none is LOW. No LOW-confidence figure carries
a constraint or the dilemma in this case.

Next step: `Run case-readiness on kite-cut.` (not run by this pass, per instruction — a separate
gate does this).
