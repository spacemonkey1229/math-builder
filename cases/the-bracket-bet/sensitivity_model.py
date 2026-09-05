#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Bracket Bet.

Tier 2 probe 5 ("flex each stated assumption by ±50%; report which flips the
verdict") needs a runnable model of the case's own D1-D3 arithmetic: grow a
level annual contribution as an ordinary annuity (D1/D2), then tax the
Traditional (Pay Later) withdrawal at the assumed FUTURE rate and the Roth
(Pay Now) contribution at TODAY's known rate (D3).

CONTRACT — exactly two required public names:

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

evaluate() returns after-tax retirement VALUE for each option directly (a
dollar amount where higher is genuinely better for Devon) -- no negation
needed, unlike the cost-minimizing models in cases/the-deferred-repair and
cases/the-breakeven-mile.

    FV                = C * ((1+r)^n - 1) / r                      (D1/D2, ordinary annuity)
    A (Pay Later)     = FV * (1 - future_tax_rate_MA2)              (D3)
    B (Pay Now/Roth)  = FV * (1 - current_tax_rate_MA1)             (D3)

Appendix A's contribution [S1], Appendix B's return rate [S5] and horizon
(years, derived from S4's sourced retirement age 67 minus Devon's stated
current age 24) are cited/given data -- NOT flexed by default (P6, data
decay, covers these instead; see "Only FLEX[] is swept" in
skills/case-readiness/SKILL.md's P5 section).

MA1 (Devon's current bracket, 12%) is carried in PARAMS for the arithmetic
but excluded from FLEX: case.json.modeling_assumptions[MA1].sensitivity says
plainly "Fixed; not a free variable in the case" -- it is a computed fact
about Devon's stated income against the real 2026 IRS table, not an assumed
scenario dial.

MA2 (assumed future bracket, Scenario 1, 22%) IS the genuine Modeling
Assumption this case asks a reader to choose, and it is the scenario
case.json.balance.margin_pct (12.8%) records as "the figure of record" (see
FACILITATOR.md's Balance argument). FLEX sweeps exactly this one dial.

MA3 (Scenario 2, 10%) is the case's own REQUIRED second scenario -- not a
sensitivity finding to surface, but a value case.md already forces every
reader to compute (D3 explicitly requires both scenarios). It is provided
here as evaluate_scenario2(), for cross-checking against case.json.balance's
disclosed 2.3% Traditional-wins figure, but is deliberately NOT in FLEX: it
is not an unstated fragility, it is the case's own stated required contrast,
already fully disclosed in case.md, case.json.balance, and FACILITATOR.md.

Expected P5 finding (not a defect -- see case.json.sensitivity_note and
FACILITATOR.md's Sensitivity note, "this is not a defect to manage down, it
is the case's entire reason to exist"): flexing MA2 by -50% (22% -> 11%)
drops the assumed future rate BELOW today's fixed 12%, which flips the
winner to A (Pay Later) -- exactly the Scenario-2-shaped outcome the case
already requires every reader to compute honestly. Flexing MA2 by +50%
(22% -> 33%) does not flip the winner but widens Roth's margin past SPEC
§2's 20% cap. Both are real, and both are already disclosed in case.md's own
structure (D5 explicitly asks readers to name the one number the
recommendation depends on most and what value flips it) -- so this is a
Category F (forecast / irreducible-unknown) disclosure, not an authoring
defect: nobody, including the case's own author, can know Devon's real
future tax bracket in advance by any amount of research.

Verified against case.json.balance / FACILITATOR.md (2026-09-04):
    base (MA2=22%)   A=$1,386,217.62  B=$1,563,937.83  Roth wins, margin 12.8%
    scenario 2 (MA3=10%)  A=$1,599,481.87  B=$1,563,937.83  Traditional wins, margin 2.3%
"""

PARAMS = {
    # --- Appendix A [S1], sourced annual contribution ------------------------
    "annual_contribution_usd": 3000.0,
    # --- Appendix B [S5], sourced long-run average annual return ------------
    "annual_return_rate": 0.10,
    # --- Appendix B, years of growth (67 [S4] - 24, Devon's stated age) -----
    "years": 43,
    # --- Appendix D / Modeling Assumption MA1: Devon's current bracket ------
    #     computed from the real 2026 IRS table against Devon's stated income,
    #     not a free scenario dial -- case.json.modeling_assumptions[MA1]
    #     .sensitivity: "Fixed; not a free variable in the case."
    "current_tax_rate_MA1": 0.12,
    # --- Appendix D / Modeling Assumption MA2: assumed future bracket -------
    #     Scenario 1 (rates rise) -- the case.json balance.margin_pct
    #     "figure of record" (12.8%, Roth wins). THE genuine assumption dial.
    "future_tax_rate_MA2": 0.22,
}

# Probe 5 flexes THIS and only this by default: the one genuinely free
# Modeling Assumption (MA2). MA1 is fixed by the case's own sensitivity
# column (above); the contribution amount, return rate, and horizon are
# cited/given data, stress-tested by P6 (data decay) instead of P5. MA3
# (Scenario 2) is the case's own already-disclosed required second scenario,
# not an unstated fragility -- see evaluate_scenario2() and the module
# docstring. Run with --flex-all to sweep everything anyway.
FLEX = [
    "future_tax_rate_MA2",
]


def _future_value(contribution, rate, years):
    """D1/D2: ordinary-annuity future value of a level annual contribution."""
    return contribution * (((1.0 + rate) ** years - 1.0) / rate)


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    fv = _future_value(p["annual_contribution_usd"], p["annual_return_rate"], p["years"])
    a_pay_later = fv * (1.0 - p["future_tax_rate_MA2"])     # D3: taxed at the future rate
    b_pay_now = fv * (1.0 - p["current_tax_rate_MA1"])      # D3: taxed at today's known rate
    return {"A": a_pay_later, "B": b_pay_now}


def evaluate_scenario2(params=None):
    """The case's own REQUIRED second scenario (MA3, Scenario 2, 10%). Not
    part of the probe 5 contract and not in FLEX -- provided so both of
    case.md's required D3 scenarios are checkable against case.json.balance,
    not just the Scenario-1 figure of record that FLEX sweeps."""
    p = dict(PARAMS)
    p.update(params or {})
    p["future_tax_rate_MA2"] = 0.10   # MA3's value
    return evaluate(p)


if __name__ == '__main__':
    base = evaluate({})
    a, b = base["A"], base["B"]
    winner = "B (Pay Now/Roth)" if b > a else "A (Pay Later/Traditional)"
    lo, hi = min(a, b), max(a, b)
    margin = 100.0 * (hi - lo) / lo
    print("base (MA2=22%%)  A=$%.2f  B=$%.2f  winner=%s  margin=%.2f%%" % (a, b, winner, margin))

    s2 = evaluate_scenario2()
    a2, b2 = s2["A"], s2["B"]
    winner2 = "A (Pay Later/Traditional)" if a2 > b2 else "B (Pay Now/Roth)"
    lo2, hi2 = min(a2, b2), max(a2, b2)
    margin2 = 100.0 * (hi2 - lo2) / lo2
    print("scenario 2 (MA3=10%%)  A=$%.2f  B=$%.2f  winner=%s  margin=%.2f%%"
          % (a2, b2, winner2, margin2))

    print("\n±50%% flex of MA2 (future_tax_rate_MA2):")
    for mult, label in ((0.5, "-50%"), (1.5, "+50%")):
        fr = PARAMS["future_tax_rate_MA2"] * mult
        r = evaluate({"future_tax_rate_MA2": fr})
        ra, rb = r["A"], r["B"]
        w = "B (Roth)" if rb > ra else "A (Traditional)"
        lo3, hi3 = min(ra, rb), max(ra, rb)
        m3 = 100.0 * (hi3 - lo3) / lo3
        flip = " *** FLIPS ***" if w.startswith("A") else ""
        print("  MA2 %s (rate=%.3f)  A=$%.2f  B=$%.2f  winner=%s  margin=%.2f%%%s"
              % (label, fr, ra, rb, w, m3, flip))
