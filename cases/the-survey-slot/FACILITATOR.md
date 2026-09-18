# Guide Notes: The Survey Slot

MS | Guide Notes | Adventure | 2026-27
**Tier:** T3 (MS-stretch / HS-entry) · **Primary metric:** expected confirmed transit detections per hour of telescope time · **Margin:** 4.22% (very tight — see the sensitivity note before Lessons Learned)

---

## Intro

Heroes, Renee has one open telescope slot and four hours before the Moon washes it out. One option is a long stare at a single, already-suspicious target. The other is twelve short looks at brand-new fields. Neither is obviously right — I don't have the answer, and neither does Renee until the numbers are actually run.

## Launch

Show an image of a light curve with a single dip in it (a real one, e.g. TOI-700 d's, works). Ask: *"If you only had a few hours of telescope time left tonight, would you spend it confirming a signal you already suspect is real, or looking somewhere brand new?"*

Let them argue it cold, no numbers yet. Then: *"Renee has to submit one lane assignment before the committee's nightly sign-off closes. Same four hours, completely different bet on what they're worth."*

> **Hero name — which option do you run? Commit out loud.**

---

## Anchor 1 — Take a stand and vote

The Candidate Watch or The Twelve-Field Sweep. No reasoning yet.

Hands up for A (Candidate Watch). Hands up for B (Sweep). Write the split on the board.

*"Is anyone courageous enough to stand with ______?"*

## Anchor 2 — What is the problem we're solving?

Do **not** let them start calculating yet.

- What's the actual question, in one sentence?
- Is it "which option is more likely to find something"? Is it "which option makes the *best use of the four hours*"? **Those sound similar and are not the same question** — a option that's slightly less likely to succeed overall can still win on a per-hour basis if it uses the time more efficiently, and vice versa.
- Someone will say "twelve chances obviously beats one chance." Push: *"Twelve chances at what, exactly — and how do twelve small chances combine? Do they just add up?"*
- Is that the right question?

> Let the confusion grow. Say it out loud: *"Huh — that's not as obvious as it sounded a minute ago."* Do not rescue them.

**The trap to let them walk into:** most learners will take the Sweep's per-field probability (10%) and multiply it by 12, getting "120% chance of a detection" — and either not notice that's an impossible number (probabilities cannot exceed 100%), or wave it away as "basically certain." The real trap is that twelve *independent* small chances do not add; they compound by the complement rule (`P(at least one) = 1 - P(none)`), and the honest number (≈71.8%) is close to, but measurably below, The Candidate Watch's single-shot rate once both are converted to a fair per-hour comparison. A learner who does the naive multiplication will overstate the Sweep's real chances and misjudge which option is actually ahead — and it's much closer than either "obviously the sure thing" or "obviously more chances wins" suggests.

## Anchor 3 — What is the process?

- What's the process we'll go through to answer it?
- If we know the probability each option finds *something* tonight, are we done? Or do we need to account for the fact that both options use the exact same four hours?
- If we end up with two rates like 0.187 and 0.179 detections per hour, how do we decide that's close enough to be a real discussion, versus one option just winning? What's our tiebreaker *before* we see the numbers?
- Is our question still the right question?

## Anchor 4 — What don't we know?

- What's missing that we'd need to answer this properly?
- Appendix F gives you the assumptions behind every probability figure. Do you believe them? Neither the candidate's confirmation odds nor the Sweep's per-field rate is a number anyone has published for this exact situation — **have them actually try a higher and a lower version of each rate and see how much the comparison moves.**
- What are we assuming stays fixed about tonight's candidate between now and when the observation actually happens? (This is the case's built-in opening for the twist — don't tip it.)

---

## Data Deep Dive

Now the numbers. Work these on the board with them.

**Step 1 — The Candidate Watch's single-event probability (D2).** Appendix C states the candidate's confirmation probability at 74.8% (from Appendix A's real, published TESS TOI catalog rate, applied to tonight's candidate). Over the full 4-hour slot: rate_A = 0.748 ÷ 4 = **0.187 confirmed detections per hour.**

**Step 2 — The Sweep's compound probability (D1).** Twelve independent fields, each with a 10% chance of a new detection.

> **Do NOT let anyone report 12 × 10% = 120% as "the probability."** That's over 100% — a mathematical impossibility, and the trap named above. The correct approach uses the complement rule:
>
> P(at least one) = 1 − P(none) = 1 − (0.90)¹² = 1 − 0.2824 = **0.7176**

Over the full 4-hour slot: rate_B = 0.7176 ÷ 4 = **0.179 confirmed detections per hour.**

**Step 3 — compare (D3).** rate_A (0.187) vs. rate_B (0.179). **The Candidate Watch wins by 4.22%** — comfortably inside the 20% balance cap, but genuinely tight.

**Push the room directly:** *"The Sweep's raw success probability (71.8%) is actually LOWER than the Candidate Watch's (74.8%) even before dividing by time — so why is this even close?"* (Answer, if nobody gets there: both slots take the exact same 4 hours, so once you divide by time the comparison collapses to comparing the two raw probabilities almost directly — the "twelve chances" framing sounds like it should matter more than it actually does here, because compounding twelve *independent* small chances tops out well below certainty.)

**Step 4 — the write-up plan (D4).** Of the Sweep's 12 fields, 5 typically clear the automated significance test as preliminary flags (Appendix D) — a larger, noisier population than the ~1.2 that go on to actually survive the false-positive check per Step 2's math. The on-call analysis team can only fully write up and cross-check 2 of those 5 flags before the morning report is due.

- Number of possible 2-field subsets: C(5,2) = **10**
- Number of possible ordered write-up schedules for a chosen pair: P(5,2) = **20**

**Push the room:** *"There are 10 different pairs we could pick — why can't the team just write up all 5 and be done with it?"* (Answer: a small on-call team has a fixed number of working hours before a fixed morning deadline — a hard staffing/time limit, not a preference, same reason Marcus in The Manifest Split couldn't just run every container through both lanes at once. Also flag this trap if it comes up: D4's 5 preliminary flags are NOT the same population as Step 1's ~1.2 expected confirmed detections — most preliminary flags don't survive the false-positive check, exactly like Appendix A's real TESS catalog. D4 is a downstream staffing question, not a restatement of Step 1–3's detection math.)

---

## Twist — drop this at ~15 minutes into the discussion

Deliver it slowly. Let each piece land.

> *"40 minutes into the slot, the pipeline sends an alert."*
>
> (pause)
>
> *"An archival cross-match just flagged a faint background star sitting almost on top of the candidate's target star, in older survey images."*
>
> (pause)
>
> *"That's precisely the kind of blended background object that has turned real-looking dips into false positives before."*

**Facilitator only — read before you drop this, do not read aloud.** Note this twist deliberately changes the SAME quantity Appendix C/MA2 already defines — the probability the candidate survives the false-positive check — via a mechanism (a newly-discovered blended background object) that is exactly the failure mode Appendix A already names as a real cause of TESS false positives. It is not a scheduling/timing change; it is new evidence bearing directly on whether the signal is real. The candidate's confirmation probability drops from 74.8% to **55%**. Recompute: rate_A = 0.55 ÷ 4 = **0.1375** detections/hour — now *below* rate_B (0.179, unchanged, since the twist says nothing about the Sweep's fields, which are unrelated stars). **The winner flips to The Twelve-Field Sweep, by 30.47%.** Confirm a room that gets there against these numbers, not just the vibe — this is a real, computable flip driven entirely by the new contamination evidence, not a vaguely-worded "things changed" twist.

