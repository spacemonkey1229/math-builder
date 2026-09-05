# QA Report — The Lease Break

## case-readiness run — 2026-09-03 (remediation + Tier 2)

**State:** TIER1_PASS   **Verdict:** TIER1_PASS_TIER2_BLOCKED — do NOT run `case-publish`.

This entry supersedes the earlier 2026-09-03 entry below (kept for history), which recorded the
initial crash/BLOCKED run. This entry documents the schema fix, the four originally-listed
BLOCKERs being resolved, and — new, found while writing quantitative balance arguments for Tier 2 —
a genuine content defect in the case's own recorded numbers that Tier 1's mechanical checks cannot
see and that blocks a clean Tier 2 pass.

### How the `margin_pct` schema issue was resolved

`tier1_structural.py`'s T1-09 (`mp = c.get('margin_pct', bal.get('margin_pct'))`) and T1-14
(`float(v)` on `balance.margin_pct`) both require `margin_pct` to be a single scalar. This case
genuinely has two scenario margins — stay-full-term (16.9%) and break-at-month-6 (6.6%) — because
D2/D3 are designed to plausibly favor different options. **The checker script
(`skills/case-readiness/scripts/tier1_structural.py`) was NOT edited.** Instead, at the
`case.json` data-shape level:

- `case.json.margin_pct` (top level, was `null`) is now `6.6` — a plain scalar.
- `case.json.balance.margin_pct` (was a two-key dict) is now `6.6` — a plain scalar.
- The full two-scenario detail is preserved, undisturbed, in a new
  `case.json.balance.margin_pct_by_scenario` object (`{"stay_full_term": 16.9,
  "break_at_month_6": 6.6, "note": ...}`), plus a new `balance.margin_pct_note` explaining the
  convention.
- The scalar reports the **more conservative (narrower) margin** (6.6%, break-at-month-6), per this
  session's instructions, since a narrower margin is the more binding constraint against SPEC §2's
  ~20% cap. This mirrors `cases/the-bracket-bet/case.json`'s pattern of using a single top-level
  scalar for a two-scenario balance (that case reports its own two margins, 12.8% and 2.3%, only in
  prose — it has no precedent multi-scenario dict, so lease-break's `margin_pct_by_scenario`
  addition is new, not copied).
- `case.json.cohort_bands[]` was also added (previously absent — a GAP, not a blocker — but its
  content now matches FACILITATOR.md's new Cohort Bands section 1:1).

This restored T1-09 and T1-14 to running (and passing) instead of crashing. **The per-scenario GAP
review requested in this session's instructions** ("per the checker's own `elif mp > 15` rule, the
16.9% stay-full-term figure would land as a GAP") is recorded here explicitly, since routing the
scalar through T1-09 as 6.6% means the mechanical check never sees 16.9% at all: **had the checker
evaluated 16.9% instead, it would report `GAP — margin is 16.9% — inside the cap but wide; the
discussion will be one-sided`.** This is disclosed here rather than silently passed. (As detailed
below, this GAP is now the least of the case's balance problems.)

### BLOCKERs fixed

1. **T1-02** — Overview's "6 mo" numeral (an exact match to MA5/MA6's contract-term figure) was
   rewritten to "a while longer" — qualitative, no leaked numeral. Confirmed PASS on re-run.
2. **T1-09** — resolved by the schema fix above.
3. **T1-13 (anchor ladder)** — `FACILITATOR.md` rebuilt with the full mandatory anchor ladder
   (Intro, Launch, Anchor 1–4, Data Deep Dive, Twist, Close, Lessons Learned, Standards Touched
   On) as level-3 `###` headings (the original file used bold text, which the checker's
   heading-regex does not match), in the required order (Anchor 2/3 before Data Deep Dive).
4. **T1-13 (Twist)** — added a full `### Twist` section with content (not "N/A").
5. **T1-13 (timed plan)** — added a `## 45-minute Socratic plan` section with a 7-row timed table
   naming the TWIST moment, matching SPEC §7.3's shape.
6. **T1-13 (Socratic-question parser mismatch)** — confirmed the root cause: the checker's regex
   (`^\s*(?:\d+[.)]|[-*>])\s.*\?`, no `DOTALL`) only matches a numbered line that itself ends in
   `?`. The original file's 5 Socratic questions were each wrapped across 2 lines, so the question
   mark never appeared on the same line as the leading `1.`/`2.`/etc., and every one silently
   missed the regex — a real formatting bug, not missing content. Fixed by putting each of the 5
   questions on a single unwrapped line. Confirmed 5/5 now parse.
   `case.json.status="qa"` also reflects `FACILITATOR.md`'s updated Status line (`case-research`
   complete, no longer `draft`).

