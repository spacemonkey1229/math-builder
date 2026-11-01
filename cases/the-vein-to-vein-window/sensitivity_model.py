#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- The Vein-to-Vein Window.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own D1/D4 arithmetic: apply the
piecewise viability function V(t) (Appendix B, sourced 180-minute cutoff) to
each route's disclosed nominal elapsed time and delay-scenario model (Appendix
C / E, Modeling Assumptions MA1-MA4), and sum the probability of the delay
scenarios that keep each route under the cutoff.

CONTRACT -- exactly two required public names:

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

The primary metric is P(dose viable at re-administration) for each route --
already "higher is better" (a probability of success), so no negation is
needed here (contrast with cases/the-quiet-thief, whose metric is a cost).

    cutoff_minutes      = 180                                    (Appendix B, [S2] x60)
    t_no_delay(route)   = nominal_minutes(route)
    t_minor(route)      = nominal_minutes(route) + minor_delay_minutes
    t_major(route)      = nominal_minutes(route) + major_delay_minutes
    V(t)                = 1 if t < cutoff_minutes else 0          (Appendix B)
    P(route viable)     = sum over scenarios s of  p(s) * V(t_s(route))

Appendix B's cutoff [S2] is cited data, not a stated assumption -- P6 (data
decay) covers it, not P5 (see "Only FLEX[] is swept" in
skills/case-readiness/SKILL.md's P5 section). Appendix C/E's four Modeling
Assumptions (MA1-MA4) ARE the case's genuinely disclosed, chosen scenario
dials -- exactly what P5 exists to flex.

Verified against case.json.balance (2026-09-09):
    base (MA1=45, MA2=150, MA3=20/50, MA4=71/20/9)
    P(A viable) = 100.00%   P(B viable) = 91.00%   margin (house convention,
    winner-loser as a percent of the LOSER, matching this script's own
    base_margin formula) = 9.89%
"""

CUTOFF_MINUTES = 180.0  # Appendix B, [S2]: 3 hours x 60 -- cited, not flexed by P5

PARAMS = {
    # --- Appendix C / Modeling Assumption MA1 (disclosed scenario dial) -----
    "a_nominal_minutes": 45.0,
    # --- Appendix C / Modeling Assumption MA2 (disclosed scenario dial) -----
    "b_nominal_minutes": 150.0,
    # --- Appendix C / Modeling Assumption MA3 (disclosed scenario dial) -----
    "minor_delay_minutes": 20.0,
    "major_delay_minutes": 50.0,
    # --- Appendix C / Modeling Assumption MA4 (disclosed scenario dial) -----
    "p_no_delay": 0.71,
    "p_minor_delay": 0.20,
    "p_major_delay": 0.09,
}

# Probe 5 flexes all four disclosed Modeling Assumptions -- MA1/MA2 (each
# route's nominal elapsed time) and MA3 (the delay-scenario minute additions).
# MA4 (the probability distribution) is deliberately NOT included in the
# default +/-50% minute-flex sweep because it is a probability triple that
# must keep summing to 1 -- flexing p_major_delay alone by +/-50% is run as a
# SEPARATE, explicit check below (renormalizing the other two proportionally)
# rather than folded into the generic FLEX[] sweep, which assumes independent
# dials. Run with --flex-all to sweep every numeric PARAM independently anyway
# (this will distort MA4's probabilities so they no longer sum to 1 -- a known,
# accepted limitation of the generic sweep for a simplex-constrained dial).
FLEX = [
    "a_nominal_minutes",
    "b_nominal_minutes",
    "minor_delay_minutes",
    "major_delay_minutes",
]


def _viable(t, cutoff=CUTOFF_MINUTES):
    """Appendix B's piecewise V(t): 1 (viable) for t < cutoff, 0 otherwise."""
    return 1.0 if t < cutoff else 0.0


def _route_probability(nominal_minutes, p):
    """D4: sum the probability of every delay scenario that keeps t < cutoff."""
    t_no_delay = nominal_minutes
    t_minor = nominal_minutes + p["minor_delay_minutes"]
    t_major = nominal_minutes + p["major_delay_minutes"]

    prob = 0.0
    prob += p["p_no_delay"] * _viable(t_no_delay)
    prob += p["p_minor_delay"] * _viable(t_minor)
    prob += p["p_major_delay"] * _viable(t_major)
    return prob


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})

    a = _route_probability(p["a_nominal_minutes"], p)
    b = _route_probability(p["b_nominal_minutes"], p)

    # Already "higher is better" (a viability probability) -- no negation.
    return {"A": a, "B": b}


