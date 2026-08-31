# QA Report — the-clampband-margin

## case-readiness run — 2026-08-31 (remediation pass)

**State:** DRAFT → **TIER1_PASS**   **Verdict:** BLOCKERS FIXED, TIER1_PASS, TIER2 MECHANICALLY CLEAN

This run picks up from the prior QA_REPORT (2026-08-31, BLOCKED at Tier 1 with 4 open
BLOCKERs). Preflight lint was already clean coming into this pass (the Appendix F retune-note
leak fix from the prior run is verified still intact — re-checked directly, see below). This pass
fixes all 4 Tier 1 BLOCKERs, reaches `TIER1_PASS`, runs Tier 2, and — the specific focus of this
pass — authors `sensitivity_model.py` and mechanically verifies whether the case's retuned 9.6%
margin survives a ±50% swing on the ×1.5 correction factor and on the underlying ISO
2768/Protolabs tolerance values.

### Preflight lint — re-verified

```
PREFLIGHT LINT -- cases/the-clampband-margin
  clean -- no advisory findings.
```

Also directly re-checked: Appendix F's retune note (case.md) still states only *why* Option B was
remodeled (the real, cited ×1.5 Bender/Motorola correction, S6) and does **not** restate either
margin number (39.9% pre-retune, 9.6% post-retune) — the prior leak fix is intact.

### Tier 1 — structural (20 checks): BLOCKERS fixed

| id | before | after | fix |
|---|---|---|---|
| T1-06 | FAIL — Appendix E orphan | PASS | Added a genuine cross-reference in Background: "...requires stating a handful of scenario modeling choices, disclosed in full ... in Appendix E (SEE APPENDIX E)." |
| T1-08 | FAIL — S2 confidence `"MEDIUM-HIGH"` invalid | PASS | Re-checked S2 (Lazansky/Sierra Nevada Corp, ESMATS 2012) directly: ESMATS/Aerospace Mechanisms Symposium is a real, committee-reviewed, NASA/ESA/CSA-adjacent proceedings series, and Lazansky is a named engineer at a real aerospace prime — that supports HIGH. Graded **MEDIUM** instead (not HIGH) because one of the two numeric values this case relies on, the release-element margin (>2.00), is itself only second-hand within S2 (attributed further to a 1995 Purdy & Hurley Clementine paper) and was never independently re-verified — an unresolved secondary attribution on a load-bearing number. Updated in both `case.json` and `case.md` Appendix F, with the reasoning spelled out in both places. |
| T1-10 | FAIL — empty `new_coverage[]` | GAP (documented carve-out, not a BLOCKER) | Added `case.json.reinforcement_note`: verified directly against `readmodel/standards_spine.json` that all 5 of this case's standards (the entire precalculus limit/asymptote group) are already `n=1, covered_by=['The Reserve Asymptote']`, and that no adjacent skill in that spine group exists for this case to legitimately claim instead — a genuine reinforcement pass, not padding. This is a GAP under the project's own doctrine (a documented carve-out downgrades from BLOCKER, per the 2026-08-17 amendment), not a clean zero — flagged below. |
| T1-13 | FAIL — anchor ladder missing all 10 headings, 0/5 Socratic questions | PASS | Rewrote `FACILITATOR.md` with real `##` headings for all 10 required anchor-ladder sections (Intro, Launch, Anchor 1–4, Data Deep Dive, Twist, Close, Lessons Learned, Standards Touched On — modeled structurally on `cases/cooling-curve/FACILITATOR.md`), preserving all the case's real content (Argument A/B, the sourced margin table, the retune correction, the trap, the twist, the 45-minute plan, cohort bands). Also rewrote the 5 Socratic questions as single-line questions (the original 3-line-wrapped questions matched 0 in the machine check, since the regex requires the `?` on the same line as the numbered start). |

**T1-14 (2 orphan numbers, 7.1/7.4):** fixed by removing the bare `(SPEC §7.1)` / `(SPEC §7.4)`
section-number citations from `FACILITATOR.md`'s headers — they cited internal doc-section
numbers, not case data, and had no home in `case.md`/`case.json`.

### Tier 1 re-run — final result

