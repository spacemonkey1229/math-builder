# Research Log — The Parity Check

Stage 3 (`case-research`) run on `cases/the-parity-check/`. 23 `{{NEEDS_SOURCE}}` placeholders in
`case.md`/`case.json.needs_source[]`. `FACILITATOR.md` carried a mandatory Robustness Check
requirement, added at write time specifically because `cases/the-overlap-call` was killed this
session for a margin that looked fine (1.11%) but flipped under small, realistic changes to a
stated Modeling Assumption. This case's primary metric has the identical fragility *shape*
(a ratio whose denominator depends on Appendix E's per-bit error rate, which was flagged at
write time as likely to land as a disclosed assumption, not a hard citation) — so the sweep
below was run **before** setting `margin_pct`, per that requirement.

Worked in load-bearing order: the two real, standing technical facts first (CRC-32/FCS, parity
convention), then real packet-size data, then the genuinely uncertain per-bit error rate, then
the narrative/flavor figures last.

## P02, P04, P05 — IEEE 802.11 FCS length and CRC-32 polynomial (Background, Appendix A)

**Fetched:** `https://en.wikipedia.org/wiki/IEEE_802.11` and
`https://www.geeksforgeeks.org/computer-networks/ieee-802-11-mac-frame/` — the latter states
plainly: "It is 4 bytes long field which contains a 32 bit CRC error detection sequence." Also
gives the standard degree-32 generator polynomial matching CRC-32.

**Cross-checked:** `https://en.wikipedia.org/wiki/Cyclic_redundancy_check` — its CRC-32
parametrization table explicitly lists **ISO/IEC/IEEE 802-11 (Wi-Fi)** and **ISO/IEC/IEEE 802-3
(Ethernet)** among the real standards using generator polynomial **0x04C11DB7**. This
independently corroborates GeeksforGeeks' claim from a second, differently-sourced real page.

**Outcome:** SOURCED as [S1] (FCS length, MEDIUM — tutorial site, not the IEEE standard document
itself) and [S2] (polynomial + standards list, HIGH — Wikipedia's well-referenced CRC article,
corroborating [S1]). Both used in Background and Appendix A.

## P01, P06 — Parity overhead percentage and the byte-parity convention (Background, Appendix A)

**Fetched:** `https://en.wikipedia.org/wiki/Parity_bit` — confirms "8 bits of data plus a parity
bit can convey all 8-bit byte values" and describes UART/serial hardware generating and checking
parity this way — exactly the convention this case's Featherweight Check uses (1 bit per 8 data
bits, byte-level, not the alternate 7-data-bit ASCII convention the same article also describes).

**Outcome:** SOURCED as [S3], HIGH confidence. The 12.5% overhead figure (1 bit ÷ 8 data bits) is
the case's own arithmetic on top of this sourced convention — marked `derived: true`.

## P03, P07 — Smallest, small-to-mid, mid, and largest realistic sensor uplink payload sizes (Background, Appendix C)

**Searched:** LoRaWAN maximum payload size by data rate/region — this class of device (a
low-power sensor uplink bolted to fence posts and buoys) matches LoRaWAN/LPWAN framing closely.

**Fetched:** `https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/lorawan.html`
— states an 11-byte application payload is supported across nearly all frequency plans and data
rates. Then `https://www.thethingsnetwork.org/docs/lorawan/regional-parameters/us915/` — a real,
live, dated table of US915 maximum application payload size by data rate: DR0=11, DR1=53,
DR2/DR6=125, DR3/DR4/DR10-13=222 bytes.

**Outcome:** SOURCED as [S4] (11-byte universal minimum) and [S5] (the full US915 table). Used
directly for Appendix C rows 1 (11, smallest), 3 (125, mid), and 4 (222, largest — the table's
own maximum).

