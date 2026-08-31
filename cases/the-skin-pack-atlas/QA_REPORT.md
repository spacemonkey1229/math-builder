## case-readiness run — 2026-08-31 (remediation pass)
**State:** DRAFT → QA   **Verdict:** TIER1_PASS, TIER2 CLEAN

Follows the 2026-08-31 run recorded below (superseded), which found 3 Tier 1 BLOCKERs and 6 GAPs.
All 3 BLOCKERs and 4 of 6 GAPs are fixed in this pass; the remaining 2 findings are structural GAPs
that are expected/inherent to this case (see T1-10, T1-13 below) and do not block Tier 1.

### What changed

- **[T1-06 fixed]** Added a real `(SEE APPENDIX E)` cross-reference in Background, at the sentence
  describing how Alicia reconstructs the missing revenue/device-tier breakdown ("built on top of a
  small set of disclosed modeling assumptions and proxies where Tanager's own real business data
  does not exist to source (SEE APPENDIX E)"). Appendix E is no longer an orphan.
- **[T1-08 fixed]** S7's confidence graded `MEDIUM` (was the non-standard `MEDIUM-HIGH`) in
  `case.json`, `case.md` Appendix F, and `RESEARCH_LOG.md`'s summary table. Rationale recorded in
  `case.json.sources[S7].note`: a single arXiv preprint (ISSRE track, empirical study of four
  commercial games) is real, current, peer-reviewed-track evidence, but not a first-party vendor
  spec or live official dashboard (the case's HIGH bar, met by S3/S5/S6/S8) — MEDIUM is the honest
  grade.
- **[T1-10 fixed → GAP, carve-out]** Added `case.json.reinforcement_note`, naming three adjacent
  skills (scalar matrix multiplication, Cramer's Rule, elimination/substitution) that were checked
  and honestly ruled out as not forced by this case's actual deliverables. `new_coverage: []` now
  downgrades from BLOCKER to GAP per the 2026-08-17 reinforcement carve-out doctrine, same
  evidentiary bar as `legacy_conversion_note`.
- **[T1-02 fixed]** Overview trimmed from 310 to 287 words (150–300 cap), light copy edits only, no
  numerals introduced.
- **[T1-13 fixed]** FACILITATOR.md's "Socratic questions" section rewritten so each of the 5
  questions is a single physical line ending in `?` (the checker's regex requires this; the prior
  5-question list wrapped across lines and only 1 was machine-detectable). Added an "Immediate
  recommit" section (present in the `cooling-curve` template, missing here) with a re-vote prompt
  tied to the D5 reveal. "Twist: N/A" justification GAP remains — see below, this is expected.
- **[T1-14 fixed]** Two orphan numbers in FACILITATOR.md (`~15%`, `~48%`, informal roundings of the
  exact 14.9%/51.8% figures already in `case.json`) reworded to reference the exact figures
  instead. A third apparent orphan (`15` in "15–20 min") was a false read against a stale QA hash;
  reworded to "up to 20 min" regardless, to be safe.
- **[T1-17 fixed]** Added `case.json.cohort_bands[]` (Full 12–20, Compressed 6–11, 1:1/pair 1–2),
  each with a note on what changes at that size.
- **[T1-16 fixed]** `case.json.qa.case_md_sha256` recorded against the final `case.md`.
- **[P5 addressed]** Authored `cases/the-skin-pack-atlas/sensitivity_model.py` (see below). Probe 5
  found MA1's four install/revenue dials unstable when flexed independently (see below); added
  `case.json.sensitivity_disclosure[]` entries (Category X, each with a verified justification
  citing the actual flexed margin) for `india_installs`, `nigeria_installs`, `india_revenue_usd`,
  `nigeria_revenue_usd`. This is a disclosed, not eliminated, instability — see Probe 5 below.

### Tier 1 — structural (20 checks), re-run 2026-08-31 post-fix

| id | result | note |
|---|---|---|
| T1-01 | PASS | |
| T1-02 | PASS | Overview now 287 words |
| T1-03 | PASS | |
| T1-04 | PASS | |
| T1-05 | PASS | |
| T1-06 | PASS | Appendix E now referenced from Background |
| T1-07 | PASS | (POLISH: all 7 Appendix G labels parsed from bullets) |
| T1-08 | PASS | S7 confidence normalized to MEDIUM |
| T1-09 | PASS | balance margin 14.9%, within the 20% cap |
| T1-10 | GAP | `new_coverage[]` empty, downgraded from BLOCKER via `reinforcement_note` carve-out — expected and correct for this second-pass/redundancy case (see `redundancy_note`) |
| T1-11 | PASS | |
| T1-12 | PASS | |
| T1-13 | GAP | Twist is N/A (mathematical, not narrative); justification is written out in FACILITATOR.md's Twist/trap sections — this GAP fires unconditionally whenever `Twist: N/A` appears, by design, and is not a defect |
| T1-14 | PASS | |
| T1-15 | PASS | (POLISH: no `published/` directory yet) |
| T1-16 | PASS | `case_md_sha256` recorded and current |
| T1-17 | PASS | `cohort_bands[]` declared (3 bands) |
| T1-18 | PASS | (POLISH: no `published/` directory yet) |
| T1-19 | PASS | (POLISH: no `published/` directory yet) |
| T1-20 | PASS | (POLISH: no `published/` directory yet) |

**BLOCKER (0).**

**GAP (2):** T1-10 (redundancy carve-out, expected), T1-13 (Twist N/A, expected/inherent).

**POLISH (5):** T1-07, T1-15, T1-18, T1-19, T1-20 — all "no `published/` directory yet."

**VERDICT: TIER1_PASS (0 blockers, 2 gaps, both expected/inherent to this case).**

### Tier 2 — simulated play (6 probes), run 2026-08-31

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | A fresh solver (no prior exposure to FACILITATOR.md/case.json) reading only the case packet chose B, correctly built M, computed det(M)=29,600,000, solved r=M⁻¹v=[0.80, 0.15], and reproduced 51.8% device-count / 85.1% revenue-weighted success for A — reaching the case's own answer by the case's own intended route (the matrix solve), not a shortcut. |
| P2 both-sides solve | **PASS** | Both options have a genuine, non-strawman best sentence. A's case (full detail, MA3 suggests the model overstates its real risk) is real but collapses once pressed on why it should override the case's own named decision metric, on which B wins outright. The case is a real dilemma, not a rigged one. |
| P3 trap check | **PASS** | The guide's named trap (stopping at Appendix C's raw device-count share, never opening Appendix A/D4's revenue-weighted figure) is the dominant, well-engineered trap — built into Launch, Anchor 2, the Twist, Socratic Q1, and the recommit vote. It is the trap that will actually catch a room. |
| P4 twist integrity | **PASS** | The mathematical twist (device-count % vs. revenue-weighted %) genuinely invalidates the naive "Crest fails ~half of devices, reckless" framing, even though the vote doesn't flip — that's the intended lesson. Independent re-derivation from Appendix A/B's stated numbers reproduces 51.8%/85.1% exactly; no undisclosed convention changes the numeric outcome (one minor documentation note: the model's implicit "uniform per-tier revenue rate across both markets" convention isn't named as its own assumption in Appendix E — not a BLOCKER, the numeric construction has no room for a divergent reading). |
| P5 sensitivity | **PASS (disclosed)** | See detail below. |
| P6 data decay | **PASS** | See detail below. |

**VERDICT: TIER 2 CLEAN (0 mechanical failures, 0 adjudicated failures).**

---

### Probe 5 detail — MA1/MA3 sensitivity (`sensitivity_model.py`, `--flex-all` not needed; ran default `FLEX[]`)

Base case reproduces the case of record exactly: revenue-weighted `{A: 85.13%, B: 100%}`, margin
14.9%, and device-count `{A: 51.8%, B: 100%}` — matching `case.json.balance` and
`FACILITATOR.md`'s worked arithmetic to the decimal.

**MA3 (`value_tier_overcount_frac`, the case's own most important honest finding) does NOT flip
the winner at any flex tested**, including the full disclosed limit case:

| flex | value | A | B | winner |
|---|---|---|---|---|
| −50% | 0.5 | 92.6% | 100% | B |
| +50% (ceiling, no-op) | 1.5→1.0 | 85.1% | 100% | B |
| full disclosed limit | 0.0 | 100.0% | 100% | **tie**, never a clean A win |

This confirms what `case.json.modeling_assumptions[MA3].sensitivity` already claims: MA3 makes
Option B's margin *conservative* (an overestimate of Option A's real risk), never enough to flip
the recommendation to A — even at the disclosed limit where every "Value-tier"-proxy install is
assumed to actually render the Crest Atlas, Option A only ties Option B, it never beats it.

**MA1's four install/revenue dials (`india_installs`, `nigeria_installs`, `india_revenue_usd`,
`nigeria_revenue_usd`) DO flip the winner and break the 20% cap when flexed independently** (one
dial at a time, the other three held fixed) — e.g. `india_installs` at −50% gives a nonsensical
431.0% margin favoring A, because halving one market's installs while holding that market's revenue
fixed forces an implied per-install revenue rate the case's real numbers don't support. This is a
real property of the linear system (v is stated independently of M), not a bug in the model script.
Per the disclosure-aware Probe 5 pass state (2026-08-13 doctrine), this is **disclosed, not
eliminated**: `case.json.sensitivity_disclosure[]` now carries 4 Category-X entries (good-faith
invented-business-figure estimates, not citations — Tanager/Molt are fictional), each with the
verified flex result recorded in the justification. `case.json.modeling_assumptions[MA1].sensitivity`
and case.md's Appendix E already told a Hero the install/revenue totals must move together,
device-tier-consistent — this Probe 5 run is the mechanical confirmation that the four dials really
are coupled, not four independent free parameters.

### Probe 6 detail — data decay (direct fetch, 2026-08-31, one day after the sources were logged)

All 7 directly-fetchable sources were re-fetched today and confirmed to still carry their cited
value, verbatim or effectively verbatim:

| id | reachable | cited value still present | notes |
|---|---|---|---|
| S1' | yes | yes | "MediaTek led India's smartphone chipset market with a 47% share, followed by Qualcomm with a 31% share" — exact match |
| S2' | yes | yes | Tecno 23.55%, Infinix 21.73%, Itel 5.41%, Transsion combined 50.69%, and every other named brand's percentage — exact match |
| S3 | yes | yes | Table 1-2: SGX 535 = 2048×2048, SGX 543 = 4096×4096 — exact match |
| S4 | **no** | n/a | Same TLS certificate mismatch on `infocenter.arm.com` already disclosed in `case.json`/`RESEARCH_LOG.md` at authoring time (2026-08-30) — not a new finding, not a BLOCKER: S4 is retained only as corroboration for the already-HIGH-confidence S3, which independently reports the identical 4096px cap for the same GPU generation |
| S5 | yes | yes | "supports texture resolutions from 1x1 up to 8192x8192" — exact match |
| S6 | yes | yes | "Unity only supports textures up to a size of 16384" — exact match |
| S7 | yes | yes | 21 of 91 (23%) GPU-related; Insufficient GPU = 11; verbatim hardware-vs-software quote — exact match (confirmed against the full-text HTML, not just the abstract, since the abstract alone doesn't carry the counts) |
| S8 | yes | yes | OpenGL ES 3.2 98.24% / 3.1 0.39% / 3.0 0.86% / 2.0 0.49%; Vulkan none 7.37% / 1.0.3 3.86% / 1.1 62.09% / 1.3 26.01% / 1.4 0.67%; snapshot ending Nov 24, 2025 — exact match on every figure |

**No BLOCKER.** No url 404'd, and no url that resolved had lost its cited figure. S4's
unreachability is a pre-existing, already-disclosed limitation (not sole citation for any
constraint), unchanged since the 2026-08-30 research pass.

### Tier 3 — human dry-run
NOT RUN (Tier 3 is a human-facilitated classroom run, out of scope for this pipeline pass).

---

**MA3 continuity check (manual, carried forward from the 2026-08-31 pre-fix run — still holds):**
MA3 is present and consistent across `case.json`, `FACILITATOR.md`, and `case.md`; the directional
claim (the model likely overstates Option A's failure risk) is stated plainly in `FACILITATOR.md`
and `case.json` but only ever pointed at (never with the winner/margin restated) in `case.md` —
consistent with keeping the answer out of student-facing text. No leak found.

---
---

## case-readiness run — 2026-08-31 (superseded by the remediation pass above)
**State:** DRAFT → (blocked)   **Verdict:** BLOCKED at Tier 1

Preflight lint found one advisory finding (a `<!-- FACILITATOR ONLY -->` HTML comment naming
"facilitator" in the student-facing `case.md` body, at the end of Appendix G). Fixed by removing
the stray comment; re-run confirmed clean before Tier 1 was run.

### Tier 1 — structural (20 checks)
| id | result | note |
|---|---|---|
| T1-01 | PASS | |
| T1-02 | GAP | Overview is 310 words; spec asks 150–300 |
| T1-03 | PASS | |
| T1-04 | PASS | |
| T1-05 | PASS | |
| T1-06 | **BLOCKER** | Appendix E (Modeling Assumptions) is an ORPHAN — never referenced from Background or Challenges. Verified by hand: "SEE APPENDIX E" appears only *inside* Appendices A, B, D and F (cross-referencing each other), never in the narrative text before Appendix A's heading. Challenges 3 and 5 (where MA1–MA3 are load-bearing) do not point at it. |
| T1-07 | PASS | (POLISH: all 7 Appendix G labels parsed from bullets; none needed the separator-run parser) |
| T1-08 | **BLOCKER** | Source S7 has no valid confidence grade. Confirmed: `case.json` records S7's confidence as `"MEDIUM-HIGH"`, but the checker (and the spec) only accept `HIGH`/`MEDIUM`/`LOW`. S7 is the arXiv 2504.20261 empirical-study source added in the 2026-08-30 staleness-remediation pass; `RESEARCH_LOG.md`'s own summary table shows the same non-standard grade was carried in from the research write-up. This is a one-line schema fix (round to `HIGH` or `MEDIUM`), not a sourcing problem — the citation itself checks out (see data-decay note below). |
| T1-09 | PASS | balance margin 14.9%, within the 20% cap |
| T1-10 | **BLOCKER** | SPEC §8 — `new_coverage[]` is empty; the case closes no gap. Confirmed: neither `legacy_conversion_note` nor `reinforcement_note` is present in `case.json`, so neither T1-10 carve-out applies. This case's `standards[]` (matrix/determinant/2×2-system skills) all show `new_coverage: []` — either the spine already credits these skills to another case (padding risk if so) or `new_coverage[]` was simply never populated for this genuinely-new case. Needs an author decision, not a QA fix. |
| T1-11 | PASS | |
| T1-12 | PASS | |
| T1-13 | GAP | Facilitator guide has 1 Socratic question (spec asks 5); Twist is N/A — confirm the justification for that is written out |
| T1-14 | GAP | CONTINUITY — 3 numbers in `FACILITATOR.md` (6.0, 15.0, 48.0) appear in neither `case.md` nor `case.json`; move into `case.json.derived` or confirm stale |
| T1-15 | PASS | (POLISH: no `published/` directory yet, nothing to drift) |
| T1-16 | GAP | MCS-11 — no `case_md_sha256` recorded yet (expected on first run) |
| T1-17 | GAP | MCS-25 — no `cohort_bands[]` declared |
| T1-18 | PASS | (POLISH: no `published/` directory yet) |
| T1-19 | PASS | (POLISH: no `published/` directory yet) |
| T1-20 | PASS | (POLISH: no `published/` directory yet) |

**BLOCKER (3):**
- [T1-06] SPEC §1.6 — Appendix E (Modeling Assumptions) is an ORPHAN: never referenced from Background or Challenges
- [T1-08] source S7 has no valid confidence grade
- [T1-10] SPEC §8 — new_coverage[] is empty; the case closes no gap

**GAP (6):**
- [T1-02] SPEC §1.2 — Overview is 310 words, spec says 150-300
- [T1-13] facilitator guide has 1 Socratic questions, spec asks for 5
- [T1-13] MCS-15 — Twist is N/A; confirm the justification is written out
- [T1-14] CONTINUITY — 3 number(s) in FACILITATOR.md appear in neither case.md nor case.json: [6.0, 15.0, 48.0]
- [T1-16] MCS-11 — no case_md_sha256 recorded yet (expected on a first run)
- [T1-17] MCS-25 — case.json declares no cohort_bands[]

**POLISH (5):** T1-07 (separator-run parser unused, all labels bulleted), T1-15/T1-18/T1-19/T1-20 (no `published/` directory yet — nothing to check)

### Tier 2 — simulated play (6 probes)
**NOT RUN.** Tier 1 did not clear (3 open BLOCKERs), so per the ladder ("TIER1_PASS requires Tier 1
clean: 0 BLOCKERs" before "Tier 2 may start") the six probes were not executed. All six probes are
recorded as `NOT RUN`, which is a real state, not a pass.

### Tier 3 — human dry-run
NOT RUN

---
**MA3 continuity check (manual, ahead of Tier 2):** MA3 (Mali-400 GPU discontinued 2015; Value-tier
cap is likely conservative for current budget silicon) is present and consistent across `case.json`
(`modeling_assumptions` MA3 row, `balance_test.argument_a`, `balance_test.margin_note`, S6/S8 source
notes), `FACILITATOR.md` (Anchor 4, "second layer" note, guide observation checklist, closing
recap), and `case.md` (Appendix E's MA3 row, plus directional pointers at lines 179 and 220). The
directional claim — that the model likely *overstates* Option A's failure risk — is stated plainly
in `FACILITATOR.md` and `case.json`, but in `case.md` it is only ever pointed at ("MA3 discloses
this is likely conservative for current budget silicon" / "SEE APPENDIX E, MA3, for what that means
for this model's Value-tier assumption") without restating the winner or the margin — consistent
with keeping the answer out of student-facing text. No leak found; preflight lint (post-fix) and a
manual read of both mentions agree.
