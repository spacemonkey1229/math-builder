# Learning Goals — Survey Corner

Bidirectional deliverable ↔ skill matrix. `case-write`, 2026-08-12.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — plat's expected corner angle (co-interior angles, parallel lines + transversal) | `geometry-transversal-line`, `geometry-how-to-find-angle-measures-given-parallel-lines-a-transversal-line-and-at-least-one-an` |
| D2 — Pin 1's actual corner angle (intersecting lines, supplementary relationship) | `geometry-how-to-find-angle-measures-of-intersecting-lines` |
| D3 — Pin 2's actual corner angle (intersecting lines, supplementary relationship) | `geometry-how-to-find-angle-measures-of-intersecting-lines` (reinforced) |
| D4 — Pin 1 witness triangle: third angle + classification | `geometry-obtuse-triangle`, `geometry-scalene-triangle`, `geometry-how-to-find-the-measure-of-an-interior-angle-of-a-polygon-given-the-other-angles` (already covered) |
| D5 — Pin 2 witness triangle: third angle + classification | `geometry-acute-triangle`, `geometry-scalene-triangle` (reinforced), `geometry-how-to-find-the-measure-of-an-interior-angle-of-a-polygon-given-the-other-angles` (reinforced) |
| D6 — angular deviation of each pin from the expected angle | `advanced-operations-how-to-evaluate-an-absolute-value-expression` (already covered) |
| D7 — percentage-margin verdict | `advanced-numbers-how-to-find-the-percent-of-a-number` (already covered) |

## LEARNING GOAL CHECK

```
deliverables: 7    claimed skills: 9    new_coverage: 6
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each new-coverage skill** (*could a competent Hero produce the
deliverable correctly without ever performing this skill?*):

- `transversal-line` — D1 is explicitly framed around identifying the parcel's west boundary as
  the transversal crossing the two parallel fence lines; there is no route to the co-interior-angle
  relationship without first recognizing this structure.
- `angle-measures-given-parallel-lines-a-transversal-line-and-at-least-one-an` — D1's actual
  numeric answer (87°) only comes from applying the co-interior-angles-sum-to-180° relationship to
  the given 93° northwest angle; no other operation produces it.
- `angle-measures-of-intersecting-lines` — D2/D3 explicitly require converting a raw backsight
  reading into the parcel's own interior angle via the supplementary relationship at an
  intersection; reading the raw value directly would be wrong by construction (88.5°/89.0° are not
  91.5°/91.0°).
- `obtuse-triangle` — D4's triangle (96°, 45°, 39°) has a angle over 90°; classifying it correctly
  requires actually computing all three angles first (the third, 39°, is not given).
- `acute-triangle` — D5's triangle (61°, 55°, 64°) requires the same computation; a Hero must find
  all three angles to confirm none exceeds 90°, not just eyeball two given angles.
- `scalene-triangle` — Both D4 and D5's triangles have three genuinely distinct angles (96/45/39
  and 61/55/64); classifying "no two sides equal" requires comparing all three computed angles, not
  assuming a default shape.

No skill here is claimed on the strength of "the case is about surveying generally" — each one
traces to a specific verb in a specific deliverable, using the exact relationship (co-interior vs.
alternate-interior, intersecting-lines supplementary vs. vertical, angle-based vs. side-based
triangle classification) each spine skill actually names.