```
TIER 1 — STRUCTURAL   case: the-clampband-margin
checks run: 20   PASS 19 · GAP 1 · FAIL 0

=== BLOCKER (0) ===

=== GAP (1) ===
 * [T1-10] SPEC §8 -- new_coverage[] is empty; the case closes no NEW gap
   (reinforcement carve-out, documented and doctrine-approved -- see above)

VERDICT: TIER1_PASS  (0 blockers, 1 gaps)
```

**Verdict: TIER1_PASS.** The single remaining GAP (T1-10) is a documented, doctrine-sanctioned
carve-out, not an unresolved defect — every adjacent skill was checked and honestly ruled out
(`case.json.reinforcement_note`).

### `sensitivity_model.py` — authored and verified (the focus of this pass)

`cases/the-clampband-margin/sensitivity_model.py` now exists, following the contract in
`skills/case-readiness/scripts/example_sensitivity_model.py` and the feasibility-gated pattern in
`cases/bioreactor-bid/sensitivity_model.py`.

**What `evaluate()` actually models — not the raw n=3 ratio.** `case.json.balance.margin_pct`
(9.6%) is the percent difference between the two stack-up methods' predicted tolerance *at n=3
only*. Per the case's own FACILITATOR.md, that number is **not** what decides the case — a Hero
who stops at n=3 sees a false near-tie and misses the point. The real recommendation logic (also
FACILITATOR.md's own language) is: does each option clear **both** of NASA-adjacent industry's
margin thresholds (gapping ≥ 1.25, release-element ≥ 2.00) at **every** modeled supplier count
(n = 3, 6, 7, 10)? An option that fails either threshold at any modeled n is disqualified (scored
0); a surviving option's score is its worst (minimum) margin across the range. `evaluate()`
implements exactly this, and `raw_ratio_n3()` is kept separately only to reproduce the stated 9.6%
figure for verification.

**Base case (reproduces the case's own numbers):**
```
A (Worst-Case)   = 0.0     (disqualified -- fails the release-element margin at n=7 and n=10)
B (Modified RSS) = 2.64    (clears both thresholds at every modeled n; worst case at n=10)
```
This matches FACILITATOR.md's table exactly (WC margin 1.79 at n=7, fails >2.00; 1.25 at n=10,
fails >2.00; MRSS margin 2.64 at n=10, its own worst point, still clears >2.00).

### Probe 5 — assumption-sensitivity: mechanically run, both scopes

**Doctrinal default scope** (SPEC §2's own definition: flex *stated Modeling Assumptions*, not
cited data): `FLEX = ["gapping_allowance_in"]` (MA4, the case's own documented "single most
load-bearing assumption"). Result: **PASS (disclosed)**.
```
base: {A: 0.0, B: 2.64}   base_winner: B
gapping_allowance_in -50% -> winner TIE (base B)   [FLIPS]
gapping_allowance_in +50% -> margin 395.3% (zero-floor artifact, not a real % -- see caveat)
```
Disclosed via a new `case.json.sensitivity_disclosure[]` entry (category F — this is a genuinely
irreducible unknown; no public source connects a tolerance-stack value to NASA-adjacent industry's
load-safety factors for a general clampband joint, so there is no more-defensible allowance to
substitute). `tier2_probes.py` accepts this as a doctrine-sanctioned pass — the instability is
disclosed, not eliminated or hidden.

**This QA pass's specific request — the ×1.5 correction factor and the ISO 2768/Protolabs
tolerance values** (cited data, swept explicitly via `--flex-all` / running the model directly,
outside the doctrinal default scope, precisely to answer the question this pass was scoped
around):

```
python3 skills/case-readiness/scripts/tier2_probes.py --case the-clampband-margin --probe 5 --flex-all
```

| dial | -50% | +50% |
|---|---|---|
| **correction_factor (×1.5, S6)** | B margin 5.27 (still wins, more comfortably) | **B margin 0.0 — DISQUALIFIED, ties with A. FLIPS.** |
| tol_flange_in (S3) | B margin 3.45 | B margin 2.13 |
| tol_ring_in (S4) | B margin 3.10 | B margin 2.29 |
| tol_boltshim_in (S3) | B margin 2.98 | B margin 2.36 |

**The real, verified answer:**

**(b) The underlying ISO 2768/Protolabs tolerance base values — ROBUST.** A ±50% swing on any one
of the three real per-interface tolerances (flange OD, ring ID, bolt+shim stack), independently,
never flips the winner and never disqualifies either option differently than the base case:
Worst-Case stays disqualified in every scenario tested (still fails the release-element margin
by n=7–n=10), and Modified RSS's worst-case margin across the modeled range stays between 2.13 and
3.45 — always comfortably above the 2.00 release-element floor. The case's real conclusion (B is
the durable winner once the scaling frame is engaged) does not depend on getting these three
tolerance values exactly right.

**(a) The ×1.5 correction factor itself — NOT symmetrically robust.** A -50% swing (factor drops
to 0.75) only strengthens Option B's case (worst-case margin nearly doubles, to 5.27). But a +50%
swing (factor rises to 2.25) is **not survived**: Modified RSS's own predicted tolerance at n=10
then exceeds NASA-adjacent industry's release-element threshold, so Modified RSS becomes
disqualified too — collapsing the case's real recommendation from "B durably clears both
thresholds across the whole modeled range" to "neither stack-up method clears the release-element
margin at the largest modeled supplier count." **This has never been mechanically checked before
this pass; it is now.** It does not mean the case's winning-option finding is wrong at the stated,
sourced value of 1.5 (S6 is a real, HIGH-confidence, directly-quoted primary source, not a guess) —
it means the case's durability claim is real but not infinitely robust, and is asymmetric in a way
neither `case.md` nor the prior `FACILITATOR.md` had stated or tested.

This asymmetric finding is recorded in `sensitivity_model.py`'s own header/docstring and in
`FACILITATOR.md`'s new "Probe 5 finding" section (pointer only, per the no-leak-in-case.md rule —
the actual numbers stay here and in `sensitivity_model.py`).

