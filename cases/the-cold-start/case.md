# Case Study: The Cold Start

MS | Math | Case Study | 2026-27 | MS Adventure

---

## Overview

Priya Shah has forty minutes before the standup where she has to say which onboarding flow ships.

On her left monitor: a mockup of the sign-up flow her team calls the fast path. A brand-new
account, thirty seconds old, already scrolling a "Recommended For You" shelf. On her right
monitor: the other mockup. A grid of movie posters, a progress dot under each one, and a
button that stays grey — *Rate a handful of titles to unlock your recommendations* — until a user
taps enough of them.

Eight months and the whole original-content budget went into *Halfmoon Bay*, the limited series
Northline premieres this Friday. Priya's team didn't pick the release date — marketing did, after
a group chat screenshot of someone's friend saying *"you have to sign up just to watch this"* went
around the office. That's the cohort Thursday's launch review is actually about: people who are
opening Northline for the very first time specifically to find one show. Priya's onboarding
choice decides whether they can.

She scrubs back and forth between the two mockups. The fast path shows the new account a feed
built entirely from what's already popular — and *Halfmoon Bay*, thirty minutes old on the
platform, has nothing in that feed to earn its place yet. The slow path would fix that, if the
account ever finishes signing up.

Priya's cursor sits on neither button. The standup is in forty minutes, and her name is on the
slide.

---

## Background

Priya Shah is a Recommendation Systems Engineer on Northline's Discovery team, a mid-size
streaming service. She owns the decision of what a brand-new account sees on its very first screen
— before the account has watched, rated, or searched for anything. That decision ships with
Friday's premiere of *Halfmoon Bay*, whose entire production budget already committed the company
to the bet that word-of-mouth sign-ups would be able to find it fast (SEE APPENDIX A).

Two onboarding flows are built and ready to ship, and Priya must recommend one before Thursday's
launch review.

**The Popularity Path** sends a brand-new account straight to its first recommendation shelf, with
zero required steps beyond creating the account. That shelf is built from a small item-similarity
matrix seeded only by aggregate, platform-wide popularity — the same matrix, the same ranking, for
every new account on day one. Because *Halfmoon Bay* has zero watch history of its own at the
moment any of these accounts are created, it has no data in that matrix yet — its own row and
column are entirely empty (SEE APPENDIX B).

**The Ratings Gate** withholds any recommendation shelf until the new account has rated at least
10 titles, using that account's own answers to build one real, if sparse, row of a user-item
ratings matrix before showing anything. A row built this way can match a new account's stated
genre preferences against *Halfmoon Bay*'s own genre — a personalization signal the Popularity
Path never has access to. But the gate is a real, additional ask before a first-time visitor sees
anything the app does, and some real share of accounts abandon it before finishing (SEE APPENDIX
C).

Northline's analytics team set one hard rule for how this decision gets scored: the primary metric
is recommendations clicked per 100 accounts that **started** signup — not per account that
finished it. Scoring only the accounts that complete the flow would silently discard everyone the
Ratings Gate loses along the way, making it look stronger than it is (SEE APPENDIX D). Priya must
defend her recommendation using that metric, computed for both options, plus the matrix tools in
APPENDIX E. Full source citations for every figure in this case are in APPENDIX F, and the full standards bridge for this case is in APPENDIX G.

---

## Dilemma

You are Priya Shah.

Do you:

**A.)** Ship **the Popularity Path** — every new account gets a recommendation shelf instantly,
built from a small item-similarity matrix seeded only by aggregate popularity, in which
*Halfmoon Bay*'s own row and column are still completely empty **OR**

