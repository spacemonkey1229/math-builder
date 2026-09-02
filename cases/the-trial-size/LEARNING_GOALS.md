# Learning Goals — The Trial Size

Bidirectional deliverable ↔ spine-skill matrix. "Forces" test applied to every row: *could a
competent student produce this deliverable correctly without ever performing this skill?* If yes,
the mapping is cut.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — two-point cost table + derived linear cost equation | `statistics-and-probability-slope`, `statistics-and-probability-y-intercept`, `statistics-and-probability-how-to-identify-the-slope-of-a-line-given-a-set-of-data-or-a-graph-o`, `statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data` |
| D2 — Cost(n) line graphed from the equation | `statistics-and-probability-how-to-draw-a-line-of-a-set-of-data-given-its-linear-equation` |
| D3 — Budget-Remaining equation read off a graph, plus its x-intercept | `statistics-and-probability-x-intercept`, `statistics-and-probability-how-to-write-a-linear-equation-given-a-graph-of-a-line-of-a-set-of-d` |
| D4 — system-of-equations break-even solve | `statistics-and-probability-system-of-equations`, `statistics-and-probability-how-to-solve-a-system-of-linear-equations` |

## Why each mapping holds

- **D1** cannot be produced without reading the marginal cost off two real data points as a slope
  (rise in cost over run in participants), and without writing the two-point-to-equation
  algebra that recovers the y-intercept (the derived fixed cost F). Both the "identify slope"
  how-to and the "write a linear equation from a set of data" how-to are literally the steps a
  student performs to build the equation — there is no way to produce D1's required "shown step
  by step" derivation without doing both.
- **D2** cannot be produced without taking the equation from D1 and plotting it as a line — that
  is the definition of "draw a line given its linear equation." A table of costs alone does not
  satisfy D2; the deliverable explicitly requires the line be drawn *from the equation*.
- **D3** hands the student a graph (Appendix B) and requires they *read the equation off it* —
  the direct target of "write a linear equation given a graph of a line of a set of data" — and
  then requires the x-intercept specifically, with a written interpretation of what it means for
  the survey (the point at which the fixed budget is exhausted). A student who only rereads
  Appendix A's numbers, without using the graph, cannot satisfy this deliverable as written.
- **D4** explicitly requires "an algebraic system-of-equations solution … solved without
  graphing," which is the direct target of both `system-of-equations` (the term) and
  `how-to-solve-a-system-of-linear-equations` (the procedure). The "without graphing" clause
  rules out shortcutting to D2/D3's graphical work instead.

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 9    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

`new_coverage` is honestly `0` — every claimed skill already sits at `n >= 1` in
`readmodel/standards_spine.json` at authoring time (2026-09-01). See `case.json`'s
`reinforcement_note` for the full carve-out reasoning and the adjacent-skill check that was run
before accepting the zero.
