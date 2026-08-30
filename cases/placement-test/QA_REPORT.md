## case-readiness run — 2026-08-30 (balance retune — TIER2_PASS)

**State:** TIER1_PASS → **TIER2_PASS**   **Verdict:** PASS. All six Tier 2 probes now PASS (6/6,
0 FAIL). Tier 1 re-confirmed clean (0 blockers, 2 pre-approved gaps, fresh `sha256(case.md)` matches
`case.json.qa`).

### The judgment call this pass closes

The prior pass (below) left P5 (assumption sensitivity) a genuine, fully-disclosed FAIL: the tie
between Option A and Option B sat exactly ON Appendix C's $5,000/variant minimum-viable-spend
threshold with **zero slack** — Full Rotation's fixed $5,000/variant split cleared the threshold at
precisely 100%, not comfortably above it. Three independently plausible assumption moves (MA1 up,
MA2 down, MA3 up) each pushed **all six** Full Rotation variants below threshold **simultaneously**
(every variant gets an identical split spend, so they cross the line together, not gradually),
flipping the recommendation to a ~100%-margin Option A win. The prior QA report flagged this
explicitly as a human judgment call: retune for real slack, or keep the razor's-edge framing and
formally disclose it. The human chose **retune**.

### The retune

**MA2 (total fixed ad-spend budget) raised from $30,000 to $60,000.** Grounding: $60,000/quarter is
a defensible paid-social test budget for a mid-size direct-to-consumer brand's single
sponsored-video campaign cycle — Background frames MA2 as a locked quarterly line item, and doubling
the prior figure keeps it inside the same order of magnitude the case already established (its
own history moved $18,000 → $30,000 → $60,000) rather than inventing a new scale. MA2 remains an
unsourceable, fictional employer-internal detail (same `basis` category as before), consistent with
SPEC §5.

At $60,000, Full Rotation's split is **$10,000/variant — double the $5,000/variant Appendix C
threshold, not exactly at it.** Because MA4/MA5 (conversion rate, CPM) apply identically to both
options once every variant clears, conversions-per-dollar is still a rate independent of how the
budget is split, so the tie is preserved exactly: `margin_pct = 0.0%` (both options now compute
80,000 total conversions on the $60,000 spend, up from 40,000 at $30,000 — same rate, bigger
budget). **New `margin_pct`: still 0.0% (unchanged) — the retune's purpose was never to change the
winner, only to give the tie real slack.**

### Verified genuine slack, not just a bigger cliff

Recomputed the Appendix C threshold under a ±50% flex on every stated assumption dial (not just
MA1/MA3) using `sensitivity_model.py` (`PARAMS.total_budget` updated to 60000.0; header comment and
docstring corrected):

```
base  {'A': 80000.0, 'B': 80000.0}  margin 0.0%   threshold/variant: 5000.0
```

`tier2_probes.py --probe 5 --flex 0.5` full sweep — **0 of 10 flex directions flip the
recommendation or breach the 20% cap:**

| param | flex | new threshold or budget | Full Rotation clearance | flips? |
|---|---|---|---|---|
| weeks_remaining (MA1) | −50% (2.5 wk) | $2,500/variant | $10,000/variant, 400% | no |
| weeks_remaining (MA1) | +50% (7.5 wk) | $7,500/variant | $10,000/variant, 133% ($2,500/33% to spare) | no |
| total_budget (MA2) | −50% ($30,000) | $5,000/variant (base) | $5,000/variant, 100% — lands exactly on the old boundary, still clears | no |
| total_budget (MA2) | +50% ($90,000) | $5,000/variant (base) | $15,000/variant | no |
| cost_per_conversion (MA3) | −50% ($10) | $2,500/variant | $10,000/variant, 400% | no |
| cost_per_conversion (MA3) | +50% ($30) | $7,500/variant | $10,000/variant, 133% ($2,500/33% to spare) | no |
| conversion_rate (MA4) | ±50% | n/a (applies to both) | tie both directions | no |
| cpm (MA5) | ±50% | n/a (applies to both) | tie both directions | no |

The worst-case single-dial move (MA1 or MA3 at +50%, raising the threshold to $7,500/variant) still
clears the new $10,000/variant split with **$2,500 (33%) real margin** — not exactly at the raised
threshold, and not the pre-retune situation where the *base* threshold itself was already the
knife-edge. MA2's own −50% flex is structurally interesting: it lands exactly on the case's prior
$30,000 setting and still clears (`≥` threshold), rather than falling below it — the old
"zero-slack tie" is now merely the *floor* of a ±50% swing, not the case's resting state.

**No `case.json.sensitivity_disclosure[]` entry was added or is needed** — unlike `fret-board`,
`cooling-curve`, and `enclosure-call`'s equivalent P5 findings (all closed via disclosure because
their arithmetic could not support genuine robustness), this case's retune produced real,
machine-verified robustness. There is nothing left to disclose.

