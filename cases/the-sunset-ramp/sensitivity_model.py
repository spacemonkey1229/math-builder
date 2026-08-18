#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Sunset Ramp.

Contract per skills/case-readiness/scripts/example_sensitivity_model.py:

    PARAMS                     dict[str, number]   every dial the case STATES
    FLEX                       list[str]            the subset that is an ASSUMPTION
    evaluate(params) -> dict   {"A": metric, "B": metric}   HIGHER is better
    evaluate_twist(params)     same shape, with the Guide Notes' backstop-battery twist applied

FLEX-scoping (see skills/case-readiness/SKILL.md, "Two behaviours that are intentional" /
P5 doctrine note, 2026-08-13): only dials the case had to CHOOSE go in FLEX[]. Cited/given
figures are stress-tested by P6 (data decay), not P5. Applying that test here:

  - t60_net_load, t120_net_load (Appendix B's 17:00 / 18:00 net-load figures) ARE an
    assumption: Appendix C (MA1) explicitly says the curve's SHAPE between anchor points is
    a modeling choice, not a directly-sourced figure, and gives its own sensitivity range
    (peak rate could plausibly run ~108-137.5+ MW/min depending on curvature). -> FLEX.
  - rise_1819_mw (the 18:00->19:00 jump) is the one real, cited figure in the table -- CAISO's
    reported 6.5 GW average rise during the 6pm hour (S5). It is given/cited data, not a
    choice the case made. -> NOT in FLEX (P6 territory).
  - battery_response_time_s is a genuine authorial convention: S4 only characterizes the
    battery qualitatively ("almost instantaneously"; 100-500 ms in the corroborating
    literature). RESEARCH_LOG.md (P01) records that the case's own working number, 1 second,
    was chosen as a deliberately conservative assumption, not read off a datasheet. -> FLEX.
  - peaker_capability_mw_per_min (50, S3), battery_power_mw (200, fixed by the bid), and both
    capital-cost totals (derived from S1/S2, themselves fixed bid quantities) are all
    cited/given or arithmetic on cited/given figures, never a scenario dial. -> NOT in FLEX.

Verified against case.json.derived (2026-08-13):
    base   peak_rate=137.5 MW/min · battery_cap=12000 MW/min · A covered, B 36.4% covered
           cost/MW-min: A=$4,721,454.55  B=$3,854,400.00  margin (B cheaper by) = 18.36%

Margin-convention note (reconciled 2026-08-17): case.json's canonical margin_pct (18.36%,
printed by this file's own __main__ self-check below) is (costA - costB) / costA * 100 --
Option B's savings expressed as a fraction of the more expensive option A's cost. That is
the number SPEC §2 / T1-09 checks against the 20% cap, and it is correct and internally
consistent everywhere it appears (case.json, FACILITATOR.md, case.md).

evaluate() below must return a HIGHER-IS-BETTER metric per the P5 contract, so it returns
each option's rate-delivered-per-dollar (1/cost) rather than raw cost. Tier 2 probe 5's
own margin formula, 100*(win-lo)/lo, applied to those inverted values, is NOT the same
quantity as case.json's margin_pct -- it works out to costA/costB - 1, i.e. Option A's cost
premium expressed as a fraction of the CHEAPER option B's cost (100*(costA-costB)/costB =
22.5% at base). Both 18.36% and 22.5% are exact, correct descriptions of the identical
$4,721,455-vs-$3,854,400 comparison; they differ only in which option's cost is the
percentage's denominator (savings-relative-to-loser vs. premium-relative-to-winner), a
well-known asymmetry in percentage math ("20% off" vs. the equivalent "25% markup"). This
is not reconcilable into one shared formula without either abandoning the higher-is-better
contract P5 requires (breaks max()/winner-detection) or fabricating an arbitrary constant
into the metric purely to hit a target number -- the latter was tried and rejected, since
it would exist for no reason but to force a number. case.json.balance.margin_pct/margin_pct
is deliberately left at 18.36% (the case's own SPEC-§2-facing convention); P5's own printed
base_margin_pct (22.5%) is the different, equally-real cost-premium framing.
"""
import math

PARAMS = {
    # --- Appendix B / Appendix C (MA1) -- the modeling-assumption net-load table -----------
    # Net load at 17:00 (t=60 min after 16:00) and 18:00 (t=120 min). The shape/curvature
    # choice Appendix C names as the case's own sensitivity concern.
    "t60_net_load_mw": 19500.0,
    "t120_net_load_mw": 22500.0,
    # --- Appendix B / Appendix D, S5 -- CITED, not an assumption (kept out of FLEX) --------
    # CAISO's own reported average 6.5 GW rise during the 6pm hour, anchoring 18:00->19:00.
    "rise_1819_mw": 6500.0,

    # --- Appendix A -- the battery --------------------------------------------------------
    "battery_power_mw": 200.0,              # fixed by the bid, not a modeling choice
    # RESEARCH_LOG.md P01: S4 is qualitative ("almost instantaneously"); the case's own
    # working figure is a deliberately conservative 1-second-to-full-power convention.
    "battery_response_time_s": 1.0,

    # --- Appendix A -- the peaker, CITED (S3), not an assumption --------------------------
    "peaker_capability_mw_per_min": 50.0,

    # --- Appendix A -- total capital costs, derived from CITED unit costs (S1, S2) --------
    "capA_total_usd": 649_200_000.0,
    "capB_total_usd": 192_720_000.0,

    # --- Twist (FACILITATOR.md) -- backstop-battery capital cost basis, CITED (S2) --------
    "battery_cost_per_kw": 1744.0,
}

# P5 sweeps THESE and only these -- the case's genuine stated assumptions.
# See the FLEX-scoping note in the module docstring for why rise_1819_mw, the peaker
# capability, battery_power_mw and both capital totals are deliberately excluded.
FLEX = [
    "t60_net_load_mw",          # Appendix C (MA1): curve-shape choice
    "t120_net_load_mw",         # Appendix C (MA1): curve-shape choice
    "battery_response_time_s",  # RESEARCH_LOG P01: conservative authorial convention
]


def _peak_ramp_rate_mw_per_min(p):
    """Fit the quadratic P(t) through the three fitted-window points (60, t60), (120, t120),
    (180, t120+rise) via Newton divided differences (equally spaced, h=60 min), then return
    the larger of dP/dt evaluated at the window's two endpoints -- dP/dt is linear in t, so
    its extreme over the window is always at one endpoint."""
    x0, x1, x2 = 60.0, 120.0, 180.0
    y0 = p["t60_net_load_mw"]
    y1 = p["t120_net_load_mw"]
    y2 = y1 + p["rise_1819_mw"]
    h = 60.0
    f01 = (y1 - y0) / h
    f12 = (y2 - y1) / h
    f012 = (f12 - f01) / (2 * h)          # = the quadratic's leading coefficient "a"

    def dPdt(t):
        return f01 + f012 * ((t - x1) + (t - x0))

    return max(dPdt(x0), dPdt(x2))


def _battery_capability_mw_per_min(p):
    # Full rated power reached within battery_response_time_s -> MW per minute.
    return p["battery_power_mw"] * 60.0 / p["battery_response_time_s"]


def _costs(p):
    """Returns (peak_rate, rate_A, rate_B, cost_A, cost_B) -- the case's own D2-D4 chain."""
    peak_rate = _peak_ramp_rate_mw_per_min(p)
    battery_cap = _battery_capability_mw_per_min(p)
    peaker_cap = p["peaker_capability_mw_per_min"]
    rate_A = min(battery_cap, peak_rate)          # D4: capped at the D2 rate
    rate_B = min(peaker_cap, peak_rate)
    cost_A = p["capA_total_usd"] / rate_A if rate_A > 0 else math.inf
    cost_B = p["capB_total_usd"] / rate_B if rate_B > 0 else math.inf
    return peak_rate, rate_A, rate_B, cost_A, cost_B


def evaluate(params):
    """Returns {'A': ..., 'B': ...} where HIGHER is better, per contract. The case's real
    primary metric (dollars per MW/min covered) is LOWER-is-better, so this returns each
    option's coverage-per-dollar (1 / cost) -- monotonically equivalent, so 'which option
    wins' and 'does a flex flip the winner' are unchanged, while still satisfying the
    higher-is-better contract the probe script relies on for max()/min()."""
    p = dict(PARAMS)
    p.update(params or {})
    _, _, _, cost_A, cost_B = _costs(p)
    return {"A": 1.0 / cost_A, "B": 1.0 / cost_B}


def evaluate_twist(params):
    """Guide Notes twist: pair a small backstop battery with the peaker, sized to cover
    exactly the peaker's shortfall (peak_rate - peaker_capability) rather than replace it
    outright -- 'a much smaller battery ... for a fraction of Option A's full battery cost.'
    Sized and costed on the same conventions already in PARAMS (same response-time
    assumption, same $/kW cost basis, S2) -- no new figure is invented. Option A (the
    original full Solar Stack) is untouched by the twist; only B changes."""
    p = dict(PARAMS)
    p.update(params or {})
    peak_rate, rate_A, rate_B, cost_A, _ = _costs(p)
    peaker_cap = p["peaker_capability_mw_per_min"]
    shortfall_mw_per_min = max(0.0, peak_rate - peaker_cap)
    # Backstop battery power (MW) needed to deliver shortfall_mw_per_min within the same
    # response-time convention as the main battery.
    backstop_power_mw = shortfall_mw_per_min * p["battery_response_time_s"] / 60.0
    backstop_cost = backstop_power_mw * 1000.0 * p["battery_cost_per_kw"]
    combined_cost = p["capB_total_usd"] + backstop_cost
    rate_B_twisted = min(peaker_cap + shortfall_mw_per_min, peak_rate)   # now fully covered
    cost_B_twisted = combined_cost / rate_B_twisted if rate_B_twisted > 0 else math.inf
    return {"A": 1.0 / cost_A, "B": 1.0 / cost_B_twisted}


if __name__ == '__main__':
    p = dict(PARAMS)
    peak_rate, rate_A, rate_B, cost_A, cost_B = _costs(p)
    margin_pct = 100.0 * (cost_A - cost_B) / cost_A   # (costA - costB) / costA, matches case.json
    print("base figures (should match case.json.derived exactly):")
    print(f"  peak_ramp_rate_mw_per_min = {peak_rate:.4f}  (expect 137.5)")
    print(f"  battery capability        = {_battery_capability_mw_per_min(p):.1f} MW/min (expect 12000.0)")
    print(f"  rate delivered A / B      = {rate_A:.1f} / {rate_B:.1f} MW/min (expect 137.5 / 50.0)")
    print(f"  cost per MW/min A         = ${cost_A:,.2f} (expect $4,721,454.55)")
    print(f"  cost per MW/min B         = ${cost_B:,.2f} (expect $3,854,400.00)")
    print(f"  margin_pct (B cheaper by) = {margin_pct:.2f} (expect 18.36)")

    ev = evaluate({})
    print("\nevaluate() (higher-is-better, inverted-cost form):", ev,
          "-> winner:", max(ev, key=ev.get))

    tw = evaluate_twist({})
    print("evaluate_twist():", tw, "-> winner:", max(tw, key=tw.get))
