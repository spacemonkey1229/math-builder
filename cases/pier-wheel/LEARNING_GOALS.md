# LEARNING GOALS — Pier Wheel

## Bidirectional deliverable <-> skill matrix

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 height-vs-time function h(t) for each option | pre-calculus-amplitude, pre-calculus-period-of-a-function, pre-calculus-cosine-function, pre-calculus-how-to-find-the-amplitude-and-period-of-a-sine-or-cosine-function |
| D2 degrees-to-radians conversion table | pre-calculus-radian, pre-calculus-how-to-convert-between-degrees-and-radians |
| D3 graph of each height function with qualifying line marked | pre-calculus-amplitude, pre-calculus-period-of-a-function, pre-calculus-cosine-function |
| D4 inverse-trig worked solution for the dwell interval | pre-calculus-inverse-trigonometric-function, pre-calculus-how-to-evaluate-an-inverse-trigonometric-function, pre-calculus-how-to-solve-a-trigonometric-equation-over-a-given-interval |
| D5 final scoring table (qualifying min/hr; per-meter-of-diameter score) | pre-calculus-how-to-solve-a-trigonometric-equation-over-a-given-interval, pre-calculus-period-of-a-function |

## The "forces" test, applied

*Could a competent student produce this deliverable correctly without ever performing this
skill?*

- **D1** cannot be written without knowing amplitude = radius, midline = radius + boarding
  clearance, and period = rotation time -- and cannot be written in the required cosine form
  without applying `how-to-find-the-amplitude-and-period-of-a-sine-or-cosine-function`. No.
- **D2** is a pure application of `how-to-convert-between-degrees-and-radians`; the radian
  vocabulary term is required to label the output correctly. No.
- **D3** requires correctly plotting a function whose shape and scale are entirely determined by
  amplitude, period, and the choice of cosine (vs. sine, which would shift the starting phase).
  No.
- **D4** cannot be solved without inverting the cosine relationship -- the entire point of the
  deliverable is applying `how-to-evaluate-an-inverse-trigonometric-function` and then
  `how-to-solve-a-trigonometric-equation-over-a-given-interval` to get both solutions in
  [0, period), not just the principal value. No.
- **D5** requires re-applying the period (rotations per hour = 60/period) and using D4's solved
  interval length; a student who fudges the interval length cannot produce a defensible scoring
  table. No.

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 9    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS (new_coverage carve-out applies -- see case.json.reinforcement_note)
```

**new_coverage[] is empty, and that is disclosed, not padded.** As of 2026-09-09 the entire
437-skill standards spine has zero skills at true n==0 (confirmed directly against
`readmodel/standards_spine.json`, consistent with ROADMAP.md's 2026-09-06 "uncovered reaches 0"
entry). Every skill in `standards[]` above sits at n=2 or n=3 in the Trigonometric Functions and
Trigonometric Identities groups -- genuinely thin, but not zero. Per the 2026-08-17
reinforcement-carve-out doctrine amendment (T1-10; see `cases/the-sunset-ramp/case.json` and
`cases/acton-survey/LEARNING_GOALS.md` for precedent), an honestly-empty `new_coverage[]` with a
`reinforcement_note` downgrades from a case-write BLOCKER to a disclosed, non-blocking GAP at
case-readiness Tier 1, not a defect in this case's own math. Every skill above is checked against
the "forces" test individually; none is claimed because it "sounds related."
