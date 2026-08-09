#!/usr/bin/env python3
"""
case-reconcile — tag untagged legacy case studies against the standards spine (MCS-17/MCS-38).

Machine drafts, human promotes (MCS-12). Two modes:

  --propose
      Walk source/Y1, Y2, Y3 (EXCLUDING "Best Of Studio" -- those are student
      SUBMISSIONS of already-tagged cases, not new case sources), find every
      "Case Study_*.docx" whose extracted title is not already in
      standards_spine.json's cases[] list, and propose spine-skill matches with
      evidence. Writes readmodel/reconcile_queue.json. NEVER touches the frozen
      spine or cases_index.json.

  --confirm "<title>" [--skills id1,id2,...]
      Promote ONE case from the queue into the frozen read-model: appends the
      case title to covered_by[] for the named skills (all proposed skills if
      --skills is omitted), recomputes n, adds the case to
      standards_spine.json's cases[] list and to cases_index.json's cases[]
      array. Snapshots both files first (readmodel/_snapshots/), per MCS-22.

Matching heuristic (lexical presence, not comprehension -- every proposal
carries the sentence that triggered it, nothing is inferred from silence):

  - "term" skills (e.g. "Percent", "Ratio", "Prism"): exact word-boundary,
    case-insensitive match of the label anywhere in the case body (Overview
    through Challenges), EXCLUDING the locked Challenge boilerplate text so a
    generic instruction sentence can't manufacture a false match.

  - "how-to" skills (e.g. "How to find the volume of a prism"): strip the
    "How to " prefix, tokenize into significant words (stopwords removed),
    require ALL of them to appear in the SAME paragraph. A "volume" mention
    three paragraphs from a "prism" mention is not evidence of the procedure
    being taught; in the same paragraph, it plausibly is.

A paragraph that MENTIONS "percent" is not proof a student computed one.
That gap is exactly why every match stays PROPOSED/INTERIM until a human
runs --confirm and chooses which of the proposals to actually accept.
"""
import argparse
import difflib
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone

STOPWORDS = {"a", "an", "the", "of", "to", "and", "or", "given", "with", "at", "least",
             "one", "two", "three", "from", "its", "in", "for", "on", "by", "using",
             "that", "as", "is", "are"}

WORD_RE = re.compile(r"[A-Za-z][A-Za-z'\-]*")


def load(path):
    return json.load(open(path, encoding='utf-8'))


def dump(obj, path):
    json.dump(obj, open(path, 'w', encoding='utf-8'), indent=1)


def norm_title(t):
    t = t.strip()
    t = re.sub(r'^Case Study[:_]\s*', '', t, flags=re.I)
    t = re.sub(r'\s+', ' ', t)
    return t.strip(' .')


def norm_key(t):
    """Loose normalization for matching a candidate title against existing spine titles."""
    t = norm_title(t).lower()
    t = t.replace('’', "'")
    t = re.sub(r"[^a-z0-9 ]", '', t)
    return re.sub(r'\s+', ' ', t).strip()


def discover_docx(project):
    """Every Case Study_*.docx under source/Y1, Y2, Y3. Excludes Best Of Studio (student
    submissions, not case sources), Word lock files, and anything not a case document."""
    out = []
    for year in ('Y1', 'Y2', 'Y3'):
        base = os.path.join(project, 'source', year)
        if not os.path.isdir(base):
            continue
        for dirpath, _dirs, files in os.walk(base):
            for fn in files:
                if fn.startswith('~$'):
                    continue
                if not fn.lower().endswith('.docx'):
                    continue
                if not re.match(r'(?i)\s*case study\s*[_:\-]', fn):
                    continue
                out.append(os.path.join(dirpath, fn))
    return sorted(out)


def extract_doc(path):
    import docx
    d = docx.Document(path)
    paras = [p.text for p in d.paragraphs if p.text.strip()]
    title = norm_title(paras[0]) if paras else None
    return title, paras


