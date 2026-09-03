# FACILITATOR.md — The Attribution Sample

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Attribution Sample · **Tier:** T2 (MS-core) · **Studio:** Adventure
**Standards:** Statistics And Probability/Sampling And Experiments — Simple Random Sampling,
Stratified Sampling, Multistage Sampling, Sample Size, Sample, Population; plus Advanced Numbers —
Percent, How to find the percent of a number (see `case.json.standards[]` for exact ids).

**Status:** `case-write` + `case-research` complete (2026-09-01) — all 14 `{{NEEDS_SOURCE}}` tokens
closed (5 SOURCED, 9 ASSUMPTION, 0 DROPPED, 0 OPEN; see `RESEARCH_LOG.md`). `case.json.status` is
`"researched"`. `margin_pct` is `19.83` (see the Balance section below) — genuinely close, no
retune or waiver needed. Not yet run through `case-qa`.

## Real-world grounding (for the facilitator's own background, not for case.md)

- **AppsFlyer's "State of Fraud for Marketers 2026" report** (appsflyer.com/company/newsroom/pr/
  organic-traffic-ad-fraud/) is the real anchor for most of this case's numbers: organic traffic
  is now the single largest source of fraudulent installs (52% of all fraud), affiliates carry
  "nearly 40%," and owned-media fraud specifically rose from 3.4% to 11% year-over-year — a real,
  precise figure this case uses directly (Appendix D, Owned & Boosted Media, S3), not as an
  assumption.
- **RocketShip HQ's summary** (rocketshiphq.com) of AppsFlyer's channel-level fraud data gives the
  real range this case's per-channel Modeling Assumptions are anchored to: self-attributing
  networks (Meta/Google/TikTok/Apple Search Ads) run 1-8% fraud, Tier-1 DSPs run 12-20%, and
  influencer/CPI networks run the widest range of any channel type, 15-30%. That last range — the
  widest of the four — is exactly why the case's small Influencer/Affiliate channel is the one
  worth protecting with a real sample: its true rate is the least certain, industry-wide, of any
  channel this case models.
- **Real methodological grounding:** the tension this case is built on — that a rare-but-important
  subgroup can be all but invisible to a simple random sample, and that stratified sampling exists
  specifically to fix that — is a textbook-standard justification for stratified sampling, not an
  artifact of this case's specific numbers. Verafly, Driftline Games, and Emberfall Kingdoms are
  all fictional; the sampling mechanics and the channel-level fraud-rate ranges they're anchored to
  are real.

## Intro

Frame the format: this is a real weekly-report decision under a real deadline, not a worksheet.
Name the opener — "You have one weekend, two ways to sample the same data, and one of your four
channels is small enough that a simple random sample might barely see it at all. Which one do you
run tonight?" Mention, once, that this exact tension — protecting a rare subgroup versus keeping
sampling cheap and fast — is why stratified sampling exists as a real, named technique in applied
statistics, not an invention for this case.

## Launch

Show Appendix A's four channels and their click-volume shares (62/26/10/2%) with no sample-size or
error numbers yet. Ask: "If you had to guess blind, which of these four channels would you trust
least in a report built from a random sample?" Most rooms will correctly guess the smallest one
(2%) — but few will yet be able to say *how* untrustworthy, in a number. Record the guess; Data
Deep Dive will make it precise.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the Pooled Random Sample — the fast one?" Show of hands,
both options, no discussion yet. Record the count.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'trust' a channel's number?"**

