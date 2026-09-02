# FACILITATOR.md — Prove It Scales

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** Prove It Scales · **Tier:** T2 (MS-core) · **Studio:** Adventure
**Standards:** Discrete Mathematics/Proof And Recursion — Mathematical Induction, Base Case,
Inductive Step, and How to prove a statement using mathematical induction (see `case.json.standards[]`
for exact ids).

**Status:** `case-research` complete (2026-09-01) — all 18 `{{NEEDS_SOURCE}}` tokens closed (11
SOURCED, 7 ASSUMPTION, 0 DROPPED, 0 OPEN; see `RESEARCH_LOG.md`). `case.json.status` is
`"researched"`. `margin_pct` is now `95.8` (see the Balance section below) — not `null`. Not yet
run through `case-qa`; treat the numbers as sourced-and-computed but not yet QA-adjudicated.

## Real-world grounding (for the facilitator's own background, not for case.md)

- **Oren Eini (Ayende Rahien), founder of RavenDB** — "Production postmortem: Your math is wrong,
  recursion doesn't work this way" (ayende.com/blog/197637-A). A real recursive map-reduce
  billing-aggregation function (Users, Credits, Charges) silently violated its own inductive
  assumption once already-reduced intermediate results were fed back into it across cluster nodes,
  producing real divergent per-account billing totals. This is the real-world precedent for
  Appendix E and for Background's "Meterworks has shipped a bug of this shape before" line — the
  Meterworks incident is fictional scenario detail *modeled on* this real failure shape; the two
  are not the same incident, and the case should never claim they are.
- **Felipe Dutra Tine e Silva, "Iterative vs Recursive vs Tail-Recursive in Golang"** — real,
  reproducible Go benchmark: iterative 16.4 ns/op, tail-recursive 33.3 ns/op, plain (non-tail)
  recursive 394 ns/op. This is the real ~2x (TCO honored) vs. ~24x (TCO not honored) gap that
  Appendix D's placeholders should eventually be scaled from.
- **pope/go_recursive_benchmark (GitHub)** — real extreme-case benchmark: a naive
  exponential-recursion Fibonacci at ~312,238,250 ns/op vs. a tail-call-optimized rewrite at
  ~35.36 ns/op — roughly an 8.8-million-times gap. This is the real anchor for Appendix E's
  "extreme end of the non-tail-callable cost gap" placeholder, and for a Twist built around "what
  if the recursive form isn't even tail-callable at all."
- **AWS TLA+ on DynamoDB/S3** (Newcombe et al., CACM 2015) and **seL4 / DARPA HACMS** (Klein et
  al.) — real, named engineering-culture anchors for "prove it, don't just argue it informally,"
  useful for Anchor 2/Intro framing and for pressure-testing whether Devon's stakes justify a
  proof at all. Neither is Meterworks' own story; both are real external comparison points.

## Intro

Frame the format: this is a real ship/no-ship engineering decision the night before a release
freeze, not a worksheet. Name the opener — "You are the engineer whose name is on this function.
One version is proven correct. The other version is proven fast. You don't get both, and you
have to pick tonight." Mention, once, that companies like AWS have used formal proof methods
(TLA+) to catch real bugs before shipping — this is a real professional practice, not an academic
exercise invented for the case.

## Launch

Show the two branches side by side exactly as the Overview describes them — the proof, and the
climbing red chart on Devon's second monitor — with no runtime numbers yet. Ask: "Which one would
you ship, just from what you see here?" Do not confirm or correct. Most rooms will split; record
the split, Close will re-ask it.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the Guaranteed Floor — the version with no proof on
file?" Show of hands, both options, no discussion yet. Record the count.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'proven correct'?"**

Let confusion grow here on purpose. Heroes will want to jump straight to "which one is faster,"
but push on what "proven correct" buys you that "tested and it looked fine" doesn't: "If the
Guaranteed Floor's tests all pass at depth 6, and Meterworks' real account trees never nest past
depth 6, does the Provable Path's proof matter at all? What would have to be true about
Meterworks' actual account hierarchies for that proof to matter?" If the room lands on "a proof
covers depths nobody has tested yet, a test suite only covers the depths someone thought to try,"
the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "which one is faster" from "which one's correctness guarantee is worth
trusting," ask them to name the actual steps before touching the appendices: write the induction
proof itself, base case and inductive step (D1); trace it on a real sample hierarchy (D2); connect
the inductive step to why runtime scales with depth (D3); build the six-cell runtime table across
both TCO scenarios and three depths (D4); and decide, using all of that, which version ships (D5).
Re-ask: "Is our question still the right one, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gap honestly: Meterworks' own traffic volume, its own maximum real
account-hierarchy depth, and which language runtime the release actually ships to are all
currently open `{{NEEDS_SOURCE}}` tokens — Meterworks is a fictional company, so none of these can
be independently verified the way the *shape* of the recursive/iterative cost gap can (that part
is anchored to a real, published benchmark). Ask which of the open figures is actually load-bearing
for the recommendation. The honest answer: the target-runtime TCO fact (Appendix B) is the single
most load-bearing open item in the whole case — it is the variable that decides whether Option A
costs ~2x or ~24x-1,000x+ more than Option B, which is a materially different question than "is
recursion slower."

