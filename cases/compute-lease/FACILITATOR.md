# FACILITATOR.md — The Compute Lease

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Compute Lease · **Tier:** T2 (MS-core) · **Studio:** Heroes Academy
**Standards:** Calculus/Series — Series, Sequence, and How to determine whether a series converges
or diverges (see `case.json.standards[]` for exact ids).

**Status:** Researched and computed 2026-08-27; Appendix D **retuned 2026-08-30** (see below). All
10 `{{NEEDS_SOURCE}}` tokens in `case.md` are closed (`RESEARCH_LOG.md`). The D4/D5 arithmetic is
done and recorded below and in `case.json.balance`.

**Retune history, read before you facilitate:** the 2026-08-27 pass found the Long Lock beating
the Open Tap at **every** growth scenario in Appendix D (Low 36.5%, Mid 63.5%, High 76.4%), all
well past SPEC §2's ~20% cap — not a close race. The case owner retuned Appendix D on 2026-08-30:
the growth-rate range was re-sourced from DigitalOcean Holdings (NYSE: DOCN), a real mid-size
cloud infrastructure company, replacing the original hyperscaler-scale proxies (largest AI data
center, notable-model training compute) that never fit Kestrel's own stated mid-size scale. MA1
(512 GPUs), MA2 (120,000 GPU-hrs/month), and both sourced rates (S1/S2, $6.88/$2.97) are
**unchanged** — checked and confirmed those levers alone could not have fixed the imbalance (see
`case.json.balance.margin_note` for why: even 100%-utilization of the committed cluster only pulls
Long Lock's cost down to its own flat rate, a 56.8% margin against Open Tap — still triple the
cap). **The winner flips**: Open Tap now wins at all three retuned scenarios (Low 15.4%, Mid 9.1%,
High 4.6%), all comfortably inside the cap, with a real crossover point (~2.48%/month, ≈34.2%/year)
that the new range approaches but does not reach. This is a genuine, honestly-sourced retune, not
a number picked to clear the cap — see `RESEARCH_LOG.md`'s 2026-08-30 entry for the full search
trail. **The discussion below is rebuilt around this new result** — read past the old capacity-
ceiling Twist description if you facilitated an earlier draft of this case; it has been replaced
(see Twist section).

## Intro

Frame the format before anything else: this is a real capital-commitment decision with a board
meeting two days out, not a worksheet. Name the opener — "You are Kestrel's infrastructure
capacity planner. Two windows open on your laptop, two completely different ways to buy the same
GPUs, and your name on the cost line either way." Let the stakes land before moving to the Launch.

## Launch

Show Appendix B and Appendix C side by side, rates only — $2.97/GPU-hr fixed vs. $6.88/GPU-hr
on-demand — with no other numbers yet. Ask: "Which one do you think a growing company should pick,
just looking at those two rates?" Do not confirm or correct answers here. Most rooms will jump to
"obviously the cheaper rate" — that instinct is worth recording out loud before anyone touches the
growth-rate appendix, because it is exactly the trap (see below), even though this time the trap
does *not* point at the answer key's winner — see "The trap" for why that matters.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the Open Tap — the option with the *higher* rate?" Show
of hands, both options, no discussion. Record the count — Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'cheaper'?"**

