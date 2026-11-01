# Facilitator Guide — The Equivalent Ledger

**Status:** post-research. All figures below are the value of record, matching
`case.json.balance`/`derived` and `sensitivity_model.py`. If any of these three ever disagree,
`sensitivity_model.py` is the arithmetic source of truth — fix the other two to match it.

**SPEC §6 flag:** this case touches workplace deadline/job-risk pressure (a verification lead
overriding an on-call engineer under a compliance clock) but no illness, death, or family
hardship — one-line flag for the discussion lead, not a heavier content warning.

---

## The two formulas, factored (the answer key)

- **O(n) = 48n² + 180n.** GCF(48, 180): 48 = 2⁴×3, 180 = 2²×3²×5 → GCF = 2²×3 = **12**.
  Fully factored: **O(n) = 12n(4n + 15)**. Every term of O(n) carries a factor of *n* — this is
  the structural feature D4 asks students to name.
- **R(n) = 54n² + 96n + 240.** GCF(54, 96, 240): 54 = 2×3³, 96 = 2⁵×3, 240 = 2⁴×3×5 →
  GCF = 2×3 = **6**. Fully factored: **R(n) = 6(9n² + 16n + 40)**. The constant term 240 has no
  factor of *n* — R(n) is **not** of the form *n* × (anything). This is the tell: O and R cannot
  be the same expression for every n, because one always evaluates to 0 at n = 0 and the other
  never does.
- **They agree only at n = 4 and n = 10** (both give $1,488 and $6,600 respectively) because
  R(n) − O(n) = 6n² − 84n + 240 = 6(n − 4)(n − 10) — a difference polynomial engineered to vanish
  at exactly those two points and nowhere else. At n = 25 (Appendix B's untested representative
  batch), O(25) = $34,500 but R(25) = $36,390 — a real $1,890 (5.5%) gap that QA's two-batch test
  could never have found.

## Argument for A — The Regression Pass

Ship now: the rewritten formula produced identical output on both real historical batches anyone
has tested it against ($1,488 at n=4, $6,600 at n=10 — Appendix B), the deployment freeze locks the
engine for six weeks starting before sunrise (Appendix C), and a full verification costs real
money too: 2 engineers × 8 hours × $48.94/hr = **$783.04** (Appendix C, [S1]). Weighed against the
stated risk figures in Appendix D (a 3.4% chance of an undetected defect × a $25,000 cost if one
reaches production = **$850.00** expected cost), the two numbers are close — A's approach is not an
obviously reckless gamble on the numbers as stated before anyone does the proof.

## Argument for B — The Full Factor

The Full Factor costs $783.04 today and buys certainty — not a probability. D1/D2's factoring
proves O(n) = 12n(4n+15) always has *n* as a factor (so a batch of zero unmatched items sweeps
$0, as it must) while R(n) = 6(9n²+16n+40) never does (it sweeps $240 even at n=0) — meaning the
two formulas are **not the same expression for any n outside the two accidentally-matching points
QA tested**. Once D4's proof is done, Appendix D's "3.4% chance of a defect" is revealed as the
wrong number entirely: for any real production batch that isn't exactly 4 or 10 unmatched items,
the rewritten formula is **certain**, not merely likely, to mis-sweep money — $1,890 off at a
25-item batch, $6,480 off at a 40-item batch. B's $783.04 is cheap next to that.

## The margin

**7.88%**, on the primary metric (expected cost of the verification decision, D5) — The Full
Factor is cheaper even before anyone does the proof. This sits inside the case's 5–10% target
band and well inside SPEC §2's 20% cap. Note the two different numbers in this case: D5's
pre-proof margin (7.88%, both options look close) is what a student sees using only Appendix D's
stated risk figures; D4's proof result (agreement at exactly 2 of infinitely many possible n) is
what reveals that Appendix D's own 3.4% probability was never the right number to trust once the
formula is provably wrong outside {4, 10}. The gap between "close on paper" and "not actually
close once you've proven it" *is* the trap — see below. Full arithmetic: `sensitivity_model.py`,
`case.json.balance.margin_basis`, `case.json.derived`.

