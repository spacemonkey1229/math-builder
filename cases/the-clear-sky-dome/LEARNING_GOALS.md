# Learning Goals — Clear-Sky Dome

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 drum-wall surface-area table | geometry-how-to-find-the-surface-area-of-a-cylinder |
| D2 drum-wall + windscreen shell-volume table (outer-minus-inner solid) | geometry-how-to-find-the-volume-of-a-cylinder, geometry-how-to-find-the-volume-of-a-cone |
| D3 dome-cap shell-volume table (hemisphere as half a sphere) | geometry-how-to-find-the-volume-of-a-sphere |
| D4 pier-footing surface-area + volume table | geometry-how-to-find-the-surface-area-of-a-pyramid, geometry-how-to-find-the-volume-of-a-pyramid |
| D5 clear-sky probability table (expected nights, run-probability) | statistics-and-probability-independent-event |
| D6 usable-hours-per-dollar table (compound unit chain: nights → hours → hours/$) | measurement-how-to-convert-an-amount-with-compound-units |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** cannot be produced without applying the cylinder surface-area formula (2πrh + the circular ends, or the specific exterior area the case asks for) to the drum's real radius and height. A student who states only a total number with no formula, or who confuses surface area with volume, has not produced this deliverable. Genuinely forces `how-to-find-the-surface-area-of-a-cylinder`.
- **D2** is impossible without computing two solids' volumes and subtracting — an outer-radius cylinder volume minus an inner-radius cylinder volume for the drum, and the equivalent outer-minus-inner cone volume for the windscreen — then converting to mass and cost. A student who estimates "some steel" or uses only surface area × a guessed thickness without the volume formula has not met the deliverable's own stated method. Genuinely forces both `how-to-find-the-volume-of-a-cylinder` and `how-to-find-the-volume-of-a-cone`.
- **D3** requires recognizing the dome cap as literally half of a full sphere and applying the sphere-volume formula (4/3)πr³ (halved) to both the outer and inner radius, then subtracting. A student who treats the dome cap as a flat disk, or who never states the sphere-volume formula at all, has not produced this deliverable. Genuinely forces `how-to-find-the-volume-of-a-sphere`.
- **D4** cannot be produced without both the pyramid surface-area formula (base + four triangular lateral faces, each needing a slant-height calculation) and the pyramid volume formula ((1/3) × base area × height) applied to the stated footing dimensions. A student who reports only one of the two, or who treats the footing as a rectangular prism instead of a pyramid, has not met this deliverable. Genuinely forces both `how-to-find-the-surface-area-of-a-pyramid` and `how-to-find-the-volume-of-a-pyramid`.
- **D5** requires explicitly modeling each night as an independent yes/no trial with a fixed probability (the site's clear-sky fraction) and using that model to compute both an expected count (probability × 365) and the probability of a specific run of consecutive successes (probability raised to a power) — which only makes sense, and is only a legitimate multiplication, because the trials are treated as independent. A student who just multiplies the fraction by 365 without ever stating or using the independence assumption for the run-probability part has not completed this deliverable's own stated requirement. Genuinely forces `Independent Event`.
- **D6** cannot be produced without chaining compound-unit conversions: nights/year → hours/year (nights × hours/night) and hours/year and dollars → hours per dollar (a compound rate), with every conversion step shown. A student who writes only a final ratio with no visible unit chain has not shown the compound-unit conversion this deliverable requires. Genuinely forces `how-to-convert-an-amount-with-compound-units`.

```
LEARNING GOAL CHECK
  deliverables: 6    claimed skills: 8    new_coverage: 0 (reinforcement — see case.json.reinforcement_note)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

Checked every claimed skill's `n` in `readmodel/standards_spine.json` live on 2026-09-17/18, immediately
before writing: `geometry-how-to-find-the-surface-area-of-a-cylinder` (n=2),
`geometry-how-to-find-the-volume-of-a-cylinder` (n=2), `geometry-how-to-find-the-volume-of-a-cone` (n=2),
`geometry-how-to-find-the-volume-of-a-sphere` (n=2), `geometry-how-to-find-the-surface-area-of-a-pyramid`
(n=2), `geometry-how-to-find-the-volume-of-a-pyramid` (n=2),
`statistics-and-probability-independent-event` (n=2),
`measurement-how-to-convert-an-amount-with-compound-units` (n=19). The concept sheet
(`cases/_concepts/CONCEPTS_astronomy_2026-09-12.md`) itself already flagged, from its own live check on
2026-09-12, that a spine-wide sweep earlier in this project's history (see
`cases/flow-state/case.json.reinforcement_note`, `cases/the-fee-route/case.json.reinforcement_note`,
`cases/the-turbine-channel/case.json.reinforcement_note`) found **zero** skills anywhere in the 437-skill
spine at true `n==0` — no freshly-authored case can produce a literal `new_coverage[]` right now.
`new_coverage[]` is therefore honestly `[]`, per the reinforcement carve-out
(`skills/case-readiness/SKILL.md`, "The reinforcement carve-out on T1-10," added 2026-08-17), rather than
padded with a skill no deliverable forces.

This case still does the job the concept sheet scored it for: all seven Geometry/Surface Area And Volume
`how-to` skills plus the one remaining thin term in that same group's family are the **entire remaining
thin set** the concept sheet identified (6/6 how-tos in Geometry/Surface Area And Volume, plus
`Independent Event` from Statistics And Probability/Probability), every one currently at n=2, and every
one is genuinely forced by a deliverable above — not listed because it sounds related. Landing this case
takes all seven Geometry/Surface Area And Volume how-tos from n=2 to n=3, a full reinforcement close of
that group's how-to set.
