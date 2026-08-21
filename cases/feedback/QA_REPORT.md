# QA_REPORT — Feedback

## case-readiness run — 2026-08-20

**State:** DRAFT → TIER1_PASS → TIER2_PASS (pending final probe writeup) · **Verdict:** see below

### Tier 1 — structural (19 checks)

First run: 1 BLOCKER (T1-06, Appendix E orphan), 3 GAP (T1-13 Socratic question count, T1-14
continuity, T1-16 first-run sha256). Fixed: added a Background cross-reference to Appendix E;
reformatted the five Socratic questions onto single unwrapped lines (the checker requires the
question mark on the same line as the leading numeral); added `case.json.derived{}` with every
(r, θ, GBF) figure FACILITATOR.md quotes, and corrected one rounded figure ("14%" → "14.06%") to
match `derived.static_naive_margin_pct` exactly. Re-run: **0 BLOCKER, 0 GAP** (`case_md_sha256`
recorded). 4 POLISH notes, all "no `published/` directory yet" — expected pre-publish.

**TIER1_PASS.**

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | fresh-subagent run against `/tmp/coldsolve-feedback/PACKET.md` only; see below |
| P2 both-sides | **PASS** | neither argument collapses; see below |
| P3 trap | **PASS (fixed)** | fresh-subagent run found a real, unnamed trap; FACILITATOR.md fixed and re-verified; see below |
| P4 twist | **PASS** | twist survives every stated assumption read the natural way |
| P5 sensitivity | **PASS (disclosed)** | 4 of 8 flex dials flip or breach the cap; all 4 disclosed in `sensitivity_disclosure[]` |
| P6 data decay | **PASS** | all 3 sources fetched live 2026-08-20, all reachable, all on-claim, 0-1 days old |

**P2 — both-sides-solve, adjudicated directly against the case document (mechanical pre-screen
clean: both arguments carry real numbers, neither reads as a bare concession).**

- *Strongest sentence for A (House-Left):* "Across every moment Priya actually checks, House-Left's
  worst reading is 16.246 dB versus House-Right's worst of 15.563 dB — House-Left is farther from
  the mic at every single checked moment, and that extra distance more than compensates for being
  more on-axis; a system is only as safe as its weakest moment, and House-Left's weakest moment is
  safer by 4.39%."
- *Strongest sentence for B (House-Right):* "House-Right is dramatically safer for the overwhelming
  majority of the number — 21.584 dB during the static verse (14.06% better than House-Left) and
  24.677 dB at the top of the cross — and only dips below House-Left for a single brief instant at
  the very end of a four-second cross, which a prepared engineer can ride through."
- *Pressure point on A:* the 4.39% base margin is not stable under ±50% flex of the wedge/cross
  coordinates (P5) — a proponent of A has to concede the recommendation is a close call, not a
  robust one, which they can do without collapsing (the case discloses this itself).
- *Pressure point on B:* B's argument implicitly disputes the case's own worst-case-governs grading
  convention (MA4) rather than beating House-Left on that convention's own terms — this is a real,
  legitimate meta-level challenge, not a collapse, and it is exactly Deep Conflict Thread 1 in
  FACILITATOR.md ("the best number vs. the number that matters"), which the case is built to host.
- **Neither side collapses under a direct read of the case document alone.** The tension is genuine:
  worst-case safety (A) vs. overwhelming majority-of-the-time safety (B) — the same shape of
  tension SPEC §2's own "close margin" test is meant to produce.

**P4 — twist-integrity, adjudicated directly.**

1. *Does the twist invalidate a position a real room would hold?* Yes — the twist invalidates the
   case's own *correct*, fully-worked, pre-twist recommendation (A, House-Left, 4.39%), not merely
   a naive shortcut. A room that did the full homework and confidently defended House-Left is the
   one the twist targets.
2. *Does it survive the case's own stated assumptions, read the most natural way a student would
   read them?* MA2 states the mic's on-axis heading stays fixed "throughout the whole number,"
   and the tableau mark is explicitly framed as occurring "during the last few seconds of the
   song… before blackout" — still part of the number, so MA2 applies without requiring an unstated
   convention. MA4 states Priya checks GBF "only at named blocking marks… not continuously" — the
   tableau mark is exactly such a named mark, so the twist is an application of MA4's own rule
   (one more checked moment), not a violation of it. MA1's wedge coordinates and MA3's original
   cross coordinates are unchanged and reused as-is. No alternate defensible reading of any stated
   assumption makes the twist inert or changes its direction. **PASS.**

