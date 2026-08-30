# Guide Notes: Fret Board

**Case:** Fret Board · **Tier:** T2 · **Band:** MS-core · **Studio:** MS Adventure
**Standards:** Basic Operations (Factoring) / Advanced Operations (Exponents) / Measurement
(Ratios) / Number Sense (Comparisons) — see `case.json.standards[]` for the exact ids; this is a
domain-opening case for `music-acoustics`, not a new-skill-coverage case (see
`case.json.reinforcement_note`).

Researched 2026-08-24 (`RESEARCH_LOG.md`, all placeholders resolved). **Retuned 2026-08-27** —
read this before you facilitate. The case's primary graded metric is now **total shop time, in
minutes, to calculate/mark/cut all 22 frets** (Appendix F), not raw cents-of-deviation. On total
shop time, Option A (Precision Method) and Option B (Rule of Eighteen) sit close — a `margin_pct`
of **4.2%**, well inside the SPEC §2 ~20% cap — because the shared, method-independent time to
cut, install, and dress the frets (MA6, 45 minutes) dwarfs the small per-fret calculation-time gap
between the two methods (MA4/MA5). This replaced the original primary metric (cents of deviation
at fret 12), which the 2026-08-26 `case-readiness` run correctly flagged as structurally
unbalanceable at 100% margin: Option A is exact by construction at *every* fret, not just fret 12,
so no honest reframing within pure accuracy could ever produce a close race — see
`case.json.balance.margin_note` for the full history and the math showing why an earlier-fret
regrade specifically does not work. The ~12.5-cent / 150%-tolerance-overshoot accuracy gap for
Option B is still real, still sourced-derived, and still fully disclosed (Appendix D,
`case.json.derived.accuracy_cost_context`) — it is simply no longer what `margin_pct` is computed
from. The Socratic discussion below is built so the room's real tension is a genuinely close time
race (Option A vs. Option B) *against* a known, named, much larger accuracy cost for Option B —
not a coin-flip on accuracy, and not a landslide on time either.

**Corrected 2026-08-27 (Tier 2 probe P5): the 4.2% time margin is genuinely thin, not just
"close."** MA4/MA5 (the per-fret calculation-time estimates behind Appendix F) are stated Modeling
Assumptions, not measured facts — and a ~50% swing in either one flips which method wins on total
shop time: MA4 (Precision Method, 20s/fret) running about 10 seconds instead, or MA5 (Rule of
Eighteen, 14s/fret) running about 21 seconds instead, each flip the recommended-by-the-metric
winner from B to A. (MA6, the 45-minute shared baseline, does not flip it at either bound.) A
prior version of this guide's balance note claimed the margin was "robust" to MA4/MA5 because
doubling MA4 alone only pushed the margin to ~16% — that check was real but tested only the
*widening* direction; it never tested the narrowing direction a ±50% sensitivity sweep requires.
This is now disclosed, not eliminated, in `case.json.sensitivity_disclosure[]` and in `case.md`'s
Modeling Assumptions table. It is good material, not a flaw to hide: see the new sensitivity
thread in "Deep conflict" and Socratic question 6 below.

## Intro

Frame the format before anything else: this is a real shop decision with a client due back before
the week is out, not a worksheet. Name the opener — "You are an apprentice luthier with one
unsupervised fret job and a mentor who isn't here to check your work. Two sticky notes, two
methods, one saw." Let the stakes land before moving to the Launch.

## Launch

Show the two sticky notes from the Overview side by side — a column of four-decimal numbers under
"exact," and a short column of whole-number divisions under "shop method" — with no explanation of
which is which. Ask: "Which one do you think a working shop actually uses more often?" Do not
confirm or correct answers here. Most rooms will assume "exact" must be right because it says so —
that instinct is worth recording out loud before anyone touches a calculator.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Yuki on the Rule of Eighteen — the shortcut, not the
'exact' one?" Show of hands, both options, no discussion. Record the count — Close will ask them
to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'exact'?"**

Let confusion grow here — this is deliberate. Heroes will want to jump straight to "which method
is more accurate," but push on what "accurate enough" even means for a guitar: "A fret a
thousandth of an inch off — does anyone's ear notice that? What would actually have to be true for
it to matter?" If the room lands on "accuracy only matters relative to some tolerance a human can
hear, not in the abstract" on its own, the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "which number is bigger" from "which drift is audible," ask them to name
the actual steps before touching the appendices: build both fret-position tables (D1/D2), convert
the *difference* between them at fret 12 into cents (D3), reduce a few open-to-fretted length
ratios by their GCF to see which frets land on clean intervals (D4), and only then compare *both*
the total-shop-time figures in Appendix F and the cents figure against the stated tolerance and
the cost of being wrong (D5). Re-ask: "Is our question still the right one, now that we can see
the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gaps honestly: Appendix D's acceptable-intonation-tolerance figure (MA1, 5 cents)
has no single hard published trade standard behind it — it's a stated mid-point of a range guitar
techs and psychoacoustic research converge on. The fret count (MA2, 22) and the client's turnaround
(MA3, 5 days) are also scenario choices, not published standards. Ask which one actually changes
the *graded* D3 cents figure if it moves. The honest answer is **none of them** — the cents
figure is pure geometry from Appendix B/C's lengths; MA1 only decides *whether that number counts
as acceptable*, and MA2/MA3 don't enter the D1–D4 math at all. Let a sharp Hero find this
themselves before confirming it.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's exponent table, D2's ratio-shortcut table, D3's cents
conversion, and D4's GCF reduction together as a room, cold-calling for D3 specifically — this is
where a Hero who computed D1/D2 correctly but never ran the log-based cents formula will visibly
struggle to explain *why* two very close-looking decimal lengths represent a real, nameable pitch
gap. That struggle is useful information for the facilitator, not a moment to rescue.

