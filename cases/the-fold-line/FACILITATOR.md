# Facilitator Guide — The Fold Line

**Sensitivity flag:** none. This is a shop-cost decision with no personal, medical, or family stakes (SPEC §6 does not apply).

---

## The balance

**Argument for A (The Fold Cut).** Total dollars per panel: **$0.9187** vs. Option B's **$1.0758** — a **17.1%** gap, Fold Cut wins. The labor-time gap (0.8 min vs. 1.6 min per panel, at $17.61/hr) is worth more in dollars than the fabric-efficiency gap (78% vs. 88% marker efficiency) at this fabric's $3.70/yd price. Scaled to the shop's 300-panel day: **$275.61** (Fold) vs. **$322.74** (Open) — about **$47/day**.

**Argument for B (The Open Cut).** The Open Cut uses meaningfully less fabric per panel — 0.1638 yd vs. 0.1848 yd, about 11% less — because the two mirror pieces are free to nest tightly instead of being locked to a fold. At a higher fabric price, or with a faster second tracing pass, that fabric saving can close the labor gap or overtake it. Priya's shop pays a real, live market wage; it does not (yet) know what next season's fabric will cost.

**The margin:** 17.1%, computed as `100 × (Total_B − Total_A) / Total_A` from the formula in `case.json`'s `balance.margin_basis`. Well inside SPEC §2's 20% cap, and close enough that a Hero arguing either side has real numbers to stand on.

## The trap

**The trap: comparing raw fabric yardage instead of total dollars.** A Hero who stops at "Open Cut uses less fabric, so it must be cheaper" has fallen into exactly the reasoning the case is built to test — the Open Cut *is* more fabric-efficient, full stop, and a Hero who only reads Appendix D will walk away confident in Option B. The trap only breaks once labor is priced in: doubling the cutting time (MA2) costs more, in this shop, than the fabric it saves. The second, quieter version of the same trap is treating the 5/8-inch seam allowance (S1) as if it differs between methods — it doesn't; it's identical overhead on both, and a Hero who "finds" a difference there has made an arithmetic error, not a real finding.

## Five Socratic questions

1. Your worksheet says the Open Cut wastes less fabric. So why does it cost more per panel — what number are you leaving out?
2. Fold Cut wins by 17.1% today. If tomorrow's fabric price doubled to $7.40/yd and nothing else changed, would the Fold Cut still win? Show the arithmetic, not just a guess.
3. MA2 fixes the Open Cut's time at exactly double the Fold Cut's. What would have to be true on Priya's floor for that ratio to be wrong — and which way would it move the answer if it were?
4. Appendix D gives two efficiency numbers from two different published ranges. If the real Fold Cut efficiency for *this exact panel* sat at the *bottom* of its cited range (75%) instead of 78%, does the recommendation change? (It does not — Fold Cut still wins, by about 13.7%. What would the efficiency have to fall to before it did?)
5. Priya's decision applies to every panel, every day, forever, once she makes it. What would have to change on the shop floor — not in the numbers, on the floor — for her to want to revisit it in six months?

---

## Intro

Frame the format for the room: this is a Socratic discussion, not a lecture. Name the opener — "Priya has to pick one cutting method for every panel her shop cuts, forever, starting tomorrow" — and remind Heroes that today's job is to defend a stance with numbers, not just an instinct.

## Launch

Show the two folders from the case's Overview — one imaginary folder labeled FOLD CUT, one labeled OPEN CUT — or read the Overview's last paragraph aloud, stopping exactly where the case stops: Priya picking up the phone.

## Anchor 1

**TAKE A STAND AND VOTE. No reasoning yet, just commit.** "Is anyone courageous enough to stand with the Fold Cut? With the Open Cut?" Count hands or have the room physically stand/sit. No justification allowed yet.

## Anchor 2

**WHAT IS THE PROBLEM WE'RE SOLVING?** "Is 'which method costs less' the right question, or is it 'which method is less risky'?" "What do you mean by 'costs less' — per panel, per day, this month, or over a year?" Let confusion grow here on purpose: "Wow, this is a harder question than it looked."

## Anchor 3

**WHAT IS THE PROCESS?** "If we find fabric cost and labor cost for both methods, how exactly do we decide?" Re-ask Anchor 2's question once the room has a process in hand: "Now that we know how we'd decide — is our question still the right one?"

## Anchor 4

**WHAT DON'T WE KNOW?** "Do we need to assume anything to answer this?" Steer toward Appendix E: the panel's exact dimensions (MA1), the per-panel cutting time (MA2), and the exact marker-efficiency point-values (MA3) are all stated assumptions, not measured facts. "Which of these, if wrong, would worry you the most?" — the room should converge on MA2 before Data Deep Dive if the discussion is working.

