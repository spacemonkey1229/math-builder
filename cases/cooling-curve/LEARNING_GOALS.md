# The Cooling Curve — Learning Goal Matrix

Bidirectional check between Challenge 3 deliverables and claimed spine skills (`case-write`
SKILL.md §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — volume-per-fin table | `geometry-how-to-find-the-volume-of-a-pyramid`, `geometry-how-to-find-the-volume-of-a-cone` (computing the volume of the Pyramid Array fin requires the pyramid volume formula; computing the volume of the Cone Standoff fin requires the cone volume formula) |
| D2 — surface-area-per-fin table | `geometry-surface-area` (computing each fin's total exposed surface area — four triangular faces plus base for the pyramid, lateral plus base for the cone) |
| D3 — manufacturing-cost-per-fin table | `geometry-how-to-find-the-volume-of-a-pyramid`, `geometry-how-to-find-the-volume-of-a-cone` (cost per fin is D1's volume converted to a material cost; a student cannot produce D3 without D1's pyramid/cone volume figures) |
| D4 — watts-per-dollar comparison table | `geometry-surface-area` (watts dissipated per fin is D2's surface area applied against the Appendix A dissipation rate; a student cannot produce D4 without D2's surface-area figures) |
| D5 — recommendation | draws on D1–D4; forces no additional skill by itself |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 3    new_coverage: 2
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forces test applied:** a competent student cannot produce D1 without applying both the pyramid
and cone volume formulas (two distinct fin geometries, one table); cannot produce D2 without
computing surface area for both fins; D3 and D4 each require, respectively, D1's volume output and
D2's surface-area output as their direct input, so they force the same skills transitively rather
than claiming new ones. D5 is a synthesis deliverable that draws on all four prior tables without
introducing a fifth skill — consistent with the precedent set in `cases/fret-board/LEARNING_GOALS.md`
for a case's final recommendation deliverable.

## Coverage note

`geometry-how-to-find-the-volume-of-a-pyramid` and `geometry-how-to-find-the-volume-of-a-cone` both
had `n == 0` in `readmodel/standards_spine.json` as of 2026-08-24 (checked at the start of this
write pass) — this case's reason to exist is closing both. `geometry-surface-area` already had
`n == 3`; it is claimed because it is genuinely load-bearing (the case's primary metric turns on
surface area as the heat-dissipation basis, per Appendix A), not because it needed opening.