Let confusion grow here on purpose. Heroes will want to jump straight to "which one is faster,"
but push on what "trust" actually means in a sampled estimate: "If Derek's report says the
Affiliate channel is 85% real installs, what would make you believe that number — versus doubt it?
What's different between a number you'd bet a decision on and a number you wouldn't?" If the room
lands on "it depends how many clicks that number is actually based on," the case is working as
designed — that's standard error, before anyone has named it.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "which one is faster" from "which one's small-channel number is actually
trustworthy," ask them to name the actual steps before touching the appendices: compute Option A's
expected per-channel sample sizes and standard errors (D1); design Option B's stratified allocation
and its standard errors (D2); tally each option's total analyst-hours against the weekend budget
(D3); combine error and hours into the case's actual primary metric (D4); and decide, using all of
that, which option Derek should run tonight (D5). Re-ask: "Is our question still the right one, now
that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gap honestly: Verafly, Driftline Games, and Emberfall Kingdoms are all fictional,
so the specific channel-volume split (62/26/10/2%), the exact per-channel fraud rates chosen inside
each real published range, and the per-click verification times are all stated Modeling
Assumptions, not measured facts (`case.json.modeling_assumptions[]`). Ask which of the open figures
is actually load-bearing for the recommendation. The honest answer: MA4 (the Affiliate channel's 2%
share) is the single most load-bearing open item — it's what makes Option A's expected sample there
(8 clicks) so thin in the first place. MA11 (the Affiliate channel's true fraud rate, chosen at the
*low end* of the real 15-30% range) matters for the qualitative stakes, not for `margin_pct`
directly — a Hero who notices this distinction has understood something real about what a Modeling
Assumption's "sensitivity" note is actually claiming.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's precision table, D2's stratified design, D3's hours
table, and D4's combined metric together as a room, cold-calling for D4 specifically — this is
where a Hero who wrote a correct D1 (noticing the Affiliate channel's SE is 12.62pp under Option A)
but never connects it to D4's actual ratio will visibly struggle to answer "so which one wins,
here, tonight, by your own numbers." Have the room independently sanity-check Appendix E's 8 vs. 40
Affiliate-channel sample counts before trusting the SE column — a common error is forgetting that
Option A's allocation is only an *expectation*, not a guarantee (see Twist).

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses: "One more thing. That 'expected 8 clicks from the Affiliate channel'
under the Pooled Random Sample — that's an average over many possible random draws. Tonight is
just one draw. If you actually ran the numbers on how likely a single 400-click random pull is to
land *fewer than 5* real samples from a channel that's only 2% of total volume — using nothing more
than what you already know about that channel's share and the total sample size — you'd find it's
close to an 11% chance. Not rare. More than one time in ten."

"If there's roughly a coin-flip's-little-brother chance that tonight's random pull gives Derek an
Affiliate-channel estimate built on four or fewer real clicks — does that change which option you'd
stand behind, even before Monday's marketing-lead board deck ever comes up?"

**Facilitator-only: what this does and doesn't change.** This is a real, computable fact (Binomial
n=400, p=0.02, P(X<5) ≈ 10.6% via normal approximation — the facilitator can walk this on the board
if the room wants to see it) — it does not appear anywhere in case.md and is not itself
load-bearing for `margin_pct`. It sharpens the *qualitative* argument for Option B (the guaranteed
floor removes exactly this risk) without changing D4's arithmetic. A Hero who says "the twist proves
Option A is wrong" has overreached — it proves Option A carries a real, quantifiable *risk* that
Option B's design specifically eliminates, which is a more precise and more defensible claim.

## Deep conflict — threads (20–30 min)

1. **Which "error" is Derek actually being graded on?** D4's primary metric is the *pooled,
   whole-report* standard error — and Option A's pooled SE (1.369pp) is barely worse than Option
   B's (1.407pp), almost a rounding difference. But the *channel-level* SEs (Appendix E) tell a
   completely different story for the Affiliate channel specifically (12.62pp vs. 5.65pp). Push:
   "If you were Driftline's marketing lead walking into next week's board deck with just the
   Affiliate-channel number, which option's number would you actually want in your slide?"
2. **Same total sample, different guarantee.** Both options verify exactly 400 clicks — the *cost*
   isn't really about verification volume, it's about setup time and where those 400 clicks land.
   Push: "If total clicks verified is identical, is 'costs more analyst time' really about the
   sampling, or about something else the case is charging Option B for? Is that charge fair?"
3. **The deadline is real, but not decisive.** Option B's 12.95 hours fits inside the 13-hour
   budget — barely. Push: "If your actual measured setup or verification time ran even 5% over
   estimate, would Option B still make Monday's deadline? What would you do differently tonight if
   you knew that going in?"

## The trap

Heroes will read D4's *pooled* standard errors (1.369pp vs. 1.407pp, nearly identical) and conclude
the two options are basically equivalent in accuracy, missing that Appendix E's *channel-level*
breakdown tells a much sharper story for exactly the channel the case's Background flags as
under scrutiny (the Affiliate channel, 12.62pp vs. 5.65pp SE). A second, related trap: treating
Option A's "expected 8 clicks from the Affiliate channel" as a guarantee rather than an average —
the Twist exists specifically to catch a Hero who has not distinguished "this is what happens on
average" from "this is what will happen tonight."