**Row 2 — the balance problem.** Computing the case's primary metric (P(scheme catches the
frame's corruption) per overhead bit spent) at all four *real* candidate sizes found from [S4]/
[S5] alone (11, 53, 125, 222) produces margins of 191% (n=11, A wins), 66% (n=53, B wins), 291%
(n=125, B wins), and 594% (n=222, B wins) — **every one exceeds SPEC §2's ~20% balance cap**. The
underlying reason is structural, not a research gap: the raw arithmetic break-even between the
two schemes (1 bit/byte × *n* bytes = the sourced 32-bit CRC overhead) is **exactly n = 32
bytes**, and none of the four real US915 table entries happens to land near it. Per
`skills/case-research/SKILL.md` §5 exit 1 and the `cases/the-turbine-channel` precedent (a
scenario constant tuned within a real envelope so neither option trivially dominates), row 2 was
retuned: **32 bytes**, chosen specifically at this real, derived crossover point, within the real
LoRaWAN payload envelope ([S4]/[S5], 11-222 bytes) but not itself one specific regional-parameter
table entry. This is disclosed as **MA2**, not presented as a sourced figure. `case.json.balance`
reports `margin_pct` at this size — see the Robustness Check section below for why this choice
does not just "hide" the balance problem, and the arithmetic behind why 32 bytes is where it
naturally belongs.

## P09 — Representative per-bit error rate (Background, Appendix E) — the load-bearing one

**Searched:** LoRaWAN/LPWAN bit error rate, Iridium Short Burst Data BER, typical wireless link
BER design targets, IEEE 802.15.4 sensitivity/PER definitions. Confirmed what the concept sheet
anticipated: **no single public per-bit BER figure exists for this class of device** — real BER
varies by many orders of magnitude depending on medium (a 2026-09-13 search directly surfaced
figures from ~1e-9 for a "well provisioned" wireless link, up to a widely repeated "typical
wireless link ~1e-5," up to "wireless link designed for BER < 1e-6, dropped around 1e-3").

**Fetched (the one concrete, real, standards-derived anchor):**
`https://www.nsnam.org/docs/models/html/lr-wpan.html` — a network-simulator project's
documentation, citing and validated against IEEE Std 802.15.4-2006 §6.1.7/E.4.1.7: receiver
sensitivity for this real low-power wireless sensor-network standard is defined at the packet
error rate that stays under 1% for a 20-byte (160-bit) reference packet. Derived per-bit BER at
that threshold: `1-(1-0.01)^(1/160) ≈ 6.28e-5`.

**Outcome: NOT FOUND** as a single hard-sourced figure for this exact fictional link — **exit
chosen: Modeling Assumption (MA1)**, value used **6×10⁻⁵**, informed by [S6] (IEEE 802.15.4's own
real sensitivity definition, applied by analogy) and bounded by the broader real-world range
found during search (~1e-6 to ~1e-3). Disclosed plausible range for the robustness sweep: **1e-6
to 1e-3**, spanning three orders of magnitude — deliberately wide, since real-world BER really
does vary this much by medium (satellite, LoRa, Wi-Fi, Ethernet all differ enormously).

## P08 — Radio energy per bit and season battery budget (Appendix D) — non-load-bearing

Checked `case.md` first: D1–D5's formulas are defined entirely in bits (overhead bits, decimal
digits, catch probabilities) — **Appendix D's numbers are never used in the graded arithmetic**,
only in Background's narrative ("the hardware lead... battery budget"). Researched anyway per
SPEC §1.6 (supplemental realism), held to a lower bar since nothing here is load-bearing.

