# QA Report — The Equivalent Ledger

## case-readiness run — 2026-09-09

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Preflight lint

`python3 skills/case-readiness/scripts/preflight_lint.py --case the-equivalent-ledger` found one
advisory finding: line 136 (the Sources appendix) matches the "twist/trap/facilitator" regex
because Appendix E cites a real, real-world article whose actual published title is "The End of
the Legacy Rewrite Trap" (Allytics Tech Perspectives). This is a citation title, not the case
naming its own twist or trap to the student — reviewed and accepted as a false positive of the
kind the script's own docstring anticipates (a real title containing a flagged word). No change
made; the citation must stay accurate to the source's real title.

Two real leaks WERE found and fixed during this same authoring pass, before the gate was run
mechanically: (1) the original MA4 row stated O(25)=$34,500 and R(25)=$36,390 with the 5.5% gap
directly in student-facing text — the literal D3 answer, handed to the student in the assumptions
table. (2) The original MA2 row stated the difference polynomial's factored form and said the two
formulas "disagree everywhere else" — the literal D4 answer. Both rewritten to describe the
assumption's basis and note that "the answer is sensitive to this value" without stating the
result, per skills/case-write/SKILL.md's 2026-08-13 rule. This is exactly the defect class that
rule exists to catch, caught here by manual review before Tier 2's cold-solve packet was even
built, not by the mechanical regex (which does not scan the Modeling Assumptions table's own
result-adjacent phrasing outside its narrow percent-proximity pattern).

### Tier 1 — structural (21 checks)

Ran `python3 skills/case-readiness/scripts/tier1_structural.py --case the-equivalent-ledger`.

First pass found 0 BLOCKERs, 3 GAPs: T1-10 (new_coverage[] empty — see reinforcement_note below),
T1-14 (8 numbers in FACILITATOR.md — the formula coefficients 48/54/96/180 and the twist figures
25920/84000/90480, plus a rhetorical "100%" — had no home in case.json because the checker's number
regex requires a non-word character after a digit, so "48n²" never matches; case.md itself always
carried these values, this was a checker-parsing gap, not a real drift), T1-16 (no hash recorded
yet, expected on a first run). Fixed: added `case.json.derived` with every formula coefficient,
GCF, D3/twist dollar figure as its own JSON field (machine-checkable, not just prose), and reworded
FACILITATOR.md's one rhetorical "it's 100%" to "it's certain" to remove a bare numeral with no
case.md/case.json home. Second pass: 0 BLOCKERs, 1 GAP (T1-10, the accepted reinforcement
carve-out).

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview 222 words, zero load-bearing numerals |
| T1-03 | PASS | Dilemma binary, opens "You are Priya Chandran." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | appendices A-F lettered, ordered, no orphans |
| T1-07 | PASS | 7 final-appendix labels, all verbatim spine labels |
| T1-08 | PASS | every number cited [S1-S3] or declared an assumption [MA1-MA9] |
| T1-09 | PASS | balance test: both arguments written, margin 7.88% (within 20% cap) |
| T1-10 | GAP (accepted) | new_coverage[] empty; reinforcement_note records the spine-wide `totals.uncovered=0` check (437/437 skills already n>=1) — no skill anywhere could satisfy the strict n==0 test; per the 2026-08-17 T1-10 reinforcement carve-out this downgrades to GAP, not BLOCKER, since D1/D2 genuinely force all six claimed Basic Operations/Factoring skills |
| T1-11 | PASS | learning-goal mutual reachability (0 unmapped, 0 unreachable) |
| T1-12 | PASS | T3 numeric load (prime factorization/GCF proof + probability-weighted cost comparison) matches declared tier |
| T1-13 | PASS | anchor ladder complete, 5 Socratic questions, trap named, 45-min timed plan, sensitivity note, SPEC §6 flag present |
| T1-14 | PASS | FACILITATOR.md agrees with case.md/case.json after adding `derived{}`; no orphan numbers |
| T1-15 | PASS | (no published/ yet — nothing to drift) |
| T1-16 | PASS | case_md_sha256 recorded below, matches this run |
| T1-17 | PASS | cohort_bands[] declared (Full/Compressed/1:1) |
| T1-18 | PASS | (no published/ yet — advisory) |
| T1-19 | PASS | (no published/ yet — advisory) |
| T1-20 | PASS | (no published/ yet — advisory) |
| T1-21 | PASS | (no published/ yet — advisory) |

