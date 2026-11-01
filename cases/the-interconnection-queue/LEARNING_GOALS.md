# Learning Goals — The Interconnection Queue

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 total-demand table (4 bids added) | fractions-how-to-add-fractions, fractions-how-to-add-with-mixed-numbers |
| D2 remaining-capacity calculation (2 subtractions) | fractions-how-to-subtract-fractions, fractions-how-to-subtract-with-mixed-numbers |
| D3 combined-bid calculation (2 bids added) | fractions-how-to-add-fractions, fractions-how-to-add-with-mixed-numbers |
| D4 head-to-head comparison (subtraction) | fractions-how-to-subtract-fractions, fractions-how-to-subtract-with-mixed-numbers |
| D5 original visual display (capacity-bar diagram) | fractions-how-to-add-fractions, fractions-how-to-subtract-fractions |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever
performing this skill? If yes, the mapping is fake.

- **D1** cannot be produced correctly without adding four mixed numbers with four different
  denominators (2-7/8, 1-1/4, 1-2/3, 1-5/6 — eighths, quarters, thirds, sixths; LCD 24). A student
  who adds the whole-number parts and then adds the numerators of the fraction parts without
  converting to a common denominator first will get a wrong running sum at every step — this is
  the concept sheet's own named trap. Genuinely forces `how-to-add-fractions` (the common-
  denominator mechanics) and `how-to-add-with-mixed-numbers` (carrying and combining whole-number
  parts with fraction parts, including any resulting improper-fraction rollover into a new whole).
- **D2** requires two separate subtractions: first 4-5/8 − 1-1/4 (quarters converted to eighths,
  no regrouping needed) to find the capacity remaining, then 3-3/8 − 2-7/8 (eighths, and this one
  *does* require regrouping — 3/8 is less than 7/8, so a whole block must be borrowed and rewritten
  as 8/8 before the subtraction can proceed). A student who does not know how to borrow across a
  mixed-number subtraction cannot produce a correct D2 at all; a student who tries to subtract
  numerators directly without a common denominator produces the case's own core trap (an over- or
  under-stated leftover capacity). Genuinely forces `how-to-subtract-fractions` and
  `how-to-subtract-with-mixed-numbers`.
- **D3** requires adding 1-1/4 and 1-2/3 (quarters and thirds; LCD 12), another genuine unlike-
  denominator mixed-number addition with an improper-fraction rollover (11/12 + who knows,
  computed correctly gives 2-11/12, only reachable by first converting both fraction parts to
  twelfths). A student who cannot perform this conversion cannot determine whether the combined
  bid actually fits inside the remaining capacity from D2. Genuinely forces `how-to-add-fractions`
  and `how-to-add-with-mixed-numbers`, independently of D1 (different denominators, different
  bids).
- **D4** requires subtracting D3's result (2-11/12, twelfths) from D2's remaining capacity (3-3/8,
  eighths) — a third genuinely different unlike-denominator pair (LCD 24) — and again requires
  regrouping (9/24 is less than 22/24). Without this subtraction a student cannot state a real
  stranded-capacity figure for Option B at all, let alone compare it to Option A's from D2.
  Genuinely forces `how-to-subtract-fractions` and `how-to-subtract-with-mixed-numbers` a second,
  independent time.
- **D5** requires building an accurately scaled bar diagram whose segment boundaries are exactly
  D2's and D4's computed sums and differences — a diagram cannot be drawn to scale without the
  underlying addition/subtraction being correct first, so a student who has not actually performed
  the arithmetic cannot produce a diagram that agrees with itself between the "used" and "stranded"
  portions. Reinforces `how-to-add-fractions` and `how-to-subtract-fractions` as a visual proof of
  the arithmetic already required by D2–D4, not a new skill.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 4    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

See `case.json.reinforcement_note` for the full accounting. Every claimed skill was checked
against `readmodel/standards_spine.json` before writing (2026-09-09) and all four are `n=1`, not
`n=0` — the task brief's "every skill in this group sits at n=1 today, a genuine full-group close
opportunity" describes the group as thin, not as containing a true zero-coverage skill. Per SPEC
§7 and case-write's own anti-padding validator, `new_coverage[]` must stay empty here (claiming an
`n=1` skill in `new_coverage[]` is a fabricated-coverage BLOCKER). This case reinforces all 4 thin
skills in Fractions/Addition and Subtraction of Fractions via the reinforcement carve-out (T1-10,
`skills/case-readiness/SKILL.md`, 2026-08-17) — the same pattern used in
`cases/the-special-order/LEARNING_GOALS.md`, `cases/the-deferred-repair/LEARNING_GOALS.md`, and
`cases/a-coachs-dilemma/LEARNING_GOALS.md`. `new_coverage[]` is `[]`, honestly, not padded.