---

## case-readiness run — 2026-08-31 (Tier 2 completion pass — SUPERSEDES the "PENDING adjudication"
## note above; this run closes P1/P2/P3/P4/P6, which the prior run left un-adjudicated)

**State:** TIER1_PASS → **TIER2_PASS**   **Verdict:** all six Tier 2 probes recorded, 0 FAIL.

This run picks up exactly where the prior run in this file left off: Tier 1 was already clean
(0 BLOCKERs, the single T1-10 GAP unchanged — re-verified below), and Probe 5 was already
mechanically PASS (disclosed). What was missing was P1/P2/P3/P4 (adjudication by a fresh read)
and P6 (a live fetch of all six source URLs). This pass performs all five, fixes one omission
found along the way (the ×1.5 correction-factor fragility was mechanically verified last run but
never entered into `case.json.sensitivity_disclosure[]`, and the Twist was never actually built
around it), and reaches `TIER2_PASS`.

### Tier 1 — re-verified, unchanged

```
python3 skills/case-readiness/scripts/tier1_structural.py --case the-clampband-margin
```
20 checks: PASS 19 · GAP 1 (T1-10, the same documented reinforcement carve-out) · FAIL 0.
`case_md_sha256` still matches `case.md` on disk — `case.md` was not touched this pass, only
`case.json` and `FACILITATOR.md`. Re-ran Tier 1 a second time after the `FACILITATOR.md` Twist
edit (below) to confirm the T1-14 continuity checks (Guide Notes vs. `case.json`/`case.md`) still
hold — they do.

### P1 · Cold solve — PASS

**Method:** dispatched a genuinely fresh general-purpose subagent with no memory of this
conversation. It was given only the path to the leak-free packet
(`/tmp/coldsolve-the-clampband-margin/PACKET.md`, the same file `tier2_probes.py` generates from
`case.md`) and was explicitly instructed not to open `FACILITATOR.md`, `QA_REPORT.md`,
`case.json`, `RESEARCH_LOG.md`, or `sensitivity_model.py`, and not to search the repo.

