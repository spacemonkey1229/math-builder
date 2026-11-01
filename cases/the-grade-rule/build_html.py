#!/usr/bin/env python3
"""Fill templates/interactive_shell.html for Grade Rule."""
import re

PROJECT = "/Users/manan/Documents/Claude/Projects/Math Builder"
SHELL = f"{PROJECT}/templates/interactive_shell.html"
OUT = f"{PROJECT}/cases/the-grade-rule/published/Grade Rule - Interactive.html"

html = open(SHELL, encoding="utf-8").read()
REPL = {}

REPL["{{CASE_TITLE}}"] = "Grade Rule"
REPL["{{CASE_YEAR}}"] = "2026-27"
REPL["{{CASE_TIER}}"] = "T2"
REPL["{{CASE_BAND}}"] = "MS-Core"
REPL["{{CASE_STRAND_SUMMARY}}"] = "Dilation &middot; Scale Factor &middot; Similarity"
REPL["{{CASE_ID}}"] = "the-grade-rule"
REPL["{{CASE_GLOSSARY_APPENDIX_LETTER}}"] = "Appendix E"
REPL["{{CASE_GLOSSARY_VERIFIED_DATE}}"] = "2026-09-18"
REPL["{{CASE_PROTAGONIST}}"] = "Devon Okafor"
REPL["{{CASE_OPTION_A_LABEL}}"] = "Uniform Dilation"
REPL["{{CASE_OPTION_A_TEXT}}"] = "One scale factor per size step, applied everywhere on the pattern."
REPL["{{CASE_OPTION_B_LABEL}}"] = "Point-Specific Grading"
REPL["{{CASE_OPTION_B_TEXT}}"] = "Each landmark point graded by its own real, individually-measured increment."
REPL["{{CASE_SPECIFIC_CSS}}"] = ""
REPL["{{CASE_SPECIFIC_ICON_SYMBOLS}}"] = ""
REPL["{{CASE_OVERVIEW_BANNER_SVG}}"] = ""

REPL["{{CASE_OVERVIEW_TEXT}}"] = """
  <p class="lede">Devon Okafor has the base-size pattern pinned flat on the light table and a factory deadline in three hours. Somewhere in the building, someone is already pulling fabric for the first cut of the new size run, and the grade rule &mdash; the set of instructions that turns one pattern into eight &mdash; has to be in their inbox before that fabric touches a blade.</p>
  <p>Every size in a run grows from the same base pattern, but bodies don't grow the same way at every point. A bust measurement climbs faster from size to size than a waist does, and a waist climbs faster than a shoulder. Scale the whole pattern up by one tidy percentage per size, and the math is fast, clean, and finished in an afternoon &mdash; but the pattern quietly stops matching real bodies the further a size sits from the middle of the run. Grade each point on the pattern by its own real, measured increment, and every size fits the way it should &mdash; but each of those separate increments has to be found and applied by hand, size by size, point by point.</p>
  <p>Devon's name goes on the tech pack. If a size doesn't fit and that size sells, the return rate lands on this decision.</p>
  <p>Devon uncaps a red pen and pulls the size chart closer.</p>
"""

REPL["{{CASE_BACKGROUND_TEXT}}"] = """
  <p>Devon Okafor is a pattern grader at a mid-size apparel company, responsible for turning the company's one approved base-size pattern into the full run of sizes the factory will cut this season. The grade rule Devon signs off on ships to the factory this week, and Devon's name is the one attached to it if a size in the run doesn't fit.</p>
  <p><strong>Uniform Dilation</strong> &mdash; scale every point on the base pattern by one single scale factor per size step, the same factor applied everywhere on the pattern, computed once and reused for the whole run. Fast to compute, cheap to produce, and mathematically a true dilation: every graded size is a perfect scaled copy of the base size.</p>
  <p><strong>Point-Specific Grading</strong> &mdash; grade each landmark point on the pattern (bust point, waist point, hip point) by its own real, individually-measured increment, matching how an actual body's proportions change from size to size rather than scaling everything by the same amount.</p>
  <p>A real, published body-measurement standard exists for exactly this purpose (SEE APPENDIX A). Because real bodies do not grow at the same rate everywhere, a single dilation factor tuned to fit the whole run reasonably well will still miss some landmarks at some sizes by more than the factory's stated fit tolerance (SEE APPENDIX B). A size Devon ships that misses tolerance at even one landmark is a size that does not reliably fit.</p>
"""

