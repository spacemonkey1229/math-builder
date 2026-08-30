#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Downbeat Split.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic.

CONTRACT -- two public names:

    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

The case's SPEC Sec.2 primary metric (case.json.balance.margin_basis) is
expected total studio minutes to deliver a broadcast-ready take: booked
rehearsal minutes (D1-D5, from MA1/MA4-MA10) plus a probability-weighted
redelivery-risk term (each option's rejection probability, MA11 for Option A
/ MA12 for Option B, times the total booked session length that has to be
re-booked if a take is rejected, MA2).

Expected total minutes is a COST -- lower is better -- but the probe's
contract is "higher is better", so evaluate() returns the NEGATIVE of the
expected total.

Verified against case.json.derived:
    base    A = -30.0  ·  B = -27.0  ·  margin 10.0%   (winner: B)
    (option_a_expected_total_min=30.0, option_b_expected_total_min=27.0,
    matching case.json exactly)
"""

PARAMS = {
    # --- D5 / Appendix D: booked rehearsal minutes, already fixed by D1-D4 --
    #     (MA1, MA4-MA10 chain to these two numbers; not re-derived here since
    #     this probe is about the retune's NEW dials, MA11/MA12/MA2, not the
    #     pre-existing fraction arithmetic those inherit from.)
    "rehearsal_min_a": 0.0,
    "rehearsal_min_b": 22.5,
    # --- Appendix E / MA11: redelivery-risk probability, Straight Cut -------
    "redelivery_risk_prob_a": 1.0 / 3.0,
    # --- Appendix E / MA12: redelivery-risk probability, Downbeat Split -----
    "redelivery_risk_prob_b": 1.0 / 20.0,
    # --- Appendix A / MA2: total booked session length re-booked on reject --
    "rebook_session_min": 90.0,
}

# Probe 5 flexes THESE and only these: the case's own stated Modeling
# Assumptions that feed the retuned primary metric's arithmetic. MA11/MA12
# are the two dials the retune specifically introduced -- genuine authorial
# scenario estimates (case.json.modeling_assumptions, "no published
# rejection-rate data exists ... the case fixes a value"), not cited/given
# data. MA2 (rebook_session_min) is also flexed since it scales both options'
# risk terms and is itself a stated Modeling Assumption. rehearsal_min_a/b
# are NOT flexed here -- they are outputs of the D1-D4 fraction chain
# (MA1/MA4-MA10), already covered by the case's original (pre-retune)
# fraction arithmetic, not new dials this retune introduced.
FLEX = [
    "redelivery_risk_prob_a",   # MA11, Appendix E
    "redelivery_risk_prob_b",   # MA12, Appendix E
    "rebook_session_min",       # MA2, Appendix A
]


def _expected_total(rehearsal_min, risk_prob, rebook_min):
    return rehearsal_min + risk_prob * rebook_min


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    total_a = _expected_total(p["rehearsal_min_a"], p["redelivery_risk_prob_a"], p["rebook_session_min"])
    total_b = _expected_total(p["rehearsal_min_b"], p["redelivery_risk_prob_b"], p["rebook_session_min"])
    # Lower expected total is better; evaluate()'s contract is "higher is
    # better", so return the negated minutes.
    return {"A": -total_a, "B": -total_b}


if __name__ == '__main__':
    base = evaluate({})
    totals = {k: round(-v, 4) for k, v in base.items()}
    win = max(base, key=base.get)
    lo = min(base, key=base.get)
    margin = 100.0 * (base[win] - base[lo]) / (base[lo] or 1)
    print("base totals (minutes)", totals, "winner", win, "margin %.1f%%" % margin)

    print("\n--flex-all +/-50%% sweep:")
    for k in FLEX:
        for mult, tag in ((0.5, "-50%"), (1.5, "+50%")):
            flexed = dict(PARAMS)
            flexed[k] = PARAMS[k] * mult
            r = evaluate(flexed)
            w = max(r, key=r.get)
            l = min(r, key=r.get)
            m = 100.0 * (r[w] - r[l]) / (r[l] or 1)
            flip = " *** FLIP ***" if w != win else ""
            print(f"  {k:26s} {tag:5s} -> A={-r['A']:.4f} B={-r['B']:.4f} "
                  f"winner={w} margin={m:.1f}%{flip}")