def strip_boilerplate(paras, boilerplate_lines):
    bp_set = {re.sub(r'\s+', ' ', l).strip() for l in boilerplate_lines if l.strip()}
    return [p for p in paras if re.sub(r'\s+', ' ', p).strip() not in bp_set]


def _is_vocab_line(paragraph, label):
    """True if the paragraph is essentially JUST the label -- a bare vocab-list entry
    (like Cold Chain's Appendix G), not the word incidentally used in running prose."""
    stripped = re.sub(r'^[\W_]+|[\W_]+$', '', paragraph).strip()
    return len(stripped) <= len(label) + 15


def match_term(label, paras):
    """Returns (evidence_snippet, confidence) or None.
    HIGH   -- the label appears as its own bare vocab-list line (Appendix-G style).
    MEDIUM -- a multi-word label (>=2 words) found in running prose -- specific enough
              that a coincidental match is unlikely.
    LOW    -- a single generic word found only in running prose -- "Time", "Even",
              "Range", "Side", "Term" etc. are common English words as often as they
              are math vocabulary; this is presence, not evidence of use."""
    # trailing s? tolerates a plain plural ("Histograms" for the "Histogram" skill)
    # without loosening the match in any other way -- still a whole-word boundary,
    # still case-insensitive, nothing else changes.
    pat = re.compile(r'(?<![A-Za-z])' + re.escape(label) + r's?(?![A-Za-z])', re.I)
    for p in paras:
        m = pat.search(p)
        if not m:
            continue
        snippet = p[max(0, m.start() - 50): m.end() + 50].strip()
        if _is_vocab_line(p, label):
            return snippet, "HIGH"
        if len(label.split()) >= 2:
            return snippet, "MEDIUM"
        return snippet, "LOW"
    return None


def match_howto(label, paras):
    """Returns (evidence_snippet, confidence) or None. All significant content words
    of the how-to phrase must co-occur in one paragraph -- inherently more specific
    than a single-word term match, so these are never rated below MEDIUM; a bare
    vocab-list occurrence of the full how-to phrase (rare, but Cold Chain-style cases
    do this) is rated HIGH."""
    body = re.sub(r'(?i)^how to\s+', '', label)
    toks = [w.lower() for w in WORD_RE.findall(body) if w.lower() not in STOPWORDS and len(w) > 2]
    if not toks:
        return None
    for p in paras:
        pl = p.lower()
        if all(re.search(r'(?<![a-z])' + re.escape(t) + r'(?![a-z])', pl) for t in toks):
            conf = "HIGH" if _is_vocab_line(p, label) else "MEDIUM"
            return p[:200].strip(), conf
    return None


def all_skills(sp):
    out = []
    for d in sp['domains']:
        for g in d['groups']:
            for s in g['skills']:
                out.append((s['id'], s['label'], s['kind'], d['domain'], g['group']))
    return out


