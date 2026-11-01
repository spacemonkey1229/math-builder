# Facilitator Guide — Grade Rule

**Sensitivity flag:** none. This is a workplace production/quality decision about garment manufacturing, no personal, medical, or family stakes (SPEC §6 does not apply).

---

## The balance

**Argument for A (Uniform Dilation).** Dollars per fully-fitting size: **$1.3022** (3 of 5 sizes fit within the stated ±0.5in tolerance) versus Option B's **$1.4424** (5 of 5 sizes fit, but at nearly double the labor cost) — a **10.77%** edge for A. The three sizes nearest the base (10, 12, 14) — typically the highest-volume sizes in a real run — fit within tolerance at a meaningfully lower labor cost; only the two extreme sizes (8, 16) miss.

**Argument for B (Point-Specific Grading).** B is the only option that reliably fits every size in the run, with zero risk of shipping a size out of tolerance. A's 10.77% edge depends on accepting that 40% of the run (2 of 5 sizes) measurably misfits at at least one landmark — and the landmark that misses worst and most often is the **waist**, exactly the measurement customers notice first when a garment doesn't fit right. Devon's name is on the tech pack, not just a spreadsheet.

**The margin:** 10.77%, computed as `100 × (cost_per_fit_B − cost_per_fit_A) / cost_per_fit_A` from `case.json`'s `balance.margin_basis`. Well inside SPEC §2's 20% cap.

## The trap

**The trap: assuming "one scale factor" means "the pattern is a perfect dilation of every size."** A Hero who computes D2's shared scale factor and applies it (D3) may assume that because a dilation is *mathematically* a similar figure by definition, the graded pattern *must* fit every size — conflating "this is a valid dilation" with "this dilation matches reality." The trap breaks in D4: the dilated prediction is only *congruent-by-tolerance* with the real body at 3 of 5 sizes, because real bodies do not scale uniformly (the waist grows disproportionately faster than the bust across this run — a real, sourced fact from Appendix A, not an invented detail).

**The mechanical version of the same trap, and the one most likely to actually happen:** D2's scale factor is anchored on the base size and the largest/smallest sizes, so it reproduces the run's *endpoints* almost exactly — a hurried Hero checks bust at size 8 and size 16, sees it's close, and declares Uniform Dilation validated without ever running D4's full point-by-point check on the *middle* sizes or the *other two landmarks* (waist and hip). That is backwards: the endpoints matching is closest to guaranteed by construction; the real test is whether the middle sizes and the non-bust landmarks — where growth rates diverge most — hold up, and bust is consistently the landmark most likely to stay in tolerance while waist is not.

**The quieter, second version:** a Hero who sees Uniform Dilation "win" the primary metric may stop checking *which* sizes fail — the two sizes that fail are the run's two extremes, which a real business would likely care about disproportionately (they're often the sizes with the thinnest margin for error, since they're already harder to fit off the rack).

## Five Socratic questions

1. Uniform Dilation applies one scale factor everywhere. Is the resulting pattern still mathematically "similar" to the base pattern? Is it still a good match to the real body at every size? Are those the same question?
2. Your fit-check table says size 16 fails under Uniform Dilation because of the waist, not the bust or hip. Why would one landmark fail when the others pass, if they're all being scaled by the exact same factor?
3. Uniform Dilation wins by 10.77% today. If the factory's fit tolerance tightened to ±0.42in tomorrow, would it still win? Show the new fit-check table, not just a guess.
4. MA2 sets Point-Specific Grading's per-point time at exactly 3× Uniform Dilation's. What would have to be true on Devon's production floor for that ratio to be wrong — and which way would it move the answer if it were?
5. If Devon's company only sells sizes 10–14 this season (the three sizes Uniform Dilation actually fits), does this decision even matter? What does that tell you about when this case's answer changes and when it doesn't?

---

## Intro

Frame the format for the room: this is a Socratic discussion, not a lecture. Name the opener — "Devon has to pick one grading method for the whole size run, and the factory starts cutting in three hours" — and remind Heroes that today's job is to defend a stance with numbers, not just an instinct about which method "sounds" more accurate.

## Launch

Read the Overview's last two paragraphs aloud, stopping exactly where the case stops: Devon uncapping a red pen, the size chart pulled close.

## Anchor 1

**TAKE A STAND AND VOTE. No reasoning yet, just commit.** "Is anyone courageous enough to stand with Uniform Dilation? With Point-Specific Grading?" Count hands or have the room physically stand/sit. No justification allowed yet.

## Anchor 2

**WHAT IS THE PROBLEM WE'RE SOLVING?** "Is 'which method costs less labor' the right question, or is it 'which method actually fits'?" "What do you mean by 'fits' — every size, most sizes, or just the sizes that sell the most?" Let confusion grow on purpose: "Wow, a method that's mathematically clean and still might not fit — that's a harder question than it looked."

## Anchor 3

**WHAT IS THE PROCESS?** "If we find the real scale factor at every landmark, and compare it against one shared factor, how exactly do we decide?" Re-ask Anchor 2's question once the room has a process in hand: "Now that we know how we'd decide — is our question still the right one?"

## Anchor 4

