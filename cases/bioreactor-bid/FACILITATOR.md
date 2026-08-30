# Guide Notes: The Bioreactor Bid

**Case:** The Bioreactor Bid · **Tier:** T2 · **Band:** MS-core · **Studio:** MS Adventure
**Standards:** Volume of Revolution (Disk Method) / Area Between Two Curves — see `case.json.standards[]`
for the exact ids; `calculus-volume-of-revolution` and
`calculus-how-to-find-the-volume-of-a-solid-of-revolution-using-the-disk-method` are new coverage.

**Facilitator-only. Do not distribute to students.** Balance argument, margin, and the wrong-path
analysis below live here and in `case.json`'s `balance` object — never in `case.md`.

**Read this before you facilitate.** The primary graded metric is liters of viable product
yielded per dollar of total vessel cost. On that ratio, the two options sit close — a `margin_pct`
of **12.4%**, well inside the SPEC §2 ~20% cap: the Wave Bid actually posts the *better*
yield-per-dollar ratio (~0.00096 L/$ vs. the Column Bid's ~0.00086 L/$), driven entirely by its
much lower total cost ($18,000 vs. $43,864) — both vessels share the exact same net-cumulative-yield
curve (Appendix A applies per liter of working volume identically to either vessel, MA6), so this is
a cost story, not a mixing/yield-per-liter story. The real dilemma is that the Wave Bid's working
volume (17.29 L, from the disk-method integral of its bag profile) falls short of the client's 25 L
contractual minimum yield [MA4] — a hard constraint that disqualifies it outright, no matter how
good its ratio looks. The Column Bid's 37.5 L working volume clears that floor with room to spare,
making it the only vessel that satisfies all three hard limits (yield floor, fill level, budget) at
once. The Socratic discussion below is built so the room's real tension is a genuinely close ratio
race *against* a hard disqualifying constraint that most Heroes will not check until forced to.

## Intro

Frame the format before anything else: this is a real capital-purchase recommendation with a
client deadline today, not a worksheet. Name the opener — "You are Wei Zhang, a bioprocess
engineer with two vendor folders on the bench and a text message from your manager: procurement
needs your number by end of day." Let the stakes land before moving to the Launch.

## Launch

Show the two vendor spec sheets side by side — the Column Bid's simple cylinder dimensions, and
the Wave Bid's curved bag cross-section with the note "requires a disk-method integral." Ask:
"Which one do you think wins on raw output per dollar, before anyone does any math?" Do not
confirm or correct answers here. Most rooms will assume the vessel with the qualitative "better
mixing" claim (Wave) must also win the numbers by more than it actually does, or that the vessel
with the bigger nominal capacity number must be the safer choice — both instincts are worth
recording out loud before anyone touches a calculator.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Wei on the Wave Bid — the one with the flashier mixing
story and the integral?" Show of hands, both options, no discussion. Record the count — Close will
ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'wins'?"**

Let confusion grow here — this is deliberate. Heroes will want to jump straight to "which vessel
produces more product," but push on what the client actually asked for: yield *per dollar*, not
raw yield, and not raw density. "If one vessel makes less product but costs way less, could it
still be the better recommendation? What would have to be true for that?" If the room lands on
"per-dollar efficiency and total output are different questions" on its own, the case is working
as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "which vessel makes more product" from "which vessel is the better
dollar-for-dollar bet," ask them to name the actual steps before touching the appendices: find the
net cumulative yield per liter of working volume from Appendix A's feed-rate and uptake-rate
curves (D1), find each vessel's actual usable working volume at its target fill level — cylinder
formula for the Column Bid, disk-method integral of the bag's cross-sectional profile for the Wave
Bid (D2) — multiply the two together for a total-yield figure per vessel (D3), and divide by each
vessel's total cost for the yield-per-dollar comparison (D4). Re-ask: "Is our question still the
right one, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gaps honestly: Appendix A's feed-rate/uptake-rate table and the g-to-liters
conversion factor (MA6) are stated assumptions shaped like real Monod-kinetics data, not a citation
to a specific published curve — no public dataset reports this cell line's rates in these units.
The Wave Bid's bag radius profile (MA7) is likewise an authored, physically plausible curve, not a
vendor measurement — bag geometry at this level of detail is proprietary. The client's 25 L minimum
yield (MA4) and the CRO's $50,000 budget cap (MA5) are also scenario choices, not sourced contract
terms. Ask which of these actually decides the recommendation if it moves. The honest answer:
MA6's absolute scale and MA7's profile are the two load-bearing ones — MA6 sets whether the yield
floor binds *at all*, and MA7 directly sets the Wave Bid's working volume, which is the number that
disqualifies it. MA4 and MA5 are the constraints being tested against those two, not decorative.
Let a sharp Hero find this themselves before confirming it.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's area-between-curves calculation (net yield ≈ 1.0 L of
viable product per liter of working volume — this number is *identical* for both vessels, since
Appendix A's curves are shared), D2's two working-volume figures (Column: 37.5 L by the cylinder
formula; Wave: 17.29 L by the disk-method integral), D3's total-yield table (Column: 37.5 L; Wave:
17.29 L), and D4's yield-per-dollar ratio (Column: ~$1,169 spent per liter; Wave: ~$1,041 spent per
liter — Wave is *more* efficient) together as a room. Cold-call specifically on D2 for the Wave
Bid — this is where a Hero who never runs the disk-method integral will substitute the bag's
nominal 50 L capacity and get a total-yield and yield-per-dollar figure for Option B that is
badly wrong, not just imprecise.

