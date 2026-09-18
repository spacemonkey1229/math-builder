# Learning Goals: Patrol Triangle

Bidirectional deliverable ↔ skill matrix (SPEC.md §1.5 item 3 / `case-write` §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — labeled sector classification table, classified by side length and angle | `geometry-scalene-triangle`, `geometry-obtuse-triangle`, `geometry-equilateral-triangle`, `geometry-acute-triangle` |
| D2 — area-and-staffing table | `geometry-area`, `measurement-how-to-find-a-missing-amount-in-a-proportion` |
| D3 — response-time table | `measurement-how-to-find-elapsed-time` |
| D4 — primary-metric comparison (minutes per km², margin, recommendation) | `measurement-how-to-find-a-missing-amount-in-a-proportion` |
| D5 — outpost-network geometry check (triangle inequality + right-triangle legs) | `geometry-triangle-inequality-theorem`, `geometry-leg` |

## The forces test, applied

- **D1.** A student cannot correctly classify the Perimeter Loop's 18/11/9 km sector without determining it has three unequal sides (scalene) and, via the largest angle (≈128°, opposite the 18 km side), that the angle is obtuse. Nor can they correctly classify the Interior Web's 5.7/5.7/5.7 km sector without recognizing equal sides (equilateral) and, from that, that all three angles are 60° (acute). Producing D1 without these four terms is not possible — a student who mislabels either sector has not completed D1 correctly.
- **D2.** Sector area for a scalene triangle from three side lengths requires the `Area` concept applied via a valid area method (e.g. Heron's formula or an equivalent base-height derivation); converting the reserve's density standard ("1 team per 14 km²") into a required team count for a specific sector area is a proportion — "1 team : 14 km² = x teams : (sector area) km²" — solved for the missing amount x.
- **D3.** Converting a distance-at-a-given-speed into a travel time in minutes, and reasoning about "how much time elapses," is exactly `How to find elapsed time`.
- **D4.** Building "minutes per km²" from D2's area and D3's time, and then computing what fraction one option's ratio is of the other (the margin), is the same missing-amount-in-a-proportion skill applied to the case's actual decision metric, not just to team-staffing.
- **D5.** Part (a) cannot be completed without applying the Triangle Inequality Theorem directly to the three reported outpost distances (6.0 + 6.5 = 12.5 < 13.0 → the three distances cannot form a real triangle). Part (b) cannot be completed without identifying and labeling the two legs of the right-triangle relay route before computing the hypotenuse.

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 9    new_coverage: 0 (reinforcement carve-out — see below)
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

- `geometry-acute-triangle`, `geometry-obtuse-triangle`, `geometry-scalene-triangle`, `geometry-equilateral-triangle`, `geometry-leg`, `geometry-triangle-inequality-theorem` are all `n=2` in the live spine — Geometry/Triangles's entire remaining thin group per the concept sheet — and are all reached by D1 or D5. A live spine sweep (2026-09-18) found zero skills anywhere at literal `n==0`, so per the reinforcement carve-out (`skills/case-readiness/SKILL.md`) these are recorded as `standards[]` with an honest empty `new_coverage[]` and a `case.json.reinforcement_note`, not padded. This case still takes the entire group from n=2 to n=3.
- `geometry-area` (n=11) and `measurement-how-to-find-elapsed-time` (n=12) and `measurement-how-to-find-a-missing-amount-in-a-proportion` (n=13) are further reinforcement — already covered elsewhere, but genuinely forced here too (D2, D3, D2/D4 respectively), not padding.
- No deliverable has an empty skills column. No claimed skill lacks a forcing deliverable.
