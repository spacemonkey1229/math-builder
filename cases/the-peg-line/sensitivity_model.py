#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- The Peg Line.

Tier 2 probe 5 ("flex each stated assumption by +-50%; report which flips
the verdict") needs a runnable model of the case's own arithmetic.

CONTRACT -- two public names:

    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

REDESIGN NOTE (2026-09-01, balance-retune pass): the ORIGINAL version of this
case compared Option A's real "normal drift" reference (30 bps) against an
UNRELATED real historical crisis-event figure for Option B (1,224/1,000/1,400
bps, from the March 2023 USDC/SVB depeg). That mixed two different risk
categories and produced margin_pct = 97.47%, far past SPEC Sec 2's ~20% cap,
structurally (sweeping all three real readings of the crisis event only moved
margin_pct within 96.9%-97.8%).

This REDESIGNED version instead derives Option B's peg-deviation risk figure
from Option A's OWN real reference figure (30 bps, S5), scaled to Option B's
own Treasury-bill duration by the square-root-of-time rule (S9) -- the real,
Basel-Committee-recommended method for scaling a risk/volatility estimate
from a shorter holding horizon to a longer one:

    dev_B_bps = dev_A_bps * sqrt(duration_B_days / duration_A_days)

The case's primary metric (case.json.balance.margin_basis) is dollars of
annual yield earned per basis point of (duration-scaled) peg-deviation risk
shouldered:

    efficiency(option) = (reserve_total * yield_rate) / deviation_bps

This is already a benefit (bigger = more yield per unit of risk), so
evaluate() returns it directly -- no negation needed.

Mechanism modeled explicitly: reserve_total multiplies BOTH options' annual-
yield numerators identically, so it cancels out of the margin between A and
B -- load-bearing for D1's scientific-notation deliverable, but not a lever
that changes who wins. Less obviously, dev_a_bps (the 30 bps base figure)
ALSO cancels out of the margin now, for the same algebraic reason -- since
dev_B is DERIVED as a fixed multiple of dev_a_bps, both options' efficiency
figures scale together when dev_a_bps changes. This is a genuine structural
difference from the original design (where dev_a_bps and dev_b_bps were two
independent real figures, and dev_a_bps WAS load-bearing for margin_pct).

FLEX therefore excludes reserve_total AND dev_a_bps (both provably cancel --
confirmed below) and sweeps the parameters that actually move the ratio:
each option's yield rate, and the two duration figures (through the
square-root-of-time scaling factor).

