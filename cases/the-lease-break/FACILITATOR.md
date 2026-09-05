# Facilitator Notes — The Lease Break

**Status:** `case-readiness` remediation complete (2026-09-04, two rounds). All sources/assumptions
in `case.json` are resolved (S1–S8, MA1–MA10); `balance.margin_pct` is computed per scenario (see
below). Treat every number below as the case of record, not a placeholder. This document is
facilitator-only — never copy any of this into `case.md`.

**RESOLVED FINDING, round 1 (case-readiness, 2026-09-04, re-entered at case-write/case-research):**
the prior pass (case-qa, 2026-09-03) found The Cedarline cheaper in BOTH scenarios (stay-full-term
by 16.9%, break-at-month-6 by 6.6%), so the case had no genuine scenario-dependent reversal. New
real-world research found two independent sources (S7, S8) documenting that early-termination fees
run 2-4 (S7) / specifically 3-4 (S8) months' rent when several months remain on a lease — exactly
Maya's break-at-month-6 situation, which is *not* the ordinary 1-2 month case S5 alone would
support. MA2 (The Cedarline's termination penalty) was revised from 2 to 3.5 months' rent on that
basis, restoring a genuine reversal. A Tier 2 twist-integrity probe also found the discussion
Twist's mapping onto D2/D3 relied on an unstated convention (how long an extension runs) — fixed by
adding **MA10**.

**RESOLVED FINDING, round 2 (case-readiness Tier 2 P6, 2026-09-04):** a data-decay check found S1/S2
(the RentCafe rent figures) had drifted — the source is a live-updating dashboard, and it had moved
from $1,389/$1,536 (as of 2026-07-02) to $1,447/$1,601 (as of 2026-08-31). S1/S2 were refreshed to
the current figures, and every value derived from them as a percent/multiple (MA1, MA2, MA3, MA4,
MA9) was recomputed at the same percent/multiple of the new rent. The dilemma still genuinely flips
after the refresh: The Cedarline wins stay-full-term (16.9%), and The Aldergate wins break-at-month-6
(10.7%), both within SPEC §2's ~20% cap and the break-scenario margin still inside the concept
sheet's 8-12% target band. See `case.json.sensitivity_note` and `RESEARCH_LOG.md` for the full
remediation record.

**Case:** The Lease Break · **Tier:** T2 (MS-core) · **Studio:** Adventure
**Standards:** Advanced Numbers — Percent, How to find the percent of a number, How to find a
whole given the percent and the part of the whole, How to add decimal numbers, How to divide
decimal numbers; Measurement — Proportion, Ratio; Number Sense — How to compare two or more values
(see `case.json.standards[]` for exact ids).

**One-line sensitivity flag (SPEC §6):** this case touches ordinary personal-financial stress (a
renter with a contract-dependent income deciding on a legal and financial commitment under a same-
day deadline). Mild weight, not a full SPEC §6 case — a one-line acknowledgment in the discussion
opener ("this is a real decision a lot of renters face") is sufficient.

---

## Argument for A — The Cedarline

The Cedarline wins the stay-full-term scenario decisively. Stay-full-term (D2): Cedarline $1,483.17
(rent $1,447 plus the $434 move-in fee amortized over 12 months) vs. Aldergate $1,734.42 (rent
$1,601 plus the $1,601 deposit amortized over 12 months) — Cedarline cheaper by 16.9%. Over a full
12-month term, The Cedarline's much lower base rent and modest move-in fee outweigh The Aldergate's
smaller per-month deposit burden, because a 12-month amortization window dilutes both leases'
up-front costs to only a few dollars or tens of dollars a month — the termination penalty never
enters this scenario at all.

## Argument for B — The Aldergate

The Aldergate wins the break-at-month-6 scenario. Break-at-month-6 (D3): Cedarline $2,363.50 (rent
$1,447 plus the $434 fee and $5,065 penalty amortized over 6 months) vs. Aldergate $2,134.67 (rent
$1,601 plus the $1,601 deposit and $1,601 buyout amortized over 6 months) — Aldergate cheaper by
10.7%. Halving the amortization window to 6 months roughly doubles the drag each lease's one-time
costs put on the monthly figure, and The Cedarline's termination penalty is now large enough (3.5
months' rent, grounded in S7/S8's real range for a lease with several months still remaining) to
outweigh its ongoing rent advantage. The Aldergate's capped, one-month buyout keeps its break-
scenario total lower even though its full-term total is higher — this is the case's real point:
Option B swings noticeably less between the two scenarios than Option A does (compare each
option's own D2 vs. D3 effective-monthly-cost figures above), which is worth naming explicitly if a
student raises it.

## The margin

Computed effective monthly costs: stay-full-term is Cedarline $1,483.17 vs. Aldergate $1,734.42
(Cedarline cheaper by 16.9%); break-at-month-6 is Cedarline $2,363.50 vs. Aldergate $2,134.67
(Aldergate cheaper by 10.7%). The two scenarios now favor opposite leases, matching this case's
design intent. Both margins are within SPEC §2's ~20% cap; the break-scenario margin (10.7%) also
lands inside the concept sheet's 8-12% target band. `case.json.balance.margin_pct` records 10.7%
(the narrower of the two magnitudes) as the single scalar of record; the full two-scenario
breakdown lives in `balance.margin_pct_by_scenario`. A facilitator running this case should expect a
genuinely split room: which lease is "right" depends on which scenario a group believes is more
likely for Maya, which is exactly the discussion this case is built to produce.

**Remaining GAP, not a blocker:** the stay-full-term margin (16.9%) is wide relative to the 8-12%
target, so the stay-full-term half of the discussion will lean toward Cedarline being the obvious
answer — a real but acceptable asymmetry, since the case's dilemma lives in the *contrast* between
the two scenarios' winners, not in either scenario being individually close.

## Five Socratic questions

1. Under the "stay full term" scenario, which lease actually costs less per month once you amortize the move-in cost, and does that match which lease has the lower sticker-price rent?
2. Under the "break at month 6" scenario, how much does each lease's effective monthly cost change compared to the full-term scenario, and why does one lease change so much more than the other?
3. The Cedarline's move-in fee is what percent of one month's rent, and the Aldergate's deposit is what percent of one month's rent — does that percentage alone tell you which lease is the better deal, or do you need the termination terms too?
4. If Maya were certain her contract would extend to the full term, would your recommendation change? What single number in Appendix A or B would have to shift for your recommendation to flip under the "break at month 6" scenario?
5. A renter who only compared the two leases' monthly rent numbers would pick one specific apartment — which one, and does that renter's shortcut hold up under both scenarios, or only one?

## The trap

The trap is now genuinely live: a learner who compares only sticker-price monthly rent picks The
Cedarline outright, and that shortcut happens to agree with the correct answer under the
stay-full-term scenario (16.9% in Cedarline's favor) — reinforcing false confidence — but is wrong
under the break-at-month-6 scenario, where the same shortcut still says "Cedarline" while the
amortized math says Aldergate by 10.7%. Watch for students who run the sticker-price comparison once,
get a confident answer, and never re-run it for the break-at-month-6 case because "we already know
Cedarline is cheaper." The second-order trap: a student who does catch the reversal may then
overcorrect and assume Aldergate is unconditionally better, missing that the reversal is
scenario-dependent, not absolute — D5's memo should defend a recommendation for *both* scenarios,
not just declare an overall winner.

## Sensitivity note

MA2 (The Cedarline's early-termination penalty, $5,065 = 3.5 months' rent) is the highest-leverage
modeling assumption in the case and the dial that determines whether the case's reversal exists at
all — see `case.json.sensitivity_note` and `sensitivity_model.py` for the full record. A Hero who
argues the penalty should sit at the lower, more ordinary end of the real range (1-2 months' rent,
per S5) is making a legitimate challenge and should be pushed to show exactly how far the number
would have to fall before the break-at-month-6 recommendation flips back to Cedarline — never state
that threshold in `case.md` itself.

---

## Guide Notes — the anchor ladder (SPEC section seven point one)

### Intro

Frame the format: Maya has to sign one lease today, sight unseen on how her contract situation
resolves. Name the opener: "Two leases. One decision, due end of business. Which one?"

### Launch

Show the Overview and Dilemma with no appendix numbers yet — just the two options as described in
plain language (lower rent vs. more flexible exit). Ask the room to react to the framing alone,
before anyone has seen a dollar figure.

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "Sign now — Cedarline or Aldergate?" Record the split; most rooms will lean toward
whichever option sounds cheaper on its face (Cedarline), which is the point.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push past "which lease is cheaper" toward "cheaper under which scenario." Let the room sit with the
discomfort that nobody — not the facilitator, not Maya herself — knows yet whether her contract will
extend. "Is 'which lease is cheaper' even the right question, or is the real question 'cheaper if
what happens, and what happens if not'?"

### Anchor 3 — WHAT IS THE PROCESS?

Before touching Appendix A/B's numbers, get the room to state the actual comparison method: take
each lease's up-front cost and any termination penalty, spread it over the number of months
actually lived there, and add that to the monthly rent (D2, D3). Re-ask: "Now that we know the
process, do we still think the question is 'which is cheaper' — or 'cheaper over how many months'?"

### Anchor 4 — WHAT DON'T WE KNOW?

Name the load-bearing unknown explicitly: whether Maya's contract extends. "Is this an assumption we
can make carefully, or are we just guessing? What would make one guess more defensible than
another?"

### Data Deep Dive

Now open Appendices A–C. Run D1–D4 as a room, or have groups report out. The two scenarios now
genuinely favor opposite leases: stay-full-term favors Cedarline by 16.9%, break-at-month-6 favors
Aldergate by 10.7%. Facilitate toward the contrast — most rooms will be surprised the answer isn't the
same in both scenarios; that surprise is the intended pedagogical moment.

### Twist

At roughly the 15-minute mark: "Maya's manager just called — the contract extension is now confirmed
for sure, one way or the other (facilitator's choice: confirmed extended, or confirmed not
extended)." Per MA10, "extended" means a long extension covering the rest of whichever lease's
12-month term Maya signs (i.e., it maps cleanly to the stay-full-term/D2 scenario) — if a student
asks "extended for how long, though?", MA10 is the answer; the case does not model a partial-length
extension. You have 60 seconds: does your recommendation change, or was it never really about the
uncertainty in the first place? Because the two scenarios now genuinely favor different leases, this
twist is a real fork: a group that recommended based only on one scenario's math should now
recognize whether their original pick still holds under the *other* scenario's resolved answer.
Groups that ran both D2 and D3 before committing should hold steady (their recommendation was
already scenario-aware); groups that only ran one should visibly reverse or scramble — that contrast
is the fragile-vs-robust moment this twist was designed to produce.

### Close

VOTE AGAIN. "Did we ask the right question?" "What math was new to you today?" Compare the re-vote
to Anchor 1's cold vote. Expect a genuine, scenario-driven split rather than convergence — use the
close to name it directly: "your answer depended on which future you bet on; is that a weakness in
the math, or is that the honest answer to an uncertain question?"

### Lessons Learned

The core transferable idea: a sticker price is not a cost — a cost has to be amortized over the
actual time period you'll experience it, and when that time period itself is uncertain, the honest
answer is "it depends," computed under both possibilities rather than assumed away.

### Standards Touched On

Percent, How to find the percent of a number, How to find a whole given the percent and the part of
the whole, How to add decimal numbers, How to divide decimal numbers, Proportion, Ratio, How to
compare two or more values.

## 45-minute Socratic plan (SPEC section seven point three)

| Time | Move |
|---|---|
| 0:00-3:00 | Cold-call launch, 30-second gut-check vote (Anchor 1) — no explanation |
| 3:00-10:00 | Position defense: "Convince us why your pick is better, not just cheaper-looking" |
| 10:00-15:00 | Pressure-test: "Whose recommendation only works under one of the two scenarios?" |
| **15:00** | **DROP THE TWIST** — the contract-extension question is resolved one way or the other; deliver slowly, with a pause before "does your recommendation change?" |
| 15:00-20:00 | Immediate recommit: who reverses, who holds? "What just broke — the number, or the reasoning?" |
| 20:00-30:00 | Threaded deep conflict — two named threads: (1) "betting on the contract extending" vs. "betting it doesn't," (2) "sticker price vs. effective monthly cost" |
| 30:00-45:00 | Close, re-vote, reflection, lessons learned |

## Cohort bands (SPEC section seven point four)

| Band | Typical size | What changes |
|---|---|---|
| **Full** | 12-20 (the size this case is written for) | Anchors and timings run as written above |
| **Compressed** | 6-11 | Anchors 2-3 combine into one pass; the deep-conflict section (20:00-30:00) runs one thread instead of two; total runtime shortens proportionally |
| **1:1 / pair** | 1-2 | No vote at Anchor 1 — instead ask for a stated initial position and why; the facilitator plays devil's advocate directly rather than cold-calling the room; the Twist still lands, and "who reverses" becomes "would you reverse, and why" |

## Content-sensitivity flag

This case touches personal financial stress (a renter with an uncertain, contract-dependent income
deciding on a legal and financial commitment). Mild weight, not a full SPEC §6 case — a one-line
acknowledgment in the discussion opener ("this is a real decision a lot of renters face") is
sufficient; no further flag needed.
