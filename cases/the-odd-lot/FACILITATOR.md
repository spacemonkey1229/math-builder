# Guide Notes: The Odd Lot

MS/HS | Guide Notes | Adventure | 2026-27
**Tier:** T3 (MS-stretch / HS-entry) · **Primary metric:** dwelling-unit-years delivered within the planning horizon · **Margin:** 5.89% (fragile — see the sensitivity note before Lessons Learned)

---

## Intro

Heroes, Priya has one memo due Thursday and three oddly-shaped parcels nobody designed on purpose.
One option changes nothing and starts building next month. The other option is a better shape on
paper but needs three property owners to agree to something first. I don't have the answer either
— that's what the numbers are for.

## Launch

Show a map or satellite image of any city block where a diagonal street cuts through a rectangular
grid (Broadway through Manhattan works well — Union Square, Madison Square, Times Square are all
real examples). Ask: *"Why do you think this block is shaped like a wedge instead of a rectangle?
Who do you think decided that?"*

Let them guess. Then: *"Nobody did. That's the whole problem Priya has to solve."*

> **Hero name — Plat As-Is, or Replat & Consolidate? Commit out loud.**

---

## Anchor 1 — Take a stand and vote

Plat As-Is (A) or Replat & Consolidate (B). No reasoning yet.

Hands up for A. Hands up for B. Write the split on the board.

*"Is anyone courageous enough to stand with ______?"*

## Anchor 2 — What is the problem we're solving?

Do **not** let them start calculating yet.

- What's the actual question, in one sentence?
- Is it "which option builds more apartments"? Is it "which option is fastest"? Is it "which option
  delivers the most total housing, counted over time, given the city has a deadline"? **Those sound
  similar and are not the same question** — only the last one is what this case's numbers actually
  measure.
- Someone will say "obviously consolidate, one big regular lot is always more efficient than three
  weird ones." Push: *"More efficient at what — building footprint, or delivering housing by a real
  deadline? Does merging three lots cost anything besides paperwork?"*
- Is that the right question?

> Let the confusion grow. Say it out loud: *"Huh — 'bigger and more regular is always better' has a
> cost we haven't counted yet."* Do not rescue them.

**The trap to let them walk into:** most learners will assume that because Option B's buildable
percentage (80%) is clearly higher than Option A's (67.6%), Option B is simply the better plan, full
stop — treating the buildable-footprint comparison (D2/D3) as if it were the final answer instead of
one input into D4. The real trap is that D4's dwelling-unit-YEARS metric also depends on *when* the
units arrive, not just how many there eventually are — and a learner who stops at "B has more square
footage" without running the lead-time and horizon arithmetic will miss that the two options are
genuinely close, and could even reach the wrong winner if the horizon were shorter than they assumed.

## Anchor 3 — What is the process?

- What's the process we'll go through to answer it?
- If we calculate buildable footprint for each option, are we done? Is that the same question as
  "how much housing does each option actually deliver by some real deadline"?
- If we end up with two numbers like 928 and 983 unit-years, how do we decide that's close enough to
  be a real discussion, versus one option just winning? What's our tiebreaker *before* we see the
  numbers?
- Is our question still the right question?

## Anchor 4 — What don't we know?

- What's missing that we'd need to answer this properly?
- Appendix F gives you the assumptions behind the lead times and the planning horizon. Do you
  believe them? **Have them actually try a longer and a shorter horizon and see how much the
  comparison moves.**
- What are we assuming stays fixed about the city's own housing deadline between now and when either
  option finishes construction? (This is the case's built-in opening for the twist — don't tip it.)

---

## Data Deep Dive

Now the numbers. Work these on the board with them.

**Step 1 — classify the parcels and find L1's missing angle (D1).** L1 (pentagon, convex): 90 +
90 + 141.3 + 128.7 + ? = 540° (pentagon interior angle sum, (5−2)×180). Missing angle = **90°**. L2
is the concave parcel — two of its six interior angles are reflex (greater than 180°): 192.5° and
218.7°, at the two corners where the diagonal cut notches inward.

