# Learning Goals — The Cold Hit

Bidirectional deliverable ↔ skill matrix (case-write §10, MCS-10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — RMP calculation (8-locus product) | statistics-and-probability-independent-event, statistics-and-probability-how-to-determine-the-probability-of-a-compound-event, advanced-numbers-how-to-find-the-percent-of-a-number |
| D2 — Two-stage database match probability (state → national) | statistics-and-probability-multistage-sampling, statistics-and-probability-how-to-determine-the-probability-of-a-compound-event, advanced-numbers-how-to-find-the-percent-of-a-number |
| D3 — Cases-closed-per-hour comparison, percent margin | advanced-numbers-how-to-find-the-percent-of-a-number |
| D4 — C(20,10) vs P(20,10) locus-subset calculation | statistics-and-probability-permutation, statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-permutation, statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination |
| D5 — Population / Sample / Convenience Sampling written explanation | statistics-and-probability-population, statistics-and-probability-sample, statistics-and-probability-convenience-sampling, statistics-and-probability-random, statistics-and-probability-conditional-probability, statistics-and-probability-how-to-determine-the-probability-of-conditional-events |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 13    new_coverage: 0 (reinforcement_note on file)
UNMAPPED DELIVERABLES: none — every deliverable (D1-D5) maps to at least one skill.
UNREACHABLE SKILLS: none — every claimed skill in standards[] is forced by at least one deliverable:
  independent-event               -> D1 (multiplying per-locus probabilities requires the independence assumption)
  permutation                     -> D4 (explicit P(20,10) calculation and contrast)
  how-to-permutation-outcomes     -> D4
  how-to-combination-outcomes     -> D4 (explicit C(20,10) calculation)
  multistage-sampling             -> D2 (state search, then national search — the real LDIS/SDIS/NDIS structure)
  convenience-sampling            -> D5 (the offender database vs. a random population sample)
  conditional-probability         -> D5 (P(match | innocent) vs. what a hit actually proves)
  how-to-conditional-probability  -> D5
  how-to-compound-event           -> D1, D2 (multiplying independent probabilities is the compound-event calculation)
  population                      -> D5
  sample                          -> D5
  random                          -> D5 (a random population sample vs. a convenience-sampled database)
  how-to-percent-of-a-number      -> D1 (expressing RMP as a percent), D2 (DMP as a percent), D3 (percent margin)
RESULT: PASS
```

"Forces" test applied per case-write §10: could a competent student produce each deliverable
correctly without ever performing the named skill? For every row above, no — D1 cannot be computed
without multiplying independent-event probabilities; D2 cannot be computed without recognizing two
sequential (multistage) searches of different sizes; D4 cannot be computed without both a
permutation and a combination formula, used correctly and distinguished from each other; D5 cannot
be written correctly without naming Population, Sample, and Convenience Sampling and using them to
draw the right distinction; D3's percent margin is the direct application of
how-to-find-the-percent-of-a-number to the two computed rates.