### Files touched

- `cases/placement-test/case.json`: `balance.argument_a/argument_b/margin_note`,
  `needs_source[MA2].resolution`, `modeling_assumptions[MA1,MA2,MA3]`, `sensitivity_note`,
  `derived{}` (D2/D3/D4 recomputed for $60,000/$10,000-per-variant), `qa.*` (state, hash, tier2.P5,
  new `second_retune_note`).
- `cases/placement-test/case.md`: Appendix B (`$60,000 [MA2]`), Appendix E MA1/MA2/MA3 rows.
- `cases/placement-test/FACILITATOR.md`: top balance-flag note, Anchor 4, the trap section's dollar
  figures, the Deep Conflict thread (rewritten — the pedagogical hook is now "a tie the math
  genuinely cannot break" rather than "a tie with zero slack"), Socratic Q5, Close section, Lessons
  Learned bullets, the 45-minute plan table, and the full Facilitator-only numbers answer key.
- `cases/placement-test/sensitivity_model.py`: `PARAMS.total_budget` → 60000.0, header docstring and
  inline comments corrected to describe the post-retune mechanics.

No numbers were invented beyond the single grounded choice of MA2 = $60,000; every other figure in
this pass (D2/D3/D4, the flex-sweep table) is arithmetic derived from that one change, re-verified
by running the actual scripts rather than computed by hand and asserted.

### Tier 1 — structural (20 checks), re-run 2026-08-30

`python3 skills/case-readiness/scripts/tier1_structural.py --case placement-test`

**PASS 17 / GAP 2 / FAIL 0. `sha256(case.md)` = `563ddf989d015c60d1ce826ee54ab011f855f6649f6a118b59ba3a2a6ca79fe0`**
(new hash — case.md changed this pass: Appendix B, Appendix E MA1/MA2/MA3 rows). T1-16 (QA hash)
now current. Same two pre-approved GAPs as every prior pass, both unrelated to this change: T1-10
(reinforcement carve-out) and T1-13 (Twist: N/A, justification already written).

**BLOCKER: 0. GAP: 2 (both expected/benign). VERDICT: TIER1_PASS.**

Preflight linter (`preflight_lint.py --case placement-test`) unchanged: 1 advisory finding, the same
line-189 HTML-comment false positive noted in every prior pass. Not blocking.

### Tier 2 — simulated play (6 probes), fully re-adjudicated 2026-08-30

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Dispatched a genuinely fresh subagent with only the regenerated `/tmp/coldsolve-placement-test/PACKET.md` (no access to `case.json`/`FACILITATOR.md`/`QA_REPORT.md`/`sensitivity_model.py`). It chose **Option A**, tie-breaking on D3's clearance margin (1200% vs. 200%) once D4 came out an exact tie — correct arithmetic throughout (D1=60, D2=$60,000/$10,000 per variant, D3=1200%/200%, D4=1.333 conversions/$ for both), a named metric, and an independently-identified strongest-counterargument and least-supported-number (MA3, the $20/conversion estimate) matching this case's own designed tension. Reaching **A** rather than **B** is not a failure here — `FACILITATOR.md`'s own Close section states this case "does not have a single correct final vote," and A-via-reliability is exactly the legitimate landing it anticipates. |
| P2 both-sides | **PASS** | `balance.argument_a`/`argument_b` rewritten with the new $60,000/$10,000 figures. Neither side collapses: A leans on 1200% threshold clearance (single-hypothesis reliability), B leans on 200% clearance (real room to spare, not a knife-edge) plus the genuine 6-variant signal Argument A can never produce. |
| P3 trap | **PASS** | The trap mechanism (compute D1/D2 correctly, skip D3, treat "6 variants tested" as automatically better) is unchanged by this pass — only the dollar figures in `FACILITATOR.md`'s trap paragraph were updated for consistency with the new numbers. Independently re-derivable from `case.md` alone; matches the guide's named trap. |
| P4 twist | **PASS** | `Twist: N/A` justification is budget-figure-independent (a one-shot allocation decision with a hard deadline, no sourceable fact to withhold) — untouched by this pass, still sound. |
| P5 sensitivity | **PASS** | Genuinely, not disclosure-gated — see "Verified genuine slack" above. `tier2_probes.py --probe 5 --flex 0.5`: 0 of 10 flex directions flip the recommendation or breach the 20% cap. No `sensitivity_disclosure[]` entry needed. |
| P6 data decay | **PASS** | Live-refetched `S1` (`support.google.com/google-ads/answer/7065882`): the "at least 30 conversions... 50 conversions for Target ROAS" figure confirmed verbatim, still current. `S2` (Meta Business Help Center) remains unfetchable via WebFetch — the same pre-existing, disclosed JS-shell-rendering limitation as every prior pass (`S2.note`), third-party-corroborated, not a new problem. |

**Tier 2 result: 6 PASS, 0 FAIL.** Per SPEC §2/MCS-26 ("PASS or PASS_DISCLOSED for `TIER2_PASS`"),
this case now reaches **`TIER2_PASS`**, closing out the human-judgment flag every prior pass carried
forward.

### Tier 3 — human dry-run
NOT RUN. (Out of scope for `case-readiness`.)

---

## case-readiness run — 2026-08-27 (P5/P6 close-out pass)
**State:** TIER1_PASS → TIER1_PASS (unchanged)   **Verdict:** TIER1_PASS. Tier 1 re-confirmed clean
(0 blockers, 2 expected/benign gaps, fresh `sha256(case.md)` matches `case.json.qa`). Tier 2 fully
re-adjudicated: **5 PASS, 1 FAIL (P5) — not `TIER2_PASS`.**

This pass closes out the two Tier-2 findings the prior adjudication (below) left open.

### What changed for P5 (assumption sensitivity)

`sensitivity_model.py`'s ±50% flex run (prior pass) found a real, previously-undisclosed
interaction: `case.json.modeling_assumptions[MA1].sensitivity` claimed weeks-remaining "does not
affect the A-vs-B recommendation," but Appendix C's threshold formula is `(50 events/week [S2] ×
weeks_remaining) × $20/conversion [MA3]`, so it scales with MA1 too. A +50% flex (5 → 7.5 weeks)
raises the threshold from $5,000 to $7,500/variant, which Full Rotation's fixed $5,000/variant
split no longer clears — flipping the recommendation to Option A, exactly like an MA2 decrease or
MA3 increase.

**Fixed by honest disclosure, not retune or a forced pass:**
- `case.json.modeling_assumptions[MA1].sensitivity` rewritten to state the threshold-formula
  interaction plainly (no new numbers invented — the $7,500 figure is the same arithmetic
  `sensitivity_model.py` and the case's own D3 formula already produce).
- `case.md`'s Appendix E MA1 row rewritten to match, word-for-word consistent with how MA2/MA3's
  rows already read.
- `FACILITATOR.md`'s Anchor 4 script corrected (it previously told facilitators "MA2 and MA3 are
  the only two that can flip it" — now says three can, MA1 included, with the mechanism explained).
- `FACILITATOR.md`'s Deep Conflict section gained a new "Why this is stronger material than a QA
  checkbox" paragraph, naming all three flip-capable assumptions together and giving facilitators
  an explicit closing question built around it — treating the zero-slack fragility as pedagogical
  material, not a checkbox to clear.
- `FACILITATOR.md`'s Facilitator-only numbers section (the answer key) updated to name all three
  flip-capable dials and the mechanism for each.
- `sensitivity_model.py`'s header comment corrected (it previously said MA1 was "inert" to the
  verdict, which was never true of the *model* — only of the case's stale prose; the model's
  `_threshold_per_variant()` always correctly included `weeks_remaining`).

**Deliberately NOT done:** no `case.json.sensitivity_disclosure[]` entry was added for MA1, MA2, or
MA3. `tier2_probes.py`'s mechanical P5 check only flips to PASS if every unstable param gets a
category-F ("forecast/irreducible unknown"), -X ("proprietary, analogue-estimated"), or -I
("validated interpolation") disclosure entry. MA1/MA2/MA3 are fictional, author-chosen scenario
dials — an unsourceable internal production calendar, an unsourceable internal budget, and a round
mid-range cost estimate — not a genuine instance of any of those three categories. Forcing one
onto them to mechanically clear P5 would misrepresent *why* they're uncertain, which is exactly
what this project's disclosure mechanism exists to prevent. This follows the same
disclosure-over-retune(-or-fudge) pattern `enclosure-call` and `fret-board`'s equivalent P5
findings used: fix the case's honesty, not the probe's pass rate. Re-running
`tier2_probes.py --case placement-test --probe 5 --flex 0.5` confirms: all three flips reproduce
exactly (`weeks_remaining +50% -> A`, `total_budget -50% -> A`, `cost_per_conversion +50% -> A`),
and the probe still reports `UNDISCLOSED instability` because no `sensitivity_disclosure[]` entry
exists — **verdict stays FAIL, correctly**, now for the honest reason (no matching F/X/I category
applies) rather than for a missing disclosure.

### What changed for P6 (data decay)

Live-fetched `S1`'s cited primary URL again: `support.google.com/google-ads/answer/6268633` still
does not carry the "30 conversions / 30-day" figure (only an unrelated "50 conversions" mention).
Live-fetched the corroborating URL named in the old `S1.note`,
`https://support.google.com/google-ads/answer/7065882?hl=en` ("About Smart Bidding") — confirmed it
carries the figure verbatim: *"Google Ads recommends measuring performance over longer time periods
that have at least 30 conversions, such as a month or longer (50 conversions for Target ROAS)."*

