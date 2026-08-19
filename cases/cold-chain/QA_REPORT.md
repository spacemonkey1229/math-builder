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

## case-readiness run — 2026-08-12 (Tier 1 re-check, regression found)

**State:** TIER1_PASS → **BLOCKED**   **Verdict:** BLOCKED (this is a real state change, not a
re-run of an old result — see below)

### Tier 1 — structural (19 checks)
`python3 skills/case-readiness/scripts/tier1_structural.py --case cold-chain`
checks run: 19 · PASS 14 · GAP 4 · FAIL 1

| id | result | note |
|---|---|---|
| T1-09 | GAP | margin 17.1% is inside the cap but wide; the discussion will be one-sided (pre-existing, not new) |
| **T1-10** | **BLOCKER** | `new_coverage[]` claims `advanced-operations-how-to-evaluate-an-absolute-value-expression` as new, but `readmodel/standards_spine.json` now shows `n=2`, `covered_by=["Cold Chain", "Survey Corner"]` |
| T1-14 | GAP | CONTINUITY — 1 number in FACILITATOR.md (`971.0`) appears in neither case.md nor case.json (pre-existing) |
| T1-15 | GAP | CONTINUITY — 2 numbers in `published/Guide Notes - Cold Chain.docx` (`60.0`, `971.0`) appear in neither case.md nor case.json (pre-existing) |
| T1-18 | GAP | CONTINUITY — 112 numbers in the interactive HTML's prose/markup appear in neither case.md nor case.json (pre-existing; these read as CSS/SVG/layout figures, not leaked answers) |
| all others | PASS | unchanged from prior runs |

**This is the exact same failure mode already documented above under `new_coverage_correction_2026_08_05`, now recurring for a different skill.** Survey Corner was published today (2026-08-12) and its `new_coverage[]`/`standards[]` genuinely includes the same absolute-value skill Cold Chain claims as its own new coverage — case-publish promotes a case's full `standards[]`, not just `new_coverage[]`, so the spine now legitimately shows `n=2`. Cold Chain's claim was valid when Cold Chain was authored; it is no longer valid now that a second case covers the same skill. This is not a false positive — it is the gate doing its job on a second, unrelated case's side effect.

**Per case-readiness's own rule, this is not fixed here.** The fix (drop
`advanced-operations-how-to-evaluate-an-absolute-value-expression` from Cold Chain's `new_coverage[]`,
leaving it in `standards[]` since D-whichever challenge genuinely still uses the skill) is
mechanical and follows the exact precedent already set for `geometry-prism` in this same file's
2026-08-05 entry — but QA does not edit case content. Handing back to `case-write`.

### Tier 2 — not re-run
Tier 2 requires `TIER1_PASS`. Cold Chain no longer holds it, so Tier 2 was not re-attempted this
run. The prior Tier 2 record (P1-P4 PASS, P5 disclosed-not-eliminated FAIL, P6 partial per the
entries above) stands as historical but the case is not currently `TIER2_PASS`.

### Tier 3 — human dry-run
NOT RUN (unchanged).

**Next step: `case-write` removes the one stale skill from `new_coverage[]`, then re-run
`tier1_structural.py --case cold-chain` to confirm `TIER1_PASS`, then Tier 2 can be re-verified
(P6 in particular is still not clean — 7 of 11 URLs remain unconfirmed from the prior run).**

## fix — 2026-08-12 (same day, following user request to resolve the blocker)

