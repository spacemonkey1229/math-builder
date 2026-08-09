# QA Report — Cold Chain

**Run:** 2026-07-31 · **Method:** independent adversarial verification (subagent, no authoring context) + mechanical checks
**`sha256(case.md)`:** `47d99383c7f83f16…` — `case-publish` must refuse if this changes
**Verdict:** **PASS WITH GAPS** — 12 BLOCKERs found, 12 resolved · 3 GAPs open, none blocking

---

## Arithmetic — independently reproduced

Every figure below was recomputed from stated dimensions by a verifier with no access to the authoring reasoning, and three of the five containers were re-checked against live UNICEF catalogue pages.

| Container | Volume (cm³) | SA (cm²) | SA:V | Cold life (h) |
|---|---|---|---|---|
| RCW4 | 30,631 | 5,906 | 0.19281 | 30.3 |
| RCW8 | 74,003 | 11,043 | 0.14922 | 57.9 |
| AOV ACB-264SL | 133,444 | 15,858 | 0.11884 | 132.3 |
| RCW25 | 194,860 | 20,385 | 0.10461 | 134.6 |
| Blowkings CB-20-CF | 252,436 | 24,270 | 0.09614 | 138.0 |

**Monotonicity confirmed:** SA:V strictly falls while cold life strictly rises, across all five.

| Check | Result |
|---|---|
| Order A cost | 3 × 102.21 = $306.63, under $320 by $13.37 ✓ |
| Order B cost | 2 × 128.00 = $256.00, under $320 by $64.00 ✓ |
| Cost per litre | A $17.04/L · B $6.40/L → B is 37.6% of A ✓ |
| Capacity → doses | A 18,000 ÷ 2.1 = 8,571 ✓ · B 40,000 ÷ 2.1 = 19,047 ✓ |
| Cold-life ledger, A | 132.3 − 8 = 124.3 h · Bulera h118 in spec (6.3 h slack) · Nyamirama h134 excursion (−9.7 h) ✓ |
| Cold-life ledger, B | 138 − 8 = 130 h · all four stops in spec · 34 h slack at h96 ✓ |
| **Balance** | A 7,771 · B 7,000 · **margin 11.0%** — inside the SPEC §2 cap under either denominator ✓ |
| Twist | +9 h → Bulera 127, Nyamirama 143, both excursions · A falls to 6,571, below B ✓ |
| Spoilage value | 800 × $0.34–$0.4230 = $272.00–$338.40 ✓ |

## Read-model integrity — clean

- All 32 `standards[]` ids resolve in the spine; no duplicates; `n_standards` correct.
- `new_coverage[]` ⊂ `standards[]`; all three promoted skills show `covered_by == ["Cold Chain"]` exactly, proving they were genuinely n=0.
- Exactly 32 spine rows contain "Cold Chain", set-identical to `standards[]`. No double-appends, no other case string mutated. `n == len(covered_by)` on all 322 rows.
- Spine totals recount exactly: 322 skills, 28 cases, 97 uncovered, 82 thin.
- `gap_queue.json` regenerates **byte-identical** from the spine — confirmed a pure derived view.
- `dashboard.html --verify`: 46 checks, 0 failed.

---

## BLOCKERs found and resolved

