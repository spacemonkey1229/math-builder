# Guide Notes: The Keyspace Decision

**Case:** The Keyspace Decision · **Tier:** T3 · **Band:** MS-stretch / HS-entry · **Studio:** Launchpad
**Standards:** Discrete Mathematics / Combinatorics — Fundamental Counting Principle (term + how-to)
and Pigeonhole Principle (term, new_coverage), plus two already-covered supports (compound-unit
conversion, percent of a number). Exact ids in `case.json.standards[]`.

**Status:** drafted at `case-write`; numeric detail below is finalized once `case-research` sources
Appendices B, C, and D. This file is re-checked for drift at every readiness run.

## Intro

Frame the format: this is not a trivia question about how big a number gets. Name the opener:
*"You do not own this budget and you cannot force the board's hand. You write the standard the
whole company runs on, and your name is on the line that says the last audit finding got fixed.
Thursday you have to recommend one policy, not two."* Say plainly that both drafts are legal,
defensible security postures used at real companies, and the room's job is to decide which one
they would put their own name on.

## Launch

Show a real, public credential-stuffing or password-breach statistic headline (a news piece, not a
number to compute with yet) — enough to establish this is a real category of attack, not a
hypothical. Ask one question and take answers without correcting any of them: *"If you had to bet
your own email password against being cracked by brute force, or against being phished, which one
would you actually worry about?"* Let the gut reads stand; the Close revisits them.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

*"Is anyone courageous enough to stand with Renata on the short password?"* Stand-or-sit vote for
both options, no discussion permitted. Record the count — the Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'more secure'?"**

Let confusion grow here; it is deliberate. The room will want to say "the longer password is more
secure" and that is wrong in an interesting, specific way. Push:

- *"More secure against what? Name the attacker."* (A machine guessing passwords all night? A
  person who tricks you into typing yours into a fake page?)
- *"The case gives you a keyspace number and a breach-share percentage. Are those the same kind
  of number?"*
- *"If a password is uncrackable by brute force but the attacker never has to crack it, does the
  length matter at all?"*

Do not resolve this. A room that leaves Anchor 2 still arguing about what "secure" even means is
exactly where it should be.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Make the room name the steps before opening any appendix:

1. Count each policy's nominal keyspace (D1).
2. Convert that keyspace, at a real cracking rate, into years to crack (D2).
3. Separately, bound how many employees the legacy system's *reduced* keyspace can hold before a
   collision is guaranteed (D3).
4. Weight the crack-time figures by how real attackers actually get in — most of the time, not by
   cracking at all (D4).
5. Divide the result by what each policy actually costs to run (D5).

Re-ask: *"Is our question still the right question, now that we can see the steps?"*

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the honest gaps, all of which live in `case.md` Appendix E:

- Bramwell is fictional; its headcount, and therefore both its cost scaling and its D3 collision
  bound, rest on a stated assumption (MA1).
- The breach-vector percentages in Appendix C describe the *industry*, not Bramwell specifically —
  there is no way to know Bramwell's own historical breach mix.
- The offline cracking-rate benchmark in Appendix B assumes attackers get a copy of the password
  hashes at all; a policy that never lets that happen changes the whole calculation.

Ask which of these changes the recommendation if it moves, and which only changes the size of the
answer.

## Data Deep Dive

Now, and only now, the numbers. Work D1 → D5 as a room. Cold-call specifically on **D3**, the
pigeonhole bound — this is the deliverable most likely to produce a Hero who has never used the
principle on a real number before, and their confusion is information, not a moment to rescue. The
sentence to fish for is some version of *"the guarantee only kicks in one employee past the entire
keyspace — that's a huge number, or it's a small one, depending which policy we're in."*

Full worked figures are filled in the **Facilitator-only numbers** section below once
`case-research` completes.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses.

