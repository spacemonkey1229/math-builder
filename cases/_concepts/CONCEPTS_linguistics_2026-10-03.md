# Concepts — Linguistics & Language Data (Deep Time & Language) — 2026-10-03

Target: domain `linguistics` (cluster Deep Time & Language), non-sports slot 6 of the sports-science wave release plan
(working direction "word-frequency / dialect-split decision from open corpora"). Per `readmodel/domains.json` the domain has
**zero existing cases** and `uncovered_signature_skills` is empty. A live spine query shows **no skill at n=0** anywhere, so, as in
`CONCEPTS_justice-forensics_2026-09-18.md`, these are reinforcement cases: score counts the thin skills (n<=3) a concept genuinely forces,
times the data factor. Scores are therefore low in absolute terms; judge them against each other and against Cold Chain's 4.2 calibration
with that in mind.

Overlap check: `cases_index.json` (173 cases) has no linguistics case. `codebreaker` (cipher with letter values, Convention 4 error rate)
uses letters only as a puzzle mechanism, not real corpora. No concept file proposes Federalist authorship, Wordle or Webster
(grep of `cases/_concepts/`). No title collisions.

Evidence tags: **[VERIFIED]** fetched or searched this session (source named); **[UNVERIFIED]** could not confirm, a research task;
**[CONSTRUCTED]** the binary framing is ours, the surrounding story is real; **[DERIVED]** reasoning only, no invented numbers.

| Rank | Concept | Story | Score | Tier guess | Data |
|---|---|---|---|---|---|
| 1 | **C1 The Disputed Twelve** | Mosteller and Wallace, Federalist authorship, 1960s | 2.2 | T3 | HIGH |
| 2 | **C2 The Five-Letter Filter** | Josh Wardle and Palak Shah, Wordle answer list, 2021 | 1.3 | T2 | MEDIUM |
| 3 | **C3 The Spelling Bet** | Noah Webster, 1828 dictionary | 1.2 | T2 | HIGH (data) / story partly UNVERIFIED |

Killed: a Cornish Standard Written Form concept (2008 compromise orthography; fits the "compromise spelling vs majority dialect"
archetype, but see the last section: usage data is not free or numeric enough).

---

### C1 — The Disputed Twelve   ·   score 2.2   ·   tier T3
**Protagonist.** Frederick Mosteller (statistician; Harvard affiliation from memory, UNVERIFIED) with David Wallace (University of
Chicago, [VERIFIED] via the Chicago Sun-Times obituary result and IMS obituary), who have to turn "Madison or Hamilton?" for twelve
essays into something a historian will accept. Personally at stake: their method has to survive scrutiny from historians who have
argued the question for 170 years.
**Facts.** Twelve Federalist essays (Nos. 49-58, 62, 63) had disputed authorship between Hamilton and Madison [VERIFIED: arXiv 2511.16040
summary and Priceonomics]. Mosteller and Wallace (book 1964) used function-word rates; "upon" averaged 3.24 per 1,000 words in Hamilton's
known work and 0.23 in Madison's; they identified 30 marker words; they concluded Madison wrote all twelve [VERIFIED across Priceonomics
and a second search result; the primary book was not fetched, so the exact figures are **[UNVERIFIED against the 1964 book]**]. The quoted
odds ("12.6 million to 1", "160 billion to 1") are one secondary source and must be **[UNVERIFIED]** or cut.
**The dilemma.** A.) Decide each disputed essay on a single transparent marker, the rate of "upon" per 1,000 words, with a stated cutoff
OR B.) Decide on a panel of marker words (for example "upon", "by", "to", "while/whilst"), combining their rates into one score.
**[CONSTRUCTED]:** the historical choice was a panel; the case asks students to defend the simpler alternative a skeptical historian might prefer.
**Primary metric.** Misclassified known essays per 100 known essays (error rate on essays whose author is not in doubt), lower is better.
**Why it's close.** [DERIVED] A single-word rule is easy to explain and audit, but the essays are short and "upon" is rare in Madison, so a
Madison-style essay can contain zero "upon" by chance: absence is weak evidence, while presence is strong. A panel gains power by pooling
many weak signals but is harder to explain and can overfit the known essays. A wins on transparency, B on error rate; the **balance risk**
is that the true error rates may not be close, and R1a must confirm this with the real counts before the case is drafted (if B dominates,
change the constraint, for example cap the rule at what a jury can follow, and say so in the dilemma).
**Would close (3 thin skills, 1 how-to / 2 term):**
| id | kind | label |
|---|---|---|
| statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data | how-to | How to create a box and whisker plot given a set of data (n=1) |
| statistics-and-probability-box-and-whisker-plot | term | Box And Whisker Plot (n=3) |
| statistics-and-probability-quartiles | term | Quartiles (n=3) |

