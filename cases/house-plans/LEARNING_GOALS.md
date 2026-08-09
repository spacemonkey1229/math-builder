# Learning Goals — House Plans

Bidirectional deliverable ↔ skill matrix. Legacy conversion, 2026-08-01.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — total heated square footage, Ranch shown as sum of two floors | `geometry-area`, `basic-operations-addition` |
| D2 — the true spending ceiling (find the whole given the percent and the part) | `advanced-numbers-percent`, `advanced-numbers-how-to-find-a-whole-given-the-percent-and-the-part-of-the-whole` |
| D3 — most upgraded affordable tier and its build cost | `advanced-numbers-decimal`, `advanced-numbers-how-to-multiply-decimal-numbers` |
| D4 — amenity package within remaining budget, final total | `advanced-numbers-how-to-subtract-decimal-numbers` |
| D5 — recommendation comparing both floor plans | `number-sense-how-to-compare-two-or-more-values` |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 8    new_coverage: 1
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each skill** (*could a competent Hero produce the deliverable correctly
without ever performing this skill?*):

- `area` — D1 requires reporting each plan's heated square footage, the case's own area metric.
  Forced.
- `addition` — the Ranch Estate's total (D1) is explicitly the sum of its two floors (3,722 +
  772); there is no other way to arrive at 4,494 sq ft as given. Forced.
- `percent` / `how-to-find-a-whole-given-the-percent-and-the-part-of-the-whole` — D2 explicitly
  requires finding the true ceiling from "$495,000 is 90% of the total" — the reverse of a
  percent-of-a-number problem. This is genuine new coverage (n=1 pre-conversion): no other case
  currently forces this specific direction. Forced.
- `decimal` / `how-to-multiply-decimal-numbers` — D3's build cost is a per-square-foot decimal
  rate multiplied by a whole-number square footage; there is no whole-number-only path to the
  correct dollar figure. Forced.
- `how-to-subtract-decimal-numbers` — D4's remaining budget is the ceiling minus the build cost,
  both decimal dollar figures. Forced.
- `how-to-compare-two-or-more-values` — D5's own instruction (compare both floor plans' final
  configuration against the ceiling) requires a direct comparison. Forced.

No skill here is claimed on the strength of "the case is about home-buying generally" — each one
traces to a specific verb in a specific deliverable. See `case.json.legacy_conversion_note` for the
real architectural-PDF source of the square-footage figures.
