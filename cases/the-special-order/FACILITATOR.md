# FACILITATOR.md — The Special Order

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Special Order · **Tier:** T2 (MS-core) · **Studio:** MS Adventure
**Standards:** Fractions/Understanding Fractions — Equivalent Fractions, Simplify, Improper
Fraction, Mixed Number, and all four matching "how to…" skills (see `case.json.standards[]` for
exact ids).

**Status:** `case-research` complete (2026-09-05). All `{{NEEDS_SOURCE: ...}}` placeholders in
`case.md` are resolved — five real figures are sourced (Appendix G: two milling allowances, the
hard maple base price, the custom-milling upcharge, and the mill's lead time), and Appendix C's
minimum order quantity is a disclosed Modeling Assumption (MA1), because no source publishes a
minimum specific to a small custom exact-width dimensioning run. `case.json.balance.margin_pct`
is a real, computed **8.33%**. Everything below is the case of record, not a placeholder.

**Sensitivity note (SPEC §6):** ordinary small-business schedule/budget pressure (a fixed-bid
job, a client-facing install date). No illness, death, or family hardship. No heavier facilitator
touch than usual is expected.

## Argument for A — Standard Stock

A's case is **availability and control**: the shop already owns the equipment, the stock is on
the shelf today, and there is no minimum order to clear and no lead time to plan around — the
kind of certainty that matters when the install date is already fixed. Its real cost is *higher
than the sticker width suggests*: every stile/rail requires a rough width of 7/4 in (net) + 1/4 in
(jointing [S1]) + 1/8 in (kerf [S2]) = 17/8 in (2-1/8 in) once converted to a common denominator —
real, recurring, fractional-inch waste on every one of this job's 96 pieces. Over the whole job
(34 board feet at $8.99/board foot [S3]) that comes to **$12.7358.../door**, a cost that is fixed
regardless of batch size because Standard Stock carries no minimum order.

## Argument for B — The Special Order

B's real, quantitative case is that its exact-width supply eliminates all width waste — but its
correctly-computed cost is not simply "$9.34/board foot [S3][S4] times the board feet actually
used." Appendix E's 30-board-foot minimum (MA1) means Grace must pay for 30 board feet even though
this job's stiles/rails only need 28, so B's true cost is **$280.20 total, $11.675/door** — genuinely
cheaper than A's $12.7358.../door, but only because this job's 24-door batch is large enough to
absorb the 2 unused board feet without erasing the per-board-foot savings. B's real weakness is
structural: the minimum order and 1–2 week lead time [S5] are commitments Grace has to make before
she can change her mind, and a smaller job would not clear the threshold at all (see "The margin,"
below).

## The margin — real numbers, and how thin they are

`case.json.balance.margin_pct` = **8.33%**, inside the project's 5–10% target band. The
arithmetic, in full:

- **Standard Stock (A):** rough width 17/8 in (2-1/8 in) per piece x 24 in length x 1 in thickness
  / 144 = 17/48 board feet/piece x 4 pieces/door = 17/12 board feet/door x 24 doors = **34 board
  feet total** x $8.99/board foot [S3] = $305.66 -> **$12.7358.../door** (constant at any batch
  size — no minimum order applies to Standard Stock).
- **The Special Order (B):** exact width 7/4 in per piece -> 7/24 board feet/piece x 4 pieces/door
  = 7/6 board feet/door x 24 doors = **28 board feet needed**. Appendix E's 30-board-foot minimum
  (MA1) means Grace buys **30 board feet**, not 28. 30 x $9.34/board foot [S3][S4] = $280.20 ->
  **$11.675/door**.
- **Margin:** |12.7358 - 11.675| / 12.7358 = **8.33%**. B is the cheaper option under MA1's
  current 30-board-foot value.

**Why this matters for the facilitator, specifically:** the breakeven batch size — the smallest
number of doors at which B's cost per door first drops below A's — is **23 doors**. This job's
batch of 24 doors clears that threshold by exactly **one door**. At 22 doors, B would still be
(barely) more expensive than A ($12.7364 vs. $12.7358/door); at 23 doors it flips ($12.18 vs.
$12.7358). MA1's 30-board-foot minimum is the case's single load-bearing dial: raise it and the
breakeven batch size rises with it, and a large enough increase pushes the breakeven past 24 doors
and flips this exact job's recommendation to A. **Do not treat a student who argues the minimum
should be lower, and concludes "B wins by even more," as having found the case's fragility — the
fragile direction is upward, and the margin is thin enough (one door of headroom) that facilitators
should expect this to come up.**

## Five Socratic questions

1. Your D2 rough-width calculation adds three fractions with different denominators — why can't you just add the numerators of 7/4, the jointing allowance, and the kerf allowance directly?
2. Appendix D's two operators wrote down what looks like two different waste widths for the same physical cut — how do you prove, mathematically, that they measured the same thing?
3. One of Appendix D's three logged entries genuinely differs from the other two — what would happen to your total waste figure for the whole job if you assumed all three were equal without checking?
4. The Special Order only becomes worthwhile once you clear its minimum order quantity — walk us through how you found the batch size, in doors, where its cost per door first drops below Standard Stock's?
5. Appendix E's 30-board-foot minimum is not a published figure — if the real minimum this mill actually enforces were somewhat higher than 30 board feet, would this job's recommendation survive?

## The trap

**A learner who treats Appendix D's two logged waste widths (one unsimplified, in eighths; one
already reduced) as two genuinely different measurements — rather than recognizing they are the
same physical width in two fraction forms — will either double-count total waste (if they
mistakenly add both logs together) or become confused about which crew's number to trust, and
either error corrupts every downstream cost-per-door figure in D4.** This is the case's core
"comparing unsimplified fractions" trap: 6/8 and 3/4 (or whatever the sourced allowance sum turns
out to equal) are the *same* width, and a pitch that never reduces both entries to lowest terms
before comparing them has fallen into this trap even if its final dollar figures look plausible.
A second, related version of the same trap: a student who correctly computes D2's rough width in
fraction form but then silently switches to decimals for D4's cost comparison has abandoned the
case's explicit fraction-only instruction — watch for a pitch with a clean fraction-based D2 and
a suddenly-decimal D4.

