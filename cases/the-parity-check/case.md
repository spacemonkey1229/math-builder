# Case Study: The Parity Check

MS | Math | Case Study | 2026 | Adventure

---

## Overview

Renata Kuo has forty minutes before the firmware freeze meeting, and the two functions on her second monitor are eleven lines apart.

One line calls `add_parity_bit()`. The other calls `add_crc32()`. Whichever one she leaves in the build tonight ships, unchanged, to eleven thousand sensor nodes already bolted to fence posts, buoys, and irrigation risers across three states — devices nobody is going to climb a pole to re-flash before next spring's maintenance window.

Her phone buzzes, face-down, next to the empty coffee cup. It's the hardware lead. He has asked her twice this week, in front of increasingly more people, how many extra milliamp-hours her error-checking scheme is going to cost his battery budget — and both times she gave him a number she wasn't fully sure would survive a real bad-weather week.

She pulls up the packet trace from the test rig: tiny frames, some barely sixteen bytes long, the sensor's whole reading crammed into less space than this sentence. She knows the trade in her gut — parity is nearly free and misses things; CRC catches almost everything and costs more, every single packet, whether it needs it or not. What she doesn't have yet is the number that turns "catches more" into "worth it, at this packet size."

The meeting invite is already open in the other window. Renata sets down the coffee cup, glances at both function calls one more time, and reaches for the keyboard.

---

## Background

Renata Kuo is the network reliability engineer at a small satellite-IoT operator. She owns the link-layer error-detection scheme for the company's new low-power sensor uplink, and she is the one who has to defend whatever she chooses — both to the firmware review board this week and, later, to the hardware team, whose battery budget her scheme eats into every time a packet goes out.

The uplink firmware freezes for the season in one week. After that, nothing about the error-checking scheme can change without a truck roll to every deployed sensor (SEE APPENDIX F). Renata is choosing between exactly two schemes, both already implemented and tested on the bench. (All figures in this case are sourced in APPENDIX I; where no public figure exists, the case says so and states its assumption in APPENDIX G.)

**The Featherweight Check:** a single even-parity bit appended to every byte of sensor data. The cost is fixed and tiny — one extra bit for every eight data bits, roughly 12.5% [S3] of the data stream (1 bit ÷ 8 data bits = 0.125). Its limitation is structural, not a matter of bad luck: a single even-parity bit can only ever detect an **odd** number of flipped bits in that byte. If exactly two bits flip — or four, or six — the parity check comes back clean and the corrupted byte is delivered as if nothing happened (SEE APPENDIX B).

**The Full-Frame Guard:** a 4-byte CRC-32 frame check sequence appended once per whole packet — the same scheme IEEE 802.11 uses to guard every Wi-Fi frame (SEE APPENDIX A). It catches essentially every realistic error pattern, including the entire class of even-bit-flip errors the Featherweight Check is blind to. Its cost is fixed **per packet**, not per byte: 4 bytes (32 bits) [S1][S2] added once, however small the packet.

That per-packet fixed cost is the whole tension. Renata's sensor packets are not one fixed size — the uplink firmware supports a range of payload sizes depending on which sensors are attached and how much telemetry a node is reporting that cycle (SEE APPENDIX C). On the company's largest packets, a 4-byte tax barely registers. On its smallest — some payloads run as small as 11 bytes [S4][S5] — that same 4 bytes can be a third or more of everything transmitted.

Every extra bit transmitted also costs battery: the radio spends measurable energy per bit sent, and the hardware team's battery budget for this deployment is fixed for the season (SEE APPENDIX D). Renata cannot evaluate either scheme by overhead alone or by catch-rate alone — the question is which scheme catches more corrupted frames **per bit spent** getting there, and that number depends on packet size, which is exactly the variable she can't pin to one value (SEE APPENDIX C). A stated per-bit error rate for this class of link, and what it implies about how often a byte suffers an even vs. an odd number of flips, is in APPENDIX E.

The vocabulary and the "how to…" skills this case will ask of you are listed in **APPENDIX H** — that is where Challenge 1 sends you.

The meeting starts in forty minutes.

---

## Dilemma

You are Renata Kuo.

Do you:

**A.)** Ship the Featherweight Check — a single even-parity bit added to every byte of sensor data **OR**

**B.)** Ship the Full-Frame Guard — a 4-byte CRC-32 check sequence added once per packet, the same scheme IEEE 802.11 uses

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A byte-level worked table: for a set of sample sensor data bytes (APPENDIX B), the number of 1-bits in each byte, whether that count is EVEN or ODD, and the single parity bit the Featherweight Check would append.
    D2. A "silent miss" demonstration: at least one worked example, built from Appendix B's sample bytes, of a corrupted byte where an EVEN number of bits flipped — showing the error the Featherweight Check misses but the Full-Frame Guard catches.
    D3. An overhead-vs-packet-size comparison table across the packet sizes in Appendix C: total data bits, Featherweight Check overhead bits, Full-Frame Guard overhead bits, and overhead as a percent of the transmitted frame, for each scheme at each size.
    D4. A bits-to-decimal-digits comparison: the maximum number of decimal digits needed to write out the largest possible check value for each scheme (a single parity bit vs. a 32-bit CRC value), showing the gap in what each scheme's check value actually takes to record, not just its bit count.
    D5. A break-even packet-size calculation and recommendation: using Appendix E's stated per-bit error rate to estimate the probability a byte suffers an even number of bit flips, compute overhead bits per additional error pattern caught for each scheme, and identify the packet size where the two schemes cross.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

