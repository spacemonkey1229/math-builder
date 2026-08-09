# Learning Goals — Catering

Bidirectional deliverable ↔ skill matrix. Legacy conversion, 2026-08-01.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — total servings, set up as a proportion from the 7% buffer | `advanced-numbers-percent`, `measurement-how-to-find-a-missing-amount-in-a-proportion` |
| D2 — total revenue and ingredient cost for the chosen menu | `advanced-numbers-decimal`, `advanced-numbers-how-to-multiply-decimal-numbers`, `advanced-numbers-how-to-add-decimal-numbers` |
| D3 — total event + delivery fees | `basic-operations-multiplication` |
| D4 — net profit | `advanced-numbers-how-to-subtract-decimal-numbers` |
| D5 — recommendation comparing both events | `number-sense-how-to-compare-two-or-more-values` |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 8    new_coverage: 1
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each skill** (*could a competent Hero produce the deliverable correctly
without ever performing this skill?*):

- `percent` / `how-to-find-a-missing-amount-in-a-proportion` — D1 explicitly asks for the 7% buffer
  to be set up and solved as a proportion, not just computed directly. This is genuine new coverage
  (n=1 pre-conversion): no other case in the corpus currently forces this specific how-to. Forced.
- `decimal` / `how-to-multiply-decimal-numbers` / `how-to-add-decimal-numbers` — D2's revenue and
  cost totals require multiplying each menu item's decimal price by the serving count, then summing
  across items. Forced.
- `multiplication` — D3's event fee (rate x hours) and delivery fee (rate x miles) are both direct
  multiplication. Forced.
- `how-to-subtract-decimal-numbers` — D4's net profit is a direct subtraction chain (revenue - cost
  - fees). Forced.
- `how-to-compare-two-or-more-values` — D5's own instruction requires comparing both events' net
  profit directly. Forced.

No skill here is claimed on the strength of "the case is about running a business generally" —
each one traces to a specific verb in a specific deliverable. See `case.json.legacy_conversion_note`
for why this conversion designs its own order specifications (the original's Appendix A was blank)
and drops the original's prep-time deliverable (no real data exists for it).
