# FACILITATOR.md — The Yield Die

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Yield Die · **Tier:** T3 (MS-stretch / HS-entry) · **Studio:** Adventure
**Standards:** Advanced Operations / Scientific Notation — Standard Notation, Scientific Notation,
How to write a number in scientific notation given its standard notation, How to write a number in
standard notation given its scientific notation (see `case.json.standards[]` for exact ids).

**Status:** `case-research` complete (2026-09-09), revised after Tier 2 P2/P4 remediation. Every
`{{NEEDS_SOURCE}}` token in `case.json` is resolved (`SOURCED` or disclosed `ASSUMPTION`).
`margin_pct = 8.23` at the case's base assumed defect density (Option A, the Compact Die, wins) —
but the verdict **genuinely flips** to Option B within the disclosed ±50% sensitivity range. See
Balance argument below.

**One-line sensitivity flag (SPEC §6):** no illness/death/family-hardship content. The stakes are a
fictional startup's business decision — real but not personally weighty in the way some corpus
cases are. No special facilitator caution needed beyond normal engagement framing.

## Real-world grounding (for the facilitator's own background, not for case.md)

- Wafer yield economics is a real, standard topic in semiconductor engineering and industry
  analysis. TSMC is the real, named foundry at the center of the 2026 AI-chip buildout; the
  protagonist's company and specific chip are fictional.
- No foundry publicly discloses its live defect density or exact node transistor density for a
  specific customer's tape-out — these are commercially sensitive figures. `case-research` will
  need to ground both in real published *ranges* (industry analyst reports, academic yield-model
  papers, investor-disclosed competitor figures) and disclose the specific value used as a stated,
  industry-representative Modeling Assumption — never presented as TSMC's own exact figure.
- The pedagogical core is genuinely real: comparing gross die count alone overstates the smaller
  die's advantage, because (a) a larger die suffers proportionally more yield loss to random
  defects, and (b) a larger die is not the same product — it carries more transistors and commands
  a higher price. Both effects have to be modeled together to get the real economic answer, and
  naive students reliably skip the yield step entirely (see the wrong-path section below).

## Balance argument

**Revised after Tier 2 remediation (2026-09-09):** the case's first-draft calibration (D0=0.10,
pure linear pricing) turned out to make Option A win on revenue per wafer at *every* non-negative
defect density — confirmed independently by a both-sides-solve probe and a twist-integrity probe,
both of which found the "assumption" could never actually flip the verdict, contradicting D5's own
prompt asking readers to name the value that would flip it. The fix: (1) the base assumed defect
density (MA2) was moved to 0.30 defects/cm² — still real and defensible (below Intel's own
disclosed 18A ceiling of 0.40), and arguably *more* defensible than the original 0.10, since this
is the company's *first* tape-out on a not-yet-mature line; (2) a modest, disclosed flagship pricing
premium (MA4, ×1.19, grounded in the real Nvidia L4-vs-H100 dollars-per-transistor gap) was added to
Option B only. Together these make the case a genuine, bidirectional dilemma with a real, findable
crossover — see below.

- **Argument for A (Compact Die):** wins on revenue per wafer at the case's base assumed defect
  density — 640 gross dies × 76.92% yield = 492 net good dies × $7,500/die = **$3,690,000**, versus
  the Full Die's 191 net good dies × $17,850/die = **$3,409,350** — an 8.23% margin. At D0=0.30, the
  Full Die's larger area costs it disproportionately more yield (62.50% vs. 76.92%) than its higher
  price and premium can make up.
