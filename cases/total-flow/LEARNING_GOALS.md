# LEARNING GOALS — Total Flow

Bidirectional deliverable ↔ skill matrix. Run per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 Riemann sum of total storm volume | calculus-riemann-sum, calculus-how-to-approximate-area-under-a-curve-using-a-riemann-sum |
| D2 fitted Q(t), general antiderivative, definite integral by FTC | calculus-antiderivative, calculus-indefinite-integral, calculus-definite-integral, calculus-how-to-find-an-antiderivative-using-the-power-rule, calculus-how-to-evaluate-a-definite-integral-using-the-fundamental-theorem-of-calculus |
| D3 area between Q(t) and the channel-capacity line | calculus-area-between-two-curves, calculus-how-to-find-the-area-between-two-curves |
| D4 floodwater-safely-managed table and acre-ft-per-$1,000 recommendation | calculus-definite-integral, calculus-area-between-two-curves |

## LEARNING GOAL CHECK

```
deliverables: 4    claimed skills: 9    new_coverage: 9
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forces test applied to each mapping** ("could a competent student produce this deliverable
without ever performing this skill?"):

- **D1 — no.** The deliverable names the interval width, where in each day the value sits, the
  sum, and the over-/under-/exact question. A gage record is a finite table of rates, not a
  volume; the only way to get a volume out of it is to multiply rates by interval widths and add
  them, which *is* a Riemann sum. The over-/under-/exact sentence cannot be answered without
  knowing which rule was used, whether the curve is rising or falling on the interval, and what
  a daily *mean* already is — that is the Riemann-sum concept, not the arithmetic.
- **D2 — no.** The deliverable explicitly requires the *indefinite* integral written as a general
  antiderivative with the constant of integration shown, *and then* the definite integral over
  stated limits. Writing the antiderivative of a fitted polynomial discharge function is the power
  rule for antiderivatives; evaluating it at two limits and subtracting is the Fundamental Theorem
  of Calculus. Neither step can be skipped and still produce the artifact, and the D1-vs-D2
  comparison forces the Hero to hold both the approximation and the exact value at once.
- **D3 — no.** The excess volume is the region bounded above by Q(t) and below by the horizontal
  line Q = channel capacity. Finding the limits of integration means solving for where the two
  curves cross, and the computation is ∫(upper − lower). A Hero who integrates Q(t) alone gets
  the wrong number, and the deliverable's own shaded diagram makes that visible.
- **D4 — no.** The Crest Standard's managed volume is not ∫(Q − capacity) — it is that integral
  *minus* the part of the hydrograph that sits above the crest's own design discharge, which is a
  second area-between-two-curves computation against a different horizontal line. The Setback
  Standard's managed volume is the same integral capped at the basin's stated storage. Both
  require the definite integral as a quantity that can be compared, split, and capped, not merely
  computed once.

**Already-covered skills also exercised, not claimed in `new_coverage[]`:** compound-unit
conversion (cfs-days → acre-feet) and percent-of-a-number arithmetic are both exercised by D1 and
D4, and both already sit at `n > 0` in the spine from legacy cases. They are deliberately **not**
listed in `standards[]` — every id in `standards[]` must be forced by a deliverable *and* appear
verbatim in the final appendix, and padding the list with already-covered arithmetic would
overstate what this case closes.

**Group closure.** The nine claimed ids close the entire **Calculus / Integrals** group (7 of 7
skills, all at `n = 0` before this case) plus 2 of the 4 skills in **Calculus / Applications Of
Integrals**. The other two Applications-of-Integrals skills — `calculus-volume-of-revolution` and
`calculus-how-to-find-the-volume-of-a-solid-of-revolution-using-the-disk-method` — are **not**
claimed: nothing in this case revolves a region about an axis, and claiming them would mark a gap
closed that no Hero ever touched.
