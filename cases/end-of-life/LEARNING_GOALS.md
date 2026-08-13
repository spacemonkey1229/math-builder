# Learning Goals — End Of Life

Bidirectional deliverable ↔ skill matrix (case-write §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — day-by-day hospital bill ledger, extended forward | `advanced-numbers-how-to-add-decimal-numbers`, `number-sense-data`, `measurement-currency` |
| D2 — total out-of-pocket cost calculation | `advanced-numbers-how-to-multiply-decimal-numbers`, `advanced-numbers-how-to-add-decimal-numbers` |
| D3 — insurance-coverage percent | `advanced-numbers-percent`, `advanced-numbers-how-to-find-the-percent-of-a-number` |
| D4 — assets map + running liquid balance | `advanced-numbers-how-to-subtract-decimal-numbers`, `number-sense-how-to-compare-two-or-more-values` |
| D5 — "running out of money" day determination | `measurement-how-to-round-a-number-to-a-specified-place-value`, `number-sense-how-to-compare-two-or-more-values` |
| D6 — asset-composition vs. cumulative-bill visual display | `statistics-and-probability-pie-chart`, `statistics-and-probability-how-to-create-a-pie-chart-given-a-set-of-data` |

`measurement-currency` is mapped explicitly to D1 (reading and recording real dollar-and-cents
figures from Appendix A into a ledger is itself a currency-unit skill, not incidental to it) so
the reachability check has a genuine, checkable deliverable-to-skill edge rather than a "well,
money is everywhere" hand-wave.

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 6    claimed skills: 11    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

Verification, deliverable by deliverable — "could a competent student produce this deliverable
correctly without ever performing this skill?":

- **D1** cannot be produced without repeatedly adding the fixed daily rate to a running total
  (`advanced-numbers-how-to-add-decimal-numbers`) across real dollar-and-cents figures
  (`number-sense-data` — organizing a dated series of values into a table is itself the skill,
  not incidental to it).
- **D2** cannot be produced without multiplying the daily rate by a day count and adding the
  Day-1 one-time charge — both decimal operations are load-bearing; a student who only adds
  (treating every day as $1) or only multiplies (dropping the one-time ER charge) gets a visibly
  wrong total.
- **D3** cannot be produced without computing (insurance pay/adj ÷ gross charge) × 100 for a
  real day in Appendix A — a direct, unavoidable application of finding what percent one number
  is of another.
- **D4** cannot be produced without subtracting each day's balance from the running liquid total
  and comparing that running total against zero (and against the brokerage-inclusive total) to
  decide which asset group to draw on next.
- **D5** cannot be produced without comparing the cumulative-cost function against two different
  fixed thresholds (liquid assets, total net worth) and rounding a fractional day count (e.g.
  13.52) up to the whole day the threshold is actually crossed on.
- **D6** cannot be produced without converting a set of category totals (Appendix B's asset
  groups, or the three checkpoint bill totals) into proportional wedges of a circle — the
  mechanical definition of building a pie chart from data.

No claimed skill in `standards[]` is unreached by this list; no deliverable's skills column is
empty. `new_coverage[]` is honestly empty — see `case.json.new_coverage_note` for why (this
legacy case's title was already present in every one of these 11 skills' `covered_by[]` before
this conversion began, so none of them had `n == 0` to close).
