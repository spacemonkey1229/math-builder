# Research Log — Grade Rule

One row per placeholder identified at case-write time, what was searched, what was found or not, and the resolution. All searches and fetches were run live on 2026-09-18.

| # | Placeholder | Searched | Found | Resolution |
|---|---|---|---|---|
| P01 | Real published body-measurement standard, by size, multiple landmarks | Searched Simplicity/McCall's/Butterick pattern-company size charts (found referenced but not extractable as clean tables); searched directly for the underlying industry standard | ASTM D5585-11e1 (2011), reproduced in full on Wikipedia's "U.S. standard clothing size" page, sizes 00–20, bust/waist(straight)/hip(straight) | SOURCED — S1, HIGH. Confirmed live via direct fetch; the real published standard, not a single retailer's proprietary chart. |
| P02 | Median hourly wage for a garment pattern grader | Searched BLS OEWS for the specific SOC code | SOC 51-6092, Fabric and Apparel Patternmakers, median $30.05/hr, May 2023 | SOURCED — S2, HIGH. Confirmed live via direct fetch. |
| P03 | Fit tolerance (acceptable grading variance per landmark) | Searched for a general patternmaking/garment-engineering fit-tolerance standard | No single trade-body figure found; fit tolerance is a real garment-engineering concept but the acceptable number is a company-internal or garment-specific choice, never standardized publicly | ASSUMPTION — MA1, disclosed as the case's own stated value (±0.5in). Flagged as the single most dilemma-relevant assumption in the case. |
| P04 | Per-point grading time, each method | Searched for garment-grading production-rate studies; none found at this granularity (an internal production-floor rate, not tracked by any trade body) | — | ASSUMPTION — MA2, disclosed with a stated 3:1 basis (Point-Specific's per-point time set at 3x Uniform Dilation's, reflecting the extra verification work each individually-derived point requires). |
| P05 | A real, published industry grade-rule table (the actual per-point increment values a company would use) | Searched ASTM's own standards catalog and general search for a free apparel grade-rule table | Matches the concept sheet's own prediction: real grade-rule tables are typically sold, not free (e.g. proprietary company standards, or paywalled ASTM/ASME grading documents beyond the base body-measurement standard) | REDESIGNED AROUND, not needed. This case instead uses the real, free ASTM D5585 body-measurement standard (S1) directly, and has the student DERIVE both options' grading arithmetic from it (Challenges D1-D2) rather than being handed a pre-computed, possibly-paywalled grade rule. This is a stronger case design, not a compromise -- it makes D1/D2's scale-factor derivation the actual assignment instead of a given fact. |

## Rejected sources / dead ends

- Simplicity, McCall's, Butterick pattern-company size charts (simplicity.com/size-charts, jaycotts.co.uk fitting guide) — real, live pages exist, but the actual numeric tables render as images or are not present in the fetched text. A search snippet gave one example row (McCall's size 10: 32.5in bust, 24in waist, 34.5in hip, 16in back-waist-length) but not the full run needed for this case's math. Superseded by the more complete and more clearly citable ASTM D5585-11e1 standard (S1), which gives every size in the run directly.
- A general web search for "garment grading fit tolerance inches standard" and "patternmaking acceptable ease tolerance" returned patternmaking educational pages discussing ease and tolerance conceptually, but no single citable numeric standard specific to grading tolerance. Resolved as MA1.

## Derivation arithmetic (supports `case.json.derived` and `balance`)

```
Base size = 12. Data (ASTM D5585-11e1, S1), inches:
  size  bust     waist   hip
  8     36.25    29.5    38.5
  10    37.25    30.5    39.5
  12    38.75    32.25   41.0   (base)
  14    40.375   34.0    42.5
  16    42.125   36.0    44.25

--- D1: point-specific scale factors (new / old), consecutive sizes ---
  8->10:  bust 37.25/36.25=1.02759   waist 30.5/29.5=1.03390   hip 39.5/38.5=1.02597
  10->12: bust 38.75/37.25=1.04027   waist 32.25/30.5=1.05738  hip 41.0/39.5=1.03797
  12->14: bust 40.375/38.75=1.04194  waist 34.0/32.25=1.05426  hip 42.5/41.0=1.03659
  14->16: bust 42.125/40.375=1.04335 waist 36.0/34.0=1.05882   hip 44.25/42.5=1.04118

--- D2: single shared (uniform dilation) scale factor ---
  Method: geometric mean of the full-range (size 8 -> size 16) ratio, averaged
  across all three landmarks, then take the 4th root (4 steps span size 8 to 16).
  ratio_bust = 42.125/36.25 = 1.162069
  ratio_waist = 36.0/29.5   = 1.220339
  ratio_hip   = 44.25/38.5  = 1.149351
  avg_ratio = (1.162069+1.220339+1.149351)/3 = 1.177253
  s = avg_ratio^(1/4) = 1.0416395   (+4.164% per size step)

--- D3: dilated predictions (base size 12 x s^n, n = steps from base) ---
  size 8  (n=-2, factor=0.921648): bust 35.714  waist 29.723  hip 37.788
  size 10 (n=-1, factor=0.960025): bust 37.201  waist 30.961  hip 39.361
  size 12 (n=0,  factor=1.000000): bust 38.750  waist 32.250  hip 41.000  (exact, base)
  size 14 (n=+1, factor=1.041639): bust 40.364  waist 33.593  hip 42.707
  size 16 (n=+2, factor=1.085013): bust 42.044  waist 34.992  hip 44.486

--- D4: fit check, tolerance +/-0.5in (MA1) ---
  size 8:  bust off 0.536 (FAIL), waist off 0.223 (ok), hip off 0.712 (FAIL) -> size FAILS
  size 10: bust off 0.049 (ok), waist off 0.461 (ok), hip off 0.139 (ok)     -> size FITS
  size 12: all exact                                                        -> size FITS (base)
  size 14: bust off 0.011 (ok), waist off 0.407 (ok), hip off 0.207 (ok)    -> size FITS
  size 16: bust off 0.081 (ok), waist off 1.008 (FAIL), hip off 0.236 (ok)  -> size FAILS
  Uniform Dilation: 3 of 5 sizes fit. Point-Specific Grading: 5 of 5 (uses real data directly).

--- D5: labor cost and decision ---
  wage = $30.05/hr = $0.500833/min
  n_point_grades = 4 non-base sizes x 3 landmarks = 12
  Uniform Dilation:   time = 3.0 (setup) + 12*0.4 = 7.8 min   -> cost = 7.8 * 0.500833 = $3.9065
  Point-Specific:      time = 12*1.2 = 14.4 min                -> cost = 14.4 * 0.500833 = $7.2120

  cost_per_fit_A = 3.9065 / 3 = $1.3022
  cost_per_fit_B = 7.2120 / 5 = $1.4424
  margin_pct = (1.4424-1.3022)/1.3022*100 = 10.77%   winner = A (Uniform Dilation)

--- Twist: tolerance tightens to +/-0.42in ---
  size 14's waist miss (0.407) is now the binding case: 0.407 <= 0.42, still FITS (barely)
  size 10's waist miss (0.461) now FAILS (> 0.42)
  size 16 still FAILS (worse misses)
  size 8 still FAILS
  Uniform Dilation: 2 of 5 sizes fit (12, 14) -> cost_per_fit_A = 3.9065/2 = $1.9533
  Point-Specific unchanged: $1.4424
  margin_pct = (1.9533-1.4424)/1.4424*100 = 35.4%   winner flips to B
```

All arithmetic re-verified by `sensitivity_model.py` at the bottom of this case's folder; running it directly reproduces every figure above.