| # | Finding | Resolution |
|---|---|---|
| B1 | QA gate never actually run; no report, no hash | This report; `case.json.qa{}` with sha256 |
| B2 | Challenge 2 not verbatim against `CHALLENGE_BOILERPLATE.md` (drift at char 110) | Canonical block pasted |
| B3 | Numeral form `**1.**` instead of locked `1.)` — broke the QA diff entirely, so a rewritten Challenge 2 passed silently | Restored `1.)` form throughout |
| B4 | Cold Chain absent from `cases_index.json` → unassignable by `case-track`, rendered null in the dashboard | Record appended |
| **B5** | **+8/+10 conflation.** Appendix B defines excursion at +8 °C; Assumption 2 warmed linearly to +10 °C over cold life ⟹ in-spec time = 0.75 × cold life ⟹ **Order B wins before the twist**, inverting the case | Assumption 2 rewritten: the container holds +2…+8 °C for its full rated cold life and fails quickly after. Cold life = in-spec time. Stated as the optimistic direction, with an invitation to model it harder |
| **B6** | **Twist only fired under a pre-deduction convention the case never stated.** Applied sequentially, Bulera at h127 is in spec and the twist does nothing | Appendix F now states the convention explicitly ("deduct all planned openings up front"), and the guide flags the sequential reading as legitimate and worth surfacing |
| B7 | `case.json` didn't match the schema its own pipeline defines — no `margin_pct`, no `deliverables[]`, no `qa{}`, sources missing `id`/`title`. `case-publish` would KeyError | Schema conformed; 4 source rows added for previously uncited figures |
| B8 | MCS-10 could not execute — with no `deliverables[]`, all 32 standards were unreachable | 6 deliverables D1–D6 authored with explicit skill maps. **Unmapped: 0. Unreachable: 0.** |
| B9 | Overview carried load-bearing and *wrong* numbers: "nine thousand doses" (the key constraint), "four hundred kilometres" (contradicts Appendix C's 1,200 km), "half the price" (true per litre, false per box) | All three removed or corrected |
| B10 | MCS-11 hash gate falsely WIRED — nothing to check against | Hash recorded above |
| B11 | `readmodel/_snapshots/` didn't exist; read-model mutated with no recovery point | Snapshots written for all four mutated files |
| B12 | README branch-coverage table disagreed with the dashboard on 6 of 7 rows (pre-promotion figures under a "after Cold Chain" heading) | Table removed; README points at the dashboard as the single rendering |

## GAPs open — accepted, not blocking

| # | Finding | Disposition |
|---|---|---|
| G1 | Spine has 322 rows but 320 unique ids — `Digit` and `Congruent` each appear in two groups. A future case covering either will double-count | **Real defect, deferred.** Fix is group-scoped ids and a 322→320 rebaseline, which touches every artifact. Tracked in ROADMAP. No current case touches either skill |
| G7 | "SA:V predicts cold life precisely" was an overclaim — `cold_life × SA:V` spans 2.3×, and with n=5 the SA:V ordering is confounded with plain size | **Turned into the lesson.** The guide now says SA:V *orders* but does not *predict*, names the Appendix E insulation confounder, and asks students what data would separate them. D2 was rewritten to require it |
| G14 | `case-qa` skill text cites "SPEC §7 Definition of Done" — it is §8 since the facilitator section was inserted | Cosmetic in the skill, not the case. Tracked |

## Deliberate design choices the verifier flagged, kept as-is

- **25.4 kg vs the WHO 25 kg single-worker guidance (G2).** Order A's central premise exceeds the recommended lift by 0.4 kg. This was flagged as a possible contradiction; it is now explicit in Background and is one of the better discussion hooks in the case — a real logistics officer makes exactly this call.
- **`Volume`, `Distance` and `Weight` each resolve to two spine ids (G13).** A consequence of G1, not of the case. Both ids are claimed and both are now mapped to a deliverable.

---

## Sign-off

Cleared for publication. Both content-level defects that would have misled a classroom (B5, B6) are resolved. The remaining gaps are structural debt in the spine and in skill documentation, not in the case.

**Re-run required if `case.md` changes** — the hash above is the gate.

---

# case-readiness run — 2026-07-31

**Gate:** `skills/case-readiness/` (supersedes `case-qa`) · **Against:** SPEC.md v1.0, RUBRIC.md v1.0
**`sha256(case.md)`:** `47d99383c7f83f16…` — unchanged since the run above, so this report and that
one describe the same file.

**State reached: `DRAFT` → Tier 1 BLOCKED. VERDICT: BLOCKED.**
1 Tier-1 BLOCKER · 4 Tier-1 GAPs · **3 of 6 Tier-2 probes FAILED**

> This case was marked `published` before Tier 2 existed. Nothing in the earlier report is
> withdrawn — the twelve structural BLOCKERs it resolved are still resolved. What follows is what
> the earlier gate could not see.

## Tier 1 — structural (17 checks)

`python3 skills/case-readiness/scripts/tier1_structural.py --case cold-chain` → exit 1

| id | result | id | result | id | result |
|---|---|---|---|---|---|
| T1-01 sections | PASS | T1-07 spine labels | PASS | T1-13 facilitator | PASS |
| T1-02 overview | PASS | T1-08 citations | PASS | T1-14 continuity (guide) | GAP |
| T1-03 dilemma | PASS | T1-09 balance | PASS | T1-15 continuity (published) | **FAIL** |
| T1-04 boilerplate | PASS | T1-10 standards | PASS | T1-16 QA hash | PASS |
| T1-05 numeral form | GAP | T1-11 reachability | PASS | T1-17 cohort bands | GAP |
| T1-06 appendices | PASS | T1-12 tier load | PASS | | |

### BLOCKER

**T1-15 · CONTINUITY STALE.** `published/Cold Chain - Student Workbook.xlsx` was built at 17:44,
**22 minutes before** the last edit to `case.md` at 18:06. The workbook a student downloads is not
generated from the case of record. This is the Murder Mystery continuity bug in its local form —
the source changed and a derived artifact did not — and no previous check would have caught it.
*Fix: re-run `case-publish`. Do not hand-edit the workbook.*

### GAPs

- **T1-05** Challenge 2's `a.)`/`b.)` sub-lines are rendered as markdown bullets (`- a.)`); the
  boilerplate locks a bare indented `a.)`. Text is otherwise verbatim. Rendering drift, not a
  rewrite — recorded rather than normalised away.
- **T1-14** 22 numbers in `FACILITATOR.md` have no home in `case.md` or `case.json`:
  `2.3, 5.84, 7.5, 8.64, 9.7, 13.27, 14.08, 15.72, 50.63, 86.0, 124.3, 127.0, 130.0, 143.0, 272.0,
  338.0, 3200.0, 4000.0, 8571.0, 18000.0, …`. Each is a guide-only derived figure. They are correct
  today and there is nothing that will tell anyone when they stop being correct.
  *Fix: move them into `case.json.derived` so `T1-14a` can key-check them.*
- **T1-15** the same 25 figures reach `published/Guide Notes - Cold Chain.docx`.
- **T1-17** no `cohort_bands[]`. The Socratic plan is written for one unstated room size.

### POLISH

- Overview numerals `4`, `40` auto-classified as texture (clock time `4:40`).
- The final appendix parsed **29 labels: 15 bulleted and 14 from the middot-separated Vocabulary
  run.** Those 14 were invisible to the legacy check — MCS-05 had only ever been enforced on half
  of Appendix G.

## Tier 2 — simulated play (6 probes)

`python3 skills/case-readiness/scripts/tier2_probes.py --case cold-chain --model skills/case-readiness/scripts/example_sensitivity_model.py`

| probe | verdict | finding |
|---|---|---|
| **P1 cold solve** | **PASS with finding** | A fresh subagent, given only the student packet, chose Order A, named its metric ("in-spec doses"), and computed correctly — the right answer for the right reasons. **But it reached 8,200 in-spec, not 7,771**, because it allocated doses in circuit order. |
| **P2 both-sides** | **PASS with finding** | Both sides are defensible — B on arithmetic, A on values — and the collapse question is sharp: *"which box delivers to Nyamirama, opened how many times?"* **But a second fresh solver could not reproduce the 11.0% margin from the packet at all**, and called it "a paper number", because A's in-spec total swings by tens of percent depending on an unstated box-assignment convention. |
| **P3 trap check** | **FAIL** | The guide names an *equity* trap (optimise total doses, quietly decide Bulera and Nyamirama don't count). The more likely trap is *arithmetic*: D3 asks for total capacity and D5 asks separately for excursions, and nothing asks the student to net them — so a student can complete every deliverable correctly and headline "8,571 vs 7,000, a 22% margin". The guide does not warn about it, **and the same conflation has infected the guide's own key numbers**. |
| **P4 twist integrity** | **FAIL** | The twist's punchline — Order A falls *below* Order B — holds only under an allocation rule the case never states: the two motorcycle villages served at 100% of need while the four truck facilities absorb the entire 429-dose shortfall. Under circuit-order allocation, pre-twist A leads 8,200 vs 7,000 (17.1%, not 11.0%) and post-twist A **ties** at 7,000 rather than falling below. The guide separately concedes that a sequential reading of Assumption 1 also stops the twist firing. **Two unresolved conventions, only one disclosed.** |
| **P5 assumption sensitivity** | **FAIL** | Base A 7,771 · B 7,000 · 11.0%. Flexing the four declared assumption dials ±50%: **Assumption 1 (opening cost 4 h) is stable at both 2 h and 6 h** — the verdict does not move. **Assumption 2 (cold life = in-spec time) is the fragility.** At −50% the winner flips to B (3,708 vs 3,950). At +50% the margin reaches **22.4%, breaking the SPEC §2 20% cap.** The twist detour is stable at ±50%. The case says Assumption 2 is optimistic; neither the case nor the guide says the verdict turns on it. |
| **P6 data decay** | **PASS with finding** | All 9 distinct URLs live, no redirects, 12 of 13 recorded values re-confirmed on the page. **One mis-citation: the 334 kJ/kg latent heat of fusion in Appendix E is not on the Engineering ToolBox *thermal conductivity* page cited as S8** — the conductivity figures are, the latent heat is not. S5/S12 (UNICEF price data, updated annually) and S3 (CDC Pink Book) are the two sources built to change and should carry a refresh-by date. |

**The three FAILs share one root cause.** Cold Chain's headline numbers depend on two conventions
the case never states — how doses are allocated across facilities, and how a fleet's boxes are
assigned to stops. Three independent fresh readers each hit it and each derived a different, also
defensible, in-spec total. *Fix at `case-write`: state the allocation rule and the box-assignment
rule in Appendix F alongside the two existing assumptions, and record in `balance_test` that the
verdict is unstable under Assumption 2.*

## Tier 3 — human dry-run

**NOT RUN.** No `cases/cold-chain/runs/RUN_*.md` exists. Per MCS-29 the case is therefore **not
`VERIFIED`**, and per this ledger's own rule it may not be marked ✅ on the strength of a dry-run
that has not happened.

## What this run changes

- `case.json.qa.state` → `BLOCKED`. The case must not be re-published until the Tier 1 BLOCKER and
  the three Tier 2 failures are closed.
- The eleven ✅ marks earned by MCS-01…MCS-11 stand. They were structural, and the structure holds.
- MCS-23, MCS-24, MCS-26 and MCS-27 were **earned by failing this case** — which is the only
  evidence worth having that a new check does anything.

---

# Rewrite + re-verification — 2026-07-31 (Track A)

**Fix applied:** Order A redesigned from 3 boxes / $320 to **4 boxes ($408.84 of $420): 3 on the
truck route, 1 on the motorcycle route**, with the split stated explicitly as Appendix F
Assumption 0. This makes the box-to-facility allocation ambiguity **moot** rather than disclosed —
capacity now covers full stated demand on both legs, so there is no shortfall left for a reader to
allocate by guesswork. `cases/cold-chain/sensitivity_model.py` (case-owned, not the reference
model) ships as the formal contract: `PARAMS`, `FLEX = [opening_cost_h, in_spec_fraction]`,
`evaluate()`, `evaluate_twist()`.

**`sha256(case.md)`:** `91baf00af89c8936d7aeaba55d70ccfe3e57eff632617128112b0ce3b39de598`
**State reached:** `DRAFT` → **`TIER1_PASS`**. Tier 2 is PASS-with-disclosed-findings on four
probes, mechanically FAILS one (disclosed, not silently accepted), and one remains **DELEGATED,
not executed** — this sandbox has no outbound network. `case.json.qa.state` is therefore recorded
as `TIER1_PASS`, not `TIER2_PASS` or `PUBLISHED`: per this ledger's own rule, a probe that has not
actually run does not count as passed.

## Tier 1 — structural, re-run clean

`python3 skills/case-readiness/scripts/tier1_structural.py --case cold-chain` → exit 0

**0 BLOCKERs.** 2 GAPs, both accepted:
- **T1-09** margin 17.1% is inside the 20% cap but wide — the discussion leans toward A. Accepted:
  the case is designed so the *arithmetic* is one-sided while the *values* argument (Thread 3,
  fragility, accountability) is not — see Deep Conflict in `FACILITATOR.md`.
- **T1-15** one number ("60 seconds", a dramatic countdown in the Twist prompt) has no data home.
  It's a rhetorical device, not a figure; left untracked deliberately.

Four fixes closed on the way to clean: T1-08 (Appendix F heading matched the checker's regex after
being renamed back to plain "Modeling Assumptions"), T1-17 (`cohort_bands[]` restructured to the
checker's `{band, note}` schema), T1-05 (Challenge 2's `a.)`/`b.)` sub-lines de-bulleted to match
the locked boilerplate form), T1-14 (every guide-only derived figure — ~26 in total — now lives in
`case.json.derived.route_plan`, checkable rather than free-floating).

## Tier 2 — simulated play, re-run with fresh subagents (P1–P4) + mechanical (P5) + delegated (P6)

P1–P4 were each run against a **fresh general-purpose agent with no access to this project's
authoring history**, given only `case.md` (and, for P3/P4 stage 2, `FACILITATOR.md` after
committing to a blind answer first) — the same adversarial-verification pattern that caught the
original allocation ambiguity.

| probe | verdict | finding |
|---|---|---|
| **P1 cold solve** | **PASS** | Fresh solver chose Order A, named the metric ("total usable/in-spec doses"), and reproduced 8,200 vs 7,000 exactly, including the SA:V cross-check and the $variable dose-price spoilage value. **New finding:** the split of the 4 truck stops among the 3 truck boxes is still unstated; the solver had to invent one. It turned out immaterial (any split clears the last truck stop), but a less careful reader could waste time hunting for a "correct" split that doesn't exist. **Closed:** Appendix F Assumption 0 now states explicitly that the split doesn't matter and shows the worst-case bound (116.3h vs the 96h last stop). |
| **P2 both-sides** | **PASS** | Independent solver built genuine, competitive cases for both options and concluded this is "a real tension… not the tension the case's surface framing presents" — A's naive "reaches all six facilities" claim collapses under the excursion arithmetic, while a narrower "we save Bulera specifically" claim survives. Explicitly noted the case's own Appendix F line rewarding students who show both orders are worse than they look reads as "a deliberately built trap, not sloppy case design." No allocation-ambiguity artifact this time — the redesign held. |
| **P3 trap check** | **PASS** | Blind stage-1 answer (arithmetic trap: conflating "reached" with "usable," the physics-not-equity framing) matched the Guide's Anchor 2 trap almost word for word, independently re-derived. |
| **P4 twist integrity** | **PASS, with a disclosed dependency found** | The tie (7,000 = 7,000) is not invariant across the full Assumption-1 range the base case is stable on. It requires `opening_cost_h ≥ ~2.65h`; at the low end of the case's own certified 2–6h range (c = 2h), Bulera's twist-day arrival still clears its effective cold life by 1.3h and **the twist does nothing** — Order A keeps its full 17.1% margin. This was a real, previously undisclosed gap between what `sensitivity_model.py`'s own FLEX sweep already knew (twist margin 17.1% at c=2, 0% at c=3–6) and what `FACILITATOR.md` told a guide running the room. **Closed:** a facilitator-only note is now inline before the Twist section stating the crossover explicitly; `case.json.balance_test.stability` and `derived.route_plan` record the same numbers so it's checkable, not just narrated. |
| **P5 assumption sensitivity** | **FAIL (mechanical), disclosed** | Base 8,200 vs 7,000, 17.1%. `opening_cost_h` (Assumption 1) is stable at both ±50% (2h and 6h) for the base case. `in_spec_fraction` (Assumption 2 — "cold life = in-spec time," which Appendix F itself calls the *optimistic* direction) is **not** stable: −50% flips the base case to an exact tie (3,950 = 3,950); +50% widens the margin to 28.6%, breaking the SPEC §2 20% cap. This is a real, structural sensitivity, not a modeling bug — and Appendix F already invites exactly this stress test ("if you think that matters, model it and show what changes"). Per MCS-26, disclosure is the requirement, not elimination: **Lessons Learned** now names both directions and the exact swing, and `balance_test.stability` records the numbers. The probe stays a mechanical FAIL because it is a pure numeric check with no disclosure-aware escape valve — that is intentional; a disclosed sensitivity is still a sensitivity. |
| **P6 data decay** | **DELEGATED, not executed** | This sandbox has no outbound network. The worklist (14 URLs, S1–S13 plus S8b) is unchanged from the original P6 pass, which found all sources live and one mis-citation (already fixed: S8/S8b split). Per SPEC's "absent data is a first-class state," this is recorded as **not run**, not as a pass — someone with network access needs to execute the fetch-and-confirm step before Cold Chain can be called `TIER2_PASS`. |

**Net effect of this pass:** the case's original defect (an undisclosed allocation convention that
three independent readers resolved three different ways) is gone — replaced by a design where
there is nothing left to allocate. Two smaller, real sensitivities were found in its place (the
twist's opening-cost floor, and Assumption 2's ±50% fragility) and both are now disclosed in the
Guide Notes and tracked in `case.json`, per MCS-26's actual requirement. Nothing was hidden to make
a probe pass.

## Tier 3 — human dry-run

**Still NOT RUN.** No `cases/cold-chain/runs/RUN_*.md` exists. `tier3_verify.py --all` confirms
Cold Chain correctly reports "not claiming VERIFIED" — this remains open and requires a real guide
running a real session; it is not something this pipeline can produce on its own.

## Ledger rows updated by this run

MCS-02, MCS-15, MCS-24, MCS-26, MCS-27 — see `DOCTRINE_LEDGER.md`. All five now name this run's
sha256 and this run's actual result; none carry the pre-rewrite numbers forward.

---

# Interactive HTML shipped + locked in as doctrine — 2026-07-31

Built `published/Cold Chain - Interactive.html` on user request (single-file, inline SVG: crest,
overview banner, a to-scale circuit map, a to-scale box-size comparison, an SA:V-vs-cold-life
scatter, a live student-input bar chart, self-checking Notebook calculators wired to the case's
own numbers). The user then asked to "lock this in as the expectation" for every future case, so
it was written into doctrine rather than left a one-off: **MCS-37**, enforced by a new
`tier1_structural.py` check, **T1-18** — requires a fresh `.html` in `published/`, scans it for
`balance_test` (in-spec totals, margin, winner) printed as a static literal (BLOCKER if found),
and sweeps every number outside `<script>` tags against the case's own number universe (GAP if
orphaned).