RESEARCH_LOG.md's redesign section sweeps THREE real, defensible ways of
deriving dev_b_bps from dev_a_bps (square-root-of-time / linear / no scaling
at all) -- this script reproduces that sweep plus the full +-50% flex probe.
"""

import math

PARAMS = {
    # --- Appendix A / S1: total reserve amount (USD) -------------------------
    "reserve_total": 73_434_000_000.0,
    # --- Appendix B / S6: Option A (Short Ladder, 4-week bills) yield --------
    "yield_a_rate": 0.0375,
    # --- Appendix C / S6: Option B (Extended Ladder, 6-week bills) yield -----
    "yield_b_rate": 0.0381,
    # --- Appendix E row 1 / S5: Option A's real reference deviation (bps) ----
    "dev_a_bps": 30.0,
    # --- Appendix B / C: average time-to-maturity outstanding (days), fixed by
    # what "4-week"/"6-week" Treasury bills literally ARE -- not a chosen
    # assumption, definitional to the two options themselves. ------------------
    "duration_a_days": 28.0,
    "duration_b_days": 42.0,
    # --- Appendix E / MA3 / S9: the exponent on (duration_b/duration_a) used
    # to derive Option B's risk figure from Option A's real base figure. This
    # IS the case's one genuine, author-chosen modeling assumption (MA3):
    # 0.5 = square-root-of-time [primary, S9's own recommended method],
    # 1.0 = linear duration scaling [S9's own discussed alternative],
    # 0.0 = no incremental duration risk [a defensible floor case]. -----------
    "dev_b_scaling_exponent": 0.5,
}

# Probe 5 flexes THIS and only this. Every other PARAMS entry is either
# (a) cited/measured data -- reserve_total (S1), yield_a_rate/yield_b_rate
# (S6), dev_a_bps (S5) -- which P6's data-decay probe stress-tests instead
# of P5 ("Halving a WHO-rated cold life is a different case, not a
# sensitivity test" -- skills/case-readiness/SKILL.md), or (b) definitional
# to what the two options literally ARE -- duration_a_days/duration_b_days,
# fixed by "4-week"/"6-week" bills the same way a WHO cold-life figure is
# fixed by the vaccine's own spec. dev_b_scaling_exponent is the ONE dial
# this case's author genuinely had to choose (MA3) -- see module docstring
# and RESEARCH_LOG.md's redesign section: three real, defensible readings
# of this exact exponent (0.0 / 0.5 / 1.0) already move the recorded winner,
# which is exactly what P5 exists to catch and what this case already
# discloses in balance.margin_note, sensitivity_note and FACILITATOR.md.
#
# CORRECTED 2026-09-01 (case-readiness Tier 2 run): the prior version of
# this file put yield_a_rate/yield_b_rate/duration_a_days/duration_b_days in
# FLEX instead -- all four are cited or definitional, not assumptions, so
# flexing them by +-50% was testing "what if this were a different case,"
# not "what if the author's modeling choice were wrong." Narrowed to the one
# real assumption dial per the doctrine above.
FLEX = [
    "dev_b_scaling_exponent",
]

# Human-readable labels for the same three exponent values, used by the
# module's own __main__ reporting and by Appendix E / RESEARCH_LOG.md /
# D4's sweep. Kept as a separate lookup so PARAMS stays purely numeric.
SCALING_LABELS = {
    0.0: "no incremental duration risk [floor case]",
    0.5: "square-root-of-time [primary, S9]",
    1.0: "linear duration scaling [alternate]",
}


def _efficiency(reserve_total, yield_rate, dev_bps):
    annual_yield = reserve_total * yield_rate
    return annual_yield / dev_bps, annual_yield


def evaluate_full(params, scaling_exponent=None):
    """Internal helper -- returns (metrics_dict, extras_dict). Used by this
    module's own __main__ reporting, which wants the intermediate annual-yield
    and dev_b_bps figures. NOT the contract entry point -- see evaluate().
    scaling_exponent overrides p['dev_b_scaling_exponent'] when given
    explicitly (used by the D4 label sweep below)."""
    p = dict(PARAMS)
    p.update(params or {})
    exponent = p["dev_b_scaling_exponent"] if scaling_exponent is None else scaling_exponent
    ratio = p["duration_b_days"] / p["duration_a_days"]
    dev_b_bps = p["dev_a_bps"] * (ratio ** exponent)
    eff_a, yield_a = _efficiency(p["reserve_total"], p["yield_a_rate"], p["dev_a_bps"])
    eff_b, yield_b = _efficiency(p["reserve_total"], p["yield_b_rate"], dev_b_bps)
    # Higher $/bp is better -- this metric is already a benefit, so no
    # negation is needed to satisfy the "higher is better" contract.
    return {"A": eff_a, "B": eff_b}, {
        "annual_yield_A": yield_a,
        "annual_yield_B": yield_b,
        "dev_b_bps": dev_b_bps,
    }


def evaluate(params):
    """CONTRACT entry point for tier2_probes.py's Probe 5 harness:
    evaluate(params) -> {"A": metric, "B": metric}, higher is better.
    Uses whatever dev_b_scaling_exponent is passed in params (defaulting to
    PARAMS' primary 0.5/square-root-of-time reading) -- this is what lets
    Probe 5's +-50% flex on FLEX=['dev_b_scaling_exponent'] actually move
    the result."""
    metrics, _ = evaluate_full(params)
    return metrics


if __name__ == '__main__':
    base, extras = evaluate_full({})
    win = max(base, key=base.get)
    lo = min(base, key=base.get)
    margin = 100.0 * (base[win] - base[lo]) / base[win]
    print("Option A (Short Ladder)     efficiency: $%.2f / bp   annual yield: $%s" %
          (base["A"], f"{extras['annual_yield_A']:,.2f}"))
    print("Option B (Extended Ladder)  efficiency: $%.2f / bp   annual yield: $%s   dev_b_bps: %.2f" %
          (base["B"], f"{extras['annual_yield_B']:,.2f}", extras["dev_b_bps"]))
    print("winner:", win, " margin: %.2f%%" % margin)
    print()

    print("--- Reserve-total cancellation check (confirms it is not a lever) ---")
    for scale in (0.5, 1.0, 2.0, 10.0):
        p = dict(PARAMS)
        p["reserve_total"] = PARAMS["reserve_total"] * scale
        b, _ = evaluate_full(p)
        m = 100.0 * (max(b.values()) - min(b.values())) / max(b.values())
        print(f"  reserve_total x{scale:<5}: margin = {m:.2f}%  (unchanged, as expected)")
    print()

    print("--- dev_a_bps cancellation check (NEW in this redesign -- confirms it is not a lever) ---")
    for scale in (0.5, 1.0, 2.0, 10.0):
        p = dict(PARAMS)
        p["dev_a_bps"] = PARAMS["dev_a_bps"] * scale
        b, _ = evaluate_full(p)
        m = 100.0 * (max(b.values()) - min(b.values())) / max(b.values())
        print(f"  dev_a_bps x{scale:<5}: margin = {m:.2f}%  (unchanged, as expected)")
    print()

    print("--- Sweep across all three real, defensible risk-scaling modes (Appendix E / D4) ---")
    for exponent, label in SCALING_LABELS.items():
        b, extras = evaluate_full({}, scaling_exponent=exponent)
        hi = max(b.values())
        lo_v = min(b.values())
        m = 100.0 * (hi - lo_v) / hi
        w = max(b, key=b.get)
        print(f"  {label:<42} dev_b_bps={extras['dev_b_bps']:>6.2f}  margin={m:6.2f}%  winner={w}")
    print()

    print("--- Context check: what if Option B had stayed the original 13-week ladder? ---")
    p = dict(PARAMS)
    p["yield_b_rate"] = 0.0387
    p["duration_b_days"] = 91.0
    b, extras = evaluate_full(p)
    m = 100.0 * (max(b.values()) - min(b.values())) / max(b.values())
    w = max(b, key=b.get)
    print(f"  13-week (91d, 3.87%): dev_b_bps={extras['dev_b_bps']:.2f}  margin={m:.2f}%  winner={w}")
    print("  (Matches the original draft's underlying duration; explains, using this case's own")
    print("   real methodology, why the 13-week draft was rejected in favor of 6-week.)")
    print()

    print("--- +-50% flex on every FLEX[] parameter (probe 5), primary scaling mode ---")
    for name in FLEX:
        for mult, label in ((0.5, "-50%"), (1.5, "+50%")):
            p = dict(PARAMS)
            p[name] = PARAMS[name] * mult
            b, _ = evaluate_full(p)
            m = 100.0 * (max(b.values()) - min(b.values())) / max(b.values())
            new_win = max(b, key=b.get)
            flipped = " *** VERDICT FLIPS ***" if new_win != win else ""
            print(f"  {name:<16} {label:<5}: margin = {m:6.2f}%  winner={new_win}{flipped}")
