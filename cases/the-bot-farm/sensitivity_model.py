#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- The Bot Farm.

Tier 2 probe 5 ("flex each stated assumption by +-50%; report which flips
the verdict") needs a runnable model of the case's own arithmetic.

CONTRACT -- two public names:

    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

The case's SPEC Section 2 primary metric (case.json.balance.margin_basis) is
confirmed-bot accounts removed per real (false-positive) account wrongly
suspended, for each cluster:

    ratio = confirmed_bots / false_positives
          = flagged * (1 - p) / (flagged * p)
          = (1 - p) / p

where p is the cluster's modeled false-positive rate (MA6 for Ring Alpha,
MA7 for Wave Nine). Higher ratio is better, matching the probe's "higher is
better" contract directly -- no negation needed (unlike a cost metric).

Mechanism modeled explicitly (this is the whole point of the case): the
ratio is ALGEBRAICALLY INDEPENDENT of cluster size (flagged_a, flagged_b)
-- they cancel out completely. FLEX[] intentionally includes them anyway,
specifically so a Tier 2 probe run empirically demonstrates that flexing
them by +-50% never changes evaluate()'s output at all, which is itself a
disclosed, load-bearing finding of this case (see case.json's MA4/MA5
sensitivity fields and RESEARCH_LOG.md's Margin section). fpr_a (MA6) and
fpr_b (MA7) are the only dials that actually move the verdict; fpr_b is the
single highest-sensitivity assumption in the whole case (the "surge
premium" -- see FACILITATOR.md's Twist).
"""

PARAMS = {
    # --- Appendix A / E, MA4-MA5: accounts flagged this incident -----------
    # (Provably do NOT affect the ratio -- included in FLEX to demonstrate
    # that empirically, not just algebraically.)
    "flagged_a": 250.0,   # Ring Alpha
    "flagged_b": 200.0,   # Wave Nine
    # --- Appendix E, MA6-MA7: modeled false-positive rates ------------------
    "fpr_a": 0.20,        # Ring Alpha (connectivity-based), MA6
    "fpr_b": 0.225,       # Wave Nine (volume-based, surge-adjusted), MA7
}

# Probe 5 flexes THESE and only these: the case's own stated Modeling
# Assumptions that feed the graded primary metric's arithmetic.
FLEX = [
    "flagged_a",   # MA4 -- Appendix A/E (provably irrelevant to the ratio)
    "flagged_b",   # MA5 -- Appendix A/E (provably irrelevant to the ratio)
    "fpr_a",       # MA6 -- Appendix E, Ring Alpha's modeled FP rate
    "fpr_b",       # MA7 -- Appendix E, Wave Nine's modeled FP rate -- the
                   #        case's real fulcrum (surge premium)
]


def _option_detail(flagged, fpr):
    false_positives = flagged * fpr
    confirmed_bots = flagged * (1.0 - fpr)
    ratio = confirmed_bots / false_positives
    return {
        "flagged": flagged,
        "fpr": fpr,
        "false_positives": false_positives,
        "confirmed_bots": confirmed_bots,
        "ratio_confirmed_per_fp": ratio,
    }


def evaluate_detail(params):
    p = dict(PARAMS)
    p.update(params or {})
    a = _option_detail(p["flagged_a"], p["fpr_a"])
    b = _option_detail(p["flagged_b"], p["fpr_b"])
    # Higher ratio is better -- matches evaluate()'s "higher is better"
    # contract directly.
    return {"A": a["ratio_confirmed_per_fp"], "B": b["ratio_confirmed_per_fp"]}, a, b


def evaluate(params):
    """Tier 2 probe 5 contract: evaluate(params) -> {'A': metric, 'B': metric}
    ONLY -- no extra return values. Full diagnostics (per-option breakdown)
    are in evaluate_detail()."""
    r, _a, _b = evaluate_detail(params)
    return r


if __name__ == '__main__':
    base, a, b = evaluate_detail({})
    win = max(base, key=base.get)
    lo = min(base, key=base.get)
    margin = 100.0 * (base[win] - base[lo]) / base[win]
    print("Ring Alpha (A):")
    for k, v in a.items():
        print(f"  {k}: {v}")
    print("Wave Nine (B):")
    for k, v in b.items():
        print(f"  {k}: {v}")
    print()
    print("ratio  A=%.4f  B=%.4f" % (base["A"], base["B"]))
    print("winner:", win, " margin: %.2f%%" % margin)

    # Demonstrate cluster-size irrelevance empirically: flex flagged_a/b by
    # +-50% and confirm the ratio (and therefore the winner/margin) never
    # moves.
    print()
    print("Cluster-size irrelevance check (flagged_a, flagged_b flexed +-50%):")
    for mult in (0.5, 0.75, 1.0, 1.25, 1.5):
        r, _, _ = evaluate_detail({"flagged_a": 250.0 * mult, "flagged_b": 200.0 * mult})
        print(f"  x{mult}: ratio_A={r['A']:.4f}  ratio_B={r['B']:.4f}  (unchanged, as expected)")

    # The real fulcrum: sweep fpr_b (MA7) down toward the unscaled real
    # academic baseline (0.15, S1) and find where the winner flips.
    print()
    print("fpr_b (MA7) sweep -- where does the winner flip?")
    lo_fpr, hi_fpr = 0.15, 0.30
    step = 0.005
    prev_win = None
    n = round((hi_fpr - lo_fpr) / step)
    for i in range(n + 1):
        fb = round(lo_fpr + i * step, 4)
        r, _, _ = evaluate_detail({"fpr_b": fb})
        cur_win = "A" if r["A"] > r["B"] else "B"
        if prev_win is not None and cur_win != prev_win:
            print(f"  WINNER FLIPS between fpr_b={fb - step:.3f} and fpr_b={fb:.3f}")
        prev_win = cur_win
    print(f"  at fpr_b=0.15 (real unscaled S1 baseline, no surge premium): "
          f"ratio_B={evaluate_detail({'fpr_b': 0.15})[0]['B']:.4f} "
          f"(beats ratio_A={base['A']:.4f})")
    print(f"  at fpr_b=0.225 (case's stated MA7, surge-adjusted): "
          f"ratio_B={base['B']:.4f} (loses to ratio_A={base['A']:.4f})")
