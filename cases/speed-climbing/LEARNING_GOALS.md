# Learning Goals — Speed Climbing

Bidirectional deliverable ↔ skill matrix (SPEC §1.7 / skills/case-write §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 complete roster, both national teams | number-sense-how-to-compare-two-or-more-values, advanced-numbers-decimal, number-sense-data |
| D2 team-composite-score calculation | statistics-and-probability-mean, statistics-and-probability-median, statistics-and-probability-how-to-find-the-mean-of-a-set-of-data, advanced-numbers-how-to-add-decimal-numbers, advanced-numbers-how-to-divide-decimal-numbers |
| D3 consistency (range) analysis | statistics-and-probability-range, statistics-and-probability-outlier, advanced-numbers-how-to-subtract-decimal-numbers |
| D4 percent-improvement (6-month trend) | advanced-numbers-how-to-find-the-percent-of-a-number, advanced-numbers-how-to-subtract-decimal-numbers, advanced-numbers-how-to-divide-decimal-numbers |
| D5 two visual displays | number-sense-bar-graph, statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data, number-sense-data |
| D6 Twist recompute + justification | statistics-and-probability-mean, statistics-and-probability-median, statistics-and-probability-how-to-find-the-mean-of-a-set-of-data, number-sense-how-to-compare-two-or-more-values |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 6    claimed skills: 14    new_coverage: 0 (legacy conversion, see below)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Forces test applied to each skill** (*could a competent student produce the deliverable correctly
without ever performing this skill?*):

- **mean / median / how-to-find-the-mean** — D2's team-composite formula is literally "mean +
  median"; there is no route to a correct D2 without computing both. D6 repeats this under the
  Twist.
- **range / outlier** — D3 explicitly asks for the range across three timed climbs and an
  explanation of what an outlier climb (e.g. Jesse's or Kylie's wild single-run swings) does and
  does not tell you. No range computation, no D3.
- **how-to-find-the-percent-of-a-number** — D4's percent-improvement calculation over six months
  requires it directly: (old − new) / old × 100 is a percent-of-a-number computation at its core.
- **how-to-compare-two-or-more-values** — D1's roster selection is fundamentally a 12-way ranking
  task; D6's "who replaces whom" is a comparison between an alternate's time and the departed
  athlete's time.
- **decimal / add / subtract / divide decimals** — every climb time in Appendices A and B is a
  decimal number of seconds; D1/D2/D3/D4 cannot be completed without decimal arithmetic on this
  exact data.
- **bar-graph / data** — D5 requires a ranked display of all twelve athletes' times, which is a bar
  graph or an equivalent ranked chart of data.
- **how-to-create-a-scatter-plot** — D5's second required visual is explicitly a six-month trend
  comparison across athletes — the natural, and simplest correct, chart type for six sequential
  monthly data points per athlete is a scatter plot (or line-through-points), not a single bar.

**Why `new_coverage[]` is honestly empty, not padded.** All 14 claimed skills already had `n >= 1`
in `readmodel/standards_spine.json` before this conversion (range 3–36). Ten of the fourteen were
already tagged `covered_by: "Speed Climbing"` from the pre-pipeline corpus scan (mean, median,
range, outlier, how-to-find-the-mean, how-to-compare-two-or-more-values,
how-to-find-the-percent-of-a-number, bar-graph, number-sense-data — nine explicit, plus this
conversion's own read confirms the tenth, decimal, is genuinely forced too). The remaining three —
scatter-plot and the three decimal-arithmetic how-tos beyond the vocabulary term — are real skills
this specific conversion's D4/D5 deliverables force, but each already has other cases covering it
(n=8, n=25, n=25, n=24), so none qualifies as `new_coverage[]` under SPEC §7's `n==0` test. Per
`skills/case-readiness/SKILL.md`'s legacy-conversion carve-out on T1-10 (2026-08-13), an honestly
empty `new_coverage[]` on a legacy conversion downgrades to a GAP, not a BLOCKER — see
`case.json.new_coverage_note`. No skill was added to `standards[]` to manufacture a false positive
here; each of the fourteen was checked against the forces test above before being kept.
