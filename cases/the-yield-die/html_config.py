CONFIG = {
    "strand_summary": "Scientific Notation &middot; Standard Notation",
    "protagonist": "Priya Anand",
    "option_a_label": "The Compact Die",
    "option_a_text": "Smaller floorplan, more gross die per wafer, fewer transistors and a lower price per chip.",
    "option_b_label": "The Full Die",
    "option_b_text": "Larger floorplan, fewer gross die per wafer, more transistors and a higher price per chip.",
    "challenge3_summary": "Include: <strong>D1</strong> gross dies per wafer for each die size, in scientific notation; <strong>D2</strong> die yield under the Seeds model for each option; <strong>D3</strong> net good (sellable) dies for each option; <strong>D4</strong> revenue per wafer for each option; <strong>D5</strong> the recommendation and the one figure it depends on most.",
    "deliverables": [
        ["D1", "Gross dies per wafer, each die size, scientific notation"],
        ["D2", "Die yield under the Seeds model, each option"],
        ["D3", "Net good (sellable) dies, each option"],
        ["D4", "Revenue per wafer, each option"],
        ["D5", "Recommendation and most sensitive figure"],
    ],
    "notebook_steps_html": """
  <div class="stepbox">
    <h4>Step 1 &mdash; Gross dies and yield-adjusted (net good) dies per wafer (D1&ndash;D3)</h4>
    <div class="goal">Using Appendix B's wafer diameter and each option's die area, find the gross (edge-loss-corrected) dies per wafer. Then, using Appendix D's Seeds yield model with the assumed defect density, find each option's die yield and its net good (sellable) dies per wafer.</div>
    <div class="fieldrow"><label for="s1grossA">Compact Die: gross dies per wafer</label><input type="number" id="s1grossA" step="1"><span id="fb1a" class="fb"></span></div>
    <div class="fieldrow"><label for="s1goodA">Compact Die: net good dies per wafer</label><input type="number" id="s1goodA" step="1"><span id="fb1b" class="fb"></span></div>
    <div class="fieldrow"><label for="s1grossB">Full Die: gross dies per wafer</label><input type="number" id="s1grossB" step="1"><span id="fb1c" class="fb"></span></div>
    <div class="fieldrow"><label for="s1goodB">Full Die: net good dies per wafer</label><input type="number" id="s1goodB" step="1"><span id="fb1d" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; Revenue per wafer (D4&ndash;D5)</h4>
    <div class="goal">Using Appendix C/E's transistor density and price-per-transistor figures (with the Full Die's flagship pricing premium), find the price per chip for each option, then multiply by Step 1's net good dies to get revenue per wafer.</div>
    <div class="fieldrow"><label for="s2revA">Compact Die: revenue per wafer ($)</label><input type="number" id="s2revA" step="1"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2revB">Full Die: revenue per wafer ($)</label><input type="number" id="s2revB" step="1"><span id="fb2b" class="fb"></span></div>
    <div class="fieldrow"><label for="s2margin">Margin between the two options (percent)</label><input type="number" id="s2margin" step="0.1"><span id="fb2c" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
  </div>
""",
    "twist_narrative_html": """
      <p>The fab's process engineer calls with the first real measurement off the pilot line: the true defect density is running at half of Priya's planning assumption. Toggle the switch below to recompute revenue per wafer at this measured, lower defect density.</p>
""",
    "twist_apply_label": "Recompute at the measured defect density (0.15 defects/cm&sup2; instead of 0.30)",
    "js_data_block": """
const PARAMS = {
  wafer_diameter_mm: 300.0,
  die_area_A_mm2: 100.0, die_area_B_mm2: 200.0,
  transistor_density_per_mm2: 2.0e8,
  defect_density_D0_per_cm2: 0.30,
  dollars_per_transistor: 3.75e-7,
  flagship_premium_B: 1.19,
};
function grossDies(diamCm, areaCm2){
  const Aw = Math.PI * Math.pow(diamCm/2.0, 2);
  return Aw/areaCm2 - (Math.PI*diamCm)/Math.sqrt(2.0*areaCm2);
}
function dieYield(D0, areaCm2){
  return 1.0/(1.0 + D0*areaCm2);
}
function evaluate(params){
  const p = Object.assign({}, PARAMS, params||{});
  const diamCm = p.wafer_diameter_mm/10.0;
  const areaAcm2 = p.die_area_A_mm2/100.0, areaBcm2 = p.die_area_B_mm2/100.0;
  const grossA = Math.floor(grossDies(diamCm, areaAcm2));
  const grossB = Math.floor(grossDies(diamCm, areaBcm2));
  const yieldA = dieYield(p.defect_density_D0_per_cm2, areaAcm2);
  const yieldB = dieYield(p.defect_density_D0_per_cm2, areaBcm2);
  const goodA = Math.floor(grossA*yieldA), goodB = Math.floor(grossB*yieldB);
  const transA = p.transistor_density_per_mm2*p.die_area_A_mm2;
  const transB = p.transistor_density_per_mm2*p.die_area_B_mm2;
  const priceA = p.dollars_per_transistor*transA;
  const priceB = p.dollars_per_transistor*transB*p.flagship_premium_B;
  const revA = goodA*priceA, revB = goodB*priceB;
  return {A: revA, B: revB, grossA, grossB, goodA, goodB, revA, revB};
}
function evaluate_twist(params){
  return evaluate(Object.assign({defect_density_D0_per_cm2: 0.15}, params||{}));
}
""",
    "notebook_check_functions": """
function checkStep1(){
  const p = window.__TWIST_APPLIED__ ? Object.assign({}, PARAMS, {defect_density_D0_per_cm2: 0.15}) : PARAMS;
  const r = evaluate(p);
  fb('fb1a', near(parseFloat(val('s1grossA')), r.grossA, 2));
  fb('fb1b', near(parseFloat(val('s1goodA')), r.goodA, 2));
  fb('fb1c', near(parseFloat(val('s1grossB')), r.grossB, 2));
  fb('fb1d', near(parseFloat(val('s1goodB')), r.goodB, 2));
}
function checkStep2(){
  const p = window.__TWIST_APPLIED__ ? Object.assign({}, PARAMS, {defect_density_D0_per_cm2: 0.15}) : PARAMS;
  const r = evaluate(p);
  const lo = Math.min(r.A, r.B), hi = Math.max(r.A, r.B);
  const margin = lo ? 100.0*(hi-lo)/lo : 0;
  fb('fb2a', near(parseFloat(val('s2revA')), r.A, 2000));
  fb('fb2b', near(parseFloat(val('s2revB')), r.B, 2000));
  fb('fb2c', near(parseFloat(val('s2margin')), margin, 1));
}
""",
    "glossary_js": """{
  "Scientific Notation": {def: "A way of writing very large or very small numbers as a number between 1 and 10 multiplied by a power of 10, e.g. 3.75 &times; 10&#8315;&#8309;.",
    url: "https://www.mathsisfun.com/numbers/scientific-notation.html"},
  "Standard Notation": {def: "The usual way of writing a number in full, e.g. 300 instead of 3 &times; 10&sup2;.",
    url: "https://www.mathsisfun.com/numbers/scientific-notation.html"},
  "Formula": {def: "A rule written using symbols that shows how to calculate a value, such as the gross-dies-per-wafer formula in Appendix B.",
    url: "https://www.mathsisfun.com/definitions/formula.html"},
  "Exponent": {def: "A small number written above and to the right of a base number, showing how many times to multiply the base by itself -- the power of 10 in scientific notation.",
    url: "https://www.mathsisfun.com/definitions/exponent.html"},
  "Percent": {def: "A ratio that compares a number to 100 -- used throughout this case's yield calculations.",
    url: "https://www.mathsisfun.com/definitions/percent.html"},
  "Ratio": {def: "A way of comparing two quantities by division, such as the ratio of net good dies to gross dies (the yield).",
    url: "https://www.mathsisfun.com/definitions/ratio.html"},
  "Rounding": {def: "Adjusting a number to a nearby value that is easier to work with -- this case rounds die counts down to the nearest whole die.",
    url: "https://www.mathsisfun.com/rounding-numbers.html"},
  "Order Of Operations": {def: "The agreed sequence for evaluating a mathematical expression (parentheses, exponents, multiplication/division, addition/subtraction) -- needed to evaluate this case's multi-step yield and revenue formulas correctly.",
    url: "https://www.mathsisfun.com/operation-order-pemdas.html"}
}""",
    "howto_js": """[
  ["how to write a number in scientific notation given its standard notation", "Scientific Notation"],
  ["how to write a number in standard notation given its scientific notation", "Standard Notation"]
]""",
    "on_twist_toggle_js": """
function onTwistToggle(){
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
}
""",
}
