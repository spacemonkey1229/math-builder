# LEARNING GOALS — The Keyspace Decision

Bidirectional deliverable ↔ skill matrix. Run per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 keyspace table (FCP) | discrete-mathematics-fundamental-counting-principle, discrete-mathematics-how-to-apply-the-fundamental-counting-principle-to-count-outcomes |
| D2 time-to-crack table (compound units) | measurement-how-to-convert-an-amount-with-compound-units |
| D3 pigeonhole collision-bound analysis | discrete-mathematics-pigeonhole-principle |
| D4 breach-vector table (percent shares) | advanced-numbers-how-to-find-the-percent-of-a-number |
| D5 cost-per-dollar synthesis | measurement-how-to-convert-an-amount-with-compound-units, advanced-numbers-how-to-find-the-percent-of-a-number |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 5    new_coverage: 1
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Forces test applied to each mapping** — *could a competent student produce this deliverable
correctly without ever performing this skill?*

- **D1 — no.** A password's keyspace is not a number anyone can look up; it exists only as
  (character-set size) raised to (password length), and the deliverable explicitly demands the
  full application of the Fundamental Counting Principle shown for at least one row. A student
  who writes "there are a lot of possible passwords" has not produced the artifact — the
  deliverable requires the actual count for three different (charset, length) pairs, which is
  three independent applications of the principle.
- **D2 — no.** The offline attack rate is sourced in guesses-per-second; the keyspace is a pure
  count; and the deliverable's output is years. There is no path from seconds to years without a
  compound-unit conversion, and the deliverable explicitly demands that conversion shown in
  writing.
- **D3 — no.** This is the one deliverable in the case that cannot be answered by comparing sizes
  intuitively. "How many employees before two are guaranteed to collide" is, by definition, the
  keyspace size plus one — a direct, textbook application of the Pigeonhole Principle, and the
  deliverable explicitly names the principle and demands the comparison against Bramwell's actual
  headcount. A student cannot produce a defensible collision bound by guessing at "probably fine"
  or "probably risky" — the guarantee threshold is a specific, computed integer.
- **D4 — no.** The breach-vector figures are published as percentage shares of a whole (breaches
  attributable to each initial-access category); combining a percentage share with an incident
  volume, and combining the MFA-blocking percentage with a takeover rate, is exactly finding the
  percent of a number, done twice and combined.
- **D5 — no.** The primary metric is a *rate* — years per dollar — built by dividing a
  time-valued figure (itself the product of D2's crack-time and D4's percent-weighted takeover
  probability) by a dollar-valued figure. Producing that single comparable number for both options
  requires both the compound-unit division and at least one more percent-of-a-number step to
  apply D4's weighting to D2's raw crack time.

## Skills deliberately NOT claimed

- **`discrete-mathematics-binomial-coefficient`** and
  **`discrete-mathematics-how-to-compute-a-binomial-coefficient`** are **not claimed**, in either
  `standards[]` or `new_coverage[]`, despite being part of the concept sheet's originally proposed
  five-skill Combinatorics group. No deliverable in this case genuinely forces "n choose k."
  Candidate framings were considered and rejected:
  - Counting which subsets of character classes satisfy a "k of n classes required" composition
    rule (e.g. NIST-style "3 of 4 character types") — rejected because this case's policy does not
    impose a composition sub-rule; adding one only to manufacture a binomial-coefficient step would
    be exactly the "bolted on" case the write procedure warns against.
  - An audit-sampling deliverable computing C(N, k) for the number of possible k-account samples
    drawn from N flagged accounts — rejected under the forces test: a competent student can design
    and defend an account-review sample without ever computing the total count of possible
    samples; the audit practice does not depend on that number, so the mapping would be fake.
  - 2FA backup-recovery-code combinatorics — rejected; no genuine decision in this case turns on
    how many codes could be chosen from a pool.
  No forcing deliverable was found. Per `skills/case-write/SKILL.md` §"LEARNING GOAL CHECK", both
  skills are dropped rather than mapped falsely.

## Already-covered skills also exercised, not new

`measurement-how-to-convert-an-amount-with-compound-units` (n=6),
`advanced-numbers-how-to-find-the-percent-of-a-number` (n=24). Both already covered elsewhere in
the corpus; claimed here because D2/D4/D5 genuinely force them, not for coverage credit.

`discrete-mathematics-fundamental-counting-principle` (n=1) and
`discrete-mathematics-how-to-apply-the-fundamental-counting-principle-to-count-outcomes` (n=1) are
also already covered once each (both closed by a prior case) and are claimed here, not counted in
`new_coverage[]`, for the same reason.

## Gap group closed

`discrete-mathematics-pigeonhole-principle` — the sole skill in `new_coverage[]`, at `n = 0` in
`readmodel/standards_spine.json` at authoring time. This is the case's whole reason to exist per
SPEC §7: it is the first case in the corpus that genuinely forces the Pigeonhole Principle, via a
real, decision-relevant collision-bound calculation rather than a decorative example.
