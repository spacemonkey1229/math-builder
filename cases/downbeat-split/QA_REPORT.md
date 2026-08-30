## case-readiness run — 2026-08-27
**State:** DRAFT → BLOCKED   **Verdict:** BLOCKED (Tier 1 did not clear; Tier 2 not run)

Preflight lint (`preflight_lint.py --case downbeat-split`) advisory finding: line 214 of `case.md`
contains an HTML comment that names "FACILITATOR" (`<!-- FACILITATOR ONLY: balance argument,
margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here.
-->`). This is an author note fenced in an HTML comment, not rendered student-facing text, and
does not itself leak balance/margin/twist content — read and not treated as a BLOCKER, but flagged
here per the preflight linter's own advisory (non-blocking) status.

### Tier 1 — structural (20 checks)
| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview length; no load-bearing numerals |
| T1-03 | PASS | Dilemma binary |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no Challenge numeral-form drift |
| T1-06 | PASS | appendices lettered, ordered, no orphans |
| T1-07 | PASS | final-appendix lines are verbatim spine labels |
| T1-08 | PASS | every number cited or declared an assumption |
| T1-09 | **FAIL** | SPEC §2 balance test — `margin_pct` not recorded. See "Judgment call" below. |
| T1-10 | PASS | `new_coverage[]` non-empty, both entries force real deliverables |
| T1-11 | PASS | learning-goal mutual reachability |
| T1-12 | PASS | tier vs numeric load |
| T1-13 | **FAIL** | facilitator guide, anchor ladder, twist, timed plan, sensitivity note — see "Judgment call" below |
| T1-14 | GAP | CONTINUITY — 2 number(s) in FACILITATOR.md (0.0, 6.0) not found in case.md/case.json |
| T1-15 | PASS | no `published/` directory yet — nothing to drift |
| T1-16 | GAP | MCS-11 — no `case_md_sha256` recorded yet (expected on a first run) |
| T1-17 | GAP | MCS-25 — `case.json` declares no `cohort_bands[]` |
| T1-18 | PASS | no `published/` directory — MCS-37 has nothing to check yet |
| T1-19 | PASS | no `published/` directory — MCS-39 has nothing to check yet |
| T1-20 | PASS | no `published/` directory — advisory, nothing to check yet |

**BLOCKER (4):**
- [T1-09] SPEC §2 — `margin_pct` not recorded. `case.json.balance` has non-empty `argument_a`/
  `argument_b`/`margin_basis`, but `margin_pct` is explicitly `null` (both at the top level and
  inside `balance`), and Appendix B's D5 decision table in `case.md` is a literal empty shell
  ("completed in D5"). The actual D1–D5 arithmetic (Straight Cut running time, partial-phrase
  check, subdivision split, read-through fit-check, and the final minutes-per-second-of-accuracy
  ratio for both options) has never been computed and recorded anywhere the gate can check. This
  is real math work against the now-sourced Appendices A–D, not a bookkeeping gap.
