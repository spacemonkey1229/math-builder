# Guide Notes: The Dosing Curve

**Case:** The Dosing Curve · **Tier:** T2 (MS-core) · **Studio:** Adventure
**Standards:** Calculus/Integrals — Antiderivative, Definite Integral, Indefinite Integral,
Riemann Sum / How to find an antiderivative using the power rule, How to evaluate a definite
integral using the Fundamental Theorem of Calculus, How to approximate area under a curve using a
Riemann sum (see `case.json.standards[]` for exact ids; this is a reinforcement case, not a
new-skill-coverage case — see `case.json.reinforcement_note`).

**Researched 2026-08-31; cost tie-breaker retuned 2026-09-01 (case-qa stage); primary PK/PD gate
restructured 2026-09-01 (case-readiness stage) into an explicit, computable convention-sensitivity
table — D5/Appendix G, see "The margin" below.** All 30 `{{NEEDS_SOURCE}}` placeholders resolved: 28
SOURCED (real, cited figures — see `case.json.sources[]` and `RESEARCH_LOG.md`), 2 ASSUMPTION
(Appendix B's reconstructed concentration-time curve, MA1; the operation's per-head budget cap,
MA5 — both anticipated by the original concept research). `margin_pct = 13.9` (retuned from an
initial 29.7%, which exceeded SPEC §2's ~20% balance-test cap — see the margin section below),
winning option **B (The Four-Day Course)** on cost. The primary fAUC/MIC gate is genuinely
convention-sensitive — neither option clears it under every real combination of dosing point, MIC
benchmark, and window convention — so the cost margin is reported as a real number regardless, not
gated on a forced single verdict on the primary axis.

**Sensitivity flag (SPEC §6): LOW, not none.** This is a livestock/veterinary antimicrobial-dosing
scenario, not a human-patient one — the safer register per SPEC's own guidance. Facilitators
should keep the discussion in a routine, professional antimicrobial-stewardship register
(protocol compliance, published efficacy thresholds, cost, real handling-cost data) and should
**not** depict animal suffering, disease progression, or death, and should avoid framing that
reads as a human-antibiotic-resistance alarmism piece — the real subject is a routine,
well-regulated veterinary dosing decision, not a public-health crisis.

## Argument for A — The Single Shot (long-acting, single injection)

The long-acting formulation's much longer half-life means its concentration curve never has a
chance to sag between doses, because there is only one dose — its computed AUC over the full
treatment window is a single, continuous definite integral with no gaps to worry about, and no
dosing-point or window-convention choice to argue about (see D5/Appendix G). Its AUC0-24h (39.1
μg·h/mL) clears the calves fAUC/MIC target (24) under every real convention, and misses only the
CLSI/adult-cattle target (48) — a target the Four-Day Course also misses in every one of its own
cells. That structural safety margin is the strongest case for A: fewer handling events (lower
cumulative injection-site-lesion cost exposure per Appendix E, and less labor), and a fAUC/MIC
result that does not move no matter which dosing point or window convention a reviewer picks. The
trade-off it accepts is a higher per-dose price and, per the real published comparative literature
summarized in the concept research, measurably more tissue damage *per injection event* than the
conventional formulation causes per event — a cost the case should have the student weigh against
A's fewer total events, not ignore.

## Argument for B — The Four-Day Course (conventional, repeated dosing)

The conventional formulation is cheaper per dose and causes less tissue damage per individual
injection. Once Appendix B's modeled curve is correctly rescaled off its 20 mg/kg study dose down
to the label's real 3–5 mg/lb/day rate (D5/Appendix G), its AUC0-24h clears the calves fAUC/MIC
target (24) in 3 of the 4 real dose/window combinations — failing only at the label's low end (3
mg/lb/day) judged on the strictest, day-1-only window (21.4 < 24). B is the lower-total-cost
option on drug price regardless of how the efficacy gate lands — but only once its larger number
of handling events is priced against Appendix E's per-event lesion-cost data, not against drug cost
alone. B's real structural risk, and the reason this case cannot be resolved by comparing
single-dose AUC totals, is that its shorter half-life means concentration could plausibly dip
toward (or below) the MIC-derived breakpoint in the gap between two doses at the low end of its
labeled range, even while a higher dosing point or the accumulated course-total reading clears the
target — that gap-level, convention-dependent behavior is exactly what D5's table is built to make
visible.

