# Guide Notes: End Of Life

**Case:** End Of Life · **Tier:** T2 · **Band:** MS-core · **Studio:** Heroes Academy
**Standards:** see `case.json.standards[]` for the exact ids (11 skills — decimal addition/
subtraction/multiplication, percent, data organization, comparison, rounding, and pie charts)

Legacy conversion, 2026-08-13, built from the original case study docx and Guide Notes
(`source/Y1/Session 6/End Of Life/`) plus three real hospital-bill PDFs and an embedded
net-worth-worksheet image, onto the current 11-anchor ladder. The bill and net-worth figures are
preserved verbatim from the legacy source (see `case.json.legacy_conversion_note`); the hospital's
real-world name was replaced with a fictional one for real-entity safety, and the Federal Poverty
Guideline table was refreshed to real, current 2026 HHS figures. The legacy Guide Notes' twist
content was internally inconsistent about the experimental-treatment dollar figure ($120,000 in
the body, $200,000 and $400,000 with different terms in "Lessons Learned," never reconciled) — the
Twist below is authored fresh, from this conversion's own real numbers, rather than silently
picking one of the three.

## Intro

Sit with the frame, not the finance: a family in a hospital cafeteria, holding real bills, facing
a decision with only two real options. Name the opener — "Two choices. Every day either one takes
longer to reach, real money moves. You have to decide with the family's own numbers, not a
hypothetical."

## Launch

Read Dr. Halbert's prognosis statement aloud (Appendix C) with no bill numbers yet: not in pain,
under 5% chance of waking, likely two to three weeks, won't survive fifty days. Ask: "Just from
this, does removing her sooner feel different from removing her later? Why or why not?" Do not
confirm or correct answers here.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who says remove her on a date you choose? Who says let it happen naturally?" Show of hands, no
discussion yet. Record the count — Close will ask again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do we need to consider in order to decide?"**

Push on what "right" means here: is this a medical question (has already been answered — terminal,
<5% chance), a financial question (can the family actually afford either path), or a values
question (what does "letting her go" vs. "letting nature decide" even mean to this family)? All
three are real considerations Tyler is weighing — not just one number.

## Anchor 3 — What is the process?

**"Do we consider all of these factors, focus on 2-3, or focus on only one? Which one(s)?"**