## 45-Minute Socratic Plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch (Intro/Launch), 30-second commitments, stand/sit vote (Anchor 1) — no explanation. |
| 3:00–10:00 | Position defense: "Convince us the fast pooled sample is still the right call — or isn't" (Anchor 2). |
| 10:00–15:00 | Pressure-test the models: process and open assumptions (Anchors 3–4) — name D1-D5, surface which figures are real vs. modeled. |
| 15:00–25:00 | Data Deep Dive — D1-D5 together; cold-call the D4 combined-metric ratio specifically. |
| **25:00** | **DROP THE TWIST** — the ~11% chance of a badly undersampled Affiliate draw, delivered slowly. |
| 25:00–30:00 | Immediate recommit: who reverses? "What just changed — the math, or your read of the risk?" |
| 30:00–40:00 | Threaded deep conflict — see below. |
| 40:00–45:00 | Close, re-vote, reflection, Lessons Learned. |

## Socratic questions

1. Option B wins D4's primary metric by 19.83% — genuinely close, not a blowout. If the margin had come out at 2% instead, would your recommendation change? What if it had come out at 60%? What does the *size* of a margin actually tell you that a plain "which one wins" doesn't?
2. Both options verify exactly 400 clicks. Explain, in your own words, why Option B still costs more analyst-hours than Option A even though neither option verifies a single extra click beyond the other.
3. The twist describes an ~11% chance that a single random pull draws fewer than 5 Affiliate-channel clicks. Does a 1-in-10 chance of a badly undersampled estimate mean Derek should never use a pooled random sample — or does it mean something more specific about which channels are safe to sample that way and which aren't?
4. If Driftline's marketing lead had *not* flagged the Affiliate channel for scrutiny — if this were just a routine week — would your D5 recommendation change? What does that tell you about how much of this decision is a math question versus a "what does the client actually need this number for" question?
5. Appendix D sets the Affiliate channel's fraud rate at 15%, the *low end* of the real published 15-30% range. If the true rate were actually 30% instead, which of your D1-D4 numbers would change, and which wouldn't?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare to Anchor 1's vote — a room that moves after the twist
should be pressed to explain the move using D1/D2/D4, not just the twist's numeric jolt.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

## Standards Touched On

Simple Random Sampling · Stratified Sampling · Multistage Sampling (vocabulary contrast only) ·
Sample Size · Sample · Population · Percent · How to find the percent of a number

## Balance argument (SPEC §2)

**Argument for A (the Pooled Random Sample).** It verifies the identical 400 clicks Option B does,
in roughly three-quarters of the time (10.1 hr vs. 12.95 hr), leaving Derek nearly 3 hours of
weekend slack against Appendix A's 13-hour budget instead of a ~4-minute margin. Its pooled,
whole-report standard error (1.369pp) is barely worse than Option B's (1.407pp) — for the single
number Derek's report leads with, the two options are nearly indistinguishable in accuracy.

**Argument for B (the Channel-Stratified Sample).** It wins the case's own stated primary metric —
attribution error per analyst-hour — and it is the only option that makes the Affiliate channel's
own estimate usable at all: 5.65 percentage points of standard error versus Option A's 12.62, on a
channel whose real-world fraud rate could plausibly run anywhere from 15% to 30% (Appendix D,
MA11, anchored to the real published range in S2) and which Driftline's marketing lead has
specifically flagged for next week's board deck. A report that reads "85% ± 12.6 points" is not a
number Derek can defend in that meeting; "85% ± 5.7 points" is closer to one he can.

**Margin — COMPUTED 2026-09-01 (case-research).** `margin_pct: 19.83`. **Winner (on the stated
primary metric): Option B, The Channel-Stratified Sample.** Pooled SE_A = 1.369pp at 10.1 total
hours → 0.1355 pp/hr. Pooled SE_B = 1.407pp at 12.95 total hours → 0.1086 pp/hr. margin_pct =
(0.1355−0.1086)/0.1355 × 100 = 19.83%. This sits just under SPEC §2's ~20% cap — **no retune pass
was needed**, and no MCS-46-style waiver applies. Full arithmetic trail: `case.json.balance.
margin_note` and `RESEARCH_LOG.md`'s Margin section; independently reproduced (with a small,
disclosed rounding difference, 19.68% vs. 19.83%, from continuous vs. whole-click allocation) in
`sensitivity_model.py`.

**What this means for facilitation.** The genuine tension is real and does not resolve just by
computing D4: Option A wins decisively on schedule slack and is nearly tied with Option B on the
*pooled* number; Option B wins the stated primary metric and is the only option that makes the
*specific* channel under scrutiny defensible. A room that only debates "which ratio is bigger" is
missing half of what this case is testing — cold-call specifically on Appendix E's channel-level
breakdown, not just D4's final ratio.

## Facilitator note — sensitivity (SPEC §6)

NONE. This is routine marketing-analytics sampling-methodology math (ad-click verification, install
fraud) — no subject-matter sensitivity flag applies.
