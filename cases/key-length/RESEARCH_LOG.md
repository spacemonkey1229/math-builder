# Research Log — Key Length

Sourced 2026-08-12, `case-research`.

## S1 — RSA-2048 and RSA-3072 real NIST security-strength figures

**Claim:** RSA-2048 provides 112-bit security, acceptable for new use through 2030; RSA-3072
provides 128-bit security, required for new use after 2030.
**Source:** NIST Special Publication 800-131A Revision 2, "Transitioning the Use of Cryptographic
Algorithms and Key Lengths" —
https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf
**Accessed:** 2026-08-12. **Confidence:** HIGH.
**Note:** Cross-checked against NIST SP 800-57's own security-strength table before use; both
sources agree on the 112-bit/128-bit figures and the 2030 transition date. This grounds Appendix
A's real-world motivation for why key length matters at all, and feeds D5's real digit-count
computation (617 / 925 decimal digits for 2048-bit / 3072-bit, via the standard `digits ≈
bits × log10(2)` conversion — a provable math fact, not requiring its own citation).

## Modeling assumptions (not sourced — see Appendix D)

- **MA1 — Elena's target difficulty (√N = 15.2 = 15.05 base + a 0.15 calibration buffer).**
  Derived from the session's stated real time budget for this exercise segment; the 0.15 buffer
  represents genuine trainer-side uncertainty about trainee testing speed. Swept ±50% on the buffer
  (effective target 15.125-15.275) in Tier 2 probe 5: margin holds 10.09%-18.68%, Candidate B stays
  the winner throughout.
- **MA2 — Candidate A (143) and Candidate B (323).** Output by Elena's own practice key-generator
  tool for this specific exercise — no public database of real training-exercise moduli exists
  (same convention as every prior case's authored domain data: Cold Chain's route, Plaza Pavers'
  border cut, Vent Cap's nesting result, Apron Order's marker layout, Survey Corner's field notes,
  Field Watch's satellite readings).

## Search methodology

Direct WebSearch verification of S1 against two independent NIST publications (SP 800-131A Rev 2
and SP 800-57) on 2026-08-12, same day as authoring — both reachable, both figures confirmed
present and mutually consistent. A separate search for real OpenSSL RSA-2048-vs-3072 throughput
benchmarks was conducted during design exploration but not used in the final case — the real
performance gap (roughly 2-5x depending on operation) proved too large to support a genuinely close,
balanced A/B dilemma (SPEC §2's ~20% cap), so the case's primary metric uses the toy-exercise
difficulty-matching framing instead, which is what the target skills (factor, prime, digit, odd,
logical-statement) genuinely force in the first place. No figure in this case is fabricated: every
number is either traced to S1, is the exercise's own authored/generator-output data (MA2, explicitly
disclosed), is an explicitly disclosed modeling assumption with basis and sensitivity (MA1), or is
arithmetic/standard math derived from those inputs (`case.json.derived`, `sensitivity_model.py`).
