Case Study: Key Length
MS | Math | Case Study | 2026-27 | Heroes Academy

## Overview

Elena Kowalski has forty minutes, a whiteboard, and a room full of employees who think
cybersecurity training is going to be boring. She is about to prove them wrong with two numbers.

Every time someone logs into a bank, a hospital portal, or a company's internal system, a real
mathematical fact is quietly doing the work of keeping that connection private: multiplying two
huge prime numbers together is fast, but taking the result apart again — factoring it back into
those two primes — is so slow it can take longer than a human lifetime, even on a fast computer,
once the numbers get big enough. That gap between "easy one way, brutal the other way" is the whole
reason online security works at all.

Elena cannot hand a room of trainees a real key-sized number — nobody is factoring anything close
to that by hand in a forty-minute session. So she has built two small, honest stand-ins: two
numbers, each one built the exact same way real keys are, each one crackable by hand if a trainee
is patient enough. The exercise only works if the number is hard enough to feel real, but not so
hard the room gives up before the lesson lands.

She has two candidates on her desk. Only one of them is going on the slide tomorrow morning.

## Background

Elena Kowalski is a cybersecurity trainer designing a hands-on "factor this practice key" exercise
for a company's security-awareness training session. The exercise is built on a real fact: modern
public-key cryptography (like RSA) generates a key by multiplying two large prime numbers together,
and the entire security of the system depends on the fact that multiplying is fast but factoring the
result back apart is slow — and gets dramatically slower as the numbers grow larger (SEE APPENDIX A).

For training purposes, Elena needs small, hand-factorable numbers that still demonstrate the real
process: a trainee tests candidate prime divisors, one at a time, until a factor is found — and a
real, provable fact from number theory means nobody ever needs to test past the square root of the
number being factored, because if no factor exists below that point, none exists at all (SEE
APPENDIX B).

Two candidate practice numbers exist. **Candidate A** is 143. **Candidate B** is 323. Elena has
worked out, from the session's real time budget, roughly how much searching she wants the exercise
to demand — not so little that it feels trivial, not so much that trainees give up before the
lesson lands (SEE APPENDIX C). Whichever candidate's actual difficulty lands closer to that target
is the one that goes on tomorrow's slide.

All figures in this case are sourced in APPENDIX E, or stated as explicit modeling assumptions in
APPENDIX D where no public figure exists. The vocabulary and the "how to…" skills this case will ask
of you are listed in APPENDIX G — that is where Challenge 1 sends you. Curious how far this idea goes
beyond tomorrow's training session? SEE APPENDIX F for further reading.

## Dilemma

You are Elena Kowalski.
Do you:
A.) Use Candidate A (143) for tomorrow's exercise OR
B.) Use Candidate B (323) for tomorrow's exercise

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. Factor Candidate A completely: list every prime you test, in order, until you find
    Candidate A's two prime factors. Report how many primes you had to test.
    D2. Factor Candidate B completely, the same way. Report how many primes you had to test.
    D3. Both of Candidate A's and Candidate B's prime factors are odd numbers. Explain why a
    candidate built this way (as the product of two primes, neither of which is 2) can never be an
    even number.
    D4. Evaluate this statement: "If a number is odd, it is safe to use as key material." Is it
    true or false? Use one of your own results from D1 or D2 to justify your answer.
    D5. A real key isn't 143 or 323 — it's hundreds of digits long. Using the fact that a number
    with `b` bits has about `b × 0.30103` decimal digits, find how many decimal digits a real
    2048-bit key and a real 3072-bit key each have (SEE APPENDIX A).
    D6. Find the square root of Candidate A and the square root of Candidate B, then find how far
    each one is from Elena's target difficulty (SEE APPENDIX C).
    D7. The verdict: using D6's two distances, find the percentage margin between them — the
    larger distance minus the smaller distance, divided by the larger distance — and recommend
    which candidate Elena should use.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — Why Key Length Matters

