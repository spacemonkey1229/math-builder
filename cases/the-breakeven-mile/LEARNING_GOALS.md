# Learning Goals — The Breakeven Mile

Bidirectional deliverable ↔ skill matrix. Rebuilt at `case-write` time on 2026-09-03 after this
case was returned from `case-research` for redesign around the linear breakeven-mileage model
(see `case.json.redesign_2026_09_03` and `RESEARCH_LOG.md`). Run per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — two cost equations (`C_A(m)`, `C_B(m)`) presented as a system of two linear equations | `statistics-and-probability-system-of-equations` |
| D2 — algebraic solve of the system for breakeven mileage `m*` | `statistics-and-probability-how-to-solve-a-system-of-linear-equations` |
| D3 — comparison table evaluating both equations at `m*`, the US average, and Renata's own mileage, plus a budget check | `statistics-and-probability-system-of-equations`, `statistics-and-probability-how-to-solve-a-system-of-linear-equations` |
| D4 — graph of both lines with `m*` and the D3 points labeled | `statistics-and-probability-system-of-equations` |

**Forcing test applied to each row:** could a competent student produce this deliverable correctly
without ever performing the listed skill(s)?

- **D1** — no. Writing two total-cost expressions as a fixed amount plus a rate times `m`, and
  presenting them together as a system in the same two unknowns (`m` and `C`), is the definition of
  setting up a system of linear equations. A student who cannot recognize the two expressions as a
  system cannot produce D1 as specified (side by side, in the same variables, ready to be solved
  together — not just two isolated formulas).
- **D2** — no. Finding the mileage where `C_A(m) = C_B(m)` by substitution or elimination, showing
  every algebraic step, is precisely what "how to solve a system of linear equations" means. A
  student who guesses the crossing point from a graph instead of solving algebraically has not
  produced D2 as specified — the deliverable explicitly requires showing the method.
- **D3** — no, for the same reason as D1/D2: evaluating the two linear equations at specific
  mileages and stating which is cheaper requires having correctly built and understood the system
  from D1, and the "how much cheaper" comparison at each point is a direct application of what
  solving the system in D2 established (which side of `m*` each evaluation point falls on).
  Reinforcement of both skills, not a new first-force.
- **D4** — reinforcement, not a first-force on its own: a student could technically plot two given
  lines without having solved anything. Included because correctly identifying and labeling the
  actual crossing point `m*` as the graphical solution to the system (not just "where the lines
  look close") is the graphical representation of the system-of-equations skill, and this is also
  Challenge 2(b)'s required "original visual display of the data."

## Claimed skills → deliverables (reverse direction)

| Claimed skill (spine id) | n (before this case, confirmed live against `readmodel/standards_spine.json` on 2026-09-03) | Forced by |
|---|---|---|
| `statistics-and-probability-system-of-equations` | 2 | D1, D3, D4 |
| `statistics-and-probability-how-to-solve-a-system-of-linear-equations` | 2 | D2, D3 |

## LEARNING GOAL CHECK

```
deliverables: 4    claimed skills: 2    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Note on `new_coverage`:** both claimed skills carry `n=2` — thin, but not zero-coverage — as of
this live check. Per `case.json.reinforcement_note`, this case does not close a skill-count gap;
it closes the **topic** gap the concept sheet identified (Life-skills taxonomy cluster #3, Major
purchase decisions — car ownership vs. rideshare had zero published coverage). This is the same
honest framing used in `cases/the-two-offers/case.json` and `cases/the-lease-break/case.json`,
both of which also disclose `new_coverage: []` rather than force a false zero-coverage claim. The
calculus-track version of this concept (`calculus-how-to-use-the-quotient-rule-to-differentiate-a-quotient-of-functions`,
`n=0`) was tried first per the concept sheet's own recommendation, but `case-research` found its
load-bearing premise (a genuinely accelerating, mileage-driven depreciation curve) does not hold
against real sourced data — see `RESEARCH_LOG.md` §0 and `case.json.redesign_2026_09_03` — so this
case was rebuilt around the concept sheet's own documented linear fallback instead.