## The trap

A learner who computes D3's sample-test table, sees O(n) and R(n) match at both tested batch
sizes, and stops there — concluding the formulas are "basically the same" — has fallen into
exactly the trap this case is built to catch: two polynomials that agree at k points are not
necessarily the same polynomial (they only have to agree everywhere if their *difference* is the
zero polynomial). A learner can even complete D5's cost comparison correctly, using the stated
3.4% risk figure, and still miss the point if they never connect D4's proof result back to
whether that 3.4% was ever the right number. The full trap has two layers: (1) sample-testing at a
handful of points is not proof, and (2) even a seemingly-reasonable probability estimate for "the
formula might be wrong" is meaningless once you have proven it wrong for a specific, identifiable
class of inputs (every n outside {4, 10}) — the risk isn't 3.4% for those inputs, it's certain.

## Five Socratic questions

1. Your D3 table shows the two formulas agreeing at both batch sizes QA tested — what would you have needed to test to catch the gap that shows up at n=25?
2. D1 factors O(n) as 12n(4n+15) and D2 factors R(n) as 6(9n²+16n+40) — what does the presence (or absence) of a factor of n in every term tell you that plugging in numbers doesn't?
3. Appendix D states a 3.4% chance the rewritten formula has an undetected defect — after finishing D4's proof, is 3.4% still the right number to use for a batch of, say, 25 unmatched items? Why or why not?
4. D5's cost comparison favors The Full Factor by only 7.88% before anyone does any factoring — if that margin had favored The Regression Pass instead, would skipping the proof have been the right call?
5. A classmate argues "it matched on real data twice, that's good enough evidence" — using only your D1/D2 factored forms, what is the one sentence that proves them wrong?

---

## Guide Notes — the anchor ladder (SPEC's facilitator-artifacts section, anchor-ladder subsection)

### Intro

Frame the format: a verification decision under a real deadline, where "it worked on the data we had" and "it is the same formula" are being treated as the same claim — and math is the only way to tell whether they actually are.

### Launch

Read the Overview aloud. Stop before the Approve button gets clicked. Ask the room: "Before you've seen either formula, would you approve on the two-batch match, or hold for the proof — and why?"

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "The Regression Pass or The Full Factor — show of hands. Is anyone courageous enough to stand with shipping now, before seeing a single factored expression?"

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push the room past "do the two formulas give the same number" toward "do the two formulas give the same number for every possible batch, not just the ones we checked." Let the confusion sit: "Wait — how would testing more numbers ever prove that?"

### Anchor 3 — WHAT IS THE PROCESS?

Get the room to state the method out loud before touching the formulas: fully factor each expression using prime factorization to find its greatest common factor, then compare the factored forms directly instead of plugging in numbers. Re-ask: "Is 'test a few batch sizes' still a fair way to answer our question?"

### Anchor 4 — WHAT DON'T WE KNOW?

Name the load-bearing unknowns explicitly: the stated 3.4% defect probability and the $25,000 cost-of-error figure (Appendix D), both Modeling Assumptions. "Which of those numbers is doing the most work in D5 — and does D4's proof change whether you trust it?"

### Data Deep Dive

Now open Appendices A–D. Run D1–D5 as a room, or have groups report out. This is also the moment to run Socratic Questions 1 and 2 (what a matching sample table can and can't prove; what the factored forms reveal that plugging in numbers doesn't).

### Twist

Once D3's sample-test table is on the table and the room is leaning toward "they matched, ship it," reveal TWO new pieces of information together, out loud, as a single package — both are new, disclosed information the room has not seen before, exactly like the case's Appendix D risk figures were disclosed:

1. Ledgerline's compliance team has just confirmed next quarter's batch, from a newly onboarded partner bank, is expected to run roughly 40 unmatched line items per night — far outside the two batch sizes (4 and 10) anyone has ever tested the rewritten formula against.
2. Compliance also estimates — and states explicitly, as a new stated assumption for this part of the discussion, the same way MA8/MA9 were stated in Appendix D — that a mis-sweep of this kind would typically take about **4 nights** of nightly batches before an auditor or a partner bank's own reconciliation catches the mismatch (based on how often partner banks independently audit their suspense-account balances).

