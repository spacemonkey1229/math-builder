# Learning Goals — Codebreaker

Bidirectional deliverable <-> skill matrix (case-write SKILL.md Step 10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — Alphanumeric keyspace (no multiplier / with multiplier, scientific notation) | `advanced-operations-factorial`, `advanced-operations-how-to-evaluate-a-factorial-expression`, `statistics-and-probability-permutation`, `statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-permutation`, `advanced-operations-scientific-notation`, `advanced-operations-standard-notation`, `advanced-operations-how-to-write-a-number-in-scientific-notation-given-its-standard-notation` |
| D2 — Circle Shift keyspace per message | `statistics-and-probability-event`, `statistics-and-probability-outcome` |
| D3 — Blind-guess probability, each cipher | `statistics-and-probability-probability`, `statistics-and-probability-how-to-determine-the-probability-of-a-single-event`, `advanced-operations-scientific-notation` |
| D4 — Both messages encoded + bar graph of character totals | `basic-operations-multiplication`, `basic-operations-product`, `basic-operations-how-to-multiply-single-digit-numbers`, `basic-operations-how-to-multiply-2-digit-numbers-by-single-digit-numbers`, `basic-operations-addition`, `basic-operations-sum`, `basic-operations-how-to-add-2-digit-numbers`, `number-sense-bar-graph`, `number-sense-data`, `number-sense-how-to-compare-two-or-more-values` |
| D5 — Pie chart, separator share of Alphanumeric characters | `statistics-and-probability-pie-chart`, `statistics-and-probability-how-to-create-a-pie-chart-given-a-set-of-data` |
| D6 — Histogram, digit frequency + Pigeonhole Principle check | `statistics-and-probability-histogram`, `statistics-and-probability-how-to-create-a-histogram-given-a-set-of-data`, `discrete-mathematics-pigeonhole-principle` |
| D7 — Zero-error transcription probability, each cipher | `statistics-and-probability-probability`, `statistics-and-probability-how-to-determine-the-probability-of-a-single-event` |
| D8 — Recommendation | `number-sense-how-to-compare-two-or-more-values` |

## LEARNING GOAL CHECK

```
deliverables: 8    claimed skills: 26    new_coverage: 1
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

Verification, skill by skill (every claimed id appears in at least one row above):

- `advanced-operations-standard-notation` — D1
- `advanced-operations-scientific-notation` — D1, D3
- `advanced-operations-factorial` — D1
- `advanced-operations-how-to-evaluate-a-factorial-expression` — D1
- `advanced-operations-how-to-write-a-number-in-scientific-notation-given-its-standard-notation` — D1
- `statistics-and-probability-permutation` — D1
- `statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-permutation` — D1
- `statistics-and-probability-event` — D2
- `statistics-and-probability-outcome` — D2
- `statistics-and-probability-probability` — D3, D7
- `statistics-and-probability-how-to-determine-the-probability-of-a-single-event` — D3, D7
- `statistics-and-probability-histogram` — D6
- `statistics-and-probability-how-to-create-a-histogram-given-a-set-of-data` — D6
- `statistics-and-probability-pie-chart` — D5
- `statistics-and-probability-how-to-create-a-pie-chart-given-a-set-of-data` — D5
- `number-sense-bar-graph` — D4
- `number-sense-data` — D4
- `number-sense-how-to-compare-two-or-more-values` — D4, D8
- `basic-operations-multiplication` — D4
- `basic-operations-product` — D4
- `basic-operations-how-to-multiply-single-digit-numbers` — D4 (letter values 1-9, e.g. J=1, times a single-digit multiplier)
- `basic-operations-how-to-multiply-2-digit-numbers-by-single-digit-numbers` — D4 (letter values 10-26 times a single-digit multiplier)
- `basic-operations-addition` — D4 (totaling character counts across messages)
- `basic-operations-sum` — D4
- `basic-operations-how-to-add-2-digit-numbers` — D4 (e.g. 57 + 63 = 120)
- `discrete-mathematics-pigeonhole-principle` — D6 (120 total digit characters, 10 possible digits, so some digit repeats at least 12 times — a genuine, checkable lower bound against the student's own histogram)

## Why `new_coverage` has exactly one entry

`discrete-mathematics-pigeonhole-principle` has `n == 0` in `readmodel/standards_spine.json`
as of 2026-08-13 and is genuinely forced by D6 (see above) — not padding. Every other claimed
standard already has `n >= 1`, already exercised by at least one other published case in this
corpus. The spine's pre-existing `covered_by: ["Codebreaker", ...]` tags on 41 skills predate
this conversion and this pipeline entirely — they were placeholder tags from the legacy
indexing pass, not evidence any of those 41 skills had actually been closed by a real, published
`case.json`. This conversion does not pad `standards[]` beyond the one genuine addition.

## Skills considered and cut

Of the 41 originally spine-tagged skills, 16 were cut because no Challenge-3 deliverable
genuinely forces them:

- `number-sense-number`, `number-sense-greater-than`, `number-sense-less-than`,
  `number-sense-equal` — too generic; no deliverable isolates comparison operators as a distinct
  skill beyond `number-sense-how-to-compare-two-or-more-values`, which is kept.
- `basic-operations-how-to-add-single-digit-numbers`, `basic-operations-how-to-add-multi-digit-numbers`
  — D4's real additions (57+63=120, 23+27=50) are 2-digit; single-digit and true multi-digit
  (3+ digit) addition are not distinctly required.
- `basic-operations-how-to-multiply-multi-digit-numbers-by-single-digit-numbers`,
  `basic-operations-how-to-multiply-2-digit-numbers-by-2-digit-numbers`,
  `basic-operations-how-to-multiply-any-two-numbers` — the multiplication D4 actually requires is
  a letter value (1-26, at most 2 digits) times a single-digit multiplier; no 2-by-2-digit or
  true multi-digit multiplication occurs.
- `measurement-rounding`, `measurement-estimating`, `measurement-how-to-round-a-number-to-a-specified-place-value`,
  `measurement-time` — no deliverable rounds a figure or works with clock time; the case's
  "3:14 AM" and "six months" are Overview/Background texture, not load-bearing numbers a student
  computes with.
- `advanced-operations-how-to-write-a-number-in-standard-notation-given-its-scientific-notation`
  — the reverse direction of the conversion D1 actually asks for (standard -> scientific); kept
  out rather than adding a deliverable just to force it.
- `statistics-and-probability-combination`, `statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination`
  — D1/D2's counts are permutations (order matters: which number goes with which letter; which
  skip value is used) and simple enumeration (D2), not combinations.

One skill was added beyond the original 41-skill legacy tag set: `discrete-mathematics-pigeonhole-principle`,
added because D6 genuinely forces it (see above) — not one of the legacy-tagged skills, but a
real, deliverable-forced addition, exactly the "add any skill a deliverable clearly forces that
isn't in this list" instruction this conversion was run under.