## Data Deep Dive

Now, and only now, the numbers (once `case-research` has closed Appendix D). Walk D1's proof, D2's
trace, D3's interpretation, and D4's six-cell table together as a room, cold-calling for D4
specifically — this is where a Hero who wrote a correct D1 proof but never connects it to D4's
actual runtime numbers will visibly struggle to answer "so is the proof worth it, here, tonight."

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses, once Appendix E is sourced: "There's a real company — not Meterworks,
a real one — whose recursive billing-aggregation function looked exactly like the Provable Path.
It was proven correct on paper. It shipped anyway. And in production, it silently violated its own
inductive assumption once an already-computed result got fed back into it one level down — two
customer accounts' billing totals came out on opposite sides of zero for the same real numbers."

"If a proof like the one you wrote for D1 can still fail in production when the *implementation*
doesn't actually match the proof's own assumptions at every call site — does that make you trust
the Provable Path more, or less, than you did five minutes ago? What exactly would you have to
check, beyond writing the proof itself, to be sure this doesn't happen to Devon's version?"

**Facilitator-only: what this does and doesn't change.** This is the real Ayende/RavenDB
postmortem (see grounding section above) — it does not change D4's runtime numbers, and it is not
proof that Option A is wrong. It is proof that "I wrote an induction proof" and "the shipped code
provably matches every premise the proof assumed" are two different claims, and a Hero who
conflates them has not fully reckoned with what D1 does and doesn't guarantee.

## 45-Minute Socratic Plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch (Intro/Launch above), 30-second commitments, stand/sit vote (Anchor 1) — no explanation. |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just fair" (Anchor 2 — what does "proven correct" actually buy you?). |
| 10:00–15:00 | Pressure-test the models: process and open assumptions (Anchors 3–4) — name the D1-D5 steps, surface which figures are real vs. stated. |
| 15:00–25:00 | Data Deep Dive — D1-D5 together; cold-call D4's six-cell table specifically. |
| **25:00** | **DROP THE TWIST** — the real RavenDB/Ayende postmortem, delivered slowly, with pauses. |
| 25:00–30:00 | Immediate recommit: who reverses? "What just broke — the proof, or your trust in what the proof covers?" |
| 30:00–40:00 | Threaded deep conflict — see the three named threads below. |
| 40:00–45:00 | Close, re-vote, reflection, Lessons Learned. |

## Deep conflict — threads (20–30 min)

1. **A proof about the function is not automatically a proof about the deployed system.** D1's
   induction proof is airtight *given its own stated assumptions* — but the RavenDB twist shows a
   real case where the code silently stopped matching those assumptions at one call site. Push:
   "What would you need to check, beyond D1 itself, to be sure Devon's implementation actually
   satisfies D1's inductive step at every real call site?"
2. **"Recursive is slower" is not one fact, it's a fact that depends on one switch.** A Hero who
   treats Appendix D as "recursion costs more" without noticing the TCO column has missed the
   entire secondary lever the case is built around. Push: "If Meterworks' target runtime honored
   TCO, would this still be a hard decision?"
3. **Correct-forever vs. fast-right-now.** The Provable Path's guarantee holds for every depth,
   including depths Meterworks doesn't have yet. Push: "Is a guarantee about hierarchy depths that
   don't exist yet worth paying for today — and does your answer change if Meterworks is growing?"

## The trap

Heroes will treat "recursive is slower" as a flat, universal fact and recommend the Guaranteed
Floor on that basis alone, without ever checking Appendix B's TCO fact — missing that the real
size of the gap (Appendix D) depends entirely on whether the target runtime honors tail-call
optimization, which is the actual analytical fork this case is built around. A second, related
trap: treating D1's induction proof as a guarantee about the *deployed* system rather than a
guarantee about the function *as specified* — the RavenDB twist exists specifically to catch a
Hero who has not distinguished "I proved the recurrence is correct" from "I verified the shipped
code actually satisfies every premise the proof assumed at every call site."

