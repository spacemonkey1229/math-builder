#!/usr/bin/env python3
"""
validate_domains.py — independent checker for readmodel/domains.json and
readmodel/domain_coverage.json. Reads the emitted JSON, not the builder's data.

Checks:
  1  every file parses as JSON
  2  no duplicate domain ids
  3  every signature_skills id exists in standards_spine.json
  4  every math_branches id exists in curriculum_tree.json
  5  every existing_cases title exists verbatim in corpus_index.json
  6  every domain has >= 1 career and >= 1 decision_archetype
  7  every career has title + math_used + entry_path, and math_used is specific
  8  every domain has >= 1 data source with a plausible URL, and a note
  9  every cluster referenced exists in clusters[]
 10  domain count is inside the commissioned 32-40 band
 11  derived counts in domains.json agree with the spine
 12  domain_coverage.json agrees with domains.json (no drift)
 13  curriculum_tree.json still parses, keeps 10 branches, and preserves
     legacy_intersections[] + intersections_superseded_by
 14  URL verification ledger tallies

Exit 0 on all pass, 1 otherwise.
"""
import json, os, re, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RM = os.path.join(ROOT, "readmodel")

VAGUE = re.compile(r"^(uses |applies )?(statistics|maths?|mathematics|algebra|geometry|"
                   r"numbers|data analysis|calculations?)\.?$", re.I)

results = []


def check(name, ok, detail=""):
    results.append((bool(ok), name, detail))


def load(n):
    try:
        with open(os.path.join(RM, n)) as f:
            return json.load(f), None
    except Exception as e:
        return None, str(e)


