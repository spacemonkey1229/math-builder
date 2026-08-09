# Learning Goals — Rent vs. Own

Bidirectional deliverable ↔ skill matrix. Legacy conversion, 2026-08-01.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — total monthly rental cost | `advanced-numbers-how-to-add-decimal-numbers` |
| D2 — down payment, closing costs, cash needed | `advanced-numbers-percent`, `advanced-numbers-how-to-find-the-percent-of-a-number` |
| D3 — monthly mortgage P&I via the standard formula | `advanced-operations-exponent-also-power`, `advanced-operations-how-to-evaluate-an-exponential-expression` |
| D4 — total monthly cost of owning | `advanced-numbers-how-to-add-decimal-numbers` |
| D5 — both options checked against DTI guidelines | `advanced-numbers-how-to-convert-percents-to-numbers`, `advanced-numbers-how-to-divide-decimal-numbers`, `number-sense-how-to-compare-two-or-more-values` |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 8    new_coverage: 2
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each skill** (*could a competent Hero produce the deliverable correctly
without ever performing this skill?*):

- `how-to-add-decimal-numbers` — D1's rent total and D4's owning total are both direct sums of
  decimal dollar figures. Forced.
- `percent` / `how-to-find-the-percent-of-a-number` — D2's down payment (2.5% of price) and
  closing costs (3.5% of price) are direct percent-of-a-number calculations. Forced.
- `exponent-also-power` / `how-to-evaluate-an-exponential-expression` — D3's mortgage formula,
  M = P*r(1+r)^n / ((1+r)^n - 1), requires evaluating (1.0025)^360. This is genuine new coverage
  (n=1 pre-conversion for both): no other case currently forces this pair, and the formula is not
  a contrived add-on -- it is the actual standard way a mortgage payment is computed. Forced.
- `how-to-convert-percents-to-numbers` / `how-to-divide-decimal-numbers` — D5's DTI ratios (cost /
  income, expressed as a percent) require both a division and a percent conversion. Forced.
- `how-to-compare-two-or-more-values` — D5's own instruction requires checking both options
  against the same guidelines directly. Forced.

No skill here is claimed on the strength of "the case is about personal finance generally" — each
one traces to a specific verb in a specific deliverable. See `case.json.legacy_conversion_note` for
why this conversion states a disclosed representative mortgage rate and a bundled PMI/tax/insurance
estimate rather than the original's three unrecoverable individual rates.
