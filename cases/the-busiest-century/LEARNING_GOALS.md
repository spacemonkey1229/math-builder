# Learning Goals — The Busiest Century

Bidirectional deliverable ↔ skill matrix, per `skills/case-write/SKILL.md` §10.

## Deliverable → Skills

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 ranking from Appendix B; gap between the two winning centuries as a percent of the larger | advanced-numbers-how-to-subtract-decimal-numbers, advanced-numbers-how-to-divide-decimal-numbers, advanced-numbers-how-to-convert-numbers-to-percents, advanced-numbers-percent |
| D2 box-and-whisker plot of dates per site (five-number summary, IQR, fences, outliers, mean) | statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data, statistics-and-probability-box-and-whisker-plot, statistics-and-probability-quartiles, statistics-and-probability-outlier, statistics-and-probability-median, statistics-and-probability-mean, statistics-and-probability-how-to-find-the-mean-of-a-set-of-data |
| D3 table of five cuts (winner on each reading, its lead over the runner-up as a percent of the winner, do the readings agree) | advanced-numbers-how-to-convert-numbers-to-percents, advanced-numbers-percent, advanced-numbers-how-to-subtract-decimal-numbers |
| D4 weighted score (1 − s) × dates score + s × sites score; break-even weight; wall sentence | advanced-numbers-how-to-divide-decimal-numbers, advanced-numbers-how-to-multiply-decimal-numbers |

## Skills → Deliverable (reverse check)

Every claimed id is reached by at least one deliverable above (D1 and D3: subtract/divide decimals, numbers to percents, Percent; D2: box-and-whisker how-to and term, Quartiles, Outlier, Median, Mean, mean how-to; D4: divide and multiply decimals).

## Forces test

- **D1**: the gap 272.0 − 244.4 is a decimal subtraction; "as a percent of the larger" is a decimal division converted to a percent.
- **D2**: the plot cannot be drawn without finding Q1, the median and Q3 from the frequency table in Appendix C, computing the 1.5 × IQR fences, and deciding which values are outliers (the term is used as a rule). The mean dates per site is a total divided by a count (the how-to for the mean); comparing it with the median is the point of the sentence.
- **D4**: each score is a decimal quotient (value ÷ largest value) and the blend multiplies decimals by (1 − s) and s.
- **D3**: each cut's lead is (winner − runner-up) ÷ winner, a decimal subtraction and division written as a percent; ten such leads are needed (five cuts × two readings), so the percent skill is exercised repeatedly. The 'do the readings agree' judgment is a comparison and forces nothing extra.
- **Honest limit:** the box plot is the thinnest skill reached (spine n=1) and is forced by D2; everything else is reinforcement of widely covered skills. Break-even weight can be read from a table of weights in steps of 0.1, so no equation-solving skill is claimed.
- **Not claimed:** histogram how-to (no deliverable asks for one), weighted-mean/equation skills, "non-linear" (the calibration curve is not a deliverable), any probability skill (the calibration and the product rule are given, not asked for).

## Learning goal check

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 12    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS (new_coverage empty -> reinforcement_note; the live spine has 0 skills at n=0)
```