REPL["{{CASE_CHALLENGE_3_DELIVERABLES_SUMMARY}}"] = ("Include: <strong>D1</strong> a point-specific scale-factor "
    "table; <strong>D2</strong> a dilation scale-factor derivation; <strong>D3</strong> a dilated-pattern "
    "prediction table; <strong>D4</strong> a fit-check table; <strong>D5</strong> a cost, coverage, and "
    "decision memo.")

REPL["{{CASE_DELIVERABLES_ARRAY}}"] = """[
  ["D1", "Point-specific scale-factor table"],
  ["D2", "Dilation scale-factor derivation"],
  ["D3", "Dilated-pattern prediction table"],
  ["D4", "Fit-check table"],
  ["D5", "Cost, coverage, and decision memo"]
]"""

REPL["{{CASE_APPENDICES_A_THROUGH_F}}"] = """
<details open id="apx-a">
<summary>Appendix A &mdash; Real Body-Measurement Data by Size</summary>
<div class="inner">
<p>Drawn directly from a real published U.S. standard for adult female body measurements, ASTM D5585-11e1 [S1]. Base size = 12.</p>
<table id="tblA"><tr><th>Size</th><th>Bust (in)</th><th>Waist (in)</th><th>Hip (in)</th></tr>
<tr><td>8</td><td class="num">36.25</td><td class="num">29.5</td><td class="num">38.5</td></tr>
<tr><td>10</td><td class="num">37.25</td><td class="num">30.5</td><td class="num">39.5</td></tr>
<tr class="hi"><td><strong>12 (base)</strong></td><td class="num">38.75</td><td class="num">32.25</td><td class="num">41.0</td></tr>
<tr><td>14</td><td class="num">40.375</td><td class="num">34.0</td><td class="num">42.5</td></tr>
<tr><td>16</td><td class="num">42.125</td><td class="num">36.0</td><td class="num">44.25</td></tr>
</table>
<p class="side-note">The change from size to size is not the same at every landmark, and is not even constant across the run at a single landmark &mdash; the waist grows by 1.0in from size 8 to 10, but by 2.0in from size 14 to 16.</p>
</div></details>

<details id="apx-b">
<summary>Appendix B &mdash; Fit Tolerance</summary>
<div class="inner">
<table id="tblB"><tr><th>Quantity</th><th>Value</th></tr>
<tr><td>Stated fit tolerance, each landmark</td><td class="num">&plusmn;0.5 in [MA1]</td></tr>
</table>
</div></details>

<details id="apx-c">
<summary>Appendix C &mdash; Grading Labor</summary>
<div class="inner">
<table id="tblC"><tr><th>Quantity</th><th>Value</th></tr>
<tr><td>Median hourly wage, Fabric and Apparel Patternmakers (U.S.)</td><td class="num">$30.05/hr [S2]</td></tr>
<tr><td>Uniform Dilation: one-time setup time</td><td class="num">3.0 min [MA2]</td></tr>
<tr><td>Uniform Dilation: time per landmark, per size</td><td class="num">0.4 min [MA2]</td></tr>
<tr><td>Point-Specific: time per landmark, per size</td><td class="num">1.2 min [MA2]</td></tr>
<tr><td>Point-grades required (4 non-base sizes &times; 3 landmarks)</td><td class="num">12</td></tr>
</table>
</div></details>

<details id="apx-d">
<summary>Appendix D &mdash; Modeling Assumptions</summary>
<div class="inner">
<blockquote>These figures are <strong>not sourced</strong>. They are stated scenario assumptions chosen by the case author. A Hero may challenge them in discussion &mdash; that is a legitimate move.</blockquote>
<table id="tblD"><tr><th>#</th><th>Assumption</th><th>Value used</th><th>Sensitivity</th></tr>
<tr><td>MA1</td><td>Stated fit tolerance</td><td class="num">&plusmn;0.5 in</td><td>The single most dilemma-relevant assumption in the case.</td></tr>
<tr><td>MA2</td><td>Per-point grading time, each method</td><td>Uniform: 3.0min setup + 0.4min/pt; Point-Specific: 1.2min/pt</td><td>Both options' total labor cost scale directly with these rates.</td></tr>
</table>
</div></details>

<details id="apx-g">
<summary>Appendix G &mdash; Plain-English Notes on Real-World Terms</summary>
<div class="inner">
<p><strong>From a body measurement to a moved point.</strong> Appendix A gives body <em>circumference</em> measurements. A flat pattern piece only covers half the body (mirrored at the side seams), so a real patternmaker always halves the body circumference (plus a small ease allowance) to get the pattern's width at that landmark &mdash; a constant background step, identical under both options. What differs between the two methods is only the <em>scale factor</em> applied to that already-halved width, not the halving itself. This case is deliberately scoped to that width-only version of grading, not full two-directional (x-and-y) point repositioning.</p>
<p><strong>Picturing the grade rule, and exactly what Devon ships.</strong> A grade rule is not a machine or a single physical object &mdash; it is a table: one row per landmark point, one column per size, each cell holding a distance telling a cutter or grading machine exactly how far to move that point from the base pattern to produce that size's version. <strong>The table of numbers is the entire deliverable that goes in the factory's inbox.</strong> Devon does not personally redraw eight full patterns by hand &mdash; Devon builds and checks the numeric table, sends it, and the factory's own graders or grading software do the actual re-plotting downstream, by hand on a light table or automatically inside grading software.</p>
<table><tr><th>Term</th><th>Plain-English explanation</th></tr>
<tr><td>Light table</td><td>An illuminated table bright enough to see a pattern's lines through paper or fabric laid on top, used for tracing a pattern accurately by hand.</td></tr>
<tr><td>Grading room / cutting room</td><td>The workspace where patterns are graded, marked, and where fabric is laid out and cut.</td></tr>
<tr><td>Pulling fabric</td><td>Taking a bolt of fabric from storage and laying it out on a cutting table, the step right before cutting begins.</td></tr>
<tr><td>Cutting</td><td>Using a blade to cut fabric along a pattern's traced outline &mdash; a hand rotary cutter/straight knife for smaller runs, or a die press (a machine that stamps a cutting-die shape through stacked fabric layers at once, like a giant cookie cutter) for high-volume runs.</td></tr>
<tr><td>Tech pack</td><td>The complete technical document a factory receives describing exactly how to cut and sew a garment, including its grade rule.</td></tr>
<tr><td>ASTM International</td><td>A real, independent standards organization publishing technical standards across many industries, including the body-measurement tables Appendix A draws from.</td></tr>
<tr><td>Fabric and Apparel Patternmaker</td><td>The official U.S. government job category for someone who does exactly Devon's job, which is why its published wage (Appendix C) is the real rate this case uses.</td></tr>
</table>
<p><strong>Hover any real-world term below for a plain-English explanation; click it for a real source.</strong></p>
<div class="glossary-grid" id="storyGlossaryGrid"></div>
</div></details>
"""

