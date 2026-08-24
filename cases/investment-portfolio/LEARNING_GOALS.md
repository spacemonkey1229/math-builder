# Learning Goals — Investment Portfolio

Bidirectional deliverable ↔ skill matrix. Legacy conversion, 2026-08-22.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — allocation table + pie chart + $10,000 breakdown, both portfolios | `measurement-ratio`, `measurement-proportion`, `advanced-numbers-percent`, `advanced-numbers-how-to-find-the-percent-of-a-number`, `advanced-numbers-how-to-convert-percents-to-numbers`, `statistics-and-probability-pie-chart`, `statistics-and-probability-how-to-create-a-pie-chart-given-a-set-of-data`, `measurement-currency`, `advanced-numbers-decimal`, `advanced-numbers-decimal-number`, `advanced-numbers-how-to-read-decimal-numbers`, `advanced-numbers-how-to-multiply-decimal-numbers` |
| D2 — return/risk/drawdown comparison table + mean/range of each portfolio's 5 return figures | `number-sense-how-to-compare-two-or-more-values`, `number-sense-greater-than`, `number-sense-less-than`, `number-sense-equal`, `advanced-numbers-negative-number`, `advanced-numbers-positive-number`, `advanced-numbers-how-to-subtract-with-negative-numbers`, `measurement-rounding`, `measurement-how-to-round-a-number-to-a-specified-place-value`, `number-sense-data`, `number-sense-number`, `statistics-and-probability-mean`, `statistics-and-probability-how-to-find-the-mean-of-a-set-of-data`, `statistics-and-probability-range` |
| D3 — return-vs-holding-period coordinate-plane chart | `geometry-coordinate-plane`, `geometry-x-axis`, `geometry-y-axis`, `geometry-origin`, `geometry-coordinate-pair-also-ordered-pair`, `geometry-how-to-graph-a-coordinate-pair-on-the-coordinate-plane`, `statistics-and-probability-slope`, `measurement-time`, `advanced-numbers-percent` (reused) |
| D4 — 30-year portfolio-value projection chart | `advanced-numbers-percent` (reused), `advanced-numbers-how-to-find-the-percent-of-a-number` (reused), `advanced-numbers-how-to-convert-percents-to-numbers` (reused), `advanced-numbers-how-to-multiply-decimal-numbers` (reused), `advanced-numbers-how-to-add-decimal-numbers`, `geometry-how-to-graph-a-coordinate-pair-on-the-coordinate-plane` (reused), `statistics-and-probability-y-intercept`, `measurement-time` (reused), `measurement-currency` (reused), `measurement-unit` |
| D5 — Year-3 -35% shock recalculation | `advanced-numbers-integer`, `advanced-numbers-negative-number` (reused), `advanced-numbers-positive-number` (reused), `advanced-numbers-how-to-add-with-negative-numbers`, `advanced-numbers-how-to-subtract-with-negative-numbers` (reused), `number-sense-how-to-compare-two-or-more-values` (reused), `advanced-numbers-how-to-find-the-percent-of-a-number` (reused) |
| D6 — worked 20-year Sharpe-ratio comparison + bar graph | `advanced-numbers-decimal` (reused), `advanced-numbers-how-to-read-decimal-numbers` (reused), `advanced-numbers-how-to-divide-decimal-numbers`, `advanced-numbers-how-to-subtract-with-negative-numbers` (reused), `number-sense-bar-graph`, `number-sense-how-to-compare-two-or-more-values` (reused) |

## LEARNING GOAL CHECK