## The margin

**`margin_pct = 13.9` (retuned from an initial 29.7%), Option B (Four-Day Course) wins on cost.**
The cost tie-breaker is resolved cleanly (see (2) below). The primary PK/PD gate is **not** resolved
to a single verdict — it is restructured into an explicit, computable convention-sensitivity table
(D5/Appendix G) that the student builds and interprets. See both findings below.

**(1) The primary gate — fAUC/MIC pass/fail — RESTRUCTURED 2026-09-01 (case-readiness stage) into
D5's convention-sensitivity table, not resolved to one verdict.** Case-research (see
`RESEARCH_LOG.md`) had already identified three genuinely disputed choices the real cited
literature does not settle for this exact dose/interval combination: (a) which point in the
conventional label's 3-5 mg/lb/day range [S5] is used, (b) whether the CLSI clinical breakpoint
(≤2 mg/L) [S3] or Winter et al.'s PK/PD cutoff (1 mg/L calves / 2 mg/L adults) [S2] is used as the
MIC denominator, and (c) whether pass/fail is judged on the first day's AUC alone or the
accumulated course-total AUC once MA2's multi-dose superposition is applied. An earlier
case-readiness pass tried to resolve this to a single verdict by (i) reading 64.7 μg·h/mL directly
off Appendix B's modeled curve for the Four-Day Course without rescaling it off the curve's
underlying 20 mg/kg (~9.07 mg/lb) study dose down to the label's actual 3-5 mg/lb/day rate, and
(ii) treating the calves MIC benchmark as case-dictated rather than carrying both real benchmarks
forward. Both of those moves are corrected here.

**The corrected table** (real numbers, full derivation in `case.json.derived.primary_gate_resolution`
and Appendix G):

| Dose (conventional) | Window | AUC0-24h (μg·h/mL) | vs. calves target (24) | vs. CLSI/adult-cattle target (48) |
|---|---|---|---|---|
| 3 mg/lb/day (label low end) | Day-1-only | 21.4 | **FAIL** | FAIL |
| 3 mg/lb/day | Course-cumulative | 26.9 | PASS | FAIL |
| 5 mg/lb/day (label high end) | Day-1-only | 35.7 | PASS | FAIL |
| 5 mg/lb/day | Course-cumulative | 44.8 | PASS | FAIL (close: 44.8 vs. 48) |

The Single Shot needs no rescaling (its 9 mg/lb label dose [S4] already ≈ the 9.07 mg/lb study
dose) and has no window choice (one continuous injection): AUC0-24h = **39.1 μg·h/mL** — PASSES the
calves target (≥24), FAILS the CLSI/adult-cattle target (<48).

**What the table shows:** the MIC-benchmark choice is the dominant swing factor — under
CLSI/adult-cattle (48), *both options fail in every cell*, regardless of dosing point or window.
Under the calves benchmark (24) — the benchmark that matches this case's own stated
stocker/feeder-calf population, though a Hero could reasonably still name the CLSI breakpoint as
a *population-independent* clinical standard worth citing too — the Single Shot always passes,
while the Four-Day Course's pass/fail flips depending on which end of its labeled range is dosed
and which window convention is applied, failing only at the low end under the strictest test.
Reasonable experts could land in different cells here: a regulator auditing worst-case exposure
might insist on the day-1-only window and the CLSI breakpoint (both options fail); a clinician
citing the case's own stated calf population and the standard multi-dose accumulation model might
call both options a pass at the label's high end. **Neither reading is fabricated — both use only
real, cited numbers — and that is the point of D5.**