def main():
    spine, e1 = load("standards_spine.json")
    tree, e2 = load("curriculum_tree.json")
    corpus, e3 = load("corpus_index.json")
    dom, e4 = load("domains.json")
    cov, e5 = load("domain_coverage.json")

    for n, err in (("standards_spine.json", e1), ("curriculum_tree.json", e2),
                   ("corpus_index.json", e3), ("domains.json", e4),
                   ("domain_coverage.json", e5)):
        check(f"[1] {n} parses", err is None, err or "")
    if any(x is None for x in (spine, tree, corpus, dom, cov)):
        report()
        return 1

    skills = {}
    for d in spine["domains"]:
        for g in d["groups"]:
            for s in g["skills"]:
                skills[s["id"]] = s["n"]
    branch_ids = {b["id"] for b in tree["branches"]}
    titles = {c["title"] for c in corpus["cases"]}
    clusters = {c["name"] for c in dom["clusters"]}
    domains = dom["domains"]

    # 2 duplicate ids
    ids = [d["id"] for d in domains]
    dupes = [i for i, n in collections.Counter(ids).items() if n > 1]
    check("[2] no duplicate domain ids", not dupes, f"dupes={dupes}")

    # 3 signature skills
    bad_sk = [(d["id"], s) for d in domains for s in d["signature_skills"] if s not in skills]
    n_sk = sum(len(d["signature_skills"]) for d in domains)
    check(f"[3] all {n_sk} signature_skills ids exist in spine", not bad_sk, f"bad={bad_sk[:8]}")

    # 4 branches
    bad_br = [(d["id"], b) for d in domains for b in d["math_branches"] if b not in branch_ids]
    n_br = sum(len(d["math_branches"]) for d in domains)
    check(f"[4] all {n_br} math_branches ids exist in tree", not bad_br, f"bad={bad_br[:8]}")

    # 5 case titles
    bad_ct = [(d["id"], t) for d in domains for t in d["existing_cases"] if t not in titles]
    n_ct = sum(len(d["existing_cases"]) for d in domains)
    check(f"[5] all {n_ct} existing_cases titles exist in corpus_index", not bad_ct, f"bad={bad_ct[:8]}")

    # 6 careers / archetypes present
    no_car = [d["id"] for d in domains if not d.get("careers")]
    no_arc = [d["id"] for d in domains if not d.get("decision_archetypes")]
    check("[6a] every domain has >=1 career", not no_car, f"{no_car}")
    check("[6b] every domain has >=1 decision_archetype", not no_arc, f"{no_arc}")

    # 7 career quality
    bad_car = []
    n_car = 0
    for d in domains:
        for c in d["careers"]:
            n_car += 1
            for k in ("title", "math_used", "entry_path"):
                if not c.get(k):
                    bad_car.append((d["id"], c.get("title"), f"missing {k}"))
            mu = c.get("math_used", "")
            if VAGUE.match(mu.strip()) or len(mu.split()) < 8:
                bad_car.append((d["id"], c.get("title"), "math_used too vague"))
    check(f"[7] all {n_car} careers complete and math_used specific", not bad_car, f"bad={bad_car[:8]}")

    # 8 data sources
    bad_src, n_url = [], 0
    for d in domains:
        da = d.get("data_availability", {})
        if da.get("grade") not in ("HIGH", "MEDIUM", "LOW"):
            bad_src.append((d["id"], "bad grade"))
        if not da.get("note"):
            bad_src.append((d["id"], "no note"))
        srcs = da.get("sources") or []
        if not srcs:
            bad_src.append((d["id"], "no sources"))
        for s in srcs:
            n_url += 1
            if not str(s.get("url", "")).startswith(("http://", "https://")):
                bad_src.append((d["id"], f"bad url {s.get('url')!r}"))
            if s.get("verified") not in ("LIVE", "LIVE_JS", "LIVE_LOGIN", "KNOWLEDGE"):
                bad_src.append((d["id"], f"bad verified state {s.get('verified')!r}"))
            if not s.get("label"):
                bad_src.append((d["id"], "source missing label"))
    check(f"[8] all {n_url} sources well-formed with grade+note", not bad_src, f"bad={bad_src[:8]}")

    # 9 clusters
    bad_cl = [(d["id"], d["cluster"]) for d in domains if d["cluster"] not in clusters]
    check("[9] every domain cluster exists in clusters[]", not bad_cl, f"bad={bad_cl}")
    empty_cl = [c["name"] for c in dom["clusters"]
                if not any(d["cluster"] == c["name"] for d in domains)]
    check("[9b] no empty clusters", not empty_cl, f"{empty_cl}")

    # 10 band
    check(f"[10] domain count {len(domains)} inside 32-40", 32 <= len(domains) <= 40)

    # 11 derived counts
    bad_der = []
    for d in domains:
        exp = [s for s in d["signature_skills"] if skills.get(s) == 0]
        if d.get("uncovered_signature_skills") != exp:
            bad_der.append((d["id"], "uncovered list drift"))
        if d.get("n_signature_skills") != len(d["signature_skills"]):
            bad_der.append((d["id"], "n_signature_skills drift"))
        if d.get("n_uncovered_signature_skills") != len(exp):
            bad_der.append((d["id"], "n_uncovered drift"))
    check("[11] derived skill counts agree with spine", not bad_der, f"bad={bad_der[:8]}")

    # 12 coverage join agrees
    check("[12a] coverage domain count matches", cov["totals"]["domains"] == len(domains))
    check("[12b] coverage branch count matches", len(cov["by_branch"]) == len(tree["branches"]))
    drift = []
    cov_by_dom = {b["domain"]: b for b in cov["by_domain"]}
    for d in domains:
        c = cov_by_dom.get(d["id"])
        if not c:
            drift.append((d["id"], "missing from by_domain"))
            continue
        if c["n_uncovered_signature_skills"] != d["n_uncovered_signature_skills"]:
            drift.append((d["id"], "uncovered count drift"))
        if c["n_existing_cases"] != len(d["existing_cases"]):
            drift.append((d["id"], "case count drift"))
    check("[12c] domain_coverage agrees with domains.json", not drift, f"drift={drift[:8]}")
    for b in cov["by_branch"]:
        pass
    bad_bj = [b["branch"] for b in cov["by_branch"]
              if set(b["domains"]) != {d["id"] for d in domains if b["branch"] in d["math_branches"]}]
    check("[12d] by_branch feeder lists recompute correctly", not bad_bj, f"{bad_bj}")

    # 13 tree integrity
    check("[13a] curriculum_tree still has 10 branches", len(tree["branches"]) == 10)
    check("[13b] legacy_intersections preserved (3 originals)",
          len(tree.get("legacy_intersections", [])) == 3,
          str([x.get("domain") for x in tree.get("legacy_intersections", [])]))
    check("[13c] intersections_superseded_by points at domains.json",
          tree.get("intersections_superseded_by") == "domains.json")
    check("[13d] intersections[] now points at every domain",
          len(tree.get("intersections", [])) == len(domains))
    bad_ref = [i.get("ref") for i in tree.get("intersections", [])
               if i.get("ref", "").split("#")[-1] not in set(ids)]
    check("[13e] every intersection ref resolves to a domain id", not bad_ref, f"{bad_ref[:5]}")

    # 14 URL ledger
    states = collections.Counter(s["verified"] for d in domains
                                 for s in d["data_availability"]["sources"])
    live = sum(v for k, v in states.items() if k.startswith("LIVE"))
    know = states.get("KNOWLEDGE", 0)
    gen = dom["_generated"]["verified"]
    check("[14a] URL ledger tally matches _generated",
          gen["urls_fetched_live"] == live and gen["urls_listed_from_knowledge"] == know,
          f"counted live={live} knowledge={know}; declared live={gen['urls_fetched_live']} knowledge={gen['urls_listed_from_knowledge']}")
    check("[14b] no URL is unverified-from-memory", know == 0, f"{know} KNOWLEDGE-only URLs")

    print(f"\nURL states: {dict(states)}")
    print(f"unique URLs: {len({s['url'] for d in domains for s in d['data_availability']['sources']})}")
    return report()


def report():
    npass = sum(1 for ok, _, _ in results if ok)
    nfail = len(results) - npass
    print()
    for ok, name, detail in results:
        print(("  PASS  " if ok else "  FAIL  ") + name + (("   " + detail) if (detail and not ok) else ""))
    print(f"\n{len(results)} checks, {npass} passed, {nfail} failed")
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