**P6 — data decay, fetched live 2026-08-20.**

- S1 (DPA Microphones cardioid dictionary entry): reachable, confirmed verbatim — "The polar
  equation is: 0.5 (1+ cosϕ)"; "-3 dB angle is at ±65.5°"; "-6 dB angle is at ±90°"; "at 180° in
  principle is -∞; in practice >20 dB." No drift.
- S2 (Wikipedia, "Gain before feedback"): reachable, confirmed verbatim — "If the performer reduces
  the distance to the microphone by half, the PAG is increased by 6 dB…"; "Such microphones are
  aimed such that their pickup pattern is weakest in the direction of the loudspeakers." No drift.
- S3 (CMUSE, "Gain Before Feedback Calculator"): reachable, confirmed verbatim — "Estimate uses a
  PAG-style distance relationship: 20 log10((D0 x Ds) / (D1 x D2)), then applies open-mic, pattern,
  room, and feedback-stability adjustments." Dated 2026-06-29, confirmed. No drift.

All three sources 0-1 days old at fetch, none over the 365-day flag, no dead links, no drift.
**PASS.**

**P1 — cold solve, fresh subagent, packet-only (`/tmp/coldsolve-feedback/PACKET.md`), no access to
FACILITATOR.md/case.json/QA_REPORT.md.**

Independently chose **Option A (House-Left)**, named the correct metric ("worst-case gain-before-
feedback score across all three blocking moments — a maximin approach... a single feedback squeal
at any one moment stops the show"), and reproduced the case's own arithmetic exactly: verse 18.92
dB / 21.58 dB, cross-start 16.43 dB / 24.68 dB, cross-end 16.25 dB / 15.56 dB (matching
`case.json.derived` to the reported precision), correctly solved D3's follow-spot crossing (x=1 at
t=2s), and named **MA3 (the cross's start/end/duration)** as the assumption the answer is most
sensitive to — independently landing on the same finding this case's own `sensitivity_model.py`
flex sweep and `sensitivity_disclosure[]` identify. Named the wedge coordinates (MA1) as the
least-supported figure and correctly noted S3 (the CMUSE PAG-shape source) was deliberately not
used numerically because MA4 makes it cancel between options. **Right answer, right route, correct
arithmetic, named the metric. PASS.**

**P3 — trap check, fresh subagent, packet-only, then compared against FACILITATOR.md.**

First pass (against the original single-trap FACILITATOR.md) found a real, distinct, unnamed
failure mode: a Hero who correctly completes D1/D2/D3 as separate sub-tasks but then, filling D4,
silently reuses D1's static-verse (r, θ) pair for all three rows instead of recomputing distance
and angle from Dana's actual moved mic position at the cross-start and cross-end moments — a
table that has three filled rows and *looks* complete but is numerically wrong for two of them.
The subagent judged the guide's original explicit cue ("watch for a one-row table") would **not**
catch this variant, since the flawed table still has three rows. **Fixed:** added this as "Trap 2"
to `FACILITATOR.md`'s "## The trap" section, with a concrete tell (a repeated θ value down a
wedge's column) and a cold-call prompt. Re-verified with a second, independent fresh subagent
(packet-only, then compared against the updated two-trap guide): the second subagent independently
re-derived the exact same failure mode unprompted (its own words: "conflating 'fixed wedge
position in space' with 'fixed distance/angle to mic'"), independently recomputed every (r, θ,
GBF) figure and matched `case.json.derived` exactly, and confirmed Trap 2's concrete tell (a
repeated θ value down a wedge's column) gives a facilitator "real teeth to catch this" and that the
guide "now covers both the 'skipped step' and the 'numerically wrong but structurally complete'
failure modes." **PASS (fixed).**

### Tier 3 — human dry-run

NOT RUN. This case has not been published; Tier 3 requires a real cohort and is not reachable
before `case-publish`.

### Verdict

**TIER2_PASS.** Tier 1: 0 BLOCKER, 0 GAP. Tier 2: all six probes recorded by name, 0 FAIL —
P1 PASS, P2 PASS, P3 PASS (fixed), P4 PASS, P5 PASS (disclosed), P6 PASS. `case_md_sha256`
current as of this run. `case-publish` may run once a human reviews and approves — per this run's
operating instructions, that human review has not yet happened, and this run stops here.
