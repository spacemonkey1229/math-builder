#!/usr/bin/env python3
"""Fill templates/interactive_shell.html for The Eight-Second Tour (case-local build script, same
precedent as cases/the-grade-rule/build_html.py and cases/the-trophy-and-the-table/build_html.py).
Content is converted from case.md so the two cannot drift; the JS notebook is a port of
sensitivity_model.py. Writes only inside cases/the-eight-second-tour/published/."""
import re, os, json, base64, html as H

PROJECT = "/Users/manan/Documents/Claude/Projects/Math Builder"
CASE = f"{PROJECT}/cases/the-eight-second-tour"
SHELL = f"{PROJECT}/templates/interactive_shell.html"
OUT_DIR = f"{CASE}/published"
OUT = f"{OUT_DIR}/The Eight-Second Tour - Interactive.html"
os.makedirs(OUT_DIR, exist_ok=True)
md = open(f"{CASE}/case.md", encoding="utf-8").read()
md = re.split(r'<!--\s*FACILITATOR ONLY', md)[0] + (md.split('-->', 1)[1] if '<!-- FACILITATOR ONLY' in md else '')
cj = json.load(open(f"{CASE}/case.json", encoding="utf-8"))
import shutil
shutil.copy(f"{CASE}/assets/lemond_1989_stage21_start.jpg", f"{OUT_DIR}/lemond_1989_stage21_start.jpg")


def sect(title_re):
    m = re.search(r'(?ms)^## ' + title_re + r'.*?\n(.*?)(?=^---\s*$|\Z)', md)
    return m.group(1).strip()


def inline(t):
    t = H.escape(t, quote=False)
    t = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', t)
    return t


_tid = [0]


