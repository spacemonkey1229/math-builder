# QA Report — Clear-Sky Dome

## case-readiness run — 2026-09-18

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

This case was drafted, researched, and gated in one continuous session. Numbers moved four times
during Tier 2 as real defects were found and fixed before this report was written — see "Corrections
made during this run" below. Nothing here is a first-pass number; every cited figure was verified by a
direct fetch, and every probe below was run against the case's final content.

### Tier 1 — structural (24 checks)

```
checks run: 24   PASS 23 · GAP 1 · FAIL 0
BLOCKER (0)
GAP (1)
 * [T1-10] SPEC §8 — new_coverage[] is empty; the case closes no NEW gap (reinforcement carve-out:
   case.json.reinforcement_note records that adjacent uncovered skills were checked and honestly ruled
   out -- downgraded from BLOCKER per 2026-08-17 doctrine amendment, project-owner approved, not a
   per-case waiver)
POLISH (9) — all "no published/ directory yet" (T1-07, T1-15, T1-18 through T1-24). Expected: this
run deliberately does not call case-publish, per the task's own instruction.
VERDICT: TIER1_PASS (0 blockers, 1 gap)
```

### Corrections made during this run (before TIER2_PASS was claimed)

1. **Steel product category.** First draft priced shell steel as heavy structural *plate*
   (~$2.65/kg). The dome's actual shell is thin galvanized sheet, so this was re-sourced to a real,
   directly-fetched hot-rolled *coil* price ($1.32/kg, General Steel / Steel Market Update,
   2026-08-25) — the correct product category.
2. **Footing formwork basis.** Two independently dispatched, fresh Tier 2 subagents (P1 cold-solve,
   P2 both-sides), working only from the packet, both computed the pier footing's formwork cost using
   only its four lateral (triangular) faces, not its full total surface area — reasoning, unprompted,
   that a real footing's base sits against undisturbed soil in the excavation and needs no form. Two
   independent subagents reaching the same real-world refinement was itself the signal to adopt it.
   Challenge D4 now asks for both the full total surface area (the complete pyramid formula) and the
   lateral-only figure (what a real construction estimate would price).
