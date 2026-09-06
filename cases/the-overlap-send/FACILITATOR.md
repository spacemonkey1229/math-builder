# FACILITATOR.md — The Overlap Send

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Overlap Send · **Tier:** T2 (MS-core) · **Studio:** MS Launchpad
**Standards:** Discrete Mathematics/Set Theory — Set, Subset, Union, Intersection, Empty Set,
Venn Diagram, and two "how to…" skills (union/intersection, Venn diagram) — see
`case.json.standards[]` for exact ids.

**Status:** `case-research` complete (2026-09-05). All `{{NEEDS_SOURCE: ...}}` placeholders in
`case.md` are resolved — one real Klaviyo benchmark figure is sourced (Appendix E, [S1]), three
supplemental real studies inform two assumptions' basis ([S2]-[S4]), and the CRM list sizes,
per-recipient cost, budget, intersection conversion rate, and AOV are disclosed Modeling
Assumptions MA1–MA5, because no publishable figure exists for any of them. `case.json.balance.margin_pct`
is a real, computed **14.1%**. Everything below is the case of record, not a placeholder.

**Sensitivity note (SPEC §6):** ordinary workplace pressure — a solo marketer facing a board
deadline and a fixed budget. No illness, death, or family hardship. Standard facilitator handling
suffices.

## Argument for A — Cast The Net

Option A's case is the **raw-reach argument**: mailing the union of both lists reaches 53,100
names [MA1] — 7.7x Option B's 6,900 — using a real, sourced, HIGH-confidence conversion rate
[S1], not an authored guess. This matters because A's conversion rate is the one figure in this
case nobody can challenge as arbitrary; whatever a Hero thinks about the intersection segment's
assumed lift (MA4), A's side of the comparison rests on a real Klaviyo benchmark. **Under the
case's own current numbers, A is close but ultimately loses on raw expected value** (see "The
margin" below) — A's real strength is that its math depends on the fewest authored assumptions,
and the case is thin enough (14.1%) that a defensible challenge to almost any one of Option B's
assumed figures flips the recommendation back to A.

## Argument for B — Mail The Middle

