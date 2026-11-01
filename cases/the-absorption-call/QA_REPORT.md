# QA Report — The Absorption Call

**state: TIER2_PASS (P7 disclosed via MCS-49 waiver — see below; not a clean mechanical pass)**
**case.md sha256:** `64d61163bc0faeb7fbf60ae68fc9ae2698b64f958f11af20bd734ca919559e25`
**Run on:** 2026-09-18

## Tier 1 — Structural

`python3 skills/case-readiness/scripts/tier1_structural.py --case the-absorption-call`

**VERDICT: TIER1_PASS — 0 BLOCKERs, 4 GAPs (all recorded and waived below), 3 POLISH notes.**

Recorded GAP waivers (human/orchestrator confirm, this run):

- **T1-10** — `new_coverage[]` is empty under the documented `reinforcement_note` carve-out in
  `case.json`. The approved concept sheet (`cases/_concepts/CONCEPTS_music-acoustics_2026-09-12.md`,
  C2) named `measurement-volume` (spine `n=2` at scoring time) as this case's new-coverage claim,
  reasoning from `gap_queue.json`'s "thin skill" framing. Re-verifying against the actual gate
  (`tier1_structural.py` T1-10) at write time showed the spine now records `covered_by:
  ['Nuclear Waste', 'Cold Chain']` — two sibling cases in this same batch closed the gap first,
  sometime between the concept's scoring pass and this case's write pass. Checked and ruled out
  before falling back to the carve-out: no skill in the Measurement or Geometry domains currently
  shows `n == 0` in the spine. **Waived** — this is an honest, documented stale-concept finding,
  not a defect in this case's own sourcing or math. See `RESEARCH_LOG.md` and `LEARNING_GOALS.md`
  for the full account.
- **T1-14 / T1-15** — a single derived arithmetic figure (`0.0929`, the exact ft²→m² conversion
  factor named in FACILITATOR.md's trap explanation) doesn't trace back to a literal token in
  `case.md`/`case.json`. It is correct, harmless, guide-only color, not a case datum. **Waived.**
- **T1-16** — hash-currency GAP is expected on a first QA run; resolved by this report itself.
- **T1-18** — a stray `0.1` in the interactive HTML's markup (a CSS/notebook step value, not case
  data) doesn't trace to `case.md`/`case.json`'s number universe. **Waived** — same class of
  false positive T1-19/T1-18's own documentation names as an accepted CSS/SVG-decimal exception.

POLISH notes (informational, no waiver needed): T1-07 (legacy-format parser note, not applicable —
final appendix already machine-generated from spine labels), T1-20 (no photographic image; the
case ships two hand-drawn SVG diagrams instead, which the note itself says is an acceptable
substitute), T1-24 (a coordinate-heuristic false positive on one decorative arrow in the
absorptive-vs-diffusive SVG figure — confirmed correct by direct DOM inspection and live-browser
JS execution; see the live browser audit section below).

## Tier 2 — Simulated Play

`python3 skills/case-readiness/scripts/tier2_probes.py --case the-absorption-call`

| # | Probe | Verdict |
|---|---|---|
| P1 | cold-solve | **PASS** |
| P2 | both-sides-solve | **PASS** |
| P3 | trap-check | **PASS** (after remediation — see below) |
| P4 | twist-integrity | **PASS** |
| P5 | assumption-sensitivity | **PASS (disclosed)** |
| P6 | data-decay | **PASS** (fetched and confirmed live, this session) |
| P7 | accessibility-cold-read | **FAIL (waived — MCS-49, `case.json.qa.tier2.P7_waiver`)** |

**0 NOT RUN across all seven probes.** P7 is the one probe that did not reach a clean mechanical
PASS after 13 genuinely-fresh remediation rounds; it is disclosed and waived, not hidden — see
below and `case.json.qa.tier2.P7_waiver` for the full evidentiary record (reason, round count,
remaining gap, approver, date) the MCS-49 waiver mechanism requires.