(Box plots of per-essay "upon" rate by author are the natural display; no claim of closing anything outside Statistics And Probability.)
**Already-covered skills it also exercises.** `measurement-ratio`, `measurement-proportion`, `advanced-numbers-how-to-find-the-percent-of-a-number`,
`statistics-and-probability-mean`, `statistics-and-probability-median`, `statistics-and-probability-outlier`,
`statistics-and-probability-histogram`, `statistics-and-probability-sample`, `statistics-and-probability-population`,
`statistics-and-probability-how-to-determine-the-probability-of-a-single-event`.
**Data feasibility: HIGH.** Named sources:
- Project Gutenberg ebook #1404, The Federalist Papers, plain text, **public domain in the US** [VERIFIED by fetch]. Students split by essay and count words themselves.
- `MWwords` data frame in the CRAN package `alr4` (word frequencies for Hamilton, Madison, Jay, and Joyce's Ulysses, from Mosteller and Wallace 1964) [VERIFIED listing at rdrr.io]. **Licence not stated on the page: check the CRAN licence before redistributing; students can load it themselves.**
Sources I am NOT confident about: the authoritative per-essay attribution list (use Library of Congress or Founders Online; not fetched, so UNVERIFIED);
text-edition differences (Gutenberg text vs the edition Mosteller and Wallace used, including headers and editorial notes, will shift counts slightly and must be disclosed).
**Sensitivity (SPEC §6).** NONE. Note for the facilitator: the case reproduces a known answer; the point is the method, not who wins.
**Split risk.** NONE (3 skills).

---

### C2 — The Five-Letter Filter   ·   score 1.3   ·   tier T2
**Protagonist.** Josh Wardle, software engineer, with his partner Palak Shah sorting the word list, building a word game for the two of them
that later became Wordle. Personally at stake: a game his partner will actually enjoy. [VERIFIED: Wikipedia "Wordle" development section]
**Facts [VERIFIED, Wikipedia; secondary]:** the prototype used about 13,000 five-letter words; Shah found many obscure; she sorted words into
three piles (knew, did not know, might have known); filtered to about 2,000, which Wardle calculated would last "roughly five years at one
puzzle per day"; original list 2,315 answers per the New York Times; the NYT acquired the game in January 2022 and by July 2022 had removed
seven answers (for example "fetus" in May 2022 after a news event). The Aperiodical says the guess list comes from Collins Scrabble Words
CSW19 and the answer list has fewer than 2,500 words **[conflicts with "13,000" and with the 12,966 figure; the pool size is UNVERIFIED, flag it]**.
The Tracy Bennett "handful of words ... too obscure or vulgar" quote came from a search summary, not a page we could fetch (CNN and Forbes
blocked fetch): **[UNVERIFIED], cite only after a direct read**.
**The dilemma.** A.) Draw answers from every valid five-letter word (about 13,000, a game that lasts decades and never gatekeeps a word)
OR B.) Draw answers only from the roughly 2,000 words Shah recognizes (about six years of puzzles, but nearly every answer is fair).
The real choice was B; **[CONSTRUCTED]** is the counterfactual framing and the sensitivity of how many words a cutoff keeps.
**Primary metric.** Share of daily answers that a typical player will know, using rank in a public word-frequency list as a stand-in
(percent of answers inside the 20,000 most frequent words), against years of daily puzzles supplied. **Balance caveat:** this is two numbers,
and the single-metric form is an open item for R1a (candidate: "familiar-answer days supplied in total" = pool size × familiar share, where A
may out-supply B because it simply has more words; if so, A and B really are close and B's advantage must be the unfamiliar-day rate).
**Why it's close.** B wins on fairness of each day; A wins on how long the game lasts and on not deciding for everyone which words
"count". A frequency cutoff is only a proxy for what a person knows (words like plurals and inflections rank high but make bad puzzles; some
good Wordle words rank low), so even the rule used to build B has an error rate students can measure.
**Would close (3 thin skills, 1 how-to / 2 term):**
| id | kind | label |
|---|---|---|
| statistics-and-probability-non-linear | term | Non-linear (n=2) |
| statistics-and-probability-line-of-best-fit | term | Line Of Best Fit (n=3) |
| statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data | how-to | How to draw a line of best fit given a set of data (n=3) |

Honest scope: the non-linear and best-fit skills are forced only if the case has students plot frequency against rank (a steeply falling
curve is not a line; best-fit applies after transforming or on a region). Confirm in `case-write`'s bidirectional check or drop them.
**Already-covered skills it also exercises.** `statistics-and-probability-histogram`, `statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data`,
`advanced-numbers-how-to-convert-numbers-to-percents`, `measurement-ratio`, `statistics-and-probability-sample`, `statistics-and-probability-population`,
`statistics-and-probability-mode`, `statistics-and-probability-range`.
**Data feasibility: MEDIUM.** Named sources:
- Peter Norvig, `count_1w.txt` (about 1/3 million most frequent words with counts from the Google Web Trillion Word Corpus; code under MIT) [VERIFIED at norvig.com/ngrams]. **Caveat: the page says the corpus data's own licence should be checked with the original distributor (Linguistic Data Consortium); do not redistribute the file inside the case, link to it.**
- The 2,315-word original answer list is mirrored in public GitHub gists and write-ups [VERIFIED to exist via search, e.g. a "Wordle 2315 words list" gist]; it is **not an official NYT download**, so cite the NYT's 2,315 count and let students fetch a mirror themselves.
- Google Books Ngram data as an alternative frequency source (see C3 licence).
Sources I am NOT confident about: the exact ~13,000 pool; any measured "words people know" survey data (none found); copyright status of the answer list itself.
**Sensitivity (SPEC §6).** Mild. Some of the removed words are slurs or tied to news events; the case should not list them gratuitously.
**Split risk.** NONE.

---

### C3 — The Spelling Bet   ·   score 1.2   ·   tier T2
**Protagonist.** Noah Webster, writing his dictionary, who has to decide which reformed spellings to print as the American standard.
Personally at stake: a decades-long project that must sell to printers and schools or it fails. **UNVERIFIED:** the precise date and exact
set of word pairs he faced; this concept uses only the well-documented ones.
**Facts [VERIFIED, search summaries of Wikipedia and Mental Floss]:** his 1828 *An American Dictionary of the English Language* had about
70,000 entries; he popularised "color", "center", "defense", "plow", "draft" and "jail" in place of "colour", "centre", "defence", "plough",
"draught" and "gaol"; other reforms ("tung" for tongue, "wimmin" for women) did not catch on; the Worcester rivalry is called the
"dictionary wars". Not fetched in full: **exact attribution of each reform to the 1806 or 1828 edition is UNVERIFIED.**
**The dilemma.** A.) Print every reform that follows his rule (drop silent letters, regularise -our/-re), including the radical ones
OR B.) Print only the reforms already visible in what printers were setting, leaving the rest as the traditional spelling.
**[CONSTRUCTED]:** we pose his choice as a two-rule decision so a student can test each rule on data.
**Primary metric.** Percent of the paired spellings that, under the chosen rule, match the form with the larger share in the US-English book corpus
when measured at a later date (accuracy of the rule, higher is better), with a stated check year.
**Why it's close.** [DERIVED] Rule A is consistent and teachable, and the heavy hitters (color, center) were exactly such reforms; but it also
prints losers. Rule B never prints a loser if the early data are a good signal, but it can miss a reform that was about to win and gives
the dictionary no principle. Whether A or B scores higher depends on the early-year counts, which are sparse and noisy: the balance is an
empirical question R1a must run on the real data before approval.
**Would close (about 2-3 thin skills, 0 how-to / terms):** `statistics-and-probability-convenience-sampling` (n=3, the book corpus is a convenience sample, a
real and graded question of what it represents), `statistics-and-probability-non-linear` (n=2, share-over-time curves). Count is honest at about
1.2 only if both are genuinely forced; otherwise this is a weak coverage case.
**Already-covered skills it also exercises.** `advanced-numbers-how-to-convert-numbers-to-percents`, `measurement-ratio`,
`statistics-and-probability-sample`, `statistics-and-probability-population`, `statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data`.
**Data feasibility: HIGH for the data, MEDIUM for the story.** Named source:
- Google Books Ngram Viewer, with separate American English and British English corpora, case-sensitive, smoothing adjustable, raw data downloadable; terms: "may be freely used for any purpose", acknowledgement requested [VERIFIED at books.google.com/ngrams/info; the page does not state a CC BY licence, so do not claim one]. Students can chart "color,colour" live with no download.
Sources I am NOT confident about: how many books and which kinds are in the corpus around 1800-1828 (OCR and sample size thin; expect noisy series, and the s/long-s issue in early print), and whether the check-year accuracy figure is stable across smoothing.
**Sensitivity (SPEC §6).** NONE.
**Split risk.** NONE.

