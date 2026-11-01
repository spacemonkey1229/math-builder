# Learning Goal Check — Grade Rule

Bidirectional deliverable ↔ skill matrix (SPEC §1.5 item 3 / case-write §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — point-specific scale-factor table | geometry-scale-factor, geometry-how-to-find-the-scale-factor-of-a-dilation |
| D2 — dilation scale-factor derivation | geometry-scale-factor, geometry-how-to-find-the-scale-factor-of-a-dilation |
| D3 — dilated-pattern prediction table | geometry-dilation, geometry-how-to-dilate-a-figure-on-the-coordinate-plane-given-a-scale-factor, geometry-similar, geometry-congruent |
| D4 — fit-check table | geometry-similar, geometry-congruent |
| D5 — cost/coverage/decision memo | measurement-how-to-convert-an-amount-from-one-unit-to-another-unit |

## Forces test

*"Could a competent student produce this deliverable correctly without ever performing this skill?"*

- **D1** cannot be produced without dividing each size's real measurement by the previous size's real measurement, separately at bust/waist/hip — that division *is* finding a scale factor, and doing it three separate times per step (rather than once for the whole pattern) is exactly what makes Point-Specific Grading point-specific.
- **D2** cannot be produced without deriving one shared scale factor from the base-size and range data — the same operation as D1, but performed once and applied everywhere, which is exactly what makes Uniform Dilation uniform.
- **D3** cannot be produced without applying D2's scale factor to every point of the base pattern (the definition of a dilation) and then explicitly judging whether the resulting scaled figure is truly a *similar*, and *congruent*-by-tolerance, copy of the real body at that size — a student who skips that judgment has not completed the deliverable, since the whole point of D3 is testing whether a mathematical dilation of the pattern matches a real, non-uniformly-scaling body.
- **D4** cannot be produced without comparing predicted (similar-by-construction) measurements against real ones and deciding congruence-within-tolerance at every landmark and size — nothing else in the case performs this comparison.
- **D5** cannot be produced without converting the final grade-rule table from inches to centimeters for the overseas factory — a direct unit conversion, and the decision memo's own arithmetic (dollars per fitting size) depends on D1–D4's results, not a new skill of its own.

## Report

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 7    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**new_coverage[] is empty by design, not by omission** — see `case.json`'s `reinforcement_note`. A live check of `readmodel/standards_spine.json` on 2026-09-18 found all 7 claimed skills already at `n>=3` (none at `n==0`); the concept sheet (`cases/_concepts/CONCEPTS_textiles-pattern_2026-09-12.md`) documents a spine-wide sweep the same week finding zero true `n==0` skills anywhere in the 437-skill spine. These are exactly the 6 dilation/scale-factor/similar/congruent skills the concept sheet's C2 entry names as the domain's headline archetype, plus the general unit-conversion how-to Challenge D5 genuinely forces.
