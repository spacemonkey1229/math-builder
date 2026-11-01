"""
sensitivity_model.py -- The Approval Gate

Graded primary metric (case.json.primary_metric): total expected monthly operating
cost of a refund-approval gate design (escalation labor cost + expected false-approval
loss cost). LOWER cost is better for Priya. This script's evaluate() contract requires
"higher wins" (per skills/case-readiness/SKILL.md's P5 spec: evaluate(params) ->
{"A": metric, "B": metric}, higher is better) -- so evaluate() returns NEGATIVE total
cost as the score. Higher score (less negative) = lower real-dollar cost = better.

    escalate(A)          = total - n_ttf                         (Option A's truth table:
                                                                    only p=T,q=T,r=F is
                                                                    "Approve")
    escalate(B)          = n_fft                                 (Option B's truth table:
                                                                    only p=F,q=F,r=T is
                                                                    "Escalate")
    approved(B)          = total - n_fft
    incorrectly_approved(B) = approved(B) - n_ttf                (auto-approved by B but
                                                                    NOT the genuinely-safe
                                                                    p=T,q=T,r=F category)
    L                    = fraud_rate x avg_value_at_risk         (expected loss per
                                                                    incorrectly approved
                                                                    request)
    cost(A) = escalate(A) x cost_per_escalation
    cost(B) = escalate(B) x cost_per_escalation + incorrectly_approved(B) x L

fraud_rate [S2, Appriss Retail / Deloitte 2024 annual returns-fraud report] is a real,
sourced, HIGH-confidence figure -- NOT flexed by default (cited data, stress-tested by
P6 instead). Every other quantity below (the 8 request-category counts, the
per-escalation cost, and the average dollar value at risk) is a stated Modeling
Assumption -- see case.json.modeling_assumptions[MA1, MA3, MA4] and RESEARCH_LOG.md;
none of these figures exists as a citable external dataset. FLEX below sweeps exactly
these ten and nothing else.

Verified against case.json.balance / FACILITATOR.md's margin arithmetic:
    base   A = $14,400.00 (winner, lower cost)  ·  B = $15,972.95  ·  margin 9.8%
    (fixed 2026-09-09: this docstring and the __main__ block below previously stated/printed
    10.9%, from dividing by the winner's cost instead of the loser's -- see the fix note above
    real_costs()'s __main__ block. The actual P5 gate, tier2_probes.py's probe_sensitivity, was
    never affected -- it already used the correct loser-denominator convention throughout.)
"""

PARAMS = {
    # --- Appendix C, Modeling Assumption MA1 -- monthly refund-request volume by
    #     p/q/r category. Not published anywhere (no company publishes its own
    #     internal AI-agent request logs) -- see RESEARCH_LOG.md.
    "n_ttt": 40.0,
    "n_ttf": 2000.0,
    "n_tft": 30.0,
    "n_tff": 430.0,
    "n_ftt": 25.0,
    "n_ftf": 850.0,
    "n_fft": 15.0,
    "n_fff": 210.0,
    # --- Appendix D, Modeling Assumption MA3 -- cost per escalated (human-reviewed)
    #     request.
    "cost_per_escalation": 9.0,
    # --- Appendix D [S2], sourced, HIGH confidence -- retail return-fraud rate.
    #     NOT in FLEX (cited data; P6 stress-tests sources instead).
    "fraud_rate": 0.1514,
    # --- Appendix D, Modeling Assumption MA4 -- average dollar value at risk per
    #     incorrectly auto-approved, risky refund request. The case's single most
    #     sensitive dial (see modeling_assumptions[MA4].sensitivity).
    "avg_value_at_risk": 66.0,
}

# Only the genuine Modeling Assumptions are swept by default (SPEC §2 asks for
# sensitivity to STATED ASSUMPTIONS, not cited measurements). fraud_rate is a real,
# sourced Appriss Retail/Deloitte figure [S2] -- halving a published industry-wide
# fraud rate is a different case, not a sensitivity test on this case's own authored
# assumptions. Run with --flex-all to sweep fraud_rate too.
FLEX = ["n_ttt", "n_ttf", "n_tft", "n_tff", "n_ftt", "n_ftf", "n_fft", "n_fff",
        "cost_per_escalation", "avg_value_at_risk"]


def _total(p):
    return (p["n_ttt"] + p["n_ttf"] + p["n_tft"] + p["n_tff"] +
            p["n_ftt"] + p["n_ftf"] + p["n_fft"] + p["n_fff"])


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    total = _total(p)
    escalate_a = total - p["n_ttf"]
    escalate_b = p["n_fft"]
    approved_b = total - p["n_fft"]
    incorrectly_approved_b = approved_b - p["n_ttf"]
    loss_per_incident = p["fraud_rate"] * p["avg_value_at_risk"]
    cost_a = escalate_a * p["cost_per_escalation"]
    cost_b = escalate_b * p["cost_per_escalation"] + incorrectly_approved_b * loss_per_incident
    # higher-wins contract: return negative cost so lower real cost -> higher score
    return {"A": -cost_a, "B": -cost_b}


def real_costs(params=None):
    """Convenience for reporting: returns the actual positive dollar costs."""
    r = evaluate(params or {})
    return {"A": -r["A"], "B": -r["B"]}


if __name__ == '__main__':
    base = real_costs({})
    a, b = base["A"], base["B"]
    win = "A" if a < b else "B"
    lo, hi = min(a, b), max(a, b)
    # Corpus-standard convention is winner-loser as a percent of the LOSER's cost.
    # Since lower cost wins here, the winner's cost is lo and the loser's is hi --
    # so the denominator is hi, not lo (fixed 2026-09-09: this line previously
    # divided by lo, the WINNER's cost, producing 10.9% instead of the correct
    # 9.8% that case.json/FACILITATOR.md/tier2_probes.py's own P5 all already use).
    margin = 100.0 * (hi - lo) / hi
    print("base A=$%.2f  B=$%.2f  winner(lower cost)=%s  margin=%.1f%%" % (a, b, win, margin))

    print("\n--- +/-50%% flex sweep (FLEX[] only) ---")
    for name in FLEX:
        base_val = PARAMS[name]
        for label, mult in (("-50%", 0.5), ("+50%", 1.5)):
            flexed = real_costs({name: base_val * mult})
            fa, fb = flexed["A"], flexed["B"]
            fwin = "A" if fa < fb else "B"
            flo, fhi = min(fa, fb), max(fa, fb)
            fmargin = 100.0 * (fhi - flo) / fhi if fhi else 0.0
            flip = " <<< FLIPS" if fwin != win else ""
            cap = " (breaks 20% cap)" if fmargin > 20 else ""
            print("  %-20s %-5s -> A=$%.2f B=$%.2f winner=%s margin=%.1f%%%s%s" %
                  (name, label, fa, fb, fwin, fmargin, flip, cap))