### P1 — cold solve

Dispatched a genuinely fresh subagent (no context beyond the packet at
`/tmp/coldsolve-the-absorption-call/PACKET.md`). It chose Option A, named the correct primary
metric (closeness of RT60 to the target for the room's dominant use), reproduced the full
arithmetic correctly (V ≈ 543.68 m³, baseline RT60 ≈ 3.00 s, RT60_A ≈ 1.00 s, RT60_B ≈ 1.63 s),
gave a real counter-argument, correctly named MA2 as the most sensitive assumption, and correctly
identified MA2's α as the least-supported number in the case. Reached the answer by the right
route — PASS.

### P2 — both-sides solve

A second fresh subagent built the strongest case for each option independently. Both sides are
genuinely defensible; it found Option B collapses first under cross-examination (its RT60 sits
outside the *entire* sourced 0.9–1.2 s amplified-target band, even at the best end of MA2's
disclosed range) while Option A's own weak point (missing the unsourced 1.6 s music target) is
softer because that target is itself explicitly challengeable. This is a legitimate, expected
asymmetry — the pass criterion is "can a competent student defend each side," not "do both sides
collapse equally," and both do. PASS.

### P3 — trap check

A third fresh subagent predicted the most plausible wrong path *before* seeing FACILITATOR.md: a
linear-vs-squared unit-conversion error (applying the 0.3048 ft→m factor directly to *areas*
instead of squaring it to 0.0929). This did **not** match the trap FACILITATOR.md originally
named (a coefficient-size comparison trap). Per the probe's own pass rule — "a trap the guide has
not anticipated is a Tier 2 FAIL even if the case is otherwise sound" — **this was remediated**:
FACILITATOR.md now names the unit-conversion error as the **primary** trap (mechanical, catches it
first) and the original coefficient-comparison trap as the **secondary** trap (conceptual, catches
whoever gets past the first one). Re-verified against the sourced physics: the error really is
internally consistent (every downstream figure scales by the same ~3.3x factor) and really would
hide behind the $50,000 budget check exactly as the subagent predicted. PASS after remediation.

### P4 — twist integrity

A fourth fresh subagent adversarially re-read FACILITATOR.md's twist against the case's own stated
numbers. Finding: the twist ("the calendar split is now roughly even") genuinely invalidates one
real position (using calendar-majority as a tiebreaker) without making any position obviously
correct, and it survives a sequential reading — no number in the case is actually derived from
calendar share, so there's no hidden order-of-operations bug the way Cold Chain's original twist
had. The subagent noted the twist is a values/framing twist, not a data twist, and FACILITATOR.md
already says so explicitly ("the Sabine calculation was never in question; the weighting of which
target to chase was") — the case is self-aware about the twist's own nature rather than
overclaiming it changes the math. PASS.

### P5 — assumption sensitivity

`sensitivity_model.py` is a direct PARAMS/FLEX/`evaluate()`/`evaluate_twist()` port matching
`sensitivity_model.py` (Python) and the HTML's embedded JS port exactly (cross-checked live in a
real browser — identical outputs to 4 decimal places). FLEX = `["alpha_diffusive",
"target_music"]`. Base-case margin: 2.3% (well under SPEC §2's 20% cap). Sweeping both dials ±50%
flips which option scores marginally higher in all 4 rows and breaks the 20% cap in 2 of 4.
**Disclosed, not eliminated**: `case.json.sensitivity_disclosure[]` records both params as
Category X (a documented good-faith estimate standing in for a real citation that does not
publicly exist — matches `RESEARCH_LOG.md`'s own NOT FOUND findings for both). PASS (disclosed)
per `tier2_probes.py`'s own disclosure-aware pass state.

### P6 — data decay

The QA sandbox has no outbound network, so this probe is formally DELEGATED by the script — but
every one of the 6 sources was actually fetched live in this session (2026-09-18) and confirmed to
still carry its cited figure:

- S1 (acoustics-engineering.com/html/sabin.html) — confirmed live, states `T = 0.161 V/A`.
- S2 (sengpielaudio.com/calculator-RT60.htm) — confirmed live, states 0.161 (m) / 0.049 (ft).
- S3 (sengpielaudio.com/calculator-RT60Coeff.htm) — confirmed live, 0.04/0.09/0.07 at 1000 Hz.
- S4 (gikacoustics.com/product/242-acoustic-art-panels-3-625-inch/) — confirmed live, "NRC: 1.05".
- S5 (commercial-acoustics.com/sound-advice/rt60-chart/) — confirmed live, "Theater (Legitimate
  Stage)" 0.9–1.2 s.
- S6 (nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors) —
  confirmed live, "1 ft = 3.048 E-01 m".

All 6/6 reachable, all 6/6 still carry their recorded value. PASS.

### P7 — accessibility cold-read — FAIL, waived (MCS-49)

Thirteen rounds of dispatch-and-remediate, each a genuinely fresh subagent with zero case context,
reading only the machine-built text packet (`published/*.html` stripped of `<script>`/`<style>`,
per `build_html_cold_read_packet()`):

| Round | Q1 (unexplained real-world concepts) | Q2 (unpicturable central object) | What changed |
|---|---|---|---|
| 1 | 7 named | FAIL — diffusor geometry unpictured | baseline |
| 2 | 4 named | FAIL | added first shape description |
| 3 | 3 named | FAIL | added static "A Few Terms, Plainly" section — packet-builder strips `<script>`, so JS-hover-only glossary content never reaches the cold-read text |
| 4 | 4 named | FAIL — found a real inconsistency: two competing shape metaphors (foil vs. blocks) | replaced under-specified "columns of different depths" with a fully-specified object |
| 5 | 0 named | FAIL — competing metaphors persisted | — |
| 6 | 0 named | FAIL — leftover "foil" mechanism analogy still read as a competing shape | removed foil metaphor everywhere |
| 7 | 4 named (softened to physics-depth curiosities) | FAIL | stated scattering as a given, cited fact instead of an under-specified causal claim |
| 8 | 0 named | FAIL — found NRC>1 internal contradiction (defined "0 to 1," then used 1.05) | — |
| 9 | 0 named | FAIL — found a genuine geometric error: "ankle-high to waist-high" implied vertical fence-board height, not depth-into-the-wall, for a wall-mounted panel | replaced "fence of boards" with "ice-cube tray of pockets at different depths" (correct orientation) |
| 10 | 3 named (mid-band, NRC>1, "why does scattering happen") | FAIL — object shape now explicitly confirmed pictured ("I can picture a bar chart of wooden blocks... and separately I can picture crumpled foil") but still asks for the underlying wave mechanism | — |
| 11 | 0 named | FAIL — same wave-mechanism ask, now against the corrected ice-cube-tray shape | reframed the mechanism as a given fact, same treatment as Sabine's constant |
| 12 | 0 named | FAIL — found the actual quoted leak: a `STORY_GLOSSARY` hover-def and an SVG `<desc>`/figcaption still asserted "scatters... in many directions," which the packet-builder inlines into cold-read text at first mention | neutralized every remaining scattering-outcome sentence (glossary def, SVG desc, figcaption, ASCII-diagram caption) to plain fact statements |
| 13 (final) | **0-2 named, explicitly caveated non-blocking** (source-citation format, confidence-grading methodology) | **still FAIL** — final subagent explicitly confirms the shape is now clearly pictured and states the sole remaining objection is that the case deliberately does not explain *why* the shape scatters sound, which it does on purpose (T2 MS scope) | see waiver below |

**Round-13 evidence that this is a structural probe limit, not a content defect:** the final
subagent's own words — *"I can picture an ice-cube tray as an object... What I cannot picture is
the mechanism... The document itself concedes this is unpicturable-by-design, not a gap in my
reading."* The case explicitly, deliberately treats the diffusor's scattering behavior as a given,
cited fact (Appendix B, MA2) — the same treatment already given to Sabine's constant (0.161) and
to "absorption converts to heat," neither of which ever tripped Q2 in any round. Q2's literal test
("is there something central you cannot picture, even though the words are familiar?") cannot
distinguish *a poorly-described object* from *a clearly-described object whose underlying physics
was deliberately, appropriately left unexplained* — both produce a "yes." `build_html_cold_read_packet()`
(`tier2_probes.py` ~line 571) strips all `<script>`/`<style>`, so no diagram's actual pixels ever
reach this probe's text-only channel regardless of how carefully it is drawn or described — this
was independently verified by finding and fixing three *literal* leaked mechanism-assertion
sentences that had escaped the SVG's own `<desc>`/`<title>`/`<figcaption>` and the JS glossary
object (round 12), which measurably helped, and by testing the fully-opposite framing (round 7:
assert the mechanism plainly; round 11: state it as a pure given fact) — both triggered Q2, just
with different wording, confirming further prose iteration was not converging.

**Real content defects this process found and fixed along the way (genuine value, independent of
the waiver):** (a) round 4 — inconsistent shape metaphors; (b) round 8 — an NRC-can-exceed-1
statement that contradicted its own "0 to 1" definition three sentences earlier; (c) round 9 — a
literal geometric orientation error (describing a wall-mounted panel's protrusion depth using
vertical "height" language); (d) via P3 (trap-check, see above) — a mismatched primary trap. All
four are fixed in the shipped `case.md`/`published/*.html`.

**Waiver.** Per MCS-49, `case.json.qa.tier2.P7` is recorded honestly as `"FAIL"`, and
`case.json.qa.tier2.P7_waiver` carries the full evidentiary record (13 remediation rounds, the
specific remaining gap, and the reasoning above) required for a disclosed FAIL to count toward
`TIER2_PASS`. The cold-read transcripts above are the record, not hidden.

**Structural note for future authors:** `build_html_cold_read_packet()` (`tier2_probes.py` line
~571) strips all `<script>`/`<style>` content, so a diagram's pixels — however carefully drawn —
never reach the cold-read subagent; only its `<title>`/`<desc>`/surrounding prose do. A
diagram-dependent explanation that leans on "see the sketch" will read as insufficient to a
text-only reader regardless of the sketch's actual quality. The fix that worked here was making
the *prose* fully self-sufficient (a complete, single, consistent physical description) rather
than treating the diagram as load-bearing for comprehension.

## Live browser audit

Performed after the interactive HTML was built (see `case-publish` section below): opened the
built file via a local HTTP server (a `file://` static preview does not execute this file's JS —
confirmed and worked around), exercised every JS entry point directly (`evaluate()`,
`evaluate_twist()`, `checkVolume()`, `checkBaseline()`, `checkOptions()`, the α slider at its 0.10
and 1.00 bounds, the dilemma picker, the twist reveal/apply toggle, CSV button wiring) via
`javascript_tool`, and confirmed zero console errors. `evaluate()`'s live output
(`{"A": 0.9546..., "B": 0.9762..., rtA: 1.0023, rtB: 1.6380}`) matches `sensitivity_model.py`'s
Python output to 4 decimal places, confirming the JS port is a real port, not a hand-derived
parallel implementation (per `INTERACTIVE_HTML_CONTRACT.md §2`'s own warning about Cold Chain's
drift bug). Both SVG diagrams render with the expected shape counts (11 shapes in the
absorptive-vs-diffusive cross-section; 81 in the rear-wall panel grid). T1-24's flagged "dangling
connector" is a static-file coordinate heuristic that cannot see the JS-injected panel/well
rectangles; confirmed correct in the live DOM.

## Sensitivity model

`sensitivity_model.py` ships, exposes `PARAMS`/`FLEX`/`evaluate()`/`evaluate_twist()` per contract,
and its FLEX sweep result is recorded and disclosed above (P5).
