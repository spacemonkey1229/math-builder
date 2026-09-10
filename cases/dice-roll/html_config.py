CONFIG = {
    "strand_summary": "Statistics And Probability &middot; Sampling And Experiments",
    "protagonist": "Marisol Ibarra, Compliance Audit Coordinator",
    "option_a_label": "The Statewide Draw",
    "option_a_text": "A multistage sample: 5 of 12 working-roster counties chosen by simple random sampling, then audit sessions inside each selected county chosen by systematic sampling -- every region of the state has a real chance of an in-person Division visit.",
    "option_b_label": "The Front Range Loop",
    "option_b_text": "A convenience sample of the 5 counties nearest the Denver office -- cheaper and simpler to run, but the Eastern Plains, the San Luis Valley, and the Western Slope are never visited, no matter how many cycles pass.",
    "challenge3_summary": "Include: <strong>D1</strong> a population-and-sample description (working roster vs. full state, and the percent each represents); <strong>D2</strong> the Statewide Draw's realized county selection plus each selected county's systematic-sampling interval and starting point; <strong>D3</strong> a cluster-sampling cost check (full-census review cost vs. the systematic subsample); <strong>D4</strong> a Front Range Loop representativeness analysis (single-cycle and three-cycle selection probability for a remote county); <strong>D5</strong> a total program cost comparison; <strong>D6</strong> a bar graph and a pie chart.",
    "deliverables": [
        ["D1", "Population-and-sample description"],
        ["D2", "Statewide Draw sampling plan (SRS + systematic)"],
        ["D3", "Cluster-sampling cost check"],
        ["D4", "Front Range Loop representativeness + probability"],
        ["D5", "Total program cost comparison"],
        ["D6", "Bar graph + pie chart"],
    ],
    "notebook_steps_html": """
  <div class="stepbox">
    <h4>Step 1 &mdash; Population, sample, and percent (D1)</h4>
    <div class="goal">This case's working roster has 12 counties (Appendix A); the state actually has 64. This cycle's visit sample is 5 counties. What percent of the 12-county working roster does the sample represent? What percent of the full 64-county state would that scale to?</div>
    <div class="fieldrow"><label for="s1pctroster">Percent of the 12-county working roster (%)</label><input type="number" id="s1pctroster" step="0.01"><span id="fb1a" class="fb"></span></div>
    <div class="fieldrow"><label for="s1pctstate">Percent of the full 64-county state (%)</label><input type="number" id="s1pctstate" step="0.01"><span id="fb1b" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; Selection probability, one cycle and three cycles (D4)</h4>
    <div class="goal">Under The Statewide Draw, 5 of 12 roster counties are chosen each cycle by simple random sampling. What is the probability a <em>specific</em> county (say, a Western Slope or San Luis Valley county) is selected in a single cycle? What is the probability it is selected at least once across three independent cycles? (Hint: find the probability it is <em>never</em> selected in three cycles first, then subtract from 1.) Compare both numbers to what The Front Range Loop gives that same county, every cycle, forever.</div>
    <div class="fieldrow"><label for="s2p1">P(selected in one cycle), Statewide Draw (%)</label><input type="number" id="s2p1" step="0.01"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2p3">P(selected at least once in 3 cycles), Statewide Draw (%)</label><input type="number" id="s2p3" step="0.01"><span id="fb2b" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
    <p class="side-note">What is that same county's probability of ever being visited under The Front Range Loop, no matter how many cycles run?</p>
  </div>

  <div class="stepbox">
    <h4>Step 3 &mdash; Total program cost and the margin (D5)</h4>
    <div class="goal">Using Appendix C's rates and Appendix A's distances, compute each option's total program cost (mileage + lodging + M&amp;IE + staff time) for its 5-county visit list, then the percent margin between them.</div>
    <div class="fieldrow"><label for="s3a">Option A (Statewide Draw) total cost (USD)</label><input type="number" id="s3a" step="0.01"><span id="fb3a" class="fb"></span></div>
    <div class="fieldrow"><label for="s3b">Option B (Front Range Loop) total cost (USD)</label><input type="number" id="s3b" step="0.01"><span id="fb3b" class="fb"></span></div>
    <div class="fieldrow"><label for="s3m">Percent margin between them (%)</label><input type="number" id="s3m" step="0.01"><span id="fb3c" class="fb"></span></div>
    <button onclick="checkStep3()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 4 &mdash; The cluster cost check (D3)</h4>
    <div class="goal">Appendix B lists how many audit sessions are scheduled this cycle in each Statewide Draw county, and the target of 2 sessions observed per county. At $25.00 per session reviewed (Appendix C), what would it cost to review <em>every</em> scheduled session in those 5 counties (the full cluster), versus the systematic subsample of 2 per county?</div>
    <div class="fieldrow"><label for="s4full">Full-cluster-census review cost (USD)</label><input type="number" id="s4full" step="0.01"><span id="fb4a" class="fb"></span></div>
    <div class="fieldrow"><label for="s4sub">Systematic-subsample review cost (USD)</label><input type="number" id="s4sub" step="0.01"><span id="fb4b" class="fb"></span></div>
    <button onclick="checkStep4()">Check</button>
  </div>
""",
    "twist_narrative_html": """
      <p>Colorado's own real risk-limiting audit -- the one that already happens in all 64 counties regardless of Marisol's visit plan -- sets its random seed at a public meeting where staff roll 20 ten-sided dice on camera while the meeting livestreams, and anyone can verify the resulting seed and recompute the ballot selection afterward (Appendix B, Appendix E S4).</p>
      <p>Suppose a county clerk pushes back on The Statewide Draw: "If a county's own audit already uses a fully public, verifiable random process, why does it matter whether the <em>Division's observers</em> get there by a random draw or by convenience? The audit itself is equally random either way." Using your D4 probability numbers, what is the flaw in that argument -- what, specifically, is being sampled by Marisol's visit plan that is <em>not</em> the same thing the county-level RLA already randomizes?</p>
""",
    "twist_apply_label": "I've addressed the county clerk's pushback in my D4/pitch reasoning",
    "js_data_block": """
const PARAMS = {
  mileage_rate: 0.68, mie_rate: 68.0, lodging_rate: 110.0,
  staff_daily_rate: 450.0, overnight_threshold_mi: 150.0, n_visits: 5,
  session_review_cost: 25.0,
  a_dist: {jefferson: 15, boulder: 66, pueblo: 114, kitcarson: 169, alamosa: 235},
  b_dist: {jefferson: 15, douglas: 29, larimer: 64, boulder: 66, elpaso: 69},
  a_sessions: {jefferson: 18, boulder: 14, pueblo: 9, kitcarson: 3, alamosa: 4},
  sessions_target_per_county: 2,
  roster_size: 12, state_counties: 64, sample_size: 5,
};
function visitCost(oneWayMi, p){
  const mileage = p.mileage_rate * 2 * oneWayMi;
  const lodging = oneWayMi > p.overnight_threshold_mi ? p.lodging_rate : 0.0;
  return {mileage, lodging};
}
function totalCost(distObj, p){
  let mileage = 0, lodging = 0;
  Object.values(distObj).forEach(d => { const c = visitCost(d, p); mileage += c.mileage; lodging += c.lodging; });
  const n = Object.keys(distObj).length;
  const mie = p.mie_rate * n;
  const staff = p.staff_daily_rate * n;
  return {mileage, lodging, mie, staff, total: mileage + lodging + mie + staff};
}
function evaluateDetail(params){
  const p = Object.assign({}, PARAMS, params||{});
  const a = totalCost(p.a_dist, p);
  const b = totalCost(p.b_dist, p);
  const cheaper = a.total < b.total ? 'A' : 'B';
  const other = cheaper === 'A' ? 'B' : 'A';
  const costs = {A: a.total, B: b.total};
  const marginPct = (costs[other] - costs[cheaper]) / costs[other] * 100.0;
  return {a, b, cheaper, marginPct};
}
function evaluate(params){
  const d = evaluateDetail(params);
  const ceiling = 2 * Math.max(d.a.total, d.b.total);
  return {A: ceiling - d.a.total, B: ceiling - d.b.total};
}
function evaluate_twist(params){
  const p = Object.assign({}, params||{});
  const a_dist = Object.assign({}, (p.a_dist || PARAMS.a_dist));
  a_dist.alamosa = a_dist.alamosa * 0.5;
  return evaluate(Object.assign({}, p, {a_dist}));
}
function probSelected(sampleSize, rosterSize, cycles){
  const pNot = 1 - sampleSize / rosterSize;
  return 1 - Math.pow(pNot, cycles);
}
""",
    "notebook_check_functions": """
function checkStep1(){
  const pctRoster = PARAMS.sample_size / PARAMS.roster_size * 100.0;
  const pctState = PARAMS.sample_size / PARAMS.state_counties * 100.0;
  fb('fb1a', near(parseFloat(val('s1pctroster')), pctRoster, 0.5));
  fb('fb1b', near(parseFloat(val('s1pctstate')), pctState, 0.5));
}
function checkStep2(){
  const p1 = PARAMS.sample_size / PARAMS.roster_size * 100.0;
  const p3 = probSelected(PARAMS.sample_size, PARAMS.roster_size, 3) * 100.0;
  fb('fb2a', near(parseFloat(val('s2p1')), p1, 0.5));
  fb('fb2b', near(parseFloat(val('s2p3')), p3, 1.0));
}
function checkStep3(){
  const d = evaluateDetail({});
  fb('fb3a', near(parseFloat(val('s3a')), d.a.total, 1.0));
  fb('fb3b', near(parseFloat(val('s3b')), d.b.total, 1.0));
  fb('fb3c', near(parseFloat(val('s3m')), d.marginPct, 0.5));
}
function checkStep4(){
  const totalSessions = Object.values(PARAMS.a_sessions).reduce((a,b)=>a+b, 0);
  const nCounties = Object.keys(PARAMS.a_sessions).length;
  const subSessions = nCounties * PARAMS.sessions_target_per_county;
  const fullCost = totalSessions * PARAMS.session_review_cost;
  const subCost = subSessions * PARAMS.session_review_cost;
  fb('fb4a', near(parseFloat(val('s4full')), fullCost, 1.0));
  fb('fb4b', near(parseFloat(val('s4sub')), subCost, 1.0));
}
""",
    "glossary_js": """{
  "Population": {def: "The entire group -- every county, every audit session -- that a sampling plan is trying to describe.",
    url: "https://www.khanacademy.org/math/statistics-probability/designing-studies/sampling-methods-stats/a/sampling-methods-review"},
  "Sample": {def: "The subset of the population actually selected and visited, used to stand in for the whole.",
    url: "https://www.khanacademy.org/math/statistics-probability/designing-studies/sampling-methods-stats/a/sampling-methods-review"},
  "Sample Size": {def: "How many members of the population are actually included in the sample.",
    url: "https://www.khanacademy.org/math/statistics-probability/designing-studies/sampling-methods-stats/a/sampling-methods-review"},
  "Random": {def: "Chosen by a chance process where every eligible member has a known, calculable probability of selection.",
    url: "https://www.khanacademy.org/math/statistics-probability/designing-studies/sampling-methods-stats/a/sampling-methods-review"},
  "Simple Random Sampling": {def: "Every member and every group of members has an equal chance of ending up in the sample.",
    url: "https://www.khanacademy.org/math/statistics-probability/designing-studies/sampling-methods-stats/a/sampling-methods-review"},
  "Systematic Sampling": {def: "Order the population, pick a random starting point, then take every k-th member from there.",
    url: "https://www.khanacademy.org/math/statistics-probability/designing-studies/sampling-methods-stats/a/sampling-methods-review"},
  "Cluster Sampling": {def: "Split the population into groups, randomly select some whole groups, and take every member inside the selected groups.",
    url: "https://www.khanacademy.org/math/statistics-probability/designing-studies/sampling-methods-stats/a/sampling-methods-review"},
  "Multistage Sampling": {def: "A sample built in more than one stage -- e.g. randomly select groups (a cluster draw), then randomly subsample members inside each selected group, instead of taking everyone in it.",
    url: "https://www.khanacademy.org/math/statistics-probability/designing-studies/sampling-methods-stats/a/sampling-methods-review"},
  "Convenience Sampling": {def: "Choosing whichever members of the population are easiest to reach, not a random process -- usually biased.",
    url: "https://www.khanacademy.org/math/statistics-probability/designing-studies/sampling-methods-stats/a/sampling-methods-review"},
  "Probability": {def: "How likely an event is to happen, from 0 (never) to 1 (certain) -- (number of favorable outcomes) / (total outcomes).",
    url: "https://www.khanacademy.org/math/statistics-probability/probability-library/basic-theoretical-probability/a/probability-the-basics"},
  "Percent": {def: "A ratio that compares a number to 100 -- literally \\"per hundred.\\"",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Proportion": {def: "An equation stating that two ratios are equal, e.g. used to scale a sample-size rule up or down.",
    url: "https://www.khanacademy.org/math/cc-seventh-grade-math/cc-7th-ratio-proportion/cc-7th-write-and-solve-proportions/v/find-an-unknown-in-a-proportion"},
  "Bar Graph": {def: "A chart that uses rectangular bars to compare values across categories.",
    url: "https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-data-statistics"},
  "Pie Chart": {def: "A circular chart divided into slices, each slice's size showing its share of the whole.",
    url: "https://www.khanacademy.org/math/statistics-probability/analyzing-categorical-data/one-categorical-variable/v/reading-pie-graphs-circle-graphs"}
}""",
    "howto_js": """[
  ["how to find the percent of a number", "Percent"],
  ["how to convert numbers to percents", "Percent"],
  ["how to find a missing amount in a proportion", "Proportion"],
  ["how to round a number to a specified place value", "Sample Size"],
  ["how to determine the probability of a single event", "Probability"],
  ["how to add multi-digit numbers", "Sample"],
  ["how to multiply any two numbers", "Sample Size"],
  ["how to create a pie chart given a set of data", "Pie Chart"]
]""",
    "on_twist_toggle_js": """
function onTwistToggle(){
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
}
""",
    "extra_css": """
.sterm{position:relative;color:#1a4d7a;text-decoration:none;border-bottom:1.5px dotted #2e8b57;cursor:help;font-weight:600}
.sterm:hover, .sterm:focus{background:#fdf3d0}
.sterm .tip{visibility:hidden;opacity:0;position:absolute;left:50%;bottom:135%;transform:translateX(-50%);
  width:260px;background:#1a2b3c;color:#fff;font-weight:400;font-size:0.82rem;line-height:1.35;
  padding:10px 12px;border-radius:8px;z-index:50;transition:opacity .15s;box-shadow:0 6px 18px rgba(0,0,0,.25)}
.sterm .tip .go{display:block;margin-top:6px;color:#f2c14e;font-weight:700}
.sterm .tip:after{content:"";position:absolute;top:100%;left:50%;transform:translateX(-50%);border:6px solid transparent;border-top-color:#1a2b3c}
.sterm:hover .tip, .sterm:focus .tip{visibility:visible;opacity:1}
#storyGlossaryCard .glossary-grid{display:flex;flex-wrap:wrap;gap:10px 16px;margin-top:8px}
#storyGlossaryCard .glossary-grid .sterm{display:inline-block;background:#fff;border:1px solid #ddd;border-bottom:1.5px dotted #2e8b57;border-radius:6px;padding:4px 10px}
.diagram-wrap{overflow-x:auto;margin:12px 0}
""",
}