**Fixed:** `case.json.sources[S1]` and `case.md`'s Appendix F Sources row retargeted — the
corroborating URL is now `S1`'s primary citation (`title`, `url`, `accessed` all updated to
2026-08-27), and the old, now-figure-less URL is dropped rather than kept as a secondary reference,
since it no longer supports the claim. `S2` (`en-gb.facebook.com/business/help/269269737396981`)
left unchanged — its JS-shell fetch limitation was already disclosed in `S2.note` before this pass
and is not a new problem; not re-litigated here per the task scope. Re-running
`tier2_probes.py --case placement-test --probe 6` now reports the fresh S1 URL (age 0d) in its
worklist — **verdict: PASS**.

### P1–P4, re-confirmed

Nothing in Background, the Challenges, or Appendices A–D changed in this pass — only Appendix E/F
(reference tables) and `FACILITATOR.md` (never student-facing) did. `tier2_probes.py --probe 1`
regenerated a fresh `/tmp/coldsolve-placement-test/PACKET.md` reflecting the corrected Appendix E,
and a genuinely fresh subagent (no access to `FACILITATOR.md`/`QA_REPORT.md`/`case.json`) was
dispatched against it: chose **B**, reproduced the case's arithmetic exactly (D1=60, D2=
$5,000/variant, D3=100%, D4=1.333 conversions/$, exact tie), and — without having read the
corrected disclosure — independently named MA2 as most load-bearing while also noting "MA1
weeks-remaining and MA3 cost-per-conversion have the same flip potential, per the appendix,"
correctly reflecting the fixed text. **P1: PASS.** P2 (both-sides), P3 (trap), and P4 (twist)
verdicts are carried forward unchanged from the prior full adjudication below — their underlying
case content did not change, and re-litigating them was not necessary. **P2: PASS. P3: PASS.
P4: PASS.**

