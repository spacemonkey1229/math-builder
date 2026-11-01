"""
sensitivity_model.py -- The Schedule Explosion

Graded primary metric (case.json.primary_metric): total idle GPU-minutes wasted
by each scheduling strategy on Appendix A's six-job pilot batch -- the only
batch size in this case small enough for a real exhaustive search over all
6! = 720 orderings. Lower idle time is better, so evaluate() returns the
NEGATIVE of each option's idle-minute total -- higher score = better, matching
this script's "higher wins" convention (same convention as
cases/the-minimum-payment-trap/sensitivity_model.py).

    Option A, The Full Sweep:   true optimum over ALL n! orderings of the
                                 switchover-cost matrix (brute-force / exhaustive
                                 search -- feasible only because n=6 here).
    Option B, The Greedy Queue: nearest-neighbor heuristic -- from the current
                                 job, always move to whichever unvisited job is
                                 cheapest to switch into next.

Appendix A's switchover-cost matrix (MA1) and Appendix C's assumed
schedule-search evaluation rate (MA2) and Appendix B's 8-hour batch window
(MA3) are this case's three stated Modeling Assumptions -- no sourced/cited
figure needed flexing here since nothing was cited as fact (RESEARCH_LOG.md).
Only MA1 (switchover_scale) is swept by P5 by default: it is the assumption
that is actually wired into evaluate()'s A/B comparison. MA2/MA3 change the
D2 FEASIBILITY-CROSSING job count (which n stops fitting the 8-hour window),
not the six-job graded margin itself, so they are exposed as separate PARAMS
and a separate helper (search_time_seconds / feasibility_crossing) rather than
swept by the required evaluate() contract -- consistent with
skills/the-minimum-payment-trap's treatment of its own non-margin dial.

Verified against case.json.balance / FACILITATOR.md's margin arithmetic:
    base   Full Sweep (A)  = 62 idle minutes (optimal order, exhaustive search)
           Greedy Queue (B) = 72 idle minutes (nearest-neighbor from LLM Fine-Tune)
           margin = |72-62|/72 = 13.9%  (A wins -- matches case.json)
"""

import itertools

JOB_NAMES = ["LLM Fine-Tune", "Vision Transformer", "Diffusion Model",
             "Speech Model", "Recommender", "Anomaly Detector"]

PARAMS = {
    # --- Appendix A [MA1], stated scenario assumption ------------------------
    # switchover_matrix[i][j] = idle minutes switching FROM job i TO job j.
    "switchover_matrix": [
        [0, 18, 21, 29, 22, 24],
        [20, 0, 12, 13, 9, 27],
        [24, 12, 0, 18, 19, 16],
        [28, 26, 23, 0, 7, 8],
        [23, 10, 18, 26, 0, 27],
        [28, 7, 18, 11, 8, 0],
    ],
    # Uniform scale factor applied to every cell in switchover_matrix -- the
    # dial P5 actually flexes (see module docstring: scaling does not change
    # WHICH ordering wins for either strategy, since both the exhaustive search
    # and the nearest-neighbor comparisons are all done via same-sign relative
    # comparisons that are unaffected by a positive uniform rescale -- so the
    # ratio-based margin is provably invariant to this dial. This is an honest,
    # informative finding, not a script bug: see RESEARCH_LOG.md).
    "switchover_scale": 1.0,
    # --- Appendix C [MA2], stated scenario assumption -------------------------
    "eval_rate_per_sec": 10_000_000.0,
    # --- Appendix B [MA3], stated scenario assumption -------------------------
    "batch_window_hours": 8.0,
}

# The one scenario assumption wired into the graded A/B margin.
FLEX = ["switchover_scale"]


def _scaled_matrix(p):
    scale = p["switchover_scale"]
    return [[v * scale for v in row] for row in p["switchover_matrix"]]


