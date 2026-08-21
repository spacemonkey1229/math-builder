# QA Report — Heist

## case-readiness run — 2026-08-20

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Preflight lint

1 advisory finding: the literal `<!-- FACILITATOR ONLY: ... -->` marker line matches the
twist/trap/facilitator word-scan because the marker text itself contains the word "FACILITATOR" —
this is a known, pre-existing false positive (confirmed identical on `cases/family-trip/case.md`,
a published `TIER2_PASS` case, same marker sentence). Non-blocking, advisory only, no case.md
change made for it.

### Tier 1 — structural (19 checks)

Two fix passes were needed before a clean run; both are recorded here rather than silently folded
into the final state.

**Pass 1** (initial run): 2 BLOCKERs — T1-08 (case.json declared `modeling_assumptions[]` but
case.md had no heading matching the mechanical `Appendix <letter> — Modeling Assumptions` pattern;
Appendix C was titled "Four's Getaway Risk Model" instead) and T1-16 (stale hash, expected after
authoring). Fixed: renamed Appendix C's heading to `Appendix C — Modeling Assumptions` (kept "Four's
Getaway Risk Model" as an intro line inside it) and re-synced the hash. Also fixed 4 GAPs in the
same pass: Background referenced the final standards appendix as "APPENDIX D" instead of the
correct "APPENDIX E" (typo); FACILITATOR.md's Five Socratic Questions were multi-line, so the
mechanical `^\d+[.)]\s.*\?$` parser found 0 of them — reformatted to one line per question;
FACILITATOR.md cited two derived percentages (75.82%, 76.43%) that weren't checkable against
case.json — added `derived.route_survival_probability_pct` and
`derived.twist_route_survival_probability_pct`.

**Pass 2** (after Appendix C rename): 1 new BLOCKER — T1-06, Appendix D (Sources) was now an
orphan (never referenced by letter). Fixed: added an Appendix D cross-reference to Background.

**Final run:**

| id | result | note |
|---|---|---|
| T1-01 | PASS | all seven structural sections present |
| T1-02 | PASS | Overview 213 words, zero load-bearing numerals |
| T1-03 | PASS | binary Dilemma, opens "You are 'Four.'" |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | all 5 appendices referenced, no orphans |
| T1-07 | PASS | final appendix lines verbatim spine labels (POLISH: 54 labels parsed — `Distance` is claimed by both `number-sense-distance` and `measurement-distance` and is printed once, the documented duplicate-label hazard) |
| T1-08 | PASS | every number cited (S1-S4) or declared a Modeling Assumption (MA1-MA4); 0 `{{NEEDS_SOURCE}}` remaining |
| T1-09 | PASS | balance test: both arguments written, margin 4.26% ≤ 20% |
| T1-10 | GAP | `new_coverage[]` empty — legacy-conversion carve-out applies (`legacy_conversion_note` present, 55/66 originally-tagged skills genuinely forced, none padded) |
| T1-11 | PASS | learning-goal mutual reachability — 0 unmapped deliverables, 0 unreachable skills |
| T1-12 | PASS | T3 tier matches numeric load (compound/conditional probability, 3+ variables: exit choice, road-type mix, time-in-vehicle, station proximity; deliberately-unused speeding-formula appendix data) |
| T1-13 | PASS | FACILITATOR.md: 11-anchor ladder complete and correctly ordered, Twist present, 5 Socratic questions, timed 45-min plan with the twist moment named |
| T1-14 | PASS | FACILITATOR.md numbers cross-check against case.json.derived |
| T1-15 | PASS (POLISH: no `published/` dir yet — nothing to check) | |
| T1-16 | PASS | hash current |
| T1-17 | PASS | 3 cohort bands declared, each with a note |
| T1-18 | PASS (POLISH: no `published/` dir yet) | interactive HTML intentionally not built — see "Scope decision" below |
| T1-19 | PASS (POLISH: no `published/` dir yet) | glossary intentionally not built — see "Scope decision" below |

