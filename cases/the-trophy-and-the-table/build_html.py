#!/usr/bin/env python3
"""Fill templates/interactive_shell.html for The Trophy and the Table (case-local build script,
same precedent as cases/the-grade-rule/build_html.py). Content is converted from case.md so the
two cannot drift; the JS notebook is a port of sensitivity_model.py."""
import re, html as H

PROJECT = "/Users/manan/Documents/Claude/Projects/Math Builder"
CASE = f"{PROJECT}/cases/the-trophy-and-the-table"
SHELL = f"{PROJECT}/templates/interactive_shell.html"
OUT = f"{CASE}/published/The Trophy and the Table - Interactive.html"
md = open(f"{CASE}/case.md", encoding="utf-8").read()
md = re.split(r'<!--\s*FACILITATOR ONLY', md)[0] + md.split('-->',1)[1] if '<!-- FACILITATOR ONLY' in md else md


def sect(title_re):
    m = re.search(r'(?ms)^## ' + title_re + r'.*?\n(.*?)(?=^---\s*$|\Z)', md)
    return m.group(1).strip()


def inline(t):
    t = H.escape(t, quote=False)
    t = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', t)
    return t


def paras(block):
    out = []
    for p in re.split(r'\n\s*\n', block.strip()):
        p = p.strip()
        if not p or p.startswith('<svg') or p.startswith('<!--'):
            continue
        out.append('<p>' + inline(p.replace('\n', ' ')) + '</p>')
    return '\n'.join(out)


