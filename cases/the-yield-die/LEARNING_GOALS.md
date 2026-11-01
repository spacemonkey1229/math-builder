# The Yield Die — Learning Goal Matrix

Bidirectional check between Challenge 3 deliverables and claimed spine skills (`case-write`
SKILL.md §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — scientific-notation conversion table (every raw figure converted both directions) | `advanced-operations-scientific-notation`, `advanced-operations-standard-notation`, `advanced-operations-how-to-write-a-number-in-scientific-notation-given-its-standard-notation`, `advanced-operations-how-to-write-a-number-in-standard-notation-given-its-scientific-notation` (a student cannot produce a conversion table with a shown exponent shift for every row without knowing what "standard notation" and "scientific notation" name, and without applying both conversion how-tos — the deliverable explicitly requires both directions, not just one) |
| D2 — transistor-count comparison (density × area, both directions of a die option) | `advanced-operations-scientific-notation`, `advanced-operations-how-to-write-a-number-in-scientific-notation-given-its-standard-notation` (multiplying two scientific-notation figures and re-expressing the product correctly in scientific notation — adding exponents and renormalizing the coefficient when it falls outside [1, 10) — is exactly this how-to; a student who cannot do this cannot produce a correct transistor count for either option) |
| D3 — gross-die-per-wafer table (wafer geometry formula, intermediate figures in scientific notation) | `advanced-operations-scientific-notation`, `advanced-operations-how-to-write-a-number-in-standard-notation-given-its-scientific-notation` (the deliverable explicitly requires converting the final gross-die count back to standard notation — a student cannot do that final conversion without this how-to, and cannot carry the wafer-area and die-area terms through the formula without treating them as scientific-notation quantities) |
| D4 — yield-and-net-good-die table (defect-density yield model, defect density entered in scientific notation) | `advanced-operations-scientific-notation`, `advanced-operations-standard-notation` (the defect density is a small decimal that is naturally written in scientific notation, and the deliverable requires the resulting yield percentage and net-good-die count to be reported in ordinary, readable standard notation — a student cannot complete D4 as specified without moving correctly between the two forms) |
| D5 — revenue-per-wafer recommendation memo | `advanced-operations-how-to-write-a-number-in-scientific-notation-given-its-standard-notation` (D5 explicitly requires every revenue figure to be shown in scientific notation before it is converted to a final dollar total — a student who only ever writes dollar totals in standard notation, with no scientific-notation intermediate step, has not produced D5 as specified) |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 4    new_coverage: []  (see coverage note — all 4 sit at n>=1, not n=0)
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forces test applied:** a competent student cannot produce D1 without correctly naming and
distinguishing standard notation from scientific notation and applying both conversion procedures
in both directions — D1 explicitly requires converting raw figures into scientific notation *and*
converting at least one given scientific-notation figure back into standard notation, so a student
who only ever practices one direction has not produced D1 as specified. D2 is not a redundant
repeat of D1: it requires multiplying two scientific-notation quantities together and correctly
renormalizing the result (the coefficient can fall outside [1, 10) after multiplication and must be
corrected by shifting the exponent), which is a materially different skill application than simply
converting a single given number. D3 and D4 both force the standard-notation-given-scientific
direction specifically, because both deliverables explicitly require converting a scientific-
notation intermediate result back into an ordinary, readable count or percentage — this is the
direction the corpus reinforces least (see coverage note) and D3/D4 are written to force it twice
more, on top of D1. D5 forces the scientific-notation-given-standard direction one further time on
a dollar figure. Neither introduces a new skill claim outside the four already in
`case.json.standards[]`.

## Coverage note

All 4 target skills (`advanced-operations-scientific-notation` n=3,
`advanced-operations-standard-notation` n=1,
`advanced-operations-how-to-write-a-number-in-scientific-notation-given-its-standard-notation` n=3,
`advanced-operations-how-to-write-a-number-in-standard-notation-given-its-scientific-notation` n=1)
were checked against `readmodel/standards_spine.json` at the start of this write pass (2026-09-09)
and every one already carries `n >= 1`. Per SPEC §4, `new_coverage[]` is strictly the subset with
`n == 0`; none of these four qualifies, so `new_coverage` is correctly `[]` here. This case does
**not** claim any skill from the sibling "Factorial" or "Absolute Value" terms in the same spine
group (those are the target of a different, separately-written case, `the-schedule-explosion`, per
the approved concept sheet's own instruction not to duplicate that case's claims).

**Why this case exists anyway — the reinforcement argument.** The approved concept sheet
(`cases/_concepts/CONCEPTS_batch-c-current-events_2026-09-09.md`, concept #3, "The Yield Die")
names this skill group as "9 of 8 skills thin (near-full close on the Scientific Notation half)" —
already thin across the board, not a zero-coverage gap. `advanced-operations-standard-notation`
(n=1) and `advanced-operations-how-to-write-a-number-in-standard-notation-given-its-scientific-
notation` (n=1) are the two thinnest skills in the entire group, tied for thinnest of the four this
case targets. D1, D3, and D4 are all written specifically to force the standard-notation-given-
scientific direction (D1 once, D3 and D4 each once more), and D1 additionally forces the bare
"Standard Notation" vocabulary term directly by requiring the student to name what they are
converting into. This is a genuine reinforcement case, not a padded zero-coverage claim.

**`reinforcement_note` (recorded in `case.json`):** "All 4 claimed skills already show n>=1 in
`readmodel/standards_spine.json` at write time (Standard Notation n=1, Scientific Notation n=3, the
scientific-given-standard how-to n=3, the standard-given-scientific how-to n=1), so `new_coverage[]`
is correctly empty per SPEC §4's literal n==0 rule. This case was approved from the concept sheet
specifically to reinforce the Scientific-Notation half of a thin skill group (the concept sheet's
own framing: '9 of 8 skills thin, near-full close on the Scientific Notation half'), targeting the
two thinnest skills in that half (Standard Notation, n=1, and the standard-given-scientific how-to,
n=1) by forcing them across D1/D3/D4, not to close a zero-coverage gap — consistent with the
precedent set in `cases/the-bracket-bet/LEARNING_GOALS.md` for disclosed reinforcement-only cases,
and consistent with the concept sheet's explicit instruction to target the Scientific Notation
skills specifically rather than duplicate the sibling `the-schedule-explosion` case's Factorial
claims."