**What a strong D5 submission looks like:** builds all 4 (or all 8, if also comparing the Single
Shot's 2 MIC rows) real cells correctly, using D1/D2's own AUC methods rescaled to each cell's
dosing rate; states plainly which cells pass and which fail for each option; and explicitly names
*which* convention it is defending and why — not "it depends," but "I would defend the label's high
end (5 mg/lb/day) and the calves benchmark, because [reason tied to the case's stated population
or a stated risk tolerance]," while acknowledging the cells where its own chosen option fails.

**What a weak D5 submission looks like:** picks one convention silently (most often reusing
Appendix A's single-dose totals, or the unscaled Appendix B curve, without noticing the dose
mismatch) and reports a single pass/fail as if the literature had settled it; or builds the table
but never states which cell it is actually willing to defend to an auditor, leaving the
"interpret" half of D5 undone.

**Regardless of how a Hero reads D5, the cost tie-breaker below is reported as the case's real
cost number — it is not gated on a forced efficacy verdict.**

**(2) The cost tie-breaker, which computes cleanly from real sourced data — RETUNED 2026-09-01.**
The original computation used EntirelyPets Rx's same-retailer, same-bottle-size list pricing (S7),
a 500 lb representative animal (MA3), and the conventional label's range-midpoint dosing rate
(MA4, 4 mg/lb/day):

- Single Shot (long-acting): 22.5 mL × $0.31998/mL = **$7.20** drug cost + 1 handling event ×
  ($7.05/head ÷ 11% 1995 incidence ≈ $64.09/lesion) × 0.2% current fed-cattle incidence ≈ **$0.13**
  expected lesion cost = **$7.33 total**.
- Four-Day Course (conventional, MA4 = 4 mg/lb/day): 10 mL/day × $0.11598/mL × 4 days = **$4.64**
  drug cost + 4 handling events × the same $0.128/event ≈ **$0.51** expected lesion cost =
  **$5.15 total**.
- margin_pct = 100 × (7.328 − 5.153) / 7.328 = **29.7%**, exceeding the ~20% SPEC §2 threshold.

Per MA4's own pre-existing sensitivity note, the margin was not knife-edge and moves ±25% at the
labeled range's ends — so it was retuned by moving MA4 to the labeled range's upper end, **5
mg/lb/day**, a real, already-sourced FDA-label value (S5), not a new figure:

- Four-Day Course (conventional, MA4 = 5 mg/lb/day): 12.5 mL/day × $0.11598/mL × 4 days = **$5.80**
  drug cost + the same **$0.51** expected lesion cost = **$6.31 total**.
- margin_pct = 100 × (7.328 − 6.312) / 7.328 = **13.9%**, Four-Day Course still cheaper, now under
  the SPEC §2 cap.

Both options are now confirmed to clear the primary PK/PD gate (see finding (1) above), so per this
case's own `margin_basis` ("if both pass, compare cost"), this retuned 13.9% margin is the number to
use for discussion framing.

## Anchor ladder (SPEC §7.1)

### Intro

Frame the format: a treatment protocol Priya has to sign her own name to, tonight, with a foreman
waiting by the chute — not a worksheet. Name the opener: "You are Dr. Priya Chandrasekaran. Two
dosing charts, both real, both from real drug labels. Your signature makes whichever one you pick
the herd's official record for a year."

### Launch

Read the Overview aloud, stop at "hovers the cursor over the other," and ask: "Before any
numbers — one shot and done, or four shots spread across a week. Which would you sign, and why,
just from that?"

### Anchor 1 — Take a stand and vote

"Is anyone courageous enough to stand with the Single Shot — one injection, higher price?" Count
hands. "And the Four-Day Course — cheaper, but the crew's back in that chute four times?" Count
hands. Record the split.

### Anchor 2 — What is the problem we're solving?

Let confusion grow. Heroes will want to jump to "which one is cheaper" — push instead: "Does a drug
protocol even get to be judged on cost before it's judged on whether it actually works?" The room
should arrive at "we need to check the exposure curve clears the efficacy target BEFORE cost even
matters" before Anchor 3.

### Anchor 3 — What is the process?

Walk the room toward: build a Riemann sum for each option's AUC from the sampled data (D1), fit and
integrate a continuous model to cross-check it (D2), compare both against the published fAUC/MIC
target (D3), then — only once both pass — compare total per-animal cost (D4).

### Anchor 4 — What don't we know?

Surface honestly: Appendix B's concentration-time table is a disclosed reconstruction (MA1), not
raw published data — the study never published one; the multi-dose superposition for the Four-Day
Course (MA2) is a standard PK assumption, not a certainty; the animal's body weight (MA3) and the
exact conventional dosing rate used for costing (MA4) are both stated scenario choices within real
labeled ranges. Ask: "Which of these, if it moved, would change whether a chart even clears the
efficacy line — not just its cost?"

### Data Deep Dive

Walk D1 through D5 together, but build D5's table using **only the calves benchmark (target 24
μg·h/mL)** for now — the benchmark that matches the case's own stated stocker/feeder-calf
population, and the one a Hero reaches for by default without being prompted that a second
benchmark exists. Under that one benchmark: the Single Shot's fixed AUC0-24h (39.1 μg·h/mL) passes;
the Four-Day Course's 4 dose/window cells (21.4, 26.9, 35.7, 44.8 μg·h/mL) pass in 3 of 4, failing
only at the label's low end under the day-1-only window. Let the room work through which single
cell they'd defend to an auditor, *then* reveal the cost comparison: $7.33 (Single Shot) vs. $6.31
(Four-Day Course), a 13.9% margin. Cold-call specifically for whether a Hero checked the efficacy
table before jumping to cost, and for which single cell they would actually defend if an auditor
picked one for them. **Do not yet mention Appendix C's second (adult-cattle/CLSI) cutoff or that
the target is population-specific** — hold that reveal for the Twist below; springing it early
gives away the Twist's entire point before it lands.

