# Guide Notes: The Manifest Split

MS | Guide Notes | Adventure | 2026-27
**Tier:** T2 (MS-core) · **Primary metric:** containers cleared per inspector-hour · **Margin:** 11.26% (fragile — see the sensitivity note before Lessons Learned)

---

## Intro

Heroes, Marcus has one lane decision and four hours before cutoff. One option is simple and never needs to move a container twice. The other is faster per check but sometimes has to move a container across the yard mid-inspection. There's no lane I'd pick either — I don't have the answer, Marcus's terminal manager doesn't either until she sees the numbers.

## Launch

Show a photo or diagram of a container yard with two inspection lanes side by side. Ask: *"If you ran this yard tonight, would you rather have one lane that does everything, or two lanes that each do one thing really well?"*

Let them argue it cold, no numbers yet. Then: *"Marcus has to commit to one lane setup before the shift locks in. Same containers, same cutoff, completely different bet on how the work gets split."*

> **Hero name — which lane do you run? Commit out loud.**

---

## Anchor 1 — Take a stand and vote

The Combined Lane or The Split Lanes. No reasoning yet.

Hands up for A (Combined). Hands up for B (Split). Write the split on the board.

*"Is anyone courageous enough to stand with ______?"*

## Anchor 2 — What is the problem we're solving?

Do **not** let them start calculating yet.

- What's the actual question, in one sentence?
- Is it "which lane checks containers fastest per container"? Is it "which lane never has to move a container twice"? Is it "which lane clears the whole flagged pool with the fewest total inspector-hours"? **Those sound similar and are not the same question** — only the last one is what Marcus's shift actually gets measured on.
- Someone will say "obviously split them, specialists are always faster." Push: *"Faster at what, exactly? Faster per check, or faster to clear the whole pool tonight?"*
- Is that the right question?

> Let the confusion grow. Say it out loud: *"Huh — that's not as obvious as it sounded a minute ago."* Do not rescue them.

**The trap to let them walk into:** most learners will assume that because only a small slice of tonight's flagged containers are dual-flagged (25 out of 195 — about 13%), the re-handling cost in The Split Lanes must be a minor detail that can't possibly outweigh two specialist crews working faster on every single check. The real trap is that the intersection is exactly where the two plans' fates are decided — a 13% slice earns its overlap being counted *twice* in Split Lanes' cost column (once per lane, plus the re-handle), and that's enough to erase most of the specialist speed advantage on tonight's numbers. A learner who dismisses the intersection as "too small to matter" without actually running D2's arithmetic will misjudge which lane is really ahead — and it's much closer than the "specialists are always faster" instinct suggests.

## Anchor 3 — What is the process?

- What's the process we'll go through to answer it?
- If we just add up how many hazmat checks and how many reefer checks happen, are we done? Is that the same as counting how many *distinct containers* get cleared tonight?
- If we end up with two rates like 7.18 and 7.99, how do we decide that's close enough to be a real discussion, versus one lane just winning? What's our tiebreaker *before* we see the numbers?
- Is our question still the right question?

## Anchor 4 — What don't we know?

- What's missing that we'd need to answer this properly?
- Appendix D gives you the assumptions behind every timing figure. Do you believe them? None of the five per-container check times are pulled from a real published number for this exact kind of terminal check — **have them actually try a faster and a slower version of each time and see how much the comparison moves.**
- What are we assuming stays the same about tonight's flagged pool between now and when the crew actually finishes? (This is the case's built-in opening for the twist — don't tip it.)

---

## Data Deep Dive

Now the numbers. Work these on the board with them.

**Step 1 — find the intersection (D1).** H = 90, R = 130, H ∪ R = 195 (read directly off the gate-scan log). By inclusion-exclusion: |H ∩ R| = |H| + |R| − |H ∪ R| = 90 + 130 − 195 = **25**. Draw the Venn diagram: H-only = 65, R-only = 105, both = 25.

**Step 2 — total inspector-minutes per configuration (D2).**

| Configuration | Work | Minutes |
|---|---|---|
| The Combined Lane | 90 hazmat checks × 8 min | 720 |
| The Combined Lane | 130 reefer checks × 7 min | 910 |
| **The Combined Lane total** | | **1,630 min = 27.17 inspector-hours** |
| The Split Lanes | 90 hazmat checks × 6 min | 540 |
| The Split Lanes | 130 reefer checks × 5 min | 650 |
| The Split Lanes | 25 re-handles × 11 min | 275 |
| **The Split Lanes total** | | **1,465 min = 24.42 inspector-hours** |

**Step 3 — containers cleared per inspector-hour (D3).** Both configurations clear the same 195 distinct containers (the union — do not let anyone add 90 + 130 = 220 here; that double-counts the 25 in both sets).

- The Combined Lane: 195 ÷ 27.17 = **7.18** containers/inspector-hour
- The Split Lanes: 195 ÷ 24.42 = **7.99** containers/inspector-hour

**The Split Lanes wins by 11.26%** — comfortably inside the 20% balance cap.