Now: **"Sixty seconds. Are you changing your recommendation — or not?"**

## Immediate recommit

- Who is **not** changing? Why?
- Who is reconsidering, even if they're not flipping?
- **What just broke in your original model?**
- **Were you wrong — or were you just missing information?** (Sit on this one.)
- Who built their case entirely on "a sure thing beats twelve long shots" without checking how thin that "sure thing" margin actually was?

---

## Deep conflict — threads (20–30 min)

**Thread 1 — The naive-multiplication trap and why it's wrong.** Twelve 10% chances do not add to 120%; they compound to about 71.8% by the complement rule. *"If twelve small independent chances don't just add up, what would make them add up instead of compound?"* Push toward: they'd add up (approximately) only if the chance of each field hitting were tiny enough that overlap is negligible — with a 10% per-field rate, that approximation breaks down fast, which is exactly why the honest calculation matters here.

**Thread 2 — Fragility to a single number.** Both MA2 (candidate confirmation probability) and MA3 (per-field detection rate) are disclosed assumptions with no directly-citable source for this exact situation — each is only *informed by* a real statistic (case.json's sensitivity_disclosure — do not read this section aloud, but use it to steer questions). *"Which option would you commit to if you had to defend it to the allocation committee, knowing either one of these two numbers could be off by a lot?"*

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. *"Thirty seconds — Candidate Watch or Sweep?"* Two or three learners, fast. Stand/sit vote, no explanation yet. |
| **3:00–10:00** | Position defense (pre-twist). *"Convince us it's better, not just louder."* · *"What's your option's actual rate — detections per hour, not just a probability."* |
| **10:00–15:00** | Pressure-test the models. *"Which option is more fragile to one wrong probability assumption?"* · *"What single number does your option depend on most?"* |
| **15:00** | **DROP THE TWIST.** Slowly, with pauses. Finish with: *"Sixty seconds. Are you changing your recommendation — or not?"* |
| **15:00–20:00** | Immediate recommit. Who reverses? *"What just broke?"* |
| **20:00–30:00** | The two threads: the naive-multiplication trap · fragility to a single assumption. |
| **30:00–45:00** | Close, re-vote, reflection, lessons learned. |

---

## Close

- **Vote again.** Compare to the Anchor 1 board. Who moved?
- We asked ______ as our key question. Was it the right one?
- What math was new to you here, and how did you attack it?
- If you got a case like this again, what would you check first?

## Lessons Learned

The arithmetic has a clean structure: an independent compound event does not add its parts, it
compounds them by the complement rule, and a rate (per hour of shared, fixed time) is the only fair
way to compare two options that use the same clock differently. The Candidate Watch's win (4.22%) is
real on tonight's numbers, and it is also fragile — both underlying probability assumptions flip the
winner or breach the SPEC balance cap at a plausible ±50% swing, and a small, realistic real-world
event (a background-contamination alert) is enough to flip it for real. That is a **disclosed, not eliminated**
sensitivity — `case.json.sensitivity_disclosure[]` carries a Category-F entry for both probability
dials, because neither can be tightened by more research; they are genuine astronomical unknowns that
no public source measures for this exact situation.

A facilitator running this room should say plainly what the case says: The Candidate Watch wins on
the numbers as modeled, that win is real, and it is also genuinely fragile to two disclosed
assumptions and to a realistic real-world update — both things are true at once, and naming both is
stronger than picking one.

---

## Standards Touched On

**Independent Event · Permutation · Standard Notation · How to determine the number of outcomes of a
combination · How to determine the number of outcomes of a permutation · How to write a number in
standard notation given its scientific notation.**

Reinforced: Combination · Theoretical Probability · Experimental Probability · Scientific Notation ·
How to determine the probability of a compound event.

See `LEARNING_GOALS.md` for the forces-test and `case.json`'s `new_coverage[]` for the live spine
check confirming all six targeted skills were genuinely still thin (n=2) at write time.

---

## Facilitator note — sensitivity

No SPEC Section 6 subject-matter sensitivity applies. This is a scheduling/resource-allocation
decision with no death, illness, or family-hardship stakes.