**Re-ran Tier 1 against Cold Chain**: `TIER1_PASS`, 0 blockers, 3 GAPs (T1-09 wide-margin,
accepted; T1-15 one untracked "60 seconds" dramatic figure, accepted; T1-18 110 orphan numbers —
verified these are CSS/SVG decimals such as opacity and stroke-width, not case data; narrowing the
sweep to exclude markup noise was judged not worth the risk of someday hiding a real drift).

**Leak detector unit-tested before being trusted**: a synthetic string containing "17.1%" fired
the check; a synthetic clean string did not. Confirmed the actual shipped file contains no literal
occurrence of 8200, 7000, or 17.1 anywhere in its source.

**Honest gap this doesn't close**: the file was hand-authored, not generated. A7 in `ROADMAP.md`
tracks building a shared template/generator before case #2 exists — otherwise MCS-37 is a real
gate but an expensive one to clear by hand every time.

---

# Hover+hyperlink math glossary shipped + locked in as doctrine — 2026-08-01

On instruction to make sure the case "cover[s] the content of the math... with hover and
hyperlinks... references to the resources to explain the concepts especially the math," rebuilt
Appendix G as a JS-rendered glossary: 15 terms (Volume, Surface Area, Prism, Ratio, Unit, Percent,
Decimal, Absolute Value, Scientific Notation, Measurement, Distance, Weight, Data, Bar Graph,
Mean) each hoverable (a plain-English `<span class="tip">` definition) and clickable (a real
external lesson), plus 14 "how-to" phrase links inline in the Notebook and Appendix table headers.
Every url was fetched with `web_fetch` and confirmed by canonical-URL echo before being embedded —
all 8 distinct target pages, all on `khanacademy.org` — per MCS-21 ("no URL from memory").