**A third trap (Tier 2 P3 finding, added after adversarial review):** a student can execute D2
perfectly as a standalone fraction drill and still silently revert to the net width (7/4 in,
1-3/4 in) instead of carrying forward their own D2 answer (17/8 in, 2-1/8 in) when they set up
D4's cost formula for Standard Stock. This is a genuinely easy slip to miss because 7/4 in is the
single most-repeated number in the whole case (it is the correct width for Option B, it is the
cut-list's headline figure, and it appears in the title of nearly every table) — nothing in
Challenge 3 explicitly flags "carry D2's result forward," the way Appendix D's own text flags
itself as a reconciliation exercise for the waste-log trap above. A pitch whose D4 cost-per-door
for Standard Stock comes out to $8.99 x 7/4 x (24/144) x 4 = $10.4883/door instead of the correct
$12.7358/door (using 17/8 in) has fallen into this trap — and because that wrong number is
*lower* than the correct one, it can make Standard Stock look artificially competitive with, or
even cheaper than, The Special Order. Watch for a D4 table whose Standard Stock width column does
not match D2's own stated rough-width answer.

## Twist

Structural, not a dropped mid-discussion fact: **this job's batch of 24 doors clears the 23-door
breakeven threshold by exactly one door**, and Appendix E's 30-board-foot minimum is an
undisclosed-to-the-mill, author-stated assumption rather than a measured fact. A student who gets
D2's common-denominator addition wrong in either direction (too small an allowance understates
Standard Stock's true cost; too large overstates it) will compute a different breakeven batch size
without realizing their arithmetic error, not their judgment, moved the answer — and because the
job's real headroom above breakeven is only one door, even a small arithmetic slip can flip which
option looks cheaper. Facilitators should treat the moment a student double-checks their D2 total
against a partner's as the natural twist moment, and can manufacture it directly with Socratic
Question 5: "If the real minimum this mill enforces were somewhat higher than 30 board feet, would
this job's recommendation survive?"

---

## Guide Notes — the anchor ladder (SPEC Section 7, anchor-ladder subsection)

### Intro
Frame the format: a blinking cursor, a saw screaming in the background, a fixed install date. This
is a real small-business sourcing decision wearing a lumber cut list, not a fractions worksheet
wearing a story.

### Launch
Read the Overview aloud. Stop at "Her thumb hovers over the quantity field." Ask the room: "Before
you've seen a single number, which of the two options do you already suspect costs more per
door — and why?"

### Anchor 1 — TAKE A STAND AND VOTE
No reasoning yet. "Standard Stock or The Special Order — show of hands." Record the split.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?
Push the room past "which stock is nicer" toward "which option's *true* cost per door, once
milling waste is counted honestly, is actually lower." Surface that the cut list's 1-3/4" width
is not the width Grace actually has to buy under Option A.

### Anchor 3 — WHAT IS THE PROCESS?
Before touching Appendix B/C's numbers, get the room to state the process out loud: find the true
rough width per stile (D2), reconcile the waste log (D3), then compare true cost per door across
both options at the job's real batch size (D4). Re-ask: "Now that we have a process, is 'which
stock is nicer' still the right question?"

### Anchor 4 — WHAT DON'T WE KNOW?
Name the load-bearing unknown explicitly: Appendix E's 30-board-foot minimum order quantity is not
a published figure from a real mill — it is this case's own stated Modeling Assumption (MA1),
because no source publishes a minimum specific to a small custom exact-width dimensioning run.
"Is 30 board feet a fact, or a stated, defensible guess? What would make a different guess just as
defensible?"

### Data Deep Dive
Open Appendices A–E. Run D1–D5 as a room, or have groups report out. This is also the moment to
run Socratic Questions 1 and 3 (common denominators, and the compound board-footage build-out).

### Twist
Once D2 and D4 are on the table, run Socratic Questions 4 and 5: "How many doors of headroom does
this job actually have above the breakeven batch size?" (Answer: exactly one door — 24 vs. a
23-door threshold.) Then: "If the real minimum this mill enforces were somewhat higher than 30
board feet, would this job's recommendation survive?" Let the room discover how thin the margin
(8.33%) and the batch-size headroom (one door) actually are.

