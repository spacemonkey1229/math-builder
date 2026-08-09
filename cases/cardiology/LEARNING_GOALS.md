# Learning Goals — Cardiology

Bidirectional deliverable ↔ skill matrix. Legacy conversion, 2026-08-02.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — 5-year survival rate per therapy, percent difference | `advanced-numbers-percent` |
| D2 — Ejection Fraction from SV/EDV | `measurement-ratio`, `advanced-numbers-how-to-convert-numbers-to-percents` |
| D3 — Year 1-5 total expenses per therapy | `advanced-numbers-how-to-multiply-decimal-numbers`, `advanced-numbers-how-to-add-decimal-numbers` |
| D4 — slope and y-intercept of each cost line | `statistics-and-probability-slope`, `statistics-and-probability-how-to-identify-the-slope-of-a-line-given-a-set-of-data-or-a-graph-o` |
| D5 — recommendation weighing survival, EF, and cost | `number-sense-how-to-compare-two-or-more-values` |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 8    new_coverage: 1
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each skill** (*could a competent Hero produce the deliverable correctly
without ever performing this skill?*):

- `percent` — D1 explicitly asks for the survival-rate gap stated as a percent. Forced.
- `ratio` / `how-to-convert-numbers-to-percents` — D2 requires computing SV/EDV as a ratio, then
  converting that ratio to a percent (Ejection Fraction is conventionally reported as a percent,
  not a raw decimal). Forced.
- `how-to-multiply-decimal-numbers` / `how-to-add-decimal-numbers` — D3's five-year totals require
  multiplying a monthly rate by 12 (and by the year count) and adding CABG's one-time surgical
  charge to its accumulating follow-up cost. Forced.
- `slope` / `how-to-identify-the-slope-of-a-line-given-a-set-of-data-or-a-graph-o` — D4 explicitly
  requires reading the yearly rate (slope) and fixed cost (y-intercept) off the Year 1-5 cost table
  each Hero just built in D3. Genuine new coverage (n=0 pre-conversion): no other case currently
  forces this skill. Forced.
- `how-to-compare-two-or-more-values` — D5's own instruction requires weighing three separate
  numbers (survival rate, Ejection Fraction, cost) against each other directly. Forced.

No skill here is claimed on the strength of "the case is about medicine generally" — each one
traces to a specific verb in a specific deliverable. See `case.json.legacy_conversion_note` for why
this conversion declares 5-year survival rate (not total cost) as the graded primary metric — the
real cost gap is driven almost entirely by CABG's one-time surgical charge and is too large to
honestly force within SPEC's 20% balance cap.
