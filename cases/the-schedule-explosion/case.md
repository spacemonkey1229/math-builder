Case Study: The Schedule Explosion
MS | Math | Case Study | 2026 | Adventure

## Overview

The dashboard is still refreshing when Dara Osei's phone buzzes on the desk beside her keyboard: *VP sync — utilization review — 10 min.* She doesn't pick it up. Behind her, the data-hall's cooling fans hold their usual low roar, the same sound she's fallen asleep to twice this month on the office couch. On her second monitor, a terminal window sits open mid-command, cursor blinking after `./run_scheduler --mode=`.

Two words are typed after the flag, then deleted, then typed again. `full_sweep`. `greedy`. `full_sweep`.

She has spent three weeks building the "perfect" version — a scheduler that checks every possible way to line up tonight's training jobs before picking the one true best ordering, instead of the fast, good-enough rule the team has shipped with for a year. Tonight's batch is small, a test run before the real rollout. It finished the exhaustive check in under a minute. She has the numbers open in the next tab, and they're good — genuinely better than what the old scheduler would have produced.

The VP's calendar invite has one line in the notes field: *"How much idle GPU time did we recover this quarter, and can we keep recovering it as the fleet grows?"*

Dara has not yet run the exhaustive check against how many jobs a *real* night's batch will have once the new GPUs finish landing. She minimizes the terminal, opens a blank sheet, and starts typing a number into the first cell of a new column: job count.

Her cursor sits in the next cell, empty, waiting for the number that comes after it.

## Background

Dara Osei has led the scheduling team at Vantage Compute, a mid-size AI cloud provider, for two years. Vantage rents out access to a fleet of Nvidia GPUs — Nvidia is the dominant supplier of the AI accelerators that cloud providers like Vantage, and far larger ones, are racing to deploy; real 2026 announcements describe cloud partners adding GPUs by the million [S2] (SEE APPENDIX E). Every night, Vantage's scheduler has to decide the order in which that night's queued training jobs run through a single shared pipeline stage — the model-and-container loading step every job passes through before it can start using the GPUs. Switching from one job to a very different one on that shared pipeline costs real idle time: nothing computes while the new job's environment loads (SEE APPENDIX A), and real published benchmarks of AI model-loading time on GPU nodes show this kind of loading step can easily run from just over a minute to several minutes depending on what is being loaded [S3].

For months, Vantage's production scheduler has run **The Greedy Queue**: whichever not-yet-run job would cost the least to switch into right now, run it next. It is fast and it always finishes. Dara's new project, **The Full Sweep**, asks a different question: for a given night's batch, is there some *other* ordering of the same jobs that wastes less total idle time — the genuinely best one, not just a good one? To answer that for certain, a scheduler has to check every possible ordering of that night's jobs and compare their total idle time directly. The number of possible orderings of a batch of jobs is a real, well-known fact from computer science: it is the factorial of the job count, and job-scheduling problems built on exactly this fact are formally classified as computationally hard for exactly this reason [S1] (SEE APPENDIX E). Appendix B lists the job counts Dara needs to check, from tonight's small test batch up through the batch sizes Vantage's own fleet growth will produce within the year. The vocabulary and "how to…" procedure needed to work through those job counts are listed in (SEE APPENDIX F).

Dara's team's headcount for next quarter is tied to a target the VP set for reducing idle GPU time — and idle GPU time is also, in the most literal sense, unsold compute Vantage is paying for and not renting out. Whichever strategy she recommends tonight has to be the one that keeps working as Vantage's fleet, and its nightly batch sizes, keep growing.

## Dilemma

