# Research Log — The Contrapositive Claim

Full search trail for `case-research`, run 2026-09-01. 47 `{{NEEDS_SOURCE}}` placeholders found in
`case.md` (P01–P47, per the enumeration script in `skills/case-research/SKILL.md`). All 47 are
resolved: 17 SOURCED, 30 ASSUMPTION (all 30 are the constructed Appendix E appeals log, which is
disclosed as Modeling Assumption MA2 — no real carrier's individual appeal file is ever public).
Zero left OPEN, zero dropped as decorative, zero redesigned away from the case (one appendix,
C, was redesigned to report a different but genuinely public metric — see P16/P17 below).

---

## P01 — Appendix A, flood-damage clause verbatim text

**Searched:** "ISO HO-3 homeowners policy flood exclusion clause exact text 'flood' defined";
"'we do not insure for loss' 'flood' 'surface water' homeowners policy exclusion verbatim
'mudslide'"; "homeowners insurance policy specimen PDF 'SECTION I - EXCLUSIONS' 'Water Damage'
'Flood, surface water'"; "'HO 00 03' '3. Water' exclusion 'Flood, surface water, waves'
'regardless of any other cause or event contributing concurrently'"; "'We do not insure for loss
caused directly or indirectly by any of the following' ... HO-3".

**Found:** No single public PDF of the current full ISO HO 00 03 form text (ISO forms are
copyrighted and not freely republished in full). Found and directly fetched two independent legal
analyses that quote fragments of the real clause verbatim with citations to the actual ISO form:
a United Policyholders–hosted attorney white paper quoting the 2011 HO3 "Water" exclusion
definitional list with a footnote citing the ISO form itself (S4), and a Property Insurance
Coverage Law Blog/IRMI line-by-line form analysis citing "Insurance Services Office, Inc.,
Homeowners 3—Special Form (HO 00 03 03 22), © 2021" for the current-edition placement of the same
"Water" exclusion category (S5). A third legal-blog source gave the verbatim standard
anti-concurrent-causation lead-in sentence used across ISO homeowners exclusions (S6), without an
independent page-level citation for that exact sentence.

**Outcome:** SOURCED, composite HIGH/HIGH/MEDIUM. Assembled the three verified fragments into one
clause for classroom use, with a confidence note in Appendix A disclosing exactly which piece came
from which source and at what confidence. This is not a single primary-document quote — it is a
transparent assembly of independently verified real fragments, which is disclosed as such rather
than presented as a single seamless primary quote.

---

## P02–P13 — Appendix B, four named carriers × 3 years each

**Searched:** "California Department of Insurance 2025 Consumer Complaint Study homeowners
justified complaint ratio State Farm General Farmers Insurance Exchange Mid-Century".

**Found:** Direct PDF link to `2025-Consumer-Complaint-Study-Home.pdf` on insurance.ca.gov.
Downloaded and parsed with `pdftotext -layout`. All four named carriers' rows matched exactly the
figures named in the task brief: State Farm General Insurance Company 1.4/1.6/11.9 (2022/2023/
2024); Farmers Insurance Exchange 4.5/24.0/40.2; Mid-Century Insurance Company 4.5/31.8/51.4; USAA
General Indemnity Company 1.6/1.4/0.6. Also captured each carrier's approximate policy-exposure
count from the same table (2,139,816 / 439,921 / 186,617 / 159,197 respectively), which the
original placeholder text did not explicitly ask for but which strengthens Appendix B's context.

**Outcome:** SOURCED, HIGH (S1) — direct download and parse of the actual PDF, dated, unambiguous
units (justified complaints per 100,000 policy exposures), primary regulator publication.

---

## P14, P15 — Appendix B, "Marisol's carrier" exposure base

**Searched:** No search possible — Marisol's carrier is fictional by the case's own construction
(it is explicitly not one of the four named real carriers).

**Found:** N/A by definition.

**Outcome:** ASSUMPTION (MA1). Exposure count (250,000) chosen between the smallest (USAA General
Indemnity, 159,197) and second-largest (Farmers Insurance Exchange, 439,921) of the four real
named carriers, at genuinely mid-size scale. 2024 ratio (18.5) chosen inside the real observed
2024 range across those same four carriers (0.6–51.4). Disclosed in Appendix F (Modeling
Assumptions) with a Sensitivity note that this row is scene-setting only — Appendix B's real
four-carrier data, not this row, is what Background and Challenge D5 actually reference.

---

## P16, P17 — Appendix C, NAIC MCAS complaint ratios

**Searched:** "NAIC Market Conduct Annual Statement MCAS Annual Statement Ratios scorecard
homeowners complaints per 1000 policies in force"; "NAIC MCAS 'Consumer Information Source'
homeowners complaints ratio public data 2023 2024"; "'MCAS' homeowners 'complaints per 1,000' OR
'complaints to claims' ratio published state insurance department".

**Fetched:** `content.naic.org/article/naic-releases-first-its-kind-national-analysis-...` (news
release, no complaint metrics); `content.naic.org/industry/mcas/homeowners-insurance-report` (no
complaint metrics, confirms company-level MCAS data is confidential); `content.naic.org/
mcas_data_dashboard.htm` (confirms a downloadable homeowners scorecard XLSX exists per year, but
the page text alone gives no numbers). Located the actual XLSX download links by fetching the raw
HTML of the dashboard page and grepping for homeowners scorecard hrefs. Downloaded and parsed
`industry_mcas_2024_scorecard_ho_all-no Citizens FL_0.xlsx` directly (unzipped as OOXML, parsed
`sharedStrings.xml` / `sheet1.xml` by hand — no `openpyxl`/`pandas` available in this environment).
The file publishes seven ratios (claims closed without payment; claims unprocessed; claims paid
beyond 60 days; non-renewals; cancellations over 60 days; cancellations under 60 days; suits opened
vs. claims closed without payment) by state — **no complaint-count or complaint-rate ratio is
published in this file at all.** Cross-checked against the MCAS Data Call — Homeowners PDF, which
confirms complaints are collected as a raw company-level data element (3-54) but are confidential
and not part of the published scorecard.

**Outcome:** NOT FOUND for the specific figures requested (complaints-per-1,000-policies,
complaints-to-claims-opened) — genuinely not published for the homeowners line by NAIC MCAS.
**Redesign**, not an assumption: Appendix C now reports two real, dated, public MCAS ratios
instead — California's 2024 Ratio 1 (claims closed without payment, 34.9%) and Ratio 7 (suits
opened / claims closed without payment, 1.9%) — which speak to the same underlying "how often does
a denial-adjacent claims-handling outcome occur" concern and are, if anything, more directly
relevant to this case's claims-denial theme than a raw complaint count would have been. Logged as
SOURCED (S2, S3) with a "Rejected anchor" note in Appendix G explaining the substitution
transparently, per the SPEC §5 "contested/unavailable figure" precedent.

