# Case Study: The Overlap Call

MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

Priya Ostrowski's browser has more tabs open than she wants to count, and her test-kit box is a lot lighter than the flagged-contact list on her second monitor.

The spreadsheet in front of her — county contact-tracing intake, refreshed every hour — lists every name flagged from this week's two confirmed cases. Far more names than kits. She has done this math in her head so many times this month that she doesn't need the calculator app anymore, and she still hates the answer.

Her phone buzzes, face-down, against the edge of the desk. She doesn't turn it over yet. It's her supervisor — it's been her supervisor more than once today — asking, gently but not that gently, why last week's surge allocation ran out early, and what she's going to do differently this week so it doesn't happen again.

A handful of names on the list appear on *both* index patients' contact sheets. The rest appear on only one or the other. She has stared at that fact for a while now, turning it over. Test everyone exposed to at least one of the two people who tested positive — the widest possible net? Or test only the ones exposed to *both* — far fewer calls, but a group she can argue, on paper, carries the highest concentration of shared risk?

The widest net would use up every kit she has left, and then some. The shared-risk group would not.

Priya opens the tab with the intake list on one monitor and the tab with her supervisor's unread message on the other, and reaches for the phone.

---

## Background

Priya Ostrowski is the contact-tracing lead for her county's communicable disease unit. Her job, in the plainest terms her supervisor uses in performance reviews, is to turn a positive test into a short list of who else might be exposed, and to make that list into confirmed test results before the exposure window closes. She is accountable for two numbers every week: how many test kits she used, and how many of those tests came back positive. Both numbers go in a report with her name on it.

Her weekly test-kit allotment does not scale with how many contacts get flagged — it is fixed, set by the county lab's processing capacity. This week, as in most weeks lately, her allotment is well short of the number of flagged contacts (SEE APPENDIX B). She has to choose *who* gets tested, not *whether* to test.

This week's two flagged index patients each carry their own list of recent contacts — the people they interacted with closely enough, and long enough, to count as a real exposure. Contact lists like this are, in the underlying structure they form, nothing more than a *network*: patients and contacts are people (**vertices**), and a recorded exposure between two people is a connection (**edge**) between them (SEE APPENDIX A). Priya's actual two lists this week are drawn from a real, published social-connection network, used here as a stand-in for a real contact-tracing network — see the Modeling Assumption in Appendix C for exactly why, and exactly what that does and doesn't change about the math.

The two options in front of her are:

**Widest Net** — test every person who appears on *either* index patient's contact list (the **union** of the two lists).

**Shared Risk** — test only the people who appear on *both* index patients' contact lists (the **intersection** of the two lists).

Widest Net always finds more total secondary cases in raw count, simply because it tests more people — that comparison settles nothing. What actually matters to Priya's supervisor, and to next week's allotment, is **confirmed secondary cases found per test kit used**: which group of tests gets more real, useful information out of the two kits she can actually spend today.

Before she can compare the two options at all, Priya has to actually build both lists as sets, find where they overlap, and rule out one contact who might not belong on either list — the raw data (SEE APPENDIX A) shows one person connected to an implausibly large share of both index patients' circles, which is worth a second look before it drives a real testing decision (SEE APPENDIX A, Data Note).

The two index patients' full contact lists, the raw source they are drawn from, and the county's weekly kit allotment are in **APPENDIX A** and **APPENDIX B**. The disclosure of exactly how this week's real contact network was constructed, and the case's stated Modeling Assumptions, are in **APPENDIX C**. The vocabulary and "how to…" skills this case will ask you to research are listed in **APPENDIX D**. Every real figure in this case is sourced in **APPENDIX E**.

She has to decide today.

---

## Dilemma

You are Priya Ostrowski.

Do you:

**A.)** Test the **union** — everyone exposed to either index patient — the widest net **OR**

