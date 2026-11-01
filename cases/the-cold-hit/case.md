Case Study: The Cold Hit
MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

"It's a name and a number, Dana. Tell me if that's enough."

Her supervisor said it from the doorway an hour ago and hasn't come back for the answer yet. Dana Osei has had the printout face-down on her desk ever since — she doesn't want to look at it again until she's decided what to write.

Six months ago, a degraded blood swab from a decade-old assault case went back through the lab for the third time — new chemistry, better recovery, same brittle old sample. It came back with a partial genetic profile, thin but real. Dana ran it the way she runs every cold case: search the state database first. Nothing. Escalate to the national one. A name came back.

No fingerprint. No confession. No witness. Just a name, a profile, and a number Dana has spent her whole career explaining to juries who want it to mean something simpler than it does.

The DA's office has a backlog of its own and wants a yes or a no, not a lecture on probability. Dana's unit has a written policy for exactly this moment, and today is the day she has to decide which version of it she's actually going to follow.

She turns the printout back over.

---

## Background

Dana Osei is the forensic statistician for a state crime laboratory's DNA unit, working alongside the state's Bureau of Forensic Services. She does not investigate cases and she does not decide guilt — her job is to tell the department, in writing, exactly what a DNA hit does and does not prove, before it becomes the centerpiece of someone's **referral**: the memo the lab sends to the district attorney's office recommending a charging decision.

A DNA **genetic profile** is a list of results at specific locations on the genome called **loci** (singular: **locus**) — think of a locus as one labeled slot in the list, and the result recorded there as one entry in that slot. CODIS's standard profile has 20 such slots. Two people's profiles "match" at a locus when their entries there are identical; a full match means every slot recorded agrees. A degraded sample — old, broken down, partially destroyed — often can't produce a reliable result at every slot, which is why this case's evidence sample only has a usable entry at 8 of the 20.

Mechanically, here is what "running a search" means: lab staff enter the evidence sample's locus-by-locus results into CODIS — software maintained by the FBI that every participating lab connects to — and the software automatically compares that list against every profile already stored, slot by slot, looking for an exact match. When a cold-case sample is too degraded to recover a full profile, the lab still runs this search — first against the state's own stored profiles (its DNA **data bank**, built from required DNA samples taken from convicted **offenders** and, in some states, from people arrested but not yet convicted — **arrestees**), then, if there's no match, against the FBI's National DNA Index System (NDIS), which pools participating states' data banks together (SEE APPENDIX A). This is not one search; it is two, run in sequence, against two databases of very different size (SEE APPENDIX B). A computer match ("hit") is a candidate only — lab staff then confirm it against the original physical sample before any name is released to investigators.

The lab's cold-case unit has exactly two policies on the table for handling a database "cold hit" — a match with no other evidence yet attached — and department leadership has asked Dana to model both before the unit commits for the year. **Refer on Match** sends the referral memo to the district attorney's office as soon as a search returns a hit, with no further lab-side delay. **Hold for Corroboration** keeps every cold-hit case in the unit for one additional step — a documented, independent, non-DNA cross-check, such as confirming the person's known location or associations line up with the crime — before it is referred, which costs investigator time on every single case but is designed to catch the cases where a hit was coincidence, not culprit. The cost of getting this wrong is not just wasted time: a referral that later has to be withdrawn carries **discovery obligations** (the legal requirement to disclose the error to the defense and the court) and real reputational and liberty consequences for whoever was wrongly named.

The core quantity separating the two policies is not the offender's guilt or innocence — it is the probability that a given hit is a **coincidental match**: two different people who happen to share a genetic profile at every locus the lab could recover, not because they're related, but by chance. That probability depends on how many loci were usable (a degraded sample yields fewer) and, separately, on how many other profiles the search compared against — a hit found by comparing against millions of records is not equivalent to a one-to-one comparison, a distinction with real statistical and legal history (SEE APPENDIX C). This year's caseload volume and the time cost of each policy are Dana's own unit's operating figures, not published anywhere (SEE APPENDIX D and APPENDIX E; both disclosed in full in APPENDIX F). Every figure in this case is either cited to a real source (SEE APPENDIX G) or disclosed as a stated Modeling Assumption. The vocabulary and "how to…" skills this case will ask you to research are listed in Appendix H.

