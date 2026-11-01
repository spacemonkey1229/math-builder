# Guide Notes: The Cold Hit

MS/HS | Guide Notes | Adventure | 2026-27
**Tier:** T3 (MS-stretch / HS-entry) · **Primary metric:** cold-hit cases closed per detective-and-lab hour · **Margin:** 10.26% (fragile — see the sensitivity note before Lessons Learned)

**SPEC Section 6 flag:** this case touches wrongful accusation. Not a death/illness/family-hardship
stake, but real enough to name at the top of the room: "the math here is really a question about
what happens to someone who didn't do it."

---

## Intro

Heroes, Dana has one memo to write and a supervisor waiting on it. One policy is fast for everyone.
The other costs everyone a little time, every time, on purpose. There's no answer I'm holding back
from you — the DA's office doesn't have one either until they see Dana's numbers.

## Launch

Show a simple diagram: a cold-case DNA sample going into a search, and coming out the other side
with just a name and a number. Ask: *"If all you had was that — a name and a probability — would
you send someone to trial on it? What would you want to know first?"*

Let them argue it cold. Then: *"Dana's unit reviews a hit like this roughly once a week. She has to
pick ONE policy for the whole year — not case by case."*

> **Hero name — Refer on Match, or Hold for Corroboration? Commit out loud.**

---

## Anchor 1 — Take a stand and vote

Refer on Match (A) or Hold for Corroboration (B). No reasoning yet.

Hands up for A. Hands up for B. Write the split on the board.

*"Is anyone courageous enough to stand with ______?"*

## Anchor 2 — What is the problem we're solving?

Do **not** let them start calculating yet.

- What's the actual question, in one sentence?
- Is it "which policy is fair to the defendant"? Is it "which policy never lets a guilty person go"?
  Is it "which policy closes the most cases correctly per hour of investigator time"? **Those sound
  similar and are not the same question** — only the last one is what this case's numbers actually
  measure.
- Someone will say "obviously hold for corroboration, you can never be too careful." Push:
  *"Careful costs hours. Every hour spent double-checking a hit that was already correct is an hour
  not spent on the next cold case. Is 'never be too careful' actually free?"*
- Is that the right question?

> Let the confusion grow. Say it out loud: *"Huh — 'better safe than sorry' has a cost, and we
> haven't priced it yet."* Do not rescue them.

**The trap to let them walk into:** most learners will assume that because a coincidental DNA match
sounds astronomically unlikely, Policy A (refer immediately) is obviously fine and Policy B's extra
step is pure overhead with no real benefit. The real trap is that this specific hit came from a
*partial*, 8-locus profile — not a full 20-locus one — and the database searched has millions of
records in it. A learner who does D1 correctly but skips D2 (the database-size correction) will
badly underestimate how often a coincidental match like this one is expected to occur, and will not
understand why the case is close at all.

## Anchor 3 — What is the process?

- What's the process we'll go through to answer it?
- If we calculate "how unlikely is this exact match," are we done? Is that the same question as
  "how likely is at least one coincidental match somewhere in a database this size"?
- If we end up with two rates like 0.1225 and 0.1111 cases per hour, how do we decide that's close
  enough to be a real discussion, versus one policy just winning? What's our tiebreaker *before* we
  see the numbers?
- Is our question still the right question?

## Anchor 4 — What don't we know?

- What's missing that we'd need to answer this properly?
- Appendix F gives you the assumptions behind every non-probability figure — the caseload, the
  time costs. Do you believe them? **Have them actually try a bigger and a smaller version of each
  and see how much the comparison moves.**
- What are we assuming stays the same about *which kinds* of cold cases the unit reviews this year?
  (This is the case's built-in opening for the twist — don't tip it.)

---

## Data Deep Dive

Now the numbers. Work these on the board with them.

**Step 1 — RMP for the 8-locus partial profile (D1).** Per-locus match probability = 0.075.
RMP = 0.075⁸ ≈ **1.001 × 10⁻⁹** (about 1 in 1 billion) — treating each locus as an independent
event, so the probabilities multiply.

**Step 2 — database match probability, both search stages (D2).**
- Stage 1 (state, 3,368,310 profiles, no hit): DMP = 3,368,310 × 1.001×10⁻⁹ ≈ **0.00337** (about
  1 in 297).
