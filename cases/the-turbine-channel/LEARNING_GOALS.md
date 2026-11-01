# Learning Goals — Turbine Channel

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 scatter plot of raw current-speed readings, each channel | statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data |
| D2 fitted-curve worksheet: polynomial fit + its antiderivative via the power rule, each channel | calculus-antiderivative, calculus-indefinite-integral, calculus-how-to-find-an-antiderivative-using-the-power-rule |
| D3 definite-integral volume table via the Fundamental Theorem of Calculus, each channel | calculus-definite-integral, calculus-how-to-evaluate-a-definite-integral-using-the-fundamental-theorem-of-calculus |
| D4 Riemann-sum cross-check from raw readings, each channel | calculus-riemann-sum, calculus-how-to-approximate-area-under-a-curve-using-a-riemann-sum |
| D5 generation-potential ratio table (kWh/m³), unit conversions shown | measurement-how-to-convert-an-amount-with-compound-units |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** cannot be produced without genuinely plotting the paired (time, speed) data for each channel as points on a coordinate grid — a student who only tabulates the numbers, or sketches a smooth curve directly from memory of "what tides look like," has not produced a scatter plot of the actual readings. Genuinely forces `how-to-create-a-scatter-plot-given-a-set-of-data`.
- **D2** is impossible without first stating a polynomial function that models the scatter data (this is where `Antiderivative` and `Indefinite Integral` as vocabulary become operative — the student must know what an antiderivative *is* before they can be asked to find one) and then finding that polynomial's antiderivative term-by-term using the power rule (`how-to-find-an-antiderivative-using-the-power-rule`). A student who never writes down v(t) as a function, or who tries to find "the antiderivative" by guessing a plausible-looking expression rather than applying the power rule to each term, has not produced this deliverable. Genuinely forces `antiderivative`, `indefinite-integral`, and the power-rule how-to.
- **D3** cannot be produced without literally evaluating a definite integral — plugging the flow-window's bounds into the antiderivative from D2 and subtracting (`how-to-evaluate-a-definite-integral-using-the-fundamental-theorem-of-calculus`) — and reporting that evaluated quantity as a `Definite Integral`, not as "the area under the curve" described only in words. A student who eyeballs the area from the graph instead of doing the FTC evaluation has not met this deliverable's own stated requirement (an evaluated integral, converted via cross-sectional area into cubic meters). Genuinely forces `definite-integral` and the FTC how-to.
- **D4** requires building an actual Riemann sum — partitioning the flow window using the raw six-minute-interval readings and summing rectangle areas (`how-to-approximate-area-under-a-curve-using-a-riemann-sum`) — as a method independent of the fitted curve used in D2/D3. A student who just restates the D3 answer, or averages the raw readings without constructing rectangles and summing them, has not produced a Riemann sum. Genuinely forces `riemann-sum` and its how-to.
- **D5** cannot be produced without converting a volume in cubic meters, through a conversion factor with compound units (kWh per m³), into kilowatt-hours — and showing that conversion as a chain of unit cancellations, not a single unexplained multiplication. A student who writes only a final number with no unit chain has not shown the compound-unit conversion this deliverable requires. Genuinely forces `how-to-convert-an-amount-with-compound-units`.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 9    new_coverage: 0 (reinforcement — see case.json.reinforcement_note)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

Checked every claimed skill's `n` in `readmodel/standards_spine.json` before writing (2026-09-11):
`calculus-antiderivative` (n=2), `calculus-definite-integral` (n=2), `calculus-indefinite-integral`
(n=2), `calculus-riemann-sum` (n=2), `calculus-how-to-find-an-antiderivative-using-the-power-rule`
(n=2), `calculus-how-to-evaluate-a-definite-integral-using-the-fundamental-theorem-of-calculus`
(n=2), `calculus-how-to-approximate-area-under-a-curve-using-a-riemann-sum` (n=2),
`measurement-how-to-convert-an-amount-with-compound-units` (n=18),
`statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data` (n=9). A mechanical
sweep of the entire spine (2026-09-11) independently confirmed **zero** skills anywhere at `n==0`
— no freshly-authored case can produce a literal `new_coverage[]` right now (see
`cases/flow-state/case.json.reinforcement_note` and `cases/the-fee-route/case.json.reinforcement_note`
for the same finding on other recent cases). `new_coverage[]` is therefore honestly `[]`, per the
reinforcement carve-out (`skills/case-readiness/SKILL.md`, "The reinforcement carve-out on T1-10,"
added 2026-08-17), rather than padded with a skill no deliverable forces.

This case still does exactly the job the concept sheet scored it for: all seven Calculus/Integrals
skills are the entire remaining thin group in that group (`readmodel/gap_queue.json`'s "Calculus /
Integrals — n_gap 7, n_total 7" entry), every one currently at n=2, and every one is genuinely
forced by a deliverable above (D2–D4) rather than listed because it sounds related. Landing this
case takes all seven from n=2 to n=3 — the full, coherent reinforcement close the concept sheet
recommended writing first.