REPL["{{CASE_NOTEBOOK_STEPS}}"] = """
  <div class="stepbox">
    <h4>Step 1 &mdash; Scale factors (D1&ndash;D2)</h4>
    <div class="goal">Find the point-specific bust scale factor from size 12 to size 14 (D1), and the single shared Uniform Dilation scale factor for the whole run (D2).</div>
    <div class="fieldrow"><label for="s1bust1214">Point-specific bust scale factor, size 12&rarr;14</label><input type="number" id="s1bust1214" step="0.0001"><span id="fb1a" class="fb"></span></div>
    <div class="fieldrow"><label for="s1shared">Uniform Dilation's single shared scale factor per step</label><input type="number" id="s1shared" step="0.0001"><span id="fb1b" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; Fit check at size 16 (D3&ndash;D4)</h4>
    <div class="goal">Using Step 1's shared scale factor, predict size 16's waist measurement, then find how far off it is from the real value (Appendix A). Is it within Appendix B's tolerance?</div>
    <div class="fieldrow"><label for="s2predwaist16">Predicted size-16 waist (in)</label><input type="number" id="s2predwaist16" step="0.001"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2diffwaist16">Difference from real size-16 waist (in)</label><input type="number" id="s2diffwaist16" step="0.001"><span id="fb2b" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 3 &mdash; Cost, coverage, and decision (D5)</h4>
    <div class="goal">Using Appendix C's labor rates, and your own full fit-check across all 5 sizes, find each option's total labor cost, how many sizes fully fit, and the dollars-per-fitting-size for each.</div>
    <div class="fieldrow"><label for="s3fitsA">Option A: sizes fully within tolerance</label><input type="number" id="s3fitsA" step="1"><span id="fb3a" class="fb"></span></div>
    <div class="fieldrow"><label for="s3costA">Option A: total labor cost ($)</label><input type="number" id="s3costA" step="0.01"><span id="fb3b" class="fb"></span></div>
    <div class="fieldrow"><label for="s3costB">Option B: total labor cost ($)</label><input type="number" id="s3costB" step="0.01"><span id="fb3c" class="fb"></span></div>
    <button onclick="checkStep3()">Check</button>
  </div>
"""