```
deliverables: 6    claimed skills: 41    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each skill** (*could a competent Hero produce the deliverable correctly
without ever performing this skill?*):

- `measurement-ratio` / `measurement-proportion` / percent family — D1's allocation table cannot
  be built without expressing each asset class as a percent of the whole and then converting that
  percent to a dollar amount of a $10,000 sample investment. Forced.
- `statistics-and-probability-pie-chart` / its how-to — D1 explicitly requires a pie chart, the
  natural (and only spine-available) chart type for a whole-broken-into-parts allocation. Forced.
- `advanced-numbers-decimal` family (read/multiply/add/divide) — every dollar figure and every
  percentage in this case (allocations, returns, standard deviations, drawdowns, the 30-year
  projection, the Sharpe ratio) is a decimal number, and D1/D4 specifically require multiplying and
  adding them repeatedly (percent-of-$10,000; year-over-year compounding), while D6's Sharpe ratio
  is literally a division of two decimals. Forced, distinctly, by different deliverables.
- `number-sense-how-to-compare-two-or-more-values` / greater-than / less-than / equal — D2
  explicitly requires comparing each return/stdev/drawdown pair directly ("which is bigger, by how
  much"); D5 requires comparing shocked vs. unshocked outcomes; D6 requires comparing two Sharpe
  ratios. Forced, three separate times, on three separate pairs of numbers.
- `advanced-numbers-negative-number` / `positive-number` / `integer` / add/subtract-with-negative
  — every maximum-drawdown figure in Appendix C is negative, D5's shock scenario is a -35% return,
  and D2's "by how much" comparison of two negative drawdown figures is a genuine
  subtract-with-negative-numbers computation. Forced.
- `statistics-and-probability-mean` / its how-to, and `statistics-and-probability-range` — D2
  explicitly asks for the mean and the range of each portfolio's five Appendix C return figures,
  a real derived computation distinct from any single cited value. Forced.
- `geometry-coordinate-plane` family (x-axis, y-axis, origin, coordinate pair, its how-to) — D3 and
  D4 both explicitly require labeled coordinate-plane charts with plotted points. Forced.
- `statistics-and-probability-slope` — D3's return-vs-holding-period chart has a genuine rate of
  change (return per additional year of holding period) between plotted points. Forced.
- `statistics-and-probability-y-intercept` — D4's projection chart's Year-0 point (before any
  return has compounded, portfolio value = $0) is the chart's actual y-intercept. Forced.
- `measurement-time` / `measurement-currency` / `measurement-unit` — D3/D4's axes are literally
  years and dollars; every value plotted or tabled in this case is one or the other. Forced.
- `measurement-rounding` / its how-to — D2/D4/D6 all require consistent rounding (Appendix D, MA4)
  to make Hero-to-Hero comparison possible. Forced.
- `number-sense-bar-graph` — D6 explicitly requires a bar graph. Forced.
- `number-sense-data` / `number-sense-number` — general vocabulary genuinely exercised across every
  table in this case (Appendix C is explicitly a data table Heroes must read and manipulate).
  Forced by D2's direct engagement with that table.

No skill here is claimed on the strength of "the case is about investing generally" — each one
traces to a specific verb in a specific deliverable. `new_coverage[]` is genuinely empty: all 41
claimed standards already had `n>0` in `standards_spine.json` before this case (this is a legacy
conversion — SPEC §8's non-empty-`new_coverage[]` rule is downgraded to a recorded GAP for exactly
this case type per `skills/case-readiness/SKILL.md`'s T1-10 legacy-conversion carve-out).

**Dropped from the 74 originally-tagged skills, and why** (see `case.json.legacy_conversion_note`
for the full text):

- The ~20 `Basic Operations` single/2-digit arithmetic skills — every arithmetic operation in this
  case's deliverables is on multi-digit decimal/percent figures; the more specific `Advanced
  Numbers` decimal how-tos already claimed are what those computations genuinely force, not the
  elementary single/2-digit versions.
- `number-sense-age` — Benjamin's age and the 30-year horizon to age 60 are narrative/background
  only; no deliverable performs a calculation that specifically forces the Age vocabulary term as
  opposed to a plain year count (`measurement-time` already covers the genuine forcing).
- `statistics-and-probability-histogram` / its how-to — no deliverable calls for a histogram; D1
  and D6 already force the two chart types (pie chart, bar graph) genuinely used.
- `advanced-numbers-how-to-convert-numbers-to-percents` and `measurement-estimating` — caught by
  case-readiness's own T1-11 mutual-reachability check on the first Tier 1 run (2026-08-22): both
  were listed in the case's draft Appendix F vocabulary/how-to list but no deliverable actually
  forces the numbers-to-percents direction (every percent conversion in this case's deliverables
  runs percent-to-number, not the reverse) or genuine estimation (every value in this case is
  computed exactly, never estimated). Removed from `standards[]` and Appendix F rather than
  padding a deliverable to manufacture a fake forcing.
- `statistics-and-probability-x-intercept` — no chart in this case has a meaningful x-intercept
  (portfolio value and annualized return never cross zero on the x-axis); `y-intercept` is kept
  because D4's Year-0 starting value genuinely is one.
