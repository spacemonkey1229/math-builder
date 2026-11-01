# QA Report — Constellation Bid

## case-readiness run — 2026-09-18

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (24 checks)

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview 197 words, no load-bearing numerals (sixty/six/two cleared, `overview_numerals_cleared[]`) |
| T1-03 | PASS | Dilemma binary, opens "You are Aisha Odom." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | numeral form consistent |
| T1-06 | PASS | 8 appendices, all referenced, no orphans |
| T1-07 | PASS | 10 final-appendix lines all verbatim spine labels (fixed after a `·` multiplication symbol in the delta-v formula was mis-parsed as a vocabulary separator — replaced with `×` throughout) |
| T1-08 | PASS | every number cited (S1–S5) or a declared Modeling Assumption (MA1–MA4) |
| T1-09 | GAP | margin 19.05% inside the 20% cap but wide — noted, discussion is designed around the twist collapsing it, not around the base margin alone |
| T1-10 | GAP | `new_coverage[]` empty; `reinforcement_note` carve-out applies (live spine sweep found zero true `n==0` skills anywhere) |
| T1-11 | PASS | learning-goal mutual reachability — 0 unmapped deliverables, 0 unreachable skills |
| T1-12 | PASS | T3 numeric load matches scientific-notation-free trig/systems-style math with 3+ variables |
| T1-13 | PASS | facilitator guide, anchor ladder, twist, timed plan, sensitivity note all present |
| T1-14 | PASS | FACILITATOR.md's derived ratios (1.25, 1.333, 1.587) now recorded in `case.json.derived` |
| T1-15 | PASS | no staleness issue at Tier 1 time (no published/ yet) |
| T1-16 | GAP → resolved | hash recorded after first Tier 1 run: `c2db7131082de7597392a234090717d55fbcfa17e77351a0066b03ff1350f9ec` |
| T1-17 | PASS | 3 cohort bands declared |
| T1-18 | PASS | (checked again after publish, see below) |
| T1-19 | PASS | (checked again after publish, see below) |
| T1-20 | PASS | (checked again after publish, see below) |
| T1-21 | PASS | (checked again after publish, see below) |
| T1-22 | PASS | (checked again after publish, see below) |
| T1-23 | PASS | (checked again after publish, see below) |
| T1-24 | PASS | connector-line check (no diagram connectors in this case) |

