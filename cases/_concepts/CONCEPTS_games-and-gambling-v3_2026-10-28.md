# CONCEPTS: games-and-gambling v3 - 2026-10-28

Tags: **[CONFIRMED]** fetched this session; **[DERIVED]** computed in python this session from fetched/constructed inputs; **[ASSUMPTION]** disclosed scenario input; **[UNVERIFIED]** not fetched/confirmed.
Domain: `games-and-gambling` (cluster Culture, Play & Performance). Existing cases read/avoided: casino-owner (card tables vs video machines, house edge), dice-roll (sampling), heist, the-bracket-bet/-cliff (IRA / ACA, not games), the-yield-die (chips), the-odd-lot. Grep of `cases/*/case.md`, `readmodel/cases_index.json` and `cases/_concepts/` found no twin of any concept below, and 0 hits for the three protagonist surnames (Prewitt, Tolliver, Abara) or first names (Ottoline, Rashida, Soren).

**Margin convention (used everywhere).** margin = (winner - loser) / winner on the stated metric (for "lower is better" metrics: (loser - winner) / loser). Secondary-metric margins are labeled secondary.

**Rejected during brute force (kept here so it is not re-proposed): Wordle opening word.** Fetched the original 2,315-word answer list and 10,657 allowed guesses [CONFIRMED, GitHub gists by cfreshman], built the full 12,972 x 2,315 feedback matrix, and played every opener against every answer with a greedy, hard-mode-legal follow-up policy [DERIVED]. All top-100 openers sit within about 1.5% of each other on mean guesses (SLATE 3.5283, SALET 3.5292, TRACE 3.5335, CRANE 3.5438, ROATE 3.5836, ADIEU 3.7555). The Pareto set on (mean, solved in <=3, failures >6) is SLATE/SALET/TRACE/SLANE/TEALS; any pair is either dominated (SLATE dominates CRANE and ADIEU on all three) or "wins" only by 1-3 words of 2,315 failures (noise). No pair passes "both win somewhere with real margin", and the ranking depends on the follow-up policy. Not proposed.

---

## C1 (RECOMMENDED). The Sixteenth Land   ·   tier T3   ·   card-game deck balance

**Protagonist.** Ottoline Prewitt, 14, building a 40-card deck for her regional youth league's Saturday qualifier. (Fictional; 0 hits in corpus.)

**Overview-level story (no numbers).** Friday night, her cousin's garage, a shoebox of sleeved cards spread across a folding table. Ottoline has 23 playable cards she loves and a pile of lands; the deck needs 40. Last week she lost a game holding seven cards and zero lands, and the week before she lost holding five lands and nothing to cast. Her cousin says "always 17"; a player at the league says the deck is so cheap it only needs 16. The 40-card deck-list form is due at the door at 9:00 a.m. Ends with her sliding one land out of the sleeve rack and holding it half-in, half-out (not a phone buzz, not pen over paper).

**Background constraints (all constructed, frozen).**
- 40-card deck, no duplicates beyond the list, all cards identical in function except land vs. spell [ASSUMPTION: generic card game; case does not need brand card text]. Opening hand 7, one draw per turn; on the play skips the turn-1 draw.
- Option label counts: A = 16 lands + 24 spells; B = 17 lands + 23 spells.
- Her deck's cost curve (stated scenario): wants 4 land drops by turn 4 and gets clumsy with 7+ lands in the first 12 cards [ASSUMPTION].
- The qualifier is best-of-three; the game-1 first player is a coin flip, so she is on the play or on the draw half the time [ASSUMPTION].
- Decision date: the Friday before the qualifier; no result of the qualifier appears before the Twist.

**The dilemma.**
You are Ottoline Prewitt.
Do you:
A.) Register 16 lands and 24 spells OR
B.) Register 17 lands and 23 spells.

**Primary metric (fixed before looking at sensitivity).** P(smooth start) = probability that the cards seen through turn 4 (10 cards on the play, 11 on the draw) contain between 3 and 6 lands inclusive. Exact hypergeometric, 40-card deck.

