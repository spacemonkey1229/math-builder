# Research Log — The Dosing Curve

30 `{{NEEDS_SOURCE}}` placeholders. 28 SOURCED, 2 ASSUMPTION (both anticipated by the case-write
concept research), 0 DROPPED, 0 OPEN.

## Background / Appendix D — product labels

| Placeholder | Searched | Found | Rejected / caveats |
|---|---|---|---|
| Liquamycin LA-200 single-dose rate, mg/lb | "Liquamycin LA-200 FDA label dosage DailyMed" | DailyMed label (setid d14180ed…): 9 mg/lb single IM/SC dose, "as effective as 2 or 3 repeated daily treatments at 3-5 mg/lb" — S4, HIGH | The label's PDF export was binary/unparseable by direct fetch; the HTML `drugInfo.cfm` page fetched cleanly instead and was used as the actual `url`. |
| Liquamycin LA-200 dosing frequency | same | Single injection (or the alternative repeated 3-5 mg/lb/day regimen, not used here) — S4 | — |
| Liquamycin LA-200 withdrawal period | same | 28 days, cattle and swine — S4 | — |
| Conventional oxytetracycline daily rate / max days | Searched several conventional-formulation labels (Terra-Vet 200, Agrimycin 200, Oxytetracycline 200); fetched DailyMed setid 2846dab1 (OXYTETRACYCLINE 200) | 3-5 mg/lb/day, once daily, not to exceed 4 consecutive days — S5, HIGH | Multiple generic 200 mg/mL products exist (Terra-Vet 200, Agrimycin 200, Vetrimycin 200, Oxytetracycline 200); confirmed via direct fetch that this specific DailyMed label's dosing text is the conventional (non-LA) regimen, not a second LA product also badged "200." |
| Conventional withdrawal period | same | 28 days, cattle — S5 | Identical to LA-200's 28 days, matching the case's own assertion that withdrawal doesn't distinguish the options. |

## Appendix A — Aktaş & Yarsan 2017 PK parameters

Direct-fetched the paper via its DOI redirect chain (doi.org → journal.frontiersin.org →
www.frontiersin.org/article/10.3389/fvets.2017.00229/full). All 10 placeholders (Cmax, Tmax,
half-life, AUC, bioavailability, x2 formulations) resolved from Table 1 of the paper in a single
fetch: Cmax 13.57±5.83 / 8.72±2.47 μg/mL; Tmax 0.46±0.09 / 0.60±0.28 h; t½ 10.47±1.30 / 27.96±11.66
h; AUC 80.21±12.71 / 87.35±10.91 μg·h/mL; F 69.71% / 83.15% (conventional / long-acting). Values
matched exactly what the task brief already anticipated from prior concept research — no
discrepancy to reconcile. Confidence: HIGH. Caveat recorded in S1's note and flagged in the
margin_note: the study dose (20 mg/kg IM, goats) differs from this case's cattle scenario in both
species and, for the conventional regimen, dose magnitude relative to the FDA label.

## Appendix B — sampled concentration-time curve (the flagged open gap)

Explicitly asked the fetch: "is there a digitized concentration-vs-time table with sampled
timepoints, or only summary statistics?" Answer, confirmed directly from the paper: only summary
statistics (Table 1) plus a plotted Figure 1; blood was sampled at 13 real timepoints (0.25, 0.5,
1, 2, 4, 8, 12, 24, 36, 48, 60, 72, 96 h) but no table of individual paired readings was ever
published. This matches the gap the case-write concept research had already flagged.

**Rejected approach:** tried building a reconstruction anchored simultaneously to Cmax, Tmax, AND
mean AUC using a standard one-compartment first-order-absorption (Bateman) model. Found this
over-constrained: solving for the absorption rate constant from Tmax and the elimination rate
constant from half-life, then requiring the model's peak to equal the reported mean Cmax, implies
a total AUC roughly 2.6x (conventional) to 2.5x (long-acting) higher than the paper's own reported
mean AUC. This is a real, informative finding — it means four averaged summary statistics from
different animals cannot be forced to describe one single "mean" curve without contradiction, a
known artifact of naive parameter-averaging across nonlinear PK models — not a fetch error.

**Accepted approach (MA1):** anchored the reconstruction to the real half-life (elimination rate)
and real mean AUC (total curve area, since AUC is the quantity the case's calculus deliverables
actually revolve around), chose the absorption rate to match the real Tmax as closely as algebra
allows, and disclosed that the resulting model's own implied Cmax (≈5.15 μg/mL conventional,
≈2.13 μg/mL long-acting) undershoots the real reported Cmax. Sampled the resulting curve at the
paper's own real 13 timepoints and placed the result in case.md's Appendix B, clearly labeled
"modeled," not real data, per SPEC §5's rule against burying an unsourced number in a table.

