CONFIG = {
    "strand_summary": "Interior Angles &middot; GCF &middot; Percent",
    "protagonist": "Marcus Ibe",
    "option_a_label": "The Regular Hexagon",
    "option_a_text": "A single repeating shape that tessellates the plane with zero gaps -- one manufactured tile line, priced accordingly.",
    "option_b_label": "The Octagon-and-Square Combination",
    "option_b_text": "The client committee's preferred pattern -- two shapes meeting at every vertex, priced from a different manufactured tile line.",
    "challenge3_summary": "Include: <strong>D1</strong> an interior-angle-sum tessellation proof for both patterns; <strong>D2</strong> a GCF-based staging-block computation; <strong>D3</strong> a cut-waste computation for both tiling options using their real manufactured sheet sizes; <strong>D4</strong> a total installed cost table (material + labor); <strong>D5</strong> a recommendation memo.",
    "deliverables": [
        ["D1", "Interior-angle-sum tessellation proof, both patterns"],
        ["D2", "GCF-based staging-block computation"],
        ["D3", "Cut-waste computation, both tiling options"],
        ["D4", "Total installed cost table (material + labor)"],
        ["D5", "Recommendation memo"],
    ],
    "notebook_steps_html": """
  <div class="stepbox">
    <h4>Step 1 &mdash; Staging block via GCF (D2)</h4>
    <div class="goal">Using the plaza's stated length and width (Appendix A), find the greatest common factor of the two dimensions -- that's the side length of the largest square staging block that divides the plaza evenly with no leftover partial block.</div>
    <div class="fieldrow"><label for="s1gcf">GCF of 45 and 30 (ft)</label><input type="number" id="s1gcf" step="1"><span id="fb1a" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; Installed cost per square foot, both patterns (D3&ndash;D5)</h4>
    <div class="goal">For each option: figure out how many manufactured sheets are needed to cover the plaza's grid (rounding up every partial row/column), add Appendix E's 10% installation waste allowance (rounding up again), multiply by the sheet's coverage and price to get material cost, then add labor (plaza area &times; labor rate, including Appendix F's hexagon labor premium on Option A only). Divide the total by plaza area for cost per square foot.</div>
    <div class="fieldrow"><label for="s2costA">Option A (Hexagon) total installed cost per sq ft (USD)</label><input type="number" id="s2costA" step="0.01"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2costB">Option B (Octagon+Square) total installed cost per sq ft (USD)</label><input type="number" id="s2costB" step="0.01"><span id="fb2b" class="fb"></span></div>
    <div class="fieldrow"><label for="s2margin">Percent margin</label><input type="number" id="s2margin" step="0.01"><span id="fb2c" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
    <p class="side-note">Which pattern wastes MORE material once you account for the real manufactured sheet sizes -- the one that tessellates perfectly, or the one that doesn't? That's the trap this case is built around.</p>
  </div>
""",
    "twist_narrative_html": """
      <p>Ashford's procurement office adds a late requirement: the labor premium for hexagon-pattern installation needs to be defensible with a number, not just "it takes longer." The only real evidence Marcus has is qualitative (Appendix F's general contractor sources) -- the case used a round 15% based on that qualitative guidance.</p>
      <p>Recompute Step 2 with the hexagon labor premium at 0% instead of 15% -- does the recommendation change? Then try 40%. Somewhere between those two values, the recommendation flips. Can you find roughly where?</p>
""",
    "twist_apply_label": "Recompute Step 2 using a 0% hexagon labor premium instead of 15%",
    "js_data_block": """
const PARAMS = {
  plaza_length_ft: 45.0, plaza_width_ft: 30.0,
  hex_sheet_w_in: 11.625, hex_sheet_h_in: 10.25, hex_coverage_per_sheet_sqft: 0.81, hex_price_per_sqft: 6.59,
  oct_sheet_side_in: 12.0, oct_coverage_per_sheet_sqft: 1.00, oct_price_per_sqft: 9.69,
  install_waste_factor: 0.10,
  base_labor_rate_per_sqft: 9.00, hex_labor_premium: 0.15,
};
function ceilClean(x){
  const r = Math.round(x*1e6)/1e6;
  return Math.abs(r - Math.round(r)) < 1e-6 ? Math.ceil(r - 1e-6) : Math.ceil(r);
}
function gcd(a,b){ a=Math.round(a); b=Math.round(b); while(b){ [a,b]=[b, a%b]; } return a; }
function sheetsNeeded(L, W, sheetWft, sheetHft){
  const cols = ceilClean(L/sheetWft), rows = ceilClean(W/sheetHft);
  return cols*rows;
}
function optionCostPerSqft(p, sheetWin, sheetHin, coveragePerSheet, pricePerSqft, laborRate){
  const plazaArea = p.plaza_length_ft * p.plaza_width_ft;
  const sheetWft = sheetWin/12.0, sheetHft = sheetHin/12.0;
  const gridSheets = sheetsNeeded(p.plaza_length_ft, p.plaza_width_ft, sheetWft, sheetHft);
  const sheetsToBuy = ceilClean(gridSheets * (1 + p.install_waste_factor));
  const purchasedCoverage = sheetsToBuy * coveragePerSheet;
  const materialCost = purchasedCoverage * pricePerSqft;
  const laborCost = plazaArea * laborRate;
  const totalCost = materialCost + laborCost;
  return {totalCost, costPerSqft: totalCost/plazaArea};
}
function evaluate(params){
  const p = Object.assign({}, PARAMS, params||{});
  const laborRateA = p.base_labor_rate_per_sqft * (1 + p.hex_labor_premium);
  const laborRateB = p.base_labor_rate_per_sqft;
  const a = optionCostPerSqft(p, p.hex_sheet_w_in, p.hex_sheet_h_in, p.hex_coverage_per_sheet_sqft, p.hex_price_per_sqft, laborRateA);
  const b = optionCostPerSqft(p, p.oct_sheet_side_in, p.oct_sheet_side_in, p.oct_coverage_per_sheet_sqft, p.oct_price_per_sqft, laborRateB);
  return {A: -a.costPerSqft, B: -b.costPerSqft};
}
function evaluate_twist(params){
  return evaluate(Object.assign({hex_labor_premium: 0.0}, params||{}));
}
""",
    "notebook_check_functions": """
function checkStep1(){
  const trueGCF = gcd(PARAMS.plaza_length_ft, PARAMS.plaza_width_ft);
  fb('fb1a', near(parseFloat(val('s1gcf')), trueGCF, 0.01));
}
function checkStep2(){
  const p = window.__TWIST_APPLIED__ ? Object.assign({}, PARAMS, {hex_labor_premium: 0.0}) : PARAMS;
  const r = evaluate(p);
  const costA = -r.A, costB = -r.B;
  const margin = 100 * Math.abs(costA - costB) / Math.max(costA, costB);
  fb('fb2a', near(parseFloat(val('s2costA')), costA, 0.02));
  fb('fb2b', near(parseFloat(val('s2costB')), costB, 0.02));
  fb('fb2c', near(parseFloat(val('s2margin')), margin, 0.5));
}
""",
    "glossary_js": """{
  "Hexagon": {def: "A polygon with six sides.",
    url: "https://www.mathsisfun.com/geometry/interior-angles-polygons.html"},
  "Octagon": {def: "A polygon with eight sides.",
    url: "https://www.mathsisfun.com/geometry/interior-angles-polygons.html"},
  "Regular Polygon": {def: "A polygon whose sides are all equal length and whose angles are all equal.",
    url: "https://www.mathsisfun.com/geometry/interior-angles-polygons.html"},
  "Sum of the Interior Angles of a Polygon Theorem": {def: "The sum of a polygon's interior angles equals (n minus 2) times 180 degrees, where n is the number of sides.",
    url: "https://www.mathsisfun.com/geometry/interior-angles-polygons.html"},
  "Greatest Common Factor": {def: "The largest number that divides evenly into two or more numbers.",
    url: "https://www.mathsisfun.com/greatest-common-factor.html"},
  "Percent": {def: "A ratio that compares a number to 100 -- literally \\"per hundred.\\"",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Area": {def: "The amount of two-dimensional space a shape covers.",
    url: "https://www.khanacademy.org/math/geometry-home/geometry-volume-surface-area"},
  "Ratio": {def: "A way of comparing two quantities by division, written a:b or a/b.",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"}
}""",
    "howto_js": """[
  ["how to find the measure of an interior angle of a polygon given the other angles", "Sum of the Interior Angles of a Polygon Theorem"],
  ["how to find the greatest common factor of a set of numbers", "Greatest Common Factor"],
  ["how to find the percent of a number", "Percent"]
]""",
    "on_twist_toggle_js": """
function onTwistToggle(){
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
}
""",
}
