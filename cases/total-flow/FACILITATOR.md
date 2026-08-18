# Guide Notes: Total Flow

**Case:** Total Flow · **Tier:** T4 · **Band:** HS · **Studio:** Launchpad
**Standards:** Calculus / Integrals (all 7) + Calculus / Applications Of Integrals (2 of 4) — all
`new_coverage` (see `case.json.standards[]` for the exact ids)

Researched 2026-08-12 against the real USGS record for Henderson Creek near Oquawka, Illinois
(site 05469000). Current `margin_pct` = 4.26 (see `sensitivity_model.py`, `case.json.derived`).
This file is re-checked for drift at every readiness run.

## Intro

Frame the format before anything else: this is a professional certification, not a worksheet.
Name the opener — "You are the engineer of record. Your seal goes on this, not the board's, and
the bid package can describe exactly one design." Let that land before the Launch.

## Launch

Put the two hydrographs on the board side by side, axes labelled, **no totals and no shading**.
Ask: "Which of these two storms put more water on this town?" Take a gut read. Do not confirm or
correct. The whole case lives in the gap between what that picture looks like and what it is.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Nadia on The Basin Standard — the one that does nothing
at all about the peak?" Show of hands on both options, no discussion. Record the count; the Close
asks them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'bigger flood'?"**

Let confusion grow — this is deliberate. Heroes will reach for the peak, because the peak is the
number a news report would give them. Push: "Nadia is not protecting the town from a rate. What is
she protecting it from?" If the room lands on the distinction between *how fast* the water arrives
and *how much of it there is* without being handed it, the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Before anyone opens an appendix, make them name the steps: turn a table of rates into a volume
(D1), turn that table into a function you can integrate exactly (D2), find the part of the volume
that is actually a problem — the part above channel capacity (D3), and only then ask what each bid
catches and what it misses (D4). Re-ask: "Is our question still the right one now that we can see
the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Appendix F's five Modeling Assumptions are all stated, not sourced — the levee district is
fictional, so its appropriation, its bids and its detention structures cannot exist publicly. The
gage, the two hydrographs, the channel capacity, the rating and the flood-frequency record are all
real and cited in Appendix E.

Then push past the table, because the honest answer is not in it. The three numbers that actually
decide this case are **not in that table**: channel capacity (1,934 cfs), the raised crown's design
discharge (5,927 cfs), and the authorised storage (25,000 acre-feet). The first and third are
sourced measurements or statute; the second is Bid A's *scope* — a chosen height, not a measured
one. Appendix F's closing block tells Heroes directly that two of these lines are chosen rather
than measured — the channel-capacity *convention* (the National Weather Service's minor flood
stage) and the height in Bid A's scope — and that moving either moves the answer. A Hero who
attacks one of those two lines is doing exactly the right thing, and the arithmetic rewards it: at
22.00 ft instead of 21.50 ft, the Basin Standard wins.

## Data Deep Dive

Now, and only now, the numbers. Work D1 → D2 → D3 → D4 together as a room, cold-calling on two
specific moments:

1. **The D1/D2 disagreement.** A Riemann sum and a Fundamental-Theorem evaluation of the *same*
   storm do not return the same number, and a Hero who reports them as if they agree has not
   understood either. Ask which is closer to the truth and how they would know without being told.
   The subtlety worth surfacing: because Appendix A's values are daily *means* and the interval is
   exactly one day, the D1 sum is not an approximation of the published record at all — Appendix D
   quotes USGS saying the daily means *are* the daily volumes in cfs-days. What the sum does miss
   is the sub-daily peak the daily mean already averaged away. The approximation error is in the
   record, not in the arithmetic.
   **Watch the endpoints.** Appendix D states the convention: an 8-row storm spans 8 days, one
   subinterval per row, so the correct D1 sum for The Slammed Door is all 8 values — 18,767
   cfs-days. A Hero who treats the 8 rows as 8 sample *instants* spanning only 7 intervals gets
   18,293 (left endpoints), 18,354 (right endpoints), or 18,323.5 (the average of the two), and
   cannot reconcile any of them with the D4 table. If you see any of those three numbers, the fix is a reading of
   Appendix D, not a re-computation.
2. **The D3 limits of integration.** Heroes will integrate Q(t) across the whole storm window
   instead of across the interval where Q exceeds channel capacity. The shaded diagram is what
   catches this; make them draw it before they compute it. D3 also asks for the same floodwater
   volume read straight off Appendix A's daily blocks and for the two to be reconciled — the
   daily-block figure (19,374 and 33,255 acre-feet) is the one D4 scores, because the board scores
   the published record, not anybody's curve fit.

