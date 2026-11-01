# Learning Goals — The Culling Volume

Bidirectional deliverable ↔ skill matrix, run per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 real volume + surface area of all 3 props (cylinder+cone / cylinder+pyramid decomposition) | `geometry-how-to-find-the-surface-area-of-a-pyramid`, `geometry-how-to-find-the-surface-area-of-a-cylinder`, `geometry-how-to-find-the-volume-of-a-pyramid`, `geometry-how-to-find-the-volume-of-a-cylinder`, `geometry-how-to-find-the-volume-of-a-cone` |
| D2 bounding sphere volume + wasted volume, per prop and scene total | `geometry-how-to-find-the-volume-of-a-sphere` |
| D3 bounding capsule volume + wasted volume, per prop and scene total | `geometry-how-to-find-the-volume-of-a-cylinder`, `geometry-how-to-find-the-volume-of-a-sphere` |
| D4 total per-frame cost (ms) for both options + margin | `geometry-how-to-find-the-volume-of-a-sphere`, `geometry-how-to-find-the-volume-of-a-cylinder` |
| D5 written recommendation + sensitivity call-out | `geometry-how-to-find-the-volume-of-a-sphere`, `geometry-how-to-find-the-volume-of-a-cylinder` |

## LEARNING GOAL CHECK

```
  deliverables: 5    claimed skills: 6    new_coverage: 0 (reinforcement carve-out — see case.json.reinforcement_note)
  UNMAPPED DELIVERABLES: none — every deliverable (D1-D5) maps to at least one claimed skill
  UNREACHABLE SKILLS: none — every claimed skill is forced by at least one deliverable:
     - surface area of a pyramid: D1 (sign post's pyramidal cap)
     - surface area of a cylinder: D1 (lamppost pole, pipe, sign post's cylinder components)
     - volume of a pyramid: D1 (sign post's pyramidal cap)
     - volume of a cylinder: D1 (all three props' cylinder components), D3 (capsule body), D4, D5
     - volume of a cone: D1 (lamppost's fixture cap)
     - volume of a sphere: D2 (bounding sphere), D3 (capsule's two hemispherical caps = one sphere), D4, D5
  RESULT: PASS
```

"Forces" test applied: a student cannot produce D1's volumes/surface areas without genuinely
applying the pyramid/cylinder/cone formulas to three different real components; cannot produce
D2/D3's bounding-shape volumes without the sphere formula (D2 directly, D3 via its hemispherical
caps); cannot produce D4's total cost without having D2 and D3's volumes already in hand. No
deliverable is decorative.

Next step: `Run case-research on the-culling-volume to fill open placeholders.` (Already run in
the same authoring pass — see `RESEARCH_LOG.md`.)
