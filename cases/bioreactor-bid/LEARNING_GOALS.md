# LEARNING_GOALS — The Bioreactor Bid

Bidirectional deliverable ↔ spine-skill matrix (SPEC §1.5 item 3 deliverables vs. `case.json.standards[]`).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 net-cumulative-yield (area between feed-rate and uptake-rate curves) | calculus-area-between-two-curves, calculus-how-to-find-the-area-between-two-curves |
| D2 working-volume calculation (cylinder for Column Bid; disk-method solid-of-revolution integral for Wave Bid) | calculus-volume-of-revolution, calculus-how-to-find-the-volume-of-a-solid-of-revolution-using-the-disk-method |
| D3 total-yield table (D1's per-liter yield × D2's working volume, for each vessel) | calculus-area-between-two-curves, calculus-how-to-find-the-area-between-two-curves, calculus-volume-of-revolution, calculus-how-to-find-the-volume-of-a-solid-of-revolution-using-the-disk-method |
| D4 yield-per-dollar comparison (D3's totals over vessel cost, for each vessel) | calculus-area-between-two-curves, calculus-how-to-find-the-area-between-two-curves, calculus-volume-of-revolution, calculus-how-to-find-the-volume-of-a-solid-of-revolution-using-the-disk-method |
| D5 original visual of the feed-rate/uptake-rate curves with the D1 area shaded | calculus-area-between-two-curves, calculus-how-to-find-the-area-between-two-curves |

**Why D3 and D4 also force the volume-of-revolution skills, not just the area skill:** neither
deliverable can be produced correctly without a correct D2 working-volume figure for the Wave
Bid — a student who skips the disk-method integral and simply uses the bag's nominal capacity
will get a total-yield and a yield-per-dollar number for Option B that is wrong, not just
imprecise. The dependency is load-bearing, not decorative.

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 4    new_coverage: 2
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

- **UNMAPPED DELIVERABLES:** none — D1–D5 each map to at least one claimed skill.
- **UNREACHABLE SKILLS:** none — all four claimed skills (`calculus-volume-of-revolution`,
  `calculus-how-to-find-the-volume-of-a-solid-of-revolution-using-the-disk-method`,
  `calculus-area-between-two-curves`, `calculus-how-to-find-the-area-between-two-curves`) are
  each forced by at least one deliverable (D1/D3/D4/D5 for the area pair; D2/D3/D4 for the
  volume-of-revolution pair).
