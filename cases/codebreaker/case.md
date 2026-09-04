# Case Study: Codebreaker

MS | Math | Case Study | 2026-27 | Heroes Academy

---

## Overview

3:14 AM. James Charmichael circles Rieterpark for the third time, breath fogging in the cold, before he lets himself sit. The bench is empty except for a man in a dark coat who adjusts his hat, sets a book on his lap — the two signals, both correct. Klaus Muller, in person, for the first time in six months of dead drops (hidden handoffs — an item left somewhere for the other person to collect later, so the two of them are never seen together) and forum handles.

"Here are the photographs," Klaus says, sliding a manila envelope down the bench without looking at him.

"We cannot be too careful," Charmichael replies, tucking it into his coat. "We're being watched. From now on, handwritten only. There's a man on Bahnhofstrasse who sleeps near the tram stop — when you have something, put it in a coffee cup and leave it with him."

Klaus's hand is shaking slightly. He's not a professional. He's a name in a terror cell's back office who decided, six months ago, to start talking to a stranger on the dark web (parts of the internet not indexed by ordinary search engines and reachable only with special software, often used to communicate anonymously), and every message since has been a small bet that no one is reading over his shoulder.

Charmichael stands to leave. "We need to write in code."

"What code?"

He doesn't answer yet. He has two, and only one of them is right for a man like Klaus.

---

## Background

James Charmichael — Agent 008, British Secret Service — has spent four years working to dismantle a terrorist cell headquartered in Berlin. Klaus Muller, his source inside the organization, has fed him intelligence for six months and has become reliable enough that Charmichael now wants to lean on him harder, which means putting more of Klaus's own safety on the line.

Charmichael is fluent in dozens of hand ciphers and can decode most of them in his head. Klaus is not. Klaus has never been trained in espionage, has no cryptography background, and every message he sends will sometimes be time-sensitive — a schedule, a name, a location that stops mattering in a matter of hours. Charmichael has to pick a cipher Klaus can actually execute correctly, by hand, under pressure, without ever having practiced it — while assuming the cell may eventually recognize *that* a cipher is in use, even if they don't have the key (**SEE APPENDIX D**, Kerckhoffs's Principle).

London has been explicit about what this particular decision is judged on. In the cable authorizing Charmichael to lean harder on Klaus, his handler put it in writing: the failure mode that ends this operation is a message that arrives *wrong*, not a message that is *eventually guessed*. Klaus has no way to know he has miscopied a character, and no way to ask for a resend without risking another face-to-face contact — precisely the kind of contact they are trying to eliminate by moving to handwritten codes at all. A cipher's resistance to a single blind guess only matters against an adversary who is actually guessing; in six months of drops, none has. What London has asked Charmichael to optimize, in writing, is the probability that Klaus's handwritten cipher text reaches him with zero errors — not how many keys a cipher theoretically has.

Two ciphers are on the table:

- **The Alphanumeric Cipher** — every letter is assigned a fixed number 1–26, that number is multiplied by a secret multiplier, and the results are written as digit strings separated by zeros (**SEE APPENDIX A**).
- **The Circle Shift Cipher** — the plaintext is rewritten starting from its first vowel, reading every third letter and wrapping around the message until every letter has been used once (**SEE APPENDIX B**).

Both ciphers must be able to encode the same two messages Charmichael needs to send Klaus this month (**SEE APPENDIX C**). The rules for counting how much Klaus actually has to write — and how likely he is to write it correctly — and for counting each cipher's keyspace, are fixed conventions (**SEE APPENDIX D**) — use them, or your numbers won't match anyone else's. Optional further reading is in **Appendix E**.

The vocabulary and "how to…" skills this case will ask of you are listed in **Appendix F** — that is where Challenge 1 sends you.

---

## Dilemma

You are James Charmichael, Agent 008.

Do you:

**A.)** Encrypt your communications with Klaus using the Alphanumeric Cipher **OR**

