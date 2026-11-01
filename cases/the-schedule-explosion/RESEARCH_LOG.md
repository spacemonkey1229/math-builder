# Research Log — The Schedule Explosion

Stage 3 (`case-research`) run on `cases/the-schedule-explosion/`. 5 `{{NEEDS_SOURCE}}` token
classes enumerated at write time: (P01) Appendix A's 30 switchover-cost cells, (P02) Appendix B's
nightly batch window, (P03) Appendix C's assumed schedule-search evaluation rate, plus the two
Modeling-Assumptions basis statements for MA1/MA2. Worked in load-bearing order: first the two real,
sourceable facts the case's narrative and math both depend on (the factorial-explosion fact itself,
and real GPU-fleet growth for scale-grounding), then the one real benchmarked range that grounds the
switchover-cost Modeling Assumption, then the definitional nearest-neighbor citation, then the three
scenario-specific numbers that genuinely have no public source and were declared as Modeling
Assumptions.

## P01 — The core math fact: n! possible job orderings

**Searched:**
- "job shop scheduling problem NP-hard proof number of possible orderings n! factorial"
- "job shop scheduling factorial explosion feasible solutions"

**Fetched directly:**
- `https://optimization.cbe.cornell.edu/index.php?title=Job_shop_scheduling` — Cornell Engineering's
  Computational Optimization Open Textbook. States directly: "There are n! feasible solutions for a
  job shop scheduling problem, therefore there are 4! = 24 feasible solutions for this example." A
  primary academic source, not a blog or forum summary.

**Outcome:** SOURCED as [S1], HIGH confidence. This is the pure math fact the entire case's dilemma
is built on — no proprietary or company-specific data was needed for it, exactly as the approved
concept sheet's feasibility note predicted ("the factorial-explosion point is a pure math fact").

## P02 — Real GPU fleet growth (scale-grounding, non-load-bearing)

**Searched:**
- "Nvidia GPU cluster deployment 100000 GPUs 2026 customer announcement"

**Fetched directly:**
- `https://investor.nvidia.com/news/press-release-details/2026/AWS-and-NVIDIA-to-Deliver-2-Million-Additional-GPUs-and-Next-Generation-Infrastructure-for-Agentic-and-Physical-AI/default.aspx`
  — NVIDIA's own investor-relations press release, dated 2026-08-26. Confirms a real, named,
  2026-era announcement: AWS and NVIDIA plan to deploy 2 million additional GPUs (Blackwell Ultra,
  Rubin, Rubin Ultra) across AWS's global infrastructure in 2027-2028, building on a prior
  announcement of over 1 million GPUs starting in 2026.

**Outcome:** SOURCED as [S2], HIGH confidence. Used only as real-world narrative color establishing
that Nvidia is the real, named dominant AI-accelerator vendor and that GPU fleets are growing fast
enough in 2026 that a smaller provider's nightly batch job counts plausibly grow too — not a number
any deliverable computes with directly, and not needed at the precision of a specific fleet size for
the fictional Vantage Compute.

## P03 — Real benchmarked range for AI model-loading time (grounds MA1's basis)

**Searched:**
- "GPU container cold start model loading time minutes AI inference"

**Fetched directly:**
- `https://aws.amazon.com/blogs/containers/fast-model-loading-for-ai-inference-on-amazon-eks/` — AWS's
  own engineering blog. Reports concrete, benchmarked before/after load times on p5.48xlarge
  instances: a 67 GiB model's unoptimized load = 82 seconds; a 203 GiB model's unoptimized load =
  457 seconds (roughly 1.4 to 7.6 minutes).

