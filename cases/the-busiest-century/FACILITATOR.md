# Guide Notes: The Busiest Century

MS | Guide Notes | Adventure | 2026-27
**Tier:** T2 (MS core) · **Primary metric:** blended headline score of a century = (1 − s) × dates score + s × sites score, each reading scored against the best century on that reading · **Margin:** **3.05% at s = 0.5 — The Sites Wall (B) wins at the starting weight**; margin = (winner − loser) ÷ winner. Reading by reading: the Dates Wall century leads its own reading by **10.15%** (272.0 vs 244.4) and the Sites Wall century leads its own reading by **15.93%** (152.5 vs 128.2).

---

## Status note

Every figure in `case.md` Appendices B–D is derived (not copied) from the New Mexico rows of p3k14c release 2025.07 (CC0, attribution requested) and the IntCal20 curve (Reimer et al. 2020), fetched and recomputed 2026-10-28; the method is in Appendix A and `data/build_derived.py`. Linnea, the museum and the sign-maker are invented. Decision freeze (M0): students hold release 2025.07, which is also the newest release on Zenodo as of 2026-10-28; nothing later exists to withhold, so the Twist below is a **withheld analysis of the same release**, not later data. Full trail: `RESEARCH_LOG.md`, `case.json`.

## Facilitator note (SPEC §6) — read before the room

**This case is about dated samples and the places they came from. It is not about people, and it must never become a ranking of peoples or a population claim.** Say so aloud at the start. Specifically:

- **Not "how many people".** A century with more dates is not a century with more people. The case rule (M6) is that dates also reflect where researchers dug, what survived and what got funded. If a student writes "most people lived here in the 1200s" (or any version of it), stop and ask: "What does one date measure?"
- **Language.** Do not use "vanished", "disappeared", "abandoned", "mystery", "primitive" or "lost civilization". Use "the records show", "dated activity", "places in use". Pueblo and other Native communities are living communities in New Mexico today, and places across this region are part of their history (case.md S6). Do not speculate in the room about who made any site or why a century is quiet.
- **No site names, numbers or locations** appear in the packet or this guide, on purpose (54 U.S.C. § 307103, case.md S7). Do not look any up in the room. If a student asks where the heaviest-dated site is, the answer is: "That is not part of what this case shares."
- **No human remains.** Bone and teeth samples are left out (M1). Do not bring them back in the room.
- Some learners may have family ties to the Pueblos or other Native communities. Do not cold-call anyone to speak for a community.

### Before first use: Pueblo and Native community review (STATUS: NOT YET DONE)

This case has not been reviewed by Native community members. Before it is run with learners (and always before it is run in New Mexico or with Native learners):

1. Send the student packet (`case.md`, the optional extract) and this guide to a Native community contact, for example cultural-resource or education staff of a Pueblo, a Tribal Historic Preservation Officer, or the education staff of the Indian Pueblo Cultural Center in Albuquerque (the Center describes itself as the gateway to the 19 Pueblos of New Mexico). The guide does not claim any of them has agreed to review it.
2. Ask three things: Is the framing ("dated activity", "places in use") acceptable? Are any words or images a problem? Is there anything the case should say about the places that it does not?
3. Apply the changes they ask for (or record, in writing, why not) before the first run, and file the outcome in the RUN_REPORT.

`case.json.community_review` records this as `NOT DONE`. Until it is recorded, treat the case as a draft.

## Argument for A (The Dates Wall)

