CONFIG = {
    "strand_summary": "Systems of Equations &middot; Matrices",
    "protagonist": "Wade Kessler",
    "option_a_label": "The Basin Shift",
    "option_a_text": "Move 2 rigs off the Permian leases into the Bakken, paying the relocation-downtime cost and disrupting the most experienced crew, to chase the Bakken's higher per-rig productivity for the rest of the quarter.",
    "option_b_label": "Hold the Line",
    "option_b_text": "Keep the current allocation -- no relocation downtime and no crew disruption, but the Permian rigs keep producing at their lower barrels-per-rig-day rate.",
    "challenge3_summary": "Include: <strong>D1</strong> a 3x3 system of equations, in matrix form, for the Basin Shift; <strong>D2</strong> solve it using Gaussian elimination or a matrix inverse, including a determinant check; <strong>D3</strong> repeat for Hold the Line (Appendix C); <strong>D4</strong> a blended-productivity comparison table using Appendix D's real EIA rates; <strong>D5</strong> a recommendation memo with a sensitivity check on relocation downtime.",
    "deliverables": [
        ["D1", "3x3 system, matrix form, for the Basin Shift"],
        ["D2", "Solve via Gaussian elimination / matrix inverse, with determinant check"],
        ["D3", "Repeat D1-D2 for Hold the Line"],
        ["D4", "Blended-productivity comparison table"],
        ["D5", "Recommendation memo with sensitivity check"],
    ],
    "notebook_steps_html": """
  <div class="stepbox">
    <h4>Step 1 &mdash; Solve the 3x3 rig-day system (D1&ndash;D3)</h4>
    <div class="goal">Define x = Permian-producing rig-days, y = Bakken-producing rig-days, z = idle relocation rig-days, for the rest of the quarter. Using Appendix A's fleet/day numbers: x + y + z = total rig-day budget; x = (Permian rigs remaining) &times; days; z = (rigs moved) &times; relocation-downtime days. Solve for x, y, z for your chosen option (0 rigs moved = Hold the Line, 2 rigs moved = Basin Shift).</div>
    <div class="fieldrow">
      <label for="s1opt">Option</label>
      <select id="s1opt"><option value="0">Hold the Line (0 rigs moved)</option><option value="2">Basin Shift (2 rigs moved)</option></select>
    </div>
    <div class="fieldrow"><label for="s1x">x &mdash; Permian rig-days</label><input type="number" id="s1x" step="0.1"><span id="fb1a" class="fb"></span></div>
    <div class="fieldrow"><label for="s1y">y &mdash; Bakken rig-days</label><input type="number" id="s1y" step="0.1"><span id="fb1b" class="fb"></span></div>
    <div class="fieldrow"><label for="s1z">z &mdash; Idle relocation rig-days</label><input type="number" id="s1z" step="0.1"><span id="fb1c" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; Blended barrels-per-rig-day for both options (D4&ndash;D5)</h4>
    <div class="goal">Using your solved rig-day values and Appendix D's real EIA per-basin productivity rates, compute total barrels and blended barrels-per-rig-day for <em>both</em> options, and the percent difference between them.</div>
    <div class="fieldrow"><label for="s2blendedA">Basin Shift: blended bbl/rig-day</label><input type="number" id="s2blendedA" step="0.01"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2blendedB">Hold the Line: blended bbl/rig-day</label><input type="number" id="s2blendedB" step="0.01"><span id="fb2b" class="fb"></span></div>
    <div class="fieldrow"><label for="s2margin">Percent difference</label><input type="number" id="s2margin" step="0.01"><span id="fb2c" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
    <p class="side-note">This margin is razor-thin by design (SPEC's own gold standard is a 0.09% race). Try Step 1 again with a different relocation-downtime value (Appendix E's real range is 1-4 weeks) to see how close this really is.</p>
  </div>
""",
    "twist_narrative_html": """
      <p>Ray texts back: the North Dakota ops lead just revised the relocation-downtime estimate. It's not 14 days anymore &mdash; it's 18, still inside Appendix E's real cited 1-4-week range, but on the higher end.</p>
      <p>Recompute Step 1/2 for the Basin Shift using 18 days of relocation downtime instead of 14. Does the Basin Shift still win? By how much, or by how little?</p>
""",
    "twist_apply_label": "Recompute using 18 days of relocation downtime instead of 14",
    "js_data_block": """
const PARAMS = {
  total_rigs: 8.0, permian_rigs: 6.0, bakken_rigs: 2.0, rigs_moved: 2.0,
  remaining_days: 60.0, relocation_downtime_days: 14.0,
  permian_bbl_per_rig_day: 1400.0, bakken_bbl_per_rig_day: 1747.0,
};
function solve3x3(a, b){
  const m = a.map((row,i) => row.concat([b[i]]));
  const n = 3;
  for(let col=0; col<n; col++){
    let pivotRow = col;
    for(let r=col; r<n; r++) if(Math.abs(m[r][col]) > Math.abs(m[pivotRow][col])) pivotRow = r;
    [m[col], m[pivotRow]] = [m[pivotRow], m[col]];
    const pivot = m[col][col];
    for(let r=0; r<n; r++){
      if(r===col) continue;
      const factor = m[r][col] / pivot;
      for(let c=col; c<n+1; c++) m[r][c] -= factor * m[col][c];
    }
  }
  return [0,1,2].map(i => m[i][n] / m[i][i]);
}
function optionRigdays(p, rigsMoved){
  const d = p.remaining_days, l = p.relocation_downtime_days;
  const permianRemaining = p.permian_rigs - rigsMoved;
  const totalBudget = p.total_rigs * d;
  const a = [[1,1,1],[1,0,0],[0,0,1]];
  const b = [totalBudget, permianRemaining*d, rigsMoved*l];
  const [x,y,z] = solve3x3(a,b);
  return {x,y,z,totalBudget};
}
function evaluate(params){
  const p = Object.assign({}, PARAMS, params||{});
  const rdA = optionRigdays(p, p.rigs_moved);
  const rdB = optionRigdays(p, 0.0);
  const barrelsA = p.permian_bbl_per_rig_day*rdA.x + p.bakken_bbl_per_rig_day*rdA.y;
  const barrelsB = p.permian_bbl_per_rig_day*rdB.x + p.bakken_bbl_per_rig_day*rdB.y;
  return {A: barrelsA/rdA.totalBudget, B: barrelsB/rdB.totalBudget};
}
function evaluate_twist(params){
  return evaluate(Object.assign({relocation_downtime_days: 18.0}, params||{}));
}
""",
    "notebook_check_functions": """
function checkStep1(){
  const p = window.__TWIST_APPLIED__ ? Object.assign({}, PARAMS, {relocation_downtime_days: 18.0}) : PARAMS;
  const rigsMoved = parseFloat(val('s1opt'));
  const rd = optionRigdays(p, rigsMoved);
  fb('fb1a', near(parseFloat(val('s1x')), rd.x, 0.5));
  fb('fb1b', near(parseFloat(val('s1y')), rd.y, 0.5));
  fb('fb1c', near(parseFloat(val('s1z')), rd.z, 0.5));
}
function checkStep2(){
  const p = window.__TWIST_APPLIED__ ? Object.assign({}, PARAMS, {relocation_downtime_days: 18.0}) : PARAMS;
  const r = evaluate(p);
  const margin = 100 * Math.abs(r.A - r.B) / Math.max(r.A, r.B);
  fb('fb2a', near(parseFloat(val('s2blendedA')), r.A, 0.05));
  fb('fb2b', near(parseFloat(val('s2blendedB')), r.B, 0.05));
  fb('fb2c', near(parseFloat(val('s2margin')), margin, 0.3));
}
""",
    "glossary_js": """{
  "Matrix": {def: "A rectangular array of numbers arranged in rows and columns.",
    url: "https://www.mathsisfun.com/algebra/matrix-introduction.html"},
  "Matrix Dimension": {def: "The size of a matrix, written rows x columns.",
    url: "https://www.mathsisfun.com/algebra/matrix-introduction.html"},
  "Determinant": {def: "A single number computed from a square matrix that reveals key properties like whether it has an inverse.",
    url: "https://www.mathsisfun.com/algebra/matrix-determinant.html"},
  "Identity Matrix": {def: "A square matrix with 1s on the main diagonal and 0s everywhere else -- multiplying by it changes nothing.",
    url: "https://www.mathsisfun.com/algebra/matrix-types.html"},
  "System of Equations": {def: "A set of two or more equations with the same variables, solved together.",
    url: "https://www.mathsisfun.com/algebra/systems-linear-equations.html"},
  "Percent": {def: "A ratio that compares a number to 100 -- literally \\"per hundred.\\"",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Ratio": {def: "A way of comparing two quantities by division, written a:b or a/b.",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Rate": {def: "A ratio that compares two quantities with different units, like barrels per day.",
    url: "https://www.khanacademy.org/math/pre-algebra/pre-algebra-ratios-rates"}
}""",
    "howto_js": """[
  ["how to add and multiply matrices", "Matrix"],
  ["how to find the determinant of a 2x2 matrix", "Determinant"],
  ["how to solve a system of equations using a matrix", "System of Equations"]
]""",
    "on_twist_toggle_js": """
function onTwistToggle(){
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
}
""",
}
