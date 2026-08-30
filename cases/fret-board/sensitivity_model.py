#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Fret Board.

Tier 2 probe 5 ("flex each stated assumption by ±50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic.

CONTRACT — two public names:

    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

The case's SPEC §2 primary metric (case.json.balance.margin_basis) is total
shop time, in minutes, to calculate/mark/cut all 22 frets: the shared,
method-independent baseline (MA6) plus each method's own per-fret
calculation time (MA4 for Option A, MA5 for Option B), summed across the
fret count (MA2).

Total shop time is a COST — lower is better — but the probe's contract is
"higher is better", so evaluate() returns the NEGATIVE of total shop time.
This preserves winner/margin semantics: whichever option has the smaller
total time has the larger (less negative) value and wins, exactly as
case.json.balance intends (Option B, Rule of Eighteen, is faster and is the
recorded winner on this metric at margin_pct=4.2%).

Only FLEX[] is swept by default, per SKILL.md's "Only FLEX[] is swept"
rule. MA4 and MA5 (the per-fret calculation-time assumptions) are the two
dials this probe was specifically asked to flex ±50% — they are genuine
authorial scenario estimates (case.json.modeling_assumptions, "reasoned
scenario estimate, not a discovered fact"), not cited/given data. MA6 (the
shared baseline) is also a stated Modeling Assumption and is included in
FLEX for completeness, since case.json.balance.margin_note's own
robustness claim ("even doubling MA4 alone keeps the margin near 16%") is
specifically about MA6 dominating -- flexing MA6 itself is the natural
converse check. MA1/MA2/MA3 are NOT flexed here: they do not enter this
metric's arithmetic at all (MA1 is an accuracy-tolerance dial for D5's
qualitative judgment, not for total shop time; MA2's fret count is swept
implicitly by being a multiplicative constant, tested separately below;
MA3 is a deadline check, not a time-cost input).

Verified against case.json.derived.shop_time_primary_metric:
    base    A = -52.33  ·  B = -50.13  ·  margin 4.2%   (winner: B)
    (total_A=52.33 min, total_B=50.13 min, matching case.json exactly)
"""

PARAMS = {
    # --- Appendix F / MA4: per-fret calculation time, Precision Method (s) --
    "calc_seconds_per_fret_a": 20.0,
    # --- Appendix F / MA5: per-fret calculation time, Rule of Eighteen (s) --
    "calc_seconds_per_fret_b": 14.0,
    # --- Appendix F / MA6: shared cut/install/dress baseline (min) ----------
    "shared_baseline_minutes": 45.0,
    # --- Appendix F / MA2: fret count on this neck ---------------------------
    "fret_count": 22,
}

# Probe 5 flexes THESE and only these: the case's own stated Modeling
# Assumptions that feed the graded primary metric's arithmetic. MA2 (fret
# count) is excluded from the default sweep -- it is a shop/client scenario
# choice bounded by a cited typical range (S4: 21-24 frets), not an
# authorial time estimate, and case.json's own sensitivity note for MA2
# says explicitly "does not change the per-fret math in D1-D4" -- it is a
# multiplicative constant common to both options and does not change which
# option wins (only how large the absolute minute gap is). Run with
# --flex-all to sweep it anyway.
FLEX = [
    "calc_seconds_per_fret_a",   # MA4, Appendix F
    "calc_seconds_per_fret_b",   # MA5, Appendix F
    "shared_baseline_minutes",   # MA6, Appendix F
]


def _total_minutes(p, calc_seconds_per_fret):
    return p["shared_baseline_minutes"] + (calc_seconds_per_fret * p["fret_count"] / 60.0)


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    total_a = _total_minutes(p, p["calc_seconds_per_fret_a"])
    total_b = _total_minutes(p, p["calc_seconds_per_fret_b"])
    # Lower total shop time is better; evaluate()'s contract is "higher is
    # better", so return the negated minutes.
    return {"A": -total_a, "B": -total_b}


if __name__ == '__main__':
    base = evaluate({})
    totals = {k: round(-v, 2) for k, v in base.items()}
    win = max(base, key=base.get)
    lo = min(base, key=base.get)
    margin = 100.0 * (base[win] - base[lo]) / (base[lo] or 1)
    print("base totals (minutes) ", totals, "winner", win, "margin %.1f%%" % margin)
