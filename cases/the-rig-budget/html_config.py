CONFIG = {
    "strand_summary": "Matrices &middot; Determinants &middot; Systems of Equations",
    "protagonist": "Dana Ruiz",
    "option_a_label": "The Direct Blend",
    "option_a_text": "Blend a multi-bone vertex's transform by directly summing the influencing bones' weighted matrices (linear blend skinning), applied once per vertex.",
    "option_b_label": "The Quaternion Blend",
    "option_b_text": "Blend a multi-bone vertex's transform by converting each influencing bone's rotation to a quaternion, blending the quaternions, and converting the result back to a matrix before applying it (direct quaternion blending).",
    "challenge3_summary": "Include: <strong>D1</strong> the elbow bone's rotation matrix R and stretch matrix S; <strong>D2</strong> two combined matrices computed by hand (elbow M=R&middot;S, shoulder M_blend=w1R1+w2R2); <strong>D3</strong> two determinants computed by hand, compared to the identity; <strong>D4</strong> recovering M_blend by solving a system of equations; <strong>D5</strong> the cost &amp; determinant table and a recommendation memo.",
    "deliverables": [
        ["D1", "Elbow bone's R and S matrices"],
        ["D2", "Two combined matrices (elbow M, shoulder M_blend)"],
        ["D3", "Two determinants, compared to the identity"],
        ["D4", "Recover M_blend by solving a system of equations"],
        ["D5", "Cost & determinant table and recommendation memo"],
    ],
    "notebook_steps_html": """
  <div class="stepbox">
    <h4>Step 1 &mdash; The elbow bone: M = R&middot;S (D1&ndash;D3a)</h4>
    <div class="goal">Using Appendix B's elbow rotation matrix R and stretch matrix S, compute M = R&middot;S entry by entry (2&times;2 matrix multiplication), then its determinant, and compare to the identity matrix's determinant (1).</div>
    <div class="fieldrow"><label for="s1m11">M[1,1]</label><input type="number" id="s1m11" step="0.01"><span id="fb1a" class="fb"></span></div>
    <div class="fieldrow"><label for="s1m12">M[1,2]</label><input type="number" id="s1m12" step="0.01"><span id="fb1b" class="fb"></span></div>
    <div class="fieldrow"><label for="s1m21">M[2,1]</label><input type="number" id="s1m21" step="0.01"><span id="fb1c" class="fb"></span></div>
    <div class="fieldrow"><label for="s1m22">M[2,2]</label><input type="number" id="s1m22" step="0.01"><span id="fb1d" class="fb"></span></div>
    <div class="fieldrow"><label for="s1det">det(M)</label><input type="number" id="s1det" step="0.01"><span id="fb1e" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; The shoulder blend-zone: M_blend = w1R1 + w2R2 (D2b&ndash;D3b)</h4>
    <div class="goal">Using Appendix B's two bone rotation matrices R1, R2 and equal blend weights, compute M_blend entry by entry (scalar multiplication + matrix addition), then its determinant, compared to the identity.</div>
    <div class="fieldrow"><label for="s2m11">M_blend[1,1]</label><input type="number" id="s2m11" step="0.01"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2m12">M_blend[1,2]</label><input type="number" id="s2m12" step="0.01"><span id="fb2b" class="fb"></span></div>
    <div class="fieldrow"><label for="s2m21">M_blend[2,1]</label><input type="number" id="s2m21" step="0.01"><span id="fb2c" class="fb"></span></div>
    <div class="fieldrow"><label for="s2m22">M_blend[2,2]</label><input type="number" id="s2m22" step="0.01"><span id="fb2d" class="fb"></span></div>
    <div class="fieldrow"><label for="s2det">det(M_blend)</label><input type="number" id="s2det" step="0.01"><span id="fb2e" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 3 &mdash; Recover M_blend by solving a system of equations (D4)</h4>
    <div class="goal">Appendix B gives two known point-mappings the engine logged under M_blend: v1=(1,1)&rarr;(0,1) and v2=(2,&minus;1)&rarr;(1.5,0.5). Set up and solve the resulting system of linear equations for M_blend's four entries. Confirm your answer matches Step 2.</div>
    <div class="fieldrow"><label for="s3m11">Recovered M_blend[1,1]</label><input type="number" id="s3m11" step="0.01"><span id="fb3a" class="fb"></span></div>
    <div class="fieldrow"><label for="s3m12">Recovered M_blend[1,2]</label><input type="number" id="s3m12" step="0.01"><span id="fb3b" class="fb"></span></div>
    <div class="fieldrow"><label for="s3m21">Recovered M_blend[2,1]</label><input type="number" id="s3m21" step="0.01"><span id="fb3c" class="fb"></span></div>
    <div class="fieldrow"><label for="s3m22">Recovered M_blend[2,2]</label><input type="number" id="s3m22" step="0.01"><span id="fb3d" class="fb"></span></div>
    <button onclick="checkStep3()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 4 &mdash; Cost table (D5)</h4>
    <div class="goal">Using Appendix D's raw per-frame costs (0.32ms, 0.39ms) and Fenwick's real 16.6ms/frame budget, compute each option's share of the frame budget, and the percent by which The Quaternion Blend costs more than The Direct Blend.</div>
    <div class="fieldrow"><label for="s4shareA">Option A share of frame budget (%)</label><input type="number" id="s4shareA" step="0.01"><span id="fb4a" class="fb"></span></div>
    <div class="fieldrow"><label for="s4shareB">Option B share of frame budget (%)</label><input type="number" id="s4shareB" step="0.01"><span id="fb4b" class="fb"></span></div>
    <div class="fieldrow"><label for="s4margin">Percent B costs more than A</label><input type="number" id="s4margin" step="0.01"><span id="fb4c" class="fb"></span></div>
    <button onclick="checkStep4()">Check</button>
    <p class="side-note">The notebook checks your arithmetic. It does not tell you which pipeline to recommend &mdash; that's D5's memo.</p>
  </div>
""",
    "twist_narrative_html": """
      <p>Everything above &mdash; D1 through D4 &mdash; was worked at the shoulder. And per the same real source that documents The Quaternion Blend's advantage, the shoulder is exactly the case where it "works perfectly": two bones, one clean joint, like an elbow.</p>
      <p>But the hero rig has two <em>other</em> blend zones you haven't touched: the underarm, and the cape's mounting point &mdash; both influenced by three or more bones at once, not two. The same real source (Appendix C) says artifacts appear at exactly these more complex joints, because The Quaternion Blend's center of rotation is fixed and doesn't adapt to the actual posture.</p>
      <p>Does your recommendation still hold at the underarm and the cape mount &mdash; or does Dana have to pick different pipelines for different blend zones on the same rig?</p>
""",
    "twist_apply_label": "Mark: does Option B's rigid-transform guarantee still hold at the underarm/cape mount (3+ bone joints)?",
    "js_data_block": """
const PARAMS = {
  direct_blend_ms: 0.32,
  quaternion_blend_ms: 0.39,
  frame_rate_fps: 60.0,
  frame_budget_ms: 16.6,
  // D1 elbow inputs
  elbow_R: [[0.8, -0.6], [0.6, 0.8]],
  elbow_S: [[1.5, 0], [0, 0.5]],
  // D2 shoulder inputs
  R1: [[1, 0], [0, 1]],
  R2: [[0, -1], [1, 0]],
  w1: 0.5, w2: 0.5,
};
function matMul2(A, B){
  return [
    [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
    [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]],
  ];
}
function det2(M){ return M[0][0]*M[1][1] - M[0][1]*M[1][0]; }
function elbowM(){ return matMul2(PARAMS.elbow_R, PARAMS.elbow_S); }
function shoulderMBlend(){
  const w1 = PARAMS.w1, w2 = PARAMS.w2;
  const R1 = PARAMS.R1, R2 = PARAMS.R2;
  return [
    [w1*R1[0][0] + w2*R2[0][0], w1*R1[0][1] + w2*R2[0][1]],
    [w1*R1[1][0] + w2*R2[1][0], w1*R1[1][1] + w2*R2[1][1]],
  ];
}
function evaluateDetail(params){
  const p = Object.assign({}, PARAMS, params||{});
  const aMs = p.direct_blend_ms, bMs = p.quaternion_blend_ms;
  const budget = p.frame_budget_ms;
  return {
    perFrameMs: {A: aMs, B: bMs},
    shareOfBudgetPct: {A: 100*aMs/budget, B: 100*bMs/budget},
    marginPct: 100 * (bMs - aMs) / bMs,  // % B costs more than A, denominator = loser (higher cost)
  };
}
// Contract entry point (matches sensitivity_model.py's evaluate(): higher is
// better, so the per-frame ms cost is negated).
function evaluate(params){
  const p = Object.assign({}, PARAMS, params||{});
  return {A: -p.direct_blend_ms, B: -p.quaternion_blend_ms};
}
""",
    "notebook_check_functions": """
function checkStep1(){
  const M = elbowM();
  fb('fb1a', near(parseFloat(val('s1m11')), M[0][0], 0.01));
  fb('fb1b', near(parseFloat(val('s1m12')), M[0][1], 0.01));
  fb('fb1c', near(parseFloat(val('s1m21')), M[1][0], 0.01));
  fb('fb1d', near(parseFloat(val('s1m22')), M[1][1], 0.01));
  fb('fb1e', near(parseFloat(val('s1det')), det2(M), 0.01));
}
function checkStep2(){
  const M = shoulderMBlend();
  fb('fb2a', near(parseFloat(val('s2m11')), M[0][0], 0.01));
  fb('fb2b', near(parseFloat(val('s2m12')), M[0][1], 0.01));
  fb('fb2c', near(parseFloat(val('s2m21')), M[1][0], 0.01));
  fb('fb2d', near(parseFloat(val('s2m22')), M[1][1], 0.01));
  fb('fb2e', near(parseFloat(val('s2det')), det2(M), 0.01));
}
function checkStep3(){
  // Same true values as Step 2 -- D4 recovers M_blend independently via the
  // system of equations, and the answer must match.
  const M = shoulderMBlend();
  fb('fb3a', near(parseFloat(val('s3m11')), M[0][0], 0.01));
  fb('fb3b', near(parseFloat(val('s3m12')), M[0][1], 0.01));
  fb('fb3c', near(parseFloat(val('s3m21')), M[1][0], 0.01));
  fb('fb3d', near(parseFloat(val('s3m22')), M[1][1], 0.01));
}
function checkStep4(){
  const d = evaluateDetail({});
  fb('fb4a', near(parseFloat(val('s4shareA')), d.shareOfBudgetPct.A, 0.1));
  fb('fb4b', near(parseFloat(val('s4shareB')), d.shareOfBudgetPct.B, 0.1));
  fb('fb4c', near(parseFloat(val('s4margin')), d.marginPct, 0.5));
}
""",
    "glossary_js": """{
  "Matrix": {def: "A rectangular array of numbers arranged in rows and columns.",
    url: "https://www.mathsisfun.com/algebra/matrix-introduction.html"},
  "Determinant": {def: "A single number computed from a square matrix that reveals key properties like whether it has an inverse.",
    url: "https://www.mathsisfun.com/algebra/matrix-determinant.html"},
  "Identity Matrix": {def: "A square matrix with 1s on the main diagonal and 0s elsewhere -- multiplying by it leaves a matrix unchanged.",
    url: "https://www.mathsisfun.com/algebra/matrix-types.html"},
  "System of Equations": {def: "A set of two or more equations with the same variables, solved together.",
    url: "https://www.mathsisfun.com/algebra/systems-linear-equations.html"},
  "Matrix Dimension": {def: "The size of a matrix, given as rows &times; columns, e.g. a 2&times;2 matrix has 2 rows and 2 columns.",
    url: "https://www.mathsisfun.com/algebra/matrix-introduction.html"},
  "Percent": {def: "A ratio that compares a number to 100 -- literally \\"per hundred.\\"",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Ratio": {def: "A way of comparing two quantities by division, written a:b or a/b.",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Decimal": {def: "A number written with place value to the right of a decimal point, e.g. 0.34.",
    url: "https://www.khanacademy.org/math/arithmetic/arith-decimals"}
}""",
    "howto_js": """[
  ["how to add and multiply matrices", "Matrix"],
  ["how to find the determinant of a 2x2 matrix", "Determinant"],
  ["how to solve a system of equations using a matrix", "System of Equations"]
]""",
    "on_twist_toggle_js": """
function onTwistToggle(){
  // Purely a facilitation/reflection toggle -- the twist here is a
  // qualitative scope limitation (S8's complex-joint artifact), not a
  // numeric recompute, so this just records the mark for the learner's own
  // notebook, no verdict printed.
  const applied = document.getElementById('applyTwist').checked;
  window.__TWIST_APPLIED__ = applied;
}
""",
}