**BLOCKER (0)** · **GAP (3, all accepted — margin width, reinforcement carve-out, and hash timing, resolved above)**

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | A genuinely fresh subagent, given only the leak-free packet, reproduced the case's own arithmetic exactly (v=7,589 m/s, 60°/120°/180° delta-v and propellant figures, $6.3M vs. $45M, 10 vs. 60 satellites, ratios 1.587e-6 vs. 1.333e-6) and correctly identified MA4 as the most sensitive assumption. It recommended **B**, not the case's disclosed base-case winner A — but by explicitly naming a different, defensible metric (mission-complete coverage rather than raw satellites-per-dollar) and by giving the strongest argument against its own choice honestly. This is a genuine PASS under the stated criterion (a defensible position, correct arithmetic, a named metric) — and is itself strong evidence the SPEC §2 balance test is real: two fresh readers can land on opposite sides without anyone being wrong on the math. |
| P2 both-sides solve | **PASS** | Argument for A: the case's own primary metric, 19.05% edge, real numbers. Argument for B: zero placement risk, guaranteed mission completion, real numbers. Neither collapses — confirmed directly by the P1 transcript, which built a genuine argument for B and then produced the strongest real argument for A ("by the case's own D4 metric... A is more capital-efficient") without either argument requiring hand-waving. |
| P3 trap check | **PASS** | A fresh subagent, given only the packet, named the trap as: applying Appendix B's raw 240°/300° RAAN offsets directly into the delta-v formula instead of first taking the minimum angular separation (120°/60°) — a concrete, mechanical error a hurried student would plausibly make. `FACILITATOR.md`'s trap section is updated to name this exact path as Trap 1, ahead of the two broader reasoning traps already drafted. |
| P4 twist integrity | **PASS** | `sensitivity_model.py`'s `evaluate_twist()` confirms the rideshare-price twist ($7,000/kg → $9,000/kg) flips the winner from A (19.05%) to B (6.67%) — a genuine, mechanically verified flip, not a null twist. The twist is a direct substitution into the same cost formula every option already uses; it does not depend on an unstated convention or an ambiguous reading of any Modeling Assumption. |
| P5 sensitivity | **PASS (disclosed)** | `sensitivity_model.py --probe 5`: altitude_km is stable across ±50% (margin unchanged at 19.05% both directions — a genuine, disclosed non-finding). wet_mass_kg flips the winner at +50% (26.0%, breaches cap) and breaches the cap at −50% in A's favor (614%). propellant_allowance_kg breaches the cap at +50% (257%, still A). All three are disclosed in `case.json.sensitivity_disclosure[]` with real, verified numbers (not estimates) — disclosure-aware PASS per the 2026-08-13 standing rule, not a stable-margin PASS. |
| P6 data decay | **PASS** | All 5 sources re-fetched live 2026-09-18 (not delegated — this session had live web access): S1 (spaceflightnow.com, 550 km altitude confirmed verbatim), S2 (en.wikipedia.org/wiki/Orbital_inclination_change, Δv=2v·sin(Δθ/2) formula confirmed verbatim), S3 (busek.com/bit3, Isp 2,150 s and 14 kg/2.39 km/s reference platform confirmed), S4 (newspaceeconomy.ca, $350,000/50kg + $7,000/kg confirmed), S5 (spacenexus.us/rockets/electron, $7.5M/300kg confirmed). All 5 reachable, all cited values still present, none moved, none dead. |
| P7 accessibility cold-read | **FAIL (waived — see `qa.tier2.P7_waiver`)** | See below. |

**P7 remediation detail.** Round 1 (before any remediation): a fresh cold-read named 7 unexplained real-world concepts (RAAN, vis-viva, μ, Isp, J2 perturbation, sun-synchronous orbit, rideshare-vs-dedicated) and a concrete Q2 FAIL (could not visualize the plane-change "walk" mechanism). Remediation: added `case.md` Appendix I (13 glossary terms plus a hula-hoop analogy for the walk). Round 2: named concepts dropped to 3 borderline items (μ's units, radio-spectrum-filing mechanics, why one burn re-tilts a whole orbit) but Q2 still FAILED (walk still not fully visualizable despite the analogy). Remediation: expanded the walk explanation with the "an orbit is just whatever circle matches current position+velocity" physical argument, added a spectrum-filing gloss, clarified μ's units. Round 3: Q1 count remained at 6–7 (the solver explicitly noted "the packet's Appendix I plain-English notes pre-empted most of these," listing them anyway as items it could not independently *derive* rather than could not *follow*), and Q2 still FAILED — the solver could recite the physical argument but stated outright it was "accepting the mechanism on the text's authority rather than actually picturing" it. **Genuine assessment after 3 real remediation rounds: the plane-change "walk" is an orbital-mechanics concept that resists full visualization in text alone, the same class of honest, disclosed limitation `the-fold-line`'s QA_REPORT records for real curved-edge marker nesting** ("real nesting is a 2-D packing problem solved by marker-making software... the case's own worked example does not claim [it] is derivable from a single reflection, since it genuinely is not"). A real diagram (an animated or multi-frame illustration of a velocity vector rotating a circular path) would likely close this gap; text describing a 3-D rotation to a zero-context reader has a real, demonstrated ceiling. Waived per MCS-49, not silently passed — see `case.json.qa.tier2.P7_waiver` for the full disclosure.

### Tier 3 — human dry-run

NOT RUN. No real cohort has used this case yet. `cohort_bands[]` is declared for when one does.