**BLOCKER (0) · GAP (1, carve-out) · POLISH (4)**

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent, packet only (`/tmp/coldsolve-heist/PACKET.md`), no access to FACILITATOR.md/case.json. Chose B, reproduced the correct compound-probability method (survival-factor multiplication, not summation), arithmetic matched `sensitivity_model.py` to within rounding (71.85%/74.90% vs. this case's 71.85%/74.91%), named the metric ("final combined probability of a clean getaway"), correctly answered D1-D5, correctly ruled out the police-proximity penalty (D4) and the optional speeding formula. |
| P2 both-sides solve | **PASS** | Worked directly. A's best sentence: Option A leaves 13 of 30 seconds unused (43% slack) against Option B's 1 second (3%) — a real, quantitative margin-for-error argument, not a concession. B's best sentence: B's compound probability (74.91%) beats A's (71.85%) by a real 3.06-point gap on the case's own graded primary metric, after accounting for the full drive, not just the building exit. Neither side collapses under pressure — A's defense doesn't depend on disputing the primary metric, and B's defense doesn't depend on ignoring the 30-second-window risk; both are independently defensible with the case's own numbers, consistent with a 4.26% margin that is a real result, not a paper one. |
| P3 trap check | **PASS** (after 1 fix) | Fresh subagent (packet-only, then FACILITATOR.md) named a genuine, more dangerous trap than FACILITATOR.md's original draft: summing Appendix C's flat risk percentages instead of multiplying survival probabilities — an error that produces a plausible-looking wrong number (additive ≈ multiplicative for small percentages) rather than just costing time. This did not match the guide's original single trap (a structural "the routes are shared" observation, which the subagent judged catches inefficiency, not a wrong answer). **Fixed:** rewrote FACILITATOR.md's Data Deep Dive to name the additive-vs-multiplicative error as the primary trap and the shared-route observation as a secondary one. Re-verified the mechanical pre-screen (`tier2_probes.py`) now reads `[READY]` against the corrected text (an intermediate run also caught and fixed a false READY→FAIL flip caused by an earlier, unrelated use of the word "trap" in Anchor 4's facilitator note). |
| P4 twist integrity | **PASS** (after 1 fix) | Worked directly, cross-checked via `sensitivity_model.py evaluate()`/`evaluate_twist()`. (1) The twist invalidates the belief that time spent driving after the building exit carries no further risk — both options get strictly worse (A: 71.85%→71.27%, B: 74.91%→74.30%). (2) Re-derived under every stated-assumption reading: **caught a real defect** — Appendix C's MA5, reused verbatim from the original 2021 source, said the per-minute risk applied to "the original vehicle," which directly conflicts with the Twist (the crew steals a *different*, non-original car) under a literal student reading — the same class of bug as Cold Chain's documented Assumption-1 twist failure. **Fixed:** reworded MA5 in case.md to "the getaway vehicle" with an explicit note that the rate is about time-on-road generally, not tied to any one specific car — holds under every reading now, doesn't depend on an unstated convention. |
| P5 assumption sensitivity | **PASS** | Fully machine (`tier2_probes.py --probe 5`). Swept all 8 `FLEX[]` dials at ±50%: **0 of 16 flexes change the winner**, and the margin is unmoved at 4.26% in every case (never approaches the 20% cap). This is a genuine structural property, not a coincidence: Option A and Option B share the identical getaway route and risk factors, so every `FLEX[]` dial multiplies both options' final percentage by the same factor and cancels out of the ratio — disclosed explicitly in `case.json.sensitivity_note` and `FACILITATOR.md`, not left for a guide to discover live. The only parameters that can move the margin are `exit_a_success_pct`/`exit_b_success_pct` — the case's given, locked dilemma numbers, deliberately excluded from `FLEX[]` since they are not modeling assumptions. |
| P6 data decay | **PASS** | All 4 sources checked. S1 (downtownboise.org/go/zions-bank) — live-fetched, address confirmed verbatim ("800 W Main St, Boise, ID 83702"). S2 (actonacademy.org/campuses/heroes-academy) — live-fetched, address confirmed verbatim ("5771 N Discovery Way, Boise, Idaho"). S3/S4 (Google Maps live directions) — not fetchable via the generic tool (JS-rendered), but both were live-fetched via the interactive browser tool the same day this report was written (2026-08-20) and their figures (8.9 mi/21 min; 6.3 mi via I-184 W) are exactly what's recorded in `sources[]`. 0 dead links, 0 drifted figures, all 4 sources dated today — none over the 365-day staleness threshold. |

**6/6 probes recorded, 0 FAIL. TIER2_PASS.**

### Scope decision: interactive HTML / glossary (T1-18/T1-19) not built

Both checks auto-downgrade to POLISH ("no `published/` directory yet") and this case has no
`published/` directory, matching the existing precedent of `cases/roofline-call` (also
`TIER2_PASS`, no `published/` dir). Per the task brief, `case-publish` is explicitly out of scope
for this run — building the packaged `published/` artifacts (interactive HTML, math glossary,
docx/xlsx) is `case-publish`'s job, not `case-readiness`'s or this conversion's. This is a scope
decision, not a defect: T1-18/T1-19 are satisfied as POLISH, not skipped as BLOCKERs.

### Tier 3 — human dry-run

NOT RUN. `PUBLISHED` (and therefore Tier 3) is out of scope for this conversion per the task brief
— this run stops at `TIER2_PASS` as instructed.
