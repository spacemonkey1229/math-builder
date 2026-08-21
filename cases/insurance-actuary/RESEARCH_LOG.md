# Research Log — Insurance Actuary

This is a legacy conversion. There were no `{{NEEDS_SOURCE}}` placeholders of the ordinary kind:
every load-bearing number in Appendix A and Appendix B is derived directly from the bundled
`source/Y3/Additional/Insurance Actuary/Safetylife Insurance Data.xlsx` workbook — Safetylife's
own claims data, which is the case's given dataset (Carbosia is an explicitly fictional country;
this is not a real-world verifiable figure requiring external sourcing, same treatment as any
other case's bundled appendix table). The 2019 forecast values in Appendix A are a documented
derivation (least-squares linear trend on the 12 known quarters, MA1) from that same given data,
not a separate research target.

What genuinely needed research: the real-world context claims in Appendix D, used to establish
that age-based actuarial risk classification (the case's whole premise) reflects real industry
practice, not an invented framing.

## P-D1 — Do young drivers really carry higher real-world crash risk, and by how much?

- Searched: "IIHS teen drivers crash rate per mile compared to older drivers 2024 2025
  statistics"; "NHTSA young drivers crash rate per mile".
- Fetched: `https://www.iihs.org/research-areas/fatality-statistics/detail/teenagers` directly
  (tier-1 primary publisher — IIHS is the industry's own crash-data research organization,
  funded by insurers and often relied on by actuaries).
- Found: "the fatal crash rate per miles driven for 16-19 year-olds is just over 3 times the rate
  for drivers ages 20 and over," sourced by IIHS from the National Household Travel Survey.
  Dated, unambiguous units (fatal crashes per mile driven), and directly the quantity needed
  (a young-vs-older comparison, not a proxy). Graded **HIGH**. Recorded as `S1`.
- Rejected: several aggregator/law-firm blog posts (arashlaw.com, dklaw.com, smithlawcenter.com)
  repeating similar "teens crash more" claims with no clear primary citation or date — these
  would be LOW confidence and were not used; IIHS's own page carried the figure directly.

## P-D2 — Do senior drivers really carry higher real-world crash/claims risk, and why?

- Searched: "NHTSA older drivers 65+ crash fatality rate per mile driven statistics".
- Fetched: `https://www.iihs.org/research-areas/fatality-statistics/detail/older-people` directly.
- Found: fatal crash involvement rate per 100 million miles traveled — 85+: 7.9; 40–64: 1.6;
  70–74: 2.1 (rate begins climbing measurably at 70–74). Also found the key actuarial nuance:
  IIHS attributes the older-driver fatality-rate rise "largely to increased susceptibility to
  injuries, particularly to the chest, and medical complications, rather than an increased
  tendency to get into crashes" (citing Cicchino, 2015) — i.e. severity/injury risk, not
  frequency. This directly supports the case's Argument B and the twist's frequency-vs-severity
  framing. Dated (2024 data), specific units, primary publisher. Graded **HIGH**. Recorded as `S2`.
- Also searched "Insurance Information Institute how age affects auto insurance rates actuaries
  young senior drivers" for a supplementary industry-practice source. Found a candidate (The
  Zebra's senior-driver premium study) but `WebFetch` returned HTTP 403 on
  `thezebra.com/resources/research/senior-drivers-car-insurance/` — could not verify the figure
  directly, so it was **not used**. IIHS's two pages (S1, S2) were judged sufficient to support
  the real-world-basis claim in Appendix D without it; nothing in the case is load-bearing on
  the rejected figure.
- Also attempted `https://www.cdc.gov/teen-drivers/risk-factors/index.html` (would have been a
  second tier-1 government source for the young-driver side) — `WebFetch` returned HTTP 403.
  Not used; S1 alone (IIHS, itself citing NHTSA's National Household Travel Survey) already
  carries the young-driver claim at HIGH confidence.

## Verification pass

```
placeholders remaining in case.md: 0
citation markers with no source row: none ([S1], [S2] both resolve)
source rows never cited in text: none
LOW-confidence sources used: none
```

## Next step

Run `case-readiness` on `insurance-actuary`.