### Tier 2 — simulated play (6 probes), final for this pass

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | fresh subagent (fresh packet), B, exact arithmetic, correctly named all three flip-capable dials |
| P2 both-sides | **PASS** | carried forward — unaffected content |
| P3 trap | **PASS** | carried forward — unaffected content |
| P4 twist | **PASS** | carried forward — unaffected content |
| P5 sensitivity | **FAIL** | now fully, honestly disclosed in prose (MA1/MA2/MA3 all named as flip-capable); mechanically still FAIL because no `sensitivity_disclosure[]` F/X/I entry applies honestly to these fictional scenario dials |
| P6 data decay | **PASS** | S1 retargeted to a live, figure-carrying URL; S2's pre-existing, disclosed tooling limitation left as-is |

**Tier 2 result: 5 PASS, 1 FAIL. Per SKILL.md ("all six probes recorded, 0 FAIL"), this case does
NOT reach `TIER2_PASS`.** State remains `TIER1_PASS`.

**Human-judgment flag, unchanged from the prior pass and now sharper:** the case's tie is real,
correctly computed, and legitimately in the intentional-0%-margin tradition — but it sits at a
**zero-slack boundary** where **three** independently plausible assumption moves (MA1 up, MA2 down,
MA3 up) each flip it to a large Option A win, and all three are now honestly disclosed in
`case.json`, `case.md`, and `FACILITATOR.md`. This is a genuine authoring judgment call, not a
mechanical defect: a human should decide whether to (a) add real budget slack so the tie stops
being knife-edge, or (b) keep the razor's-edge framing deliberately — it is pedagogically strong,
and `FACILITATOR.md`'s Deep Conflict section now makes the three-dial fragility an explicit
discussion beat rather than a hidden risk. Either path is legitimate; this pass did not make that
call, only made sure it is impossible to miss.

### Tier 3 — human dry-run
NOT RUN. Not reachable until `TIER2_PASS`.

---

## case-readiness run — 2026-08-27 (remediation pass)
**State:** BLOCKED → TIER1_PASS   **Verdict:** TIER1_PASS (Tier 1 clean, 0 blockers; Tier 2
mechanical pre-screens clear but probes not yet adjudicated)

This is a `case-write`-stage remediation pass on the three BLOCKERs from the prior run (T1-09,
T1-10, T1-13). See "What changed" below for the exact fixes, including the SPEC §2 balance retune.

**Preflight lint (advisory):** unchanged — 1 finding, line 189 of `case.md`, the same HTML comment
false positive noted in the prior run (`<!-- FACILITATOR ONLY: ... -->`). Not blocking.

### What changed