---

## Recommendation

**Write C1 The Disputed Twelve**, conditional on R1a confirming from the real Gutenberg counts that single-word and panel rules really are close
(error rates within about 5-15%); if not, fix the constraint (e.g. the rule must be explainable in one sentence to a jury). It is the only concept
that is a true, fully recognized story, with public-domain text and published reference rates, and it fits "open corpora". C2 Wordle is the
engagement favorite and the best runner-up (every student has played), but it is weaker on data (answer-list provenance, frequency-list
licence) and its single-metric balance is unresolved. **Kill C3 first** if only one must go: its story facts are the least verified, the 1800-1828
Ngram series are thin, and its coverage claims are the weakest. Next step: approve a concept, then run case-write on it (and send it through
R1a/b/c as the release plan requires).

## Not recommended: Cornish Standard Written Form (2008)
Real story, fits the archetype exactly: four language groups agreed a compromise orthography in May 2008 after two years of negotiation
(Cornish Language Partnership), adopted by Gorsedh Kernow in June 2009 [VERIFIED, Wikipedia]. But the free data are thin: the 2021 census
recorded 471 people with Cornish as main language (464 in 2011) [VERIFIED via search of the ONS result, not fetched], a Wikipedia line that
the SWF accounts for about 25% of written output 2009-2024 [VERIFIED, secondary, no named dataset], and no free per-orthography user counts.
Too little for a mathematics case; revisit if a Cornish Language Partnership survey with orthography counts can be found.
## Also considered
Norwegian Bokmål/Nynorsk: Statistics Norway StatBank tables 05232 and 03743 give pupils by official written form (621,961 pupils on 1 Oct 2025:
544,960 Bokmål, 68,842 Nynorsk, 908 Sami; page updated 17 Dec 2025) [VERIFIED by fetch; licence not confirmed on the page]. Great live data
but no recognizable single decision-maker story was found; hold as a data source for a later municipal-school-board case.

