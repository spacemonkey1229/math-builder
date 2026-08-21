# Learning Goals — Travel Planner

Bidirectional deliverable ↔ skill matrix. Legacy conversion, 2026-08-20.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — theme-park ticket cost table (list price by age category, discounted price by tier) | `advanced-numbers-percent`, `advanced-numbers-how-to-find-the-percent-of-a-number`, `advanced-numbers-decimal`, `advanced-numbers-how-to-multiply-decimal-numbers`, `basic-operations-multiplication` |
| D2 — hotel cost breakdown (nightly rate × nights, then 8.5% off) | `advanced-numbers-how-to-find-the-percent-of-a-number`, `advanced-numbers-how-to-multiply-decimal-numbers`, `basic-operations-multiplication` |
| D3 — Gina's 4% agency fee on the combined hotel-plus-ticket total | `advanced-numbers-how-to-find-the-percent-of-a-number`, `advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-without-exponents-or`, `advanced-numbers-how-to-add-decimal-numbers` |
| D4 — grand total vs. the $3,950 cap, margin in dollars and percent | `advanced-numbers-how-to-add-decimal-numbers`, `advanced-numbers-how-to-subtract-decimal-numbers`, `advanced-numbers-how-to-convert-numbers-to-percents` |
| D5 — day-by-day itinerary with start/end clock times per block | `measurement-how-to-add-and-subtract-time` |
| D6 — recommendation comparing both plans' totals and cap margins | `number-sense-how-to-compare-two-or-more-values` |

## LEARNING GOAL CHECK

```
deliverables: 6    claimed skills: 11    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each skill** (*could a competent Hero produce the deliverable correctly
without ever performing this skill?*):

- `percent` / `how-to-find-the-percent-of-a-number` — D1's 2%/6% tier discount, D2's 8.5% Priceline
  discount, and D3's 4% agency fee are each a direct percent-of-a-number calculation on a real
  dollar total from Appendix C/D. Forced.
- `decimal` / `how-to-multiply-decimal-numbers` — every price in Appendix C and D is a decimal
  dollar amount; D1 and D2 require multiplying a decimal unit price by a whole-number count (people,
  nights) or applying a decimal discount rate. Forced.
- `basic-operations-multiplication` — the same D1/D2 quantity × rate multiplications are, at their
  core, multiplication before any percent conversion is layered on. Forced.
- `how-to-evaluate-an-expression-with-multiple-operations-without-exponents-or` (order of
  operations) — D3's fee is 4% of a *sum* (discounted hotel + discounted tickets), which only
  resolves correctly if the Hero adds before taking the percent, not the other way around. This is
  the concrete order-of-operations trap the deliverable is built to force.
- `how-to-add-decimal-numbers` / `how-to-subtract-decimal-numbers` — D3 sums two discounted
  subtotals; D4 sums tickets + hotel + fee, then subtracts that grand total from $3,950 to find the
  dollar margin. Forced.
- `how-to-convert-numbers-to-percents` — D4 explicitly asks for the margin "as a percent of the
  cap," which requires converting a (cap − total) / cap ratio into a percent, not just reporting a
  dollar figure. Forced.
- `how-to-add-and-subtract-time` — D5 requires laying out a day's activities as a sequence of
  start/end clock times (park hours, meal breaks, beach time, return to hotel), which only works
  by adding and subtracting durations against a clock. Forced.
- `how-to-compare-two-or-more-values` — D6's own instruction requires directly comparing both
  plans' grand totals and cap margins, using real numbers for the plan not chosen as well as the
  one chosen. Forced.

No skill here is claimed on the strength of "the case is about planning a trip generally" — each
one traces to a specific verb in a specific deliverable. See `case.json.legacy_conversion_note` for
why every claimed skill already has n>0 in the standards spine (this conversion formalizes existing
corpus coverage rather than closing a fresh gap — the same carve-out `Family Trip` and
`Gerrymandering` document in their own `legacy_conversion_note`), and why D5's itinerary deliverable
was narrowed from the original source's open-ended "gas, food, and travel snack costs" list (no real
per-mile driving distance or food-cost data exists in the source or was found during research to
compute those honestly).
