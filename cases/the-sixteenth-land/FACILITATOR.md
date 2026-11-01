# Guide Notes: The Sixteenth Land

MS | Guide Notes | Launchpad | 2026-27
**Tier:** T3 (MS-stretch / HS-entry) · **Primary metric:** probability of a smooth start (3 to 6 lands among the cards seen through turn 4), exact hypergeometric, averaged over the play (10 cards) and the draw (11 cards), higher is better · **Margin:** 0.75% (gap divided by the winner's value, the margin convention of Appendix D). The Seventeen-Land List (Option B) is ahead, 0.8510 against 0.8446. **The margin is window-driven:** across the 3x3 window grid in Appendix D the lead changes hands (16 leads in 3 windows, 17 in 6) and the pooled margin runs from 0.14% to 7.72%. Read the sensitivity note before Lessons Learned.

---

## Intro

Heroes, nobody in this room is wrong yet. Two experienced players gave Ottoline two different numbers, and she has to hand in a form by morning. Before we start: this case is about reading probabilities, not about buying cards or winning prizes. There is nothing to buy, nothing to win and nothing to bet. We are asking what "a good start" means and whether the cards, or the definition, is doing the deciding.

## Launch

Draw two columns on the board, "16" and "17". Put one question to the room: *"Last week Ottoline lost holding no lands. The week before, holding nothing but lands. Which loss should she fear more?"* Take thirty seconds of answers, then: *"She has to pick one number tonight. Her cousin says 17. A kid at the league says 16."*

> **Hero name: Sixteen or Seventeen? Commit out loud.**

Teach-from-scratch note: many Heroes will not have played a card game. Walk through Appendix A on the board with a real shuffled stack of ordinary playing cards (red cards as lands, black as spells) and deal an opening seven. Do not skip the play/draw distinction: the 10-versus-11 cards is the first place the case can be mis-set.

---

## Anchor 1 — Take a stand and vote

Option A (Sixteen-Land List) or Option B (Seventeen-Land List). No reasoning yet.

Hands up for A. Hands up for B. Write the split on the board.

*"Is anyone courageous enough to stand with the sixteen?"*

## Anchor 2 — What is the problem we're solving?

Do **not** let them start computing yet.

- What is the question in one sentence? "Which list gives her the most lands?" "Which list avoids the no-play hand?" "Which list has the fewest floods?" "Which list wins more?" Those sound alike and are not the same question.
- Someone will say "more lands is safer." Push: *"Safer against what?"* Do not rescue them.
- Someone will say "17 because the experienced player said so." Push: *"Does an expert's rule of thumb tell us what Ottoline's deck needs?"*
- Is "a smooth start" a fact about the cards, or a choice we made?

> Let the confusion grow. Say it out loud: *"Huh. 'Which is better' depends on what we count as a good start."*

**The trap to let them walk into (four forms).** (0) Stopping at the opening-hand number: D1 and D2 come first and are the vivid ones, so a hurried Hero sees 13.41% against 10.52% (17 has 21.54% fewer no-play hands) and writes *17 is clearly better, about 21.54% better.* The yardstick is the 3-to-6 window, where the lists are within 0.75%, and the opening-hand number ignores flood entirely. (1) Most Heroes compute D3 with Ottoline's window, see the Seventeen-Land List ahead by 0.75%, and stop: *17 wins.* They miss that the 0.75% is the smallest margin in the grid and that the sign changes when the window or the turn count changes. A recommendation that never says why it adopts one window has not answered the question. (2) Drawing with replacement: using "17/40 per card" (a binomial with p = 17/40) instead of counting hands. That gives 0.7940 (play) and 0.7777 (draw) for 17 lands and 0.7779 and 0.7817 for 16, all about six points too low. The structure is wrong, not just the size. (3) Setting the window after seeing the result: picking 4-to-7 because it makes the favourite win. D6 asks them to say which window they adopt and why *before* they defend the answer. Arithmetic slips to watch: using 10 cards for both positions, forgetting the play skips the turn-1 draw, adding the play and the draw instead of averaging them, and computing the margin from rounded values (0.85 against 0.84 gives 1.2%, not 0.75%).

## Anchor 3 — What is the process?

- If we have the full distribution of lands among 10 and 11 cards, how do we get the probability for any window? (Sum the terms.)
- How do we combine the play and the draw? What does "half and half" assume? (MA4.)
- How do we compare two lists on a window, and what do we divide by? (The margin convention.)
- Is our question still the right question?

## Anchor 4 — What don't we know?

- Which assumptions are choices? (The window, the turn count, the play share, no redraws.) Which one did Ottoline fix before computing, and does fixing it first make it right?
- If Ottoline's notebook shows 3 wins in 6 games with 17 lands, what does it tell us? (Almost nothing; see the notebook note below.)
- Are better players more likely to run a certain land count? What would that do to any record of wins?

---

## Data Deep Dive

Now the numbers. Work them on the board with them.

**Step 1: counting hands (D1).** C(40,7) = 18,643,560 different opening hands. For the Sixteen-Land List (16 lands, 24 spells): 0 lands is C(16,0) x C(24,7) = 1 x 346,104 = 346,104 hands; 1 land is C(16,1) x C(24,6) = 16 x 134,596 = 2,153,536 hands. For the Seventeen-Land List (17 lands, 23 spells): 0 lands is C(17,0) x C(23,7) = 245,157; 1 land is C(17,1) x C(23,6) = 17 x 100,947 = 1,716,099. (Exactly 2 lands is 5,100,480 and 4,576,264 hands, not asked for.)

**Step 2: the no-play hand (D2).** 16 lands: (346,104 + 2,153,536) / 18,643,560 = 2,499,640 / 18,643,560 = 0.134075 (13.41%). 17 lands: (245,157 + 1,716,099) / 18,643,560 = 1,961,256 / 18,643,560 = 0.105198 (10.52%). Fewer such hands is better, so the Seventeen-Land List leads, by (0.134075 - 0.105198) / 0.134075 = **21.54%**. This is a secondary measure and it is the one place a margin exceeds the 20% line; it is one failure mode, not the primary metric.

**Step 3: the primary metric (D3).** Denominators: C(40,10) = 847,660,528 (play, 10 cards) and C(40,11) = 2,311,801,440 (draw, 11 cards). Numerators (sum for 3 to 6 lands): 16 lands, play 709,533,440, draw 1,970,060,400; 17 lands, play 724,770,112, draw 1,957,987,240.

| | play (10 cards) | draw (11 cards) | averaged |
|---|---|---|---|
| 16 lands | 0.8370 | 0.8522 | 0.8446 |
| 17 lands | 0.8550 | 0.8470 | 0.8510 |

Margin on the average: (0.8510 - 0.8446) / 0.8510 = **0.75%**, Option B ahead. On the play B leads by 2.10%; on the draw A leads by 0.61%. The play share at which the two lists tie is 22.5% (13123/58291): B leads whenever Ottoline is on the play in more than about a fifth of her games.

**Step 4: the window grid (D4)**, averaged over the two positions, turn 4:

| window | 16 lands | 17 lands | leads | margin |
|---|---|---|---|---|
| 2 to 5 | 0.8068 | 0.7596 | 16 | 5.84% |
| 2 to 6 | 0.9306 | 0.9144 | 16 | 1.75% |
| 2 to 7 | 0.9706 | 0.9719 | 17 | 0.14% |
| 3 to 5 | 0.7208 | 0.6963 | 16 | 3.40% |
| **3 to 6** | 0.8446 | 0.8510 | 17 | 0.75% |
| 3 to 7 | 0.8846 | 0.9086 | 17 | 2.64% |
| 4 to 5 | 0.5174 | 0.5258 | 17 | 1.60% |
| 4 to 6 | 0.6412 | 0.6805 | 17 | 5.78% |
| 4 to 7 | 0.6812 | 0.7381 | 17 | 7.72% |

16 leads in 3 of 9 windows, 17 in 6. Pattern: windows that tolerate only two lands, or cap the top at five, favour 16; windows that demand four lands favour 17. Turn counts for 3 to 6: through turn 3, 17 leads (0.8397 against 0.8123, 3.27%); through turn 5, 16 leads (0.8432 against 0.8252, 2.13%). Per-position margins in the grid reach 9.05% (window 4 to 7 on the play); none reaches 20%.

**Step 5: the chart (D5)**, window 3 to 6, turn 4: play 14 / 15 / 16 / 17 / 18 / 19 lands = 0.7627, 0.8061, 0.8370, 0.8550, 0.8599, 0.8518; draw = 0.8156, 0.8418, 0.8522, 0.8470, 0.8266, 0.7920; averaged = 0.7892, 0.8240, 0.8446, 0.8510, 0.8433, 0.8219. The **play** curve peaks at 18 lands (0.8599) and the **draw** curve peaks at 16 (0.8522); the averaged curve peaks at 17. So 17 is the best averaged value on this window, but the ballot is binary and 18 is better than both on the play: do not say 18 "loses to both".

**Step 6 (D6): a notebook is not evidence.** Six games cannot separate two lists whose probabilities of a smooth start differ by under one percentage point; even many hundreds of real games would be confounded because players who choose different land counts also differ in skill and in the rest of the deck.

---

## Twist

Saturday morning at the hall door. The organiser pins the format card to the wall. Read it slowly: *"At the start of each game any player may shuffle away their opening seven and draw a fresh seven, once, free of charge. The second seven must be kept."* Add the rule Ottoline uses: she redraws exactly when the opening seven has 0, 1, 6 or 7 lands. **State two conventions aloud before they compute, or the room will report different margins:** the discarded seven is shuffled back into all 40 cards, and the discarded cards do not count as 'cards seen' (the metric still counts the final 10 or 11 cards). Say plainly that the twist overrides the 'no redraws' rule of Appendix A (MA1). Under other readings the winner still flips to the Sixteen-Land List but the margin changes: discards counted as seen, 1.5% to 1.7%; second seven drawn from the remaining 33 cards, 1.0%.

Ask them to redo D3 with the redraw. (Sum over first hands: keep a 2-to-5-land hand and draw 3 or 4 more cards from the remaining 33; redraw otherwise and treat the second seven as a fresh deal from all 40.) The answer: on the 3-to-6 window the averaged probability is **0.8998 (16 lands)** against **0.8949 (17 lands)**. The Sixteen-Land List now leads by **0.54%**. The two lists move up by about five points and the lead changes hands. The advantage of 17 was largely the screened-out no-land hands, and a free redraw removes them.

How the twist holds up: with a looser redraw rule (only 0 or 1 lands) 16 still leads, 0.8933 to 0.8845 (0.99%); with redraw also on 2 lands (0, 1, 2, 5, 6, 7) the two are tied to a hundredth (0.9058 against 0.9052, 0.07%, 16 nominally ahead). It does not flip every window: for 4 to 6, 17 still leads (0.7419 against 0.7127, 3.93%), and for 2 to 6, 16 leads more (2.04%).

Then: *"Sixty seconds. Are you changing your list, or not?"* The twist invalidates "17 is better because it avoids the no-land hand" without making 16 obviously correct.

Follow-up, the whole point: **"What just broke in your original model? Were you wrong, or were you just missing information?"**

**Optional extension (a plan only; nothing here was analysed).** Ask: if we had records of many thousands of real games with decks of different land counts, what would we compute, and what would the result be confounded by? A public dataset of this kind exists; its licence was not confirmed and no file was downloaded for this case, so the guide must not quote a win-rate figure from it. If a guide runs this, they should check the licence first, and compute win rate by land count with a confidence interval, and bring the confounders: skill of drafter, curve of the deck, play versus draw.

---

## Deep conflict — threads (20-30 min)

**Thread 1 — What counts as a good start?** *"Ottoline fixed her window before she computed. Is that principle enough? What if she had chosen differently?"* Push toward: the window should come from the deck's needs (her cost curve, Appendix B), and the case shows it can flip the result; a defence is a reason for the window, not just a result.

**Thread 2 — Which failure can the deck afford?** *"The Seventeen-Land List has 21.54% fewer no-play hands. The Sixteen-Land List has an extra spell. Which cost is worse for this deck, this week?"* Compare the 21.54% (secondary) to the 0.75% (primary); is the primary the right yardstick?

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00-3:00** | Cold-call launch. *"Thirty seconds: sixteen or seventeen?"* Two or three learners, fast. Stand/sit vote, no explanation yet. |
| **3:00-10:00** | Position defense (pre-twist). *"Convince us it's better, not just different."* · *"Which window, and why that one?"* |
| **10:00-15:00** | Pressure-test the models. *"Whose recommendation is most fragile?"* · *"What single choice does your argument depend on most?"* |
| **15:00** | **DROP THE TWIST.** Slowly, with pauses. Finish with: *"Sixty seconds. Are you changing your list, or not?"* |
| **15:00-20:00** | Immediate recommit. Who reverses? *"What just broke?"* |
| **20:00-30:00** | The two threads: what counts as a good start · which failure can the deck afford. |
| **30:00-45:00** | Close, re-vote, reflection, lessons learned. |

---

## Socratic questions (each answerable only with the case's numbers)

1. Your D3 puts the Seventeen-Land List ahead by 0.75% on Ottoline's window. Which window in the grid gives the largest lead, and for whom?
2. On the play the Seventeen-Land List leads by 2.10%, on the draw the Sixteen-Land List leads by 0.61%. What share of her games would she need to be on the play for the two to tie?
3. The Seventeen-Land List has 21.54% fewer no-play hands. Why is that not the primary metric, and would you change your answer if it were?
4. Through turn 3 the Seventeen-Land List leads; through turn 5 the Sixteen-Land List does. What does that say about what Ottoline's deck needs, and when?
5. After the redraw rule the lead changes hands by 0.54%. Was your original choice wrong, or did you lack information?

---

## Close

- **Vote again.** Compare to the Anchor 1 board. Who moved?
- We asked ______ as our key question. Was it the right one?
- What math was new to you here, and how did you attack it?
- If you got a case like this again, what would you check first?

## Lessons Learned

Two lists can differ by under one percentage point on a stated yardstick and swap places when a definition is changed: the window, the turn count or the share of games on the play. The margin here (0.75%) is a product of the definition as much as the cards. A recommendation must therefore say what a good start is and why, and it must say what real results could not tell it. In the grid the lead changes hands, the pooled margin runs from 0.14% to 7.72%, and after a free redraw the lead changes hands again. All of that is true at once. The margin is stable to the 20% cap inside the grid but the answer is not stable to the window; the case discloses this in `case.json.sensitivity_disclosure[]`.

## Standards Touched On

**Combination · Binomial Coefficient · Factorial · Percent · How to determine the number of outcomes of a combination · How to compute a binomial coefficient · How to evaluate a factorial expression · How to determine the probability of a single event · How to convert numbers to percents · How to create a scatter plot given a set of data · How to compare two or more values.**

See `LEARNING_GOALS.md` for the forces-test and `case.json.reinforcement_note` for why `new_coverage[]` is honestly empty.

---

## Facilitator note — SPEC §6 (games, money, and minors)

The protagonist is 14 and the learners may be minors. This case is about card-game deck construction and reading probabilities. It has **no wagering, no prizes, no entry fees and no booster-pack or card purchases**, and nothing in it is marketed to anyone. Keep it that way: do not let the discussion turn into "which cards are worth buying" or "how to win a tournament". If a Hero brings up gambling, name the difference plainly: here nothing is staked. Real pack opening and trading-card collecting have a gambling-like structure; this case is not about that. The scene is constructed (Ottoline, her cousin, the league); no real player is portrayed. No illness, death or family-hardship content, but a lost game can feel bad; avoid framing a loser as "unlucky" or "bad".

## Sensitivity note (facilitator only, do not read aloud)

The margin on the primary (0.75%) is the smallest in the window grid except for 2 to 7 (0.14%). It depends on the window, the turn count and the play share. Flexing each stated assumption by 50% (sensitivity_model.py): window lower bound 3 to 1.5 (rounds to 2) gives window 2 to 6, 16 leads (1.75%); to 4.5 (rounds to 4) gives 4 to 6, 17 leads (5.78%). Upper bound 6 to 3 gives 3 to 3 (exactly three lands): 16 leads at 16.20%; 6 to 9 gives 17 leading (3.25%). Turn 4 to 2: 17 leads (5.51%); to 6: 16 leads (5.33%). Play share 0.5 to 0.25: 17 leads by 0.07%; to 0.75: 17 leads by 1.43%. So the verdict flips under the window and turn flexes; it does not under the play-share flex in either direction (and only below 22.5% does 16 lead). Narrow windows outside the Appendix D grid can exceed the 20% line (for example 1 to 2 lands: 27.92%), which is why the grid is limited to windows with a lower bound of 2 to 4 and an upper bound of 5 to 7. Deck size, hand size and the land counts are rules of the game, not assumptions, and are not flexed. The case flags the instability rather than hiding it. Cited data: only the hypergeometric formula (S1); P6 covers it.

**Notebook note.** Appendix B's six games (16 lands: 1 win and 2 losses; 17 lands: 2 wins and 1 loss) are invented noise. They cannot support any conclusion at this margin and are in the case so that D6 can say so.
