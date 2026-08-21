# Guide Notes: Insurance

**Case:** Insurance · **Tier:** T3 · **Band:** MS-stretch / HS-entry · **Studio:** Adventure
**Standards:** see `case.json.standards[]` for the exact ids (32 skills — algebraic variables/
constants/coefficients/terms, percent, decimal arithmetic, probability, mean, and two required
visual displays)

Legacy conversion, 2026-08-20, built from the original case study docx
(`source/Y3/Session 2/Insurance/Case Study_ Health Insurance.docx` and `Guide Notes.docx`, plus 6
bundled reference PDFs) onto the current 11-anchor ladder, with the binary dilemma re-locked per
`cases/_concepts/LEGACY_DILEMMA_LOCKS_2026-08-20.md`. See `case.json.legacy_conversion_note` for
the full account of what changed and why, including the primary-metric retune (raw dollar cost is
a real landslide; the graded metric is each plan's out-of-pocket maximum instead).

**A note on sensitive content (SPEC §6):** this case touches a real family's health information
(a child's chronic condition, a couple discussing a future pregnancy) and money stress after a
voluntary job change. Keep the discussion on the math and the disclosed numbers — this is not an
invitation for Heroes or the facilitator to share personal medical or financial history.

## Intro

Frame the format: this is a real family's real 2021 insurance decision, not a worksheet with a
story stapled on. Name the opener — "Two ways to insure a family of five. One costs $569 less
every single month. The other one costs less if things go wrong. You have to pick before you know
which year this is."

## Launch

Read the Overview aloud, then Background's two sentences establishing the two options (HDHP+HSA
vs. Navigator Gold 2000) and the real $1,394/month tax credit, with no Appendix numbers shown yet.
Ask: "Just from what you've heard — does 'cheaper' sound like an easy question here?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who's going HDHP? Who's staying with Gold 2000?" Show of hands, no discussion yet. Record the
count — Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'cheaper'?"**

Push on what "cheaper" means here. Cheaper *this month, on the premium bill*? Cheaper *over the
whole year, on average*? Cheaper *in the worst case, if something goes badly wrong*? Let the room
sit in the ambiguity — "Is anyone courageous enough to define 'cheaper' before we start adding
numbers?" Deliberately let it feel underdetermined: "Wow, this is a harder question than it
sounded."

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has picked a working definition of "cheaper," ask them to name the actual steps:
total premium (Appendix A), total expected out-of-pocket given the family's real care pattern
(Appendix C/D), and each plan's out-of-pocket maximum (Appendix A). Re-ask: "Given how we just
defined 'cheaper' — is that still the right process?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix G's five Modeling Assumptions as a group, out loud, before anyone computes
anything — especially MA1 (the HDHP's coinsurance rate, which the source never actually states)
and MA2 (the friend's plan is secondhand, unverified). Ask which ones the room thinks matter most.

## Data Deep Dive

Now, and only now, the numbers. Walk D1 and D2's cost breakdown together as a room.

**The trap:** most Heroes will compute the premium gap ($6,828/year, real and large), maybe layer
on the family's real 2020 care pattern, and conclude the HDHP wins by a landslide — which is
arithmetically correct (Appendix A/case.json.balance.argument_a; base case margin ~39.5%). The
trap is stopping there and treating the case as solved. The case's actual graded question (SEE
`case.json.primary_metric`) is a different, real, sourced number: each plan's own stated
out-of-pocket MAXIMUM — Option A $12,800, Option B $12,000, a real, close 6.7% gap the OTHER way.
Cold-call on this specifically once the landslide argument has been made confidently: "You've just
told me one plan is obviously way cheaper. Does either plan's own paperwork say how much you could
lose in a bad year? Did you check those two numbers against each other?"

## Twist — drop this at roughly the 15-minute mark

Deliver slowly, with pauses:

"Everyone's argument so far has used the family's real 2020 medical history — no ER visits beyond
what's already documented, no big surprises. Here's something the Sandersons have actually
discussed: Tiffany and Greg are considering trying for a fourth child this year. Let's say it's not
hypothetical anymore. Tiffany is pregnant, due later this year."

**Facilitator-only.** Recompute both totals live with the room, using Navigator Gold 2000's own
real SBC coverage example for pregnancy ($12,700 total cost, patient share $4,170):

- Option A (HDHP): total pre-insurance spend for the year rises to $19,057.04; the family blows
  past its $6,300 deductible and now owes the deductible plus 20% coinsurance on the rest —
  $8,851.41 out of pocket, **69% of its own $12,800 cap.** Total for the year: $10,351.41.
- Option B (Gold 2000): baseline copays/coinsurance ($2,568.00) plus the real $4,170 pregnancy
  share = $6,738.00 out of pocket, **56% of its own $12,000 cap.** Total for the year: $15,066.00.

Option A is *still* cheaper on raw total dollars ($10,351.41 vs. $15,066.00) — the twist does not
flip the landslide. What it does do: it turns "out-of-pocket maximum" from an abstract number
nobody expected to hit into something both families are now most of the way toward, in a single
real, plausible year. Ask: "You now have 60 seconds. Does this change your recommendation — or
not?" Then, the follow-up that matters more than the vote: **"What just broke in your original
model? Was the landslide argument wrong — or was it just missing how close a real bad year can
get to each cap?"**

Do not hand over a "correct" answer. A family that just spent $6,828 less on premium and is still
$4,714.59 cheaper overall, even in a pregnancy year, has a genuinely strong case — and a family that
values a fully predictable bill and keeping their current doctors has a genuinely strong case too.

**Twist soundness check (SPEC §6):** re-derived under both a sequential reading (pregnancy is one
more real event layered onto the family's existing 2021 care) and a standalone reading (pregnancy
alone, ignoring the rest of the year's care) of every stated Modeling Assumption — holds under
both; the pregnancy share alone ($4,170 for B, or $6,300 deductible-clearing for A) is large enough
on its own to make both caps feel real, without needing the rest of the year's spending to make the
point.

## Immediate recommit

Re-vote immediately. "Did the pregnancy reveal change your hand — or did it just change *why*
you're holding it up?"

## Close

Re-vote once more after full discussion. Ask: "Did we ask the right question at Anchor 2, or did
'cheaper' turn out to mean something different by the end?" And: "What math was new to you today,
and how did you attack it?"

## Lessons Learned

*(Migrated and extended from the original Guide Notes.)* The original guide's own reflection said
introducing the HSA/HDHP option "with little background at the onset" was a mistake, and suggested
introducing a pregnancy as the twist — this conversion builds the twist exactly that way, with real
sourced numbers instead of an invented one. The original guide also noted the room got "deep into
the topic" despite a rocky start, with heroes "challenging each other more than usual" — that
energy is best protected here by NOT resolving the landslide-vs-cap tension for the room. The
mathematically real lesson this conversion adds: **the metric you choose decides the winner.** On
raw average-case dollars, the HDHP wins by a landslide, every time this case's own real numbers are
tested. On worst-case exposure — a real number both plans publish — Navigator Gold 2000 wins, by a
real but much narrower margin. Both are true at once; the discussion is about which one a family
that has already lost one income should weight more heavily.

## Five Socratic Questions

Use these across Anchors 2–4 and the Data Deep Dive — each is answerable only with this case's own
numbers, not general opinion.

1. The HDHP saves $6,828 a year in premium alone — how many "ordinary" years like 2020 would it take for that premium savings to get eaten up by the HDHP's own higher out-of-pocket costs?
2. Navigator Gold 2000's out-of-pocket maximum ($12,000) is $800 lower than the HDHP's ($12,800) — is an $800 difference in your absolute worst case worth $6,828 a year in guaranteed premium?
3. Neither plan is confirmed to be accepted by the family's current doctors if they pick the HDHP — how would you put a dollar value on "keeping the same urologist for Neri"?
4. Under the pregnancy twist, Option A is still cheaper overall ($10,351.41 vs. $15,066.00) — at what total pregnancy cost would Option B actually become the cheaper total?
5. The friend's HDHP numbers were relayed secondhand, not from the family's own marketplace application like Navigator Gold 2000's were — how much does that change how much you'd trust them?

## Standards Touched On

See `case.json.standards[]` (32 ids) and `LEARNING_GOALS.md` for the full deliverable ↔ skill
matrix. In brief: algebraic variables/constants/coefficients/terms and evaluating an expression,
percent (coinsurance), decimal/currency arithmetic, probability and mean (from the family's real
2020 incident data), and two required visual displays (bar graph, pie/comparison chart).

## Cohort Bands

See `case.json.cohort_bands[]`.

- **Full (12–20):** Anchors 2–3 run as written; the room splits into a "premium is real money, pick
  the cheap plan" faction and a "the cap protects you when it matters" faction before the Twist
  forces everyone to hold both numbers at once.
- **Compressed (6–11):** Anchors 2–3 combine into one pass; D5's two visual displays are worked as
  one shared example (one option) instead of every Hero building both independently.
- **1:1 / pair (1–2):** No vote to take — Anchor 1 becomes a stated initial position instead of a
  cold-call show of hands; the guide plays devil's advocate directly, arguing whichever side the
  Hero didn't pick.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote (Anchor 1) — no explanation |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just cheaper" |
| 10:00–15:00 | Pressure-test the models: "Did you check the out-of-pocket maximum, or just the premium?" |
| **15:00** | **DROP THE TWIST** — the pregnancy reveal, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00–30:00 | Threaded deep conflict — two named threads: (1) "average-case cost" vs. "worst-case exposure" as competing definitions of *cheaper*; (2) predictable small bills (Gold 2000's copays) vs. a much smaller guaranteed monthly bill (the HDHP's premium) as competing definitions of *affordable* |
| 30:00–45:00 | Close, re-vote, reflection, Lessons Learned |
