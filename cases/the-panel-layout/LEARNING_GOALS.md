# LEARNING GOALS — Panel Layout

Bidirectional deliverable ↔ skill matrix. Run per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 whole-panel Fitts's Law model + derivative + critical points | calculus-critical-point, calculus-how-to-find-critical-points-of-a-function |
| D2 first-derivative-test sign chart | calculus-how-to-use-the-first-derivative-test-to-classify-a-critical-point |
| D3 closed-domain optimization table (endpoints + critical points) | calculus-how-to-solve-an-optimization-problem-using-derivatives |
| D4 miss-rate-weighted final decision table | calculus-how-to-solve-an-optimization-problem-using-derivatives |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 4    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Note on `new_coverage: 0`.** This is expected and correct for this case, not a defect. Per
`cases/_concepts/CONCEPTS_pim-sector-gaps_2026-08-24.md`'s C12 entry, this is a **second-pass /
redundancy** case for Calculus/Applications Of Derivatives: verified directly against
`readmodel/standards_spine.json` at authoring time, all four claimed ids
(`calculus-critical-point`, `calculus-how-to-find-critical-points-of-a-function`,
`calculus-how-to-use-the-first-derivative-test-to-classify-a-critical-point`,
`calculus-how-to-solve-an-optimization-problem-using-derivatives`) already sit at `n=2`. The group
already has n>=2 coverage; this case adds a further covering case so the group's weekly rotation
has more than a single point of failure. `new_coverage[]` is therefore correctly left empty in
`case.json` — this is a batch header instruction, not a validation failure.

**Forces test applied to each mapping** — *could a competent student produce this deliverable
correctly without ever performing this skill?*

- **D1 — no.** Building T(x) = MT_crit(x) + N·MT_other(x) from Appendix A's endpoint
  specifications and Appendix B's Fitts's Law formula, then differentiating a sum of logarithmic
  terms and solving T'(x) = 0 algebraically, is precisely what "how to find critical points of a
  function" requires. There is no shortcut to "the critical point(s) of T" other than performing
  that differentiation and solving the resulting equation — a student cannot fill in D1 by
  inspection or by comparing Options A and B alone, because the deliverable explicitly asks for
  every critical point in the continuous interior of the domain, not just the two named endpoints.
- **D2 — no.** Classifying a critical point as a local minimum, maximum, or neither by testing the
  sign of T'(x) on each side of it *is* the first-derivative test; a student who instead guesses
  from the shape of a sketch, or asserts a classification without evaluating T' at a test point on
  each side, has not produced the deliverable as specified.
- **D3 — no.** T(x) is defined on a closed interval [0, 1], and its global minimum can in
  principle sit at an interior critical point *or* at either endpoint — the deliverable
  specifically requires comparing all of them, which is the complete "solve an optimization
  problem using derivatives" procedure (not just "find a critical point and stop"). A student who
  only reports the interior critical point without checking it against Long Reach (x=0) and Close
  Reach (x=1) has solved a different, incomplete problem.
- **D4 — no.** Turning D3's result into an actual engineering recommendation requires evaluating
  the optimization's output against real constraints (only two of the three candidate x-values
  have tested miss-rate data) and stating explicitly what is assumed versus known before computing
  the final metric — this is the applied half of "solve an optimization problem using
  derivatives": using the located optimum to make a defensible decision, not just computing it in
  the abstract.

## Skills touched but not claimed

None. The concept sheet notes no additional already-covered skills this case "also exercises"
beyond the four claimed ids.

## Gap group touched

`Calculus/Applications Of Derivatives` — all four claimed skills already at `n=2` in
`readmodel/standards_spine.json` at authoring time (verified directly against the spine in the
case-write session). This case is a further covering case for the group, not a gap-closing one;
`new_coverage[]` is correctly empty per the batch header in
`CONCEPTS_pim-sector-gaps_2026-08-24.md`.
