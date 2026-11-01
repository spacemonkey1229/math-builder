# QA Report: The Hundredth

## case-readiness run: 2026-10-03
**State:** DRAFT -> TIER1_PASS -> TIER2_PASS   **Verdict:** TIER2_PASS (PUBLISHED not licensed; no publish run)
sha256(case.md) = 31ff62ebcdb2b871ee3df513a1a5698e9f23b54c925056f8a3a6ae92394a3d8a

### Tier 1: structural (24 checks)
0 BLOCKERs. One GAP: T1-10 (empty new_coverage; reinforcement carve-out with reinforcement_note: the spine has no n==0 skill left). T1-14 and T1-16 GAPs were closed (guide-only figure moved into case.json.derived; hash recorded). POLISH: T1-15, 18-24 have nothing to check because there is no published/ directory (case-publish was not run, so no interactive HTML exists and no live-browser audit applies yet; one is REQUIRED after publish per project practice).

### Tier 2: simulated play (7 probes)
| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh solver did D1-D6, correct arithmetic, chose A with low confidence, named metric P. Flagged ambiguity of percent-difference base (fixed afterwards: defined in Appendix E and D5). |
| P2 both-sides | PASS | A defensible; B defensible only at the scenario values; B is the fragile side (collapses at "what frame rate / where does J come from"), A's hard question is "how do you know the lag is below the gap". Neither side collapses. |
| P3 trap | PASS | Hurried-student path matches the guide's trap; guide extended to a 4th item (percent base). |
| P4 twist | PASS | Run 1: BLOCKER, percent-difference base unstated (14.9% vs 0.93% used different bases). Fixed. Run 2: PASS, winner flips to Pad Ranks under every reading; size conventions closed; rooms with lag above about 0.022 s keep Contact Ranks (facilitator line added). |
| P5 sensitivity | PASS (disclosed) | Plus/minus 50% flips: delta_lag -50%, judge_band +50%, fps -50%. All within 20% cap; three category-F sensitivity_disclosure entries. |
| P6 data decay | PASS | S1-S7 reachable, claims confirmed. S5: the "sliding/pushing" wording was only in a reader comment; removed from the case. S8 arithmetic verified. S6 is the 2009-2013 edition (not 2008). |
| P7 accessibility | PASS (after 3 rounds) | Round 1 FAIL (about 12 unexplained terms; central indecision-band model unpicturable). Round 2 FAIL (about 10 fuzzy items; pad lag mechanism). Round 3 PASS: no blocking terms; Q2 none. Fixes: plain-words section, side-view pad SVG, timeline SVG, worked example of the band rule. |

Caveat on currency: P1, P2 and P3 ran on case.md BEFORE the final clarifying additions (percent-difference definition, plain-words section, two SVGs, worked example, rule-number note). Those edits were additive explanations; no figure, option or deliverable changed. P4 (run 2) and P7 (round 3) ran on the later version. A re-run of P1 on the final hash is recommended before publish.

### Tier 2 detail: P1 full solve (verbatim summary of the solver's response)
D1: v = 100/50.58 = 1.97707 m/s; 0.01 s = 0.0197707 m = 1.977 cm. Approximation: race average, hand near wall stroking (faster) or gliding (slower) (MA5).
D2 (hand speed 197.707 cm/s): 30 fps 0.03333 s 6.590 cm; 60 fps 0.01667 s 3.295 cm; 240 fps 0.004167 s 0.824 cm; 1000 fps 0.001 s 0.198 cm. 240 and 1000 can separate 0.01 s; 30 and 60 cannot.
D3: (i) dropped third digit: Phelps true in [50.580,50.590), Cavic [50.590,50.600): gap above 0 and below 0.020 s (discrete thousandths 0.001-0.019 s = 0.198-3.756 cm); (ii) rounded: Phelps [50.575,50.585), Cavic [50.585,50.595): same open interval, 0 to 0.020 s (0 to 3.954 cm). Margin cannot be treated as exactly 0.01 s.
D4: c = Delta - d, d = 0.01. Delta -0.010 -> c -0.020 (Phelps); 0.000 -> -0.010; 0.005 -> -0.005; 0.010 -> 0 (simultaneous); 0.015 -> +0.005 (Cavic); 0.020 -> +0.010; 0.030 -> +0.020. Sign check: pad time = contact + lag so d = -c + Delta. Plausible range chosen: Delta 0 to about 0.015 s, defended from the named claims as claims (all three have Cavic gliding, implying Delta >= 0; magnitude unsourced). Threshold Delta = d = 0.010 s (true d anywhere in (0, 0.02)).
D5: P = 1 - b/(2W), 2W = 0.10. Scenario: A b = 0.010, P = 0.900; B b = 1/240 + 0.005 = 0.009167, P = 0.9083; difference 0.00833 = 0.83 points = 0.93% of P_A. Break-even |Delta| = 0.00917 s. Sweep: Delta 0 -> A 1.000 (A wins); 0.005 -> 0.950 (A); 0.010 -> 0.900 (B); 0.015 -> 0.850 (B); 0.020 -> 0.800 (B). Over solver's 0-0.015 range, mean Delta 0.0075, P_A 0.925 vs P_B 0.908, A narrowly. 60 fps: P_B 0.783 (A wins for |Delta| below 0.0217); 1000 fps: P_B 0.94.
D6: leaves out: ambiguity of what counts as first contact; uniform close-finish window W arbitrary; pad's own 0.01 s resolution not in A's band; video error modelled as frame time + J only (no parallax/occlusion); Delta treated as fixed though it varies by touch and swimmer. Most threatening: true Delta; measurement: controlled touch test with a 1000 fps sensor, gliding vs pushing.
Final answers: chose A (Pad Ranks), low confidence; metric P (ordering reliability for close finishes); strongest counter: Bertaud/protest imply gliders under-trigger the pad (systematic positive Delta); most sensitive to Delta (flip at 0.00917) then frame rate; ignored SW 13.4.2 (combined heats); least supported number J = 0.005 s. Ambiguities reported (all addressed or accepted): percent-difference base (fixed); open vs discrete D3 bounds (guide shows both); "can separate" definition (fixed: frame period below 0.01 s); scenario Delta equal to d gives c = 0 (now explained in the guide); A's band scored against first contact as truth (disclosed in the model note).