## Appendix C — Winter et al. 2024 PK/PD target and CLSI breakpoint

Direct-fetched PMC11652485 (Winter et al., Frontiers in Microbiology 2024). Confirmed target
fAUC24h/MIC range 19.1 h (M. haemolytica, serum, per Lees et al. 2018) to 28.0 h (P. multocida,
serum, per Lees et al. 2018), with 23.2 h also reported in broth (Brentnall et al. 2013) —
authors fixed their own working target at 24 h for a 24-h dosing interval. PK/PD cutoff
concentrations: 1 mg/L (calves), 2 mg/L (adult cattle), for a long-acting 20 mg/kg / 48-h-interval
regimen at the 90th-percentile population-target-attainment level. Confidence HIGH — this is the
paper's own headline finding, directly fetched, not a secondary summary.

**Caveat, not resolved by case-research:** these cutoffs were derived specifically for a
48-hour-dosing-interval long-acting regimen. Applying them unmodified to this case's conventional
24-hour-interval regimen, or to a long-acting dose (9 mg/lb) different from the 20 mg/kg the paper
modeled, is an extrapolation. Flagged in case.json's S2 note and in the margin_note rather than
silently treated as directly transferable.

CLSI VET01S breakpoint (susceptible ≤2 mg/L, resistant ≥8 mg/L): the primary CLSI standard itself
is a paywalled/binary PDF (two different CLSI-adjacent PDFs — a University of Guelph AHL lab note
and the CLSI correction-notice document — were fetched and both returned as unparseable
binary/font-stream content, not extractable text). Corroborated instead via a secondary source (an
EMA "antibiotic clinical breakpoints" Q&A document referencing the CLSI table) plus an independent
search-summary corroboration citing the same ≤2 / ≥8 mg/L values. Graded MEDIUM, not HIGH, because
the primary standard's own table was never directly read — this is a deliberate downgrade per the
grading rubric, not an oversight.

## Appendix D note — 1983 tissue-damage study

Located and confirmed PMID 6869141 (Xia, Nielsen, Gyrd-Hansen, *Acta Vet Scand* 1983) by name
search rather than a direct fetch of the paywalled full text; the PubMed abstract itself gave the
needed quantitative/qualitative claim directly (plasma >0.5 μg/mL maintained ~60h by either
preparation after 20 mg/kg IM; pronounced injection-site tissue damage 1-2 weeks post-LA-injection
vs. minimal irritation from the conventional preparation). Old (1983), small n (4 cows), but a
real, dated, unambiguous, directly-relevant source matching the concept research's named citation.
Confidence HIGH for the qualitative/comparative claim; not used as a load-bearing numeric input.

## Appendix E — pricing and lesion economics

**Per-dose pricing (the second flagged open gap).** Concept research had already found no current
price-differential figure. Re-searched as instructed. Rejected sources, in order:
- Valley Vet Supply product pages: returned HTTP 403 on direct fetch (bot-blocked), so no price
  could be confirmed from that retailer despite search results suggesting it stocks both products.
- Muleshoe Vet Supply's "Oxytetracycline Inj 200 (500ML)" at $51.27: fetched successfully, but the
  product page's own description does not state whether this specific listing is the conventional
  or a long-acting formulation — rejected as ambiguous rather than assumed.
- Tractor Supply Co product pages: repeated fetch timeouts (60s), abandoned after two attempts.
- Jeffers Pet LA-200 250cc product URL: 404, page structure had changed since indexing.