**[T1-09] SPEC §2 balance test — genuine retune, not a computed-then-hidden number.**
The prior run's `margin_pct: null` was not a missing-arithmetic problem: at the case's originally
stated $18,000 budget (MA2), `margin_basis`'s own exclusion rule (drop any Full Rotation variant
below Appendix C's $5,000/variant threshold) left **all six** variants below threshold, so Option
B had zero usable attributable conversions — Option A would win by construction, a real SPEC §2
balance failure (the same shape of finding `fret-board`'s QA_REPORT.md flagged for a human).
Confirmed real, not a misreading: the case's own `MA2` sensitivity note already documented this
exact mechanism and its own flip point ("recommendation flips toward Option B once total budget
reaches roughly $30,000 or more").

**Resolution:** raised MA2 from $18,000 to **$30,000** — the flip threshold the case's own
documentation already named, not a new invented number. At $30,000, every Full Rotation variant's
$5,000 split spend clears the $5,000/variant threshold exactly (100%, zero dollars to spare).
Because the conversion-rate (MA4, 2%) and CPM (MA5, $15) assumptions apply identically to both
options once every variant clears, the two options' conversions-per-dollar rates are structurally
identical whenever B clears — so this retune produces an **exact tie, `margin_pct = 0.0%`**, well
inside SPEC §2's ~20% cap. Both totals: 40,000 attributable conversions on the $30,000 spend for
either option (arithmetic: `1000/$15 CPM × 2% conv. rate = 1.333333 conversions/$`; full working
in `case.json.derived` and `FACILITATOR.md`'s "Facilitator-only numbers" section). Updated
`case.md` Appendix B, Appendix E (MA2, MA3 rows), and `case.json` (`margin_pct`, `balance.*`,
`modeling_assumptions[MA2,MA3]`, `sensitivity_note`, `derived{}`, `needs_source[MA2].resolution`).

**Judgment call flagged for a human:** the resulting tie sits exactly at the Appendix C threshold
with zero slack — B's $5,000/variant spend equals the $5,000 minimum precisely. Any downward move
in MA2, or any upward move in MA3 above $20/conversion, flips the case straight back to a ~100%
Option A win. This fragility is disclosed in `case.json.balance.margin_note` and in
`FACILITATOR.md`, not hidden, but a human may want to add slack (e.g. $36,000+) on a future
revision if the exact-boundary framing feels too razor-thin for classroom use. Not changed here,
to avoid picking a second, less-documented number beyond the one the case itself already named.

**[T1-10] SPEC §8 reinforcement carve-out — mechanical transcription, done.**
Copied the already-adequate justification from `FACILITATOR.md`/`LEARNING_GOALS.md` into
`case.json.reinforcement_note` (both permutation skills were already `n=1` via `Codebreaker`,
concept-sheet pre-authorized). No new authoring; downgrades T1-10 from BLOCKER to the expected
GAP per the 2026-08-17 doctrine amendment.

**[T1-13] FACILITATOR.md — full rewrite to the §7.1/§7.2/§7.3 shape.**
Rewritten to the complete anchor ladder (Intro / Launch / Anchor 1–4 / Data Deep Dive / Twist /
Close / Lessons Learned / Standards Touched On), preserving and folding in the original 5 Socratic
questions (now single-line, per the mechanical checker's format expectation) and the original
trap description (sharpened with concrete numbers so it reads as a learner action, not a
difficulty note — see P3 fix below). Added a full 45-minute timed Socratic plan (§7.3) and a
one-thread Deep Conflict section (T2 compression). `Twist: N/A` recorded with a written
justification (no sourceable withheld fact exists for a one-shot budget-allocation dilemma without
inventing a number — same reasoning pattern as `the-optimal-can`'s Twist: N/A). Added
`case.json.cohort_bands[]` (Full / Compressed / 1:1-pair, §7.4).

### Tier 1 — structural (20 checks), after remediation

| id | result | note |
|---|---|---|
| T1-01–T1-08 | PASS | unchanged from prior run |
| T1-09 | **PASS** | balance test: both arguments written (now with concrete numbers), `margin_pct` = 0.0%, well inside the ~20% cap |
| T1-10 | GAP | reinforcement carve-out — `case.json.reinforcement_note` now present and adequate (downgraded from BLOCKER, expected) |
| T1-11 | PASS | learning-goal mutual reachability, unchanged |
| T1-12 | PASS | unchanged |
| T1-13 | GAP | MCS-15 — Twist is `N/A`; checker flags this state for human confirmation, which this report provides (see "What changed" above) |
| T1-14 | PASS | FACILITATOR.md continuity with case.md/case.json |
| T1-15 | PASS | no `published/` yet |
| T1-16 | PASS | QA hash current (`033d2096f11e16b7d831342788a597c1a7f4f22b593c5b77fa2c16eea6af2d8e`) |
| T1-17 | PASS | `cohort_bands[]` now declared (Full/Compressed/1:1-pair) |
| T1-18–T1-20 | PASS | no `published/` directory, nothing to check |

**BLOCKER: 0. GAP: 2 (both expected/benign — see above). VERDICT: TIER1_PASS.**

### Tier 2 — simulated play (6 probes)

Ran `tier2_probes.py --case placement-test`. Mechanical pre-screens now all clear (fixed two real
findings from the first Tier-2 attempt during this pass):

- **P2 both-sides-solve** — originally mechanically `FAIL`: both `balance.argument_a`/`argument_b`
  carried almost no digits (SPEC §2 wants the strongest *quantitative* argument for each side).
  Fixed by adding concrete figures ($30,000 total, 1 vs. 6 variants, $5,000/variant threshold) to
  both arguments without leaking the margin/winner. Now `READY`.
- **P3 trap-check** — originally mechanically `FAIL`: the trap description read as a difficulty
  note rather than a learner action. Fixed by naming the concrete wrong path more directly
  ("will often... recommend... missing D3 entirely, never checking..."). Now `READY`.
- **P1 cold-solve** — `READY`; packet built at `/tmp/coldsolve-placement-test/PACKET.md`, leak-free.
- **P4 twist-integrity** — `READY` (N/A twist, justification written).
- **P5 assumption-sensitivity** — `NOT RUN`: no `cases/placement-test/sensitivity_model.py` exists.
  Same as the prior run; out of this remediation's scope (T1-09/T1-10/T1-13 only).
- **P6 data-decay** — `DELEGATED`: sandbox has no outbound network; S1/S2 URLs need a live fetch.

**All six probes still require a genuinely fresh subagent / live fetch to produce a recorded
verdict** (per `skills/case-readiness/SKILL.md`'s own rule: a probe with no recorded verdict is
`NOT RUN`, not a pass). That adjudication was not performed in this remediation pass — it is
explicitly the next step, separate from the BLOCKER fixes this pass was scoped to. State remains
`TIER1_PASS`, not `TIER2_PASS`.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | NOT RUN (mechanically READY) | packet built and leak-free; needs a fresh subagent dispatch |
| P2 both-sides | NOT RUN (mechanically READY) | prior mechanical FAIL fixed this pass |
| P3 trap | NOT RUN (mechanically READY) | prior mechanical FAIL fixed this pass |
| P4 twist | NOT RUN (mechanically READY) | N/A twist, justification written |
| P5 sensitivity | NOT RUN | no `sensitivity_model.py` |
| P6 data decay | NOT RUN | delegated — needs live fetch of S1/S2 |

### Tier 3 — human dry-run
NOT RUN.

## case-readiness run — 2026-08-27 (Tier 2 adjudication)
**State:** TIER1_PASS → TIER1_PASS   **Verdict:** Tier 2 fully adjudicated, 4 PASS / 2 FAIL —
**not TIER2_PASS**. `sha256(case.md)` unchanged (`033d2096f11e16b7d831342788a597c1a7f4f22b593c5b77fa2c16eea6af2d8e`),
confirmed by a fresh `tier1_structural.py` run (0 blockers, 2 gaps, same as prior).

This pass ran all six Tier 2 probes to genuine, independently-adjudicated verdicts (a fresh
subagent for P1, a written `sensitivity_model.py` for P5, and live fetches of both `sources[]`
URLs for P6) — the work the prior remediation pass explicitly left pending.

### P1 · Cold solve — PASS

Dispatched a genuinely fresh subagent with only `/tmp/coldsolve-placement-test/PACKET.md` (no
`FACILITATOR.md`, `QA_REPORT.md`, or `case.json`). It chose **B**, optimizing D4 (attributable
conversions/dollar), and reproduced the case's arithmetic exactly: D1 = 60 (`5P3`), D2 =
$30,000/$5,000 per variant, D3 = 600%/100%, D4 = 1.3333 conversions/$ for both, an exact tie. It
independently named MA2 as the most sensitive assumption ("set exactly at the level where Full
Rotation's $5,000/variant split just barely clears the Appendix C threshold") and MA3 ($20/conv.)
as the least-supported figure — both matching the case's own documented fragility without having
read it. Reached the answer by the right route, with correct arithmetic and a named metric.

### P2 · Both-sides solve — PASS

Built the strongest quantitative case for each option from `case.md` alone. **A:** all $30,000 on
1 variant, 600% clearance, zero risk of any data being excluded as unreliable — the single most
statistically trustworthy read this quarter can produce, at the cost of testing only 1 of 6
combinations. **B:** identical $30,000 split six ways at $5,000/variant, clearing Appendix C's
threshold exactly, so none of the extra timing/CTA signal is thrown out, and D4 shows this costs
nothing in conversions-per-dollar. Neither side collapses under pressure: A's case is genuinely
solid on reliability grounds (600% cushion is real, not a bluff), and B's case is genuinely solid
on signal grounds (the tie is not a paper number — the fresh-subagent solve in P1 reproduced it
independently). B's argument has an acknowledged soft spot (100% clearance is exactly at the
threshold, not comfortably above it), but that is the case's own designed tension, not a collapse.

### P3 · Trap check — PASS

Read `case.md` fresh, before opening `FACILITATOR.md`. Independently named the trap: a student
correctly computes D1 (60 sequences) and D2 ($5,000/variant) and then recommends B purely on "6
variants tested = 6x the information," never checking D3 — i.e., treating variant count as
automatically meaning usable signal, without verifying each variant's split spend actually clears
the platform's minimum-viable-spend threshold. `FACILITATOR.md`'s "The trap" section names this
exact path verbatim ("missing D3 entirely, never checking whether each of those six $5,000 splits
actually clears the platform's $5,000/variant minimum-spend threshold"). Guide anticipates the
trap that will actually catch the room.

### P4 · Twist integrity — PASS

`Twist: N/A` in `FACILITATOR.md`, justified as: a one-shot budget-allocation recommendation with a
hard deadline, where no sourceable fact exists that could be withheld from Background and revealed
mid-discussion without either fabricating a number (forbidden by SPEC §5) or merely restating
information the Hero already has by Anchor 4. Checked this independently: the only plausible
twist candidate for a case like this — "the budget shrinks/CPM rises after the fact" — would
require inventing an unsourced dollar or percentage figure, exactly the fabrication SPEC §5
forbids, and the case's own Anchor 4 / Deep Conflict sections already carry the "what if the
numbers move" pressure a twist would otherwise add. The justification is sound, and the same
reasoning pattern already used for `the-optimal-can` is genuinely analogous here, not just cited by
label. `case.json` has no `facilitator.twist` key and `FACILITATOR.md` carries a `## Twist`
heading with the N/A justification, so the mechanical MCS-15 check is also satisfied.

### P5 · Assumption sensitivity — FAIL (genuinely unstable, undisclosed)

Wrote `cases/placement-test/sensitivity_model.py` (contract: `PARAMS`, `evaluate()`, `FLEX[]` of
5 assumption dials — MA1–MA5; no `evaluate_twist()`, consistent with Twist: N/A). Base case
reproduces `case.json.derived` exactly: `A = B = 40,000` conversions, `margin_pct = 0.0`, Appendix C
threshold = $5,000/variant. Ran `tier2_probes.py --probe 5 --flex 0.5`:

```
weeks_remaining  -50% -> TIE (no change)      weeks_remaining  +50% -> A wins (B excluded, margin "4,000,000%")
total_budget     -50% -> A wins (B excluded)  total_budget     +50% -> TIE (no change)
cost_per_conv.   -50% -> TIE (no change)      cost_per_conv.   +50% -> A wins (B excluded)
conversion_rate  ±50% -> TIE both directions (applies identically to both options, as documented)
cpm              ±50% -> TIE both directions (applies identically to both options, as documented)
```

This **confirms exactly** what the task flagged going in and what the case's own `sensitivity_note`
already documents: a downward move in MA2 (budget) or an upward move in MA3 (cost/conversion)
above $20 flips the case straight back to a large Option A win, because one or more Full Rotation
variants drop below the Appendix C $5,000/variant threshold and are excluded from B's total. The
margin-% figures the script prints on these flips (millions of percent) are a formula artifact of
`base[loser] == 0` after exclusion (the script's own documented `zero_baseline_caveat`), not a
literal percentage — the real finding is the binary flip, not the number.

**One new, previously-undisclosed finding:** `case.json`'s MA1 sensitivity claim — "Only changes
the magnitude of D1's permutation count. Does not affect the A-vs-B recommendation as long as at
least 3 weeks remain" — is **not fully accurate**. Appendix C's threshold formula is `(Meta's 50
events/week × weeks_remaining) × $20/conversion [MA3]`, so it scales with `weeks_remaining` too. A
+50% flex on MA1 (5 → 7.5 weeks) raises the threshold from $5,000 to $7,500/variant, which B's
fixed $5,000/variant split no longer clears — flipping the recommendation to A, contradicting the
case's own stated claim that MA1 doesn't affect the recommendation. This is a real interaction the
case's Appendix E / `modeling_assumptions[MA1].sensitivity` text does not currently disclose.

Per the skill's disclosure-aware pass rule, an unstable param can still PASS if given a matching
`case.json.sensitivity_disclosure[]` entry with an honest F/X/I category. I deliberately did **not**
add one: MA1/MA2/MA3 are fictional, author-chosen scenario dials (an internal, unsourceable budget
and headcount-schedule detail; a round mid-range cost estimate), not a forecast/irreducible-unknown
(F), a proprietary-but-estimated-from-a-public-analogue figure (X), or a validated
interpolation/extrapolation (I) — forcing one of those labels onto them to flip this to a
mechanical PASS would misrepresent why they're uncertain, which the instructions establishing that
mechanism explicitly rule out. **Verdict: FAIL**, genuinely and not for lack of trying — this is
the same fragility already disclosed in prose (`balance.margin_note`, `FACILITATOR.md`), now
machine-confirmed, plus one new interaction (MA1) that prose disclosure currently misses.

### P6 · Data decay — FAIL (one source's cited URL no longer carries its figure)

Live-fetched every `sources[].url`:

- **S1 primary** (`support.google.com/google-ads/answer/6268633`) — reachable, HTTP OK, but three
  separate fetches of its current content found only "at least 50 conversions, for a clearer
  perspective" (about assessing bid-strategy reports) — **no "30 conversions per 30-day period"
  figure appears anywhere on this page as currently rendered**, even though that is exactly the
  value `S1.value` cites this URL for. This is the "resolves but no longer carries the figure"
  case the skill calls worse than a 404.
- **S1 corroborating URL** (`support.google.com/google-ads/answer/7065882`, named in `S1.note`) —
  reachable, and *does* carry the cited figure verbatim: "Google Ads recommends measuring
  performance over longer time periods that have at least 30 conversions, such as a month or
  longer (50 conversions for Target ROAS)." The underlying fact is real and live; the case's
  primary citation just points at the wrong one of its two named URLs now.
- **S2** (`en-gb.facebook.com/business/help/269269737396981`) — reachable (HTTP OK) but, as
  `S2.note` already disclosed, serves a JS-rendered shell WebFetch cannot read (confirmed again on
  two fetch attempts, including a `.com` non-`en-gb` retry). A web search independently
  corroborates the cited "~50 optimization events within 7 days to exit Learning" figure via
  multiple third-party sources referencing Meta's guidance, but this is not a direct read of
  Meta's own page, same limitation as before.

**Verdict: FAIL.** Not because a figure is fabricated or false — both cited values are still real
and independently confirmed — but because S1's `sources[].url` field cites a specific page that no
longer visibly carries its own cited figure, which is exactly the silent-drift failure mode P6
exists to catch. **Fix recommended for `case-research`/`case-write`, not applied here:** swap S1's
primary `url` to `https://support.google.com/google-ads/answer/7065882?hl=en` (confirmed live to
carry the figure verbatim) and demote the current primary URL to a secondary/corroborating
reference, or drop it.

### Tier 2 — simulated play (6 probes), final

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | fresh subagent reached B by the right route, exact arithmetic match |
| P2 both-sides | **PASS** | neither side collapses; both are genuinely quantitative |
| P3 trap | **PASS** | independently-named trap matches the guide's named trap exactly |
| P4 twist | **PASS** | N/A justification checked and sound; no fabrication-free twist exists |
| P5 sensitivity | **FAIL** | confirms MA2-down/MA3-up flip exactly as case predicted; PLUS a new undisclosed MA1 interaction; no honest F/X/I disclosure category applies |
| P6 data decay | **FAIL** | S1's cited primary URL no longer carries its figure (corroborating URL does); S2 still unfetchable (known tooling limit, third-party-corroborated) |

**Tier 2 result: 4 PASS, 2 FAIL. Per SKILL.md ("all six probes recorded, 0 FAIL"), this case does
NOT reach `TIER2_PASS`.** State remains `TIER1_PASS`. Both FAILs are fixable without new
authoring judgment (retarget one URL; either add slack to MA2/retune, or write an honest
F/X/I-categorized `sensitivity_disclosure[]` entry if the case's owner judges the fictional-budget
dial genuinely fits one of those categories — I did not make that call unilaterally) — but per
this skill's own rule, neither may be marked PASS until actually fixed and re-probed.

**Human-judgment flag, separate from the mechanical FAILs above:** this case's tie is real,
correctly computed, and legitimately in the Payroll-precedent tradition of an intentional
0%-margin design — but it sits at a **zero-slack boundary condition** (B's spend equals the
threshold exactly), which P5 now shows flips under a plausible ±50% move in either of two
assumptions, plus a third (MA1) the case doesn't currently disclose as load-bearing. A human should
decide whether to (a) add real budget slack (e.g. the $36,000+ figure the prior QA pass already
suggested) so the tie is robust rather than knife-edge, or (b) keep the razor's-edge framing
deliberately (it is pedagogically defensible — the Deep Conflict section already turns "zero slack"
into the discussion question) and instead formally disclose all three unstable dials. Either path
clears P5; neither is a purely mechanical fix.

### Tier 3 — human dry-run
NOT RUN.
