#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Seton Hall (owned by this case, per MCS-26 / A2).

Authored 2026-08-13 for the initial legacy conversion, to give Tier 2 probe P5
a mechanical backstop from day one rather than leaving it NOT RUN.

Unlike most cases in this corpus, Seton Hall's graded primary metric is not
built from an author-chosen Modeling Assumption that could plausibly have
been set differently -- it is a real, fixed historical fact: Seton Hall's
position in the final 2019-20 AP media poll (No. 15) relative to the
tournament's No. 16 top-seed-line cutoff (case.json.balance.margin_basis).
There is no "what if the assumption were different" lever on that number --
it happened once, and it is cited (case.json sources S3/S4).

What IS genuinely a modeling choice, and what this model exists to test, is
*which real ranking* governs the verdict. Three real, differently-computed
national rankings exist for the same team on the same date:
  - ap_rank        (15)  -- human media poll, the case's own primary_metric
  - net_rank       (12)  -- the NCAA's own opponent-adjusted system
  - win_pct_only_rank (50) -- a real, computed rank ignoring schedule
                              strength entirely (the FACILITATOR.md "trap")
evaluate() checks the case's own primary metric (AP vs cutoff). evaluate_twist()
re-checks the same cutoff test against NET -- the real corroborating ranking
FACILITATOR.md's Twist reveals -- rather than a hypothetical parameter shift,
because this case's twist is a real second data point, not a change in
circumstance. See margins() for the win_pct_only_rank comparison too.

CONTRACT — exactly two public names (see skills/case-readiness/scripts/
example_sensitivity_model.py for the full spec this follows):

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     same shape, with the twist applied

Verified against cases/seton-hall/case.json.derived (2026-08-13):
    evaluate():       A=1 (cutoff_rank - ap_rank), B=0  -> A>B, "yea", by the
                       thinnest possible real margin (1 spot / 6.25% of 16)
    evaluate_twist():  A=4 (cutoff_rank - net_rank), B=0 -> A>B, "yea", by a
                       wider real margin (4 spots / 25.0% of 16) -- NET
                       corroborates AP's verdict but with more room to spare
"""

PARAMS = {
    # --- case.json sources S4: real, dated 2019-20 final AP media poll rank --
    "ap_rank": 15,
    # --- case.json sources S5: real NCAA NET ranking, final tracked week ------
    "net_rank": 12,
    # --- MA2: the tournament's top-16-overall-seed-line cutoff (structural,
    # not an author-chosen scenario magnitude -- fixed by the real format) ----
    "cutoff_rank": 16,
    # --- derived{}: a real, computed alternate rank ignoring schedule
    # strength entirely -- the FACILITATOR.md "trap" reading -----------------
    "win_pct_only_rank": 50,
    "win_pct_field_size": 270,
    "national_field_size": 353,
}

# CORRECTED 2026-08-13 (Tier 2 P5 re-run): the original version of this file
# put BOTH ap_rank and net_rank in FLEX. That was a real bug, not a stylistic
# choice -- per SPEC Section 2 / MCS-26 and the reference model's own doctrine
# ("halving a WHO-rated cold life is not a sensitivity test... cited data is
# stress-tested by P6 instead"), net_rank is cited data (source S5) that
# evaluate() never even reads -- flexing it produced pure noise (identical
# A/B every time) and a spurious "breaks the 20% cap" finding that told a
# reader nothing about the case. Removed.
#
# ap_rank stays in FLEX. It is also, honestly, cited data (source S4) rather
# than an author-chosen Modeling Assumption (MA1-MA3 in case.json, none of
# which touch the graded primary metric at all -- MA1 only affects the D3/D4
# comparison set, MA2/MA3 are fixed external tournament rules, not dials --
# see each one's own `sensitivity` note in case.json). A strict SPEC-Section-2
# reading could argue ap_rank should move to P6 and this probe should report
# nothing. That would be a mistake here: ap_rank IS the graded primary metric,
# and P5 exists precisely so a guide never defends a margin that does not
# exist. Excluding the one number the whole verdict rests on, just to make
# FLEX empty and force a mechanical pass, would be gaming the checker, not
# fixing the case. See __main__ and QA_REPORT.md for the honest conclusion:
# genuine elimination was attempted (a different, less-thin real ranking was
# considered as primary_metric and rejected -- see QA_REPORT.md P5 section)
# and is not honestly available, so P5 is reported FAIL, per MCS-26/41 (no
# disclosure-aware pass state), not silently converted to PASS.
FLEX = ["ap_rank"]


def evaluate(params):
    """The case's own graded primary metric: AP poll rank vs. the No. 16
    cutoff. A = cutoff_rank - ap_rank (positive = clears the cutoff, i.e.
    'yea'). B = 0, the floor at exactly the cutoff line."""
    p = dict(PARAMS)
    p.update(params or {})
    return {"A": p["cutoff_rank"] - p["ap_rank"], "B": 0}


def evaluate_twist(params):
    """FACILITATOR.md's Twist: the real, corroborating NET ranking, checked
    against the same cutoff. Not a hypothetical parameter change -- a second
    real data point that either confirms or contradicts evaluate()'s verdict."""
    p = dict(PARAMS)
    p.update(params or {})
    return {"A": p["cutoff_rank"] - p["net_rank"], "B": 0}


