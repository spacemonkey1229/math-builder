# Learning Goals — The Manifest Split

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 labeled Venn diagram + intersection calculation from given H, R, H∪R | discrete-mathematics-set, discrete-mathematics-subset, discrete-mathematics-union, discrete-mathematics-intersection, discrete-mathematics-venn-diagram, discrete-mathematics-how-to-find-the-union-and-intersection-of-two-sets, discrete-mathematics-how-to-represent-a-set-relationship-using-a-venn-diagram |
| D2 total-inspection-time table for each lane configuration | discrete-mathematics-subset, discrete-mathematics-intersection |
| D3 containers-cleared-per-inspector-hour comparison and percent margin | discrete-mathematics-union |
| D4 written recommendation + empty-set edge case | discrete-mathematics-set, discrete-mathematics-empty-set, discrete-mathematics-union, discrete-mathematics-intersection |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** cannot be produced without knowing what a **set** is (H and R are each defined as a set of containers), that H and R are each a **subset** of the total flagged pool, and without actually computing the **union** (given directly as the gate-scan total) and the **intersection** (the quantity the deliverable exists to force the student to find, via H + R − |H∪R|). A student who guesses the overlap or eyeballs it from a drawing rather than deriving it algebraically has not performed `how-to-find-the-union-and-intersection-of-two-sets`. The deliverable also explicitly requires a drawn **Venn diagram** with all three regions correctly labeled with their counts — a student who only produces the arithmetic without the diagram has not performed `how-to-represent-a-set-relationship-using-a-venn-diagram`, and a student who only draws two overlapping circles without correct region counts has not performed either how-to correctly. Genuinely forces `set`, `subset`, `union`, `intersection`, `venn-diagram`, and both how-tos.
- **D2** requires correctly identifying which containers belong to which region of D1's Venn diagram to know how many times each check applies — a container in the **intersection** (a specific, non-empty **subset** of both H and R) gets both checks plus the re-handle cost in Plan B, while a container in H-only or R-only gets exactly one check. A student who applies the re-handle cost to every container in H or every container in R, rather than only to the intersection subset, has not correctly used the subset/intersection relationship this deliverable depends on. Genuinely forces `subset` and `intersection`.
- **D3** requires using D1's **union** count (the total distinct containers cleared) as the numerator for both configurations' rates — a student who instead adds H + R without removing the double-counted intersection (i.e., who does not understand that H ∪ R, not H + R, is the actual number of distinct containers) will report an inflated and incorrect containers-cleared figure for both plans. Genuinely forces `union`.
- **D4** requires reasoning about what happens to the **union**, the **intersection**, and each container's inspection path when the intersection is the **empty set** — a student who cannot explain that an empty intersection means no container ever needs the re-handle step, and that in that case H ∪ R = H + R exactly (no double-counting to remove), has not engaged with the empty-set edge case the deliverable explicitly asks for. This also requires correctly naming H and R as **sets** in the written recommendation. Genuinely forces `set`, `empty-set`, `union`, and `intersection`.

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 8    new_coverage: 0 (see case.json.reinforcement_note)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

At case-write time (2026-09-17/18), a fresh read of `readmodel/standards_spine.json` found all eight
Discrete Mathematics/Set Theory skills targeted by this case already at **n=3** (`covered_by` length 3),
not n=2 as the concept sheet (`CONCEPTS_maritime-shipping_2026-09-12.md`, C1) recorded when it was
written. The spine has moved since that concept sheet was authored — plausibly another case landing
concurrently against the same thin group. Per the reinforcement carve-out (T1-10,
`skills/case-readiness/SKILL.md`, "The reinforcement carve-out on T1-10", added 2026-08-17),
`new_coverage[]` is honestly recorded as empty rather than padded with a skill this case's
deliverables don't force or, worse, a false claim that a skill is still at n==0 when it is not. All 8
claimed skills are still genuinely forced by the deliverables above (see the forces-test), and this
case still adds real reinforcement value to a group that — even at n=3 — remains one of the thinnest
in the entire spine. This project does not edit `readmodel/standards_spine.json` from `case-write` or
`case-readiness`; the live count should be re-verified at `case-publish` time before promotion.