### Tier 2 detail: P2 full solve (verbatim summary)
Shared arithmetic as P1. Option A best case: constant lag cancels; P_A = 1 - |Delta|/0.1 beats B at 240 fps for every |Delta| below 0.00917 s; A needs no frame-rate or J assumption; B needs at least about 200 fps to tie A at Delta 0.010 (at 60 fps B loses to A for Delta below 0.0217, at 30 fps below 0.0383); rule text gives the pad precedence, applied identically. Best A sentence: a shared lag cancels, so the pad is wrong only if lanes differ by more than the gap; video needs at least 200 fps and a judge sharper than 5 ms just to match it (0.9083 vs 0.9000). Option B best case: P_B = 0.9083 vs 0.9000 (0.93%); above Delta 0.00917 B wins outright (Delta 0.015: +5.83 pts, 6.9%; 0.020: +10.83 pts, 13.5%; 0.030: +20.83 pts, 29.8%); the pad is blind below 0.01 s (true gap 0 to 0.020 s); at 1000 fps b = 0.006, P_B = 0.94; lag plausibly systematic (glider vs pusher). Best B sentence: the pad measures when a hand pushed hard enough, not when it arrived. B collapses first at: what was the footage frame rate, and where does J come from. A's hardest question: how do you know Delta is below d.

### Tier 3: human dry-run
NOT RUN.

## Honest notes for the human gate
- 2008-edition FINA wording NOT FOUND (2009-2013 and 2015-2017 read); the case says so.
- 2008 footage frame rate, pad lag and judge reading band are assumptions (MA1-MA3).
- Rule-number point: the equal-hundredths placing rule is SW 11.2 (the concept named SW 13.4.2, which is the combined-heats rule); the case cites both accurately.
- No interactive HTML exists. After publish, a live-browser audit is still required.

## Addendum 2026-10-04: Appendix C diagram label fix (post-TIER2_PASS)
**What changed:** in the Appendix C side-view SVG in case.md, label text/positions only. (1) "swimmer's hand and arm, moving right" (x=150, y=85) became "swimmer's hand, moving right" (x=100, y=82), so it no longer runs into the touchpad plate and pool wall. (2) "touchpad plate" (x=262, y=36) became right-aligned at x=308, y=36 (text-anchor end), so it sits left of the plate and clear of "pool wall". No shape, figure, number, option, deliverable or prose changed. The Challenge 5 asterisk was left alone (shared boilerplate).
**Hash:** case.md sha256 31ff62eb... -> 8218204980a1b3ec3d5894b6ca7d92cce88b82cd65f8b360998edece0955b44f. case.json.qa.case_md_sha256 and published/MANIFEST.json updated to match. Tier 1 re-run on the new hash: 0 blockers, 0 FAIL (TIER1_PASS; GAPs unchanged: T1-10 reinforcement carve-out, plus two T1-15 publish-continuity gaps on the xlsx lag-grid cell and a guide-only 45.0).
**Probes not re-run:** Tier 2 probes P1-P7 were NOT re-run on the new hash. The edit touches only the position and wording of two SVG text labels, with no change to any number, option, rule or instruction a solver could use, so the P1-P7 findings (all about arithmetic, framing and answerability) are not expected to change. A fresh P7-style visual check of the diagram was done in the rebuilt docx render and in the browser; see the run note from the caller.


## Publish waivers (2026-10-19)
Human instruction to publish received in chat after the promotion preview listed these open gaps; recorded as waived:
- T1-10: empty new_coverage, documented reinforcement carve-out (spine has no n==0 skill)
- T1-15: xlsx cell -0.01 (case.md uses a Unicode minus) and '45' from the '45-minute Socratic plan' heading in the facilitator guide; cosmetic
