# Learning Goals — Baseball Lineup

Bidirectional deliverable ↔ skill matrix. Legacy conversion, 2026-08-01.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — batting-average table for all 15 players (hits, at-bats, AVG rounded to 3 decimals) | `advanced-numbers-how-to-divide-decimal-numbers`, `fractions-fractions`, `measurement-rounding`, `measurement-how-to-round-a-number-to-a-specified-place-value` |
| D2 — plate-appearance outcome breakdown for all 15 players (6 percentages, rounded to nearest tenth) | `advanced-numbers-percent`, `advanced-numbers-how-to-convert-numbers-to-percents`, `measurement-rounding`, `measurement-how-to-round-a-number-to-a-specified-place-value` (reused — a second, distinct rounding task) |
| D3 — both lineups' combined AVG and mean-of-individual AVG, with one sentence on why they differ | `statistics-and-probability-mean`, `statistics-and-probability-how-to-find-the-mean-of-a-set-of-data`, `number-sense-how-to-compare-two-or-more-values` |
| D4 — one original bar graph comparing the two lineups | `number-sense-bar-graph` |
| D5 — number of distinct batting orders for a fixed 9-player lineup, via the Fundamental Counting Principle | `discrete-mathematics-fundamental-counting-principle`, `discrete-mathematics-how-to-apply-the-fundamental-counting-principle-to-count-outcomes` |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 12    new_coverage: 2
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each skill** (*could a competent Hero produce the deliverable correctly
without ever performing this skill?*):

- `how-to-divide-decimal-numbers` — batting average is literally hits ÷ at-bats; there is no way to
  produce D1's table without a decimal division for all 15 players. Forced.
- `fractions` — before it is a decimal, hits/AB is a fraction (a real ratio of two counted
  quantities); Appendix C states the ratio explicitly as the definition students work from. Forced.
- `rounding` / `how-to-round-a-number-to-a-specified-place-value` — Appendix C's Assumption 2 fixes
  the rounding convention (3 decimals for AVG, nearest tenth of a percent for D2); a Hero cannot
  match anyone else's table without applying it. Forced by both D1 and D2, independently.
- `percent` / `how-to-convert-numbers-to-percents` — D2 explicitly asks for a 6-way percentage
  breakdown of plate-appearance outcomes; there is no percent-free way to produce it. Forced.
- `mean` / `how-to-find-the-mean-of-a-set-of-data` — D3 explicitly asks for the mean of each
  lineup's 9 individual batting averages, stated *separately* from the combined figure, precisely
  so a Hero has to compute an actual mean rather than reuse the combined-average division. Forced.
- `how-to-compare-two-or-more-values` — D3's own closing instruction ("one sentence on why these
  two numbers are not identical") requires comparing the combined and mean figures directly, and
  Challenge 2's pitch requires comparing the two candidates' lineups overall. Forced by D3.
- `bar-graph` — D4 requires one original bar graph. The case does not mandate a specific chart type
  for Challenge 2(b)'s general "original visual display," so this spine skill is claimed only
  through D4's own explicit instruction, not through Challenge 2 generically. Forced.
- `fundamental-counting-principle` / `how-to-apply-the-fundamental-counting-principle-to-count-outcomes`
  — D5 explicitly asks for the count of distinct 9-player batting orders, and Appendix C's
  Assumption 3 leans on that exact number (362,880) to justify why the case sets ordering aside.
  This is genuine new content: the original 2020-21 Guide Notes ask "does order matter?" but the
  pre-Discrete-Math spine had no vocabulary to capture a real answer. Forced.

No skill here is claimed on the strength of "the case is about statistics generally" — each one
traces to a specific verb in a specific deliverable. See `case.json.legacy_conversion_note` for the
16 skills the original pre-pipeline matrix tagged to this case that did **not** survive this test
(mostly bare-vocabulary terms like "Number"/"Data"/"Greater Than" with no deliverable actually
forcing them, plus Histogram/Pie Chart, which Challenge 2 never specifically requires).