def propose(project):
    sp = load(os.path.join(project, 'readmodel', 'standards_spine.json'))
    bp_text = open(os.path.join(project, 'doctrine', 'CHALLENGE_BOILERPLATE.md'),
                    encoding='utf-8').read()
    bp_lines = bp_text.splitlines()

    existing_keys = {norm_key(t) for t in sp['cases']}
    skills = all_skills(sp)

    docs = discover_docx(project)
    by_title = {}
    errors = []
    for path in docs:
        try:
            title, paras = extract_doc(path)
        except Exception as e:
            errors.append(f"{path}: {e!r}")
            continue
        if not title:
            continue
        by_title.setdefault(norm_key(title), []).append((path, title, paras))

    queue = []
    for key, entries in sorted(by_title.items()):
        if key in existing_keys:
            continue
        raw_title = entries[0][1]
        close = difflib.get_close_matches(key, existing_keys, n=1, cutoff=0.72)
        paths = [e[0] for e in entries]
        # if multiple files produced the same normalized title, use the longest doc
        # (more content = better matching), but record every path found
        paras = max((e[2] for e in entries), key=len)
        content = strip_boilerplate(paras, bp_lines)

        proposals = []
        for sid, label, kind, domain, group in skills:
            hit = match_term(label, content) if kind == 'term' else match_howto(label, content)
            if hit:
                snippet, conf = hit
                proposals.append({"id": sid, "label": label, "kind": kind, "domain": domain,
                                   "group": group, "evidence": snippet, "confidence": conf})
        n_high = sum(1 for p in proposals if p['confidence'] == 'HIGH')
        n_med = sum(1 for p in proposals if p['confidence'] == 'MEDIUM')
        n_low = sum(1 for p in proposals if p['confidence'] == 'LOW')
        queue.append({
            "title": raw_title,
            "source_paths": paths,
            "n_source_files": len(paths),
            "proposed_skills": proposals,
            "n_proposed": len(proposals),
            "n_high": n_high, "n_medium": n_med, "n_low": n_low,
            "possible_revision_of": close[0] if close else None,
        })

    doc = {
        "_schema": {
            "_comment": "case-reconcile PROPOSE output (MCS-17/MCS-38). Machine drafts, human "
                        "promotes -- nothing here is written into standards_spine.json or "
                        "cases_index.json until `reconcile.py --confirm \"<title>\"` is run by "
                        "name. possible_revision_of flags a title that fuzzy-matches an EXISTING "
                        "spine case (e.g. a v2 of an already-tagged case) -- resolve that by "
                        "hand before confirming; the matcher will not guess."
        },
        "_candidate": True,
        "_confirmed_titles": [],
        "_staged_at": datetime.now(timezone.utc).isoformat(),
        "_promotion": "Sign-off-gated: run `reconcile.py --confirm \"<title>\"` to promote one "
                       "case's proposed skills into standards_spine.json.cases[]/covered_by[] "
                       "and add it to cases_index.json. Never automatic.",
        "discovery_errors": errors,
        "cases": queue,
    }
    out_path = os.path.join(project, 'readmodel', 'reconcile_queue.json')
    dump(doc, out_path)

    print(f"PROPOSE: {len(docs)} docx scanned, {len(queue)} untagged case(s) staged -> {out_path}")
    if errors:
        print(f"  ({len(errors)} file(s) failed to parse, see discovery_errors[])")
    for r in queue:
        flag = f"  [possible revision of {r['possible_revision_of']!r} -- resolve by hand]" \
            if r['possible_revision_of'] else ""
        print(f"  - {r['title']}  ({r['n_high']} HIGH / {r['n_medium']} MED / {r['n_low']} low "
              f"of {r['n_proposed']} proposed, {r['n_source_files']} source file(s)){flag}")
    return doc


def snapshot(project, filenames):
    ts = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    snap_dir = os.path.join(project, 'readmodel', '_snapshots')
    os.makedirs(snap_dir, exist_ok=True)
    for fn in filenames:
        src = os.path.join(project, 'readmodel', fn)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(snap_dir, f"{fn}.{ts}"))


