#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Trial Size.

Tier 2 probe 5 ("flex each stated assumption by +-50%; report which flips
the verdict") needs a runnable model of the case's own arithmetic.

CONTRACT — two public names:

    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

REBUILD 2026-09-02 (Tier2 P5 was FAIL: the previous version of this file
modeled the case's SUPERSEDED $/cluster metric. The current primary_metric
(case.json.balance) is the worst-case 95% CI half-width produced by the
real, sourced Henderson & Sundaresan (1982) cluster-survey precision
formula:

    d = z * sqrt(deff * p * (1 - p) / n)

applied to each option's real sample sizes (case.md Appendix D). d is a
COST (a CI half-width) -- lower is better -- but the probe's contract is
"higher is better", so evaluate() returns the NEGATIVE of each option's
worst-case d, exactly the convention the cost-minimization reference model
(skills/case-readiness/scripts/example_sensitivity_model.py's own sibling
cost cases) uses: negate the thing where lower wins so max() still finds
the true winner and the flip-probe's higher-is-better logic works
unmodified.

Option A (Full Precision) collects data ONLY in the existing district, at
n = 658 [S1]. Its worst (and only) CI half-width is d(658).

Option B (Reserve And Expand) collects data in TWO places: the existing
district at the certified-adequate n = 192 [S3], and a newly opened
district at n = new_clusters * density_per_cluster = 8 * 12 = 96
(Appendix C). Its worst-case CI half-width is the WIDER (weaker) of the
two -- a campaign report is only as trustworthy as its loosest estimate --
which is structurally always the new district here since 96 < 192.

PARAMS holds every dial the case states, cited or assumed. FLEX sweeps
ONLY the two entries case.json's own modeling_assumptions[] actually
flags as author-chosen conventions (MA1, MA2) -- not the real,
Carcelen-et-al.-sourced sample sizes (658, 192) or the WHO-sourced z/deff,
per SPEC §2's "flex the stated ASSUMPTION, not the cited data" rule.

Verified against case.json / case.md Appendix A/C/D:
    base   A: d = 1.96*sqrt(2*0.25/658)      = 0.0537 -> 5.4%
    base   B: d = 1.96*sqrt(2*0.25/96)       = 0.1414 -> 14.1%
                (existing-district d = 1.96*sqrt(2*0.25/192) = 0.1000 -> 10.0%,
                 not the binding one -- 96 is B's weakest link)
    margin_pct = 100*(14.1-5.4)/14.1 = 61.7%  -> matches case.json (61.7)
    winner: A (Full Precision)
"""
import math

PARAMS = {
    # --- Appendix D: WHO EPI precision formula parameters (S7, S8) -----------
    "z": 1.96,
    "deff": 2.0,
    # --- MA1: max-variance convention (case.json.modeling_assumptions) -------
    #     Stated HIGH confidence ("standard, universally-used... not an
    #     invented number") but it IS a disclosed Modeling Assumption, not a
    #     directly-sourced figure, so it is swept in FLEX per MA1's own id.
    "p": 0.5,
    # --- Appendix A: Full Precision's real total participant count (S1) ------
    "n_full": 658.0,
    # --- Appendix A: certified-adequate minimum sample size, existing
    #     clusters, Reserve And Expand (S3) -------------------------------------
    "n_existing_b": 192.0,
    # --- Appendix C: number of new clusters Reserve And Expand's freed
    #     budget opens (floor($13,980 / $1,620/cluster), a real derived
    #     count, not itself a Modeling Assumption) ------------------------------
    "new_clusters": 8.0,
    # --- MA2: new-cluster participant density (case.json.modeling_assumptions)
    #     192 / 16 existing clusters = 12/cluster, reused for new clusters.
    #     This is the disclosed assumption that directly determines the new
    #     district's CI half-width, and therefore the case's margin_pct. -------
    "density_per_cluster": 12.0,
}

# Probe 5 flexes THESE and only these: the two entries case.json's own
# modeling_assumptions[] (MA1, MA2) actually name as author-chosen
# conventions. Real cited data (n_full, n_existing_b, z, deff, new_clusters)
# is stress-tested by the data-decay probe (P6) instead, not this one.
FLEX = [
    "p",                    # MA1 -- max-variance convention
    "density_per_cluster",  # MA2 -- new-cluster participant density
]


def _half_width(p, n):
    """d = z * sqrt(deff * p * (1 - p) / n), the Henderson & Sundaresan
    (1982) cluster-survey CI half-width formula (case.md Appendix D)."""
    if n <= 0:
        return float("inf")
    return p["z"] * math.sqrt(p["deff"] * p["p"] * (1.0 - p["p"]) / n)


def evaluate_detail(params):
    p = dict(PARAMS)
    p.update(params or {})

    d_full = _half_width(p, p["n_full"])

    n_new = p["new_clusters"] * p["density_per_cluster"]
    d_existing_b = _half_width(p, p["n_existing_b"])
    d_new = _half_width(p, n_new)
    d_worst_b = max(d_existing_b, d_new)  # B's weakest link

    detail_a = {"n": p["n_full"], "d": d_full, "d_pct": 100.0 * d_full}
    detail_b = {
        "n_existing": p["n_existing_b"],
        "d_existing": d_existing_b,
        "n_new": n_new,
        "d_new": d_new,
        "d_worst": d_worst_b,
        "d_worst_pct": 100.0 * d_worst_b,
    }
    # Lower CI half-width is better; evaluate()'s contract is "higher is
    # better", so return the negated half-width (matches the convention
    # used by this pipeline's other cost-minimization sensitivity models).
    return {"A": -d_full, "B": -d_worst_b}, detail_a, detail_b


def evaluate(params):
    """Tier 2 probe 5 contract: evaluate(params) -> {'A': metric, 'B': metric}
    ONLY -- no extra return values. Full diagnostics in evaluate_detail()."""
    r, _a, _b = evaluate_detail(params)
    return r


if __name__ == '__main__':
    base, a, b = evaluate_detail({})
    win = max(base, key=base.get)  # higher (less negative) evaluate() value wins
    lo = min(base, key=base.get)
    win_d, lo_d = -base[win], -base[lo]  # back to actual CI half-width (decimal)
    margin = 100.0 * (lo_d - win_d) / lo_d  # % tighter the winner is than the loser
    print("Option A (Full Precision):")
    for k, v in a.items():
        print(f"  {k}: {v}")
    print("Option B (Reserve And Expand):")
    for k, v in b.items():
        print(f"  {k}: {v}")
    print()
    print("CI half-width  A=%.4f (%.1f%%)  B=%.4f (%.1f%%)" % (-base["A"], -base["A"] * 100, -base["B"], -base["B"] * 100))
    print("winner:", win, " margin: %.2f%%" % margin)