def evaluate_twist(params=None):
    """The FACILITATOR.md twist (a second patient's dose needing the SAME one
    certified on-site pharmacist today) is a SCHEDULING/CAPACITY-CONTENTION
    fact about which dose gets which route, not a change to either route's
    own per-dose V(t) or probability model -- it does not change today's
    dose's numbers at all. It is grounded directly in a fact case.md's
    Background already states (On-Site Rapid Thaw depends on the unit's ONE
    specially certified pharmacist, who can attend only one dose at a time),
    not a new resource limit invented only for the Twist -- this was tightened
    2026-09-09 after a Tier 2 probe 4 fresh-reviewer finding that the
    originally-drafted 'capped monthly budget' framing contradicted
    Background's 'on standby around the clock' description of the same cost
    (a continuous commitment, not a metered quota). Returns the unchanged
    base evaluate() result so Tier 2 probe 4 can mechanically confirm the
    twist is a genuine N/A-for-the-math twist (a scheduling/policy reframe)
    rather than a silently-absent one -- see FACILITATOR.md's own framing of
    this exact distinction."""
    return evaluate(params)


if __name__ == '__main__':
    base = evaluate({})
    a, b = base["A"], base["B"]
    hi, lo = max(a, b), min(a, b)
    margin = 100.0 * (hi - lo) / lo  # house convention: winner-loser as a % of the LOSER
    print("base  P(A viable)=%.2f%%  P(B viable)=%.2f%%  margin=%.2f%%"
          % (a * 100, b * 100, margin))
    assert abs(a - 1.0) < 1e-9, "P(A viable) drifted from the disclosed 100%"
    assert abs(b - 0.91) < 1e-9, "P(B viable) drifted from the disclosed 91%"
    assert abs(margin - 9.89) < 0.05, "margin drifted from case.json's recorded 9.89%"

    twist = evaluate_twist()
    print("twist (policy reframe, no per-dose math change): P(A)=%.2f%%  P(B)=%.2f%%"
          % (twist["A"] * 100, twist["B"] * 100))
    assert twist == base, "evaluate_twist() should be numerically identical to evaluate() -- the twist is a policy reframe, not a math change"

    print("\n+/-50%% flex of each disclosed Modeling Assumption (MA1-MA3):")
    for name in FLEX:
        for mult, label in ((0.5, "-50%"), (1.5, "+50%")):
            val = PARAMS[name] * mult
            r = evaluate({name: val})
            a2, b2 = r["A"], r["B"]
            hi2, lo2 = max(a2, b2), min(a2, b2)
            m2 = 100.0 * (hi2 - lo2) / lo2 if lo2 else 0.0
            state = "A" if a2 > b2 else ("B" if b2 > a2 else "TIE")
            print("  %-20s %-5s -> %6.1f   P(A)=%6.2f%%  P(B)=%6.2f%%  margin=%5.2f%%  winner=%s"
                  % (name, label, val, a2 * 100, b2 * 100, m2, state))

    print("\nSeparate check -- MA4's major-delay probability at +/-50%,")
    print("renormalized against p_no_delay/p_minor_delay proportionally:")
    for mult, label in ((0.5, "-50%"), (1.5, "+50%")):
        p_major_new = PARAMS["p_major_delay"] * mult
        remaining = 1.0 - p_major_new
        base_remaining = PARAMS["p_no_delay"] + PARAMS["p_minor_delay"]
        p_no_delay_new = PARAMS["p_no_delay"] / base_remaining * remaining
        p_minor_new = PARAMS["p_minor_delay"] / base_remaining * remaining
        r = evaluate({
            "p_major_delay": p_major_new,
            "p_no_delay": p_no_delay_new,
            "p_minor_delay": p_minor_new,
        })
        a2, b2 = r["A"], r["B"]
        hi2, lo2 = max(a2, b2), min(a2, b2)
        m2 = 100.0 * (hi2 - lo2) / lo2 if lo2 else 0.0
        state = "A" if a2 > b2 else ("B" if b2 > a2 else "TIE")
        print("  p_major_delay %-5s -> %.3f  P(A)=%6.2f%%  P(B)=%6.2f%%  margin=%5.2f%%  winner=%s"
              % (label, p_major_new, a2 * 100, b2 * 100, m2, state))
