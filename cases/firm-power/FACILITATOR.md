# Guide Notes: Firm Power

MS | Guide Notes | Adventure | 2026-27
**Tier:** T3 (MS-stretch/HS-entry) · **Primary metric:** dollars per megawatt-hour of 100%-firm capacity · **Margin:** thin — see `case.json.balance` for the exact figure

---

## Argument for A (the Peaker Contract)

Fully dispatchable at 100% reliability with no separate accreditation charge of any kind — even
at the real published low end of Lazard's national range, $149 per megawatt-hour buys a mature,
well-understood technology with none of the capacity-accreditation-methodology uncertainty CAISO
and other grid operators are still actively revising for solar-plus-storage (Appendix D itself
notes CAISO has been lowering its own ELCC values for this exact technology in recent years). A
guide should let a Hero who picks A on reliability-certainty grounds alone defend it — the numbers
favor B, but not by enough to make A an unreasonable choice.

## Argument for B (the Firmed Solar Contract)

Wins on the case's own real, published numbers once both options are priced on the same
100%-firm basis: $142 per megawatt-hour ($73/MWh raw cost plus the real, CAISO-specific $69/MWh
firming charge) against the Peaker Contract's $149 per megawatt-hour — even using the most
favorable realistic point in gas peaking's own real cost range. The gap is real but thin.

## Margin

**Computed: margin_pct = 4.7%, the Firmed Solar Contract wins.**
`margin_pct = |149 - 142| / max(149, 142) x 100 = 4.70%`. Both rates are Lazard's own real,
published figures; see `case.json.balance` and `RESEARCH_LOG.md` for full derivation.
**The single most load-bearing modeling choice in this case is using the LOW END of gas peaking's
real cost range ($149) rather than its midpoint (~$200).** At the midpoint, B's margin widens well
past this case's own 4.7%. At the high end of gas peaking's range, the comparison would not even
be close. This is disclosed in `case.json.sensitivity_disclosure[]` and should be surfaced in
discussion, not treated as a hidden fragility.

---

## Five Socratic questions

1. Appendix C uses the LOW end of gas peaking's real cost range, not its midpoint. If you used the
   midpoint instead, what would happen to your recommendation — and is using the low end a
   reasonable modeling choice, or a thumb on the scale?
2. Your D1 outlier test and your D3 peak-window count both come from the same 24-hour data set.
   Could a day with a genuinely unusual shape (a heat wave, a grid emergency) change your D3 answer
   even if it didn't produce a statistical outlier by the 1.5×IQR test? What's the difference
   between those two ideas?
3. Appendix D's $69/MWh firming charge is a real published number, not something you derived from
   scratch. What would you need to see to trust that number the way you'd trust your own D1/D2
   arithmetic?
4. D4's budget-based equation shows what the board's monthly authorization alone could buy in
   firming capacity. How does that number relate — or not relate — to your actual recommendation?
5. MA1 scales every dollar figure in D3 and D5 by the same 3% factor. Does that assumption change
   which contract wins? What is the one thing it actually changes?

## The trap

**A student compares solar-plus-storage's raw $73/MWh figure directly against gas peaking's
$149-$251/MWh range and concludes solar-plus-storage is an overwhelming, obviously-correct choice
— without ever adding in the real $69/MWh firming charge that brings it to the same reliability
standard as a gas plant.** This is the single most common real-world version of this mistake: it
looks rigorous (both numbers are real and cited) and produces a confident, wrong-by-omission
conclusion, because it compares an intermittent resource's raw cost against a fully-dispatchable
resource's cost, on different reliability terms. The case's own Background paragraph warns about
exactly this ("comparing solar's cost alone against gas would not be a fair fight"), but a hurried
student will often skip straight to Appendix C and the LCOE-only half of Appendix D.

## Twist

**N/A.** This case's tension is genuinely economic/technical — the real firming-cost mechanism
itself — rather than an information-withholding twist. There is no piece of data revealed
mid-discussion that would invalidate a popular position without simply changing the inputs.
Authors considered a twist (e.g., a mid-discussion reveal that CAISO's own ELCC value for
solar-plus-storage was recently lowered further) and found it would only sharpen an argument
already present in Appendix D's own text, not invalidate a position outright — N/A is the honest
call, consistent with `the-turbine-channel` and `wind-call`'s own N/A calls for structurally
similar reasons.

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch, 30-second commitments, stand/sit vote at Anchor 1 — no explanation yet. |
| **3:00–10:00** | Position defense. *"Convince us your contract is the fair comparison, not just the cheaper number on the page."* |
| **10:00–15:00** | Pressure-test the models. *"Where in your work did you account for reliability, not just raw cost?"* |
| **15:00–20:00** | Walk the room through D1–D3 together. **No twist drops here** — see Twist: N/A above; this slot instead surfaces the trap (raw LCOE vs. firmed total) if no one in the room has caught it yet. |
| **20:00–30:00** | Two named threads: **(1)** is using the low end of gas peaking's real range a fair modeling choice or a thumb on the scale?; **(2)** does MA1's 3% share assumption matter to the *recommendation*, or only to the *scale* of the numbers? |
| **30:00–45:00** | Close, re-vote, reflection, lessons learned. |