- **Argument for B (Full Die):** genuinely wins at a *lower* defect density — at D0=0.15 (within the
  disclosed −50% sensitivity flex), the Full Die's 235 net good dies × $17,850 = $4,194,750 edges
  out the Compact Die's 556 × $7,500 = $4,170,000, a real (if thin) 0.59% win for B. The crossover
  defect density is approximately **D0 ≈ 0.157–0.16 defects/cm²**: below it, the Full Die's double
  transistor count and flagship premium win; above it (including the case's own base assumption),
  the Compact Die's much larger gross-die-per-wafer count and better-preserved yield win.
- **The margin — RESOLVED by case-research:** `case.json.balance.margin_pct = 8.23` at the base
  case. `margin_basis` in `case.json` records the full method; full arithmetic (including the
  crossover derivation) is in `RESEARCH_LOG.md`. **case.md never states which option wins, nor the
  crossover value.**
- **Why this is close and not obvious:** a student who compares only gross die counts (ignoring
  yield and price entirely) sees the Compact Die produce roughly **double** the raw die count of
  the Full Die (640 vs. 306, a naive ~109.15% "advantage") — but once yield loss (worse for the Full
  Die at this defect density) and price (better for the Full Die) are both applied correctly, the
  real revenue-per-wafer gap narrows sharply, from a naive ~109.15% down to the true 8.23% — and could
  even flip entirely under a different, equally defensible reading of the one open assumption. That
  gap — between the naive gross-count comparison and the true revenue comparison — is exactly the
  concept sheet's stated wrong-path pitfall, reproduced by this case's own numbers (see "The trap,"
  below).
- **Sensitivity (MA2, defect density) — GENUINELY FLIPS:** flexing the assumed defect density ±50%
  (0.30 → 0.15 or 0.30 → 0.45) **does** flip the winner. At −50% (D0=0.15), Option B wins by 0.59%.
  At +50% (D0=0.45), Option A wins by 15.09%. See `sensitivity_model.py`.

## Five Socratic questions

Do not let a Hero see the resolved margin (8.23%) before Anchor 4.

1. Your D3 table shows one option with far more gross dies per wafer than the other — before you look at D4, what would have to be true about defect density or pricing for the option with fewer dies to still win?
2. If a classmate said "just count the chips — more chips per wafer always wins," what row in your D4 or D5 table would you show them to demonstrate that gross die count and revenue per wafer are not the same question?
3. D2 gives you a transistor count for each option using the same transistor-density figure for both — what does that tell you about what's actually driving the difference between the two options?
4. D5 asks you to name the one figure your recommendation depends on most — is it the transistor density, the defect density, or the price benchmark, and how did you decide which one actually moves the answer versus which ones just scale both options equally?
5. Appendix A says the company has committed to exactly one wafer lot this quarter — if they could afford to run a small trial batch of the other option first, would that change how confident you'd want to be in your Appendix D assumption before submitting the real order?

## The trap

A learner who compares only gross die count (Appendix B/D3) — "the Compact Die makes roughly twice
as many chips per wafer, so it's the easy choice" — has committed exactly the trap this case is
built around. That comparison never applies Appendix D's defect-density yield model at all, and it
implicitly assumes every die is worth the same regardless of size, which Appendix C and Appendix E
directly contradict (the Full Die carries more transistors and sells for more). The tell in
discussion: ask a Hero who picked the Compact Die on gross count alone to state the Full Die's
actual net good die count and price per die from D4/D5 — most will not have carried the calculation
that far, because the gross-count comparison already felt conclusive.

## Sensitivity note

The defect density (MA2 in case.json.modeling_assumptions, once case-research completes) is this
case's one genuine free scenario dial — no foundry discloses its live defect density for a specific
node, so any figure used is a disclosed, industry-representative estimate rather than a confirmed
fact. `sensitivity_model.py`'s `FLEX` sweeps exactly this parameter. The transistor-density figure
(MA1) and the pricing-benchmark derivation (MA3) both scale *both* options by the same factor and
so do not change which option wins — only the absolute dollar figures in D5; they are recorded as
assumptions for transparency, not because they are fragile.

---

## Guide Notes — the anchor ladder (SPEC §7)

### Intro

Frame the format: Priya has one wafer lot, one irreversible decision, and a board waiting on the
number. Name the opener: "You have the die-size field open. What goes in the box?"

### Launch

Show the Overview's two floorplans and the engineer's line ("More chips per wafer. It's not
close.") with no numbers yet. Ask the room to react to his confidence before anyone has seen
Appendix D.

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "Is anyone courageous enough to stand with the Full Die — the option with the
lower die count?" Record the split; most rooms will lean toward the Compact Die before seeing any
math, which is the point.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push past "which die is bigger" toward "what actually determines how much money one wafer makes."
Let the room sit with the fact that more chips is not automatically more revenue. "Is 'which option
makes more chips' even the right question, or is the real question 'which option makes more
money'?"

### Anchor 3 — WHAT IS THE PROCESS?

Before touching Appendix D's numbers, get the room to state the actual comparison method: count
gross dies (D3), apply the *same* defect density to both options to get real yield (D4), then value
each good die at its actual price, not an assumed equal price (D5). Re-ask: "Now that we know the
process, do we still think this is about counting chips — or about revenue?"

### Anchor 4 — WHAT DON'T WE KNOW?

Name the load-bearing unknown explicitly: the real defect density on this not-yet-running process
line. "Is this something we could look up if we tried harder, or is it something nobody — not even
TSMC's own customers — can know for certain in advance? What makes a defensible assumption
different from a guess here?"

### Data Deep Dive

Now open Appendices B–E. Run D1–D5 as a room, or have groups report out.

### Twist

At roughly the 15-minute mark: "TSMC just told you their measured defect density on this line came
in at 0.15 defects per square centimeter — half of what you assumed. You have 60 seconds: does your
recommendation change?" This is a real, computed flip, not a hypothetical: at D0=0.15 the Full Die
actually overtakes the Compact Die — 235 net good dies × $17,850 = $4,194,750 for B, versus 556 ×
$7,500 = $4,170,000 for A — Option B wins by 0.59%. Any group that recommended the Compact Die at
the case's base assumption (D0=0.30) now has
to decide, live, whether their reasoning survives a cleaner-than-expected process line. Groups whose
argument was "the Compact Die always wins, more chips is more chips" should be visibly shaken; a
group whose argument was "at THIS defect density the Compact Die wins, but I know that's not
guaranteed" should barely flinch — that contrast is the whole teaching moment, and it now has a
mathematically real crossover (~D0=0.157–0.16) behind it, not just an assumption that moves the
margin without ever changing the winner.

### Close

VOTE AGAIN. "Did we ask the right question?" "What math was new to you today?" Compare the re-vote
to Anchor 1's cold vote.

### Lessons Learned

The core transferable idea: a bigger raw count (more chips, more of anything) is not automatically
a bigger win once you account for the two things that actually determine value — how many of them
actually work, and how much each one is worth. Counting is not the same as valuing.

### Standards Touched On

Standard Notation, Scientific Notation; How to write a number in scientific notation given its
standard notation; How to write a number in standard notation given its scientific notation.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00-3:00 | Cold-call launch, 30-second gut-check vote (Anchor 1) — no explanation |
| 3:00-10:00 | Position defense: "Convince us why your pick makes more money, not just more chips" |
| 10:00-15:00 | Pressure-test: "Whose recommendation never actually applied the yield model?" |
| **15:00** | **DROP THE TWIST** — the real defect density comes in different than assumed; deliver slowly, with a pause before "does your recommendation change?" |
| 15:00-20:00 | Immediate recommit: who reverses, who holds? "What just broke — the number, or the reasoning?" |
| 20:00-30:00 | Threaded deep conflict — two named threads: (1) "counting chips vs. valuing chips," (2) "a rule of thumb vs. running your own yield numbers" |
| 30:00-45:00 | Close, re-vote, reflection, lessons learned |

## Cohort bands (SPEC §7)

| Band | Typical size | What changes |
|---|---|---|
| **Full** | 12-20 (the size this case is written for) | Anchors and timings run as written above |
| **Compressed** | 6-11 | Anchors 2-3 combine into one pass; the deep-conflict section (20:00-30:00) runs one thread instead of two; total runtime shortens proportionally |
| **1:1 / pair** | 1-2 | No vote at Anchor 1 — instead ask for a stated initial position and why; the facilitator plays devil's advocate directly rather than cold-calling the room; the Twist still lands, and "who reverses" becomes "would you reverse, and why" |