**Accepted:** EntirelyPets Rx, because it carries clearly-labeled, distinctly-named products for
both formulations at the same bottle size (500 mL) from the same retailer, letting the case use an
apples-to-apples comparison rather than mixing retailers with different markups: "VetOne Vetrimycin
200" (explicitly described on its own page as a conventional, non-LA 200 mg/mL solution) at
$57.99 list / $43.99 sale, and "Liquamycin LA-200" at $159.99 list / $132.92 sale. Graded MEDIUM:
retail/consumer online-pharmacy pricing, not a wholesale distributor or in-clinic acquisition
price, and the "sale" pricing is promotional and will drift. Converting this per-mL price into a
per-dose price required two further Modeling Assumptions (MA3: representative 500 lb animal; MA4:
a specific rate, 4 mg/lb/day, from the conventional label's 3-5 mg/lb/day range) since neither a
body weight nor a single point-dose is stated anywhere else in the case.

**Injection-site-lesion cost and incidence.** The classic $7.05/head (1995 NBQA) figure, sourced
via ND State University Extension's BQA page (S8, MEDIUM — the 1995 original audit report itself
was not directly located online, only this clearly-attributed republication). For "most recent
edition" incidence, per the task's explicit instruction to get both 1995 and 2022 figures: found
NBQA-2022 reports 2.9% (market cows/bulls, confirmed by direct fetch of the peer-reviewed primary
paper, *Translational Animal Science* txae178, HIGH for that specific segment) and 0.2% (fed
steers/heifers — the segment actually relevant to this case's stocker/feeder cattle — confirmed
only via the ND State Extension secondary citation, not independently verified in the primary
paper txaf150's own fetched text, which discusses the metric being recorded but did not surface
the number on direct fetch). Used the fed-cattle 0.2% figure in case.md as the "most recent survey"
row since it is the segment matching this case's cattle type; noted the market-cow/bull 2.9% figure
in case.json's S9 note as corroboration of comparable order of magnitude.

**Operation's fixed per-head budget cap.** No public figure can exist for this fictional
operation's specific budget — recognized immediately as an Exit-1 (stated Modeling Assumption)
case, not a NOT-FOUND-after-search case. To avoid picking an arbitrary number, searched for a real
benchmark to ground the assumption: USDA APHIS NAHMS Feedlot survey direct BRD treatment cost,
found at ~$23.60/case via a trade-press summary (S10, MEDIUM — located via search summary, not a
directly fetched primary NAHMS report). Set MA5's stated value at $25/head, close to that real
figure rather than picked freehand.

## Margin computation (facilitator-only; full detail in FACILITATOR.md and case.json balance object)

Computed margin_pct = 29.7%, winning option B (Four-Day Course) on the cost tie-breaker, using
real sourced prices (S7), the stated body-weight and dosing-rate assumptions (MA3, MA4), and the
lesion-cost/incidence data (S8, S9). This exceeds the ~20% SPEC §2 threshold and is reported
plainly rather than softened. Separately and more importantly: attempting the PRIMARY fAUC/MIC
pass/fail gate computation (the case's actual decisive metric, per its own margin_basis) using the
real Appendix A/C parameters under a simple one-compartment/superposition model found the outcome
genuinely sensitive to (a) which point in the conventional label's dosing range is used, (b)
whether the CLSI clinical breakpoint or Winter et al.'s PK/PD-modeled cutoff is used as the MIC
denominator, and (c) whether every 24-h window or only the course-level cumulative total must
clear the target. This is not a NOT-FOUND situation — real, sourced numbers were used throughout —
but it is not case-research's place to hand-pick a winner on the case's primary axis when the real
literature itself does not cleanly settle it for this specific dose/interval combination. Flagged
for case-qa / a human judgment call, following the fret-board precedent.

## Retune (case-qa stage, 2026-09-01) — cost tie-breaker only

The 29.7% cost-tiebreaker margin exceeds SPEC §2's ~20% balance-test cap. The PRIMARY fAUC/MIC
efficacy gate above is an explicit, deliberate human-judgment-call disclosure and was left
untouched.

The cost margin is driven by MA3 (500 lb animal, unchanged — cancels out in the cost ratio per its
own sensitivity note), S7's real list pricing (unchanged, both list prices from the same
retailer/bottle size), and MA4 (the conventional dosing rate used to price the Four-Day Course).
MA4 was originally set at 4 mg/lb/day, the midpoint of the conventional label's real, sourced 3-5
mg/lb/day range [S5]. MA4's own pre-existing sensitivity note already flagged that course drug cost
moves ±25% at the range's ends — so the retune moves MA4 to **5 mg/lb/day, the range's upper end**,
still the same real FDA-label figure [S5], not a new or fabricated number.

