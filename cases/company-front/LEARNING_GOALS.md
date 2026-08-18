# Learning Goals — Company Front

Bidirectional deliverable ↔ skill matrix. `case-write`, 2026-08-12.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — symmetry check (reflect across Y-axis) | `geometry-how-to-reflect-a-figure-across-the-y-axis`, `geometry-transformation` |
| D2 — The Expand worked in full (dilation + reverse scale-factor) | `geometry-dilation`, `geometry-scale-factor`, `geometry-how-to-dilate-a-figure-on-the-coordinate-plane-given-a-scale-factor`, `geometry-how-to-find-the-scale-factor-of-a-dilation` |
| D3 — The Mirror Turn worked in full (90° CCW rotation + CW comparison) | `geometry-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-counterclockwise`, `geometry-rotation`, `geometry-clockwise`, `geometry-counter-clockwise`, `geometry-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-clockwise` |
| D4 — congruent-or-similar classification | `geometry-congruent`, `geometry-similar` |
| D5 — the ruled-out 180° pivot | `geometry-how-to-rotate-a-figure-on-the-coordinate-plane-180-degrees` |
| D6 — the verdict (ceiling comparison, as a percentage) | `advanced-numbers-how-to-find-the-percent-of-a-number` |

## LEARNING GOAL CHECK

```
deliverables: 6    claimed skills: 15    new_coverage: 9
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each skill** (*could a competent Hero produce the deliverable correctly
without ever performing this skill?*):

- `how-to-reflect-a-figure-across-the-y-axis` — D1 explicitly requires reflecting the right-half
  markers across the Y-axis and checking the result against the left half; there is no other way
  to produce that check.
- `dilation`, `scale-factor`, `how-to-dilate-a-figure-on-the-coordinate-plane-given-a-scale-factor`
  — D2's entire first half is dilating nine markers by the stated scale factor; a Hero cannot find
  the new coordinates or the resulting travel distances without performing a dilation.
- `how-to-find-the-scale-factor-of-a-dilation` — D2's second half explicitly asks a Hero to
  recover the scale factor from only one marker's start/end coordinates, the mirror-image skill of
  applying one. This is a distinct move from the first half (division rather than multiplication)
  and is the one place in the case an unknown scale factor must be solved for.
- `how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-counterclockwise` — D3 requires
  rotating all nine markers 90° about center; the case specifies counterclockwise as the primary
  direction for The Mirror Turn (the already-covered clockwise skill is reused only for the
  D3 comparison question, which explicitly does not require re-deriving all nine coordinates a
  second time — it is answerable from the symmetry argument D1 already proved).
- `congruent`, `similar` — D4 requires classifying each of two results (not one), and requires a
  justification tied to the *defining property* of the transformation that produced it (rotation
  preserves size and shape → congruent; dilation by a non-unit scale factor preserves shape only →
  similar). A Hero who cannot state this distinction cannot complete D4 correctly.
- `how-to-rotate-a-figure-on-the-coordinate-plane-180-degrees` — D5 requires finding all nine
  markers' positions under a 180° rotation, a distinct computation from D3's 90° rotation (different
  transformation rule: `(x,y) -> (-x,-y)` vs `(x,y) -> (-y,x)`). The fact that this option is later
  rejected for a non-geometric reason does not make the geometry itself optional — the deliverable
  requires computing it before explaining why it was set aside, mirroring the project's existing
  pattern (Plaza Pavers' rhombus/kite non-geometric rejection).

**Already-covered skills also exercised, not claimed in `new_coverage[]`:** `geometry-transformation`
(n=1, D1), `geometry-rotation` (n=1, D3), `geometry-clockwise` (n=1, D3), `geometry-counter-clockwise`
(n=1, D3), `geometry-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-clockwise` (n=1, D3's
CW-vs-CCW comparison question), `advanced-numbers-how-to-find-the-percent-of-a-number` (n=17, D6) —
all closed elsewhere already; reused here where genuinely forced. `geometry-translation` is
deliberately **not** claimed — nothing in this case's deliverables forces a translation, only
dilation and rotation.

No skill here is claimed on the strength of "the case is about transformations generally" — each
one traces to a specific verb in a specific deliverable. This case closes the entire remaining
Geometry/Transformations gap (20/20 skills now covered across Plaza Pavers + Company Front).
