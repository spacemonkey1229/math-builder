#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Lease Break.

Tier 2 probe 5 ("flex each stated assumption by +-50%; report which flips the
verdict") needs a runnable model of the case's own D2/D3 arithmetic.

CONTRACT — exactly two public names:

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}

`evaluate` returns each option's D3 (break-at-month-6) effective monthly cost,
since that is the closer, more contested of the two scenarios (D2's
stay-full-term comparison is a 16.9% landslide even before flexing anything,
per case.json.balance.margin_pct_by_scenario). Per the harness contract,
HIGHER should be better -- but this case's primary_metric is a COST (lower is
better), so this file returns 1/cost (a "value" proxy, higher = cheaper) rather
than raw cost, to match tier2_probes.py's max()-picks-the-winner convention.
Divide 1 by either returned value to recover the actual dollar figure.

RETUNED 2026-09-04 (case-readiness remediation): the 2026-09-03 pass found
OPTION A (Cedarline) winning BOTH D2 and D3 at every stated PARAMS value, so
the case's designed scenario-dependent reversal did not exist. Root cause and
fix are in case.json.sensitivity_note: cedarline_termination_penalty (MA2) was
revised from 2 to 3.5 months' rent, grounded in two new real sources (S7, S8)
documenting a real 2-4 / 3-4 month range specifically for a lease with several
months still remaining -- exactly Maya's break-at-month-6 situation. D3 now
genuinely favors OPTION B (Aldergate).

REFRESHED again the same day after a Tier 2 P6 data-decay check found S1/S2's
live rent-trends source had moved on from its originally-cited $1,389/$1,536
figures to $1,447/$1,601 -- every PARAMS value below tied to those rents (the
move-in fee, the penalty, the deposit, the buyout) was recomputed at the same
percent/multiple of the refreshed rent, per case.json.sensitivity_note.

Verified against cases/the-lease-break/case.md and case.json:
    D2 (not modeled here -- see docstring)  A=1483.17  B=1734.42  (A cheaper by 16.9%)
    D3 (modeled below)                      A=2363.50  B=2134.67  (B cheaper by 10.7%)

Disclosed instability (see MA2's `sensitivity` field and FACILITATOR.md): a
-50% flex of cedarline_termination_penalty alone (back inside the ordinary 1-2
month range) flips D3 back to OPTION A. This is the single dial the case
explicitly names as the most dilemma-relevant assumption; every other FLEX[]
dial, and every other direction of this one, leaves D3's winner unmoved. This
is a disclosed, not hidden, sensitivity per SPEC §2/MCS-26.
"""

FLEX = [
    "cedarline_movein_fee",             # MA1
    "cedarline_termination_penalty",    # MA2
    "aldergate_deposit",                # MA3
    "aldergate_buyout",                 # MA4
    "break_month",                      # MA6
]
# cedarline_rent (S1) and aldergate_rent (S2) are cited real market data, not
# stated modeling assumptions -- flexing them is a data-decay question (P6),
# not an assumption-sensitivity one (P5), so they are deliberately excluded
# from FLEX[] (still sweepable with --flex-all).

PARAMS = {
    # --- Appendix A ----------------------------------------------------------
    "cedarline_rent": 1447.0,
    "cedarline_movein_fee": 434.0,          # MA1
    "cedarline_termination_penalty": 5065.0,  # MA2 -- most dilemma-relevant dial
    # --- Appendix B ------------------------------------------------------------
    "aldergate_rent": 1601.0,
    "aldergate_deposit": 1601.0,             # MA3
    "aldergate_buyout": 1601.0,              # MA4
    # --- Appendix C ------------------------------------------------------------
    "break_month": 6.0,                      # MA6 -- D3's amortization window
}


def evaluate(params):
    """Return {"A": value, "B": value} for the D3 break-at-month-N scenario,
    where value = 1 / effective_monthly_cost (higher value = cheaper = better),
    per the harness's max()-wins convention."""
    p = {**PARAMS, **params}
    n = max(p["break_month"], 1e-9)  # guard against a flexed-to-zero month

    cost_a = p["cedarline_rent"] + (p["cedarline_movein_fee"] + p["cedarline_termination_penalty"]) / n
    cost_b = p["aldergate_rent"] + (p["aldergate_deposit"] + p["aldergate_buyout"]) / n

    return {"A": 1.0 / cost_a, "B": 1.0 / cost_b}


if __name__ == "__main__":
    base = evaluate(PARAMS)
    cost_a, cost_b = 1 / base["A"], 1 / base["B"]
    print(f"base D3 effective monthly cost: A(Cedarline)=${cost_a:.2f}  B(Aldergate)=${cost_b:.2f}")
    winner = "A" if cost_a < cost_b else "B"
    # margin convention matches case.json.balance: percent difference relative
    # to the CHEAPER (winning) option's cost, e.g. "B is 10.8% cheaper than A".
    margin = abs(cost_a - cost_b) / min(cost_a, cost_b) * 100
    print(f"winner (lower cost): {winner}   margin: {margin:.1f}%")
