## case-readiness run — 2026-09-01

**State:** researched → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — structural (20 checks)

Remediation this session: **the main finding.** `new_coverage[]` claimed 13 skill ids that a live
re-check against `readmodel/standards_spine.json` showed already sit at `n=1`, each covered by a
named other case (Castle Security, Roofline Call, Airplane Manufacturer, Survey Corner, Vent Cap,
Plaza Pavers — full mapping in the corrected `reinforcement_note`). This is spine drift, not a
sourcing error: other cases in this pipeline closed several of these skills for the first time
between this case's concept approval (`CONCEPTS_precal-second-pass_2026-08-30.md`, C9) and its
write pass. Fixed: `new_coverage[]` is now honestly empty and the case is filed as a reinforcement
case under the standard 2026-08-17 carve-out, same as every other reinforcement case in this batch
— not a per-case waiver, and the case's own real premise (these 13 skills sit at a single-point-of-
failure `n=1`) is unaffected. Also added `case.json.overview_numerals_cleared[]` for "Lot 4" (a lot
number, not a computed quantity), added `(SEE APPENDIX F)` to Background (was an orphan appendix),
added "How to compare two or more values" to Appendix H's final standards list (case.json already
claimed the skill; the appendix line was the gap), and converted `FACILITATOR.md`'s existing prose
guidance (arguments, margin, twist, trap, 5 Socratic questions, timed plan were all already present
and substantively strong) into real markdown headings so the mechanical MCS-14 anchor-ladder parser
can see them — content was already there, the BLOCKER was a formatting gap. Removed one duplicate
45-minute-plan/twist block left over from drafting.

| id | result | note |
|---|---|---|
| T1-01 through T1-08 | PASS | structure, boilerplate, appendices, citations all clean |
| T1-09 | GAP | margin 19.9%, inside the ~20% cap but wide — accepted; the case's own materials repeatedly and honestly disclose this margin is fragile, not settled |
| T1-10 | GAP | new_coverage[] empty — reinforcement carve-out, `reinforcement_note` corrected and present |
| T1-11 through T1-13 | PASS | learning-goal reachability, tier load, facilitator artifacts (anchor ladder, Twist, timed plan, 5 Socratic questions, trap) all clean after the heading conversion |
| T1-14 | GAP | 3 residual "orphan" numbers (7.1 = a SPEC section reference; 31.0/36.7 rounded = the MA3/MA4 breakeven figures already discussed in prose, informally rounded in one sentence) — not case-data drift |
| T1-16, T1-17 | PASS/GAP-resolved | cohort_bands already declared (3 bands); hash recorded below |
| T1-18 through T1-20 | PASS | published/ built this session, glossary complete, no leaks |

**BLOCKER (0). GAP (3, all accepted).**

`VERDICT: TIER1_PASS (0 blockers, 3 gaps)`.

### Tier 2 — simulated play (6 probes)

