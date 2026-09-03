# FACILITATOR.md — The Fee Ladder

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Fee Ladder · **Tier:** T2 (MS-core) · **Studio:** Adventure
**Standards:** Discrete Mathematics/Proof And Recursion — Recursive Formula, How to write a
recursive formula for a sequence, How to convert a recursive formula to an explicit formula (see
`case.json.standards[]` for exact ids).

**Status:** `case-research` complete (2026-09-01) — all 10 `{{NEEDS_SOURCE}}` tokens closed (3
SOURCED, 7 ASSUMPTION, 0 DROPPED, 0 OPEN; see `RESEARCH_LOG.md`). `case.json.status` is
`"researched"`. `margin_pct` is `13.32` — not `null`. Not yet run through `case-qa`; treat the
numbers as sourced-and-computed but not yet QA-adjudicated.

## Real-world grounding (for the facilitator's own background, not for case.md)

- **State Street Bank and Trust Company — two real, filed custody fee schedules.** The Gabelli
  Global Small and Mid Cap Value Trust schedule (0.50 bp first $500M / 0.3875 bp remainder) and the
  Green Century Funds schedule (7.0 bp first $150M / 4.0 bp excess) are both real SEC-filed
  exhibits to real custody agreements. Together they show the real range custody bp rates span
  (roughly 0.4–7 bp) depending on fund/account scale — this is the real anchor for Appendix C's
  fictional ladder's rate magnitudes (2.00/1.25/0.75/0.50 bp), not a guess.
- **Both real schedules are standard marginal-bracket schedules** — each tier's rate applies to a
  fixed dollar range of the *original* balance, exactly like a tax bracket. Meridian's fictional
  ladder (Appendix C) is deliberately *not* built that way — it is a stated Modeling Assumption
  where each tier's rate applies to the balance remaining *after* the previous tier's own fee was
  subtracted, which is what makes it a genuine sequence recursion (Bₖ defined in terms of Bₖ₋₁)
  instead of a standard bracket sum. This is a disclosed authorial choice (Appendix E's note in
  case.md says so explicitly) — a facilitator should be ready to explain, if asked, that real
  custody schedules are *not* usually built this way, and that's fine: the case says so.
- **SEC v. State Street, Press Release 2019-114 (2019-06-27).** A real enforcement action: State
  Street collected $170 million in overcharges from custody clients from 1998–2015 (including $110
  million from an undisclosed SWIFT-messaging markup) and paid over $88 million to settle. This is
  the real-world stakes anchor for Appendix F and for the Twist — a real custody bank really did
  get a client-facing number wrong (in that case, deliberately hidden) for *years*, and it cost real
  money and real reputational damage once discovered.
- **The scale-invariance finding (D4) is provable, not just observed.** Because both the Quick-Quote
  (linear in AUC) and the Full Ladder's true fee (homogeneous of degree 1 in AUC, since Bₖ =
  B₀·∏(1−rᵢ) is a straight scalar multiple of B₀) are linear functions of the client's balance,
  their ratio — and therefore the percentage error between them — is mathematically guaranteed to
  be the same number at every AUC size. This was verified computationally at three different sizes
  (case.json.balance.margin_note) and is worth having the room *prove* algebraically in Anchor 3 or
  the Data Deep Dive, not just observe numerically.

## Intro

Frame the format: this is a real "what number do I say on the phone in the next ten minutes" ops
decision, not a worksheet. Name the opener — "You have one number to give sales, right now, for a
client worth a multi-year relationship. One version of that number takes ten seconds to produce.
The other takes hours, and gets you the actual, provably correct answer. You don't have hours."

## Launch

Show the two tabs exactly as the Overview describes them — the Quick-Quote card (one number) and
the Full Ladder spreadsheet (four rows, waiting to be walked) — with no rates or dollar figures
yet. Ask: "Which one would you read over the phone, just from what you see here?" Do not confirm or
correct. Record the split; Close will re-ask it.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the Quick-Quote — the flat number nobody recalculated
for this specific client?" Show of hands, both options, no discussion yet. Record the count.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'recursive'?"**