**Computed [DERIVED, python, exact].**
- Window 3-6 lands through turn 4: on the play, 16 lands 0.8370 vs 17 lands 0.8550 (17 wins by 2.1%); on the draw, 16 lands 0.8522 vs 17 lands 0.8470 (16 wins by 0.6%); pooled 50/50: 0.8446 vs 0.8510 (17 by 0.8%).
- Secondary, opposite directions: P(0 or 1 land in opening 7) 13.41% (16) vs 10.52% (17) - 17 better by 21.5%; P(>=7 lands in first 12 cards) 11.61% (16) vs 16.43% (17) - 16 better by 29.3%; expected spells in first 11 cards 6.60 vs 6.325 - 16 better by 4.2%; P(opening 7 has 2-5 lands) 85.50% vs 87.85% - 17 better by 2.7%.
- **Hidden-dominance check (every land count 14-19, four windows x play/draw = 8 cells).** More lands monotonically lowers screw and raises flood, so no count dominates; the "smooth" metric peaks at 16 (draw, 3-6 window), 17 (play, 3-6) or 18-19 depending on window. Cells where 16 beats 17: 2 of 8 (draw/3-6, draw/4-5), margins 0.6% and 0.8%; 17 wins the other 6 with margins 2.1% to 9.1% (largest: window 4-7 on the play, 0.6990 vs 0.6357). Maximum margin in any cell <= 9.1%, well under 20%. **Disclosure:** the 3-6 window was chosen as the primary; the sensitivity table (4-6, 4-7, 4-5) favors 17 more often, which the case should show, not hide: the answer is definition-dependent, and that is the argument.
- 15 and 18 are not on the ballot (binary), but are shown as extra rows: 15 loses to both on screw; 18 loses to both on flood.

**Why it works.** Each side has a number: 17 = fewer no-land hands and better on the play; 16 = fewer floods, one more spell, and better on the draw. The student must say which failure (screw or flood) the deck can afford and whether to trust a window they chose. Shape: metric-choice / definition-dependent, not a single break-even.

**Deliverables (each forces math).**
1. Count the possible 7-card hands: C(40,7) = 18,643,560, and the hands with exactly 2 lands for 16 and 17 lands (binomial coefficients by hand or with a stated formula).
2. P(0-1 lands in opening 7) for each option from combination counts.
3. P(3-6 lands in the first 10 and 11 cards) for each option (sum of hypergeometric terms; may use a supplied table of C(n,k) for the large numbers).
4. A plot of P(smooth) vs land count 14-19 for play and draw, with 16 and 17 marked.
5. A memo paragraph choosing a window and defending it, plus one sentence on what real game results could and could not tell her (confounding: better players may run different land counts).

**Spine skills (only those the deliverables force; ids verified in standards_spine.json).**
- `statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination` (n=2): deliverables 1-3.
- `discrete-mathematics-binomial-coefficient` (term, n=2) and `discrete-mathematics-how-to-compute-a-binomial-coefficient` (n=2): deliverable 1.
- `advanced-operations-how-to-evaluate-a-factorial-expression` (n=3): deliverable 1 (C(n,k) from factorials).
- Not claimed: `independent-event` (hypergeometric draws are dependent; claiming it would be wrong).

**Twist (post-decision; later data only here).** Show 17Lands public draft game records [UNVERIFIED, full-file analysis not run]: observed win rate by land count for a set, then ask whether the model's near-tie shows up and why observed win rates are confounded (better drafters, different curves). Optionally: she keeps going 0-2 on one land count after 12 games - how many games would tell a 1% edge from noise?

**Facilitator note (SPEC 6).** Card-game deckbuilding only; no wagering, no booster-pack-opening/"chase rare" framing. Keep it about reading probabilities, not buying cards.

**Data feasibility - HIGH for the math, MEDIUM for the real-data Twist.**
- The core is exact combinatorics; no external data needed.
- 17Lands public datasets: [CONFIRMED] `https://17lands-public.s3.amazonaws.com/analysis_data/game_data/game_data_public.{DMU,NEO,BRO,MOM}.PremierDraft.csv.gz` return HTTP 200 (DMU 81,110,022 bytes; NEO 43,549,860; BRO 40,827,409; MOM 96,232,781). A 3 MB range sample parsed (35,283 game rows; columns include `won`, `on_play`, `num_mulligans`, `deck_<card>`, `opening_hand_<card>`). **Not analysed** (full files not downloaded; a download needs explicit user permission). **[UNVERIFIED]**: licence (believed CC BY 4.0, 17lands.com page is JS-rendered and could not be read), how to identify nonbasic lands from deck_ columns (needs 17Lands cards file), and the actual win-rate gap by land count.

---

## C2. The Bigger Jackpot   ·   tier T3-T4   ·   lottery design as public finance