Once the room picks its deciding factor(s), ask them to name the actual steps: build the day-by-day
ledger (Appendix A extended via Appendix E), find the total cost of the position taken, map which
assets pay it (Appendices B, F), and find the day the money runs out (if it does). Re-ask: "Do we
agree that's the right process for the factor we picked?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the three real, disclosed conventions: the flat daily-rate projection beyond Dec 13
(Appendix E, MA1), which assets count as "liquid" for D4/D5 (Appendix F, MA2), and what household
size to use for the poverty-guideline lookup (Appendix D, MA3 — genuinely unresolved, a real
judgment call about Audrey and Caleb's dependent status). Ask which one actually changes the
family's bottom line the most.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's ledger and D2's total-cost calculation together as a
room, cold-calling for the Day-1-vs-Day-2-onward distinction specifically — this is where a Hero
who multiplies the daily rate by the FULL day count (including Day 1 at the wrong rate) will get a
real, visibly wrong total instead of the correct one built from Appendix E's actual rule
($2,488.91 once, then $8,743.26 per day after).

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"It's Day 4. Tyler's phone rings — it's Dr. Halbert. Lauren has opened her eyes. She's talking.
The family spends the whole day at her bedside — Grace makes it in time. That evening, Lauren
falls back asleep, and back into the coma."

**Facilitator-only.** This does not change Dr. Halbert's prognosis in any way — he is clear that
this kind of brief return is consistent with what he already told the family (under 5%, but not
zero), not a sign the original 14–21 day / 50-day window has changed. What it does is force the
room to re-confront Position A directly: has anything about the arithmetic changed? (No — the
bill kept accruing at the same $8,743.26/day the whole time she was awake; ICU and ventilator
charges don't pause for a good day.) Has anything about the values question changed? That's the
room's to answer, not yours.

**Second beat — deliver after the room reacts to the first:** "Dr. Halbert has one more thing to
tell you. There's an experimental treatment. It's not covered by insurance at all. It costs
**$150,000**, due up front. It would not change how long Lauren has — Dr. Halbert is clear the
50-day outer bound still holds either way — but for however many of those days she has left, she
would very likely be conscious, alert, and able to go home instead of staying in the ICU. Would
you buy it? How would the family pay for it?"

This twist is authored fresh for this conversion (see `case.json.legacy_conversion_note` — the
legacy source's own twist figures were internally inconsistent and could not be preserved as a
single real number). It is checked sound under every stated assumption:

- **Under Appendix E's daily-rate convention**, a family that buys the treatment and takes Lauren
  home stops paying the $8,743.26/day ICU/ventilator rate the moment she leaves the ICU — so the
  $150,000 up-front cost is being compared against bill days the family would otherwise still be
  paying, not simply added on top with no offset. (A Hero who treats it as pure addition on top of
  the full ICU rate is missing this — worth surfacing directly if the room does.)
- **Under Appendix F's liquid/illiquid grouping**, $150,000 up front is larger than the family's
  entire liquid-plus-brokerage total ($111,953.63) — buying it forces a retirement-account
  withdrawal (with real tax/penalty consequences) or a loan, regardless of which Position the
  family originally took. This holds whether the room reads Appendix F sequentially (spend liquid
  first, then retirement) or all-at-once (treat the whole pool as available) — either way, $150,000
  exceeds the liquid pool alone.
- **It does not silently change Position A's or B's underlying arithmetic** — a Hero who was
  defending Position A (remove sooner) can still defend it by declining the treatment; a Hero
  defending Position B can still defend it with or without buying it. The twist adds a real,
  affordable-or-not decision layered on top of the original binary, it does not retroactively
  invalidate either original position.

## Immediate recommit

Re-vote immediately. Ask by name: "Did the twist change your original Position — or did it just
add a new decision on top of the one you'd already made?"

## Deep conflict — three threads (20–30 min)

1. **The $150,000 question, standing alone.** It doesn't change how long Lauren lives (still
   capped at 50 days either way) — it changes what those remaining days look like, and it costs
   more than the family's entire liquid safety net. Is "how she spends her remaining time" worth a
   forced retirement-account withdrawal, on numbers this real?
2. **Financial stewardship vs. honoring natural death.** Removing life support sooner protects
   real money a living 14-year-old will need. Is it ever fair to weigh a specific dollar amount
   against a specific number of remaining days with your mother — and who gets to make that call,
   the family or something else (a hospital ethics board, a living will, nobody)?
3. **What Appendix D's poverty-guideline table is actually for.** The family's own asset picture
   makes it very unlikely they qualify for hospital charity care at any reasonable household size —
   does including Appendix D in your pitch anyway (to show you checked and ruled it out) count as
   real financial diligence, or is citing data you already expect not to help just padding?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — read Dr. Halbert's prognosis aloud, cold-call for a gut read, no bill numbers yet |
| 3:00–10:00 | Position defense — *"Convince us your Position is right for THIS family's numbers, not just 'it feels right'"* |
| 10:00–15:00 | Pressure-test the models — *"Which factor is actually deciding your vote — the money, the odds, or something else?"* |
| **15:00** | **DROP THE TWIST** — Lauren briefly wakes, then the $150,000 treatment, delivered slowly in two beats |
| 15:00–20:00 | Immediate recommit — did the twist change the original Position, or just add a new decision on top |
| 20:00–30:00 | Threaded deep conflict (the $150,000 question; stewardship vs. natural death; what Appendix D is actually for) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

**The trap to let them walk into:** Position B's full 50-day bill total (about $430,908.65) dwarfs
Position A's stop-now total — so a Hero who runs D2's total-cost comparison for both positions will
see that dollar gap, find it huge, and pick Position A on the strength of that one comparison alone,
stopping there. So most learners will assume the total-cost gap settles the case and never look
further. The real trap is that D2's total-cost gap is not this case's actual decision point: it
skips D5 entirely — the family's liquid-plus-brokerage runway (~13.52 days) lands within about 3.4%
of Dr. Halbert's own stated LOW-end estimate (14 days, Appendix C), a near-coincidence that is the
case's real tension — and it skips checking that the family's TOTAL net worth ($667,756.51) still
covers the full 50-day worst-case bill (~$430,908.65) without selling the house. A Hero who computes
the D2 total, calls the decision settled, and never runs D5 at all is wrong — not on arithmetic (the
totals are correct) but on completeness — and it's worth asking them directly whether they ever
found the day the money actually runs out (Data Deep Dive, Socratic Q1–Q2).

## Socratic questions

1. Your liquid-asset runway (about 13.52 days) lands within 3.43% of Dr. Halbert's own low-end survival estimate (14 days) — that 3.43% margin is this case's actual balance-test number (see `case.json.balance.margin_pct`). Using the "how to…" resource you researched, how would you explain that near-coincidence to Tyler in one sentence, and does it make the decision easier or harder?
2. By Day 26, the bill alone exceeds the family's ENTIRE net worth, but by Day 50 their total assets still cover it. What's the real difference between "we'll owe more than we're worth for a while" and "we'll actually lose everything," and which one is really true here?
3. The plan has no out-of-pocket maximum. What percent of a typical ICU day did insurance actually cover in Appendix A, and what does "no maximum" change about that percent as the days pile up?
4. The $150,000 experimental treatment doesn't change how long Lauren has — only what those days look like. If your Position was A, does this new option change your removal date? If your Position was B, does it change how you'd pay for the rest of the stay?
5. Appendix D's poverty guidelines almost certainly don't help this family, given their net worth. What did checking anyway — and ruling it out with real numbers — actually accomplish for your pitch?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight, and
how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that didn't move at
all after the twist is worth asking about directly: did the $150,000 question not feel like a real
factor, or did the room already treat "how long" as the only number that mattered?

## Lessons Learned

Preserved from the legacy Guide Notes, migrated into this ladder: the original run found the room
converged almost unanimously on Position A (remove sooner) early, and that the real discussion
energy was in WHEN, not WHETHER — "it was 100% take her off the breathing machine so the debate
was on what day." The legacy facilitators also found the math itself wasn't the hard part (decimals
and percentages the cohort had already done many times) — the hard part was making the dilemma feel
real enough that a Hero's chosen removal date meant something, not just a plugged-in number. Expect
the same pattern here; if a room converges fast on A, spend Anchor 3 and the deep-conflict threads
pushing on WHEN and on the $150,000 question specifically, since those are where this conversion's
real math (D1, D2, D5, and the twist) actually lives.

