# LEARNING GOALS — The Optimal Can

Bidirectional deliverable ↔ skill matrix. Run per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 surface-area function + derivative (power rule) | calculus-derivative, calculus-instantaneous-rate-of-change, calculus-how-to-find-a-derivative-using-the-power-rule |
| D2 critical point + first-derivative test / concavity, proving a minimum | calculus-critical-point, calculus-how-to-find-critical-points-of-a-function, calculus-local-minimum, calculus-local-maximum, calculus-how-to-use-the-first-derivative-test-to-classify-a-critical-point, calculus-concavity, calculus-how-to-solve-an-optimization-problem-using-derivatives |
| D3 material-cost comparison table (area, weight, cost, % reduction) | measurement-how-to-convert-an-amount-with-compound-units, advanced-numbers-how-to-find-the-percent-of-a-number |
| D4 annual savings, payback months, break-even volume | advanced-numbers-how-to-find-the-percent-of-a-number, measurement-how-to-convert-an-amount-with-compound-units |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 12    new_coverage: 10
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Forces test applied to each mapping** — *could a competent student produce this deliverable
correctly without ever performing this skill?*

- **D1 — no.** The deliverable explicitly demands S(r) written symbolically with the
  fixed-volume substitution shown, and its derivative found **using the power rule** — the only
  way to differentiate 2πr² + 2V/r term-by-term. `calculus-instantaneous-rate-of-change` is forced
  because the deliverable requires dS/dr to be *reported as* the rate of change of surface area
  with respect to radius, not merely produced as a symbolic byproduct — a student who writes the
  derivative but cannot say what it means has not completed the artifact as specified.
- **D2 — no.** Solving dS/dr = 0 *is* finding a critical point; there is no other way to locate r*.
  The deliverable then demands proof that r* is a **minimum and not a maximum**, which is exactly
  what the first derivative test (or a concavity/second-derivative check) does and nothing else
  does — a student who finds r* and stops has produced half the artifact. Proving "not a maximum"
  forces the student to know what a local maximum's sign pattern would look like, which is why
  `calculus-local-maximum` is forced here even though the case's answer is a minimum.
  `calculus-how-to-solve-an-optimization-problem-using-derivatives` is forced by the deliverable's
  full arc — setting up the constrained function, differentiating it, and classifying the critical
  point is precisely that procedure end to end, not one isolated step of it.
- **D3 — no.** Converting a surface area in square inches to a weight in pounds requires a
  thickness (in) and a density (lb/in³) chained through two different unit systems into one
  compound conversion; converting that weight to a dollar figure chains a third unit (USD/lb).
  Reporting the reduction "as a percent" is a percent-of-a-number computation on a quantity the
  student just derived, not a number they can read off a table.
- **D4 — no.** Trip savings scale from per-can dollars to an annual dollar figure by a
  cans-per-year compound rate, and the payback period converts a dollar ratio into a time unit
  (months) — both compound-unit conversions. The break-even annual volume is solved by asking what
  input to that same rate produces a stated percent of the retooling cost recovered per year, which
  is again a percent-of-a-number computation, this time run in reverse to find an unknown.

## Skills deliberately NOT claimed

- **`geometry-how-to-find-the-surface-area-of-a-cylinder` / `geometry-surface-area`** are touched —
  the case is, after all, a cylinder's surface area — but are **not claimed**. The deliverables
  never ask for the surface area of a *fixed*-dimension cylinder as a standalone geometry exercise;
  they ask for the surface area *as a function of one variable, differentiated*, which is squarely
  a Calculus/Applications Of Derivatives deliverable, not a Geometry/Surface Area one. Claiming the
  geometry skills here on the strength of the same formula appearing inside a calculus problem
  would be exactly the "sounds related" failure mode SPEC's forces test exists to catch.
- **`calculus-how-to-find-the-second-derivative-of-a-function`-style skills** are not claimed:
  D2 asks for the first derivative test *or* a concavity check, and the case does not require the
  student to have used the second derivative specifically — `calculus-concavity` is claimed as the
  vocabulary term the concavity check exercises, not the second-derivative how-to procedure.

## Already-covered skills also exercised, not claimed in `new_coverage[]`

`measurement-how-to-convert-an-amount-with-compound-units` (n=6),
`advanced-numbers-how-to-find-the-percent-of-a-number` (n=24).

## Gap group closed

`Calculus/Applications Of Derivatives` — **7 of 7 skills, the entire group**, all at `n = 0` in
`readmodel/standards_spine.json` at authoring time. Also closes `calculus-derivative`,
`calculus-instantaneous-rate-of-change` and
`calculus-how-to-find-a-derivative-using-the-power-rule` from `Calculus/Derivatives`, all likewise
at `n = 0`. No partial claim, no split with a second case.
