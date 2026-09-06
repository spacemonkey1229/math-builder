# Learning Goals — The Custom Die

Bidirectional deliverable ↔ skill matrix. `case-write`, 2026-09-05.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — shape audit of six whiteboard candidates, name each, keep/reject reasoning | `geometry-face`, `geometry-edge`, `geometry-how-to-name-a-3-d-shape`, `geometry-cylinder`, `geometry-cone`, `geometry-pyramid`, `geometry-sphere`, `geometry-prism` |
| D2 — dimensioned net of each option, faces labeled, Length/Width/Depth marked | `geometry-net`, `geometry-how-to-draw-the-net-of-a-3-d-shape`, `geometry-face`, `geometry-edge`, `number-sense-depth` |
| D3 — net-area material table, from the net, not the volume | `geometry-surface-area`, `geometry-how-to-find-the-surface-area-of-a-prism` |
| D4 — wasted-space table: product volume vs. each box's interior volume | `geometry-volume`, `geometry-how-to-find-the-volume-of-a-prism` |
| D5 — tooling-amortized cost comparison, state winner and margin | `advanced-numbers-how-to-find-the-percent-of-a-number` (already covered) |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 16    new_coverage: 1
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each new-coverage skill** (*could a competent Hero produce the
deliverable correctly without ever performing this skill?*):

- `number-sense-depth` — D2 requires marking each box's Depth directly on the labeled net, and
  that Depth value (3.25 in for Option A, 3.25 in for Option B's cross-section leg 2) is the same
  number D3 and D4 multiply into the net-area and volume formulas. A Hero who cannot identify which
  of a box's three dimensions is its Depth (as distinct from Length and Width) mislabels the net
  and gets D3/D4's arithmetic wrong downstream — this is load-bearing, not decorative. `n=0` in the
  spine before this case; this is the case's entire reason to exist per SPEC section 8.

**Forcing test applied to the already-covered skills claimed** (why each is still genuinely
required, not padding):

- `geometry-face`, `geometry-edge` — D1's shape audit is written entirely in terms of face/edge/
  vertex counts (see Appendix A); a Hero cannot name a candidate shape correctly without reading
  and applying those counts. D2 requires labeling every face on both nets.
- `geometry-how-to-name-a-3-d-shape` — D1's whole point: six candidates described by properties,
  none named on the whiteboard. Naming them is the deliverable, not a byproduct of it.
- `geometry-cylinder`, `geometry-cone`, `geometry-pyramid`, `geometry-sphere` — each is one of the
  six D1 candidates; a Hero must correctly identify and then explain in one sentence why each one
  is or is not viable for a triangular cross-section, which requires actually knowing the shape,
  not just recognizing its name in a word bank.
- `geometry-prism` — both surviving options (A and B) are prisms (rectangular and triangular);
  D1 requires naming both candidates 3 and 6 correctly as prisms, and D2–D5 are built entirely on
  prism geometry.
- `geometry-net`, `geometry-how-to-draw-the-net-of-a-3-d-shape` — D2's literal deliverable is
  constructing a real, dimensioned net for each option, not citing a surface-area formula. This is
  the case's load-bearing how-to skill named in the approved concept.
- `geometry-surface-area`, `geometry-how-to-find-the-surface-area-of-a-prism` — D3 requires actually
  computing net area for a rectangular prism and a triangular prism, the case's central trap
  (material cost tracks net area, not volume — see FACILITATOR.md).
- `geometry-volume`, `geometry-how-to-find-the-volume-of-a-prism` — D4 requires computing volume
  for the product and both box interiors to quantify wasted space; this is the fact a Hero must
  keep separate from D3's net-area figure to avoid the case's trap.
- `advanced-numbers-how-to-find-the-percent-of-a-number` — D5 explicitly requires stating the
  margin ("by how much"), which is a percent computation on real numbers, not an assertion.

No skill here is claimed on the strength of "the case is about boxes generally" — each one traces
to a specific requirement in a specific deliverable. `geometry-3-dimensional`, the eleventh skill
in the Geometry/Visual Perceptibility group, is deliberately **not** claimed: no deliverable in this
case specifically forces classifying a shape as "3-dimensional" as a distinct exercise separate
from naming it outright, so claiming it would be padding.