- [T1-13 / MCS-14] anchor ladder incomplete — `FACILITATOR.md` is missing every one of the required
  headings: Intro, Launch, Anchor 1, Anchor 2, Anchor 3, Anchor 4, Data Deep Dive, Twist, Close,
  Lessons Learned, Standards Touched On. The file that exists is explicitly a write-time draft
  (its own first line: "Drafted at write time, before `case-research` fills Appendices A–D... Margin
  is `null` until the sourced/assumed figures land") and was never revisited after research closed.
- [T1-13 / MCS-15] no Twist section and no explicit "Twist: N/A" justification in `FACILITATOR.md`.
- [T1-13 / MCS-16] no timed 45-minute Socratic plan (SPEC §7.3) in `FACILITATOR.md`.

**GAP (4):**
- [T1-13] facilitator guide has 5 Socratic questions listed under "Five Socratic questions," but
  they are not embedded in a timed anchor ladder, so the script cannot credit them against a
  specific Anchor step.
- [T1-14] CONTINUITY — 2 number(s) in `FACILITATOR.md` (0.0, 6.0) appear in neither `case.md` nor
  `case.json`. These read as artifacts of the word "zero" (used repeatedly in the Argument-for-A
  prose and the trap paragraph) and a similarly-parsed figure, not obviously stale derived
  numbers — worth a human glance when `FACILITATOR.md` is rewritten for the T1-13 fix, but not
  independently blocking.
- [T1-16] MCS-11 — no `case_md_sha256` recorded yet; expected on a first `case-readiness` run.
  Current hash: `75cc4971ea6fe4302d3e2a128c92dbcf7b5689085ae2d6f1aac35596fd1038e9`.
- [T1-17] MCS-25 — `case.json` declares no `cohort_bands[]`. A Socratic discussion that works with
  12 does not work with 24; the bands this case is tuned for (and what changes at each) are not yet
  declared.

**POLISH (5):**
- [T1-07] parsed 4 labels (4 bulleted, 0 from separator-run lines).
- [T1-15/18/19/20] no `published/` directory yet — nothing for these checks to examine.

### Judgment call for a human (SPEC §2 balance + facilitator completeness) — read before doing anything else with this case

Two BLOCKER classes, both squarely `case-write`/`case-research` work, not `case-readiness`'s to
compute or write:

1. **The balance test has never actually been run.** Appendices A–D are now sourced/assumed (0 open
   `{{NEEDS_SOURCE}}` placeholders, confirmed), but nobody has done the D1–D5 arithmetic and
   recorded a real `margin_pct`. `FACILITATOR.md`'s own margin section (`margin_basis`) already
   flags this: it says the comparison is *not* a simple two-variable ratio because Option A's
   rehearsal-minute numerator is "at or near zero," which is exactly the kind of near-zero-
   denominator case SPEC §2's margin formula can break down on (see the fret-board QA precedent).
   Whoever runs D1–D5 for real needs to (a) compute both options' minutes-per-second-of-accuracy
   ratios from Appendices A–D and Appendix E's Modeling Assumptions, (b) record the result in
   `case.json.balance.margin_pct` (and top-level `margin_pct`), and (c) if Option A's numerator is
   genuinely 0, decide — and document, the same way fret-board did — how the margin is stated when
   the ratio's denominator-of-comparison degenerates, rather than leaving it silently `null`.
2. **`FACILITATOR.md` was never brought forward from its write-time draft.** It still opens with
   "Drafted at write time, before `case-research` fills Appendices A–D" and explicitly defers its
   own margin section. It needs the full Intro/Launch/Anchor 1–4/Data Deep Dive/Twist/Close/Lessons
   Learned/Standards Touched On ladder, a stated Twist (or an explicit "Twist: N/A" with
   justification per the case's `sensitivity_note`/concept sheet), and a timed 45-minute Socratic
   plan built around the 5 questions that already exist. This is a rewrite, not a patch — the
   existing Argument-for-A/Argument-for-B/trap prose is usable content and should be preserved
   inside the new ladder, not discarded.

Both blockers are load-bearing on each other: the facilitator guide's Twist/anchor ladder cannot be
written correctly until the real balance result (and whether Option A's near-zero numerator changes
the story) is known, so item 1 should be done first.

**This case is not `case-readiness`'s to fix.** Sending back to `case-write`/`case-research` to (1)
complete the D1–D5 balance computation and record `margin_pct`, and (2) rewrite `FACILITATOR.md`
against the full anchor-ladder template. `cohort_bands[]` (T1-17 GAP) can be added in the same pass.

### Tier 2 — simulated play (6 probes)
NOT RUN. Tier 1 did not reach `TIER1_PASS` (4 open BLOCKERs: T1-09 x1, T1-13 x3). Per
`skills/case-readiness/SKILL.md`'s ladder, Tier 2 may only start after Tier 1 is clean, and running
probes against a case with no recorded balance result and no complete facilitator guide would not
produce a meaningful P2/P3/P4 finding anyway.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | NOT RUN | blocked on T1-09/T1-13 |
| P2 both-sides | NOT RUN | blocked on T1-09/T1-13 |
| P3 trap | NOT RUN | blocked on T1-13 (no complete FACILITATOR.md to name the trap against) |
| P4 twist | NOT RUN | blocked on T1-13 (no Twist section) |
| P5 sensitivity | NOT RUN | blocked on T1-09; no `sensitivity_model.py` present either |
| P6 data decay | NOT RUN | blocked on T1-09/T1-13 |

### Tier 3 — human dry-run
NOT RUN.

---

## case-readiness run — 2026-08-27 (remediation re-run)
**State:** DRAFT → BLOCKED   **Verdict:** BLOCKED (Tier 1 did not clear; Tier 2 not run)

This is a re-run after `case-write`-stage remediation: the D1–D5 balance arithmetic was computed
for real (`case.json.balance`/`case.json.derived`), and `FACILITATOR.md` was rewritten with the
full §7.1 anchor ladder (Intro/Launch/Anchor 1–4/Data Deep Dive/Twist/Close/Lessons Learned/
Standards Touched On), a real Twist, and a timed 45-minute Socratic plan (§7.3). `cohort_bands[]`
was added to `case.json` (§7.4). The existing Argument-for-A/B and trap prose were preserved inside
the new ladder, not discarded.

Preflight lint (`preflight_lint.py --case downbeat-split`) advisory finding is unchanged from the
first run: line 214's `<!-- FACILITATOR ONLY: ... -->` HTML comment is an author note, not
rendered student-facing text — read and not treated as a BLOCKER, per its own advisory
(non-blocking) status.

### Tier 1 — structural (20 checks)
| id | result | note |
|---|---|---|
| T1-01 | PASS | |
| T1-02 | PASS | |
| T1-03 | PASS | |
| T1-04 | PASS | |
| T1-05 | PASS | |
| T1-06 | PASS | |
| T1-07 | PASS | |
| T1-08 | PASS | |
| T1-09 | **FAIL** | SPEC §2 — margin is now honestly computed and recorded: 100.0%. See "Judgment call" below — **not fixed, out of this remediation pass's scope.** |
| T1-10 | PASS | |
| T1-11 | PASS | |
| T1-12 | PASS | |
| T1-13 | PASS (fixed) | FACILITATOR.md rewritten with the full anchor ladder, a real Twist, a timed 45-minute Socratic plan, and 5 single-line Socratic questions (previously 0 detected — they existed but were line-wrapped so the mechanical check couldn't see them; now one physical line each) |
| T1-14 | PASS (fixed) | CONTINUITY — the two orphan numerals (0.0, 6.0 — artifacts of "n=0" and "SPEC §6", not stale derived figures) no longer appear; FACILITATOR.md's numbers now live in `case.json.derived` and are checkable |
| T1-15 | PASS | |
| T1-16 | PASS | |
| T1-17 | PASS (fixed) | `cohort_bands[]` added: Full (10-16) / Compressed (5-9) / 1:1-pair (1-2) |
| T1-18 | PASS | |
| T1-19 | PASS | |
| T1-20 | PASS | |

**BLOCKER (1):**
- [T1-09] SPEC §2 — UNBALANCED: margin is 100.0% on "rehearsal minutes required per second of
  timing accuracy gained" (cap ~20%). Retune a constraint. Do NOT fix this by hiding data.

**GAP (0).**

### Judgment call for a human (SPEC §2 balance) — read before doing anything else with this case

`margin_pct` is now honestly recorded, not left `null` and not hidden: **100.0%**. D1–D5, computed
from Appendices A–D and the existing Modeling Assumptions (no new figures invented):

- D1 (Straight Cut total): 3¾ beats × 1⅓ sec/beat × 4 repeats = **20 sec**.
- D2 (partial-phrase check): 3/8 × 3¾ beats × 1⅓ sec/beat = **1⅞ sec (1.875 sec)** — exactly the
  gap between the 20-sec written total and the 21⅞-sec target (MA1).
- D3 (subdivision split): 3/8 ÷ 1/2 (MA8) = **3/4**.
- D4 (read-through fit-check): 22½ min (MA10) ÷ 2½ min (MA9) = **9 read-throughs**.
- D5 (decision table): Option A rehearsal minutes = **0**; Option B = 2½ × 9 = **22.5**. Both
  options close the 1.875-sec gap exactly (A via a continuously-adjustable uniform tempo nudge, B
  via D3's exact subdivision), so both show 0 sec off target and both "gain" the same 1.875 sec —
  ratio: Option A = **0.0 min/sec**, Option B = **12.0 min/sec**.
- `margin_pct` = 100 × (12.0 − 0.0) / 12.0 = **100.0%**, worse (higher-ratio) option as the
  denominator so Option A's exact-zero numerator doesn't produce an undefined ratio.

**This case is not balanced on its stated primary metric, well past SPEC §2's ~20% cap** — the same
structural pattern found in `fret-board`'s QA precedent (`cases/fret-board/QA_REPORT.md`): Option
A's rehearsal-minute cost is exactly zero *by the case's own construction* (already rehearsed, and
a uniform tempo nudge can close any residual gap exactly, by definition), so the stated ratio metric
is structurally incapable of producing a close race — any nonzero Option B cost against an
exact-zero Option A numerator computes to 100% under the standard margin formula. This is not a
bookkeeping gap masking a genuinely close case; it is a structural property of the metric as
currently stated.

The case's real defensibility does not rest on the primary metric alone — it rests on the Twist and
the trap (already in `FACILITATOR.md`, preserved and now embedded in the anchor ladder): Option A's
zero *rehearsal* cost is not zero *cost*, once the risk of a take that misses the network's
frame-accuracy tolerance is priced in, and that risk has no term in the stated ratio. **A human
needs to decide: retune the primary metric (e.g. grade against expected re-book cost rather than
booked rehearsal minutes alone, so Option A's cost is not structurally zero) or consciously accept
and document that this case's defensibility rests on the risk/Twist argument rather than a tight
primary-metric race.** Either is legitimate; picking one is not this remediation pass's or
`case-readiness`'s to make.

**This case is not `case-readiness`'s (or this remediation pass's) to fix on T1-09.** The D1–D5
arithmetic and the facilitator-guide rewrite (both explicitly `case-write` work per the prior run)
are done; what remains is a genuine SPEC §2 design judgment call that only a human/case-owner
should resolve.

### Tier 2 — simulated play (6 probes)
NOT RUN. Tier 1 did not reach `TIER1_PASS` (1 open BLOCKER: T1-09). Per
`skills/case-readiness/SKILL.md`'s ladder, Tier 2 may only start after Tier 1 is clean, and running
probes against a case with a known-unbalanced primary metric would not produce a meaningful P2/P5
finding beyond what is already documented above.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | NOT RUN | blocked on T1-09 |
| P2 both-sides | NOT RUN | blocked on T1-09 |
| P3 trap | NOT RUN | blocked on T1-09 |
| P4 twist | NOT RUN | blocked on T1-09 |
| P5 sensitivity | NOT RUN | blocked on T1-09; no `sensitivity_model.py` present either |
| P6 data decay | NOT RUN | blocked on T1-09 |

### Tier 3 — human dry-run
NOT RUN.

---

## case-readiness run — 2026-08-29 (retune: primary-metric reframe — TIER2_PASS)

**State:** TIER2_PASS   **Verdict:** TIER2_PASS (all six Tier 2 probes PASS or PASS (disclosed); Tier 1 clean, 0 blockers, 0 gaps)

### What changed this pass

The prior run (above) found T1-09 FAILED: `margin_pct` = 100.0% on "rehearsal minutes required per
second of timing accuracy gained." Investigation confirmed this was structural, not an unlucky
tuning: Option A's rehearsal-minute numerator is exactly zero by the case's own construction
(already rehearsed; a continuous tempo nudge closes any residual gap exactly, by definition,
regardless of the gap's size), so ANY nonzero Option B rehearsal cost computes to a 100% margin
under SPEC §2's formula — no retuning of MA1–MA10 could fix it. This is the same structural pattern
already found and fixed in `fret-board` (`cases/fret-board/QA_REPORT.md`), used here as precedent.

**Fix applied: retuned the primary metric**, per case-owner instruction, not the fret-board-style
"shared baseline" retune (that approach was checked by hand and rejected here — it would require an
implausibly large fixed post-production baseline, ~90+ minutes on a 20-second radio spot, to shrink
a 22.5-minute absolute gap under the 20% cap). Instead: reframed to **expected total studio minutes
to deliver a broadcast-ready take** — booked rehearsal minutes (D1–D5, unchanged) plus a
probability-weighted redelivery-risk term (each option's own rejection probability × the total
booked session length that has to be re-booked if a take is rejected). This directly formalizes the
real tension already present in the case's Background/Dilemma and in `FACILITATOR.md`'s pre-existing
Twist (a producer's aside that a tempo-compromise take of this kind has already been rejected once
for this client) — the risk term was not invented from nothing; it gives the Twist's existing
narrative a number.

**New Modeling Assumptions (case.json + case.md Appendix E):**
- **MA11** — probability the Straight Cut's tempo-compromise take is rejected on delivery = **1/3**.
  No published rejection-rate data exists for broadcast frame-accuracy QC specifically (searched:
  "broadcast commercial ad delivery rejected quality control frame accuracy percentage reject rate";
  "AFM recording session re-book re-record commercial jingle cost redo" — both NOT FOUND as
  specific figures, recorded in `RESEARCH_LOG.md` P13). Set in line with the case's own Twist (one
  prior rejection for this client on this exact failure mode).
- **MA12** — probability the Downbeat Split's rehearsed, exact-fit take is rejected = **1/20**, set
  well below MA11 because it is rehearsed to an exact target across 9 full read-throughs before
  ever being recorded, but not zero (no live take is risk-free).
- Re-book session length reuses **MA2** (90 min) rather than inventing a new figure — Appendix A now
  states explicitly that a rejected take of either option requires re-booking a full session of the
  same length, closing a P4 ambiguity found during this pass (see Tier 2 below).

**D5 (Challenge 3 and Appendix D's decision table)** extended with two new rows — probability-
weighted redelivery-risk minutes and expected total minutes — replacing the old ratio's two rows
(timing accuracy in seconds / rehearsal-minutes-per-second). Raw rehearsal-minute figures (0 min vs.
22.5 min) are NOT deleted; they remain the first row of D5, fully visible, so the risk-weighted flip
is auditable, not hidden.

**Result:** Option A = 0 + 1/3 × 90 = **30.0 expected total minutes**. Option B = 22.5 + 1/20 × 90 =
**27.0 expected total minutes**. Option B is now the lower-expected-cost option (a reversal from the
old metric's "A is unbeatable" framing). `margin_pct` = 100 × (30.0 − 27.0) / 30.0 = **10.0%**, well
inside SPEC §2's ~20% cap and the T1-09 15% "wide" threshold. Full derivation in
`case.json.balance.margin_note` and `case.json.derived`.

No numbers were invented without disclosure: MA11/MA12 are both recorded as unsourced author
scenario estimates (matching MA9/MA10's existing precedent in this same case), and both are flagged
in `case.json.sensitivity_disclosure[]` (Category X) because `sensitivity_model.py` shows the
verdict flips under a ±50% flex — see Tier 2 P5 below.

**P4 fix, same pass:** re-derived the Twist under every defensible reading of the stated
assumptions (adversarial pass, per SKILL.md's Cold Chain precedent) and found one real ambiguity —
the case never stated whether a rejected take of *either* option requires the same re-book session
length, or whether the Downbeat Split (already exactly right, just unlucky) might get a cheaper
make-good. Fixed by adding one sentence to Appendix A: "If a delivered take is rejected, the studio
has to book a brand-new session of the same total booked length ... to re-cut the spot from scratch,
regardless of which arrangement was rejected." Re-verified Tier 1 clean after this addition
(new sha256 below).

`FACILITATOR.md` updated throughout: Data Deep Dive's D5 arithmetic, Argument for A/B, "The margin"
(with a "Retune history" note), the Twist's framing (a confirmation of an existing, page-visible
number rather than a brand-new one — the trap is now "a discounted term," not "a missing term"), the
trap, all five Socratic questions, Lessons Learned, and a new "Facilitator note — assumption
sensitivity (Tier 2 probe P5)" section. The existing Argument-for-A/B and trap prose were preserved
and adapted, not discarded, per the fret-board precedent's own methodology note.

### Re-run: `sensitivity_model.py` (new file, authored this pass)

```
base totals (minutes) {'A': 30.0, 'B': 27.0} winner B margin -10.0%
```

### Tier 1 — structural (20 checks), re-run 2026-08-29

`python3 skills/case-readiness/scripts/tier1_structural.py --case downbeat-split`

**PASS 20 / GAP 0 / FAIL 0. sha256(case.md) = 91a66c18dd64d728bef6e23010e922c8a2d83b62c8d7a790dac9514ac5b677ce**

| id | result | note |
|---|---|---|
| T1-01–T1-08 | PASS | unchanged in substance; case.md's Background/D5/Appendix D/E text updated for the retune, structure unaffected |
| T1-09 | **PASS** | SPEC §2 balance test — `margin_pct` = 10.0% on the retuned primary metric (cap ~20%, "wide" gap threshold 15%). Was the sole BLOCKER; now clears cleanly. |
| T1-10–T1-13 | PASS | unchanged; FACILITATOR.md's full anchor ladder, Twist, and 45-minute plan preserved and updated for the retune |
| T1-14 | PASS | CONTINUITY — all new FACILITATOR.md numbers (30.0, 27.0, 10.0%, MA11/MA12 fractions) trace to `case.json.derived`/`balance` |
| T1-15–T1-20 | PASS | unchanged (no `published/` directory yet) |

**BLOCKER (0). GAP (0).** Five POLISH-level notes only, all pre-existing "no `published/` directory
yet" advisories, unaffected by this retune.

Preflight linter (`preflight_lint.py --case downbeat-split`) reports the same single pre-existing
advisory as every prior run (the `<!-- FACILITATOR ONLY -->` marker comment) — advisory only, not a
blocker, not introduced by this pass.

### Tier 2 — simulated play (6 probes), fully adjudicated this pass

`python3 skills/case-readiness/scripts/tier2_probes.py --case downbeat-split`

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Dispatched a genuinely fresh subagent with access to ONLY `/tmp/coldsolve-downbeat-split/PACKET.md` (leak-free — confirmed by preflight lint and by inspection). It chose **Option B**, with arithmetic matching `case.json.derived` exactly (A = 30 min, B = 27 min), named the metric explicitly ("expected total studio minutes... the packet is explicit that the decision has to be judged on one number"), independently identified **MA11** as the most sensitive assumption and computed its own break-even point (p = 0.30, matching this report's own hand-check), named the AFM dollar rate as the appendix item it ignored (correctly — it never enters the D1–D5 arithmetic), and named MA11 as the least-supported number, with a skeptical, well-reasoned critique of it. A defensible position reached by the right route. |
| P2 both-sides | **PASS** | Built the strongest case for each option. A: "already rehearsed, and even after weighting MA11's risk its expected cost (30 min) is close enough to B's (27 min) that a real, data-backed MA11 could still make A the safer bet." B: "the only option that hits the target exactly, with a small bounded rehearsal cost and a far lower rejection risk because it's actually rehearsed to that target." Neither collapses to a bare concession — A's retreat (skepticism of MA11 as a single-anecdote estimate) is a specific, arguable pressure point, not a surrender; B's position does not depend on MA11 being exactly 1/3, only on it being meaningfully larger than MA12. |
| P3 trap check | **PASS** | From case.md alone, the most plausible wrong path: read D5's rehearsal-minutes row (0 vs. 22.5), price Option A as cheaper, and treat Appendix E's MA11 redelivery-risk row as a formality to complete mechanically without weighing it in the final recommendation. `FACILITATOR.md`'s trap names exactly this ("the trap here is not a missing term, it is a discounted one... reading Appendix E's MA11... as a formality to skim past rather than a real term to multiply into the decision table"). Guide names the same trap the case actually contains. |
| P4 twist integrity | **PASS (after one fix, this pass)** | (1) The twist confirms MA11 is not hypothetical — it already happened to this client — invalidating a room's position that priced Option A's real cost at zero. (2) Adversarial re-derivation under every stated-assumption reading (per SKILL.md's Cold Chain precedent) found one genuine ambiguity: the case never stated whether a rejected take of *either* option incurs the same re-book session length, or whether the Downbeat Split might get a cheaper make-good since it is already exactly right. **Fixed this pass**: added one sentence to Appendix A stating the re-book session is the same total length "regardless of which arrangement was rejected." Re-verified Tier 1 clean after the fix (sha256 above). No other convention-dependent ambiguity found across MA1–MA12. |
| P5 sensitivity | **PASS (disclosed)** | `sensitivity_model.py --flex-all` (authored this pass; contract: `PARAMS` = {rehearsal_min_a, rehearsal_min_b, redelivery_risk_prob_a, redelivery_risk_prob_b, rebook_session_min}, `FLEX` = the three MA11/MA12/MA2 dials the retune introduced) reproduces the base case exactly (A=30.0, B=27.0, margin −10.0%, matching `case.json.derived`). ±50% sweep: **UNSTABLE** — `redelivery_risk_prob_a` (MA11) at −50% flips B→A, and `rebook_session_min` (MA2) at −50% also flips B→A; no other flex flips it. Both are disclosed in `case.json.sensitivity_disclosure[]` (Category X — no published data exists for either quantity, both are good-faith estimates from the closest available context) with justifications ≥20 chars naming the exact flip mechanics and the verification method (`tier2_probes.py --probe 5 --flex 0.5`). `tier2_probes.py` reports mechanical verdict `PASS (disclosed)`. `FACILITATOR.md`'s new "Facilitator note — assumption sensitivity (Tier 2 probe P5)" section states this honestly for the discussion lead; `case.json.modeling_assumptions` MA11/MA2 sensitivity fields and case.md's Appendix A/E Sensitivity columns were rewritten to disclose direction without leaking the numeric margin, per `case-write`'s "never the RESULT" rule. |
| P6 data decay | **PASS** | Both sources (S1, S2 — same AFM Commercial Announcements Agreement Signatory Packet PDF, `afm47.org`) re-fetched live: URL returns HTTP 200 (confirmed via `curl`), and the PDF's own page 5 ("Original Sessions / Standard Recording Rates") was read directly and verbatim-confirms both cited figures: "a minimum call session length of one (1) hour" (S2, unchanged) and "Currently, the basic scale wage for an instrumentalist (called a 'Side Musician') for a minimum call session is **$133.01**" (S1, unchanged). No dead links, no drifted figures, no URL moves. (WebFetch's automatic text-extraction on this PDF returned "unreadable" for this large scanned-style document — not a data-decay finding, just this tool's extraction limitation; the direct page-image read confirms the source is intact.) |

**Overall Tier 2: 6/6 clear the gate (4 PASS, 2 PASS (disclosed)).** Combined with Tier 1 clean (0
blockers, 0 gaps), this reaches **`TIER2_PASS`** per SPEC §2/MCS-26.

### Tier 3 — human dry-run
NOT RUN. (Out of scope for `case-readiness`.)

### Remaining genuine judgment call for a human

None blocking. One item worth a human's attention, not a defect: **MA11's 1/3 redelivery-risk value
is the case's single most load-bearing number** (P1's cold solver and P5's sensitivity sweep both
independently flagged it as the thing to watch). This is disclosed, not hidden, in three places
(`case.json.sensitivity_disclosure[]`, `case.json.modeling_assumptions`, `FACILITATOR.md`'s P5
note) — a discussion lead should expect a strong room to push on "why 1/3, why not something else,"
and the honest answer is "there is no public number for this; the case's own Twist is the best
available evidence, and reasonable people could land elsewhere." This is intended discussion
content, matching this project's disclosure-aware pass precedent (`fret-board`, `enclosure-call`,
`reroute-wait`), not a case-readiness defect.