Recomputed: Four-Day Course drug cost = 12.5 mL/day (2500 mg/day ÷ 200 mg/mL) × $0.11598/mL × 4
days = $5.799 (was $4.64 at 4 mg/lb/day). Lesion cost is unchanged (still 4 handling events ×
~$0.128/event ≈ $0.51, since handling-event count doesn't depend on MA4). Four-Day Course total =
$6.312 (was $5.153). Single Shot total is unchanged at $7.328 (MA4 doesn't affect it).

New margin_pct = 100 × (7.328 − 6.312) / 7.328 = **13.9%**. Option B (Four-Day Course) still wins
on cost, now under the SPEC §2 cap. Winner did not flip — reported honestly either way per
instructions. Updated case.json (`margin_pct`, `balance.margin_pct`, `balance.margin_note`),
case.md (MA4 row, Appendix E table and per-dose-price note), and FACILITATOR.md's margin section
to match. No sensitivity_model.py exists for this case (unlike some other cases in this pipeline);
computation was done and cross-checked by hand, matching the arithmetic FACILITATOR.md itself had
already anticipated ("only drops to ~14% at the range's upper end (5 mg/lb/day)").

## Addendum (case-readiness stage, 2026-09-01) — primary gate restructured into an explicit D5 convention table

A prior case-readiness pass (documented only in `case.json.derived.primary_gate_resolution` and
FACILITATOR.md, not in this log) tried to force the primary fAUC/MIC gate above to a single verdict
("both options pass") by reading the Four-Day Course's day-1 AUC directly off Appendix B's modeled
curve (64.7 μg·h/mL) and treating the calves MIC benchmark as case-dictated. Revisited per
instructions to turn the genuine, already-documented ambiguity above (which dosing point, which
MIC benchmark, window-vs-course-total) into an explicit, calculable student deliverable instead of
either an open-ended discussion prompt or a single hand-picked verdict. Two problems found on
recheck of that prior resolution:

1. **Unscaled dose.** Appendix B's modeled curve (MA1) was built at Aktaş & Yarsan 2017's real
   study dose, 20 mg/kg IM ≈ 9.07 mg/lb [S1] — not at the conventional label's actual 3-5 mg/lb/day
   dosing rate [S5]. Reading 64.7 μg·h/mL off that curve compares the label's real dose against a
   target using an exposure computed at roughly double the label's actual dose. Since linear PK is
   already assumed throughout this case (MA2), AUC scales linearly with dose: rescaling 64.7 by
   (label dose ÷ 9.07 mg/lb) gives **21.4 μg·h/mL at 3 mg/lb/day** and **35.7 μg·h/mL at 5
   mg/lb/day**, for a single day, before any multi-dose accumulation.
2. **One MIC benchmark silently preferred.** The prior pass dismissed the CLSI VET01S breakpoint
   (≤2 mg/L [S3]) and Winter et al.'s own adult-cattle cutoff (2 mg/L [S2], numerically identical
   to CLSI here) as inapplicable, on the grounds that the case's stated population is calves. Both
   are real, cited benchmarks a reviewer could reasonably invoke — the CLSI breakpoint in
   particular is a population-independent clinical standard, not itself age-split — so both are
   carried forward here as genuine alternatives, not one silently preferred over the other.

Also computed the "course-cumulative" window convention using the standard linear-PK multi-dose
accumulation factor R = 1/(1 − e^(−ke·τ)), ke = ln(2)/half-life, with the conventional
formulation's real half-life (10.47 h [S1]) and the 24-h dosing interval: R ≈ 1.257. This gives
**26.9 μg·h/mL (3 mg/lb/day)** and **44.8 μg·h/mL (5 mg/lb/day)** as the accumulated steady-state
daily-AUC reading — a real, standard PK formula, consistent with MA2 (already a disclosed modeling
assumption in this case), not a fitted or fabricated number.

Full corrected table (Four-Day Course, 2 dosing points × 2 window conventions; Single Shot needs
neither axis — its 9 mg/lb label dose [S4] already ≈ the 9.07 mg/lb study dose and it is one
continuous injection):

| Option | Dose | Window | AUC0-24h (μg·h/mL) | Calves target (24) | CLSI/adult-cattle target (48) |
|---|---|---|---|---|---|
| Single Shot | 9 mg/lb (fixed) | n/a | 39.1 | PASS | FAIL |
| Four-Day Course | 3 mg/lb/day | Day-1-only | 21.4 | FAIL | FAIL |
| Four-Day Course | 3 mg/lb/day | Course-cumulative | 26.9 | PASS | FAIL |
| Four-Day Course | 5 mg/lb/day | Day-1-only | 35.7 | PASS | FAIL |
| Four-Day Course | 5 mg/lb/day | Course-cumulative | 44.8 | PASS | FAIL (close) |

## Addendum (case-readiness stage, 2026-09-01) — Tier 2 remediation: trap, twist pacing, S9 citation

Case-readiness Tier 2 probes P3, P4, and P6 all FAILed on a fresh readiness pass; the trigger for
this addendum. Three independent fixes, none of which change `margin_pct` (13.9%, unchanged):

**P3 — trap mismatch (FACILITATOR.md).** A fresh, blind subagent solving from the student packet
alone independently hit the exact dose-rescaling error this project's own earlier case-authoring
pass had already made and corrected (see the addendum above,
`case.json.derived.primary_gate_resolution.note_on_prior_resolution`): reading the Four-Day
Course's AUC off Appendix B's curve without rescaling off its ~9.07 mg/lb study dose down to the
label's real 3-5 mg/lb/day rate. FACILITATOR.md's "The trap" section, however, only named the
Appendix A single-dose-comparison trap, not this one. Fixed by rewriting "The trap" into two named
traps: Trap 1 (the dose-rescaling error, flagged as empirically demonstrated, both by the blind
solve and by the project's own prior mistake) and Trap 2 (the pre-existing Appendix A trap, kept —
it is real and still worth watching for). No case.md change needed; this is facilitator-guide-only.

**P4 — twist pacing (FACILITATOR.md).** The Data Deep Dive section's script had the facilitator
build D5's table "against both MIC benchmarks" and "let the room see the table flip" — i.e., reveal
that a second (CLSI/adult-cattle) MIC benchmark exists and that switching to it flips every cell to
FAIL, all before the scripted Twist beat at 25:00 that is supposed to be the moment this exact
reveal lands. By the time the Twist beat arrived, there was nothing left to reveal. Fixed by
restructuring the Data Deep Dive to build D5's table using only the calves benchmark (the one a
Hero reaches for by default, matching the case's own stated population) and explicitly instructing
the facilitator not to mention the second benchmark yet; the 45-Minute Socratic Plan table's
matching row was updated to match. The Twist section itself (already correct) is unchanged — it
still delivers the full population-specific-cutoff reveal and the "every cell flips to FAIL" beat.
This is purely a guide-pacing fix; case.md's own D5/Appendix G (which students read on their own
schedule) already presented both benchmarks together, and still does — nothing in the student
packet changed.

