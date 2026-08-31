# Research Log — Panel Layout

Run: `case-research`, 2026-08-31. 14 `{{NEEDS_SOURCE}}` placeholders found in `case.md`
(P01-P14). Outcome: 2 SOURCED (P09, P10 — Fitts's Law coefficients), 12 ASSUMPTION (P01-P08,
P11-P14 — invented device dimensions and miss-rate log). 0 OPEN, 0 DROPPED.

## Sourceable figures (P09, P10 — Fitts's Law a/b coefficients)

Target: real, dated a/b regression coefficients for the Shannon-formulation Fitts's Law model,
from a published ISO 9241-9 conformant target-acquisition study.

1. **Searched:** "MacKenzie Fitts's law ISO 9241-9 typical coefficients a b seconds intercept
   slope" and "ISO 9241-9 Fitts law coefficients regression table mouse a b milliseconds study."
   Found MacKenzie's survey work and several ISO 9241-9-conformant studies by name, but no
   reproduced numeric table in the search snippets themselves.
2. **Fetched** `https://www.yorku.ca/mack/ijhcs2004.html` (MacKenzie, "Perspectives on 27 years of
   Fitts' law research in HCI" — the paper that formally connects Fitts's law research to the ISO
   9241-9 standardization effort). Its Table 4 ("Survey of Nine Studies That Used the ISO9241-9
   Standard") reports **throughput** (bits/s) for nine ISO-conformant studies (Douglas et al. 1999,
   Isokoski & Raisamo 2002, Keates et al. 2002, MacKenzie & Jusoh 2001, MacKenzie et al. 2001,
   MacKenzie & Oniszczak 1998, Oh & Stuerzlinger 2002, Poupyrev et al. 2004, Silfverberg et al.
   2001) but does **not** reproduce the individual regression coefficients (a, b) for those
   studies — **rejected as a direct source for a/b**, kept as background context only.
3. **Fetched** `https://www.yorku.ca/mack/CHI99b.html` (Douglas, Kirkpatrick & MacKenzie 1999,
   "Testing pointing device performance and user assessment with the ISO9241, Part 9 standard" —
   one of the nine ISO-9241-9-conformant studies in the table above). Confirmed it reports
   throughput and error/movement-time means, but **not** linear-regression a/b coefficients —
   **rejected**.
4. **Fetched** `https://www.csit.carleton.ca/~rteather/pdfs/vr2010.pdf` (Evaluating Haptic
   Feedback in Virtual Environments using ISO 9241-9) and
   `https://www.yorku.ca/mack/45520779.pdf` (Evaluating Eye Tracking with ISO 9241 - Part 9) —
   both PDFs returned unparseable binary/font-stream content through the fetch tool and could not
   be read; **abandoned**, not because the papers lack the data but because the tool could not
   extract it.
5. **Fetched** `https://www.yorku.ca/mack/hci1992.html` (MacKenzie, "Fitts' Law as a Research and
   Design Tool in HCI," 1992). Its Figure 11 is a real, well-known, widely-cited table of a/b
   coefficients (ms and ms/bit) across six early Fitts's-law device studies (mouse, joystick, foot
   pedal, eye tracker with hardware button, etc. — e.g. Mouse, Card 1978: a=1030 ms, b=96 ms/bit).
   **Rejected as the case's primary citation** even though it is real and citable: this table
   predates the ISO 9241-9 standard's formal publication (the standard came later, and these are
   the pre-standardization studies it built on), and the case's Appendix B placeholder explicitly
   asks for a published ISO 9241-9 study's coefficients. Kept as a plausibility check only (the
   values ultimately used, S1, fall in a broadly comparable ms/bit range).
6. **Searched** "MacKenzie Kauppinen Silfverberg 2001 accuracy measures Fitts law coefficients"
   and "ISO 9241-9 evaluation mouse MT = seconds regression equation study touchpad trackball
   published" — surfaced the correct citation (MacKenzie, Kauppinen & Silfverberg, CHI 2001,
   "Accuracy Measures for Evaluating Computer Pointing Devices") but no accessible full text with
   the numeric table; **not pursued further** given time budget once (7) below succeeded.
7. **Fetched** `https://www.yorku.ca/mack/hcii2019.html` (Hassan, Magee & MacKenzie, "A Fitts' Law
   Evaluation of Hands-Free and Hands-On Input on a Laptop Computer," HCII 2019, LNCS 11572).
   **Confirmed** the paper explicitly states it used "the Fitts' law two-dimensional task in ISO
   9241-9" (circular target arrangement, 11 targets/sequence, ID = log2(A/W+1), amplitudes
   100/200/400 px, widths 20/40/80 px). Table 1 reports real regression coefficients for four
   conditions. Used the **Touchpad + tap** row (a=699.2 ms, b=171.4 ms/bit, r=.9124) — the
   condition closest to this case's manual tap/press task, among the options reported (the other
   three rows are dwell-based or camera-mouse conditions, worse proxies). **ACCEPTED as S1.**
   Graded MEDIUM, not HIGH: real, dated, ISO 9241-9 conformant, unambiguous units — but the
   measured task (fingertip tap on a laptop touchpad) is a proxy for a hand reaching to press a
   physical medical-device panel button, and no public ISO 9241-9 study of a bedside medical
   device control panel specifically exists.

## Unsourceable figures (P01-P08, P11-P14 — device-specific dimensions and miss-rate log)

