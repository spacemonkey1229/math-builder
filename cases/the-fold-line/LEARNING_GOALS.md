# Learning Goal Check — The Fold Line

Bidirectional deliverable ↔ skill matrix (SPEC §1.5 item 3 / case-write §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — coordinate-grid reflection diagram | geometry-how-to-reflect-a-figure-across-the-y-axis, geometry-line-of-symmetry, geometry-symmetry, geometry-reflection, measurement-distance |
| D2 — congruence check | geometry-congruent |
| D3 — cutting-dimensions & yardage worksheet | fractions-how-to-add-with-mixed-numbers, fractions-how-to-multiply-a-fraction-and-a-mixed-number, measurement-how-to-convert-an-amount-from-one-unit-to-another-unit, measurement-distance |
| D4 — cost-per-panel table and daily-run projection | measurement-how-to-convert-an-amount-from-one-unit-to-another-unit |

## Forces test

*"Could a competent student produce this deliverable correctly without ever performing this skill?"*

- **D1** cannot be produced without literally reflecting the half-pattern across the fold line (the y-axis) to construct the mirrored half — that reflection *is* the diagram. The line of symmetry must be identified and labeled to show where the fold sits, and "symmetry"/"reflection" are the vocabulary that describes what the diagram shows. Every labeled dimension on the diagram is a distance measurement.
- **D2** cannot be produced without checking that corresponding sides/angles of the original half-pattern and its mirror image match — that is the definition of congruent, and nothing else in the case asks the student to verify it.
- **D3** cannot be produced without adding the finished width/length to their seam and hem allowances, all given as mixed numbers with unlike denominators (23 1/4 + 1 1/2 + 5/8) — that forces mixed-number addition. Converting the resulting cutting length from inches to yards is a multiplication by the fraction 1/36 against a mixed-number quantity — that forces multiplying a fraction and a mixed number. The inch-to-yard step is itself a unit conversion, and every quantity involved is a distance.
- **D4** cannot be produced without converting the marking/cutting minutes (Appendix C) into hours to multiply against an hourly wage — a unit conversion. The daily-run projection folded into D4 is a direct multiplicative extension of the same per-panel totals and claims no additional skill beyond the conversion already required.

## Report

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 9    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**new_coverage[] is empty by design, not by omission** — see `case.json`'s `reinforcement_note`. A live check of `readmodel/standards_spine.json` on 2026-09-17 found every one of this case's 9 claimed skills already at `n>=2` (none at `n==0`); the concept sheet (`cases/_concepts/CONCEPTS_textiles-pattern_2026-09-12.md`) documents that a spine-wide sweep the same week found zero true `n==0` skills anywhere in the 437-skill spine. Three of the nine claimed skills are still genuinely thin (`geometry-how-to-reflect-a-figure-across-the-y-axis`=4, `geometry-line-of-symmetry`=3, `geometry-symmetry`=3, `geometry-congruent`=4 at the time of this check) and this case is exactly the kind of reinforcement the concept sheet recommended writing first.