Let confusion grow here — this is deliberate. Heroes will want to jump straight to "which rate is
lower," but push on what "cheaper" even means when one option's total bill depends on how much
gets used and the other's doesn't: "If Kestrel signs the Long Lock and then barely uses it, is
$2.97/GPU-hr still the cheap option? What has to be true for a lower rate to actually mean a lower
bill?" If the room lands on "cost per GPU-hour delivered isn't the same as the rate on the price
sheet" on its own, the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "which rate is lower" from "which total cost per GPU-hour delivered is
lower," ask them to name the actual steps before touching the appendices: build the 24-month
demand sequence under all three growth scenarios (D1), write both options' 24-month cost series as
explicit sums (D2), classify the Open Tap's underlying series for convergence if growth held
forever (D3), divide each option's total cost by GPU-hours delivered for all six option-scenario
combinations (D4), and find the exact growth rate where the two options tie (D5). Re-ask: "Is our
question still the right one, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gaps honestly: Appendix A's cluster size (MA1, 512 GPUs) and starting demand
(MA2, 120,000 GPU-hours/month) are both stated Modeling Assumptions, not sourced figures — Kestrel
is a fictional company, so no real business supplies them. Ask which one actually changes the
*graded* D4/D5 results if it moves. The honest answer is **both, heavily** — these two are the
single most load-bearing inputs in the whole case: MA1 sets the Long Lock's fixed monthly cost
floor, and MA2 is the seed value for every month of D1's demand sequence under every growth
scenario, so it feeds every D2/D4/D5 result directly. Let a sharp Hero find this themselves before
confirming it. If a Hero asks *why* Appendix D's growth rates look like an actual company's own
earnings numbers rather than a rounder, more "textbook" range — that's a fair question, and the
honest answer is in Anchor 4's spirit too: real company data is what this case's growth-rate range
is now built from (DigitalOcean's own quarterly results), on purpose, not to make the arithmetic
cleaner.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's demand sequence, D2's two cost series, D3's convergence
classification, and D4's six-result table together as a room, cold-calling for D4 specifically —
this is where a Hero who computed D1/D2 correctly but never divided by GPU-hours *delivered*
(rather than dollars alone) will visibly struggle to explain why the Open Tap keeps winning by a
*narrower* margin as growth increases, not a wider one — the opposite direction from what
Argument A's framing might lead them to expect. That struggle is useful information for the
facilitator, not a moment to rescue.

**Facilitator-only arithmetic note.** Long Lock's 24-month total cost is constant regardless of
scenario: $2.97/GPU-hr × 512 GPUs × 730 hr/month × 24 months = $26,641,608. Open Tap's cost per
GPU-hour delivered is trivially constant at $6.88 under this case's reading (its total cost is
exactly rate × hours delivered, so the ratio always returns the rate). D4's six results: Low
(1.1%/month) — Long Lock $8.13/GPU-hr vs. Open Tap $6.88, **Open Tap wins**, margin 15.4%. Mid
(1.7%/month) — Long Lock $7.57 vs. $6.88, **Open Tap wins**, margin 9.1%. High (2.1%/month) —
Long Lock $7.21 vs. $6.88, **Open Tap wins**, margin 4.6%. D5's crossover growth rate is
≈2.48%/month (≈34.2%/year) — *above* Appendix D's entire 1.1%–2.1% stated range, meaning the Open
Tap wins under every one of the case's own sourced scenarios, but the race tightens noticeably
toward the top of the range (High's 4.6% margin is a near-tie). Full derivation in
`case.json.balance.margin_note`.

## Twist — drop this at ~15 minutes into the discussion

**This Twist replaces the original capacity-ceiling twist** (retained below the fold for context).
Under the retuned Appendix D range, Kestrel's demand never gets remotely close to the 512-GPU
physical ceiling within the 24-month window — even at the High scenario, the case's own numbers
put that crossing over 50 months out. The capacity-ceiling twist has nothing to bite on anymore,
so it has been replaced with one built from the same source this retune already cites.

Deliver slowly, with pauses:

"The 22%, and the 29%-guided, growth figures Appendix D borrows are DigitalOcean's *realized and
guided revenue* growth. The same earnings release that gives you the 29% figure for Q2 2026 also
discloses something else: DigitalOcean's *booked-but-not-yet-realized* future business — contracts
already signed, revenue not yet counted — grew more than 10 times year over year. And in the same
release, DigitalOcean told investors it now expects *2027* revenue growth to exceed 50% — far
above anything in Appendix D's range."

"If Kestrel's own sales pipeline looked anything like that — bookings racing ahead of realized
revenue — would you trust Appendix D's range to hold for the full 24 months? Does that change what
Sofia should recommend?"

**Facilitator-only: what this actually does, and does not, change.** The 50%-plus 2027 guidance
and the "10X RPO growth" figure are both real, already-sourced numbers (`S4`'s own source) — this
twist introduces no new figure, it reuses the case's own citation more fully than Appendix D's
table alone captures. It does **not** change D4/D5's arithmetic or which option wins under
Appendix D's own stated range — the Open Tap still wins Low/Mid/High. What it *does* do is put real
weight behind a question the primary metric alone cannot answer: **is Appendix D's range even the
right range for the growth Kestrel might actually see?** D5's crossover point (≈34.2%/year) sits
*below* DigitalOcean's own 2027 guidance (over 50%) — meaning if Kestrel's own trajectory
resembles DigitalOcean's disclosed forward acceleration rather than its trailing 12 months, the
Long Lock could win instead. The case has no sourced way to say which trajectory Kestrel will
actually follow — inventing one here would be exactly the fabrication SPEC §5 forbids. **The twist
reframes, it doesn't resolve:** a recommendation defended only by "Appendix D's own range favors
the Open Tap" has not yet grappled with whether that range is the range Kestrel will actually see,
and a Hero who never checks D5's crossover against anything outside Appendix D's own four corners
has not really pressure-tested their answer.

<details>
<summary>Superseded twist (pre-2026-08-30 retune) — kept for continuity, do not use</summary>

The original twist used the physical 512-GPU capacity ceiling (373,760 GPU-hrs/month): under the
*prior* (faster, hyperscaler-proxied) growth range, demand crossed that ceiling within the 24-month
window (month 9–20 depending on scenario), raising a real question about what happens to demand
above the committed cluster's physical limit. Under the *retuned*, slower DigitalOcean-based
range, that crossing does not occur until roughly 54.7–103.9 months out (High 54.7, Mid 67.4, Low
103.9 — see `case.json.derived`) — outside the evaluation window entirely under all three
scenarios — so this twist no longer has anything to reveal. MA1
(512 GPUs) itself is unchanged and still real; the capacity ceiling simply is not reached by any
scenario this case now models. If a future retune ever pushes the High scenario's growth rate back
up near or past D5's crossover, this capacity-ceiling twist becomes usable again largely as
originally written.

</details>

## Immediate recommit

Re-vote immediately. Ask by name: "Does the RPO/2027-guidance signal change your vote — or does it
just tell you that Appendix D's range, however well-sourced, is still a bet on which part of one
real company's growth story Kestrel's own trajectory will resemble?" That distinction is the
transferable skill, not the vote itself.

## Deep conflict — three threads (20–30 min)

1. **A cheaper rate is not always a cheaper bill — but this time, "the cheaper bill" is also the
   one you might have expected.** The Open Tap's rate is more than double the Long Lock's, and it
   still *wins* on cost-per-GPU-hour-delivered at every sourced growth scenario — this lines up
   with the "never pay for capacity nobody rents" intuition many rooms reach for at Anchor 1, which
   makes it easy to mistake "the intuitive answer happened to be right" for "the intuitive
   *reasoning* was right." Push on whether a Hero who voted Open Tap at Anchor 1 purely on "the
   fixed rate feels riskier" can actually explain *why* it wins using D4's ratio — not just that it
   does.
2. **The margin narrows with growth, not widens.** A Hero expecting "committing to a fixed rate
   pays off more the faster you grow" (Argument A's framing) will be surprised that the Open Tap's
   lead *shrinks* from 15.4% (Low) to 4.6% (High) as growth increases. Why does more growth help
   the *loser* (Long Lock) close the gap here, even though it never wins within Appendix D's range?
   What does that trend, extended further, predict about growth rates *above* the stated range?
3. **What a well-sourced range can't tell you.** The twist introduces a real, sourced signal
   (DigitalOcean's own forward guidance and booked pipeline) suggesting growth could plausibly run
   well above Appendix D's range. Is a well-sourced *historical* range enough to defend a
   24-month capital commitment, or does "the same source hints growth could accelerate past the
   range" cut the other way — toward treating D5's crossover as a real risk to flag, not a reason
   to abandon the D4 numbers?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both rates side by side, cold-call for a gut read, no other numbers yet |
| 3:00–10:00 | Position defense — *"Convince us your option actually costs less per GPU-hour delivered, not just per rate quoted"* |
| 10:00–15:00 | Pressure-test the models — *"Where in Appendix D's range does your recommendation actually flip?"* |
| **15:00** | **DROP THE TWIST** — DigitalOcean's own RPO/2027-guidance signal, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (intuition vs. reasoning; why the margin narrows with growth; what a well-sourced range can't tell you) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Heroes will compare the two options' 24-month total dollar spend directly — not their cost *per
GPU-hour delivered* — and conclude whichever number is smaller in isolation is the better choice.
That comparison silently assumes both options deliver the same amount of usable GPU-hours to
paying customers, which is exactly what is *not* true: the Long Lock's fixed capacity sits there
whether or not customers rent it, so at these retuned (slower) growth rates the Long Lock is paying
the same total dollars for far fewer *delivered* GPU-hours than a naive total-dollar comparison
would suggest, which is exactly why it loses. **A second, sharper trap specific to this case's
current numbers:** a Hero who votes for the Open Tap at Anchor 1 purely on "never overpay for
unused capacity" gut instinct, and then never runs D4 at all, still lands on the *correct* option —
but for the wrong reason, and without the tools to know *how close* the race actually is (4.6% at
the High scenario) or *where* it flips (D5's crossover, ≈34.2%/year, sits below DigitalOcean's own
disclosed 2027 guidance). A Hero who "got lucky" on the vote but cannot produce D4/D5 has not
actually done the case.

A third, related trap: treating Appendix D's own stated range as the *entire* space of plausible
outcomes rather than checking what the crossover point implies about growth *outside* that range.
A Hero who computes only the mid-scenario result and stops has not yet found out whether the
recommendation is robust across the whole plausible range — or fragile just past its edge, which,
in this case, it is: the crossover (≈34.2%/year) sits only about 5 points of annualized growth
above the High scenario (29%/year), not comfortably beyond it.

## Socratic questions

1. Your D4 table shows six different cost-per-GPU-hour-delivered results — two options across three growth scenarios. Do the same six numbers all point to the same recommendation, or does the answer actually change depending on which scenario you believe?
2. The Long Lock's contract term runs longer than the 24-month window you were asked to evaluate. If you only look at the 24-month cost-per-GPU-hour number, what cost is your evaluation quietly leaving out — and does that omission favor the Long Lock or the Open Tap?
3. Your D3 classification says the Open Tap's underlying growth series diverges if the growth rate held steady forever. Kestrel isn't actually committing to "forever" — so why does that divergence result matter to a two-year decision at all?
4. Your D5 crossover rate tells you the exact growth rate where both options tie. Is that crossover rate inside or outside Appendix D's stated range — and what does that position tell you about how confident Sofia should be in her recommendation?
5. If Kestrel's actual growth rate turned out to be *outside* Appendix D's stated range entirely — faster than anything Appendix D models, closer to the same source's own 2027 guidance — which option would be more painful to be locked into, and why?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that voted for
the Open Tap at Anchor 1 purely on "the fixed rate feels riskier" and stays with the Open Tap after
the twist for a *different, numbers-and-crossover-based* reason has genuinely moved, even if the
vote count looks unchanged. A room that flips *toward* the Long Lock after the twist should be
pressed to say exactly why — "the crossover is close to a real forward-guidance number" is a
defensible answer; "the twist felt like it wanted us to switch" is not.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Anchor 4's "both MA1 and MA2 are heavily load-bearing" finding landed as a discovery or
  had to be told outright.
- Whether Heroes who voted Open Tap at Anchor 1 on gut instinct alone could still produce a correct
  D4/D5 justification when asked — or whether "got the right answer, couldn't show the work" turned
  out to be the actual sticking point this case surfaces, given the vote and the metric now agree.
- Whether the DigitalOcean RPO/2027-guidance twist felt like a genuine new complication or felt
  like a facilitator reaching outside the case for a plot twist — worth listening for directly,
  since the twist deliberately reuses an already-cited source rather than introducing a new one,
  and that distinction may or may not read clearly to a room in the moment.
- Whether a room found it more or less satisfying that this case's math now points the "expected"
  direction (favor the option that adapts to usage) compared to the pre-retune version, where the
  math cut against that intuition — and whether that changes how hard the facilitator has to work
  to keep the room honestly engaging with D4/D5 rather than coasting on the vote.

## Standards Touched On

Series · Sequence · How to determine whether a series converges or diverges

## Facilitator note — sensitivity (SPEC §6)

NONE. This is routine infrastructure-procurement and cost-modeling math — no subject-matter
sensitivity flag applies. `case.json.sensitivity_note` records the load-bearing modeling
assumptions (MA1/MA2) instead, which is a different (non-§6) kind of note.