---

## Dilemma

You are Dana Osei.

Do you:

**A.)** Recommend **Refer on Match** — send every cold hit to the DA's office for a charging decision as soon as the database search returns it, with no additional lab-side delay **OR**

**B.)** Recommend **Hold for Corroboration** — require one independent, non-DNA corroborating check on every cold hit before it is referred, adding investigator time to every case

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:

- **D1 — A random match probability (RMP) calculation.** Using Appendix C's per-locus match probability, calculate the RMP for this case's 8-usable-locus partial profile — the probability that two unrelated people would coincidentally share a matching genetic result at all 8 loci. Show why multiplying the per-locus probabilities together requires treating a match at each locus as an independent event, and state that assumption explicitly.
- **D2 — A two-stage database match probability (DMP) table.** Using Appendix B's two database sizes (the state data bank, searched first; the national NDIS, searched second) and your D1 result, calculate the database match probability at each stage of the search — the chance that *at least one* coincidental match would turn up by chance in a database that size. Show both stages and label which search actually produced this case's hit.
- **D3 — A cases-closed-per-detective-hour comparison.** Using Appendix D's caseload figures and Appendix E's per-case time costs, compute total detective-and-lab hours for a full year under Policy A and under Policy B, then compute the cases-closed-per-detective-hour rate for each. State the percent margin between them and which policy wins on this year's numbers.
- **D4 — A combination-vs-permutation calculation.** CODIS's core panel has 20 loci (Appendix A). Calculate how many different 10-locus subsets could be drawn from that panel (a combination), and separately calculate how many *ordered* selections of 10 loci from 20 are possible (a permutation). Explain in one paragraph why choosing which loci to test is a combination problem, not a permutation problem — and why that distinction is part of the reason CODIS requires every lab to test the *same* fixed panel rather than letting each lab pick its own subset.
- **D5 — A written explanation using Population, Sample, and Convenience Sampling.** The per-locus match probability in Appendix C comes from population genetics studies designed to sample many unrelated people at random. The database Dana searches is not that — it only contains people who were previously arrested or convicted. Using all three terms, explain in a short paragraph why the database being searched is not a random sample of the general population, and whether — and how — that distinction should change how confident anyone is in a "cold hit" by itself.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A — CODIS Architecture: The Three-Tier Search and the 20 Core Loci

Referenced in Background and Challenge 3 (D2, D4). The Combined DNA Index System (CODIS) operates at three levels: the **Local DNA Index System (LDIS)**, where a profile is first developed; the **State DNA Index System (SDIS)**, which lets laboratories within one state compare against each other; and the **National DNA Index System (NDIS)**, the top tier, which compares across every participating state [S4]. A profile that finds no match at the state level is eligible to be searched at the national level — this is exactly the two-stage search Dana's unit runs on every cold case.

Since January 1, 2017, every laboratory participating in NDIS has been required to type a profile at a minimum of 20 "CODIS core loci," up from the original 13 used since the 1990s. The FBI's own stated reason: as CODIS grew larger, expanding the core loci became "imperative... in order to reduce the possibility of fictitious matches," alongside gains in discriminating power and compatibility with international DNA databases [S5]. The 13 original core loci are CSF1PO, D3S1358, D5S818, D7S820, D8S1179, D13S317, D16S539, D18S51, D21S11, FGA, TH01, TPOX, and vWA; the 7 loci added in 2017 are D1S1656, D2S441, D2S1338, D10S1248, D12S391, D19S433, and D22S1045 [S5]. This case's evidence sample is too degraded to recover all 20 — only 8 loci produced a usable result (SEE APPENDIX C).

---

## Appendix B — Database Sizes Searched This Year

Referenced in Background and Challenge 3 (D2).

| Search stage | Database | Profiles searched | Source | As of |
|---|---|---|---|---|
| Stage 1 (searched first, no hit) | State DNA Index System — this state's Bureau of Forensic Services data bank | **3,368,310** | State DOJ Data Bank Program quarterly report [S1] | 2024-12-31 |
| Stage 2 (searched second — this is where the hit came from) | National DNA Index System (NDIS) | **18,000,000** (>14,000,000 offender profiles + >4,000,000 arrestee profiles) | Combined DNA Index System summary, citing FBI-published NDIS statistics [S2] | 2020-09 |