def margins(params=None):
    """Reporting helper -- all three real rankings against the cutoff, for
    cross-checking against case.json.derived. Not used by evaluate()/
    evaluate_twist() -- MCS-26's contract needs exactly two named metrics,
    this gives the fuller picture for a human reader."""
    p = dict(PARAMS)
    p.update(params or {})
    cutoff = p["cutoff_rank"]
    return {
        "ap_spots_to_spare": cutoff - p["ap_rank"],
        "ap_margin_pct_of_cutoff": round(100 * (cutoff - p["ap_rank"]) / cutoff, 2),
        "net_spots_to_spare": cutoff - p["net_rank"],
        "net_margin_pct_of_cutoff": round(100 * (cutoff - p["net_rank"]) / cutoff, 2),
        "win_pct_only_rank": p["win_pct_only_rank"],
        "win_pct_only_verdict": "nay (well outside)" if p["win_pct_only_rank"] > cutoff else "yea",
    }


if __name__ == '__main__':
    print("margins (base params):", margins())

    print("\nverdict check (evaluate / evaluate_twist) -- A=spots to spare, B=0 floor:")
    base, tw = evaluate({}), evaluate_twist({})
    print(f"  AP  (evaluate)       A={base['A']}  B={base['B']}  "
          f"verdict={'yea' if base['A'] > base['B'] else 'nay'}  "
          f"margin_pct={100*base['A']/PARAMS['cutoff_rank']:.2f}% (case.json margin_pct: 6.25%)")
    print(f"  NET (evaluate_twist) A={tw['A']}  B={tw['B']}  "
          f"verdict={'yea' if tw['A'] > tw['B'] else 'nay'}  "
          f"margin_pct={100*tw['A']/PARAMS['cutoff_rank']:.2f}%")

    print("\nFLEX sweep, ap_rank (base 15) -- where does the real-data verdict flip?")
    for r in (13, 14, 15, 16, 17, 18):
        a = PARAMS["cutoff_rank"] - r
        print(f"  ap_rank={r:2d}  spots_to_spare={a:+d}  "
              f"{'YEA' if a > 0 else ('TIE at the line' if a == 0 else 'NAY')}")
    print("  -> the real, cited ap_rank=15 sits only 2 spots from where the case's")
    print("     own verdict would flip (ap_rank=17) -- a genuinely close, real margin.")

    print("\nFLEX sweep, net_rank (base 12):")
    for r in (10, 11, 12, 15, 16, 17):
        a = PARAMS["cutoff_rank"] - r
        print(f"  net_rank={r:2d}  spots_to_spare={a:+d}  "
              f"{'YEA' if a > 0 else ('TIE at the line' if a == 0 else 'NAY')}")

    print("\nTrap check -- win_pct_only_rank (real, computed, ignores schedule strength):")
    m = margins()
    print(f"  win_pct_only_rank={m['win_pct_only_rank']} of {PARAMS['win_pct_field_size']}  "
          f"-> {m['win_pct_only_verdict']} (vs. cutoff_rank={PARAMS['cutoff_rank']})")
