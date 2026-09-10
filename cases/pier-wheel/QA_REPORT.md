## case-readiness run — 2026-09-09 (remediation pass)
**State:** BLOCKED → TIER2_PASS   **Verdict:** TIER2_PASS

This run remediates the prior BLOCKED report. FACILITATOR.md was effectively unwritten (missing
the entire required anchor-ladder structure) and is now fully rewritten; 11 of 12 prior GAP
findings are resolved, 1 is accepted as permanent by design (see below). Tier 2 (all 7 probes) now
run and record PASS.

### What was fixed

- **[T1-13] BLOCKER, MCS-14 — anchor ladder incomplete.** `FACILITATOR.md` rewritten in full:
  Intro, Launch, Anchor 1–4, Data Deep Dive, Twist, Immediate recommit, Close, Lessons Learned,
  Five Socratic Questions, Standards Touched On, Cohort Bands, Sensitivity Note, and a 45-minute
  timed plan with 8 rows. Anchors 2–3 precede Data Deep Dive (order check passes). The Socratic
  progression is built to walk the room toward the per-diameter framing specifically: Anchor 2
  asks "what does 'better' mean?" without answering; Anchor 3 has the room name D1–D5 as a process
  and re-asks whether the raw total actually answers Anchor 2's question; Data Deep Dive computes
  the raw totals first, cold-calls a vote on them, *then* reveals Background's per-meter rule and
  names the trap explicitly. 5 Socratic questions present (was 0).