---

# Round 2 revision (2026-10-04) — response to REVIEW_BRIEF_non-sports-slots_2026-10-04.md

Original text above is unchanged. Everything below was computed this session from the real Gutenberg #1404 text (fetched; tokenised as
lower-case `[a-z]+` words after each essay's salutation line; "PUBLIUS" signatures dropped; 189,773 words in 85 essays). Scripts are in the
session scratchpad, not in the repo.

## Verdict on the slot

**C1 The Disputed Twelve FAILS the balance test as a two-sided dilemma. C2 and C3 also do not pass. Nothing in this file passes. Recommendation:
swap the slot to `climate-science` (see "Recommendation" below), and treat the new linguistics idea only as a back-up that has NOT been solved.**

### Attribution table used (known = 65 essays, the Mosteller-Wallace set)
Hamilton 51 (Nos. 1, 6-9, 11-13, 15-17, 21-36, 59-61, 65-85); Madison 14 (Nos. 10, 14, 37-48); disputed 12 (Nos. 49-58, 62, 63); Jay 5; joint 18-20
(excluded). Gutenberg headers label the 12 disputed as "MADISON" and 18-20 "MADISON, with HAMILTON"; I did not trust those headers for the
disputed set and excluded them from training. **The disputed-list authority is still not cleanly sourced:** the Library of Congress guide fetched
only discusses 18-20 and 50-52 credit-lists, Founders Online would not load (DNS failure), and a Wikipedia fetch summary was garbled. What is
supported: the 1963 JASA paper (search result) says twelve papers were disputed and concluded Madison wrote all twelve; the 49-58/62/63 set matches
the earlier arXiv 2511.16040 summary and the Gutenberg headers. Treat the list as **[VERIFIED-secondary]**; a Founders Online or LOC page naming
the 12 numbers is still needed (R1b).