### Status: verified clean re-run

```
python3 skills/case-readiness/scripts/tier1_structural.py --case the-lease-break
VERDICT: TIER1_PASS  (0 blockers, 1 gaps)
```

| id | result | note |
|---|---|---|
| T1-01..T1-09 | PASS | — |
| T1-10 | GAP | `new_coverage[]` empty; carved out by `reinforcement_note` per the 2026-08-17 doctrine amendment (pre-existing, not new) |
| T1-11..T1-20 | PASS | T1-15/18/19/20 report POLISH ("no `published/` dir yet") — expected pre-publish |

---

## MAJOR FINDING (found writing Tier 2's quantitative balance arguments, not a Tier 1 check)

While writing `case.json.balance.argument_a`/`argument_b` with real numbers (required for Tier 2
Probe 2's "no bare qualitative argument" mechanical screen), the numbers themselves exposed that
**the case's own recorded conclusion about which lease wins the break-at-month-6 scenario is
backwards.**

Independently re-derived, three times (by hand, by a purpose-built `sensitivity_model.py`, and by
two separate fresh subagents dispatched for Probes 1 and 3 who reached the same numbers on their
own): using the case's own D2/D3 methodology and its own recorded dollar figures —

- **Stay-full-term (D2):** Cedarline $1,423.58 vs. Aldergate $1,664.00 → **Cedarline cheaper by
  16.9%.** (This matches the original write-up.)
- **Break-at-month-6 (D3):** Cedarline $1,921.17 vs. Aldergate $2,048.00 → **Cedarline cheaper by
  6.6%.** (The original case-research write-up and `RESEARCH_LOG.md` both stated this exact pair of
  dollar figures but attributed the win to **Aldergate**. $1,921.17 < $2,048.00 — Cedarline is
  numerically cheaper. The 6.6% *magnitude* was computed correctly; only the *winner label* was
  backwards — a sign/attribution error, not an arithmetic error.)

**Consequence:** Cedarline is cheaper in BOTH scenarios under current assumptions. This case does
not currently have the scenario-dependent reversal it was designed around (`balance.margin_basis`:
"the two scenarios are designed to plausibly favor different options" — they don't, as sourced).
A learner who only compares sticker-price rent and a learner who does the full amortized-cost math
in both scenarios currently reach the same answer — there is no live "trap" distinguishing careless
from careful analysis either.

**What was fixed in this pass (arithmetic honesty only, not the design defect):**
- `case.json.balance.argument_a` / `argument_b`, `margin_pct_by_scenario.note`, and
  `sensitivity_note` all corrected to state which side actually wins each scenario.
- `FACILITATOR.md`'s "Argument for A/B," "The margin," "The trap," "Data Deep Dive," "Twist," and
  "Close" sections all corrected to state the real numbers and flag the design defect explicitly,
  rather than asserting the (incorrect) reversal as fact.
- A top-of-file "MAJOR OPEN FINDING" note added to `FACILITATOR.md` so no facilitator can miss it.

**What was NOT fixed, and why:** retuning MA1–MA4 to restore a genuine flip (or accepting a
single-scenario case and rewriting the Dilemma/D5/Twist framing around a risk-vs-cost tension
instead of a cost-reversal tension) is a case-research/case-write design decision, not a QA
mechanical fix — `case.json.sensitivity_note` records the specific dead ends already checked (MA2
is already at the top of its real 1–2-month cited range and cannot legitimately go higher without
becoming unsupported; MA4 is already at the bottom of its range and cannot go lower). This case
should not be published until a human decides which path to take.

---

## Tier 2 — six probes, run for real

**P1 · cold solve — PASS.** Dispatched a genuinely fresh, unbriefed subagent given only
`/tmp/coldsolve-the-lease-break/PACKET.md` (verified leak-free by the harness) and forbidden from
reading any other file.
- Chose **A (The Cedarline)**.
- Named the metric explicitly: effective cost per month of actual occupancy, amortized under both
  scenarios.
- Arithmetic verified independently and matches the case's own numbers exactly: D2 $1,423.58 vs.
  $1,664.00; D3 $1,921.17 vs. $2,048.00; D4 spot-checks ($415/$1,389=29.9% ≈ MA1's "~30%"; reverse
  check on the Aldergate deposit) both correct.
- Unprompted, identified the same methodological crack this report is built around: the Aldergate's
  security deposit is refundable, and amortizing it as a sunk cost (as the case's own D2/D3
  instructions literally require) may overstate Aldergate's cost — excluding it would flip D3 to
  favor Aldergate ($1,792 vs. Cedarline's $1,921.17). Correctly named MA2 as the most sensitive
  assumption and flagged it as the least-supported figure.
Reaches a defensible position via correct arithmetic and names the metric — the pass bar. **PASS.**

**P2 · both-sides solve — FAIL.** Mechanical screen was clean (both arguments carry real numbers)
once `case.json.balance.argument_a/argument_b` were rewritten with dollar figures, but the
human-adjudicated result is a clear FAIL:
- **Argument A** is not just strong, it is a foregone conclusion — Cedarline wins both scenarios,
  by 16.9% and by 6.6%, on the case's own recorded numbers.
- **Argument B** cannot survive as a *cost* argument at all — the only version of it that holds up
  under pressure is a risk-bounding argument ("Aldergate's exposure is capped at a known $1,536"),
  not a cheaper-lease argument. A student asked to defend B by cost, as D5 implicitly invites
  ("defended with D2's and D3's effective-monthly-cost numbers"), has nothing real to stand on.
- **Which side collapses first?** B, immediately, the moment anyone runs D3's actual numbers rather
  than asserting "Aldergate's buyout is capped so it must be cheaper in the break scenario."
This is exactly the "if either side collapses, the recorded margin is a paper number" failure mode
the probe's own prompt warns about. **FAIL.**

**P3 · trap check — FAIL (self-diagnosed).** Mechanical pre-screen initially FAILed for a scripting
reason (the extraction regex grabbed the word "trap" from this report's/FACILITATOR's own
introductory prose before reaching the real `## The trap` heading) — fixed by removing earlier bare
uses of the word "trap" in `FACILITATOR.md` so the heading is the first match; not a case defect,
not a script edit.
With that fixed, a second genuinely fresh subagent was dispatched: given only `case.md`, it
independently predicted the intended trap (sticker-price shortcut vs. amortized math), then verified
by running D2/D3 itself — and, unprompted, discovered the same result as above (Cedarline wins
both scenarios, so the trap does not spring). Reading `FACILITATOR.md` second, it confirmed the
guide names the identical intended trap and is honest that the trap is currently inert, identifying
the guide's own fallback (Argument B's cost-vs-risk conflation) as the only trap with real teeth
right now — a narrower, softer trap than the one `case.md`'s D1–D5 structure is built around.
Verdict: the guide *anticipated the right trap* (a pass condition), but the trap **does not
currently function** in a live room (a fail condition) — net **FAIL**, rooted in the same content
defect as P2, not a new one.

**P4 · twist integrity — FAIL.** The Twist ("Maya's manager confirms the contract extension one way
or the other — does your recommendation change?") was designed to expose fragile
(scenario-specific) vs. robust reasoning. Under current numbers:
- If the facilitator delivers "confirmed NOT extended" (forcing D3): no group's recommendation
  should change, since D3 already favors Cedarline — the twist does no invalidating work in this
  branch.
- If the facilitator delivers "confirmed extended" (forcing D2 only, D3 moot): this branch *does*
  invalidate one real position — a room that chose Aldergate specifically to hedge the early-break
  risk should now abandon that reasoning, since the risk it was hedging is gone and Cedarline was
  already cheaper on D2 alone. This is a real, usable moment.
`FACILITATOR.md` currently presents both branches as an interchangeable "facilitator's choice"
without surfacing this asymmetry, so as written the guide under-equips a facilitator to extract the
one branch that actually works. The core "fragile vs. robust, does the scenario-dependent
recommendation survive" contrast this Twist mechanic exists to produce cannot fire at all, in either
branch, because there is no scenario-dependent recommendation to begin with. **FAIL** — same root
cause as P2/P3, plus a guide-authoring gap (the branch asymmetry) that is independent of it and
worth fixing regardless of how the margin defect is resolved.

**P5 · assumption sensitivity — FAIL.** Authored `cases/the-lease-break/sensitivity_model.py`
(models D3's break-at-month-6 comparison; declares `FLEX = [cedarline_movein_fee,
cedarline_termination_penalty, aldergate_deposit, aldergate_buyout, break_month]`, excluding the two
cited-market rents S1/S2 from the assumption sweep since those are P6's concern, not P5's):

```
python3 skills/case-readiness/scripts/tier2_probes.py --case the-lease-break --probe 5 --flex 0.5
base_winner: A   base_margin_pct: 6.6
! VERDICT UNSTABLE: cedarline_termination_penalty +50% -> winner B; aldergate_deposit -50% -> winner B; aldergate_buyout -50% -> winner B
! BALANCE BREAKS: cedarline_termination_penalty -50% -> margin 21.2% (breaches 20% cap)
! UNDISCLOSED instability on 3 params — no case.json.sensitivity_disclosure[] entries
```
3 of 5 legitimate assumption dials either flip the winner or breach SPEC §2's cap on a ±50% swing,
and none of this instability is disclosed in `case.json`. Independent of the P2–P4 winner-label
defect, this shows the break-at-month-6 comparison is genuinely fragile — a further, separate
reason this case is not ready. **FAIL.**

**P6 · data decay — PASS, with disclosed drift.** All 6 sources fetched live this session
(`WebFetch`; S6's PDF required a local `pdftotext`-equivalent read after `WebFetch`'s own summarizer
failed to parse the binary, same issue the original researcher hit and logged in `RESEARCH_LOG.md`):

| id | reachable | claim still supported | notes |
|---|---|---|---|
| S1/S2 | Yes | **Drifted** | RentCafe's Boise page now shows studio $1,447 / 1BR $1,601 (recorded: $1,389 / $1,536), "Last updated: August 31, 2026" vs. the case's `as_of: 2026-07-02` — a ~4.2% rise on both figures in ~2 months, consistent with a rolling monthly aggregator rather than a stale/dead link. Re-running D2/D3 with the current figures (informational only, not applied) does **not** change the qualitative finding — Cedarline still wins both scenarios, by 14.3% and by a wider dollar gap in D3 — so this drift does not itself resolve or worsen the MAJOR FINDING above. Recommend refreshing S1/S2 at the next `case-research` touch given they are 2 months stale as of this QA run. |
| S3 | Yes | Exact match | 20–50% range, 2022-08-18, unchanged. |
| S4 | Yes | Exact match | 59.6% of leases at 12 months, Jan–Jun 2022 survey, unchanged. |
| S5 | Yes | Exact match | 1–2 months' rent range, unchanged. |
| S6 | Yes | Exact match on the cited clause ("cannot exceed one month's rent... or a reasonable fixed amount") | **Metadata correction:** the case records "no publication date stated on document"; the actual PDF footer states **"December 2020"** on every page. Minor — does not change the claim's confidence or currency assessment materially — but the case.json note should be corrected at the next touch. |
No URL 404s, no fabricated citation, no MCS-21 concern. **PASS** with two disclosed, non-blocking
corrections for the next case-research pass (S1/S2 refresh, S6 date correction).

---

### Tier 2 summary

| probe | verdict |
|---|---|
| P1 cold solve | **PASS** |
| P2 both-sides | **FAIL** |
| P3 trap | **FAIL** (self-diagnosed; script regex issue found and worked around, not fixed in the script) |
| P4 twist | **FAIL** |
| P5 sensitivity | **FAIL** |
| P6 data decay | **PASS** (2 disclosed, non-blocking drift/metadata findings) |

**Tier 2 is NOT clean.** P2, P3, and P4 all trace back to the same root cause (the case does not
currently have a genuine scenario-dependent reversal). P5 is a related but independently-discovered
fragility in the break-scenario comparison. None of this was fixed in this pass — it is a
case-research/case-write decision (retune assumptions to restore the intended reversal, or redesign
the case around a risk-vs-cost tension) that this QA pass is not authorized to make unilaterally.

## Tier 3 — human dry-run
NOT RUN. Do not schedule until Tier 2's findings above are resolved and a clean re-run posted.

## Next step
Route back to `case-research`/`case-write` with this report. Recommended paths, in order of
preference: (1) find real-world grounding for a larger Cedarline-side cost (a steeper termination
penalty, an additional real fee) that restores a genuine break-at-month-6 reversal without exceeding
real cited ranges; (2) if no such grounding exists, redesign the Dilemma/D5/Twist/FACILITATOR.md
trap around the risk-vs-cost tension this case's numbers actually support (Cedarline is cheaper,
Aldergate is safer) rather than a cost-reversal tension. Either path requires a fresh Tier 1 + Tier 2
run before this case can move toward `case-publish`.

---

## case-readiness run — 2026-09-03 (superseded, kept for history)
**State:** DRAFT → (blocked)   **Verdict:** BLOCKED

### Preflight lint
Clean — no advisory findings (no Modeling-Assumptions leak, no FLEX[]/sources[] collision).

### Tier 1 — structural

`tier1_structural.py --case the-lease-break` **crashed** at check T1-14 before it can print any
report (all output in this script is buffered until `run()` returns, so an uncaught exception mid-run
produces zero stdout — see "Script defect" below). To recover the checks that had already executed
before the crash, `run()` was re-invoked with the exception trapped and the in-progress `R` result
object read from the crashed frame — a read-only introspection, not a modification of the script or
the case. That recovered 13 of 20 checks. **T1-14 through T1-20 did not run and have no verdict —
`NOT RUN`, not a pass.**

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | **FAIL/BLOCKER** | Overview contains numeral **`6`** (from "...push the contract another **6 mo**?..."), not a clock time or a year. This is a real leak, not texture: Appendix C / MA5 / MA6 fix Maya's contract term at exactly 6 months, and MA6's break-scenario window is defined as equal to that term. A student who notices this line could treat it as confirmation of the 6-month figure without doing the D3 reasoning. Needs a human read and either a recorded clearance in `case.json.overview_numerals_cleared[]` (if judged texture) or a rewrite of that line. |
| T1-03 | PASS | Dilemma binary, opens "You are Maya Ferris." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | appendices lettered, ordered, no orphans |
| T1-07 | PASS | final-appendix lines verbatim (POLISH: 8 labels parsed, all from bullets, none from a separator run — informational only) |
| T1-08 | PASS | every number cited or declared an assumption |
| T1-09 | **FAIL/BLOCKER** | "SPEC §2 — margin_pct not recorded." Root cause: `case.json`'s top-level `margin_pct` key is present but `null`; the real values live at `balance.margin_pct` as a **two-key dict** (`{"stay_full_term": 16.9, "break_at_month_6": 6.6}`), not the scalar SPEC §2/case.json-schema shape (`"margin_pct": 12.4`) the checker's T1-09 logic reads. Because the top-level key exists (even as `null`), `c.get('margin_pct', bal.get('margin_pct'))` returns `None` rather than falling back to the dict, so T1-09 never sees either number and reports the field as missing outright — a false "not recorded," not a real margin-cap breach. **The actual scenario margins on file are 16.9% (stay-full-term) and 6.6% (break-at-month-6), both well inside SPEC §2's 20% blocker cap.** Had the checker been able to read them as scalars, per its own thresholds the 6.6% figure would clear cleanly and the **16.9% figure would land as a GAP** ("margin is 16.9% — inside the cap but wide; the discussion will be one-sided"), not a BLOCKER. This finding is recorded as a BLOCKER here because the mechanical check cannot currently pass on this case's schema shape at all, independent of the underlying numbers being fine. |
| T1-10 | GAP | `new_coverage[]` empty; case.json's `reinforcement_note` is present and downgrades this per the 2026-08-17 carve-out (not re-litigated here) |
| T1-11 | PASS | learning-goal mutual reachability |
| T1-12 | PASS | tier vs. numeric load |
| T1-13 | **FAIL/BLOCKER** | Three findings against `FACILITATOR.md`, which is still marked `**Status:** draft (written at case-write time...)` at its own top line: (1) **BLOCKER** — anchor ladder incomplete, missing headings `Intro, Launch, Anchor 1, Anchor 2, Anchor 3, Anchor 4, Data Deep Dive, Twist, Close, Lessons Learned, Standards Touched On` (SPEC §6/§7, MCS-14); (2) **BLOCKER** — no `Twist` section and no explicit "Twist: N/A" justification (MCS-15); (3) **BLOCKER** — no timed 45-minute Socratic plan (SPEC §7.3, MCS-16). Additionally a GAP: the script's parser counts 0 Socratic questions against a spec of 5, even though a "Five Socratic questions" section with 5 numbered items exists in the file — likely a heading-format mismatch the parser doesn't recognize; flagged for `case-write`/`case-research` to reconcile, not fixed here. |
| T1-14 | **NOT RUN — script crashed** | see "Script defect" below |
| T1-15 | NOT RUN | blocked by the T1-14 crash |
| T1-16 | NOT RUN | blocked by the T1-14 crash |
| T1-17 | NOT RUN | blocked by the T1-14 crash |
| T1-18 | NOT RUN | blocked by the T1-14 crash |
| T1-19 | NOT RUN | blocked by the T1-14 crash |
| T1-20 | NOT RUN | blocked by the T1-14 crash |

**BLOCKERS (4, all confirmed real, none fixed at the time of this original entry — all resolved in
the entry above):**
1. `[T1-02]` Overview numeral `6` matches MA5/MA6's contract-term figure exactly.
2. `[T1-09]` `margin_pct` unreadable by the checker in its current schema shape.
3. `[T1-13]` `FACILITATOR.md` missing the mandatory anchor-ladder headings entirely.
4. `[T1-13]` `FACILITATOR.md` has no Twist section / no "Twist: N/A" justification.
5. *(counted with #3/#4 above by the script)* `[T1-13]` no timed 45-minute Socratic plan.

**GAPS (2):** `[T1-10]` empty `new_coverage[]`, carved out by `reinforcement_note` (informational);
`[T1-13]` Socratic-question count parses as 0 against a spec of 5 (parser/heading mismatch — the
questions did exist in the file).

**POLISH (1):** `[T1-07]` all 8 Appendix E labels parsed from bullets, none from a separator run.

### Script defect found while running this case (not fixed — reporting only)

`tier1_structural.py` line 595 (inside T1-14's balance-continuity cross-check) calls `float(v)` on
`balance.margin_pct` without checking its type. This case's `margin_pct` was deliberately a two-key
dict (`stay_full_term` / `break_at_month_6`) rather than a single scalar, because the case is
designed so the two scenarios can favor different options — a legitimate design choice recorded in
`balance.margin_basis` and `balance.margin_pct.note`. The checker has no schema support for a
multi-scenario margin, so it raised `TypeError: float() argument must be a string or a real number,
not 'dict'` and aborted before printing anything. Per this skill's own rule ("this skill CANNOT
fix"), the script was not patched. **Resolved by a case.json data-shape fix** (see the top entry of
this report) — `margin_pct` is now a scalar at both the required locations, with the full
two-scenario detail preserved separately in `margin_pct_by_scenario`.

### Tier 2 — simulated play (original entry)
NOT RUN at the time — see the top entry of this report for the real six-probe run.

### Tier 3 — human dry-run
NOT RUN.

---

## case-readiness run — 2026-09-04 (case-write/case-research remediation + full Tier 2 re-run)

**State:** TIER2_PASS   **Verdict:** TIER2_PASS — `case-publish` may run (pending a human decision to do so; not executed by this run).

This entry supersedes the 2026-09-03 `TIER1_PASS_TIER2_BLOCKED` entry above. The blocking defect
named there (Tier 2 P2/P3/P4/P5 FAIL because the case's own recorded numbers showed The Cedarline
cheaper in BOTH the stay-full-term and break-at-month-6 scenarios, so the designed scenario-dependent
reversal did not exist) was fixed at its root — re-entering at case-write/case-research per
PIPELINE.md's "QA BLOCKER on balance -> re-enter at case-write," never by hiding or reweighting data.

### The real defect and the real fix

The case was designed so that stay-full-term favors The Cedarline (lower rent wins over a long
horizon) and break-at-month-6 favors The Aldergate (its capped, one-month exit cost beats The
Cedarline's steep termination penalty once the up-front costs are amortized over only 6 months
instead of 12). As sourced on 2026-09-03, MA2 (The Cedarline's early-termination penalty) was set at
2 months' rent — the top of LeaseRunner's general 1-2 month range [S5] — which was not large enough
to overcome The Cedarline's ongoing rent advantage even at month 6: Cedarline was cheaper in both
scenarios (16.9% and 6.6%).

**Fix (case-research, 2026-09-04):** found two additional, independent real sources — Landing [S7]
and a second, distinct LeaseRunner article [S8] — both reporting that early-termination fees run
higher (2-4 / specifically 3-4 months' rent) *specifically* when several months remain on a lease at
the time of the break. That is exactly Maya's break-at-month-6 situation (6 of the Cedarline's
12-month term still outstanding), not the "ordinary" case S5 alone describes. MA2 was revised to 3.5
months' rent (the middle of S8's elevated sub-range) — a real, sourced, scenario-matched figure, not
an unsupported number picked to hit a target margin.

**A second, independent defect surfaced and fixed during Tier 2 itself:**
- **P4 (twist integrity)** found the discussion Twist's mapping of "contract extension confirmed /
  not confirmed" onto the D2/D3 scenarios relied on an unstated convention (how long an extension
  would run). Fixed by adding **MA10**, stating explicitly that an extension, if granted, covers the
  remainder of the lease's 12-month term.
- **P6 (data decay)** found that S1/S2 (RentCafe's Boise, ID rent-trends page) is a live-updating
  dashboard that had moved on from its originally-cited $1,389/$1,536 figures (as of 2026-07-02) to
  $1,447/$1,601 (as of 2026-08-31) — a URL that resolves but no longer carries the recorded figure,
  which P6's own rule calls "worse [than a dead link], because nothing else in the pipeline would
  ever have noticed." Fixed by refreshing S1/S2 to the current figures and recomputing every value
  originally set as a percent/multiple of rent (MA1, MA2, MA3, MA4, MA9) at the same percent/multiple
  of the refreshed rent, preserving the case's stated proportional structure exactly.

Every change is recorded, with sources and dates, in `RESEARCH_LOG.md`, `case.json.sensitivity_note`,
`case.json.balance`, and `FACILITATOR.md`. No figure was fabricated, hidden, or reweighted to force a
target margin — each revised value is real, dated, and cited.

### Final numbers (current state)

| Scenario | The Cedarline | The Aldergate | Winner | Margin |
|---|---|---|---|---|
| Stay full term (D2) | $1,483.17/mo | $1,734.42/mo | Cedarline | 16.9% |
| Break at month 6 (D3) | $2,363.50/mo | $2,134.67/mo | Aldergate | 10.7% |

`case.json.margin_pct` / `balance.margin_pct` = **10.7** (the narrower, more binding of the two
scenario margins, per the established convention of reporting the tighter constraint against SPEC
§2's ~20% cap). Full detail in `balance.margin_pct_by_scenario`. The dilemma now genuinely flips
between scenarios, restoring the case's original design intent, with the break-scenario margin
landing inside the concept sheet's 8-12% target band.

**Remaining GAP (not a blocker):** the stay-full-term margin (16.9%) is wide relative to the 8-12%
target — that half of the discussion will lean one-sided toward Cedarline. Flagged in
`FACILITATOR.md`; this is an acceptable asymmetry since the case's dilemma lives in the *contrast*
between the two scenarios' winners, not in either scenario being individually close.

### Tier 1 — structural (21 checks), re-run after all fixes

PASS 20 · GAP 1 · FAIL 0 · BLOCKER 0. `sha256(case.md)` = `a6f77f1fa6883332e3c9170dec65e6f07a2b875e555d8a7f66d46ab8d227432b`.

- All 21 checks PASS except **T1-10** (GAP, pre-existing, unrelated to this remediation): `new_coverage[]`
  is empty; downgraded from BLOCKER to GAP under the 2026-08-17 reinforcement carve-out because
  `case.json.reinforcement_note` records that adjacent uncovered skills were genuinely checked and
  ruled out. Not touched by this run.
- T1-14 (continuity) re-verified clean after every FACILITATOR.md/case.json number was brought back
  into agreement following both remediation rounds.

### Tier 2 — simulated play (6 probes, as scoped for this case)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent (packet-only, no other files) chose Option B (The Aldergate) on a downside-protection/minimax rationale, reproduced D2/D3's arithmetic exactly ($1,483.17/$1,734.42 and $2,363.50/$2,134.67), named the metric it optimized (worst-case effective monthly cost, since expected cost is a near-wash), named a real counterargument, correctly identified MA2 as both the most sensitive assumption and the least-supported number, and named a legitimate appendix item it ignored (MA9). Reached a defensible position with correct arithmetic and a named metric — not the "right answer by the wrong route" failure mode. |
| P2 both-sides | **PASS** | A fresh subagent built real, numeric best-case sentences for both options directly from the case's own D2/D3 figures. Found Option A's case is the more fragile of the two (it collapses at "what happens if the contract does not extend?", since A's entire advantage lives in the stay-full-term branch) while B's position is a legitimate, harder-to-invalidate hedge — but neither side degenerates into a bare concession, and the "which side is weaker" finding matches the case's own intended asymmetry (contrast between scenarios), not a sign the balance test is a paper number. |
| P3 trap | **PASS** | Two independent fresh cold-reads (run before and after the final remediation) each proposed a candidate wrong path different from the guide's named trap (anchoring on the stay-full-term result; a divisor-confusion error in D3), then read FACILITATOR.md's "## The trap" section and, in both runs, independently concluded the guide's named trap (the sticker-price shortcut that happens to be correct in one scenario, reinforcing false confidence before it fails in the other) is the more dominant failure mode and the one the discussion's structure (Anchor 3, the Twist, Socratic Q5) is actually built to surface. |
| P4 twist | **PASS** (after one remediation round) | Initial fresh-subagent run correctly found the twist invalidates a real room position (criterion 1 PASS) but found the twist's mapping onto D2 vs. D3 depended on an unstated convention — how long a contract extension runs — which is a real BLOCKER-class finding per this probe's own rule. Fixed by adding **MA10** (an extension, if granted, covers the remainder of the 12-month lease term). A second fresh subagent, given the corrected case.md, re-derived both twist branches from the case's own appendices/MAs and confirmed both criteria now PASS with no remaining unstated convention. |
| P5 sensitivity | **PASS (disclosed)** | Mechanical ±50% sweep of all 5 `FLEX[]` dials in `sensitivity_model.py` (updated to the case's current figures). Two dials are genuinely unstable: `cedarline_termination_penalty` flips the verdict at -50% and breaks the SPEC §2 20% cap at +50%; `break_month` breaks the cap at -50%. Both are disclosed with a real, ≥20-character, categorized justification in `case.json.sensitivity_disclosure[]` (Category F — an invented apartment/an unknowable-in-advance contract outcome, not a researchable true value) — matching this project's disclosure-not-elimination convention (2026-08-13), the same pattern used in `cases/the-deferred-repair/case.json`. No undisclosed instability remains. |
| P6 data decay | **PASS** (after one remediation round) | Fetched all 8 cited URLs directly. S1/S2 (RentCafe) resolved but no longer carried the originally-cited figures — the live dashboard had moved from $1,389/$1,536 to $1,447/$1,601 — fixed by refreshing S1/S2 and recomputing every dependent MA (see above). S3 (Redfin), S4 (BLS), S5 and S8 (LeaseRunner, two distinct articles), S6 (HUD PDF, confirmed via `pdftotext` after WebFetch's PDF text-extraction failed), and S7 (Landing) all reachable with their recorded figures still verbatim present on the page. No dead links; no other drifted figures. |

Six probes, six recorded verdicts, 0 FAIL. `qa.state` set to `TIER2_PASS`.

### Tier 3 — human dry-run

NOT RUN. `case-publish` is licensed by this Tier 2 pass but was not executed — publish requires two
explicit human confirms per PIPELINE.md and was out of scope for this remediation run.