---

## P18–P47 — Appendix E, 10 rows × 3 columns (constructed appeals log)

**Searched:** N/A — the appendix's own text states this is "a constructed scenario dataset, not a
real carrier's internal file — no insurer publishes its individual appeal records." No real
per-appeal insurance file of this kind is ever public, by definition (privacy, litigation
privilege, and the fact that no such log exists prior to the case's own construction).

**Outcome:** ASSUMPTION (MA2). Constructed a 14-row log (expanded from the original 10-row table
stub, following the `alert-curve` precedent of growing a constructed log at research time when the
original row count cannot support a within-cap margin — see Margin Retune below). Design:

- 6 rows where the ground-truth cause is genuinely flood (creek overflow, storm surge, surface
  water/hillside runoff, lake overflow after a dam release, flash flood after a levee failure,
  tidal water) — both candidate standards correctly uphold the denial, no catch needed.
- 6 rows where the ground truth is *not* flood but the misapplication is plain on the clause's own
  definition (ice-dam meltwater backup, dry-week sewer backup, HVAC condensate clog, sump-pump
  failure in ordinary rain, water-heater rupture, an improperly sealed window air-conditioner) — a
  diligent reviewer applying *either* standard's own definition of "flood" (Appendix A) catches
  these on their face, without needing to independently re-examine the reported facts for a
  competing cause.
- 1 row (row 1) — the windstorm/roof-breach scenario from the case's own Overview, deliberately
  placed in the log to tie the appendix back to the case's inciting incident — where the
  adjuster's stated reasoning merely labels the loss "flood" without addressing the wind-created
  roof opening visible in the reported facts. Only the Mirror-Image Standard's explicit
  non-flood-cause check (per `case.json` `balance.argument_b`) is structurally positioned to catch
  this one; the Plain-Text Standard, taking the adjuster's stated label at face value, is not.
- 1 row (row 14) — the twist candidate the FACILITATOR.md left open pending Appendix E's
  construction — where the competing cause (a slow, unrelated pinhole leak) was not visible in the
  reported facts at the time of the appeal review at all, so *neither* standard catches it. This
  directly supports the FACILITATOR's planned twist: logical equivalence protects against the
  converse/inverse error specifically, not against every possible misjudgment on appeal.

**Margin retune.** An earlier 14-row draft (3 both-catch rows, 3 Mirror-Image-only-catch rows, 8
flood rows) produced Plain-Text = 3, Mirror-Image = 6 catches — a 100% margin, far outside SPEC
§2's ~20% cap, and the FACILITATOR.md explicitly warned against shipping a runaway margin without
retuning. Retuned to 6 both-catch rows and 1 Mirror-Image-only-catch row (Plain-Text = 6,
Mirror-Image = 7 catches out of 8 wrongly-denied rows), landing the computed margin at 16.7% —
inside the cap — while preserving every failure mode the case's balance argument depends on. See
`case.json` → `modeling_assumptions[MA2].sensitivity` for the full retune note, and
`case.json` → `balance.margin_note` for the full arithmetic derivation (facilitator-only; never
placed in `case.md`).

---

## Supplemental: Appendix D legal/regulatory citations

Appendix D's narrative text already named CACI No. 2332, *Hangarter v. Provident*, and the
"affirming the consequent"/"denying the antecedent" fallacy names, but carried no `[S#]` markers.
Per the task brief's instruction to "verify and cite properly," each was independently confirmed
and added to Appendix G — Sources:

- **CACI No. 2332** — confirmed real and currently titled "Bad Faith (First Party) — Failure to
  Properly Investigate Claim — Essential Factual Elements" via the official Judicial Council of
  California compiled CACI PDF and corroborated via Justia's CACI Series 2300 page (S8, HIGH).
- ***Hangarter v. Provident Life and Accident Insurance Co.***, 373 F.3d 998 (9th Cir. 2004) —
  confirmed real via Justia's full-text opinion (S9, HIGH).
- ***Carver v. Lehman***, No. 06-35176 (9th Cir. 2008) — confirmed real via the Ninth Circuit's own
  official opinion PDF (docket number and decision date match). The "denying the antecedent"
  fallacy discussion was corroborated indirectly: the court's own `cdn.ca9.uscourts.gov` library
  system preserved a snapshot of the Wikipedia "Denying the antecedent" article specifically
  because *Carver v. Lehman* cited it — a strong signal the opinion (majority or a separate writing
  within the same disposition) engages with the fallacy by name, consistent with the earlier
  concept-research finding this citation was built on (S7, HIGH).

---

## Note on `case.json.modeling_assumptions[MA0]`

MA0 (adjusters confusing the clause's converse with its contrapositive as this case's own scenario
premise) was preserved verbatim in framing per the task brief's explicit instruction — this is the
case's own modeling premise, not a documented insurance-specific incident, and no search this run
found one. Only its citation was strengthened (added the specific *Carver v. Lehman* docket number
and the S7 source row it now points to).
