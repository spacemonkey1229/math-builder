# Learning Goals — Key Length

Bidirectional deliverable ↔ skill matrix. `case-write`, 2026-08-12.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — factor Candidate A, list every prime tested | `basic-operations-factor`, `basic-operations-prime`, `basic-operations-how-to-factor-a-number` |
| D2 — factor Candidate B, list every prime tested | `basic-operations-factor`, `basic-operations-prime`, `basic-operations-how-to-factor-a-number` (reinforced) |
| D3 — explain why a two-odd-prime product can't be even | `number-sense-odd` |
| D4 — evaluate "odd implies safe," true/false | `discrete-mathematics-logical-statement` |
| D5 — real 2048-bit/3072-bit key decimal digit counts | `number-sense-numbers-and-counting-digit` |
| D6 — square roots and target distances | `advanced-operations-how-to-evaluate-an-absolute-value-expression` (already covered) |
| D7 — percentage-margin verdict | `advanced-numbers-how-to-find-the-percent-of-a-number` (already covered) |

## LEARNING GOAL CHECK

```
deliverables: 7    claimed skills: 8    new_coverage: 6
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each new-coverage skill** (*could a competent Hero produce the
deliverable correctly without ever performing this skill?*):

- `factor` / `prime` / `how-to-factor-a-number` — D1/D2 explicitly require listing every prime
  tested in order until the two prime factors are found; there is no route to the correct factor
  pairs (11×13, 17×19) without actually performing trial-division factoring.
- `odd` — D3 asks for an explanation grounded in the specific fact that the primes involved are odd
  (neither is 2); a Hero must reason about parity, not just report the factors.
- `logical-statement` — D4 requires evaluating a specific conditional statement ("if odd, then
  safe") as true or false with a justifying counterexample — 143 itself, odd but not prime, is the
  natural disproof a Hero who did D1 already has in hand.
- `digit` — D5's answer (617 and 925 decimal digits) only comes from applying the given
  bits-to-digits conversion to real bit counts; guessing a round number would not produce these
  specific values.

No skill here is claimed on the strength of "the case is about cryptography generally" — each one
traces to a specific verb in a specific deliverable, using the exact operation (factor vs. classify
vs. evaluate a conditional vs. count) each spine skill actually names.