**WHAT DON'T WE KNOW?** "Do we need to assume anything to answer this?" Steer toward Appendix D: the fit tolerance (MA1) and the per-point grading time (MA2) are both stated assumptions, not measured facts. "Which of these, if wrong, would worry you the most?" — the room should converge on MA1 before Data Deep Dive if the discussion is working.

## Data Deep Dive

Now, and only now, work the numbers as a room: the real per-landmark scale factors (D1), the single shared factor (D2), the dilated predictions (D3), the fit check (D4), and the final labor-cost-per-fit comparison (D5). Watch for the trap (above) — someone will assume "it's a valid dilation" means "it fits."

## Twist

At roughly the 15-minute mark: **the factory's incoming QC inspector announces the actual enforced fit tolerance is tighter than planned — ±0.42in, not ±0.5in** — a real, disclosed change to Appendix B's tolerance, not a hypothetical. Deliver it slowly: the inspection note, the new tolerance, nothing else.

Recompute at ±0.42in (everything else unchanged; full arithmetic in `case.json.balance.twist_effect` and cross-checked by `sensitivity_model.py`'s `evaluate_twist()`):
- Uniform Dilation now fits only **2 of 5 sizes** (down from 3) — size 12 (the base, exact) and size 14 (whose waist miss of 0.407in is just inside the new 0.42in line)
- Uniform Dilation's cost-per-fit rises to **$1.9533** (up from $1.3022)
- Point-Specific Grading is unchanged: **$1.4424**, still 5 of 5

**The winner flips to B, by a 35.4% margin.** Push: "size 14 just barely survives the new tolerance — 0.407in against a 0.42in line. What would you tell your boss if the inspector's next memo tightened it to ±0.4in instead?" (At exactly ±0.4in, size 14 also fails, dropping Uniform Dilation to 1 of 5 fitting sizes.)

**"Sixty seconds. Does your recommendation change?"** — most Heroes who backed A should reverse; press them on whether they would have backed A as confidently at the start if they'd known how close size 14 was cutting it.

## Close

**VOTE AGAIN.** "Did we ask the right question at the start? What math was new to you today, and how did you attack it?"

## Lessons Learned

A dilation is mathematically clean by definition — every point scales by the same factor, and the result is provably similar to the original. That mathematical cleanliness says nothing about whether it matches a real, non-uniformly-changing body. The case's real lesson is that "this is a valid transformation" and "this transformation is a good model of reality" are two different claims, and a method can be right about the first and wrong about the second.

## Standards Touched On

Dilation; scale factor; how to dilate a figure on the coordinate plane given a scale factor; how to find the scale factor of a dilation; similar; congruent; how to convert an amount from one unit to another unit.

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch: "Uniform, or point-specific — thirty seconds, no explanation, stand if Uniform, sit if Point-Specific." |
| 3:00–10:00 | Position defense: "Convince us why it's *better*, not just cheaper." Watch for the "valid dilation = good fit" trap (see above). |
| 10:00–15:00 | Pressure-test: "Whose plan is most fragile? What single number, if it moved, would break your position?" |
| 15:00 | **DROP THE TWIST** — the tighter ±0.42in QC tolerance. Deliver it slowly: the inspection note, the new tolerance, nothing else. |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke in your model — or did anything?" |
| 20:00–30:00 | Threaded deep conflict, two threads: (1) mathematical validity vs. real-world accuracy — is "this is a real dilation" ever a good enough answer on its own; (2) assumption ownership — MA2's 3:1 labor-time ratio is the case's real soft spot; whose job is it to verify a number like that before shipping a grade rule to a factory? |
| 30:00–45:00 | Close, re-vote, reflection: "What math was new to you, and how did you attack it? Was our original question — 'which method costs less labor' — still the right question, or should it have been 'which method actually fits'?" |

---

## Cohort bands

See `case.json.cohort_bands[]` for the machine-readable record. Summary:

- **Full (12–20):** run the plan above as written; both 20:00–30:00 threads run.
- **Compressed (6–11):** Anchors 2–3 combine into one pass; run only the sharper of the two threads; total runtime shortens proportionally.
- **1:1/pair (1–2):** no vote at Anchor 1 — the learner states an initial position instead; guide plays devil's advocate directly; twist still lands, "who reverses" becomes "would you reverse, and why."

## Sensitivity note

The base 10.77% margin is genuinely fragile — `sensitivity_model.py`'s ±50% sweep (run 2026-09-18) flips the winner under all four stated assumptions in at least one direction: tolerance (MA1) flips at −50% (170.83% to B) and cap-breaches at +50% (47.69%, still A); setup time flips at +50% (7.64% to B) and cap-breaches at −50% (37.14%, still A); Uniform Dilation's per-point time flips at +50% (18.06% to B) and cap-breaches at −50% (60.00%, still A); Point-Specific's per-point time flips at −50% (80.56% to B) and cap-breaches at +50% (66.15%, still A). **All of this is disclosed, not hidden** — see `case.json.sensitivity_disclosure[]`, and treat the base 10.77% margin as exactly as close as it looks: nearly every dial in this case can move the recommendation. The tolerance-tightening twist above is the one instability the case actually drops on the room live, but a sharp Hero should recognize the case's whole foundation is this thin before the twist ever lands.
