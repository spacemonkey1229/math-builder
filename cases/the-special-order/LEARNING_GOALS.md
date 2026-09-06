# Learning Goals — The Special Order

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 cut-list conversion table | fractions-mixed-number, fractions-improper-fraction, fractions-how-to-convert-an-improper-fraction-to-a-mixed-number, fractions-how-to-convert-a-mixed-number-to-an-improper-fraction |
| D2 rough-width calculation (common denominator) | fractions-equivalent-fractions, fractions-how-to-find-equivalent-fractions, fractions-improper-fraction, fractions-mixed-number, fractions-how-to-convert-an-improper-fraction-to-a-mixed-number |
| D3 waste-log reconciliation (simplify) | fractions-simplify, fractions-how-to-simplify-a-fraction, fractions-equivalent-fractions, fractions-how-to-find-equivalent-fractions |
| D4 true cost-per-door comparison | fractions-improper-fraction, fractions-mixed-number, fractions-how-to-convert-a-mixed-number-to-an-improper-fraction, fractions-how-to-convert-an-improper-fraction-to-a-mixed-number, fractions-equivalent-fractions |
| D5 original visual display (fraction strip) | fractions-equivalent-fractions, fractions-simplify |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever
performing this skill? If yes, the mapping is fake.

- **D1** cannot be produced correctly without a genuine two-way conversion: the cut list states
  the net width as a mixed number (1-3/4 in) but the rough-width math in D2 needs it as an
  improper fraction (7/4) to add against other fractions with unlike denominators, and the final
  answer has to be read back off a tape measure as a mixed number. A student who only ever writes
  "1-3/4" and never converts has not produced the conversion table the deliverable asks for.
  Genuinely forces `mixed-number`, `improper-fraction`, and both how-tos.
- **D2** is impossible without finding a common denominator across three different-denominator
  fractions (7/4, an eighths-based jointing allowance, and an eighths- or sixteenths-based kerf
  allowance) — a student who tries to add 7/4 + 1/4 + 1/8 without converting to a shared
  denominator will get a wrong total rough width. The final step explicitly requires converting
  the resulting improper-fraction sum back into a mixed number, because that is the form a rip-saw
  fence gauge is actually set to. Genuinely forces `equivalent-fractions`, the equivalent-fractions
  how-to, `improper-fraction`, `mixed-number`, and the improper-to-mixed how-to.
- **D3** is impossible without simplifying: Appendix D deliberately logs the same physical waste
  width as an unsimplified eighths fraction (Operator 1) and a reduced fraction (Operator 2), and
  the deliverable explicitly requires proving they are the same width before any total can be
  trusted. A student who skips simplification and treats the two log entries as different waste
  totals (the case's own built-in trap) fails this deliverable even if every other number in their
  pitch is correct. Genuinely forces `simplify`, the simplify how-to, `equivalent-fractions`, and
  the equivalent-fractions how-to (two fractions describing the same width are, by definition,
  equivalent fractions, and recognizing that is the same skill as reducing one to match the
  other's denominator).
- **D4** requires carrying D2's mixed-number rough width and D1's cut-list fractions through a
  real board-footage/cost calculation, and finding the batch-size breakeven requires comparing a
  per-door cost expressed in fraction terms against a threshold quantity (Appendix C's minimum
  order) also expressed in fractional board feet — a student who converts everything to decimals
  partway through has not produced this deliverable as specified (the deliverable is explicit:
  "computed entirely in fraction/mixed-number arithmetic"). Genuinely forces `improper-fraction`,
  `mixed-number`, both conversion how-tos, and `equivalent-fractions` (combining Appendix B's and
  Appendix C's differently-denominated figures).
- **D5** requires rendering D2's rough-width-vs-net-width split as a scaled fraction strip in
  eighths — which is impossible without first expressing every width (however it started, in
  fourths, eighths, or sixteenths) as an equivalent fraction over the same eighths denominator, and
  impossible to read cleanly without simplifying the resulting strip segments to their
  lowest-terms labels. Genuinely forces `equivalent-fractions` and `simplify`.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 8    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

See `case.json.reinforcement_note` for the full accounting. Every claimed skill was checked
against `readmodel/standards_spine.json` before writing and none is `n == 0` — the lowest are
`fractions-improper-fraction`, `fractions-mixed-number`, and both conversion how-tos, all at
`n=1`. This case reinforces all 8 thin (low-but-nonzero-coverage) skills in
Fractions/Understanding Fractions rather than closing a true zero-coverage gap, via the
reinforcement carve-out (T1-10, `skills/case-readiness/SKILL.md`, 2026-08-17) — the same pattern
used in `cases/the-deferred-repair/LEARNING_GOALS.md` and `cases/a-coachs-dilemma/LEARNING_GOALS.md`.
`new_coverage[]` is `[]`, honestly, not padded: including any of these 8 ids in `new_coverage[]`
would trip case-write's own anti-padding validator ("new_coverage[] claims a skill already
covered"), since each already has `n>=1`. This is a deliberate, disclosed deviation from the
concept sheet's "8/8-skill close" framing, which used low-`n` ("thin") as its target criterion
rather than SPEC §7's strict `n==0` bar for `new_coverage[]` — flagged for the project owner.
