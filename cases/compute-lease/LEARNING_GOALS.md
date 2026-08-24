# LEARNING_GOALS.md — The Compute Lease

Bidirectional deliverable ↔ skill matrix. Claimed skills (`case.json.standards[]`):
`calculus-series`, `calculus-how-to-determine-whether-a-series-converges-or-diverges`,
`calculus-sequence`.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — monthly GPU-hour demand sequence (recursive + closed form, 3 scenarios) | calculus-sequence |
| D2 — two 24-month total-cost series, written as explicit sums | calculus-series |
| D3 — convergence/divergence classification of the extended growth series | calculus-how-to-determine-whether-a-series-converges-or-diverges, calculus-series |
| D4 — total cost per GPU-hour delivered, summed from the D2 series, 2 options × 3 scenarios | calculus-series |
| D5 — the crossover growth rate between the two series' totals | calculus-series |
| D6 — recommendation, defended with D4/D5 results | calculus-series (applied, no new skill forced) |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 6    claimed skills: 3    new_coverage: 2
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Forces test applied:** could a competent student produce D1 without building a sequence
(recursive + closed form)? No — that is the deliverable's literal content. Could they produce
D2, D4, or D5 without writing and summing a series? No — the totals are series sums by
construction, not single arithmetic products, because the Open Tap's monthly cost changes every
month under growth. Could they produce D3 without applying the convergence/divergence test to a
specific common ratio? No — D3 explicitly asks for the classification and its reasoning, not just
a final number.

`calculus-sequence` (n=1, already covered) is exercised by D1 alone and is not claimed as
`new_coverage` — it reinforces prior coverage rather than closing a gap, per the concept sheet.
`calculus-series` and `calculus-how-to-determine-whether-a-series-converges-or-diverges` both had
`n=0` before this case and are the `new_coverage[]` set (SPEC §7 — the reason this case exists).

No deliverable was written to force `calculus-taylor-series` or its how-to, and neither id appears
in `standards[]` — a Taylor expansion has no natural role in this scenario and was excluded per
the approved concept sheet.
