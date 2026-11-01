# Research log: The Sixteenth Land (2026-10-28)

Stages 2 and 3 were run in one pass. Every input in this case is a constructed scenario input (Modeling Assumptions MA1-MA7); the case needs no externally sourced figure. All probabilities were recomputed exactly (fractions, `math.comb`) in `sensitivity_model.py`; no number was taken from memory or from the concept sheet.

| Item | Searched / fetched | Result |
|---|---|---|
| Hypergeometric PMF notation | WebFetch en.wikipedia.org/wiki/Hypergeometric_distribution | S1 MEDIUM. PMF C(K,k)C(N-K,n-k)/C(N,n); sampling without replacement. Fetched 2026-10-28. CC BY-SA, cited not copied. |
| 17Lands public datasets licence | WebFetch www.17lands.com/public_datasets | NOT FOUND. Page returned only "17Lands.com" (JavaScript-rendered). Licence unverified. |
| 17Lands game files | Not downloaded | A 40-96 MB download needs the user's explicit permission, which was not given, and the licence is unverified. The real-data Twist is therefore CUT TO A PLAN (FACILITATOR.md, "Optional extension"), not analysed and not claimed. No 17Lands figure appears anywhere in the student packet. |
| Concept-sheet figures | Recomputed | Concept said pooled margin 0.8% (gap/loser); with the gap/winner convention it is 0.75%. Play-side 3-6 peak is 18 lands (0.8599), not 17; 18 is not "worse on play". Concept's "16 wins 2 of 8 cells" replaced by the 3x3 window grid (16 wins 3 of 9 pooled). |
| Mulligan Twist | Computed | Free one-time redraw of an opening 7 with 0,1,6 or 7 lands: primary pooled 0.8998 (16) vs 0.8949 (17); winner flips, margin 0.54%. |
