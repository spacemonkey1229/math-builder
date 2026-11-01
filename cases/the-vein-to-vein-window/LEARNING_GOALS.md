# Learning Goals — The Vein-to-Vein Window

Bidirectional deliverable ↔ skill matrix (SPEC §1.5 item 3 ↔ `case.json.standards[]`).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — one-sided limits of `V(t)` at the hard cutoff | `calculus-limit`, `calculus-one-sided-limit` |
| D2 — the formal continuity test at the hard cutoff | `calculus-continuity`, `calculus-discontinuity`, `calculus-how-to-determine-whether-a-function-is-continuous-at-a-point` |
| D3 — worked contrast: algebraic limit of `S(x)`, removable discontinuity | `calculus-how-to-evaluate-a-limit-algebraically`, `calculus-discontinuity`, `calculus-limit` |
| D4 — probability of viability comparison (primary metric) | `calculus-limit`, `calculus-discontinuity` |
| D5 — writing the cutoff argument into the pitch, using the case's vocabulary | `calculus-limit`, `calculus-one-sided-limit`, `calculus-continuity`, `calculus-discontinuity` |

## Forces test, applied to each claimed skill

*"Could a competent student produce this deliverable correctly without ever performing this
skill?"* — for all six, no:

- **`calculus-limit`** — D1, D3, D4, D5 all require reasoning about a limiting value directly; D1's
  entire task is evaluating one. Not decorative: the piecewise `V(t)` in Appendix B has no other
  way to be evaluated exactly at the cutoff.
- **`calculus-one-sided-limit`** — D1 explicitly requires both the left- and right-approaching
  limits of `V(t)`, and D5 requires using the term correctly in the write-up describing why the two
  sides disagree. A student who only computes a single two-sided limit (which does not exist here)
  cannot complete D1.
- **`calculus-continuity`** — D2's three-part test is the formal continuity definition applied by
  name; D5 requires using the term to explain the trap. No deliverable can be completed by treating
  the case as "just probability" without invoking continuity explicitly.
- **`calculus-discontinuity`** — D2 requires naming and classifying the discontinuity type (jump);
  D3 requires classifying a second, contrasting discontinuity (removable); D5 requires using the
  term in the pitch. The whole rubric trap (SEE FACILITATOR.md) is a discontinuity-literacy trap.
- **`calculus-how-to-evaluate-a-limit-algebraically`** — D3's entire task is factoring `(x²+5x)/x`
  and canceling to remove a 0/0 indeterminate form; D1 also requires algebraic evaluation from the
  piecewise definition (not a numeric table lookup).
- **`calculus-how-to-determine-whether-a-function-is-continuous-at-a-point`** — D2 is this
  procedure, applied by name, with all three of its parts shown.

## Error classes

- **UNMAPPED DELIVERABLES: none.** Every deliverable (D1–D5) has a non-empty skills column.
- **UNREACHABLE SKILLS: none.** Every claimed skill in `case.json.standards[]` is forced by at
  least one deliverable (see the forces test above; cross-check against the D1–D5 skills columns).

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 6    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

`new_coverage[]` is empty by design — every claimed skill already has `n=2` in the spine (thin, not
zero). See `case.json.reinforcement_note` for the live spine check and the disclosed-reinforcement
rationale (SPEC §8's zero-coverage rule does not apply; this is a full-group thickening of an
already-touched but thin group, per the case-readiness T1-10 reinforcement carve-out).
