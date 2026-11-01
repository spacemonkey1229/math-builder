# Learning Goals — The Equivalent Ledger

Bidirectional deliverable ↔ skill matrix. Run at case-write time per skills/case-write/SKILL.md
step 10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — complete factorization of O(n) via prime factorization / GCF | basic-operations-factor, basic-operations-greatest-common-factor, basic-operations-prime, basic-operations-composite, basic-operations-how-to-factor-a-number, basic-operations-how-to-find-the-greatest-common-factor-of-a-set-of-numbers |
| D2 — complete factorization of R(n) via prime factorization / GCF | basic-operations-factor, basic-operations-greatest-common-factor, basic-operations-prime, basic-operations-composite, basic-operations-how-to-factor-a-number, basic-operations-how-to-find-the-greatest-common-factor-of-a-set-of-numbers |
| D3 — sample-test table at three batch sizes, dollars and percent | advanced-numbers-how-to-find-the-percent-of-a-number |
| D4 — written proof verdict from the factored forms | basic-operations-factor, basic-operations-greatest-common-factor |
| D5 — cost comparison table, dollars and percent | advanced-numbers-how-to-find-the-percent-of-a-number |
| D6 — recommendation memo synthesizing D4 and D5 | basic-operations-factor, advanced-numbers-how-to-find-the-percent-of-a-number |

## Forcing test applied to every row

*Could a competent student produce this deliverable correctly without ever performing this skill?*

- **D1/D2** cannot be built without prime-factorizing every coefficient — a student who merely
  guesses a common factor without a factor tree or repeated division has not performed "how to
  factor a number," and cannot correctly identify the *greatest* common factor without comparing
  prime factorizations term by term. The deliverable explicitly requires labeling primes found
  along the way and flagging any intermediate composite number that still needs breaking down —
  a student cannot fully factor 48, 180, 54, 96, or 240 without repeatedly asking "is this factor
  prime, or is it composite and does it need to keep splitting?" That is the whole mechanism of
  the "Factor"/"Prime"/"Composite" terms and the two "how to…" procedures — this case is the
  first in the corpus to force a student through that process twice, on two different
  expressions, specifically so the results can be compared.
- **D3** requires evaluating both formulas and stating a percent difference — direct
  percent-of-a-number work, and it is the step that manufactures the false confidence the case
  is built to catch (two formulas that agree at both tested batch sizes).
- **D4** is the core of the case: a student cannot correctly answer "are these the same
  expression for every n, or only coincidentally equal at two points" by looking at D3's matching
  numbers — that question can only be answered by comparing D1 and D2's fully factored forms and
  checking whether every term of each factored expression shares the same structure (specifically,
  whether *n* itself is a common factor of every term). A student who skips D1/D2 and answers from
  D3 alone has done exactly the "incomplete-proof" move the case is designed to catch, and will
  get D4 wrong.
- **D5** requires taking a percent of a dollar figure (labor hours × wage) and comparing it against
  a probability-weighted dollar figure (probability × cost) — direct percent-of-a-number and
  dollar-comparison work.
- **D6** requires citing the factoring proof (Factor/GCF) to argue whether D5's risk figure was
  even the right number to trust in the first place, plus restating D5's percent comparison —
  a student cannot write a defensible memo without both.

## LEARNING GOAL CHECK

```
deliverables: 6    claimed skills: 7    new_coverage: 0 (see case.json.reinforcement_note)
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```
