# FACILITATOR.md — The Minimum-Payment Trap

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the end of case.md.*

**Case:** The Minimum-Payment Trap · **Tier:** T3 (MS-stretch / HS-entry) · **Studio:** MS Adventure
**Standards:** Discrete Mathematics — Recursive Formula, Base Case, and the how-to for writing a
recursive formula for a sequence; plus Advanced Numbers' Percent and its how-to for finding the
percent of a number (see `case.json.standards[]` for exact ids).

**Status:** `case-research` complete (2026-09-04). All `{{NEEDS_SOURCE: ...}}` placeholders in
`case.md` are resolved — every figure is a real, cited number (Appendix E): a national-average
starting balance (LendingTree), a real average APR (CFPB), a real major issuer's own minimum-payment
formula (Chase), and a real CARD Act-mandated 36-month payoff disclosure (CFPB Reg Z Appendix M1),
with the specific dollar amount of that disclosure derived from the sourced balance and APR.
`case.json.balance.margin_pct` is a real, computed **10.8%**. No Modeling Assumptions were needed —
every figure is sourced. Everything below is the case of record, not a placeholder.

**Sensitivity note (SPEC §6):** this case touches ordinary money stress — a working nurse who took
on credit card debt during a real income disruption (cut hours), now budgeting a fixed monthly
payment against a shared long-term goal (a mortgage pre-approval). No illness, death, or family
hardship beyond that. Facilitators should be alert if a Hero's own household has faced a similar
income disruption.

## Argument for A — The Minimum Track

Option A's real strength is **liquidity, not price**: its required payment starts at $240.44 in
month 1 and keeps shrinking — down to $202.67 by month 18 — because the formula recalculates off a
smaller balance every cycle, while The Fixed Push demands a flat $309.20 with no exceptions. Summed
over the eighteen months, The Minimum Track requires $3,978.88 in total payments versus The Fixed
Push's $5,565.57 — a real $1,586.69 kept in Priya's monthly budget across the same window. **Under
the case's own numbers, this is the harder argument to win on total cost** (see "The margin" below)
— its real strength is that it survives another income shock, which is exactly what created this
balance in the first place (SEE BACKGROUND), and it is only a thin margin away from being close on
interest too.

## Argument for B — The Fixed Push

B's case rests on two real, computed numbers, not one: it pays $290.79 less in interest over the
same eighteen months (a real but thin 10.8% margin — see "The margin" below), **and**, more
important for what Priya is actually optimizing for, it leaves the balance at $4,595.01 by month 18
versus The Minimum Track's $6,472.49 — a $1,877.48 difference in exactly the number a mortgage
lender looks at when Priya and her partner sit down for the pre-approval conversation. B's argument
is not "The Minimum Track is a bad idea," it is "the eighteen-month interest margin alone
understates how much this decision matters, because the metric Priya actually cares about at month
18 is the balance, not the interest paid to get there."

## The margin — real numbers, and why eighteen months, not lifetime