**Fetched:** `https://pmc.ncbi.nlm.nih.gov/articles/PMC12788325/` (Soler-Fernández et al., "LoRa
Power Model for Energy Optimization in IoT Applications," *Sensors*, Jan 2, 2026) — a real,
peer-reviewed ASIC validation measurement: 35 mJ per 1,800-byte (14,400-bit) transmission at 0
dBm, measured via voltage drop across a supercapacitor. Derived: 35 mJ ÷ 14,400 bits ≈ **2.43
µJ/bit**.

**Fetched:** `https://www.dragino.com/products/lora-lorawan-end-node/item/155-lsn50-v2.html` — a
real, commercially available outdoor LoRaWAN sensor node (fence-post/field-deployable class,
matching this case's own Overview) — confirms an 8,500 mAh Li/SOCl2 battery.

**Fetched:** `https://wiki.dragino.com/docs/FAQs/general/battery-life-calculation/` — vendor
guidance citing 8–10 years of expected multi-year field life for this class of node.

**Outcome:** SOURCED [S7] (energy/bit, derived, HIGH) and [S8] (battery capacity, HIGH); [S9]
(multi-year life, MEDIUM — general vendor guidance, not device-exact). Season budget derived as
**MA4**: 8,500 mAh ÷ 10 years ≈ 850 mAh/season (assuming a "season" is one year of the cited
lifespan) — disclosed as an assumption since the season-to-year mapping and the even split across
years are not themselves published facts. Flagged non-load-bearing in `case.json`.

## P10 — Sample sensor data bytes and corrupted variants (Appendix B) — constructed, not sourced

Re-read the placeholder text: these are illustrative 8-bit worked-example values for D1/D2, not a
record of any real transmission — there is no real-world fact to search for, matching the
treatment already established this session for `cases/the-cold-start` and
`cases/the-attribution-sample`'s narrative-construct placeholders. No search performed.

**Constructed** (verified by hand): byte 1 = `01101001` (4 ones, EVEN, parity=0), corrupted by
flipping 2 bits → `11101101` (still 6 ones, EVEN — a genuine silent miss for D2). Byte 2 =
`10010001` (3 ones, ODD, parity=1), corrupted by flipping 1 bit → `10110001` (now 4 ones, EVEN —
correctly *caught*, since an odd number of bits flipped always changes parity). Byte 3 =
`11110000` (4 ones, EVEN, parity=0), corrupted by flipping 2 bits → `01111000` (still 4 ones,
EVEN — silent miss). Byte 4 = `00100000` (1 one, ODD, parity=1), corrupted by flipping 1 bit →
`00100010` (now 2 ones, EVEN — caught). All four satisfy the case's own D1/D2 requirements exactly
(2 even-flip / 2 odd-flip demonstrations).

**Outcome:** ASSUMPTION (MA3), non-load-bearing.

## P11 — Firmware freeze date and deployed node count (Appendix F) — narrative restatement

Framed by the placeholder text itself as "as used in the Overview/Background" — these numbers
already appear in this case's own Overview ("eleven thousand sensor nodes") and Background ("the
uplink firmware freezes for the season in one week"). An authorial narrative choice, not a
real-world fact to source. No search performed.

**Outcome:** ASSUMPTION (MA5). Decorative, not load-bearing.

---

## THE MANDATORY ROBUSTNESS SWEEP — full result

**Model:** `cases/the-parity-check/sensitivity_model.py` (runnable; `python3
cases/the-parity-check/sensitivity_model.py` reproduces every number below). Primary metric,
restated per `case.json.primary_metric`/Background's own "catches more corrupted frames per bit
spent" framing: for each scheme, `P(scheme catches the frame's corruption) / (overhead bits that
scheme adds)`. Featherweight Check misses a frame only if every corrupted byte has an EVEN,
nonzero flip count; Full-Frame Guard is modeled as catching essentially all corruption (per
Appendix A's real CRC-32 guarantees). `FLEX = ["error_rate"]` — the one assumption
(MA1) this case's own Robustness Check names; packet size is a fixed scenario/sourced input the
Hero explores directly (D3), not an assumption dial.

**Sweep 1 — at the reported packet size (32 bytes), across the full disclosed error-rate range:**

| error_rate | winner | margin |
|---|---|---|
| 1e-6 | B | 0.0003% |
| 1e-5 | B | 0.0035% |
| 6e-5 (Appendix E's stated value) | B | 0.0208% |
| 1e-4 | B | 0.0346% |
| 1e-3 | B | 0.3086% |

**The winner (B, Full-Frame Guard) never flips across three orders of magnitude of the error-rate
assumption.** The margin stays razor-thin throughout (comparable in spirit to SPEC §2's own gold
standard, Route 1 beating Route 2 by 0.09%) but never crosses zero.

**Sweep 2 — break-even packet size at each tested error rate (bisection):**

| error_rate | break-even n* (bytes) |
|---|---|
| 1e-6 | 32.00 |
| 1e-5 | 32.00 |
| 6e-5 | 31.99 |
| 1e-4 | 31.99 |
| 1e-3 | 31.90 |

**The break-even point is essentially independent of the error-rate assumption** — it moves by
less than 0.1 bytes across three orders of magnitude of BER. This makes sense analytically: the
raw arithmetic break-even (1 bit/byte × 32 bytes = 32 bits = the sourced CRC overhead) is a
geometric fact about the two schemes' fixed costs, not a probabilistic one; the error rate only
determines *how much* is at stake near that point, not *where* it sits.

**Sweep 3 — winner at all four Appendix C candidate sizes, across the full error-rate range:**

| packet size (bytes) | winner(s) across full 1e-6–1e-3 range |
|---|---|
| 11 | A only |
| 32 | B only |
| 125 | B only |
| 222 | B only |

**Every candidate packet size has a single, stable winner across the entire disclosed error-rate
range.** Packet size — not the error-rate assumption — is what determines which option wins away
from the n=32 crossover, and this is a real, robust, sourced structural property (11 < 32 < 125 <
222, all real/assumption-anchored per Appendix C), not an artifact of guessing the error rate.

**CONCLUSION: STABLE / ROBUST.** Unlike `cases/the-overlap-call` (killed because its margin
flipped winner at -13% off its stated kit-allotment assumption and at +5% off its stated
dual-exposure-rate assumption — both well inside a plausible real range), this case's reported
margin at the packet size it actually reports (32 bytes) does not flip anywhere across the full
disclosed 1e-6–1e-3 error-rate range. `margin_pct = 0.02` (at Appendix E's stated 6e-5 value) is
recorded in `case.json.balance` and `case.json.margin_pct`. `sensitivity_disclosure[]` is
correctly empty — no swept parameter flips the winner or breaches the SPEC §2 20% cap within its
disclosed plausible range at the reported size.

## Summary table

| ID | Placeholder | Resolution | Value | Confidence |
|---|---|---|---|---|
| P02/P04/P05 | IEEE 802.11 FCS length + CRC-32 polynomial | SOURCED ([S1], [S2]) | 4 bytes/32-bit CRC, 0x04C11DB7 | MEDIUM/HIGH |
| P01/P06 | Byte-parity convention + overhead % | SOURCED ([S3]), derived | 1 bit/8 data bits, 12.5% | HIGH |
| P03/P07 | Payload sizes (rows 1,3,4) | SOURCED ([S4], [S5]) | 11, 125, 222 bytes | HIGH |
| — | Payload size row 2 | ASSUMPTION (MA2) | 32 bytes (arithmetic break-even) | n/a |
| P09 | Per-bit error rate | NOT FOUND — ASSUMPTION (MA1), informed by [S6] | 6e-5 (range 1e-6–1e-3) | n/a |
| P08 | Energy/bit, battery budget | SOURCED ([S7],[S8],[S9]), derived, non-load-bearing | ~2.43 µJ/bit, ~850 mAh/season | HIGH/HIGH/MEDIUM |
| P10 | Sample bytes (Appendix B) | ASSUMPTION (MA3), constructed | 4 bytes + corrupted variants | n/a |
| P11 | Freeze date, node count | ASSUMPTION (MA5), narrative restatement | 1 week; 11,000 nodes | n/a |

Sourced: 9 sources ([S1]–[S9]). Assumptions: 5 (MA1–MA5). Dropped: 0. Open: 0. All 23
`{{NEEDS_SOURCE}}` placeholders resolved. `sensitivity_disclosure[]` correctly empty — the
Robustness Check confirmed stability, so no unresolved fragility needed disclosing.

---

## Retune (2026-09-13) — Appendix C row 2 moved from 32 to 35 bytes, coin-flip margin fixed

A post-research review flagged that landing Appendix C row 2 (MA2) exactly on the schemes'
raw arithmetic tie point (n = 32 bytes, where 1 bit/byte × 32 bytes = 32 bits = the CRC's own
sourced 32-bit overhead) made `margin_pct = 0.02` an essentially coin-flip result — the same
failure shape that nearly killed `cases/the-overlap-call` this session: a margin this tight
risks a fresh solver reasonably landing on either side depending on rounding, even though the
underlying relationship (packet size vs. two fixed-cost schemes) is directionally stable and the
robustness sweep across error rates (already run above, and NOT redone here since it was
independently confirmed sound) held up fine.

**First checked: is packet size retunable here, unlike `the-overlap-call`?** `the-overlap-call`
was killed via disclosure because its scenario constant was flat-rate-invariant — no real value
of that constant could move its margin out of the fragile zone. Packet size in this case is
different: the primary metric's efficiency for each scheme scales with `n` in structurally
different ways (A's total overhead scales linearly with n; B's is fixed), so moving n genuinely
moves the margin, and moves it fast. This case is retunable, not disclose-only.

**Mapped the margin surface** by running `evaluate()` from `sensitivity_model.py` (before editing
it) across a fine sweep of n at the stated error rate (6e-5):

| n (bytes) | winner | margin |
|---|---|---|
| 30 | A | 6.64% |
| 31 | A | 3.20% |
| 32 | B | 0.02% (the original, coin-flip value) |
| 33 | B | 3.15% |
| 34 | B | 6.25% |
| 35 | B | 9.40% |
| 36 | B | 12.52% |
| 37 | B | 15.65% |
| 53 | B | ~66% (matches the earlier P03/P07 finding for the real S5 table value) |

The margin compounds very fast moving away from n=32 in either direction — this is exactly why
sitting on n=32 itself was fragile (a hair's-width rounding difference decides the sign), and why
several bytes of clearance in either direction is enough to produce a large, unambiguous margin.
**n = 35 bytes lands at 9.40%, comfortably inside SPEC §2's ~5–15% target band and far from both
the coin-flip zone at n≈31–32 and the landslide zone at n≥53.**

**Checked real-world plausibility of 35 bytes.** It is not one of the four sourced US915
data-rate-table entries ([S5]: 11, 53, 125, 222), so — same treatment as the original MA2 choice —
it is disclosed as a Modeling Assumption, not presented as a table value. It sits comfortably
within the real LoRaWAN payload envelope those sourced entries define (11–222 bytes), and is
consistent with a compact multi-field sensor reading (e.g. temperature + humidity + battery
voltage + a short device/sequence ID) — plausible for a device class this case's Overview already
frames as a fence-post/buoy/irrigation-riser sensor reporting more than a single scalar reading.
This is a legitimate real-world packet-size convention, not a number picked purely because it
produces a convenient margin — though the margin was of course the deciding factor among several
otherwise-plausible nearby sizes (34, 35, 36 all work; 35 was chosen as landing closest to the
middle of the target band).

**Re-ran the full robustness sweep at n = 35** (updated `sensitivity_model.py`,
`PARAMS["packet_size_bytes"] = 35.0`; `FLEX` unchanged, still `["error_rate"]`):

| error_rate | winner at n=35 | margin |
|---|---|---|
| 1e-6 | B | 9.3754% |
| 1e-5 | B | 9.3788% |
| 6e-5 (stated) | B | 9.3978% |
| 1e-4 | B | 9.4128% |
| 1e-3 | B | 9.7084% |

**Result: STABLE, and now comfortably inside the target band throughout the swept range** (margin
moves by less than 0.4 percentage points, from 9.38% to 9.71%, across three full orders of
magnitude of the error-rate assumption — the winner never flips and the margin never leaves the
5–15% band). The winner-by-packet-size table (Sweep 3, unaffected by this retune except that its
middle row is now n=35 instead of n=32) still shows a single stable winner at every Appendix C
candidate size across the full error-rate range: A only at n=11, B only at n=35, B only at n=125,
B only at n=222. The schemes' exact geometric tie point (n≈31.90–32.00 bytes, from the original
Sweep 2 bisection) is unaffected by this change — it is a property of the two schemes' fixed costs,
not of which size the case happens to report its comparison at.

**Files updated:** `case.md` (Appendix C row 2: 32→35; Appendix G MA2 row: value and basis,
including the explicit note that 35 bytes was chosen a few bytes off the exact tie point rather
than on it), `case.json` (`margin_pct`: 0.02→9.4; `balance.margin_basis`,
`balance.winner_at_reported_size`, `balance.winner_by_packet_size`, `balance.robustness_check`,
`modeling_assumptions[MA1].sensitivity`, `modeling_assumptions[MA2].value_used`/`basis`/
`sensitivity`, `sensitivity_note` — all updated to 35 bytes and the new margin/range figures;
`sensitivity_disclosure[]` left empty, since the retuned case is stable with no unresolved
fragility to disclose), `FACILITATOR.md` (header margin figure, both balance arguments, margin
basis, Robustness Check section and table, the "honest caveat" paragraph, and Socratic Questions
1/3/4, all updated to reflect 35 bytes as the reported size and 9.40% as the margin, while
preserving the pedagogically important fact that the true arithmetic tie point remains 32 bytes).
`status` remains `"researched"`; `qa.verdict` remains `null`; `readmodel/*.json` was not touched;
`case-readiness`/`case-qa`/`case-publish` were not run.

## Next step

Run `case-readiness` on `the-parity-check`. (Not run as part of this task, per its own hard
lines: this task explicitly excludes running case-readiness/case-qa/case-publish.)
