#!/usr/bin/env python3
"""
TIER 2 — SIMULATED PLAY  (machine + model, blocking)

Seven probes.  P1-P6 are modelled on the HIGH GRADE murder-mystery kit's six
simulated-play probes, which is also the kit that proves why Tier 2 is not
enough: it passed all thirteen structural checks and all six probes and still
failed live. P7 (MCS-48) is new: P1-P6 test mathematical/sourcing soundness
for a capable, patient reader -- none of them test whether a reader with ZERO
background in the case's real-world SETTING can follow it at all.

    python3 skills/case-readiness/scripts/tier2_probes.py --case cold-chain
    python3 skills/case-readiness/scripts/tier2_probes.py --case cold-chain --probe 5
    python3 skills/case-readiness/scripts/tier2_probes.py --case cold-chain --json t2.json

WHAT THIS SCRIPT DOES AND DOES NOT DO
  P1 cold solve        -> builds the packet, proves it is leak-free, PRINTS THE PROMPT.
                          The solve itself must be run by a FRESH SUBAGENT.  A script
                          cannot be naive about a case it just parsed.
  P2 both-sides solve  -> prints the prompt.  Model work.
  P3 trap check        -> machine pre-screen + prints the prompt.
  P4 twist integrity   -> machine recomputation when a sensitivity model exists,
                          plus the prompt.
  P5 assumption flex   -> FULLY MACHINE.  Runs only if the case ships a model.
                          No model => NOT RUN, which is a real answer, not a pass.
  P6 data decay        -> emits the fetch worklist + source ages.  The fetch itself
                          is delegated (the QA sandbox has no outbound network).
  P7 accessibility     -> machine pre-screen (sketch/graph deliverables vs real
                          visuals) + PRINTS THE PROMPT for a fresh, zero-context
                          subagent cold-read of real-world (non-math) vocabulary.

Exit 0 = every probe that CAN run mechanically passed.  Exit 1 = a mechanical probe
failed.  Exit 2 = probes are pending model/subagent adjudication.  Tier 2 is not
clean until every probe verdict is recorded in QA_REPORT.md by name.
"""
import argparse, importlib.util, itertools, json, os, re, sys, datetime

PROBES = {
    1: "cold-solve",
    2: "both-sides-solve",
    3: "trap-check",
    4: "twist-integrity",
    5: "assumption-sensitivity",
    6: "data-decay",
    7: "accessibility-cold-read",
}