## Socratic questions

1. Your D4 table has two very different numbers for the recursive version — one under a TCO-honoring runtime, one without. Which of those two numbers should actually drive Devon's recommendation, and why does it matter which one you pick?
2. Your D1 proof shows the recursive version is correct for a hierarchy of *any* depth. Does that proof, by itself, tell you anything about how *fast* the function runs? Why or why not?
3. The twist describes a real company whose recursive aggregation function was proven correct on paper and still produced wrong billing totals in production. Does that mean D1's proof was worthless — or does it mean something more specific about what a proof does and doesn't cover?
4. If Meterworks' maximum real account-hierarchy depth turned out to be much shallower than the "Deep" row in Appendix D, which parts of your D4/D5 argument would still hold, and which wouldn't?
5. Appendix A lists a target language/runtime for the release as a still-open figure. If you had to recommend a version *before* that runtime is finalized, would you recommend differently than if you already knew whether it honors tail-call optimization? What does that tell you about how much of this decision is actually a math question versus an infrastructure question?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare to Anchor 1's vote — a room that moves after the
twist should be pressed to explain the move using D1/D4, not just the twist's emotional weight.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

## Standards Touched On

Mathematical Induction · Base Case · Inductive Step · How to prove a statement using mathematical
induction

## Balance argument (SPEC §2 — drafted now, `margin_pct` is `null` until sourced)

**Argument for A (the Provable Path).** The induction proof (D1) is airtight for every hierarchy
depth Meterworks will ever have, including depths that don't exist in its account base yet — a
real, permanent asset for billing-critical code, and the exact kind of guarantee AWS's own
engineers have said they wished they'd had before shipping DynamoDB/S3-critical code informally.
If the target runtime honors TCO (Appendix B), the real Go-benchmark-anchored cost gap is small
(~2x per the strengthened concept research), which makes the correctness guarantee close to free.

**Argument for B (the Guaranteed Floor).** Its per-call cost never depends on a runtime detail
Devon does not control and Appendix A hasn't even settled yet — if the target runtime does *not*
honor TCO, the real benchmark-anchored gap is large (~24x in a modest case, and the real extreme-case
benchmark shows it can reach ~8.8 million times in the worst case), a cost Devon would be accepting
for a proof that only covers the function *as specified*, not the deployed system (see the twist).
Meterworks has already shipped one bug of exactly the shape the twist describes, real-world
precedent included — an argument that a flat, boring, easy-to-verify-by-hand implementation has its
own kind of safety.

**Margin — COMPUTED 2026-09-01 (case-research).** `margin_pct: 95.8`. **Winner: Option B, The
Guaranteed Floor (iterative).** At the Shallow depth (closest to Appendix A's real max hierarchy
depth, 5 levels, AWS Organizations FAQ), under Go — Appendix A's target runtime, which Appendix
B/S4 confirms does not guarantee or reliably apply TCO — Option A (recursive) costs 3.94 ms per
10,000 rollups and Option B (iterative) costs 0.164 ms, both real, directly-measured figures from
the Felipe Dutra Tine e Silva Go benchmark (S1). margin_pct = (3.94-0.164)/3.94 × 100 = 95.8%.

**This margin is wide, well past SPEC §2's ~20% guideline, and it is not being softened** — the
task that produced it was explicit that an over-20% margin should be reported plainly. Checked the
counterfactual: even under a TCO-*honoring* runtime instead of Go, the same Shallow-row real data
gives (0.333-0.164)/0.333 = 50.8% — still far over 20%. So this is not an artifact of picking Go
as the target runtime (MA7): the real, cited D4 numbers show iterative beating recursive decisively
under *both* runtime regimes at every measured depth. No available Modeling Assumption is a lever
that would bring the margin under ~20% without contradicting real, cited benchmark data (S1, S2) —
retuning is not available here the way it was on other cases, because the gap is real, not a
modeling artifact.

**What this means for facilitation.** The case's genuine tension is *not* a close numeric race on
D4 — it's the qualitative one `argument_a`/`argument_b` are already built around: D1's permanent,
depth-independent correctness guarantee vs. D4's decisive, real, sourced performance cost. Treat
this the way a T1-tier case with a clean, lopsided winner is treated: the room's real work is
arguing whether the correctness guarantee is worth paying a large, real cost for — not disputing
whose number is bigger. Full arithmetic trail: `case.json.balance.margin_note`.

## Facilitator note — sensitivity (SPEC §6)

NONE. This is routine software-engineering correctness-vs-performance math — no subject-matter
sensitivity flag applies.
