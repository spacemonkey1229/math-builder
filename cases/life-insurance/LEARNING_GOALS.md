# Learning Goals — Life Insurance

Bidirectional deliverable <-> skill matrix (case-write SKILL.md step 10 / MCS-10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 coverage-need calculation | basic-operations-multiplication, basic-operations-how-to-multiply-multi-digit-numbers-by-single-digit-numbers, basic-operations-addition, basic-operations-how-to-add-multi-digit-numbers, measurement-rounding, measurement-how-to-round-a-number-to-a-specified-place-value |
| D2 term-length + total-premium recommendation | basic-operations-multiplication, advanced-numbers-decimal, advanced-numbers-how-to-multiply-decimal-numbers, number-sense-how-to-compare-two-or-more-values |
| D3 whole life cash-value projection (recursive -> explicit) | calculus-sequence, discrete-mathematics-recursive-formula, discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence, discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula, advanced-operations-exponent-also-power, advanced-operations-how-to-evaluate-an-exponential-expression, advanced-numbers-percent |
| D4 rate-of-return comparison | number-sense-how-to-compare-two-or-more-values, advanced-numbers-percent |
| D5 rider recommendation | advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number |
| D6 original visual (cumulative premiums vs. cash value) | number-sense-bar-graph |

## The forces test

*Could a competent student produce this deliverable correctly without ever performing this
skill?* Applied to each row above:

- **D1** cannot be produced without multiplying income by years, adding the mortgage, and
  rounding to a stated increment — all three operations are explicit, required steps of the
  deliverable's own text, not incidental.
- **D2** cannot be produced without multiplying a decimal monthly rate by 12 and by a chosen
  term length, and cannot pick *which* standard term length without comparing the candidate
  lengths against D1's need window.
- **D3** cannot be produced without writing the year-over-year growth as a recursive rule
  (`CV_n = CV_(n-1) x 1.03`) and then converting it to closed form — a 39-step and a 54-step
  recursive walk by hand is not a realistic path to the deliverable, so the recursive-to-explicit
  conversion is not decorative, it is the only tractable route to the answer. Evaluating the
  explicit form at n=39/54 requires evaluating an exponential expression, and the growth rate
  itself is a percent.
- **D4** is nothing but a comparison of two percentages with a written interpretation — cannot
  be produced without the comparison skill and percent.
- **D5** cannot be produced without converting a stated dollar/percent rider cost into "percent
  increase to the base premium."
- **D6** is a bar graph by its own definition (three checkpoints x two options, categorical
  comparison).

## LEARNING GOAL CHECK

```
deliverables: 6    claimed skills: 18    new_coverage: 4
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

Every one of the 18 skills in `standards[]` is the direct target of at least one row above (no
skill was added because it "sounds related" — each was pulled from working the actual arithmetic
of a deliverable first, then named). Every one of the 6 deliverables has a non-empty skills
column.
