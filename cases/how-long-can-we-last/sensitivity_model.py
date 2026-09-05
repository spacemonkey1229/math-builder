"""Sensitivity model for How Long Can We Last (SPEC section 2 balance test, case-readiness
Tier 2 probe 5). CONTRACT: evaluate(params) -> {"A": metric, "B": metric}, higher wins.

Metric: dollars of coverage margin each fund provides against the household's documented dry
spell, expressed the same way case.json.balance does -- Fund B's size minus Fund A's size is the
margin story, so for a comparable "higher wins" framing this model reports each fund's SURVIVAL
MONTHS against the flexed dry-spell length, and evaluate() returns the fund SIZE (a fund that must
be bigger to do the same job is, all else equal, the "worse" -- more expensive -- option, so this
model treats coverage-sufficiency as the deciding metric and dollar size as secondary; see
notes below and the printed report for the actual winner logic used).

Single disclosed formula, no hidden blend:
    Fund_A = 3 * essential_monthly_expenses                      (flat rule, unaffected by MA2)
    Fund_B = dry_spell_months * (essential_monthly_expenses - renata_monthly_income)
    Fund_A_coverage_months = Fund_A / (essential_monthly_expenses - renata_monthly_income)
    winner = the fund that fully covers dry_spell_months, at the lower cost. If both do (or
             neither does), report the higher-coverage-per-dollar fund as a CAVEAT.
"""

PARAMS = {
    "essential_monthly_expenses": 5874.0,   # Appendix A, S1
    "renata_monthly_income": 2983.0,        # Appendix B, S2
    "dry_spell_months": 7.0,                # Appendix C/D, MA2 -- the case's ONLY load-bearing
                                             # sizing assumption (MA1 affects only the D2 exercise,
                                             # not fund sizing -- see case.json.modeling_assumptions)
    "rule_of_thumb_months": 3.0,            # the flat convention Option A is built on (not flexed;
                                             # it is the fixed, widely-quoted number being tested)
}

# Probe 5 flexes THIS and only this -- SPEC §2 asks for sensitivity to STATED ASSUMPTIONS, not to
# cited measurements. MA2 (the dry spell's length/severity) is the case's one load-bearing
# modeling assumption for fund sizing; every other figure in PARAMS is a cited source (S1, S2) or
# a fixed convention (the "3 months" rule itself, which is what's being tested, not an assumption
# about the household). MA1 is deliberately excluded from FLEX -- case.json's own sensitivity note
# for MA1 states it "plays no role in sizing either fund," which this model's structure confirms:
# MA1 never appears in PARAMS at all.
FLEX = ["dry_spell_months"]


def monthly_shortfall(p):
    return p["essential_monthly_expenses"] - p["renata_monthly_income"]


def fund_sizes(p):
    fund_a = p["rule_of_thumb_months"] * p["essential_monthly_expenses"]
    fund_b = p["dry_spell_months"] * monthly_shortfall(p)
    return fund_a, fund_b


def coverage_months(fund, p):
    return fund / monthly_shortfall(p)


def evaluate(p):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. Metric = months of coverage each fund
    actually provides against the flexed dry-spell shortfall (the case's own primary_metric),
    capped conceptually at dry_spell_months for "fully sufficient" framing but reported uncapped
    here so the margin below the requirement is visible."""
    fund_a, fund_b = fund_sizes(p)
    return {
        "A": coverage_months(fund_a, p),
        "B": coverage_months(fund_b, p),
    }


def evaluate_twist(p):
    """Twist: N/A for this case (see FACILITATOR.md) -- no separate twist scenario to evaluate.
    Provided only so callers expecting the optional hook do not fail; returns evaluate(p)."""
    return evaluate(p)


if __name__ == "__main__":
    shortfall = monthly_shortfall(PARAMS)
    fund_a, fund_b = fund_sizes(PARAMS)
    print(f"Monthly shortfall (essential - Renata's income): ${shortfall:.2f}")
    print(f"Fund A (Rule-of-Thumb, 3mo x expenses): ${fund_a:.2f}")
    print(f"Fund B (Real-Stretch, {PARAMS['dry_spell_months']:.0f}mo x shortfall): ${fund_b:.2f}")

    margin = (fund_b - fund_a) / fund_a * 100
    print(f"margin_pct (Fund B vs Fund A, dollar size) = {margin:.2f}%")
    assert abs(margin - 14.84) < 0.05, "margin drifted from case.json's recorded 14.84%"

    ev = evaluate(PARAMS)
    print(f"\nAt base case: Fund A covers {ev['A']:.2f} months, Fund B covers {ev['B']:.2f} months, "
          f"dry spell requires {PARAMS['dry_spell_months']:.1f} months.")
    print(f"Fund A coverage as % of dry spell: {ev['A']/PARAMS['dry_spell_months']*100:.1f}%")

    print("\nFlexing MA2 (dry_spell_months) by +/-50%:")
    for mult, label in [(0.5, "-50%"), (1.5, "+50%")]:
        p2 = dict(PARAMS)
        p2["dry_spell_months"] = PARAMS["dry_spell_months"] * mult
        fa2, fb2 = fund_sizes(p2)
        ev2 = evaluate(p2)
        pct_a = ev2["A"] / p2["dry_spell_months"] * 100
        a_sufficient = ev2["A"] >= p2["dry_spell_months"]
        print(f"  dry_spell_months={p2['dry_spell_months']:.2f} ({label}): Fund A covers "
              f"{ev2['A']:.2f}mo ({pct_a:.1f}% of stretch, {'SUFFICIENT' if a_sufficient else 'SHORT'}); "
              f"Fund B size=${fb2:.2f} vs Fund A size=${fa2:.2f} "
              f"(fund-size margin {((fb2-fa2)/fa2*100):.2f}%)")

    print("\nFlexing MA2 by +/-100% (extreme check):")
    for mult, label in [(0.0, "0 (no dry spell)"), (2.0, "+100%")]:
        p2 = dict(PARAMS)
        p2["dry_spell_months"] = PARAMS["dry_spell_months"] * mult
        if p2["dry_spell_months"] == 0:
            print(f"  dry_spell_months=0.00 ({label}): both funds trivially sufficient (no shortfall "
                  f"period to survive) -- Fund A is strictly better (same protection, less cash tied up).")
            continue
        fa2, fb2 = fund_sizes(p2)
        ev2 = evaluate(p2)
        pct_a = ev2["A"] / p2["dry_spell_months"] * 100
        a_sufficient = ev2["A"] >= p2["dry_spell_months"]
        print(f"  dry_spell_months={p2['dry_spell_months']:.2f} ({label}): Fund A covers "
              f"{ev2['A']:.2f}mo ({pct_a:.1f}% of stretch, {'SUFFICIENT' if a_sufficient else 'SHORT'}); "
              f"Fund B size=${fb2:.2f} vs Fund A size=${fa2:.2f} "
              f"(fund-size margin {((fb2-fa2)/fa2*100):.2f}%)")

    print("\nBreak-even: dry_spell_months at which Fund A exactly covers the stretch "
          f"(Fund A / shortfall == dry_spell_months): {fund_a/shortfall:.3f} months")
