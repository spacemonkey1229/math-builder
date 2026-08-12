#!/usr/bin/env python3
"""
TIER 2 — SIMULATED PLAY  (machine + model, blocking)

Six probes.  Modelled on the HIGH GRADE murder-mystery kit's six simulated-play
probes, which is also the kit that proves why Tier 2 is not enough: it passed
all thirteen structural checks and all six probes and still failed live.

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
            for form in (f"{v:,}", str(v), str(int(v)) if float(v).is_integer() else str(v)):
                if re.search(r'(?<![\d.])' + re.escape(form) + r'(?![\d])', md):
                    leaks.append(f"balance_test.{k} = {v} appears in case.md; the solver is handed "
                                 f"the answer")
                    break
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
        m = re.search(r'(?i)(the )?trap[^.\n]*[:.\n](.{0,400})', fac, re.S)
        if not m:
            machine.append("MCS-24 — FACILITATOR.md never names a trap. A case with no plausible "
                           "wrong path has no discussion in it.")
        else:
            trap_txt = re.sub(r'\s+', ' ', m.group(0))[:400]
            # a trap must describe a WRONG PATH, not merely a hard bit
            if not re.search(r'(?i)\b(will|most|learners|students|never notice|quietly|assume|'
                             r'optimi[sz]e|forget|miss|skip|default)\b', trap_txt):
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
            row = {"param": name, "flex": direction, "value": round(val * mult, 6),
                   "result": {k: round(v, 2) for k, v in r.items()},
                   "winner": win if r[win] != r[lo] else "TIE",
                   "margin_pct": round(margin, 1),
                   "flips": (win != base_win and r[win] != r[lo]) or (r[win] == r[lo]),
                   "breaks_20pct_cap": margin > 20}
            rows.append(row)
            if row["flips"]:
                flips.append(f"{name} {direction} -> winner {row['winner']} (base {base_win})")
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
    out.append({"probe": 5, "name": PROBES[5],
                "machine_status": 'FAIL' if (flips or unbalanced) else 'PASS',
                "scope": scope_note,
                "base": {k: round(v, 2) for k, v in base.items()},
                "base_winner": base_win, "base_margin_pct": round(base_margin, 1),
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

    print(f"TIER 2 — SIMULATED PLAY   case: {a.case}   "
          f"model: {mpath if model else 'NONE (probe 5 cannot run)'}")
    for r in out:
        print(f"\n--- P{r['probe']} {r['name']}  [{r['machine_status']}]")
        for k in ('base', 'base_winner', 'base_margin_pct', 'scope', 'trap', 'twist', 'packet', 'computed'):
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
    print("Tier 2 is NOT clean until all six verdicts are written into QA_REPORT.md by name.")
    if a.json:
        json.dump({"case": a.case, "probes": out}, open(a.json, 'w'), indent=1)
    sys.exit(1 if failed else (2 if pending else 0))


if __name__ == '__main__':
    main()