You are Dara Osei.
Do you:
A.) Ship The Full Sweep — commit to always finding the true, provably optimal job ordering by exhaustively checking every possible ordering of that night's batch OR
B.) Ship The Greedy Queue — keep the fast nearest-neighbor rule already in production, accepting a calculable, bounded amount of extra idle time in exchange for a schedule that finishes instantly at any job count

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A factorial table: for each job count n listed in Appendix B (4, 6, 8, 10, 12, 15, 18, and
    20), evaluate n! — the number of possible orderings of a batch of that size — showing your
    method in full for at least three of the values.
    D2. Using Appendix C's assumed schedule-search speed, convert each of your D1 values into the
    total time a complete Full-Sweep search of that job count's orderings would take (in seconds,
    hours, days, or years, whichever is clearest), and compare each one to Vantage's fixed
    eight-hour nightly batch window (Appendix B). State, with your arithmetic shown, the largest
    job count at which The Full Sweep still finishes inside that window, and the smallest job
    count at which it does not.
    D3. For Appendix A's six-job pilot batch: first restate your D1 value for 6! and confirm, in
    your own words, that it is small enough for a real exhaustive search to actually examine every
    single ordering. Then carry out that exhaustive search (by hand, spreadsheet, or systematic
    listing — show your method) to find The Full Sweep's true-optimal total idle time for the six
    jobs. Separately, apply The Greedy Queue's nearest-neighbor rule (Appendix D) to the same six
    jobs to find its total idle time. Report both totals and the percent margin between them, with
    your arithmetic shown.
    D4. A written explanation, referencing at least two specific job-count/search-time pairs from
    your D2 table, of why Vantage's team cannot simply "wait for faster computers" to make The Full
    Sweep work at realistic nightly job counts. Your explanation must state, in your own words,
    what a factorial is and why it grows the way it does.
    D5. An original visual display (a bar or line chart, using a logarithmic vertical scale) plotting
    job count against either n! or total Full-Sweep search time, across all of your D1/D2 job
    counts, showing the shape of the explosion.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — Vantage's Six-Job Pilot Batch: Switchover-Cost Matrix

Referenced in Background and Challenge 3 (D3). These six jobs are Vantage's smallest realistic
test batch, run nightly through the shared model-loading pipeline before the full fleet's batch
runs, listed in the order they were submitted to the queue that night (LLM Fine-Tune first). Each
cell is the idle time (in minutes) the pipeline loses switching from the row job directly into the
column job, before the column job can start using the GPUs.

| From \ To | LLM Fine-Tune | Vision Transformer | Diffusion Model | Speech Model | Recommender | Anomaly Detector |
|---|---|---|---|---|---|---|
| **LLM Fine-Tune** | — | 18 [MA1] | 21 [MA1] | 29 [MA1] | 22 [MA1] | 24 [MA1] |
| **Vision Transformer** | 20 [MA1] | — | 12 [MA1] | 13 [MA1] | 9 [MA1] | 27 [MA1] |
| **Diffusion Model** | 24 [MA1] | 12 [MA1] | — | 18 [MA1] | 19 [MA1] | 16 [MA1] |
| **Speech Model** | 28 [MA1] | 26 [MA1] | 23 [MA1] | — | 7 [MA1] | 8 [MA1] |
| **Recommender** | 23 [MA1] | 10 [MA1] | 18 [MA1] | 26 [MA1] | — | 27 [MA1] |
| **Anomaly Detector** | 28 [MA1] | 7 [MA1] | 18 [MA1] | 11 [MA1] | 8 [MA1] | — |

## Appendix B — Vantage's Batch Sizes, Today and As The Fleet Grows

Referenced in Background and Challenge 3 (D1, D2). Vantage's nightly batch window is fixed at
8 hours [MA3] before the next day's jobs must begin loading. The job counts below span Vantage's
current smallest test batch up through batch sizes its own fleet-growth plans point toward within
the year (SEE APPENDIX E for the real, publicly announced GPU-fleet growth this scaling is
grounded in):

| Job count (n) | Context |
|---|---|
| 4 | smallest illustrative case |
| 6 | Vantage's actual six-job pilot batch (Appendix A) |
| 8 | small test batch |
| 10 | small test batch |
| 12 | Vantage's current typical nightly batch size |
| 15 | near-term projected batch size |
| 18 | one-year projected batch size |
| 20 | one-year projected batch size, upper estimate |

## Appendix C — Vantage's Assumed Schedule-Search Speed

Referenced in Challenge 3 (D2). To find the true optimal ordering, The Full Sweep must evaluate
the total idle time of every possible ordering of a batch and keep the best one. Vantage's own
scheduling code has not yet been benchmarked at realistic job counts, so this case states an
assumed evaluation speed rather than an unsourced "typical" number:

| | Value |
|---|---|
| Orderings The Full Sweep can fully evaluate per second | 10,000,000 [MA2] |

## Appendix D — The Greedy Queue's Nearest-Neighbor Rule

