"""
sensitivity_model.py — Gerrymandering

Graded primary metric (case.json.primary_metric): absolute value of the projected
statewide efficiency gap (%) on the 3-district map, computed under Modeling
Assumption MA2 (every region's two-party vote share is assumed equal to Idaho's
real, sourced statewide two-party vote share). Lower |efficiency gap| is fairer,
so evaluate() returns the NEGATIVE of |efficiency gap| for each plan -- higher
score = better, matching this script's "higher wins" convention.

Why this is a TIE by disclosed design (see case.json.balance.margin_basis and
RESEARCH_LOG.md): under MA2, every region shares the identical statewide 2-party
vote split. The wasted-vote share in any single-winner district is always exactly
50% of that district's votes (half the votes are "wasted" for a fixed win
percentage, regardless of the district's population size -- see the derivation in
Appendix E's methodology). Because efficiency gap is normalized by total votes,
this makes the projected efficiency gap identical for Plan A and Plan B: it is
driven entirely by vote SHARE (fixed, uniform across regions by MA2), not by how
population is grouped into districts. This is the intended real finding, not a
degenerate model -- see FACILITATOR.md's Twist.

Population-balance (D1) and compactness (D2) are the two metrics that DO
discriminate sharply between the plans in real, computed, opposite directions --
they are deliberately NOT the graded primary metric (see RESEARCH_LOG.md's "note
on the primary metric" for why: the real 2020 Census numbers make Plan A's
population deviation a fixed, unavoidable +18.44%, which is not something any
redesign of the non-Treasure-Valley regions can close, so it cannot serve as a
SPEC §2 close-margin primary metric without either fabricating numbers or hiding
the real finding -- neither is permitted). Their real numbers are surfaced to
students honestly through Challenge deliverables D1/D2, not through this model.
"""

PARAMS = {
    # Real, sourced 2020 Census populations (S5) -- NOT flexed by default; these
    # are cited data, not case-authored assumptions.
    "tv_population": 726072,
    "west_population": 569068,   # North & West-Central Idaho, 22 counties
    "east_population": 543966,   # South-Central & East Idaho, 20 counties

    # Real, sourced 2020 statewide two-party vote totals (S12, S13).
    "statewide_r_votes": 561405,
    "statewide_d_votes": 255531,

    # MA1 -- the Plan B population-share split derived to bring West and East to
    # the statewide ideal (case.md Appendix F / Modeling Assumptions). This is a
    # case-authored assumption about WHERE the dividing line falls, not a cited
    # figure -- flex it.
    "planB_west_share_of_tv": 0.06055,   # ~43,967 / 726,072
    "planB_east_share_of_tv": 0.09514,   # ~69,069 / 726,072

    # MA2 -- every region's two-party vote share is assumed equal to the real
    # statewide two-party split, rather than a sourced county-level split.
    # This is the load-bearing case-authored assumption -- flex it.
    "statewide_r_share": 561405 / (561405 + 255531),
}

# Only the two disclosed Modeling Assumptions are swept by default (SPEC §2 asks
# for sensitivity to STATED ASSUMPTIONS, not to the cited 2020 Census/election
# data itself -- see the "Only FLEX[] is swept" rule in skills/case-readiness).
FLEX = ["planB_west_share_of_tv", "planB_east_share_of_tv", "statewide_r_share"]


def _efficiency_gap_pct(r_share):
    """Every single-winner district under a uniform r_share wastes exactly 50%
    of its votes combined (winner wastes votes above 50%, loser wastes all of
    theirs) -- so the statewide efficiency gap under a uniform vote share is
    driven only by r_share, not by district population size or count."""
    d_share = 1.0 - r_share
    r_wasted = max(0.0, r_share - 0.5)
    d_wasted = d_share if r_share >= 0.5 else max(0.0, d_share - 0.5)
    # Signed gap (favor-R positive); magnitude is what the case grades.
    return abs(d_wasted - r_wasted) * 100.0


def evaluate(params):
    """Both plans use the SAME statewide-uniform vote share (MA2) applied to
    every region regardless of population -- so under this assumption Plan A's
    and Plan B's projected efficiency gap are mathematically identical. The
    planB_*_share_of_tv params (MA1) determine POPULATION distribution, not vote
    SHARE, so they do not move this metric either -- a real, disclosed, and
    intentional insensitivity, not a bug. See the module docstring."""
    eg = _efficiency_gap_pct(params["statewide_r_share"])
    # higher score = better = lower |efficiency gap|
    return {"A": -eg, "B": -eg}


if __name__ == "__main__":
    base = evaluate(PARAMS)
    print("base:", base, "-- expected an exact tie by disclosed design (MA2)")
    for name in FLEX:
        for mult in (0.5, 1.5):
            p = dict(PARAMS)
            p[name] = PARAMS[name] * mult
            r = evaluate(p)
            print(f"{name} x{mult}: {r}")