**B.)** Test the **intersection** — only the people exposed to both index patients — the smaller, higher-shared-risk group

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — Both index patients' contact lists, written out as two labeled sets** using proper set notation (curly braces, each contact named or numbered once), built directly from the raw network data in Appendix A. Label which people in each set are the index patient's own direct contacts (a **subset** of the county's full flagged-contact list).
- **D2 — A single Venn diagram showing both sets**, every contact placed in the correct region (only in Set A, only in Set B, or in both), with the empty region labeled if either circle has no contacts unique to it, and a one-sentence statement of whether either circle is itself an **empty set**.
- **D3 — The union and the intersection of the two contact sets, written out explicitly** (list every member of each, not just the count), with $|A \cup B|$ and $|A \cap B|$ clearly labeled.
- **D4 — A written decision about the outlier contact** flagged in Appendix A: is this person a real shared exposure, or a likely data error that should be dropped from both sets before you calculate anything else? Show the reasoning, not just the verdict.
- **D5 — A comparison table of confirmed secondary cases per test kit used**, for the Widest Net plan and the Shared Risk plan, using the county's weekly kit allotment (Appendix B) and a disclosed secondary-case rate (Appendix B). Follow Appendix B's counting convention (round the expected case count to the nearest whole person before dividing) for both plans. Show your arithmetic for both ratios, not just the final numbers.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A: The Two Index Patients' Contact Circles

Priya's county contact-tracing system does not use a real, individually identifiable public contact-tracing dataset — one does not exist publicly, and building one would violate the privacy of real patients. Instead, this case uses a real, published, anonymized **social connection network** as a structural stand-in: two real people's actual friend circles, with the same union/intersection structure a real contact-tracing case would have. Appendix C states exactly why this substitution is used and what it changes.

**Live source (explore it yourself):** Stanford SNAP, **`ego-Facebook` dataset** — [snap.stanford.edu/data/ego-Facebook.html](https://snap.stanford.edu/data/ego-Facebook.html) [S1]. This dataset publishes real, anonymized Facebook friend lists ("ego networks") for a set of volunteer users, each broken into labeled "circles" of friends. You can browse the raw circle files yourself at the link above, or download the full raw archive at [snap.stanford.edu/data/facebook.tar.gz](https://snap.stanford.edu/data/facebook.tar.gz) [S2].

| Quantity | Value |
|---|---|
| Ego-network dataset used | Ego-node **698** ("Index Patient 1") and ego-node **686** ("Index Patient 2") [S2]. Chosen because their circle sizes (66 and 170) are large enough to make "more names than kits" a real problem, small enough to reproduce and count in full by hand, and because this pair is one of only two among the dataset's 10 ego-networks with a real, non-trivial overlap between their contact circles (most pairs share zero or one contact — these two real people's friend circles happen to overlap substantially). |
| Index Patient 1's contact circle (full list of node ids) | $A$ = {697, 703, 708, 713, 719, 729, 745, 747, 753, 769, 772, 774, 776, 798, 800, 803, 804, 805, 810, 811, 819, 823, 825, 828, 830, 840, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895} [S2] |
| Index Patient 2's contact circle (full list of node ids) | $B$ = {687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856} [S2] |
| Size of Index Patient 1's contact circle | 66 [S2] |
| Size of Index Patient 2's contact circle | 170 [S2] |

**Data Note — check this before you calculate anything.** One contact id in the raw circle files above appears in an implausibly large share of *both* index patients' circles: node **828**. Within Index Patient 1's circle, node 828 is directly connected (a recorded edge) to 19 of the other 65 members — 29.2%, versus that circle's own average member-to-member connection rate of about 12.6%. Within Index Patient 2's circle, node 828 is directly connected to 77 of the other 169 members — 45.6%, versus that circle's average of about 11.5% [S2, derived from the raw edge files]. That is roughly 2.3× and 4.0× each circle's own typical rate — no other shared contact comes close to that on *both* circles at once. A real contact-tracing system would flag a number like that for review before treating it as a genuine double exposure. Decide, and show your reasoning (this is Deliverable D4).

> *Source: Stanford Network Analysis Project (SNAP), `ego-Facebook` dataset, J. McAuley and J. Leskovec, "Learning to Discover Social Circles in Ego Networks," NIPS 2012, [papers.nips.cc/paper/4532](https://papers.nips.cc/paper/4532-learning-to-discover-social-circles-in-ego-networks) [S6]. Dataset accessed 2026-09-12.*

---

## Appendix B: Weekly Test Kit Allotment and Secondary-Case Rate

| Quantity | Value |
|---|---|
| Priya's weekly test-kit allotment | **45 kits/week** [MA1 — see Appendix C] |
| Total flagged contacts this week (from both index patients combined, before removing duplicates) | derived from Appendix A: 66 + 170 = 236 |
| Secondary-case (positivity) rate applied to tested union-only contacts | **16.6%** (95% CI 14.0%–19.3%) — pooled household close-contact secondary attack rate [S3] |
| Secondary-case (positivity) rate applied to tested intersection (dual-exposure) contacts | **16.6%** — same sourced rate as above, applied to the dual-exposure group [MA2 — see Appendix C] |

> *Note: no published rate specific to a "dual index-patient exposure" contact was found (two independent search attempts, including a direct check for a compounded/multiple-exposure secondary attack rate in the epidemiology literature). That absence is itself a real finding — the case does not invent a higher number for the intersection group. See Appendix C, MA2.*

**Counting convention — read this before you compute D5.** A "confirmed secondary case" is a whole person, not a fraction of one. For each plan, first multiply the number of kits that plan actually uses by the secondary-case rate to get an *expected* case count (this will usually come out as a decimal), then **round that expected count to the nearest whole number** before dividing by the kits used to get the per-kit ratio. Example: 45 kits × 16.6% = 7.47 expected cases → rounds to **7** confirmed cases → 7 ÷ 45 is the ratio. Apply this same two-step process (multiply, round, then divide) to both plans, using each plan's own kit count and pool size.

---

## Appendix C: Modeling Assumptions

**Assumption — Real network, proxy framing.** This case uses two real people's real friend circles from the Stanford SNAP `ego-Facebook` dataset as a structural stand-in for two index patients' contact-tracing lists. The underlying union/intersection math — which people are exposed to one source, both sources, or neither — is identical whether the network represents friendships or disease contacts. No individually identifiable public-health contact-tracing dataset is used, because none exists publicly, and none should. Treat the *names/ids* in Appendix A as real data and the *disease-exposure framing* around them as a disclosed modeling proxy, not a real outbreak.

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case author. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Priya's weekly test-kit allotment | 45 kits/week | No public figure exists for a county unit's weekly test-kit supply specifically. A real, dated CDC report on U.S. contact-tracing programs [S5] found a median caseload of 29 contacts assigned per contact tracer *per month* — a related but different quantity (staffing workload, not kit supply). 45/week is set at a plausible, comparable order of magnitude for a small county unit's weekly kit budget, not derived arithmetically from that figure. | The margin between the two plans is sensitive to this number — see Appendix A's Data Note and Deliverable D4. A different allotment changes how many of each set get tested and can change which plan uses its kits more efficiently. |
| MA2 | Secondary-case rate for dual-exposure (intersection) contacts | 16.6% — same as the sourced single-exposure rate [S3] | Two search attempts (a direct search for a "dual index-patient exposure" secondary attack rate, and a review of a real study that does report household-vs-non-household rates from one cohort [S4]) found no published rate specific to a dual/compounded-exposure contact. Reusing the single-exposure rate is the honest choice available with real sourced data — it is very likely an **understatement** of the intersection group's true risk (every real source found shows closer/more concentrated exposure raising secondary attack rate, never lowering it), not an overstatement. | Because this assumption applies the *same* rate to both groups, it makes the two plans' per-kit yields nearly identical by construction — the case's real comparison rests on how each plan spends its kits (full coverage of a small group vs. partial coverage of a much larger one), not on a rate advantage this case does not claim to have found. |

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->

---

## Appendix D: "How To…" Math Questions To Research

**Vocabulary**

Set · Subset · Union · Intersection · Empty Set · Venn Diagram · Vertex · Edge · Graph (Vertices And Edges) · Outlier

**How to…**

- How to find the union and intersection of two sets
- How to represent a set relationship using a Venn diagram

---

## Appendix E: Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | ego-Facebook dataset description (nodes, edges, ego networks) | 4,039 nodes; 88,234 edges; 10 ego networks | Stanford SNAP — [ego-Facebook dataset page](https://snap.stanford.edu/data/ego-Facebook.html) | accessed 2026-09-12 | HIGH |
| S2 | Index Patients 1 and 2's real contact-circle data (Appendix A), including the union, intersection, and the flagged outlier's connection shares | Ego 698: 66 contacts; Ego 686: 170 contacts; ∩=27; ∪=209; node 828 at 29.2%/45.6% internal-connection share | Stanford SNAP — [raw ego-Facebook data archive](https://snap.stanford.edu/data/facebook.tar.gz) | accessed 2026-09-12 | HIGH |
| S3 | Secondary attack rate for a close-contact exposure (Appendix B) | 16.6% (95% CI 14.0%–19.3%), 54 studies, 77,758 participants | Madewell et al., "Household Transmission of SARS-CoV-2: A Systematic Review and Meta-analysis," [*JAMA Network Open* 2020;3(12):e2031756](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2774102) | published 2020-12-14; accessed 2026-09-12 | HIGH |
| S4 | Real-world example that exposure type/intensity changes secondary attack rate (supplemental — informs Appendix C's MA2, not used as a value directly) | Household 11.8% (n=10,592) vs. non-household 1.9% (n=48,481), same cohort | Park et al., "Contact Tracing during Coronavirus Disease Outbreak, South Korea, 2020," [*Emerging Infectious Diseases* 26(10)](https://wwwnc.cdc.gov/eid/article/26/10/20-1315_article) | published 2020-10 (study period Jan 20–Mar 27, 2020); accessed 2026-09-12 | MEDIUM (supplemental) |
| S5 | Real-world contact-tracer/case-investigator caseload (basis for Appendix C's MA1) | Median 29 contacts per contact tracer, 31 cases per case investigator, per month | CDC, ["COVID-19 Case Investigation and Contact Tracing Efforts from Health Departments — United States, June 25–July 24, 2020," MMWR 70(3)](https://www.cdc.gov/mmwr/volumes/70/wr/mm7003a3.htm) | published 2021-01-22; accessed 2026-09-12 | HIGH |
| S6 | ego-Facebook dataset methodology paper | — | McAuley & Leskovec, "Learning to Discover Social Circles in Ego Networks," [NIPS 2012](https://papers.nips.cc/paper/4532-learning-to-discover-social-circles-in-ego-networks) | published 2012; accessed 2026-09-12 | HIGH |
