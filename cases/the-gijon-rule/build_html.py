#!/usr/bin/env python3
"""Fill templates/interactive_shell.html for The Gijon Rule (case-local build script, same precedent as
cases/the-trophy-and-the-table/build_html.py and cases/the-grade-rule/build_html.py). The page text is
converted from case.md so the two cannot drift; the Working Notebook is a JS port of sensitivity_model.py
(PARAMS / FLEX / evaluate / evaluate_twist, plus the enumeration helpers). The STORY_GLOSSARY layer is NOT
written here: run
    python3 skills/case-publish/scripts/render_context.py --case the-gijon-rule
after this script (it renders case.json.context_glossary[] into the HTML).

Run:  python3 build_worked_example.py && python3 build_html.py   (from this directory)
"""
import os
import re
import html as H
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(os.path.dirname(HERE))
SHELL = f"{PROJECT}/templates/interactive_shell.html"
OUT = f"{HERE}/published/The Gijon Rule - Interactive.html"
sys.path.insert(0, HERE)
import build_worked_example as BWE  # noqa: E402

md = open(f"{HERE}/case.md", encoding="utf-8").read()
md = re.sub(r'<!--.*?-->', '', md, flags=re.S)       # drops the FACILITATOR ONLY marker comment
svg_fixed = BWE.fixed_svg()


def inline(t):
    t = H.escape(t, quote=False)
    t = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', t)
    return t