**Facilitator-only arithmetic note.** Precision Method fret 12 lands at exactly 12.7500 in (half of
25.5000 in, by construction of the 2:1 octave ratio). Rule of Eighteen fret 12 lands at 12.6573 in.
Converting the *remaining* (bridge-side) length ratio (12.7500 : 12.8427) through
`cents = 3986.3 × log10(ratio)` gives ≈ −12.5 cents — the Rule of Eighteen sits flat of true pitch,
matching the qualitative "trends flat" finding in the sourced reference (Appendix G, [S3]). Frets
1–5's open:fretted ratios (Appendix E) reduce cleanly for none of them except the octave itself —
worth naming as its own small discovery: equal temperament makes every fret before the 12th an
irrational multiple of the open length, so a "nice" GCF reduction anywhere before the octave would
be a rounding coincidence, not a real property of the method.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Yuki takes her cents-of-deviation number to the shop's owner, ready to argue the Rule of Eighteen
is unacceptable. The owner listens, then says: 'You're marking frets. You're not the last hands on
this neck.' She pulls out the setup log from the last three guitars the shop shipped — every one
of them fretted with the Rule of Eighteen, every one of them passed a professional tuner check at
final setup, after the bridge saddle was compensated."

"Does that change what Yuki should actually recommend?"

**Facilitator-only: what this actually does, and does not, change.** Bridge-saddle compensation —
adjusting the length each string travels *past* the fretted point, done at final setup on every
instrument regardless of which fret-marking method was used — is a real, standard step in guitar
building that corrects for a range of systematic intonation errors, including some of the kind the
Rule of Eighteen introduces. This case does **not** have a sourced number for how many cents of
correction compensation buys back on this specific build — no source in Appendix G speaks to that,
and inventing one here would be exactly the fabrication SPEC §5 forbids. What the twist *does* is
real and nameable without a number: it shows Yuki's D3 figure, which is correct and load-bearing at
the fret-marking stage, is not the last word on whether the finished instrument plays in tune — a
different craftsperson, at a different stage, using a different tool, also has a say. **The twist
does not erase the ~12.5-cent finding or flip which method is more exact** — it reframes what that
finding is actually worth deciding, from "is Option B disqualified" to "is Option B's known,
named gap something the shop's own downstream process already absorbs, partially absorbs, or
doesn't touch at all." Do not hand a specific answer to that question — it is genuinely open given
what this case can honestly source, and that openness is the point.

## Immediate recommit

Re-vote immediately. Ask by name: "Does the setup log change your vote — or does it just tell you
that Yuki's number was never measuring the whole instrument's final intonation?" That distinction
is the transferable skill, not the vote itself.

## Deep conflict — three threads (20-30 min)

1. **A correct number is not always the last number.** D3's cents figure is real, sourced-adjacent
   arithmetic, and it is *not* the finished instrument's final intonation — bridge compensation
   happens after Yuki's job is done. Is that a flaw in what the case grades, or a real lesson about
   which stage of a process a given number actually describes?
2. **Close in inches, not close in cents.** Appendix B and C's fret-12 lengths differ by less than
   a tenth of an inch, yet the case forces a full logarithmic conversion before that gap means
   anything. Why does "the numbers looked close" fail as a stopping point here?
3. **What downstream compensation can and can't buy back.** The twist introduces a real shop
   practice with no sourced number attached to it in this case. Is a real, named, but unquantified
   mitigating factor enough to change a recommendation — or does "we don't know how much it helps"
   cut the other way, toward not relying on it?
4. **The time race is thinner than it looks.** MA4/MA5 (Appendix F's per-fret calculation-time
   estimates) are the case author's own scenario guesses, not measured facts — and Appendix G says
   so directly. If a Hero simply doubts one of those numbers by a plausible amount ("an exponent
   isn't THAT much slower to key in than a division"), the metric's winner can flip from B to A.
   Does a recommendation resting on a 4.2% margin built from two unmeasured guesses deserve the
   same confidence as one resting on a wide, stable gap — and if not, what should Yuki actually do
   with that uncertainty?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both sticky notes, cold-call for a gut read, no formulas yet |
| 3:00–10:00 | Position defense — *"Convince us your method is the one Yuki should trust, not just the one that sounds more careful"* |
| 10:00–15:00 | Pressure-test the models — *"Whose recommendation is most fragile to the tolerance line moving?"* |
| **15:00** | **DROP THE TWIST** — the shop's setup log, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (a correct number vs. the last number; close-in-inches vs. close-in-cents; what compensation can and can't buy back) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