The Dates reading is the one the field uses for large sets of calibrated dates (a summed probability, case.md S4), and 700–799 leads it by **10.15%** (272.0 vs 244.4 for 1200–1299; 18.2% over 1100–1199's 222.4). The Sites reading counts a site that has one stray date exactly as much as a site that has been studied for decades: **358** of the 863 sites (41.5%) have exactly one date. Among the **87** sites with 10 or more dates (1,685 dates), 700–799 leads **both** readings (dates 154.6 vs 88.4; sites 38.4 vs 36.6), and among the 208 sites with 5 or more dates the Sites reading is a near tie (70.9 for 1200–1299, 68.8 for 1100–1199, 68.7 for 700–799) while 700–799 still leads Dates 201.4 vs 151.0. At weights s below 0.389 the blended score also favours A (at s = 0, by 10.15%). A wall about "the busiest stretch" is a claim about intensity of dated activity, not about the number of rooms in the list.

## Argument for B (The Sites Wall)

The Sites reading leads by **15.93%** (152.5 for 1200–1299 vs 128.2 for 700–799), a bigger gap than A's, and 1200–1299 is second on Dates (only 10.15% behind), while 700–799 is only fifth on Sites. Choosing B gives up less on the other reading than choosing A does. The Dates lead is carried by a few heavily dated sites: the heaviest has 137 dates and supplies 39.2 of the 272.0 (14.4%) in 700–799 but 14.1 of 244.4 (5.8%) in 1200–1299 (see Twist, part 1). A cluster bootstrap over sites (2,000 resamples, seed 20261028, `data/check_figures.py`) has 700–799 ahead of 1200–1299 on Dates in only about 71% of resamples (0.710) but 1200–1299 ahead of 700–799 on Sites in about 98% (0.978). At weights s above 0.389 the blended score favours B (at s = 0.5, by 3.05%).

## Margin

`margin = (winner − loser) ÷ winner`. Per-reading margins above are inside SPEC §2's 20% cap (10.15% and 15.93%). The primary metric is the blended score, in which a student's own weight s decides: the balanced region is the whole range 0 ≤ s ≤ 1, where the margin never exceeds 15.93%.

| s (weight on Sites) | A (700–799) | B (1200–1299) | Winner, margin |
|---|---|---|---|
| 0.0 | 1.0000 | 0.8985 | A, 10.15% |
| 0.1 | 0.9841 | 0.9087 | A, 7.66% |
| 0.2 | 0.9681 | 0.9188 | A, 5.09% |
| 0.3 | 0.9522 | 0.9290 | A, 2.44% |
| 0.4 | 0.9363 | 0.9391 | B, 0.30% |
| 0.5 | 0.9203 | 0.9493 | B, 3.05% |
| 0.6 | 0.9044 | 0.9594 | B, 5.73% |
| 0.7 | 0.8885 | 0.9696 | B, 8.36% |
| 0.8 | 0.8725 | 0.9797 | B, 10.94% |
| 0.9 | 0.8566 | 0.9899 | B, 13.46% |
| 1.0 | 0.8407 | 1.0000 | B, 15.93% |

Break-even weight: s\* = 0.389 (A wins below it, B above it). Ground-truth scores: A dates score 272.0 ÷ 272.0 = 1.0000, sites score 128.2 ÷ 152.5 = 0.8407; B dates score 244.4 ÷ 272.0 = 0.8985, sites score 152.5 ÷ 152.5 = 1.0000. All values above are from the rounded Appendix B figures (the unrounded model gives 3.04% at s = 0.5).

## Ground truth by deliverable

**D1.** Dates top three (centuries start at 0, 100, …): 700–799 (272.0), 1200–1299 (244.4), 1100–1199 (222.4). Sites top three: 1200–1299 (152.5), 1100–1199 (143.6), 900–999 (131.9). Winners on both readings: 700–799 is 272.0 / 128.2; 1200–1299 is 244.4 / 152.5. Gaps as a percent of the larger value: Dates 10.15%; Sites 15.93%.

**D2.** n = 863 sites, 3,616 dates. Smallest 1; Q1 1; median 2; Q3 4; largest 137; IQR 3; fences −3.5 and 8.5; the lower whisker ends at 1 and the upper whisker at 8 (the largest value inside the fences); 103 outlier sites (9 or more dates); mean = 3,616 ÷ 863 = 4.19 dates per site, more than twice the median. Quartile conventions (halves with or without the median, or interpolation) agree here. Expected sentence: a few heavily dated sites can pile dates into whatever century they sit in.

**D3.** Five cuts:

| Cut | Dates winner (lead over runner-up) | Sites winner (lead over runner-up) | Agree? |
|---|---|---|---|
| Centuries from 0 | 700–799, 272.0 (10.15%, runner-up 1200–1299 at 244.4) | 1200–1299, 152.5 (5.84%, runner-up 1100–1199 at 143.6) | no |
| Centuries shifted 50 | 650–749, 272.0 (13.60%, runner-up 750–849 at 235.0) | 1150–1249, 147.4 (7.73%, runner-up 1050–1149 at 136.0) | no |
| Median year | 700–799, 286 (6.99%, runner-up 1200–1299 at 266) | 1200–1299, 154 (5.84%, runner-up 1100–1199 at 145) | no |
| Mean year | 800–899, 274 (4.38%, runner-up 700–799 at 262) | 1100–1199, 156 (7.05%, runner-up 1200–1299 at 145) | no |
| Mode year | 1100–1199, 353 (10.20%, runner-up 900–999 at 317) | 1100–1199, 198 (14.14%, runner-up 900–999 at 170) | **yes** |

What survives: in four of five cuts the readings disagree, with the Dates winner in the 650–899 range and the Sites winner in the 1100–1299 range; the answer "700–799 and 1200–1299" is specific to the aligned, summed-probability cut. What does not survive: the mode cut makes both readings agree on 1100–1199, which is neither reading's winner under the other cuts. Lesson: *the disagreement* is robust; *which century wins* is not.

**D4.** See the Margin table. The sentence is the student's. Look for: names the reading; says "dates" or "places with dated activity", never "people"; one thing it does not claim; a defended s (an s defended with "because the wall is about X" is better than one defended by the result).

**M1 check (bone and teeth left in).** With the 62 samples back in (3,678 dates, 870 sites) the Dates reading gives 280.0 for 700–799 vs 246.1 for 1200–1299 (12.1% gap) and the Sites reading gives 153.1 vs 129.2 (15.6% gap): same winners, slightly wider margins. Do not use this in the room unless a student asks why bone is excluded; the exclusion is a choice about remains, not a result-driven one.

## Five Socratic questions

1. "Your D1 table says the Dates winner gives up 10.15% on dates by choosing the Sites winner, and the Sites winner gives up 15.93% on sites by choosing the Dates winner. Which wrong turn costs the wall more, and who decides?"
2. "Your box plot has a median of 2 dates per site and a mean of about 4.19. What does the gap between them tell you about the Dates reading, and what does the 358-site bar at 1 date tell you about the Sites reading?"
3. "The break-even weight is s = 0.389. What does s = 0.5 say about what 'busiest' means on a public wall, and who would you have to ask before you picked a number?"
4. "In the five-cut table the mode cut puts both readings at 1100–1199. If a colleague had used the mode shortcut, what would their wall say, and what would you tell them?"
5. "Your sentence says 'dates' or 'places with dated activity'. What is one thing a visitor might read into it that the records cannot support?"

## The trap

Two traps, in order of likelihood. **(1) Reading dates as people.** Heroes will write "the most people lived here in the 1200s" or "the busiest century, population-wise". Neither reading counts people; the case rule (M6) says so, and the facilitator note at the top says what to do. **(2) Reading the bigger bar as the truth.** Heroes will take the Dates or Sites winner without asking what each bar counts, and will treat a 10% gap as settled. The fix is D2 (a few sites carry the date counts), D3 (the winner moves with the cut) and D4 (the verdict flips at s = 0.389). A quieter slip: dividing the gap by the loser (11.3% for Dates, 19.0% for Sites) instead of by the larger value; the case states the convention, so ask for it. Another: adding the Sites column down the century rows to "total sites" (a site is counted in every century it is active, so it does not add).

## Twist

At about 15:00, reveal two withheld analyses of the **same release** (nothing later exists; this is a review, per M0). Both ask the same question: *whose sites are in the sample?* Each one removes the lead of one reading; neither makes the other reading obviously right.

**Part 1 — set aside the single most heavily dated site** (137 dates, about 3.8% of all dates, one of 863 sites). Centuries starting at 0:

| Aligned centuries | Dates 700–799 | Dates 1200–1299 | Dates winner | Sites 700–799 | Sites 1200–1299 |
|---|---|---|---|---|---|
| All 863 sites | 272.0 | 244.4 | 700–799 | 128.2 | 152.5 |
| Heaviest site set aside | 232.8 | 241.1 | **1200–1299** | 127.2 | 151.5 |
| Five heaviest sites set aside (379 dates) | 219.3 | 224.9 | **1200–1299** | 124.5 | 149.6 |

With one site set aside the readings **agree** on 1200–1299; the 10.15% Dates lead for 700–799 becomes a 3.4% lead for 1200–1299 ((241.1 − 232.8) ÷ 241.1). Blended at s = 0.5, B then wins by 9.73% (five set aside: 9.65%), up from 3.05% (`sensitivity_model.py`, `evaluate_twist_part1`). This invalidates *"700–799 is the busiest century on the dates reading"* and with it *"the two readings disagree"* as a fact about the dataset. The honest second half: **under the centuries shifted 50 years the Dates winner stays where it was** (650–749 stays ahead: 250.8 vs 228.7 for 1150–1249 with the heaviest site set aside, 231.9 vs 214.3 with five set aside), so one site does not explain the whole 650–749 bump. The aligned-century split depends on one site *and* on where the century edges fall.

**Part 2 — keep only the well-studied sites**, the 87 sites with 10 or more dates (1,685 dates, 46.6% of all dates; 87 of 863 sites, 10.1%). Centuries starting at 0: Dates 700–799 is 154.6 against 88.4 for 1200–1299, and Sites 700–799 is 38.4 against 36.6. **Both readings now name 700–799.** Blended at s = 0.5, A scores 1.0000 and B scores 0.7624 (A wins by 23.76%, scored against the better of the two centuries in this subset; `evaluate_twist`). This invalidates *"the Sites reading is the sturdier one"* and *"1200–1299 is robustly the century with the most places"*. The honest second half again: this is a sample rule chosen after the fact. It discards 776 of 863 sites, which is exactly the breadth the Sites reading exists to count. The result holds under the shifted centuries (both readings name 650–749: Dates 169.2 vs 116.6, Sites 39.9 vs 37.2), and under the median cut; under the mean cut Dates still names 700–799 and Sites ties 700–799 with 800–899; under the mode cut it does not hold.

**What the pair shows together.** The Dates winner depends on a few heavily dated sites; the Sites winner depends on the many sites with one or two dates. Each reading is a statement about *which sites you let in*. Also name the plateau: Dates for 600–1299 stay within about 74% of the top value (200.8 to 272.0), so "busiest" is a ranking inside a long busy stretch, not a spike. Ask: *"What just broke in your model? Were you wrong, or just missing information?"* and *"Would you put one century on the wall, or would the honest sign name a range?"* (The dilemma is binary; the range is a legitimate answer to the second question, not a third option.)

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. Read the Overview aloud. *"One wall, one century. Dates or sites?"* Stand/sit vote, no explanation. |
| **3:00–10:00** | Position defense. *"Convince us, with the numbers, that your reading is the right one for the wall."* Press anyone arguing from "it's bigger": *"Bigger what?"* |
| **10:00–15:00** | Pressure-test. *"Whose position is most fragile? What does your box plot say about your reading?"* |
| **15:00** | **DROP THE TWIST** — the two withheld analyses (heaviest site set aside; well-studied sites only), delivered slowly, full pause before the 60-second recommit. |
| **15:00–20:00** | Immediate recommit. Who reverses? *"What just broke?"* |
| **20:00–30:00** | Two threads: **(1) what a bar counts** — dates, sites, effort, preservation, and why neither counts people; **(2) the cut** — five cuts, one disagreement that survives and a winner that does not. |
| **30:00–45:00** | Close, re-vote against the Anchor 1 board, reflection, lessons learned. |

---

## Guide Notes — the anchor ladder

### Intro
Heroes, a museum has one wall and two honest ways to read the same public records. The numbers are real, they are not people, and they do not settle it.

### Launch
Read the Overview. Show the two option labels only (The Dates Wall, The Sites Wall), not Appendix B. *"Which would you cut into the wall?"*

### Anchor 1 — Take a stand and vote
Dates Wall or Sites Wall. No reasoning yet. Hands up; write the split on the board. *"Is anyone courageous enough to stand with the sites?"*

### Anchor 2 — What is the problem we're solving?
Do not let them calculate. What is "busiest"? Most samples? Most places? Most people? (Park that one: the records cannot say.) Is "a date" even a point in time? *Let the confusion grow: "Wow, this is a hard question to even state."*

### Anchor 3 — What is the process?
If we find the data, how will we decide? Rank the centuries on each reading, compare the winners, test the winners against the way we cut. Is our question still the right question?

### Anchor 4 — What don't we know?
Where researchers have and have not dug; what survived; which projects had money for dating. The weight s is a value judgment. Which of these is most critical, and who could we ask?

## Data Deep Dive
Walk D1–D4 with the ground truth above. Hold the five-cut table until D3 and the two site-sample analyses until the Twist.

## Close
Vote again. Who moved, and why? Was "which century is busiest" the right question, or was it "what do we want the wall to claim"? What math was new, and how did you attack it?

## Lessons Learned
A bar chart is an answer to a question about what is counted. The same records can name different centuries depending on what you count and where you cut. A defended weight is more honest than a hidden one.

## Standards Touched On

**New coverage:** none. The spine has no uncovered skill left (see `case.json.reinforcement_note`). **Reinforced:** How to create a box and whisker plot given a set of data (n=1→2, the thinnest skill reached, forced by D2), Box And Whisker Plot, Quartiles, Outlier, Median, Mean, How to find the mean of a set of data, Percent, How to convert numbers to percents, How to subtract / multiply / divide decimal numbers. **Not claimed:** weighted-mean or equation-solving skills (the D4 break-even may be read from a table), histogram skills (no deliverable asks for one).

## Facilitator note — sensitivity

Applies (SPEC §6 is about illness, money and hardship; here the sensitivity is cultural heritage and living Native communities, handled above). Do not frame the vote as a vote about a people.

## Sensitivity disclosure

The weight s is the load-bearing assumption and flips the verdict inside its stated range (0.25 gives A by 3.79%; 0.75 gives B by 9.66%; see `sensitivity_model.py`). The 3.05% margin is a *starting-value* margin; the case's real answer is the student's defended weight. The three numeric scope limits in M1 (age limits, error ceiling) do not move the winner when halved or raised by half; the bone-and-teeth exclusion is a choice about remains, shown above not to change the winners.
