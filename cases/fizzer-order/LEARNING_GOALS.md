# LEARNING GOALS — Fizzer Order

Bidirectional deliverable ↔ skill matrix. Run per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 dimensioned nets + surface-area table | geometry-how-to-find-the-surface-area-of-a-pyramid, geometry-surface-area, geometry-pyramid, geometry-cone |
| D2 interior-volume capacity table | geometry-how-to-find-the-volume-of-a-pyramid, geometry-how-to-find-the-volume-of-a-cone, geometry-volume |
| D3 usable-capacity (packing) table | geometry-how-to-find-the-volume-of-a-sphere, geometry-sphere, advanced-numbers-how-to-find-the-percent-of-a-number |
| D4 material-cost-per-fizzer comparison | advanced-numbers-how-to-find-the-percent-of-a-number |
| D5 shipping-carton footprint estimate | advanced-numbers-how-to-find-the-percent-of-a-number |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 10    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Forces test applied to each mapping** — *could a competent student produce this deliverable
correctly without ever performing this skill?*

- **D1 — no.** The deliverable explicitly demands a scaled net and a surface-area table for the
  Peak Box, a square pyramid. There is no way to fill that table's Option A cell without applying
  the pyramid surface-area formula (base area plus the area of the four triangular lateral faces,
  each requiring the slant height found from the pyramid's own height and half the base edge) —
  that computation *is* `geometry-how-to-find-the-surface-area-of-a-pyramid`. Correctly identifying
  which faces belong to a pyramid versus a cone (base, lateral faces vs. base, lateral surface) to
  build the net in the first place forces `geometry-pyramid` and `geometry-cone` as named,
  distinguishable 3-D shapes, and the deliverable's own title names `geometry-surface-area`
  directly as the quantity being tabulated.
- **D2 — no.** A capacity table cannot be completed for Option A without the pyramid volume
  formula (`geometry-how-to-find-the-volume-of-a-pyramid`) and cannot be completed for Option B
  without the cone volume formula (`geometry-how-to-find-the-volume-of-a-cone`) — two genuinely
  different formulas, both required by the same one-row table. `geometry-volume` is forced because
  the deliverable's entire output is stated, and understood, as a volume.
- **D3 — no.** Finding "the volume of a single Mini Fizzer sphere" has exactly one formula that
  applies — `geometry-how-to-find-the-volume-of-a-sphere` — and a student cannot apply the packing
  figure to get a usable-capacity number without first knowing what shape a Mini Fizzer even is
  (`geometry-sphere`). Applying Appendix C's 64% figure to D2's volume, and then reporting a whole
  usable count, is a percent-of-a-number computation applied to a quantity the student just
  derived, not a number they can read off a table.
- **D4 — no.** Dividing a material cost (from D1) by a usable-count (from D3) to get a
  dollars-per-unit rate, and then stating which option wins "and by how much," is a
  percent/ratio computation performed on two numbers the student had to derive themselves in D1
  and D3 — it cannot be looked up.
- **D5 — no.** Converting a linear box-per-side count into a percent of a 144 sq in floor covered
  requires computing each shape's own footprint area (a square for the Peak Box, a circle for the
  Twist Cone) and expressing covered-area over total-area as a percent — the same
  percent-of-a-number skill applied to a fresh, self-derived pair of quantities.