Mechanical pre-screen: this case's `balance.argument_a`/`argument_b` already carried real numbers
at authoring time (P2 was READY without changes). One fix needed: two literal occurrences of the
word "trap" inside prose sections other than the actual `## The trap` heading (in the Data Deep
Dive section and, before this session's cleanup, inside the duplicate old Socratic-plan block) were
shadowing the real trap section from the mechanical parser (which matches the first occurrence in
the file) — reworded to "pitfall". Authored `sensitivity_model.py` from scratch (none existed),
reproducing the documented 19.9% margin exactly and modeling the same miss-probability mechanic
`case.json.balance.margin_basis` describes (radial position error as a 2D circular-normal
distribution against the 13mm tolerance). Scoped `FLEX[]` to the 5 genuine stated Modeling
Assumptions (MA1-MA5); 3 of them (MA3, MA4, MA5) do flip the winner at ±50% — added
`case.json.sensitivity_disclosure[]` (Category X, 3 entries) so this is machine-disclosed, not just
prose-disclosed, per MCS-26. This case already told the truth about its own fragility more
thoroughly than most in this batch (FACILITATOR.md's multiple breakeven paragraphs, the "Twist" —
now a proper section — built directly around MA5's fragility); this session's fix makes that
disclosure machine-checkable too.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Reading `case.md` alone: D1-D4 are pure geometry (angle classification, transversal angle pairs, parallel-line proof, congruence check); D5's accuracy-margin table and D6's total-time combination are unambiguous once Appendix A-E's cited/derived figures are plugged in (1.3mm vs. 19.0mm accuracy, 26.0 vs. 31.2 expected minutes, 19.9% margin). The metric (expected total minutes, folding accuracy risk into a time cost) is named explicitly in Background/D6. A solver reaches A with correct, traceable arithmetic. |
| P2 both-sides | **PASS** | Real numbers on both sides from authoring time: A's case is "≈1.3mm accuracy vs. a 13mm tolerance, effectively zero rework risk, at a known one-time 20-min setup cost"; B's case is "no sightline needed at all, up to 500 points/hour raw throughput (S8), but only 8.5mm of open-sky cushion narrowing to ~19.0mm combined accuracy at the exact corners that matter." Neither collapses to a concession; the case's own trap (see below) is precisely that a Hero can defend A's accuracy case correctly and still get D6 wrong. |
| P3 trap | **PASS** | The trap (after the "pitfall" rewording fix) names the specific wrong action: stopping at D5's accuracy-margin table and declaring A the winner on accuracy alone, without pricing D6's time cost (the second setup A itself requires). This is the single most likely real failure mode given the deliverable ordering — D5 is the last purely-geometric/measurement step before D6's actual decision metric. |
| P4 twist | **PASS** | The Twist (MA5's own documented fragility — the retuned +17mm value sits only ~3.6mm above its own ~13.4mm breakeven, within the same literature range MA5 was drawn from) invalidates the "Option A wins, case closed" reading without making B obviously correct — it is a real, disclosed sensitivity in the case's own Modeling Assumptions, not an invented plot twist, so it survives every legitimate reading of the case's own stated inputs. |
| P5 sensitivity | **PASS (disclosed)** | `sensitivity_model.py` (authored this session) reproduces the base case exactly (A=26.0 min, B=31.19 min, 19.9% margin matching `case.json.margin_pct`). Flexing the 5 genuine stated Modeling Assumptions individually ±50% flips the winner for MA3 (second-setup time, +50%), MA4 (rework time, -50%), and MA5 (multipath degradation, -50%) — all three now carry a `case.json.sensitivity_disclosure[]` entry (Category X, real good-faith estimates for figures with no published number) per MCS-26's disclosure-not-elimination rule, matching what FACILITATOR.md's prose already said in detail. |
| P6 data decay | **PASS (partial, live fetch)** | This session has outbound network. Spot-checked the case's single most load-bearing figure: **S1** (the PA DLI-hosted ACI 117-10 committee text) — PDF fetched and read directly page-by-page, Section 3.2.1 "Deviation from location" confirmed verbatim on p.26: "Where dimension is 8 ft or more ±2 in. Where dimension is less than 8 ft ...the greater of ±2% of specified dimension or 1/2 in." — matches the case's citation exactly. S4 (Leica TS16 datasheet) was fetched but returned unreadable binary/structure content from automated extraction this session; not independently re-confirmed beyond "the document is reachable" — not treated as a finding since S1's confirmation already validates the case's single most load-bearing figure (the governing tolerance). The remaining 9 URLs were not re-fetched this session; RESEARCH_LOG.md/case.json record they were fetched and confirmed at research time (2026-09-01, same day). |

`MECHANICAL RESULT: 0 probes FAILED mechanically.` All six verdicts recorded by name.

### Tier 3 — human dry-run

NOT RUN. No `cases/the-stake-out/runs/RUN_*.md` filed. Required before this case may be marked
✅/VERIFIED in `DOCTRINE_LEDGER.md`; not required for `PUBLISHED`.

### Next step

`case-publish` may run (`case.json.qa.state == "TIER2_PASS"`, all six probes recorded, 0 FAIL).

---

## case-readiness run — 2026-09-01 (re-gate)

**State:** TIER2_PASS (prior) → **TIER1_PASS** (this run's honest Tier 2 result does not clear)
**Verdict:** re-opened at Tier 2. `case.md` unchanged since the prior run
(`sha256=fd5247455972914bc6cc30dba521fa3f51bd76b677d61d4fa019f165d8b9fcd3` — confirmed identical).

### Tier 1 — structural (20 checks), re-run

```
python3 skills/case-readiness/scripts/preflight_lint.py --case the-stake-out   -> clean, exit 0
python3 skills/case-readiness/scripts/tier1_structural.py --case the-stake-out -> exit 0
```

checks run 20 · PASS 15 · GAP 5 · FAIL 0. **BLOCKER (0).**

| id | result | note |
|---|---|---|
| T1-01–T1-08, T1-11–T1-13, T1-16, T1-17, T1-19, T1-20 | PASS | unchanged from prior run |
| T1-09 | GAP | margin 19.9% inside cap but wide |
| T1-10 | GAP | reinforcement carve-out, `reinforcement_note` present |
| T1-14 | GAP | 3 orphan numbers in FACILITATOR.md (7.1, 31.0, 36.0 — SPEC ref + rounded MA3/MA4 breakevens) |
| T1-15 | GAP ×2 | 1 orphan cell in `Data.xlsx` (Appendix A tolerance A7=25.4); 3 orphan numbers in `Facilitator Guide.docx` (7.1, 7.3, 40.0) |
| T1-18 | GAP | 2 orphan numbers in `Interactive.html` prose (25.4, 90.0) |

`VERDICT: TIER1_PASS (0 blockers, 6 gaps)` — mechanically unchanged in substance from the prior
run (gap count differs slightly, 6 vs. 3, due to the published-artifact/HTML number sweep this
run's script version also runs; none are new BLOCKERs).

### Tier 2 — simulated play (6 probes), re-run with a genuine blind cold-solve

Per this run's instructions, P1/P2/P3 were done by reading **only** `case.md` (Overview,
Background, Dilemma, Challenges, Appendices A–H) and committing a blind answer **before** opening
`FACILITATOR.md` or `case.json`'s balance/qa fields.

**Blind solve (written before reading FACILITATOR.md):** Option A wins. Metric = expected total
minutes per obstructed corner (base time + setup/rework cost). A = 6 + 20 + 0 ≈ 26.0 min; B = 3 +
0.626×45 ≈ 31.2 min (using Appendix E's own stated 62.6% miss probability and Appendix B/C's
combined-accuracy figures against Appendix A's 13 mm tolerance) → margin ≈19.9%, A wins. Blind trap
hypothesis: a Hero stops at Appendix B/C's accuracy-margin comparison (Option A has 1.3 mm vs.
Option B's 19.0 mm) and declares A the winner on accuracy alone, without pricing D6's actual
time-cost combination.

Both matched `FACILITATOR.md` exactly on arithmetic and on the named trap. **However, a
independent, more serious finding surfaced while reading case.md cold, that the prior run's report
did not flag:**

**FINDING — the Modeling Assumptions table in `case.md` (student-facing, before the `<!--
FACILITATOR ONLY -->` marker at line 222) states the winner outright.** MA5's "Sensitivity"
column reads: *"...below it, Option B's faster base time wins outright; above it, Option A's
accuracy margin wins. At 17 mm the case sits only ≈3.6 mm above breakeven..."* — this is a direct,
prose statement of which option wins at the case's own stated value, sitting in the student
packet. MA3's and MA4's Sensitivity columns do the same thing in weaker form (each states a
breakeven and which side of it the stated value sits on, letting a reader back out the winner
without doing any of D1–D6). This evades `preflight_lint.py`'s leak regex because the regex only
matches a stated **percentage** margin/winner (`"wins by X%"`, `"margin is X%"`); this leak is
phrased in mm/minutes instead, so it passed preflight clean and passed T1-08's/T1-18's leak checks,
but it is the identical defect class those checks exist to catch (skills/case-write/SKILL.md
2026-08-13 rule: no stated margin/winner in student-facing material, not just an assumption's
basis).

**This changes two probe verdicts from the prior report:**

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **FAIL** | The blind arithmetic route reaches the right answer for the right reasons (matches FACILITATOR.md) — but the case does not actually require that route. A Hero can read MA5's Sensitivity column alone and correctly report "Option A wins, ~19.9%-scale margin" without ever doing D1–D6. Per this skill's own criterion, a case that lets the intended answer be reached by copying it off a table, rather than by the case's own arithmetic, fails P1 regardless of what a diligent solver would do instead. |
| P2 both-sides | PASS | Both A's and B's arguments are independently well-supported with real numbers; neither collapses to a concession. Unaffected by the leak finding. |
| P3 trap | PASS | The blind trap hypothesis (stop at the accuracy-margin table, skip D6's time pricing) matches `FACILITATOR.md`'s stated trap exactly. (Note: the leak above creates a second, easier, unnamed shortcut — reading MA5's Sensitivity column instead of doing D5/D6 at all — which the guide's trap section does not name; flagged under P1 above rather than double-counted here.) |
| P4 twist | **FAIL** | Two separate questions here, and only one is comfortable. (a) Numeric survival: judged on its own, MA5's fragility (3.6 mm cushion, breakeven 13.4 mm vs. stated 17 mm) is disclosed, not hidden, and a natural reading of the cited literature's own qualifier — "several centimeters" (S6/S7) most naturally reads as ≥20 mm, i.e. further from breakeven, not closer — so the twist's numeric core is a defensible, not obviously-broken, pass. (b) Twist delivery: **this is the actual failure.** `FACILITATOR.md`'s planned "Twist" beat (drop at 25:00, "MA5 is the case's real fault line," ask the room to defend a lower value) has no surprise left to deliver, because the student packet already states, in plain prose, that MA5 sits only ~3.6 mm above its own breakeven and names which option wins on each side of it. A twist that is already printed in the material the room read before class is not a twist; it is a spoiler. This is a genuine BLOCKER-class defect, not a numeric-fragility judgment call — fix is in `case-write`'s hands (move MA3/MA4/MA5's breakeven-comparison sentences to FACILITATOR-only material, leaving only the assumption's *basis* in the student-facing table, per the same 2026-08-13 rule), not something this gate can waive. |
| P5 sensitivity | PASS (disclosed) | Re-ran `python3 skills/case-readiness/scripts/tier2_probes.py --case the-stake-out --probe 5 --flex 0.5`. Base A=−26.0/B=−31.19 (script's internal sign convention; margin −16.6% by its formula, same underlying 19.9%/Option A result). Confirmed **3 of 5 FLEX[] entries flip the winner at ±50%**: `second_setup_min` (+50% → B), `rework_min` (−50% → B), `multipath_degradation_mm` (−50% → B). Matches `case.json.sensitivity_disclosure[]` and `FACILITATOR.md`'s own numbers exactly. Machine verdict: PASS (disclosed) — MCS-26's disclosure-not-elimination standard is met; these are genuinely disclosed, not hidden. |
| P6 data decay | PASS | Live web check via subagent, all 11 `sources[].url` entries: 9/11 (S1, S2, S3, S4, S5, S8, S9, S10, S11) reachable with the cited value/figure confirmed verbatim on the live page/PDF, no drift. S6, S7 (the two peer-reviewed multipath papers) confirmed as real, findable, correctly attributed papers, but full-text access to the specific "several centimeters" magnitude claim was blocked by publisher bot-protection (403) on every mirror tried — same limitation `case.json`'s own S6/S7 notes already disclose; not a new finding, not treated as a fail since the qualitative claim is corroborated by two independent real sources and no drift was found in what *was* readable. No dead links, no URL moves.

`MECHANICAL RESULT (P5 script): 0 probes FAILED mechanically.` **Honest overall Tier 2 result:
2 of 6 probes FAIL (P1, P4) — Tier 2 is NOT clean. `TIER2_PASS` from the prior run is retracted.**

### Tier 3 — human dry-run

NOT RUN (unchanged).

### Next step

**Hand back to `case-write`, not `case-publish`.** The single concrete fix that clears both new
FAILs: in `case.md`'s Modeling Assumptions table (student-facing half, above the `<!--
FACILITATOR ONLY -->` line), shorten MA3/MA4/MA5's "Sensitivity" column to describe direction and
rough size of consequence only (e.g. "a large swing in this figure could change which option is
cheaper on time — see discussion") — remove the explicit breakeven values and the "above/below it,
Option [A/B] wins" sentences, which belong in `FACILITATOR.md` only (which already carries the
full breakeven analysis in its own "The margin" and "Sensitivity note" sections — nothing new
needs to be written there). Once that edit lands, re-run Tier 2's P1 and P4 only (P2/P3/P5/P6 need
not be re-run unless `case.md` changes elsewhere). This is a text-trim, not a numeric retune —
`margin_pct`, MA5's value, and every other figure in the case are unaffected and should not be
touched again.

---

## case-readiness run — 2026-09-01 (RE-GATE, post-leak-fix)

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

This is a re-gate after the Modeling Assumptions table's Sensitivity column (MA3/MA4/MA5) was
rewritten to describe direction only, with the stated winner/breakeven numbers removed, per the
prior run's fix instruction. Re-ran the full ladder from scratch, including a genuinely fresh blind
solve, rather than trusting that the text edit alone cleared P1/P4.

### Tier 1 — structural (20 checks)

`python3 skills/case-readiness/scripts/tier1_structural.py --case the-stake-out --json /tmp/t1-stake-out-2.json`
→ PASS 15 · GAP 6 · FAIL 0 · **0 BLOCKERs**. Unchanged from the prior run's structural state
(T1-09 wide-but-in-cap margin, T1-10 reinforcement carve-out, T1-14/T1-15 minor guide/published-doc
number drift, T1-18 no image) — none are new, none are BLOCKERs. `TIER1_PASS`.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Solved D1–D6 from `case.md` alone, blind, before opening `FACILITATOR.md`/`case.json`. Re-read MA3/MA4/MA5's Sensitivity column first specifically to check for a leak: all three now state direction only ("shifts the balance toward Option B/A") with no breakeven mm/min value and no "Option X wins" sentence — the exact leak class the prior run flagged is gone. Reaching the answer required actually doing the arithmetic: Option A = 6 + 20 + (0×45) = 26.0 min; Option B = 3 + (0.626×45) = 31.2 min, using Appendix E's own stated 62.6% miss probability and Appendix A/B/C's tolerance/accuracy figures. Margin = (31.2−26.0)/26.0 ≈ **19.9%, Option A wins** — matches `FACILITATOR.md` and `case.json.balance` exactly, reached by the intended route, not read off a table. |
| P2 both-sides | PASS | Built independently from the packet: A's case (huge 1.3mm accuracy cushion, near-zero rework risk, only cost is a known 20-min setup) and B's case (no sightline needed, faster raw throughput, real weakness is accuracy margin, not time) are both real, numeric, non-concessive arguments. Neither collapses. |
| P3 trap | PASS | Blind trap hypothesis, named before reading the guide: a Hero stops at the accuracy-margin comparison (A's 1.3mm vs. B's 19.0mm) and declares A the winner on accuracy alone, without pricing D6's time cost. Matches `FACILITATOR.md`'s stated trap exactly. |
| P4 twist | **PASS** | Confirmed MA5's fragility (~3.6mm cushion above ~13.4mm breakeven) is NOT stated anywhere in student-facing `case.md` — searched for "13.4", "3.6", "breakeven" and found only Appendix E's sigma value (13.4mm, the per-axis standard deviation of the circular-normal miss-probability model), a different quantity that happens to share the same number but is never labeled or discussed as a breakeven/flip-point. The gated Twist reveal in `published/The Stake-Out - Interactive.html` (behind a facilitator-only reveal button) also states only "sitting close to its own breakeven point" with no number. The twist still has something genuinely new to reveal: the exact breakeven value, the ~3.6mm cushion size, and the explicit "which option wins on each side" statement all remain FACILITATOR-only. Both twist-integrity questions pass: it still invalidates a real room's Anchor-1 confidence in Option A, and it survives the case's own stated assumptions under the natural student reading. |
| P5 sensitivity | PASS (disclosed) | Re-ran `tier2_probes.py --probe 5 --flex 0.5`. Base A=26.0/B=31.19 min (script convention shows −26.0/−31.19), Option A wins, ≈19.9%-scale margin. Confirmed 3 of 5 `FLEX[]` entries flip the winner at a ±50% swing: `second_setup_min` (+50%→B), `rework_min` (−50%→B), `multipath_degradation_mm` (−50%→B). Matches `case.json.sensitivity_disclosure[]` and `FACILITATOR.md` exactly — genuinely disclosed, not hidden, per MCS-26. |
| P6 data decay | PASS | Live-fetched all 11 `sources[].url` entries. 9/11 (S1, S2, S3, S4, S5, S8, S9, S10, S11) reachable, cited figure confirmed verbatim: S2's "greater of 13mm or 2% of specified dimension"; S3's Knox County 12×6 footing row (2-Story slab-on-grade, all soil bearing values); S4's Leica TS16 1″/2″/3″/5″ angular accuracy and ±(1mm+1.5ppm) EDM spec; S5's Trimble R12i single-baseline RTK ±(8mm+1ppm) RMS; S8's "500 or more points per hour" Alphageo figure; S9's WA DES $275/day Topcon robotic total station line item; S10's $269/day KWIPPED average; S11's $150/$250 two-supplier KWIPPED listing. S1 (PA DLI-hosted ACI 117-10) loads and is confirmed as the genuine ACI 117-10 (Reapproved 2015) document with the expected "Section 3—Foundations" structure. S6, S7 (Mekik & Can 2010; O'Connor et al. 2024, the two multipath papers) both returned HTTP 403 on live fetch — unchanged from the prior run's disclosed finding (publisher bot-protection blocks the specific data table; the qualitative "several centimeters" claim remains corroborated by two independently-real, correctly-attributed papers). No dead links, no URL moves, no drifted figures.

**All six probes PASS. Tier 2 is clean. `TIER2_PASS`.**

### Tier 3 — human dry-run

NOT RUN (unchanged).

### Next step

Run `case-publish` on `the-stake-out`. No further QA-driven edits are needed; `case-write` should
not touch `case.md`/`case.json` further based on this report.