Meridian Medical and this hardware revision are invented for this case (confirmed against
`case.json.protagonist` and the concept sheet, C12 — "the protagonist and company are invented,
not a real public product"). No real product's panel drawing, tooling spec, or usability test log
can be sourced for an invented device — attempting to search for one is a dead end by
construction, so no search log entries are recorded for each individual placeholder beyond
confirming this.

**Exit taken: Stated Modeling Assumption** for all 12 (P01-P08, P11-P14), per SKILL.md's exit #1
— this matches the guidance already written into the case's own Appendix D stub before this run.
A 13th assumption (MA9) was added for the linear-interpolation modeling choice already present in
`case.md`'s Appendix A prose, which was structural but previously unlabeled.

To keep the assumed values inside a real, generally-defensible range rather than picking numbers
freehand, two general (non-load-bearing, not cited as S#) searches were run for orientation:
- "FDA human factors medical device control button minimum size mm target width guidance IEC
  60601-1-6 touch target" — surfaced general human-factors guidance that touchscreen targets
  should be at least ~20 mm to avoid performance decrements under gloved/clinical use, and named
  IEC 60601-1-6 and ANSI/AAMI HE75:2009 as the relevant real standards (full text not fetched —
  used only as directional context for MA1/MA2/MA7's ~20 mm benchmark, not cited as a source for
  a specific number).
- "infusion pump control panel button size spacing mm human factors design" — confirmed medical
  infusion-console panels commonly combine large touch/graphical buttons and fixed tactile
  buttons per Fitts's-law-informed design guidance (IEC 62366), general background only.

All 13 assumptions (MA1-MA13), their stated basis, and their sensitivity are recorded in
`case.md` Appendix D and in `case.json.modeling_assumptions[]`. Three were confirmed by direct
numerical computation (not just asserted) to be dilemma-flipping:
- MA8 (count of other required controls, n): Close Reach wins at n≤2, Long Reach wins at n≥3.
- MA6 (Close Reach's other-controls shared distance): Close Reach wins below ≈118 mm (used: 140).
- MA13 (Close Reach's other-controls miss rate): Close Reach wins below ≈4.1% (used: 7%).
MA12 (Close Reach's Confirm miss rate) was checked and found **not** dilemma-flipping even at its
extreme (0%) — flagged in `case.md` as the less-consequential lever, to head off a common but
weaker sensitivity argument.

## Computation (facilitator-only, not written into case.md)

Built T(x) = [a + b·log2(Dc(x)/Wc(x)+1)] + n·[a + b·log2(Do(x)/Wo+1)] with the MA1-MA9 endpoint
values and S1's a/b, linearly interpolated per MA9. Solved T'(x)=0 symbolically (Python/SymPy):
reduces to the quadratic 24x² − 36x + 11 = 0, with exactly one root in [0,1]:
x* = 3/4 − √15/12 ≈ 0.4273, confirmed a local (and global, vs. both endpoints) minimum of T(x) by
the first-derivative test (T' < 0 on (0, x*), T' > 0 on (x*, 1)).

D3 comparison: T(0) ≈ 4.6250 s, T(1) ≈ 4.6111 s, T(x*) ≈ 4.6067 s — x* wins on raw movement time.

D4 (miss-rate-weighted, expected seconds per successful actuation, using MA10-MA13; x* has no
tested miss-rate figure by design, so only the two named options can be compared on this metric):
E(Long Reach, x=0) ≈ 4.7773 s; E(Close Reach, x=1) ≈ 4.8949 s. **Option B (Long Reach) wins**;
margin_pct = (4.8949 − 4.7773) / 4.7773 × 100 ≈ **2.46%**. Not flagged (well under ~20%).

## Verification

`case.md`: 0 `{{NEEDS_SOURCE}}` placeholders remain; citation marker `[S1]` has a matching
Appendix E row; all 13 `(MA#)` markers have matching Appendix D rows. `case.json`: `sources[]`
has 1 complete entry (no missing required fields), 0 LOW-confidence sources,
`needs_source[].status` is `SOURCED` ×2 / `ASSUMPTION` ×12 / `OPEN` ×0, `modeling_assumptions[]`
has 13 entries, `status` set to `"researched"`.

## Post-gate correction (case-readiness Tier 2 probe 6, data decay — 2026-08-31)

A web-access subagent checking S1's cited DOI (`https://doi.org/10.1007/978-3-030-49282-3_9`)
found it **resolves but is the WRONG paper**: it lands on "Evaluating Hands-On and Hands-Free
Input Methods for a Simple Game" (LNCS 12188, HCII 2020, pp. 124-142) — a different, later paper
by the same three authors, not the Fitts's Law laptop study S1 actually cites. The correct DOI for
the cited paper is `10.1007/978-3-030-23563-5_20` (LNCS **11573**, not 11572 as originally
recorded — the LNCS volume number was also off by one). The author's own mirror page
(`https://www.yorku.ca/mack/hcii2019.html`) is reachable and independently corroborates the exact
numeric coefficients (a=699.2 ms, b=171.4 ms/bit, r=.9124 for the touchpad+tap condition) against
its own posted regression table — the underlying figures used in this case's D1-D4 model are
confirmed correct and unchanged. **Fixed:** `case.md` Appendix E and `case.json.sources[0]`
updated to the correct DOI and LNCS volume; `case.json.sources[0].note` records the correction.
This is a citation-URL fix only — no case.md numeric figure, no balance_test value, and no
sensitivity_model.py PARAMS value changed.

## Next step

Run `case-readiness` on `the-panel-layout`.