### (a) Is there a genuine two-sided dilemma on the disputed essays? No.
Real rates of "upon" per 1,000 words, computed:

| Group | Essays | Words | "upon" | Pooled rate | Mean of essay rates | Range of essay rates |
|---|---|---|---|---|---|---|
| Hamilton | 51 | 112,886 | 374 | **3.31** | 3.27 | 1.01 to 7.51 |
| Madison | 14 | 38,771 | 7 | **0.18** | 0.16 (median 0.0) | 0.00 to 1.21 |
| Disputed | 12 | 24,070 | 3 | 0.12 | | 0.00 to 1.00 |

Eleven of the 14 Madison essays contain zero "upon"; **no Hamilton essay contains zero** (lowest is No. 25 at 1.01). So the original sheet's claim
that "absence is weak evidence" is wrong for this data: zero "upon" in a 2,000-word essay is strong evidence for Madison.

**Single-word rule on the 65 known essays** (call it Hamilton if rate >= cutoff):

| Cutoff (per 1,000) | Hamilton called Madison | Madison called Hamilton | Errors / 65 |
|---|---|---|---|
| 0.50 | 0 | 2 (Nos. 38, 42) | 2 (3.1%) |
| 0.75 to 1.00 | 0 | 1 (No. 38, 1.21) | **1 (1.5%)** |
| 1.02 to 1.10 | 1 (No. 25) | 1 (No. 38) | 2 (3.1%) |
| 1.25 | 1 | 0 | 1 (1.5%) |
| 1.50 | 4 | 0 | 4 (6.2%) |
| 2.00 | 10 | 0 | 10 (15.4%) |

Best in-sample cutoff errs on 1 of 65; leave-one-out (refit the cutoff without the essay being tested) errs on 2 of 65 (3.1%). R1b's "about 3%" is
confirmed. The cutoff is knife-edge: the whole gap between the two authors' essay rates is 1.01 (Hamilton min) vs 1.21 (Madison max), they overlap.

**Panel rule** (naive-Bayes Poisson log-likelihood ratio over a prespecified 30-word list recalled from the Mosteller-Wallace marker words:
upon, also, an, by, of, on, there, this, to, although, both, enough, while, whilst, always, though, commonly, consequently, considerable, according,
apt, direction, innovation, language, vigor, kind, matter, particularly, probability, work, would; list is from memory, **[UNVERIFIED against the book]**):
leave-one-out errors **0 of 65**. An 8-word panel errs on 1 of 65. So the panel beats the single word (0 vs 2 LOO errors), as R1a said.

**Abstain rule (explicit costs).** Single-word LOO Poisson log-likelihood ratio, abstain when |LLR| < tau:

| tau | Errors | Abstains (of 65) |
|---|---|---|
| 0 | 2 | 0 |
| 2 | 1 | 3 |
| 3 | 1 | 8 |
| 4 | 0 | 12 |

Panel: 0 errors, 0 abstains at every tau from 0 to 5. Minimum total cost (wrong = W, abstain = 1) for the single word: W=1 gives 2, W=3 gives 5,
W=10 gives 10; for the panel it is 0 at every W. **The panel is weakly better at every cost ratio, so no cost ratio makes the two options trade off.**