**Result:** the solver chose **B**, optimizing for "does the margin against NASA-adjacent
industry's thresholds hold across the full modeled supplier-count range, not just at n=3" — the
correct metric, arrived at for the correct reason (the case's own framing: "a stated position on
how the company evaluates every future joint of this kind"). Its arithmetic reproduces
`FACILITATOR.md`'s table exactly: WC margins 4.17 / 2.08 / 1.79 / 1.25 and MRSS margins 4.61 /
3.40 / 3.15 / 2.63 at n = 3/6/7/10, and it independently re-derived D2's algebraic horizontal
asymptote ($R(n) = 1.5/\sqrt{n} \to 0$). It named MA4 (the gapping allowance) as the most sensitive
assumption and the assumption itself as the least-trustworthy number in the case — both consistent
with `case.json`'s own `sensitivity_disclosure[]` and Appendix E's own self-assessment.

**Pass criterion met:** a defensible position, correct arithmetic, a named and justified metric,
reached by the intended route (engaging the scaling/asymptote argument), not by eyeballing which
n=3 number looked bigger. Full transcript is in this session's record; not reproduced here to
avoid re-leaking the solved arithmetic into a file a future Hero might read.

### P2 · Both-sides solve — PASS

**Method:** verified `case.json.balance.argument_a` / `argument_b` directly (not via a fresh
solver — this probe's machine pre-screen is the applicable check, per `tier2_probes.py`'s own
design). Both carry real, load-bearing quantitative content — `argument_a` cites the real n=3
margin (4.17), the real per-supplier tolerance sum (0.0168 in from Appendix C's actual 0.0079 +
0.0050 + 0.0039), and the real thresholds (1.25 / 2.00); `argument_b` cites the real ×1.5
Bender/Motorola correction and its sourced rationale (S6). Neither reads as a concession
("B is cheaper but worse in every other way") — both are genuine, numbers-forward cases for their
side.

**Which side collapses first, and where:** in the case's own base scenario, **Option A (Worst-
Case) collapses first and structurally** — it fails the release-element margin starting at n=7
and sits exactly at the gapping-margin floor by n=10 (Appendix D's real numbers, no flex needed).
Option B does not collapse anywhere in the case's stated base scenario; it only wobbles under an
adversarial *flex* of a cited, sourced dial (the ×1.5 correction factor, +50% — see Probe 5), which
is a different, and disclosed, kind of fragility than a structural collapse inside the case as
written. This asymmetry — A fails on the case's own terms, B only fails if you doubt one of its
real inputs by half — is itself evidence the balance is genuine rather than a paper 9.6%: a
sharp Hero can mount a real defense of either side, and the two defenses fail for different,
identifiable reasons rather than one side just being weaker throughout.

### P3 · Trap check — PASS

**Method:** the same fresh subagent's blind answer (question 8: "what's the most plausible wrong
path?") was recorded *before* it or I referenced `FACILITATOR.md`'s own trap text, then compared.

**Result:** near-exact match. The subagent's blind answer: a student computes only n=3, sees both
methods clear the thresholds comfortably, and picks "whichever looks safer/bigger" without ever
building the table past n=3 — missing that the case is a scaling/policy decision, not a single-
joint check. `FACILITATOR.md`'s own trap (written independently, before this probe): "Heroes will
compute the n=3 case (D4), see that both methods clear the thresholds by comparable amounts, and
conclude the dilemma is trivial or already resolved — 'just pick whichever number is bigger/safer,
it barely matters' ... A Hero who never builds the table past n=3 never sees that divergence." The
guide names the trap a fresh reader actually falls into — this is not a guide anticipating the
wrong danger.

### P4 · Twist integrity — PASS (strengthened this pass)

**Q1 — does the twist invalidate a position a real room would hold?** Yes. The trap identified in
P3 (stopping at n=3, "pick whichever's safer") is precisely the position Anchor 2's own script
expects most Heroes to land on initially ("most Heroes will initially frame this as a single
pass/fail check on today's three parts and miss the scaling angle entirely"). The Twist's scaling
reveal directly invalidates exactly that position.

**Q2 — does the twist survive the case's own stated assumptions, read the way a student would?**
Checked against Appendix E's MA1: MA1 states the modeled counts (n=6, 7, 10) were chosen because
they are "the counts where the real math actually changes the pass/fail answer," not because they
are asserted to be any specific real future program's contracted design. The Twist's claim that
"the exact count is in Appendix D, MA1" is consistent with, not contradicted by, that framing —
MA1 doesn't preclude one of its illustrative counts from also being the story's next-program
figure, and nothing in Appendix E states a convention that would make this reading strained. No
BLOCKER-level convention gap found (contrast with Cold Chain's twist, which failed here).

**Strengthened this pass, per the explicit brief:** the disclosed ×1.5-correction-factor asymmetry
(Probe 5) was mechanically verified last run but was sitting only in `sensitivity_model.py` and
this report — it was not yet built into the case's actual discussion mechanics, and
`case.json.sensitivity_disclosure[]` didn't carry an entry for it either (only `gapping_allowance_in`
did). Both gaps are now closed:

- Added a `correction_factor` entry to `case.json.sensitivity_disclosure[]` (category F),
  recording the same asymmetric finding in the same disclosure structure as MA4's entry.
- Rewrote `FACILITATOR.md`'s Twist section into two beats. **Beat 1** is the original scaling
  reveal, unchanged. **Beat 2** (new) comes immediately after the room has recommitted to B: the
  facilitator presses the most confident B-defender directly — "you're trusting a ×1.5 correction
  factor from a 1962 study; what if it should really be 2.25?" — and, without pre-answering it,
  lets the room discover that at n=10 (the count B's whole "durable" case rests on), a ×2.25
  factor pushes Modified RSS past the release-element threshold too, disqualifying B alongside A.
  This is exactly the "discussion lead pressing a confident B-defender and watching the case
  genuinely wobble" mechanic the brief asked for, and it is now mechanically grounded (Probe 5's
  own numbers), not an invented dramatic beat. Also updated the 45-minute plan and the Lessons
  Learned placeholder to reference Beat 2. Re-ran Tier 1 after this edit — T1-14 continuity checks
  (Guide Notes agree with `case.json`) still pass.

### P5 · Assumption sensitivity — PASS (disclosed) — unchanged from the prior run in this file

No change to the mechanical result from the previous section of this report. Restated for
completeness: doctrinal-scope (FLEX = `["gapping_allowance_in"]`) result is PASS (disclosed);
the explicitly-requested `--flex-all` stress-test of the ×1.5 correction factor and the three
ISO 2768/Protolabs tolerance values found the tolerance base values robust and the correction
factor asymmetrically fragile (survives -50%, fails +50% at n=10) — see the prior section of this
report for the full numbers. Both findings are now disclosed in `case.json.sensitivity_disclosure[]`
(this pass added the `correction_factor` entry; `gapping_allowance_in` was already there).

### P6 · Data decay — PASS

The QA sandbox restriction did not apply outside this session — all six `sources[]` URLs were
live-fetched directly (via `curl` for reachability and via direct PDF read for content
verification, since two of the six did not extract cleanly through a summarizing web-fetch tool).

| # | URL | Reachable | Figure still present | Notes |
|---|---|---|---|---|
| S1 | extapps.ksc.nasa.gov/.../2214.pdf (NASA GD-ED-2214) | YES (200) | YES — verbatim | Read all 8 pages directly. Page 6: "The criterion for designing strap preloads is that no gapping occurs when the maximum expected load is applied." Confirmed: no numeric margin (1.25 or 2.00) appears anywhere in the document — the case's own "correction" note about this is accurate, not stale. |
| S2 | esmats.eu/amspapers/pastpapers/pdfs/2012/lazansky.pdf (Lazansky, SNC, ESMATS 2012) | YES (200) | YES — verbatim | Read the relevant page directly (author Chuck Lazansky, "Refinement of a Low-Shock Separation System"). Page 11: "A reasonable choice is to design and test to 1.25x worst case load predictions. Maintaining high margins on the release element (>2.00) has been recommended..." Reference list confirms footnote 15 = "Purdy, W & Hurley, M 'The Clementine Mechanisms,' 29th Aerospace Mechanisms Symposium, May 1995" — exactly matching `case.json`'s note that the release-element figure is itself second-hand within S2. MEDIUM confidence grading (assigned in the prior QA pass) stands as correctly calibrated, not stale. |
| S3 | rpproto.com/.../General-Tolerances-ISO-2768.pdf | YES (200) | YES — verbatim | Table 1, class f (fine): 120–400mm range ±0.2mm, 6–30mm range ±0.1mm. Exact match to Appendix C. |
| S4 | protolabs.com/.../fine-tuning-tolerances-for-cnc-machined-parts/ | YES (200) | YES | "+/- 0.005 in. (0.13mm)... in accordance with ISO 2768-1-1989-f (metals), ISO 2768-1-1989-m (plastics)" confirmed verbatim. Minor, non-load-bearing wording drift noted: the live page currently reads "...at the Protolabs semi-automated factory and the Protolabs Network..." where `case.json`'s S4 quote says "...at the Protolabs automated factory..." — the cited tolerance VALUE and the ISO-equivalence claim (the load-bearing content) are unchanged; only the descriptor of which factory tier this applies to has drifted slightly. Not a BLOCKER (the number didn't move), flagged as a POLISH-level wording note for a future pass. |
| S5 | protolabs.com/.../injection-molding-tolerances/ | YES (200) | YES — verbatim | "+/- 0.003 in. (0.076mm)" mold-tool tolerance and "+/- 0.002 in./in. (0.051mm/mm)" resin tolerance both confirmed exactly as quoted. |
| S6 | faculty.washington.edu/fscholz/Reports/isstech-95-030.pdf (Scholz, Boeing, 1995) | YES (200) | YES — verbatim | Read the relevant pages directly. Page 16: "if $T_i$ is specified with the misconception $T_i \equiv 2\sigma_i$, then $T_i$ is too small by a factor 1.5. To correct for this, Bender (1962) suggests to multiply the $\pm T_{assy}$ value by 1.5 and calls this process 'benderizing'" with the boxed equation $T_{assy}(\text{Bender}) = 1.5\sqrt{a_1^2T_1^2+\ldots+a_n^2T_n^2} = 1.5\,T_{assy}$ — matches `case.json` S6's quote and the case's D2/D4 formula exactly. Glossary (p. iv) independently corroborates the same formula.

**Verdict: PASS.** All six sources reachable, all six recorded figures verified present and
unchanged against direct primary-source reads (not just automated summarization, which failed to
extract usable text from two of the six PDFs) — including both aerospace sources specifically
named in this pass's brief. One cosmetic, non-load-bearing wording drift noted on S4 (POLISH, not
a defect requiring a case-write pass).