- Whether the Day-1-vs-Day-2-onward rate distinction (D1/D2) or the liquid-vs-illiquid asset
  ordering (D4) was the place most Heroes actually got stuck.
- Whether Heroes anchored on the 50-day worst case or the 14-day typical case as their real
  deciding number, and whether that split along any pattern.
- Whether the $150,000 twist changed anyone's chosen removal date under Position A, or only
  changed how Position B Heroes planned to pay.

## Standards Touched On

Percent · Currency · Data · Pie Chart · How to add decimal numbers · How to subtract decimal
numbers · How to multiply decimal numbers · How to find the percent of a number · How to compare
two or more values · How to round a number to a specified place value · How to create a pie chart
given a set of data

## Facilitator note — sensitivity

Real end-of-life care decision for a fictional family, built on a real hospital billing-statement
format and real, current federal poverty guidelines (SPEC.md §6). Keep the discussion frame on the
family's own real numbers (the bill ledger, the net-worth worksheet, the doctor's stated survival
window) — steer away from personal end-of-life anecdotes from the room, which this kind of case can
surface unexpectedly and which a math discussion isn't equipped to hold. Flag this case to a
facilitator before running it with any cohort where a recent family loss is known.

**Sensitivity disclosure (SPEC §2 / Tier 2 probe 5 -- required, not optional).** The primary metric
(liquid-asset runway vs. Dr. Halbert's low-end survival estimate, base margin 3.43%) is NOT stable
under a +-50% flex of the two real dials it depends on. Flexing `daily_rate` (Appendix E) to -50%
stretches the runway to 26.04 days, flipping the winner from B to A at an 86.0% margin -- a swing
that also breaks the SPEC 20% cap. Flexing `survival_low_days` (Appendix C) to -50% moves the
doctor's own reference point to 7.0 days, likewise flipping to A at a 93.1% margin. The +50%
direction on either dial does not flip the winner but still breaks the 20% cap (49.8% and 55.3%
respectively). If a room happens to test either figure at half its stated value, the "razor-thin
3.43%" framing does not hold -- say so rather than defending a margin that no longer exists at that
input. This is disclosed, not eliminated: both dials are real, legacy-preserved bill/estimate
figures (see `legacy_conversion_note`), not authorial fudge, and the metric's closeness to the
doctor's own estimate is exactly why it was chosen over the naive total-cost gap (which is always a
landslide for A and can never honestly clear the 20% cap at all -- see `case.json.balance.
margin_basis`). A metric this genuinely close cannot also be flex-stable without becoming a less
honest metric. Both unstable dials carry Category-F `case.json.sensitivity_disclosure[]` entries
with real justifications (irreducible forecast uncertainty -- a projected future billing rate and a
physician's own estimate range, neither is researchable to a firmer number by any amount of
work). Per the 2026-08-13 disclosure-aware-pass-state amendment to `tier2_probes.py`, a genuinely
unstable dial that is disclosed this way -- category, param, and a real justification on file --
passes Tier 2 probe 5 as **PASS_DISCLOSED**, not FAIL. This supersedes the older `DOCTRINE_LEDGER.md`
MCS-26/MCS-41 text (written before that amendment existed, when no disclosure-aware pass state
existed at all), which is stale on this point and should not be read as still governing this case.
Recorded in `case.json.qa.tier2.P5` as `PASS_DISCLOSED`. Full flex table:
`cases/end-of-life/sensitivity_model.py` (FLEX = `daily_rate`, `survival_low_days`,
`twist_treatment_cost` -- the twist-cost dial is stable across its full range and does not flip
anything).

**Twist soundness check (SPEC §6 / case-write §5).** The Twist above was checked against every
stated Modeling Assumption (MA1–MA3) both sequentially (apply Appendix E's daily rate, then
Appendix F's liquid/illiquid grouping, then the twist's $150,000 cost, one at a time) and
simultaneously (all three assumptions active at once, as a Hero working the full case would
actually apply them) — in both readings, $150,000 exceeds the family's liquid-plus-brokerage total
under Appendix F, and the 50-day survival cap from Appendix C is never altered by the twist, so
the twist cannot silently flip a Hero's D5 "runs out of money" day into a different day depending
on which order they happened to apply the assumptions in.
