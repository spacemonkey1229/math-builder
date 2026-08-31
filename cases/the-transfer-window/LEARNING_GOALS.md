# LEARNING GOALS — The Transfer Window

Bidirectional deliverable ↔ skill matrix. Run per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — parametric position equations, each trajectory | pre-calculus-parametric-equation, pre-calculus-parameter |
| D2 — eliminate the parameter / rectangular equation / target-radius crossing check | pre-calculus-how-to-eliminate-the-parameter-to-find-a-rectangular-equation |
| D3 — propellant-mass-fraction and payload-mass calculation | advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number |
| D4 — primary-metric table (kg payload per day of transit) | advanced-numbers-how-to-divide-decimal-numbers |
| D5 — cumulative radiation-dose estimate | measurement-how-to-convert-an-amount-with-compound-units |
| D6 — recommendation, defended with D4/D5 | advanced-numbers-how-to-divide-decimal-numbers (reinforcement — re-examines D4's division under a changed assumption; introduces no new spine skill of its own, matching the reinforcement pattern used elsewhere in this project, e.g. The Compute Lease's D6) |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 6    claimed skills: 7    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Note on `new_coverage: 0`.** This is expected and correct for this batch, not a defect. Per the
concept sheet (`cases/_concepts/CONCEPTS_pim-sector-gaps_2026-08-24.md`, C9), this is a
**second-pass/redundancy case**: Pre-Calculus/Polar And Parametric already has `n>=1` coverage on
all three of `pre-calculus-parametric-equation`, `pre-calculus-parameter`, and
`pre-calculus-how-to-eliminate-the-parameter-to-find-a-rectangular-equation` (each verified at
`n=1` directly against `readmodel/standards_spine.json` at authoring time, in the case-write
session — this is the group's first case beyond its single existing entry, per the concept
sheet's own framing, "the first case in this corpus to touch the group at all beyond its single
existing entry"). The remaining four claimed skills
(`advanced-numbers-percent` n=52, `advanced-numbers-how-to-find-the-percent-of-a-number` n=55,
`advanced-numbers-how-to-divide-decimal-numbers` n=30, `measurement-how-to-convert-an-amount-with-
compound-units` n=14) are heavily covered elsewhere and were never candidates for
`new_coverage[]`. `new_coverage[]` is therefore correctly left empty in `case.json` — this case
exists to thicken Polar And Parametric's coverage depth (so the group has more than one usable
case in rotation), not to close a zero-coverage gap.

**Forces test applied to each mapping** — *could a competent student produce this deliverable
correctly without ever performing this skill?*

- **D1 — no.** A trajectory's position over time cannot be written as a single x-vs-y rule without
  introducing a third variable that both x and y depend on — the parameter. The deliverable
  explicitly demands the parameter be named and its physical meaning explained (what it
  represents, what values it ranges over), which a student cannot do without understanding what a
  parameter is and what a parametric equation is in the first place, not just plugging numbers
  into a memorized ellipse formula.
- **D2 — no.** Finding the rectangular equation requires solving each of the two parametric
  equations for a trigonometric function of the parameter and combining them via the Pythagorean
  identity to eliminate the parameter entirely — this is the deliverable's core artifact, not a
  restatement of D1. The target-radius crossing check that follows depends directly on having that
  rectangular equation in hand; a student who never eliminates the parameter has no equation to
  check the crossing against.
- **D3 — no.** A propellant mass fraction is, by definition, a percent of the kick stage's total
  wet mass, and the deliverable requires every percent to be shown as arithmetic. A student who
  never computes percent of a number cannot produce a mass-fraction figure, only restate one.
- **D4 — no.** The primary metric itself — kilograms of payload per day of transit — is a
  quotient of two other deliverables' results (D2's transit time, D3's payload mass). A student
  cannot produce this deliverable without performing that division for both options, and the
  deliverable explicitly requires the division to be shown.
- **D5 — no.** Radiation dose accumulates as a rate (rad per day) applied over a duration (days),
  and the deliverable requires the resulting compound-unit conversion (rate × time → total dose)
  to be shown explicitly, with the result compared against a tolerance stated in the same or a
  convertible unit — a student cannot produce a comparable cumulative-dose figure without
  performing that conversion.
- **D6 — n/a (reinforcement).** D6 introduces no new skill; it requires the student to re-examine
  D4's division under a changed assumption ("what would have to change... for your recommendation
  to flip"), which reinforces `advanced-numbers-how-to-divide-decimal-numbers` from a new angle
  rather than forcing a distinct skill of its own. This mirrors the reinforcement pattern already
  used in this project's case corpus (e.g. The Compute Lease's D6, The Placement Test's D4).

## Skill verification against the spine (run at write time)

```
n= 1 term    | Pre-Calculus/Polar And Parametric | Parametric Equation | pre-calculus-parametric-equation
n= 1 term    | Pre-Calculus/Polar And Parametric | Parameter | pre-calculus-parameter
n= 1 how-to  | Pre-Calculus/Polar And Parametric | How to eliminate the parameter to find a rectangular equation | pre-calculus-how-to-eliminate-the-parameter-to-find-a-rectangular-equation
n=52 term    | Advanced Numbers/Percents | Percent | advanced-numbers-percent
n=55 how-to  | Advanced Numbers/Percents | How to find the percent of a number | advanced-numbers-how-to-find-the-percent-of-a-number
n=30 how-to  | Advanced Numbers/Decimals | How to divide decimal numbers | advanced-numbers-how-to-divide-decimal-numbers
n=14 how-to  | Measurement/Units | How to convert an amount with compound units | measurement-how-to-convert-an-amount-with-compound-units
```

All seven ids confirmed present in `readmodel/standards_spine.json` with the kinds and counts
shown above. None have `n == 0`, so none qualify for `new_coverage[]` — consistent with this case
being a second-pass/redundancy write, not a gap-closing one.
