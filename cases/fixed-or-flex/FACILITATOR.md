# Guide Notes: Fixed Or Flex

MS | Guide Notes | Launchpad | 2026-27
**Tier:** T4 (HS) · **Primary metric:** weighted trips bought per year by the $100,000 = (average trips per $100,000 of that mode) × ρ × w · **Margin:** **6.48% — More Fixed (A) wins at the starting values (ρ_F = ρ_D = w = 1)**, margin = (winner − loser) ÷ winner

---

## Status note

Every figure in `case.md` Appendix A is a real NTD value (dataset `ekg5-frzt`, NTD ID 30044), fetched 2026-10-28 and recomputed in Python; Appendix B is from WCTA's own pages. ρ_F, ρ_D and w are disclosed Modeling Assumptions (Appendix C). Teodora, the board and the $100,000 are invented. Decision-year freeze (M0): students hold report year (RY) 2024 as the latest year. **RY2025 exists in the dataset and is withheld for the Twist.** Full trail: `RESEARCH_LOG.md`, `case.json`.

## Facilitator note (SPEC §6) — read before the room

The vans carry older adults, riders with disabilities and medical-assistance patients. The case compares *service bought per dollar*; it must not become a debate about whose life or trip is worth more. **People are not ranked.** The weight `w` is a value judgment about *access*, meaning how much a trip matters when the rider has no other way to make it and has waited for the booking. Invite students to defend any `w`, including 1.0, and to say who goes without under their choice (the commuter keeps today's last bus; the van rider keeps today's booking wait). Say aloud: a cost per trip is not a measure of a rider's worth. Some learners may have relatives who use these services; do not cold-call anyone for a personal story.

## Argument for A (More Fixed)

At the plain NTD average, fixed route buys **2,698.4 trips per $100,000** against **2,523.7** for vans, so More Fixed wins by 6.48%, and on passenger-miles per $100,000 by 15.70% (34,344 vs 28,952). The signed gap D (vans minus fixed) moved toward fixed every year (+462.8, +160.3, −174.7). The fixed route carries 205,556 trips against 158,133. Fare recovery is a dead heat, so no lens favours the vans except trips weighted by `w`.

## Argument for B (More Flex)

Marginal fixed-route hours are the least productive ones (late evenings, outer branches), so ρ_F below **0.935** is easy to defend, and that alone flips the case. A van trip is door-to-door for a rider who often cannot board a bus, so `w` above **1.069** is defensible, and flips it by itself. Vans won RY2022 and RY2023. Vans buy twice as many revenue hours per dollar (1,137.8 vs 574.4), which matters if the need is coverage and availability.

## Margin

`margin = (winner − loser) ÷ winner` on weighted trips per $100,000. Base case: (2,698.4 − 2,523.7) ÷ 2,698.4 = **6.48%**, inside SPEC §2's 20% cap. The balanced region (|margin| ≤ 20%) at ρ_F = ρ_D = 1 is roughly 0.8 < w < 1.4 (w = 0.8 → A by 25.18%, outside; w = 1.2 → B by 10.90%; w = 1.5 → B by 28.72%, outside). The case is deliberately a **region**, not a point:

| Quantity | Value |
|---|---|
| A wins iff | ρ_F ÷ (ρ_D · w) > 0.9352 |
| Break-even ρ_F (ρ_D = w = 1) | 0.9352 (fixed hours may be 6.5% less productive than average and A still ties) |
| Break-even trips per revenue hour, fixed | 4.393 (today's average 4.698) |
| Break-even trips per revenue hour, vans | 2.372 (today's average 2.218, +6.9%) |
| Break-even w (ρ_F = ρ_D = 1) | 1.069 |
| ρ_F = 0.95 → A by | 1.55% |
| ρ_F = 0.90 → B by | 3.77% |
| ρ_F = 0.85 → B by | 9.12% |
| ρ_F = 0.80 → B by | 14.46% |
| Passenger-miles lens, A by | 15.70% (B's break-even ρ_F = 0.843) |
| Fare revenue per $ of expense | fixed 0.05027, vans 0.05037 (vans higher by 0.20%) |

## Build-up (RY2024) — ground truth for D1

| | A: fixed (MB) | B: vans (DR) |
|---|---|---|
| Cost per revenue hour | $174.09 | $87.89 |
| Trips per revenue hour | 4.698 | 2.218 |
| Revenue hours $100,000 buys | 574.4 | 1,137.8 |
| Trips bought (= trips per $100,000) | 2,698.4 | 2,523.7 |
| Riders' worth (÷ 520) | 5.19 | 4.85 |

History: RY2022 fixed 2,340.4 vs vans 2,803.2 (D = +462.8, vans ahead by 16.51%); RY2023 2,600.4 vs 2,760.7 (D = +160.3, vans ahead by 5.81%); RY2024 D = −174.7. D4 slope: (−174.7 − 462.8) ÷ 2 = **−318.8 per year** (unrounded −318.76). Straight-line projection for RY2025: −174.7 + (−318.8) = **−493.5**.

## Five Socratic questions

1. "Your build-up table says the vans buy 1,137.8 revenue hours for the $100,000 and fixed route only 574.4, yet fixed route carries more trips. Which table row explains that, and what does it tell you about what each dollar buys?"
2. "At starting values More Fixed wins by 6.48%. If added fixed-route hours are only 90% as productive as the average hour, who wins and by how much? What kind of hour would the board actually be adding?"
3. "Your break-even w is about 1.07. Who is a van trip worth more than a bus trip to, and who would you have to ask before you picked a number? What would w = 1.0 say about the riders?"
4. "Your D4 line says the gap keeps moving toward fixed route by about 319 trips per year. How many data points is that built on, and what would you need to see before you trusted it?"
5. "You compared passenger-miles per $100,000 as well. Which yardstick would you fund, trips or miles, and does an unlinked trip count the same thing on a bus with a transfer as on a van?"

## The trap

Heroes will take the NTD averages as the verdict: "fixed route wins by 6%, done." That treats an *average* hour as if it were the *next* hour and treats a van trip and a bus boarding as the same unit. The 6.48% lead disappears if ρ_F drops 6.5% or if `w` rises 7%, both inside the ranges the case invites. The quieter trap is the D4 trend: a straight line through two points looks like evidence, and a Hero who writes "the gap will be −493.5 next year" has confused an extrapolation with a forecast. A second slip: dividing gap by the loser instead of the winner (6.92% vs 6.48%); the case states the convention, so ask for it.

## Twist

At about 15:00, reveal report year 2025 (same dataset):

| | Fixed (MB) RY2025 | Vans (DR) RY2025 |
|---|---|---|
| Operating expense | $8,267,834 | $6,981,124 |
| Revenue hours | 44,819 | 76,918 |
| Unlinked trips | 204,462 | 164,014 |
| Trips per $100,000 | 2,473.0 | 2,349.4 |

Framing (M0 freeze): present this as a review a year later ("the board asks Teodora to come back"), not as data Teodora had; M0 says later figures are a review of the decision after the fact. Tie it to D4's "what two points can and cannot prove". Fixed route still wins, but by **5.00%** (ρ_F* rises to 0.950), and the signed gap is **−123.6**, not the **−493.5** the D4 line predicted. The trend position is invalidated. Then the marginal view: from RY2024 to RY2025, fixed-route hours grew 1,061 and trips *fell* 1,094 (−1.03 trips per added hour, −168.3 trips per added $100,000 on $650,150 of added expense); van hours grew 5,621 and trips grew 5,881 (+1.05 trips per added hour, +822.3 per added $100,000 on $715,163). So neither mode's added hours behaved like the average hour: "added = average" breaks for both. Per added *hour* (the M2-consistent view): ρ_F ≈ −1.03 ÷ 4.698 = −0.22, ρ_D ≈ 1.05 ÷ 2.218 = 0.47; the per-dollar figures above also contain rate growth (cost per hour rose from $174.09 to $184.47 for fixed and from $87.89 to $90.76 for vans), which means M2's constant-cost-per-hour assumption fails in RY2025, so per-hour and per-dollar ρ differ: −0.22 and 0.47 per hour; −0.06 and 0.33 per dollar (both against RY2024 averages). ρ_F is negative, outside the M3 range: one year-over-year difference is a single noisy observation, not an estimate of ρ. This **does not make B obviously right**: it is one year, agency-wide, and the added hours and trips moved for many reasons (2022–2024 were post-COVID recovery years; trips can fall for reasons unrelated to added hours). Have students compare this year's difference with the RY2022→2023 and RY2023→2024 differences they can compute from Appendix A (below). RY2025 figures: dataset `ekg5-frzt`, ntd_id 30044, re-verified live 2026-10-28 (S5). Ask: *"What just broke in your model? Were you wrong, or just missing information?"* and *"Could any one year of increments be an estimate of ρ?"*

Caution: if students compute RY2022→2023 and 2023→2024 increments early, they get vans 3.15 then 0.16 trips per added hour (fixed 40.8, then 29.3, mostly recovery). That swing is itself the discussion: two or three increments are not an estimate of ρ.

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. Read the Overview aloud. *"One pot of money. More buses or more vans?"* Stand/sit vote, no explanation. |
| **3:00–10:00** | Position defense. *"Convince us, with the numbers, that your choice buys more."* Press anyone arguing from sympathy alone: *"Where is your build-up table?"* |
| **10:00–15:00** | Pressure-test. *"Whose plan is most fragile? What does your ρ_F assume about the next bus hour?"* |
| **15:00** | **DROP THE TWIST** — report year 2025, delivered slowly, full pause before the 60-second recommit. |
| **15:00–20:00** | Immediate recommit. Who reverses? *"What just broke?"* |
| **20:00–30:00** | Two threads: **(1) average vs next hour** — "can any amount of history tell you what a new hour will carry?"; **(2) what is a trip worth** — `w`, access, and who goes without under each choice (no ranking of riders). |
| **30:00–45:00** | Close, re-vote against the Anchor 1 board, reflection, lessons learned. |

---

## Guide Notes — the anchor ladder

### Intro
Heroes, a public agency has one pot of new money and two very different services. The numbers are real and public, and they do not settle it.

### Launch
Read the Overview. Show only the one-line descriptions of the two services (Appendix B), not the data table. *"Which would you fund?"*

### Anchor 1 — Take a stand and vote
More Fixed or More Flex. No reasoning yet. Hands up; write the split on the board. *"Is anyone courageous enough to stand with the vans?"*

### Anchor 2 — What is the problem we're solving?
Do not let them calculate. What is the question: most trips? most miles? who has no other option? Is "a trip" even the same thing on both services? *Let the confusion grow: "Wow, this is a hard question to even state."*

### Anchor 3 — What is the process?
If we find the data, how will we decide? Cost per hour, trips per hour, trips per dollar; then what do we do about the fact that the next hour is not the average hour? Is our question still the right question?

### Anchor 4 — What don't we know?
No denied-trip count, no program split of van trips, no marginal-cost split, and `w` is a value, not data. Which assumption is most critical, and who could we ask?

## Data Deep Dive
Walk D1–D5 with the ground-truth tables above. Hold the history table until D4.

## Close
Vote again. Who moved, and why? Was "which service is cheaper per trip" the right question? What math was new, and how did you attack it?

## Lessons Learned
Averages describe the past; decisions buy the next hour. A close case is decided by the assumptions, so say them out loud. A straight line through two points is a guess with a ruler.

## Standards Touched On

**New coverage:** none. The spine has no uncovered skill left (see `case.json.reinforcement_note`). **Reinforced:** How to divide with negative numbers (n=2→3, the thinnest skill reached, forced by the D4 slope arithmetic); How to subtract / add with negative numbers; slope; compound units; percent skills; one-step equations. **Not claimed:** How to multiply with negative numbers (an earlier draft's RY2026 projection was dropped because one year of addition forces no multiplication).

## Facilitator note — sensitivity

Applies (SPEC §6): older adults, riders with disabilities and medical-assistance patients. See the note at the top. Do not frame the vote as "who deserves it".

## Sensitivity disclosure

ρ_F, ρ_D and `w` are the load-bearing assumptions and each flips the verdict inside its stated range (see `sensitivity_model.py`). The 6.48% margin is a *starting-value* margin; the case's real answer is the student's defended triple.
