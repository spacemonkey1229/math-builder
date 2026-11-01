# Case Study: The Sixteenth Land

MS | Math | Case Study | 2026-27 | Launchpad

---

## Overview

The shoebox is open on the folding table, and the garage smells of cold concrete and cardboard dust. Ottoline Prewitt fans her cards face up under the work light, spells on the left and lands on the right, the way her cousin taught her.

Last week she lost a game holding a hand full of spells and nothing to pay for them. The week before she lost holding a hand of lands and nothing worth playing. Both times she shrugged. Neither shrug was convincing.

Her cousin has played since before Ottoline could read. He tapped the table with a screwdriver handle and said it like weather: "Seventeen. Always seventeen." Yesterday a quiet kid at the league, with a battered binder and a deck full of cheap spells, told her the same thing the other way: one fewer, and use the slot for a spell you actually love.

The deck-list form is due at the door of the community hall tomorrow morning, before the qualifier starts, and once she hands it in the list is locked for the whole day. The form has a blank for lands and a blank for spells. The pencil behind her ear has no eraser left.

Upstairs a door closes. The dehumidifier cycles off and the garage goes very quiet. Ottoline counts the lands in the right-hand row out loud, all the way to the sixteenth, and stops there with the next number still in her mouth.

---

## Background

Ottoline Prewitt, 14, is building the 40-card deck she will register for her regional youth league's Saturday qualifier. She is accountable for one thing: the deck-list form, which fixes how many land cards and how many spell cards the deck holds. *(Constructed framing, disclosed: Ottoline, her cousin, the league and the garage are invented for this case. The game is a generic two-player card game described in Appendix A; it is not any particular product.)* The qualifier has no entry fee and no prize, and nothing in this case is for sale.

All her other 23 spell cards are already chosen (SEE APPENDIX B). The only open question is the last slot, and the two lists she can hand in are:

- **The Sixteen-Land List:** 16 lands and 24 spells.
- **The Seventeen-Land List:** 17 lands and 23 spells.

The game's rules, in plain words, are in Appendix A. The tools for counting card combinations are in Appendix C.

**Her yardstick, fixed before any calculation.** Ottoline calls an opening stretch a **smooth start** if, among all the cards she has seen through her **turn 4**, she holds **at least 3 and at most 6 lands**. Three, because her main spells need three lands in play. Six, because with seven or more lands among her first ten or eleven cards she has seen too few spells to use them. She wrote this window down on Friday evening, 30 October 2026, before running a single number, and she treats the two game positions equally (she is on the play half of her games and on the draw half). Her **primary metric** is the probability of a smooth start under that rule, averaged over the two positions (SEE APPENDIX F, assumptions MA2 to MA4).

**Other players disagree about what a smooth start is.** Appendix D lists the other windows and the other turn counts you will be asked to test. The point of testing them is to see how much of any answer comes from the cards and how much from the definition.

Nothing later than Friday 30 October 2026 is available to her: no result of the qualifier appears in this case before the discussion. The Appendices hold the rules (A), her deck and notebook (B), counting tools (C), the windows to test and the margin convention (D), plain-English notes (E), the assumptions (F), the sources (G) and the "How To…" list (H).

---

## Dilemma

You are Ottoline Prewitt.

Do you:

A.) Register the Sixteen-Land List: 16 lands and 24 spells OR

