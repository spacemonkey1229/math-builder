# Learning Goals — Food Rationing

Bidirectional deliverable ↔ skill matrix. Test applied to every row: *could a competent student
produce this deliverable correctly without ever performing this skill?* If yes, the mapping is cut.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — total caloric inventory (21-item multiply-and-sum conversion of Appendix C into calories, using Appendix D's per-unit rates, several of which are compound units like kcal/lb or kcal/oz) | basic-operations-multiplication, basic-operations-how-to-multiply-any-two-numbers, advanced-numbers-how-to-multiply-decimal-numbers, basic-operations-addition, basic-operations-how-to-add-multi-digit-numbers, measurement-unit, measurement-how-to-convert-an-amount-from-one-unit-to-another-unit, measurement-how-to-convert-an-amount-with-compound-units |
| D2 — stated, defended rationing horizon (the family doesn't know if rescue is 1 day or 1 month away; the student must pick and defend a number of days, in consistent day units) | measurement-how-to-convert-between-units-of-time, basic-operations-division |
| D3 — per-person rationing plan for the chosen option, plus percent of each person's full recommended calories delivered | advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number, advanced-numbers-how-to-convert-numbers-to-percents, measurement-ratio, measurement-proportion, measurement-how-to-find-equivalent-ratios, basic-operations-division, basic-operations-how-to-divide-a-multi-digit-number-by-a-2-digit-number |
| D4 — total-days-of-coverage comparison, Option A vs. Option B, plus percent difference | basic-operations-division, basic-operations-how-to-divide-a-multi-digit-number-by-a-2-digit-number, advanced-numbers-how-to-find-the-percent-of-a-number, number-sense-how-to-compare-two-or-more-values |
| D5 — two visual displays: bar graph (A vs. B totals) and pie chart (chosen plan's daily split by person) | number-sense-bar-graph, statistics-and-probability-pie-chart, number-sense-data, statistics-and-probability-how-to-create-a-pie-chart-given-a-set-of-data |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 21    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

Every claimed skill traces to at least one deliverable above; every deliverable has a non-empty
skills column.

## Why `new_coverage[]` is honestly empty

"Food Rationing" was checked against `readmodel/standards_spine.json`'s `covered_by[]` before
writing this case, and it was **not** pre-tagged there (unlike Family Trip/Airstrike — see
`readmodel/reconcile_queue.json`, which shows only 2 LOW-confidence proposed skills for this case,
one a false positive from "faces" in the source Overview text). Each of the 21 ids above was
individually checked against the spine (see `case-write`'s validation script output below) and
every one already has `n >= 4` — none is a true zero-coverage gap this specific case closes. Per
`skills/case-readiness/SKILL.md`'s legacy-conversion carve-out on T1-10 (2026-08-13), this
downgrades the empty-`new_coverage[]` finding from a BLOCKER to a recorded GAP because
`case.json.legacy_conversion_note` is present — this case is being *formalized* from a real,
richly-documented legacy source (case doc + guide notes + a full 45-minute Socratic plan + a real
food inventory), not freshly authored with no purpose. No skill was padded into `standards[]`
because it "sounded related" — every one of the 21 is directly forced by D1–D5's real arithmetic.

## Spine verification (run at write time)

```
n=29 term    | Basic Operations/Addition | Addition
n=23 how-to  | Basic Operations/Addition | How to add multi-digit numbers
n=23 term    | Basic Operations/Multiplication | Multiplication
n=20 how-to  | Basic Operations/Multiplication | How to multiply any two numbers
n=23 term    | Basic Operations/Division | Division
n=20 how-to  | Basic Operations/Division | How to divide a multi-digit number by a 2-digit number
n=27 how-to  | Advanced Numbers/Decimals | How to multiply decimal numbers
n=23 term    | Measurement/Units | Unit
n=10 how-to  | Measurement/Units | How to convert an amount from one unit to another unit
n=11 how-to  | Measurement/Units | How to convert an amount with compound units
n=11 how-to  | Measurement/Units | How to convert between units of time
n=36 term    | Advanced Numbers/Percents | Percent
n=35 how-to  | Advanced Numbers/Percents | How to find the percent of a number
n=22 how-to  | Advanced Numbers/Percents | How to convert numbers to percents
n=12 term    | Measurement/Ratios And Proportions | Ratio
n= 8 term    | Measurement/Ratios And Proportions | Proportion
n= 4 how-to  | Measurement/Ratios And Proportions | How to find equivalent ratios
n=36 how-to  | Number Sense/Comparisons | How to compare two or more values
n=31 term    | Number Sense/Measurement And Data | Bar Graph
n=25 term    | Statistics And Probability/Displaying Data | Pie Chart
n=26 term    | Number Sense/Measurement And Data | Data
n=20 how-to  | Statistics And Probability/Displaying Data | How to create a pie chart given a set of data
```

No id was missing from the spine. All 21 have `n >= 4`, confirming the `new_coverage[]` GAP note
above rather than a false zero.