BLOCKER (0). GAP (1, accepted — T1-10 reinforcement carve-out). POLISH: T1-07/15/18/19/20/21 all
note "no published/ directory yet" — expected, since `case-publish` is intentionally not run this
pass.

### Tier 2 — simulated play (6 probes, per task scope — P7/MCS-48 not in scope this pass)

Ran `python3 skills/case-readiness/scripts/tier2_probes.py --case the-equivalent-ledger [--probe N]`.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh, unbriefed subagent given only the leak-free packet chose B (The Full Factor), independently prime-factorized every coefficient (48=2⁴×3, 180=2²×3²×5, GCF=12; 54=2×3³, 96=2⁵×3, 240=2⁴×3×5, GCF=6), correctly noted the remaining trinomial 9n²+16n+40 is irreducible (negative discriminant), reproduced D3's table exactly (1,488/1,488; 6,600/6,600; 34,500/36,390, 5.48% gap), answered D4 using ONLY the factored forms (O(n)=12n(4n+15) forces O(0)=0; R(n)=6(9n²+16n+40) does not, so R(0)=240≠0 — "not the same expression"), and independently derived D5's $850.00 vs $783.04, 7.88% exactly matching `sensitivity_model.py`. Explicitly named the optimized metric (expected dollar cost) and reached the position via the proof, not by reasoning backward from D3's numbers alone — the correct route, not just the correct answer. |
| P2 both-sides | PASS | Independent fresh subagent built the strongest real case for each option from the packet alone. B is defensible on every axis (proof, numeric confirmation, cost). A is defensible only on a narrower, non-quantified operational-continuity ground (the 6-week freeze and hand-patching burden) once its two stated grounds (the two-batch match "proves" equivalence; A is cheaper) are shown false by D3/D4/D5 — the subagent explicitly judged A "close to a paper tiger on its stated grounds" but not a full collapse, since a real, unquantified freeze-cost argument survives. Neither side vanished entirely and the case's own $66.96/7.88% margin is real, not a manufactured artifact of an unbalanced setup. |
| P3 trap | PASS | Independent fresh subagent identified its own wrong path before reading FACILITATOR.md: a student who does D1-D3 correctly, finds the n=25 mismatch, and then answers D4 by citing that empirical mismatch as "proof" — smuggling sample-testing back in to answer a question the case explicitly designed to require a structural (factored-form-only) argument instead. On reading FACILITATOR.md, the subagent found the guide's headline "trap" (stopping at D3's two-point match) is largely foreclosed by the packet's own design (D3 forces evaluation at the untested n=25, so a careful student cannot miss the divergence) — but judged that Socratic Question 5 ("using only your D1/D2 factored forms, what is the one sentence that proves them wrong?") is clearly aimed at exactly the deeper trap the subagent found, concluding the two traps are effectively the same one, just not both named in "The trap" section's headline prose. Consistent with the-marginal-call's P3 precedent (a narrower independently-identified variant judged covered by the guide's existing mechanism, not an unanticipated gap) — no remediation required. |
| P4 twist | PASS (after 1 remediation round) | **First pass: FAIL on question 2.** An independent fresh reviewer confirmed the polynomial arithmetic at n=40 was correct and not fudged (O(40)=$84,000, R(40)=$90,480, $6,480/7.7% gap, independently re-derived) and that the twist genuinely invalidates a plausible Option A position (PASS on question 1) — but found `evaluate_twist()`'s `twist_nights_until_detected=4` multiplier existed only in backstage `case.json.derived`/`sensitivity_model.py`, with no mention anywhere a student in the room would actually hear, making the twist's headline $25,920 figure unverifiable from "the case's own stated assumptions" as read by a student (FAIL on question 2) — an unstated convention, BLOCKER-level per this probe's own rule, structurally the same class of defect the-marginal-call's P4 caught. **Fix applied:** FACILITATOR.md's Twist section rewritten so the facilitator explicitly STATES the "4 nights" figure to the room as new, disclosed information at the moment of the twist reveal — the same mechanism by which Appendix D's original MA8/MA9 figures were disclosed — rather than leaving it as a silent backstage parameter; `case.json.derived.twist_nights_until_detected_note` records the fix. A second, independent fresh subagent re-verified from scratch (did not read the first agent's report): independently re-derived the n=40 arithmetic and the twist recompute with no discrepancy, confirmed FACILITATOR.md's Twist section now explicitly instructs the facilitator to state the "4 nights" figure aloud to the room as new disclosed information (with a bolded line: "Say the '4 nights' number to the room explicitly... it must be stated as clearly as Appendix D's original figures were"), and confirmed PASS on both questions with no remaining unstated convention found. |
| P5 sensitivity | PASS (disclosed) | `sensitivity_model.py`, ±50% flex on the 3 declared FLEX[] dials (hours_per_engineer, p_defect, cost_of_error) confirmed by direct execution: base cost_A=$850.00, cost_B=$783.04, margin 7.88%, winner B. Three genuine, real instabilities found, each disclosed in `case.json.sensitivity_disclosure[]`: cost_of_error -50% ($12,500) flips to A ($425.00 < $783.04); p_defect -50% (1.7%) flips to A for the same multiplicative reason; hours_per_engineer +50% (12h) flips to A by raising cost_B to $1,174.56. This is a genuinely thin base margin (7.88%, inside the case's 5-10% target band) and it is honestly fragile under ±50% flex in three different directions — all three disclosed with real, non-generic justifications naming the exact flip mechanism, per the disclosure-aware PASS state (2026-08-13 doctrine), not a stable-margin PASS. D4's proof (whether O(n)/R(n) share a structural n-factor) is a fixed fact of MA1/MA2, correctly excluded from FLEX[] and not swept. |
| P6 data decay | PASS (after 1 correction) | All 3 cited URLs live-fetched on 2026-09-09 (same day as this QA run): S1 (BLS OEWS 15-1253, $48.94/hr, May 2023) confirmed present verbatim. S3 (Allytics Tech Perspectives) confirmed reachable, current, and carrying the quoted "you cannot run a global bank on a system built through probabilistic experimentation and AI hallucinations" passage. S2 (CodeRabbit): the originally-cited newsroom URL only carries the aggregate "~1.7x more issues" headline, not the specific "critical/major defects" and "logic/correctness +75%" breakdown claimed in the case — found during this same P6 fetch pass. **Fixed:** re-pointed S2's URL to CodeRabbit's own blog post of the same report (coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report), which does carry both figures verbatim ("AI PRs show ~1.4-1.7x more critical and major findings"; "Logic and correctness issues were 75% more common in AI PRs") — confirmed by direct fetch. Case.md, case.json, and RESEARCH_LOG.md all corrected from "up to 1.7x" to the precise "1.4-1.7x" range and re-pointed to the correct URL. All ages 0 days at time of this check; none 404'd; one source needed a URL correction to the same organization's more specific page, not a dead link. |

### Tier 3 — human dry-run

NOT RUN. Case is not published (case-publish intentionally not run this pass per task scope).

---

## Verdict

`qa.state`: **TIER2_PASS**. 0 Tier-1 BLOCKERs, 1 accepted GAP (T1-10 reinforcement carve-out).
Six Tier-2 probes recorded by name, 0 FAIL. `margin_pct` = 7.88%, inside the case's 5-10% target
band and SPEC §2's 20% cap. The case genuinely forces a factoring-based proof of structural
(non-)equivalence — confirmed independently by two separate fresh subagents (P1, P3) who both,
unprompted, arrived at the same structural argument (does every term of the factored form carry a
common factor of n) as the required proof method, and both explicitly flagged that answering from
D3's sample-test numbers alone is the trap, not the intended route.

**Next step:** `case-publish` (not run this pass, per task instructions) — or continue to Tier 2
probe P7 (MCS-48 accessibility cold-read) before publish, since P7 is part of the full
`case-readiness` ladder even though it was out of scope for this specific task run.

---

## P7 remediation run — 2026-09-10

**Integrity gap found:** the case had already reached `status: "published"` with `qa.verdict:
"PASS"` while `case.json.qa.tier2` carried NO "P7" key at all — not FAIL, not "NOT RUN", simply
absent. This is exactly the silent-pass failure mode this pipeline's own doctrine forbids (a probe
that has not been run must never be treated as passing by omission). This run closes that gap for
real, not by editing the field to say PASS without doing the work.

**Cold-read finding (prior round, informal, not filed in case.json):** a review of the published
`Interactive.html` found 7 real, unglossed real-world (non-math) terms a zero-background reader
would stumble on: **pull request**, **code-diff / diff**, **on-call engineer**, **QA** (the bare
abbreviation, never spelled out), **deployment ticket**, the **Confidence (HIGH/MEDIUM)** column on
the Sources table (never explained), and the **"Sensitivity"** column on the Modeling Assumptions
table (demonstrated by example throughout the table but never explicitly defined).

**Fix applied, to both `case.md` and `published/The Equivalent Ledger - Interactive.html`:**
- Added 5 new `STORY_GLOSSARY` entries (HTML) — `Pull Request`, `Diff`, `On-Call Engineer`, `QA`,
  `Deployment Ticket` — each with a plain-English `desc` and a real, live, verified Wikipedia
  `link` (`Distributed_version_control`, `Diff`, `Schedule_(workplace)`, `Quality_assurance`,
  `Issue_tracking_system` respectively; every link fetched and confirmed live and on-topic this
  session before use). These auto-link at first mention via the page's existing
  `autoLinkStoryGlossaryTerms()` mechanism (`#overview`/`#dilemma` containers) and also appear in
  the visible "Enterprise-Software Vocabulary" glossary box.
- Added matching inline parenthetical glosses to `case.md`'s Overview paragraph (diff, pull
  request, on-call engineer, deployment ticket) and Dilemma option A (QA), so the source document
  and the shipped artifact both explain these terms, not just the HTML.