**A still-growing real system, frozen for this case.** Both real databases have continued to grow since the dates above — NDIS specifically has published monthly since the early 2000s and by design never stops adding profiles. This case fixes both counts at the dates in the table above and does not update them; every calculation in this case uses these two frozen values, not "today's" NDIS size.

---

## Appendix C — Match Probability Figures

Referenced in Background and Challenge 3 (D1, D2).

**Per-locus match probability.** Real, published per-locus random match probabilities vary by locus and by population group — there is no single true value. A commonly cited representative figure, drawn from courtroom testimony reported in the press, is that two unrelated people have roughly a **7.5% (0.075) chance of matching by coincidence at any single locus** [S3]. This case uses that figure as a stated representative average across loci; a real casework report would use the specific published allele-frequency table for the exact alleles observed, locus by locus, which this case does not have access to.

**This case's usable loci.** The evidence sample in this case produced a usable result at **8 of the 20 CODIS core loci** — this specific count (8) is a scenario construction for this case, chosen to be realistic for a degraded decade-old sample per real-world reporting that partial, degraded-sample profiles routinely recover fewer than the full core panel.

**The database match probability (DMP) rule.** A 1996 National Research Council report on forensic DNA evidence addressed exactly Dana's situation — a match found by *searching* a database, not by comparing one suspect to one piece of evidence. Its recommendation: "When the suspect is found by a search of DNA databases, the random-match probability should be multiplied by N, the number of persons in the database," producing what is called the database match probability [S6]. In symbols: **DMP = N × RMP**, where N is the number of profiles searched and RMP is the random match probability for the profile recovered.

---

## Appendix D — This Year's Cold-Hit Caseload

Referenced in Background and Challenge 3 (D3). All figures in this appendix are disclosed Modeling Assumptions — see Appendix F, MA1–MA2.

| Figure | Value | Applies to |
|---|---|---|
| Cold-hit cases reviewed by the unit this year | **60** | Both policies |
| Share of the unit's annual caseload recovered from a partial (fewer than 20-locus) profile like this case's | **60%** | Determines how many of the 60 hits reviewed carry this case's D2 database match probability |

---

## Appendix E — Policy Costs

Referenced in Background and Challenge 3 (D3). All figures in this appendix are disclosed Modeling Assumptions — see Appendix F, MA3–MA5.

| Cost | Value | When it applies |
|---|---|---|
| Base investigative file review, per cold-hit case | **6 hours** | Every case, under either policy |
| Independent corroboration step, per case | **3 hours** | Every case, **only under Policy B (Hold for Corroboration)** |
| Rework cost when a referral later turns out to have been a coincidental match | **200 hours** | Only under Policy A (Refer on Match), only for cases that turn out to be false — expected count computed from Appendix C's database match probability |

---

## Appendix F — Modeling Assumptions

> These figures are **not published anywhere** — no state or federal agency publishes a specific crime laboratory's annual cold-hit caseload, its partial-profile share, or its own internal time cost for a corroboration step or a referral walk-back. They are stated scenario assumptions chosen by the case author, set at a scale consistent with a real, mid-sized state forensic laboratory's cold-case unit. A Hero may challenge any of these numbers in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Cold-hit cases reviewed this year | 60 | No public source publishes a specific lab's annual cold-hit volume; set at a scale consistent with a state DNA unit actively working a backlog, informed by the real, published scale of state data-bank hit totals (SEE APPENDIX G, S1). | The case's totals scale with this figure, but the *ratio* between the two policies is not very sensitive to it alone — see `sensitivity_model.py`. |
| MA2 | Share of the annual caseload from a partial (sub-20-locus) profile | 60% | No public source publishes this split for any specific lab. Degraded, older cold-case evidence is realistically more likely to yield a partial profile than fresh evidence, which is the basis for setting this above 50%. | The case's numbers are sensitive to this figure — see `sensitivity_model.py`. |
| MA3 | Base investigative file review time, per case | 6 hours/case | No public source publishes a lab's internal file-review time. Applies equally under both policies, so it does not by itself change which policy wins — it sets the shared floor both totals are built on. | Low — affects both policies' totals equally. |
| MA4 | Corroboration step time, per case (Policy B only) | 3 hours/case | No public source publishes a specific corroboration procedure's time cost. Set as a modest fixed add-on representative of a documented alibi/location cross-check, not a full re-investigation. | Sensitive — see `sensitivity_model.py`. |
| MA5 | Rework cost per false referral (Policy A only) | 200 hours | No public source publishes this figure for any lab. Set well above the corroboration cost to reflect that walking back a referral already sent to the DA's office (re-investigation, discovery obligations, potential exposure from a wrongful referral) is a materially larger event than a routine corroboration check would have been — this asymmetry is the entire basis of the case's tension. | Highly sensitive — see `sensitivity_model.py`. |