**Step 2 — buildable footprint, Option A (D2).**

| Parcel | Area | Rear/notch length | Required yard (× 30 ft) | Buildable |
|---|---|---|---|---|
| L1 | 11,000 | 40 ft | 1,200 | 9,800 |
| L2 (concave) | 7,900 | 204 ft (80+60+64) | 6,120 | 1,780 |
| L3 | 11,100 | 80 ft | 2,400 | 8,700 |
| **Total** | **30,000** | | **9,720** | **20,280 (67.6%)** |

**Push the room directly:** *"L2 is less than 27% of the total land area, but it loses over 63% of
its own area to the required yard. Why does the concave shape cost it so much more?"* (Answer: its
notch creates two extra lot lines that this case's rule also treats as requiring the yard — the more
edges a shape's boundary has facing away from the street, the more of it a fixed-depth yard eats
into.)

**Step 3 — buildable footprint, Option B, and the plaza (D3).** Consolidated lot: 30,000 − (200 ×
30) = 30,000 − 6,000 = **24,000 sq ft (80%)**. Octagon plaza: perimeter = 8 × 30 = 240 ft; area =
½ × 240 × 36.2 = **4,344 sq ft**, well clear of the real 2,000 sq ft minimum.

**Step 4 — dwelling units and unit-years (D4).**

- Units A = 20,280 × 3.44 ÷ 714 ≈ **97.7**
- Units B = 24,000 × 3.44 ÷ 714 ≈ **115.6**
- Unit-years A = 97.7 × (120 − 6) / 12 ≈ **928.2**
- Unit-years B = 115.6 × (120 − 18) / 12 ≈ **982.9**

**Replat & Consolidate wins by 5.89%** — comfortably inside the 20% balance cap, but not by much.

---

## Twist — drop this at ~15 minutes into the discussion

Deliver it slowly. Let each piece land.

> *"The mayor's office just announced it."*
>
> (pause)
>
> *"The city's housing plan isn't a ten-year horizon anymore. It's five."*
>
> (pause)
>
> *"Every unit that doesn't exist yet in five years doesn't count toward the target — no matter how
> good the design is."*
>
> (pause)
>
> *"And it applies to every project that hasn't broken ground yet — including one already mid-filing
> on the old timeline. There's no grandfathering for a zoning lot merger already in progress, and no
> partial credit for time already spent on it either — every option's own lead time still counts in
> full, measured from today, regardless of how far along it already was."*

