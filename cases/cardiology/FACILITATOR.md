# Guide Notes: Cardiology

**Case:** Cardiology · **Tier:** T3 · **Band:** MS-stretch/HS-entry · **Studio:** Heroes Academy
**Standards:** see `case.json.standards[]` for the exact ids (8 skills — percent, ratio, slope,
decimal arithmetic, and comparison)

Legacy conversion, 2026-08-02, built from the original case study docx
(`source/Y2/Session 3/Cardiology/Case Study_ Cardiology.docx`) onto the current 11-anchor ladder.
The source is the real STICH trial (ClinicalTrials.gov NCT00023595, Duke University) — Paul's lab
values are real, cited data, not invented for this conversion. Cost figures were not in the
original materials and are a disclosed modeling convention (case.md Appendix C).

**Correction, 2026-08-04:** the mortality table this guide originally cited was fabricated (it did
not match the real trial's published results) and has been replaced with the trial's real reported
numbers — see `case.json.correction_2026_08_04` for the full account and sources. The twist below
now runs in the opposite direction from the original draft: the real gap *widens* at 10 years and
only becomes statistically significant there, rather than narrowing.

**Remediation, 2026-08-20:** a Tier 2 gate run found two real defects — see
`case.json.qa.remediation_note_2026_08_20` and `QA_REPORT.md`'s 2026-08-20 entry for the full
account. (1) This guide's old "The trap" section named a difficulty (which factor a student
weighs) rather than a concrete wrong move; a fresh cold-solve found the actual trap — Appendix A is
headed *mortality*, D1 asks for *survival rate*, and the point gap survives the swap, so a rushed
Hero can copy mortality numbers into D1 unconverted and get an internally-consistent but backwards
answer. Rewritten below. (2) `case.md`'s own Appendix A used to print both the 5-year and 10-year
rows together, so the Twist's "surprise" was already sitting in the packet before Anchor 1's vote.
`case.md` now shows only the 5-year row before the `<!-- FACILITATOR ONLY -->` marker; the real
10-year data moved to a facilitator-only section after that marker (case.md is not stripped for a
student read this way in any other case in this project's corpus yet — this is the first case to
actually rely on that mechanism for load-bearing content, not just the boilerplate comment). The
published interactive HTML's Appendix A table was also cut down to the 5-year row to match; the
10-year figures still appear, but only inside the gated Twist section a student must click through.

## Intro

Frame the format: this is a real treatment decision for a real kind of patient, built on a real
published trial, not a worksheet. Name the opener — "Two therapies. Both real, both studied. One
patient who has to live with whichever one gets recommended."

## Launch

Read Paul's real risk profile aloud (98% occlusion, family history, daily smoker) with no numbers
from Appendix A yet. Ask: "Just from this profile, does this feel like a close call to you?" Do not
confirm or correct answers here.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who recommends MT? Who recommends CABG?" Show of hands, no discussion. Record the count — Close
will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do we need to consider in order to decide?"**

Push on what "best" means here for a doctor, not a hospital administrator: survival odds, quality
of life, cost to the patient, and the patient's own stated risk factors are all real considerations
Dr. Hotchkiss has to weigh — not just one number.

## Anchor 3 — What is the process?

**"Do we consider all of these factors, focus on 2-3, or focus on only one? Which one(s)?"**

Once the room has picked its deciding factor(s), ask them to name the actual steps: survival rate
from the trial table, Ejection Fraction from Paul's own SV/EDV, five-year cost for each therapy,
and the slope/intercept of each cost line. Re-ask: "Do we agree that's the right process for the
factor we picked?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the two real conventions: the cost figures (Appendix C) are a stated modeling assumption,
not trial data, and the cost model assumes no medication-price changes or inflation over five
years. Ask which one actually matters more to the final recommendation.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's survival-rate comparison and D2's Ejection Fraction
calculation together as a room, cold-calling for the SV/EDV division specifically — this is where a
Hero who divides the wrong way (EDV/SV instead of SV/EDV) will get a real, visibly wrong (impossibly
high) Ejection Fraction instead of Paul's real value from Appendix B.

Also cold-call for the mortality-to-survival conversion specifically, the moment the room touches
Appendix A: D1 asks for *survival rate*, and Appendix A's table is headed *mortality*. A Hero who
skips converting mortality into survival (survival% is what's left after mortality%) and treats 41%/36% as if they were already the survival rates will
land on an internally-consistent but backwards 5.0-point gap, with MT (41) reading as the bigger,
better number instead of CABG (which really wins at 64% vs 59%). See "The trap" below — this is the
trap, not a side issue.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses. As of the 2026-08-20 fix, `case.md`'s Appendix A shows only the
5-year row before the reveal — this is genuinely the first time a student sees the 10-year numbers,
not a repeat of something already sitting in front of them.

"Paul asks Dr. Hotchkiss one more question: 'What about ten years out, not just five?'"

**Facilitator-only.** The real trial's extended follow-up (the STICHES study, published five years
after the original) reports 10-year outcomes: CABG's mortality rises to 58.9%, MT's to 66.1% — both
much worse in absolute terms (this is an older, sicker cohort further out), but CABG's real
advantage actually *widens*, from a 5.0-percentage-point gap at 5 years to a 7.2-point gap at 10
years. This is a genuine recompute with the trial's own additional real data, not a new invented
number.