def table_html(rows):
    cells = [[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
    hdr, body = cells[0], cells[2:]
    _tid[0] += 1
    h = '<table id="tbl%d"><tr>%s</tr>\n' % (_tid[0], ''.join('<th>%s</th>' % inline(c) for c in hdr))
    for r in body:
        h += '<tr>%s</tr>\n' % ''.join('<td>%s</td>' % inline(c) for c in r)
    return h + '</table>'


def blocks(block):
    """minimal markdown -> html: paragraphs, tables, bullet lists, images, raw svg, blockquotes"""
    out, lines, i = [], block.strip().split('\n'), 0
    while i < len(lines):
        l = lines[i]
        if not l.strip():
            i += 1; continue
        if l.lstrip().startswith('<svg'):
            j = i
            while '</svg>' not in lines[j]:
                j += 1
            out.append('<figure>' + '\n'.join(lines[i:j + 1]) + '</figure>'); i = j + 1; continue
        if l.strip().startswith('|'):
            j = i
            while j < len(lines) and lines[j].strip().startswith('|'):
                j += 1
            out.append(table_html(lines[i:j])); i = j; continue
        if l.startswith('!['):
            m = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', l)
            cap = ''
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and lines[j].startswith('*'):
                cap = lines[j]; i = j
            out.append('<figure><img src="lemond_1989_stage21_start.jpg" alt="%s" style="max-width:100%%;height:auto;border-radius:6px;display:block;margin:0 auto"><figcaption>%s</figcaption></figure>' % (H.escape(m.group(1)), inline(cap.strip('*'))))
            i += 1; continue
        if l.startswith('- '):
            items = []
            while i < len(lines) and lines[i].startswith('- '):
                items.append(lines[i][2:]); i += 1
            out.append('<ul>' + ''.join('<li>%s</li>' % inline(x) for x in items) + '</ul>'); continue
        if l.startswith('> '):
            out.append('<blockquote>%s</blockquote>' % inline(l[2:])); i += 1; continue
        para = [l]; i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith(('|', '- ', '![', '> ')) and not lines[i].lstrip().startswith('<svg'):
            para.append(lines[i]); i += 1
        out.append('<p>' + inline(' '.join(para)) + '</p>')
    return '\n'.join(out)


def appendix(letter):
    m = re.search(r'(?ms)^## Appendix %s — (.*?)\n(.*?)(?=^---\s*$)' % letter, md)
    return m.group(1).strip(), m.group(2).strip()


html = open(SHELL, encoding="utf-8").read()
R = {}
R["{{CASE_TITLE}}"] = "The Eight-Second Tour"
R["{{CASE_YEAR}}"] = "2026-27"
R["{{CASE_TIER}}"] = "T3"
R["{{CASE_BAND}}"] = "MS-Stretch / HS-Entry"
R["{{CASE_STRAND_SUMMARY}}"] = "Ratios &middot; Percent &middot; Cube Law &middot; Break-Even &middot; Linear Equations"
R["{{CASE_ID}}"] = "the-eight-second-tour"
R["{{CASE_GLOSSARY_APPENDIX_LETTER}}"] = "Appendix F"
R["{{CASE_GLOSSARY_VERIFIED_DATE}}"] = "2026-10-04"
R["{{CASE_PROTAGONIST}}"] = "the sports director of Greg LeMond's team"
R["{{CASE_OPTION_A_LABEL}}"] = "Aero Bars"
R["{{CASE_OPTION_A_TEXT}}"] = "Commit LeMond to the aero position, with lower drag and less sustainable power."
R["{{CASE_OPTION_B_LABEL}}"] = "Full Power"
R["{{CASE_OPTION_B_TEXT}}"] = "Ride LeMond in the conventional position at full power."
R["{{CASE_SPECIFIC_CSS}}"] = (".num{text-align:right;font-variant-numeric:tabular-nums}\n  "
    "figure{margin:14px 0}figcaption{font-size:.82rem;color:#555;margin-top:6px}\n  "
    "#storyGlossaryCard{margin-top:12px}.glossary-grid{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 16px}")
R["{{CASE_SPECIFIC_ICON_SYMBOLS}}"] = ""
R["{{CASE_OVERVIEW_BANNER_SVG}}"] = ""

ov = sect('Overview').split('\n\n')
R["{{CASE_OVERVIEW_TEXT}}"] = '<p class="lede">' + inline(ov[0].replace('\n', ' ')) + '</p>\n' + blocks('\n\n'.join(ov[1:]))
R["{{CASE_BACKGROUND_TEXT}}"] = blocks(sect('Background')) + (
    '\n<div class="card" id="storyGlossaryCard"><strong>Cycling Vocabulary</strong><p class="side-note" style="margin-top:6px">'
    'Hover any underlined term below (or in the prose above) for a plain-English definition; click to open a real source on it. '
    'This is separate from the math vocabulary in Appendix F &mdash; these are the cycling words the story itself is told in.</p>'
    '<div class="glossary-grid" id="storyGlossaryGrid"></div></div>')
R["{{CASE_CHALLENGE_3_DELIVERABLES_SUMMARY}}"] = (
    "Include: <strong>D1</strong> a times-and-speeds table with the baseline range; <strong>D2</strong> the needed power factor at each end of the baseline; "
    "<strong>D3</strong> a break-even table (aero-only and full model); <strong>D4</strong> an original break-even chart, line, shares and decision rule; "
    "<strong>D5</strong> model limits. The full wording of each deliverable is in the case document.")
R["{{CASE_DELIVERABLES_ARRAY}}"] = """[
  ["D1", "Times-and-speeds table and baseline range"],
  ["D2", "Needed power factor at each end of the baseline"],
  ["D3", "Break-even table (aero-only and full model)"],
  ["D4", "Break-even chart, line, shares and decision rule"],
  ["D5", "Model limits in numbers and words"]
]"""

apx = ""
for letter, opn in (('A', ' open'), ('B', ''), ('C', ''), ('D', ''), ('E', '')):
    t, b = appendix(letter)
    apx += '<details%s id="apx-%s"><summary>Appendix %s &mdash; %s</summary><div class="inner">\n%s\n</div></details>\n' % (opn, letter.lower(), letter, inline(t), blocks(b))
R["{{CASE_APPENDICES_A_THROUGH_F}}"] = apx

R["{{CASE_NOTEBOOK_STEPS}}"] = """
  <div class="stepbox">
    <h4>Step 1 &mdash; The baseline and the total ratio (D1)</h4>
    <div class="goal">Find LeMond/Fignon speed ratios from Appendix A, then enter the low and high ends of the baseline range b and the total speed ratio LeMond needs over Fignon's 27:55 pace (four decimal places).</div>
    <div class="fieldrow"><label for="s1lo">Baseline b, low end</label><input type="number" id="s1lo" step="any" placeholder="decimal"><span id="fb1a" class="fb"></span></div>
    <div class="fieldrow"><label for="s1hi">Baseline b, high end</label><input type="number" id="s1hi" step="any" placeholder="decimal"><span id="fb1b" class="fb"></span></div>
    <div class="fieldrow"><label for="s1tot">Total speed ratio needed over Fignon</label><input type="number" id="s1tot" step="any" placeholder="decimal"><span id="fb1c" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; The needed power factor (D2)</h4>
    <div class="goal">Using the cube law, find the factor by which power must rise for the aero position to supply what the baseline leaves, at the low end and at the high end of the baseline range.</div>
    <div class="fieldrow"><label for="s2lo">Power factor, low-end baseline</label><input type="number" id="s2lo" step="any" placeholder="decimal"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2hi">Power factor, high-end baseline</label><input type="number" id="s2hi" step="any" placeholder="decimal"><span id="fb2b" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 3 &mdash; Break-even power loss (D3)</h4>
    <div class="goal">Enter the largest power loss y, in percent, that still reaches the bar. Aero-only form at a 10% drag-area cut, for each end of the baseline; then the full model at a 10% cut for the low-end baseline.</div>
    <div class="fieldrow"><label for="s3a">Aero-only, 10% cut, low-end baseline (%)</label><input type="number" id="s3a" step="any" placeholder="decimal"><span id="fb3a" class="fb"></span></div>
    <div class="fieldrow"><label for="s3b">Aero-only, 10% cut, high-end baseline (%)</label><input type="number" id="s3b" step="any" placeholder="decimal"><span id="fb3b" class="fb"></span></div>
    <div class="fieldrow"><label for="s3c">Full model, 10% cut, low-end baseline (%)</label><input type="number" id="s3c" step="any" placeholder="decimal"><span id="fb3c" class="fb"></span></div>
    <button onclick="checkStep3()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 4 &mdash; Your own pair (D4)</h4>
    <div class="goal">Enter the drag-area cut x and power loss y (in percent) you believe, then the aero position's speed ratio over the conventional position for that pair (four decimal places).</div>
    <div class="fieldrow"><label for="s4x">Your x (%)</label><input type="number" id="s4x" step="any" placeholder="decimal"></div>
    <div class="fieldrow"><label for="s4y">Your y (%)</label><input type="number" id="s4y" step="any" placeholder="decimal"></div>
    <div class="fieldrow"><label for="s4r">Aero speed ratio over conventional</label><input type="number" id="s4r" step="any" placeholder="decimal"><span id="fb4a" class="fb"></span></div>
    <button onclick="checkStep4()">Check</button>
    <p class="side-note">These checks only confirm your arithmetic. Which option to choose, which decision rule to use, and whether the assumptions deserve your trust, is still yours.</p>
  </div>

  <div class="stepbox">
    <h4>Step 5 &mdash; Model limits (D5)</h4>
    <div class="goal">Use the full model at LeMond's real 26:57 average speed and enter the power it implies, in watts, to the nearest whole watt.</div>
    <div class="fieldrow"><label for="s5w">Implied power (W)</label><input type="number" id="s5w" step="any" placeholder="watts"><span id="fb5a" class="fb"></span></div>
    <button onclick="checkStep5()">Check</button>
  </div>
"""

R["{{CASE_TWIST_NARRATIVE}}"] = """
      <p>Your team physiologist comes in with a number: a lab estimate for the aero position. It is not a measurement from the race. It is a hypothetical, built for tonight.</p>
      <p>Drag area down by twelve and a half percent. Sustainable power down by fourteen. Both numbers are inside the ranges in your own Appendix D.</p>
      <p>Treat them as the only estimate of the aero position you have tonight: they replace your own x and y. Run it again. Are you changing your recommendation, or not?</p>
"""
R["{{CASE_TWIST_APPLY_LABEL}}"] = "Apply the twist to Step 4's check (x and y replaced by the twist's values)"

srcs = [
    ("S1", "Wikipedia", "1989 Tour de France", "https://en.wikipedia.org/wiki/1989_Tour_de_France"),
    ("S2", "Wikimedia Commons", "File:Greg LeMond 1989 Tour de France stage 21 TT.jpg (Benjamin Werner, CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Greg_LeMond_1989_Tour_de_France_stage_21_TT.jpg"),
    ("S3", "PubMed", "Garc&iacute;a-L&oacute;pez et al. 2008, J Sports Sci", "https://pubmed.ncbi.nlm.nih.gov/17943597/"),
    ("S4", "PubMed", "Fintelman et al. 2014, J Biomech", "https://pubmed.ncbi.nlm.nih.gov/24726654/"),
    ("S5", "Wikipedia", "1989 Tour de France, Prologue to Stage 10", "https://en.wikipedia.org/wiki/1989_Tour_de_France,_Prologue_to_Stage_10"),
    ("S6", "Wikipedia", "1989 Tour de France, Stage 11 to Stage 21", "https://en.wikipedia.org/wiki/1989_Tour_de_France,_Stage_11_to_Stage_21"),
]
R["{{CASE_SOURCES_LIST}}"] = "\n".join('      <li>[%s] %s &mdash; <a href="%s" target="_blank" rel="noopener">%s</a></li>' % s for s in srcs)

R["{{CASE_JS_DATA_BLOCK}}"] = """
// Ported from cases/the-eight-second-tour/sensitivity_model.py. Given data and stated assumptions only.
const DIST_KM = 24.5, RIVAL_S = 1675, DEFICIT_S = 50;
const RHO = 1.225, CDA0 = 0.32, MASS = 78, CRR = 0.004, G = 9.81;
const B_LOW = 1.0, B_HIGH = 4346/4299;
const PARAMS = { cda_cut: 0.125, power_loss: 0.085, twist_cda_cut: 0.125, twist_power_loss: 0.14, baseline_ratio: (B_LOW + B_HIGH)/2 };
const FLEX = ["cda_cut", "power_loss"];
const needed = () => RIVAL_S/(RIVAL_S-DEFICIT_S);
const speedRatio = (x,y) => Math.pow((1-y)/(1-x), 1/3);
const power = (v,cda) => 0.5*RHO*cda*Math.pow(v,3) + CRR*MASS*G*v;
function cubeBreakEven(x,b){ return 1 - Math.pow(needed()/b,3)*(1-x); }
function fullBreakEven(x,b){
  const v0 = DIST_KM*1000/RIVAL_S*b, v1 = DIST_KM*1000/RIVAL_S*needed();
  return 1 - power(v1, CDA0*(1-x))/power(v0, CDA0);
}
function evaluate(params){
  const p = Object.assign({}, PARAMS, params||{});
  const v0 = DIST_KM/(RIVAL_S/3600)*p.baseline_ratio;
  return {A: v0*speedRatio(p.cda_cut, p.power_loss), B: v0};
}
function evaluate_twist(params){
  const p = Object.assign({}, PARAMS, params||{});
  const v0 = DIST_KM/(RIVAL_S/3600)*p.baseline_ratio;
  return {A: v0*speedRatio(p.twist_cda_cut, p.twist_power_loss), B: v0};
}
"""

R["{{CASE_NOTEBOOK_CHECK_FUNCTIONS}}"] = """
function checkStep1(){
  fb('fb1a', near(parseFloat(val('s1lo')), B_LOW, 0.0003));
  fb('fb1b', near(parseFloat(val('s1hi')), B_HIGH, 0.0003));
  fb('fb1c', near(parseFloat(val('s1tot')), needed(), 0.0003));
}
function checkStep2(){
  fb('fb2a', near(parseFloat(val('s2lo')), Math.pow(needed()/B_LOW,3), 0.001));
  fb('fb2b', near(parseFloat(val('s2hi')), Math.pow(needed()/B_HIGH,3), 0.001));
}
function checkStep3(){
  fb('fb3a', near(parseFloat(val('s3a')), 100*cubeBreakEven(0.10, B_LOW), 0.06));
  fb('fb3b', near(parseFloat(val('s3b')), 100*cubeBreakEven(0.10, B_HIGH), 0.06));
  fb('fb3c', near(parseFloat(val('s3c')), 100*fullBreakEven(0.10, B_LOW), 0.06));
}
function checkStep4(){
  let x = parseFloat(val('s4x'))/100, y = parseFloat(val('s4y'))/100;
  if(window.__TWIST_APPLIED__){ x = PARAMS.twist_cda_cut; y = PARAMS.twist_power_loss; }
  fb('fb4a', near(parseFloat(val('s4r')), speedRatio(x,y), 0.0006));
}
function checkStep5(){
  const v = DIST_KM*1000/1617;
  fb('fb5a', near(parseFloat(val('s5w')), power(v, CDA0), 1.5));
}
"""
R["{{CASE_ON_TWIST_TOGGLE_FUNCTION}}"] = """
function onTwistToggle(){
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
}
"""
R["{{CASE_GLOSSARY_OBJECT}}"] = """{
  "Time": {def: "How long something takes. Here, race times such as 26:57 (minutes:seconds) that must be converted to seconds before dividing distance by time.",
    url: "https://www.mathsisfun.com/time.html"},
  "Percent": {def: "A ratio that compares a number to 100, literally per hundred.",
    url: "https://www.mathsisfun.com/percentage.html"},
  "Ratio": {def: "A comparison of two quantities by division. Here, one rider's speed divided by another's.",
    url: "https://www.mathsisfun.com/numbers/ratio.html"},
  "Exponent": {def: "A small raised number saying how many times to multiply a number by itself. Cubing a speed ratio means using the exponent 3.",
    url: "https://www.mathsisfun.com/exponent.html"},
  "Variable": {def: "A letter standing for a number that can change, such as x for the drag-area cut or y for the power loss.",
    url: "https://www.mathsisfun.com/definitions/variable.html"},
  "Equation": {def: "A statement that two expressions are equal, such as the break-even condition you solve for y.",
    url: "https://www.mathsisfun.com/definitions/equation.html"},
  "Scatter Plot": {def: "A graph that shows each item as one dot, placed by two measurements, so you can see how they move together.",
    url: "https://www.mathsisfun.com/data/scatter-xy-plots.html"},
  "Slope": {def: "How steep a line is: how much it rises for each step across. For the break-even line, points of tolerable power loss per point of drag cut.",
    url: "https://www.mathsisfun.com/geometry/slope.html"},
  "Linear Equation": {def: "An equation whose graph is a straight line, such as y = mx + b.",
    url: "https://www.mathsisfun.com/algebra/linear-equations.html"}
}"""
R["{{CASE_HOWTO_ARRAY}}"] = """[
  ["how to convert between units of time", "Time"],
  ["how to convert numbers to percents", "Percent"],
  ["how to convert percents to numbers", "Percent"],
  ["how to evaluate an exponential expression", "Exponent"],
  ["how to evaluate a variable expression (substitution property)", "Variable"],
  ["how to solve a multi-step equation with a variable on one side", "Equation"],
  ["how to create a scatter plot given a set of data", "Scatter Plot"],
  ["how to identify the slope of a line given a set of data, or a graph of a line of a set of data, or its linear equation", "Slope"],
  ["how to write a linear equation given a set of data", "Linear Equation"]
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
