# Learning Goals: The Sixteenth Land

LEARNING GOAL CHECK (bidirectional: every deliverable forces a spine skill; every claimed skill is forced by a deliverable).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 Opening-hand counts by factorial cancellation (C(40,7), hands with 0 and 1 lands) | statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination, statistics-and-probability-combination, discrete-mathematics-how-to-compute-a-binomial-coefficient, discrete-mathematics-binomial-coefficient, advanced-operations-how-to-evaluate-a-factorial-expression, advanced-operations-factorial |
| D2 P(0 or 1 land in the opening 7) as fraction, percent, margin | statistics-and-probability-how-to-determine-the-probability-of-a-single-event, advanced-numbers-how-to-convert-numbers-to-percents, advanced-numbers-percent |
| D3 Primary metric: sums of hypergeometric terms for 10 and 11 cards, averaged | statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination, statistics-and-probability-how-to-determine-the-probability-of-a-single-event |
| D4 Window grid (9 windows + 2 other turn counts) with margins | advanced-numbers-how-to-convert-numbers-to-percents, number-sense-how-to-compare-two-or-more-values |
| D5 Chart of P(smooth) vs lands 14-19, play and draw | statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data |
| D6 Window statement and what real results could/could not show | number-sense-how-to-compare-two-or-more-values |

## Forces-test notes

- **Combination count, binomial coefficient, factorial (D1):** D1 forbids a table and a combinations key and requires each count as a product of C(n,k) evaluated by cancelling factorials. A student cannot produce 18,643,560 or 346,104 on paper without evaluating C(40,7) and C(24,7) as factorial quotients. Appendix C supplies the *definition* of C(n,k), not any value. This is the only place the binomial/factorial claims are forced; D3 may use a tool, so it is claimed only for the combination-count and single-event skills.
- **Single event (D2, D3):** probability = favorable hands / all hands.
- **Percent (D2, D4):** the margin is a percent under a stated convention.
- **Scatter plot (D5):** the chart is a set of ordered pairs (lands, probability).
- **Compare values (D4, D6):** deciding which list leads in each window and defending a window.
- **Not claimed:** `independent-event` (hypergeometric draws are dependent, claiming it would be wrong); `dependent-event` (the counting method handles it without a student performing a dependent-event calculation); hypergeometric/ factorial *term* beyond Factorial; `how-to-determine-the-probability-of-a-compound-event` (the window sum is a sum of counts, not a compound-event calculation).

## Result

```
LEARNING GOAL CHECK
  deliverables: 6    claimed skills: 11    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS (new_coverage empty by honest reinforcement; no skill in the spine has n=0; see case.json.reinforcement_note)
```
