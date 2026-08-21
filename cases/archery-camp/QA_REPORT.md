## case-readiness run — 2026-08-19
**State:** DRAFT → TIER1_PASS → TIER2 run (see verdict)   **Verdict:** TIER1_PASS (Tier 2 did not clear — P3 FAIL)

### Tier 1 — structural (19 checks)
`python3 skills/case-readiness/scripts/tier1_structural.py --case archery-camp`
sha256(case.md) = e103aed156df9e7d... (matches `case.json.qa.case_md_sha256`)

| id | result |
|---|---|
| T1-01 | PASS |
| T1-02 | PASS |
| T1-03 | PASS |
| T1-04 | PASS |
| T1-05 | PASS |
| T1-06 | PASS |
| T1-07 | PASS (POLISH: 11 labels parsed, 6 bulleted + 5 separator-run) |
| T1-08 | PASS |
| T1-09 | PASS |
| T1-10 | PASS |
| T1-11 | PASS |
| T1-12 | PASS |
| T1-13 | PASS |
| T1-14 | GAP |
| T1-15 | GAP |
| T1-16 | PASS |
| T1-17 | PASS |
| T1-18 | GAP |
| T1-19 | PASS |

**BLOCKER (0):** none.

**GAP (3):**
- [T1-14] CONTINUITY — 1 number in `FACILITATOR.md` appears in neither `case.md` nor `case.json`: `152.0` (Guide Notes says "152.44 people means 153" — the `152` half-token isn't itself in `derived{}`; only `option_a_attendance_for_target_exact: 152.44` and `option_a_attendance_for_target: 153` are). Either treat as guide-only prose (152 is just half of "152.44" written out) or add explicitly to `derived`.
- [T1-15] CONTINUITY — 2 numbers in the published `.docx` Facilitator Guide (`45.0`, `152.0`) appear in neither source. Same root cause as T1-14 plus a `45` (likely the 45-minute Socratic plan header) that isn't itself a case fact.
- [T1-18] CONTINUITY — 30 numbers in `Archery Camp - Interactive.html`'s prose/markup appear in neither `case.md` nor `case.json` (a run of small decimals — `0.01, 1.4, 1.55, 1.6, 2.4, 2.5, 3.4...` — consistent with the CSS/SVG-decimal class this project already treats as decorative, but not individually re-confirmed here).

**POLISH (1):** [T1-07] — informational, not actionable.

None of these are BLOCKERs; `TIER1_PASS` holds as of this run (0 blockers, 3 gaps — up from the 1 gap recorded in `case.json.qa` at the last Tier 1 run, still 0 blockers).

### Tier 2 — simulated play (6 probes)

`sensitivity_model.py` authored this run (`cases/archery-camp/sensitivity_model.py`). Reproduces the case's own published numbers exactly: Option A $117.44/participant (13 ranges, 156 capacity), Option B $129.09/participant (15 ranges, 180 capacity), margin 9.92%, D5 = 152.44 → 153 (exceeds Karen's 150-person ceiling), twist total demand 300 / Option A shortfall 144 / Option B shortfall 120. `FLEX = ["planned_attendance"]` only — the sole numeric figure Appendix C actually labels an Assumption (140); every dollar figure, rate, range count, and the twist's 160-surge are cited/given data per Appendix A/B/C/Background and are correctly out of scope for P5 per SPEC §2.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | A genuinely fresh subagent, given only the leak-free student packet, chose Option A, correctly reproduced every published figure ($117.44, $129.09, D4=126, D5 exact 152.44 → 153 rounded up, correctly flagged as exceeding the 100–150 ceiling), named its optimized metric (per-participant charge vs. the board's $110 target) explicitly "tempered by a secondary check on max capacity," and used exactly that capacity tension as its own strongest counter-argument — i.e., it reached the case's intended answer via the case's intended reasoning, not by luck. It also independently flagged the $26.30/attendee equipment estimate as the least-supported number, an observation this report agrees with (see P6/legacy_conversion_note). |
| P2 both-sides | **PASS** | Built independently from the packet: Argument A — $117.44/participant, 9.92% cheaper, 156-capacity comfortably clears the stated 150 ceiling. Argument B — $129.09/participant but 180 capacity (24 more seats than A), material given the camp's own stated growth (10 → 50+ attendees over 4 years) and directly vindicated by the twist (300 total demand; A short 144, B short 120). Neither side is numbers-free or a bare concession; neither collapses. Genuine additional finding, not a FAIL trigger but worth surfacing: **neither option actually clears the board's own $110/participant target at the 140-attendee planning figure** (A is $7.44 over, B is $19.09 over) — the case's own D5/D6 chain already surfaces this for Option A, but it is not stated anywhere that Option B misses the target by an even wider margin; a pitch for B on capacity grounds could quietly imply it also meets the board's cost goal, which it does not, and neither Challenge 2 nor D6 explicitly forces a Hero to check that. |
| P3 trap | **FAIL** | `FACILITATOR.md`'s named trap ("computes the per-participant charge, finds Option A cheaper, and stops — never checking either option's maximum capacity") failed the machine pre-screen (the description doesn't use an actual wrong-doing verb the checker recognizes — "stops" / "never checking" vs. the checker's `never notice/assumes/forgets/misses/skips` list; a real but narrow wording gap, not dispositive on its own). More substantively: a second fresh subagent, given only the packet and asked to name the single most plausible wrong path cold, did **not** converge on capacity-blindness at all. It independently centered on **D5's break-even algebra** as the real trap — and, tellingly, got its own prediction wrong in exactly the way that makes the point: it asserted that "a higher attendance, still within the 100–150 range... does bring Option A under $110," which is false (the true break-even is 153, one above the stated 150 ceiling; at n=150 exactly, Option A is still $111.36, per `derived.option_a_per_participant_at_150` — confirmed independently by `sensitivity_model.py`). That a competent cold reader converged on this specific wrong belief is itself evidence D5's rounding/ceiling interaction is a live trap the guide does not name as "the trap" (the Data Deep Dive section does separately coach the ×3 rental-day multiplier and round-up-not-nearest points, but only as computational checkpoints inside the walkthrough, not badged as *the* trap the way the capacity-blindness path is). Two independent traps exist in this case and the guide anticipates and names only one of them. Per doctrine ("a trap the guide has not anticipated is a FAIL even if the case is sound"), this is a FAIL. **Not a case defect to fix here** — see "Never fix the case"; the fix (adding the D5 break-even/rounding trap to `FACILITATOR.md`'s Trap section, or its own explicit Socratic question) belongs to `case-write`. |
| P4 twist | **PASS** | (1) Does the twist invalidate a position a room would hold? Yes — a room that voted A purely on the 9.92%-cheaper cost figure has to reconcile that A turns away *more* campers (144 vs. 120) than B under the surge, which is exactly the tension P1's own subagent pre-empted by weighing capacity from the start. (2) Does it survive the case's own stated assumptions read the way a student would? Yes on both: Assumption 1 (140-attendee planning figure fixes the cost model) is never contradicted — nothing in the twist re-bills at the surged headcount, so the per-participant figures from D3/D5 stay exactly as computed; the twist operates in a genuinely separate dimension (capacity, already present as `max_capacity` for both options pre-twist) rather than reopening the cost arithmetic. Assumption 2 (a field's range count — and therefore capacity — is fixed regardless of actual attendance) is exactly what makes the shortfall real and not reducible by relabeling ranges. `sensitivity_model.py`'s mechanical check confirms the winner flips: `evaluate()` (cost lens) picks A; `evaluate_twist()` (post-surge campers served) picks B, 180 > 156 — a genuine, mechanically-verified flip, not merely an assertion. |
| P5 sensitivity | **PASS** | Fully machine (`tier2_probes.py --probe 5 --flex 0.5`). The one declared assumption, `planned_attendance` (140), was flexed to 70 and 210: winner stays A at both extremes (margin 10.1% at −50%, 8.2% at +50%), never breaches the SPEC §2 20% cap. This is structurally guaranteed, not coincidental: Option A's fixed cost ($12,759) is strictly lower than Option B's ($14,391) regardless of headcount, and the $26.30/attendee equipment cost is identical for both options at any given attendance, so the ranking A-cheaper-than-B cannot flip for any positive `planned_attendance` value — the case's own primary verdict is genuinely robust to this assumption, not merely untested. |
| P6 data decay | **PASS** | All 4 live URLs in the case fetched and reachable, values still supported. `case.json.sources[]` S1 (City of Boise — Simplot Sports Complex, accessed 2026-08-04, 15 days old): reachable, page confirms "a 161-acre large special use area," matching the claim. Also checked, beyond the formal `sources[]` list, the 3 further links `case.md` Appendix D calls "real, live resources as of 2026-08-18" (not tracked in `case.json.sources[]`, so not required by the mechanical worklist, but load-bearing for the case's own factual claim): USA Archery Safety (reachable, 0.57/1,000 injury-rate figure and coach-certification content present), Archery360 Ultimate Beginner's Guide (reachable, covers bow types/equipment/local programs as claimed), Math Is Fun Combinations & Permutations (reachable, covers the counting method D4 needs). No dead links, no drifted figures. **Finding, not a BLOCKER:** 3 of the case's 4 live-resource claims (Appendix D) have no corresponding `case.json.sources[]` entry — they're correctly out of scope for T1-08's citation check (they aren't cited numeric facts, just further-reading links) but also outside this probe's formal worklist; recommend adding lightweight `sources[]` rows for them if the "verified as of 2026-08-18" claim in `case.md` is meant to be an auditable one going forward, not a one-time claim nobody re-checks. |

### Tier 3 — human dry-run
NOT RUN.

---

**TIER2_PASS was NOT reached.** P3 (trap check) is a genuine FAIL: the guide names and coaches for a capacity-blindness trap, but an independent cold read converged on a different, real trap (D5's break-even/rounding interaction against the stated 100–150 ceiling) that `FACILITATOR.md` never badges as "the trap" and has no dedicated Socratic question for. Five of six probes (P1, P2, P4, P5, P6) PASS. This is not a defect QA may fix — the case document, `FACILITATOR.md`, and `case.json` were not modified beyond this report and the `qa` block below.

---

## Remediation run — 2026-08-20

**Change made:** edited `FACILITATOR.md`'s Trap section only (facilitator-only file; `case.md` was
**not** touched — the trap stays out of the student packet per house doctrine). Verified the
underlying figures against `sensitivity_model.py`/`case.json.derived` first: Option A's true D5
break-even is exact `152.44` → rounded up `153` whole attendees (`option_a_attendance_for_target` /
`_exact`), and Karen's stated planning ceiling is `150` — 153 > 150 confirmed independently by
re-running `sensitivity_model.py`'s `solve_d5_target_attendance()`, matching `case.json.derived`
exactly.

The old single "The trap" paragraph (capacity blindness only) was split into two explicitly badged
traps:
- **Trap 1 — capacity blindness** (the original trap, reworded slightly — "misses ... never
  notices ..." — so the machine pre-screen's wrong-doing-verb check, which was *also* silently
  failing this case before today per the P3 finding above, now recognizes it as a real trap
  description and not a difficulty note).
- **Trap 2 — the D5 break-even/rounding trap** (new): names the exact failure mode P3 found —
  a Hero who does not round `152.44` up to `153`, or who never checks `153` against the stated
  150-person ceiling, will falsely believe an in-range attendance number clears the board's $110
  target, when the true break-even actually sits one whole attendee above Karen's own ceiling.

Also added Socratic question 6, directly forcing the rounding-up step and the 153-vs-150 ceiling
check.

Rebuilt `published/Archery Camp - Case Study.docx` and `published/Archery Camp - Facilitator Guide.docx`
via `node skills/case-publish/scripts/build_docx.js archery-camp` (student docx is byte-for-byte
unaffected since `case.md` is unchanged — hash `e103aed15...` matches before and after; only the
facilitator docx content changed) — required to clear T1-15's staleness check after editing
`FACILITATOR.md` (this is the same corpus-wide mtime-staleness class fixed across 28 other packets
in `7e8e230`, not a new bug).

### Tier 1 re-run
`python3 skills/case-readiness/scripts/tier1_structural.py --case archery-camp` → **TIER1_PASS**,
0 blockers, 3 gaps (T1-14, T1-15, T1-18 — unchanged from the prior run; same pre-existing
guide-only-figure/decorative-decimal continuity gaps, not new).

### P3 re-verification
Regenerated the leak-free student packet via `tier2_probes.py --case archery-camp --probe 1`
(`/tmp/coldsolve-archery-camp/PACKET.md`). The mechanical trap-verb pre-screen
(`tier2_probes.py --probe 3`) now returns **READY** (was FAIL before the reword).

Two independent, genuinely fresh subagents (Agent tool, `general-purpose`, no access to
`FACILITATOR.md` or any file but the packet) were asked cold to name the case's most plausible
wrong path:

1. **First agent** (full solve + wrong-path naming): reached the correct answer (Option A, D5 =
   152.44 → 153, correctly flagged as exceeding the 150 ceiling), then named as its top wrong path
   "forgetting to ×3 the daily field rental" — explicitly traced through to show it corrupts D5's
   fixed cost and flips the break-even from 153 (outside range) to a false 141 (inside range),
   producing exactly the false belief category the original P3 finding flagged: a student
   concluding an in-range attendance number clears the $110 target. Named a second wrong path
   (sizing counselors off attendee headcount instead of rented ranges, contra Assumption 2).
2. **Second agent** (trap-naming only, facilitator-style reasoning, no full solve required):
   independently converged on the *same* top wrong path — the ×3-day field-rental omission —
   again explicitly tracing it to the 153-vs-141 D5 flip, and named it as the trap most likely to
   "catch the room" over the range-sizing alternative, because nothing in the packet flags the
   per-day unit the way Assumption 2 flags the range-count convention.

**Comparison against the updated guide:** both fresh reads center on the same underlying failure
mode already covered by `FACILITATOR.md` in two places — the pre-existing Data Deep Dive paragraph
("dropping that multiplier produces a deceptively plausible near-$110 number... cascade straight
into a wrong D5 answer... cold-call for the ×3 step specifically") and the new Trap 2 paragraph plus
Socratic Q6 (the general false-in-range-belief pattern and the 153 > 150 finding). The second wrong
path both agents raised (range-count vs. attendee-count for counselor sizing) is separately
anticipated by Anchor 4's explicit surfacing of Assumption 2. Unlike the original failing run,
neither fresh agent converged on a wrong path the guide fails to anticipate.

**P3 verdict: PASS.**

### Other probes
P1, P2, P4, P5, P6 were not re-run mechanically this session — none of their inputs (`case.md`,
`case.json`, `sensitivity_model.py`) changed; only `FACILITATOR.md` (facilitator-only) and the two
`published/` docx files were touched. Their prior PASS verdicts stand unaffected.

**TIER2_PASS reached.** All six probes now PASS: P1 PASS, P2 PASS, P3 PASS (this run), P4 PASS,
P5 PASS, P6 PASS. `qa.state` promoted to `TIER2_PASS` below.