**Outcome:** SOURCED as [S3], HIGH confidence (a primary vendor engineering blog with concrete
benchmark numbers, not a proxy or an undated estimate). This range is the basis for Modeling
Assumption MA1 (Appendix A's switchover-cost matrix), not a value directly restated in the case:
Appendix A's matrix values (7-29 minutes) run somewhat higher than S3's 1.4-7.6 minute range because
a full training-job environment switch (new container image + new dataset mount + new checkpoint) is
a larger real operation than S3's single-inference-model load — the case is honest about this
extrapolation rather than presenting S3's inference-specific numbers as if they were the case's own
figures.

## P04 — Nearest-neighbor as a standard, real named technique (non-load-bearing)

**Searched:**
- "nearest neighbor heuristic traveling salesman percent worse than optimal average"

**Fetched directly:**
- `https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm` — confirms the nearest-neighbor rule is
  a standard, widely documented heuristic for routing/scheduling problems. **Rejected** as a source
  for any load-bearing "X% worse than optimal on average" figure: the article's only concrete claim
  is about unbounded WORST-CASE behavior ("for every constant r there is an instance... greater than
  r times the optimal tour"), not a defensible average-case percentage. Some secondary sources found
  in search results claimed "~15% worse on average" or "~25% average error," but neither traced to a
  primary, citable study with a clear, consistent methodology — exactly the kind of contested,
  poorly-sourced figure SPEC §5 says to exclude rather than launder into the case.

**Outcome:** SOURCED as [S4], MEDIUM confidence, but ONLY for the narrow, definitional claim that
nearest-neighbor is a real, standard, named heuristic (Appendix D) — not for any percentage. **No
external "heuristics are typically N% worse than optimal" figure appears anywhere in this case.**
The actual margin between The Full Sweep and The Greedy Queue (13.9%) is instead computed directly
from the case's own six-job switchover-cost matrix (Appendix A, a stated Modeling Assumption) via a
real exhaustive search and a real nearest-neighbor simulation (`sensitivity_model.py`) — a
case-specific, verifiable computation, not an imported statistic.

## MA1, MA2, MA3 — the three genuine NOT FOUND figures, declared as Modeling Assumptions

**Searched (before declaring NOT FOUND):**
- "AI training job GPU checkpoint reload container switch time minutes" — returned only the same
  inference-serving cold-start figures already captured as [S3]; nothing published specifically for
  a *training*-job-to-training-job environment switch on a shared multi-tenant scheduling pipeline.
- "GPU cluster nightly batch scheduling window hours AI training" — no public source states any real
  provider's specific nightly batch window length; this is an internal operational parameter no
  company publishes.
- "combinatorial schedule search evaluations per second solver throughput" — no public benchmark
  exists for a specific, not-yet-built exhaustive job-ordering search of the kind this fictional case
  describes; general solver-throughput figures found were for entirely different problem classes
  (SAT solvers, MILP) and would have been a misleading proxy, not a genuine match.

**Outcome:** Genuine NOT FOUND on all three, after real search attempts and one direct fetch attempt
each. Per SPEC §5's three exits, all three are **stated Modeling Assumptions** (never a redesign,
since removing them would remove the case's own scenario entirely, and never dropped, since all
three are load-bearing to the deliverables):

- **MA1** (Appendix A's switchover-cost matrix): value used is the specific 6x6 matrix in the case
  (7-29 minutes per cell), basis stated in `case.md`'s Modeling Assumptions block, grounded in but
  not equal to [S3]'s real inference-loading range.
- **MA2** (Appendix C's assumed schedule-search evaluation rate): 10,000,000 orderings/second, a
  conservative estimate for a simple compiled loop, stated basis in `case.md`.
- **MA3** (Appendix B's 8-hour nightly batch window): a round, representative overnight window,
  explicitly NOT claimed to be any specific real provider's published schedule.

## Note on the graded margin's dependence on Modeling Assumptions

Unlike `cases/the-minimum-payment-trap` (which needed zero Modeling Assumptions), this case's graded
six-job margin (13.9%) depends directly on MA1's switchover-cost matrix — the matrix is not a
side detail, it IS the data the exhaustive search and the nearest-neighbor heuristic both run against.
This is disclosed plainly in `case.json.balance.margin_basis`, in `case.md`'s Modeling Assumptions
block, and is the reason `sensitivity_model.py`'s `FLEX` includes `switchover_scale` (P5 must sweep
this). MA2 and MA3 do NOT affect the six-job graded margin at all — they only affect D2's
feasibility-crossing job count (which n first exceeds the batch window) — and are therefore exposed
as separate PARAMS rather than swept by the required `evaluate()` A/B contract, matching the same
distinction `the-minimum-payment-trap`'s model draws between its graded-window dial and its
non-graded dials.

## Summary table

| ID | Placeholder | Resolution | Value | Confidence |
|---|---|---|---|---|
| P01 | n! feasible orderings fact | SOURCED (S1) | n! feasible solutions | HIGH |
| P02 | Real GPU fleet growth (narrative grounding) | SOURCED (S2) | 2,000,000 additional GPUs, AWS/Nvidia | HIGH |
| P03 | Real model-loading time range (grounds MA1) | SOURCED (S3) | 82s-457s (67GiB-203GiB models) | HIGH |
| P04 | Nearest-neighbor as a standard technique (non-load-bearing) | SOURCED (S4) | standard named heuristic | MEDIUM |
| MA1 | Appendix A switchover-cost matrix | ASSUMPTION | 6x6 matrix, 7-29 min | n/a |
| MA2 | Appendix C evaluation rate | ASSUMPTION | 10,000,000/sec | n/a |
| MA3 | Appendix B batch window | ASSUMPTION | 8 hours | n/a |

Sourced: 4 (S1-S4). Assumption: 3 (MA1-MA3). Dropped: 0. Open: 0.

## Next step

Run `case-readiness` on `the-schedule-explosion`.
