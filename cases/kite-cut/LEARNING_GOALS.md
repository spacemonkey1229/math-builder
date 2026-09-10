# Learning Goals — Kite Cut

Bidirectional deliverable ↔ skill matrix. `case-write` + `case-research` combined pass, 2026-09-09.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — dimensioned diagram of each frame; classify A as Rhombus, B as Kite via side-length arithmetic and diagonal-bisection check | `geometry-rhombus`, `geometry-kite`, `geometry-quadrilateral`, `geometry-fundamentals-of-geometry-congruent`, `geometry-perpendicular-lines` |
| D2 — sail area of each option via the diagonals formula; compare | `geometry-area` |
| D3 — nest two Option A panels into a Parallelogram; verify opposite sides parallel/congruent; confirm zero-waste area | `geometry-parallelogram`, `geometry-parallel-lines`, `geometry-fundamentals-of-geometry-congruent`, `geometry-area` |
| D4 — fabric area consumed per kite (sail + tail); convert to roll yardage | `geometry-area`, `advanced-numbers-how-to-divide-decimal-numbers` |
| D5 — full material cost table per kite and for the run; state the winner and margin | `advanced-numbers-how-to-multiply-decimal-numbers`, `advanced-numbers-how-to-divide-decimal-numbers`, `advanced-numbers-how-to-find-the-percent-of-a-number` |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 11    new_coverage: 3
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each new-coverage skill** (*could a competent Hero produce the
deliverable correctly without ever performing this skill?*):

- `geometry-rhombus` — D1 requires computing all four of Option A's side lengths (via the
  Pythagorean relationship from the half-diagonals) and showing they are all equal — a Hero who
  cannot identify or verify a rhombus cannot complete this half of D1 correctly, only guess at it.
- `geometry-kite` — D1 requires the same for Option B, but showing two *unequal* pairs of adjacent
  equal sides instead of four equal sides — the deliverable is specifically designed so a Hero who
  conflates "kite" with "rhombus" produces a wrong classification, catchable only by actually
  computing both side-length pairs.
- `geometry-parallelogram` — D3 requires constructing the two-panel nested cutting pattern,
  labeling it as a parallelogram, and *verifying* (not asserting) that its opposite sides are
  parallel and congruent before using its area to prove zero fabric waste. A Hero who cannot
  recognize what makes a quadrilateral a parallelogram cannot complete the verification step D3
  explicitly requires.

**Forcing test applied to reinforcement skills** (already `n > 0` in the spine, still genuinely
required):

- `geometry-quadrilateral` — both D1 classifications start from "this four-sided shape is a
  quadrilateral with these properties"; the rhombus/kite classifications are sub-cases of it.
- `geometry-fundamentals-of-geometry-congruent` — D1 and D3 both require showing specific sides are
  congruent (equal length) as the actual proof step, not just labeling shapes by eye.
- `geometry-perpendicular-lines` — D1 requires confirming the spine and spreader (the sail's two
  diagonals) meet at a right angle in both options, which the kite/rhombus classifications and the
  diagonals area formula both depend on.
- `geometry-parallel-lines` — D3 requires verifying the nested parallelogram's opposite sides are
  parallel, using the actual construction (not simply stated).
- `geometry-area` — D2, D3, and D4 all require computing an area (diagonals formula, parallelogram
  area, and total fabric area) as the literal arithmetic content of the deliverable.
- `advanced-numbers-how-to-multiply-decimal-numbers`, `advanced-numbers-how-to-divide-decimal-numbers`,
  `advanced-numbers-how-to-find-the-percent-of-a-number` — D4's yardage conversion and D5's full
  cost table and margin statement are decimal multiplication/division and percent-comparison
  arithmetic throughout.

No skill here is claimed on the strength of "the case is about kites generally" — each one traces
to a specific requirement in a specific deliverable.