*"Everyone in this room has now computed D2. Someone read me Option A's number."* (Let a Hero say
something like "over ten trillion years.") *"And Option B's?"* ("About a hundred and thirty
years.") *"So The Long Wall wins by roughly seventy billion times over. Show of hands — who is
recommending Option A right now, on exactly that basis?"*

Let hands go up. Then: *"That number is real. Every digit of it is correctly computed. And it is
the wrong answer. Here is why: it assumes the only way into Bramwell's systems is guessing the
password from scratch. Verizon's 2026 breach report says that in 39% of real breaches, the
attacker already had a valid credential — stolen, phished, or reused — before they ever touched a
login screen. A fourteen-character password does nothing to stop that. You have five minutes.
Redo D5 using D4's numbers instead of D2's alone. Does the recommendation survive?"*

**Facilitator-only: what the numbers actually do.** Weighting each option's protection by how real
attackers actually get in (61% weight on the direct-guessing channel D2 measures, 39% on the
credential-abuse channel D3/D4 measure, per Appendix E MA3's stated attack-cadence assumption),
Option A's expected time to compromise falls to **320.5 years** and Option B's to **214.0 years**
— but Option B costs less ($36/employee/year against Option A's $60), so on the case's actual
primary metric (years **per dollar**), Option B still wins, **5.94 years/$ against 5.34 years/$,
a margin of 10.1%.** The verdict does not flip on the raw years alone (Option A's 320.5 is larger
than Option B's 214.0) — it flips because Option B is *both* more protective per dollar spent and
cheaper outright, once the credential-theft channel counts at all.

**The honest caveat, and hand it over if pushed.** This whole result hinges on one openly stated,
unsourced number: Appendix E MA3's assumed 0.8%-per-year rate at which a given employee account
suffers a successful credential-theft attempt. Below about **0.72%**, Option A wins instead. No
public source measures this rate for a specific company — it is the case's most fragile, most
important dial, and it is named as such in Appendix E, not hidden in a footnote.

Do not hand the arithmetic over unprompted. A Hero who says *"I'd want to see how sensitive this
is to that 0.8% number before I trusted it"* has given the strongest possible answer.

## Deep conflict — threads (20–30 min)

1. **A number you can compute versus a number you have to trust.** D1's keyspace is exact, derived
   from the case's own stated policy — nobody can argue with the arithmetic. D4's breach-vector
   percentages come from someone else's data set, collected somewhere else, about other companies.
   Which kind of number should carry more weight in a recommendation, and is "I can prove this one
   with a calculator" actually the same thing as "this one matters more"?
2. **Whose name is on the finding.** The audit finding is Renata's to close, not the board's and
   not the CISO's. Does that change which standard she should recommend, independent of which one
   is mathematically "better" — and is that a legitimate factor, or a bias the case should ask her
   to set aside?
3. **The legacy system nobody chose.** Neither draft standard controls what the accounts-payable
   system actually stores. Is it fair to judge either policy by a constraint neither one created?

## Socratic questions

1. The Long Wall's nominal keyspace is astronomically larger than The Second Gate's — why does that fact alone not settle the case?
2. Your D3 pigeonhole bound and Bramwell's actual headcount — which one is bigger, by how much, and what does that gap actually tell you about accidental collisions at this company?
3. D4 asks you to combine a percentage share of breaches with a percentage rate at which 2FA blocks takeover — are those two percentages of the same denominator?
4. If Bramwell's headcount were ten times larger, which of your five deliverables would change, and which would not move at all?
5. The legacy accounts-payable system caps every password at 8 lowercase-and-digit characters no matter which draft standard wins — what does that fact do to Argument A's claim that length alone solves the problem?

## 45-Minute Socratic Plan

The anchor ladder above, laid out against a 45-minute clock. Adjust proportionally for the
Compressed or 1:1 cohort bands (see Tier 1/Cohort bands below); this is the Full-band timing.

| Time | Segment | What happens |
|---|---|---|
| 0:00 | Intro | Frame the format; name what's on the line for Renata. |
| 3:00 | Launch | Real credential-stuffing headline; gut-read question, no correcting. |
| 6:00 | Anchor 1 | Stand-or-sit vote, no reasoning yet. Record the count. |
| 10:00 | Anchor 2 | "What is the problem we're solving?" — let confusion about "more secure" grow. |
| 16:00 | Anchor 3 | Name the five-step process (D1→D5) before opening any appendix. |
| 20:00 | Anchor 4 | Surface the honest gaps in Appendix E; which assumptions are load-bearing. |
| 25:00 | Data Deep Dive | Work D1→D5 as a room; cold-call on D3's pigeonhole bound. |
| 33:00 | TWIST | Drop the twist: the raw D2-only number is real and wrong. Five minutes to redo D5 with D4's weighting. |
| 38:00 | Deep conflict | Pick one of the three threads; 5–7 minutes. |
| 43:00 | Close | Vote again; "did we ask the right question at the start?" |

## Close

**VOTE AGAIN.** Then: *"Did we ask the right question at the start?"* and *"What math was new to
you tonight, and how did you actually attack it?"*

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

## Standards Touched On

Fundamental Counting Principle · Pigeonhole Principle · How to apply the Fundamental Counting
Principle to count outcomes · How to convert an amount with compound units · How to find the
percent of a number

## Facilitator note — sensitivity

None required (SPEC §6). The stakes are professional and organizational — an audit finding and a
security analyst's remediation record. No personal loss, no family hardship.

## Facilitator-only numbers

Every figure below resolves in `case.json.derived` and is reproduced by
`python3 cases/the-keyspace-decision/sensitivity_model.py`.

**D1 — Keyspaces.** Long Wall (70¹⁴): **67,822,307,284,900,000,000,000,000**. Second Gate (70⁸):
**576,480,100,000,000**. Legacy AP system (36⁸): **2,821,109,907,456**.

**D2 — Crack times at 138,675 H/s [S1].** Long Wall: **1.55 × 10¹³ years**. Second Gate:
**131.8 years** (Hive Systems itself publishes 132 years for this exact case — an independent
match). Legacy AP system: **0.645 years (≈ 236 days)**.

**D3 — Pigeonhole.** Guarantee threshold: **2,821,109,907,457** employees (legacy keyspace + 1).
Bramwell's actual AP-system population: **80**. Ratio: guarantee is about **35 billion times**
larger than actual headcount — accidental collision is not a practical risk at Bramwell's scale,
under either draft standard.

**D4/D5 — Weighted years and the primary metric.** Option A: **320.5 years** expected time to
compromise ÷ **$60.00**/employee/year = **5.34 years/$**. Option B: **214.0 years** ÷
**$36.00**/employee/year = **5.94 years/$**. **Option B wins, margin 10.1%.**

**The trap, quantified.** The same D2 crack-times divided naively by cost (skipping D4's
weighting entirely) give Option A a raw metric of **2.585 × 10¹¹ years/$** against Option B's
**3.66 years/$** — Option A "wins" by a factor of **≈ 70 billion**. This is the number a rushed
pitch will report. It is wrong because it assumes brute force is the only attack that exists.

**Sensitivity.** The 10.1% margin depends entirely on Appendix E MA3 (assumed 0.8%/year
credential-theft cadence). Flip point: **≈ 0.72%/year**. Below it, Option A wins; the margin
widens quickly above it (63.5% at 2%/year cadence, 84.9% at 5%/year).

**Tier 2 probe 5, disclosed (2026-08-17).** A ±50% sweep on the two Appendix E assumptions that
enter the primary metric (`ma3_credential_theft_cadence`, `ma4_helpdesk_increment`) mechanically
FAILS stability: MA3 at -50% flips the verdict to Option A (margin 78.8%, breaking the SPEC §2 20%
cap), MA3 at +50% breaks the cap the other direction (66.1%, no flip), and MA4 at +50% breaks the
cap on its own (22.4%, no flip). This is not a modeling bug — a genuine retune was attempted first
(sweeping MA3's base value from 0.008 up through 0.020 and MA4's base value from $12 up through
$40) and no setting keeps both the base margin and every ±50% flex result inside the 20% cap
simultaneously; the metric's reciprocal-of-a-weighted-rate structure is inherently this sensitive
to its most load-bearing dial, which is the pedagogical point of the case (see the trap, above, and
Socratic question 5 below). Both parameters are now recorded in `case.json.sensitivity_disclosure[]`
as Category X (a real value exists — Bramwell's true phishing-compromise rate and true help-desk
cost — but neither is publicly measurable; both stated values are documented good-faith estimates
anchored to the closest public analogue). Tier 2 probe 5 reads `PASS (disclosed)`, not a stable
margin — say so if this case is ever cited as a "close, stable" example.