- Stage 2 (national NDIS, 18,000,000 profiles, hit found here): DMP = 18,000,000 × 1.001×10⁻⁹ ≈
  **0.01802** (about 1 in 55.5).

**Push the room directly:** *"1 in 55 sounds a lot less impressive than 1 in a billion. Which
number is actually the right one to weigh this hit against?"* (Answer: the database one — the
1-in-a-billion figure answers "how unlikely is THIS exact profile," but the hit wasn't produced by
comparing one suspect to one profile; it was produced by searching 18 million.)

**Step 3 — cases closed per hour, both policies (D3).**

| Policy | Work | Hours |
|---|---|---|
| A — Refer on Match | 60 cases × 6 h base | 360 |
| A — Refer on Match | 0.649 expected false referrals × 200 h rework | ≈130 |
| **A total** | | **≈489.75 h → rate 0.1225/h** |
| B — Hold for Corroboration | 60 cases × 6 h base | 360 |
| B — Hold for Corroboration | 60 cases × 3 h corroboration | 180 |
| **B total** | | **540 h → rate 0.1111/h** |

**Refer on Match wins by 10.26%** — comfortably inside the 20% balance cap, but not by much.

---

## Twist — drop this at ~15 minutes into the discussion

Deliver it slowly. Let each piece land.

> *"New funding came through this morning."*
>
> (pause)
>
> *"A state grant, specifically for clearing the oldest, most degraded cases in the backlog —
> the ones everyone's been putting off because the evidence is in the worst shape."*
>
> (pause)
>
> *"Every single cold hit on this year's list is now a partial profile. Not 60% of them. All of
> them."*

**Facilitator only — read before you drop this, do not read aloud.** frac_partial rises from 0.6 to
1.0. Expected false referrals under Policy A rise from 0.649/year to **1.081/year**, raising Policy
A's total hours from 489.75 to **576.24** (rate drops to 0.1041/h). Policy B's total (540 h, rate
0.1111/h) is unaffected — corroboration is applied to every case either way. **The winner flips to
Hold for Corroboration, by 6.71%.** Confirm a room that gets there against these numbers, not just
the logic.

Now: **"Sixty seconds. Are you changing your recommendation — or not?"**

## Immediate recommit

- Who is **not** changing? Why?
- Who is reconsidering, even if they're not flipping?
- **What just broke in your original model?**
- **Were you wrong — or were you just missing information?** (Sit on this one.)
- Who built their case entirely on "a coincidental match is basically impossible" without ever
  running D2's database-size correction?

---

## Deep conflict — threads (20–30 min)

**Thread 1 — The prosecutor's fallacy, made concrete.** RMP tells you the probability of the
*evidence* if the person is innocent. It does not tell you the probability the person is innocent.
*"If someone told a jury '1 in a billion, so there's a 1-in-a-billion chance he's innocent' — what
exactly did they get wrong?"* Push toward: with an 18-million-profile database searched, the
relevant number isn't 1-in-a-billion, it's roughly 1-in-55 for *some* coincidental hit to occur
somewhere in that search — the search itself, not just the profile, changes what the evidence means.

**Thread 2 — Fragility to a single number.** Every one of the five caseload/cost figures (Appendix
F) is a disclosed assumption with no real public source behind it. Flex `h_corrob` or `h_rework` by
50% in either direction, and the winner flips (see case.json's sensitivity_disclosure — do not read
this section aloud, but use it to steer questions). *"Which policy would you defend to a department
head who asks 'what if corroboration actually only takes half the time you assumed?'"*

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. *"Thirty seconds — refer now, or hold?"* Two or three learners, fast. Stand/sit vote, no explanation yet. |
| **3:00–10:00** | Position defense (pre-twist). *"Convince us it's better, not just safer-sounding."* · *"What's your actual cases-per-hour rate — not a guess."* |
| **10:00–15:00** | Pressure-test the models. *"Which policy is more fragile to one wrong time estimate?"* · *"What single number does your policy depend on most?"* |
| **15:00** | **DROP THE TWIST.** Slowly, with pauses. Finish with: *"Sixty seconds. Are you changing your recommendation — or not?"* |
| **15:00–20:00** | Immediate recommit. Who reverses? *"What just broke?"* |
| **20:00–30:00** | The two threads: the prosecutor's fallacy made concrete · fragility to a single assumption. |
| **30:00–45:00** | Close, re-vote, reflection, lessons learned. |

