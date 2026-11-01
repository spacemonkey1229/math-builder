# FACILITATOR.md — The Referral Cut

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Referral Cut · **Tier:** T2 (MS-core) · **Studio:** MS Adventure
**Standards:** Fractions/Multiplication Of Fractions (all 4 skills) plus Fractions/Understanding
Fractions' Simplify, Mixed Number, Improper Fraction and their matching how-tos (see
`case.json.standards[]` for exact ids).

**Status:** `case-research` complete (2026-09-09). All three `{{NEEDS_SOURCE}}` placeholders in
`case.md` are resolved — Amazon's own public referral-fee page (S1, HIGH), a detailed third-party
reconstruction of Amazon's gated FBA fee table (S2, MEDIUM, with a disclosed $0.20 discrepancy
against a second source), and Amazon's own corporate fee-update announcement plus unanimous
secondary corroboration for the fuel surcharge (S3, HIGH). `case.json.balance.margin_pct` is a
real, computed **10.83%**. Everything below is the case of record, not a placeholder.

**Sensitivity note (SPEC §6):** ordinary small-business cash-flow decision under a new wholesale
contract's guaranteed monthly volume. No illness, death, or family hardship. No heavier
facilitator touch than usual is expected.

## Argument for A — Fulfilled by Merchant (FBM)

A's case is that Mia pays Amazon nothing beyond the 15% referral fee [S1] — every other dollar of
cost is one she controls directly, unlike a fixed marketplace fee schedule she cannot negotiate.
Post-referral proceeds are $15-15/16 per unit (list price $18-3/4 × referral retention 17/20).
After her own $3-1/8 packaging/postage cost and $6-1/2 production cost, her true net margin is
**$6-5/16 per unit**, or **$252-1/2 per month** at Rivendell's guaranteed 40-unit order — the
higher of the two options under current figures. Its real weakness is working capital: Appendix
A's 6-1/2 weeks of held, unsold inventory (versus Option B's 2-1/4 weeks) ties up real cash every
single month that never shows up in a per-unit margin figure but is very real to a business Mia's
size ($2,212-7/16 tied up under A versus $765-27/32 under B — see D5).

## Argument for B — Fulfilled by Amazon (FBA)

B's case is that its fees replace a cost Mia already pays herself under FBM (packaging + postage),
and free up several weeks' worth of working capital that FBM leaves sitting on a shelf as unsold
inventory. Its correctly-computed cost is **not** simply "15% off the top" — Option B pays *two*
real cuts: the same 15% referral fee [S1], plus a true total per-unit fulfillment fee of
**$3.68 × 1.035 = $3-1011/1250** (≈$3.8088) [S2, S3], where the 1.035 comes from Amazon's real
2026 fuel-and-logistics surcharge applied *to the fulfillment fee itself*, not to the item price.
Her true net margin under B is **$5-6287/10000 per unit** (≈$5.6287), or **$225-37/250 per month**
(≈$225.15) — genuinely lower than FBM's by a real, computed **10.83%**. B's real weakness, this
job's numbers, is that its combined fee load currently costs Mia more per unit than the
packaging/postage she already handles herself — even though every figure in it is real, sourced,
and non-negotiable.

## The margin — real numbers, and how thin they are

`case.json.balance.margin_pct` = **10.83%**, inside the approved concept's 8–15% target band. The
arithmetic, in full (all in exact fractions via `sensitivity_model.py`'s `Fraction` arithmetic —
decimals shown only for readability):

- **Post-referral proceeds (both options):** $18-3/4 × 17/20 = $15-15/16 (≈$15.9375).
- **Option A (FBM):** $15-15/16 − $3-1/8 (packaging/postage) − $6-1/2 (production) =
  **$6-5/16/unit** (≈$6.3125) → × 40 units = **$252-1/2/month** (≈$252.50).
- **Option B (FBA):** total fulfillment fee = $3.68 × (1 + 7/200) = $3-1011/1250 (≈$3.8088);
  net margin = $15-15/16 − $3-1011/1250 − $6-1/2 = **$5-6287/10000/unit** (≈$5.6287) → × 40 units =
  **$225-37/250/month** (≈$225.148).
- **Margin:** |252.5 − 225.148| / 252.5 = **10.83%**. A (FBM) wins under the current sourced
  figures.

