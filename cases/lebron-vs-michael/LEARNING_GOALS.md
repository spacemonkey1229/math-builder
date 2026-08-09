# Learning Goals — LeBron vs. Michael

Bidirectional deliverable ↔ skill matrix. Legacy conversion, 2026-08-02.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — career regular-season 2pt/3pt/FT% | `advanced-numbers-percent`, `advanced-numbers-how-to-convert-numbers-to-percents` |
| D2 — career regular-season mean assists/rebounds per game | `statistics-and-probability-mean`, `statistics-and-probability-how-to-find-the-mean-of-a-set-of-data` |
| D3 — same five stats for the playoffs | `advanced-numbers-percent`, `statistics-and-probability-mean` |
| D4 — box-and-whisker plot of career PPG, median + quartiles | `statistics-and-probability-box-and-whisker-plot`, `statistics-and-probability-quartiles`, `statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data` |
| D5 — self-designed weighted algorithm + recommendation | `number-sense-how-to-compare-two-or-more-values` |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 8    new_coverage: 1
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each skill** (*could a competent Hero produce the deliverable correctly
without ever performing this skill?*):

- `percent` / `how-to-convert-numbers-to-percents` — D1 and D3 both explicitly require converting
  a makes/attempts ratio into a percent, career-wide, for three separate shot types. Forced.
- `mean` / `how-to-find-the-mean-of-a-set-of-data` — D2 and D3 both explicitly require a
  games-weighted mean of assists and rebounds — not a simple average of season averages
  (Assumption 2). Forced.
- `box-and-whisker-plot` / `quartiles` / `how-to-create-a-box-and-whisker-plot-given-a-set-of-data`
  — D4 explicitly requires building a box-and-whisker plot from real season-by-season data and
  reading off its median and quartiles. Genuine new coverage (n=1 pre-conversion) for the how-to
  skill: no other case currently forces it. Forced.
- `how-to-compare-two-or-more-values` — D5's own instruction requires applying a self-designed
  formula to compare both players directly. Forced.

No skill here is claimed on the strength of "the case is about basketball generally" — each one
traces to a specific verb in a specific deliverable. See `case.json.legacy_conversion_note` for why
this conversion declares career regular-season 3-point percentage (not the case's subjective
"algorithm" verdict) as the graded primary metric — it is one of the case's own required stats and a
real, close 5.42% gap, while championships, scoring titles, and other lopsided real gaps stay as
disclosed context for each Hero's own algorithm.
