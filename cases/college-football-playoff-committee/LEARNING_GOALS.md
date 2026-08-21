# Learning Goal Check — Playoff Committee

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 Human-Poll Standings Table (percent-of-maximum AP points, per team) | advanced-numbers-percent, advanced-numbers-how-to-convert-numbers-to-percents |
| D2 Computer Power-Rating Table (percent-of-ceiling SRS, per team) | advanced-numbers-percent, advanced-numbers-how-to-convert-numbers-to-percents |
| D3 Composite Selection Score Table (mean of Human% and Machine% for 5+ teams) | statistics-and-probability-mean, statistics-and-probability-how-to-find-the-mean-of-a-set-of-data |
| D4 Supporting-Evidence Brief (5+ data points, at least one a calculated mean) | statistics-and-probability-mean, statistics-and-probability-how-to-find-the-mean-of-a-set-of-data |

**"Forces" test applied:** could a competent student produce D1 or D2 without computing a
part-of-a-whole as a percent for every row in a 25-team table? No — the percent-of-maximum and
percent-of-ceiling columns are the entire point of those two tables. Could a student produce D3
without averaging two numbers per team? No — "the mean of the two" is stated explicitly as the
required output. Could a student satisfy D4's "at least one of the five must itself be a
calculated mean" without performing that skill? No — it is an explicit sub-requirement.

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 4    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**On `new_coverage[]` being empty:** every skill this case's real deliverables force —
`advanced-numbers-percent` (n=48), `advanced-numbers-how-to-convert-numbers-to-percents` (n=36),
`statistics-and-probability-mean` (n=24), `statistics-and-probability-how-to-find-the-mean-of-a-
set-of-data` (n=22) — already has coverage elsewhere in the spine. The zero-`n` skills currently
in `standards_spine.json` (a handful of geometry/calculus/discrete-math terms and how-tos — see
`legacy_conversion_note` in `case.json`) have no honest connection to a poll-vs-power-rating
comparison case: nothing in the real underlying data (AP voting points, SRS ratings, win-loss
records) forces a volume, a derivative, or a truth table. Rather than bolt on an unreachable
skill just to populate `new_coverage[]`, this case is submitted with it legitimately empty, per
`case-write` SKILL.md's own allowance and the precedent set by `cases/gerrymandering`
(`new_coverage: []` with a documented `legacy_conversion_note`).