B's real, quantitative case is Challenge 3 (D4)'s actual expected-net-revenue comparison,
correctly weighted by conversion rate: under MA4's stated 0.60% intersection-segment rate, Option
B's expected net revenue comes out **higher** than Option A's (see "The margin" below), despite
mailing 7.7x fewer names. This is a genuinely different route to a plausible-sounding conclusion
than the reasoning shortcut named later in this guide (which reaches a similar-sounding "the small
list can't possibly beat the big one" intuition backwards) — B's D4-based case is the correct
answer to the correctly-posed question, at least under MA4's current value. It is also fragile:
because MA4 (like several of this case's other assumptions) is a stated Modeling Assumption, not
an empirical certainty, a Hero who mounts a defensible challenge that the real conversion lift is
smaller than assumed can legitimately move the comparison back toward A.

## The margin — real numbers, and how fragile this case actually is

`case.json.balance.margin_pct` = **14.1%**, inside the SPEC §2 target 10–15% band. The arithmetic,
in full:

- **Reach:** `|P ∪ L|` = 21,400 + 38,600 − 6,900 = **53,100** (Option A). `|P ∩ L|` = **6,900**
  (Option B).
- **Option A (Cast The Net):** 53,100 × 0.16% × $58 − 53,100 × $0.06 = $4,927.68 − $3,186.00 =
  **$1,741.68**.
- **Option B (Mail The Middle):** 6,900 × 0.60% × $58 − 6,900 × $0.06 = $2,401.20 − $414.00 =
  **$1,987.20**.
- **Margin:** |1,987.20 − 1,741.68| / 1,741.68 = **14.1%** (the loser's value is the denominator, per the corpus's standard margin formula).

**Under the case's current numbers, B is the higher-expected-revenue option** — $1,987.20 against
A's $1,741.68. This margin is a designed property of five authored Modeling Assumptions (MA1, MA2,
MA4, MA5's values), not an empirical finding — only the 0.16% broad-send conversion rate [S1] is a
real, sourced figure.

**Why this matters for the facilitator, specifically:** this case is unusually fragile by design.
`sensitivity_model.py`'s ±50% flex sweep found that **every one of the six flexed assumptions
breaks the case's balance in at least one direction**, and six of the twelve flex points actually
**flip the recommendation from B to A**: `p_size` (+50%), `l_size` (+50%), `p_and_l` (−50%),
`per_recipient_cost` (−50%), `conv_intersection` (−50%), and `aov` (+50%). All six are disclosed
in `case.json.sensitivity_disclosure[]` as Category X (proprietary/inaccessible estimates). The
single most sensitive lever is `conv_intersection` (MA4) — a modest downward challenge to the
0.60% intersection conversion-rate assumption is the single cleanest way to flip the case, and it
is also the assumption a sharp student is most likely to challenge, since it is the only Appendix C
figure with no direct public benchmark behind it (unlike [S1]). **Do not treat a student who argues
the intersection rate should be even higher, and concludes "B wins by even more," as having found
the case's fragility — the more pedagogically interesting move is downward, toward A.**

## Five Socratic questions

1. Option A's list has 7.7 times the reach of Option B's — why isn't "more names" the same thing as "more expected revenue"?
2. MA4 sets the intersection segment's conversion rate at 0.60% — no source measures this exact segment. If the real rate were meaningfully lower, would Option B still come out ahead, or does the recommendation flip to Option A?
3. You checked whether any of the four Venn-diagram regions was the empty set — what would it have meant for this whole decision if P ∩ L actually *were* empty?
4. Is Set P a subset of Set L, or Set L a subset of Set P, or neither — and how do you know, from the actual counts in Appendix A, not just intuition about which list "sounds bigger"?
5. If the whole case rests on five separate authored assumptions rather than five sourced facts, what would you need to see to trust MA1/MA2/MA4/MA5 more than you do right now — and does knowing the case's own margin is only 14.1% wide make that question more or less urgent?

## The trap

**A learner who eyeballs "Option A's list has several times the reach of Option B's" and stops
there will pick Option A without ever computing expected revenue — missing that reach and
conversion rate do not trade off one-to-one.** The whole point of this case is that only the
*product* of reach and conversion rate (minus cost) tells you which option actually wins. A pitch
that compares raw reach counts (53,100 vs. 6,900) without multiplying through by each option's own
conversion rate and AOV, or that compares total revenue without subtracting the flat
per-recipient cost, has fallen into this trap even if it reaches the same recommendation B's
correct math also favors, and even if its prose sounds confident.

**A second, related trap:** a student who correctly computes D1–D3 can still get D4 wrong by
applying the *wrong* conversion rate to the *wrong* reach figure — e.g., multiplying Option A's
much larger reach by the intersection segment's higher 0.60% rate (an "everyone converts like the
best segment" error), or multiplying Option B's small reach by the broad 0.16% rate (a "the
overlap segment is nothing special" error). Either swap produces a plausible-looking dollar figure
built from real numbers in the case, but silently erases the entire reason the two options are
compared separately. Watch for a D4 table where the two conversion rates appear to have been
swapped, or where only one rate is used for both rows.

## Twist

Not built as a scripted mid-discussion reveal for this case — the "twist" here is structural
rather than a dropped new fact, and it lives inside MA4 itself: **the assumption a Hero is most
likely to challenge (the 0.60% intersection conversion rate, since it is the one Appendix C figure
with no direct public benchmark behind it) is also the single lever most likely to flip the entire
recommendation from B to A.** Facilitators should treat the moment a student notices this — usually
while working through Socratic Question 2 — as the twist moment, and can manufacture it directly by
asking Question 2 if no student raises it unprompted.

---

## Guide Notes — the anchor ladder (SPEC Section 7, anchor-ladder subsection)

### Intro

Frame the format: two customer lists nobody on a three-person team has ever actually compared,
one send, one number to bring to the board on Friday.

### Launch

Read the Overview aloud. Stop at "One list. One send. One number to bring to the board on
Friday." Ask the room: "Before you've seen a single number, which list do you think should win —
the big one or the overlapping one? Why?"

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "Cast The Net or Mail The Middle — show of hands." Record the split. Most rooms
will lean toward the bigger list before seeing any numbers.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push the room past "which list is bigger" toward "which list produces more real, expected
revenue once you account for how differently each one actually converts." Let the room sit with
the fact that the intersection segment's conversion rate (MA4) is not published anywhere — it is
the case's own stated Modeling Assumption, not a fact anyone can look up.

### Anchor 3 — WHAT IS THE PROCESS?

Before touching Appendix C's numbers, get the room to state the actual comparison method out
loud: draw the Venn diagram (D1), compute the set sizes with inclusion-exclusion (D2), price each
option out against the budget (D3), then weight each option's reach by its own conversion rate to
get an expected-revenue figure comparable across both options (D4). Re-ask: "Is 'which list is
bigger' still the right question?"

### Anchor 4 — WHAT DON'T WE KNOW?

Name the load-bearing unknown explicitly: nobody — not Klaviyo, not Basecamp Crate, not this
case — has ever measured a real conversion rate for exactly "recent purchaser AND newsletter
subscriber." "Is 0.60% a fact, or a stated, defensible guess? What would make a different guess
just as defensible?"

### Data Deep Dive

Now open Appendices A–D. Run D1–D5 as a room, or have groups report out. This is also the moment
to run Socratic Questions 1, 3, and 4 (the reach-vs-rate logic, the empty-set check, and the
subset determination).

### Twist

Once D4's numbers are on the table and a recommendation has started to form, run Socratic
Question 2 directly: "MA4's 0.60% is the one number in this case nobody actually measured. If the
real rate is lower, does your recommendation survive?" Let the room discover that the margin is
only 14.1% — closer than almost anyone will expect from a "the math says so" pitch — and that a
defensible downward challenge to MA4 alone is enough to flip it.

### Close

VOTE AGAIN. "Did the vote move? For the people who didn't move, what would it take to change your
mind — a different number, or a different assumption entirely?"

### Lessons Learned

The core transferable idea: when reach and conversion rate move in opposite directions, only their
*product* (net of cost) tells you which option actually wins — eyeballing either number alone,
even a genuinely sourced one, can point you the wrong way. A second, equally real lesson: a case
built almost entirely from disclosed, authored assumptions can still produce a defensible
recommendation, as long as the assumptions and their fragility are stated in the open rather than
buried.

### Standards Touched On

Set, Subset, Union, Intersection, Empty Set, Venn Diagram; How to find the union and intersection
of two sets; How to represent a set relationship using a Venn diagram.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold read of the Overview, gut-check vote (Anchor 1) — no numbers shown yet |
| 3:00–8:00 | Position defense: "Convince us your list wins, not just that it's bigger or tighter" |
| 8:00–20:00 | Data Deep Dive — build the Venn diagram (D1) and the set-notation summary (D2) as a room |
| 20:00–30:00 | Build D3's cost table and D4's expected-net-revenue comparison; confirm the 14.1% margin and where it comes from |
| **30:00** | **DROP THE TWIST** — Socratic Question 2: MA4's 0.60% intersection rate is unmeasured; if the real rate is lower, does the recommendation survive? |
| 30:00–38:00 | Pressure-test MA4 directly: how close is 14.1% to flipping, and what would a defensible challenge to the intersection rate, list sizes, cost, or AOV actually change? |
| 38:00–45:00 | Close, re-vote, D1/D2's empty-set and subset findings, lessons learned |

## Cohort bands (SPEC Section 7, cohort-bands subsection)

| Band | Typical size | What changes |
|---|---|---|
| **Full (12–20)** | the size this case is written for | Anchors and the 45-minute timed plan run as written above |
| **Compressed (6–11)** | smaller room | Anchors 2–3 combine into one pass; the 20:00–30:00 cost/expected-revenue build-out runs as a single worked example instead of small-group work; total runtime shortens proportionally |
| **1:1 / pair (1–2)** | tutoring context | No vote at Anchor 1 — ask for a stated initial position and why instead; the facilitator plays devil's advocate directly rather than cold-calling the room; the MA4 pressure-test (30:00–38:00) still runs in full, since it is the single most important move in the case |
