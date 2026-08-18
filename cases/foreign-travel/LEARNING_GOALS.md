# LEARNING GOALS — Foreign Travel

Bidirectional deliverable ↔ skill matrix (`case-write` §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — total transportation cost table, currency-converted, grand total | `measurement-currency`, `measurement-how-to-convert-an-amount-from-one-unit-to-another-unit`, `basic-operations-addition`, `basic-operations-sum`, `basic-operations-how-to-add-multi-digit-numbers`, `advanced-numbers-how-to-add-decimal-numbers` |
| D2 — complete timed itinerary, all 9 days, elapsed travel time across the March 28 clock change | `measurement-time`, `measurement-how-to-find-elapsed-time`, `measurement-how-to-add-and-subtract-time`, `measurement-how-to-convert-between-units-of-time`, `measurement-how-to-find-the-start-or-end-time-given-the-start-or-end-and-the-elapsed-time` |
| D3 — percent breakdown pie chart of the chosen option's own total cost | `advanced-numbers-percent`, `advanced-numbers-how-to-find-the-percent-of-a-number`, `statistics-and-probability-pie-chart`, `statistics-and-probability-how-to-create-a-pie-chart-given-a-set-of-data` |
| D4 — bar graph, chosen option vs. estimated other option, 3+ categories | `number-sense-bar-graph`, `number-sense-how-to-compare-two-or-more-values` |

## LEARNING GOAL CHECK

```
deliverables: 4    claimed skills: 17    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forces test applied to each skill** (*could a competent student produce the deliverable correctly
without ever performing this skill?*):

- `measurement-currency` / `...convert-an-amount-from-one-unit-to-another-unit` — every appendix
  price is given in GBP or EUR; a USD grand total (D1) is impossible without converting every line.
- `basic-operations-addition` / `sum` / `...add-multi-digit-numbers` / `...add-decimal-numbers` —
  D1's grand total is a sum of ~6-9 dollars-and-cents line items; no shortcut around it.
- `measurement-time` / `...find-elapsed-time` / `...add-and-subtract-time` /
  `...convert-between-units-of-time` / `...find-the-start-or-end-time-given-...-elapsed-time` — D2
  requires computing true elapsed travel time from posted local departure/arrival clock times that
  are offset by a time zone that does not change mid-trip (Appendix B/E), and sequencing 9 days of
  legs into a single coherent clock.
- `advanced-numbers-percent` / `...find-the-percent-of-a-number` /
  `statistics-and-probability-pie-chart` / `...how-to-create-a-pie-chart-given-a-set-of-data` — D3
  is explicitly a percent-of-total pie chart; cannot be produced without computing each category's
  share of D1's total.
- `number-sense-bar-graph` / `...how-to-compare-two-or-more-values` — D4 is explicitly a
  side-by-side bar comparison across categories; requires computing the *other* option's total
  from the same appendix data and setting the two totals against each other.

No claimed skill sits in `standards[]` without a deliverable requiring it; no deliverable produces
a usable artifact without at least one of these skills. `new_coverage[]` is empty — every skill
above already has `n >= 1` in the live spine (checked immediately before this file was written, see
`case.json.new_coverage_note`) — covered by `case.json.legacy_conversion_note` per the T1-10
legacy-conversion carve-out (`skills/case-readiness/SKILL.md`, "added 2026-08-13").