**Why this matters for the facilitator, specifically:** the recommendation for A does **not** rest
on Amazon's fees at all — Tier 2 Probe 5 confirmed that flexing the fuel-and-logistics surcharge
[S3] by ±50% never flips the verdict (A wins across the whole range). It rests instead on Appendix
A's own packaging/postage cost figure ($3-1/8/unit) — the one number in this case that is Mia's
own operational estimate, not an externally verifiable fact. `sensitivity_model.py`'s P5 run
(`FLEX=["packaging_cost"]`) found the verdict flips from A to B at a +50% flex ($4.6875/unit); the
exact flip point is $3.8088/unit, a real, computed threshold (`case.json.sensitivity_disclosure`).
**Do not treat a student who argues Mia's real packaging/shipping cost might be higher than
$3-1/8 as having found an error — questioning the one figure in this case nobody outside the
fictional business could verify is exactly the legitimate move this case is built to reward.**

## Five Socratic questions

1. Your D3 total fulfillment fee for Option B multiplies the base fee by (1 + the surcharge fraction) — why can't you just add the surcharge's raw percentage number (3.5, or 0.035) directly onto the $3.68 base fee instead?
2. Your D1 calculation multiplies a mixed number (the list price) by a fraction — walk us through why you convert the mixed number to an improper fraction before multiplying, instead of multiplying the whole-number part and the fraction part separately?
3. Appendix A gives two different numbers of weeks of inventory for the two options — why does that number matter to Mia's decision at all, if it never appears in either option's per-unit net margin calculation?
4. Your D4 monthly totals multiply a per-unit margin by 40 units — if Rivendell's guaranteed order size were much larger, would the option that wins per unit still be the option that wins per month?
5. Every number in Appendix B and C came from a real, published Amazon source — but Appendix A's packaging/postage cost is Mia's own estimate of her own business. If that one number were higher than stated, would this recommendation survive?

## The trap

**A learner who computes Option B's true total fulfillment fee by adding the surcharge's raw
percentage number directly onto the base fee's dollar amount — $3.68 + 0.035 = $3.715 — instead of
multiplying the base fee by (1 + the surcharge fraction) — $3.68 × 1.035 = $3.8088 — has made a
plausible-looking but wrong calculation.** The two numbers ($3.715 vs. $3.8088) look close enough
that a learner who makes this mistake may never notice anything is wrong, but the error is a real
unit-mixing mistake: 0.035 is a *rate*, not a *dollar amount*, and adding a rate directly onto a
dollar figure is not a defined operation, even though it produces a number that looks like one.
This is the case's core "successive percentage cuts are multiplicative, not additive" trap — the
same family of error as a shopper assuming two stacked discounts (say 15% and then 3.5%) combine
by simple addition, when the second discount actually has to be applied to what's left after the
first, not tacked on as a raw number.

*(Watch, in particular, for a pitch whose D3 arithmetic never converts 3.5% into a fraction at
all before "applying" it — treating the surcharge as a bare number 3.5 or 0.035 mixed directly
into a dollar computation is the tell.)*

**A second trap (Tier 2 P3 finding, added after adversarial review):** a student can correctly
convert the surcharge to a fraction and still apply it to the *wrong base* — taking 3.5% of the
$18-3/4 item price instead of 3.5% of the $3.68 fulfillment fee. Appendix C's own wording ("applies
on top of the base fulfillment fee itself, not on top of the item's price") pre-empts this, but a
student skimming past that line and pattern-matching "3.5% × price" from D1's referral-fee step can
still make this mistake. Watch for a D3 whose surcharge amount is calculated as $18-3/4 × 7/200
(≈$0.656) rather than $3.68 × 7/200 (≈$0.129) — the wrong-base version inflates Option B's
fulfillment fee by roughly half a dollar more than the correct calculation, which is large enough
to visibly widen Option A's already-real margin advantage without necessarily looking implausible
on its own.

## Twist

**Structural, not a dropped mid-discussion fact: every fee in this case is a real, sourced,
non-negotiable Amazon number — but the number that actually decides the dilemma is Mia's own
estimate of her own packaging/postage cost, which nobody outside her business could ever verify.**
A student who treats Appendix A's $3-1/8 figure with the same confidence as Appendix B/C's cited
Amazon fees has missed that these are not the same kind of number. `sensitivity_model.py` confirms
Amazon's own recently-changed fuel-and-logistics surcharge [S3] does **not** move the verdict even
at a ±50% flex — the case is robust to that platform-fee uncertainty — but a +50% change in Mia's
own packaging/postage estimate flips the recommendation to B. Facilitators should treat the moment
a student challenges Appendix A's own cost figure (rather than Amazon's fees) as the natural twist
moment, and can manufacture it directly with Socratic Question 5.

---

## Guide Notes — the anchor ladder (SPEC Section 7, anchor-ladder subsection)

