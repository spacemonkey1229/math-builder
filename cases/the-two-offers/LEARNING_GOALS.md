# Learning Goals — The Two Offers

Bidirectional deliverable ↔ skill matrix. Run at `case-write` time per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — cumulative net value equation for each offer, slope + y-intercept identified | `statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data`, `statistics-and-probability-how-to-identify-the-slope-of-a-line-given-a-set-of-data-or-a-graph-o`, `statistics-and-probability-slope`, `statistics-and-probability-y-intercept` |
| D2 — graph of both offers' equations on shared axes, crossover marked | `statistics-and-probability-how-to-draw-a-line-of-a-set-of-data-given-its-linear-equation` |
| D3 — exact crossover point via system of linear equations, full algebraic work | `statistics-and-probability-system-of-equations`, `statistics-and-probability-how-to-solve-a-system-of-linear-equations` |
| D4 — recommendation for two tenure lengths, justified from the D1 equations | `statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data`, `statistics-and-probability-how-to-solve-a-system-of-linear-equations` |

**Forcing test applied to each row:** could a competent student produce this deliverable correctly
without ever performing the listed skill(s)? For D1, no — a student who cannot identify slope and
y-intercept from the offer data, or cannot express those as a linear equation, cannot produce a
correct V(t). For D2, no — plotting a line from its equation is exactly the drawing skill listed.
For D3, no — the crossover point is defined here as the solution to the system; eyeballing a chart
does not satisfy the deliverable ("full algebraic work" is required in Challenge 3's text). For D4,
no — a correct answer at two tenure lengths requires evaluating/reasoning from the D1 equations and
the D3 solution, not restating day-one numbers (this is also the case's named trap — see
`FACILITATOR.md`).

## Claimed skills → deliverables (reverse direction)

| Claimed skill (spine id) | n (before this case) | Forced by |
|---|---|---|
| `statistics-and-probability-system-of-equations` | 2 | D3 |
| `statistics-and-probability-how-to-solve-a-system-of-linear-equations` | 2 | D3, D4 |
| `statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data` | 7 | D1, D4 |
| `statistics-and-probability-how-to-identify-the-slope-of-a-line-given-a-set-of-data-or-a-graph-o` | 3 | D1 |
| `statistics-and-probability-slope` | 6 | D1 |
| `statistics-and-probability-y-intercept` | 3 | D1 |
| `statistics-and-probability-how-to-draw-a-line-of-a-set-of-data-given-its-linear-equation` | 2 | D2 |

## LEARNING GOAL CHECK

```
deliverables: 4    claimed skills: 7    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Note on `new_coverage: 0`:** every claimed skill above already has `n >= 2` in
`readmodel/standards_spine.json` as of 2026-09-03 (confirmed live, not from the concept sheet's
cached counts, which matched). This case is not being written to close a skill-count gap — it is
being written to close a **topic** gap (life-skills cluster #4, Employment & income, had zero
published cases per the audit behind `cases/_concepts/CONCEPTS_life-skills-first10_2026-09-03.md`).
SPEC §7's "a case that closes nothing has no reason to exist" is read here as applying to topic
coverage as well as skill coverage, consistent with existing precedent
(`cases/the-bracket-cliff/case.json` also ships `new_coverage: []`). This is flagged explicitly so
`case-qa` / a human reviewer can confirm the empty array is an intentional topic-gap case, not an
oversight.