Referenced in Background and Challenge 3 (D3). The Greedy Queue is Vantage's production scheduler.
Its rule is fixed and simple: starting from the first job submitted to the queue that night
(Appendix A's top row, LLM Fine-Tune), always run whichever not-yet-run job has the lowest
switchover cost from the job that just finished — never look ahead, never reconsider a job once it
has run. This is the standard nearest-neighbor heuristic used broadly in routing and scheduling
problems [S4] (SEE APPENDIX E).

## Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Appendix A's switchover-cost matrix (idle minutes per job-to-job transition) | 6-by-6 matrix, values 7-29 minutes (see Appendix A) | No public data exists for Vantage's specific job-to-job container/checkpoint reload overheads. The case sets a matrix whose values fall inside the real, benchmarked range for AI model-loading time on GPU nodes [S3] (roughly 1 to 8 minutes for a single model load), extended somewhat higher on some pairs to represent a full training-job environment switch (a new container image plus a new dataset mount plus a new checkpoint), which is a larger operation than loading one inference model. | The margin between The Full Sweep and The Greedy Queue on the six-job pilot batch is sensitive to the relative differences within this matrix, though not to its overall scale — scaling every value in the matrix up or down by the same factor does not change which strategy wins or by how much. |
| MA2 | Appendix C's assumed schedule-search evaluation rate | 10,000,000 orderings evaluated per second | No public benchmark exists for Vantage's own (not-yet-built) exhaustive schedule-search code. The case assumes a conservative rate for a simple, compiled loop that sums a handful of lookup-table values per ordering — well within general-purpose modern hardware's throughput for simple arithmetic on short lists. | Changing this value shifts exactly which job count crosses from feasible to infeasible inside the eight-hour window, but a factorial's growth guarantees some crossing point exists regardless of the exact rate chosen — even a rate a thousand times faster only delays, and does not remove, the explosion. |
| MA3 | Vantage's nightly batch window | 8 hours | Stated as a round, representative overnight window between the close of one business day's job submissions and the start of the next day's interactive workloads — a common pattern in batch-computing operations generally, not a figure specific to any named real provider's published schedule. | A shorter or longer window changes exactly which job count from Appendix B first exceeds it, but does not change the underlying factorial growth rate itself. |

## Appendix E — Real-World Grounding and Sources

Referenced in Background, Appendix B, and Appendix D. All figures and facts in this case are cited
in the table below.

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | The number of feasible orderings/solutions for a job-scheduling problem of n jobs is n!, and job-scheduling problems built on this fact are formally classified as computationally hard (NP-hard) | n! feasible solutions | Cornell University — [Cornell Engineering Computational Optimization Open Textbook, "Job shop scheduling"](https://optimization.cbe.cornell.edu/index.php?title=Job_shop_scheduling) | accessed 2026-09-09 | HIGH |
| S2 | Real, publicly announced 2026 growth in deployed Nvidia GPU fleets among major cloud providers | 2,000,000 additional GPUs (AWS, 2027-2028), building on a prior announcement of over 1,000,000 GPUs starting 2026 | NVIDIA Corporation — [AWS and NVIDIA to Deliver 2 Million Additional GPUs and Next-Generation Infrastructure for Agentic and Physical AI](https://investor.nvidia.com/news/press-release-details/2026/AWS-and-NVIDIA-to-Deliver-2-Million-Additional-GPUs-and-Next-Generation-Infrastructure-for-Agentic-and-Physical-AI/default.aspx) | 2026-08-26 | HIGH |
| S3 | Real benchmarked range for AI model-loading/container-reload time on a GPU node | approx. 82 seconds (67 GiB model, unoptimized) to approx. 457 seconds (203 GiB model, unoptimized) | Amazon Web Services — [Fast model loading for AI inference on Amazon EKS](https://aws.amazon.com/blogs/containers/fast-model-loading-for-ai-inference-on-amazon-eks/) | accessed 2026-09-09 | HIGH |
| S4 | The nearest-neighbor rule (always move next to whichever unvisited option is cheapest from the current one) is a standard, widely used heuristic for routing and scheduling problems | standard named heuristic | Wikipedia — [Nearest neighbour algorithm](https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm) | accessed 2026-09-09 | MEDIUM |

## Appendix F — "How To…" Math Questions To Research

**Vocabulary terms**

- Factorial

**"How to…" questions**

- How to evaluate a factorial expression

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