---

## Appendix G — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Total DNA data bank profiles uploaded to a state's own CODIS since that state's data-bank law took effect | 3,368,310 | California Department of Justice, Bureau of Forensic Services — [Proposition 69 DNA Data Bank Program Report, Fourth Quarter 2024](https://www.oag.ca.gov/system/files/media/databank-quarterly-rpt-q4-2024.pdf) | as of 2024-12-31 | HIGH |
| S2 | National DNA Index System (NDIS) size | >14,000,000 offender profiles, >4,000,000 arrestee profiles (used here as 18,000,000 combined) | [Combined DNA Index System — Wikipedia](https://en.wikipedia.org/wiki/Combined_DNA_Index_System), citing FBI-published NDIS statistics | as of 2020-09 | MEDIUM (secondary republication of FBI data, not the FBI page directly — le.fbi.gov's own statistics page returned an access error when fetched directly) |
| S3 | Representative per-locus random match probability | ~7.5% (0.075) chance of a coincidental match at a single locus | [Are the F.B.I.'s Probabilities About DNA Matches Crazy? — Freakonomics](https://freakonomics.com/2008/08/are-the-fbis-probabilities-about-dna-matches-crazy/), reporting real courtroom testimony figures | accessed 2026-09-18 | MEDIUM (journalism reporting a real testified figure; real per-locus values vary by locus and population, so this is used as a representative average, not an exact figure for any one locus) |
| S4 | CODIS operates as a three-tier hierarchy (LDIS/SDIS/NDIS), with profiles searched at the state level before the national level | three levels as described | National Institute of Justice — [CODIS Hierarchy, Forensic DNA Education for Law Enforcement Decisionmakers](https://nij.ojp.gov/nij-hosted-online-training-courses/forensic-dna-education-law-enforcement-decisionmakers/partial-matches/codis-hierarchy); cross-checked against [Combined DNA Index System — Wikipedia](https://en.wikipedia.org/wiki/Combined_DNA_Index_System) | accessed 2026-09-18 | HIGH |
| S5 | CODIS core loci expanded from 13 to 20 on January 1, 2017, to reduce the possibility of fictitious/coincidental matches as the database grows, among other benefits; exact loci lists | 13 original + 7 added = 20 core loci, as listed | RTI International / SAKI (Sexual Assault Kit Initiative, DOJ Bureau of Justice Assistance-funded) — [Switching to 20 Core CODIS Loci and the Impact on SAKI Testing](https://www.sakitta.org/resources/docs/12104SAKIImpctSAKTstCoreLociv3.pdf) | published 2018 (2017 policy effective date stated in text) | HIGH |
| S6 | The 1996 National Research Council report's recommendation that a database-search match probability be computed as random-match-probability × N (the number of profiles in the searched database) | "the random-match probability should be multiplied by N, the number of persons in the database" | National Academies Press (National Research Council Committee on DNA Technology in Forensic Science, *The Evaluation of Forensic DNA Evidence*, 1996), hosted at NCBI Bookshelf — [Statistical Issues](https://www.ncbi.nlm.nih.gov/books/NBK232615/) | 1996 report; page accessed 2026-09-18 | HIGH |

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->

---

## Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Independent Event
- Permutation
- Multistage Sampling
- Convenience Sampling
- Conditional Probability
- Population
- Sample
- Random

**"How to…" questions**

- How to determine the number of outcomes of a permutation
- How to determine the number of outcomes of a combination
- How to determine the probability of conditional events
- How to determine the probability of a compound event
- How to find the percent of a number