REPL["{{CASE_TWIST_NARRATIVE}}"] = """
      <p>The factory's incoming QC inspector announces the actual enforced fit tolerance is tighter than planned: <strong>&plusmn;0.42in</strong>, not the originally stated &plusmn;0.5in.</p>
"""
REPL["{{CASE_TWIST_APPLY_LABEL}}"] = "Recompute Option A's fit check at the tighter twist tolerance (±0.42in instead of ±0.5in)"

REPL["{{CASE_SOURCES_LIST}}"] = """
      <li>[S1] ASTM International (via Wikipedia) &mdash; <a href="https://en.wikipedia.org/wiki/U.S._standard_clothing_size" target="_blank" rel="noopener">U.S. standard clothing size (ASTM D5585-11e1)</a></li>
      <li>[S2] U.S. Bureau of Labor Statistics &mdash; <a href="https://www.bls.gov/oes/2023/may/oes516092.htm" target="_blank" rel="noopener">Fabric and Apparel Patternmakers, May 2023</a></li>
"""

REPL["{{CASE_JS_DATA_BLOCK}}"] = """
// Ported from cases/the-grade-rule/sensitivity_model.py
// sha256(case.md) = 8f6e1a1f0166b599bf2602b2a46080fafa6cc1dcdf0df2d6d5d2022078812c9a
const PARAMS = {
  base_size: 12, sizes: [8,10,12,14,16],
  bust:  {8:36.25, 10:37.25, 12:38.75, 14:40.375, 16:42.125},
  waist: {8:29.5,  10:30.5,  12:32.25, 14:34.0,   16:36.0},
  hip:   {8:38.5,  10:39.5,  12:41.0,  14:42.5,   16:44.25},
  wage_per_hr: 30.05,
  tolerance_in: 0.5, setup_min: 3.0, per_point_min_a: 0.4, per_point_min_b: 1.2,
  twist_tolerance_in: 0.42,
};
const FLEX = ["tolerance_in", "setup_min", "per_point_min_a", "per_point_min_b"];
const LANDMARKS = ["bust", "waist", "hip"];

function dilationScaleFactor(p){
  const lo = Math.min(...p.sizes), hi = Math.max(...p.sizes);
  const nSteps = (hi - lo) / 2;
  const ratios = LANDMARKS.map(lm => p[lm][hi] / p[lm][lo]);
  const avgRatio = ratios.reduce((a,b)=>a+b,0) / ratios.length;
  return Math.pow(avgRatio, 1.0/nSteps);
}
function predictions(p){
  const s = dilationScaleFactor(p);
  const base = p.base_size;
  const out = {};
  p.sizes.forEach(sz => {
    const n = (sz - base) / 2;
    const factor = Math.pow(s, n);
    out[sz] = {};
    LANDMARKS.forEach(lm => out[sz][lm] = p[lm][base] * factor);
  });
  return out;
}
function fitsA(p, tolerance){
  const preds = predictions(p);
  let n = 0;
  p.sizes.forEach(sz => {
    const ok = LANDMARKS.every(lm => Math.abs(preds[sz][lm] - p[lm][sz]) <= tolerance);
    if(ok) n += 1;
  });
  return n;
}
function costs(p){
  const nPointGrades = (p.sizes.length - 1) * LANDMARKS.length;
  const wagePerMin = p.wage_per_hr / 60.0;
  const timeA = p.setup_min + nPointGrades * p.per_point_min_a;
  const timeB = nPointGrades * p.per_point_min_b;
  return [timeA*wagePerMin, timeB*wagePerMin];
}
function evaluate(params){
  const p = Object.assign({}, PARAMS, params||{});
  const fa = fitsA(p, p.tolerance_in);
  const fb = p.sizes.length;
  const [ca, cb] = costs(p);
  return {fitsA: fa, fitsB: fb, costA: ca, costB: cb, cpfA: ca/fa, cpfB: cb/fb};
}
function evaluate_twist(params){
  const p = Object.assign({}, PARAMS, params||{});
  const fa = fitsA(p, p.twist_tolerance_in);
  const fb = p.sizes.length;
  const [ca, cb] = costs(p);
  return {fitsA: fa, fitsB: fb, costA: ca, costB: cb, cpfA: ca/fa, cpfB: cb/fb};
}
"""

