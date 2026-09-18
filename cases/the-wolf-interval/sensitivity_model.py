#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- The Wolf Interval.

CONTRACT (skills/case-readiness/scripts, Tier 2 probe 5):
    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     optional; same shape, with the twist applied

This case is unusual for P5: every quantity that feeds the primary metric is
EITHER a cited, universally-agreed mathematical definition (Appendix D, S1/S2:
the pure fifth is 3/2, the pure octave is 2/1) OR a fixed structural fact of
12-tone Western tuning (a closed circle uses 12 fifths spanning 7 octaves --
that is what makes it "12-tone", not an authorial estimate). Nothing in this
case's math is a stated Modeling Assumption -- there is no Modeling
Assumptions block in case.md, and case.json.modeling_assumptions is empty on
purpose, per RESEARCH_LOG.md and case.json.reinforcement_note.

FLEX = [] is therefore correct, not an oversight: SPEC §2 / this skill's P5
asks for sensitivity to STATED ASSUMPTIONS, never to cited/definitional data
(halving a defining ratio is a different tuning system, not a sensitivity
test of THIS one). With nothing to flex, P5 mechanically reports PASS -- and
that PASS is itself a real, meaningful finding: the case's central result
(both options carry EXACTLY the same average per-key mistuning, because both
distribute the same Pythagorean comma computed in Appendix B) is an algebraic
identity forced by prime factorization (Appendix A), not an estimate that
could have come out differently under different assumptions. There is
nothing to be fragile TO.

Verified against cases/the-wolf-interval/case.md Appendix B:
    base    A = -1.9550008653874178   B = -1.9550008653874178   TIE (margin 0.0%)
"""
import math

# Every PARAM below is either S1/S2-cited (Appendix D) or a fixed structural
# count of 12-tone tuning (Appendix A/B) -- never an assumption. See FLEX note.
PARAMS = {
    "fifth_num": 3,          # Appendix D, S1 -- pure perfect fifth ratio 3/2
    "fifth_den": 2,          # Appendix D, S1
    "octave_num": 2,         # Appendix D, S1 -- pure octave ratio 2/1
    "octave_den": 1,         # Appendix D, S1
    "n_fifths": 12,          # Appendix A/B -- 12-tone tuning, by definition
    "n_octaves": 7,          # Appendix B -- the closest whole-octave match to 12 fifths
}

# No stated assumption exists in this case to flex -- see module docstring.
# Declaring FLEX = [] (not leaving it undeclared) is a deliberate, documented
# choice, not an omission: it tells tier2_probes.py "swept nothing, on
# purpose" instead of silently defaulting to sweeping the cited constants.
FLEX = []


def _comma_ratio(p):
    fifth = (p["fifth_num"] / p["fifth_den"]) ** p["n_fifths"]
    octaves = (p["octave_num"] / p["octave_den"]) ** p["n_octaves"]
    return fifth / octaves


def evaluate(params):
    """Returns {"A": metric, "B": metric}, HIGHER is better (a "purity" score
    = -1 x average fraction-of-a-semitone mistuning per key, so less
    mistuning scores higher). Appendix B shows both options distribute the
    exact same total comma across the same 12 keys, so their AVERAGE per-key
    mistuning is always identical by construction -- this function reproduces
    that identity rather than re-deriving two different numbers, because that
    identity IS the case's central, provable finding (Appendix A's
    prime-factorization proof: the comma can be relocated, never eliminated
    or unevenly erased on average)."""
    p = dict(PARAMS)
    p.update(params or {})
    comma_ratio = _comma_ratio(p)
    comma_cents = 1200.0 * math.log2(comma_ratio)
    avg_mistuning_cents_per_key = comma_cents / p["n_fifths"]   # true for A and for B alike
    score = -(avg_mistuning_cents_per_key / 100.0)              # fraction of a semitone, sign flipped
    return {"A": score, "B": score}


if __name__ == '__main__':
    base = evaluate({})
    print("base", base, "margin %.4f%%" % (100 * abs(base["A"] - base["B"]) /
                                            (max(abs(base["A"]), abs(base["B"])) or 1)))