**Protagonist.** Rashida Tolliver, a game-design analyst at a multi-state lottery association, July 2015. (Fictional; 0 hits.) She is not selling anything; her job is to make a recommendation about the draw-game format.

**Overview-level story (no numbers).** A conference room, a whiteboard with two ball-count grids, and a spreadsheet of states' education-fund transfers that rise and fall with how big the headline jackpot is. A colleague says bigger jackpots mean more beneficiary dollars; another points out that most players only ever see the small prizes. Ends on the whiteboard magnet for the 69-ball pool sitting in her hand, not yet placed on the grid.

**Frozen decision date.** Announcement window July 2015; effective date of the real change was 2015-10-04 (Wikipedia Powerball; not shown to students as the answer). Nothing after July 2015 appears before the Twist.

**The dilemma.**
You are Rashida Tolliver.
Do you:
A.) Keep the current 5-of-59 white balls + 1-of-35 red Powerball format OR
B.) Move to 5-of-69 white balls + 1-of-26 red Powerball.

**Primary metric.** Expected fixed-prize return per $2 ticket, excluding the jackpot (what a typical player actually gets back).

**Computed [DERIVED, python, from combination counts and the pre-/post-2015 fixed prize tables].**
- C(59,5) x 35 = 175,223,510 vs C(69,5) x 26 = 292,201,338 jackpot combinations (match the published odds).
- Fixed-prize return per ticket (prizes: $4, $4, $7, $7, $100, $100, 4+PB $10,000 old / $50,000 new, 5+0 $1,000,000; no Power Play): old 36.05 cents vs new 31.99 cents. **A wins by 11.3%.**
- P(win any prize): old 3.140% (1 in 31.85) vs new 4.021% (1 in 24.87): B wins by 21.9% (secondary, just over the 20% line; reported, not the primary).
- P(at least one jackpot winner in a draw) at 40 million tickets: old 20.4% vs new 12.8% (A by 37%, secondary). At 20M: 10.8% vs 6.6%; at 80M: 36.7% vs 24.0%.
- Hidden-dominance check: only two formats exist on the ballot; neither wins every lens (A: return, jackpot-hit frequency; B: any-prize frequency, longer rollover runs to bigger headlines). Third formats (e.g., 5/62) are out of scope and noted as such.

**Why it is close / what the student must defend.** For A: players keep more of each ticket and the jackpot is hit more often. For B: players win something more often and rollovers build bigger headline jackpots that the association believes raise sales for beneficiaries. The unresolved variable - how sales respond to jackpot size - is not in the primary metric; the student has to state and defend an assumption. Shape: definition-dependent (whose welfare counts: player, or fund beneficiary).

**Deliverables.** (1) Compute both jackpot odds with combination counts; (2) compute P(4+PB), P(5+0) for each; (3) compute the fixed-prize return for each from the tables; (4) sketch P(jackpot hit) vs tickets sold for both formats (exponent form); (5) one-paragraph memo stating the sales-response assumption (e.g., jackpot size x sales) the B case needs, with a break-even stated as a percent change.

**Spine skills.** `statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination` (n=2), `discrete-mathematics-how-to-compute-a-binomial-coefficient` (n=2), `fractions-how-to-multiply-two-fractions` (n=2; probability of a white-ball match x red match). Verify at write time.

**Twist.** Jan 2016: the new format produced a record jackpot of about $1.586B after a long rollover run (Wikipedia: 20 consecutive rollovers, three winning tickets) [UNVERIFIED primary; secondary news cites]. Ask: did the design objective come true, and for whom?

**Facilitator note (SPEC 6).** Gambling-adjacent. Frame strictly as analysis of the game's odds and public-finance design. Do not ask students to pick numbers, estimate how much they would spend, or imagine winning. Note gambling harms and that many players are low-income; avoid anything that glamorizes play. The case does not market lotteries to minors.

**Data feasibility - HIGH for current format; MEDIUM for pre-2015 tables.**
- [CONFIRMED] `https://www.powerball.com/powerball-prize-chart` (HTTP 200): current odds 1 in 292,201,338; 1 in 24.87 any prize.
- [CONFIRMED, secondary] Wikipedia Powerball raw wikitext (fetched): old matrix 5/59 + 1/35 (Jan 19, 2014 to Oct 3, 2015) with prize table and odds (1 in 175,223,510); 2015 change text. Licence CC BY-SA; cite MUSL tables rather than copy prose.
- **[UNVERIFIED]:** original MUSL pre-2015 prize table (Wikipedia only), Powerball sales vs jackpot history (needed for any quantitative sales assumption), beneficiary-fund amounts. Case would present sales response as a Modeling Assumption unless a dated source is fetched.