**On the 12 disputed essays** (training on all 65 known; LLR negative = Madison):

| Essay | Words | "upon" | upon-only LLR | 30-word panel LLR |
|---|---|---|---|---|
| 49 | 1,646 | 0 | -5.1 | -11.9 |
| 50 | 1,101 | 1 | **-0.6 (odds about 1.8:1)** | -14.6 |
| 51 | 1,914 | 0 | -6.0 | -42.0 |
| 52 | 1,844 | 0 | -5.8 | -25.8 |
| 53 | 2,164 | 0 | -6.8 | -28.4 |
| 54 | 1,996 | 2 | **-0.6 (about 1.7:1)** | -31.0 |
| 55 | 2,043 | 0 | -6.4 | -7.0 (weakest panel margin) |
| 56 | 1,650 | 0 | -5.2 | -13.6 |
| 57 | 2,206 | 0 | -6.9 | -34.7 |
| 58 | 2,080 | 0 | -6.5 | -29.2 |
| 62 | 2,387 | 0 | -7.5 | -36.6 |
| 63 | 3,039 | 0 | -9.5 | -37.0 |

Ten of twelve have zero "upon" and are decisive on one word; only Nos. 50 and 54 (rates 0.91 and 1.00, straddling the 1.0 cutoff) are near-ties, and
the panel resolves both toward Madison. A rule that abstains on 50 and 54 would be the only point where the single word differs, and it is dominated by
the panel which decides them confidently. All twelve land on Madison under every sensible rule; the "disputed" margin is a margin of evidence, not a
two-sided choice. **Fails balance test: the panel dominates; the abstain trade only exists inside the weaker single-word option.**

### Fixes requested by R1b (apply to any future use)
- Rates: the secondary 3.24 / 0.23 (Priceonomics) should not be quoted as fact. From the real text: **3.31 and 0.18 pooled (3.27 and 0.16 as mean of essay rates)**. The sheet's earlier "[VERIFIED]" tag on 3.24/0.23 is withdrawn; students compute their own.
- Odds: the "12.6 million to 1" and "160 billion to 1" figures are **cut** (single secondary source).
- Citation: Mosteller, F. and Wallace, D. L. (1963), "Inference in an Authorship Problem," Journal of the American Statistical Association 58(302), 275-309 [VERIFIED by search result, citation matches Google Scholar lookup]; book: *Inference and Disputed Authorship: The Federalist* (Addison-Wesley, 1964) [from memory, publisher not fetched].
- `alr4` (CRAN 1.0.7, 2026-01-17): licence **GPL-2 | GPL-3** [VERIFIED at cran.r-project.org]. The rdrr.io page for `MWwords` says it holds frequencies and ranks for Hamilton, Madison, Jay and Ulysses from the 1964 book, but **does not say whether "upon" is a row or whether the units are counts or rates**. Not promised; I did not download the tarball (needs permission). The C1 sheet's "[VERIFIED listing]" should read "listing seen, contents unchecked".
- The "5-15%" balance target in the original Recommendation is superseded by the numbers above (3.1% vs 0%).

