#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- Investment Portfolio.

CONTRACT -- exactly two required public names, plus an optional third:

    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     optional; same shape, with the twist applied

Every entry in PARAMS must correspond to something the case STATES -- a
modelling assumption, a rated figure, a convention. Do not put an authorial
fudge factor in here.

WHAT IS AND ISN'T A DIAL IN THIS CASE, AND WHY.

case.json.primary_metric is the 20-year Sharpe ratio (annualized risk-adjusted
return) for each portfolio -- chosen as the primary metric specifically
because it is the one real, cited comparison point where the two named
options land essentially dead even (see Appendix C's 20-year return/stdev
rows), unlike raw 30-year terminal portfolio value, which is not close at all
(Buffett 90/10 wins that by roughly 55%, per case.json.derived).

Appendix C's 20-year annualized RETURN and STANDARD DEVIATION figures for
both portfolios are GIVEN/CITED data (S2, a real dated backtest) -- not a
dial. Per the FLEX-scoping doctrine in skills/case-readiness/SKILL.md P5,
cited data is stress-tested by P6 (data decay), not swept by P5.

Appendix D's Modeling Assumptions state THREE genuine author-chosen
conventions:

  MA1 -- risk-free rate assumption (1.5%), used only to compute the Sharpe
  ratio in D6. This is the case's one true continuous, freely-choosable
  dial for the PRIMARY metric -- no one can cite "the" risk-free rate a
  30-year-old investor should assume for a 20-year-forward Sharpe estimate.
  This IS FLEX.

  MA2 -- forward-looking expected return assumption for the D4/D5 30-year
  PROJECTION (each portfolio's own trailing 30-year historical return, used
  going forward). This is a real, stated, load-bearing assumption -- but it
  drives the D4/D5 PROJECTION metric (30-year terminal portfolio value),
  which is NOT this case's primary_metric. Modeled below as
  project_30yr()/evaluate_projection() for transparency and because D4/D5
  are real graded deliverables, but it is a SEPARATE function from
  evaluate(), not swept into the primary P5 sensitivity report by default.

  MA3 -- contribution schedule (40% of $100k income, growing at 2.6%/yr
  inflation). This is Benjamin's own stated plan restated as a fixed input,
  not an authorial modeling choice -- not a dial (same status as Appendix B's
  raw applicant scores in the Psychologist case: given data, not FLEX).

base() -- primary_metric: 20-year Sharpe ratio for the two NAMED, FIXED
          options in the Dilemma -- Warren Buffett's 90/10 Portfolio (A) and
          Ray Dalio's All-Weather Portfolio (B).

twist() -- see FACILITATOR.md: the real, sourced 2014 disclosure that
           Buffett's own 90/10 instruction was written for his wife's
           inheritance (a lump sum, no further contributions, no 30-year
           earning horizon) -- not a recommendation for an actively-earning,
           actively-contributing 30-year-old. The twist does not change any
           number in this model; it changes which assumption (MA2/MA3) a
           Hero should trust applying to Benjamin's very different situation.
           There is no separate evaluate_twist() because the twist is an
           interpretive challenge to MA2/MA3's applicability, not a new
           numeric input -- see FACILITATOR.md for how to run it live.

Verified against case.json.balance:
    base Sharpe(20yr):  A(Buffett) = 0.6611   B(All-Weather) = 0.6600
    margin ~0.17% (Buffett fractionally ahead) -- a real, sourced near-tie.