| | Value |
|---|---|
| RSA-2048 security strength | 112 bits — acceptable for new use through 2030 [S1] |
| RSA-3072 security strength | 128 bits — required for new use after 2030 [S1] |
| Approx. decimal digits in a real 2048-bit / 3072-bit modulus | SEE CHALLENGE D5 |

Real public-key cryptography's security depends entirely on how hard the underlying number is to
factor — which is exactly what this exercise's trial-division process demonstrates, at a scale a
human can actually do by hand.

## Appendix B — Why You Only Test Up To the Square Root

If a number `N` has no factor at or below its own square root, it cannot have any factor at all
(other than 1 and itself) — because any factor pair `p × q = N` must have at least one of `p` or
`q` at or below √N. This is why Elena's exercise design uses √N as the real measure of "how far a
trainee has to search."

## Appendix C — The Target Difficulty

| | Value |
|---|---|
| Elena's target √N for this exercise | 15.2 — SEE APPENDIX D, MA1 |
| Candidate A (143) | √143 ≈ 11.96 — SEE CHALLENGE D6 |
| Candidate B (323) | √323 ≈ 17.97 — SEE CHALLENGE D6 |

## Appendix D — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, each with a real basis named below. A Hero may challenge them in discussion — that is a
> legitimate move, and Appendix G names the skill a Hero would need to test one.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Elena's target difficulty (√N) for the exercise | **15.2** (15.05 base + a 0.15 calibration buffer) | Derived from the session's real time budget for this exercise segment; the 0.15 buffer represents Elena's own uncertainty about how quickly a typical trainee tests each candidate divisor. | Directly load-bearing. The 0.15 buffer flexed ±50% in Tier 2 probe 5 (effective target 15.125-15.275): margin ranges 10.09%-18.68%, Candidate B stays the winner throughout. |
| MA2 | Candidate A (143) and Candidate B (323) themselves | See Appendix C | Output by Elena's practice key-generator tool for this specific exercise — no public database of real training-exercise moduli exists (same convention as every prior case's authored domain data). | Not swept in Tier 2 probe 5 (generator-output exercise data, not a stated numeric flex-eligible dial). |

## Appendix E — Sources

| id | Claim | Value | Source | Accessed | Confidence |
|---|---|---|---|---|---|
| S1 | RSA-2048's and RSA-3072's real NIST-defined security strength and use-through dates | RSA-2048 = 112-bit security, acceptable through 2030; RSA-3072 = 128-bit security, required after 2030 | NIST, Special Publication 800-131A Revision 2, "Transitioning the Use of Cryptographic Algorithms and Key Lengths" ([link](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf)) | 2026-08-12 | HIGH |

## Appendix F — Learn More

These are real, freely available resources for a curious Hero who wants to go beyond the math
required for this case. None of this is required for the Challenges above.

- [Khan Academy, "RSA encryption: Step 1"](https://www.youtube.com/watch?v=EPXilYOa71c) — the first video in Khan Academy's "Journey into cryptography" series, walking through why RSA needs the "easy one way, hard the other way" trick that Appendix A describes.
- [Computerphile, "Prime Numbers & RSA Encryption Algorithm"](https://www.youtube.com/watch?v=JD72Ry60eP4) — a short video from the Computerphile channel explaining, in plain terms, how large prime numbers become the foundation of RSA encryption.
- [Wikipedia, "Sieve of Eratosthenes"](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) — an article on the classic ancient algorithm for finding every prime number up to a given limit, a faster relative of the trial-division search Challenges D1 and D2 ask you to do by hand.
- [NIST, "Cybersecurity Starts with Your Employees"](https://www.nist.gov/blogs/manufacturing-innovation-blog/cybersecurity-starts-your-employees) — a NIST blog post making the real-world case for exactly the kind of employee security-awareness training Elena is running in this case.

## Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Factor
- Prime
- Digit
- Odd
- Logical Statement

**"How to…" questions**

- How to factor a number
- How to evaluate an absolute value expression
- How to find the percent of a number

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
