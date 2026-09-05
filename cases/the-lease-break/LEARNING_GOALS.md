# Learning Goals — The Lease Break

Bidirectional deliverable ↔ skill matrix. Run at `case-write` time, before `case.json` is emitted.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 lease-terms comparison table | number-sense-how-to-compare-two-or-more-values |
| D2 stay-full-term effective monthly cost | advanced-numbers-how-to-add-decimal-numbers, advanced-numbers-how-to-divide-decimal-numbers, measurement-proportion |
| D3 break-at-month-6 effective monthly cost | advanced-numbers-how-to-add-decimal-numbers, advanced-numbers-how-to-divide-decimal-numbers, measurement-proportion, measurement-ratio |
| D4 deposit-and-total-cost percent table | advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number, advanced-numbers-how-to-find-a-whole-given-the-percent-and-the-part-of-the-whole, measurement-ratio |
| D5 recommendation memo | number-sense-how-to-compare-two-or-more-values |

## Coverage check

- Claimed skills (`standards[]`): 8
  - advanced-numbers-percent
  - measurement-proportion
  - measurement-ratio
  - advanced-numbers-how-to-find-the-percent-of-a-number
  - advanced-numbers-how-to-find-a-whole-given-the-percent-and-the-part-of-the-whole
  - advanced-numbers-how-to-add-decimal-numbers
  - advanced-numbers-how-to-divide-decimal-numbers
  - number-sense-how-to-compare-two-or-more-values

### Reasoning per skill (why each is genuinely forced, not decorative)

- **number-sense-how-to-compare-two-or-more-values** — D1 requires laying the two leases' terms side by side in a way that supports a decision; D5's memo requires comparing four cost figures (two leases × two scenarios) to pick a winner. A student could not produce either without comparing values.
- **advanced-numbers-how-to-add-decimal-numbers** — D2 and D3 both require adding a per-month amortized up-front cost (and, in D3, an amortized penalty) to the base monthly rent, in dollars-and-cents. Cannot skip addition and still produce a correct effective-monthly-cost figure.
- **advanced-numbers-how-to-divide-decimal-numbers** — D2 and D3 both require dividing a total up-front dollar cost (and, in D3, a penalty) by a number of months to amortize it. This division is the entire mechanism that makes "effective cost per month" different from "rent."
- **measurement-proportion** — D2 and D3 both require allocating a fixed up-front cost proportionally across the months actually lived in the unit — a direct proportional-reasoning task (fixed cost spread over a variable number of months changes the per-month share).
- **measurement-ratio** — D3's month-6 scenario and D4's percent table both require reasoning about one quantity (deposit, or termination penalty) relative to another (one month's rent, or a full year's rent) as a ratio before converting it to a percent.
- **advanced-numbers-percent** — D4's entire deliverable is expressing costs as percentages of a reference quantity (one month's rent; a full year's rent).
- **advanced-numbers-how-to-find-the-percent-of-a-number** — D4 explicitly requires calculating "what a full year of stated monthly rent alone would cost" as a reference figure and comparing a scenario's total against it as a percent — the forward direction (find X% of a known whole).
- **advanced-numbers-how-to-find-a-whole-given-the-percent-and-the-part-of-the-whole** — D4 explicitly requires the reverse direction: given the move-in cost (the part) and its relationship to one month's rent (the percent), or given a scenario's total cost as a stated percent of the annual-rent whole, work back to confirm the underlying whole. D4's text calls this out directly: "Show the arithmetic for both directions."

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 8    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

Every one of the 5 Challenge-3 deliverables (D1–D5) maps to at least one claimed skill. Every one
of the 8 claimed skills is forced by at least one deliverable (see reasoning above). Both
directions of the bidirectional check are clean.

## Note on `new_coverage[]` (see case.json for full detail)

`new_coverage[]` is empty for this case. As of 2026-09-03 (the date `readmodel/standards_spine.json`
was checked), no skill in the spine with `n == 0` fits this case's actual math (percent, ratio,
proportion, decimal arithmetic, comparison) — the only six `n == 0` skills in the entire spine are
Depth, Digit, Volume Of A Sphere, the Quotient Rule, Taylor Series, and Finding A Taylor Series At
A Point, none of which this case could honestly force. This is a deviation from the concept
sheet's framing (`cases/_concepts/CONCEPTS_life-skills-first10_2026-09-03.md`, concept #5), which
described `advanced-numbers-how-to-find-a-whole-given-the-percent-and-the-part-of-the-whole` as a
skill this case "would close" — that skill's actual `n` is 2, not 0, so claiming it as
`new_coverage[]` would violate the hard rule against marking a gap closed that the student never
touched. See case.json's `reinforcement_note` for the full statement.