**P6 — S9 citation (case.json, case.md).** S9 claimed a 0.2% (99.8%-lesion-free) fed-cattle
injection-site-lesion incidence figure, cited to the ND State University Extension "Injections"
page, with a companion cite to the peer-reviewed *Translational Animal Science* txaf150 paper.
Direct re-fetch of the ND State page (both via a summarizing fetch and a raw-HTML grep for "0.2"
and "99.8") confirms it contains only the 1995 11%/$7.05 figures — no 2022 or 0.2%/99.8% figure
appears anywhere on that page. Direct re-fetch of txaf150 (via its Oxford Academic HTML page) also
confirms its Materials and Methods section states lesion presence/absence was recorded on the 2022
fed-cattle audit, but no percentage appears in its Results/Discussion text or any table surfaced by
fetch. This figure was genuinely mis-cited, not fabricated: re-searching found it stated verbatim,
with a named byline, on South Dakota State University Extension's "Injection Site Lesions" page
(Addie Stamps): "99.8% of cattle processed in the fed cattle processing plants surveyed had no
visible injection site lesions" (2022 NBQA) — directly confirmed by raw-HTML fetch of that page.
The same SDSU page also independently states the market-cow/bull figure (97.1%/2.9%), matching
S9's own already-verified companion figure, which corroborates the page's reliability. S9's
citation is corrected to this SDSU Extension page; the 0.2% figure itself is unchanged, so it does
not require recomputing the expected lesion cost or `margin_pct` in the margin calculation
(`$7.05/head ÷ 11% ≈ $64.09/lesion, × 0.2% ≈ $0.13` per animal — unchanged). Per this project's
never-fabricate doctrine (MCS-06), a correctable mis-citation is fixed at the citation, not
converted to a Modeling Assumption, since the real, findable source was located.

This is not a NOT-FOUND situation and not an arbitrary coin flip: every cell uses real, cited
numbers (S1, S2, S3, S5). But it genuinely does not collapse to one verdict — under the
CLSI/adult-cattle benchmark both options fail in every cell; under the calves benchmark the Single
Shot always passes while the Four-Day Course's pass/fail depends on which dosing point and window
convention are used. Shipped as a new deliverable, **D5** (case.json, case.md Challenges section),
with its underlying real inputs in a new **Appendix H** (case.md), and the full table plus
facilitator guidance on strong vs. weak student submissions in FACILITATOR.md's "The margin"
section. `case.json.balance.margin_pct` (13.9%, Option B wins on cost) and the cost-tiebreaker
computation from the retune above are **unchanged** by this addendum — only the primary
efficacy-gate framing, `case.json.derived.primary_gate_resolution`, `balance.argument_a`,
`balance.argument_b`, and the relevant `balance.margin_note` clause were rewritten. Updated
`case.json.qa.case_md_sha256` to match the edited case.md.