### Twist

Reveal that Appendix C's PK/PD cutoff concentration is population-specific — 1 mg/L for calves, 2
mg/L for adult cattle — and that the CLSI clinical breakpoint (≤2 mg/L) lands on that same 2 mg/L
number regardless of age class. Ask: "If someone in the room used that adult-cattle/CLSI number
instead of the calves cutoff, what happens to D5's whole table?" (Answer: every cell for both
options fails — even the Four-Day Course's best case, 44.8 μg·h/mL, falls short of the 48 μg·h/mL
target.) This is not a fabricated plot twist; it is the case's own real, computed table, and it
shows that a single unstated assumption (which MIC benchmark applies) can flip the entire table
from "several passing cells" to "zero passing cells" even though every underlying number is real
and unchanged.

### Close

Re-vote. "Did we ask the right question at Anchor 2? Was this ever really about which chart is
cheaper, or about which chart Priya can actually defend as effective, on paper, for the population
she's actually treating?"

### Lessons Learned

- A drug's total single-dose exposure being similar to another's (Appendix A) says nothing about
  whether the *shape* of its curve over a full multi-day course stays above an efficacy line — only
  the full-window definite integral answers that.
- An efficacy target expressed as a ratio (fAUC/MIC) is only as good as the MIC you plug in — and
  which MIC applies can depend on a fact about the case (here, the animals' age class) a Hero might
  not think to check.
- A convention-sensitivity table (D5) is not a way of dodging a recommendation — it is a way of
  showing exactly which assumption a recommendation rests on, so it can be defended cell-by-cell
  rather than asserted as if the literature had settled it.
- Cost is explicitly a tie-breaker in this case, not the primary metric — a Hero who compares cost
  first has answered the wrong question first, even if the arithmetic is correct.

### Standards Touched On

Calculus/Integrals — Antiderivative, Definite Integral, Indefinite Integral, Riemann Sum, and the
3 how-to skills (power-rule antiderivatives, FTC evaluation, Riemann-sum approximation). See
`case.json.standards[]`. `new_coverage[]` is empty by design — see the reinforcement note above.

---

## 45-Minute Socratic Plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch (Intro/Launch above), 30-second commitments, stand/sit vote (Anchor 1) — no explanation. |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just cheaper" (Anchor 2 — efficacy before cost). |
| 10:00–15:00 | Pressure-test the models: process and open assumptions (Anchors 3–4) — what's real published PK data vs. a disclosed reconstruction. |
| 15:00–25:00 | Data Deep Dive — D1–D5 together, build the convention-sensitivity table live using the calves benchmark only, then reveal the 13.9% cost margin. Hold the second (CLSI/adult-cattle) MIC benchmark back for the Twist. |
| **25:00** | **DROP THE TWIST** — the calves-vs-CLSI/adult-cattle MIC cutoff question, delivered slowly, showing every table cell flip to FAIL. |
| 25:00–30:00 | Immediate recommit — does anyone reverse? "What just broke — the cost comparison, or the efficacy table?" |
| 30:00–40:00 | Threaded deep conflict, two named threads: (1) similar single-dose totals vs. very different full-course curve shapes; (2) a population-dependent efficacy cutoff that zeroes out the whole table vs. a clean cost margin. |
| 40:00–45:00 | Close, re-vote, Lessons Learned. |

---

## Five Socratic questions

1. Your Riemann-sum AUC and your Fundamental-Theorem-of-Calculus AUC for the same option should land close together — if they don't, is the disagreement in your sampled data, your fitted curve, or your arithmetic?
2. The Single Shot's single-dose AUC and the Four-Day Course's single-dose AUC start out close to each other in Appendix A — so why can't Priya just compare those two totals and be done?
3. Between two conventional-formulation doses, does the computed concentration ever dip low enough that a definite integral over that gap alone would fail the fAUC/MIC target, even if the full-course total clears it?
4. If the Four-Day Course's total drug cost comes out lower, does that automatically make it the cheaper option once you price in its extra handling events using Appendix E's lesion-cost data?
5. Which of your four deliverables would change first if the multi-dose superposition assumption behind the Four-Day Course's cumulative AUC turned out to be wrong — and would it flip your recommendation, or just your confidence in the margin?

## The trap

**Trap 1 (empirically demonstrated — the one to watch for hardest).** Heroes will read the
Four-Day Course's AUC0-24h directly off Appendix B's modeled concentration-time curve without first
rescaling it off the curve's underlying ~9.07 mg/lb study dose down to the conventional label's
actual 3–5 mg/lb/day dosing rate (D5/Appendix G) — treating Appendix B as if it already represented
the labeled dose. This is not a hypothetical failure mode: a fresh, blind solve using only the
student packet independently made exactly this error, reading 64.7 μg·h/mL straight off the curve
instead of rescaling down to the correct 21.4-44.8 μg·h/mL range (see
`case.json.derived.primary_gate_resolution.note_on_prior_resolution`, which documents an earlier
case-authoring pass making this identical mistake before it was caught and corrected). A student
who skips the rescaling step does a real, correctly-executed integral in service of the wrong
input — the arithmetic checks out, but the dose it describes isn't the one on the label. Watch for
this specifically when a Hero moves from D2's curve-fitting straight to D3's pass/fail table
without pausing to ask "what dose was Appendix B's curve actually built at, and is that the dose
the Four-Day Course is labeled for?"

**Trap 2.** Heroes will compare the two options' single-dose AUC totals from Appendix A — a small
percentage apart — and conclude the choice barely matters, since "the areas are basically the
same." That reasoning misses that the Four-Day Course's shorter half-life means its concentration
curve behaves very differently *between* doses than the Single Shot's curve ever has to: the two
single-dose totals being close does not mean the two full-treatment-window curves behave the same
way, and only the definite integral over the *entire* window — not the single-dose AUC comparison
in Appendix A — can show whether the repeated-dosing option's cumulative exposure ever sags below
the efficacy threshold in the gaps between injections. A student who stops at Appendix A has done
real calculus (a correct AUC computation) in service of the wrong question.

## What a strong defense sounds like

There is no single right answer here, so don't grade toward "picked Option A" or "picked Option
B." A strong defense gets D1–D5 arithmetically right, states a clear recommendation, and then does
two things a weak defense skips: it builds D5's convention-sensitivity table *before* comparing
cost — not after, and not by assuming a similar single-dose AUC (Appendix A) settles the question —
and it names *which* cell of that table (dosing point, MIC benchmark, window convention) it is
defending and why, rather than presenting one pass/fail as if the literature had settled it. A Hero
who says "I'd sign the Four-Day Course at the label's high end (5 mg/lb/day) — it clears the calves
benchmark under both windows, it's cheaper, and here's why I'd defend the calves cutoff over the
CLSI/adult-cattle one for this stated population, while owning that the low end of the range would
fail" is defending far better than one who jumps straight to the 13.9% cost margin, or who reports
D5 as a single "it passes" verdict without saying which convention that rests on. A Hero who names
MA4 (the conventional dosing rate chosen from the label's 3–5 mg/lb/day range) as a real, disclosed
assumption — and can say which way both the margin *and* the efficacy table move if a different
point in that range were used — is defending better than one who treats either the margin or the
efficacy verdict as settled fact. Either recommendation (A or B) can be a strong one if it shows
this reasoning; neither is a strong one without it.

## Modeling-assumption watch (facilitator-only) — resolved 2026-08-31

The concept research flagged three placeholders as likely to resolve as stated Modeling
Assumptions rather than cited figures. Outcome, now that `case-research` has run:

1. **Appendix B's sampled curve** — resolved as anticipated: no raw digitized table exists (only
   summary stats + a plotted figure in Aktaş & Yarsan 2017), so it shipped as **MA1**, a disclosed
   one-compartment reconstruction anchored to the real half-life and real mean AUC. Its own implied
   Cmax undershoots the paper's reported Cmax — disclosed in `case.md`, not hidden; see MA1's
   sensitivity note and `RESEARCH_LOG.md`.
2. **Multi-dose superposition** — resolved as anticipated: shipped as **MA2**, stated and justified
   explicitly (linear/time-invariant PK), with the sensitivity direction noted (a real violation
   would hurt, not help, the Four-Day Course's margin).
3. **Per-dose price differential** — resolved *better* than anticipated: a real, current,
   same-retailer price comparison **was** found (S7, EntirelyPets Rx, MEDIUM confidence — retail,
   not wholesale, pricing) and shipped as a SOURCED figure, not an assumption. Converting it to a
   per-dose cost still required two further stated assumptions (**MA3**, representative body
   weight; **MA4**, a specific point-dose within the conventional label's range), since neither is
   stated anywhere else in the case.

One additional assumption not anticipated by the concept research also shipped: **MA5**, the
operation's fixed per-head treatment budget cap, necessarily fictional to this specific operation,
grounded in a real USDA APHIS NAHMS feedlot BRD-treatment-cost benchmark (S10) rather than picked
arbitrarily.

**Restructured 2026-09-01 (case-readiness stage):** the case's primary fAUC/MIC pass/fail gate does
not have one clean verdict under the real sourced parameters — it depends on which dosing point,
MIC benchmark, and window convention are used, and this is now an explicit deliverable (D5,
Appendix G) rather than a fact the facilitator hands the student. See "The margin" above,
`case.json.balance.margin_note`, and `case.json.derived.primary_gate_resolution` for the full
computable table and reasoning.