**B.)** Encrypt your communications with Klaus using the Circle Shift Cipher

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following. **Work the deliverables in this order** — D4's character counts feed directly into D7, so compute them first. D1–D3 and D7 answer two different questions: D1–D3 ask how hard each cipher is to guess in a single blind try; D7 asks how likely Klaus is to actually execute the cipher correctly, by hand, under pressure, the first time. Both are real numbers a Hero has to compute. D8 asks you to decide, explicitly, which one should govern this specific decision — don't let whichever number you compute first, or whichever one looks bigger, make that call for you by default.

- **D4 — Both required messages, encoded in your chosen cipher** (Appendix C), plus a bar graph comparing the total number of characters Klaus must correctly handwrite for each cipher, across both messages.
- **D5 — A pie chart** showing, for the Alphanumeric Cipher, what share of every character Klaus writes is a "0" separator versus a digit of an actual letter value.
- **D6 — A histogram** of how often each digit 0–9 appears across your two Alphanumeric-encoded messages. Using the Pigeonhole Principle and your total digit count, state the minimum number of times *some* digit must repeat — and confirm your histogram is consistent with it.
- **D7 — The probability Klaus correctly transcribes an entire cipher text with zero character errors**, for each cipher, using Appendix D's stated per-character error rate.
- **D1 — The Alphanumeric Cipher's keyspace.** If the terror cell recognized the cipher type but not the letter-to-number key, how many possible keys are there with no multiplier? How many with an unknown single-digit multiplier? Show your factorial and write both answers in scientific notation.
- **D2 — The Circle Shift Cipher's keyspace.** If the terror cell recognized the cipher type but not the number of letters skipped, how many possible keys are there for each of the two messages in Appendix C?
- **D3 — Blind-guess probability.** What is the probability a single random guess lands on the exact correct key, for each cipher, expressed in scientific notation where useful?
- **D8 — A recommendation** weighing each cipher's keyspace, error-free transcription probability, and how much Klaus has to correctly handwrite by hand, under time pressure, with no training. London's stated standard for this decision (Background) is the probability that Klaus's cipher text reaches Charmichael with zero errors — not how many keys a cipher has. **Given that stated standard, state explicitly which single number — D3's blind-guess probability or D7's zero-error transcription probability — actually answers the question London asked, and why the other one, while real, doesn't govern this specific decision.**

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A: The Alphanumeric Cipher

Assign each letter of the alphabet a unique value 1–26:

| Letter | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Value | 20 | 17 | 4 | 8 | 10 | 22 | 11 | 16 | 14 | 1 | 9 | 3 | 12 | 23 | 15 | 5 | 25 | 7 | 13 | 2 | 21 | 18 | 26 | 24 | 6 | 19 |

**To encrypt:** multiply each letter's value by a secret single-digit multiplier. Write each letter's resulting number in order. Between each pair of consecutive letters, write a `0`. Do not write spaces.

**Worked example (multiplier = 2):**

Plain text: `NEED EXTRACTION NOW`
Cipher text: `46020020016020048040140400804028030046046030052`

