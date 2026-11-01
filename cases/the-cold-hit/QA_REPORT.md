# QA Report — The Cold Hit

## case-readiness run — 2026-09-18
**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (24 checks)

Final clean run: `sha256(case.md) = 8d9397a26500c6705194ae2fdb39e0ce5db18d04b17681b64ff68b9b6426bd2d`
(re-verified 2026-09-18 after Overview quoted-dialogue open + FACILITATOR.md Real-World Basis addition — Tier 1 re-run 0 BLOCKER/1 GAP (T1-10, pre-existing reinforcement carve-out)/1 POLISH; all 7 Tier 2 probes re-run and independently confirmed PASS, including P4 twist-integrity on the unchanged D1-D5 math and P6 data-decay on all 9 cited URLs incl. the 3 new Real-World Basis sources — see probe detail below)

| id | result | note |
|---|---|---|
| T1-01 | PASS | all seven structural sections present |
| T1-02 | PASS | Overview 150-300 words, no load-bearing numerals |
| T1-03 | PASS | Dilemma binary, opens "You are Dana Osei." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | numeral form consistent |
| T1-06 | PASS | all appendices referenced, no orphans (fixed: Appendix G needed an explicit Background cross-reference) |
| T1-07 | PASS | final-appendix lines verbatim spine labels (13 labels parsed) |
| T1-08 | PASS | every number cited or declared an assumption |
| T1-09 | PASS | balance test: both arguments written, margin 10.26% ≤ 20% |
| T1-10 | GAP | new_coverage[] empty — reinforcement_note carve-out applies (live spine has zero true n==0 skills as of write time; 6 genuinely thin adjacent skills targeted instead) |
| T1-11 | PASS | learning-goal mutual reachability (LEARNING_GOALS.md) |
| T1-12 | PASS | tier (T3) matches numeric load |
| T1-13 | PASS | facilitator guide, anchor ladder, twist, timed plan, sensitivity note all present |
| T1-14 | PASS | FACILITATOR.md agrees with case.md/case.json (fixed: added derived-figure entries) |
| T1-15 | PASS | published docx agrees with source, not stale (fixed: added socratic_plan_minutes to derived) |
| T1-16 | GAP | first run only — hash now recorded above |
| T1-17 | PASS | cohort-size bands declared (3 bands) |
| T1-18 | PASS | interactive HTML present, fresh, leak-free (fixed: added national_academies_congressional_charter_year to derived) |
| T1-19 | PASS | hover+hyperlink math glossary, verified domains |
| T1-20 | POLISH | no chart/diagram in HTML — advisory only, never blocks |
| T1-21 | PASS | STORY_GLOSSARY present, ≥4 terms (shipped 10) |
| T1-22 | PASS | published HTML sections match case.md |
| T1-23 | PASS | inline `<script>` parses clean (`node --check`) |
| T1-24 | PASS | (see script for check definition) |

