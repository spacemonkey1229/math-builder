# Learning Goals — Bathroom Problems

Bidirectional deliverable ↔ skill matrix. Test applied to every row: *could a competent student
produce this deliverable correctly without ever performing this skill?* If yes, the mapping is cut.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — minute-by-minute bathroom schedule (cumulative start/slot/finish times from a fixed 6:50 AM start, including converting decimal-minute slot lengths into minutes:seconds, and comparing each finish time against a stated leave-by time) | measurement-time, measurement-how-to-add-and-subtract-time, measurement-how-to-find-elapsed-time, measurement-how-to-find-the-start-or-end-time-given-the-start-or-end-and-the-elapsed-time, basic-operations-how-to-add-multi-digit-numbers, measurement-how-to-convert-an-amount-with-compound-units, number-sense-how-to-compare-two-or-more-values |
| D2 — total shower-water-usage calculation (shower minutes × GPM per person, then summed) | measurement-unit, basic-operations-how-to-multiply-any-two-numbers, basic-operations-how-to-add-multi-digit-numbers |
| D3 — hot-water-availability calculation (First Hour Rating ÷ GPM = minutes of hot water; compare to D2's total shower minutes needed) | basic-operations-how-to-divide-a-multi-digit-number-by-a-2-digit-number, measurement-how-to-convert-an-amount-from-one-unit-to-another-unit, number-sense-how-to-compare-two-or-more-values |
| D4 — needs-weighted proportional allocation table (each person's share of the 227-minute total need, scaled to the 70-minute window) and flat equal share, then a useful-minutes total and percent-difference comparison across Option A vs. Option B | measurement-ratio, measurement-proportion, measurement-how-to-find-equivalent-ratios, measurement-how-to-find-a-missing-amount-in-a-proportion, basic-operations-how-to-divide-a-multi-digit-number-by-a-single-digit-number, advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number, advanced-numbers-how-to-convert-numbers-to-percents |
| D5 — two visual displays: bar graph (percent-of-need-met, A vs. B, per family member) and pie chart (the 70-minute window's actual division under the chosen option) | number-sense-bar-graph, statistics-and-probability-pie-chart, statistics-and-probability-how-to-create-a-pie-chart-given-a-set-of-data, number-sense-data |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 23    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

Every claimed skill traces to at least one deliverable above; every deliverable has a non-empty
skills column.

## Why `new_coverage[]` is honestly empty

"Bathroom Problems" is a legacy conversion (`legacy_conversion_note` in `case.json`), being
*formalized* from a real source case, not freshly authored with no pedagogical purpose. Each of the
23 skill ids above was individually checked against `readmodel/standards_spine.json` (see the spine
verification below) and every one already has `n >= 2` — none is a true zero-coverage gap this
specific case closes. Per `skills/case-readiness/SKILL.md`'s legacy-conversion carve-out on T1-10
(2026-08-13), this downgrades the empty-`new_coverage[]` finding from a BLOCKER to a recorded GAP.
No skill was padded into `standards[]` because it "sounded related" — every one is directly forced
by D1–D5's real arithmetic: time addition and elapsed-time/compound-unit conversion for the
schedule (D1), rate multiplication/division and unit conversion for the water calculations (D2/D3),
ratio/proportion and percent for the needs-weighted allocation and useful-minutes comparison (D4),
and the two required visual displays (D5).

## Spine verification (run at write time)

```
n=19 term    | Measurement/Units | Time
n=14 how-to  | Measurement/Time | How to add and subtract time
n=11 how-to  | Measurement/Time | How to find elapsed time
n= 2 how-to  | Measurement/Time | How to find the start or end time given the start or end and the elapsed time
n=29 how-to  | Basic Operations/Addition | How to add multi-digit numbers
n=26 term    | Measurement/Units | Unit
n=12 how-to  | Measurement/Units | How to convert an amount with compound units
n=27 how-to  | Basic Operations/Multiplication | How to multiply any two numbers
n=26 how-to  | Basic Operations/Division | How to divide a multi-digit number by a 2-digit number
n=14 how-to  | Measurement/Units | How to convert an amount from one unit to another unit
n=43 how-to  | Number Sense/Comparisons | How to compare two or more values
n=43 term    | Advanced Numbers/Percents | Percent
n=44 how-to  | Advanced Numbers/Percents | How to find the percent of a number
n=29 how-to  | Advanced Numbers/Percents | How to convert numbers to percents
n=18 term    | Measurement/Ratios And Proportions | Ratio
n=13 term    | Measurement/Ratios And Proportions | Proportion
n= 5 how-to  | Measurement/Ratios And Proportions | How to find equivalent ratios
n= 6 how-to  | Measurement/Ratios And Proportions | How to find a missing amount in a proportion
n=19 how-to  | Basic Operations/Division | How to divide a multi-digit number by a single-digit number
n=40 term    | Number Sense/Measurement And Data | Bar Graph
n=31 term    | Statistics And Probability/Displaying Data | Pie Chart
n=22 how-to  | Statistics And Probability/Displaying Data | How to create a pie chart given a set of data
n=32 term    | Number Sense/Measurement And Data | Data
```

No id was missing from the spine. All 23 have `n >= 2`, confirming the `new_coverage[]` GAP note
above rather than a false zero.
