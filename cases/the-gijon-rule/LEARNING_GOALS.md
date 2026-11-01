# Learning Goals — The Gijon Rule

Bidirectional deliverable ↔ skill matrix (case-write §10, MCS-10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — Group 2 standings and goal-difference arithmetic | advanced-numbers-negative-number, advanced-numbers-how-to-add-with-negative-numbers, number-sense-how-to-compare-two-or-more-values |
| D2 — The three-point test | statistics-and-probability-outcome, number-sense-how-to-compare-two-or-more-values |
| D3 — Option A grids and counts | discrete-mathematics-fundamental-counting-principle, discrete-mathematics-how-to-apply-the-fundamental-counting-principle-to-count-outcomes, statistics-and-probability-outcome, statistics-and-probability-event, advanced-numbers-how-to-convert-numbers-to-percents |
| D4 — Option B grids and a Venn diagram | discrete-mathematics-set, discrete-mathematics-subset, discrete-mathematics-how-to-find-the-union-and-intersection-of-two-sets, discrete-mathematics-how-to-represent-a-set-relationship-using-a-venn-diagram, advanced-numbers-how-to-convert-numbers-to-percents |
| D5 — The cost to history | number-sense-how-to-compare-two-or-more-values |
| D6 — The recommendation | advanced-numbers-percent, advanced-numbers-how-to-convert-numbers-to-percents, statistics-and-probability-event, statistics-and-probability-outcome, number-sense-how-to-compare-two-or-more-values |

## LEARNING GOAL CHECK

```
deliverables: 6    claimed skills: 13    new_coverage: 0 (reinforcement_note on file)
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none — every claimed skill in standards[] is forced by at least one deliverable:
  fundamental-counting-principle          -> D3 (state how many cells the 7 x 7 grid has)
  how-to apply FCP to count outcomes      -> D3
  outcome                                 -> D2, D3, D6 (a cell is an outcome of Algeria-Chile; a scoreline is an outcome of the other match)
  event                                   -> D3, D6 (the set of cells in which a scoreline is safe is an event)
  set                                     -> D4 (the safe-cell sets under A and under B)
  subset                                  -> D4 (the case asks whether one safe set is a subset of the other)
  how-to union and intersection           -> D4 (counts for only-A / both / only-B)
  how-to Venn diagram                     -> D4
  negative number                         -> D1 (Chile's goal difference; Algeria's and Austria's changes are signed)
  how-to add with negative numbers        -> D1 (Austria: +3 plus -1)
  how-to compare two or more values       -> D1, D2, D5, D6 (ranking by the ladder; comparing ceilings)
  how-to convert numbers to percents      -> D3, D4, D6 (safe cells as a percent of all the cells; the ceiling)
  percent                                 -> D6
RESULT: PASS
```

"Forces" test per case-write §10: could a competent student produce each deliverable correctly without ever performing the named skill? D3 cannot state the grid's cell count without the Fundamental Counting Principle; D4's three counts and its subset statement cannot be produced without intersection and set difference; D1's table has a negative goal difference and a signed update; D3/D4/D6's percents are required outputs.

Note: Probability is deliberately NOT claimed. The 49 cells are a counting device, not probabilities (MA1).