**Push the room directly:** *"Only 25 of 195 containers are dual-flagged. Why does that 13% slice decide the whole comparison?"* (Answer, if nobody gets there: those 25 containers are the *only* place the two configurations' cost structures actually differ in kind — Combined Lane pays a small per-container speed tax on all 195 containers, Split Lanes pays a chunky one-time re-handle tax on just the 25. Whichever tax adds up to more, wins.)

---

## Twist — drop this at ~15 minutes into the discussion

Deliver it slowly. Let each piece land.

> *"It's 11:15pm. Compliance calls."*
>
> (pause)
>
> *"New bulletin, effective tonight: refrigerated shipments of lithium-ion cells now require hazmat placarding too — not just a reefer flag."*
>
> (pause)
>
> *"Your crew re-checks the reefer set. Thirty of those containers are lithium-ion cell shipments. They're hazmat-flagged now."*

**Facilitator only — read before you drop this, do not read aloud.** Those 30 containers were already inside R (reefer-flagged); they now also join H. Because they were already counted in the union, the union stays at 195 — but H rises from 90 to 120, and by inclusion-exclusion the intersection jumps from 25 to **55**. Re-run Step 2 and Step 3: Combined Lane total becomes 8(120)+7(130) = 1,870 min = 31.17 hours, rate 195/31.17 = **6.26**. Split Lanes total becomes 6(120)+5(130)+11(55) = 1,975 min = 32.92 hours, rate 195/32.92 = **5.92**. **The Combined Lane now wins, by 5.61%** — the winner flips. Confirm a room that gets there against these numbers, not just the logic — this is a real, computable flip driven entirely by the intersection growing past its crossover point (x = 40, for tonight's H+R), not a vaguely-worded "things changed" twist.

Now: **"Sixty seconds. Are you changing your lane assignment — or not?"**

## Immediate recommit

- Who is **not** changing? Why?
- Who is reconsidering, even if they're not flipping?
- **What just broke in your original model?**
- **Were you wrong — or were you just missing information?** (Sit on this one.)
- Who built their case entirely on "specialists are always faster" without ever checking how the intersection was sized?

---

## Deep conflict — threads (20–30 min)

**Thread 1 — Specialization vs. the hidden double cost.** The Split Lanes' crews are faster at every individual check, and still lose once the intersection is large enough. *"If specialists are faster at everything, why does the combined lane ever win?"* Push toward: the intersection is checked *and moved* under Split Lanes, but only checked once under Combined — specialization only pays off on the containers that never cross between lanes.

**Thread 2 — Fragility to a single number.** Every one of the five per-container timing figures (Appendix D) is a disclosed assumption with no real public source behind it. Flex any single one by 50% in either direction, and the winner either flips or the margin blows past the 20% balance cap (see case.json's sensitivity_disclosure — do not read this section aloud, but use it to steer questions). *"Which lane would you commit to if you had to defend it to a terminal manager who might ask 'what if the reefer check actually takes six minutes, not five?'"*

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. *"Thirty seconds — Combined or Split?"* Two or three learners, fast. Stand/sit vote, no explanation yet. |
| **3:00–10:00** | Position defense (pre-twist). *"Convince us it's better, not just louder."* · *"How many containers does your lane clear per inspector-hour — the actual rate, not a guess."* |
| **10:00–15:00** | Pressure-test the models. *"Which lane is more fragile to one wrong timing assumption?"* · *"What single number does your lane depend on most?"* |
| **15:00** | **DROP THE TWIST.** Slowly, with pauses. Finish with: *"Sixty seconds. Are you changing your lane — or not?"* |
| **15:00–20:00** | Immediate recommit. Who reverses? *"What just broke?"* |
| **20:00–30:00** | The two threads: specialization vs. the hidden double cost · fragility to a single assumption. |
| **30:00–45:00** | Close, re-vote, reflection, lessons learned. |

---

## Close

- **Vote again.** Compare to the Anchor 1 board. Who moved?
- We asked ______ as our key question. Was it the right one?
- What math was new to you here, and how did you attack it?
- If you got a case like this again, what would you check first?

## Lessons Learned

The arithmetic has a clean structure: a union tells you how many distinct things you actually have,
and an intersection tells you exactly where two competing plans' cost structures genuinely differ.
The Split Lanes' win (11.26%) is real on tonight's numbers, and it is also fragile — every one of
the five timing assumptions behind it flips the winner or breaches the SPEC balance cap at a
plausible ±50% swing, and a small, realistic reclassification (30 containers, out of 195) is enough
to flip it for real. That is a **disclosed, not eliminated** sensitivity — `case.json.sensitivity_disclosure[]`
carries a Category-F entry for every timing dial, because none of them can be tightened by more
research; they are genuine terminal-operational unknowns no public source measures.

A facilitator running this room should say plainly what the case says: The Split Lanes wins on the
numbers as modeled, that win is real, and it is also genuinely fragile to several disclosed
assumptions and to a realistic reclassification — both things are true at once, and naming both is
stronger than picking one.

---

## Standards Touched On

**Set · Subset · Union · Intersection · Empty Set · Venn Diagram · How to find the union and intersection of two sets · How to represent a set relationship using a Venn diagram.**

See `LEARNING_GOALS.md` for the forces-test and `case.json.reinforcement_note` for why `new_coverage[]`
is honestly empty (the spine's own n for this skill group moved from 2 to 3 between when the concept
sheet was scored and when this case was written).

---

## Facilitator note — sensitivity

No SPEC Section 6 subject-matter sensitivity applies. This is an operations/compliance decision with
no death, illness, or family-hardship stakes.
