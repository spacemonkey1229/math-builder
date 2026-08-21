# Learning Goals — Fast Food

Bidirectional deliverable ↔ skill matrix. Legacy conversion, 2026-08-20.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — start-up cost breakdown + Day-1 staffing, checked against the $806,000 ceiling | `advanced-numbers-how-to-add-decimal-numbers`, `number-sense-how-to-compare-two-or-more-values` |
| D2 — first-year operating cost table (royalty/ad-fund/food-cost as % of revenue) | `advanced-numbers-percent`, `advanced-numbers-how-to-find-the-percent-of-a-number` |
| D3 — first-year revenue (from AUV) and net profit | `advanced-numbers-how-to-add-decimal-numbers`, `advanced-numbers-how-to-subtract-decimal-numbers` |
| D4 — break-even point in months (one-step equation) | `advanced-operations-equation`, `advanced-operations-variable`, `advanced-operations-how-to-solve-a-one-step-equation` |
| D5 — break-even point in monthly transactions (variable on both sides) | `advanced-operations-variable`, `advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-both-sides` |
| D6 — recommendation comparing first-year ROI | `advanced-numbers-how-to-convert-numbers-to-percents`, `number-sense-how-to-compare-two-or-more-values` |

## LEARNING GOAL CHECK

```
deliverables: 6    claimed skills: 10    new_coverage: 2
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each skill** (*could a competent Hero produce the deliverable correctly
without ever performing this skill?*):

- `how-to-add-decimal-numbers` — D1 sums a franchise fee, build-out cost, equipment, and initial
  inventory, all dollar figures with cents; D3 sums operating costs. Forced.
- `percent` / `how-to-find-the-percent-of-a-number` — D2 explicitly requires each operating cost
  (royalty, ad fund, food cost) to be computed as a percent of the D3 revenue figure, from
  Appendix B's published rates. Forced, and this is exactly the kind of percent-of-a-number
  application this project already covers heavily elsewhere — claimed for continuity with the
  original 2021 case's own "Percent" vocabulary line, not for new coverage.
- `how-to-subtract-decimal-numbers` — D3's net profit is revenue minus the D1/D2 totals. Forced.
- `equation` / `variable` / `how-to-solve-a-one-step-equation` — D4 explicitly requires setting up
  `start-up investment = monthly net profit × months` and solving for months, a genuine one-step
  (divide-both-sides) equation. **New coverage** (n=0 pre-conversion): no other case in the corpus
  currently forces this specific how-to.
- `how-to-solve-a-multi-step-equation-with-a-variable-on-both-sides` — D5 explicitly requires the
  transaction count to appear on both sides of the break-even equation: revenue
  (`avg ticket × transactions`) on one side, fixed costs plus percent-of-revenue costs (themselves
  `rate × avg ticket × transactions`) on the other. Isolating the variable requires combining like
  terms across both sides before dividing — the real forcing task for this how-to, not a
  restatement of D4's simpler one-step equation. **New coverage** (n=0 pre-conversion).
- `how-to-convert-numbers-to-percents` — D6's ROI is explicitly required "as a percent," computed
  from the raw net-profit-÷-investment ratio D4/D5 produce as decimals. Forced.
- `how-to-compare-two-or-more-values` — D1 requires comparing the start-up total against the
  $806,000 ceiling; D6 requires comparing both franchises' ROI directly. Forced.

No skill here is claimed on the strength of "the case is about running a business generally" —
each one traces to a specific verb in a specific deliverable. See `case.json.legacy_conversion_note`
for what the conversion kept from the source (the couple's own financial figures, used as given
scenario data) vs. dropped (the third Sonic option per the approved dilemma lock; the household
spending budget and the couple's individual incomes/debt, which no deliverable needs) vs. added
new (D4/D5/D6's break-even-and-ROI analysis, absent from the original 2021 case entirely).