### Close
VOTE AGAIN. "Did the vote move? For anyone who didn't move, what would it take to change your
mind — a different number, or a different priority (cost vs. schedule certainty) entirely?"

### Lessons Learned
The core transferable idea: two numbers that look different on paper (an unsimplified fraction and
a simplified one; a net width and a true rough width) can be the same or meaningfully different,
and the only way to tell is to actually do the fraction arithmetic — not to trust how a number is
written down.

### Standards Touched On
Equivalent Fractions; Simplify; Improper Fraction; Mixed Number; How to find equivalent fractions;
How to simplify a fraction; How to convert an improper fraction to a mixed number; How to convert
a mixed number to an improper fraction.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold read of the Overview, gut-check vote (Anchor 1) — no numbers shown yet |
| 3:00–8:00 | Position defense: "Convince us your pick is cheaper, not just more familiar" |
| 8:00–20:00 | Data Deep Dive — build D1's conversion table and D2's rough-width sum as a room |
| 20:00–30:00 | Reconcile Appendix D's waste log (D3); build D4's cost-per-door and breakeven |
| **30:00** | **DROP THE TWIST** — "This job's batch clears the breakeven threshold by exactly one door. If the mill's real minimum were somewhat higher than 30 board feet, does the recommendation survive?" |
| 30:00–38:00 | Pressure-test MA1 directly: re-derive D4's breakeven with a higher assumed minimum and see where the answer moves |
| 38:00–45:00 | Close, re-vote, D5's visual walkthrough, lessons learned |

## Cohort bands (SPEC Section 7, cohort-bands subsection)

| Band | Typical size | What changes |
|---|---|---|
| **Full (12–20)** | the size this case is written for | Anchors and the 45-minute timed plan run as written above |
| **Compressed (6–11)** | smaller room | Anchors 2–3 combine into one pass; the 20:00–30:00 build-out runs as a single worked example instead of small-group work; total runtime shortens proportionally |
| **1:1 / pair (1–2)** | tutoring context | No vote at Anchor 1 — ask for a stated initial position and why instead; the facilitator plays devil's advocate directly; the arithmetic pressure-test (30:00–38:00) still runs in full |
