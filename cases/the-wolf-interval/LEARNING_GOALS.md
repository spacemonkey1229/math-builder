# LEARNING GOALS — The Wolf Interval

Bidirectional deliverable ↔ skill matrix (case-write §10, MCS-10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — prime-factorization proof table (3^12 vs 2^k) | `basic-operations-prime`, `basic-operations-composite`, `basic-operations-how-to-factor-a-number` |
| D2 — worked comma calculation, comma expressed as a fraction in lowest terms | `basic-operations-how-to-factor-a-number` |
| D3 — spread the comma's excess fraction across 12 fifths | `fractions-how-to-divide-a-fraction-by-a-whole-number` |
| D4 — octave ratio ÷ fifth ratio, how many fifth-steps complete an octave | `fractions-how-to-divide-a-whole-number-by-a-fraction` |
| D5 — per-key distribution table + average fraction-of-a-semitone mistuning (total ÷ 12 keys) | `fractions-how-to-divide-a-fraction-by-a-whole-number` |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 5    new_coverage: 0
UNMAPPED DELIVERABLES: none — every deliverable (D1–D5) has a non-empty skills column
UNREACHABLE SKILLS: none — every claimed skill in standards[] is forced by at least one deliverable:
  basic-operations-prime                                    <- D1
  basic-operations-composite                                <- D1
  basic-operations-how-to-factor-a-number                   <- D1, D2
  fractions-how-to-divide-a-fraction-by-a-whole-number       <- D3, D5
  fractions-how-to-divide-a-whole-number-by-a-fraction       <- D4
RESULT: PASS
```

**"Forces" test applied per skill:**

- *Prime / Composite / How to factor a number* — D1's entire deliverable IS the factorization
  proof. A student cannot show "3^12 and 2^k share no common prime factor" without actually
  factoring both numbers and classifying primes vs. composites along the way. There is no
  shortcut that skips this.
- *How to divide a fraction by a whole number* — D3 requires taking the comma's excess fraction
  (7153/524288) and dividing it by the whole number 12 to find the per-fifth share; D5's average
  (total mistuning ÷ 12 keys) is the same operation applied to the final answer. A student who
  multiplies instead of divides, or who converts to a decimal first, has not done the deliverable
  as specified (case.md explicitly asks for the fraction-by-whole-number division to be shown).
- *How to divide a whole number by a fraction* — D4 requires dividing the whole-number octave
  ratio (2) by the fractional fifth ratio (3/2) to find the remaining ratio (4/3). This is the
  one calculation in the case that is NOT a whole-number-by-whole-number operation and NOT
  reducible to D3's form (a whole number divided by a fraction is the reciprocal operation of
  D3's fraction divided by a whole number — both skills genuinely appear, not just one dressed
  up twice).

## new_coverage — why it is empty (reinforcement carve-out, see case.json.reinforcement_note)

None of this case's five claimed skills has `n == 0` in the live `readmodel/standards_spine.json`
(checked 2026-09-17): `basic-operations-prime` n=2, `basic-operations-composite` n=2,
`basic-operations-how-to-factor-a-number` n=2, `fractions-how-to-divide-a-fraction-by-a-whole-number`
n=1, `fractions-how-to-divide-a-whole-number-by-a-fraction` n=1. A full sweep of the spine
(`python3 -c "..."` over every domain/group) found **zero** skills anywhere in the entire spine at
n==0 — every skill in the corpus has been touched by at least one case already, so no case authored
today can produce a literal SPEC §7 "closes a gap that was at n==0" claim. This case instead closes
`readmodel/gap_queue.json`'s Basic Operations/Factoring group (`n_gap: 3` of 6, its full remaining
thin-skill list: Prime, Composite, How to factor a number, all three exercised here) and adds a
second, non-redundant forcing of the Fractions/Division-Of-Fractions group's two n=1 skills — the
group's thinnest remaining pair, and deliberately the two `The Downbeat Split` (a sibling
music-acoustics case) does NOT already claim (that case forces
`fractions-how-to-divide-a-fraction-by-a-fraction` and
`fractions-how-to-divide-fractions-and-mixed-numbers` instead — checked in `cases/the-downbeat-split/`
where present, and against `standards_spine.json`'s own `covered_by[]` for these two ids). No
adjacent n==0 skill exists anywhere in Basic Operations, Factoring, or the Division-Of-Fractions
group for this case to honestly claim instead — see `case.json.reinforcement_note` for the record of
this check, per the 2026-08-17 T1-10 reinforcement carve-out.