- Added a short explanatory sentence near the Sources table/list (case.md Appendix E and the
  HTML footer) defining what HIGH vs. MEDIUM confidence means.
- Added a short explanatory sentence near the Modeling Assumptions table (case.md and HTML)
  defining what the "Sensitivity" column means in plain English.
- Re-ran `tier1_structural.py` after the edit: 0 BLOCKERs (`T1-16`/`T1-15` staleness introduced by
  the `case.md` edit resolved via `resync_artifacts.py` plus a manual `MANIFEST.json` mtime touch,
  since that file isn't in the resync script's glob; no content in any published artifact besides
  `case.md`/the interactive HTML needed to change). Same 1 accepted GAP (T1-10 reinforcement
  carve-out) as before, plus the pre-existing, unrelated T1-15 GAP on Facilitator Guide.docx's
  "7.3" figure (not touched — out of scope for this remediation).

**Fresh P7 cold-read (round 1, this run):** dispatched a genuinely fresh, zero-context subagent
with the instruction "you have no background in [Priya Chandran / Ledgerline's reconciliation
verification decision] — read this case as a student would" and had it **read the actual published
`Interactive.html` file directly** (not a text-extracted packet), per this skill's explicit
requirement. Result: all 7 originally-flagged terms confirmed to now have a working hover-glossary
entry, a visible "Enterprise-Software Vocabulary" box entry, or an inline parenthetical — the agent
found only **one** minor unexplained term, "Anchor 1" (a facilitation-protocol reference in a
Dilemma toolnote, unrelated to the case's math or its financial/software setting), and one
borderline non-blocking item ("excellent" words) it explicitly declined to count. **Verdict: PASS**
(1 unexplained concept, within the 0-1 pass bar) — no second remediation round needed.

**`case.json.qa.tier2.P7` updated:** `"PASS (after remediation — 7 terms glossed, re-verified by a
fresh cold-read; 1 residual minor unexplained term, 'Anchor 1', within the 0-1 pass bar)"`.
`qa.verdict` remains `"PASS"` and `qa.state` remains `"TIER2_PASS"` — this run fills in a field that
was wrongly missing, not upgrading a case that hadn't earned it; P7 has now genuinely been run and
genuinely passes. `qa.run_on` updated to 2026-09-10. Resynced via
`skills/case-readiness/scripts/resync_artifacts.py --case the-equivalent-ledger`.

No changes made to `readmodel/` or any other case's files. `case-publish` was not re-run, per task
scope — the case was already promoted and this remediation only corrects the QA record and the
already-published artifact's content.