B.) Register the Seventeen-Land List: 17 lands and 23 spells

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. Counting the opening hand: the number of different 7-card hands that can be drawn from the 40-card deck, and, for each list, the number of those hands with exactly 0 lands and with exactly 1 land. Write every count as a product of combination counts C(n, k) = n! / (k! (n - k)!) and evaluate it by cancelling the factorials by hand; show the cancellation for each count (no combinations key and no table for this deliverable).
    D2. The no-play hand: for each list, the probability that the opening 7 cards contain 0 or 1 lands, built from the D1 counts, as a fraction and as a percent. State which list has fewer such hands and by what percent, using the margin convention in Appendix D.
    D3. The primary metric: for each list, the probability of 3 to 6 lands among the first 10 cards (the play) and among the first 11 cards (the draw), each as a sum of terms of the form C(lands, k) x C(spells, cards - k) / C(40, cards). Show one term in full with its factorials; the other terms may be computed with a tool whose formula you name. Then give the average over the two positions and the margin between the lists.
    D4. The window grid: using your D3 terms, the averaged probability for every window and turn count in Appendix D for both lists, which list leads in each, and the margin in each. State how many of the nine windows (at turn 4) each list wins, and separately which list leads at turn 3 and at turn 5.
    D5. A chart of the probability of a smooth start (3 to 6 lands, turn 4) against the number of lands in the deck, from 14 to 19 lands, as one line for the play and one for the draw, with the 16 and 17 marked.
    D6. Inside your pitch, a short statement of the window and turn count you adopt for the decision, your reason for it, and one sentence on what a record of real games (such as Ottoline's notebook, Appendix B) could and could not tell her about the choice.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

### Appendix A: The Game, In Plain Words

This is a generic two-player card game, described only as far as this case needs.

| Rule | Detail |
|---|---|
| Deck | 40 cards, shuffled so every order is equally likely. Each card is a **land** or a **spell**. |
| Lands and spells | A spell is a card that does something useful in the game, such as putting a character on the table or hurting the opponent; what each one does does not matter for this case, only that spells are how a player wins and that each costs power. A land you play stays in play and gives 1 point of power every turn. Power does not carry over: each turn you may spend the power your lands give that turn, on one or more spells, and any unspent power is lost. A spell costs power to play (a 3-cost spell needs 3 lands in play). A player may play at most one land per turn. |
| Opening hand | Both players draw 7 cards. |
| Drawing | The player who goes first is **on the play**; the other is **on the draw**. Each player draws 1 card at the start of each of their own turns, except that the player on the play skips the draw on their very first turn. |
| Cards seen through turn 4 | On the play: 7 + 3 = 10 cards (draws on turns 2, 3 and 4). On the draw: 7 + 4 = 11 cards (draws on turns 1, 2, 3 and 4). |
| Redraws | None. In this case a player keeps the opening hand dealt. |
| Positions | The first player in game 1 is decided by a coin flip. |

*All rules in this table are constructed scenario inputs (SEE APPENDIX F, MA1).*

### Appendix B: Ottoline's Deck And Notebook

**Her 23 chosen spells, by cost in points of power.** (Constructed.)

| Cost | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Number of spells | 3 | 8 | 7 | 3 | 2 |

The Sixteen-Land List adds a 24th spell that costs 2. The Seventeen-Land List adds a 17th land instead. Her plan is to play her 3-cost spells on turn 3.

**Her notebook, last six league games** (constructed; "L16" and "L17" mean the lands in the deck that game):

| Game | Lands in deck | On the | Result | Note |
|---|---|---|---|---|
| 1 | 16 | play | win | |
| 2 | 16 | draw | loss | no lands in the opening 7 |
| 3 | 16 | draw | loss | |
| 4 | 17 | play | win | |
| 5 | 17 | draw | win | |
| 6 | 17 | draw | loss | seven lands in the first 10 cards |

*Her cousin's other advice, "always play the cheapest spell first," does not enter any calculation here.*

### Appendix C: Counting Tools

- **Factorial.** n! means n x (n - 1) x ... x 2 x 1. For example 5! = 120.
- **Combination count.** The number of different ways to choose k cards from n cards, ignoring order, is C(n, k) = n! / (k! (n - k)!). (Invented small example, not from this case: choosing 2 cards from 5 gives C(5, 2) = 5! / (2! x 3!) = 10.) The same quantity is called a binomial coefficient.
- **Hands with exactly k lands.** If a deck has L lands and S spells, the number of different m-card hands with exactly k lands is C(L, k) x C(S, m - k). The number of all m-card hands is C(L + S, m). Every hand is equally likely, so the probability of an event is (hands in the event) / (all hands).
- Because cards are not put back, each draw changes the deck. The counting method above takes account of that; treating every draw as "L out of 40" does not [S1].

*Invented example of a chart (not this case's data): a toy deck of 6 cards, 3 of them lands, and the probability that at least one land appears among the first n cards seen. It shows the style of chart D5 asks for: one point per value on the horizontal axis, points joined by a line, axes labelled.*

<svg viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Chart of an invented toy deck: probability of at least one land against number of cards seen, rising from one half at one card to one at four cards" style="max-width:420px;width:100%;height:auto">
  <line x1="50" y1="180" x2="330" y2="180" stroke="currentColor"/><line x1="50" y1="20" x2="50" y2="180" stroke="currentColor"/>
  <text x="190" y="214" text-anchor="middle" font-size="12" fill="currentColor">cards seen (n)</text>
  <text x="14" y="100" font-size="12" fill="currentColor" transform="rotate(-90 14 100)" text-anchor="middle">P(at least 1 land)</text>
  <polyline points="90,100 150,52 210,28 270,20" fill="none" stroke="currentColor" stroke-width="2"/>
  <circle cx="90" cy="100" r="4" fill="currentColor"/><circle cx="150" cy="52" r="4" fill="currentColor"/><circle cx="210" cy="28" r="4" fill="currentColor"/><circle cx="270" cy="20" r="4" fill="currentColor"/>
  <text x="90" y="196" text-anchor="middle" font-size="11" fill="currentColor">1</text><text x="150" y="196" text-anchor="middle" font-size="11" fill="currentColor">2</text><text x="210" y="196" text-anchor="middle" font-size="11" fill="currentColor">3</text><text x="270" y="196" text-anchor="middle" font-size="11" fill="currentColor">4</text>
  <text x="44" y="184" text-anchor="end" font-size="11" fill="currentColor">0</text><text x="44" y="104" text-anchor="end" font-size="11" fill="currentColor">0.5</text><text x="44" y="24" text-anchor="end" font-size="11" fill="currentColor">1</text>
</svg>

### Appendix D: The Windows To Test, And The Margin Convention

**Windows (lands among the cards seen through turn 4):**

| | at most 5 | at most 6 | at most 7 |
|---|---|---|---|
| **at least 2** | 2 to 5 | 2 to 6 | 2 to 7 |
| **at least 3** | 3 to 5 | **3 to 6** (Ottoline's) | 3 to 7 |
| **at least 4** | 4 to 5 | 4 to 6 | 4 to 7 |

**Turn counts for Ottoline's window (3 to 6):** through turn 3 (9 cards on the play, 10 on the draw) and through turn 5 (11 on the play, 12 on the draw), as well as turn 4.

**Margin convention.** For a probability that higher is better, margin = (leader - other) / leader, as a percent. For a probability that lower is better (the no-play hand), margin = (other - leader) / other. Use unrounded values until the last step.

### Appendix E: Plain-English Notes

| Term | Plain-English explanation |
|---|---|
| Land | A card that gives power each turn once played; it does nothing else. |
| Spell | A card that costs power to play; spells are how a player wins. |
| Power | The currency a player spends each turn to play spells. |
| On the play / on the draw | Going first (skips the first draw) / going second (draws every turn). |
| Opening hand | The 7 cards dealt before the game starts. |
| Flood | Seeing so many lands that there are too few spells to use. |
| Screw | Seeing too few lands to play the spells in hand. |
| Qualifier | A one-day event whose results decide who moves on to the next round of league play. |
| Best-of-three | A match won by the first player to win two games. |
| Deck-list form | A paper form on which a player writes down exactly which cards are in their deck before the event starts. |
| Hypergeometric | Describes drawing cards without putting them back from a deck that has two kinds of card [S1]. |

### Appendix F: Modeling Assumptions

> These figures are **not sourced from the world**. They are stated scenario assumptions chosen by the case author. A Hero may challenge them in discussion, and that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Game rules and deck: 40 cards, opening hand 7, one draw per turn (none on the play's first turn), no redraws, cards drawn in random order | as in Appendix A | A generic card game; the rules are chosen so the case does not depend on any product. | Held fixed; changing them is a different game. |
| MA2 | Window for a smooth start: at least 3 and at most 6 lands | 3 to 6 | Ottoline's rule of thumb from her cost curve (Appendix B) and the two bad games she lost; fixed Friday 30 October 2026 before any calculation. | The answer is sensitive to this value. Other players draw it differently (Appendix D). |
| MA3 | Cards-seen horizon | through turn 4 | The turn by which her deck wants its main spells in play. | The answer is sensitive to this value (Appendix D). |
| MA4 | Share of games on the play | one half | Game 1 is a coin flip; later games are assumed to alternate evenly. | The answer is sensitive to this value. |
| MA5 | The 24th spell | cost 2 | Constructed; Option A needs some spell in the slot. | Only affects the cost-curve story, not the calculation. |
| MA6 | Decision date and information | Friday 30 October 2026; nothing later is known | Freezes the scenario (SPEC 5). | n/a |
| MA7 | The notebook games | six invented games (Appendix B) | Constructed to look like a small real record. | None; they are not used in any calculation. |

### Appendix G: Sources

| # | Claim | Source | Date | Confidence |
|---|---|---|---|---|
| S1 | Probability of k successes in n draws without replacement from a finite population is C(K, k) C(N - K, n - k) / C(N, n); contrast with draws with replacement | Wikipedia, "Hypergeometric distribution" ([link](https://en.wikipedia.org/wiki/Hypergeometric_distribution)), CC BY-SA, cited not copied | accessed 2026-10-28 | MEDIUM |

*Every other figure in this case is a stated scenario assumption (Appendix F) or is computed by you. Search trail: `RESEARCH_LOG.md`.*

### Appendix H: "How To…" Math Questions To Research

**Vocabulary terms**

- Combination
- Binomial Coefficient
- Factorial
- Percent

**"How to…" questions**

- How to determine the number of outcomes of a combination
- How to compute a binomial coefficient
- How to evaluate a factorial expression
- How to determine the probability of a single event
- How to convert numbers to percents
- How to create a scatter plot given a set of data
- How to compare two or more values

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
