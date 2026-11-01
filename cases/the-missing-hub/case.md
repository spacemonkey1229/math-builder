# Case Study: The Missing Hub

MS | Math | Case Study | 2026 | Adventure

---

## Overview

Sam Iyer refreshes the export one more time, hoping the blank cell fills itself in.

It doesn't. Row forty-one of the friend-circle degree table — the one Sam has stared at for six straight hours — still reads a bare dash where a number should be. Scrolling both directions twice confirms it: every other row in tonight's export came through clean. Just one member of the social circle Sam has spent the semester mapping has no recorded number of connections.

The conference submission portal sits open in the next tab, cursor blinking in the file-upload box. Sam's advisor, halfway out the lab door with a coat over one arm, doesn't look back. "Whatever you send tonight is what goes to the program committee," she says. "Just don't let one bad row wreck a real dataset."

The laptop fan spins up. Two sticky notes are stuck to the edge of the monitor. One says RECOVER IT — MATH. The other says DROP IT — HONEST. Sam has slid each one back and forth between "definitely" and "maybe" three times tonight.

The lab's data-collection tool is down for scheduled maintenance until Monday — two days after the deadline. There is no re-scraping this circle by morning. Whatever Sam submits tonight is what the committee reads, and whatever the tool shows on Monday is what everyone else finds out.

Sam pulls up both drafts of the summary-statistics paragraph, side by side on a split screen, and reads the first sentence of each one again.

---

## Background

Sam Iyer is a graduate research assistant in a university network-science lab, finishing an independent case study built on one real, anonymized Facebook user's friend circle — one of ten public ego-networks published by Stanford's SNAP project (SEE APPENDIX A). Sam's advisor is the submission's **corresponding author** (the person the review committee — the panel of researchers deciding which papers get accepted — contacts with any questions) and has made clear that she is accountable to that committee for what ships tonight; Sam is accountable to her.

The friend circle Sam is studying has a fixed number of members, each represented as a labeled node, connected to another member (an edge) whenever the two are also connected within the circle itself (SEE APPENDIX A). Tonight's degree-count export — the file recording exactly how many connections each member has — is missing exactly one member's row. Every other row exported cleanly (SEE APPENDIX B). There is no way to re-run the **crawl** (the automated process that re-reads every member's connections directly from the social network) before the deadline; the lab's data-collection tool is offline for scheduled maintenance until Monday.

Sam is choosing between exactly two ways to finish tonight's summary-statistics paragraph and the box-and-whisker plot that goes with it (SEE APPENDICES B, C):

**A.) The Recovery:** Algebraically reconstruct the missing member's degree count using the circle's last verified mean-degree statistic — recorded five weeks ago, before tonight's export — together with the 51 known members' degree counts (SEE APPENDIX C). This keeps the reported circle at its true size of 52 members, but the reconstructed number is only ever as good as the five-week-old statistic it is built from.

**B.) The Clean Drop:** Exclude the missing member from the dataset entirely and re-report every summary statistic — mean, median, quartiles, and the box-and-whisker plot itself — across the remaining 51 known members only (SEE APPENDIX B). This never risks reporting a fabricated number for any one member, but the paper now describes a circle one member smaller than the one that actually exists.

Both options start from the same 51 known degree counts (SEE APPENDIX B); the only difference is what happens to the 52nd. The vocabulary and "how to…" skills this case will ask you to research are listed in **APPENDIX D** — that is where Challenge 1 sends you. Every figure in this case is either cited to the real public dataset or stated as a modeling assumption, in **APPENDIX C** and **APPENDIX E**.

The upload portal closes at midnight.

---

## Dilemma

You are Sam Iyer.

Do you:

**A.)** Reconstruct the missing member's degree count algebraically, using the circle's last verified mean-degree statistic and the 51 known members' data **OR**