The plausible wrong answer is treating "small rounding error" as automatically negligible because
the words "small" and "traditional" both sound reassuring. Heroes will be tempted to eyeball the
Rule of Eighteen's fret-position numbers, see they're close to the Precision Method's, and declare
B safe without ever computing the cents conversion in D3 — missing that cents is a logarithmic
(multiplicative) scale, not a linear one, so a length difference that looks tiny in inches can
still represent a musically nameable number of cents. The case forces D3 specifically so no one can
skip straight from "the numbers look close" to "the methods are equivalent."

## Socratic questions

1. Your D3 cents-of-deviation figure at fret 12 — is that number bigger or smaller than you expected before you calculated it, and what does that tell you about why the Rule of Eighteen survived as a real shop method for so long?
2. If the Rule of Eighteen's drift crosses the acceptable-tolerance line in Appendix D, does it cross it exactly at fret 12, or does your D1/D2 comparison suggest it might cross earlier or later — and why does the case's primary metric only ask about fret 12?
3. Your D4 table shows none of frets 1–5 reducing to a simple whole-number ratio, while fret 12 reduces exactly to 2:1. What does a "nice" ratio actually correspond to on the instrument, and why is the octave the one place equal temperament guarantees you'll find one?
4. Appendix F shows the two methods' total shop time is close, while Appendix D shows their accuracy gap is not. A week of unpaid rework is the cost of being wrong (Appendix F). Which of those two numbers should actually drive Yuki's recommendation — the one where the methods are close, or the one where they aren't — and why doesn't "close on time" settle the decision by itself?
5. The "Rule of Eighteen" is named for a whole number, but the source in Appendix G shows the more precise modern divisor luthiers sometimes use instead is 17.817154, not 18. Why would a trade keep using a rounded nickname for over a century instead of correcting the name to match the number some shops actually use?
6. MA4 and MA5 (Appendix F/G) are Yuki's own guesses at how many seconds each method takes to calculate one fret's position — nobody timed a real luthier doing this. If you think either guess is off by even 5-6 seconds in the right direction, the total-shop-time comparison can flip which method wins. Should a recommendation built on a margin that thin lean more heavily on the accuracy gap in Appendix D instead — and if so, how thin does a margin have to get before you stop trusting it as the deciding factor?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that voted for
B at Anchor 1 purely on "it's the traditional method" and stays with B after the twist for a
*different, numbers-and-process-based* reason has genuinely moved, even if the vote count looks
unchanged.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Anchor 4's "none of the Modeling Assumptions touch the graded D3 figure" finding landed
  as a discovery or had to be told outright.
- Whether the "close in inches, not close in cents" trap was the actual sticking point, or whether
  D4's GCF reduction was the harder gate for most Heroes.
- Whether the twist's unquantified compensation factor felt like an honest open question or felt
  like the case dodging a real answer — worth listening for directly.
- Whether the retuned primary metric (total shop time, Appendix F) read to Heroes as a fair,
  real-world framing of the dilemma, or as a distraction from the accuracy gap that actually
  matters most for a finished instrument — this is exactly the tension Socratic Q4 is built to
  surface, and it's worth checking whether the room found it on their own.

## Standards Touched On

Greatest Common Factor · Factor · Exponent (also Power) · Ratio

## Facilitator note — assumption sensitivity (Tier 2 probe P5)

**Corrected 2026-08-27.** The total-shop-time margin (4.2%, Appendix F) is NOT robust to a ±50%
swing in MA4 or MA5, the two per-fret calculation-time estimates that feed it directly — it flips
from Option B (Rule of Eighteen) to Option A (Precision Method) if MA4 runs about 50% faster
(~10s instead of 20s) or if MA5 runs about 50% slower (~21s instead of 14s). MA6 (the 45-minute
shared baseline) does not flip it at either bound. This was checked mechanically in
`cases/fret-board/sensitivity_model.py` and is recorded in `case.json.sensitivity_disclosure[]`
(Category X on both MA4 and MA5 — a good-faith estimate from the closest public analogue, not a
measured fact) and in `case.md`'s Modeling Assumptions table. **Do not present the 4.2% margin as
a settled result.** A Hero who challenges MA4/MA5's plausibility is doing exactly the right thing —
use "Deep conflict" thread 4 and Socratic question 6 to let that challenge surface naturally, and
do not hand down a resolution; the honest answer is that the time race is thin and the accuracy gap
(Appendix D) is the sturdier basis for a recommendation, which is exactly what D5 and the Twist are
already built to weigh.

## Facilitator note — sensitivity (SPEC §6)

None required — the stakes here are a first solo job, a client deadline, and a shop cost, not
personal loss, illness, or hardship. `case.json.sensitivity_note` is `null` for the same reason.
(This is a different kind of "sensitivity" than the assumption-sensitivity note above — SPEC §6 is
about emotionally sensitive subject matter, not numeric fragility.)
