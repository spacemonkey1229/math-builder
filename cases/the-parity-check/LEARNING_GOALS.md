# The Parity Check — Learning Goal Matrix

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — byte-level parity worked table (1-bit counts, even/odd, appended bit) | `number-sense-even`, `number-sense-odd`, `number-sense-number` |
| D2 — "silent miss" corrupted-byte demonstration | `number-sense-even` |
| D3 — overhead-vs-packet-size comparison table | `number-sense-number` |
| D4 — bits-to-decimal-digits comparison (parity bit vs. 32-bit CRC value) | `number-sense-numbers-and-counting-digit` |
| D5 — break-even packet-size calculation and recommendation | `statistics-and-probability-probability`, `number-sense-even`, `number-sense-odd` |

## Bidirectional check

**Claimed skills (standards[]), 5 total:**

`number-sense-even`, `number-sense-odd`, `number-sense-numbers-and-counting-digit`, `number-sense-number`, `statistics-and-probability-probability`

Every one of the 5 appears in at least one deliverable's skill list above:

- **`number-sense-even` / `number-sense-odd`** — D1 is not producible without actually counting each sample byte's 1-bits and classifying that count as even or odd; that classification *is* the parity bit. D2 requires constructing a specific corrupted byte with an even bit-flip count and showing why it evades detection — a student who cannot tell even from odd cannot build this deliverable at all, only describe it vaguely. D5 requires estimating the probability of an even-vs-odd flip count per byte from Appendix E's stated rate; a student cannot separate "the parity-blind case" from "the parity-catches case" in that probability estimate without the even/odd distinction.
- **`number-sense-numbers-and-counting-digit`** — D4 is not solvable by describing bit counts alone; it requires converting a bit-length (1 bit vs. 32 bits) into the number of base-10 digits needed to write the largest possible value of that length, the same bits-to-decimal-digits reasoning used in `cases/key-length`'s D5. A student who only reports "32 bits" without converting to a digit count has not produced D4.
- **`number-sense-number`** — D1 requires reading each sample byte's raw bit pattern as a number (or at minimum counting its 1-bits as a numeric quantity) before classification is possible; D3's overhead table is a table of numbers (bit counts, byte counts, percentages) that must be computed, not narrated.
- **`statistics-and-probability-probability`** — D5's break-even calculation is not reachable without first estimating a probability (the chance a byte suffers an even, undetected number of flips) from Appendix E's stated per-bit error rate. Comparing raw overhead bits alone, with no probability estimate, cannot produce the primary metric's denominator (error patterns caught).

**"Forces" test applied:** for each mapping above, a competent student could not produce the named deliverable correctly by narrating around the skill — each requires actually performing it (counting and classifying bit counts, converting a bit-length to a digit count, or estimating a probability from a stated rate) to get a checkable, specific answer, not a plausible-sounding paragraph.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 5    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Note on `new_coverage: 0`.** All five claimed skills are currently `n >= 1` on the live spine
(re-verified 2026-09-12: `number-sense-even`, `number-sense-odd`, and
`number-sense-numbers-and-counting-digit` are each `n=1`; `number-sense-number` is `n=25`;
`statistics-and-probability-probability` is `n=17`). Per SPEC §4, `new_coverage[]` is strictly the
subset with `n==0` before this case, so none of these five qualify under the strict test and
`new_coverage[]` is correctly empty. This case is a **reinforcement** case for the three thin
skills — see `case.json`'s `reinforcement_note` — following the identical, already-established
resolution documented in `cases/pixel-snap/LEARNING_GOALS.md` and `cases/the-repeat-match/case.json`
for a case whose target skills had already moved past `n==0` by write time. Flagged here for human
sign-off per SPEC §7's intent, not silently resolved.