`case.json.balance.margin_pct` = **10.8%**, inside the SPEC §2 target 10-15% band. The arithmetic,
in full (both computed by iterating the same recursive model from `sensitivity_model.py`, starting
at Appendix A's $7,756 balance, 25.2% APR, monthly rate 2.1%):

- **The Minimum Track (A), 18-month interest:** sum of each month's `balance_(n-1) x 0.021`, where
  `payment_n = max(0.01 x balance_(n-1) + interest_n, 40)` — **$2,695.37**.
- **The Fixed Push (B), 18-month interest:** same monthly interest formula, but `payment_n = 309.20`
  fixed every month — **$2,404.58**.
- **Margin:** |2,695.37 − 2,404.58| / 2,695.37 = 290.79 / 2,695.37 = **10.8%**.

**Why the graded comparison is eighteen months, not the full life of the balance — say this out loud
to a Hero who asks:** comparing LIFETIME total interest instead is a real, sourced, and dramatically
lopsided figure — $14,465.14 over 19.42 years (233 months) for The Minimum Track, versus $3,375.11
over exactly 3 years (36 months) for The Fixed Push. That comparison is real and un-engineered (it's
exactly what D4 asks students to compute), but it structurally cannot land inside SPEC §2's 20% cap,
because a payment that shrinks every month as the balance shrinks *cannot* keep pace with a fixed
payment over the full life of a debt — the gap is not a modeling choice, it is what "minimum
payment" mathematically means. Eighteen months is not an arbitrary shrink-to-fit window: it is
Priya's own stated real-world decision horizon (SEE BACKGROUND — the mortgage conversation), and it
is the comparison that is actually genuinely close, which is what makes it defensible as the graded
primary metric, while the dramatic lifetime numbers still appear in the case (D4) as real, unforced
context.

## Five Socratic questions

1. Your D2 table shows The Minimum Track's required payment shrinking from $240.44 in month 1 to $202.67 in month 18 — why doesn't paying less each month mean you're paying less overall?
2. The Fixed Push saves only $290.79 in interest over eighteen months, a 10.8% margin — is that margin alone a strong enough reason to give up $1,586.69 in monthly cash flow over the same period?
3. If you had charged interest on Appendix A's original $7,756 for all eighteen months instead of recalculating it every month on the shrinking balance, would your D2 interest total have come out higher or lower than your real answer — and by how much?
4. The Minimum Track and The Fixed Push start out demanding a similar monthly dollar amount in month 1 — at what point in your D2 table do the two strategies stop looking similar, and why does that moment matter more than comparing their sticker prices?
5. If Priya's hours got cut again halfway through the eighteen months, which strategy is easier to keep paying — and does that change which option you'd recommend, even knowing The Fixed Push leaves a lower balance at month 18?

## The trap

**A learner who compares the two strategies' MONTH-ONE payments ($240.44 vs. $309.20) and concludes
The Minimum Track is "obviously cheaper" — without ever running the D1 recursion past month one —
has fallen into the case's main trap.** The two payments look close on day one specifically because
the case is designed that way; the whole point is that one of them (The Minimum Track) recalculates
itself smaller every month as a direct consequence of barely denting the balance, while the other
(The Fixed Push) does not move. A pitch that never builds D2's full eighteen-row table for both
strategies, or that treats month 1's numbers as representative of the whole eighteen months, has
fallen into this trap even if it lands on the "correct" recommendation by coincidence.

**A second, related trap, named explicitly in Challenge 3 (D4) — and the case's real numeric trap,
not just a comparison-of-first-months mistake:** a learner who freezes Appendix A's *original*
$7,756 balance for every month's interest charge (and, for The Minimum Track, inside Appendix B's
"1% of balance" term too) instead of recalculating both on each month's own shrinking balance gets
the wrong answer for BOTH strategies — but **the two errors do not move the same direction, and a
guide who assumes they do will mis-referee the discussion.** Verified by hand and by
`sensitivity_model.py` (`case.json.derived`):

- **The Minimum Track (A):** freezing the balance also freezes the minimum-payment formula's "1% of
  balance" input, so the naive shortcut computes a CONSTANT $240.44/month forever (it never lets the
  required payment shrink, contradicting the very premise of "minimum payment"). That constant,
  too-high payment appears to clear the balance in only 100 months — **badly UNDERestimating** the
  true 233-month payoff — but because every one of those 100 months is charged the frozen, too-high
  $162.88 interest instead of a declining one, the naive total interest comes out to $16,287.60,
  which **OVERestimates** the true $14,465.14 figure. Months: under. Interest: over. Both wrong, in
  opposite directions.
- **The Fixed Push (B):** the $309.20 payment is already fixed by design, so freezing only the
  interest calculation makes the naive principal-per-month a constant $146.32, giving a naive payoff
  of about 53 months and $8,633.35 in interest — both **OVERestimating** the true 36 months and
  $3,375.11.

Watch for a pitch that reports one clean "always underestimates" or "always overestimates" rule
across both strategies — that pitch has not actually run the numbers for each strategy separately,
it has guessed a plausible-sounding pattern. (This finding was corrected during Tier 2 review: an
earlier draft of this guide claimed the shortcut "badly underestimates both the number of months and
the total interest paid" for The Minimum Track — true for months, but wrong for interest, confirmed
independently by two fresh Tier 2 subagents and by direct recomputation. Say the real, verified
direction, not the intuitive-sounding one.)

## Twist

Structural, not a scripted mid-discussion reveal: **the metric a Hero optimizes by default (total
interest paid) is not actually the metric Priya's own stated goal cares about (the balance at month
18).** This is a twist about Priya's own numbers, not an appeal to an outside, uncited lending rule
— Background is explicit that "meaningfully lower" is a goalpost she and her partner set for
themselves, not a figure a bank gave them. Facilitators should manufacture the twist directly, at
roughly the 30-minute mark, by telling the room: *"Priya and her partner's own goal is a card
balance they'll feel good showing a lender in eighteen months — not the lowest total interest paid
along the way. Does that change your recommendation?"* This does not make either option obviously
right — The Fixed Push's lower balance is a real, computed advantage ($4,595.01 vs. $6,472.49) that
a pure interest-margin comparison (10.8%) understates, but The Minimum Track's cash-flow protection
is still real given Priya's history of a hours cut, and a Hero can reasonably push back that Priya
never actually defined "meaningfully lower" in dollar terms, so the twist reframes the question
without fully resolving it. Watch for the room's `10.8%` anchor loosening once the balance numbers,
not just the interest numbers, are on the table.