**B.)** Ship **the Ratings Gate** — no recommendation shelf until the new account rates 10 titles
and builds a real, if sparse, row of the user-item ratings matrix that can actually match
*Halfmoon Bay*'s genre

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A matrix dimension and sparsity comparison.** State the dimensions of Option A's
  item-similarity matrix and Option B's user-item ratings matrix (Appendices B and C). For Option
  A, compute how many of the cells associated with *Halfmoon Bay*'s own row and column are filled
  on day one. For Option B, compute the sparsity of the full ratings matrix at the reference scale
  in Appendix C, then compute the sparsity of one new account's own row immediately after clearing
  the Ratings Gate. Explain in your own words why "sparse" does not mean "empty" for Option B the
  way it does for *Halfmoon Bay*'s row in Option A.
- **D2 — A worked matrix addition example, plus an identity-matrix explanation.** Using Appendix
  E's baseline popularity matrix P and sample-account adjustment matrix U, compute the blended
  matrix P + U by hand, showing your work cell by cell. Then explain, using the identity matrix,
  why the Popularity Path's feed is mathematically the same as multiplying P by the identity
  matrix instead of adding an adjustment matrix to it.
- **D3 — A determinant check.** Compute the determinant of Appendix E's adjustment matrix U.
  Explain in your own words what a nonzero determinant tells you about whether U's effect on the
  blended matrix could, in principle, be reversed.
