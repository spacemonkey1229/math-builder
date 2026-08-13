# Learning Goals — A Coach's Dilemma

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 season shooting-percentage table | advanced-numbers-percent, advanced-numbers-how-to-convert-numbers-to-percents, advanced-numbers-how-to-divide-decimal-numbers, advanced-numbers-decimal, number-sense-place-value |
| D2 best/worst FT and 3PT shooter | number-sense-how-to-compare-two-or-more-values, measurement-how-to-round-a-number-to-a-specified-place-value, measurement-rounding, number-sense-place-value |
| D3 one-and-one probability (p²) | statistics-and-probability-probability, statistics-and-probability-independent-event, statistics-and-probability-how-to-determine-the-probability-of-a-compound-event, advanced-numbers-percent |
| D4 single-shot vs. compound comparison (the trap) | number-sense-how-to-compare-two-or-more-values, statistics-and-probability-how-to-determine-the-probability-of-a-single-event, advanced-numbers-percent |
| D5 original bar graph | number-sense-bar-graph, basic-operations-division, basic-operations-quotient |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** cannot be produced without converting a makes/attempts ratio to a percent (dividing a decimal, then expressing it as a percent) for 8 players × 3 shot types = 24 conversions, each rounded to a stated decimal place -- which requires identifying the tenths-place digit. Genuinely forces `advanced-numbers-percent`, `-how-to-convert-numbers-to-percents`, `-how-to-divide-decimal-numbers`, `advanced-numbers-decimal`, `number-sense-place-value`.
- **D2** requires sorting/comparing 8 players' percentages (from D1) to find the extremes, and rounding is used throughout D1's table to a consistent decimal place (the tenths place) so comparisons are apples-to-apples. Genuinely forces `number-sense-how-to-compare-two-or-more-values`, `measurement-how-to-round-a-number-to-a-specified-place-value`, `measurement-rounding`, `number-sense-place-value`.
- **D3** is impossible without recognizing the one-and-one as two dependent-on-the-first-make attempts (an "event" whose probability compounds) and computing p². Genuinely forces `statistics-and-probability-probability`, `-independent-event`, `-how-to-determine-the-probability-of-a-compound-event`, `advanced-numbers-percent`.
- **D4** requires comparing the raw single-attempt percentage (a single-event probability) against D3's compound result and explaining, in writing, why squaring changes the ranking. Genuinely forces `number-sense-how-to-compare-two-or-more-values`, `statistics-and-probability-how-to-determine-the-probability-of-a-single-event`, `advanced-numbers-percent`.
- **D5** requires computing division-based percentages for at least 4 players and rendering them as bars with labeled axes/categories. Genuinely forces `number-sense-bar-graph`, `basic-operations-division`, `basic-operations-quotient`.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 15    new_coverage: 1
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

Checked every claimed skill's `n` value in `readmodel/standards_spine.json`. Only `number-sense-place-value`
is n=0 (genuinely uncovered anywhere in the spine before this case) — D1/D2 force it honestly,
since rounding every computed percentage to a stated decimal place requires identifying which
digit sits in that place. `statistics-and-probability-independent-event` (n=2) and
`statistics-and-probability-how-to-determine-the-probability-of-a-compound-event` (n=3) are also
genuinely forced by D3/D4 but are not n=0, so they stay in `standards[]` without counting toward
`new_coverage[]`. Checked the full n=0 list in the spine (137 skills, dominated by geometry,
pre-calculus, calculus, and discrete-math) for anything else this case might naturally force —
nothing else fit without padding.