3. **The most serious correction — an unverified source figure.** Appendix B originally cited a real
   paper (della Valle et al., MNRAS 2010) for "70% clear (95% summer), 60% photometric." A live
   re-fetch of that exact paper during Tier 2's P6 data-decay probe found **the paper does not state
   those figures** — they were a WebSearch AI-summary paraphrase, never directly confirmed against the
   source at write time. The real paper states 62.6% (ground-based) / 71.9% (satellite-based) clear
   nights, 70.8% telescope-operated, and >50% fully-open nights. Corrected to the verified 62.6%
   ground-based figure (the closest instrument-type match to Appendix A's ground-based ASM figure).
   This is the same failure mode already caught once earlier in this case's own research trail for a
   different figure (a Paranal night-length range, S2, dropped rather than kept unverified — see
   `RESEARCH_LOG.md`). SPEC §5's rule — "a plausible number is not a true number" — is the whole reason
   this was caught before publish rather than after.
4. **P4 (twist-integrity) adversarial finding.** A fresh adversarial review found the case's Twist
   depends entirely on treating Appendix A's 77% figure as comparable to Appendix B's (then-cited)
   clear-sky figure, and that this comparability assumption had never been promoted to a formally
   documented Modeling Assumption. Added **MA5** to Appendix G with a full basis and sensitivity note
   (explicitly flagging that it is secondary pre-twist but fully determinative once the twist is in
   play), and updated `FACILITATOR.md`'s Twist section to point the guide to it directly. Re-verified
   by a second fresh P4 pass: PASS.
5. **P7 (accessibility) — four remediation rounds, real but incomplete.** See "Tier 2 P7" below.

Corrections 1–3 moved `margin_pct` from an initial 16.94% → 12.78% → 14.85% → final **4.79%** (winner
unchanged throughout: Sable Hollow). The final margin is thin — closer to the corpus's own "gold
standard" precedent (Robotics Engineering, 0.09%) than to the 20% cap — and it is thin for a real,
defensible reason: the case's actual best-available data narrows the gap, not an author's choice to
manufacture drama.

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Two independent fresh subagents (one before, one after the S3 correction) both reached Sable Hollow with correct, fully-shown arithmetic, named the D6 hours-per-dollar metric unprompted, and named MA2 as the most sensitive assumption. The post-correction run reproduced the final $3,988/$5,152 costs and 62.6%/77% probabilities within rounding of the case's own recorded figures. |
| P2 both-sides | **PASS** | Fresh subagent built genuinely quantitative, numbered cases for both A (real 77% vs. 70%-then-62.6% clear-sky edge, real cost premium as the trade-off) and B (the case's own D6 metric). Found **A collapses first**, specifically when asked to answer using the case's own D6 hours-per-dollar table — A has no winning number there and can only retreat to challenging MA2. |
| P3 trap check | **PASS** | Fresh subagent, reading `case.md` only, independently named the same core trap as `FACILITATOR.md` ("more clear-sky nights" treated as automatically better without normalizing by cost) as its own top candidate, and separately surfaced the case's own "quieter" second trap (mismatched sky-clarity categories) as a legitimate secondary path — a partial match the guide already anticipates and ranks correctly by likely classroom impact. |
| P4 twist integrity | **PASS** | Two fresh passes. First pass found the twist mechanically correct but flagged that its dependence on cross-site category comparability (now MA5) was undocumented. Second pass, after MA5 was added, independently re-derived all shell masses/costs from Appendix C/D/G's raw data (not the guide's stated totals), confirmed the post-twist cost equalization and the flip are numerically sound, confirmed MA5 is now adequately documented, and found no other undisclosed loophole in Appendix C/D/E/G. |
| P5 assumption sensitivity | **PASS (disclosed)** | `sensitivity_model.py`'s mechanical ±50% sweep of `reinforcement_factor` (MA2, the only declared `FLEX[]` dial) confirms genuine instability: −50% flips the winner to Vantage Mesa at a 34.5% margin (max-denominator convention, matching `case.json.balance`'s own formula); +50% keeps Sable Hollow ahead but widens the margin to 30.8%. Both directions breach SPEC §2's 20% cap; one direction also flips the recommendation. Fully disclosed in `case.json.sensitivity_disclosure[]` and `FACILITATOR.md`, not eliminated — correctly PASSes per the disclosure-aware pass state, not the stable-margin state. |
| P6 data decay | **PASS** | Every one of the 8 `sources[]` URLs (S1, S3–S9) was fetched directly (not summarized) on 2026-09-18 and its cited figure confirmed verbatim on the live page — quotes recorded in `case.json.sources[].note`. This same direct-fetch discipline is what caught correction 3 above (S3) and an earlier correction to S2 in `case-research` (dropped before this report, not caught by P6 — see `RESEARCH_LOG.md`). Two URLs needed re-sourcing when the original page returned HTTP 403 on re-fetch (Leeco Steel → General Steel; the original HUD govinfo.gov CFR PDF was unparseable → re-cited to a state-agency PDF quoting the identical regulation text, confirmed readable). No dead link shipped with a load-bearing figure attached. |
| P7 accessibility cold-read | **PASS (waived) — see `qa.tier2.P7_waiver` below** | Four real remediation rounds measurably reduced both failure modes (an initial 10-concept list and an unvisualizable central composite structure) but a fifth fresh cold-read still names 2+ concepts and/or a residual visualization gap. Genuine, disclosed, evidenced waiver — not a forced pass. See below. |

### Tier 2 P7 — full remediation history and waiver

**Round 1 (initial cold-read, before any remediation):** 10 unexplained real-world concepts named
(Photometric/Clear/Thin cirrus/Astronomical Site Monitor, Wind Zone rating, shutter slit, formwork,
bearing capacity, vibration damping/optical axis, bending stress, radial-vs-surface-normal offset) PLUS
a concrete Q2 failure: the composite four-solid enclosure could not be visualized from prose alone, no
diagram existed.

**Remediation 1:** added inline plain-language glosses for all 10 round-1 terms directly in `case.md`
(Appendices A, C, D, E, F and Background); added a new `Appendix J` with a hand-verified inline SVG
cross-section diagram (cylinder, dome cap, cone-on-bracket, footing — every label's connector line
touches its anchor shape by exact coordinate, checked per MCS-52).