**Facilitator-only figures.** Whole-storm volumes first, because D1 asks for them: The Slammed Door
carries 18,767 cfs-days (37,224 acre-feet) past the gage and The Long Guest 32,437 cfs-days
(64,338 acre-feet). Only the part above the 1,934 cfs channel capacity is *floodwater*, and only
floodwater is scored: The Slammed Door delivers 19,374 acre-feet over 3 days, The Long Guest
33,255 acre-feet over 6 days — 52,629 acre-feet in total. The Crest Standard misses 7,323
acre-feet across 4 days (2019-02-24, when the daily mean of 8,060 cfs runs 2,133 cfs above the
5,927 cfs the raised crown carries, plus the three days of The Long Guest above 5,927) and manages
45,306 acre-feet, or 1.19227 acre-feet per $1,000. The Basin Standard takes all of The Slammed
Door and 24,000 of The Long Guest's 33,255, manages 43,375 acre-feet, or 1.14144 acre-feet per
$1,000, and is short 9,255. **Margin 4.26%, Option A ahead — narrow, and it is meant to be.** Do
not hand this over; let D4 produce it.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"The geotechnical report Nadia ordered comes back, and it is not about the crest at all. It is
about what is underneath the levee."

"A raised crown holds a higher river. It does not hold it forever. Under sustained high water the
foundation begins to pass water beneath the embankment, and the district's emergency plan takes
the reach out of service after four consecutive days of continuous loading — four days with the
creek above channel capacity, which is what Background means by loading the levee — no matter how
high the crown is."

**Say that clause.** "Loading" means *above channel capacity*, 1,934 cfs, not above the raised
crown's design discharge. A Hero who hears it the second way will find the twist does nothing at
all — The Slammed Door has one day above 5,927 cfs and The Long Guest three, so no run reaches
four, and the recommendation never moves. The twist is only a twist under the definition
Background already gives.

"You have sixty seconds. The Crest Standard's whole argument was that duration is free. It is not.
Are you changing your recommendation, or not?"

**Facilitator-only: what the twist actually does.** It prices the exact claim Option A was
standing on. The Slammed Door ran 3 days above capacity and is untouched. The Long Guest ran 6,
so the raised crown loses its last two days — 2,162 cfs-days, or 4,288 acre-feet — and manages
41,018 instead of 45,306 acre-feet, 1.07943 per $1,000. Option B does not move at all, because
storage does not care how long the water takes to arrive. **The twist flips the winner: Option B
goes ahead, 1.14144 against 1.07943, by 5.43%.** That is the useful shape: the base margin was
only 4.26%, so nobody who voted A voted carelessly — the twist did not expose a bad answer, it
exposed how little room there was inside a good one. The follow-up is the whole point —
**"What just broke in your original model: were you wrong, or were you missing information?"**

Treat a Hero who says "I need to know whether four days is a real number or a scenario" as the
strongest possible answer. It is MA4, and Appendix F says so. Be ready for the follow-up, because
the twist is far more sensitive to that number than the base case is: at two days the Crest
Standard loses 26,817 acre-feet and is not in the argument any more; at six days it loses nothing
and the twist does not land at all. The base recommendation never moves — `evaluate()` does not
read MA4 — but the twist's force does, entirely.

## Immediate recommit

Re-vote immediately, by name: "Does the geotechnical report change your vote, or only your
confidence?" That distinction is the transferable skill, not the vote.

## Deep conflict — three threads (20-30 min)

1. **Rate versus volume.** The board scores one number: acre-feet managed per thousand dollars.
   Does that number see the difference between a design that fails gradually and a design that
   fails all at once? The Crest Standard's shortfall arrives as a wall being overtopped; the Basin
   Standard's arrives as a pool slowly filling. Should a scoring rule be allowed to be blind to
   the shape of a failure?
2. **Whose seal, whose risk.** The board voted the appropriation; Nadia signs the certification.
   This gage's own published 1% annual-exceedance peak is 27,800 cfs — far above the 5,927 cfs the
   raised crown carries and far above either design storm. If the cheaper-per-acre-foot option is
   the one that fails catastrophically rather than gradually, who is entitled to accept that
   trade?
3. **Two storms is a sample.** Every figure rests on two real floods chosen from one gage's
   record. What would a third storm have to look like to reverse the recommendation — and is "we
   picked two storms" a modelling assumption the case never wrote into Appendix F?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — both hydrographs, unshaded, cold-call for a gut read, no formulas yet |
