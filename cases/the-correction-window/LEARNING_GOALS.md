# Learning Goals — The Correction Window

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 Taylor series derivation of both polynomials | calculus-taylor-series, calculus-how-to-find-the-taylor-series-of-a-function-at-a-point |
| D2 exact-error table + convergence check | calculus-taylor-series, calculus-sequence, calculus-series, calculus-how-to-determine-whether-a-series-converges-or-diverges |
| D3 per-correction compute-cost derivation | measurement-how-to-convert-an-amount-with-compound-units |
| D4 whole-mission compute-budget and error-rate table | advanced-numbers-how-to-find-the-percent-of-a-number, measurement-how-to-convert-an-amount-with-compound-units |
| D5 primary-metric comparison and visual | advanced-numbers-how-to-find-the-percent-of-a-number, calculus-taylor-series |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** is impossible without applying the general Taylor series formula (Appendix D) — a student
  who simply copies "θ − θ³/6" and "θ − θ³/6 + θ⁵/120" from Appendix C without deriving them from
  f(0), f′(0), f″(0), … has not produced this deliverable at all, since D1 explicitly requires the
  derivation "from scratch." Genuinely forces `calculus-taylor-series` (the object being built) and
  the how-to (the mechanical process of building a Taylor series at a specific point, θ = 0).
- **D2** cannot be produced by only subtracting two decimal numbers per cell — the second half of
  the deliverable (checking the error against the next un-kept term, and stating whether more terms
  would keep shrinking the error indefinitely) requires treating each Taylor polynomial as a
  partial sum of an infinite series and asking a genuine convergence question about it. Genuinely
  forces `calculus-sequence` (the ordered terms being added), `calculus-series` (the sum itself),
  the converges-or-diverges how-to (the "would it keep shrinking forever" question), and
  `calculus-taylor-series` (the remainder/next-term reasoning is specific to a Taylor expansion,
  not a generic series).
- **D3** requires expressing a rate (single-cycle operations per correction, and clock speed in
  cycles per second) as a compound-unit chain converted down to nanoseconds — a student who just
  writes "3 operations" or "5 operations" without the unit conversion into time has not completed
  the deliverable, which explicitly demands "every conversion step shown." Genuinely forces
  `measurement-how-to-convert-an-amount-with-compound-units`.
- **D4** requires two distinct compound-unit conversions chained together (loop rate → total cycles
  over the transit; per-correction time → total mission time) and a percent-style weighted
  computation (what fraction of gust-weighted cycles exceed tolerance). A student who skips the
  cycle-count conversion cannot get a total compute-budget figure at all. Genuinely forces
  `advanced-numbers-how-to-find-the-percent-of-a-number` and
  `measurement-how-to-convert-an-amount-with-compound-units`.
- **D5** requires pulling forward D4's two computed figures per build and combining them into the
  single named ratio metric, then displaying the comparison — a student who instead just displays
  raw error rates (skipping the division by compute cost) has fallen into the case's own named trap,
  not completed the deliverable, since the metric is specifically defined as a ratio.
  `advanced-numbers-how-to-find-the-percent-of-a-number` is forced by the ratio arithmetic;
  `calculus-taylor-series` is forced because the error-rate half of the ratio is itself defined by
  each build's Taylor-polynomial accuracy from D1/D2.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 7    new_coverage: 2
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

`calculus-taylor-series` and `calculus-how-to-find-the-taylor-series-of-a-function-at-a-point` were
both confirmed `n == 0` in `readmodel/standards_spine.json` before writing (2026-09-05) — true
zero-coverage skills, the highest-priority close named at concept approval. `calculus-sequence`
(n=2), `calculus-series` (n=1), `calculus-how-to-determine-whether-a-series-converges-or-diverges`
(n=1), `measurement-how-to-convert-an-amount-with-compound-units` (n=16), and
`advanced-numbers-how-to-find-the-percent-of-a-number` (n=71) are reinforcement, not padding — each
is genuinely forced by a specific deliverable (see the LEARNING GOAL CHECK above), consistent with
the concept sheet's note that this case should "reinforce calculus-sequence/series/convergence
skills if the case can naturally motivate a remainder-term convergence check" — D2's convergence
check is exactly that motivation, not a bolted-on skill claim.