Those last two lines are deliberate, not filler — they close off two real objections a sharp Hero
will otherwise raise, in order. First: in actual zoning practice, a project already filed before a
deadline change is sometimes exempted (a "vested rights" argument) — say "no grandfathering" so
nobody argues Option B's already-underway merger buys it an exemption from the shortened horizon.
Second, and easier to miss: even once a Hero accepts the deadline applies to Option B, "already
mid-filing" invites a natural but wrong follow-up — that if the merger is already halfway done, only
the *remaining* lead time (not the full 18 months) should count against the new, shorter clock. It
should not: `sensitivity_model.py`'s `evaluate_twist()` still charges B's full stated `lead_B` (18
months) against the shortened horizon, with no credit for partial progress. Say the "no partial
credit" line explicitly, or a room that runs the math with a discounted lead time will reach a
different (wrong, per this case's own numbers) unit-years total for B and may not see the winner
flip at all.

**Facilitator only — read before you drop this, do not read aloud.** `horizon` drops from 120 to 60
months. Unit-years A = 97.7 × (60−6)/12 ≈ **439.7**. Unit-years B = 115.6 × (60−18)/12 ≈ **404.7**.
**The winner flips to Plat As-Is, by 8.64%.** Confirm a room that gets there against these numbers,
not just the logic — B's extra 18 units no longer have enough years left in the shorter window to
outweigh its 12-month head start disadvantage.

Now: **"Sixty seconds. Are you changing your recommendation — or not?"**

## Immediate recommit

- Who is **not** changing? Why?
- Who is reconsidering, even if they're not flipping?
- **What just broke in your original model?**
- **Were you wrong — or were you just missing information?** (Sit on this one.)
- Who built their case entirely on "80% beats 67.6%" without ever running D4's timeline arithmetic?

---

## Deep conflict — threads (20–30 min)

**Thread 1 — Efficiency vs. speed.** Option B is the better shape on paper; Option A is faster to
start. *"If Option B is simply the more efficient design, why does it ever lose?"* Push toward: a
better design that arrives too late doesn't out-produce a worse design that's already running,
within a bounded window — efficiency and speed are genuinely different currencies, and the horizon
length is the exchange rate between them.

**Thread 2 — Fragility to a single number.** All three timeline dials (Appendix F, MA3–MA4) are
disclosed assumptions with no real public source behind them. Flex `lead_B` or `horizon` by 50% in
either direction, and the winner flips (see case.json's sensitivity_disclosure — do not read this
section aloud, but use it to steer questions). *"Which option would you put your name on if the
mayor's office changed the deadline again next year?"*

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. *"Thirty seconds — as-is, or consolidate?"* Two or three learners, fast. Stand/sit vote, no explanation yet. |
| **3:00–10:00** | Position defense (pre-twist). *"Convince us it's better, not just bigger-sounding."* · *"What's your actual dwelling-unit-years number — not a guess."* |
| **10:00–15:00** | Pressure-test the models. *"Which option is more fragile to one wrong timeline estimate?"* · *"What single number does your option depend on most?"* |
| **15:00** | **DROP THE TWIST.** Slowly, with pauses. Finish with: *"Sixty seconds. Are you changing your recommendation — or not?"* |
| **15:00–20:00** | Immediate recommit. Who reverses? *"What just broke?"* |
| **20:00–30:00** | The two threads: efficiency vs. speed · fragility to a single assumption. |
| **30:00–45:00** | Close, re-vote, reflection, lessons learned. |

---

## Close

- **Vote again.** Compare to the Anchor 1 board. Who moved?
- We asked ______ as our key question. Was it the right one?
- What math was new to you here, and how did you attack it?
- If you got a case like this again, what would you check first?

## Lessons Learned

The arithmetic has a clean structure: a fixed-depth required yard eats into an irregular, especially
concave, shape's area far more than it does a compact regular one, but "more buildable footprint"
and "more housing delivered by a real deadline" are not automatically the same question once a
process delay enters the picture. Replat & Consolidate's win (5.89%) is real on the city's stated
10-year horizon, and it is also fragile — two of the three underlying timeline assumptions flip the
winner at a plausible ±50% swing, and a realistic policy change (a shortened housing deadline) is
enough to flip it for real. That is a **disclosed, not eliminated** sensitivity —
`case.json.sensitivity_disclosure[]` carries a Category-F entry for every timeline dial, because none
of them can be tightened by more research; they are genuine planning unknowns no public source
measures for a specific hypothetical project.

A facilitator running this room should say plainly what the case says: Replat & Consolidate wins on
the numbers as modeled, that win is real, and it is also genuinely fragile to several disclosed
assumptions and to a realistic policy shift — both things are true at once, and naming both is
stronger than picking one.

---

## Standards Touched On

**Polygon · Irregular Polygon · Convex · Concave · Regular Polygon · Octagon · Area · Perimeter ·
Ratio · Proportion · Population · Sum of the interior angles of a polygon theorem · How to find the
measure of an interior angle of a polygon given the other angles · How to find the area of a regular
polygon · How to find the percent of a number.**

See `LEARNING_GOALS.md` for the forces-test and `case.json.reinforcement_note` for why
`new_coverage[]` is honestly empty (the live spine had zero true zero-coverage skills remaining at
write time; every claimed skill here is nonetheless genuinely thin, n between 2 and 11, except two
reinforcing high-n skills).

---

## Facilitator note — sensitivity

No SPEC Section 6 subject-matter sensitivity applies. This is a zoning/housing-capacity planning
decision with no death, illness, or family-hardship stakes.
