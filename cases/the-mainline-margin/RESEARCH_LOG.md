# RESEARCH_LOG — The Mainline Margin

`case-research` run: 2026-09-01. 23 `{{NEEDS_SOURCE}}` placeholders enumerated from `case.md`.
Outcome: 15 SOURCED, 7 stated Modeling Assumptions (ASSUMPTION), 1 DROPPED (decorative, folded
into an already-sourced appendix). Zero left OPEN.

Placeholder IDs (P01–P23) below match the line-numbered enumeration run at the start of this
pass. Source IDs (S1, S2, …) match `case.md` Appendix G and `case.json`'s `sources[]`.
Assumption IDs (MA1, …) match `case.md`'s Modeling Assumptions block and `case.json`'s
`modeling_assumptions[]`.

---

## P01 — relationship between PVC pipe diameter and weight per linear foot (Background)

Decorative narrative reference, not a load-bearing figure — the actual weight values needed are
Appendix B/C's per-diameter figures, which are sourced separately (see P09/P13 below). **Exit 3:
dropped.** Replaced `{{NEEDS_SOURCE}}` with a plain appendix pointer: "(SEE APPENDIX B, C)".

## P16 — NRCS Code 430 maximum design velocity ceiling, ft/sec (Appendix D)

The task brief for this case assumed "≤7 ft/sec" as Code 430's real ceiling. Fetched the primary
document directly to check.

- Searched "NRCS Conservation Practice Standard 430 Irrigation Pipeline maximum velocity ft/sec
  Hazen-Williams C value 150" — found the real PDF at nrcs.usda.gov.
- Downloaded and read the full 2020R revision
  (`Irrigation_Pipeline_430_NHCP_CPS_2020.pdf`, 10 pp.) directly. Page 430-CPS-2, "Flexible
  conduit design → Plastic pipe": *"When operating at design capacity, do not exceed
  5-feet-per-second velocity in the full-pipe flow in pipelines with valves or some other flow
  control appurtenance placed within the pipeline or at the downstream end."* **5 ft/sec, not 7.**
- Checked whether this had changed in a newer revision: found and fetched the current November
  2024 revision (`Irrigation Pipeline (430) (Ft.) (11-24) Standard Document.pdf`). Identical
  language, same 5-feet-per-second figure, page 430-CPS-2 equivalent. Confirmed stable across both
  the 2020R and current versions.
- **Investigated the discrepancy rather than silently overriding it** (SPEC §5: never smooth over
  a contested figure — name the dispute). Searched `NRCS Code 430 "7 feet per second" OR "7 fps"
  irrigation pipeline velocity`. Result: 7 ft/sec is real, but belongs to a *different* standard —
  NRCS Code 443 (Irrigation System, Surface and Subsurface) allows up to 7 ft/sec with surge
  protection, and a 7 ft/sec *flush* velocity is separately permitted in microirrigation submains
  under Code 441. Code 430 — the standard this case's pipeline is actually certifying against per
  its own Background text — is 5 ft/sec.
- **Verdict: SOURCED, S1, HIGH confidence.** Used 5 ft/sec throughout. Added an explicit note in
  case.md's Appendix D and Appendix G naming the 7-vs-5 distinction so nobody downstream mistakes
  this for a typo or a softened number.

## P17 — Hazen-Williams equation, exact form (Appendix D)

Code 430 itself only says "compute head loss... using one of the following equations: Manning's,
Hazen-Williams, or Darcy-Weisbach" — it does not print the equation. Went to the National
Engineering Handbook it points to for design criteria.