REPL["{{CASE_NOTEBOOK_CHECK_FUNCTIONS}}"] = """
function checkStep1(){
  const bustFactor1214 = PARAMS.bust[14]/PARAMS.bust[12];
  const shared = dilationScaleFactor(PARAMS);
  fb('fb1a', near(parseFloat(val('s1bust1214')), bustFactor1214, 0.001));
  fb('fb1b', near(parseFloat(val('s1shared')), shared, 0.001));
}
function checkStep2(){
  const p = window.__TWIST_APPLIED__ ? Object.assign({}, PARAMS) : PARAMS;
  const preds = predictions(p);
  const predWaist16 = preds[16].waist;
  const diff = Math.abs(predWaist16 - p.waist[16]);
  fb('fb2a', near(parseFloat(val('s2predwaist16')), predWaist16, 0.01));
  fb('fb2b', near(parseFloat(val('s2diffwaist16')), diff, 0.01));
}
function checkStep3(){
  const r = window.__TWIST_APPLIED__ ? evaluate_twist() : evaluate();
  fb('fb3a', near(parseFloat(val('s3fitsA')), r.fitsA, 0.5));
  fb('fb3b', near(parseFloat(val('s3costA')), r.costA, 0.05));
  fb('fb3c', near(parseFloat(val('s3costB')), r.costB, 0.05));
}
"""

REPL["{{CASE_ON_TWIST_TOGGLE_FUNCTION}}"] = """
function onTwistToggle(){
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
}
document.getElementById('storyGlossaryGrid').innerHTML = Object.keys(STORY_GLOSSARY).map(k => stermHTML(k)).join('');
"""

REPL["{{CASE_GLOSSARY_OBJECT}}"] = """{
  "Dilation": {def: "A transformation that scales every point of a figure by the same factor from a fixed center, producing a similar (same-shape) figure.",
    url: "https://www.mathsisfun.com/geometry/dilation.html"},
  "Scale Factor": {def: "The number every length is multiplied by in a dilation -- greater than 1 enlarges, between 0 and 1 shrinks.",
    url: "https://www.mathsisfun.com/definitions/scale-factor.html"},
  "Similar": {def: "Two figures are similar if one is a scaled (dilated) copy of the other -- same shape, same angles, proportional side lengths.",
    url: "https://www.mathsisfun.com/geometry/similar.html"},
  "Congruent": {def: "Two figures are congruent if they are exactly the same size and shape -- a similarity with scale factor exactly 1.",
    url: "https://www.mathsisfun.com/geometry/congruent.html"},
  "Ratio": {def: "A way of comparing two quantities by division, written a:b or a/b -- a scale factor is itself a ratio.",
    url: "https://www.mathsisfun.com/definitions/ratio.html"},
  "Percent": {def: "A ratio that compares a number to 100 -- literally \\"per hundred.\\"",
    url: "https://www.mathsisfun.com/percentage.html"},
  "Absolute Value": {def: "How far a number is from zero on the number line -- always zero or positive; used to measure a fit-check's size regardless of direction.",
    url: "https://www.mathsisfun.com/numbers/absolute-value.html"},
  "Coordinate Plane": {def: "The grid of two perpendicular number lines (x and y axes) used to plot points and transformations like dilations.",
    url: "https://www.mathsisfun.com/data/cartesian-coordinates.html"}
}"""