**Facilitator-only arithmetic note.** D1: sum of (feed − uptake) over days 0–5 (6, 6, 5, 4, 2, 0),
each pair of consecutive days averaged and multiplied by the 1-day step (the standard
connect-the-dots area-under-a-curve method) = 20 g/L, × the 0.05 L/g conversion factor [MA6] =
1.0 L viable product per liter of working volume, for either vessel. D2 Column: 50 L × 75% fill = 37.5 L (plain arithmetic, no
integral). D2 Wave: disk-method integral of Appendix C's r(h) profile from base to the target fill
height ≈ 17.29 L (the case's own MA7-sourced figure). D4: Column $43,864 / 37.5 L ≈ $1,169.71/L;
Wave $18,000 / 17.29 L ≈ $1,041.06/L. Inverted to the primary metric's own units (L per $): Column
≈ 0.0008551 L/$, Wave ≈ 0.0009606 L/$ — Wave leads by (0.0009606 − 0.0008551) / 0.0008551 ≈ 12.36%,
rounded to `margin_pct: 12.4` in `case.json`.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Wei runs the numbers and the ratio favors the Wave Bid. He's drafting the recommendation memo
when his director stops by his desk. 'Before you send that — remember the client's downstream
purification line. They told us flat out: anything under 25 liters from this run and their
schedule slips a week. That's not a preference. That's in the contract.'"

"Does that change what Wei should actually recommend?"

**Facilitator-only: what this actually does, and does not, change.** The 25 L minimum [MA4] was
always stated in the Background as a hard limit Wei's recommendation "has to clear... at once"
alongside fill level and budget — a careful first read should have caught it before Anchor 4 even
asked "what don't we know." The twist's real function is to force a *recheck*, not to reveal new
information: many rooms will have computed D4's ratio, seen Wave ahead by ~12%, and moved straight
to recommending it without ever comparing D3's 17.29 L figure against the 25 L floor stated on page
one. The twist does not erase the Wave Bid's real cost-efficiency advantage, and a Hero arguing
Argument B (MA4 is itself unsourced and possibly negotiable) is making a legitimate move — but the
case as written treats MA4 as binding, and a Hero who reverses their vote should be pressed on
*why* they missed it the first time, not just on the new vote.

## Immediate recommit

Re-vote immediately. Ask by name: "Does the 25 L floor change your vote — or does it just tell you
that your yield-per-dollar number was never the whole decision?" That distinction is the
transferable skill, not the vote itself.

## Deep conflict — three threads (20–30 min)

1. **A better ratio is not always a usable ratio.** D4's yield-per-dollar figure genuinely favors
   the Wave Bid — is that number simply void once a hard constraint disqualifies the option it
   describes, or does it still tell you something worth naming (e.g., what the Wave Bid *would* be
   worth if the client's minimum were smaller, or if a future run could combine two Wave batches)?
2. **Where mixing's claimed advantage actually lives — and doesn't.** The Background credits the
   Wave Bid's "superior mixing" with a higher achievable cell density, but Appendix A's feed/uptake
   curves are shared and identical for both vessels (MA6's own sensitivity note says this
   explicitly). Why does a qualitative claim in the story not automatically become a quantitative
   advantage in the math — and what would it take to actually wire "better mixing" into the graded
   numbers?
3. **Is MA4 a wall or a lever?** The 25 L minimum is a stated modeling assumption, not a sourced
   figure — is it fair to argue it should flex (e.g., across multiple runs, or via renegotiation),
   or does treating a stated hard constraint as negotiable undermine the whole point of having
   constraints in a case like this?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both spec sheets, cold-call for a gut read, no formulas yet |
| 3:00–10:00 | Position defense — *"Convince us your vessel is the one Wei should send up the chain, not just the one with the better pitch"* |
| 10:00–15:00 | Pressure-test the models — *"Whose recommendation is most fragile if one number moves?"* |
| **15:00** | **DROP THE TWIST** — the director's reminder about the 25 L floor, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (a better ratio vs. a usable ratio; where mixing's advantage actually lives; is MA4 a wall or a lever) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

The plausible reasoning that produces a confident wrong answer: a Hero computes D1–D4 correctly,
sees the Wave Bid winning the yield-per-dollar ratio by a real (~12%) margin, and recommends it —
without ever checking that ratio against the client's stated 25 L minimum total yield in the
Background. A second, related trap: a Hero reads "superior mixing" in the Background and assumes
the Wave Bid must therefore have a *better* net-cumulative-yield curve in Appendix A, when the
table is explicitly shared and identical for both vessels — the mixing claim never enters the
graded math at all. Both traps look like careful work right up until the numbers meet the
constraint list.

## Socratic questions

1. Your yield-per-dollar table gives the Wave Bid the edge — what would its validation cost have to rise to for that ranking to flip in the Column Bid's favor?
2. You integrated the bag's radius profile to get the Wave Bid's working volume instead of using its nominal capacity — how many liters did that integral cost you compared to just using the sticker number, and why does that gap matter to your final recommendation?
3. The client's minimum required total yield rules the Wave Bid out entirely — does its yield-per-dollar number even matter anymore, and what does that tell you about the order in which you should check a set of hard constraints?
4. Your net-cumulative-yield figure came from the area between two curves that are identical for both vessels — so why does the Background credit the Wave Bid's "superior mixing" with a yield advantage at all? Where, if anywhere, would that claim actually need to show up in the math for it to matter?
5. Two teams could compute the same disk-method integral and land on different working volumes for the Wave Bid — what's the most likely place a small measurement or rounding choice in Appendix C would change whether it clears the 25 L floor?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that voted for
the Wave Bid at Anchor 1 purely on "it sounds more advanced" and moves to the Column Bid after the
twist for a *different, constraint-based* reason has genuinely learned something, even if the vote
count looks similar.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether the room checked the 25 L floor against D3 before the twist, or whether it took the
  director's line to surface it — this is the single most useful signal for whether Anchor 3's
  "name the steps first" framing is doing its job.
- Whether Anchor 4's finding — that the Background's "superior mixing" claim never actually enters
  the graded D1 calculation — landed as a discovery or had to be told outright.
- Whether the "is MA4 a wall or a lever" thread produced genuine disagreement or converged
  immediately; if it converges immediately, the twist may need a sharper edge in a future revision.

## Standards Touched On

Volume of Revolution · How To Find The Volume Of A Solid Of Revolution Using The Disk Method ·
Area Between Two Curves · How To Find The Area Between Two Curves

## Facilitator note — sensitivity (SPEC §6)

NONE. This case does not touch illness, death, financial hardship, or family stress — it is a
production-engineering capital-purchase decision. No sensitivity flag applies;
`case.json.sensitivity_note` is `null` for the same reason.