def _exhaustive_optimum(matrix):
    n = len(matrix)
    best = None
    best_order = None
    for perm in itertools.permutations(range(n)):
        cost = sum(matrix[perm[i]][perm[i + 1]] for i in range(n - 1))
        if best is None or cost < best:
            best = cost
            best_order = perm
    return best, best_order


def _nearest_neighbor(matrix, start=0):
    n = len(matrix)
    unvisited = set(range(n)) - {start}
    cur = start
    order = [start]
    cost = 0.0
    while unvisited:
        nxt = min(unvisited, key=lambda j: matrix[cur][j])
        cost += matrix[cur][nxt]
        cur = nxt
        order.append(cur)
        unvisited.remove(cur)
    return cost, order


def evaluate(params=None):
    """Returns {"A": score, "B": score} for the six-job pilot batch (the graded metric).
    Score is NEGATIVE total idle minutes (higher score = less waste = better)."""
    p = dict(PARAMS)
    p.update(params or {})
    matrix = _scaled_matrix(p)
    opt_cost, _ = _exhaustive_optimum(matrix)
    nn_cost, _ = _nearest_neighbor(matrix, start=0)
    return {"A": -opt_cost, "B": -nn_cost}


def evaluate_detail(params=None):
    """Full detail (orders + costs) for both strategies -- facilitator/report use."""
    p = dict(PARAMS)
    p.update(params or {})
    matrix = _scaled_matrix(p)
    opt_cost, opt_order = _exhaustive_optimum(matrix)
    nn_cost, nn_order = _nearest_neighbor(matrix, start=0)
    return {
        "A": {"idle_minutes": opt_cost, "order": [JOB_NAMES[i] for i in opt_order]},
        "B": {"idle_minutes": nn_cost, "order": [JOB_NAMES[i] for i in nn_order]},
    }


def factorial_table(job_counts=(4, 6, 8, 10, 12, 15, 18, 20)):
    import math
    return {n: math.factorial(n) for n in job_counts}


def search_time_seconds(params=None, job_counts=(4, 6, 8, 10, 12, 15, 18, 20)):
    """D2's conversion of n! into total Full-Sweep search time at the assumed eval rate."""
    p = dict(PARAMS)
    p.update(params or {})
    ft = factorial_table(job_counts)
    return {n: ft[n] / p["eval_rate_per_sec"] for n in job_counts}


def feasibility_crossing(params=None, job_counts=(4, 6, 8, 10, 12, 15, 18, 20)):
    """The largest feasible n and smallest infeasible n against the batch window."""
    p = dict(PARAMS)
    p.update(params or {})
    window_s = p["batch_window_hours"] * 3600.0
    times = search_time_seconds(p, job_counts)
    feasible = [n for n in job_counts if times[n] <= window_s]
    infeasible = [n for n in job_counts if times[n] > window_s]
    return {
        "largest_feasible": max(feasible) if feasible else None,
        "smallest_infeasible": min(infeasible) if infeasible else None,
        "window_seconds": window_s,
        "times": times,
    }


if __name__ == '__main__':
    base = evaluate({})
    ia, ib = -base["A"], -base["B"]
    win = "A" if ia < ib else "B"
    lo, hi = min(ia, ib), max(ia, ib)
    margin = 100.0 * (hi - lo) / hi
    print("Six-job pilot batch idle minutes: A(Full Sweep)=%.0f  B(Greedy Queue)=%.0f  winner=%s  margin=%.1f%%" %
          (ia, ib, win, margin))

    d = evaluate_detail({})
    print("Full Sweep order:", " -> ".join(d["A"]["order"]))
    print("Greedy Queue order:", " -> ".join(d["B"]["order"]))

    fc = feasibility_crossing({})
    print("Largest feasible n inside %.0fh window: %s" % (PARAMS["batch_window_hours"], fc["largest_feasible"]))
    print("Smallest infeasible n: %s" % fc["smallest_infeasible"])
    for n, t in fc["times"].items():
        print("  n=%2d  n!=%d  search_time=%.6g sec" % (n, factorial_table([n])[n], t))
