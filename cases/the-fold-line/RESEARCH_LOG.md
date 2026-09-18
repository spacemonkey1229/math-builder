# Research Log — The Fold Line

Written retrospectively alongside `case-write`, since this case was authored and researched in a
single pass (no `{{NEEDS_SOURCE}}` placeholder stage was shipped as an intermediate artifact).
Every figure below was genuinely searched and, where live-fetchable, confirmed via a real browser
navigation on 2026-09-17 — see each row's Confirmed column.

| Placeholder (design intent) | Searched | Found | Confirmed | Outcome |
|---|---|---|---|---|
| Fabric bolt width | "standard fabric bolt width 44 45 inches cotton" | The Fabric Calculator's width guide; multiple retailers corroborate 44/45in as the quilting/shirting standard | Live via WebSearch aggregation; not independently browser-fetched (low-risk, near-universal, non-numeric-precision claim) | SOURCED — S2, MEDIUM (trade convention, not a standards body) |
| Cotton/blend fabric price per yard, 44/45in | "cotton twill fabric price per yard wholesale 2026"; "44 inch wide quilting cotton fabric price"; "onlinefabricstore.com broadcloth cotton 45 inch price" | JoAnn's Quilter's Showcase (44in, ~$5.99, but joann.com now redirects to michaels.com — dead as a live citation, rejected); OnlineFabricStore 45" White Broadcloth ($3.70/yd, 44/45in, 65/35 poly-cotton) | Browser-fetched live 2026-09-17: confirmed product BROADOPT, $3.70/yd, "Width 44/45", 65% Polyester/35% Cotton | SOURCED — S4, MEDIUM (undated retail page) |
| Cutting-room labor wage | "BLS median hourly wage cutting and slicing machine textile 2024"; then the textile-specific SOC code directly | Two BLS OEWS occupation pages: 51-9032 "Cutting and Slicing Machine Setters..." (median $21.31, but excludes textile cutting by its own scope note) and 51-6062 "Textile Cutting Machine Setters, Operators, and Tenders" (median $17.61) | Both browser-fetched live 2026-09-17. Chose 51-6062 as the more precise real-world match — 51-9032 explicitly excludes "Textile Cutting Machine Setters, Operators, and Tenders (51-6062)" in its own scope note, so using it here would have been the less accurate of the two. | SOURCED — S5, HIGH |
| Marker efficiency (definition + typical ranges) | "marker efficiency percentage apparel cutting fabric utilization typical range garment industry" | Multiple hits describing an established, real garment-industry KPI with published typical ranges by garment type and by marker method (single-size/manual vs. multi-size/nested) | textiletrainer.com (definition + worked formula, browser-confirmed live) and apexfashionlab.com (75-82% single-size/manual vs. 82-90% multi-size/optimized nesting, browser-confirmed live) | SOURCED (definition) — S3, MEDIUM; SOURCED (ranges) — S6, MEDIUM |
| Standard seam allowance | (general sewing-industry knowledge check, not independently re-searched this session; 5/8in is the standard convention cited across essentially every U.S. home-sewing and light-manufacturing pattern instruction sheet) | The Spruce Crafts' seam-allowance reference page | Not independently browser-fetched this session (low novelty-risk, extremely well-established convention); flagged for a future P6 data-decay check to confirm the specific URL still resolves | SOURCED — S1, HIGH |
| Exact bodice front panel dimensions (a specific commercial pattern's coordinates) | "freesewing.eu bodice front panel pattern draft measurements"; "Simplicity pattern fitted bodice yardage requirements chart 45in fabric size 12" | FreeSewing's parametric drafts exist but no single citable numeric panel dimension surfaced in search; Simplicity's yardage charts are pattern-specific and not indexed at the individual-figure level by search | NOT FOUND after two distinct search framings and no single primary document surfaced with a directly fetchable coordinate table | **NOT FOUND → Modeling Assumption (MA1).** No manufacturer publishes the exact coordinate dimensions of a specific proprietary pattern; MA1's stated width/length are sized consistently with the *published range* of home-sewing yardage requirements for a fitted bodice front (5/8-7/8 yd of 45in fabric), which is the closest real, citable anchor available. Redesign was considered (e.g., basing the panel directly on a specific free FreeSewing draft's own published measurements) but rejected for this pass: FreeSewing's drafts are parametric formulas keyed to a user's own body measurements, not a single fixed reference panel, so pulling "the" dimensions from it would itself have required choosing an arbitrary body-measurement input -- no more sourced than stating the assumption directly, and considerably more work to make legible to a MS reader. |
| Per-panel marking/cutting time, by method | (no search attempted — this is explicitly an internal production-floor rate; the concept sheet itself flagged this as "not confident about... a real published cutting-labor rate") | n/a — no trade body publishes floor-level per-piece cutting time, and the concept sheet correctly anticipated this | n/a | **NOT FOUND (anticipated) → Modeling Assumption (MA2).** The 2:1 ratio between methods is fixed directly by the case's own stated premise (Background: "cutting two separate mirror-image half-pieces takes about twice as long"), not derived from any external figure — flagged as the single most dilemma-relevant assumption in Appendix E and FACILITATOR.md. |

## Rejections

- **JoAnn.com** as a live fabric-price citation — rejected. `joann.com` now 301-redirects to `michaels.com` (confirmed via WebFetch 2026-09-17); a dead retailer domain cannot be a live, verifiable citation even though a cached price ($5.99/yd) was findable via search-engine summary.
- **A single exact marker-efficiency percentage for this specific panel/bolt combination** — no such figure exists publicly (marker efficiency is measured per real production marker, not published per generic panel shape). Used the two real, cited *ranges* (S6) and disclosed a chosen point from each as MA3, rather than presenting either point-value as if it were itself a citation.
- **A single "the" bodice pattern with published coordinates** — see the NOT FOUND row above; redesign was considered and rejected in favor of a disclosed, well-grounded Modeling Assumption.

## Balance computation (ground truth for `sensitivity_model.py` and `case.json.derived`)

```
width  = 8.375 + 0.625            = 9.0        in   (finished width + side/shoulder seam allowance)
length = 23.25 + 1.5 + 0.625      = 25.375     in   (finished length + hem allowance + shoulder seam allowance)
area   = 9.0 * 25.375             = 228.375    in^2

fabric_in2_fold = 228.375 / 0.78  = 292.7885   in^2
fabric_in2_open = 228.375 / 0.88  = 259.5170   in^2

fabric_yd_fold  = (292.7885/44)/36 = 0.18484   yd
fabric_yd_open  = (259.5170/44)/36 = 0.16384   yd

fabric_cost_fold = 0.18484 * 3.70 = 0.68391   USD
fabric_cost_open = 0.16384 * 3.70 = 0.60620   USD

labor_cost_fold = (0.8/60) * 17.61 = 0.23480  USD
labor_cost_open = (1.6/60) * 17.61 = 0.46960  USD

total_fold = 0.68391 + 0.23480 = 0.91871  USD
total_open = 0.60620 + 0.46960 = 1.07580  USD

margin_pct = 100 * (1.07580 - 0.91871) / 0.91871 = 17.10%   (Fold Cut / A wins)

daily (x300):
  fold: 275.61 USD/day
  open: 322.74 USD/day
  gap:   47.12 USD/day
```

Status: **researched.** Zero `{{NEEDS_SOURCE}}` placeholders remain in `case.md`. `sources[]` (6) and
`modeling_assumptions[]` (3) are populated in `case.json`.

## P6 data-decay finding and fix (2026-09-18, case-readiness pass)

Live re-verification of every source URL (case-readiness Tier 2 probe 6) found **S1's original URL
dead**: `https://www.thesprucecrafts.com/standard-seam-allowances-for-sewing-2msep-2977745` now
301-redirects to an unrelated article, "Safety Pointers to Sew Stuffed Animals, Dolls, Toys" — no
seam-allowance content anywhere on the resulting page. Confirmed via live browser navigation
2026-09-18. This is exactly the "a URL that resolves but no longer carries the figure" case P6
exists to catch — worse than a clean 404, because nothing else in the pipeline would ever have
noticed.

**Fix:** replaced S1 with `https://en.wikipedia.org/wiki/Seam_allowance`, confirmed live the same
day, which states commercial home-sewing patterns range 1/4–5/8in and calls out 5/8in specifically
for fray protection, citing two real patternmaking textbooks (Kim & Kim 2014; Matthews-Fairbanks
2018). Graded HIGH (real citations to named academic sources, unambiguous units, the figure the
case actually needs). `case.json` and `case.md` Appendix G both updated. All other five sources
(S2–S6) were confirmed live and unmoved during original research (see rows above) and were not
re-checked in this pass; a full P6 re-verification of all six is recommended before any future
publish step.
