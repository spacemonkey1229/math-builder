# Learning Goals — The Referral Cut

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 referral-fee conversion + post-referral proceeds | fractions-simplify, fractions-how-to-simplify-a-fraction, fractions-how-to-multiply-a-fraction-and-a-mixed-number, fractions-mixed-number, fractions-improper-fraction, fractions-how-to-convert-a-mixed-number-to-an-improper-fraction, fractions-how-to-convert-an-improper-fraction-to-a-mixed-number |
| D2 Option A (FBM) true net margin per unit | fractions-mixed-number |
| D3 Option B's true total fulfillment fee | fractions-how-to-multiply-two-fractions, fractions-how-to-convert-an-improper-fraction-to-a-mixed-number, fractions-mixed-number |
| D4 Option B net margin + monthly totals | fractions-how-to-multiply-a-fraction-and-a-whole-number, fractions-mixed-number, fractions-improper-fraction |
| D5 working-capital comparison | fractions-how-to-multiply-two-mixed-numbers, fractions-mixed-number |
| D6 original visual display | fractions-mixed-number, fractions-how-to-convert-an-improper-fraction-to-a-mixed-number |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever
performing this skill? If yes, the mapping is fake.

- **D1** cannot be produced without simplifying: Amazon's published referral fee percentage (15%)
  converts to an unsimplified fraction over 100 (15/100) before it reduces to lowest terms (3/20)
  — the deliverable explicitly demands "an exact fraction in lowest terms." It then cannot be
  produced without multiplying a mixed number (the list price, $18-3/4) by a fraction (the
  referral retention fraction, 17/20) to find post-referral proceeds — the standard method
  requires converting the mixed number to an improper fraction first, multiplying straight
  across, and converting the result back into a mixed number to state the answer as a dollar
  figure a human reads ("$15-15/16," not "$255/16"). Genuinely forces `simplify`, the simplify
  how-to, `mixed-number`, `improper-fraction`, both conversion how-tos, and the
  fraction-and-mixed-number multiplication itself.
- **D2** requires carrying D1's mixed-number post-referral proceeds through a mixed-number
  subtraction against two further mixed-number costs, and stating the result as a mixed number
  rather than a decimal, as the case's fraction-only instruction requires. Genuinely forces
  `mixed-number`.
- **D3** is impossible without multiplying two fractions together: the base fulfillment fee
  (expressed as a fraction of a dollar) and (1 + the surcharge fraction) are each fractions, and
  the deliverable explicitly requires combining them by multiplication — not by adding the
  surcharge's raw percentage number directly onto the fee (the case's built-in trap; see
  `FACILITATOR.md`). The result, an improper fraction, must then be converted to a mixed number to
  state the true total fee. A student who adds instead of multiplies produces a different, wrong
  total fee. Genuinely forces `multiply two fractions`, the improper-to-mixed how-to, and
  `mixed-number`.
- **D4** requires a mixed-number subtraction analogous to D2, and then requires multiplying each
  option's per-unit net margin (a mixed number) by Appendix A's guaranteed monthly order quantity,
  40 units — a whole number. A student who cannot multiply a mixed number by a whole number cannot
  produce the required monthly totals. Genuinely forces `multiply a fraction and a whole number`,
  `mixed-number`, and `improper-fraction` (the intermediate product before restating as a mixed
  number).
- **D5** requires multiplying two mixed numbers together, twice: weeks of inventory (a mixed
  number, 6-1/2 or 2-1/4) by weekly production cost (a mixed number, $340-3/8) for each option
  separately. There is no way to produce this deliverable's dollar figures without performing
  mixed-number-by-mixed-number multiplication. Genuinely forces `multiply two mixed numbers` and
  `mixed-number`.
- **D6** explicitly requires every dollar amount on the visual to be labeled as an exact mixed
  number, never a rounded decimal — impossible without first converting each of D4's and D5's raw
  multiplication outputs (some of which are improper fractions) back into mixed-number form for
  the label. A student who labels the chart with decimals has not satisfied the deliverable as
  written. Genuinely forces `mixed-number` and the improper-to-mixed how-to.

```
LEARNING GOAL CHECK
  deliverables: 6    claimed skills: 10    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

See `case.json.reinforcement_note` for the full accounting. Every claimed skill was checked
against `readmodel/standards_spine.json` before writing and none is `n == 0` — the lowest are the
four Multiplication of Fractions how-tos this concept specifically targets (three at `n=1`, one at
`n=2`). A full spine scan run the same day (2026-09-09) found **zero** skills anywhere in the
322-skill spine at `n==0` — the entire corpus has already closed every true zero-coverage gap (see
the prior batch's publish commit, "spine reaches 0 uncovered"). This means `new_coverage[]` cannot
be non-empty for *any* case written against the current spine snapshot, not just this one — a
corpus-wide condition, not a defect in this case's skill selection. This case reinforces all 4
thin skills in Fractions/Multiplication Of Fractions (the concept's named target group) plus 6
adjacent thin Fractions/Understanding Fractions skills (`simplify`, `mixed-number`,
`improper-fraction`, and their three matching how-tos) that are genuinely required as intermediate
steps to carry out the multiplications D1/D3/D4/D5/D6 demand — via the reinforcement carve-out
(T1-10, `skills/case-readiness/SKILL.md`, 2026-08-17), the same pattern used in
`cases/the-special-order/case.json`. `new_coverage[]` is `[]`, honestly, not padded.