---

## Close

- **Vote again.** Compare to the Anchor 1 board. Who moved?
- We asked ______ as our key question. Was it the right one?
- What math was new to you here, and how did you attack it?
- If you got a case like this again, what would you check first?

## Lessons Learned

The arithmetic has a clean structure: an independent-event product tells you how unlikely one exact
match is, and a database-size multiplication tells you how likely *some* coincidental match is
across an entire search — those are very different numbers, and the gap between them (1 in a
billion versus roughly 1 in 55) is the whole reason this case is close instead of obvious. Refer on
Match's win (10.26%) is real on this year's numbers, and it is also fragile — three of the five
underlying assumptions flip the winner or breach the SPEC balance cap at a plausible ±50% swing, and
a realistic shift in caseload composition (the twist) is enough to flip it for real. That is a
**disclosed, not eliminated** sensitivity — `case.json.sensitivity_disclosure[]` carries a
Category-F entry for every cost/caseload dial, because none of them can be tightened by more
research; they are genuine lab-operational unknowns no public source measures.

A facilitator running this room should say plainly what the case says: Refer on Match wins on the
numbers as modeled, that win is real, and it is also genuinely fragile to several disclosed
assumptions and to a realistic caseload shift — both things are true at once, and naming both is
stronger than picking one.

---

## Real-World Basis — read aloud only after the vote is closed

Dana Osei and her lab are fictional. The numbers problem she's facing is not — it happened, in a
real courtroom, with a real conviction on the line.

In 2008, John Puckett was convicted of a 1972 California murder on a DNA "cold hit" produced by
searching the state's database of 338,711 offender profiles. The prosecutor told the jury the match
had a 1-in-1.1-million chance of being coincidental — the raw per-profile random match probability.
What the jury was never told: once you account for the fact that the match came from searching
338,711 people rather than comparing one suspect to one profile, the odds of a coincidental match
turning up *somewhere* in that search were closer to **1 in 3**. That's the exact database-size
correction this case makes you compute in D2 — it's not a classroom simplification. It's
Recommendation 5.1 of the National Research Council's 1996 DNA forensic science report (the same
S6 source behind this case's Appendix C formula), left out of a real trial.

Puckett's conviction was upheld on appeal. The case remains a standard reference point in the
ongoing legal and statistical debate over how — and whether — cold-hit probabilities should be
explained to a jury. Tell the room: *"The math you just did isn't hypothetical. A jury got the
1-in-1.1-million number and not the 1-in-3 number, and it mattered."*

Sources: [Cold Case Hits Use Vastly Exaggerated DNA "Match" Statistics](https://www.prisonlegalnews.org/news/2009/jan/15/cold-case-hits-use-vastly-exaggerated-dna-match-statistics-8232upheld-by-california-supreme-court/) (Prison Legal News); [In DNA Numbers Game, Statistics Could Lead to False Convictions](https://thecrimereport.org/2008/05/08/in-dna-numbers-game-statistics-could-lead-to-false-convictions/) (The Crime Report); Roth, ["Safety in Numbers? Deciding When DNA Alone Is Enough to Convict"](https://www.marcellodibello.com/mathtrial/resources/RothDNA2010.pdf) (2010).

---

## Standards Touched On

**Independent Event · Permutation · Multistage Sampling · Convenience Sampling · Conditional
Probability · Population · Sample · Random · How to determine the number of outcomes of a
permutation · How to determine the number of outcomes of a combination · How to determine the
probability of conditional events · How to determine the probability of a compound event · How to
find the percent of a number.**

See `LEARNING_GOALS.md` for the forces-test and `case.json.reinforcement_note` for why
`new_coverage[]` is honestly empty (the live spine had zero true zero-coverage skills remaining at
write time; every claimed skill here is nonetheless genuinely thin, n between 2 and 9, except the
reinforcing percent-of-a-number skill).

---

## Facilitator note — sensitivity

SPEC Section 6 applies: this case's stakes are wrongful accusation via a coincidental DNA match —
real weight, framed as protection (avoiding a wrongful referral), not punishment. Flag this at the
top of the discussion, plainly and without dwelling on it.
