# Learning Goals — The Average Lies

Bidirectional deliverable ↔ skill matrix (case-write §10, MCS-10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — The four tuition bills | calculus-sequence, advanced-operations-how-to-evaluate-an-exponential-expression |
| D2 — What the calculator says | statistics-and-probability-how-to-find-the-mean-of-a-set-of-data, calculus-series, discrete-mathematics-recursive-formula, discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence, discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula, advanced-operations-how-to-evaluate-an-exponential-expression |
| D3 — What history says | discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence, discrete-mathematics-recursive-formula, advanced-numbers-how-to-convert-numbers-to-percents, advanced-numbers-how-to-find-the-percent-of-a-number |
| D4 — The planning gap | advanced-numbers-how-to-find-the-percent-of-a-number, advanced-numbers-how-to-convert-numbers-to-percents |
| D5 — The order experiment | advanced-numbers-how-to-convert-numbers-to-percents, advanced-numbers-how-to-find-the-percent-of-a-number |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 9    new_coverage: 0 (reinforcement_note on file)
UNMAPPED DELIVERABLES: none — every deliverable maps to at least one skill.
UNREACHABLE SKILLS: none — every claimed skill in standards[] is forced by at least one deliverable:
  sequence                                                     -> D1
  series                                                       -> D2
  how-to-write-a-recursive-formula-for-a-sequence              -> D2, D3
  recursive-formula                                            -> D2, D3
  how-to-convert-a-recursive-formula-to-an-explicit-formula    -> D2
  how-to-evaluate-an-exponential-expression                    -> D1, D2
  how-to-find-the-percent-of-a-number                          -> D3, D4, D5
  how-to-convert-numbers-to-percents                           -> D3, D4, D5
  probability-how-to-find-the-mean-of-a-set-of-data            -> D2
RESULT: PASS
```

## Why each thin or low-coverage skill is genuinely forced

- **calculus-series (n=2):** D2 requires the lump sum a steady-return calculator names, which is the present value of four growing bills, a finite geometric series; it must be computed in closed form and checked against the recursion. A student cannot produce D2's closed-form figure without the series.
- **calculus-sequence (n=3):** D1 requires the sequence of the four bills and its explicit formula.
- **how-to-convert-a-recursive-formula-to-an-explicit-formula (n=3):** D2's check requires converting the steady-return balance recursion to its explicit form and showing it matches the closed-form lump sum.

## Reinforcement carve-out

All nine claimed skills already have n>0 in the live spine (no skill anywhere has n==0), so `new_coverage[]` is empty and `case.json.reinforcement_note` records what was checked. "Thin" is n in {1,2} (the spine's `totals.thin_1_2`): this case forces one thin skill (calculus-series n=2); skills at n=3 are real reinforcement, not thin. The geometric mean has no spine skill (logged as a spine gap); the case teaches it inside D2 under the mean how-to and does not claim it.