## Data Deep Dive

Now, and only now, work the numbers as a room: fabric cost per panel, labor cost per panel, total per panel, and the daily projection. This is where D1–D5 get compared out loud. Watch for the trap (above) — someone will announce a winner off Appendix D alone before labor is added in.

## Twist

At roughly the 15-minute mark: **the fabric mill notifies the shop that its price for this broadcloth is rising from $3.70/yd to $6.50/yd next month, effective on the very next fabric order** — a real, disclosed change to Appendix B's price, not a hypothetical. Deliver it slowly: the mill notice, the new price, nothing else.

Recompute at $6.50/yd (efficiencies, wage, and labor time unchanged; full arithmetic and the twist's own derived figures are recorded in `case.json.derived_twist` and cross-checked by `sensitivity_model.py`'s `evaluate_twist()`):
- Total, Fold Cut: **$1.4363/panel**
- Total, Open Cut: **$1.5345/panel**
- New margin: **≈6.8%**, Fold Cut (A) still wins.

**The twist does not flip the winner — it collapses the margin from 17.1% to about 6.8%.** This is deliberately the harder twist to run well: ask directly, "did anything just break in your model, or not?" A Hero who only checked *whether* the recommendation changes will say no and move on; the sharper answer is that the case got much closer, and a Hero confident at 17.1% should be far less confident at 6.8%. Push: "at what fabric price would this actually flip?" Setting Total_A(p) = Total_B(p) gives a breakeven price of about **$11.18/yd** (see `case.json.derived_twist.breakeven_price_per_yd`) — below that, Fold Cut wins; above it, Open Cut wins.

**"Sixty seconds. Does your recommendation change?"** — most Heroes will say no (correctly) but should be pressed on *how close* it now is, and whether they would still stake the shop's margin on it as confidently as before.

## Close

**VOTE AGAIN.** "Did we ask the right question at the start? What math was new to you today, and how did you attack it?"

## Lessons Learned

A margin can survive a twist and still be a different case afterward — "the recommendation didn't change" and "nothing changed" are not the same sentence. The labor-time assumption (MA2) mattered more than either efficiency assumption; a Hero who spent all their effort double-checking Appendix D's percentages and none checking MA2 checked the less decisive number.

## Standards Touched On

Reflection across the y-axis; line of symmetry; symmetry; congruent; adding mixed numbers; multiplying a fraction and a mixed number; converting an amount from one unit to another; distance.

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch: "Fold, or open — thirty seconds, no explanation, stand if Fold, sit if Open." |
| 3:00–10:00 | Position defense: "Convince us why it's *better*, not just fair." Watch for the fabric-only trap (see above). |
| 10:00–15:00 | Pressure-test: "Whose plan is most fragile? What single number, if it moved, would break your position?" |
| 15:00 | **DROP THE TWIST** — the fabric-price increase to $6.50/yd. Deliver it slowly: the mill notice, the new price, nothing else. |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke in your model — or did anything?" |
| 20:00–30:00 | Threaded deep conflict, two threads: (1) labor-time-vs-fabric-efficiency framing — which cost driver should a cutting-room lead trust more, a fixed wage or a volatile commodity price; (2) assumption ownership — MA2's 2:1 labor-time ratio is the case's real soft spot; whose job is it to verify a number like that before betting a shop's margin on it? |
| 30:00–45:00 | Close, re-vote, reflection: "What math was new to you, and how did you attack it? Was our original question — 'which method costs less' — still the right question, or should it have been 'which method is less risky'?" |

---

## Cohort bands

See `case.json.cohort_bands[]` for the machine-readable record. Summary:

- **Full (14–20):** run the plan above as written; both 20:00–30:00 threads run.
- **Compressed (7–10):** Anchors 2–3 combine into one pass; run only the labor-vs-fabric thread; total runtime ~30 minutes.
- **1:1/pair (1–2):** no vote at Anchor 1 — each Hero states an initial position instead; guide plays devil's advocate directly; twist still lands, "who reverses" becomes "would you reverse, and why."

## Sensitivity note

Within either efficiency assumption's cited real range (Fold Cut 75–82%, Open Cut 82–90%), the 17.1% base margin narrows or widens but never flips — Fold Cut wins even at the least favorable realistic point in either range. The verdict only flips under `sensitivity_model.py`'s synthetic ±50% mechanical stress test, which pushes an efficiency value far outside any cited real range (see `case.json.sensitivity_disclosure[]`). MA2 (the labor-time ratio) changes the margin's size substantially but never flips the winner within ±50% either. **The single most dilemma-relevant real-world risk is the fabric-price twist** (see Twist, above) — a real, plausible market move, unlike the synthetic efficiency stress test.