Written into doctrine as **MCS-39**, enforced by a new `tier1_structural.py` check, **T1-19**:
requires at least 8 real glossary terms with a resolved url, every url `https://` to an
allowlisted educational domain (`khanacademy.org`, `mathsisfun.com`, `cuemath.com`,
`purplemath.com`, `ck12.org`, `nctm.org`, `openstax.org`). The check recognizes two legal
authoring styles — static `<a class="gterm" href="...">` anchors, or a JS `{label: {def, url}}`
data object rendered at page load (Cold Chain's actual pattern) — because the anchors themselves
don't exist as static text in the file until the browser runs the render function; a naive
static-text scan would have under-counted real coverage down to the one template literal that
builds them.

**T1-19 unit-tested against 5 synthetic cases before being trusted** against the real file: no
wiring at all (BLOCKER), only 3 real terms (BLOCKER), 9 terms with one on a non-allowlisted domain
(BLOCKER, correctly names the bad url), 9 terms with one on insecure `http://` (correctly excluded
from the count rather than false-accepted), 10 clean allowlisted terms (PASS). **Caught and fixed
a real bug in the check's own first draft**: when a JS data object and static template scaffolding
coexist, the draft was merging the unresolved template placeholder href into the same
URL-validation list as the real data-object entries — harmless here, but in principle could have
let an unrelated bad-domain anchor elsewhere on the page hide next to real glossary data. Fixed to
treat the JS data object as the sole source of truth for both the count and the URL check when one
is present.

**Ran the full Tier 1 gate afterward**: `TIER1_PASS`, 0 blockers, 3 GAPs (T1-09 wide-margin,
accepted; T1-15 one untracked figure, accepted; T1-18 111 orphan numbers, same CSS/SVG-decimal
category as before). T1-19 itself: clean PASS, no gap.

---

# Tier 2 probe 6 attempted for real — 2026-08-01

While reviewing Track A completeness, found `case.json.status` and `cases_index.json` both saying
`"published"` while `case.json.qa.state` (still `TIER1_PASS`) and its own note said the opposite —
*"Not TIER2_PASS or PUBLISHED until P6 actually runs."* Rather than guess which was right, actually
ran P6 (`skills/case-readiness/scripts/tier2_probes.py --case cold-chain --probe 6`) and then
fetched every URL on its emitted worklist — this session has live outbound network access, unlike
the sandbox every prior run of this probe was DELEGATED in.

**Worklist: 11 distinct URLs (14 worklist rows, S2≡S13 and S4≡S11 and S5≡S12 sharing a URL).**

| URL (source ids) | Result |
|---|---|
| `extranet.who.int/…/e004-cold-boxes-and-vaccine-carriers` (S2) | **CONFIRMED LIVE, figure present.** Cold-life definition quoted verbatim; 8 kg carrier / 50 kg cold box max design weight and 25 kg one-worker lift guidance both quoted verbatim. |
| same URL (S13) | **CONFIRMED LIVE, figure NOT located.** The 30-minute data-logger interval and 8-hour clinic-session limit this citation claims were not found on the fetched page content. Per the probe's own instruction ("a url that resolves but no longer carries the figure is worse, because nothing else would notice") this is flagged, not silently passed — see below. |
| `iea-ebc.org/…/EBC_Annex_39_PSR.pdf` (S7) | **CONFIRMED LIVE, figure present.** Downloaded and text-extracted (`pdfplumber`, no `pdftotext` available in this environment): "0.004 W/(m·K) after production" and "Thermal conductivity λ (25 yr) [W/(m·K)] < 0.008" both present verbatim, matching the case's "0.004 as-produced / 0.008 design value" claim. |
| `engineeringtoolbox.com/thermal-conductivity-d_429.html` (S8) | **CONFIRMED LIVE, figure present.** Polyurethane foam 0.03, Polystyrene (expanded) 0.03, Styrofoam 0.033, Ice 2.18 — all four match. (`WebFetch` returned 403 here; a plain `curl` with a browser `User-Agent` returned 200 — see note below.) |
| `engineeringtoolbox.com/latent-heat-melting-solids-d_96.html` (S8b) | **CONFIRMED LIVE, figure present.** "Water, Ice 334" matches the 334 kJ/kg claim. |
| `supply.unicef.org/s0002344.html` (S1) | **INCONCLUSIVE — blocked.** 403 Forbidden from both `WebFetch` and `curl` with a realistic browser UA. Not evidence the page is dead — UNICEF's supply catalogue actively blocks automated fetchers — but not evidence it's live either. |
| `supply.unicef.org/s0002095.html` (S9) | Same — **INCONCLUSIVE — blocked**, 403. |
| `supply.unicef.org/s0002353.html` (S10) | Same — **INCONCLUSIVE — blocked**, 403. |
| `cdc.gov/pinkbook/…/chapter-5-vaccine-storage-and-handling.html` (S3) | **INCONCLUSIVE — blocked**, 403 from both tools. |
| `unicef.org/supply/media/24526/file/Measles-vaccines-05122025.pdf` (S5/S12) | **INCONCLUSIVE — blocked**, 403 from both tools. |
| `medrxiv.org/content/10.1101/2023.11.03.23298045v1.full` (S6) | **INCONCLUSIVE — blocked**, 403 from both tools. |
| `apps.who.int/iris/bitstream/…/WHO-IVB-17.06-eng.pdf` (S4/S11) | **INCONCLUSIVE — moved.** 302-redirects to `iris.who.int/bitstream/handle/10665/255749/WHO-IVB-17.06-eng.pdf` (`WHO-IVB-17.06`'s own citation should probably be updated to this URL). `WebFetch` got 403 there; `curl` got 200 but the body is a DSpace/Angular app shell (WHO migrated IRIS to DSpace 7, and the old direct-`bitstream` path no longer serves the raw file to an unauthenticated script client) — a human opening this link in a real browser almost certainly still reaches the document through the app's UI, but neither fetch tool in this session could mechanically confirm the 2.1 cm3/dose, 3.1 cm3/dose, or "up to 100%" figures are still on it. |

**Net result: 3 of 11 distinct URLs mechanically confirmed live-and-accurate (E004, Annex 39, both
Engineering ToolBox pages), 1 flagged finding (S13's specific claim not located on an otherwise-live
page), 7 genuinely inconclusive** — six blocked by site-side bot protection this session's tools
could not get past even with a real browser `User-Agent`, one (S4/S11) blocked by a platform
migration that changed how the URL serves content to a non-browser client. **None were confirmed
dead** (no 404s), which matters — this is not the same finding as a broken link, and MCS-28 is
explicit that a link that silently stopped carrying its figure is the worse failure of the two.

**This is genuine progress over the prior DELEGATED state, and it is still not a clean `TIER2_PASS`
on P6.** The probe's own bar is a reachable/figure-present verdict for *every* URL; 7 of 11 remain
unconfirmed. `case.json.qa` updated to record this accurately rather than rounding up. The
`status: "published"` field on both `case.json` and `cases_index.json` predates this run and was
already inconsistent with `qa.state` before today — that inconsistency is **not resolved by this
run** (P6 still isn't clean, and P5 still mechanically FAILs, disclosed-not-eliminated per MCS-26)
and is flagged back to the user rather than silently corrected either direction.

**S13's finding is the one genuinely new fact this run surfaced** and is a real candidate for a
`case-readiness` re-run finding, not just a network artifact: either the 30-min/8-h figures belong
on a different, uncited page and S13's `url` field needs correcting, or they were paraphrased from
a part of the E004 page the fetch tool's summarization missed. A human should open the page
directly and check before this is called resolved either way.