def confirm(project, title, only_ids=None, include_low=False):
    qpath = os.path.join(project, 'readmodel', 'reconcile_queue.json')
    q = load(qpath)
    rec = next((r for r in q['cases'] if r['title'] == title), None)
    if not rec:
        print(f"ERROR: {title!r} not found in reconcile_queue.json cases[]. "
              f"Run --propose first, or check exact title spelling.")
        sys.exit(1)
    if rec.get('possible_revision_of'):
        print(f"REFUSING: {title!r} is flagged possible_revision_of "
              f"{rec['possible_revision_of']!r}. Resolve by hand (edit reconcile_queue.json to "
              f"clear the flag, or confirm the OTHER title instead) before confirming this one.")
        sys.exit(1)

    if only_ids is not None:
        accepted = [p for p in rec['proposed_skills'] if p['id'] in only_ids]
    else:
        # default: HIGH + MEDIUM confidence only. LOW-confidence single-word matches
        # (found only in running prose, e.g. "Time", "Even", "Range") require an
        # explicit --skills list or --include-low to be confirmed -- they should not
        # ride along silently just because they showed up in the proposal.
        levels = {"HIGH", "MEDIUM"} | ({"LOW"} if include_low else set())
        accepted = [p for p in rec['proposed_skills'] if p['confidence'] in levels]
    accepted_ids = {p['id'] for p in accepted}
    if not accepted:
        print("ERROR: nothing to confirm -- empty accepted-skills set (all proposals may be "
              "LOW confidence; pass --include-low or --skills to override).")
        sys.exit(1)

    snapshot(project, ['standards_spine.json', 'cases_index.json'])

    sp_path = os.path.join(project, 'readmodel', 'standards_spine.json')
    ci_path = os.path.join(project, 'readmodel', 'cases_index.json')
    sp = load(sp_path)
    ci = load(ci_path)

    if title not in sp['cases']:
        sp['cases'].append(title)

    touched = 0
    domains_touched = set()
    for d in sp['domains']:
        for g in d['groups']:
            for s in g['skills']:
                if s['id'] in accepted_ids:
                    domains_touched.add(d['domain'])
                    if title not in s['covered_by']:
                        s['covered_by'].append(title)
                        s['n'] = len(s['covered_by'])
                        touched += 1
    all_n = [s['n'] for d in sp['domains'] for g in d['groups'] for s in g['skills']]
    sp['totals']['uncovered'] = sum(1 for n in all_n if n == 0)
    # thin_1_2 was drifting stale here -- confirm() recomputed uncovered/cases but
    # never this one, so every case-reconcile confirm since it was introduced left
    # it reporting a pre-confirm number. Recompute it every time, same as the others.
    sp['totals']['thin_1_2'] = sum(1 for n in all_n if 1 <= n <= 2)
    sp['totals']['cases'] = len(sp['cases'])
    dump(sp, sp_path)

    new_case = {
        "id": re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-'),
        "title": title,
        "status": "legacy",
        "source": "corpus",
        "tier": None, "band": [], "studio": None, "primary_metric": None,
        "options": {"A": None, "B": None}, "margin_pct": None,
        "standards_count": touched,
        "domains_touched": sorted(domains_touched),
        "new_coverage_count": None, "authored_on": None, "published_on": None,
        "qa_verdict": None,
        "paths": {"case_md": None, "case_json": None, "published_dir": None, "drive_url": None,
                  "source_docx": rec['source_paths']},
        "notes": f"Tagged via case-reconcile {datetime.now().date().isoformat()} -- "
                 f"{touched} skill(s) confirmed of {rec['n_proposed']} proposed by the lexical "
                 f"matcher. Confirmed set chosen at --confirm time, not auto-accepted.",
    }
    if not any(c['title'] == title for c in ci['cases']):
        ci['cases'].append(new_case)
    dump(ci, ci_path)

    q['_confirmed_titles'].append(title)
    dump(q, qpath)

    print(f"CONFIRMED {title!r}: {touched} skill(s) written to standards_spine.json.covered_by[], "
          f"case added to cases_index.json as id={new_case['id']!r}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--project', default=os.getcwd())
    ap.add_argument('--propose', action='store_true')
    ap.add_argument('--confirm', metavar='TITLE')
    ap.add_argument('--skills', metavar='ID1,ID2,...',
                     help='confirm only these skill ids (default: HIGH+MEDIUM confidence)')
    ap.add_argument('--include-low', action='store_true',
                     help='also confirm LOW-confidence (single generic word, prose-only) matches')
    a = ap.parse_args()

    if a.confirm:
        only = set(a.skills.split(',')) if a.skills else None
        confirm(a.project, a.confirm, only, include_low=a.include_low)
    elif a.propose:
        propose(a.project)
    else:
        ap.error("specify --propose or --confirm \"<title>\"")


if __name__ == '__main__':
    main()