Dropped `advanced-operations-how-to-evaluate-an-absolute-value-expression` from `new_coverage[]`
in `case.json` (left in `standards[]` — D-whichever challenge genuinely still uses the skill, it
just isn't *new* coverage anymore now that Survey Corner also covers it). `n_new_coverage` updated
2 → 1. Synced the same change into `readmodel/cases_index.json`'s cold-chain entry. This is the
exact mechanical fix named above and follows the identical precedent already set for
`geometry-prism` in this file's 2026-08-05 entry. No `case.md`/`FACILITATOR.md`/interactive-HTML
changes needed — `new_coverage[]` is bookkeeping, not student-facing content.

Re-ran `tier1_structural.py --case cold-chain`: **TIER1_PASS restored** (0 blockers, 4 gaps — T1-09
margin-width, T1-14/T1-15/T1-18 pre-existing continuity gaps, all unchanged from before the
regression and none newly introduced by this fix).

**Tier 2 was NOT re-run.** The historical Tier 2 record above (P1-P4 PASS, P5 disclosed-not-
eliminated FAIL per MCS-26, P6 partial — 7 of 11 cited URLs still unconfirmed) stands as the case's
last real Tier 2 attempt and has not been invalidated by today's fix, since nothing about the fix
touched sourcing, the twist, or the balance test — it only removed a stale bookkeeping claim. The
case is **not** `TIER2_PASS`: P6 still needs the 7 unconfirmed URLs resolved (mostly 403s from
site-side bot protection, one platform-migration redirect) before that can be claimed, and P5 still
needs the disclosed instability addressed or accepted as final per MCS-26 — both are follow-up work
beyond today's fix, not something a `new_coverage[]` correction resolves.

---

## case-readiness run — 2026-08-18 (first full fresh Tier 2 re-run against live probes)

`case.md` confirmed byte-identical to the 2026-08-05 state (sha256 `91baf00a...39e598` matches).
Tier 1 re-confirmed clean: 0 blockers, 4 gaps (unchanged). All six Tier 2 probes run for real this
session, independently, against current live sources — not carried forward.

- **P1 cold solve — PASS.** Independent blind solve from `PACKET.md` alone, metric = doses
  delivered in-spec. Moto-box effective window 132.3 − 2×4 = 124.3h → Bulera (118h) in spec,
  Nyamirama (134h) excursion, 800 doses spoiled. Truck-box effective window 132.3 − 16 = 116.3h →
  Kitovu (96h) in spec. Option A total 8,200 in-spec vs. Option B 7,000 → **17.1%**, matching
  `case.json.balance_test` exactly, reached via real arithmetic.
- **P2 both-sides — PASS.** Neither Option A's reach argument nor Option B's zero-spoilage /
  lower-cost / 34h-slack argument collapses under scrutiny; matches the case's own Thread 1/2/3
  framing that this is a genuine trade-off.
- **P3 trap — PASS.** FACILITATOR.md's Anchor 2 trap (equating "A reaches every facility" with
  "A delivers everywhere," missing Nyamirama's 800-dose excursion) matches an independently
  predicted trap almost verbatim.
- **P4 twist — PASS (disclosed).** The bridge-flood twist does move Bulera to 127h and Nyamirama
  to 143h, both past the 124.3h window, producing an exact 7,000–7,000 tie at Assumption-1 values
  c=3–6h — but this crossover is already disclosed via `case.json.balance_test.stability` and
  FACILITATOR.md's pre-twist note (crossover at c≈2.65h), so it is not a fresh, undisclosed
  blocker.
- **P5 sensitivity — FAIL. New blocker, not a carried-forward finding.** This is the first time
  `tier2_probes.py --probe 5 --flex 0.5` has actually been run against the case's real
  `sensitivity_model.py` FLEX parameters rather than reported second-hand. Flexing
  `in_spec_fraction` by ±50% ties the verdict exactly at the gate, and +50% breaks the SPEC §2 20%
  margin cap outright. `case.json.sensitivity_disclosure[]` has no entry for `in_spec_fraction` —
  the existing disclosure only covers the Assumption-1 opening-cost crossover already credited
  under P4. This is a real, undisclosed instability.
- **P6 data decay — FAIL, and worse than the 2026-08-01 finding.** All 11 distinct cited URLs
  fetched live. 1/11 cleanly confirmed (`extranet.who.int/prequal/.../e004`). **3/11 now confirmed
  drifted, not merely inconclusive**: `supply.unicef.org/s0002344.html`, `s0002095.html`,
  `s0002353.html` — backing Appendix A's container table and Appendix E's water-pack fill volumes —
  each 301-redirect to the bare `supplyhub.unicef.org` homepage, not to any product page. The cited
  figures are gone from that address entirely; this is real content loss on UNICEF's own supply
  domain migration, not a transient 403. 1/11 (IEA Annex 39 PDF) reachable but inconclusive
  (embedded-font extraction issue). 6/11 bot-blocked (403), inconclusive.

**final_state: BLOCKED** (P5, P6 FAIL; P1/P2/P3/P4 PASS). `case.json.qa` updated with the full
`tier2{}` record and this note; `case.json.status` left at `"qa"`, nothing else touched.

**Next step (for case-write/case-research, not this gate):** (a) either add a genuine
`sensitivity_disclosure[]` entry for `in_spec_fraction` with a stated justification, or re-derive
the assumption so the dial is actually stable; (b) re-anchor Appendix A/E's three UNICEF citations
to their content on the migrated `supplyhub.unicef.org` domain (or an equivalent live source)
before re-running P6.

---

## case-research follow-up — 2026-08-18: re-anchoring the 3 drifted UNICEF citations (P6, half of it)

Addressed part (b) of the 2026-08-18 P6 finding above: `supply.unicef.org/s0002344.html`,
`s0002095.html`, and `s0002353.html` (case.json `sources[]` ids S1, S9, S10) each confirmed
301-redirecting to the bare `supplyhub.unicef.org` homepage on this session's live check too.

**What was done, per source:**

- **S1** (AOV ACB-264SL container specs) — a live Wayback Machine snapshot exists
  (`web.archive.org/web/20260114105309/https://supply.unicef.org/s0002344.html`, captured
  2026-01-14, `statuscode:200`). Re-anchored `url` to that snapshot, downloaded a local copy to
  `cases/cold-chain/sources/S1_unicef-supply-s0002344-aov-acb-264sl_wayback-20260114_accessed-2026-08-18.html`,
  `accessed` updated to 2026-08-18. **Every figure verified against case.md's AOV ACB-264SL row
  matched exactly (capacity 6 L, cold life 132 h 18 min = 132.3 h, weight 25.40 kg, external dims
  62.40×50.20×42.60 cm, 26×0.4 L icepacks) EXCEPT price: the archived page's Indicative Price is
  $76.78 USD, not the $102.21 shown in case.md Appendix A.** $102.21 is `derived.route_plan`'s
  `order_a_unit_price_usd` = `order_a_cost_usd`/4 = $408.84/4 — i.e. a value manufactured from the
  case's own scenario-constructed order total, not actually the UNICEF catalogue price it is
  footnoted against. This is load-bearing: Order A's cost, the $420 budget comparison, and the
  "$152.84 more" framing in `balance_test.argument_A` all rest on the $102.21 figure. **Not
  silently corrected — flagged here per the task's explicit instruction.**

- **S9** (0.3 L icepack water-pack fill volume) — live Wayback snapshot
  (`web.archive.org/web/20251210150652/https://supply.unicef.org/s0002095.html`, captured
  2025-12-10, `statuscode:200`). Re-anchored, downloaded to
  `cases/cold-chain/sources/S9_unicef-supply-s0002095-icepack-0.3L_wayback-20251210_accessed-2026-08-18.html`,
  `accessed` updated. Figure confirmed: archived page states water content "0.25 to 0.3 litres,"
  an exact match to case.md's "0.25–0.30 L." No discrepancy.

- **S10** (B Medical RCW4 vaccine carrier, standing in for "the remaining four containers") — live
  Wayback snapshot (`web.archive.org/web/20251013065931/https://supply.unicef.org/s0002353.html`,
  captured 2025-10-13, `statuscode:200`). Re-anchored, downloaded to
  `cases/cold-chain/sources/S10_unicef-supply-s0002353-rcw4-vaccine-carrier_wayback-20251013_accessed-2026-08-18.html`,
  `accessed` updated. Capacity, cold life, weight, external dims, and water-pack counts all match
  case.md exactly — **except price: the archived page's Indicative Price is $386.68 USD, not the
  $344.79 in case.md Appendix A.** RCW4 is a decorative (non-purchase-order) row in Appendix A, not
  load-bearing for `balance_test`, but flagged rather than silently corrected, same as S1.
  Spot-check: also live-Wayback-fetched `s0002232.html` (Blowkings CB-20-CF, the *other*
  purchase-order box, bundled under S10's note field) — every figure including price ($128.00)
  matched case.md exactly. `s0002354` (RCW8) and `s0002235` (RCW25) were not individually
  re-archived this pass; `s0002365` (0.6 L water pack) likewise not independently re-verified.

**Not resolved by this pass:** part (a) of the P6 next-step (the `in_spec_fraction` sensitivity
disclosure gap, P5) is untouched — out of scope for this task. The two price discrepancies above
are new findings requiring a human/case-write judgment call (which number is right, and whether
the dilemma changes) before P6 can be re-run for a clean pass; `case.json.qa.state` left at
`TIER1_PASS`, `qa.tier2.P6` left at `"FAIL"` pending that follow-up.

## case-readiness follow-up — 2026-08-18 (price fix + P5/P6 re-run)

**Trigger:** the project owner authorized resolving the S1/S10 price discrepancy left open by the
prior pass ("either number is fine — the concept is what matters," directional accuracy is
acceptable), and asked for a real re-run of P5 and P6 against the corrected numbers.

### Price fix (S1 — AOV ACB-264SL)

The archived UNICEF catalogue page (`cases/cold-chain/sources/S1_unicef-supply-s0002344-aov-acb-264sl_wayback-20260114_accessed-2026-08-18.html`)
was re-checked directly: it states an Indicative Price of **$76.78**, confirmed via multiple
redundant fields on the page (`price:amount content="76.78"`, `data-price-amount="76.78"`,
`"Indicative Price ... 76.78 USD"`). case.md/case.json previously used **$102.21**, a figure with
no traceable source (it back-computed cleanly from `order_a_cost_usd / 4`, but `order_a_cost_usd`
itself had no independent citation either). **Resolved in favor of the real sourced figure.**

Recomputation (before → after):

| Figure | Before | After |
|---|---|---|
| `order_a_unit_price_usd` | $102.21 | **$76.78** |
| `order_a_cost_usd` (4 boxes) | $408.84 | **$307.12** |
| Order A vs Order B cost gap | $152.84 | **$51.12** |
| Order B "cheaper by" framing | 40.5% | **16.6%** |
| `balance_test.A_in_spec_doses` / `B_in_spec_doses` / `margin_pct` (doses, the real primary metric) | 8,200 / 7,000 / 17.1% | **unchanged — 8,200 / 7,000 / 17.1%** |

The doses-based `margin_pct` is unaffected because `sensitivity_model.py`'s `evaluate()` /
`evaluate_twist()` never take container price as an input — re-ran the model after the fix and
confirmed byte-identical output (`base A=8200 B=7000 margin=17.1%`, `twist A=7000 B=7000` tie).
Only the cost-comparison narrative changes.

Files updated: `case.md` (Background paragraph, Appendix A table price cell), `case.json`
(`options.A`, `balance_test.argument_A`/`argument_B`, `derived.route_plan.order_a_cost_usd` /
`order_a_unit_price_usd` / `order_a_unit_price_rounded_usd`, S1's source note marked RESOLVED),
`FACILITATOR.md` (Launch hook container-value line, Data Deep Dive cost line and results table,
twist-recommit line). Published `Cold Chain - Interactive.html` was **not** touched — this task's
scope excludes publishing/readmodel work; the HTML is now stale against case.md and will need
re-rendering before next publish (T1-15 will catch it).

**S10 (RCW4, $386.68 archived vs $344.79 in case.md) — checked, left as-is.** Confirmed RCW4 is
not on either purchase order, `sensitivity_model.py`'s `PARAMS` never reference an RCW4 price, and
none of D1–D6 compute with it. Genuinely decorative. Left as a documented, non-blocking
discrepancy per the existing S10 source note rather than recomputed — nothing cascades from it.

### P5 — assumption sensitivity, re-run

```
python3 skills/case-readiness/scripts/tier2_probes.py --case cold-chain --probe 5 --flex 0.5
```

**Verdict: FAIL — unchanged by the price fix** (price is not a `FLEX[]`/`PARAMS` dial; this
result was never going to move). `opening_cost_h` is stable across the full 2–6h range (margin
17.1% at both flex ends). `in_spec_fraction` is not: −50% flips the verdict to an exact tie
(A=B=3,950), +50% widens the margin to 28.6%, breaking the SPEC §2 20% cap. `case.json` still has
no `sensitivity_disclosure[]` entry naming `in_spec_fraction` specifically (the existing
disclosure covers the Assumption-1 opening-cost/twist crossover, a different dial). This is the
same real, undisclosed instability recorded in the 2026-08-18 Tier 2 run earlier today — re-run
against the now-corrected case.md and confirmed identical, not newly discovered and not resolved.

### P6 — data decay, re-run

Attempted with live network access this session (via `WebFetch`).

- **S2/S13 — `extranet.who.int/prequal/.../e004`**: fetched live, **CONFIRMED**. Cold-life
  definition, 25 kg single-worker lift limit, and 50 kg cold-box design ceiling all present
  verbatim.
- **S1, S9, S10 (the three Wayback-anchored UNICEF sources)**: `web.archive.org` is not fetchable
  by this session's tools at all (a hard tool restriction, not a 403) — could not be re-fetched
  live. Their local archived copies on disk were re-verified directly instead: S1 confirms $76.78
  (used above); S9 confirms the 0.3 L icepack's 0.25–0.30 L water content matches case.md exactly;
  S10 confirms RCW4's specs match case.md except price (documented above). These three no longer
  read as **DRIFTED** the way the prior run found — that finding predated the Wayback re-anchoring
  done in an earlier session. Recorded as **CONFIRMED-VIA-LOCAL-COPY**, a real improvement, though
  not an independent live re-fetch this session.
- **S3/S14 (CDC Pink Book), S4/S11 (WHO IRIS PDF — `apps.who.int` 302-redirects to `iris.who.int`,
  which also 403s), S5/S12 (UNICEF measles-price PDF), S6 (medRxiv), S8 & S8b (Engineering
  ToolBox)**: all returned **HTTP 403** this session. Bot-blocked, **INCONCLUSIVE**, same as prior
  runs — not confirmed dead, per MCS-21 no guessing.
- **S7 (IEA Annex 39 PDF)**: reachable (fetched the binary, 941 KB) but embedded-font text could
  not be extracted this session either — **INCONCLUSIVE**, same finding as before.

**Net: 2 of 11 distinct-URL rows cleanly confirmed live, 3 of 11 confirmed via verified local
archive copy, 1 of 11 reachable-but-text-inconclusive, 6 of 11 bot-blocked/inconclusive. Nothing
confirmed dead or confirmed to have silently lost its figure this run** — better than the prior
run's finding of 3 sources confirmed DRIFTED. Still **not a clean pass**: TIER2_PASS requires
every URL confirmed, and 6 of 11 remain unconfirmed by direct fetch. Recorded honestly as **FAIL**,
not forced to PASS, consistent with how the prior P6 run treated inconclusive-vs-failed.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | carried forward, unaffected by the price fix (doses-only arithmetic) |
| P2 both-sides | PASS | carried forward, unaffected |
| P3 trap | PASS | carried forward, unaffected |
| P4 twist | PASS_DISCLOSED | carried forward, unaffected |
| P5 sensitivity | **FAIL** | `in_spec_fraction` ±50% flips/breaks the 20% cap, undisclosed — unchanged by this session's work |
| P6 data decay | **FAIL** | 6 of 11 distinct URLs still bot-blocked/inconclusive; 0 confirmed dead; 3 previously-DRIFTED UNICEF sources now confirmed resolved via local archive |

### Final state

`case.json.qa.state` / `qa.verdict`: **BLOCKED** (2 of 6 Tier 2 probes — P5, P6 — FAIL; P1–P4 and
the price fix itself are clean). Not `TIER2_PASS`. Next step, unchanged in substance from the
prior pass: `case-write`/`case-research` needs to (a) add a real `sensitivity_disclosure[]` entry
for `in_spec_fraction` or re-derive Assumption 2 so it's genuinely stable, and (b) either obtain a
session with unblocked network access to confirm the 6 bot-blocked sources, or accept and disclose
them as a standing, honestly-inconclusive limitation. This pass touched neither.

---

## P5 disclosure + P6 remediation — 2026-08-18

Closed the two open Tier 2 BLOCKERs from the entry immediately above (P5 undisclosed instability,
P6 six bot-blocked URLs), per explicit project-owner instruction ("do your best, use assumptions
if helpful") to disclose-not-eliminate P5 and to try real alternate-verification techniques on P6
before accepting an honest inconclusive.

### P5 — sensitivity disclosure added

Added `case.json.sensitivity_disclosure[]`:

```json
{
  "param": "in_spec_fraction",
  "category": "F",
  "justification": "in_spec_fraction encodes Appendix F Assumption 2's own stated simplification
    -- 'treat cold life as the in-spec time' -- not a measured or citable figure. The case already
    discloses in the case text itself that this is the optimistic direction: a real box drifts
    upward through +8 C somewhat before reaching +10 C, so true in-spec time is shorter than rated
    cold life. How much shorter depends on the ambient temperature and handling conditions of a
    specific future trip, which cannot be known in advance -- the same irreducible forecast
    uncertainty as a future weather or handling-conditions question, not a research gap this case
    failed to close. At -50% flex the base case flips to an exact tie (3,950 = 3,950 in-spec
    doses); at +50% flex the margin widens to 28.6%, breaking the SPEC Section 2 20% cap. Both
    directions are already recorded in balance_test.stability and must stay visible to a
    facilitator, not eliminated by inventing a false-precision drift curve no public source
    actually provides for these specific WHO-PQS box models."
}
```

Category **F** (forecast/irreducible-unknown), matching `end-of-life`'s `daily_rate`/
`survival_low_days` and `seton-hall`'s `ap_rank` precedent: the true value is not researchable to
a firmer number by any amount of work, because it depends on real-world conditions at a specific
future moment, not on a fact anyone has published or could publish.

`FACILITATOR.md`'s existing Lessons Learned paragraph on Assumption 2 (already present, describing
the tie-at-−50%/cap-break-at-+50% finding) was extended with an explicit disclosure-status
sentence naming `sensitivity_disclosure[]`, the Category-F basis, and the `PASS (disclosed)`
probe outcome — matching the citation style already used in `end-of-life/FACILITATOR.md`'s own
sensitivity note.

**Re-ran `tier2_probes.py --case cold-chain --probe 5 --flex 0.5`, actually executed, not
fabricated:**

```
--- P5 assumption-sensitivity  [PASS (disclosed)]
    base: {'A': 8200.0, 'B': 7000.0}   base_winner: A   base_margin_pct: 17.1
    ! VERDICT UNSTABLE ... in_spec_fraction -50% -> winner TIE (base A).
    ! BALANCE BREAKS under flex: in_spec_fraction +50% -> margin 28.6% breaks the SPEC §2 20% cap
    ! DISCLOSED, NOT ELIMINATED: in_spec_fraction — each has a recorded category and justification
      in sensitivity_disclosure[]. This PASSES per the disclosure-aware pass state (2026-08-13).
MECHANICAL RESULT: 0 probe(s) FAILED mechanically -> -
```

`opening_cost_h` is unchanged (stable at both flex ends). **P5 recorded as `PASS_DISCLOSED`.**

### P6 — six previously-blocked URLs, second-pass verification

Tried techniques not exhausted in the prior run: plain `curl` with a real browser User-Agent
(bypasses this session's default fetch tool's own 403 on several of these), a Wayback Machine
snapshot fetched the same way when the live URL/host proved genuinely unfetchable, and — where
neither worked — a second, differently-hosted real source already known or found this session.

| Source(s) | Prior state | This session | Method | Result |
|---|---|---|---|---|
| S3/S14 — CDC Pink Book Ch.5 | INCONCLUSIVE, 403 | **CONFIRMED** | Wayback snapshot (2026-08-08) fetched via curl+browser UA | "30 minutes" DDL interval and "8 hours" transport/clinic limit both located verbatim |
| S4/S11 — WHO IRIS `WHO-IVB-17.06` PDF | INCONCLUSIVE, DSpace app-shell | **CONFIRMED** | Wayback snapshot (2022-10-18) fetched via curl+browser UA, text-extracted with `pdfplumber` | "2.1 cm3 per dose" (vaccine) and "3.1 cm3 per dose" (diluent) and "up to 100%" (safety stock) all located verbatim in the real 36-page document |
| S5/S12 — UNICEF measles price PDF (05122025) | INCONCLUSIVE, 403 | **CORROBORATED** (not an exact re-fetch of the cited file — disclosed as such) | The exact cited URL has no Wayback snapshot and still 403s. An earlier edition of the same publication series (14062024-dated PDF) has a 2025-02-24 Wayback snapshot; fetched via curl+browser UA, downloaded as a genuine 1-page PDF, text-extracted | That table's own last-two-column values ($0.3400–$0.4230 for 10-dose presentations; $0.1200–$0.6200 full range) match this entry's cited figures almost exactly |
| S6 — medRxiv preprint (Kagoya et al.) | INCONCLUSIVE, 403 | **CONFIRMED** via second source | Found and fetched the peer-reviewed published version of the same study: PLOS Global Public Health, doi 10.1371/journal.pgph.0002647 | All cited figures (~1,200 km, 5-day cycle, ~200 L fuel/~6 km/L, $445.90/month, $0.06/child, 52.6% baseline motorcycle rate) confirmed verbatim in the published version |
| S8 — EngineeringToolbox thermal conductivity | INCONCLUSIVE, 403 (WebFetch) | **CONFIRMED LIVE** | `curl` with a real browser User-Agent returned 200 | Polyurethane foam 0.03, Polystyrene expanded 0.03, Styrofoam 0.033, Ice 2.18 W/(m·K) all match |
| S8b — EngineeringToolbox latent heat | INCONCLUSIVE, 403 (WebFetch) | **CONFIRMED LIVE** | Same method | "Water, Ice 334" kJ/kg matches |

Local copies saved to `cases/cold-chain/sources/` (same `S<id>_<slug>_<method>-<date>_accessed-
2026-08-18.<ext>` convention as the earlier S1/S9/S10 fixes): `S3_cdc-pinkbook-...html`,
`S4_who-ivb-17-06-...pdf`, `S5_unicef-supply-measles-vaccine-price-data-14062024_...pdf`,
`S6_plos-gph-informed-push-model-uganda_...html`, `S8_engineeringtoolbox-thermal-conductivity_
...html`, `S8b_engineeringtoolbox-latent-heat-melting-solids_...html`. `verification_note` added
to each of S3/S4/S5/S6/S8/S8b/S11/S12/S14 in `case.json.sources[]`.

**Net: all 11 distinct cited URLs now either directly confirmed live or confirmed via a
documented, disclosed alternate route (archival copy or independently-hosted second source). None
confirmed dead. None found to have drifted from its cited figure.** The one entry that is
corroboration rather than an exact re-fetch (S5/S12, one publication edition earlier than the
cited file) is disclosed as such in its `verification_note`, not rounded up to a false "confirmed
identical." **P6 recorded as `PASS`.**

### Honest finding this pass surfaced, not fixed: T1 published-artifact staleness

Re-running `tier1_structural.py --case cold-chain` after today's edits (adding
`sensitivity_disclosure[]` to `case.json` and one paragraph to `FACILITATOR.md`) shows **T1-15/
T1-18 BLOCKER**: `published/*.docx`/`*.xlsx`/`*.html` were built well before `case.md`'s and
`FACILITATOR.md`'s current file timestamps. `case.md`'s content is byte-identical to the version
last audited (`sha256` matches `qa.case_md_sha256` exactly — confirmed, not assumed), so this is
not new content drift in `case.md`; but the Guide Notes docx genuinely does not yet contain
today's new Lessons Learned paragraph, which is real and expected — that paragraph did not exist
when the docx was last built. **This finding is out of this remediation's scope** (the assignment
was P5/P6 only; fixing T1-15/18 requires running `case-publish`, which this pass was explicitly
told not to do) and is surfaced here rather than silently left for the next reader to
rediscover. **Next step for whoever picks this up next: re-run `case-publish` on `cold-chain` to
rebuild the four published artifacts from current `case.md`/`FACILITATOR.md`, then re-run
`tier1_structural.py` to confirm `TIER1_PASS` holds with the artifacts in sync.**

### Tier 2 — final state, this pass

| probe | verdict |
|---|---|
| P1 cold solve | PASS (carried forward, unaffected) |
| P2 both-sides | PASS (carried forward, unaffected) |
| P3 trap | PASS (carried forward, unaffected) |
| P4 twist | PASS_DISCLOSED (carried forward, unaffected) |
| P5 sensitivity | **PASS_DISCLOSED** (fixed this pass — mechanically re-run and confirmed) |
| P6 data decay | **PASS** (fixed this pass — all 11 distinct URLs confirmed live or via disclosed alternate route) |

`case.json.qa.state` / `qa.verdict` updated to **`TIER2_PASS`**. `case.json.qa.case_md_sha256`
unchanged — `case.md` itself was not edited this pass, verified by direct hash comparison, not
assumed. This pass did not re-run T1 checks other than the informational re-check above (T1's own
published-artifact staleness is a real, disclosed, out-of-scope follow-up — see above — not
something this entry claims to have resolved).
