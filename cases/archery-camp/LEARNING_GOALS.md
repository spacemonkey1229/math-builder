# Learning Goals — Archery Camp

Bidirectional deliverable ↔ skill matrix. Legacy conversion, 2026-08-01.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — total ranges and max capacity | `advanced-numbers-how-to-add-decimal-numbers` |
| D2 — counselors required and total pay | `basic-operations-multiplication`, `advanced-numbers-how-to-multiply-decimal-numbers` |
| D3 — total cost and per-participant charge | `advanced-numbers-decimal`, `advanced-numbers-how-to-divide-decimal-numbers` |
| D4 — number of 5-field combinations from 9 fields | `statistics-and-probability-combination`, `statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination` |
| D5 — recommendation comparing both combinations | `number-sense-how-to-compare-two-or-more-values` |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 8    new_coverage: 1
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each skill** (*could a competent Hero produce the deliverable correctly
without ever performing this skill?*):

- `how-to-add-decimal-numbers` — D1's range/capacity totals sum each field's range count from
  Appendix B. Forced.
- `multiplication` / `how-to-multiply-decimal-numbers` — D2's counselor pay is a direct
  rate x count x days multiplication. Forced.
- `decimal` / `how-to-divide-decimal-numbers` — D3's per-participant charge is total cost divided
  by 140 attendees, a decimal quotient. Forced.
- `combination` / `how-to-determine-the-number-of-outcomes-of-a-combination` — D4 explicitly asks
  for the count of 5-field combinations from 9 fields, order irrelevant. This is genuine new
  coverage (n=1 pre-conversion): no other case currently forces this specific how-to. Forced.
- `how-to-compare-two-or-more-values` — D5's own instruction requires a direct comparison of both
  combinations' cost and capacity. Forced.

No skill here is claimed on the strength of "the case is about event planning generally" — each one
traces to a specific verb in a specific deliverable. See `case.json.legacy_conversion_note` for why
this conversion designs its own range-per-field data (the original Appendix B was not
machine-readable).