def block_html(block, grid_ids=None):
    """Render a case.md block (paragraphs, bullet/numbered lists, tables, blockquote, figure, svg)."""
    lines = block.strip('\n').split('\n')
    out, i = [], 0
    tcount = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.strip().startswith('<svg'):
            while '</svg>' not in lines[i]:
                i += 1
            i += 1
            out.append('<figure><div style="overflow-x:auto"><div style="min-width:640px">' + svg_fixed +
                       '</div></div><figcaption>Drawn by the case author to illustrate the method on a scoreline you are not asked to do. '
                       'Green S = safe, grey N = not safe. On a narrow screen, scroll this figure sideways.</figcaption></figure>')
            continue
        if line.strip().startswith('<figure'):
            buf = []
            while True:
                buf.append(lines[i])
                if '</figure>' in lines[i]:
                    break
                i += 1
            i += 1
            out.append(' '.join(buf))
            continue
        if line.strip().startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                rows.append(lines[i])
                i += 1
            cells = [[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
            hdr, bodyrows = cells[0], cells[2:]
            is_grid = hdr[0].startswith('Algeria \\ Chile')
            tcount += 1
            tid = (grid_ids or {}).get(tcount) if grid_ids else None
            h = '<table%s%s><tr>%s</tr>\n' % (' id="%s"' % tid if tid else '', ' class="gridtbl"' if is_grid else '',
                                                ''.join('<th>%s</th>' % inline(c) for c in hdr))
            for r in bodyrows:
                if is_grid:
                    h += '<tr><th scope="row">%s</th>%s</tr>\n' % (inline(r[0]), ''.join('<td>%s</td>' % inline(c) for c in r[1:]))
                else:
                    h += '<tr>%s</tr>\n' % ''.join('<td>%s</td>' % inline(c) for c in r)
            out.append('<div style="overflow-x:auto">' + h + '</table></div>')
            continue
        if line.startswith('> '):
            q = []
            while i < len(lines) and lines[i].startswith('>'):
                q.append(lines[i].lstrip('> ').strip())
                i += 1
            out.append('<blockquote>%s</blockquote>' % inline(' '.join(q)))
            continue
        m = re.match(r'^(\s*)(-|\d+\.)\s+(.*)$', line)
        if m:
            ordered = m.group(2) != '-'
            items = []
            while i < len(lines):
                mm = re.match(r'^(\s*)(-|\d+\.)\s+(.*)$', lines[i])
                if not mm:
                    break
                body = [mm.group(3)]
                i += 1
                while i < len(lines) and lines[i].strip() and not re.match(r'^(\s*)(-|\d+\.)\s+', lines[i]) \
                        and not lines[i].strip().startswith(('|', '<', '>')):
                    body.append(lines[i].strip())
                    i += 1
                items.append('<li>%s</li>' % inline(' '.join(body)))
            out.append('<%s>%s</%s>' % ('ol' if ordered else 'ul', ''.join(items), 'ol' if ordered else 'ul'))
            continue
        para = [line.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith(('|', '<svg', '<figure', '> ')) \
                and not re.match(r'^(\s*)(-|\d+\.)\s+', lines[i]):
            para.append(lines[i].strip())
            i += 1
        out.append('<p>' + inline(' '.join(para)) + '</p>')
    return '\n'.join(out)


def sect(title_re):
    m = re.search(r'(?ms)^## ' + title_re + r'[^\n]*\n(.*?)(?=^---\s*$|\Z)', md)
    return m.group(1).strip()


def appendix(letter):
    m = re.search(r'(?ms)^## Appendix %s — (.*?)\n(.*?)(?=^---\s*$)' % letter, md)
    return m.group(1).strip(), m.group(2).strip()


html = open(SHELL, encoding="utf-8").read()
R = {}
R["{{CASE_TITLE}}"] = "The Gijon Rule"
R["{{CASE_YEAR}}"] = "2026-27"
R["{{CASE_TIER}}"] = "T2"
R["{{CASE_BAND}}"] = "MS-Core"
R["{{CASE_STRAND_SUMMARY}}"] = "Counting &middot; Sets &amp; Venn Diagrams &middot; Negative Numbers &middot; Percents"
R["{{CASE_ID}}"] = "the-gijon-rule"
R["{{CASE_GLOSSARY_APPENDIX_LETTER}}"] = "Appendix H"
R["{{CASE_GLOSSARY_VERIFIED_DATE}}"] = "2026-10-04"
R["{{CASE_PROTAGONIST}}"] = "Marguerite Adeyemi"
R["{{CASE_OPTION_A_LABEL}}"] = "Same-Clock Only"
R["{{CASE_OPTION_A_TEXT}}"] = "Recommend that the final group matches kick off simultaneously, with the tie-break ladder unchanged."
R["{{CASE_OPTION_B_LABEL}}"] = "Same-Clock, Goals First"
R["{{CASE_OPTION_B_TEXT}}"] = "Recommend that the final group matches kick off simultaneously, and that goals scored are checked before goal difference."
R["{{CASE_SPECIFIC_CSS}}"] = """.num{text-align:right;font-variant-numeric:tabular-nums}
  table.gridtbl td{height:34px;min-width:38px;text-align:center}
  table.gridtbl th[scope=row]{background:#e8eef5;color:var(--navy);text-align:center;width:90px}
  figure img{max-width:100%;height:auto;border-radius:6px}
  .stepbox input[type=number]{width:132px}
  .twistflag{font-family:var(--sans);font-size:.8rem;font-weight:700;color:#7a4a00;background:var(--gold-lt);border:1px solid var(--gold);border-radius:6px;padding:4px 9px;display:none;margin-bottom:10px}
  .fb.empty{color:var(--sub);background:#eee}"""
R["{{CASE_SPECIFIC_ICON_SYMBOLS}}"] = ""
R["{{CASE_OVERVIEW_BANNER_SVG}}"] = ""

ov = [p for p in re.split(r'\n\s*\n', sect('Overview')) if p.strip()]
R["{{CASE_OVERVIEW_TEXT}}"] = '<p class="lede">' + inline(ov[0].replace('\n', ' ')) + '</p>\n' + '\n'.join(
    '<p>' + inline(p.replace('\n', ' ')) + '</p>' for p in ov[1:])
R["{{CASE_BACKGROUND_TEXT}}"] = block_html(sect('Background')) + (
    '\n<div class="card" id="storyGlossaryCard"><strong>Football Vocabulary</strong>'
    '<p class="side-note" style="margin-top:6px">Hover any underlined term in the story (or below) for a plain-English definition; click it to open a real source. '
    'These are the football words the story is told in; the math vocabulary is in Appendix H.</p>'
    '<div class="glossary-grid" id="storyGlossaryGrid"></div></div>')
_ch = sect('Challenges')
_dl = re.findall(r'(?m)^- (\*\*D\d .*?)(?=^- \*\*D\d |^\d+\.\)|\Z)', _ch, re.S)
assert len(_dl) == 6, len(_dl)
_dl_html = '<ul>' + ''.join('<li>%s</li>' % inline(' '.join(x.split())) for x in _dl) + '</ul>'
# one hand-placed glossary anchor so the auto-linker links "set" where it is used as the math term (D4), not in
# the Background's ordinary-English "a set of small leagues" (the auto-linker otherwise takes the first mention).
_SET_DEF = "A well-defined collection of distinct objects, considered as an object in its own right."
_SET_URL = "https://www.mathsisfun.com/sets/sets-introduction.html"
_set_anchor = ('<a class="gterm" data-term="Set" href="%s" target="_blank" rel="noopener">set<span class="tip">%s'
               '<span class="go">Open a lesson on this &rarr;</span></span></a>' % (_SET_URL, _SET_DEF))
assert 'of the set of safe cells under Option A' in _dl_html
_dl_html = _dl_html.replace('of the set of safe cells under Option A', 'of the ' + _set_anchor + ' of safe cells under Option A', 1)
R["{{CASE_CHALLENGE_3_DELIVERABLES_SUMMARY}}"] = 'Your pitch must include:' + _dl_html
R["{{CASE_DELIVERABLES_ARRAY}}"] = """[
  ["D1", "Group 2 standings and the goal-difference arithmetic"],
  ["D2", "The three-point test"],
  ["D3", "Option A: two grids and a count"],
  ["D4", "Option B: two grids and a Venn diagram"],
  ["D5", "The cost to history"],
  ["D6", "The recommendation"]
]"""

# ---------------- appendices A-G ----------------
apx = ""
for letter, open_attr in (("A", " open"), ("B", ""), ("C", ""), ("D", ""), ("E", ""), ("F", ""), ("G", "")):
    title, body = appendix(letter)
    apx += '<details%s id="apx-%s"><summary>Appendix %s &mdash; %s</summary><div class="inner">\n%s\n</div></details>\n' % (
        open_attr, letter.lower(), letter, inline(title), block_html(body))
R["{{CASE_APPENDICES_A_THROUGH_F}}"] = apx

# ---------------- notebook ----------------
def row(lab, iid, fid, ph="whole number"):
    return ('<div class="fieldrow"><label for="%s">%s</label><input type="number" id="%s" step="any" placeholder="%s">'
            '<span id="%s" class="fb"></span></div>' % (iid, lab, iid, ph, fid))


R["{{CASE_NOTEBOOK_STEPS}}"] = """
  <div class="stepbox">
    <h4>Step 1 &mdash; Group 2 before West Germany-Austria (D1)</h4>
    <div class="goal">Use matches 1 to 4 and Algeria-Chile as played (matches 1 to 5 in Appendix B), two points per win. Goal difference can be negative: type the minus sign.</div>
""" + row("Austria's points", "s1a", "fb1a") + row("Austria's goal difference", "s1b", "fb1b") + row("Algeria's goal difference", "s1c", "fb1c") + \
    row("West Germany's goal difference", "s1d", "fb1d") + row("Chile's goal difference", "s1e", "fb1e") + \
    row("Austria's goal difference after West Germany 1-0 Austria is added", "s1f", "fb1f") + """
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; The three-point test (D2)</h4>
    <div class="goal">Hold Algeria-Chile at its as-played 3-2 and run every West Germany win in the 0-6 window (West Germany scores more than Austria), using the 1982 ladder and two points per win.</div>
""" + row("How many West Germany wins are there in the window?", "s2a", "fb2a") + \
    row("In how many does the ladder send West Germany and Austria through?", "s2b", "fb2b") + \
    row("In how many is second versus third unresolved?", "s2c", "fb2c") + \
    row("In how many does the advancing pair change if a win is worth three points?", "s2d", "fb2d") + """
    <button onclick="checkStep2()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 3 &mdash; Option A: the grids and the counts (D3)</h4>
    <div class="twistflag" id="twistTag3">Twist applied: use only the surviving Algeria-Chile cells.</div>
    <div class="goal">Under the 1982 ladder (points, goal difference, goals scored), count the Algeria-Chile cells and the safe cells for the two benchmark scorelines. Unresolved cells are never safe.</div>
""" + row("Number of Algeria-Chile cells in the grid", "s3a", "fb3a") + row("West Germany 1-0 Austria: safe cells", "s3b", "fb3b") + \
    row("West Germany 6-5 Austria: safe cells", "s3c", "fb3c") + row("For 1-0: safe cells in which Algeria wins", "s3d", "fb3d") + """
    <button onclick="checkStep3()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 4 &mdash; Option B: the grids and the Venn counts (D4)</h4>
    <div class="twistflag" id="twistTag4">Twist applied: use only the surviving Algeria-Chile cells.</div>
    <div class="goal">Under Option B's ladder (points, goals scored, goal difference), count the safe cells for the two benchmarks, then for 1-0 give the three regions of the Venn diagram of the safe sets under A and under B.</div>
""" + row("West Germany 1-0 Austria: safe cells under Option B", "s4a", "fb4a") + row("West Germany 6-5 Austria: safe cells under Option B", "s4b", "fb4b") + \
    row("1-0 Venn: cells safe only under Option A", "s4c", "fb4c") + row("1-0 Venn: cells safe under both", "s4d", "fb4d") + \
    row("1-0 Venn: cells safe only under Option B", "s4e", "fb4e") + """
    <button onclick="checkStep4()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 5 &mdash; The cost to history (D5)</h4>
    <div class="goal">Apply Option B's ladder to the final tables in Appendix D (two points per win).</div>
""" + row("How many of Groups 1, 3, 4, 5 and 6 would have a different pair advance?", "s5a", "fb5a") + \
    row("Group 2 as played under Option B: goals scored by the team that finishes second", "s5b", "fb5b") + """
    <button onclick="checkStep5()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 6 &mdash; The ceiling, the average and the comparison (D6)</h4>
    <div class="twistflag" id="twistTag6">Twist applied: percents are out of the surviving Algeria-Chile cells.</div>
    <div class="goal">Enter each percent to the nearest tenth. The ceiling is the larger of the two benchmark percents; the average is their mean. Compare Option B with Option A two ways: as a difference in percentage points, and as a percent of Option A's figure.</div>
""" + row("Option A ceiling (percent)", "s6a", "fb6a", "percent") + row("Option B ceiling (percent)", "s6b", "fb6b", "percent") + \
    row("Ceiling gap, B minus A (percentage points)", "s6c", "fb6c", "points") + \
    row("Ceiling gap as a percent of Option A's ceiling", "s6d", "fb6d", "percent") + \
    row("Option A average (percent)", "s6e", "fb6e", "percent") + row("Option B average (percent)", "s6f", "fb6f", "percent") + """
    <button onclick="checkStep6()">Check</button>
    <p class="side-note">These checks only confirm your arithmetic. Which option to recommend, and which summary the committee should trust, is still yours.</p>
  </div>
"""

R["{{CASE_TWIST_NARRATIVE}}"] = """
      <p>&ldquo;The two matches kick off at the same moment, as both options require.&rdquo;</p>
      <p>&ldquo;Late in both matches, word reaches the benches. The Algeria-Chile match is over. It ended as a narrow Algeria win: by one goal or by two. Like the 3-2 that was actually played.&rdquo;</p>
      <p>&ldquo;Treat that as settled for the other match. Cross out every cell that is not a one-goal or two-goal Algeria win; the grid is now those cells only, and your percents are out of those cells. Rerun your ceiling and your average.&rdquo;</p>
"""
R["{{CASE_TWIST_APPLY_LABEL}}"] = "Apply the twist to Steps 3, 4 and 6 (use only the surviving Algeria-Chile cells; percents out of those cells)"

_src_title, _src_body = appendix("G")
_src_rows = [[c.strip() for c in l.strip().strip('|').split('|')] for l in _src_body.splitlines() if l.startswith('| S')]
R["{{CASE_SOURCES_LIST}}"] = "\n".join(
    '<li>[%s] %s</li>' % (r[0], re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', r[2]))
    for r in _src_rows)

R["{{CASE_JS_DATA_BLOCK}}"] = """
// Ported from cases/the-gijon-rule/sensitivity_model.py. Raw given data and assumptions only; the notebook
// computes every answer live from these (it never stores a verdict).
// W = West Germany, A = Austria, G = Algeria, C = Chile.  Matches 1-4 of Appendix B (source S1):
const PRIOR = [["W","G",1,2], ["C","A",0,1], ["W","C",4,1], ["G","A",0,2]];
const PARAMS = { cap: 6, points_win: 2 };
const FLEX = ["cap"];
// Appendix D final tables [W, D, L, GF, GA] (sources S1, S4-S8)
const GROUPS = {
  1: {POL:[1,2,0,5,1], ITA:[0,3,0,2,2], CMR:[0,3,0,1,1], PER:[0,2,1,2,6]},
  2: {FRG:[2,0,1,6,3], AUT:[2,0,1,3,1], ALG:[2,0,1,5,5], CHI:[0,0,3,3,8]},
  3: {BEL:[2,1,0,3,1], ARG:[2,0,1,6,2], HUN:[1,1,1,12,6], SLV:[0,0,3,1,13]},
  4: {ENG:[3,0,0,6,1], FRA:[1,1,1,6,5], TCH:[0,2,1,2,4], KUW:[0,1,2,2,6]},
  5: {NIR:[1,2,0,2,1], ESP:[1,1,1,3,3], YUG:[1,1,1,2,2], HON:[0,2,1,2,3]},
  6: {BRA:[3,0,0,10,2], URS:[1,1,1,6,4], SCO:[1,1,1,8,8], NZL:[0,0,3,2,12]}
};
function _table(results, win){
  const T = {W:[0,0,0], A:[0,0,0], G:[0,0,0], C:[0,0,0]};            // points, goals for, goals against
  results.forEach(([h,a,hg,ag]) => {
    [[h,hg,ag],[a,ag,hg]].forEach(([t,gf,ga]) => {
      T[t][1] += gf; T[t][2] += ga; T[t][0] += gf > ga ? win : (gf === ga ? 1 : 0);
    });
  });
  return T;
}
function _cmp(x, y){ for(let i=0;i<x.length;i++){ if(x[i] !== y[i]) return y[i] - x[i]; } return 0; }   // descending
function top2(algChile, wgAut, ladder, win){
  const T = _table(PRIOR.concat([["G","C",algChile[0],algChile[1]], ["W","A",wgAut[0],wgAut[1]]]), win);
  const key = t => { const [p,gf,ga] = T[t]; return ladder === "A" ? [p, gf-ga, gf] : [p, gf, gf-ga]; };
  const order = Object.keys(T).sort((x,y) => _cmp(key(x), key(y)));
  if(_cmp(key(order[1]), key(order[2])) === 0) return null;            // unresolved: second vs third left to a lot
  return order.slice(0,2).sort().join("");
}
function safeCells(wgAut, cap, ladder, win, narrow){
  const cells = [];
  for(let a=0;a<=cap;a++) for(let c=0;c<=cap;c++){
    if(narrow && !(a-c >= 1 && a-c <= 2)) continue;
    cells.push([a,c]);
  }
  const ok = cells.filter(cell => top2(cell, wgAut, ladder, win) === "AW");
  const unresolved = cells.filter(cell => top2(cell, wgAut, ladder, win) === null);
  return {ok, n: cells.length, unresolved};
}
function benchmarkScorelines(cap){ return [[1,0], [cap, cap-1]]; }
function ceiling(ladder, cap, win, narrow){
  let best = 0;
  benchmarkScorelines(cap).forEach(sl => { const s = safeCells(sl, cap, ladder, win, narrow); best = Math.max(best, s.ok.length / s.n); });
  return best;
}
function average(ladder, cap, win, narrow){
  const v = benchmarkScorelines(cap).map(sl => { const s = safeCells(sl, cap, ladder, win, narrow); return s.ok.length / s.n; });
  return v.reduce((x,y) => x+y, 0) / v.length;
}
// higher is better, so the (lower-is-better) ceiling is negated, exactly as in sensitivity_model.py
function evaluate(params){
  const p = Object.assign({}, PARAMS, params || {}); const cap = Math.round(p.cap);
  return {A: -ceiling("A", cap, p.points_win, false), B: -ceiling("B", cap, p.points_win, false)};
}
function evaluate_twist(params){
  const p = Object.assign({}, PARAMS, params || {}); const cap = Math.round(p.cap);
  return {A: -ceiling("A", cap, p.points_win, true), B: -ceiling("B", cap, p.points_win, true)};
}
function groupTop2(rows, ladder){
  const key = t => { const [w,d,l,gf,ga] = rows[t]; const pts = 2*w + d; return ladder === "A" ? [pts, gf-ga, gf] : [pts, gf, gf-ga]; };
  const order = Object.keys(rows).sort((x,y) => _cmp(key(x), key(y)));
  return {pair: order.slice(0,2).sort().join(","), second: order[1], resolved: _cmp(key(order[1]), key(order[2])) !== 0};
}
"""

R["{{CASE_NOTEBOOK_CHECK_FUNCTIONS}}"] = """
function _num(id){ const v = document.getElementById(id).value; return (v === '' || v === null) ? NaN : parseFloat(v); }
function fb2(fbId, inputId, expected, tol){
  const x = _num(inputId); const el = document.getElementById(fbId);
  if(isNaN(x)){ el.className = 'fb empty'; el.textContent = 'enter a value'; return; }
  fb(fbId, near(x, expected, tol));
}
function checkStep1(){
  const T = _table(PRIOR.concat([["G","C",3,2]]), PARAMS.points_win);
  const T2 = _table(PRIOR.concat([["G","C",3,2], ["W","A",1,0]]), PARAMS.points_win);
  fb2('fb1a','s1a', T.A[0], 0);
  fb2('fb1b','s1b', T.A[1]-T.A[2], 0);
  fb2('fb1c','s1c', T.G[1]-T.G[2], 0);
  fb2('fb1d','s1d', T.W[1]-T.W[2], 0);
  fb2('fb1e','s1e', T.C[1]-T.C[2], 0);
  fb2('fb1f','s1f', T2.A[1]-T2.A[2], 0);
}
function checkStep2(){
  let wins = 0, adv2 = 0, unres = 0, differ = 0;
  for(let w=0; w<=PARAMS.cap; w++) for(let u=0; u<=PARAMS.cap; u++){
    if(w <= u) continue;
    wins++;
    const p2 = top2([3,2],[w,u],"A",2), p3 = top2([3,2],[w,u],"A",3);
    if(p2 === "AW") adv2++;
    if(p2 === null) unres++;
    if(p2 !== p3) differ++;
  }
  fb2('fb2a','s2a', wins, 0); fb2('fb2b','s2b', adv2, 0); fb2('fb2c','s2c', unres, 0); fb2('fb2d','s2d', differ, 0);
}
function _narrow(){ return !!window.__TWIST_APPLIED__; }
function checkStep3(){
  const n = _narrow(), cap = PARAMS.cap, win = PARAMS.points_win;
  const s10 = safeCells([1,0], cap, "A", win, n), s65 = safeCells([cap, cap-1], cap, "A", win, n);
  fb2('fb3a','s3a', s10.n, 0); fb2('fb3b','s3b', s10.ok.length, 0); fb2('fb3c','s3c', s65.ok.length, 0);
  fb2('fb3d','s3d', s10.ok.filter(c => c[0] > c[1]).length, 0);
}
function checkStep4(){
  const n = _narrow(), cap = PARAMS.cap, win = PARAMS.points_win;
  const a10 = safeCells([1,0], cap, "A", win, n), b10 = safeCells([1,0], cap, "B", win, n), b65 = safeCells([cap, cap-1], cap, "B", win, n);
  const setB = new Set(b10.ok.map(c => c.join(",")));
  const both = a10.ok.filter(c => setB.has(c.join(","))).length;
  fb2('fb4a','s4a', b10.ok.length, 0); fb2('fb4b','s4b', b65.ok.length, 0);
  fb2('fb4c','s4c', a10.ok.length - both, 0); fb2('fb4d','s4d', both, 0); fb2('fb4e','s4e', b10.ok.length - both, 0);
}
function checkStep5(){
  let changed = 0;
  [1,3,4,5,6].forEach(g => { if(groupTop2(GROUPS[g], "A").pair !== groupTop2(GROUPS[g], "B").pair) changed++; });
  const second = groupTop2(GROUPS[2], "B").second;
  fb2('fb5a','s5a', changed, 0); fb2('fb5b','s5b', GROUPS[2][second][3], 0);
}
function checkStep6(){
  const n = _narrow(), cap = PARAMS.cap, win = PARAMS.points_win;
  const e = n ? evaluate_twist() : evaluate();
  const cA = -e.A * 100, cB = -e.B * 100;
  fb2('fb6a','s6a', cA, 0.15); fb2('fb6b','s6b', cB, 0.15);
  fb2('fb6c','s6c', cB - cA, 0.15); fb2('fb6d','s6d', (cB - cA) / cA * 100, 0.3);
  fb2('fb6e','s6e', average("A", cap, win, n) * 100, 0.15); fb2('fb6f','s6f', average("B", cap, win, n) * 100, 0.15);
}
"""
R["{{CASE_ON_TWIST_TOGGLE_FUNCTION}}"] = """
function onTwistToggle(){
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
  ['twistTag3','twistTag4','twistTag6'].forEach(id => { const el = document.getElementById(id); if(el) el.style.display = window.__TWIST_APPLIED__ ? 'block' : 'none'; });
  document.querySelectorAll('#s3a,#s3b,#s3c,#s3d,#s4a,#s4b,#s4c,#s4d,#s4e,#s6a,#s6b,#s6c,#s6d,#s6e,#s6f').forEach(inp => {
    const f = inp.parentElement.querySelector('.fb'); if(f){ f.className = 'fb'; f.textContent = ''; }
  });
}
"""

R["{{CASE_GLOSSARY_OBJECT}}"] = """{
  "Fundamental Counting Principle": {def: "If there are n ways to do one task and m ways to do a second task, there are n \\u00d7 m ways to do both.",
    url: "https://openstax.org/books/contemporary-mathematics/pages/7-1-the-multiplication-rule-for-counting"},
  "Outcome": {def: "A single possible result. In this case, one Algeria-Chile scoreline is one outcome.",
    url: "https://www.mathsisfun.com/data/probability.html"},
  "Event": {def: "One or more outcomes grouped together. In this case, the cells in which a scoreline is safe form an event.",
    url: "https://www.mathsisfun.com/data/probability.html"},
  "Set": {def: "A well-defined collection of distinct objects, considered as an object in its own right.",
    url: "https://www.mathsisfun.com/sets/sets-introduction.html"},
  "Subset": {def: "A set every one of whose elements is also a member of some larger set.",
    url: "https://www.mathsisfun.com/sets/sets-introduction.html"},
  "Venn Diagram": {def: "A diagram using overlapping circles to show how sets relate -- shared regions are the intersection, everything inside either circle is the union.",
    url: "https://www.mathsisfun.com/sets/venn-diagrams.html"},
  "Negative Number": {def: "A number less than zero -- on a number line, anything to the left of zero.",
    url: "https://www.mathsisfun.com/positive-negative-integers.html"},
  "Comparing Values": {def: "Using symbols like <, >, and = to show whether one value is less than, greater than, or equal to another.",
    url: "https://www.mathsisfun.com/equal-less-greater.html"},
  "Percent": {def: "A ratio that compares a number to 100 -- literally \\"per hundred.\\"",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"}
}"""
R["{{CASE_HOWTO_ARRAY}}"] = """[
  ["How to apply the Fundamental Counting Principle to count outcomes", "Fundamental Counting Principle"],
  ["How to find the union and intersection of two sets", "Venn Diagram"],
  ["How to represent a set relationship using a Venn diagram", "Venn Diagram"],
  ["How to add with negative numbers", "Negative Number"],
  ["How to convert numbers to percents", "Percent"],
  ["How to compare two or more values", "Comparing Values"]
]"""

for k, v in R.items():
    if k not in html:
        raise SystemExit("MISSING PLACEHOLDER IN SHELL: " + k)
    html = html.replace(k, v)
left = [m for m in re.findall(r'\{\{[A-Z_0-9]+\}\}', html) if m != '{{PLACEHOLDER}}']
if left:
    raise SystemExit("Unfilled placeholders remain: %s" % left)
# The shell's Challenge 2 line is generic boilerplate ("which order you'd choose"); this case chooses an option.
assert "which order you'd choose" in html
html = html.replace("which order you'd choose", "which option you would choose")
# The photo is served through the Commons file-path redirect on commons.wikimedia.org, the same domain S12 cites
# (same file, same licence); the raw upload.wikimedia.org thumbnail URL in case.md is not a cited domain (T1-20).
_up = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Interior_de_El_Molin%C3%B3n.JPG/960px-Interior_de_El_Molin%C3%B3n.JPG"
assert _up in html
html = html.replace(_up, "https://commons.wikimedia.org/wiki/Special:FilePath/Interior_de_El_Molin%C3%B3n.JPG?width=960")
# the shell's explanatory comment mentions the placeholder syntax literally; keep the shipped file free of "{{"
html = html.replace("{{PLACEHOLDER}} tokens", "placeholder tokens")
os.makedirs(f"{HERE}/published", exist_ok=True)
open(OUT, "w", encoding="utf-8").write(html)
print("wrote", OUT, len(html), "chars")