Here is the real detail that makes this twist land: the 5-year gap Dr. Hotchkiss and Paul are
looking at **right now, in this appointment, was not statistically significant** (p=0.12 in the
real trial — a real difference could easily just be noise at that sample size). The 10-year gap
**was** significant (p=0.02). Dr. Hotchkiss has to make a real recommendation today on data that,
strictly speaking, could not yet prove CABG was better — it took ten more years of real follow-up to
confirm the difference was real. Ask: "Knowing the 5-year gap wasn't yet statistically proven — does
that change how confidently you'd have recommended CABG at the time? And does it matter that the
real world later showed the gap was real after all?"

Do not hand over a "correct" answer — reasonable people weigh a real-but-unproven advantage
differently, and reasonable doctors have to recommend under exactly this kind of uncertainty all the
time.

## Immediate recommit

Re-vote immediately. Ask by name: "Did the ten-year numbers change your recommendation, or did they
just make you want to ask Paul more about his own priorities?"

## Deep conflict — three threads (20-30 min)

1. **Survival rate vs. cost.** CABG is safer by a real 5.0-percentage-point margin at 5 years (not
   yet statistically proven at that point); MT is cheaper by a real $67,000 over the same window. Is
   any cost difference large enough to outweigh a real, but not-yet-certain, survival-rate edge, or
   does that depend entirely on what the patient can actually afford?
2. **What the trial's average patient doesn't capture about Paul specifically.** Paul's own risk
   factors (98% occlusion, family history, daily smoking) — does that make him more or less likely
   to benefit from CABG's survival edge than the trial's average participant?
3. **The disclosed referral fee.** Dr. Hotchkiss's office earns 0.97% on every MT medication sale.
   Does that fact change how you'd want a doctor to present this decision to a patient, even if the
   trial data itself is real and unbiased?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — read Paul's risk profile aloud, cold-call for a gut read, no trial numbers yet |
| 3:00–10:00 | Position defense — *"Convince us your therapy is the right call for Paul specifically, not just 'the trial showed a difference'"* |
| 10:00–15:00 | Pressure-test the models — *"Which factor is actually deciding your vote — survival, cost, or something else?"* |
| **15:00** | **DROP THE TWIST** — the 10-year numbers, delivered slowly |
| 15:00–20:00 | Immediate recommit — did the longer horizon change anyone's answer |
| 20:00–30:00 | Threaded deep conflict (survival vs. cost; Paul's specific risk profile; the disclosed referral fee) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

The real trap is a label swap, not a weighting choice. Appendix A's table is headed **mortality**
(41% MT / 36% CABG at 5 years); Challenge D1 asks for **survival rate**. A rushed Hero can copy the
mortality percentages straight into D1 as if they were already the survival rates, skipping the
mortality-to-survival conversion entirely. The point gap still comes out to 5.0 either way (41 − 36 =
64 − 59), so the arithmetic "checks" — but the labels invert: MT's 41% now reads as the bigger
number and looks like the winner, when the real survival winner is CABG (64% vs 59%, not 41% vs
36%). This can flip a Hero's entire D5 recommendation while looking internally consistent, and it
is the single most likely wrong move a fast solver makes on this case. Watch for it specifically
during the Data Deep Dive, the moment the room converts Appendix A's numbers for D1 — do not let it
pass uncaught just because the final point-gap number happens to match.

A secondary, softer trap, worth naming if the room clears the first one cleanly: a Hero computes
the cost difference, recommends MT on price alone, and never engages with the real survival-rate
gap the trial actually measured — or the reverse, recommending CABG on survival alone without ever
mentioning that $94,000 is a real number a real family has to find. The case's actual tension is
that a cheaper option carries a real, disclosed survival cost, not that one option is simply
"better" — but this is a distant second to the mortality/survival label swap above.

## Socratic questions

1. CABG's five-year survival rate is 5.0 percentage points higher than MT's — how would you explain to Paul and Cindy why that gap is or isn't decisive on its own?
2. CABG costs more than MT over five years — does a cost gap that size ever get to override a real survival-rate difference, and who should get to make that call: the doctor or the patient?
3. Paul's Ejection Fraction is in the low 30s as a percent — using the "how to…" resource you researched, what does that number suggest about how sick his heart already is, independent of which therapy he picks?
4. Dr. Hotchkiss's office earns money on every MT prescription. Does knowing that change how you'd weight his own stated recommendation, even though the trial data itself doesn't come from him?
5. The ten-year numbers widen CABG's advantage from 5.0 to 7.2 percentage points, and only at ten years does the gap become statistically significant. What does it mean for a recommendation Dr. Hotchkiss has to make today, on data that can't yet prove itself?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that didn't
move at all after the twist is worth asking about directly: did the ten-year numbers not feel like
a real factor, or did the room already treat "five-year survival" as the number that mattered most?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether the SV/EDV division (D2) or the cost-table slope/intercept read (D4) was the place most
  Heroes actually got stuck.
- Whether Heroes anchored on survival rate or cost as their real deciding factor, and whether that
  split along any pattern.
- Whether the disclosed referral-fee detail changed how Heroes framed their own pitch, even though
  it isn't part of the graded balance test.

## Standards Touched On

Percent · Ratio · Slope · Decimal · Data · Measurement · Mean · Unit · How to convert numbers to
percents · How to find equivalent ratios · How to identify the slope of a line given a set of data
· How to multiply decimal numbers · How to add decimal numbers · How to compare two or more values

## Facilitator note — sensitivity

Real medical decision-making with a named patient facing a life-or-death treatment choice (SPEC.md
§6). Keep the discussion frame on the real trial data and Paul's own stated risk factors — steer
away from personal medical anecdotes from the room, which can turn a math discussion into something
a facilitator isn't equipped to hold.