### Appendix A — Standards and Specifications

| | Value |
|---|---|
| IEEE 802.11 Frame Check Sequence length | 4 bytes (32 bits) — a 32-bit CRC calculated over the MAC header and frame body [S1][S2] |
| CRC-32 generator polynomial (for reference, not required arithmetic) | 0x04C11DB7 — the standard CRC-32 polynomial used by ISO/IEC/IEEE 802-11 (Wi-Fi) and ISO/IEC/IEEE 802-3 (Ethernet) alike [S2] |
| Single even-parity-bit convention (1 bit added per 8 data bits) | 8 data bits plus 1 parity bit, the standard byte-level serial/UART convention [S3] |

### Appendix B — Sample Sensor Data Bytes

A working set of sample byte values, given as 8-bit binary strings, for D1 and D2.

| Byte # | Bit pattern (as transmitted) | Corrupted variant (bits flipped) |
|---|---|---|
| 1 | 01101001 | 11101101 (2 bits flipped) |
| 2 | 10010001 | 10110001 (1 bit flipped) |
| 3 | 11110000 | 01111000 (2 bits flipped) |
| 4 | 00100000 | 00100010 (1 bit flipped) |

*These four sample bytes are worked examples constructed for this case, not measurements of any real transmission (SEE APPENDIX G, Modeling Assumptions).*

### Appendix C — Candidate Packet Sizes

| Payload size (bytes) | Notes |
|---|---|
| 11 | smallest sensor reading (e.g. single temperature reading) [S4][S5] |
| 35 | a small-to-mid payload (SEE APPENDIX G, Modeling Assumptions) |
| 125 | a mid-size multi-field reading [S5] |
| 222 | full multi-sensor telemetry burst [S5] |

### Appendix D — Radio Energy Budget

| | Value |
|---|---|
| Energy cost per transmitted bit, this radio/data rate | ≈2.43 µJ/bit, derived [S7] (SEE APPENDIX G, Modeling Assumptions) |
| Season battery energy budget allocated to this deployment | ≈850 mAh per node per season, derived [S8][S9] (SEE APPENDIX G, Modeling Assumptions) |

### Appendix E — Per-Bit Error Rate

| | Value |
|---|---|
| Representative per-bit error rate for this class of link | 6×10⁻⁵, stated scenario value (SEE APPENDIX G, Modeling Assumptions); real published figures for wireless/LPWAN links range roughly 10⁻⁶–10⁻³ depending on medium and conditions [S6] |

### Appendix F — Deployment and Freeze Constraints

| | Value |
|---|---|
| Firmware freeze date | one week from the Overview's "today" (SEE APPENDIX G, Modeling Assumptions) |
| Number of deployed sensor nodes affected | 11,000 (SEE APPENDIX G, Modeling Assumptions) |

### Appendix G — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, or values the case states about itself. A Hero may challenge them in discussion — that
> is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Representative per-bit error rate for this class of link (Appendix E) | 6×10⁻⁵ | Real-world bit-error rates vary enormously by medium and conditions — no single public figure exists for this fictional link. This value is derived from a real published receiver-sensitivity definition for a small wireless sensor-network standard, applied here by analogy since no BER figure exists for this exact fictional device [S6]. | The answer is sensitive to this value at some packet sizes and not at others — recompute D5 with this value doubled and halved and compare. |
| MA2 | Second candidate packet size (Appendix C, row 2) | 35 bytes | No single "typical" mid-size payload is publicly documented for this fictional uplink. Chosen as a plausible payload size within the real payload envelope this class of device supports (Appendix C rows 1 and 4, sourced) rather than tied to one specific regional data-rate table entry — comparable to a compact multi-field reading (e.g. temperature + humidity + battery voltage + a short device/sequence ID) that fits comfortably between the smallest single-reading payload (11 bytes) and the mid-size multi-field payload (125 bytes). Deliberately chosen a few bytes away from the schemes' exact arithmetic tie point (32 bytes = 1 bit/byte × 32 bytes = the CRC's 32-bit overhead) so the comparison at this size has a real, checkable winner rather than landing on a coin flip. | The answer is sensitive to this value — recompute D5 with a somewhat larger and somewhat smaller packet size and compare. |
| MA3 | Sample sensor data bytes and their corrupted variants (Appendix B) | See Appendix B table | Constructed worked-example data for D1/D2, not a measurement of any real transmission — no such record is a public, sourceable fact. Built to satisfy the case's own stated even/odd-flip requirements. | Not load-bearing — does not affect D3–D5 or the recommendation. |
| MA4 | Energy cost per bit and season battery budget (Appendix D) | ≈2.43 µJ/bit; ≈850 mAh/season | Energy-per-bit is derived from a real published measurement on a real LoRa sensor radio [S7]; the season battery budget is derived by dividing a real commercial outdoor sensor node's total battery capacity [S8] by its manufacturer-cited multi-year field life [S9], assuming a "season" is one year of that life. Neither figure is specific to this fictional deployment. | Not load-bearing — Challenges D1–D5 and the primary metric are defined entirely in bits, not energy; Appendix D is background context only. |
| MA5 | Firmware freeze date and deployed node count (Appendix F) | One week; 11,000 nodes | Restates, for the record, the same figures already stated in this case's own Overview and Background narrative ("forty minutes before the firmware freeze meeting... freezes for the season in one week"; "eleven thousand sensor nodes"). An authorial scenario choice, not a real-world fact to source. | Not load-bearing — flavor and stakes-setting only; does not enter the D1–D5 arithmetic. |

### Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Even
- Odd
- Digit
- Number
- Probability

**"How to…" questions**

*(none — this case's claimed spine skills are all vocabulary terms; Challenge 1's research task points to whichever of the five terms above the Hero found the least familiar.)*

### Appendix I — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | IEEE 802.11 MAC frame FCS field length | 4 bytes, 32-bit CRC | GeeksforGeeks — "IEEE 802.11 Mac Frame" ([link](https://www.geeksforgeeks.org/computer-networks/ieee-802-11-mac-frame/)) | accessed 2026-09-13 | MEDIUM |
| S2 | CRC-32 generator polynomial and its use by IEEE 802.11/802.3 | 0x04C11DB7; used by ISO/IEC/IEEE 802-11 (Wi-Fi) and ISO/IEC/IEEE 802-3 (Ethernet) | Wikipedia — "Cyclic redundancy check" ([link](https://en.wikipedia.org/wiki/Cyclic_redundancy_check)) | accessed 2026-09-13 | HIGH |
| S3 | Standard byte-level parity convention | 8 data bits + 1 parity bit (1 bit per 8 data bits, 12.5% overhead, derived) | Wikipedia — "Parity bit" ([link](https://en.wikipedia.org/wiki/Parity_bit)) | accessed 2026-09-13 | HIGH |
| S4 | LoRaWAN application payload size supported across nearly all frequency plans/data rates | 11 bytes | AWS Whitepapers — "LoRaWAN, Implementing LPWAN Solutions with AWS IoT" ([link](https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/lorawan.html)) | accessed 2026-09-13 | HIGH |
| S5 | LoRaWAN US915 maximum application payload size by data rate | DR0=11, DR1=53, DR2/DR6=125, DR3/DR4/DR10-13=222 bytes | The Things Network — "US902-928 MHz Band (US915) Regional Parameters" ([link](https://www.thethingsnetwork.org/docs/lorawan/regional-parameters/us915/)) | accessed 2026-09-13 | HIGH |
| S6 | Receiver-sensitivity-defining packet error rate for a small wireless sensor-network standard | 1% PER at a 20-byte (160-bit) reference packet, IEEE Std 802.15.4-2006 §6.1.7 — implies an approximate per-bit BER of ≈6.3×10⁻⁵ at the sensitivity threshold (derived: 1-(1-0.01)^(1/160)) | ns-3 Network Simulator documentation — "IEEE 802.15.4: Low-Rate Wireless Personal Area Network (LR-WPAN) — Model Library," citing IEEE Std 802.15.4-2006 §6.1.7/E.4.1.7 ([link](https://www.nsnam.org/docs/models/html/lr-wpan.html)) | accessed 2026-09-13 | MEDIUM (secondary confirmation of a primary standard's definition; applied here by analogy, not a direct measurement of this case's fictional link) |
| S7 | LoRa radio transmit energy per bit | 35 mJ per 1,800-byte (14,400-bit) transmission at 0 dBm ⇒ ≈2.43 µJ/bit, derived | Soler-Fernández et al., "LoRa Power Model for Energy Optimization in IoT Applications," *Sensors* (MDPI), Jan 2, 2026 ([link](https://pmc.ncbi.nlm.nih.gov/articles/PMC12788325/)) | accessed 2026-09-13 | HIGH (derived from a peer-reviewed, dated measurement) |
| S8 | Outdoor LoRaWAN sensor node battery capacity | 8,500 mAh Li/SOCl2 battery | Dragino — "LSN50-V2 Waterproof Long Range Wireless LoRa Sensor Node" product page ([link](https://www.dragino.com/products/lora-lorawan-end-node/item/155-lsn50-v2.html)) | accessed 2026-09-13 | HIGH |
| S9 | Expected multi-year field life of this class of battery-powered LoRaWAN node | ≈8–10 years | Dragino Documentation Center — "How to calculate battery life of Dragino sensors" ([link](https://wiki.dragino.com/docs/FAQs/battery-life-calculation/)) | accessed 2026-09-13 | MEDIUM (vendor guidance, general rather than device-specific) |

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