### Tier 2 — final scorecard

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | fresh solver reached B via the intended metric (durability across modeled n, not the n=3 ratio), with correct arithmetic matching `FACILITATOR.md` exactly |
| P2 both-sides | **PASS** | both arguments carry real quantitative content; A collapses first and structurally (n≥7 in the base case), B only wobbles under an adversarial flex of a cited dial (disclosed separately) |
| P3 trap | **PASS** | fresh reader's blind wrong-path answer matches `FACILITATOR.md`'s stated trap almost exactly |
| P4 twist | **PASS** | invalidates a position a real room would hold (the P3 trap position); survives the case's own stated assumptions (MA1 does not contradict it); strengthened this pass with a second twist beat built on the disclosed ×1.5-factor fragility |
| P5 sensitivity | **PASS (disclosed)** | doctrinal scope (MA4) discloses a real instability; explicitly-requested `--flex-all` sweep found the ISO 2768/Protolabs tolerance base robust and the ×1.5 correction factor asymmetrically fragile — both now disclosed in `case.json.sensitivity_disclosure[]` |
| P6 data decay | **PASS** | all 6 sources live, all 6 figures verified unchanged against direct primary-source reads, including both aerospace PDFs named in this pass's brief |

## Verdict

**TIER2_PASS.** All four Tier 1 BLOCKERs from the original run remain fixed (re-verified); the one
remaining Tier 1 finding (T1-10) is the same documented, doctrine-approved reinforcement carve-out.
All six Tier 2 probes are now recorded by name, 0 FAIL.

