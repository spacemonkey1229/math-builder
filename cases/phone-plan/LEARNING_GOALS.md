# Learning Goals — Phone Plan

Bidirectional deliverable ↔ skill matrix. Legacy conversion, 2026-08-01.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — linear cost equation for each carrier, slope and y-intercept identified | `advanced-operations-variable`, `advanced-operations-equation`, `statistics-and-probability-slope`, `statistics-and-probability-y-intercept`, `statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data` |
| D2 — total monthly cost, with tax, at 2/3/4 lines | `advanced-numbers-percent`, `advanced-numbers-how-to-find-the-percent-of-a-number` |
| D3 — break-even line count via a system of equations | `statistics-and-probability-system-of-equations`, `statistics-and-probability-how-to-solve-a-system-of-linear-equations` |
| D4 — recommendation at 2 lines, checked against the 3-line plan | `number-sense-how-to-compare-two-or-more-values` |

## LEARNING GOAL CHECK

```
deliverables: 4    claimed skills: 10    new_coverage: 2
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each skill** (*could a competent Hero produce the deliverable correctly
without ever performing this skill?*):

- `variable` / `equation` / `slope` / `y-intercept` / `how-to-write-a-linear-equation-given-a-set-of-data`
  — D1 explicitly asks for each carrier's cost written as a linear equation with slope and
  y-intercept named, from Appendix A's given per-line rates. Forced.
- `percent` / `how-to-find-the-percent-of-a-number` — D2 requires applying Appendix B's 8% tax
  rate to a computed subtotal. Forced.
- `system-of-equations` / `how-to-solve-a-system-of-linear-equations` — D3 explicitly asks for the
  break-even line count, found by solving the two carriers' equations together. This is genuine new
  coverage (n=0 pre-conversion for both): no other case in the corpus currently forces this pair.
  Forced.
- `how-to-compare-two-or-more-values` — D4's own instruction (recommend at 2 lines, then check
  against the 3-line plan) requires a direct numeric comparison at two different line counts.
  Forced.

No skill here is claimed on the strength of "the case is about algebra generally" — each one traces
to a specific verb in a specific deliverable. See `case.json.legacy_conversion_note` for why this
conversion designs its own clean pricing data rather than the original's now-unrecoverable carrier
screenshots.
