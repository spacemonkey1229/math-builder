# Learning Goals — Psychologist

Bidirectional deliverable ↔ skill matrix. Legacy conversion, 2026-08-20.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — normalized-score table for all 27 applicants (5 categories → percent of pool max) | `measurement-ratio`, `advanced-numbers-percent`, `advanced-numbers-how-to-convert-numbers-to-percents` |
| D2 — per-applicant single-best normalized score and composite (mean) score | `number-sense-how-to-compare-two-or-more-values`, `statistics-and-probability-mean`, `statistics-and-probability-how-to-find-the-mean-of-a-set-of-data` |
| D3 — two ranked top-3 admit lists (by single-best, by composite) | `number-sense-how-to-compare-two-or-more-values` (reused — a second, distinct ranking task from D2's per-applicant figures) |
| D4 — one original bar graph comparing the two slates | `number-sense-bar-graph` |

## LEARNING GOAL CHECK

```
deliverables: 4    claimed skills: 7    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each skill** (*could a competent Hero produce the deliverable correctly
without ever performing this skill?*):

- `measurement-ratio` — converting a raw score into "percent of the category's pool-best score" is
  literally computing a ratio (raw score : pool-max) before it is ever expressed as a percent.
  D1 cannot be produced without forming this ratio for all 27 applicants × 5 categories. Forced.
- `percent` / `how-to-convert-numbers-to-percents` — D1 explicitly requires every raw score
  expressed as a percent of its category's pool max (Appendix C, MA1). There is no percent-free way
  to build the table. Forced.
- `mean` / `how-to-find-the-mean-of-a-set-of-data` — D2 explicitly asks for each applicant's
  composite score, defined in Appendix C (MA2) as the mean of their five category percentages,
  stated *separately* from the single-best figure so a Hero has to compute an actual mean rather
  than just take a maximum. Forced.
- `how-to-compare-two-or-more-values` — forced twice, independently: D2's "single-best normalized
  score" requires comparing an applicant's own five percentages to find their maximum; D3's two
  ranked top-3 lists require comparing all 27 applicants' D2 figures against each other to produce
  a rank order. Both are genuine comparison tasks, not the same computation restated.
- `bar-graph` — D4 requires one original bar graph. The case does not mandate a chart type for
  Challenge 2(b)'s general "original visual display," so this spine skill is claimed only through
  D4's own explicit instruction, not through Challenge 2 generically. Forced.

No skill here is claimed on the strength of "the case is about statistics generally" — each one
traces to a specific verb in a specific deliverable. `new_coverage[]` is genuinely empty: every one
of the 7 claimed skills already has `n>0` in `standards_spine.json` (this is a legacy conversion,
not new authorship — SPEC §8's non-empty-`new_coverage[]` rule is downgraded to a recorded GAP for
exactly this case type per `skills/case-readiness/SKILL.md`'s T1-10 legacy-conversion carve-out).
The spine was searched for any `n==0` skill plausibly related to normalization, weighted averages,
composite scores, percentile, or z-scores before concluding this — no such skill exists in
`standards_spine.json` at all (there is no z-score/standard-deviation/percentile skill in the
spine), so none of this case's genuinely-forced normalization/weighting content could ever have
counted as `new_coverage[]` regardless of authorship path. See `case.json.new_coverage_note` and
`legacy_conversion_note`.
