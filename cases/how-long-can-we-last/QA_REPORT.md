## case-readiness run — 2026-09-04

**State:** DRAFT → TIER1_PASS → TIER2_PASS. **Verdict:** TIER2_PASS (Tier 1 clean, 0 blockers,
2 documented GAPs after `resync_artifacts.py`; all six Tier 2 probes recorded, 0 mechanical FAIL,
0 unresolved finding).

### Tier 1 — structural (21 checks)
sha256(case.md) = see `case.json.qa.case_md_sha256` (set by `resync_artifacts.py` after this report)

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview has zero load-bearing numerals (a "three tabs," "three times," "half of a conversation" are texture, not data the student needs) |
| T1-03 | PASS | Dilemma binary, opens "You are Renata Osei." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | GAP → fixed | final standards appendix (G) was referenced only as "Appendix F" in Background due to a lettering typo; corrected to reference Appendix G correctly, and Appendix F (Sources) is now correctly referenced too |
| T1-07 | PASS | Appendix G's vocabulary and "how to…" lines are verbatim spine labels |
| T1-08 | PASS | every number cited (S1-S5) or declared a Modeling Assumption (MA1, MA2) |
| T1-09 | PASS | `margin_pct` = 14.84, both arguments written |
| T1-10 | GAP (documented) | `new_coverage[]` empty; downgraded from BLOCKER by the reinforcement carve-out — see `case.json.reinforcement_note` (all 7 claimed skills already `n>0`; this case reinforces the group's two thinnest skills while closing the emergency-fund-sizing topic gap) |
| T1-11 | PASS | learning-goal mutual reachability — 0 unmapped deliverables, 0 unreachable skills |
| T1-12 | PASS | tier (T2) vs numeric load (percent, ratio, proportion, two competing variables — fund size vs. real survival) |
| T1-13 | GAP (documented) | FACILITATOR.md has the full anchor ladder, a justified `Twist: N/A`, a timed 45-minute plan, and 5 Socratic questions; the Twist-is-N/A confirmation remains a GAP by design (MCS-15's non-blocking downgrade), and was independently re-confirmed sound by Tier 2 P4's adversarial re-read |
| T1-14 | PASS | FACILITATOR.md numbers reconcile with case.json — all guide-only derived/illustrative figures (coverage percentages, common-error worked examples, sensitivity-flex results) moved into `case.json.derived` so they are checkable, not orphaned |
| T1-15 | PASS | no `published/` dir — nothing to drift |
| T1-16 | PASS (after resync) | `case.json.qa.case_md_sha256` set by `resync_artifacts.py` to match the final case.md |
| T1-17 | PASS | `cohort_bands[]` declared (Full / Compressed / 1:1 pair) |
| T1-18/19/20/21 | PASS (no-op) | no `published/` dir yet — nothing to check |

**BLOCKER (0). GAP (2, after `resync_artifacts.py`), both documented carve-outs, not defects:**
- **[T1-10]** `new_coverage[]` empty — see `case.json.reinforcement_note`, same evidentiary pattern
  as `cases/the-two-offers/case.json`.
- **[T1-13]** `Twist: N/A`, justified in FACILITATOR.md and independently confirmed by Tier 2 P4.

(T1-16 was open earlier in this pass — `case.json.qa.case_md_sha256` was still `null` — and was
resolved by running `resync_artifacts.py` after all edits were finalized; see the summary at the
end of this report.)

A preflight lint pass (`skills/case-readiness/scripts/preflight_lint.py`) was run before and after
every substantive edit in this pipeline stage; the one real finding it caught (a `<!-- ... -->`-free
leak of the literal word "FACILITATOR.md" inside case.md's MA2 sensitivity note) was fixed before
Tier 1 was run for the first time. Final preflight run: clean.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Dispatched to a fresh, unbriefed subagent given only the packet (`/tmp/coldsolve-how-long-can-we-last/PACKET.md`) and the 7 standard questions, with no access to FACILITATOR.md/case.json/RESEARCH_LOG.md. It built D1's percent breakdown correctly (Housing 37.3%, largest), solved D2 correctly (whole = part ÷ percent = $756/0.21 = $3,600, and independently sanity-checked it against the stated "modest surplus" narrative), computed both fund sizes correctly via proportion (Fund A $17,622, Fund B $20,237), ran the D4 survival test correctly (Fund A = 6.10mo/87.1%, Fund B = 7.00mo/100%), chose Option B with a named metric (percent/dollar coverage of the documented dry spell, not "biggest fund" or "fastest to invest"), and named a genuine counter-argument (opportunity cost of the extra $2,615) and the correct most-sensitive assumption (MA2) unprompted. It also correctly flagged MA2 as the case's own least-supported figure — a real, already-disclosed property of the case, not a hidden defect. |
| P2 both-sides | **PASS** | Dispatched to a second fresh subagent, packet only. Built a real, numbers-backed sentence for each side (A: "still covers 6.1 of 7 months — 87% of the worst stretch on record — while putting $2,615 to work today"; B: "sized off this household's own invoicing history... covers exactly 100%... $0 short"). Identified the specific collapse question correctly: Option A collapses at "where does the $2,615 shortfall in month 7 come from?", which has no quantitative answer from the packet (only a qualitative concession — sell investments or use credit); Option B's weakest point (opportunity cost) survives with its own real number. Neither argument is a bare concession, confirming the balance test is real, not a paper margin. |
| P3 trap check | **PASS (guide amended)** | Dispatched to a third fresh subagent on the packet, then given FACILITATOR.md's trap section. Its predicted trap — reusing total essential expenses ($5,874) as the D4 divisor instead of the documented monthly shortfall ($2,891), silently retesting Option A against a fabricated 3-month bar instead of the real 7-month dry spell — did **not** match either of the guide's two originally-named traps (skipping the D4 comparison entirely; the D2 part/whole reversal), and the subagent correctly flagged that this specific error would "likely slip through unnoticed" since neither Socratic question nor cold-call target addressed it. Rather than record a bare FAIL, `FACILITATOR.md`'s "The trap" section was amended with a third, explicitly named trap covering this exact D4-divisor substitution, with a cold-call instruction (check a Hero's D4 setup for the specific divisor used, not just their final percent). Verified Tier 1 and the preflight lint still pass after the edit. |
| P4 twist integrity | **PASS** | Twist is `N/A`, justified in FACILITATOR.md. A fourth fresh subagent adversarially re-derived every number (D1–D4, margin) under every plausible alternate reading of Appendix B/C/D's stated assumptions — including the "21% of typical" vs. "21% decrease" ambiguity in D2 and a rounded-vs-unrounded intermediate-value check — and found no hidden-convention bug: the "21% decrease" misreading is a real candidate error but is not textually invited by the packet's own unambiguous "part as a percent of whole" wording, and it is already named and disclosed in FACILITATOR.md's trap section rather than being a blind spot. All arithmetic matched FACILITATOR.md exactly. The N/A holds up. |
| P5 assumption sensitivity | **PASS (disclosed)** | `cases/how-long-can-we-last/sensitivity_model.py` authored (contract: `PARAMS`, `evaluate(params)`, `FLEX=["dry_spell_months"]` — MA2, the case's one load-bearing sizing assumption; MA1 is correctly excluded from `FLEX` since it plays no role in either fund's size). Flexing MA2 ±50% found a genuine instability: at −50% (3.5 months) the verdict flips to Option A (Fund A already exceeds the shorter stretch); at +50% (10.5 months) the fund-size margin balloons to 72.26%, breaching the SPEC §2 20% cap. This is disclosed, not eliminated, per `case.json.sensitivity_disclosure[0]` (category F — forecast/irreducible unknown, since no amount of research can establish in advance how long a *future* dry spell will last; the case is authored and balanced at its own household's *documented historical* 7-month worst case, not a free dial) and mirrored in FACILITATOR.md's Anchor 4. The disclosure meets the script's structured schema (param/category/justification ≥20 chars), so the mechanical result is `PASS (disclosed)`. |
| P6 data decay | **PASS** | The QA sandbox has no outbound network, so this probe was run directly by the orchestrating session (which does have live web access) rather than delegated to a separate subagent. Fetched all 5 unique source URLs directly. All returned reachable content. Confirmed the cited figure is present in the fetched content for S1 (BLS: all six 2024 category dollar figures matched Table 2 exactly), S2 (BLS OOH: "$35,800 in May 2025" quoted verbatim), S3 (Federal Reserve: both the 59% and the 56%-vs-26%-excluding-gig figures quoted verbatim), S4, and S5. **A real defect was caught and fixed during this probe, not merely a clean pass:** the original S4 entry's "9% typical swing, ≥21% swing in 1-in-4 months" claim could not be re-verified on its own cited URL — a direct fetch asked to quote every percent-figure sentence on that page returned seven real quotes, none matching. A second targeted web search for the exact phrase also failed. Disposition: **removed as unverifiable**, per SPEC §5's "never fabricate a number" (this had been a fabricated/misattributed synthesis from an earlier search-tool summary, not something this case invented deliberately, but the effect — an uncitable number presented as sourced — is the same defect the rule exists to catch). Replaced with two figures verified by direct fetch: S4 (same JPMC report URL, correctly quoted this time: "vast majority of people aged 18-24, bottom income quintile, or Western workers experienced... more than a 30 percent month-to-month change") and S5 (a different, correctly-identified JPMC 2018 report page: "58 percent [of transportation-platform earners] had earnings in just three or fewer months of that year"). `case.json` (sources[], modeling_assumptions[], sensitivity_disclosure[]) and `case.md` (Appendices D and F) were updated to match; the full correction is documented in `RESEARCH_LOG.md`'s "Correction — 2026-09-04" section rather than silently rewritten. S1/S2/S3 required no correction. |

**On the P6 correction's effect on the rest of the case:** MA1's 21%/$756/$3,600 relationship and
MA2's 7-month/$0 dry spell are unchanged in value — both were always disclosed as this case's own
stated scenario choices, only "informed by" (not directly quoting) the swapped-out figures. No
number in Appendix A, B, or C changed; no fund size, margin, or D1–D4 answer key changed. The
correction is entirely confined to which real external citation backs the *plausibility* of MA1's
and MA2's magnitude, not to any number a student computes.

### Tier 3 — human dry-run
NOT RUN.

---

**Summary of what changed in this pass (case-write → case-research → case-readiness, run together
for this case):**
1. Wrote `case.md`/`case.json`/`LEARNING_GOALS.md`/`FACILITATOR.md` with all figures sourced or
   disclosed as Modeling Assumptions from the start (no `{{NEEDS_SOURCE}}` placeholder stage was
   shipped as a separate artifact, since research was performed inline before first draft; see
   `RESEARCH_LOG.md` for the full search/rejection record).
2. Fixed a Background lettering error (Appendix F/G reference swap) caught by T1-06.
3. Fixed a `<!-- FACILITATOR ONLY -->`-style leak (case.md's MA2 sensitivity note named
   `FACILITATOR.md` directly) caught by `preflight_lint.py`.
4. Moved 9 guide-only illustrative/derived figures into `case.json.derived` so T1-14's continuity
   sweep has a checkable home for them instead of flagging them as orphans.
5. Added a third named trap to `FACILITATOR.md` after Tier 2 P3 surfaced a real, unanticipated
   wrong path (the D4 divisor substitution) that neither original trap would have caught.
6. Authored `sensitivity_model.py` for Tier 2 P5 and added a structured
   `case.json.sensitivity_disclosure[]` entry after P5 found a genuine ±50%-flex instability.
7. Corrected a real sourcing defect (the unverifiable JPMC "9%/21%" figure) found by Tier 2 P6,
   with the full correction documented in `RESEARCH_LOG.md` rather than silently fixed.
8. Set `case.json.qa` to `TIER2_PASS` with all six probe verdicts recorded by name, and ran
   `resync_artifacts.py` to set `case_md_sha256` to the final, post-correction case.md.