---

## Guide Notes — the anchor ladder

### Intro
Heroes, today's case is a real grid-planning decision: not "which technology is cheaper," but
"which technology is cheaper once both are priced on the same reliability terms."

### Launch
Read the Overview aloud, or show it on screen. Stop at "She pulls both folders toward her."

### Anchor 1 — Take a stand and vote
The Peaker Contract or the Firmed Solar Contract. No reasoning yet. Hands up, write the split on
the board. *"Is anyone courageous enough to stand with the gas plant?"*

### Anchor 2 — What is the problem we're solving?
Do not let them calculate yet.
- Is this actually "which is cheaper," or "which is cheaper at the same reliability"?
- Someone will say "solar's obviously cheaper, look at the numbers." What numbers, exactly — the
  raw LCOE, or the firmed total?
- Let the confusion grow. *"We don't even agree yet on what we're comparing."*

### Anchor 3 — What is the process?
- If we just compare the two headline LCOE numbers, are we done? (No — that skips the firming
  charge entirely.)
- What do we need from the real data to size the actual decision?
- Is our question still the right question?

### Anchor 4 — What don't we know?
- Do we need to assume anything? Which assumption is load-bearing? (Steer toward the choice of
  where in gas peaking's real range to land, without naming the exact figure.)
- What would Priya still not know, even with both numbers in hand?

## Data Deep Dive
Walk the room through reconstructing the missing hour (D2), computing the real descriptive
statistics (D1), sizing the peak-window capacity gap (D3), and converting the real Net CONE figure
into a solvable equation (D4). Ground truth for cross-checking a Hero's own work is in
`case.json.balance` — do not read the exact figures aloud before the room has attempted D1–D5
themselves.

## Close
- Vote again. Who moved, and why?
- Was "which is cheaper" the right question, or was it really "which is cheaper at the same
  reliability"?
- What math was new to you here — the missing-data reconstruction, the quartiles, or the
  unit-conversion chain in D4?

## Lessons Learned
The case's real lesson sits in the gap between a resource's raw cost and its firmed cost. A
learner who only compares the two raw LCOE figures has answered a question the case never
actually asked. This is not a manufactured classroom trick — real grid operators (CAISO, PJM,
MISO, and others) publish exactly this kind of firming-cost analysis for exactly this reason.

## Standards Touched On

**New coverage:** none — see `case.json.reinforcement_note`. This case reinforces five
Statistics And Probability/Data Analysis skills (including the group's two thinnest, `quartiles`
and the missing-data-element how-to), plus a thin Advanced Operations/Variables how-to.

**Claimed:** Quartiles · Outlier · Median · Range · Mean · How to find a missing data element
given the mean and the remaining elements of its set · How to find the mean of a set of data ·
How to find the percent of a number · How to convert an amount with compound units · How to solve
a multi-step equation with a variable on one side

## Facilitator note — accessibility (P7 waiver)

This case's Tier 2 accessibility cold-read (P7) is on file as a **waived FAIL** (`case.json.qa.tier2.P7_waiver`) — a zero-context reader still names real financial/regulatory jargon (ELCC computation mechanics, Net CONE's economic basis, the firming charge's contractual trigger) as genuinely hard to picture, even after real remediation. A guide running this case in a live room should plan to spend a few extra minutes on Anchor 4 ("what don't we know?") walking through the firming-charge mechanism concretely — the three-step payment/trigger explanation in Appendix D is the best starting point.

## Facilitator note — sensitivity

None required. This is a capacity-procurement business decision with no death, illness, or
family-hardship stakes — SPEC §6 does not apply. The one thing worth flagging to a guide is the
range-endpoint choice named in `case.json.sensitivity_disclosure[]` — a strong Hero challenging
the low-end gas-peaking figure is engaging with the case exactly as intended.

## What a strong defense sounds like

Not "solar is cheaper" — that's the trap, not the defense. A strong defense shows the firmed
total (not just the raw LCOE), names where in Lazard's real published range the gas-peaking figure
sits and why, states the 3% share assumption out loud, and is honest that the margin is thin
enough that a defensible board could reasonably land on either contract.
