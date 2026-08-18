# Concept sheet — Cryptography & Cybersecurity (`cryptography-security`)

Single-concept sheet, target pre-selected from `ROADMAP.md` §B4 item 7 ("Key-length decision").
Approved by the user's standing instruction to work Queue 1 in order.

**Rescope note.** ROADMAP's own note claims this domain "closes the entire Factoring group, 6/6" —
that estimate has partly collapsed since it was written: `basic-operations-greatest-common-factor`
and its how-to pair were absorbed by Plaza Pavers (this run), and `basic-operations-composite` was
already covered by the legacy case "Player Of The Year." Of the Factoring group's 6 skills, 3 remain
genuinely zero-coverage (`factor`, `prime`, `how-to-factor-a-number`). Combined with 3 more
zero-coverage signature skills from other groups (`number-sense-numbers-and-counting-digit`,
`number-sense-odd`, `discrete-mathematics-logical-statement`), this concept honestly closes 6 —
matching the queue's usual per-case count, even though the Factoring group itself is now only
half-closed rather than the originally-estimated 6/6.

### C1 — Key Length · tier T2

**Protagonist.** Elena Kowalski, a cybersecurity trainer building a hands-on "factor this practice
key" exercise for a company's security-awareness training session.

**The real math hook.** RSA-style public-key cryptography's security rests on a real, well-known
fact: multiplying two large primes is easy, but factoring the product back into its primes is hard
— and gets exponentially harder as the numbers grow (SEE APPENDIX A, real NIST source). Elena's
practice exercise uses two small, hand-factorable "toy" composite numbers (candidate moduli) so
trainees can experience real trial-division factoring themselves, the same core operation (in
miniature) that makes real key-breaking hard at scale.

**The dilemma.** Two candidate toy moduli exist for the exercise. A.) Candidate A (143 = 11×13,
needing 5 trial divisions to fully factor) OR B.) Candidate B (323 = 17×19, needing 7 trial
divisions). Elena wants a candidate whose difficulty — measured by how far a tester must search
before finding a factor (real math: only primes up to √N ever need testing) — lands close to a
target she's calculated from the session's real time budget. Neither candidate is exactly on
target; the dilemma is which one is *closer*.

**Would close (6 skills, all new zero-coverage):**

| id | kind | label |
|---|---|---|
| basic-operations-factor | vocab | Factor |
| basic-operations-prime | vocab | Prime |
| basic-operations-how-to-factor-a-number | how-to | How to factor a number |
| number-sense-numbers-and-counting-digit | vocab | Digit |
| number-sense-odd | vocab | Odd |
| discrete-mathematics-logical-statement | vocab | Logical Statement |

**Data feasibility: HIGH**, matching `domains.json`'s own grade. Real, verified source: NIST SP
800-57/800-131A's real security-strength figures for RSA-2048 (112-bit security, acceptable through
2030) and RSA-3072 (128-bit security, required beyond 2030) — real, HIGH confidence, grounding why
key length matters at all. The toy candidates' specific values are Elena's own authored exercise
data (no public database of specific training-exercise moduli exists, same convention as every
prior case's authored domain data). The real bits-to-decimal-digits conversion (`digits ≈
bits × log10(2)`) is standard, provable math, not requiring external citation, used to connect the
toy exercise to real-world key sizes.

**Sensitivity (SPEC §6).** None required — the stakes are a training-exercise design choice, not
personal loss or hardship.

**Split risk.** None — 6 skills, each with a genuinely distinct, motivated deliverable.

## Recommendation

Write C1 as specified — only concept on this sheet, pre-selected by queue order.
**Next step:** approved by queue order — proceed to `case-write`.