---

## Guide Notes — the anchor ladder (SPEC, facilitator-artifacts anchor-ladder subsection)

### Intro

Frame the format: two buttons, same size, same color, one number already filled in for her. This
is a real household budgeting decision dressed as a banking-app screenshot, not the other way
around.

### Launch

Read the Overview aloud. Stop at "Her thumb hovers over the blank field." Ask the room: "Before
you've seen a single number, which button do you think you'd tap — and why does the bank make one
of them the default?"

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "The Minimum Track or The Fixed Push — show of hands." Record the split. Most
rooms split closer than they expect once they realize the two month-one payments look almost the
same size.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push the room past "which payment is bigger" toward "which strategy's required payment changes over
time, and why does that matter more than its starting size." Let the room sit with the fact that
Appendix B's formula recalculates every single month — nothing about The Minimum Track is fixed
except the *rule*, not the dollar amount.

### Anchor 3 — WHAT IS THE PROCESS?

Before touching any numbers past month one, get the room to state the actual method out loud: build
each strategy's recursive balance model (D1), iterate it eighteen times to get real month-by-month
figures (D2), then sum those figures into a real total and a real percent margin (D3). Re-ask: "Now
that we have a process, is 'which payment is bigger' still the right question?"

### Anchor 4 — WHAT DON'T WE KNOW?

Name what the case does NOT give the room: neither Appendix A, B, nor C states how many months The
Minimum Track actually takes to reach $0, or what its true lifetime interest is — that has to be
derived, not looked up. "Is that a gap in the case, or is that the actual point?"

### Data Deep Dive

Now open Appendices A-D. Run D1-D6 as a room, or have groups report out. This is also the moment
to run Socratic Questions 1 and 3 (why a shrinking payment doesn't mean shrinking total cost, and
the simple-interest trap).

### Twist

Once D3's eighteen-month numbers are on the table and a recommendation has started to form, deliver
the twist described above: Priya's own goal is the balance at month 18, not the interest paid to get
there. Run Socratic Question 2 immediately after.

### Close

VOTE AGAIN. "Did the vote move? For the people who didn't move, what would it take to change your
mind — a different number, or a different priority entirely?"

### Lessons Learned

The core transferable idea: a payment that recalculates itself smaller every month can look like
the "cheaper" option indefinitely if you only ever look at this month's bill — the real cost only
shows up when you run the recursion far enough to see where it actually leads (19.42 years and
$14,465.14 in interest, on a $7,756 balance).

### Standards Touched On

Recursive Formula, Base Case; How to write a recursive formula for a sequence; Percent; How to find
the percent of a number.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00-3:00 | Cold read of the Overview, gut-check vote (Anchor 1) — no numbers shown yet |
| 3:00-8:00 | Position defense: "Convince us your pick is the smarter budget move, not just the smaller bill" |
| 8:00-20:00 | Data Deep Dive — build D1's recursive model and D2's eighteen-month tables as a room |
| 20:00-30:00 | Build D3's totals and percent margin; confirm the 10.8% figure and where it comes from |
| **30:00** | **DROP THE TWIST** — Priya's own stated goal is the balance at month 18, not the interest paid to get there; run Socratic Question 2 |
| 30:00-38:00 | Pressure-test the recommendation: does the balance-at-month-18 framing change anyone's vote, and does it survive Socratic Question 5 (a second hours cut)? |
| 38:00-45:00 | Close, re-vote, D4's full-payoff reveal (19.42 years / $14,465.14 vs. 3 years / $3,375.11), lessons learned |

## Cohort bands (SPEC, facilitator-artifacts cohort-bands subsection)

| Band | Typical size | What changes |
|---|---|---|
| **Full (12-20)** | the size this case is written for | Anchors and the 45-minute timed plan run as written above |
| **Compressed (6-11)** | smaller room | Anchors 2-3 combine into one pass; D2's two eighteen-row tables are built as one shared worked example instead of small-group work; total runtime shortens proportionally |
| **1:1 / pair (1-2)** | tutoring context | No vote at Anchor 1 — ask for a stated initial position and why instead; the facilitator plays devil's advocate directly rather than cold-calling the room; the D4 full-payoff reveal (30:00-38:00 equivalent) still runs in full, since it is the single most important move in the case |