### (b) C2 The Five-Letter Filter, with sourced list sizes
Pool conflict, resolved by search (secondary sources; not an NYT download):
- Original Wordle source: **2,315 answers + 10,657 other allowed guesses = 12,972 valid words** (Winning Wordle Wisely, arXiv 2202.02148, and Lessard's solver repo, per search summary). "About 13,000" is a rounding of 12,972; Wikipedia says "approximately 13,000" and "about 2,000 more familiar words".
- After the NYT acquisition: 2,309 answers (Wikipedia) and about 12,966 total valid words (search summary, **secondary, unverified against NYT**). So 13,000 vs 12,972 vs 12,966 is not a real conflict: it is rounding plus a post-2022 edit of six words.
- "Fewer than 2,500" (Aperiodical) is the **answer** list, not the pool; consistent with 2,315.
- Wikipedia: Shah sorted words into knew / did not know / might have known; about 2,000 would last "roughly five years" (2,315 days is about 6.3 years).
- Answer list is a community mirror, not an official NYT download; Norvig `count_1w.txt` has the LDC licence caveat. **I did not download either file**, so no frequency-based number is computed.

Single metric: only the following can be resolved honestly on paper: "fraction of answer days a typical player does not know" over a fixed horizon.
At a fixed 2,315-day horizon B (curated list) is built to minimise this and A (all 12,972 words) can only be worse, so **B dominates**, the same defect as C1.
A genuine tension would need a horizon longer than the list (A never repeats; B repeats after about 6.3 years), which is a real, current story (the
answers run out around 2027), but then the metric needs a repeat-penalty weight that we would be inventing. **Not computed; not claimed.**
Verdict: C2 cannot be made honest from what was fetched.

### (b) C3 The Spelling Bet — computed with Google Books Ngram (US English 2019 corpus, JSON endpoint, smoothing 0), 22 pairs I chose
Fourteen pairs where the reformed form leads in 2000-2010 (color, honor, favor, labor, center, theater, defense, offense, plow, jail, music, public, traveler, mold);
eight where it never does (tung, wimmin, dawter, masheen, giv, bred, hed, iland). Reformed-form share of the pair, US corpus:
- 1800-06: color 0.22, honor 0.32, center 0.23, plow 0.16, theater 0.03, defense 0.04, offense 0.06, traveler 0.07, mold 0.02, jail 0.50, music 0.91, public 0.94; radical forms 0.00 except bred 0.21 (a real word, "bred", so this is contamination).
- Rule A "print every reform" (threshold 0): 14 right of 22 = **64%**.
- Rule B "print the reform only if it already has at least X share" in 1800-06: X=1% gives 21/22 = **95%**; X=5% gives 18/22 = 82%; X=15% gives 16/22 = 73%; X=50% gives 11/22 = 50%.
- Same test on 1822-28 shares: best is 16/22 = 73% at X=1%.
So a rule B with a low cutoff beats A by 31 points and the high-cutoff versions are worse than the low one: **one option dominates and the interior thresholds are dominated by the 1% rule. Fails balance test.** Caveats: the pair list is hand-picked with hindsight; Ngram is OCR-based, 1800s data are thin and affected by the long s; the radical Webster respellings (some from his 1789 *Dissertations*, not the 1828 dictionary) are unverified as to which edition. C3 killed.

### (c) New linguistics concept: not delivered
I did not find, solve and verify a replacement in time. Checked: Education Counts (NZ Māori-medium data) returned HTTP 403 to fetch, so no data check was possible; Stats NZ and Welsh census options were not fetched. Norwegian StatBank (earlier VERIFIED) still lacks a decision-maker story. A candidate worth a future research task, **unsolved and unverified**: the Māori language-nest (Te Kōhanga Reo, 1982) versus adult-class funding decision; needs a portal fetch and a cold solve first.

## Recommendation (round 2)
1. **Do not write C1, C2 or C3.** C1 has a computed dominated option (0 vs 2 LOO errors; no cost ratio flips it); C3 is dominated by a low-threshold rule; C2 is dominated at a fixed horizon and otherwise uncomputed.
2. **Swap the slot to `climate-science`**: `readmodel/domains.json` lists `existing_cases: []`, `authoring_priority` MEDIUM, HIGH data; `cases/` has no climate case and `cases/_concepts/` has no climate concept file (listed and grepped). NOAA Climate at a Glance fetched live this session (monthly temperature/precipitation for global, US national, state, county, city; the page states no formal data-use policy and says recent data are preliminary; cite it as NOAA NCEI public data and confirm reuse terms). Its decision archetype "report a warming trend from 30 years of data or say the record is too short to call" is a natural candidate for a computed balance check. `mining-minerals` (also zero cases; USGS MCS) is the second choice. `robotics-automation`, `media-recommendation` and `disaster-response` each already have 1-3 cases.
3. Linguistics can be revisited later with the Māori or Welsh idea after a real fetch and solve; it needs a decision whose two options both win somewhere on real data.

Balance test result for this file: **NOT PASSED** for any concept. No pass is claimed.