"""

# --- Appendix C: cited backtest data (S2), NOT a dial. ----------------------
RETURN_20YR = {"A": 10.63, "B": 6.74}     # percent, annualized, 20-year window
STDEV_20YR = {"A": 13.81, "B": 7.94}      # percent, annualized, 20-year window

# --- Appendix C: cited backtest data (S2), NOT a dial -- used only by the
#     D4/D5 projection model, not by the primary-metric evaluate(). ---------
RETURN_30YR = {"A": 9.98, "B": 7.40}      # percent, used as MA2's forward-return assumption

# --- Appendix D, MA3: Benjamin's own stated plan, NOT a dial. ---------------
INCOME = 100_000.0
CONTRIB_RATE = 0.40
INFLATION = 0.026          # 2.6%/yr, S4

PARAMS = {
    # --- Appendix D, MA1: the case's one genuine continuous assumption
    #     dial for the PRIMARY metric (Sharpe ratio).
    "risk_free_rate": 1.5,   # percent
}

# Only MA1's risk-free-rate assumption is swept for the primary-metric P5
# probe. MA2 (forward-return assumption) and MA3 (contribution schedule) are
# real stated assumptions too, but they drive the D4/D5 PROJECTION metric,
# which is not case.json.primary_metric -- see project_30yr()/FLEX_PROJECTION
# below for how those are separately, explicitly sensitivity-tested.
FLEX = [
    "risk_free_rate",
]

# A second, clearly-separated FLEX list for the projection metric (D4/D5),
# reported separately -- not the default P5 sweep, which targets
# primary_metric only.
FLEX_PROJECTION = [
    "forward_return_A", "forward_return_B", "inflation",
]


def evaluate(params):
    """Primary metric per case.json: 20-year Sharpe ratio = (return - risk
    free rate) / standard deviation, for each named option. Higher wins."""
    p = dict(PARAMS)
    p.update(params or {})
    rf = p["risk_free_rate"]
    a = (RETURN_20YR["A"] - rf) / STDEV_20YR["A"]
    b = (RETURN_20YR["B"] - rf) / STDEV_20YR["B"]
    return {"A": round(a, 4), "B": round(b, 4)}


def project_30yr(forward_return_pct, inflation=INFLATION, shock_year=None,
                  shock_return=-0.35, years=30):
    """D4/D5 projection metric: 30-year terminal portfolio value in dollars,
    given a constant assumed forward annual return (MA2) and Benjamin's
    stated contribution schedule (MA3). shock_year/shock_return model D5's
    -35%-in-Year-3 scenario."""
    r = forward_return_pct / 100.0
    value = 0.0
    for n in range(1, years + 1):
        contrib = CONTRIB_RATE * INCOME * (1 + inflation) ** (n - 1)
        this_r = shock_return if (shock_year == n) else r
        value = value * (1 + this_r) + contrib
    return value


def evaluate_projection(params=None):
    """The D4/D5 projection metric (NOT case.json.primary_metric): 30-year
    terminal portfolio value, using each portfolio's own 30-year historical
    return (MA2) as the assumed forward rate. Reported separately from
    evaluate() -- kept here, not folded into it, because case.json's
    primary_metric is the Sharpe-ratio tie, and this projection is
    deliberately NOT close (see docstring above)."""
    p = {
        "forward_return_A": RETURN_30YR["A"],
        "forward_return_B": RETURN_30YR["B"],
        "inflation": INFLATION,
    }
    p.update(params or {})
    a = project_30yr(p["forward_return_A"], inflation=p["inflation"])
    b = project_30yr(p["forward_return_B"], inflation=p["inflation"])
    return {"A": round(a, 2), "B": round(b, 2)}


def evaluate_projection_shock(params=None):
    """D5: same as evaluate_projection(), with a -35% return forced into
    Year 3 for both portfolios."""
    p = {
        "forward_return_A": RETURN_30YR["A"],
        "forward_return_B": RETURN_30YR["B"],
        "inflation": INFLATION,
    }
    p.update(params or {})
    a = project_30yr(p["forward_return_A"], inflation=p["inflation"], shock_year=3)
    b = project_30yr(p["forward_return_B"], inflation=p["inflation"], shock_year=3)
    return {"A": round(a, 2), "B": round(b, 2)}


if __name__ == '__main__':
    base = evaluate({})
    print("primary metric -- 20yr Sharpe ratio:", base)
    margin = 100.0 * (base["A"] - base["B"]) / base["B"]
    print("margin %.3f%% (Buffett 90/10 fractionally ahead)" % margin)

    for rf in (0.75, 1.5, 2.25):  # +/-50% flex on MA1
        r = evaluate({"risk_free_rate": rf})
        state = "A" if r["A"] > r["B"] else ("B" if r["B"] > r["A"] else "TIE")
        print(f"  risk_free_rate={rf:5.2f}  A={r['A']:.4f}  B={r['B']:.4f}  winner={state}")

    proj = evaluate_projection()
    shock = evaluate_projection_shock()
    print("\n30-year projection (D4, MA2 forward-return assumption):", proj,
          " margin %.2f%% (Buffett 90/10 favored)" %
          (100.0 * (proj["A"] - proj["B"]) / proj["B"]))
    print("30-year projection with Year-3 -35% shock (D5):", shock,
          " margin %.2f%% (Buffett 90/10 favored)" %
          (100.0 * (shock["A"] - shock["B"]) / shock["B"]))
    print("  shock impact vs base -- A: %.2f  B: %.2f" %
          (shock["A"] - proj["A"], shock["B"] - proj["B"]))

    for mult in (0.5, 1.0, 1.5):  # +/-50% flex on MA2's forward-return assumption
        r = evaluate_projection({"forward_return_A": RETURN_30YR["A"] * mult,
                                  "forward_return_B": RETURN_30YR["B"] * mult})
        print(f"  forward_return_mult={mult:.1f}  A=${r['A']:,.0f}  B=${r['B']:,.0f}")