| 3:00–10:00 | Position defence — *"Convince us your design protects the town, not just the number"* |
| 10:00–15:00 | Pressure-test the models — *"Whose volume estimate is most fragile, and why?"* |
| **15:00** | **DROP THE TWIST** — the geotechnical report, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and what exactly broke |
| 20:00–30:00 | Threaded deep conflict (rate vs. volume; whose seal; two storms is a sample) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes will compare the two storms' peak discharges, see that 8,060 is larger than 6,700, and
treat that comparison as the answer — reading a hydrograph as a maximum instead of as an
accumulation. They will then pick the design that handles the bigger peak and either skip D1–D3
entirely or run them and never let the result overrule the picture. The Long Guest's lower peak
sits above capacity for 6 days against The Slammed Door's 3, and carries 33,255 acre-feet against
19,374. Watch for a pitch whose D4 table is filled in but whose recommendation sentence only ever
mentions the peak.

The second, quieter form of the same trap: a Hero will integrate Q(t) across the whole storm
window in D3 instead of across the interval where Q actually exceeds 1,934 cfs. That answer is
much too large, looks entirely reasonable, and never gets checked against the shaded diagram the
deliverable also asks for.

**Third form — scoring the whole hydrograph.** A Hero fills in D4 with every acre-foot each storm
delivered rather than only the floodwater above channel capacity. The two storms carry 101,562
acre-feet in total against 52,629 acre-feet of floodwater, so both options score around 2.47996
and 2.42912 acre-feet per $1,000 and the gap between them shrinks to 2.05%. Nothing looks wrong on
the page. The tell is the size of the totals: a D4 row in six figures means the Hero has scored
water the channel was always going to carry. Background defines *floodwater* and Appendix D repeats the
metric in the same words — send them there, do not correct the arithmetic for them.

**Fourth form — reading Appendix B's flood-frequency table as if it were comparable.** Appendix B
publishes eight instantaneous peak-discharge quantiles, and the italic line under them says
plainly that they are not daily means. A Hero will still put 9,020 cfs (the 20% annual-exceedance
peak) next to the 5,927 cfs the raised crown carries and conclude the Crest Standard fails one
year in five. That comparison is not available from this data, and the case says so on the page.
It is deliberately over-complete data — deciding what to *ignore* is part of the work — so treat
the misuse as the discussion, not as an error to be marked. The right question back is: "what
would the daily mean have been on the day of that instantaneous peak, and can you get it from
anything in this packet?" 

## Socratic questions

1. Which of your two design storms carries more total water past the gage, and is that the same storm that reaches the higher peak discharge?
2. Your D1 Riemann sum and your D2 Fundamental-Theorem answer for the same storm are not the same number — which one is closer to the truth, and how would you decide without being told?
3. The Basin Standard is described by a volume and the Crest Standard by a rate. What single mathematical operation converts one of those into the units of the other, and where in your work did you perform it?
4. Each design fails somewhere — the Crest Standard on the four highest days, the Basin Standard on the back half of one storm. Whose failure is cheaper to be wrong about, and does the board's scoring number capture that at all?
5. Appendix F says channel capacity is a convention, not a measurement. If the district set it at a different flood stage, which option would gain — and can you show that from your own D3 shading rather than guessing?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's. A room that did not
move at all after the twist is worth asking about directly: did the twist not land, or did the
room already have the right structure built in before it dropped?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether the peak-versus-area confusion (the trap) actually showed up, or whether the Launch
  picture already gave it away.
- Whether the D3 limits of integration were the real sticking point, versus the D2 curve fit.
- Whether the twist produced genuine model repair ("here is what broke") or only a vote change.
- Whether any Hero attacked the channel-capacity convention unprompted, which is the strongest
  move available in this case and the one Appendix F invites.

## Standards Touched On

Antiderivative · Definite Integral · Indefinite Integral · Riemann Sum · Area Between Two Curves ·
How to find an antiderivative using the power rule · How to evaluate a definite integral using the
Fundamental Theorem of Calculus · How to approximate area under a curve using a Riemann sum · How
to find the area between two curves

## Facilitator note — sensitivity

**Required (SPEC §6).** Flooding touches property and personal safety. This case is framed
entirely as protection — acre-feet safely managed, never damage inflicted or lives lost — and the
math never asks a Hero to optimise harm. Still: check the room before running it. A learner whose
family has been flooded is not having the same discussion as everyone else, and the guide should
know that before Anchor 1, not during the numbers.