**B.)** Drop the missing member entirely and re-report every summary statistic across the remaining 51 known members

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A worked reconstruction: use the circle's last verified mean-degree statistic (Appendix C) and the sum of the 51 known members' degree counts (Appendix B) to algebraically solve for the missing 52nd member's degree count, showing every step.
    D2. A side-by-side summary-statistics table: mean, median, first quartile (Q1), and third quartile (Q3), computed once for the 52-member dataset (using your D1 reconstruction) and once for the 51-member dataset (dropping the missing member entirely). Use the median-of-halves method for Q1 and Q3: order the data, find the median, then find the median of the lower half and the median of the upper half (when the dataset has an odd count, exclude the overall median itself from both halves).
    D3. Two box-and-whisker plots, drawn to scale from your D2 quartiles — one for the 52-member (reconstructed) dataset, one for the 51-member (dropped) dataset — with every quartile, whisker, and any outlier clearly labeled.
    D4. A written comparison: how far does each option's newly reported mean move away from the circle's last verified mean-degree statistic (Appendix C), and does either box-and-whisker plot in D3 still show the circle's most-connected member as a statistical outlier?
    D5. A one-page recommendation memo that opens by citing your D1 reconstructed value and your D4 comparison, then states which option Sam should submit before midnight and why.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

### Appendix A — The Friend Circle

The dataset behind this case is real: Stanford's SNAP project publishes ten anonymized "ego networks," each built from one real Facebook user's own friend circle, with every member relabeled as an anonymous numeric ID [S1]. This case uses ego-network **3980** — a circle of 52 members, connected to each other by 292 friendship links among themselves (member 3980, the circle's owner, is not one of the 52 and is not counted in any statistic below) [S2].

| | Value |
|---|---|
| Members in the circle (nodes) | 52 |
| Friendship links among members (edges) | 292 |
| Members with a complete, exported degree count tonight | 51 |
| Members whose degree count is missing from tonight's export | 1 (see Appendix C) |

A member's **degree** is simply how many of the circle's other 51 members that person is friends with. The circle is connected but uneven — some members know only a couple of others in the group, while a few know a large share of the whole circle (SEE APPENDIX B).

### Appendix B — Known Degree Counts (51 Members)

Every member's degree count that exported cleanly tonight, grouped by value. This is the raw data both Option A and Option B start from [S2].

| Degree (connections) | Number of members with this degree |
|---|---|
| 2 | 10 |
| 4 | 4 |
| 6 | 9 |
| 8 | 1 |
| 10 | 4 |
| 12 | 4 |
| 14 | 3 |
| 16 | 6 |
| 18 | 2 |
| 20 | 4 |
| 22 | 1 |
| 26 | 2 |
| 34 | 1 |
| **Total members** | **51** |

### Appendix C — Modeling Assumptions: The Missing Row and the Last Verified Statistic

> These figures are **not** re-derived from tonight's export — the whole point of this appendix
> is that tonight's export is incomplete. MA1 below is a stated modeling assumption: a real prior
> measurement Sam's lab recorded five weeks ago, offered here as the best available stand-in for
> what tonight's export would have shown if it had exported cleanly.

| | Value |
|---|---|
| Anonymized member ID of the row missing from tonight's export | 4030 |
| Data-collection tool's earliest possible next full re-scrape of this circle | Monday, two days after tonight's submission deadline |

| # | Assumption | Value used | Basis |
|---|---|---|---|
| MA1 | The circle's mean degree, as last verified by a full crawl of this same 52-member circle five weeks before tonight's export | 10.75 connections per member | A real prior measurement from the lab's own records, not a figure computed from tonight's (incomplete) export. Friend circles gain and lose connections over time, so this number is not guaranteed to still be exactly correct tonight — that gap is the entire reason Option A carries risk. The answer is sensitive to this value; see `sensitivity_model.py`. |

### Appendix D — "How To…" Math Questions To Research

**Vocabulary terms**

- Mean
- Outlier

**"How to…" questions**

- How to find a missing data element given the mean and the remaining elements of its set
- How to create a box and whisker plot given a set of data

### Appendix E — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | SNAP's ego-Facebook dataset publishes 10 real, anonymized Facebook users' friend-circle networks, each member relabeled as an anonymous numeric ID | 10 ego-networks, 4,039 members total across all ten | Stanford SNAP — "Social circles: Facebook" dataset page ([link](https://snap.stanford.edu/data/ego-Facebook.html)) | accessed 2026-09-18 | HIGH (primary dataset source) |
| S2 | Ego-network 3980's member count, link count, and the full degree count of each of its 52 members | 52 members, 292 links; individual degree counts as tabulated in Appendices B and C | Stanford SNAP — `facebook.tar.gz`, file `facebook/3980.edges` ([link](https://snap.stanford.edu/data/facebook.tar.gz)) — downloaded and parsed directly this session | accessed 2026-09-18 | HIGH (primary data file, computed directly from the raw edge list) |

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