def table(block, tid):
    rows = [l for l in block.splitlines() if l.strip().startswith('|')]
    cells = [[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
    hdr, body = cells[0], cells[2:]
    h = '<table id="%s"><tr>%s</tr>\n' % (tid, ''.join('<th>%s</th>' % inline(c) for c in hdr))
    for r in body:
        h += '<tr>%s</tr>\n' % ''.join('<td>%s</td>' % inline(c) for c in r)
    return h + '</table>'


def appendix(letter):
    m = re.search(r'(?ms)^## Appendix %s — (.*?)\n(.*?)(?=^---\s*$)' % letter, md)
    return m.group(1).strip(), m.group(2).strip()


html = open(SHELL, encoding="utf-8").read()
R = {}
R["{{CASE_TITLE}}"] = "The Trophy and the Table"
R["{{CASE_YEAR}}"] = "2026-27"
R["{{CASE_TIER}}"] = "T3"
R["{{CASE_BAND}}"] = "MS-Stretch / HS-Entry"
R["{{CASE_STRAND_SUMMARY}}"] = "Scatter Plots &middot; Line of Best Fit &middot; Residuals &middot; Break-Even"
R["{{CASE_ID}}"] = "the-trophy-and-the-table"
R["{{CASE_GLOSSARY_APPENDIX_LETTER}}"] = "Appendix H"
R["{{CASE_GLOSSARY_VERIFIED_DATE}}"] = "2026-10-03"
R["{{CASE_PROTAGONIST}}"] = "a member of the club's board"
R["{{CASE_OPTION_A_LABEL}}"] = "Keep the Winner"
R["{{CASE_OPTION_A_TEXT}}"] = "Keep the manager who won the Europa League trophy; the 17th-place finish is not treated as a reason to change."
R["{{CASE_OPTION_B_LABEL}}"] = "Change After 17th"
R["{{CASE_OPTION_B_TEXT}}"] = "Replace the manager after the 17th-place league finish, betting that the reset cost is smaller than the shortfall it avoids."
R["{{CASE_SPECIFIC_CSS}}"] = ".num{text-align:right;font-variant-numeric:tabular-nums}\n  " + '.sterm{position:relative;color:var(--navy-dk);text-decoration:none;border-bottom:1.5px dotted var(--ok);cursor:help;font-weight:600}\n  .sterm:hover, .sterm:focus{background:var(--ok-bg)}\n  .sterm .tip{visibility:hidden;opacity:0;position:absolute;left:50%;bottom:135%;transform:translateX(-50%);width:230px;background:var(--navy-dk);color:#fff;font-family:var(--sans);font-weight:400;font-size:.76rem;line-height:1.4;padding:9px 11px;border-radius:7px;box-shadow:0 4px 14px rgba(0,0,0,.25);transition:opacity .12s;z-index:30}\n  .sterm .tip .go{display:block;margin-top:6px;color:var(--ok);font-weight:700}\n  .sterm:hover .tip, .sterm:focus .tip{visibility:visible;opacity:1}\n  .glossary-grid .sterm{display:inline-block;background:#fff;border:1px solid var(--line);border-bottom:1.5px dotted var(--ok);border-radius:999px;padding:5px 12px;font-family:var(--sans);font-size:.82rem}'
R["{{CASE_SPECIFIC_ICON_SYMBOLS}}"] = ""
R["{{CASE_OVERVIEW_BANNER_SVG}}"] = ""

ov = sect('Overview').split('\n\n')
R["{{CASE_OVERVIEW_TEXT}}"] = '<p class="lede">' + inline(ov[0].replace('\n', ' ')) + '</p>\n' + paras('\n\n'.join(ov[1:]))
R["{{CASE_BACKGROUND_TEXT}}"] = paras(sect('Background')) + '\n<div class="card" id="storyGlossaryCard"><strong>Football Vocabulary</strong><p class="side-note" style="margin-top:6px">Hover any underlined term for a plain-English definition; click to open a real source. These are the football words the story is told in; the math vocabulary is in Appendix H.</p><div class="glossary-grid" id="storyGlossaryGrid"></div></div>'
R["{{CASE_CHALLENGE_3_DELIVERABLES_SUMMARY}}"] = (
    "Include: <strong>D1</strong> a scatter plot, line of best fit and its equation; <strong>D2</strong> a residual table for all 20 clubs; "
    "<strong>D3</strong> an outlier check with the club's row removed; <strong>D4</strong> a break-even comparison with your own reset-cost range; "
    "<strong>D5 (graded)</strong> what the model leaves out. The full wording of each deliverable is in the case document.")
R["{{CASE_DELIVERABLES_ARRAY}}"] = """[
  ["D1", "Scatter plot, line of best fit, equation"],
  ["D2", "Residual table for all 20 clubs"],
  ["D3", "Outlier check (club's row removed)"],
  ["D4", "Break-even comparison and your reset-cost range"],
  ["D5", "What the model leaves out (graded)"]
]"""

# ---- appendices A-F ----
apx = ""
tA, bA = appendix('A')
apx += '<details open id="apx-a"><summary>Appendix A &mdash; %s</summary><div class="inner">\n%s\n</div></details>\n' % (inline(tA), paras(bA))
tB, bB = appendix('B')
intro = bB.split('\n\n')[0]
apx += '<details id="apx-b"><summary>Appendix B &mdash; %s</summary><div class="inner">\n<p>%s</p>\n%s\n</div></details>\n' % (inline(tB), inline(intro.replace('\n',' ')), table(bB, 'tblB'))
tC, bC = appendix('C')
items = [l[2:] for l in bC.splitlines() if l.startswith('- ')]
pre = bC.split('\n\n')[0]
apx += '<details id="apx-c"><summary>Appendix C &mdash; %s</summary><div class="inner">\n<p>%s</p>\n<ul>%s</ul>\n</div></details>\n' % (inline(tC), inline(pre), ''.join('<li>%s</li>' % inline(i) for i in items))
tD, bD = appendix('D')
_tail = bD[bD.index('**What')-0:] if '**What' in bD else ''
_svgD = re.search(r'(?s)<svg.*?</svg>', _tail).group(0) if _tail else ''
apx += '<details id="apx-d"><summary>Appendix D &mdash; %s</summary><div class="inner">\n<blockquote>%s</blockquote>\n%s\n%s\n<figure>%s<figcaption>Drawn without a scale; shows no figure from this case.</figcaption></figure>\n</div></details>\n' % (inline(tD), inline(bD.split('\n\n')[0].replace('\n',' ')), table(bD, 'tblD'), paras(re.sub(r'(?s)<svg.*?</svg>', '', _tail)), _svgD)
tE0, bE0 = appendix('E')
apx += '<details id="apx-e0"><summary>Appendix E &mdash; %s</summary><div class="inner">\n%s\n%s\n</div></details>\n' % (inline(tE0), paras(bE0.split('\n\n')[0]), table(bE0[bE0.index('| Season pair'):], 'tblE0') + paras(re.sub(r'(?s)<svg.*?</svg>', '', bE0[bE0.index('**Reading it'):])) + '<figure>' + re.search(r'(?s)<svg.*?</svg>', bE0).group(0) + '<figcaption>Derived by the case author from the ten Wikipedia season tables in Appendix G. Each dot is one club-pair.</figcaption></figure>')
tE, bE = appendix('F')
svg = re.search(r'(?s)<svg.*?</svg>', bE).group(0)
apx += '<details id="apx-e"><summary>Appendix F &mdash; %s</summary><div class="inner">\n%s\n<figure>%s<figcaption>Invented illustration: made-up dots from a different subject, with no numbers. It is not this case\'s data.</figcaption></figure>\n</div></details>\n' % (inline(tE), paras(re.sub(r'(?s)<svg.*?</svg>', '', bE)), svg)
tF, bF = appendix('G')
apx += '<details id="apx-f"><summary>Appendix G &mdash; %s</summary><div class="inner">\n%s\n</div></details>\n' % (inline(tF), table(bF, 'tblF'))
R["{{CASE_APPENDICES_A_THROUGH_F}}"] = apx

R["{{CASE_NOTEBOOK_STEPS}}"] = """
  <div class="stepbox">
    <h4>Step 1 &mdash; The line of best fit (D1)</h4>
    <div class="goal">Fit a line to all 20 clubs (goal difference on the horizontal axis, points on the vertical axis) and enter its slope and intercept.</div>
    <div class="fieldrow"><label for="s1slope">Slope (points per goal)</label><input type="number" id="s1slope" step="any" placeholder="a decimal number"><span id="fb1a" class="fb"></span></div>
    <div class="fieldrow"><label for="s1int">Intercept (points)</label><input type="number" id="s1int" step="any" placeholder="a decimal number"><span id="fb1b" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; The club's residual and the residual spread (D2)</h4>
    <div class="goal">Using the 20-club line, find the club's residual (actual minus predicted points) and the residual spread of all 20 clubs (Appendix F's recipe, dividing by the number of clubs minus 2).</div>
    <div class="fieldrow"><label for="s2res">Club's residual (points)</label><input type="number" id="s2res" step="any" placeholder="a decimal number, negative if below the line"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2sd">Residual spread, 20 clubs (points)</label><input type="number" id="s2sd" step="any" placeholder="a decimal number"><span id="fb2b" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 3 &mdash; The outlier check (D3)</h4>
    <div class="goal">Refit the line with the club's row removed. Find the club's residual against the new line, the other 19 clubs' residual spread, and how many spreads below the line the club sits.</div>
    <div class="fieldrow"><label for="s3res">Club's residual against the 19-club line (points)</label><input type="number" id="s3res" step="any" placeholder="a decimal number"><span id="fb3a" class="fb"></span></div>
    <div class="fieldrow"><label for="s3sd">Residual spread, other 19 clubs (points)</label><input type="number" id="s3sd" step="any" placeholder="a decimal number"><span id="fb3b" class="fb"></span></div>
    <div class="fieldrow"><label for="s3z">Residual spreads below the line (a positive number)</label><input type="number" id="s3z" step="any" placeholder="a decimal number"><span id="fb3c" class="fb"></span></div>
    <button onclick="checkStep3()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 4 &mdash; Forecast shortfall and the break-even (D4)</h4>
    <div class="goal">Using the 19-club line as the model of record and Appendix E's slope, forecast the club's next-season shortfall under Keep the Winner, find its expected points, and find the break-even reset cost. Your own reset-cost range and verdicts are for your write-up, not this box.</div>
    <div class="fieldrow"><label for="s4a">Forecast next-season shortfall, Keep the Winner (points)</label><input type="number" id="s4a" step="any" placeholder="a decimal number"><span id="fb4a" class="fb"></span></div>
    <div class="fieldrow"><label for="s4b">Expected points, Keep the Winner</label><input type="number" id="s4b" step="any" placeholder="a decimal number"><span id="fb4b" class="fb"></span></div>
    <div class="fieldrow"><label for="s4be">Break-even reset cost (points)</label><input type="number" id="s4be" step="any" placeholder="a decimal number"><span id="fb4c" class="fb"></span></div>
    <button onclick="checkStep4()">Check</button>
    <p class="side-note">These checks only confirm your arithmetic. Which option to choose, and which reset cost you believe, is still yours.</p>
  </div>
"""

R["{{CASE_TWIST_NARRATIVE}}"] = """
      <p>The analyst adds one fact. In the ten seasons behind Appendix E, no club ever finished as far below its own season's line as this club did; the largest earlier miss was smaller. The slope was fitted on typical clubs, not on a miss this size. Suppose, for the next five minutes, that for a miss this size the slope is <strong>the top of Appendix E's range, 0.27</strong>, not 0.11. Change After 17th still pays only its reset cost. This is a what-if, not a measured fact.</p>
"""
R["{{CASE_TWIST_APPLY_LABEL}}"] = "Apply the twist to Step 4's check (use slope 0.27 instead of 0.11)"

R["{{CASE_SOURCES_LIST}}"] = """
      <li>[S1] Wikipedia &mdash; <a href="https://en.wikipedia.org/wiki/2024%E2%80%9325_Premier_League" target="_blank" rel="noopener">2024&ndash;25 Premier League</a></li>
      <li>[S2] Wikipedia &mdash; <a href="https://en.wikipedia.org/wiki/2024%E2%80%9325_Tottenham_Hotspur_F.C._season" target="_blank" rel="noopener">2024&ndash;25 Tottenham Hotspur F.C. season</a></li>
      <li>[S3] Wikipedia &mdash; <a href="https://en.wikipedia.org/wiki/UEFA_Europa_League" target="_blank" rel="noopener">UEFA Europa League</a></li>
      <li>[S4] Premier League &mdash; <a href="https://www.premierleague.com/en/news/4208927" target="_blank" rel="noopener">Spurs face injury crisis with all four senior centre-backs injured</a></li>
      <li>[S5] Football-Data.co.uk &mdash; <a href="https://www.football-data.co.uk/data.php" target="_blank" rel="noopener">Data page</a></li>
      <li>[S6] StatsBomb &mdash; <a href="https://github.com/statsbomb/open-data" target="_blank" rel="noopener">open-data repository</a></li>
      <li>[S7] Understat &mdash; <a href="https://understat.com/league/EPL" target="_blank" rel="noopener">EPL page</a></li>
      <li>[S8] Wikipedia &mdash; <a href="https://en.wikipedia.org/wiki/Promotion_and_relegation" target="_blank" rel="noopener">Promotion and relegation</a></li>
      <li>[S14]&ndash;[S23] Wikipedia season pages, 2015&ndash;16 to 2024&ndash;25 Premier League (CC BY-SA), used for the derived Appendix E; listed with links in Appendix G.</li>
"""

R["{{CASE_JS_DATA_BLOCK}}"] = """
// Ported from cases/the-trophy-and-the-table/sensitivity_model.py. Raw given data and assumptions only.
const TABLE = [
  ["Liverpool",45,84],["Arsenal",35,74],["Manchester City",28,71],["Chelsea",21,69],["Newcastle United",21,66],
  ["Aston Villa",7,66],["Nottingham Forest",12,65],["Brighton & Hove Albion",7,61],["AFC Bournemouth",12,56],
  ["Brentford",9,56],["Fulham",0,54],["Crystal Palace",0,53],["Everton",-2,48],["West Ham United",-16,43],
  ["Manchester United",-10,42],["Wolverhampton Wanderers",-15,42],["Tottenham Hotspur",-1,38],
  ["Leicester City",-47,25],["Ipswich Town",-46,22],["Southampton",-60,12]
];
const CLUB = "Tottenham Hotspur";
const PARAMS = { a: 0.11, d: 2.0, a_twist: 0.27 };
const FLEX = ["a", "d"];
function fitLine(rows){
  const n = rows.length;
  const mx = rows.reduce((s,r)=>s+r[1],0)/n, my = rows.reduce((s,r)=>s+r[2],0)/n;
  let sxx=0, sxy=0; rows.forEach(r=>{ sxx += (r[1]-mx)*(r[1]-mx); sxy += (r[1]-mx)*(r[2]-my); });
  const slope = sxy/sxx, intercept = my - slope*mx;
  let sse = 0; rows.forEach(r=>{ const e = r[2]-(intercept+slope*r[1]); sse += e*e; });
  return {slope, intercept, sd: Math.sqrt(sse/(n-2))};
}
const FULL = fitLine(TABLE);
const OTHERS = TABLE.filter(r => r[0] !== CLUB);
const LOO = fitLine(OTHERS);
const CLUB_ROW = TABLE.filter(r => r[0] === CLUB)[0];
const FULL_PRED = FULL.intercept + FULL.slope*CLUB_ROW[1];
const LOO_PRED = LOO.intercept + LOO.slope*CLUB_ROW[1];
function evaluate(params){
  const p = Object.assign({}, PARAMS, params||{});
  const shortfall = Math.abs(CLUB_ROW[2] - LOO_PRED);
  return {A: LOO_PRED - p.a*shortfall, B: LOO_PRED - p.d};
}
function evaluate_twist(params){
  const p = Object.assign({}, PARAMS, params||{});
  const shortfall = Math.abs(CLUB_ROW[2] - LOO_PRED);
  return {A: LOO_PRED - p.a_twist*shortfall, B: LOO_PRED - p.d};
}
"""

R["{{CASE_NOTEBOOK_CHECK_FUNCTIONS}}"] = """
function checkStep1(){
  fb('fb1a', near(parseFloat(val('s1slope')), FULL.slope, 0.003));
  fb('fb1b', near(parseFloat(val('s1int')), FULL.intercept, 0.03));
}
function checkStep2(){
  fb('fb2a', near(parseFloat(val('s2res')), CLUB_ROW[2]-FULL_PRED, 0.06));
  fb('fb2b', near(parseFloat(val('s2sd')), FULL.sd, 0.03));
}
function checkStep3(){
  const res = CLUB_ROW[2]-LOO_PRED;
  fb('fb3a', near(parseFloat(val('s3res')), res, 0.06));
  fb('fb3b', near(parseFloat(val('s3sd')), LOO.sd, 0.03));
  fb('fb3c', near(parseFloat(val('s3z')), Math.abs(res)/LOO.sd, 0.03));
}
function checkStep4(){
  const slope = window.__TWIST_APPLIED__ ? PARAMS.a_twist : PARAMS.a;
  const shortfall = Math.abs(CLUB_ROW[2]-LOO_PRED);
  fb('fb4a', near(parseFloat(val('s4a')), slope*shortfall, 0.06));
  fb('fb4b', near(parseFloat(val('s4b')), LOO_PRED - slope*shortfall, 0.06));
  fb('fb4c', near(parseFloat(val('s4be')), slope*shortfall, 0.06));
}
"""
R["{{CASE_ON_TWIST_TOGGLE_FUNCTION}}"] = """
function onTwistToggle(){
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
}
""" + '\nconst STORY_GLOSSARY = {\n  "Europa League": {desc: "A European club soccer tournament that sits one step below the Champions League. Clubs from many countries qualify by how they finish in their home leagues, and the winner earns a place in the next Champions League.",\n    link: "https://en.wikipedia.org/wiki/UEFA_Europa_League"},\n  "Champions League": {desc: "The top European club soccer tournament, contested by leading clubs from many countries and one of the competitions clubs most want to qualify for.",\n    link: "https://en.wikipedia.org/wiki/UEFA_Champions_League"},\n  "manager": {desc: "In British football, the head coach: the person with overall responsibility for running the team, including picking the squad and setting tactics.",\n    link: "https://en.wikipedia.org/wiki/Manager_(association_football)"},\n  "centre-back": {desc: "A central defender, whose main job is to defend the area in front of the goal and stop the other team from scoring.",\n    link: "https://en.wikipedia.org/wiki/Defender_(association_football)"},\n  "relegated": {desc: "Sent down to a lower division. In the Premier League the bottom three of 20 clubs drop to the second division at the end of a season.",\n    link: "https://en.wikipedia.org/wiki/Promotion_and_relegation"},\n  "goal difference": {desc: "Goals a club scored in league games minus goals it conceded. A club that scores 64 and concedes 65 has a goal difference of minus 1.",\n    link: "https://en.wikipedia.org/wiki/Goal_difference"}\n};\nfunction stermHTML(label, textOverride){\n  const g = STORY_GLOSSARY[label];\n  if(!g) return textOverride || label;\n  const text = textOverride || label;\n  return `<a class="sterm" data-sterm="${label}" href="${g.link}" target="_blank" rel="noopener">${text}<span class="tip">${g.desc}<span class="go">Open a real source on this &rarr;</span></span></a>`;\n}\nfunction renderStoryGlossary(){\n  const el = document.getElementById(\'storyGlossaryGrid\');\n  if(!el) return;\n  el.innerHTML = Object.keys(STORY_GLOSSARY).map(k => stermHTML(k)).join(\'\');\n}\nrenderStoryGlossary();\nfunction autoLinkStoryTerms(containerSelectors){\n  const linked = new Set();\n  const terms = Object.keys(STORY_GLOSSARY).sort((a, b) => b.length - a.length);\n  const esc = s => s.replace(/[.*+?^${}()|[\\]\\\\]/g, \'\\\\$&\');\n  const master = new RegExp(\'\\\\b(\' + terms.map(t => esc(t) + \'s?\').join(\'|\') + \')\\\\b\', \'gi\');\n  const keyFor = raw => terms.find(t => raw.toLowerCase() === t.toLowerCase() || raw.toLowerCase() === (t + \'s\').toLowerCase());\n  const skip = \'script, style, .gterm, .sterm, #apx-glossary, #storyGlossaryCard, button, input, select, textarea, label\';\n  const roots = [];\n  containerSelectors.forEach(sel => document.querySelectorAll(sel).forEach(el => roots.push(el)));\n  roots.forEach(root => {\n    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {acceptNode(node){\n      if(!node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;\n      const p = node.parentElement;\n      if(!p || p.closest(skip)) return NodeFilter.FILTER_REJECT;\n      return NodeFilter.FILTER_ACCEPT; }});\n    const nodes = []; let n; while((n = walker.nextNode())) nodes.push(n);\n    nodes.forEach(node => {\n      const text = node.nodeValue; master.lastIndex = 0;\n      let m, lastEnd = 0, frag = null;\n      while((m = master.exec(text))){\n        const key = keyFor(m[0]);\n        if(!key || linked.has(key)) continue;\n        linked.add(key);\n        if(!frag) frag = document.createDocumentFragment();\n        if(m.index > lastEnd) frag.appendChild(document.createTextNode(text.slice(lastEnd, m.index)));\n        const span = document.createElement(\'span\'); span.innerHTML = stermHTML(key, m[0]);\n        frag.appendChild(span.firstChild); lastEnd = m.index + m[0].length;\n      }\n      if(frag){ if(lastEnd < text.length) frag.appendChild(document.createTextNode(text.slice(lastEnd))); node.parentNode.replaceChild(frag, node); }\n    });\n  });\n}\nautoLinkStoryTerms([\'#overview\', \'#background\', \'#dilemma\', \'#challenges\', \'#appendices\', \'#notebook\', \'#twist\']);\n'
R["{{CASE_GLOSSARY_OBJECT}}"] = """{
  "Scatter Plot": {def: "A graph that shows each item as one dot, placed by two measurements (here, goal difference across and points up), so you can see how the two move together.",
    url: "https://www.mathsisfun.com/data/scatter-xy-plots.html"},
  "Correlation": {def: "How strongly and in which direction two sets of numbers move together. Strong correlation does not by itself show that one causes the other.",
    url: "https://www.mathsisfun.com/data/correlation.html"},
  "Line Of Best Fit": {def: "The straight line that comes closest to all the dots on a scatter plot, found by making the squared gaps from the dots to the line as small as possible.",
    url: "https://www.mathsisfun.com/data/least-squares-regression.html"},
  "Slope": {def: "How steep a line is: how much it rises (or falls) for each step across. On this case's line, points gained per extra goal of goal difference.",
    url: "https://www.mathsisfun.com/geometry/slope.html"},
  "Mean": {def: "The average: add up every value, then divide by how many values there are.",
    url: "https://www.mathsisfun.com/mean.html"},
  "Outlier": {def: "A value that lies far outside most of the others in a data set.",
    url: "https://www.mathsisfun.com/definitions/outlier.html"},
  "Variability": {def: "How spread out a set of numbers is. The residual spread in Appendix F is one way to measure it.",
    url: "https://www.mathsisfun.com/data/standard-deviation.html"},
  "Percent": {def: "A ratio that compares a number to 100, literally per hundred.",
    url: "https://www.mathsisfun.com/percentage.html"}
}"""
R["{{CASE_HOWTO_ARRAY}}"] = """[
  ["how to create a scatter plot given a set of data", "Scatter Plot"],
  ["how to identify correlation given a scatter plot or set of data", "Correlation"],
  ["how to draw a line of best fit given a set of data", "Line Of Best Fit"],
  ["how to identify the slope of a line given a set of data, or a graph of a line of a set of data, or its linear equation", "Slope"],
  ["how to find the mean of a set of data", "Mean"],
  ["how to find the percent of a number", "Percent"]
]"""

for k, v in R.items():
    if k not in html:
        raise SystemExit("MISSING PLACEHOLDER IN SHELL: " + k)
    html = html.replace(k, v)
left = [m for m in re.findall(r'\{\{[A-Z_0-9]+\}\}', html) if m != '{{PLACEHOLDER}}']
if left:
    raise SystemExit("Unfilled placeholders remain: %s" % left)
open(OUT, "w", encoding="utf-8").write(html)
print("wrote", OUT)
