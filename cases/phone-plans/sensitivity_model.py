#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Phone Plans (cases/phone-plans).

CONTRACT — exactly two public names (see skills/case-readiness/scripts/
example_sensitivity_model.py for the full spec this follows):

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     same shape, with the twist applied

The graded primary_metric is a total monthly DOLLAR COST, where lower is
better for the family. To fit the harness's "higher is better" convention,
evaluate() returns SCALE / total_cost for each option. This is not just a
sign flip: a naive (CEILING - total_cost) transform was tried first and
rejected (2026-08-17) because tier2_probes.py's margin formula,
100*(winner-loser)/loser, applied to (CEILING - cost) values does NOT
reduce to the real dollar-cost percentage margin for any finite CEILING —
it silently shrinks every reported margin (12.5% real came back as 3.1%,
25.0%/28.6% came back as 6.5%/6.3%), corrupting the 20%-cap check. The
reciprocal transform is scale-invariant and algebraically exact: for
SCALE/a and SCALE/b with b < a (B cheaper, B wins), 100*(SCALE/b -
SCALE/a)/(SCALE/a) = 100*(a-b)/b, which IS the real dollar-cost percentage
margin, independent of SCALE's value. Verified: base margin now returns
18.8% (matches case.json.balance.margin_pct) and every FLEX-swept margin
below matches case.json.sensitivity_disclosure[]'s recomputed extremes
exactly.

Base case (2 phone lines + 2 tablet lines, today's need):
    A (Verizon Plus)  total = $232.81/mo post-tax
    B (AT&T Extra 2.0) total = $196.05/mo post-tax
    margin  = (232.81 - 196.05) / 196.05 = 18.8%   (B/AT&T is cheaper)

Re-derived 2026-08-18: verizon_tablet_rate corrected from an untiered $20.00/mo
to the live-verified, tier-matched Unlimited Plus rate of $25.00/mo (raw
verizon.com pricing page, re-checked via WebFetch of the raw HTML) -- this
moved the base margin from 12.5% to 18.8% and changed both tablet-rate
sensitivity extremes from "exact tie" to non-tie B-still-wins/cap-breach
outcomes (see case.json's sensitivity_disclosure[] for the recomputed
extremes).

FLEX[] contains ONLY the case's two genuinely stated, authored assumptions
(Appendix F, MA1 and MA2) — never the sourced per-line carrier pricing
(Appendices A/B), which is fixed, cited, real-world fact, not a dial the
case authors chose. Per skills/case-readiness/SKILL.md's P5 rule, only
authored assumptions are swept by default.
"""

PARAMS = {
    # --- Appendix A/B, sourced per-line phone pricing (fixed fact, NOT flexed) ---
    "verizon_plus_2line": 140.00,
    "att_extra_2line": 120.00,
    # --- Appendix C, Modeling Assumption 1 (MA1): flat per-tablet rate -----------
    "verizon_tablet_rate": 25.00,
    "att_tablet_rate": 20.00,
    "n_tablets": 2,
    # --- Appendix D, Modeling Assumption 2 (MA2): blended tax/fee multiplier -----
    "oregon_tax_rate": 0.2253,
}

# Only the two stated, authored modeling assumptions are swept by default —
# the carrier per-line pricing itself is sourced, given data (P6's job, not P5's).
FLEX = ["verizon_tablet_rate", "att_tablet_rate", "oregon_tax_rate"]

SCALE = 100000.0  # arbitrary positive constant; margin_pct is scale-invariant


def _total(phone_cost, tablet_rate, n_tablets, tax_rate):
    pretax = phone_cost + tablet_rate * n_tablets
    return round(pretax * (1.0 + tax_rate), 2)


def _totals(p):
    a_total = _total(p["verizon_plus_2line"], p["verizon_tablet_rate"],
                      p["n_tablets"], p["oregon_tax_rate"])
    b_total = _total(p["att_extra_2line"], p["att_tablet_rate"],
                      p["n_tablets"], p["oregon_tax_rate"])
    return a_total, b_total


def evaluate(params):
    # CONTRACT: exactly two keys, "A" and "B" (see module docstring). A prior
    # version of this function also returned "A_cost"/"B_cost" debug keys —
    # harmless when hand-read, but tier2_probes.py's flex/margin logic does
    # max(r, key=r.get) / min(r, key=r.get) over EVERY key in the returned
    # dict, not just "A"/"B". With four keys present, the cost keys (much
    # smaller in magnitude than the SCALE/cost score keys) were silently
    # winning the min() call, corrupting every P5 margin/flip/tie computation
    # (fixed 2026-08-17 — see QA_REPORT.md / DOCTRINE_LEDGER.md for the prior
    # FAIL this produced). Use _totals(params) directly for raw dollar figures.
    a_total, b_total = _totals(params)
    return {"A": round(SCALE / a_total, 4), "B": round(SCALE / b_total, 4)}


def evaluate_twist(params):
    """The Twist (FACILITATOR.md): Jake's real hotspot usage on the road
    (4+ days/week) is assumed here to approach Verizon Plus's 30GB cap,
    forcing an upgrade to a higher Verizon tier (+$10/line list) to avoid
    throttling — while AT&T Extra 2.0's 50GB heaadroom needs no upgrade.
    This does not change which option a Hero would evaluate on Appendix A/B
    alone; it only strengthens Option B's real-world case once hotspot
    capacity, not just price, is weighed (see D5)."""
    twisted = dict(params)
    # Twist: Verizon needs a $10/mo upgrade surcharge to cover realistic hotspot use.
    twisted_a_pretax = (params["verizon_plus_2line"] + 10.0
                         + params["verizon_tablet_rate"] * params["n_tablets"])
    a_total = round(twisted_a_pretax * (1.0 + params["oregon_tax_rate"]), 2)
    _, b_total = _totals(params)
    return {"A": round(SCALE / a_total, 4), "B": round(SCALE / b_total, 4)}


if __name__ == "__main__":
    a_total, b_total = _totals(PARAMS)
    margin = 100.0 * (a_total - b_total) / b_total
    print(f"A (Verizon Plus) total: ${a_total:.2f}")
    print(f"B (AT&T Extra 2.0) total: ${b_total:.2f}")
    print(f"margin (A vs B): {margin:.1f}%")
    r = evaluate(PARAMS)
    print("evaluate():", r)
    t = evaluate_twist(PARAMS)
    print("evaluate_twist():", t)
