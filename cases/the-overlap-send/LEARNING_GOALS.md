# Learning Goals — The Overlap Send

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 Venn diagram with all four regions labeled, including an empty-set check | discrete-mathematics-venn-diagram, discrete-mathematics-set, discrete-mathematics-empty-set, discrete-mathematics-how-to-represent-a-set-relationship-using-a-venn-diagram |
| D2 set-notation summary (\|P\|, \|L\|, \|P∩L\|, \|P∪L\|) + subset determination | discrete-mathematics-set, discrete-mathematics-subset, discrete-mathematics-union, discrete-mathematics-intersection, discrete-mathematics-how-to-find-the-union-and-intersection-of-two-sets |
| D3 reach-and-cost table for Option A (P∪L) vs Option B (P∩L) | discrete-mathematics-union, discrete-mathematics-intersection |
| D4 expected-net-revenue calculation for each option | discrete-mathematics-union, discrete-mathematics-intersection |
| D5 written recommendation in correct set notation, addressing the reach-vs-rate trap | discrete-mathematics-subset, discrete-mathematics-union, discrete-mathematics-intersection, discrete-mathematics-empty-set |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** cannot be produced without first defining Set P and Set L as actual sets (the `set` term is not decorative — a Venn diagram is a diagram OF sets), representing them inside a bounding universe rectangle (the `venn-diagram` term and its how-to), and correctly labeling all four regions including checking whether the "neither" region (or any other region) is the `empty set` — a student who skips the empty-set check, or who draws only two circles with no bounding universe, has not produced this deliverable. Genuinely forces `venn-diagram`, `set`, `empty-set`, and the Venn-diagram how-to.
- **D2** is impossible without treating P and L as genuine sets with a defined membership count (`set`), computing `|P ∪ L|` via inclusion-exclusion from `|P|`, `|L|`, and `|P ∩ L|` (the union/intersection how-to, and the `union`/`intersection` terms individually, since the calculation needs both), and stating a real subset determination — a student who asserts "P is a subset of L" without checking the actual counts (P ∩ L ≠ P, since |P| ≠ |P ∩ L| in this case's data) fails the `subset` requirement even if the rest of the arithmetic is correct. Genuinely forces `set`, `subset`, `union`, `intersection`, and the union/intersection how-to.
- **D3** requires pulling the exact `|P ∪ L|` and `|P ∩ L|` counts computed in D2 forward into a real cost comparison — a student who has not correctly computed the union and intersection sizes cannot produce a correct table here, since the recipient counts ARE those two set operations' outputs. Genuinely forces `union` and `intersection` as applied, load-bearing quantities, not just vocabulary.
- **D4** requires the same union/intersection reach figures as D3, now multiplied through the conversion-rate/AOV chain — a student who mixed up which count is the union and which is the intersection (a common error given Option B's much smaller number) produces a materially wrong expected-revenue comparison. Genuinely forces `union` and `intersection` as the multiplicands the entire recommendation turns on.
- **D5** requires writing the recommendation in actual set notation (∩, ∪, ⊆/⊄, ∅) — a student who writes "the overlap group" and "everyone" in plain English without ever notating P ∩ L, P ∪ L, or the subset/empty-set findings from D1/D2 has not met this deliverable's own stated requirement, even if the dollar conclusion is right. Genuinely forces `subset`, `union`, `intersection`, and `empty-set` as the notation the paragraph must actually use.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 8    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

See `case.json.reinforcement_note` for the full accounting. Every one of the 8 claimed skills
(`discrete-mathematics-set`, `-subset`, `-union`, `-intersection`, `-empty-set`, `-venn-diagram`,
`-how-to-find-the-union-and-intersection-of-two-sets`,
`-how-to-represent-a-set-relationship-using-a-venn-diagram`) was checked against
`readmodel/standards_spine.json` before writing and every one is `n = 1`, not `n = 0` — this case
reinforces a genuinely **thin** group (the concept sheet's own framing: "🟠 thin (8 of 8 skills,
every one at exactly n=1)") rather than closing a true zero-coverage gap. `new_coverage[]` is `[]`,
honestly, per the reinforcement carve-out (T1-10, `skills/case-readiness/SKILL.md`, 2026-08-17) —
the same pattern used in `cases/the-deferred-repair/LEARNING_GOALS.md`. Every one of the 8 skills
is genuinely forced by at least one deliverable (see the matrix and check above), so landing this
case takes the whole Discrete Mathematics / Set Theory group from `n=1` to `n=2` across the board —
real value against the concept sheet's gap-queue accounting, even though it is not, technically,
`new_coverage[]`.
