# Learning Goals — Fixed Or Flex

Bidirectional deliverable ↔ skill matrix, per `skills/case-write/SKILL.md` §10.

## Deliverable → Skills

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 build-up table (unit rates, trips per $, riders' worth, gap as % of larger) | measurement-how-to-convert-an-amount-with-compound-units, advanced-numbers-how-to-convert-numbers-to-percents, measurement-ratio, advanced-numbers-percent |
| D2 break-even sheet (solve for ρ_F; percent of today's productivity; trips per hour) | advanced-operations-how-to-solve-a-one-step-equation, advanced-numbers-how-to-find-the-percent-of-a-number |
| D3 access-weight statement (solve for tie weight w) | advanced-operations-how-to-solve-a-one-step-equation |
| D4 signed-gap trend (D = vans − fixed; slope of line through 2022 and 2024; RY2025 extension) | advanced-numbers-how-to-subtract-with-negative-numbers, advanced-numbers-how-to-divide-with-negative-numbers, advanced-numbers-how-to-add-with-negative-numbers, statistics-and-probability-how-to-identify-the-slope-of-a-line-given-a-set-of-data-or-a-graph-o, advanced-numbers-negative-number, statistics-and-probability-slope |
| D5 decision memo (passenger-miles lens margin as a percent) | advanced-numbers-how-to-convert-numbers-to-percents, measurement-how-to-convert-an-amount-with-compound-units |

## Skills → Deliverable (reverse check)

Every claimed id is reached by at least one deliverable above (D1: compound units, numbers to percents, Ratio, Percent; D2: one-step equation, percent of a number; D3: one-step equation; D4: subtract/add/divide with negatives, slope how-to, Negative Number, Slope; D5: numbers to percents, compound units).

## Forces test

- **D1** cannot be done without dividing dollars by hours and trips by hours and combining them into trips per dollar (compound units), and the gap-as-a-percent-of-the-larger is a number-to-percent conversion.
- **D2**: `2,698.4 × ρ_F = 2,523.7` is a one-step equation; "93.5% of today's 4.698" is a percent of a number.
- **D3**: `2,698.4 = 2,523.7 × w` is a one-step equation.
- **D4**: D is negative in the decision year (subtracting a larger from a smaller number); the slope is a negative total change divided by a positive number of years (divide with negatives); the extension adds a negative to a negative. A competent student cannot produce the line without these. Honest limit: each is a one-step operation, so the skills are *thin by design*, not deep. They are forced by D4, not by the dilemma itself: a student can choose A or B without D4.
- **Not claimed:** `how to multiply with negative numbers`. An earlier draft projected RY2026 as 2 × −318.8; the shipped D4 stops at RY2025 (one addition), so no multiplication is forced. `how to find a whole given the percent and the part` and `how to find a missing amount in a proportion` were considered and dropped: a competent student reaches hours and trips by plain division or unit rates, so neither is forced.

## Learning goal check

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 14    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS (new_coverage empty -> reinforcement_note; the live spine has 0 skills at n=0)
```