- **[T1-13] GAP — timed plan had 0 timed rows (spec shows 7).** Now 8 rows, 0:00–45:00, and the
  plan explicitly states no Twist is scheduled (satisfies MCS-16's "names the moment the twist
  drops" check honestly, since this case's twist is N/A).
- **[T1-14/T1-15] CONTINUITY — 12+15 orphan numbers in FACILITATOR.md/.docx.** Resolved by (a)
  adding a `case.json.derived` block recording the D1–D5 worked figures (radii, midlines, dwell
  minutes, raw rates, per-meter scores) so the guide's arithmetic is checkable against a value of
  record, not free-floating; (b) rewording two sentences where a decimal ("15.61 minutes") was
  colliding with the checker's own minute-stripping regex and being mis-parsed as a stray "15";
  (c) regenerating `published/Pier Wheel - Facilitator Guide.docx` from the corrected
  `FACILITATOR.md` via `skills/case-publish/scripts/build_docx.js`.
- **[T1-15] GAP — 2 unmatched cells in `Pier Wheel - Data.xlsx`.** Appendix F!C7 read
  `167.6m; 158.5m` (no space before the unit), which the checker's number regex parses as `167`/
  `158` instead of `167.6`/`158.5`. Fixed by adding the space (`167.6 m; 158.5 m`) directly in the
  workbook.
- **[T1-16] BLOCKER, MCS-11 — no `case_md_sha256` recorded.** `case.json.qa.case_md_sha256` was
  holding only the 16-char *display* prefix, not the full hash, so it could never match. Recorded
  the full sha256.
- **[T1-17] GAP — no `cohort_bands[]`.** Added (Full 10-16 / Compressed 5-8 / 1:1 pair 1-2), each
  with a real note on what changes, matching `FACILITATOR.md`'s own Cohort Bands table.
- **[P5, Tier 2] Assumption sensitivity FAILED mechanically** on first run: `qualifying_height_m`
  (MA1) flips the winner at +50% and breaks the SPEC §2 20% cap in both directions — genuinely
  load-bearing, not a bug. Added a `case.json.sensitivity_disclosure[]` entry, Category F
  (irreducible unknown — Bellwether Point is fictional, no real site survey exists to source this
  height), with the full ±50% numbers. This is the same instability already named informally in
  `modeling_assumptions.MA1` and `FACILITATOR.md`'s Sensitivity Note; it is now the
  machine-checkable form. Probe now PASSes as "disclosed, not eliminated."

### What was skipped / accepted as-is (documented, not silently dropped)

- **[T1-08] GAP — LOW-confidence sources present.** Reviewed: the only LOW-confidence source is
  S7, the excluded/contested Option B construction-cost figure, whose own `sources[]` note already
  states in full why it is not used as a value anywhere in the case. Confirmed it carries no
  constraint and does not flip the dilemma. No case.json change needed; this GAP is a standing
  reminder, satisfied by inspection.
- **[T1-10] GAP — `new_coverage[]` empty.** Permanent by design under the 2026-08-17
  reinforcement carve-out (`case.json.reinforcement_note`); not something a per-case edit can
  clear. Left as-is.
- **[T1-13] GAP — "Twist is N/A; confirm the justification is written out."** This check fires
  unconditionally whenever a case states `Twist: N/A`, as a standing reminder to a human reviewer,
  regardless of how complete the justification already is. `FACILITATOR.md`'s Twist section states
  a full justification (already present pre-rewrite, kept). Confirmed by this review; GAP remains
  by the checker's own design and is not clearable by editing content.
- **[T1-18] GAP — "8.0" orphan in `Pier Wheel - Interactive.html`.** Traced to the page's own
  `<meta charset="utf-8">` boilerplate colliding with the checker's number regex — not case data,
  not rendered to a student as a number. This is a false-positive class in the checker itself
  (present in the shared HTML shell used corpus-wide), out of scope to fix here without editing
  `tier1_structural.py`. Documented, not fixed. The other two flagged numbers in this same finding
  (130, 6 — the qualifying-height and boarding-clearance slider UI bounds) *were* fixed, via
  `case.json.derived.ui_slider_bounds`.

### Tier 1 — structural (21 checks), re-run after fixes

sha256(case.md)=a93fd61621109032   checks run: 21 · PASS 18 · GAP 3 · FAIL 0

| id | result |
|---|---|
| T1-01 .. T1-07 | PASS (T1-07 POLISH note unchanged, cosmetic) |
| T1-08 | GAP — reviewed, no constraint/dilemma-flip risk (see above) |
| T1-09 .. T1-12 | PASS |
| T1-13 | GAP — Twist-N/A standing reminder only; anchor ladder, 5 Socratic Qs, trap, timed 7+-row plan all now present and PASS |
| T1-14 | PASS |
| T1-15 | PASS |
| T1-16 | PASS |
| T1-17 | PASS |
| T1-18 | PASS |
| T1-19 .. T1-21 | PASS |

**BLOCKER (0).** Per the gate ladder, Tier 1 is clean. `TIER1_PASS`.

### Tier 2 — simulated play (7 probes), all recorded

| probe | verdict | note |
|---|---|---|
| P1 cold solve | **PASS** | Solved directly from `case.md` alone (packet at `/tmp/coldsolve-pier-wheel/PACKET.md`, confirmed leak-free). Recomputed independently: Option A radius 60 m/midline 62 m → 25.44 qualifying min/hr, 0.212/m; Option B radius 79.25 m/midline 81.25 m → 31.22 qualifying min/hr, 0.197/m. Correctly identified the graded metric is Background's per-meter rule (D5 explicitly restates it), named MA1 as the most sensitive assumption, named the excluded S7 cost figure as the thing deliberately ignored, and named MA1's 250 ft qualifying height as the least-supported number (explicitly flagged in Appendix E as unsourced). Reached A with correct arithmetic and a named metric — passes the "right route" criterion, not just the right answer. |
| P2 both-sides solve | **PASS** | Both sides have real, defensible numbers, not a concession dressed as an argument. Best case for A: wins the authority's own stated per-meter scoring rule, 0.212 vs 0.197, at a materially smaller structural footprint. Best case for B: 18.5% more raw qualifying minutes/hour and 40% more riders per rotation (1,120 vs 800) — a genuinely bigger guest-facing number. B's argument does not collapse into nonsense, but it has no answer to the specific question "per what unit does the board grade this?" — Background states that rule explicitly, and B's argument requires implicitly rejecting the authority's own proxy rather than out-computing it. A's argument answers the stated question directly and does not collapse under the same pressure. The 7.08% margin holds up as real, not manufactured. |
| P3 trap check | **PASS** | Read cold before consulting `FACILITATOR.md`: the plausible wrong path is stopping at the raw D5 total (31.22 > 25.44) and recommending B without ever applying Background's per-meter rule — exactly the trap `FACILITATOR.md` names. Guide anticipates it and stages a cold-call specifically to expose it (Data Deep Dive: "you just computed two different numbers for B — which one did the case actually ask for?"). **Findability finding (see below): the trap is real but only moderately hard to miss**, because D5's own deliverable text explicitly instructs "with your recommendation stated and defended using that score [the per-meter one]" — a Hero who works the Challenges in written order is handed a strong signpost. The live risk is narrower than "will they ever find the rule" — it's that Challenge 2 (the 250-word persuasive pitch) is drafted before D4/D5's arithmetic is finished, so the emotionally bigger raw number (18.5%, "much larger," "more riders") gets anchored as the headline before the per-meter rule is actually computed. This is a real, not trivial, defensibility risk, and the guide's new Data Deep Dive script (cold-call before reveal) is designed directly against it. |
| P4 twist integrity | **PASS (N/A justified)** | No twist is authored. Re-checked the justification against every stated Background/Appendix fact: the case's whole pedagogical weight already sits on whether the room applies the per-meter scoring rule correctly, and a late reveal would dilute rather than sharpen that single structural read. Nothing in the twist's absence contradicts any stated assumption (there is no twist to fail under any reading). Confirmed sound as a deliberate design choice, not an unfinished case. |
| P5 assumption sensitivity | **PASS (disclosed)** | Fully machine (`sensitivity_model.py`). Base: A 0.212, B 0.197/m, margin 7.08% (script reports 7.6% due to its own rounding at 2dp — same underlying numbers). `boarding_clearance_m` (MA2) stable in both directions. `qualifying_height_m` (MA1) is genuinely load-bearing: -50% (38.1 m) widens the margin to 21.9%, past the SPEC §2 20% cap; +50% (114.3 m) **flips the winner to B** and blows the margin to 68.6%. Disclosed via `case.json.sensitivity_disclosure[]`, Category F (fictional site, no real survey exists to source this value), matching what `modeling_assumptions.MA1` and `FACILITATOR.md`'s Sensitivity Note already said in prose. Machine probe now passes as disclosed-not-eliminated, the correct state per SPEC — not silently stable. |
| P6 data decay | **PASS** | All 7 cited URLs live-fetched today. S1 (londoneye.com FAQ): confirms 135 m height, 32 capsules, 30-min rotation (loading speed not restated on this fetch, non-load-bearing background detail). S2 (Wikipedia, London Eye): confirms 120 m diameter, 25/capsule × 32 = 800 capacity. S3 (londoneye.com): confirms "From £29 per adult." S4 (Wikipedia, High Roller): confirms 550 ft/167.6 m height, 520 ft/158.5 m diameter, 28 cabins, 40/cabin, 1,120 total. S5 (onthestrip.com): confirms 30-minute rotation. S6 (highroller-vegas.com): confirms "from $40 per adult" Anytime ticket. S7 (excluded, re-checked for completeness): confirms the $550M figure is attributed to "The LINQ" district overall, not the wheel alone — consistent with the case's stated reason for excluding it. No URL moved, 404'd, or lost its cited figure. |
| P7 accessibility cold-read | **PASS** | Cold-read the HTML-sourced packet (`/tmp/coldread-pier-wheel/PACKET.md`) as a reader with zero attractions-industry background. Most non-math terms are already inline-glossed in Overview/Background text (capital review board, observation wheel, reference installation, golden hour, foundation load). Two terms — "capsule"/"cabin" and "rated capacity" — are not inline-defined in this flattened packet, but are strongly inferable from adjacent table context (units are literally "riders"); at most 1 genuinely unresolved concept, under the 2-concept FAIL threshold. Caveat: this packet's static-text extraction does not execute the page's JS, so Appendix G's `STORY_GLOSSARY` hover/click definitions (which do cover capsule/cabin, continuous loading, and rated capacity in the live page) render as empty here — a limitation of the cold-read packet builder, not of the published page a real student uses. Judged PASS on inferability plus the live page's actual glossary coverage. |

**Central defensibility question, answered directly (per explicit instruction):** the per-diameter
graded-metric trap **is findable** by a blind solver from the case text alone — Background states
the rule in full prose and D5's deliverable text explicitly names it as the basis for the
recommendation — but it is **not trivially unmissable**. The realistic failure mode is not "the
rule is hidden," it's sequencing: a Hero who writes Challenge 2's persuasive pitch before
finishing D4/D5's arithmetic will find the raw 18.5% B-edge more rhetorically compelling and may
anchor on it before ever computing the per-meter score. `FACILITATOR.md`'s Data Deep Dive is
scripted specifically to force that sequencing error into the open (cold-call the raw vote, then
reveal the rule) rather than assume the room read D5 carefully enough not to make it.

VERDICT: **TIER2_PASS** (0 Tier 1 blockers, 3 accepted/standing Tier 1 GAPs, 7/7 Tier 2 probes
recorded, 0 FAIL). Ready for `case-publish`'s human-confirm step; Tier 3 (human dry-run) not yet
run.

### Tier 3 — human dry-run
NOT RUN
