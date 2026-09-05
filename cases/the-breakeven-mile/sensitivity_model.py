#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Breakeven Mile.

Tier 2 probe 5 ("flex each stated assumption by ±50%; report which flips the
verdict") needs a runnable model of the case's own D1/D2 arithmetic.

CONTRACT — exactly two required public names:

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

Both options' totals are annual COSTS (case.json.balance.margin_basis:
C_A(m) = 3039 + 0.2303m, C_B(m) = 1.50m), so lower is better. evaluate()
returns each option's cost NEGATED so that "higher is better" holds for the
harness, matching the convention documented in cases/compute-lease and
cases/fret-board's models.

FLEX is scoped to MA1 (Renata's own annual mileage) only. Per this project's
doctrine (see cases/compute-lease/sensitivity_model.py's header), sensitivity
to STATED MODELING ASSUMPTIONS is what P5 tests; sensitivity to cited/sourced
data (S1's fixed costs, S2's per-mile operating rate, S3's rideshare rate) is
instead stress-tested by P6 (data decay), not P5. MA1 is also, per
case.json.modeling_assumptions[MA1].sensitivity and FACILITATOR.md, THE
single most fragile input in this case by design — the retune from 11,500
mi/yr down to 2,760 mi/yr is exactly what was done to land the margin inside
SPEC §2's cap, and this is the model that lets P5 check whether that retune
actually holds up under a ±50% swing, not just at its own chosen point.
Run with --flex-all (via tier2_probes.py) to additionally sweep the three
sourced dials anyway.

Verified against case.json / case.md (2026-09-03 redesign):
    base (MA1 = 2,760 mi/yr)   C_A = $3,674.63   C_B = $4,140.00
                               Keys of Her Own wins, margin 11.24%
                               (matches case.json.balance.margin_pct)
    m* (breakeven)             2,393.5... mi/yr  (case.json.balance.margin_basis)
"""

PARAMS = {
    # --- Appendix A, sourced (S1) --------------------------------------------
    "fixed_costs_usd_per_year": 3039.0,   # $1,572 insurance + $854 loan interest + $613 registration
    # --- Appendix B, sourced (S2) --------------------------------------------
    "per_mile_operating_usd": 0.2303,
    # --- Appendix C, sourced (S3) --------------------------------------------
    "rideshare_rate_usd_per_mile": 1.50,
    # --- Appendix D / Modeling Assumption MA1 --------------------------------
    "annual_mileage_MA1": 2760.0,          # Renata's own estimated annual mileage
}

# Probe 5 flexes THIS and only this by default: the one stated, disclosed
# Modeling Assumption (MA1). The fixed costs, per-mile operating rate, and
# rideshare rate are cited/sourced data (S1, S2, S3), stress-tested by P6
# (data decay) instead of P5 -- flexing AAA's or RideWise's published figures
# by +-50% is not a sensitivity test of this case's own assumption, it is a
# different case.
FLEX = [
    "annual_mileage_MA1",   # MA1
]


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})

    m = p["annual_mileage_MA1"]
    cost_a = p["fixed_costs_usd_per_year"] + p["per_mile_operating_usd"] * m
    cost_b = p["rideshare_rate_usd_per_mile"] * m

    # Negate: lower annual cost is better, but the harness convention is
    # higher-is-better, matching cases/compute-lease and cases/fret-board.
    return {"A": -cost_a, "B": -cost_b}


def evaluate_twist(params):
    """FACILITATOR.md's Twist: re-solve at S3's corrected low-end metro
    rideshare rate ($0.90/mile, most US cities -- Tier 2 Probe 6 corrected
    S3's disclosed range 2026-09-03 to $0.90-$1.60/mile most cities, up to
    $2.50+/mile in the highest-cost metros) instead of the $1.50/mile
    national average, holding everything else (including MA1) fixed. This
    is the end of the range that FLIPS the verdict to Option B -- see
    evaluate_twist_high() for the other end, which does not flip it. Not
    part of the probe 5 contract; used by probe 4 (twist integrity) when
    present."""
    p = dict(PARAMS)
    p.update(params or {})
    p["rideshare_rate_usd_per_mile"] = 0.90
    return evaluate(p)


def evaluate_twist_high(params=None):
    """The other end of S3's corrected range ($2.50/mile, highest-cost
    metros such as NYC) -- Option A wins even more comfortably here. Not
    part of any probe contract; provided so both ends of the Twist's real
    range are checkable, not just the one that flips the verdict."""
    p = dict(PARAMS)
    p.update(params or {})
    p["rideshare_rate_usd_per_mile"] = 2.50
    return evaluate(p)


def crossover_mileage(params=None):
    """Solve for the breakeven mileage m* at which A and B tie -- i.e. D2.
    Not part of the probe 5 contract; provided for convenience / cross-
    checking against case.json.balance.margin_basis (m* ~= 2,393.5 mi/yr)."""
    p = dict(PARAMS)
    p.update(params or {})
    denom = p["rideshare_rate_usd_per_mile"] - p["per_mile_operating_usd"]
    return p["fixed_costs_usd_per_year"] / denom


if __name__ == '__main__':
    base = evaluate({})
    ca, cb = -base["A"], -base["B"]
    winner = "A (Keys of Her Own)" if ca < cb else "B (The All-App Life)"
    loser_cost, winner_cost = max(ca, cb), min(ca, cb)
    margin = 100.0 * (loser_cost - winner_cost) / loser_cost
    print("base  C_A=$%.2f  C_B=$%.2f  winner=%s  margin=%.2f%%" % (ca, cb, winner, margin))
    print("D2 breakeven mileage m* = %.1f mi/yr" % crossover_mileage())

    print("\n±50%% flex of MA1 (annual_mileage_MA1):")
    for mult, label in ((0.5, "-50%"), (1.5, "+50%")):
        m = PARAMS["annual_mileage_MA1"] * mult
        r = evaluate({"annual_mileage_MA1": m})
        ca2, cb2 = -r["A"], -r["B"]
        w2 = "A (Keys of Her Own)" if ca2 < cb2 else "B (The All-App Life)"
        lo2, hi2 = min(ca2, cb2), max(ca2, cb2)
        margin2 = 100.0 * (hi2 - lo2) / hi2
        flip = " *** FLIPS ***" if w2 != winner else ""
        print("  MA1 %s (m=%.1f)  C_A=$%.2f  C_B=$%.2f  winner=%s  margin=%.2f%%%s"
              % (label, m, ca2, cb2, w2, margin2, flip))