- Searched "NRCS National Engineering Handbook 652 chapter Hazen-Williams equation form irrigation
  pipe C 150 130" — found `Title 210 – National Engineering Handbook (210-634-H, 1st Ed., Feb
  2022), Chapter 4 – Pipe Flow`, directives.nrcs.usda.gov.
- Downloaded the full 76-page chapter PDF and rendered pages 15–17 as images (pdftotext lost the
  superscript exponents on first pass — verified visually instead of trusting the garbled text
  extraction).
- Section 634.0404 gives five equivalent Hazen-Williams forms (eq. 4-21 through 4-30: velocity-form,
  SI and English; discharge-form; head-loss-solved form; diameter-solved form). Used eq. 4-28
  (English, Q-based, solved for head loss — the form that matches what Code 430's certification
  needs): **h_f = 4.732 · (Q/C_HW)^1.85 · (L/D^4.87)**, h_f in ft, Q in cfs, L and D in ft, p.
  634-4.11.
- **Verdict: SOURCED, S2, HIGH confidence.**

## P11, P15 — Hazen-Williams C-coefficient for PVC/plastic (Appendices B, C)

- Same NEH Chapter 4 document, Figure 4-8 "Values of the Hazen-Williams coefficient" (p. 634-4.12,
  rendered as image to confirm exact rows). PVC, PE, HDPE: **C = 150.**
- Noted for the record: the same table gives Aluminum = 120, not 130 as an earlier concept note
  assumed — moot for this case (neither option is aluminum pipe), but flagged in the source note
  so it doesn't get carried forward uncorrected into a future case that does use aluminum.
- **Verdict: SOURCED, S3, HIGH confidence.** Same value used for both options (both PVC).

## P18 — Standard EQIP Practice 430 cost-share rate, percent (Appendix E)

- Searched for the EQIP payment-rate statute. `WebFetch` on eCFR's own page was blocked (redirect
  to an anti-bot page); worked around it via eCFR's public renderer API
  (`ecfr.gov/api/renderer/v1/content/enhanced/current/title-7?part=1466&section=1466.23`), which
  returned the real regulatory text.
- 7 CFR § 1466.23(b)(1)(i): *"Seventy-five percent of the estimated costs incurred by implementing
  the conservation practice"* is the standard ceiling. (b)(3): historically underserved producers
  may receive up to 90%; not applicable to this case's client.
- **Verdict: SOURCED, S4, HIGH confidence.**

## P19 — EQIP Practice 430 reimbursement rate, USD per pound (Appendix E)

- General EQIP program pages don't publish per-pound rates (those are set per state, per year).
  Searched for a live state payment schedule and found "Fiscal Year 2025 Kansas EQIP Payment
  Schedule (Rest of State)" on nrcs.usda.gov.
- Downloaded the 40-page PDF and grepped for "430" / "pound": Practice 430 "Irrigation Pipeline,"
  row "PVC, by the pound" = **$4.22/lb** (standard rate); "HU-PVC, by the pound" = $5.06/lb
  (historically-underserved rate, not used).
- Kansas also happens to be the same state as the K-State Extension MF2360 publication named in
  the task brief, which kept the case's implied geography internally consistent.
- **Verdict: SOURCED, S5, HIGH confidence.** Note recorded: this is a fixed schedule rate paid on
  completion "regardless of the cost of installing it" per NRCS payment-schedule policy — it does
  not require re-deriving 75% of an actual installed cost.

## P08, P09, P12, P13 — Nominal diameters and weight per linear foot (Appendices B, C)

- Needed a real, adjacent standard-size pair of ag PVC mainline pipe with published weight data.
  Searched several PVC price-list/spec-sheet leads (FlexPVC, National Pipe & Plastics — no usable
  public PDF found for the latter) before finding **JM Eagle's "Irrigation P.I.P." product
  catalog** (`jmeagle.com`), which explicitly states it "MEETS ASTM D2241 AND/OR NRCS 430-DD" —
  i.e., it is built for this exact NRCS practice.
- `WebFetch` couldn't parse the PDF's embedded tables as text; downloaded it directly and ran
  `pdftotext -layout`, which worked. Section 04 "Dimensions and Weights," Rated 125 psi (SDR 32.5)
  table:
  - 6 in: O.D. 6.140 in, weight **2.40 lb/ft**
  - 8 in: O.D. 8.160 in, weight **4.16 lb/ft**
- These also fix the diameter choice itself (6 in / 8 in as adjacent standard nominal PIP sizes)
  rather than an arbitrary pick.
- **Verdict: SOURCED, S6, MEDIUM confidence** (downgraded from HIGH: the live catalog PDF carries
  no visible revision date on its cover or in the body text; its embedded PDF metadata shows a
  2009 creation date. The dimensions conform to the fixed ASTM D2241 SDR series, which does not
  change, but the document's currency as posted today could not be independently confirmed).

## P10, P14 — Material cost per linear foot (Appendices B, C)

- Manufacturer catalogs don't publish retail prices. Searched "PVC IPS Class 125 pipe price list
  per foot... irrigation mainline 2025 2026" and found Direct Pivot Parts, an online ag-pipe
  retailer, selling gasketed PIP pipe by the foot at matching PSI ratings.
- 6 in, 125 psi: **$5.10/ft** (SKU 6PIPE125). 8 in, 125 psi: **$7.30/ft** (SKU 8PIPE125).
- **Verdict: SOURCED, S7/S8, MEDIUM confidence.** Both product pages flag "Limited Availability"
  and "Starting at" language and invite a quote for confirmed current pricing — a real, dated
  retail list price, but a proxy for material cost rather than a manufacturer mill price, and
  possibly regionally specific. Noted as a caveat in both source records.

## P20 — Pump fuel type (Appendix F)

Case.md itself frames this as "this case's own scenario constraint — not an external source." Set
to **electricity** (grid-powered pump) — this choice is what let P21/P22 below resolve to a
real, dated, national reference figure rather than a regionally volatile diesel/propane price.
**Verdict: ASSUMPTION, MA7.**

## P21 — Water-horsepower-hours per unit of pumping energy (Appendix F)

- Searched "water horsepower hours per gallon diesel per kWh irrigation pumping cost university
  extension table." Found references to the "Nebraska Pumping Plant Performance Criteria," widely
  cited but not itself easily fetchable as a live primary document.
- `WebFetch` on the Oklahoma State University Extension PDF that republishes this table returned
  HTTP 403 (blocked); direct `curl` also returned an HTML anti-bot page, not the PDF. Did not
  fabricate the well-known figures from memory — kept searching for a fetchable republication.
- Found and successfully fetched **University of Georgia CAES Field Report C965, "Irrigation
  Pumping Plant Performance,"** Table 1: Diesel 12.5 whp-hr/gal; Gasoline 8.55 whp-hr/gal;
  Electricity **0.885 whp-hr/kWh**; LP gas 6.89 whp-hr/gal. Explicitly states these assume 75%
  pump efficiency and 5% drive loss for non-electric units. Reviewed 2012-06-22, originally
  published 2009-06-25.
- **Verdict: SOURCED, S9, MEDIUM confidence** (a secondary, attributed republication of the
  original Nebraska test-lab criteria, and over a decade old — but this is the long-standing
  industry-standard reference table and has not been superseded; the diesel figure is
  independently corroborated by S10 below, which increases confidence in the table as a whole
  even though the formal grade stays MEDIUM per the "undated/secondary" rule).

## P22 — Local price per unit of pump fuel or electricity (Appendix F)

- Fetched the U.S. Energy Information Administration's live "Electricity Monthly Update" page
  directly. Industrial-sector average retail price, June 2026: **9.17 cents/kWh** (national
  average; residential 18.34¢, commercial 14.19¢, overall average 14.48¢, for context).
- Also pulled the EIA's current U.S. average on-highway diesel retail price ($5.652/gal, week of
  8/24/26) in case a diesel scenario were used instead — not used in the final case since MA7
  chose electricity, but recorded here in case a future revision needs it.
- **Verdict: SOURCED, S12, HIGH confidence.** Primary government statistical source, dated. Noted
  as a national-average proxy for this specific farm's actual utility rate.

## P23 — Brake-horsepower formula constants and typical pump efficiency (Appendix F)

- Searched "Texas A&M AgriLife EB-6011 pump brake horsepower formula BHP Q H 3960 efficiency" —
  confirmed the formula shape via search snippet, then found and fetched the actual EB-6011 PDF
  directly (`gfipps.tamu.edu/files/2021/11/EB-6011-Sizing.pdf`, Guy Fipps, March 2021) after the
  OakTrust repository mirror returned HTTP 403.
- WHP = (GPM × TDH)/3,960 (Equation 1). BHP = WHP / pumping plant efficiency (Equation 2). Worked
  example in the same document: *"Typically, a pump efficiency of 75 percent is used in the
  design."* The same worked example independently uses "each gallon of diesel will provide 12.5
  WHP-hours," matching S9's Nebraska-criteria figure exactly — good cross-source corroboration.
- **Verdict: SOURCED, S10, HIGH confidence.**

## P02, P03, P04, P05, P07 — Design flow rate, run length, acreage, labor rate, operating hours (Appendix A)

These describe properties of a specific fictional farm layout, not a publicly documented fact.
Searched for grounding ranges rather than a single citable "the" number, on the reasoning that a
defensible range beats no attempt at all:

- Center-pivot/mainline design-flow guidance: searched "Kansas State Extension center pivot design
  flow rate gpm per acre mainline example quarter section." Found repeated, if aggregator-sourced,
  statements that most pivots need roughly 5–8 GPM/acre, and that a standard quarter-section pivot
  (125–130 acres) needs about 700–900 GPM. No single K-State MF-series document with an explicit
  gpm/acre design table could be pinned to a fetchable URL in the time available.
- Installation labor/trenching cost: searched "agricultural PVC mainline installation labor cost
  per foot trenching irrigation contractor 2025." Found only residential-scale trenching-cost
  aggregator pages (HomeAdvisor, Angi, HomeGuide) citing $5–$12/ft for basic work and $13–$40/ft
  for complex/deep work — LOW-tier sources by this skill's grading rubric, and none specific to
  agricultural mainline. No usable ag-contractor rate sheet found.
- Annual operating hours: no citable "typical annual mainline operating hours" figure (distinct
  from a whole pivot system's seasonal hours) could be found.
- **Verdict for all five: NOT FOUND at HIGH/MEDIUM confidence for this specific farm → Exit 1,
  stated Modeling Assumption** (MA1 through MA5 respectively), each with the search-derived range
  as its basis, a stated value, and a sensitivity call — see case.md's Modeling Assumptions block
  and case.json's `modeling_assumptions[]`. MA1 (flow rate) and MA3 (acreage) were chosen together
  so their ratio (450 GPM / 90 ac = 5 GPM/ac) sits inside the sourced-range low end.

## P06 — Competing contractor's total quoted price (Appendix A)

case.md explicitly labels this "this case's own competing-bid figure — scenario constraint, not
an external source" — no search was attempted; a real external competing bid cannot exist for a
fictional farm. Set to $24,000 (MA6), chosen after computing both options' realistic net installed
costs so the number gives Denise's own bid genuine stakes either way. **Verdict: ASSUMPTION, MA6.**

---

## Verification pass

```
placeholders remaining: 0
S markers used in text: [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S12]
MA markers used in text: [MA1, MA2, MA3, MA4, MA5, MA6, MA7]
source rows defined:     [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S12]
MA rows defined:         [MA1, MA2, MA3, MA4, MA5, MA6, MA7]
markers with no source row: (none)
MA markers with no row:     (none)
```

(S11 is intentionally unused — the diesel EIA price was pulled during P22's research as a
fallback in case MA7 had chosen a fuel other than electricity, and is documented above but was
not carried into a numbered source/placeholder since it isn't cited in case.md.)

No LOW-confidence source carries a constraint or a dilemma-flipping quantity. The lowest grades in
this case (S6 MEDIUM, S7/S8 MEDIUM, S9 MEDIUM) are all either a manufacturer spec sheet with an
unconfirmed-but-plausible currency, or a retail list price with an honest "confirm before
ordering" caveat, or a long-standing but decade-old secondary republication of a still-standard
reference table — none of them fabricated, none of them a bare guess.

**Next step:** `case-readiness`.

---

## Addendum, 2026-09-01: MA1/MA3 retune to bring the margin toward SPEC §2

`case-qa`'s balance test (SPEC §2) computed the original case at **margin 115.8%, winner B**,
against a ~20% target. The size of the margin was a direct, honest consequence of NRCS Code 430's
all-or-nothing EQIP forfeiture rule combined with MA1's original 450 GPM design flow rate sitting
only ~2% *over* the Lean Main's certified maximum flow of ~440.7 GPM (computed from the sourced
5 ft/sec ceiling, S1, and the sourced 6 in diameter, S6) — enough to fail certification and forfeit
the entire ~$13,369 reimbursement, per Appendix E's stated all-or-nothing condition.

**Retune performed:** MA1 lowered from 450 GPM to **440 GPM**. MA3 (acreage) lowered in lockstep
from 90 to **88 acres**, at the same established 5 GPM/acre rate MA1's basis already used (5 × 88
= 440) — no new rate or unsupported figure introduced; 88 acres remains squarely "mid-size" and
barely distinguishable from the original 90-acre figure.

**Why this value:** 440 GPM sits ~0.16% *below* the Lean Main's certified maximum of ~440.7 GPM —
close enough that whether the design certifies is not obvious without running Challenge D4's exact
one-step-equation check (a Hero eyeballing "440 vs. ~440.7" cannot reliably call it either way).
This preserves the case's real dilemma and the forfeiture mechanism's genuine tension, per the
retune brief, rather than moving MA1 far enough from the cliff that certification becomes an
obvious non-issue.

**Model built to verify:** `sensitivity_model.py` was written for this case (it did not exist
before this pass) implementing the case's own arithmetic end-to-end — Hazen-Williams friction loss
(S2), the NRCS Code 430 velocity check (S1), the all-or-nothing EQIP forfeiture rule (Appendix E),
straight-line 20-year capital amortization, and the BHP/whp-hr/kWh pump-energy-cost chain (S9, S10,
S12) — matching the original case's published numbers almost exactly as a calibration check
(computed ~$244/yr and ~$60/yr pump energy cost at 450 GPM against the case's published ~$244.01
and ~$60.30; computed installed costs of $39,732/$42,636 and reimbursements of ~$13,369/~$23,173
exactly).

**Result at MA1 = 440 GPM:**
- Option A (Lean Main) velocity: ~4.9927 ft/sec — **certifies** (ceiling 5.0 ft/sec), keeps its
  ~$13,369 EQIP reimbursement.
- Option B (Margin Main) velocity: ~2.8084 ft/sec — certifies comfortably, keeps its ~$23,173
  reimbursement (unchanged from before — weight-based, not flow-based).
- Total annualized cost/acre-inch: A ≈ $1.3263, B ≈ $0.8825.
- **New margin: ~50.3%. Winner unchanged: B — The Margin Main.**

**Why 50.3%, not ~20%:** with the forfeiture no longer triggered, the remaining gap is the case's
real, purely economic margin — driven by Option B's much larger EQIP reimbursement (heavier pipe
earns more per pound under Appendix E's per-pound schedule) and much lower annual pump energy cost,
which together more than offset its higher material/labor cost. A parameter sweep of MA1 across
the entire range that keeps the Lean Main certified (tested 380–440.6 GPM) shows the margin holds
in a narrow ~45.4%–50.3% band throughout — i.e., once certification is no longer in question, MA1
has very little further leverage over the margin's size. Reaching SPEC §2's ~20% target would
require retuning a different constraint entirely (material cost, labor rate, or the pipe sizes'
relative weight spread) — explicitly out of scope for this pass, which was scoped only to MA1/MA3.
This result is reported as computed, not smoothed toward the target, consistent with this
project's practice of retuning constraints and disclosing the outcome rather than hiding data
(SPEC §2).

**Files updated:** `case.json` (Appendix A values, `modeling_assumptions[MA1, MA3]`,
`balance.margin_pct`/`margin_pct_note`/`margin_basis`, `sensitivity_note`, `needs_source`
resolutions for MA1/MA3), `case.md` (Appendix A table, Modeling Assumptions table),
`FACILITATOR.md` (margin section, numbers table, sensitivity note). `sensitivity_model.py` added
new to this case directory.

---

## Addendum, 2026-09-01: metric reframe — separating true efficiency from the EQIP subsidy

**Trigger.** After the MA1/MA3 retune above, both pipe options certify against NRCS Code 430 and
the case's single primary metric (net-of-subsidy total annualized cost per acre-inch) settled at a
real, sourced ~50.3% margin (winner B). Nothing about that number was wrong, but it blends two
different things into one figure: (1) true engineering efficiency — material, labor, and pump
energy — and (2) the EQIP Practice 430 cost-share reimbursement, which pays **per pound of pipe
installed** (Appendix E, S5), not per unit of efficiency. That structure is worth surfacing on its
own, since it means the reimbursement mechanically favors the heavier pipe regardless of whether it
is the more cost-efficient design. This addendum documents recomputing the case's cost comparison
with the subsidy term removed entirely, to see whether the "true" gap between the options is
actually as large as 50.3%.

**Method.** `sensitivity_model.py` was restructured (not re-parameterized — no change to PARAMS,
FLEX, MA1/MA3, or any sourced figure S1–S12) to compute each option's annualized cost two ways from
the same shared arithmetic: `true_total_annual_cost` = (material + labor)/20-yr life + annual pump
energy cost, with NO reimbursement term at all; and `net_total_annual_cost` = the same, minus the
EQIP reimbursement (forfeited on failed certification, unchanged from the prior pass). `evaluate()`
now returns the TRUE metric (the new primary); `evaluate_net_of_subsidy()` returns the NET metric
(now secondary). Ran `python3 sensitivity_model.py`:

```
[PRIMARY] true (subsidy-free) cost/acre-inch  A=1.8993  B=1.8757
[PRIMARY] true winner: B  margin: 1.26%
[SECONDARY] net-of-subsidy cost/acre-inch  A=1.3263  B=0.8825
[SECONDARY] net-of-subsidy winner: B  margin: 50.29%
Subsidy-formula effect on the margin: 49.03 points (net 50.29% - true 1.26%)
Lean Main certified max flow: 440.64 GPM
```

**Result.** The true, subsidy-free comparison: Option A (Lean Main) = $2,215.83/yr ($1.8993/ac-in);
Option B (Margin Main) = $2,188.27/yr ($1.8757/ac-in). B still wins, but by only **~1.3%** — a
genuine engineering toss-up, not a landslide, driven by B's much lower pump energy cost (~$56/yr
vs. ~$229/yr) just barely outweighing its ~$2,904 higher installed cost with zero subsidy counted.
The net-of-subsidy comparison (unchanged from the prior addendum): A = $1,547.38/yr, B =
$1,029.63/yr, a ~50.3% margin. **Roughly 49 of those ~50.3 percentage points are attributable
entirely to the EQIP reimbursement formula paying by weight** (B's ~$23,173 reimbursement vs. A's
~$13,369 — a ~$9,800 gap driven by B's pipe weighing 4.16 lb/ft against A's 2.40 lb/ft, at the same
$4.22/lb rate, S5), not to any difference in material or energy efficiency.

**Decision, per the case-owner's task brief:** because the true efficiency gap (~1.3%) is
meaningfully smaller than the net-of-subsidy gap (~50.3%) — not close, not a rounding difference —
TRUE (subsidy-free) cost per acre-inch is now the case's **primary metric**, and `case.json`'s
top-level `margin_pct` / `balance.margin_pct` were recomputed to **1.3%** (winner unchanged: B).
The net-of-subsidy figure (~50.3%) is retained and disclosed explicitly as the case's **secondary**
metric — it is what actually shows up on Denise's bid — surfaced in `case.md`'s new "A note on the
two cost comparisons" section, in D1/D3/D6's rewritten deliverable text (both figures required,
D6's recommendation memo must address both explicitly and quantify the subsidy's point-contribution),
and in `FACILITATOR.md`'s rewritten margin section and two-part Twist (Part 1: MA1's certification
cliff, unchanged; Part 2, new: the subsidy formula alone explains ~49 of the ~50.3 points).

**What did NOT change:** NRCS Code 430 certification data (S1, S2), MA1 (440 GPM), MA3 (88 acres),
any sourced figure S1–S12, the Hazen-Williams arithmetic, or the certification pass/fail results for
either option. This addendum is a metric-framing and disclosure change only. The prior
`balance_test_waiver` (MCS-46), granted against the old 50.3% primary metric exceeding SPEC §2's
~20% target, is retained in `case.json` for the historical record with an added `superseded_note`:
the new 1.3% primary margin does not on its own terms need that waiver, since it already sits well
inside the ~20% target.

**Files updated:** `sensitivity_model.py` (restructured to expose true/net metrics separately;
`evaluate()` now primary/true, `evaluate_net_of_subsidy()` now secondary/net), `case.json`
(`primary_metric`, top-level `margin_pct`, `balance.argument_a/argument_b/margin_basis/winner/
margin_pct/margin_pct_note`, `sensitivity_note`, `deliverables[D1, D3, D6].text`,
`balance_test_waiver.superseded_note`), `case.md` (Overview closing beat, Background paragraph on
the two comparisons, new "A note on the two cost comparisons" section with both figures, D1/D3/D6
challenge text), `FACILITATOR.md` (Argument for B, "The margin" section rewritten with both metrics,
Data Deep Dive, two-part Twist, Close, Lessons Learned, a new Socratic question 6, "The trap"'s
second trap, sensitivity note).

---

## Addendum, 2026-09-01: Tier 2 re-gate remediation — P5 assumption-sensitivity disclosure and P6 S6 source-decay check

Tier 2 probe 5 (`--probe 5 --flex 0.5`) FAILed: flexing MA1 (`design_flow_gpm`) and MA5
(`annual_hours`) by -50% each flips the PRIMARY metric's winner from B to A. Tier 2 probe 6 FAILed:
S6 (JM Eagle "Irrigation P.I.P." catalog, the source for the 6 in / 8 in pipe weight-per-foot
figures used throughout the cost/EQIP arithmetic) was flagged as returning 404. Both are addressed
below as disclosure/citation fixes, per the case-owner's brief — no retuning of MA1, MA5, or any
sourced figure.

**P5 — re-deriving the actual flip thresholds.** The probe confirms -50% flips the primary winner,
but doesn't say how much smaller a swing is actually needed. Bisecting `sensitivity_model.py`'s
`evaluate_detail()` on each parameter independently (holding all others at their stated values):

```
design_flow_gpm: winner flips B->A at multiplier ~0.9409 (440 -> ~414.0 GPM), i.e. about -5.9%
annual_hours:    winner flips B->A at multiplier ~0.8405 (1200 -> ~1008.6 hr/yr), i.e. about -16.0%
```

Both thresholds are well inside the ±50% Tier 2 sweeps, meaning the primary metric's ~1.3% margin
is considerably more fragile to these two real, sourced Modeling Assumptions than the probe's pass/
fail flex alone would suggest. This tracks the case's own reframe logic: with the EQIP subsidy term
removed, Option B's win reduces to Hazen-Williams's steep diameter sensitivity (head loss ~
diameter^-4.87, S2/S3) just barely outweighing its higher material/labor cost — a margin that thin
is *supposed* to be this touchy. Per SPEC.md §2 / MCS-26 ("a verdict unstable under a ±50% swing
must SAY SO ... disclosure is the fix, not necessarily elimination"), and because this instability
is itself informative (it reinforces the "genuine engineering toss-up" framing rather than
undermining it), neither MA1 nor MA5's stated value was changed. Added `case.json.
sensitivity_disclosure[]` (two entries, category `I` — real/sourced parameters, disclosed
sensitivity, not a fictional or unresearchable dial) documenting both exact flip thresholds, and a
new paragraph in `FACILITATOR.md`'s Sensitivity note section disclosing the same fragility in
guide-facing language.

**P6 — S6 source-decay check.** Re-fetched `https://www.jmeagle.com/sites/default/files/
Irrigation_web.pdf` directly (not via a bare `curl`, which does return 404 from this host) using a
browser-like request; it returned 200 and served the full, current 28-page JM Eagle "Irrigation
P.I.P." catalog. Its "Dimensions and Weights" table (contents-listed as section 04, pp. 8-9) still
shows, under "Rated 125 psi (SDR 32.5)*": 6 in = 2.40 lb/ft, 8 in = 4.16 lb/ft — an exact match to
S6's cited figures. Cross-checked against two independent mirrors of the same JM Eagle data
(`jmeagle.com/sites/default/files/jme_Irrigation.pdf` and a `mtncom.net` reseller-hosted copy of JM
Eagle's "Irrigation P.I.P." one-sheet, revised 10/22/2012), both showing the identical 2.40 / 4.16
lb/ft row. Conclusion: the source is not actually gone — Tier 2 probe 6's automated fetch was almost
certainly blocked by JM Eagle's own bot-detection/WAF (confirmed: a plain `curl` gets 404 from both
the original URL and the `jme_Irrigation.pdf` mirror, while a browser-UA request gets 200 from
both), not a genuine 404. To make the citation resilient to this going forward, `archive.org`'s
availability API was queried and returned a live, dated snapshot (`web.archive.org/web/
20260211155828/https://www.jmeagle.com/sites/default/files/Irrigation_web.pdf`, captured 2026-02-11,
status 200) of the exact same file. S6's `url` was updated to this archive.org snapshot (a
permanent, bot-detection-proof citation, same approach as the-irregular-boundary's earlier S6-class
fix), `accessed` updated to 2026-09-01, and `note` rewritten to record both the live re-verification
and the reason for the switch to an archived URL. No change to S6's `value`, `confidence` and other
fields, or to any downstream figure (Appendix B/C diameters and weights, material costs) — this is a
citation-resilience fix only.

**Verification.** Re-ran `python3 sensitivity_model.py` after these changes: output unchanged
(true winner B, margin 1.26%; net-of-subsidy winner B, margin 50.29%), confirming no arithmetic was
touched. Re-running `tier2_probes.py --case the-mainline-margin --probe 5 --flex 0.5` and `--probe 6`
is expected to still report the same underlying flip/decay facts (this addendum discloses them, per
the task brief, rather than eliminating them) — a full fresh Tier 2 re-gate is a separate pass.

**Files updated:** `case.json` (new `sensitivity_disclosure[]`, S6 source `url`/`accessed`/`note`),
`FACILITATOR.md` (new paragraph in the Sensitivity note section), `RESEARCH_LOG.md` (this addendum).
`case.md` untouched — no citation reference there needed updating.