def load_model(path):
    spec = importlib.util.spec_from_file_location("sensmodel", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    for attr in ("PARAMS", "evaluate"):
        if not hasattr(m, attr):
            raise AttributeError(f"{path} must define {attr}")
    return m


# ---------------------------------------------------------------- probe 1 ----
def probe_cold_solve(project, cid, c, md, fac, out):
    """Build the student-facing packet and prove it leaks nothing."""
    pkt_dir = os.path.join('/tmp', f'coldsolve-{cid}')
    os.makedirs(pkt_dir, exist_ok=True)
    pkt = os.path.join(pkt_dir, 'PACKET.md')
    open(pkt, 'w', encoding='utf-8').write(md)

    # leak test: no answer-bearing string from FACILITATOR.md may appear in the packet
    leaks = []
    if fac:
        # every number the guide teaches as a RESULT must not be pre-computed in the packet
        bal = c.get('balance') or c.get('balance_test') or {}
        for k in ('A_in_spec_doses', 'B_in_spec_doses', 'margin_pct'):
            v = bal.get(k)
            if v is None:
                continue
            # Same fix as tier1_structural.py's T1-18 (2026-08-13): margin_pct is inherently
            # a percent/points figure. A small round value (1, 5, 10...) collides constantly
            # with unrelated case vocabulary -- appendix/step numbers, dose counts, "Option 1"
            # -- that share nothing with the balance verdict except being the same small
            # integer. Require a nearby %/point unit for margin_pct specifically; other keys
            # keep the original bare-token match.
            require_unit = (k == 'margin_pct')
            found = False
            for form in (f"{v:,}", str(v), str(int(v)) if float(v).is_integer() else str(v)):
                pat = r'(?<![\w.])' + re.escape(form) + r'(?![\w-])'
                for m in re.finditer(pat, md):
                    if require_unit:
                        window = md[m.end():m.end() + 15]
                        if not re.search(r'\s*%|\s*point', window, re.I):
                            continue
                    found = True
                    break
                if found:
                    break
            if found:
                leaks.append(f"balance_test.{k} = {v} appears in the packet; the solver is handed "
                             f"the answer")
        # The twist must not be pre-disclosed.  Shingle test, not word overlap:
        # a twist about Nyamirama will always say "Nyamirama", and the village is
        # legitimately in Appendix C.  What must NOT appear is the twist's own
        # phrasing.
        tw = (c.get('facilitator') or {}).get('twist') or ''
        if tw:
            def toks(t):
                return re.findall(r'[a-z0-9]+', t.lower())
            mt, tt = toks(md), toks(tw)
            mdset = {tuple(mt[i:i + 6]) for i in range(max(0, len(mt) - 5))}
            hits = [' '.join(tt[i:i + 6]) for i in range(max(0, len(tt) - 5))
                    if tuple(tt[i:i + 6]) in mdset]
            if hits:
                leaks.append(f"twist is pre-disclosed in case.md — shared phrasing: {hits[:3]}")
        # no facilitator section heading may have been pasted into the packet
        for h in re.findall(r'(?m)^#{1,3}\s+(.{3,60})$', fac):
            hh = h.strip().rstrip(' —-')
            if len(hh) > 12 and hh in md:
                leaks.append(f"FACILITATOR.md heading {hh!r} appears in the student packet")
    status = 'FAIL' if leaks else 'READY'
    out.append({
        "probe": 1, "name": PROBES[1], "machine_status": status, "leaks": leaks,
        "packet": pkt,
        "prompt": (
            f"You are a fresh solver. You have never seen this case, its guide notes, or any "
            f"discussion of it. Read ONLY {pkt}. Do not read any other file in the project.\n\n"
            f"Work the case as a student would. Then answer, in order:\n"
            f"  1. Which option do you choose, A or B?\n"
            f"  2. What metric did you optimise, and why that metric?\n"
            f"  3. Show the arithmetic that got you there.\n"
            f"  4. What is the strongest argument against your choice?\n"
            f"  5. Which stated assumption is your answer most sensitive to?\n"
            f"  6. Name one thing in the appendices you decided to IGNORE, and why.\n"
            f"  7. Which single number in this case felt least supported?\n\n"
            f"PASS CRITERIA for the probe (do not show these to the solver): the solver reaches a "
            f"defensible position with correct arithmetic AND names a metric. Reaching the "
            f"'right' answer by the wrong route is a FAIL, not a pass — that is the whole point "
            f"of a cold solve."),
    })


# ---------------------------------------------------------------- probe 2 ----
def probe_both_sides(project, cid, c, md, out):
    bal = c.get('balance') or c.get('balance_test') or {}
    opts = c.get('options') or {}
    machine = []
    for k, arg in (('A', bal.get('argument_A') or bal.get('argument_a')),
                   ('B', bal.get('argument_B') or bal.get('argument_b'))):
        if not arg:
            machine.append(f"no written argument for option {k}")
            continue
        if len(re.findall(r'\d', arg)) < 3:
            machine.append(f"argument {k} carries almost no numbers — SPEC §2 asks for the "
                           f"strongest QUANTITATIVE argument")
        # a concession-only argument is the classic fake balance
        if re.search(r'(?i)\bbut\b.*\b(worse|only|fails|abandons|loses)\b', arg) and \
           not re.search(r'(?i)\b(cheaper|more|better|higher|lower|superior|zero)\b', arg):
            machine.append(f"argument {k} reads as a concession, not a case")
    out.append({
        "probe": 2, "name": PROBES[2], "machine_status": 'FAIL' if machine else 'READY',
        "findings": machine,
        "prompt": (
            f"Build the strongest defensible case for EACH option, independently, using only "
            f"the case document. Then answer:\n"
            f"  - Can a competent student defend option A in front of peers? What is the single "
            f"best sentence for A?\n"
            f"  - The same for B.\n"
            f"  - Which side collapses first under pressure, and at what question?\n"
            f"If either side collapses, the recorded margin of "
            f"{c.get('margin_pct')}% is a paper number and the balance test has not really been "
            f"passed.\n"
            f"Options: A = {opts.get('A')!r}  ·  B = {opts.get('B')!r}"),
    })


# ---------------------------------------------------------------- probe 3 ----
def probe_trap(project, cid, c, fac, out):
    machine = []
    trap_txt = ''
    if not fac:
        machine.append("no FACILITATOR.md — the trap cannot be named")
    else:
        m = re.search(r'(?i)(the )?\btrap\b[^.\n]*[:.\n](.{0,400})', fac, re.S)
        if not m:
            machine.append("MCS-24 — FACILITATOR.md never names a trap. A case with no plausible "
                           "wrong path has no discussion in it.")
        else:
            trap_txt = re.sub(r'\s+', ' ', m.group(0))[:400]
            # a trap must describe a WRONG PATH, not merely a hard bit. Verb forms need their
            # normal inflections (skip/skips/skipped, miss/misses/missed, assume/assumes/
            # assuming...) -- a bare \bskip\b does NOT match "skips" (no word boundary between
            # the 'p' and the 's', both word characters), which produced false FAILs on
            # multiple real, well-written traps in 2026-08 batches. Fixed 2026-08-18.
            if not re.search(r'(?i)\b(will|most|learners?|students?|never notice|quietly|'
                             r'assumes?|assumed|assuming|optimi[sz]es?|optimi[sz]ed|optimi[sz]ing|'
                             r'forgets?|forgot|forgetting|misses?|missed|missing|skips?|skipped|'
                             r'skipping|defaults?|defaulted|defaulting)\b', trap_txt):
                machine.append("the named trap does not describe what a learner will actually DO "
                               "wrong; it reads as a difficulty note, not a trap")
    out.append({
        "probe": 3, "name": PROBES[3], "machine_status": 'FAIL' if machine else 'READY',
        "findings": machine, "trap": trap_txt,
        "prompt": (
            "Read the case document only. Name the most plausible WRONG path — the analysis a "
            "competent, hurried student would produce that looks right and is not. Then read the "
            "Guide Notes and answer:\n"
            "  - Does the guide name that same path?\n"
            "  - If the guide names a different trap, which one will actually catch the room?\n"
            "A trap the guide has not anticipated is a Tier 2 FAIL even if the case is otherwise "
            "sound, because the guide will not be watching for it."),
    })


# ---------------------------------------------------------------- probe 4 ----
def probe_twist(project, cid, c, fac, model, out):
    machine, computed = [], {}
    f = c.get('facilitator') or {}
    twist = f.get('twist')
    if not twist:
        if not re.search(r'(?im)^#+.*twist', fac or ''):
            machine.append("MCS-15 — no twist authored and no justified N/A")
    else:
        bal = c.get('balance') or c.get('balance_test') or {}
        eff = bal.get('twist_effect') or ''
        if not eff:
            machine.append("twist is authored but balance_test.twist_effect is empty — nobody has "
                           "written down what it changes, so nobody has checked that it changes "
                           "anything")
        if model is not None and hasattr(model, 'evaluate_twist'):
            base = model.evaluate(dict(model.PARAMS))
            tw = model.evaluate_twist(dict(model.PARAMS))
            computed = {"base": base, "twist": tw}
            b_win = max(base, key=base.get)
            t_win = max(tw, key=tw.get)
            if b_win == t_win and abs(base[b_win] - base[min(base, key=base.get)]) <= \
                                  abs(tw[t_win] - tw[min(tw, key=tw.get)]):
                machine.append(f"the twist does not invalidate any position: {b_win} wins before "
                               f"({base}) and after ({tw}), by no smaller a margin")
    out.append({
        "probe": 4, "name": PROBES[4], "machine_status": 'FAIL' if machine else 'READY',
        "findings": machine, "computed": computed, "twist": twist,
        "prompt": (
            "Two questions, and the second is the one that gets skipped:\n"
            "  1. Does the twist invalidate at least one position a real room would hold?\n"
            "  2. Does the twist survive the case's OWN stated assumptions — read the assumptions "
            "the most natural way a student would read them, not the way the author intended?\n"
            "Cold Chain's twist originally failed (2) — under a sequential reading of Assumption 1 "
            "the twist did nothing at all, and the case shipped that way until an adversarial pass "
            "caught it. Re-derive the twist's effect under EVERY defensible reading of every stated "
            "assumption, and under the case's own stated capacity limits. If the effect depends on "
            "a convention the case never states, that is a BLOCKER."),
    })


# ---------------------------------------------------------------- probe 5 ----
def probe_sensitivity(project, cid, c, model, flex, out, flex_all=False):
    if model is None:
        out.append({
            "probe": 5, "name": PROBES[5], "machine_status": 'NOT RUN',
            "findings": [
                "MCS-26 — the case ships no sensitivity model, so 'flex each assumption by "
                f"±{int(flex*100)}%' cannot be executed. NOT RUN is the honest state; it is not a "
                "pass. Author cases/<id>/sensitivity_model.py exposing PARAMS and "
                "evaluate(params) -> {'A': metric, 'B': metric}. See "
                "skills/case-readiness/scripts/example_sensitivity_model.py."],
            "table": []})
        return

    base = model.evaluate(dict(model.PARAMS))
    base_win = max(base, key=base.get)
    base_lo = min(base, key=base.get)
    denom = base[base_lo] or 1
    base_margin = 100.0 * (base[base_win] - base[base_lo]) / denom
    # base_state, not base_win, is the correct reference point for "did the flex
    # flip the verdict": a case whose graded metric is a designed TIE (margin
    # 0 by construction, e.g. Payroll) has no real winner to flip away from --
    # base_win is just an arbitrary dict-ordering artifact of max() on equal
    # values. See T1-10-style fix note below.
    base_state = base_win if base[base_win] != base[base_lo] else "TIE"
    # Documented caveat (added 2026-08-13, not a code rewrite): margin_pct is
    # 100*(winner-loser)/loser, with a `or 1` fallback when the loser is exactly
    # 0. For a metric shape pinned to a fixed zero floor (e.g. a case whose
    # evaluate() always returns B=0 by construction, such as a rank-vs-cutoff
    # comparison), this formula does not compute a real percentage of anything
    # -- it is the raw winner value x100, and can read as an arbitrarily large
    # or small "%" that has nothing to do with real-world margin size. The
    # underlying finding (how thin the raw gap is) can still be real; the
    # percent figure and any 20%-cap breach derived from it should be read with
    # that in mind, not taken as a literal percentage margin.
    zero_baseline_caveat = (
        "CAVEAT: base_winner's opposing value is exactly 0, so margin_pct below is "
        "NOT a true percentage (it reduces to 100x the raw winning value via the /1 "
        "fallback). This usually means the metric has a fixed zero floor by "
        "construction (e.g. a rank-vs-cutoff comparison) rather than being a ratio-"
        "like quantity (dollars, probability). Read any 'breaks the 20% cap' finding "
        "below as evidence the raw gap is small in absolute terms, not as a literal "
        "percentage-margin fact."
    ) if base[base_lo] == 0 else None

    # SPEC §2 asks for sensitivity to STATED ASSUMPTIONS.  A model may narrow the
    # sweep with FLEX = [...]; without one, everything is swept and the report
    # says so, because silently flexing cited data produces theatre.
    sweep = getattr(model, 'FLEX', None) if not flex_all else None
    if sweep is None:
        sweep = list(model.PARAMS)
        scope_note = ("model declares no FLEX[] — every parameter was swept, including cited "
                      "measurements. Halving a WHO-rated figure is a different case, not a "
                      "sensitivity test; declare FLEX[] to scope this honestly.")
    else:
        scope_note = f"swept the {len(sweep)} declared assumption dial(s): {sweep}"

    rows, flips, unbalanced = [], [], []
    for name in sweep:
        val = model.PARAMS[name]
        if not isinstance(val, (int, float)) or isinstance(val, bool):
            rows.append({"param": name, "note": "non-numeric — flex by hand", "base": val})
            continue
        for direction, mult in (("-%d%%" % (flex * 100), 1 - flex), ("+%d%%" % (flex * 100), 1 + flex)):
            p = dict(model.PARAMS)
            p[name] = val * mult
            try:
                r = model.evaluate(p)
            except Exception as e:                      # a model that dies IS a finding
                rows.append({"param": name, "flex": direction, "error": repr(e)})
                continue
            win = max(r, key=r.get)
            lo = min(r, key=r.get)
            d = r[lo] or 1
            margin = 100.0 * (r[win] - r[lo]) / d
            new_state = win if r[win] != r[lo] else "TIE"
            row = {"param": name, "flex": direction, "value": round(val * mult, 6),
                   "result": {k: round(v, 2) for k, v in r.items()},
                   "winner": new_state,
                   "margin_pct": round(margin, 1),
                   # FIXED 2026-08-13 (real defect, not a per-case workaround): the
                   # old condition `... or (r[win] == r[lo])` flagged ANY resulting
                   # tie as a "flip", even when the base case was ALREADY a tie
                   # (e.g. a case whose graded primary_metric is intentionally
                   # margin_pct=0 by design). Going tie -> tie is not a flip by any
                   # definition. A flip is now defined relative to the actual base
                   # STATE (which may itself be "TIE"), not the arbitrary dict-order
                   # winner max() picks when base is tied.
                   "flips": new_state != base_state,
                   "breaks_20pct_cap": margin > 20}
            rows.append(row)
            if row["flips"]:
                flips.append(f"{name} {direction} -> winner {row['winner']} (base {base_state})")
            if row["breaks_20pct_cap"]:
                unbalanced.append(f"{name} {direction} -> margin {row['margin_pct']}% breaks the "
                                  f"SPEC §2 20% cap")
    findings = []
    if flips:
        findings.append("VERDICT UNSTABLE under a ±%d%% assumption swing: %s. SPEC §2 does not "
                        "forbid this, but the case MUST say so — in the Guide Notes and in "
                        "balance_test — or the guide will defend a margin that does not exist."
                        % (flex * 100, "; ".join(flips)))
    if unbalanced:
        findings.append("BALANCE BREAKS under flex: " + "; ".join(unbalanced))
    if zero_baseline_caveat:
        findings.append(zero_baseline_caveat)

    # ---- disclosure-aware pass state (added 2026-08-13, project-owner approved) ----
    # Resolves an open design question this project's own maintainers had left
    # unresolved (see DOCTRINE_LEDGER.md MCS-26/41): can a genuinely unstable P5
    # ever pass if it's disclosed? Yes, but narrowly, and only if the disclosure
    # is structured and machine-checkable -- prose buried in a Guide Notes file
    # is not a clearance any more than an unrecorded Overview-numeral clearance
    # is (same "a clearance not written down is not a clearance" rule this
    # skill already applies elsewhere). Every param this run found unstable
    # (flips the verdict or breaks the 20% cap) must have a matching entry in
    # case.json's top-level `sensitivity_disclosure[]`:
    #   {"param": "<name>", "category": "F"|"X"|"I", "justification": "<1+ sentence>"}
    # Category F = forecast/irreducible-unknown: the true value cannot be known
    #   in advance by ANY amount of research (a future price, a future outcome).
    # Category X = proprietary/inaccessible, one-time exception: the true value
    #   exists and is knowable in principle but not publicly accessible, and a
    #   documented good-faith estimate was made from the closest public
    #   analogue. Flag every use of Category X in the finding so it stays
    #   visible as an exception, not a template for skipping research.
    # Category I = interpolation: the value is computed from a validated
    #   mathematical/physical/statistical relationship (a real formula, scaling
    #   law, or trend) applied WITHIN the range that relationship is actually
    #   tested/documented over -- not extrapolated past known data. This is the
    #   strongest of the three (a real calculation, not a guess) but distinct
    #   from a flat citation because the number is derived, not directly
    #   quoted. The justification must name the formula/method AND state that
    #   the applied range is interpolation, not extrapolation -- a category-I
    #   claim that is actually extrapolating past validated data does not
    #   qualify (re-tag as F or X, or find a source that actually covers the
    #   range used).
    # What does NOT qualify, regardless of what's written in the disclosure list:
    #   - no model at all (NOT RUN, handled above, never reaches this code)
    #   - a flip caused by cited/given data sitting in FLEX[] by a scoping
    #     error -- that's a bug in the model, not a real instability, and
    #     rescoping FLEX[] is the actual fix (see the FLEX-scoping doctrine
    #     note above), not a disclosure entry
    #   - an unstable param with no matching entry, or an entry missing a
    #     category or a real justification (a blank or generic "may vary"
    #     justification is not a justification)
    unstable_params = sorted({row["param"] for row in rows
                               if row.get("flips") or row.get("breaks_20pct_cap")})
    disclosure = c.get("sensitivity_disclosure", []) if isinstance(c, dict) else []
    disclosed_by_param = {}
    for entry in disclosure:
        if not isinstance(entry, dict):
            continue
        pname = entry.get("param")
        cat = entry.get("category")
        just = (entry.get("justification") or "").strip()
        if pname and cat in ("F", "X", "I") and len(just) >= 20:
            disclosed_by_param[pname] = entry

    machine_status = 'PASS'
    if unstable_params:
        undisclosed = [p for p in unstable_params if p not in disclosed_by_param]
        if undisclosed:
            machine_status = 'FAIL'
            findings.append(
                "UNDISCLOSED instability: " + ", ".join(undisclosed) + " — flips the verdict or "
                "breaks the 20% cap with no matching case.json.sensitivity_disclosure[] entry "
                "(needs param/category F-or-X-or-I/a real justification of 20+ chars). Not a pass "
                "until every unstable param is either disclosed this way or the case is retuned.")
        else:
            machine_status = 'PASS (disclosed)'
            cat_x = [p for p in unstable_params if disclosed_by_param[p]["category"] == "X"]
            cat_i = [p for p in unstable_params if disclosed_by_param[p]["category"] == "I"]
            findings.append(
                f"DISCLOSED, NOT ELIMINATED: {', '.join(unstable_params)} — each has a recorded "
                f"category and justification in sensitivity_disclosure[]. This PASSES per the "
                f"disclosure-aware pass state (2026-08-13), not the stable-margin state."
                + (f" NOTE: {', '.join(cat_x)} used the Category-X proprietary-estimate exception "
                   f"— a best-effort estimate from a public analogue, not a real citation for the "
                   f"actual quantity. Confirm this is still a genuine one-time exception, not a "
                   f"substitute for real sourcing." if cat_x else "")
                + (f" NOTE: {', '.join(cat_i)} used Category-I interpolation — confirm the "
                   f"justification actually names the formula/method and that the applied range is "
                   f"interpolation within tested data, not extrapolation past it." if cat_i else ""))

    out.append({"probe": 5, "name": PROBES[5],
                "machine_status": machine_status,
                "scope": scope_note,
                "base": {k: round(v, 2) for k, v in base.items()},
                "base_winner": base_win, "base_margin_pct": round(base_margin, 1),
                "unstable_params": unstable_params,
                "findings": findings, "table": rows,
                "params": {k: v for k, v in model.PARAMS.items()}})


# ---------------------------------------------------------------- probe 6 ----
def probe_decay(project, cid, c, out, today=None):
    today = today or datetime.date.today()
    work, stale = [], []
    for s in c.get('sources', []):
        acc = s.get('accessed')
        age = None
        try:
            age = (today - datetime.date.fromisoformat(acc)).days
        except Exception:
            pass
        rec = {"id": s.get('id'), "url": s.get('url'), "accessed": acc, "age_days": age,
               "confidence": s.get('confidence'), "claim": (s.get('claim') or '')[:90],
               "value": s.get('value')}
        work.append(rec)
        if age is not None and age > 365:
            stale.append(f"{s.get('id')} last verified {age} days ago")
    # dated figures inside the case that will need refresh
    dated = sorted(set(re.findall(r'\b(19|20)\d\d\b', json.dumps(c.get('sources', [])))))
    out.append({
        "probe": 6, "name": PROBES[6], "machine_status": 'DELEGATED',
        "findings": stale, "worklist": work,
        "prompt": (
            "The QA sandbox has no outbound network, so this probe is delegated. For EACH url in "
            "the worklist: fetch it, and report (a) HTTP reachable yes/no, (b) whether the "
            "recorded `value` still appears on the page, (c) if the page moved, the new URL. "
            "A url that 404s while its figure is load-bearing is a BLOCKER; a url that resolves "
            "but no longer carries the figure is worse, because nothing in the pipeline would "
            "ever have noticed. Report NOT FOUND rather than guessing — MCS-21 makes a fabricated "
            "URL the worst failure available."),
    })


# ---------------------------------------------------------------- probe 7 ----
# Neither Tier 1 nor probes P1-P6 test whether a reader with ZERO background in
# the case's real-world SETTING (not its math) can follow the story well enough
# to do the work -- Tier 1's T1-21 checks that a story glossary MECHANISM
# exists and clears a term-count floor, and P1-P6 test mathematical/sourcing
# soundness for a capable, patient reader who already knows what a "claim
# file" or a "speed square" is. A deep human review of five already-published,
# genuinely TIER2_PASS cases (apron-order, field-watch, roofline-call,
# feedback, curves-turn) found real, substantive accessibility gaps in every
# one anyway -- unexplained domain vocabulary and missing diagrams for a
# Challenge that explicitly asks a student to sketch/graph something hard to
# picture. MCS-48 makes this a real, gated probe rather than a chance "polish"
# pass. Two independent checks, same two-stage shape as probe_trap (P3):
#   (a) mechanical pre-screen -- does every deliverable that asks a student to
#       sketch/draw/graph/plot/diagram something have a real visual (an <img>
#       with a non-placeholder src, or an inline <svg> with actual shape
#       content) anywhere in the published Interactive HTML? A student asked
#       to produce a diagram they were never shown a comparable example of is
#       a real, mechanically-checkable gap.
#   (b) model-judged cold-read -- a genuinely fresh subagent, told nothing
#       about the setting, reads the student packet and lists every
#       real-world (non-math) term or concept it could not picture well
#       enough to proceed. 2+ such findings is a FAIL regardless of whether
#       T1-21 mechanically passed, because T1-21 only proves a glossary
#       MECHANISM exists and clears a floor -- not that coverage is complete.
VISUAL_KEYWORD_RE = re.compile(r'\b(sketch|diagram|graph of|draw|plot)\w*\b', re.I)


def probe_accessibility(project, cid, c, md, out):
    cdir = os.path.join(project, 'cases', cid)
    pub = os.path.join(cdir, 'published')

    # ---- (a) mechanical pre-screen: sketch/graph deliverables vs real visuals ----
    matched = [d.get('id') for d in (c.get('deliverables') or [])
               if VISUAL_KEYWORD_RE.search(d.get('text') or '')]

    n_visuals = 0
    if os.path.isdir(pub):
        for fn in os.listdir(pub):
            if not fn.lower().endswith('.html'):
                continue
            txt = open(os.path.join(pub, fn), encoding='utf-8', errors='ignore').read()
            body_only = re.sub(r'(?is)<script.*?</script>|<style.*?</style>', ' ', txt)
            imgs = re.findall(r'<img\b[^>]*\bsrc=["\']([^"\']+)["\']', body_only)
            real_imgs = [s for s in imgs if s and 'placeholder' not in s.lower()
                        and not s.strip().startswith('data:image/gif;base64,R0lGOD')]
            n_visuals += len(real_imgs)
            svg_blocks = re.findall(r'(?is)<svg\b[^>]*>(.*?)</svg>', txt)
            n_visuals += sum(1 for blk in svg_blocks
                             if re.search(r'(?is)<(path|circle|rect|line|polygon|polyline|ellipse)\b', blk))

    machine = []
    if matched and n_visuals == 0:
        machine.append(f"MCS-48 — deliverable(s) {matched} ask for a sketch/diagram/graph/drawing/"
                       f"plot, and published/ has NO real visual (no <img> with a real src, no "
                       f"<svg> with actual shape content) anywhere. A student asked to produce a "
                       f"diagram was never shown a comparable example -- this is a real, mechanical "
                       f"gap distinct from the qualitative cold-read below.")
    elif matched and n_visuals < len(matched):
        machine.append(f"MCS-48 — {len(matched)} deliverable(s) ask for a sketch/diagram/graph/"
                       f"drawing/plot ({matched}) but only {n_visuals} real visual(s) were found in "
                       f"published/ HTML. Mechanical count only -- a human should confirm each "
                       f"listed deliverable actually has its own comparable worked example, not "
                       f"just that SOME visual exists somewhere in the file.")

    # ---- (b) model-judged cold-read: dispatch a genuinely fresh subagent ----
    pkt_dir = os.path.join('/tmp', f'coldsolve-{cid}')
    os.makedirs(pkt_dir, exist_ok=True)
    pkt = os.path.join(pkt_dir, 'PACKET.md')
    open(pkt, 'w', encoding='utf-8').write(md)

    setting = (c.get('protagonist') or c.get('title') or cid)
    metric = c.get('primary_metric') or ''

    out.append({
        "probe": 7, "name": PROBES[7],
        "machine_status": 'FAIL' if any('NO real visual' in m for m in machine) else 'READY',
        "findings": machine,
        "matched_deliverables": matched, "n_visuals_found": n_visuals,
        "packet": pkt,
        "prompt": (
            f"Dispatch a genuinely fresh subagent with ZERO extra context. Give it the packet path "
            f"({pkt}) and this exact instruction:\n\n"
            f"  'You have no background in {setting}"
            f"{(' -- the real-world setting is centered on ' + metric) if metric else ''}. "
            f"Read this case as a student would. List every real-world term or concept you could "
            f"NOT picture or understand well enough to proceed, without looking anything up outside "
            f"this document.'\n\n"
            f"PASS CRITERIA (do not show these to the subagent): a finding that names 2 or more "
            f"genuinely unexplained real-world (non-math) concepts is a FAIL -- the glossary/"
            f"explanation coverage is insufficient regardless of whether Tier 1's T1-21 mechanically "
            f"passed. 0-1 named concepts is a PASS; some irreducible unfamiliarity is fine."),
    })


# ------------------------------------------------------------------ main ----
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--case', required=True)
    ap.add_argument('--project', default=os.getcwd())
    ap.add_argument('--probe', type=int, default=None, choices=sorted(PROBES))
    ap.add_argument('--model', default=None, help='path to a sensitivity model .py')
    ap.add_argument('--flex', type=float, default=0.5)
    ap.add_argument('--flex-all', action='store_true',
                    help='sweep every PARAM, not just the declared FLEX[] assumption dials')
    ap.add_argument('--json', default=None)
    a = ap.parse_args()

    cdir = os.path.join(a.project, 'cases', a.case)
    md_raw = open(os.path.join(cdir, 'case.md'), encoding='utf-8').read()
    # The student packet is never the raw file. case-publish's own contract (SKILL.md #1a)
    # strips everything from the `<!-- FACILITATOR ONLY -->` marker onward before it reaches a
    # student; P1's leak test is meaningless against a packet that still carries the answer key,
    # so build the same stripped view here. Found via a leak-test false-negative on plaza-pavers
    # (2026-08-12), then confirmed the same defect against tide-window's already-shipped case.md.
    md = re.split(r'<!--\s*FACILITATOR ONLY\s*-->', md_raw, maxsplit=1)[0]
    c = json.load(open(os.path.join(cdir, 'case.json'), encoding='utf-8'))
    fp = os.path.join(cdir, 'FACILITATOR.md')
    fac = open(fp, encoding='utf-8').read() if os.path.exists(fp) else ''

    mpath = a.model or os.path.join(cdir, 'sensitivity_model.py')
    model = load_model(mpath) if os.path.exists(mpath) else None

    out = []
    want = [a.probe] if a.probe else sorted(PROBES)
    if 1 in want: probe_cold_solve(a.project, a.case, c, md, fac, out)
    if 2 in want: probe_both_sides(a.project, a.case, c, md, out)
    if 3 in want: probe_trap(a.project, a.case, c, fac, out)
    if 4 in want: probe_twist(a.project, a.case, c, fac, model, out)
    if 5 in want: probe_sensitivity(a.project, a.case, c, model, a.flex, out, a.flex_all)
    if 6 in want: probe_decay(a.project, a.case, c, out)
    if 7 in want: probe_accessibility(a.project, a.case, c, md, out)

    print(f"TIER 2 — SIMULATED PLAY   case: {a.case}   "
          f"model: {mpath if model else 'NONE (probe 5 cannot run)'}")
    for r in out:
        print(f"\n--- P{r['probe']} {r['name']}  [{r['machine_status']}]")
        for k in ('base', 'base_winner', 'base_margin_pct', 'scope', 'trap', 'twist', 'packet',
                  'computed', 'matched_deliverables', 'n_visuals_found'):
            if r.get(k):
                print(f"    {k}: {r[k]}")
        for f in r.get('findings', []) + r.get('leaks', []):
            print(f"    ! {f}")
        for row in r.get('table', []):
            print("    " + json.dumps(row))
        if r.get('worklist'):
            for w in r['worklist']:
                print(f"    {w['id']:>4}  age {w['age_days']}d  {w['confidence']:<6} {w['url']}")
        if r.get('prompt'):
            print("    PROMPT >>>")
            for line in r['prompt'].splitlines():
                print("      " + line)

    failed = [r['probe'] for r in out if r['machine_status'] == 'FAIL']
    pending = [r['probe'] for r in out if r['machine_status'] in ('READY', 'DELEGATED', 'NOT RUN')]
    print(f"\nMECHANICAL RESULT: {len(failed)} probe(s) FAILED mechanically -> {failed or '-'}")
    print(f"PENDING adjudication (subagent / fetch / missing model): {pending or '-'}")
    print("Tier 2 is NOT clean until all seven verdicts are written into QA_REPORT.md by name.")
    if a.json:
        json.dump({"case": a.case, "probes": out}, open(a.json, 'w'), indent=1)
    sys.exit(1 if failed else (2 if pending else 0))


if __name__ == '__main__':
    main()
