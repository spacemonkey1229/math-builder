# Learning Goals — Protein Per Dollar

Bidirectional deliverable ↔ skill matrix (case-write §10, MCS-10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — Unit rates: grams of protein per dollar, dozen/pound to grams | measurement-ratio, measurement-how-to-find-equivalent-ratios |
| D2 — Month and quarter totals in grams, and their difference | measurement-how-to-find-equivalent-ratios |
| D3 — Margin (gap ÷ winner) and break-even prices as percent changes | advanced-numbers-how-to-find-the-percent-of-a-number |
| D4 — Two blended orders | measurement-ratio, measurement-how-to-find-equivalent-ratios |
| D5 — Monthly grams-per-dollar line chart, Jan 2006 – Aug 2024 | measurement-ratio |
| D6 — Dry-bean grams per dollar, the difference, and how many times as many | measurement-ratio, advanced-numbers-how-to-find-the-percent-of-a-number |

## LEARNING GOAL CHECK

```
deliverables: 6    claimed skills: 3    new_coverage: 0 (reinforcement_note on file)
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
  measurement-ratio                                          -> D1, D4, D5, D6
  measurement-how-to-find-equivalent-ratios                  -> D1, D2, D4
  advanced-numbers-how-to-find-the-percent-of-a-number       -> D3, D6
RESULT: PASS
```

## Why each skill is genuinely forced

- **measurement-how-to-find-equivalent-ratios (n=7):** D1 and D2 cannot be produced without scaling "75 grams per dozen" to "grams per dollar" and "grams per dollar" to a monthly budget; a student who does not scale a ratio cannot fill the table.
- **measurement-ratio (n=30):** D1, D5 and D6 are ratios of grams to dollars computed 224 times (D5) and compared as "how many times as many" (D6).
- **advanced-numbers-how-to-find-the-percent-of-a-number (n=90):** D3 requires the margin as a percent of the winner's value and the break-even prices as percent changes of the August price (price × (1 − p) or price × (1 + p)).

## New coverage

None. Checked `readmodel/standards_spine.json` live on 2026-10-28: no skill has n == 0 anywhere in the spine, so `new_coverage[]` is correctly empty per SPEC §4's n == 0 rule. The `reinforcement_note` in `case.json` records the adjacent thin skills considered and not claimed. `statistics-and-probability-range` (n=9) was considered and dropped: no deliverable forces it (the chart only plots the series).