- **D4 — A weighted-blend system of equations, solved with a matrix.** Using Appendix E's baseline
  vector and adjustment vector, set up the stated 2-equation, 2-unknown system for the blend
  weights (w_A, w_B) as a matrix equation, and solve it using a matrix method (row reduction,
  matrix inverse, or Cramer's rule — show which you used).
- **D5 — A recommendation memo.** State which onboarding flow Priya should ship, defended with
  Appendix D's recommendations-clicked-per-100-starters table, D1's sparsity findings, and at
  least one of D2–D4's matrix results. Address directly: does scoring by *completers only* instead
  of *starters* change which option wins, and why does Appendix D insist on starters?

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

## Appendix A: Northline's Premiere Constraints

| Quantity | Value |
|---|---|
| Cohort size used to compute the primary metric | 100 accounts that start signup [definitional] |
| *Halfmoon Bay*'s watch history at the moment any of these accounts is created | Zero — the series has not premiered yet [flavor] |
| Days from case launch to Priya's Thursday launch review | 3 days [MA1] |
| Reference catalog scale used in Appendices B, C, D (titles) | 62,000 [S1] |
| Reference mature-platform account scale used in Appendix C (accounts) | 162,000 [S1] |

*Note: Northline is a scenario construction for this case — there is no real streaming company by
this name. *Halfmoon Bay* is a fictional series.*

---

## Appendix B: Option A — The Popularity Path (Item-Similarity Matrix)

| Spec | Value |
|---|---|
| Matrix built | Item-similarity matrix, dimension 62,000 × 62,000 (catalog scale, Appendix A) [S1 proxy] |
| Data used to seed the matrix | Aggregate, platform-wide popularity / co-view counts only — no per-account signal |
| Cells in *Halfmoon Bay*'s own row + column (2 × 62,000 − 1, avoiding double-counting the diagonal cell) | 123,999 |
| Of those cells, filled on day one | 0 — zero watch history means zero co-occurrence data exists for it yet |
| Personalization applied to a brand-new account's feed | None — mathematically equivalent to multiplying the baseline popularity matrix by the identity matrix (SEE APPENDIX E) |
| Required steps before first recommendation shelf | 0, beyond account creation |
| Modeled click-through rate on the *Halfmoon Bay* recommendation, among all accounts that reach the shelf | 20% [MA2] |

---

## Appendix C: Option B — The Ratings Gate (User-Item Ratings Matrix)

| Spec | Value |
|---|---|
| Matrix built | User-item ratings matrix, reference (mature-platform) dimension 162,000 × 62,000 [S1] |
| Filled cells at that reference scale | 25,000,000 ratings [S1] |
| Sparsity of that reference matrix | 25,000,000 ÷ (162,000 × 62,000) = 0.2489% filled → 99.751% empty [S1, derived] |
| Required ratings before first recommendation shelf | 10 titles — matches the real onboarding design the MovieLens research platform used [S2] |
| A new account's own row immediately after clearing the gate | 10 filled cells of 62,000 possible columns = 0.0161% filled |
| Measured historical dropout on an identical "rate ≥ 10 titles before first recommendation" gate, real MovieLens live experiment (2002) | 49 of 351 accounts, 13.96% [S2] |
| Modeled dropout for Northline's 2026 mobile-first, friend-referral sign-up cohort | 40% [MA3 — see Modeling Assumptions] |
| Modeled click-through rate on the *Halfmoon Bay* recommendation, among accounts that complete the gate | 35% [MA4] |

---

## Appendix D: Primary Metric — Recommendations Clicked per 100 Accounts That Started Signup

| Option | Accounts reaching a recommendation shelf (of 100 starters) | Click-through rate on *Halfmoon Bay* | Clicks per 100 starters |
|---|---|---|---|
| A — Popularity Path | 100.0 | 20% [MA2] | 20.0 |
| B — Ratings Gate, modeled 2026 dropout | 60.0 [MA3] | 35% [MA4] | 21.0 |
| B — Ratings Gate, real 2002 MovieLens dropout (sensitivity check, not the modeled value) | 86.0 [S2] | 35% [MA4] | 30.1 |

*The bottom row is not Priya's decision scenario — it is a sensitivity check using the literal
historical dropout rate instead of MA3's modeled 2026 figure. See the Modeling Assumptions block
and RESEARCH_LOG.md for why the two rows differ and which one governs the recommendation.*

---

## Appendix E: Matrix Toolkit — Worked Examples

**Baseline popularity matrix P** (platform-wide, 30-day figures at the moment *Halfmoon Bay*
premieres; rows = genre, columns = [minutes streamed (thousands), 7-day trend]) [MA5 — illustrative
scenario numbers, scaled for a clean worked example, not measured platform data]:

|  | Minutes streamed (thousands) | 7-day trend |
|---|---|---|
| Drama | 80 | +2 |
| Comedy | 60 | +5 |

**Sample-account adjustment matrix U** (same dimensions and same row/column meaning, derived from
one new account's first 2 ratings during the Ratings Gate — a 5-star rating on a drama title, a
1-star rating on a comedy title) [MA5]:

|  | Minutes streamed (thousands) | 7-day trend |
|---|---|---|
| Drama | +12 | +3 |
| Comedy | −8 | −1 |

**Target blend** for the weighted-blend system in Challenge D4 (a hypothetical hybrid design, not
Priya's actual A/B choice): Drama total of 100, Comedy total of 40.

**Identity matrix**, for reference in Challenge D2:

|  |  |
|---|---|
| 1 | 0 |
| 0 | 1 |

---

## Modeling Assumptions

> These figures are **not sourced** from Northline (a fictional company) or, in some cases, from
> any external record at all. They are stated scenario assumptions chosen by the case author. A
> Hero may challenge any of them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Days from case launch to Priya's launch review | 3 days | Matches the Overview's "forty minutes before the standup" / Thursday-review, Friday-premiere framing. | None — flavor only, not load-bearing. |
| MA2 | Click-through rate on the *Halfmoon Bay* recommendation among all accounts that reach the Popularity Path's shelf | 20% | No platform publishes click-through data for a same-week premiere appearing in an unpersonalized shelf. A modest but non-zero value, reflecting that some organic exposure survives a heavily marketed premiere week even without personalization. | HIGH — the most narratively-invented number in the case; see RESEARCH_LOG.md for the margin's sensitivity to this value. |
| MA3 | Modeled onboarding dropout during the Ratings Gate, Northline's 2026 mobile-first, friend-referral cohort | 40% | Anchored above two real, cited figures: Baymard's real, confirmed 17% cart/checkout abandonment due to "too long / complicated checkout process" [S4] (a shorter, lower-friction, already-purchase-intent flow), and the real, historically measured 13.96% dropout on an identical "rate ≥ 10 titles before recommendations" gate on the real 2002 MovieLens site [S2]. MovieLens's 2002 population were self-selected, already-engaged research-community members, not a general new-subscriber cohort arriving from a friend's text message — general digital-product research consistently finds that additional required steps before first value increase abandonment (a real, transferable direction, even though no single transferable magnitude exists for this exact gate). | **HIGH — this is the single most dilemma-relevant modeling choice in the case.** Appendix D's bottom row shows what happens if the literal 2002 figure (13.96%) is used instead — see `balance.margin_note`. |
| MA4 | Click-through rate on the *Halfmoon Bay* recommendation among accounts that complete the Ratings Gate | 35% | Only some fraction of the 10 ratings an account provides will happen to land in *Halfmoon Bay*'s own genre; not independently sourced, since no platform publishes click-through data for an unreleased show. | MEDIUM — see RESEARCH_LOG.md for the margin recomputed at alternate values. |
| MA5 | Appendix E's worked-example matrices (P, U, and the target blend) | See Appendix E | Illustrative scenario numbers, scaled down for a clean hand-worked example. Not measured platform data. | None — pedagogical only; does not feed the primary metric in Appendix D. |

---

## Appendix F: Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | MovieLens 25M dataset scale: ratings, users, movies | 25,000,000 ratings; 162,000 users; 62,000 movies | GroupLens Research — [MovieLens 25M Dataset](https://grouplens.org/datasets/movielens/25m/) | Page current as of access | HIGH — real, published dataset statistics; used as a proxy for "a streaming catalog and user base at this scale," since Northline is fictional. |
| S2 | Real onboarding design ("rate 10 or more titles before recommendations") and measured live-experiment dropout on that exact gate | Design: "the system presents pages of ten movies until the user rates ten or more movies." Dropout: 49 of 351 total online-experiment users (13.96%) abandoned before completing signup; 302 completed. | Rashid, A.M., Albert, I., Cosley, D., Lam, S.K., McNee, S.M., Konstan, J.A., Riedl, J. — ["Getting to Know You: Learning New User Preferences in Recommender Systems"](https://cs.fit.edu/~pkc/apweb/related/rashid-iui02.pdf), IUI '02 | 2002-01-13 | HIGH — real, published, peer-reviewed live experiment on the real MovieLens platform; same "rate ≥10 items before recommendations" mechanic as Option B. Confidence on transferring the exact 13.96% figure to a 2026 streaming cohort is lower — see MA3. |
| S3 | Share of viewing hours a real streaming platform's own recommender system influences | "Approximately 80 percent of hours of content streamed" | Gomez-Uribe, C.A. & Hunt, N., "The Netflix Recommender System: Algorithms, Business Value, and Innovation," *ACM Transactions on Management Information Systems* 6(4), 2015 — quoted and cited (footnote 238) in [New America, "Case Study: Netflix"](https://www.newamerica.org/insights/why-am-i-seeing-this/case-study-netflix/) | 2015 (paper); accessed 2026-09-01 (secondary page) | MEDIUM-HIGH — real, peer-reviewed figure, confirmed via a reputable secondary source that names and footnotes the original paper; used as Background stakes framing (why personalization matters at all), not as an input to Appendix D's metric arithmetic. |
| S4 | Real-world abandonment attributed specifically to checkout complexity | "17% of US online shoppers have abandoned an order due to a 'too long / complicated checkout process.'" | Baymard Institute — [Cart Abandonment Rate Statistics](https://baymard.com/lists/cart-abandonment-rate) | Page current as of access | HIGH — real, directly confirmed figure; used only as a real lower-bound anchor for MA3, not as a literal transferred number (checkout is a shorter, lower-friction, purchase-intent flow than a 10-item rating gate). |

---

### Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Matrix
- Matrix Dimension
- Determinant
- Identity Matrix

**"How to…" questions**

- How to add and multiply matrices
- How to find the determinant of a 2x2 matrix
- How to solve a system of equations using a matrix

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