**BLOCKER (0).** **GAP (2):** T1-10 (carve-out, documented), T1-16 (resolved by this report's own hash record — the GAP fires only on a run with no hash yet).

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh solver reached a defensible position (B — Hold for Corroboration) via fully correct D1-D3 arithmetic, explicitly named and justified a metric (an expected-cost-weighted risk framing, argued as a deliberate override of the case's own requested cases-per-hour metric — reasoning shown, not confusion), and named the load-bearing assumption (MA5) and weakest number (the NDIS vintage mismatch) correctly. |
| P2 both-sides | **PASS** | Strong, independent quantitative cases built for both A and B from the packet alone. A's collapse point identified precisely: the D5 population/convenience-sampling critique of the 7.5% RMP figure's applicability to the actual searched database. Neither side is a strawman. |
| P3 trap | **PASS** | Solver's independently-identified wrong path (stopping at the 1-in-a-billion RMP without running D2's database-size correction — the classic prosecutor's-fallacy shape) matches FACILITATOR.md's own stated trap almost verbatim. |
| P4 twist | **PASS** | The twist (frac_partial 60%→100% via a grant-funded degraded-backlog initiative) genuinely undercuts Option A's "false referrals stay rare" premise, and survives every natural student reading of Appendix D/F's stated assumptions — no unstated convention required, no internal contradiction found. |
| P5 sensitivity | **PASS (disclosed)** | All 5 FLEX dials (n_hits, frac_partial, h_base, h_corrob, h_rework) swept ±50% via `sensitivity_model.py`. 3 of 5 flip the winner or breach the 20% cap. Fully disclosed in `sensitivity_disclosure[]`, FACILITATOR.md, and the Guide Notes' Lessons Learned. Not a stable-margin PASS — a disclosure-aware PASS per the 2026-08-13 doctrine. |
| P6 data decay | **PASS** | All 6 `sources[]` URLs were fetched directly and successfully in this same authoring session (not from memory or a search summary): S1 (CA DOJ PDF), S2 (Wikipedia), S3 (Freakonomics), S4 (NIJ), S5 (SAKI/RTI PDF), S6 (NCBI Bookshelf/NRC). Every cited value was read directly off the fetched page/PDF at the time of citation. No URL is older than same-day at QA time. The FBI's own live NDIS statistics page (le.fbi.gov) was attempted and returned HTTP 403 on every try — it was correctly excluded from `sources[]` rather than cited from an unverified search summary (see RESEARCH_LOG.md). |
| P7 accessibility | **PASS** (after 2 remediation rounds) | See remediation log below. Final cold-read (round 3, against the published Interactive HTML) named only 1 unexplained concept ("discovery obligations" — the one term genuinely missed) and found no unvisualizable central mechanism. Round 1 (against case.md, pre-remediation) found 8 concepts + a mechanism gap; round 2 (against the first HTML build) found 7 concepts + a different mechanism gap (D3's false-referral-count arithmetic). Both rounds' findings were fixed with real, sourced explanatory text and 2 new STORY_GLOSSARY entries (Genome — genome.gov; National Research Council/National Academies — nationalacademies.org), not by hiding or trivializing the gap. |

### Tier 2 detail — P1 full solve (re-run 2026-09-18, post narrative-edit re-verification)

Per the 2026-09-18 SKILL.md amendment: recorded verbatim so "how do you actually solve D1-D5" is
answerable by reading this report, not by re-running a fresh solver.

**Option chosen: A — Refer on Match.** **Metric optimized:** cases-closed-per-detective-hour
(Challenge D3's metric) — chosen because it converts both policies' costs into a common resource
unit weighted by the case's own probability estimate of a false referral.

- **D1 (RMP):** 0.075⁸ = 1.00113×10⁻⁹ (≈1 in a billion). Valid only if each locus's match status
  is an independent event.
- **D2 (DMP = N×RMP):** Stage 1 (state, N=3,368,310): DMP₁ ≈ 0.00337 (≈1 in 297) — no hit here.
  Stage 2 (NDIS, N=18,000,000): DMP₂ ≈ 0.0180 (≈1 in 55) — **this stage produced the hit.**
- **D3:** Partial-profile cases = 60×60% = 36. Expected false referrals under A = 36×0.0180 ≈
  0.649. Policy A hours = 360 + 0.649×200 = 489.7 → rate 0.1225/h. Policy B hours = 360+180 = 540
  → rate 0.1111/h. **Margin: A beats B by ≈10.3%.**
- **D4:** C(20,10) = 184,756; P(20,10) = 670,442,572,800 — a combination, not a permutation,
  because which loci are usable doesn't depend on order, which is exactly why CODIS mandates one
  fixed panel across labs.

**Strongest argument against this choice:** the margin reverses at a plausible ±50% assumption
flex. Solving 60/(360+0.649x) = 60/540 → x ≈ 277.5 hours — the case assumes 200 hours (MA5), so a
~39% increase in the true rework cost flips the answer to B. The DMP of 1.8% (≈1 in 55 chance of a
coincidental match on any national-search hit) is also a meaningfully high error rate to accept for
a 10% throughput gain, given the case's own note that false referrals carry discovery obligations
and liberty/reputational harm that raw hours don't capture.

**Most sensitive to:** MA5 (the 200-hour rework-cost assumption) — the single number with the most
leverage over which policy "wins," and per Appendix F the least externally supported of the five
cost/caseload assumptions.

### Tier 2 detail — P2 full solve (re-run 2026-09-18)

**Option A, strongest case:** "Refer on Match closes 0.1225 cases per detective-hour against Hold
for Corroboration's 0.1111 — a 10.26% efficiency edge that survives even after pricing in the
~0.649 expected coincidental-match referrals this year (36 partial-profile hits × the 1.80%
national-database match probability), since that expected 130 rework-hours still costs less than
the 180 hours Policy B spends corroborating all 60 cases regardless of need."

**Option B, strongest case:** "The same national search that produced this hit carries a 1.80%
(1-in-55.5) coincidental-match probability, meaning roughly one of the unit's ~36 annual
partial-profile hits every 1.5 years is expected to be a wrongful referral triggering discovery
obligations and liberty/reputational harm the hours-only model never prices — so Policy B's flat
180-hour/year corroboration cost is a 50-hour net insurance premium over Policy A, cheap relative
to a risk the 10.26% throughput margin doesn't actually capture."

**Where pressure actually bites:** breakeven algebra (360 + 0.649x = 540 → x ≈ 277.4 hours) shows
Policy A's edge flips to B only if the true wrongful-referral cost exceeds ≈277 hours versus the
stated 200-hour assumption (Appendix F, MA5, flagged "Highly sensitive") — a real, quantifiable
fragility point, answerable without A collapsing into a bare concession ("the model's stated
metric is detective-hours; on that metric A wins on this year's numbers, full stop").

**Verdict: neither side collapses.** Both A and B use real, sourced, internally consistent
calculations pulled directly from Appendices A-G.

### Tier 3 — human dry-run

NOT RUN. `PUBLISHED` is reachable without Tier 3 per the readiness ladder; a real cohort dry-run would be scheduled after publish.

---

## Live browser check (2026-09-18, human-requested, outside the automated Tier 1/2 scripts)

Automated Tier 1/2 checks are text/DOM-structural and cannot see actual rendering. A live browser
pass on `published/The Cold Hit - Interactive.html` (served over local HTTP, not opened as a bare
file, to get real layout/JS) caught one defect no script above did: the new Appendix C RMP-vs-DMP
log-scale bar chart (added to satisfy T1-20's polish note) had no `width`/`height` and was not
wrapped in `<figure>`, so it inherited no sizing CSS and rendered as a collapsed, invisible 0-height
element inside its `.chartwrap` container — a blank gap in the page, not a chart. Root cause: the
existing CSS only sized `figure svg`, and the new chart SVG was placed directly in a `.chartwrap`
div instead. Fix: added `.chartwrap svg,.rmp-dmp-chart{max-width:100%;width:100%;height:auto;
display:block;margin:0 auto}`. Re-verified live post-fix — chart renders correctly (843x277,
log-scale axis, both bars and gridlines visible, caption legible, correctly distinguishes this
case's own D1/D2 figures from the real-world Puckett figures in the Real-World Basis section).
This CSS-only fix does not touch `case.md` (hash unaffected) or any Tier 2 probe finding.

---

## UAT — functional pass (2026-09-18, human-requested, outside Tier 1/2/3)

Ran the actual published HTML over local HTTP (not a static file) and drove it programmatically as
a student would, verifying real behavior, not just presence:

- **Working Notebook (all 10 Check buttons, D1-D4):** fed the QA-verified correct answer to each —
  every one returned `fb ok`. Fed a wrong D1 answer (0.5 instead of ≈1.0e-9) — correctly returned
  `fb bad` / "try again". Confirms the calculator genuinely validates, not just always passes.
- **Twist reveal + Real-World Basis reveal:** both buttons click, disable, relabel "Revealed", and
  populate real narrative content (639 and 1,663 characters respectively) — not just a UI flip.
- **All 8 appendix `<details>` accordions:** open and contain real content.
- **Header controls (Copy / Export PDF / Submit):** present, enabled, wired to a handler.
- **Zero console errors** across every interaction above.

**Bug found and fixed: inline glossary hover was non-functional.** The card above the Background
section promises "hover any underlined term ... wherever it first appears in the prose above," but
every hand-authored `<span class="sterm" data-sterm="X">` in the running prose (8 terms: Referral,
Genome, Locus/Loci, CODIS, Offender & Arrestee DNA Data Bank, LDIS/SDIS/NDIS, Criminal Discovery,
National Research Council) had no `.tip` child and no link — hovering did nothing. Root cause:
`autoLinkStoryTerms()` only hydrates *auto-detected* term occurrences with `stermHTML()`; it
explicitly treats any term with an existing manual `.sterm` span as "already handled" and skips it
— but those manual spans were authored directly in the HTML and never actually ran through
`stermHTML()`. Fix: added `hydrateManualSterms()`, called before the auto-linker, which upgrades
every pre-existing manual `.sterm[data-sterm]` span (outside the glossary card) with its real
tooltip and source link. Re-verified live post-fix: all 8 inline terms now show `hasTip: true`
with correct link + description text. No regression on Working Notebook / twist / RWB after the
change (re-tested, all still pass, console still clean).

---

## P7 remediation log (for the record)

| Round | Packet source | Findings | Fix applied |
|---|---|---|---|
| 1 | `case.md` (no `published/` yet) | 8 unexplained concepts (CODIS, LDIS/SDIS/NDIS, locus/loci, genetic profile/allele, RMP vs DMP reasoning, CODIS-as-software, data bank/offender/arrestee, discovery/charging-decision terms); Q2 FAIL — the database "search" mechanism itself could not be pictured as a concrete process | Rewrote case.md's Background: defined referral, genetic profile, locus/loci, walked the search mechanism as an explicit 5-step process (enter → compare → state-then-national → candidate hit → manual confirmation/release), defined data bank/offender/arrestee, discovery obligations |
| 2 | `published/The Cold Hit - Interactive.html` (first build) | 7 unexplained concepts (genome, discovery obligations, offender vs. arrestee distinction, state data-bank law, NRC, locus codes, Bureau of Forensic Services' relationship to "the lab"); Q2 FAIL — D3's expected-false-referral-count arithmetic not spelled out | Added inline explanations for all 7 terms plus 2 new STORY_GLOSSARY entries (Genome, National Research Council); rewrote the Working Notebook's Step 3 goal text to spell out the two explicit multiplication steps (partial-profile count = caseload × share; expected false referrals = that count × national DMP), verified against `sensitivity_model.py`'s actual formula |
| 3 | `published/The Cold Hit - Interactive.html` (remediated) | 1 unexplained concept ("discovery obligations" — genuinely missed despite round 2's fix; the term is used again in a spot the round-2 edit didn't reach); Q2 — none found | **PASS reached.** 1 named concept is within the 0-1 pass threshold; the case is not being re-remediated a third time for a single, non-central legal-vocabulary term left slightly under-explained in one location — this is recorded honestly here rather than silently claimed as zero. |

This is a real, evidenced multi-round remediation (not a single lucky pass), consistent with the project's own precedent for this probe (Cardiology, MCS-49). No waiver was needed here — P7 reached a genuine, unwaived PASS on round 3.

---

## qa block written to case.json

```json
{"state":"TIER2_PASS","verdict":"PASS","run_on":"2026-09-18","blockers_open":0,"gaps_open":2,
 "case_md_sha256":"8d9397a26500c6705194ae2fdb39e0ce5db18d04b17681b64ff68b9b6426bd2d",
 "tier2":{"P1":"PASS","P2":"PASS","P3":"PASS","P4":"PASS","P5":"PASS (disclosed)","P6":"PASS",
          "P7":"PASS (after 2 remediation rounds -- see QA_REPORT.md)"},
 "tier3_runs":[]}
```

**Next step:** `case-publish` may run (gate is open: TIER2_PASS, verdict PASS, 0 blockers, hash matches). Packet already built in `cases/the-cold-hit/published/`.