---

## C3. Eight Seats   ·   tier T3   ·   tournament format (esports / school league)

**Protagonist.** Soren Abara, a student organizer at a school esports club running an 8-team bracket day. (Fictional; 0 hits.)

**Overview-level story.** The gym is booked 9 a.m. to 3 p.m., there are eight consoles, and the club's best team lost to the bottom seed in a scrimmage last week; the bottom seed's captain has asked whether the format guarantees everybody a second chance. Ends at the bracket poster with two tape lines drawn, a single and a double.

**The dilemma.**
You are Soren Abara.
Do you:
A.) Run a single-elimination bracket where every match is best-of-three OR
B.) Run a double-elimination bracket where every match is a single game.

**Primary metric.** Probability that the strongest team is crowned champion, using team strength modeled on the Elo expected-score formula p = 1/(1 + 10^((Rb-Ra)/400)), rating spread between seeds fixed at 50 points before looking at results, standard 1v8/4v5/2v7/3v6 seeding [ASSUMPTION].

**Computed [DERIVED, python, exact enumeration].**
- Spread 50: A 0.516 vs B 0.465 (A wins by 9.9%). Spread 25: 0.344 vs 0.304 (11.6%). Spread 75: 0.629 vs 0.582 (7.5%). Spread 100: 0.709 vs 0.669 (5.6%).
- Expected games played: A 16.7 vs B 14.5 (B uses 13.6% fewer); maximum games: A 21 vs B 15. B wins on time/budget; A wins on the primary.
- Hidden-dominance check: groups-of-4 then knockout (15 games) was also tested and loses accuracy by 25-30% to A at the same spreads, so it is not on the ballot. **Weak point:** B's only demonstrated win is time/worst-case length, not an accuracy-type metric; a second lens where B wins (e.g., P(strongest team finishes top 2) or "second chance" fairness) was NOT computed and must be added before this goes forward. Rank 3 for that reason.

**Spine skills (to verify):** `statistics-and-probability-independent-event` (n=2) - multiplying match probabilities along a bracket path; `fractions-how-to-multiply-two-fractions` (n=2).

**Twist.** After the day: the strongest team wins both ways but the third seed wins the single-elim sibling bracket on another campus - small-sample luck vs format.

**Facilitator note.** No gambling or betting pools; ratings are scenario inputs, not real players. Avoid framing losers as "bad".

**Data feasibility - MEDIUM.** Elo formula is public knowledge [no fetch needed]; rating spreads are a disclosed assumption; real esports bracket structures (e.g., double elimination at large events) would need a named, fetched source. FIDE January 2024 top-10 ratings (2830 to 2749) were fetched from Wikipedia "Candidates Tournament 2024" [CONFIRMED] as a real-world spread benchmark (about 9-10 points per rank), far narrower than the 50-point scenario; not used.

---

## Ranking summary

| Rank | Concept | Skills closed (thin n<=2) | Data | Balance |
|---|---|---|---|---|
| 1 | C1 The Sixteenth Land | 4 (combination how-to, binomial term + how-to, factorial how-to n=3) | HIGH math / MEDIUM real data | Margin <=9.1% in all 8 cells; 16 wins 2 cells, 17 wins 6; no dominance |
| 2 | C2 The Bigger Jackpot | 3 | HIGH current / MEDIUM history | Primary 11.3% (A); B wins any-prize by 21.9% (secondary) |
| 3 | C3 Eight Seats | 2 | MEDIUM | Primary 9.9% (A); B's second win not yet computed |

**Recommended pick: C1.** Cleanest math, a real student-felt choice, a genuinely definition-dependent answer, and the thin combination/binomial skills are forced by the deliverables.

**UNVERIFIED items:** 17Lands licence and the actual win-rate-by-land-count result (full files not downloaded), nonbasic-land identification in 17Lands columns; Powerball pre-2015 prize table from MUSL (only Wikipedia fetched), Powerball sales vs jackpot, beneficiary amounts, Jan 2016 jackpot details; any real esports bracket source; Wordle lists' licence (rejected concept anyway).