### Intro
Frame the format: a garage packing table, a tape gun out of tape, two open notifications on one
phone. This is a real seller-platform fee decision wearing a small-business story, not a fractions
worksheet wearing a story.

### Launch
Read the Overview aloud. Stop at "The Seller Central screen is still open, waiting on one button."
Ask the room: "Before you've seen a single number, which button do you think Mia should press —
and why?"

### Anchor 1 — TAKE A STAND AND VOTE
No reasoning yet. "FBM or FBA — show of hands." Record the split.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?
Push the room past "which fee is smaller" toward "which option's *true* net margin per unit, once
every real cost is counted honestly and correctly combined, is actually higher — and does that
answer change once you multiply by a real monthly order size?"

### Anchor 3 — WHAT IS THE PROCESS?
Before touching Appendix B/C's numbers, get the room to state the process out loud: convert the
referral fee to a fraction and find post-referral proceeds (D1), find each option's true per-unit
margin (D2, D3, D4), scale to the guaranteed monthly volume (D4), then compare the working-capital
cost of each option (D5). Re-ask: "Now that we have a process, is 'which fee is smaller' still the
right question?"

### Anchor 4 — WHAT DON'T WE KNOW?
Name what has to be looked up before anything else can be computed: Appendix B's referral fee
percentage and Appendix C's base fulfillment fee and fuel surcharge, all real published Amazon
figures that Challenge 1 sends the room to go find and confirm for themselves. Flag, too, that
Appendix C's base fee itself could not be pulled from Amazon's own public pages during this case's
own research (it sits behind a Seller Central login) — this is a real, disclosed limitation of the
source, not a hidden one.

### Data Deep Dive
Open Appendices A–C. Run D1–D5 as a room, or have groups report out. This is also the moment to
run Socratic Questions 1 and 2 (multiplicative vs. additive fee-stacking, and mixed-number ×
fraction multiplication).

### Twist
Once D3 and D4 are on the table, run Socratic Question 5: "Every number in Appendix B and C came
from a real, published Amazon source — but Appendix A's packaging/postage cost is Mia's own
estimate. If that one number were higher than stated, would this recommendation survive?" Let the
room discover that the case's real fragility lives in the one number nobody outside the story could
ever independently verify — not in Amazon's own published, non-negotiable fees.

### Close
VOTE AGAIN. "Did the vote move? For anyone who didn't move, what would it take to change your
mind — a different fee number, or a different priority (margin vs. cash flow) entirely?"

### Lessons Learned
The core transferable idea: two sequential percentage cuts never combine the way they look like
they should at a glance — you have to actually multiply the retention fractions, in order, to
find out what's really left, and mixing a raw percentage number into dollar arithmetic (instead of
converting it to a fraction first) hides exactly the kind of small difference that determines a
real business decision.

### Standards Touched On
Simplify; Mixed Number; Improper Fraction; How to simplify a fraction; How to convert a mixed
number to an improper fraction; How to convert an improper fraction to a mixed number; How to
multiply a fraction and a whole number; How to multiply two fractions; How to multiply a fraction
and a mixed number; How to multiply two mixed numbers.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold read of the Overview, gut-check vote (Anchor 1) — no numbers shown yet |
| 3:00–8:00 | Position defense: "Convince us your pick nets more per unit, not just feels safer" |
| 8:00–20:00 | Data Deep Dive — build D1's fraction conversion and post-referral proceeds, then D2/D3's per-option costs, as a room |
| 20:00–30:00 | Build D4's monthly totals and D5's working-capital comparison |
| **30:00** | **DROP THE TWIST** — "Amazon's fees are all sourced and fixed. Mia's own packaging cost is not — if it were higher, would the recommendation survive?" |
| 30:00–38:00 | Pressure-test the winning option under a higher assumed packaging/postage cost |
| 38:00–45:00 | Close, re-vote, D6's visual walkthrough, lessons learned |

## Cohort bands (SPEC Section 7, cohort-bands subsection)

| Band | Typical size | What changes |
|---|---|---|
| **Full (12–20)** | the size this case is written for | Anchors and the 45-minute timed plan run as written above |
| **Compressed (6–11)** | smaller room | Anchors 2–3 combine into one pass; the 20:00–30:00 build-out runs as a single worked example instead of small-group work; total runtime shortens proportionally |
| **1:1 / pair (1–2)** | tutoring context | No vote at Anchor 1 — ask for a stated initial position and why instead; the facilitator plays devil's advocate directly; the D3 chained-fraction pressure-test still runs in full |