REPL["{{CASE_HOWTO_ARRAY}}"] = """[
  ["how to dilate a figure on the coordinate plane given a scale factor", "Dilation"],
  ["how to find the scale factor of a dilation", "Scale Factor"],
  ["how to convert an amount from one unit to another unit", "Ratio"]
]"""

REPL["{{CASE_STORY_GLOSSARY_BLOCK}}"] = """
const STORY_GLOSSARY = {
  "Grade rule": {desc: "The written set of instructions -- a table of point/size/distance -- that turns one base-size pattern into a whole run of sizes.",
    link: "https://en.wikipedia.org/wiki/Pattern_grading"},
  "Pattern grader": {desc: "The person responsible for building a grade rule and checking that every graded size actually fits.",
    link: "https://en.wikipedia.org/wiki/Pattern_grading"},
  "Tech pack": {desc: "The complete technical document a factory receives describing exactly how to cut and sew a garment, including its grade rule.",
    link: "https://en.wikipedia.org/wiki/Advanced_Fashion_Design_and_Technology"},
  "Light table": {desc: "An illuminated table bright enough to see a pattern's lines through paper or fabric laid on top, used for tracing a pattern accurately by hand.",
    link: "https://en.wikipedia.org/wiki/Light_table"},
  "Base size": {desc: "The one size a company's pattern is originally drafted and fitted on; every other size in the run is graded up or down from it.",
    link: "https://en.wikipedia.org/wiki/Pattern_grading"},
  "Landmark point": {desc: "A specific, named location on a pattern (like the bust point or waist point) whose position is tracked and adjusted separately when grading.",
    link: "https://en.wikipedia.org/wiki/Pattern_grading"},
  "Ease": {desc: "The small, deliberate extra room built into a garment beyond a person's exact body measurement, so the garment is wearable and comfortable.",
    link: "https://en.wikipedia.org/wiki/Ease_(sewing)"},
  "Misses figure type": {desc: "A standard body-shape/proportion category used in U.S. commercial sizing standards, distinct from categories like 'women's' or 'petite.'",
    link: "https://en.wikipedia.org/wiki/U.S._standard_clothing_size"},
  "ASTM International": {desc: "A real standards organization that publishes the body-measurement tables this case's Appendix A data comes from.",
    link: "https://en.wikipedia.org/wiki/ASTM_International"}
};
function stermHTML(label, textOverride){
  const g = STORY_GLOSSARY[label];
  if(!g) return textOverride || label;
  const text = textOverride || label;
  return `<a class="sterm gterm" data-term="${label}" href="${g.link}" target="_blank" rel="noopener">${text}<span class="tip">${g.desc}<span class="go">Learn more &rarr;</span></span></a>`;
}
"""

REPL["{{CASE_JS_DATA_BLOCK}}"] = REPL["{{CASE_JS_DATA_BLOCK}}"] + "\n" + REPL["{{CASE_STORY_GLOSSARY_BLOCK}}"]
del REPL["{{CASE_STORY_GLOSSARY_BLOCK}}"]

for k, v in REPL.items():
    if k not in html:
        raise SystemExit(f"MISSING PLACEHOLDER IN SHELL: {k}")
    html = html.replace(k, v)

leftover = [m for m in re.findall(r'\{\{[A-Z_]+\}\}', html) if m != '{{PLACEHOLDER}}']
if leftover:
    raise SystemExit(f"Unfilled placeholders remain: {leftover}")

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print("wrote", OUT)