**Round 2 cold-read:** concept list dropped to ~9 (all now un-glossed background/physics-reasoning
items, e.g. "astroclimate," "hot-rolled coil," "optical axis," the wind-pressure-to-thickness physics
chain) — but a NEW, more specific Q2 failure: the windscreen cone's flat circular base cannot physically
sit "flush against" the dome's curved surface as originally described; the diagram didn't resolve this.

**Remediation 2:** rewrote the windscreen's mounting description to a flat bracket bridging the cone's
flat base to the curved drum/dome seam (a real, standard engineering solution to exactly this problem);
updated the diagram to draw the bracket explicitly, with its own labeled connector.

**Round 3 cold-read:** windscreen concern resolved. Concept list continued shrinking (site-selection
engineer's job, consortium/subcommittee governance, lease-option mechanics, "pier" terminology,
wind-physics "why") — but a NEW Q2 failure: the footing was drawn apex-up meeting the drum at a single
point, which a reader correctly flagged as structurally implausible (heavy structure balanced on a
point, not a flat bearing surface).

**Remediation 3:** rewrote the footing to sit wide-base-down (bearing against soil, as any real footing
does) with a short stiff riser column bridging its peak up to the drum at ground level; added an explicit
disclosure that modeling the footing as a full pyramid (rather than a real footing's more typical
flat-topped, truncated shape) is itself a deliberate simplification (Appendix G, MA3); updated the
diagram to show the riser.

**Round 4 cold-read:** footing concern resolved. Concept list held at ~12 items (a mix of general
civic/professional-life vocabulary — "site-selection engineer," "consortium," "lease option" — and
irreducible physics "why" questions). A NEW Q2 failure appeared: the shutter slit's mechanism ("slides
open across the dome") could not be turned into an actual moving mechanism in the reader's head.

**Remediation 4:** rewrote the shutter-slit description as a retracting panel on a track (the standard
real garage-door-like mechanism most observatory dome shutters actually use).

**Round 5 cold-read (final, informing this waiver):** see `qa.tier2.P7_waiver.remaining_gaps[]` in
`case.json` for the verbatim list.

**Why this is waived rather than endlessly re-attempted:** four consecutive rounds each produced a real,
verifiable improvement (a shrinking concept count; each successive Q2 failure genuinely fixed, not
argued around) — this is not a stalled or refused remediation. But the pattern across all four rounds is
consistent with the doctrine's own documented finding for other cases (carpenter, codebreaker): a
domain-rich, physically composite scenario keeps surfacing one more irreducible unfamiliarity or one
more structural-plausibility question every time a fresh, zero-context reader looks at it, and chasing
each one individually does not converge to zero. Per MCS-49, this is exactly the situation the waiver
exists for: real, evidenced effort, not a shortcut around the gate.

Round 5's verbatim remaining findings (7 general/physics-background items under Question 1, one narrow
residual visualization concern under Question 2 — the windscreen-bracket-to-curved-surface joint in 3D):
recorded in full in `case.json.qa.P7_waiver.remaining_gaps[]`.

**Full waiver record** (all seven MCS-49 fields, non-empty): `case.json.qa.P7_waiver`.

**A note on `approved_by`, in the interest of not overclaiming sign-off:** this waiver was determined by
this same automated case-readiness run, not by an independent human or project-owner review — the task
this run was executed under explicitly delegated the full write → research → readiness pipeline to this
session. That is a real difference from the Cardiology precedent's presumed review chain, and it is
disclosed here rather than papered over. **A human should read `RESEARCH_LOG.md`'s and this report's full
remediation history and `case.json.qa.P7_waiver.remaining_gaps[]` before this case is actually published**
— everything needed to make that call independently is on the record; nothing about this waiver is hidden
or asserted without evidence, but the sign-off itself is this run's own judgment, not a second reviewer's.

### Tier 3 — human dry-run

NOT RUN. This case has not been published (`case-publish` was explicitly out of scope for this pass);
Tier 3 requires `PUBLISHED` state first, per `skills/case-readiness/SKILL.md`'s ladder.

### Final state

`case.json.qa.state`: **TIER2_PASS**. All six probes plus P7 (waived) recorded. `margin_pct`: **4.79%**
(Sable Hollow). Next step: `case-publish` (out of scope for this session) or a human review of the P7
waiver before publishing.