*(Verified digit-by-digit against the rule above and the letter table's own values — see Appendix D and `legacy_conversion_note` in `case.json` for one other worked example from the original 2020 handout that did NOT reproduce correctly when re-derived from this same rule, and was dropped rather than guessed at.)*

---

## Appendix B: The Circle Shift Cipher

**To encrypt:** find the first vowel in the plain text. Starting there, write every third letter, circulating back to the beginning of the message each time you reach the end, until every letter (and space) has been written exactly once. Write spaces as `_`.

**Worked example:**

Plain text: `MISSION COMPROMISED`
Cipher text: `ii_mosmsnoridsocpme`

Plain text: `NEED EXTRACTION NOW`
Cipher text: `e_tconndxai_weertno`

---

## Appendix C: The Two Required Messages

Charmichael needs Klaus able to receive both of these messages, in whichever cipher is chosen:

1. `Your brothers are alive`
2. `Your wife is a double agent`

---

## Appendix D: Modeling Assumptions and Conventions

These four conventions split into two groups that answer two different questions. Convention 1
tells you how to count each cipher's *keyspace* — how many keys an adversary would have to
search to break a single message by brute force (feeds D1–D3). Conventions 2 and 4 tell you how
to count what Klaus has to *write* and how often he might get a character wrong — feeding D4–D7's
picture of whether he can execute the cipher correctly the first time, under pressure, with no
training. Convention 3 is a shared modeling detail both tracks need for their worked examples.
Neither group's numbers is automatically bigger, more real, or more decisive than the other's —
D8 asks you to weigh them against each other yourself; this appendix doesn't do that weighing for
you.

**Convention 1 — Keyspace counting.** "How many possible keys" is counted from the terror cell's point of view under **Kerckhoffs's Principle**: they know *which* cipher type is in use (Alphanumeric vs. Circle Shift) but not the specific key (the letter-to-number assignment and multiplier, or the number of letters skipped). This is the standard cryptographic assumption that a cipher's security should not depend on the *algorithm* staying secret — only the key. (Wikipedia, "Kerckhoffs's principle" — Appendix E, Source 5.)

- Alphanumeric key = a unique assignment of the numbers 1–26 to the 26 letters (a permutation of 26 items), times an unknown single-digit multiplier (1–9).
- Circle Shift key = the number of letters skipped between each written character. For a message (including spaces) of length *n*, the skip can be any whole number from 1 to *n* − 1 (a skip of 0 or *n* does nothing).

**Convention 2 — Counting handwritten characters.** For D4/D5/D6, count every character Klaus must physically write:
- Alphanumeric: every digit of every letter's multiplied value, plus every `0` separator written *between* consecutive letters (none after the last letter). Spaces in the plaintext are not encoded and are not written.
- Circle Shift: every output character, including underscores for spaces — the cipher text is exactly as long as the plaintext (letters + spaces).

**Convention 3 — Multiplier for worked examples.** Where a specific multiplier is needed for a worked example (Appendix A) or for D4–D6, use multiplier = 2. The actual multiplier Charmichael and Klaus agree on in the field is a secret between them — this case only needs *a* representative value to make the deliverables computable, exactly the way Cold Chain and Cardiology fix a modeling convention when the source material doesn't hand you one.

**Convention 4 — Transcription error rate (Modeling Assumption).** For D7, assume Klaus has a 0.15% (0.0015) probability of miswriting any single character — a digit, letter, or separator — when copying a cipher text by hand under field conditions (low light, time pressure, no training). This is a stated scenario assumption, not a researched or sourced figure: no external source gives a real handwriting-under-duress error rate for this specific situation, and this case does not claim one. The probability the *entire* message transcribes with zero errors is (1 − 0.0015) raised to the power of the total character count from Convention 2.

---

## Appendix E: Optional Sources to Learn More

1. Khan Academy — [Cryptography](https://www.khanacademy.org/computing/computer-science/cryptography) (course overview)
2. Khan Academy — [Intro to Cryptography](https://www.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/a/intro-to-cryptography)
3. Math Is Fun — [Combinations and Permutations](https://www.mathsisfun.com/combinatorics/combinations-permutations.html)
4. Wikipedia — [Frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis)
5. Wikipedia — [Kerckhoffs's principle](https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle)

*(The original 2020 handout's Guardian and Exploratorium links no longer resolve — see `legacy_conversion_note` in `case.json`. Replaced with the five links above, each confirmed live on 2026-08-13.)*

---

## Appendix F: "How To…" Math Questions To Research

**Vocabulary**

Standard Notation · Scientific Notation · Factorial · Permutation · Event · Outcome · Probability · Histogram · Pie Chart · Bar Graph · Data · Multiplication · Product · Addition · Sum · Pigeonhole Principle

**How to…**

- How to write a number in scientific notation given its standard notation
- How to evaluate a factorial expression
- How to determine the number of outcomes of a permutation
- How to determine the probability of a single event
- How to create a histogram given a set of data
- How to create a pie chart given a set of data
- How to multiply single-digit numbers
- How to multiply 2-digit numbers by single-digit numbers
- How to add 2-digit numbers
- How to compare two or more values