**Standing caveat, not a blocker:** this case's real recommendation ("B wins durably across the
full modeled supplier-count range") is asymmetrically fragile to one cited, sourced input — the
×1.5 Bender/Motorola correction factor. It is real, HIGH-confidence, and mechanically verified
live and unchanged (this pass's P6 fetch), and a -50% error in it only strengthens B's case — but
a +50% error collapses B's advantage entirely at the largest modeled supplier count (n=10), tying
it with the already-disqualified A. This is disclosed in `case.json.sensitivity_disclosure[]`,
mechanically encoded in `sensitivity_model.py`, and — new this pass — built directly into
`FACILITATOR.md`'s Twist as a second discussion beat, so a facilitator running this case is
equipped to use the fragility live rather than be caught by it if a sharp Hero raises it
unprompted. This is not a defect requiring the case to be blocked or retuned — SPEC §2 does not
forbid an assumption-sensitive verdict, only an *undisclosed* one — and the underlying ISO
2768/Protolabs tolerance values themselves (the other thing this pass was asked to check) are
genuinely robust to the same ±50% test.

**Next step:** `case-publish` may now run on `the-clampband-margin` (Tier 1 + Tier 2 both clean).
Tier 3 (a human dry-run with real learners) remains `NOT RUN` and is not required for `PUBLISHED`,
only for `VERIFIED` / a ✅ in the doctrine ledger.

### Tier 2 — simulated play (6 probes): mechanical layer clean

```
MECHANICAL RESULT: 0 probe(s) FAILED mechanically
PENDING adjudication (subagent / fetch / missing model): [1, 2, 3, 4, 6]
```

| probe | mechanical status | note |
|---|---|---|
| P1 cold solve | READY | needs a fresh-eyes solver run (not performed in this pass — out of this pass's specific scope, which was Tier 1 blockers + Probe 5) |
| P2 both-sides | READY (was FAIL) | fixed: `case.json.balance.argument_a` carried zero digits; added real quantitative content (WC's n=3 margin of 4.17, the real Appendix C tolerance sum) so the strongest-case-for-A argument is quantitative, per SPEC §2 |
| P3 trap | READY (was FAIL) | fixed: `FACILITATOR.md`'s opening sentence used the word "trap" before the real trap section, and that first occurrence (a meta-comment about where content lives) had no wrong-path verb, so the mechanical check graded the wrong sentence. Reworded the opening sentence to drop that early "trap" mention; the real trap section (unchanged content) is now what the check reads. |
| P4 twist | READY | not separately adjudicated this pass |
| P5 sensitivity | **PASS (disclosed)** | see above — the case's real focus this pass |
| P6 data decay | DELEGATED | QA sandbox has no outbound network; the 6 source URLs (S1–S6) still need a live fetch-and-confirm pass |

Tier 2 is mechanically clean (0 hard FAILs), but per the skill's own rule, is not fully "clean"
until P1/P2/P3/P4 are adjudicated by a fresh read and P6's 6 URLs are actually fetched — both
require either a subagent session or live network access neither of which this specific pass's
scope (Tier 1 blockers + the sensitivity-model verification) covered. Flagged here as the honest
remaining state, not silently marked done.

## Verdict

**TIER1_PASS.** All 4 original Tier 1 BLOCKERs are fixed; the one remaining Tier 1 finding
(T1-10) is a documented, doctrine-approved carve-out. Tier 2's mechanical layer is clean (0 hard
FAILs across all 6 probes, including two additional fixes found and closed along the way — P2's
non-quantitative Argument A, and P3's mis-triggered trap-name check).

**Probe 5, specifically on the ×1.5 correction factor:** the case's retuned 9.6% margin_pct is a
raw n=3 ratio, not the quantity that actually decides the dilemma. The quantity that does decide
it — does each option clear NASA-adjacent industry's thresholds at every modeled supplier count —
is **robust to a ±50% swing on the three real ISO 2768/Protolabs tolerance values**, but is
**only asymmetrically robust to a swing on the ×1.5 correction factor itself**: it survives being
too small (-50%) with the winning margin nearly doubling, but does **not** survive being too large
(+50%) — at that flex, the Modified RSS Stack itself fails the release-element margin at n=10 and
the case's clean "B wins durably" recommendation collapses to "neither option clears the threshold
at the largest modeled count." This is now mechanically verified, not just argued in prose, and is
recorded in `sensitivity_model.py`, `case.json.sensitivity_disclosure[]`, and
`FACILITATOR.md`.
