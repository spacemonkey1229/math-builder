#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- Biostatician.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips
the verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the reference
shape this file follows.

CONTRACT:
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            subset of PARAMS Tier 2 flexes
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher = stronger case for that option

`evaluate()` models the case's actual GRADED primary_metric (case.json
`primary_metric` / `balance.margin_pct` = 13.1pp): the two percentages
Ingrid is really weighing side by side --
  A = the measured time-spent gap (%) between the average-weight group and
      the pooled overweight+obese group (Appendix B, the case's own real,
      cited dataset -- see sources[] S1/S2)
  B = the training program's total cost, as a percent of a typical year's
      profit (Appendix C's given six-year profit history and $265/physician
      training cost -- this case's own fictional-but-fixed scenario data)
A wins (recommend the training) when the measured gap is the bigger
percentage; B wins (don't recommend) when the cost-as-percent-of-profit is
the bigger percentage.

Base case (matches case.json.derived and case.json.balance.margin_pct):
    A = 26.58%   (mean_avg_time=31.36min, mean_heavier_time=23.03min)
    B = 13.45%   (cost=$490,780 / avg_profit=$3,650,000)
    margin = A - B = 13.14 percentage points -- under the SPEC.md Section 2
    20% cap in the case's own percentage-point framing, and (per the flex
    sweep below) winner-stable across every tested +/-50% flex of either
    FLEX dial: the training's cost never catches up to the size of the
    measured gap within the tested range. NOTE: tier2_probes.py's mechanical
    cap check uses a *relative*-margin formula ((larger-smaller)/smaller x
    100) rather than this pp framing, and because B is itself a small
    percentage that formula flags a nominal cap breach at every tested flex
    of both dials (even at this unflexed base). This is disclosed, not
    eliminated, as a Category F (irreducible forecast uncertainty) finding
    on both dials in case.json.sensitivity_disclosure[] -- see
    case.json.balance.stability and FACILITATOR.md's Sensitivity Note.
"""

# --- Appendix B: real, cited dataset (Hebl & Xu 2001; sources[] S1/S2) ------
#     NOT flexed -- this is cited/given data, not a stated scenario
#     assumption. Per skills/case-readiness/SKILL.md's P5 doctrine, cited
#     measurements are stress-tested by probe 6 (data decay), not probe 5.
MEAN_AVG_TIME_MIN = 31.363636363636363          # Appendix B, Average group, n=33
MEAN_HEAVIER_TIME_MIN = 23.026315789473685      # Appendix B, Overweight+Obese pooled, n=76

# --- Appendix C: given (fictional-but-fixed) six-year profit history, most
#     recent year last. NOT flexed for the same reason as above -- it is
#     Benedictus Hospital Group's own stated scenario data, not an
#     assumption Ingrid has to choose. -----------------------------------
PROFIT_HISTORY_USD = [1_500_000, 1_700_000, 2_600_000, 4_500_000, 7_600_000, 4_000_000]

# --- Appendix C: given training cost per physician. NOT flexed -- stated
#     directly in the legacy case text as a fixed quote from the training
#     firm. --------------------------------------------------------------
COST_PER_PHYSICIAN_USD = 265

PARAMS = {
    # --- Appendix D, MA1: which physicians the training program would
    #     cover if recommended. The case text ("provide training to its
    #     physicians") does not resolve this -- a genuine stated modeling
    #     assumption, not a given figure. Base case reads it as the full
    #     physician staff.
    "trained_physician_count": 1852,
    # --- Appendix D, MA2: how many of the six given profit years to
    #     average when judging a "typical" year against the training's
    #     cost. Base case uses all six; a narrower window weighting only
    #     the most recent years is an equally defensible reading. Capped
    #     to [1, 6] in profit_avg() below since only 6 years are given.
    "profit_window_years": 6,
}

# Probe 5 flexes THESE and only these -- both are genuine stated modeling
# assumptions (Appendix D, MA1/MA2), not cited measurements. The Appendix B
# time data and the Appendix C profit/cost figures are this case's own
# real/given data and are deliberately excluded from FLEX -- see the module
# docstring and skills/case-readiness/SKILL.md's P5 FLEX-scoping rule.
FLEX = [
    "trained_physician_count",
    "profit_window_years",
]


def profit_avg(window_years):
    """Average of the most recent `window_years` of PROFIT_HISTORY_USD,
    clamped to [1, len(PROFIT_HISTORY_USD)] since the case only gives 6
    years of history -- a flex beyond that range still reads the full
    six-year history, not a fabricated extra year."""
    n = max(1, min(len(PROFIT_HISTORY_USD), round(window_years)))
    recent = PROFIT_HISTORY_USD[-n:]
    return sum(recent) / len(recent)


def evaluate(params=None):
    """The case's actual graded primary_metric: the measured time-spent gap
    (%) vs. the training cost as a percent of a typical year's profit --
    case.json `primary_metric` / `balance.margin_pct` = 13.1pp."""
    p = dict(PARAMS)
    p.update(params or {})

    gap_pct = 100 * (MEAN_AVG_TIME_MIN - MEAN_HEAVIER_TIME_MIN) / MEAN_AVG_TIME_MIN

    total_cost = COST_PER_PHYSICIAN_USD * p["trained_physician_count"]
    avg_profit = profit_avg(p["profit_window_years"])
    cost_pct = 100 * total_cost / avg_profit

    return {"A": gap_pct, "B": cost_pct}


# No evaluate_twist() -- this case's Twist (the 13 missing physician
# responses out of 122, and their uneven distribution across weight groups;
# see FACILITATOR.md) is a data-completeness/inference question, not a
# recomputation of the A/B metric above. It changes how much a Hero should
# TRUST the measured gap, not the arithmetic of the gap itself, so it is
# not represented as a second evaluate_twist() metric function.


if __name__ == '__main__':
    base = evaluate({})
    print("base (graded primary_metric)", {k: round(v, 2) for k, v in base.items()},
          "  margin = %.2f percentage points (A - B)" % (base["A"] - base["B"]))

    print("\nFLEX sweep (+/-50%):")
    for key in FLEX:
        base_val = PARAMS[key]
        for mult, tag in [(0.5, "-50%"), (1.5, "+50%")]:
            flexed = evaluate({key: base_val * mult})
            margin = flexed["A"] - flexed["B"]
            winner = "A" if flexed["A"] > flexed["B"] else ("B" if flexed["B"] > flexed["A"] else "TIE")
            base_winner = "A" if base["A"] > base["B"] else ("B" if base["B"] > base["A"] else "TIE")
            flips = winner != base_winner
            cap_break = abs(margin) > 20
            print(f"  {key} {tag} ({base_val} -> {base_val*mult:.1f}): "
                  f"A={flexed['A']:.2f} B={flexed['B']:.2f} margin={margin:.2f} "
                  f"winner={winner} {'FLIP' if flips else 'stable'} "
                  f"{'CAP-BREACH' if cap_break else ''}")