**Say the "4 nights" number to the room explicitly — it is new information being disclosed at the twist, not a fact any Hero could have derived from the original packet, and it must be stated as clearly as Appendix D's original figures were, or the recomputation below has no basis a student can check.** (This is a correction made after Tier 2 P4 found the original draft treated the nights-until-detected figure as a backstage-only modeling detail in `case.json.derived`, never actually disclosed to the room — an unstated convention a student could not have used to independently verify the twist's arithmetic. It is now a stated, disclosed twist assumption, delivered the same way the original twist information always is.)

With both pieces on the table, recompute D3's comparison at n=40: O(40) = $84,000, R(40) = $90,480 — a **$6,480 (7.7%) gap, every single night**, if the rewritten formula ships unverified and is wrong the way D4 already proved it is for any n outside {4, 10}. `sensitivity_model.py`'s `evaluate_twist()` models this: it recomputes Option A's expected cost not from the flat $25,000 Appendix D assumption, but from the actual $6,480 per-night mis-sweep, accumulated across the newly-stated 4 nights before anyone notices — pushing Option A's true cost to $25,920 against Option B's unchanged $783.04, a decisive, not a close, result. Ask immediately: "What just broke in your model? Was your original 3.4%-and-$25,000 estimate wrong, or was it just never the right question once D4's proof existed?"

### Close

VOTE AGAIN. "Did the vote move? Where did your confidence in the two-batch test come from in the first place?"

### Lessons Learned

Testing a function at a finite set of points can never prove two functions are identical — it can only fail to disprove it. Factoring is what turns "matched every time we checked" into "provably the same," and the two are not the same kind of confidence, no matter how many times you check.

### Standards Touched On

Factor; Greatest Common Factor; Prime; Composite; How to factor a number; How to find the greatest common factor of a set of numbers; How to find the percent of a number.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote on A vs. B — no explanation |
| 3:00–10:00 | Position defense: "Convince us why it's not just faster, but actually right" |
| 10:00–15:00 | Pressure-test: "What would it take to prove — not just test — that these are the same?" |
| **15:00** | **DROP THE TWIST** — the 40-item production batch, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00–30:00 | Threaded deep conflict: (1) D1/D2's proof vs. D3's sample table, (2) trusting a stated probability (D5) vs. trusting a completed proof (D4) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## Cohort bands (SPEC's facilitator-artifacts section, cohort-bands subsection)

| Band | Typical size | What changes |
|---|---|---|
| Full (12–20) | the size this case is authored for | Anchors and the 45-minute plan run as written |
| Compressed (6–11) | roughly half | Anchors 2–3 combine into one pass; the 20:00–30:00 deep-conflict step runs as a single thread (the D4 proof vs. the D5 cost table) instead of two; runtime shortens proportionally |
| 1:1 / pair (1–2) | one or two learners | no vote at Anchor 1 — a stated initial position instead; facilitator plays devil's advocate directly; the twist still drops but "who reverses" becomes "would you reverse, and why" |

## Sensitivity note

Two stated Modeling Assumptions (MA5 the defect probability, MA6 the cost-of-error) carry D5's
pre-proof cost comparison — no public source publishes either figure for a specific private
company's specific internal formula. Tier 2 P5 (`sensitivity_model.py`, ±50% flex on every
`FLEX[]` dial) found:

- **The cost-of-error figure (MA6) is the load-bearing, dilemma-flipping dial** on D5's pre-proof
  metric. At −50% ($12,500), Option A's expected cost drops to $425, below Option B's $783.04,
  flipping the recommendation on D5's numbers alone — before anyone has done D1/D2's proof. This
  is disclosed, not hidden: it is exactly why the case does not let D5 stand on its own and
  requires D6 to reconcile it against D4's proof.
- The defect probability (MA5) and the verification hours (MA4) do **not** flip D5's verdict at
  ±50% individually.
- D4's proof result (do the factored forms share a common factor of n) is not a flex target — it
  is a fixed structural fact about the two stated formulas, not a scenario assumption.