Let confusion grow here on purpose. Heroes will want to jump straight to "which fee is bigger,"
but push on what "recursive" actually means in Appendix C: "If Tier 2's rate applies to the balance
*after* Tier 1's fee was already taken out, does the order of the tiers matter? What if Meridian
ran Tier 4's rate first and Tier 1's rate last — would the total fee change?" (It would, very
slightly — worth letting a Hero discover that recursion is *order-dependent* in a way a flat sum
is not, even if the numeric effect here is tiny.) If the room lands on "a recursive rule tells you
how to get the next value from the value you already have, not a shortcut to skip ahead," the case
is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "which number is bigger" from "which number is actually correct," ask them
to name the actual steps before touching the appendices: write the recursive rule itself (D1);
walk it tier by tier for today's client; convert that recursion into an explicit, non-recursive
formula by substitution (D2); use both to build the fee-quote-error table (D3); check whether that
error changes at other client sizes (D4); and decide, using all of that, which method Marcus should
actually use today (D5). Push the room to *predict* D4's answer before computing it: "Do you think
a flat-rate approximation gets more accurate, less accurate, or stays the same as the client gets
bigger?" Most rooms will guess "more accurate" (bigger client, bigger numbers, errors wash out) —
that intuition is wrong here, and D4 is built to catch it.

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gap honestly: Meridian is fictional, so its client's exact AUC, its own internal
four tier rates, and its Quick-Quote card's flat rate are all stated Modeling Assumptions, not
independently verifiable facts — unlike the *shape and scale* of real custody bp fee schedules
(Appendix E), which is anchored to two real, filed SEC exhibits. Ask which of the open figures is
actually load-bearing for the recommendation. The honest answer: MA5 (the card's flat rate) and
MA6 (the ladder's four tier rates) are the two that set `margin_pct` — everything else (client size,
deadline length, number of tiers) is flavor or structural, not numerically load-bearing.

## Data Deep Dive

Now, and only now, the numbers (once `case-research` has closed Appendices A–D). Walk D1's
tier-by-tier recursion, D2's explicit-formula derivation, D3's error table, and D4's sensitivity
check together as a room, cold-calling for D2 specifically — this is where a Hero who wrote a
correct D1 recursion but can't actually *substitute it into itself* to get an explicit formula will
visibly struggle. Have the room verify D4's surprising finding by testing it themselves at a fourth
AUC size they pick.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses, once Appendix F is sourced: "There's a real bank — not Meridian, a
real one — whose custody clients were billed the wrong number for seventeen years. Not because
anyone did the recursive math wrong. Because a flat markup got added to a bill once, quietly, and
nobody ever recalculated it against what the real, correct charge should have been. When regulators
finally checked, that bank had collected a hundred and seventy million dollars more than it should
have — and had to pay back tens of millions more on top of that once it got caught."

"Marcus isn't hiding anything — the Quick-Quote card is published, approved, and everyone at
Meridian knows it's an approximation. But if every quote off that card is *always* off by the same
13.32%, in the same direction, for years, on every client big enough to matter — is that
meaningfully different from what happened to that real bank? What exactly would have to be true for
the Quick-Quote to be a defensible shortcut instead of a slow-motion version of the same problem?"

**Facilitator-only: what this does and doesn't change.** This is the real SEC/State Street
settlement (see grounding section above) — it does not change D3/D4's numbers, and it is not proof
that Option A is fraud (it isn't — the card is published and approved, not hidden). It is proof
that "everyone knows it's an approximation" and "the approximation is small enough not to matter"
are two different claims, and a Hero who conflates them has not fully reckoned with what a
guaranteed, scale-invariant 13.32% error actually compounds into over a multi-year relationship.

## 45-Minute Socratic Plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch (Intro/Launch above), 30-second commitments, stand/sit vote (Anchor 1) — no explanation. |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just fair" (Anchor 2 — what does "recursive" actually buy you over a flat sum?). |
| 10:00–15:00 | Pressure-test the models: process and open assumptions (Anchors 3–4) — name the D1–D5 steps, predict D4's answer before computing it. |
| 15:00–25:00 | Data Deep Dive — D1–D5 together; cold-call D2's substitution steps specifically. |
| **25:00** | **DROP THE TWIST** — the real State Street/SEC settlement, delivered slowly, with pauses. |
| 25:00–30:00 | Immediate recommit: who reverses? "What just broke — the math, or your read of how much a 'small' error is allowed to matter?" |
| 30:00–40:00 | Threaded deep conflict — see the three named threads below. |
| 40:00–45:00 | Close, re-vote, reflection, Lessons Learned. |

## Deep conflict — threads (30–40 min)

1. **A fixed-percentage error on a linear system never shrinks.** D4's finding (13.32% at every
   client size) surprises most Heroes, who expect flat-rate approximations to "average out" on
   bigger accounts. Push: "If margin_pct doesn't change with client size, does it matter that
   Meridian's biggest institutional clients are the ones this quote is most likely to be used on?"
2. **Recursive is not automatically more accurate than flat — it just tracks a different
   assumption exactly.** A Hero who treats "recursive" as a magic-better-answer button without
   being able to say *what* the recursion is tracking (balance-after-fee, not balance-in-bracket)
   has missed the actual structural difference the case is built around. Push: "If Meridian
   switched to a standard marginal-bracket schedule instead (Appendix E's real structure), would
   D1's recursion still be the right tool — and would the Quick-Quote's error look the same?"
3. **Published-and-approved vs. small-and-unnoticed.** The Quick-Quote card is not secret — but
   the Twist's real precedent involved a markup that also wasn't originally secret from the bank's
   own decision-makers, just never checked against the true number once client-facing pressure took
   over. Push: "What's the actual difference between a disclosed shortcut and an undisclosed one, if
   neither one gets rechecked against the true number for years?"

## The trap

Heroes will treat "recursive is exact, flat is an approximation" as reason enough to always pick
Option B, without ever running D4 — missing that a fixed, scale-invariant 13.32% error might
genuinely be an acceptable, known, bounded cost of speed under a real deadline, not an open-ended
risk that grows with every new client. A second, related trap: treating D1's recursion as
automatically "more correct" than a flat sum without being able to say structurally *why* — a Hero
who cannot explain, using Appendix C's own definition, why Bₖ depends on Bₖ₋₁ rather than on a
fixed bracket of B₀, has not actually engaged with what makes this a recursion problem instead of
an ordinary percent-of-total problem.

## Socratic questions

1. Your D2 explicit formula and your D1 tier-by-tier walk should give the same total fee. If a Hero's two answers disagree, is the recursion wrong, the explicit formula wrong, or an arithmetic slip somewhere in between — and how would you find out which?
2. D4 shows the Quick-Quote's percentage error is the same at $300 million, $850 million, and $1.2 billion. Using D2's explicit formula (not a calculator), can you explain in words *why* that has to be true, without computing a fourth example?
3. The twist describes a real custody bank that collected $170 million in overcharges over seventeen years before anyone caught it. Is Meridian's Quick-Quote card the same kind of problem, a smaller version of it, or a genuinely different situation? What would you need to know to tell the difference?
4. Appendix A gives Marcus under an hour and estimates the Full Ladder computation takes about three hours to do properly. If that deadline were instead a full business day, would your D5 recommendation change? What does your answer say about whether this is really a math problem or a scheduling problem?
5. If Meridian's pricing desk recalibrated the Quick-Quote card's rate to exactly match the Full Ladder's true blended rate (4.499306 bp) for this one AUC band, would the dilemma in this case disappear? What would still be true about the two methods even if margin_pct dropped to 0%?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare to Anchor 1's vote — a room that moves after the twist
should be pressed to explain the move using D3/D4, not just the twist's emotional weight.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

## Standards Touched On

Recursive Formula · How to write a recursive formula for a sequence · How to convert a recursive
formula to an explicit formula

## Balance argument (SPEC §2)

**Argument for A (the Quick-Quote).** It is read off the card in seconds, comfortably inside
Cassidy's one-hour deadline (Appendix A), and — because it undercharges relative to the true
recursive fee — it hands sales a more competitive number in a room where a rival custodian is
already circling. It is also a published, pricing-desk-approved number, not something Marcus
invented under pressure.

**Argument for B (the Full Ladder).** It is exact, not an estimate, and the only one of the two
numbers Marcus could actually defend tier-by-tier to the client's own finance team or to Meridian's
compliance desk. Real precedent (Appendix F, the State Street/SEC settlement) shows what an
indefensible custody-fee number can cost a bank once it is checked years later — $170 million in
overcharges, over $88 million to settle. A quote that is off by a real, computable, scale-invariant
13.32% every year, for the life of a multi-year relationship, is a real and recurring cost.

**Margin — COMPUTED 2026-09-01 (case-research).** `margin_pct: 13.32`. At AUC = $850,000,000: the
Full Ladder's true total fee is $382,441.03 (tier-by-tier: $170,000.00 / $106,228.75 / $63,729.28 /
$42,483.00); the Quick-Quote's flat fee is $331,500.00. Gap = -$50,941.03 (Option A undercharges).
margin_pct = 50,941.03 / 382,441.03 × 100 = 13.32%. **This is comfortably under SPEC §2's ~20% cap
— no retune or waiver needed.** Verified scale-invariant: re-run at $300,000,000 and $1,200,000,000
(Appendix D) gives 13.32% both times as well (full arithmetic trail in `case.json`'s
`balance.margin_note`).

**What this means for facilitation.** Both options are genuinely defensible on the numbers: B wins
decisively on accuracy and long-run defensibility; A wins decisively on meeting today's deadline and
on the deal's competitive dynamics. The room's real work is weighing a known, bounded, ~13%
recurring error against a three-hour delay Marcus does not have — not disputing whose number is
"the real one" (both are real, correctly-computed numbers under their own stated method).

## Facilitator note — sensitivity (SPEC §6)

NONE. This is routine financial-operations math (a fee-quote decision under a deadline) — no
subject-matter sensitivity flag applies. The real external precedent (Appendix F/S3) involves
corporate regulatory penalties, not personal harm, illness, or financial hardship to an individual.
