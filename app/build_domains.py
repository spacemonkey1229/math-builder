#!/usr/bin/env python3
"""
build_domains.py — emits readmodel/domains.json and readmodel/domain_coverage.json

domains.json is the Phase-4 "Root Connections" spine: the application domains that
consume the curriculum tree. It supersedes the 3-item curriculum_tree.intersections[].

Authoring content lives in DOMAINS below. Everything else is derived or validated.
Run:  python3 app/build_domains.py            # write both files
      python3 app/build_domains.py --dry-run  # validate only
"""
import json, os, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RM = os.path.join(ROOT, "readmodel")

# --------------------------------------------------------------------------
# source-verification ledger
# Every URL below was fetched during authoring on 2026-07-31.
# state: LIVE (fetched, renders, free) | LIVE_JS (renders only in a browser,
#        still free) | LIVE_LOGIN (free but account required) | KNOWLEDGE (listed
#        from knowledge, NOT fetched)
# --------------------------------------------------------------------------

CLUSTERS = [
    {"id": "health-life", "name": "Health & Life Sciences"},
    {"id": "earth-climate", "name": "Earth, Climate & Environment"},
    {"id": "food-energy", "name": "Food, Energy & Resources"},
    {"id": "movement", "name": "Movement & Logistics"},
    {"id": "built", "name": "Built Environment"},
    {"id": "making", "name": "Making & Materials"},
    {"id": "space-sky", "name": "Space & Sky"},
    {"id": "digital", "name": "Digital Systems & Information"},
    {"id": "money-risk", "name": "Money, Risk & Markets"},
    {"id": "civic", "name": "Civic Life, Law & Learning"},
    {"id": "culture-play", "name": "Culture, Play & Performance"},
    {"id": "deep-time", "name": "Deep Time & Language"},
]


def S(label, url, state, note):
    return {"label": label, "url": url, "verified": state, "offers": note}


DOMAINS = [
# ===================== HEALTH & LIFE SCIENCES =============================
{
 "id": "epidemiology",
 "name": "Epidemiology & Public Health",
 "cluster": "Health & Life Sciences",
 "one_line": "Modeling how disease moves through a population and where to spend the one dose you have.",
 "math_branches": ["pre-algebra", "algebra-2", "prob-stats", "calculus"],
 "signature_skills": [
   "statistics-and-probability-population", "statistics-and-probability-sample-size",
   "statistics-and-probability-conditional-probability",
   "statistics-and-probability-how-to-determine-the-probability-of-conditional-events",
   "advanced-numbers-how-to-find-a-whole-given-the-percent-and-the-part-of-the-whole",
   "advanced-operations-how-to-evaluate-an-exponential-expression",
   "statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data",
   "measurement-ratio"],
 "why_it_engages": "Every kid now has a personal memory of a school closing, and they still argue about whether it was worth it.",
 "decision_archetypes": [
   "Vaccinate the 5,000 highest-contact adults or the 12,000 most vulnerable elderly, with doses for only one group.",
   "Close schools for two weeks now on a rising curve, or stay open and add testing.",
   "Spend the county budget on a mobile clinic in one dense neighbourhood or on mailed test kits county-wide."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("CDC WONDER", "https://wonder.cdc.gov/", "LIVE", "queryable US mortality, natality and disease counts by county/age"),
   S("WHO Global Health Observatory", "https://www.who.int/data/gho", "LIVE", "country-level indicators for 194 member states"),
   S("Our World in Data", "https://ourworldindata.org/", "LIVE", "downloadable CSV behind every chart"),
   S("NYT COVID-19 data archive", "https://github.com/nytimes/covid-19-data", "LIVE", "daily US county case/death series, CSV, archived but complete")],
  "note": "Counts and rates are trivially easy. What is hard for a student is a real contact-rate or R0 for a named local outbreak — those come from modelling papers, not open portals, and must be handled as a stated assumption."},
 "existing_cases": ["Cold Chain"],
 "careers": [
  {"title": "Epidemiologist", "math_used": "Computes attack rates and case-fatality ratios, fits exponential growth to early case counts, and reads 95% confidence intervals to decide whether two neighbourhoods actually differ.", "entry_path": "BS in biology/statistics then an MPH in epidemiology; state health departments hire at the MPH level."},
  {"title": "Public Health Data Analyst", "math_used": "Age-standardises crude rates against a reference population and builds per-100,000 comparisons so a town of 4,000 can be compared with a city of 400,000.", "entry_path": "Bachelor's in public health, stats or geography; SQL and Excel are the actual gate."},
  {"title": "Vaccine Cold-Chain Logistician", "math_used": "Converts vial counts to doses under a stated wastage fraction, then solves a route-and-capacity problem against a fixed cooler volume.", "entry_path": "Supply-chain or logistics degree, or military logistics experience; UNICEF/Gavi field roles."}],
 "authoring_priority": "MEDIUM"
},
{
 "id": "clinical-medicine",
 "name": "Clinical Medicine, Diagnostics & Trials",
 "cluster": "Health & Life Sciences",
 "one_line": "Deciding whether a test result, or a drug, is telling you the truth.",
 "math_branches": ["pre-algebra", "algebra-1", "prob-stats"],
 "signature_skills": [
   "statistics-and-probability-conditional-probability",
   "statistics-and-probability-how-to-determine-the-probability-of-conditional-events",
   "statistics-and-probability-experiment", "statistics-and-probability-variability",
   "statistics-and-probability-simple-random-sampling",
   "statistics-and-probability-how-to-find-a-missing-data-element-given-the-mean-and-the-remaining-",
   "statistics-and-probability-box-and-whisker-plot",
   "statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data",
   "statistics-and-probability-outlier"],
 "why_it_engages": "The false-positive paradox genuinely shocks people the first time they see it, including adults who have had the test.",
 "decision_archetypes": [
   "Screen every 40-year-old or only the high-risk 15%, when the test is 95% accurate and the disease is rare.",
   "Stop a trial early because the drug looks like it is working, or run it to full enrolment.",
   "Buy one fast, less accurate analyser or two slow, accurate ones for the same money."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("ClinicalTrials.gov", "https://clinicaltrials.gov/", "LIVE", "protocols, enrolment counts and posted results for registered trials"),
   S("CDC NHANES", "https://www.cdc.gov/nchs/nhanes/index.htm", "LIVE", "raw exam + lab microdata on a real US sample"),
   S("CDC National Vital Statistics System", "https://www.cdc.gov/nchs/nvss/index.htm", "LIVE", "births, deaths, cause-of-death tables"),
   S("CDC WONDER", "https://wonder.cdc.gov/", "LIVE", "mortality by cause, age, county")],
  "note": "Test sensitivity/specificity for a *specific commercial device* is usually in the FDA 510(k) summary rather than a data portal; if a case needs one, cite the 510(k) or state it as an assumption. Patient-level records (MIMIC etc.) require credentialing and are out of reach for students."},
 "existing_cases": ["Cardiology", "End Of Life", "Biostatician", "Medical Statician", "Medical Transport", "Psychologist"],
 "careers": [
  {"title": "Biostatistician", "math_used": "Powers a trial by solving for the sample size that detects a 4-point difference at 80% power, then reports a hazard ratio with its confidence interval.", "entry_path": "MS or PhD in biostatistics; pharma, CROs and academic medical centres."},
  {"title": "Diagnostic Radiologist", "math_used": "Reads sensitivity and specificity off an ROC curve and applies Bayes' rule to a pre-test probability before calling a scan positive.", "entry_path": "MD plus a 5-year radiology residency."},
  {"title": "Clinical Pharmacologist", "math_used": "Fits dose-response curves, computes number-needed-to-treat from absolute risk reduction, and scales dosing by body-surface area.", "entry_path": "PharmD or MD/PhD; regulatory and pharma roles."}],
 "authoring_priority": "LOW"
},
# ===================== EARTH, CLIMATE & ENVIRONMENT =======================
{
 "id": "climate-science",
 "name": "Climate & Atmospheric Science",
 "cluster": "Earth, Climate & Environment",
 "one_line": "Separating a trend from noise in a record that swings wildly year to year.",
 "math_branches": ["pre-algebra", "algebra-1", "algebra-2", "prob-stats", "calculus"],
 "signature_skills": [
   "statistics-and-probability-line-of-best-fit",
   "statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data",
   "statistics-and-probability-slope",
   "statistics-and-probability-how-to-identify-the-slope-of-a-line-given-a-set-of-data-or-a-graph-o",
   "statistics-and-probability-how-to-write-a-linear-equation-given-a-graph-of-a-line-of-a-set-of-d",
   "statistics-and-probability-how-to-draw-a-line-of-a-set-of-data-given-its-linear-equation",
   "statistics-and-probability-correlation", "statistics-and-probability-non-linear",
   "advanced-numbers-negative-number", "advanced-numbers-how-to-subtract-with-negative-numbers"],
 "why_it_engages": "They have been told the answer their whole life and have never once been handed the actual numbers and asked to check.",
 "decision_archetypes": [
   "Spend a town's resilience budget on a sea wall sized for the 1-in-100 flood, or on buying out the twelve houses that flood most.",
   "Site the new solar farm where irradiance is highest or where transmission already exists.",
   "Report a warming trend from 30 years of data or say the record is too short to call."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("NOAA Climate at a Glance", "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/", "LIVE", "monthly/annual temp & precip by US city, state, country, with CSV"),
   S("NASA GISTEMP", "https://data.giss.nasa.gov/gistemp/", "LIVE", "global surface temperature anomaly series"),
   S("Our World in Data — CO2 & GHG", "https://ourworldindata.org/co2-and-greenhouse-gas-emissions", "LIVE", "per-country emissions, per-capita, cumulative, all CSV"),
   S("NOAA National Data Buoy Center", "https://www.ndbc.noaa.gov/", "LIVE", "hourly wind, wave and air/sea temperature per buoy")],
  "note": "Observations are excellent and free. Model *projections* (CMIP6) are large NetCDF files a middle-schooler cannot open — use IPCC summary tables instead, or keep the case in the observational record."},
 "existing_cases": [],
 "careers": [
  {"title": "Climate Scientist", "math_used": "Removes a seasonal cycle by subtracting a monthly climatology, then tests whether the residual slope differs from zero.", "entry_path": "PhD in atmospheric or earth science; MS is enough for many lab/analyst roles."},
  {"title": "Catastrophe Risk Modeller", "math_used": "Converts a return period into an annual exceedance probability (1-in-100 = 1%) and stacks independent-year probabilities over a 30-year mortgage.", "entry_path": "Maths/physics degree into a reinsurer or a firm like Verisk/Moody's RMS."},
  {"title": "Air Quality Engineer", "math_used": "Runs Gaussian plume dispersion — an exponential in crosswind distance — to place monitors and set stack heights.", "entry_path": "BS in environmental/chemical engineering; state EPA permitting roles."}],
 "authoring_priority": "MEDIUM"
},
{
 "id": "oceanography",
 "name": "Oceans, Tides & Marine Science",
 "cluster": "Earth, Climate & Environment",
 "one_line": "The sea is a sum of sine waves, and getting a ship over a sandbar means predicting them.",
 "math_branches": ["geometry", "algebra-2", "precalc", "prob-stats", "calculus"],
 "signature_skills": [
   "number-sense-depth", "measurement-how-to-find-elapsed-time",
   "measurement-how-to-find-the-start-or-end-time-given-the-start-or-end-and-the-elapsed-time",
   "measurement-how-to-add-and-subtract-time", "number-sense-height",
   "statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data",
   "measurement-how-to-convert-an-amount-with-compound-units",
   "geometry-how-to-find-the-volume-of-a-prism",
   "pre-calculus-sine-function", "pre-calculus-amplitude", "pre-calculus-period-of-a-function",
   "calculus-definite-integral"],
 "why_it_engages": "A tide table is a real prediction of the future, published years in advance, and it is right — that is a strange and convincing thing to hold.",
 "decision_archetypes": [
   "Sail the loaded ship at 04:00 on a marginal tide, or wait 11 hours for the spring tide and miss the contract.",
   "Site the tidal turbine in the fast narrow channel or the slower but deeper one.",
   "Dredge the channel by 1.2 m or lighten every ship by 800 tonnes."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("NOAA Tides & Currents", "https://tidesandcurrents.noaa.gov/", "LIVE", "6-minute observed water level and published tide predictions per station"),
   S("NOAA National Data Buoy Center", "https://www.ndbc.noaa.gov/", "LIVE", "wave height, period and direction, hourly"),
   S("NOAA Office of Coast Survey", "https://nauticalcharts.noaa.gov/", "LIVE", "free electronic nautical charts with soundings")],
  "note": "Tide, wave and chart data are among the best free datasets that exist. Vessel draft and cargo tonnage for a *named* ship are commercial (AIS resellers) — build the case around a stated vessel spec instead."},
 "existing_cases": [],
 "careers": [
  {"title": "Harbour Pilot", "math_used": "Computes under-keel clearance as charted depth plus predicted tide minus draft minus squat, with a stated safety margin, and back-solves the latest safe departure time.", "entry_path": "Sea time and a mate's licence, then a competitive state pilotage apprenticeship."},
  {"title": "Physical Oceanographer", "math_used": "Decomposes a water-level record into tidal constituents — sinusoids of known period — and takes the residual as storm surge.", "entry_path": "PhD in oceanography; NOAA, Scripps, WHOI."},
  {"title": "Hydrographic Surveyor", "math_used": "Turns multibeam sonar travel times into depths using the speed of sound in water, correcting for the beam angle with trigonometry.", "entry_path": "Survey/geomatics degree plus IHO Category B certification."}],
 "authoring_priority": "HIGH"
},
{
 "id": "hydrology-water",
 "name": "Water Supply & Hydrology",
 "cluster": "Earth, Climate & Environment",
 "one_line": "A reservoir is a volume with an inflow, an outflow and a town that will not stop drinking.",
 "math_branches": ["pre-algebra", "geometry", "algebra-1", "calculus"],
 "signature_skills": [
   "geometry-volume", "geometry-how-to-find-the-volume-of-a-prism",
   "geometry-how-to-find-the-volume-of-a-cone", "measurement-volume",
   "measurement-how-to-convert-an-amount-with-compound-units",
   "measurement-how-to-convert-an-amount-from-one-unit-to-another-unit",
   "measurement-ratio", "measurement-proportion",
   "measurement-how-to-find-a-missing-amount-in-a-proportion"],
 "why_it_engages": "Reservoir drawdown is the rare crisis you can watch happen on a photograph of a bathtub ring.",
 "decision_archetypes": [
   "Cut agricultural allocation by 30% or municipal allocation by 12%, when both save the same acre-feet.",
   "Build the pipeline from the distant clean source, or the treatment plant on the dirty near one.",
   "Fix the 18% distribution leak or find a new well field."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("USGS National Water Dashboard", "https://dashboard.waterdata.usgs.gov/", "LIVE", "live gauge height and discharge at thousands of US stream gauges"),
   S("USGS Water Services API", "https://waterservices.usgs.gov/", "LIVE", "machine-readable historical discharge series, no key"),
   S("EPA / Water Quality Portal", "https://www.epa.gov/waterdata/water-quality-data-download", "LIVE", "sampled contaminant concentrations by site")],
  "note": "Streamflow is superb. Reservoir *storage* curves and municipal per-capita demand vary by utility; many US utilities publish an annual water quality/consumption report as a PDF — cite the specific utility's report rather than a national figure."},
 "existing_cases": [],
 "careers": [
  {"title": "Water Resources Engineer", "math_used": "Balances a reservoir with inflow minus release minus evaporation over a monthly timestep, converting cfs to acre-feet, and sizes the spillway to the design storm.", "entry_path": "BS civil engineering plus a PE licence."},
  {"title": "Hydrologist", "math_used": "Fits a flood-frequency distribution to an annual-peak series to get the 1-in-100 discharge, then propagates it through a rating curve to a stage.", "entry_path": "BS/MS in hydrology or geoscience; USGS and state water agencies."},
  {"title": "Irrigation District Manager", "math_used": "Allocates acre-feet across crops by consumptive-use ratio and prices the shortfall so total withdrawals match the decree.", "entry_path": "Agronomy or ag-engineering degree plus district experience."}],
 "authoring_priority": "MEDIUM"
},
{
 "id": "wildlife-conservation",
 "name": "Wildlife & Biodiversity Conservation",
 "cluster": "Earth, Climate & Environment",
 "one_line": "You can afford to protect one habitat corridor; count what each one actually saves.",
 "math_branches": ["pre-algebra", "geometry", "prob-stats", "algebra-2"],
 "signature_skills": [
   "statistics-and-probability-sample", "statistics-and-probability-population",
   "statistics-and-probability-stratified-sampling", "statistics-and-probability-cluster-sampling",
   "statistics-and-probability-systematic-sampling",
   "measurement-how-to-find-a-missing-amount-in-a-proportion",
   "geometry-area", "geometry-perimeter",
   "geometry-how-to-find-the-measure-of-the-perimeter-of-a-polygon"],
 "why_it_engages": "Mark-recapture is a magic trick — you catch 40 fish and suddenly you know how many are in the whole lake.",
 "decision_archetypes": [
   "Buy 900 acres of prime habitat or 3,200 acres of degraded land that connects two existing reserves.",
   "Cull the invasive predator or fence the last nesting beach.",
   "Fund the captive breeding programme or the ranger patrol, with survival odds for each."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("GBIF", "https://www.gbif.org/", "LIVE", "3bn+ georeferenced species occurrence records, free CSV download"),
   S("IUCN Red List", "https://www.iucnredlist.org/", "LIVE", "assessed status, population trend and range maps per species"),
   S("Movebank", "https://www.movebank.org/", "LIVE", "GPS animal tracking tracks, many openly licensed"),
   S("eBird", "https://ebird.org/data/download", "LIVE", "citizen-science bird observations; bulk download is a free request")],
  "note": "Occurrence and status data are excellent. Absolute population *estimates* with error bars are patchy and often a decade old — treat any single population number as a cited estimate with its year, never as current truth."},
 "existing_cases": [],
 "careers": [
  {"title": "Wildlife Biologist", "math_used": "Estimates abundance by Lincoln-Petersen mark-recapture (N = MC/R) and reports the interval, not just the point.", "entry_path": "BS wildlife biology; MS for most federal/state positions."},
  {"title": "Conservation GIS Analyst", "math_used": "Computes patch area, edge-to-area ratio and least-cost corridor paths over a raster grid to rank reserve designs.", "entry_path": "Geography/ecology degree plus GIS certificate; QGIS is free to learn on."},
  {"title": "Fisheries Stock Assessor", "math_used": "Fits a surplus-production model to catch-per-unit-effort to set a maximum sustainable yield quota.", "entry_path": "MS in fisheries science; NOAA Fisheries and regional councils."}],
 "authoring_priority": "HIGH"
},
{
 "id": "disaster-response",
 "name": "Disaster Response & Emergency Management",
 "cluster": "Earth, Climate & Environment",
 "one_line": "Limited trucks, a closing window, and a map that is changing while you plan.",
 "math_branches": ["pre-algebra", "geometry", "algebra-1", "prob-stats", "discrete"],
 "signature_skills": [
   "measurement-how-to-find-elapsed-time", "measurement-how-to-add-and-subtract-time",
   "measurement-how-to-convert-an-amount-with-compound-units",
   "geometry-area", "geometry-how-to-find-the-area-of-a-circle",
   "statistics-and-probability-how-to-determine-the-probability-of-a-single-event",
   "advanced-numbers-how-to-find-the-percent-of-a-number",
   "number-sense-how-to-compare-two-or-more-values"],
 "why_it_engages": "Evacuation timing is a maths problem where the wrong answer is on the news that night.",
 "decision_archetypes": [
   "Order a full evacuation 36 hours out on a 40% strike probability, or wait 12 hours for a better forecast and lose road capacity.",
   "Stage the supply depot centrally or split it into two half-sized depots nearer the coast.",
   "Cut the firebreak along the ridge or defend the town edge directly."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("OpenFEMA data sets", "https://www.fema.gov/about/openfema/data-sets", "LIVE", "declared disasters, NFIP claims, individual assistance, all CSV/API"),
   S("NOAA Billion-Dollar Disasters", "https://www.ncei.noaa.gov/access/billions/", "LIVE", "event-level US cost and fatality series since 1980"),
   S("USGS Earthquake Catalog", "https://earthquake.usgs.gov/earthquakes/search/", "LIVE", "every event with magnitude, depth, location, CSV export"),
   S("OpenStreetMap", "https://www.openstreetmap.org/", "LIVE", "road network and building footprints for evacuation routing")],
  "note": "Hazard and cost data are strong. Real-time road capacity and shelter occupancy during an event are almost never published afterwards — a case needing those must state them as scenario assumptions in the open."},
 "existing_cases": ["Wildfire", "Airstrike", "Food Rationing"],
 "careers": [
  {"title": "Emergency Manager", "math_used": "Multiplies clearance time by lane capacity to get an evacuation window, then compares it against forecast landfall minus a stated safety margin.", "entry_path": "Emergency management degree or fire/EMS route plus FEMA credentialing."},
  {"title": "Wildfire Behaviour Analyst", "math_used": "Estimates rate of spread from slope, wind and fuel model, and projects an elliptical fire perimeter forward in hours.", "entry_path": "Fire science degree plus red-card qualifications and NWCG certification."},
  {"title": "Humanitarian Logistics Officer", "math_used": "Solves a knapsack over pallet weight and volume against aircraft payload, and computes days-of-supply per beneficiary.", "entry_path": "Logistics/supply-chain background; UN WFP, IFRC, MSF."}],
 "authoring_priority": "MEDIUM"
},
# ===================== FOOD, ENERGY & RESOURCES ===========================
{
 "id": "agriculture-food",
 "name": "Agriculture & Food Systems",
 "cluster": "Food, Energy & Resources",
 "one_line": "Yield per acre, price per bushel, and a planting decision you cannot take back for a year.",
 "math_branches": ["pre-algebra", "geometry", "algebra-1", "prob-stats"],
 "signature_skills": [
   "measurement-ratio", "measurement-proportion",
   "measurement-how-to-find-equivalent-ratios", "measurement-how-to-find-a-missing-amount-in-a-proportion",
   "geometry-area", "geometry-how-to-find-the-area-of-a-rectangle",
   "advanced-numbers-how-to-find-the-percent-of-a-number",
   "fractions-how-to-divide-a-whole-number-by-a-fraction",
   "statistics-and-probability-mean", "statistics-and-probability-range"],
 "why_it_engages": "A farm is the most legible business a teenager will ever see: one input, one output, one weather event that ruins it.",
 "decision_archetypes": [
   "Plant corn or soybeans on 400 acres, given last year's prices and this year's fertiliser cost.",
   "Buy the pivot irrigation system now or rent water for three more seasons.",
   "Sell the harvest at today's spot price or store it for four months at a stated cost per bushel."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("USDA NASS data & statistics", "https://www.nass.usda.gov/datasets/", "LIVE", "county-level yield, acreage, production and price files"),
   S("USDA NASS Quick Stats", "https://quickstats.nass.usda.gov/", "LIVE_JS", "interactive query over the same census/survey data; browser only"),
   S("USDA FoodData Central", "https://fdc.nal.usda.gov/", "LIVE", "nutrient composition per 100g for ~400k foods"),
   S("Our World in Data — Agricultural Production", "https://ourworldindata.org/agricultural-production", "LIVE", "global yields and land use, CSV per chart; sourced from FAOSTAT")],
  "note": "FAOSTAT's own site (fao.org/faostat) is a JavaScript app that will not load for a scripted fetch — reach the same numbers through Our World in Data, which republishes them with citations. Farm-level cost-of-production is published by USDA ERS as regional averages only, never per farm."},
 "existing_cases": ["Food Rationing", "Fast Food", "Catering"],
 "careers": [
  {"title": "Agronomist", "math_used": "Converts a soil test in ppm to pounds-per-acre of fertiliser using a stated soil bulk density, then computes marginal yield response per added pound.", "entry_path": "BS in agronomy or soil science; Certified Crop Adviser exam."},
  {"title": "Commodity Trader", "math_used": "Prices the basis (local cash minus futures) and computes carry — storage plus interest — to decide whether to sell now or hold.", "entry_path": "Finance/ag-econ degree into a grain merchandiser; Series 3 for brokered work."},
  {"title": "Food Scientist", "math_used": "Solves mass-balance blending problems — mixing two streams of known protein content to hit a spec — as a system of two equations.", "entry_path": "BS food science; IFT membership and plant experience."}],
 "authoring_priority": "MEDIUM"
},
{
 "id": "energy-grid",
 "name": "Energy Generation & the Grid",
 "cluster": "Food, Energy & Resources",
 "one_line": "Supply must equal demand every second, and the cheapest plant is not always the one you can turn on.",
 "math_branches": ["pre-algebra", "algebra-1", "algebra-2", "calculus", "prob-stats"],
 "signature_skills": [
   "measurement-how-to-convert-an-amount-with-compound-units",
   "measurement-unit", "measurement-how-to-convert-an-amount-from-one-unit-to-another-unit",
   "statistics-and-probability-how-to-create-a-histogram-given-a-set-of-data",
   "statistics-and-probability-mean", "statistics-and-probability-range",
   "advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-one-side",
   "advanced-numbers-how-to-find-the-percent-of-a-number"],
 "why_it_engages": "The grid is the largest machine ever built and it has to balance on a knife edge every single second, including right now.",
 "decision_archetypes": [
   "Build 200 MW of solar plus 4 hours of battery, or 120 MW of gas peaker, for the same capital.",
   "Pay for the transmission upgrade or curtail the wind farm 14% of the time.",
   "Charge the school bus fleet overnight at a low rate or midday off the roof array."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("EIA Open Data", "https://www.eia.gov/opendata/", "LIVE", "generation, capacity, fuel price and consumption series, free API"),
   S("EIA Hourly Electric Grid Monitor", "https://www.eia.gov/electricity/gridmonitor/dashboard/electric_overview/US48/US48", "LIVE", "hourly demand, generation by fuel and interchange per balancing authority"),
   S("NREL PVWatts", "https://pvwatts.nrel.gov/", "LIVE", "hourly modelled solar output for any address, free"),
   S("IEA Data & Statistics", "https://www.iea.org/data-and-statistics", "LIVE", "global energy statistics; free browsing, some full datasets are paid")],
  "note": "US hourly grid data is world-class and free. Actual plant *capital cost* and power-purchase-agreement prices are commercially confidential — use NREL's published Annual Technology Baseline ranges or Lazard's free LCOE report and cite the range, not a point."},
 "existing_cases": [],
 "careers": [
  {"title": "Grid Operator (Balancing Authority Dispatcher)", "math_used": "Stacks generator bids into a merit-order curve and finds the marginal unit that clears forecast load, second by second.", "entry_path": "Two-year technical degree plus NERC System Operator certification."},
  {"title": "Energy Analyst", "math_used": "Computes levelised cost of energy by discounting a 25-year cash flow against lifetime MWh at a stated capacity factor.", "entry_path": "Engineering or economics degree; utilities, consultancies, NGOs."},
  {"title": "Solar Design Engineer", "math_used": "Sizes an array from irradiance, module efficiency and roof area, then sets tilt and azimuth from the site's latitude and the sun's declination.", "entry_path": "BS electrical engineering or NABCEP certification."}],
 "authoring_priority": "MEDIUM"
},
{
 "id": "nuclear-energy",
 "name": "Nuclear Energy & Radioactive Waste",
 "cluster": "Food, Energy & Resources",
 "one_line": "Half-lives, shielding thickness and a container that must survive longer than any civilisation has lasted.",
 "math_branches": ["pre-algebra", "geometry", "algebra-2", "calculus"],
 "signature_skills": [
   "geometry-cylinder", "geometry-how-to-find-the-volume-of-a-cylinder",
   "geometry-how-to-find-the-surface-area-of-a-cylinder", "geometry-3-dimensional",
   "advanced-operations-exponent-also-power", "advanced-operations-how-to-evaluate-an-exponential-expression",
   "advanced-operations-scientific-notation",
   "advanced-operations-how-to-write-a-number-in-scientific-notation-given-its-standard-notation",
   "fractions-how-to-multiply-two-fractions"],
 "why_it_engages": "\"Keep this dangerous for 24,000 years\" is a design brief no other field ever writes down.",
 "decision_archetypes": [
   "Store spent fuel in dry casks on site for 60 years or ship it 1,800 miles to a repository now.",
   "Extend the licence of a 45-year-old reactor or replace it with gas plus renewables.",
   "Use thicker steel or a wider standoff distance to hit the same dose limit at the fence line."],
 "data_availability": {"grade": "MEDIUM", "sources": [
   S("US NRC datasets", "https://www.nrc.gov/reading-rm/doc-collections/datasets/", "LIVE", "reactor status, licensing, inspection and event spreadsheets"),
   S("IAEA Reference Data Series No.2 (RDS-2)", "https://www-pub.iaea.org/MTCD/Publications/PDF/RDS-2-45_web.pdf", "LIVE", "free PDF: every power reactor in the world with capacity and load factor"),
   S("EIA Open Data", "https://www.eia.gov/opendata/", "LIVE", "US nuclear generation and capacity factors by plant")],
  "note": "IAEA's interactive PRIS portal now redirects to a JavaScript app that needs registration for detail; the RDS-2 PDF carries the same headline data and is free. Cask internal geometry and shielding specs are vendor-controlled — use the published NRC certificate of compliance for a named cask design, or state the geometry as a scenario assumption."},
 "existing_cases": ["Nuclear Waste"],
 "careers": [
  {"title": "Health Physicist", "math_used": "Applies the inverse-square law and exponential attenuation (I = I0 e^-mu x) to compute the shielding thickness that brings dose under a limit.", "entry_path": "BS physics or health physics; ABHP certification for senior roles."},
  {"title": "Nuclear Fuel Cycle Analyst", "math_used": "Runs decay chains through N(t) = N0(1/2)^(t/T) across mixed isotopes to size the heat load a cask must reject.", "entry_path": "Nuclear engineering degree; national labs and utilities."},
  {"title": "Radiation Protection Technician", "math_used": "Converts counts-per-minute to dose rate using an instrument efficiency factor, then integrates over stay time to a total-dose budget.", "entry_path": "Two-year technical programme plus site-specific qualification."}],
 "authoring_priority": "LOW"
},
{
 "id": "mining-minerals",
 "name": "Mining & Mineral Extraction",
 "cluster": "Food, Energy & Resources",
 "one_line": "Grade, tonnage and the stripping ratio decide whether a mountain is worth money or not.",
 "math_branches": ["pre-algebra", "geometry", "algebra-1", "precalc"],
 "signature_skills": [
   "geometry-how-to-find-the-volume-of-a-prism", "geometry-how-to-find-the-volume-of-a-cone",
   "geometry-volume", "geometry-3-dimensional", "geometry-cone", "geometry-angle", "geometry-degree",
   "measurement-ratio", "measurement-how-to-convert-an-amount-with-compound-units",
   "number-sense-place-value", "number-sense-digit", "number-sense-numbers-and-counting-digit",
   "advanced-numbers-how-to-find-the-percent-of-a-number"],
 "why_it_engages": "Every phone in the room contains about 30 elements, and someone had to move a hundred tonnes of rock for each one.",
 "decision_archetypes": [
   "Open-pit the deposit at a 6:1 stripping ratio or drive an underground decline to the high-grade core.",
   "Mine the 0.4% copper body near the rail line or the 1.1% body 200 km from anywhere.",
   "Reprocess the old tailings dam or open new ground."],
 "data_availability": {"grade": "MEDIUM", "sources": [
   S("USGS Mineral Commodity Summaries", "https://www.usgs.gov/centers/national-minerals-information-center/mineral-commodity-summaries", "LIVE", "annual production, price, reserves and import reliance for ~90 commodities"),
   S("USGS Mineral Resources Data System (MRDS)", "https://mrdata.usgs.gov/mrds/", "LIVE", "location, commodity and status for hundreds of thousands of US deposits"),
   S("UN Comtrade", "https://comtradeplus.un.org/", "LIVE", "who exports which ore to whom, by tonnage and value")],
  "note": "Commodity prices and national production are easy. A specific mine's ore grade and cost-per-tonne sit in NI 43-101 or JORC technical reports filed by listed companies — those are free PDFs on SEDAR+/company sites but must be found per company, not queried. Grade MEDIUM for that reason. mrdata.usgs.gov's root page returns empty to scripted fetch; the /mrds/ path serves fine."},
 "existing_cases": [],
 "careers": [
  {"title": "Mining Engineer", "math_used": "Computes pit volume as a truncated cone at the maximum stable slope angle, derives the stripping ratio, and back-solves the cut-off grade at which the next bench pays for itself.", "entry_path": "BS mining engineering plus a PE; on-site graduate programmes."},
  {"title": "Resource Geologist", "math_used": "Interpolates drill-hole assays across a block model by inverse-distance weighting to estimate contained metal with a stated confidence category.", "entry_path": "Geology degree; Competent Person status needs years of logged experience."},
  {"title": "Mine Ventilation Engineer", "math_used": "Balances airflow through a network using resistance in series and parallel — the same algebra as a resistor network.", "entry_path": "Mining engineering with a ventilation specialisation."}],
 "authoring_priority": "MEDIUM"
},
# ===================== MOVEMENT & LOGISTICS ===============================
{
 "id": "aviation",
 "name": "Aviation & Air Traffic",
 "cluster": "Movement & Logistics",
 "one_line": "Headings, fuel and separation minima — three constraints that all bite at once.",
 "math_branches": ["geometry", "algebra-1", "precalc", "prob-stats"],
 "signature_skills": [
   "geometry-angle", "geometry-degree", "geometry-right-triangle", "geometry-hypotenuse",
   "geometry-pythagorean-theorem", "geometry-how-to-find-the-distance-between-two-coordinate-pairs-on-a-coordinate-plane",
   "measurement-how-to-convert-an-amount-with-compound-units",
   "measurement-how-to-find-elapsed-time", "measurement-distance",
   "statistics-and-probability-how-to-create-a-histogram-given-a-set-of-data",
   "pre-calculus-vector", "pre-calculus-magnitude-of-a-vector",
   "pre-calculus-how-to-add-and-subtract-vectors"],
 "why_it_engages": "There are about 10,000 aircraft in the sky right now and you can watch every one of them on a free map.",
 "decision_archetypes": [
   "Take the shorter route into a 90-knot headwind or the longer one with a tailwind, on the same fuel load.",
   "Hold the inbound aircraft or divert it, given fuel remaining and forecast ceiling.",
   "Add a fifth gate or retime the bank of departures to cut turnaround conflicts."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("BTS On-Time Performance", "https://www.transtats.bts.gov/ontime/", "LIVE", "every US scheduled flight: times, delays, cancellations, by cause"),
   S("OpenSky Network", "https://opensky-network.org/", "LIVE", "historical and live ADS-B position tracks, free for research/education"),
   S("Aviation Weather Center", "https://aviationweather.gov/", "LIVE", "METARs, TAFs and winds-aloft forecasts, the actual planning inputs"),
   S("FAA Air Traffic By The Numbers", "https://www.faa.gov/air_traffic/by_the_numbers", "LIVE", "national operations counts and airport rankings")],
  "note": "Flight, weather and delay data are excellent. Airline fuel burn per tail number and real ticket revenue are commercial; use published aircraft-type fuel-flow figures from the manufacturer or ICAO's engine emissions databank instead."},
 "existing_cases": ["Air Traffic Controller", "Airplane Manufacturer"],
 "careers": [
  {"title": "Air Traffic Controller", "math_used": "Holds 3 nm lateral or 1,000 ft vertical separation by projecting closure rate from two groundspeeds and headings — a relative-velocity vector problem done in the head.", "entry_path": "FAA Academy after an AT-CTI programme or military experience; hiring closes at age 31."},
  {"title": "Airline Dispatcher", "math_used": "Builds a fuel plan by summing trip, contingency, alternate and reserve burn against forecast winds aloft, then re-solves when the wind changes.", "entry_path": "FAA Aircraft Dispatcher certificate; a ~5-week course, no degree required."},
  {"title": "Flight Test Engineer", "math_used": "Resolves airspeed, wind and ground track into a wind triangle to back out true airspeed, and fits climb-rate curves against density altitude.", "entry_path": "Aerospace engineering degree plus a test-pilot-school or OEM programme."}],
 "authoring_priority": "HIGH"
},
{
 "id": "maritime-shipping",
 "name": "Shipping, Ports & Global Trade",
 "cluster": "Movement & Logistics",
 "one_line": "Great-circle routes, container slots and a canal toll that changes the whole answer.",
 "math_branches": ["geometry", "algebra-1", "precalc", "discrete"],
 "signature_skills": [
   "geometry-how-to-find-the-distance-between-two-coordinate-pairs-on-a-coordinate-plane",
   "geometry-coordinate-plane", "geometry-how-to-graph-a-coordinate-pair-on-the-coordinate-plane",
   "geometry-prism", "geometry-how-to-find-the-volume-of-a-prism",
   "measurement-how-to-convert-an-amount-with-compound-units",
   "measurement-currency", "measurement-how-to-find-elapsed-time",
   "number-sense-depth",
   "discrete-mathematics-graph-vertices-and-edges", "discrete-mathematics-weighted-graph",
   "discrete-mathematics-how-to-find-the-shortest-path-between-two-vertices-in-a-weighted-graph"],
 "why_it_engages": "About 90% of everything they own arrived in a steel box, and almost none of them have ever thought about how it was packed.",
 "decision_archetypes": [
   "Route Asia–Europe via Suez with the toll and the risk surcharge, or around the Cape at 11 extra days.",
   "Slow-steam at 16 knots to cut fuel or hold 21 knots to keep the berth window.",
   "Load 40-ft high-cubes to volume or 20-ft boxes to weight, given the ship's deadweight and TEU limits."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("UN Comtrade", "https://comtradeplus.un.org/", "LIVE", "bilateral trade flows by commodity, tonnage and value"),
   S("UNCTADstat", "https://unctadstat.unctad.org/", "LIVE", "fleet, port throughput and liner connectivity indices"),
   S("Port of Los Angeles container statistics", "https://www.portoflosangeles.org/business/statistics/container-statistics", "LIVE", "monthly loaded/empty TEU by direction, back to 1995"),
   S("NOAA nautical charts", "https://nauticalcharts.noaa.gov/", "LIVE", "free ENCs with channel depths for the approach problem")],
  "note": "Trade volumes and port throughput are public and clean. Live per-voyage AIS tracks and actual charter rates are commercial (Clarksons, Lloyd's List); build the case on published port stats plus a stated vessel spec rather than a real voyage."},
 "existing_cases": ["Navigation"],
 "careers": [
  {"title": "Ship's Navigator (Deck Officer)", "math_used": "Solves great-circle distance and initial course from two lat/long pairs with spherical trigonometry, then corrects the compass for variation and deviation.", "entry_path": "Maritime academy plus a Third Mate unlimited licence."},
  {"title": "Port Terminal Planner", "math_used": "Assigns containers to yard slots to minimise re-handles — a stacking problem — and computes crane moves per hour against a berth window.", "entry_path": "Logistics or industrial engineering degree; terminal operator graduate schemes."},
  {"title": "Marine Surveyor / Loadmaster", "math_used": "Computes the centre of gravity of a loaded ship as a weighted average of cargo moments and checks the metacentric height stays above the stability minimum.", "entry_path": "Sea time plus naval architecture study; IIMS/SAMS accreditation."}],
 "authoring_priority": "HIGH"
},
{
 "id": "transit-routing",
 "name": "Transit, Routing & Last-Mile Logistics",
 "cluster": "Movement & Logistics",
 "one_line": "Shortest path, tightest schedule, fewest vehicles — pick two.",
 "math_branches": ["pre-algebra", "number-theory", "algebra-1", "geometry", "discrete", "linear-algebra"],
 "signature_skills": [
   "basic-operations-factor", "basic-operations-how-to-factor-a-number",
   "measurement-how-to-add-and-subtract-time", "measurement-how-to-find-elapsed-time",
   "measurement-how-to-find-the-start-or-end-time-given-the-start-or-end-and-the-elapsed-time",
   "measurement-how-to-convert-between-units-of-time",
   "measurement-how-to-convert-an-amount-with-compound-units",
   "geometry-how-to-find-the-distance-between-two-coordinate-pairs-on-a-coordinate-plane",
   "number-sense-how-to-compare-two-or-more-values",
   "advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-both-sides"],
 "why_it_engages": "Everyone in the room has an opinion about their bus, and the timetable is a solvable maths object they have never been shown.",
 "decision_archetypes": [
   "Run the bus every 10 minutes on one corridor or every 25 minutes on three.",
   "Add a fourth delivery van or extend the shift of the three you have.",
   "Reroute around the closure with 6 extra minutes for everyone, or split the line and force a transfer."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("Transitland", "https://www.transit.land/", "LIVE", "GTFS feeds for thousands of agencies — real stops, times, shapes"),
   S("GTFS specification", "https://gtfs.org/", "LIVE", "the schema; makes a raw feed readable by a student"),
   S("OpenStreetMap", "https://www.openstreetmap.org/", "LIVE", "the road graph, free, with speed limits and turn restrictions"),
   S("NYC Open Data", "https://data.cityofnewyork.us/browse", "LIVE", "taxi trip records, bus speeds, subway ridership")],
  "note": "GTFS is the gift here: a zip of CSVs holding an entire agency's schedule that a student can open in a spreadsheet. Real-time vehicle positions (GTFS-RT) need per-agency keys and are protobuf — too far for a middle-school case."},
 "existing_cases": ["Travel Planner", "Family Trip", "Foreign Travel"],
 "careers": [
  {"title": "Transit Service Planner", "math_used": "Sets headway from the fleet-size identity (buses = cycle time / headway) and tests whether a 3-minute running-time cut buys back a whole vehicle.", "entry_path": "Urban planning or civil engineering degree; agency planning departments."},
  {"title": "Route Optimisation Engineer", "math_used": "Solves capacitated vehicle-routing with time windows — building a distance matrix, then improving tours with 2-opt swaps.", "entry_path": "CS or operations research degree; UPS/Amazon/Route4Me-type roles."},
  {"title": "Traffic Engineer", "math_used": "Times a signal by allocating green per approach in proportion to critical lane volume, then checks the cycle against Webster's delay formula.", "entry_path": "BS civil engineering, PE, plus PTOE certification."}],
 "authoring_priority": "HIGH"
},
# ===================== BUILT ENVIRONMENT ==================================
{
 "id": "surveying-geodesy",
 "name": "Surveying, Mapping & GPS",
 "cluster": "Built Environment",
 "one_line": "You cannot reach the far side of the canyon, so you measure an angle instead.",
 "math_branches": ["geometry", "algebra-1", "precalc", "linear-algebra"],
 "signature_skills": [
   "geometry-angle", "geometry-degree", "geometry-right-triangle", "geometry-leg",
   "geometry-hypotenuse", "geometry-pythagorean-theorem", "geometry-similar",
   "geometry-scale-factor", "geometry-how-to-find-the-scale-factor-of-a-dilation",
   "geometry-how-to-find-angle-measures-of-intersecting-lines",
   "geometry-transversal-line", "geometry-vertical-angles",
   "geometry-how-to-find-angle-measures-given-parallel-lines-a-transversal-line-and-at-least-one-an",
   "geometry-acute-triangle", "geometry-obtuse-triangle", "geometry-scalene-triangle",
   "geometry-triangle-inequality-theorem",
   "geometry-how-to-find-the-distance-between-two-coordinate-pairs-on-a-coordinate-plane",
   "pre-calculus-vector", "pre-calculus-how-to-find-the-magnitude-and-direction-of-a-vector",
   "pre-calculus-matrix"],
 "why_it_engages": "Trigonometry stops being abstract the moment you use it to measure a building you are standing next to.",
 "decision_archetypes": [
   "Run the boundary survey by total station at $X per day or by drone photogrammetry at a coarser tolerance.",
   "Route the pipeline over the ridge with a 9% grade or around it with 4 extra kilometres.",
   "Accept the GPS fix with a 2.4 m error circle or occupy the point for another 40 minutes."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("NOAA NGS datasheets", "https://geodesy.noaa.gov/datasheets/", "LIVE", "published coordinates and elevations for real survey monuments"),
   S("USGS National Map Downloader", "https://apps.nationalmap.gov/downloader/", "LIVE", "3DEP elevation, contours, hydrography, free"),
   S("NGS Coordinate Conversion (NCAT)", "https://geodesy.noaa.gov/NCAT/", "LIVE", "converts between lat/long, State Plane and UTM — the actual working tool"),
   S("Census TIGER/Line shapefiles", "https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html", "LIVE", "boundaries and road centrelines")],
  "note": "Monument datasheets are the strongest teaching asset here: a student can pick two real benchmarks, get exact coordinates, and check their own trigonometry against the published distance. Raw total-station field books are not published anywhere; a case needing them must supply invented-but-declared field notes."},
 "existing_cases": ["Navigation"],
 "careers": [
  {"title": "Land Surveyor", "math_used": "Closes a traverse by summing latitude and departure components (d·cos B, d·sin B) around a loop and distributing the closure error proportionally.", "entry_path": "Surveying degree plus FS then PS licensure; apprenticeship route exists in many states."},
  {"title": "Geodesist", "math_used": "Transforms coordinates between datums with a seven-parameter Helmert transformation — three translations, three rotations, one scale.", "entry_path": "Geomatics/geodesy MS; NGS, national mapping agencies."},
  {"title": "Construction Layout Technician", "math_used": "Sets out a curve by deflection angles and chord lengths from the tangent point, checking each stake against the computed radius.", "entry_path": "Two-year survey technology programme plus field time."}],
 "authoring_priority": "HIGH"
},
{
 "id": "construction-architecture",
 "name": "Construction & Architecture",
 "cluster": "Built Environment",
 "one_line": "A floor plan is a constrained area problem where every wall costs money and every angle has to close.",
 "math_branches": ["pre-algebra", "geometry", "algebra-1", "precalc"],
 "signature_skills": [
   "geometry-quadrilateral", "geometry-parallelogram", "geometry-trapezoid",
   "geometry-how-to-find-the-area-of-a-rectangle", "geometry-how-to-find-the-area-of-a-triangle",
   "geometry-how-to-find-the-measure-of-the-perimeter-of-a-polygon",
   "geometry-right-angle", "geometry-perpendicular-lines", "geometry-parallel-lines",
   "geometry-supplementary-angles", "geometry-complementary-angles", "geometry-adjacent-angles",
   "geometry-acute-angle", "geometry-obtuse-angle", "geometry-ray",
   "geometry-rhombus", "geometry-kite",
   "geometry-how-to-find-the-surface-area-of-a-prism", "geometry-scale-factor",
   "geometry-pyramid", "geometry-face", "geometry-edge", "geometry-how-to-name-a-3-d-shape",
   "geometry-how-to-find-the-volume-of-a-pyramid", "geometry-how-to-find-the-surface-area-of-a-pyramid",
   "fractions-how-to-add-with-mixed-numbers", "fractions-how-to-subtract-with-mixed-numbers",
   "fractions-how-to-subtract-fractions", "fractions-how-to-multiply-two-mixed-numbers",
   "fractions-how-to-divide-a-fraction-by-a-whole-number", "fractions-how-to-divide-fractions-and-mixed-numbers"],
 "why_it_engages": "Everyone has stood in a room that felt wrong, and a floor plan lets you prove why in numbers.",
 "decision_archetypes": [
   "Build the 1,900 sq ft two-storey or the 1,900 sq ft single-storey on the same lot, given foundation and roof cost per square foot.",
   "Frame at 16-inch or 24-inch centres given the lumber price and the span table.",
   "Add the dormer for 90 sq ft of usable floor or take the money as a bigger kitchen."],
 "data_availability": {"grade": "MEDIUM", "sources": [
   S("Census Building Permits Survey", "https://www.census.gov/construction/bps/", "LIVE", "permits, units and valuation by county and month"),
   S("NYC Open Data", "https://data.cityofnewyork.us/browse", "LIVE", "individual building permits with declared job cost and floor area"),
   S("ASCE 7 Hazard Tool", "https://ascehazardtool.org/", "LIVE", "site-specific wind, snow and seismic design loads by address, free"),
   S("Sheet Metal gauge chart", "https://sheetmetal.me/sheet-metal-gauge-chart/", "LIVE", "standard gauge-to-thickness tables for flashing and stud work")],
  "note": "Permits, valuations and design loads are free. Unit-cost data (RSMeans) is a paid subscription — the honest substitute is a live materials price list from a named retailer, captured with a date, or the declared job cost on real permits. Graded MEDIUM for that reason."},
 "existing_cases": ["House Plans", "Carpenter", "Castle Securtiy", "Bathroom Problems"],
 "careers": [
  {"title": "Architect", "math_used": "Works a scale factor between drawing and building in both directions, computes floor-area ratio against the zoning cap, and sets stair rise/run to hit code with a whole number of risers.", "entry_path": "Professional B.Arch or M.Arch, AXP hours, then the ARE exams."},
  {"title": "Quantity Surveyor / Estimator", "math_used": "Takes off areas and volumes from drawings, applies waste factors, and reconciles two bids that use different measurement conventions.", "entry_path": "Construction management degree; RICS route in the UK/Commonwealth."},
  {"title": "Structural Engineer", "math_used": "Sums moments about a support to size a beam, then checks deflection against span/360.", "entry_path": "BS/MS civil engineering plus PE and often SE licensure."}],
 "authoring_priority": "MEDIUM"
},
{
 "id": "urban-planning",
 "name": "Urban Planning & Zoning",
 "cluster": "Built Environment",
 "one_line": "Density, access and the fact that every parcel belongs to somebody who will show up to the meeting.",
 "math_branches": ["pre-algebra", "geometry", "algebra-1", "prob-stats", "discrete"],
 "signature_skills": [
   "geometry-area", "geometry-polygon", "geometry-irregular-polygon", "geometry-convex", "geometry-concave",
   "geometry-how-to-find-the-area-of-a-regular-polygon",
   "geometry-how-to-find-the-area-of-a-circle",
   "measurement-ratio", "measurement-proportion",
   "statistics-and-probability-population", "number-sense-data"],
 "why_it_engages": "The 15-minute-city argument is happening in their town right now and it is settled by measuring circles on a map.",
 "decision_archetypes": [
   "Upzone the transit corridor for 900 apartments or spread 900 across four low-rise neighbourhoods.",
   "Convert two traffic lanes to a protected bike lane or keep the lanes and widen the pavement.",
   "Site one large park or four pocket parks, measured by how many residents fall inside a 400 m walk."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("Census TIGER/Line shapefiles", "https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html", "LIVE", "tract, block-group and parcel-adjacent geometry"),
   S("data.gov", "https://data.gov/", "LIVE", "363k+ datasets; municipal zoning, parcels, land use"),
   S("NYC Open Data", "https://data.cityofnewyork.us/browse", "LIVE", "PLUTO parcel file — lot area, floor area, use, per parcel"),
   S("OpenStreetMap", "https://www.openstreetmap.org/", "LIVE", "amenities, footways and building footprints for walkshed analysis")],
  "note": "Geometry and demographics are abundant. Small towns often publish nothing; if a case is set in a specific small municipality, expect to substitute a comparable city or state it as a constructed scenario."},
 "existing_cases": ["Urban Planner"],
 "careers": [
  {"title": "Urban Planner", "math_used": "Computes floor-area ratio, units-per-acre and walkshed coverage, then projects population from a build-out schedule against school and sewer capacity.", "entry_path": "Master of Urban Planning; AICP certification after two years."},
  {"title": "Transportation Demand Modeller", "math_used": "Runs a gravity model — trips between two zones falling off with distance — to distribute forecast trips across a network.", "entry_path": "Civil engineering or planning MS; MPOs and consultancies."},
  {"title": "Housing Policy Analyst", "math_used": "Builds rent-burden distributions (share of income above 30%) and tests how a subsidy shifts the whole distribution, not the mean.", "entry_path": "Public policy or economics degree; city agencies, think tanks."}],
 "authoring_priority": "MEDIUM"
},
# ===================== MAKING & MATERIALS =================================
{
 "id": "manufacturing-nesting",
 "name": "Manufacturing, Cutting & Material Nesting",
 "cluster": "Making & Materials",
 "one_line": "Fit the parts onto the sheet with the least scrap — rotate, flip and slide until it pays.",
 "math_branches": ["pre-algebra", "geometry", "algebra-1", "discrete"],
 "signature_skills": [
   "geometry-transformation", "geometry-translation", "geometry-rotation",
   "geometry-reflection", "geometry-clockwise", "geometry-counter-clockwise",
   "geometry-how-to-translate-a-figure-on-the-coordinate-plane",
   "geometry-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-clockwise",
   "geometry-how-to-rotate-a-figure-on-the-coordinate-plane-180-degrees",
   "geometry-how-to-reflect-a-figure-across-the-y-axis",
   "geometry-congruent", "geometry-fundamentals-of-geometry-congruent", "geometry-area",
   "geometry-how-to-find-the-area-of-a-rectangle",
   "geometry-net", "geometry-how-to-draw-the-net-of-a-3-d-shape"],
 "why_it_engages": "It is a puzzle with money attached: every square inch of scrap is cash in the bin, and rotating one part 90 degrees can save it.",
 "decision_archetypes": [
   "Nest the 14 brackets at 0 degrees for a fast cut path, or rotate half of them 90 degrees to fit on one fewer sheet.",
   "Buy 4x8 sheets or 5x10 sheets, given the part mix and a 3 mm kerf.",
   "Run the job on the laser with tight nesting and slow cut time, or the punch press with wider spacing and half the cycle time."],
 "data_availability": {"grade": "MEDIUM", "sources": [
   S("Sheet Metal gauge & size chart", "https://sheetmetal.me/sheet-metal-gauge-chart/", "LIVE", "gauge-to-thickness and standard sheet sizes for steel and aluminium"),
   S("McMaster-Carr", "https://www.mcmaster.com/", "LIVE", "real, dated prices and dimensions for stock sheet, bar and fasteners"),
   S("ESICUP cutting & packing data sets", "https://www.euro-online.org/websites/esicup/data-sets/", "LIVE", "the academic benchmark instances for nesting problems"),
   S("OR-Library bin packing data", "https://people.brunel.ac.uk/~mastjjb/jeb/orlib/binpackinfo.html", "LIVE", "classic packing instances with known optima")],
  "note": "This is the honest MEDIUM. Part geometry has to be authored by the case writer (draw the brackets on a grid) — there is no public library of 'real factory parts'. What IS real and citable: sheet stock sizes, material prices with a capture date, and the benchmark instances. Say so in the case."},
 "existing_cases": ["Airplane Manufacturer"],
 "careers": [
  {"title": "CNC Programmer / Nesting Engineer", "math_used": "Places congruent part outlines on a sheet using translation and 90/180-degree rotation about the origin, tracking utilisation = summed part area / sheet area, and adds kerf offset to every edge.", "entry_path": "Two-year machining or manufacturing technology programme; NIMS credentials."},
  {"title": "Industrial Engineer", "math_used": "Balances a line by assigning tasks to stations so no station exceeds takt time, then computes yield loss through a multi-step process as a product of stage yields.", "entry_path": "BS industrial engineering; Six Sigma belts on top."},
  {"title": "Sheet Metal Fabricator", "math_used": "Develops a flat pattern from a 3-D part by unfolding its net and subtracting bend allowance computed from the K-factor and bend radius.", "entry_path": "Apprenticeship (SMART union) or trade school."}],
 "authoring_priority": "HIGH"
},
{
 "id": "textiles-pattern",
 "name": "Textiles, Pattern & Garment Design",
 "cluster": "Making & Materials",
 "one_line": "A garment is a set of flat shapes that must tile a bolt of cloth and then wrap a moving body.",
 "math_branches": ["pre-algebra", "geometry", "algebra-1"],
 "signature_skills": [
   "geometry-reflection", "geometry-line-of-symmetry", "geometry-symmetry",
   "geometry-how-to-reflect-a-figure-across-the-y-axis",
   "geometry-how-to-reflect-a-figure-across-the-x-axis",
   "geometry-dilation", "geometry-scale-factor",
   "geometry-how-to-dilate-a-figure-on-the-coordinate-plane-given-a-scale-factor",
   "geometry-how-to-find-the-scale-factor-of-a-dilation",
   "geometry-similar", "geometry-translation",
   "fractions-how-to-add-with-mixed-numbers", "fractions-how-to-multiply-a-fraction-and-a-mixed-number",
   "measurement-how-to-convert-an-amount-from-one-unit-to-another-unit"],
 "why_it_engages": "Grading a pattern from size 8 to size 16 is a dilation — and it is why cheap clothes fit badly, which they already know.",
 "decision_archetypes": [
   "Grade the pattern by uniform dilation (cheap, fits badly at the extremes) or by graded increments per measurement point (costly, fits).",
   "Cut on the fold to halve marking time, or cut open to nest the pieces tighter on a 44-inch bolt.",
   "Print the fabric with a repeat that matches at the seam, or accept a mismatch and save 0.6 m per garment."],
 "data_availability": {"grade": "MEDIUM", "sources": [
   S("FreeSewing", "https://freesewing.eu/designs/", "LIVE", "open-source parametric sewing patterns — enter measurements, get the maths"),
   S("The Met Collection (Open Access)", "https://www.metmuseum.org/art/collection", "LIVE", "high-res costume and textile images with dimensions"),
   S("Rijksstudio", "https://www.rijksmuseum.nl/en/rijksstudio", "LIVE", "public-domain textile and pattern images at high resolution"),
   S("Sheet Metal gauge chart (for the nesting analogue)", "https://sheetmetal.me/sheet-metal-gauge-chart/", "LIVE", "used only as the parallel case for standard stock widths")],
  "note": "FreeSewing is the find here — it is literally parametric geometry with the formulas exposed, and the site moved from .org to .eu, so cite freesewing.eu. Standard bolt widths (44/45in and 58/60in) are near-universal trade convention but are not published by a standards body; state them as trade convention with a retailer citation, not as a standard. Body-measurement size charts differ per brand — use one named brand's published chart."},
 "existing_cases": [],
 "careers": [
  {"title": "Pattern Grader", "math_used": "Applies non-uniform dilation: each pattern point moves by a grade rule vector, so the bust grows 1 inch while the shoulder grows 3/8 — a per-point scale factor, not one global one.", "entry_path": "Fashion/apparel technology diploma; industry apprenticeship."},
  {"title": "Textile Print Designer", "math_used": "Builds a repeat tile that tessellates the plane by translation (or half-drop translation), checking that every edge matches its opposite exactly.", "entry_path": "Textile design degree; studio or freelance."},
  {"title": "Apparel Production Manager", "math_used": "Computes marker efficiency (pattern area / marker area) and yield in metres per garment, then multiplies across an order to price the fabric buy.", "entry_path": "Apparel merchandising or industrial engineering degree."}],
 "authoring_priority": "HIGH"
},
{
 "id": "robotics-automation",
 "name": "Robotics & Automation",
 "cluster": "Making & Materials",
 "one_line": "Where the gripper ends up is a chain of rotations, and the arm has to get there without hitting anything.",
 "math_branches": ["geometry", "algebra-2", "precalc", "linear-algebra", "discrete"],
 "signature_skills": [
   "geometry-rotation", "geometry-clockwise", "geometry-counter-clockwise",
   "geometry-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-clockwise",
   "geometry-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-counterclockwise",
   "geometry-coordinate-plane", "geometry-coordinate-pair-also-ordered-pair",
   "geometry-angle", "geometry-degree", "geometry-hypotenuse", "geometry-pythagorean-theorem",
   "measurement-how-to-convert-an-amount-with-compound-units"],
 "why_it_engages": "Inverse kinematics is the moment maths visibly becomes control of a physical object.",
 "decision_archetypes": [
   "Use a 6-axis arm that reaches everything slowly, or two 4-axis arms that are faster but need a handoff.",
   "Position the part feeder inside the fast inner workspace or outside it where the operator can reach.",
   "Run the cell at 80% speed with no safety fence, or full speed behind a fence that costs floor area."],
 "data_availability": {"grade": "MEDIUM", "sources": [
   S("Universal Robots UR5e datasheet", "https://www.universal-robots.com/media/1807465/ur5e_e-series_datasheets_web.pdf", "LIVE", "reach, payload, joint ranges, repeatability, cycle time — free PDF"),
   S("Stanford 3D Scanning Repository", "http://graphics.stanford.edu/data/3Dscanrep/", "LIVE", "real 3-D part meshes to reason about grasping and volume"),
   S("GeoGebra", "https://www.geogebra.org/", "LIVE", "free tool to build and check a two-link arm's reach envelope")],
  "note": "Manufacturer datasheets are the reliable free asset — every major arm vendor publishes reach envelopes and payload curves as PDFs. Global robot-density and installation statistics come from the IFR World Robotics report, which is paid; do not cite a number from it that you have not seen. Graded MEDIUM."},
 "existing_cases": ["Robotics Engineer"],
 "careers": [
  {"title": "Robotics Engineer", "math_used": "Solves two-link inverse kinematics with the law of cosines to get joint angles from a target (x, y), then checks the elbow-up and elbow-down solutions against joint limits.", "entry_path": "BS mechanical/electrical engineering or mechatronics; ROS skills matter as much as the degree."},
  {"title": "Automation Controls Technician", "math_used": "Converts encoder counts to millimetres through a gear ratio and lead screw pitch, and tunes a PID loop by watching overshoot and settling time.", "entry_path": "Two-year mechatronics programme plus PLC certification."},
  {"title": "Warehouse Robotics Operations Analyst", "math_used": "Models the floor as a grid graph and computes throughput as robots multiplied by trips per hour, with collision-avoidance waits as a queueing penalty.", "entry_path": "Industrial engineering or CS degree; Amazon/Ocado-type operators."}],
 "authoring_priority": "MEDIUM"
},
# ===================== SPACE & SKY ========================================
{
 "id": "spaceflight",
 "name": "Spaceflight & Orbital Mechanics",
 "cluster": "Space & Sky",
 "one_line": "Every kilogram to orbit is paid for in fuel, and the launch window is 41 seconds wide.",
 "math_branches": ["geometry", "algebra-2", "precalc", "calculus", "linear-algebra"],
 "signature_skills": [
   "advanced-operations-scientific-notation",
   "advanced-operations-how-to-write-a-number-in-scientific-notation-given-its-standard-notation",
   "advanced-operations-how-to-write-a-number-in-standard-notation-given-its-scientific-notation",
   "advanced-operations-exponent-also-power",
   "geometry-circumference", "geometry-how-to-find-the-measure-of-the-circumference-of-a-circle",
   "geometry-radius", "geometry-pi",
   "measurement-how-to-convert-an-amount-with-compound-units",
   "measurement-how-to-find-elapsed-time",
   "calculus-derivative", "calculus-instantaneous-rate-of-change", "pre-calculus-vector"],
 "why_it_engages": "Orbital velocity is about 7.8 km/s and nothing in a teenager's intuition prepares them for what that number means.",
 "decision_archetypes": [
   "Launch a 60-satellite constellation on one big rocket to one plane, or six small rockets to six planes.",
   "Carry extra fuel for a plane change or accept a longer, cheaper transfer with a worse revisit time.",
   "De-orbit the ageing satellite now or keep it flying through a debris-conjunction season."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("CelesTrak", "https://celestrak.org/", "LIVE", "current TLEs for every tracked object; period and altitude fall straight out"),
   S("JPL Horizons", "https://ssd.jpl.nasa.gov/horizons/", "LIVE", "precise ephemerides for planets, moons and spacecraft"),
   S("NASA Open Data Portal", "https://data.nasa.gov/", "LIVE", "mission datasets and catalogues"),
   S("GCAT — General Catalog of Artificial Space Objects", "https://planet4589.org/space/gcat/", "LIVE", "every launch ever, with mass, orbit and outcome")],
  "note": "Orbital elements and launch history are exceptionally good and free. Per-launch *price* is negotiated and mostly unpublished — use the vendor's public list price with a capture date and say it is a list price."},
 "existing_cases": [],
 "careers": [
  {"title": "Mission Design Engineer", "math_used": "Sizes a Hohmann transfer from two orbital radii, sums the two delta-v burns, and converts that to propellant mass with the Tsiolkovsky rocket equation (an exponential in delta-v).", "entry_path": "Aerospace engineering MS; NASA centres, JPL, launch providers."},
  {"title": "Satellite Operations Engineer", "math_used": "Propagates a TLE to predict the next pass, computes elevation angle over the ground station, and works out the contact window in minutes.", "entry_path": "Engineering or physics degree plus operator training; many entry roles at operators."},
  {"title": "Launch Range Safety Analyst", "math_used": "Builds debris-footprint ellipses from dispersion statistics and integrates population density inside them to hold expected casualties below a fixed threshold.", "entry_path": "Aerospace or statistics degree; Space Force ranges and FAA AST."}],
 "authoring_priority": "HIGH"
},
{
 "id": "astronomy",
 "name": "Observational Astronomy",
 "cluster": "Space & Sky",
 "one_line": "Everything you know about a star came from an angle, a brightness and a shift in colour.",
 "math_branches": ["geometry", "algebra-2", "precalc", "prob-stats"],
 "signature_skills": [
   "geometry-angle", "geometry-degree", "geometry-similar",
   "geometry-sphere", "geometry-how-to-find-the-volume-of-a-sphere",
   "advanced-operations-scientific-notation",
   "advanced-operations-how-to-write-a-number-in-scientific-notation-given-its-standard-notation",
   "measurement-how-to-convert-an-amount-from-one-unit-to-another-unit",
   "statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data",
   "statistics-and-probability-outlier",
   "number-sense-how-to-compare-two-or-more-values",
   "pre-calculus-radian", "pre-calculus-reference-angle"],
 "why_it_engages": "Parallax means you can measure the distance to a star by holding your thumb up and thinking carefully — the whole ladder starts there.",
 "decision_archetypes": [
   "Point the 4-hour telescope slot at the one candidate exoplanet transit or at 12 shallow survey fields.",
   "Site the observatory at high altitude with bad weather or moderate altitude with clear skies, given usable nights per year.",
   "Follow up the marginal 3-sigma detection or spend the time on a fresh target."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("NASA Exoplanet Archive", "https://exoplanetarchive.ipac.caltech.edu/", "LIVE", "every confirmed planet with period, radius, and the light curves"),
   S("SIMBAD", "https://simbad.u-strasbg.fr/simbad/", "LIVE", "positions, magnitudes, parallaxes and spectral types for millions of objects"),
   S("AAVSO", "https://www.aavso.org/", "LIVE", "variable-star brightness time series contributed by amateurs"),
   S("Stellarium Web", "https://stellarium-web.org/", "LIVE", "free planetarium for altitude/azimuth and visibility windows")],
  "note": "Astronomy is arguably the single most open science on the internet — nearly everything is free, cited and machine-readable. The limit is student handling: FITS files and VOTables need tooling, so prefer the archive's CSV export view."},
 "existing_cases": [],
 "careers": [
  {"title": "Observational Astronomer", "math_used": "Turns parallax in arcseconds into distance in parsecs (d = 1/p) and converts apparent to absolute magnitude with the distance modulus — a base-10 logarithm.", "entry_path": "PhD in astronomy or physics."},
  {"title": "Telescope Operations Scheduler", "math_used": "Maximises science-per-night as a constrained assignment problem over target airmass, moon distance and slew time.", "entry_path": "Physics/CS degree; observatory staff astronomer route."},
  {"title": "Planetarium Educator", "math_used": "Converts between altitude/azimuth and right ascension/declination with spherical trigonometry to place any object for any date, time and latitude.", "entry_path": "Science education or astronomy degree; museum and science-centre roles."}],
 "authoring_priority": "HIGH"
},
# ===================== DIGITAL SYSTEMS & INFORMATION ======================
{
 "id": "computer-graphics",
 "name": "Computer Graphics & Animation",
 "cluster": "Digital Systems & Information",
 "one_line": "Everything on the screen is a list of points being multiplied by a matrix, sixty times a second.",
 "math_branches": ["geometry", "algebra-2", "precalc", "linear-algebra"],
 "signature_skills": [
   "geometry-transformation", "geometry-translation", "geometry-rotation", "geometry-reflection",
   "geometry-dilation", "geometry-scale-factor",
   "geometry-how-to-translate-a-figure-on-the-coordinate-plane",
   "geometry-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-counterclockwise",
   "geometry-how-to-rotate-a-figure-on-the-coordinate-plane-180-degrees",
   "geometry-how-to-reflect-a-figure-across-the-x-axis",
   "geometry-how-to-dilate-a-figure-on-the-coordinate-plane-given-a-scale-factor",
   "geometry-coordinate-pair-also-ordered-pair", "geometry-how-to-graph-a-coordinate-pair-on-the-coordinate-plane",
   "geometry-similar", "geometry-fundamentals-of-geometry-congruent",
   "pre-calculus-matrix", "pre-calculus-matrix-dimension",
   "pre-calculus-how-to-add-and-multiply-matrices"],
 "why_it_engages": "They have spent thousands of hours inside rendered worlds and have never been told the worlds are matrices.",
 "decision_archetypes": [
   "Animate the character by hand-keying 24 poses or by rigging a skeleton and driving it with rotations.",
   "Ship the 40,000-triangle model at full fidelity or the 6,000-triangle version that renders at 60fps on a phone.",
   "Bake the lighting once or compute it per frame, given a fixed frame budget in milliseconds."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("Stanford 3D Scanning Repository", "http://graphics.stanford.edu/data/3Dscanrep/", "LIVE", "the Bunny, Dragon, Happy Buddha — real meshes with vertex counts"),
   S("Blender", "https://www.blender.org/", "LIVE", "free professional 3-D tool; students can verify a transform by doing it"),
   S("GeoGebra", "https://www.geogebra.org/", "LIVE", "free tool for showing a transform on the coordinate plane"),
   S("NASA Open Data Portal", "https://data.nasa.gov/", "LIVE", "free 3-D spacecraft models for a rendering case")],
  "note": "Tooling and reference meshes are abundant and free. Studio render-farm costs and per-frame timings are proprietary; a case needing them should use published cloud-render list prices with a capture date."},
 "existing_cases": [],
 "careers": [
  {"title": "Technical Artist / Rigger", "math_used": "Composes rotation, scale and translation matrices in the right order (order matters — RT is not TR) and works in the joint's local coordinate frame.", "entry_path": "Animation or CS degree; a demo reel outweighs the degree."},
  {"title": "Graphics Programmer", "math_used": "Builds the model-view-projection matrix chain and normalises surface vectors before a dot product to get a lighting term.", "entry_path": "CS degree with linear algebra and C++; games and engine teams."},
  {"title": "3-D Scanning / Photogrammetry Technician", "math_used": "Registers two point clouds by solving for the rigid transform (rotation plus translation) that minimises squared distance between matched points.", "entry_path": "Surveying, VFX or engineering background plus software training."}],
 "authoring_priority": "HIGH"
},
{
 "id": "remote-sensing",
 "name": "Satellite Imagery & Remote Sensing",
 "cluster": "Digital Systems & Information",
 "one_line": "Two pictures of the same place, taken 12 days apart, only tell you something once you line them up exactly.",
 "math_branches": ["geometry", "algebra-1", "linear-algebra", "prob-stats"],
 "signature_skills": [
   "geometry-transformation", "geometry-translation", "geometry-rotation", "geometry-dilation",
   "geometry-scale-factor", "geometry-how-to-find-the-scale-factor-of-a-dilation",
   "geometry-how-to-translate-a-figure-on-the-coordinate-plane",
   "geometry-how-to-dilate-a-figure-on-the-coordinate-plane-given-a-scale-factor",
   "geometry-coordinate-plane", "geometry-x-axis", "geometry-y-axis", "geometry-origin",
   "geometry-area", "measurement-how-to-convert-an-amount-from-one-unit-to-another-unit"],
 "why_it_engages": "You can personally download a satellite photo of your own street from last week, for free, and measure something on it.",
 "decision_archetypes": [
   "Buy 3 m commercial imagery weekly or use free 10 m Sentinel imagery every 5 days for the same deforestation alert.",
   "Register the two scenes by shifting whole pixels (fast, slightly wrong) or resampling sub-pixel (slow, correct).",
   "Declare the field burned from the index change, or wait one more revisit and risk the insurance deadline."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("USGS EarthExplorer", "https://earthexplorer.usgs.gov/", "LIVE", "full Landsat archive, free, with scene metadata"),
   S("NASA Worldview", "https://worldview.earthdata.nasa.gov/", "LIVE", "daily global imagery browser, no account, snapshot export"),
   S("Sentinel-2 on AWS Open Data", "https://registry.opendata.aws/sentinel-2-l2a-cogs/", "LIVE", "free Sentinel-2 cloud-optimised GeoTIFFs, no account"),
   S("Copernicus Browser", "https://browser.dataspace.copernicus.eu/", "LIVE_LOGIN", "Sentinel browser; viewing is free, download needs a free account")],
  "note": "Imagery itself is free and enormous. The catch for a classroom is file size and GeoTIFF handling — prefer Worldview's snapshot export or a pre-clipped scene supplied in the appendix. Sub-metre commercial imagery (Maxar, Planet) is paid except for disaster-activation releases."},
 "existing_cases": [],
 "careers": [
  {"title": "Remote Sensing Analyst", "math_used": "Computes NDVI = (NIR − Red)/(NIR + Red) per pixel, then differences two co-registered dates and thresholds the change.", "entry_path": "Geography/environmental science degree with GIS; ASPRS certification."},
  {"title": "Photogrammetrist", "math_used": "Solves the affine or projective transform that maps image pixel coordinates onto ground coordinates using control points — a least-squares system.", "entry_path": "Geomatics degree; ASPRS Certified Photogrammetrist."},
  {"title": "Agricultural Imagery Consultant", "math_used": "Scales a per-pixel index to per-acre yield using a regression calibrated on ground samples, and reports the residual spread honestly.", "entry_path": "Agronomy plus GIS; ag-tech firms and co-ops."}],
 "authoring_priority": "HIGH"
},
{
 "id": "cryptography-security",
 "name": "Cryptography & Cybersecurity",
 "cluster": "Digital Systems & Information",
 "one_line": "Security is arithmetic that is easy one way and ruinously hard backwards.",
 "math_branches": ["number-theory", "algebra-1", "discrete", "prob-stats"],
 "signature_skills": [
   "basic-operations-factor", "basic-operations-prime", "basic-operations-composite",
   "basic-operations-how-to-factor-a-number",
   "basic-operations-greatest-common-factor",
   "basic-operations-how-to-find-the-greatest-common-factor-of-a-set-of-numbers",
   "advanced-operations-exponent-also-power", "advanced-operations-how-to-evaluate-an-exponential-expression",
   "advanced-operations-factorial", "advanced-operations-how-to-evaluate-a-factorial-expression",
   "statistics-and-probability-permutation",
   "statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-permutation",
   "number-sense-numbers-and-counting-digit", "number-sense-odd", "number-sense-even",
   "discrete-mathematics-fundamental-counting-principle",
   "discrete-mathematics-how-to-apply-the-fundamental-counting-principle-to-count-outcomes",
   "discrete-mathematics-logical-statement"],
 "why_it_engages": "Password cracking is a combinatorics problem with a stopwatch, and the answer for their own password is usually humiliating.",
 "decision_archetypes": [
   "Force 14-character passwords or 8 characters plus a second factor, given cracking rates for each.",
   "Patch the vulnerability that is exploited in the wild but hard to reach, or the easy one nobody is using yet.",
   "Pay the ransom or restore from backups that are 19 hours stale."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("CISA Known Exploited Vulnerabilities catalog", "https://www.cisa.gov/known-exploited-vulnerabilities-catalog", "LIVE", "the authoritative list of actively exploited CVEs, with CSV/JSON feeds"),
   S("NIST National Vulnerability Database", "https://nvd.nist.gov/", "LIVE", "CVSS severity scores and exploitability metrics per vulnerability"),
   S("Have I Been Pwned", "https://haveibeenpwned.com/", "LIVE", "breach sizes and dates — real magnitudes for a risk calculation")],
  "note": "Vulnerability and breach data are excellent and free. Actual breach *cost* figures come from vendor reports (IBM/Ponemon) which are free to download but survey-based — cite them as survey averages, not facts about any one firm."},
 "existing_cases": ["Codebreaker"],
 "careers": [
  {"title": "Cryptographic Engineer", "math_used": "Works in modular arithmetic — RSA is c = m^e mod n, and its security is that factoring n back into two primes is hard.", "entry_path": "CS or maths degree, often an MS; deep number theory required."},
  {"title": "Security Operations Analyst", "math_used": "Reasons about base rates: with a 0.1% attack prevalence and a 1% false-positive rate, most alerts are noise — Bayes decides the triage order.", "entry_path": "IT or CS background plus Security+/CySA+; SOC entry roles."},
  {"title": "Penetration Tester", "math_used": "Estimates keyspace as characters^length, divides by an attacker's guess rate, and reports time-to-crack as an order of magnitude.", "entry_path": "Self-taught plus OSCP is a genuine route; CS degree optional."}],
 "authoring_priority": "HIGH"
},
{
 "id": "network-science",
 "name": "Networks, Graphs & Social Structure",
 "cluster": "Digital Systems & Information",
 "one_line": "Who is connected to whom decides everything from rumour spread to which airport you cannot afford to close.",
 "math_branches": ["algebra-1", "discrete", "linear-algebra", "prob-stats"],
 "signature_skills": [
   "geometry-vertex", "geometry-line-segment", "geometry-point",
   "statistics-and-probability-how-to-create-a-histogram-given-a-set-of-data",
   "statistics-and-probability-mean", "statistics-and-probability-median",
   "statistics-and-probability-outlier", "statistics-and-probability-non-linear",
   "statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination",
   "statistics-and-probability-combination",
   "number-sense-how-to-compare-two-or-more-values",
   "discrete-mathematics-graph-vertices-and-edges", "discrete-mathematics-vertex",
   "discrete-mathematics-edge", "discrete-mathematics-weighted-graph",
   "discrete-mathematics-how-to-find-the-shortest-path-between-two-vertices-in-a-weighted-graph"],
 "why_it_engages": "Six degrees of separation is a testable claim, and a social graph they can actually download settles it.",
 "decision_archetypes": [
   "Vaccinate the 50 highest-degree people or 500 at random, on the same contact network.",
   "Add the new flight route between two hubs or between a hub and an unserved city.",
   "Remove the single most-central account to stop a rumour, or throttle everyone slightly."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("Stanford SNAP datasets", "https://snap.stanford.edu/data/", "LIVE", "real social, road, citation and collaboration graphs as edge lists"),
   S("Network Repository", "https://networkrepository.com/", "LIVE", "6,000+ networks with precomputed degree and centrality statistics"),
   S("OpenStreetMap", "https://www.openstreetmap.org/", "LIVE", "an extractable road graph for a real town"),
   S("BTS On-Time Performance", "https://www.transtats.bts.gov/ontime/", "LIVE", "an airport-pair graph with real weights")],
  "note": "Graph data is abundant. The constraint is size — SNAP graphs run to millions of edges. For a case, hand the student a 30-node subgraph in the appendix and cite the source it was drawn from."},
 "existing_cases": [],
 "careers": [
  {"title": "Network Scientist", "math_used": "Computes degree distributions and betweenness centrality, and recognises a power law by a straight line on a log-log plot.", "entry_path": "PhD in CS, physics or applied maths; also industry research labs."},
  {"title": "Fraud Analyst", "math_used": "Finds rings by looking for unusually dense subgraphs and shared-attribute edges, scoring accounts by connectivity to known-bad nodes.", "entry_path": "Statistics or CS degree; banks, payment processors, marketplaces."},
  {"title": "Contact Tracing Coordinator", "math_used": "Builds the contact graph and prioritises by degree and recency, estimating secondary-case counts per index case.", "entry_path": "Public health training; scaled hugely during COVID and still used for TB/STI work."}],
 "authoring_priority": "HIGH"
},
{
 "id": "media-recommendation",
 "name": "Film, Streaming & Recommendation",
 "cluster": "Digital Systems & Information",
 "one_line": "A ratings table is a matrix with holes in it, and the whole business is guessing the holes.",
 "math_branches": ["pre-algebra", "algebra-1", "prob-stats", "linear-algebra"],
 "signature_skills": [
   "statistics-and-probability-mean", "statistics-and-probability-median", "statistics-and-probability-mode",
   "statistics-and-probability-how-to-find-the-mean-of-a-set-of-data",
   "statistics-and-probability-how-to-find-a-missing-data-element-given-the-mean-and-the-remaining-",
   "statistics-and-probability-correlation",
   "statistics-and-probability-how-to-identify-correlation-given-a-scatter-plot-or-set-of-data",
   "statistics-and-probability-scatter-plot", "statistics-and-probability-outlier",
   "statistics-and-probability-sample-size", "measurement-currency"],
 "why_it_engages": "The recommendation row on their homepage is a linear-algebra guess about them personally, and it is often wrong in ways they can explain.",
 "decision_archetypes": [
   "Green-light the $40m film with a known star or four $10m films with unknowns, given the historical return distribution.",
   "Recommend what is similar to what they watched, or what is popular overall, when the user has only rated three things.",
   "Release day-and-date to streaming or hold a 45-day theatrical window."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("MovieLens datasets", "https://grouplens.org/datasets/movielens/", "LIVE", "100k to 25m real user ratings, free, built for teaching"),
   S("IMDb non-commercial datasets", "https://developer.imdb.com/non-commercial-datasets/", "LIVE", "titles, ratings, runtimes, crew — full TSV dumps"),
   S("The Numbers", "https://www.the-numbers.com/", "LIVE", "budget and box office per film, browsable"),
   S("FiveThirtyEight data repo", "https://github.com/fivethirtyeight/data", "LIVE", "cleaned entertainment datasets including Bechdel-test and ratings work")],
  "note": "MovieLens is purpose-built for exactly this and is the best classroom recommender dataset that exists. Streaming *viewership* is the opposite — Netflix publishes only selective hours-viewed lists, so any per-title streaming number must be cited to that specific Netflix report or excluded."},
 "existing_cases": ["Movie Producer", "Cinema"],
 "careers": [
  {"title": "Recommendation Systems Engineer", "math_used": "Factorises a sparse user-by-item ratings matrix into two thin matrices of latent factors, and predicts a missing cell as a dot product.", "entry_path": "CS degree with linear algebra and ML; industry ML teams."},
  {"title": "Film Finance Analyst", "math_used": "Models a waterfall — distributor fee, then P&A recoupment, then talent participation — to find the break-even box office multiple.", "entry_path": "Finance or film business degree; studio and sales-agent roles."},
  {"title": "Audience Research Analyst", "math_used": "Weights a tracking survey to match the target population's age and region quotas before reporting an awareness percentage.", "entry_path": "Statistics/marketing degree; studios and research firms."}],
 "authoring_priority": "MEDIUM"
},
# ===================== MONEY, RISK & MARKETS ==============================
{
 "id": "insurance-actuarial",
 "name": "Insurance & Actuarial Risk",
 "cluster": "Money, Risk & Markets",
 "one_line": "Charge enough to cover the losses you cannot predict individually but can predict collectively.",
 "math_branches": ["pre-algebra", "algebra-1", "algebra-2", "prob-stats"],
 "signature_skills": [
   "statistics-and-probability-probability", "statistics-and-probability-event",
   "statistics-and-probability-outcome", "statistics-and-probability-theoretical-probability",
   "statistics-and-probability-experimental-probability",
   "statistics-and-probability-how-to-determine-the-probability-of-a-single-event",
   "statistics-and-probability-how-to-determine-the-probability-of-a-compound-event",
   "statistics-and-probability-independent-event", "statistics-and-probability-dependent-event",
   "advanced-numbers-how-to-find-the-percent-of-a-number", "measurement-currency",
   "statistics-and-probability-mean"],
 "why_it_engages": "An insurance company is legally betting against you and publishing the odds, which is a more honest casino than a casino.",
 "decision_archetypes": [
   "Set the teen-driver premium from the crash statistics or cap it politically and cross-subsidise from older drivers.",
   "Take the $500 deductible at a higher premium or the $2,000 deductible and self-insure the gap.",
   "Write flood cover in the coastal zone at an actuarially fair price nobody will pay, or exit the market."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("SSA Actuarial Life Table", "https://www.ssa.gov/oact/STATS/table4c6.html", "LIVE", "probability of death within a year by exact age and sex — the core table"),
   S("NHTSA FARS", "https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars", "LIVE", "every US fatal crash: age, time, conditions, restraint use"),
   S("OpenFEMA / NFIP claims", "https://www.fema.gov/about/openfema/data-sets", "LIVE", "millions of real flood claims with payout amounts"),
   S("CDC WONDER", "https://wonder.cdc.gov/", "LIVE", "cause-specific mortality rates for a life-contingency case")],
  "note": "Mortality, crash and flood-claim data are outstanding and free. Actual *premium* rate tables are filed with state insurance departments and are technically public but scattered across 50 state portals — expect to use a quoted premium from a real online quote, captured with a date and the exact inputs."},
 "existing_cases": ["Insurance Actuary", "Life Insurance", "Insurance", "End Of Life", "Driving Age"],
 "careers": [
  {"title": "Actuary", "math_used": "Prices a policy as expected loss (probability of claim times severity) plus loading, discounts future claims to present value, and reads q_x straight off a mortality table.", "entry_path": "Maths/actuarial degree plus the SOA/CAS exam sequence — the exams, not the degree, are the credential."},
  {"title": "Underwriter", "math_used": "Applies relativity factors multiplicatively to a base rate (age × territory × vehicle × history) and checks the result against the loss ratio target.", "entry_path": "Business or maths degree; CPCU designation."},
  {"title": "Claims Reserving Analyst", "math_used": "Projects ultimate losses from a claims-development triangle using chain-ladder factors — a table of ratios applied down the diagonal.", "entry_path": "Actuarial or statistics background; insurer reserving teams."}],
 "authoring_priority": "LOW"
},
{
 "id": "markets-investing",
 "name": "Markets, Investing & Corporate Finance",
 "cluster": "Money, Risk & Markets",
 "one_line": "Compounding, volatility and the fact that the right answer depends on how long you can wait.",
 "math_branches": ["pre-algebra", "algebra-1", "algebra-2", "prob-stats", "calculus"],
 "signature_skills": [
   "advanced-operations-exponent-also-power", "advanced-operations-base",
   "advanced-operations-how-to-evaluate-an-exponential-expression",
   "advanced-numbers-percent", "advanced-numbers-how-to-find-the-percent-of-a-number",
   "advanced-numbers-how-to-convert-percents-to-numbers",
   "statistics-and-probability-mean", "statistics-and-probability-range",
   "statistics-and-probability-variability", "statistics-and-probability-quartiles",
   "advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-with-exponents-order",
   "measurement-currency", "statistics-and-probability-line-of-best-fit"],
 "why_it_engages": "The gap between 6% and 8% over forty years is not 2% — it is roughly double the money, and that fact lands hard.",
 "decision_archetypes": [
   "Pay off the 6.5% student loan or invest in an index fund with a 7% historical average and real variance.",
   "Take the salary or the equity grant, given the company's stage and a stated failure probability.",
   "Hold cash through a downturn or stay invested, judged on a real historical window."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("FRED (St. Louis Fed)", "https://fred.stlouisfed.org/", "LIVE", "845,000+ series: rates, inflation, wages, housing, all CSV, no key"),
   S("SEC EDGAR", "https://www.sec.gov/edgar", "LIVE", "every public company's actual filed financial statements"),
   S("BLS CPI data", "https://www.bls.gov/cpi/data.htm", "LIVE", "inflation series and average prices for specific goods"),
   S("Stock Analysis historical prices", "https://stockanalysis.com/stocks/aapl/history/", "LIVE", "free daily OHLC history per ticker, no account")],
  "note": "Macro data is superb. Free *daily stock price CSVs* are the fragile part — Yahoo's endpoint and Stooq both now block scripted access, so use the stockanalysis.com history page (browsable and copyable) or FRED's own equity series, and record the retrieval date."},
 "existing_cases": ["Stock Market", "Investing - Stock Market - Options (Jia)", "Payroll", "Payroll 2.0"],
 "careers": [
  {"title": "Financial Analyst", "math_used": "Discounts a five-year cash-flow forecast at a stated WACC to a present value and tests how the answer moves when the terminal growth rate shifts by 50 basis points.", "entry_path": "Finance or accounting degree; CFA Level I is the common signal."},
  {"title": "Quantitative Trader", "math_used": "Computes rolling volatility as the standard deviation of log returns and sizes positions so each trade risks a fixed fraction of capital.", "entry_path": "Maths, physics or CS degree, often a PhD; prop shops and hedge funds."},
  {"title": "Financial Planner", "math_used": "Solves the future-value annuity formula for the monthly contribution that reaches a target, then re-solves in real terms after inflation.", "entry_path": "Any bachelor's plus the CFP coursework and exam."}],
 "authoring_priority": "LOW"
},
{
 "id": "pricing-household-money",
 "name": "Pricing, Retail & Household Money",
 "cluster": "Money, Risk & Markets",
 "one_line": "Tariffs, tiers and bundles designed so the comparison is hard on purpose.",
 "math_branches": ["pre-algebra", "algebra-1", "prob-stats"],
 "signature_skills": [
   "advanced-numbers-percent", "advanced-numbers-how-to-find-the-percent-of-a-number",
   "advanced-numbers-how-to-convert-numbers-to-percents",
   "advanced-numbers-how-to-find-a-whole-given-the-percent-and-the-part-of-the-whole",
   "measurement-currency", "measurement-unit",
   "advanced-operations-variable", "advanced-operations-how-to-evaluate-a-variable-expression-substitution-property",
   "advanced-operations-like-terms", "advanced-operations-distributive-property",
   "advanced-operations-how-to-add-and-subtract-an-expression-with-variables",
   "advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-both-sides",
   "number-sense-place-value",
   "statistics-and-probability-system-of-equations",
   "statistics-and-probability-how-to-solve-a-system-of-linear-equations",
   "statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data",
   "number-sense-how-to-compare-two-or-more-values"],
 "why_it_engages": "Two phone plans that cross over at 11 GB is the first time a system of equations has ever mattered to them personally.",
 "decision_archetypes": [
   "Take the plan with the low base and per-unit overage or the flat unlimited plan, given a usage distribution not a single number.",
   "Price the listing high with 60% occupancy or low with 85%, on real neighbourhood data.",
   "Buy the appliance that costs more and uses less power, given the local tariff and a stated lifetime."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("BLS CPI average price data", "https://www.bls.gov/cpi/data.htm", "LIVE", "actual average US prices for named goods, monthly"),
   S("Inside Airbnb", "https://insideairbnb.com/get-the-data/", "LIVE", "per-listing price, availability and reviews for dozens of cities"),
   S("FRED", "https://fred.stlouisfed.org/", "LIVE", "rents, wages, electricity price per kWh by state"),
   S("EIA Open Data", "https://www.eia.gov/opendata/", "LIVE", "residential electricity and fuel prices by state and month")],
  "note": "Published tariffs from carriers and utilities change constantly — always screenshot with a date and reproduce the table in the appendix, because the case must survive the page changing. Inside Airbnb is a scrape, not an official Airbnb release; say so."},
 "existing_cases": ["Phone Plan", "Phone Plans", "AirBnb", "Rent Vs. Own", "Caribbean Internet Cafe", "Pets", "Fast Food"],
 "careers": [
  {"title": "Pricing Analyst", "math_used": "Estimates price elasticity from two observed price/volume points and finds the revenue-maximising price where marginal revenue crosses zero.", "entry_path": "Economics or business analytics degree; retail and telecom pricing teams."},
  {"title": "Revenue Manager (Hotel/Airline)", "math_used": "Runs expected-marginal-seat-revenue: hold the last room for a possible high-fare booking only if price times probability beats the discounted sale now.", "entry_path": "Hospitality or analytics degree; property then corporate revenue roles."},
  {"title": "Consumer Financial Counsellor", "math_used": "Converts an APR to a monthly rate and amortises a balance to show how much of each payment is interest in month one versus month sixty.", "entry_path": "AFC or NFCC certification; nonprofit and credit-union roles."}],
 "authoring_priority": "LOW"
},
# ===================== CIVIC LIFE, LAW & LEARNING =========================
{
 "id": "elections-apportionment",
 "name": "Elections, Districting & Apportionment",
 "cluster": "Civic Life, Law & Learning",
 "one_line": "The same votes produce different winners depending on where you draw the lines and how you round the seats.",
 "math_branches": ["pre-algebra", "geometry", "algebra-1", "prob-stats", "discrete"],
 "signature_skills": [
   "measurement-rounding", "measurement-how-to-round-a-number-to-a-specified-place-value",
   "measurement-ratio", "measurement-proportion",
   "measurement-how-to-find-a-missing-amount-in-a-proportion",
   "geometry-perimeter", "geometry-area", "geometry-irregular-polygon",
   "geometry-convex", "geometry-concave",
   "geometry-how-to-find-the-measure-of-the-perimeter-of-a-polygon",
   "advanced-numbers-how-to-convert-numbers-to-percents",
   "statistics-and-probability-population"],
 "why_it_engages": "Five different, defensible rounding rules give five different answers about who runs the country. That is not a bug story — it is the actual history.",
 "decision_archetypes": [
   "Apportion the last seat by Hamilton's method or Huntington-Hill, when they disagree and one state loses.",
   "Draw the map for compactness or for keeping a county whole, when you cannot have both.",
   "Keep the Electoral College or move to national popular vote, argued from a specific past election's numbers."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("MIT Election Data & Science Lab", "https://electionlab.mit.edu/data", "LIVE", "precinct, county and state returns, cleaned, back decades"),
   S("Census congressional apportionment", "https://www.census.gov/topics/public-sector/congressional-apportionment.html", "LIVE", "official populations and seat allocations, every decade"),
   S("Redistricting Data Hub", "https://redistrictingdatahub.org/", "LIVE_LOGIN", "precinct shapefiles and block-level data; free signup to download"),
   S("Dave's Redistricting", "https://davesredistricting.org/", "LIVE", "draw a map and it computes compactness and partisan metrics live")],
  "note": "Everything needed is free. Dave's Redistricting is the standout classroom tool — a student can literally redraw a state and watch the seat count change. Precinct shapefiles need a free account, which is a small friction worth flagging to the facilitator."},
 "existing_cases": ["Electoral College", "Gerrymandering"],
 "careers": [
  {"title": "Redistricting Analyst", "math_used": "Scores maps on Polsby-Popper compactness (4·pi·area / perimeter squared) and efficiency gap, and runs thousands of random maps to see whether the proposed one is an outlier.", "entry_path": "Maths, geography or political science plus GIS; commissions, litigation teams, nonprofits."},
  {"title": "Election Administrator", "math_used": "Sizes polling places by queueing: arrival rate versus service rate per machine, to hold expected wait under a target.", "entry_path": "Public administration route; county clerk offices."},
  {"title": "Polling Statistician", "math_used": "Weights a raw sample to census targets by raking, and reports a margin of error that accounts for the design effect, not just root-n.", "entry_path": "Statistics degree; polling firms, media, campaigns."}],
 "authoring_priority": "MEDIUM"
},
{
 "id": "justice-forensics",
 "name": "Law, Forensics & Criminal Justice",
 "cluster": "Civic Life, Law & Learning",
 "one_line": "A one-in-a-million match sounds conclusive until you ask how many people were in the database.",
 "math_branches": ["pre-algebra", "algebra-1", "geometry", "prob-stats"],
 "signature_skills": [
   "statistics-and-probability-conditional-probability",
   "statistics-and-probability-how-to-determine-the-probability-of-conditional-events",
   "statistics-and-probability-independent-event",
   "statistics-and-probability-how-to-determine-the-probability-of-a-compound-event",
   "statistics-and-probability-random", "statistics-and-probability-convenience-sampling",
   "statistics-and-probability-population", "statistics-and-probability-sample",
   "geometry-angle", "geometry-right-triangle", "geometry-pythagorean-theorem",
   "advanced-numbers-how-to-find-the-percent-of-a-number"],
 "why_it_engages": "The prosecutor's fallacy has put innocent people in prison, and a 13-year-old can be taught to spot it in one lesson.",
 "decision_archetypes": [
   "Charge on the DNA database hit alone, or hold for corroborating evidence, given the database size.",
   "Deploy the extra patrol shift to the historic hotspot or spread it evenly, judged on displacement.",
   "Accept the plea at 3 years or go to trial with a stated conviction probability and a 12-year exposure."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("FBI Crime Data Explorer", "https://cde.ucr.cjis.gov/", "LIVE", "agency-level offence and arrest counts, downloadable"),
   S("Bureau of Justice Statistics", "https://bjs.ojp.gov/", "LIVE", "sentencing, recidivism, corrections population series"),
   S("NHTSA FARS", "https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars", "LIVE", "crash reconstruction inputs: speeds, angles, road conditions"),
   S("data.gov", "https://data.gov/", "LIVE", "city-level incident-with-coordinates files from many police departments")],
  "note": "Aggregate crime data is free but famously inconsistent between agencies and reporting years — a case must say which agencies reported. Forensic error rates (fingerprint, bite-mark, hair) come from the 2009 NAS report and PCAST 2016; both are free PDFs and should be cited directly rather than paraphrased."},
 "existing_cases": ["Heist"],
 "careers": [
  {"title": "Forensic Statistician", "math_used": "Computes a likelihood ratio — probability of the evidence if guilty over probability if innocent — and explains why that is not the probability of guilt.", "entry_path": "Statistics MS; crime labs, defence and prosecution experts."},
  {"title": "Crash Reconstruction Specialist", "math_used": "Back-calculates impact speed from skid length and a drag factor, and resolves post-impact vectors by conservation of momentum.", "entry_path": "Police service plus ACTAR accreditation, or engineering degree."},
  {"title": "Crime Analyst", "math_used": "Builds kernel-density hotspot maps and tests whether a change is real or within normal weekly variation using a control chart.", "entry_path": "Criminal justice or geography degree; IACA certification."}],
 "authoring_priority": "MEDIUM"
},
{
 "id": "education-systems",
 "name": "Education Systems & School Design",
 "cluster": "Civic Life, Law & Learning",
 "one_line": "The institution they sit in every day is itself an optimisation problem with a budget.",
 "math_branches": ["pre-algebra", "algebra-1", "prob-stats", "discrete"],
 "signature_skills": [
   "statistics-and-probability-mean", "statistics-and-probability-median",
   "statistics-and-probability-quartiles", "statistics-and-probability-outlier",
   "statistics-and-probability-how-to-find-the-mean-of-a-set-of-data",
   "statistics-and-probability-how-to-create-a-histogram-given-a-set-of-data",
   "statistics-and-probability-sample-size", "statistics-and-probability-convenience-sampling",
   "statistics-and-probability-variability",
   "statistics-and-probability-box-and-whisker-plot",
   "advanced-numbers-how-to-find-the-percent-of-a-number", "measurement-currency",
   "discrete-mathematics-graph-vertices-and-edges", "discrete-mathematics-vertex", "discrete-mathematics-edge"],
 "why_it_engages": "They are the dataset. Handing a student the timetabling constraints for their own school changes the argument permanently.",
 "decision_archetypes": [
   "Cut class size from 26 to 21 or keep 26 and fund a full-time reading specialist, on the same money.",
   "Start school at 08:50 for adolescent sleep or keep 07:40 for bus-fleet efficiency.",
   "Admit on test score alone or on a weighted index, shown against the resulting class composition."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("NCES", "https://nces.ed.gov/", "LIVE", "enrolment, staffing, finance and outcomes for every US district and school"),
   S("Urban Institute Education Data Portal", "https://educationdata.urban.org/", "LIVE", "the same federal data, cleaned and joined, with a free API"),
   S("College Scorecard", "https://collegescorecard.ed.gov/data/", "LIVE", "cost, completion and post-enrolment earnings per institution"),
   S("OECD PISA", "https://www.oecd.org/pisa/data/", "LIVE", "cross-country 15-year-old achievement with full microdata")],
  "note": "US and OECD education data are exceptionally complete. What is NOT public is any individual school's actual timetable constraint set or per-teacher salary — for a scheduling case, use the school's own published bell schedule and state staffing as an assumption."},
 "existing_cases": ["College Admissions", "Seton Hall", "Acton Survey", "Psychologist"],
 "careers": [
  {"title": "Education Data Analyst", "math_used": "Compares growth rather than level by computing a value-added residual — actual score minus score predicted from prior year — so a poor intake is not read as a poor school.", "entry_path": "Statistics, economics or education policy degree; districts and state agencies."},
  {"title": "School Scheduler / Registrar", "math_used": "Solves a graph-colouring problem: courses that share students cannot share a period, and the number of periods is the chromatic number.", "entry_path": "School administration route; a genuinely underrated maths job."},
  {"title": "Psychometrician", "math_used": "Fits item response theory curves so a hard question and an easy question contribute differently to the same ability estimate.", "entry_path": "PhD in educational measurement or quantitative psychology; testing organisations."}],
 "authoring_priority": "MEDIUM"
},
# ===================== CULTURE, PLAY & PERFORMANCE ========================
{
 "id": "music-acoustics",
 "name": "Music, Sound & Acoustics",
 "cluster": "Culture, Play & Performance",
 "one_line": "Pitch is frequency, harmony is small whole-number ratios, and a room can ruin both.",
 "math_branches": ["pre-algebra", "number-theory", "geometry", "algebra-2", "precalc"],
 "signature_skills": [
   "measurement-ratio", "measurement-how-to-find-equivalent-ratios",
   "basic-operations-factor", "basic-operations-greatest-common-factor",
   "basic-operations-how-to-find-the-greatest-common-factor-of-a-set-of-numbers",
   "fractions-fractions", "fractions-how-to-multiply-two-fractions",
   "fractions-how-to-divide-a-fraction-by-a-fraction",
   "fractions-equivalent-fractions", "fractions-how-to-find-equivalent-fractions",
   "advanced-operations-exponent-also-power", "advanced-operations-how-to-evaluate-an-exponential-expression",
   "geometry-reflection", "geometry-angle",
   "measurement-how-to-convert-an-amount-with-compound-units",
   "pre-calculus-sine-function", "pre-calculus-amplitude", "pre-calculus-period-of-a-function"],
 "why_it_engages": "A guitar string cut in half sounds exactly one octave higher, every time, and nobody ever tells them that is a 2:1 ratio doing it.",
 "decision_archetypes": [
   "Tune the keyboard in just intonation (perfect thirds, unplayable in every key) or equal temperament (every key slightly wrong, all usable).",
   "Treat the hall's rear wall with absorption to kill the echo, or with diffusion to keep the liveness.",
   "Site the outdoor stage facing the housing with a shorter cable run, or facing the field with a longer one, against a decibel limit at the property line."],
 "data_availability": {"grade": "MEDIUM", "sources": [
   S("Freesound", "https://freesound.org/", "LIVE", "Creative Commons audio a student can analyse; free account to download"),
   S("Million Song Dataset", "http://millionsongdataset.com/", "LIVE", "tempo, key, loudness and timbre features for a million tracks"),
   S("Audacity", "https://www.audacityteam.org/", "LIVE", "free tool with a spectrum analyser — students can measure a frequency themselves")],
  "note": "Interval ratios and equal-temperament frequencies are mathematics, not data, and need no citation beyond a definition. Measured reverberation times for a *named* hall are published only in acoustics papers and consultants' reports — build the room case on Sabine's formula with stated absorption coefficients from a published materials table. Spotify's audio-features API is no longer open to new applications; do not plan a case around it."},
 "existing_cases": [],
 "careers": [
  {"title": "Acoustic Consultant", "math_used": "Applies Sabine's equation RT60 = 0.161V/A — reverberation time from room volume over total absorption — and works in decibels, where adding two equal sources gains 3 dB, not double.", "entry_path": "Physics or acoustical engineering degree; INCE board certification."},
  {"title": "Instrument Maker / Luthier", "math_used": "Places frets by the twelfth root of two: each fret sits at the previous scale length divided by 2^(1/12).", "entry_path": "Lutherie school or apprenticeship."},
  {"title": "Live Sound Engineer", "math_used": "Computes delay-tower timing from distance over the speed of sound (about 343 m/s) so the far speaker fires in phase with the stage.", "entry_path": "Audio engineering programme or, more commonly, years of load-ins."}],
 "authoring_priority": "HIGH"
},
{
 "id": "tiling-pattern-art",
 "name": "Tessellation, Tiling & Pattern Art",
 "cluster": "Culture, Play & Performance",
 "one_line": "Only seventeen ways exist to repeat a pattern across a wall, and craftsmen found all of them before mathematicians named them.",
 "math_branches": ["geometry", "number-theory", "discrete"],
 "signature_skills": [
   "geometry-transformation", "geometry-translation", "geometry-rotation", "geometry-reflection",
   "geometry-symmetry", "geometry-line-of-symmetry",
   "geometry-clockwise", "geometry-counter-clockwise",
   "geometry-how-to-translate-a-figure-on-the-coordinate-plane",
   "geometry-how-to-reflect-a-figure-across-the-x-axis",
   "geometry-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-clockwise",
   "geometry-pentagon", "geometry-hexagon", "geometry-heptagon", "geometry-octagon",
   "geometry-nonagon", "geometry-decagon", "geometry-dodecagon",
   "geometry-rhombus", "geometry-kite", "geometry-regular-polygon", "geometry-n-gon",
   "geometry-vertical-angles", "geometry-supplementary-angles",
   "basic-operations-greatest-common-factor",
   "basic-operations-how-to-find-the-greatest-common-factor-of-a-set-of-numbers",
   "geometry-sum-of-the-interior-angles-of-a-polygon-theorem",
   "geometry-how-to-find-the-measure-of-an-interior-angle-of-a-polygon-given-the-other-angles",
   "geometry-how-to-find-the-area-of-a-regular-polygon",
   "discrete-mathematics-fundamental-counting-principle"],
 "why_it_engages": "Pentagons will not tile a floor and hexagons will, and once you see why, you cannot unsee it in every bathroom you enter.",
 "decision_archetypes": [
   "Tile the plaza in hexagons (no waste, no cuts) or in the client's preferred octagon-and-square pattern (more cuts, more waste).",
   "Restore the damaged section by matching the original symmetry group exactly, or use a modern approximation that costs a third as much.",
   "Design the repeat as a straight grid or a half-drop, given the fabric width and the visible seam."],
 "data_availability": {"grade": "MEDIUM", "sources": [
   S("Tiling Search (MIT)", "https://tilingsearch.mit.edu/", "LIVE", "large searchable archive of Islamic geometric patterns, measurable"),
   S("Tilings Encyclopedia (Bielefeld)", "https://tilings.math.uni-bielefeld.de/", "LIVE", "substitution tilings with their symmetry data"),
   S("Rijksstudio", "https://www.rijksmuseum.nl/en/rijksstudio", "LIVE", "public-domain high-resolution decorative-art images"),
   S("The Met Collection", "https://www.metmuseum.org/art/collection", "LIVE", "open-access Islamic and Roman mosaic images with dimensions"),
   S("GeoGebra", "https://www.geogebra.org/", "LIVE", "free tool for constructing and checking a tiling")],
  "note": "Pattern imagery is abundant and public-domain. Tile prices and installer labour rates are not published centrally — for the cost side of a case, use a named retailer's live price list captured with a date. Graded MEDIUM only because of the cost leg, not the geometry leg."},
 "existing_cases": [],
 "careers": [
  {"title": "Architectural Tile Designer", "math_used": "Checks that the interior angles meeting at each vertex sum to exactly 360 degrees, and computes waste as cut-tile area over total area.", "entry_path": "Design or architecture degree; also a craft route through tiling trades."},
  {"title": "Heritage Conservator", "math_used": "Identifies which of the 17 wallpaper groups a historic pattern belongs to, then reconstructs missing sections by applying that group's generating transformations.", "entry_path": "Conservation MSc; museums and heritage bodies."},
  {"title": "Surface Pattern Designer", "math_used": "Builds a repeat tile whose translations tessellate the plane seamlessly, and computes the drop offset so no seam is visible at the printed width.", "entry_path": "Textile or graphic design degree; licensing and freelance."}],
 "authoring_priority": "HIGH"
},
{
 "id": "sports-analytics",
 "name": "Sports Analytics & Team Selection",
 "cluster": "Culture, Play & Performance",
 "one_line": "Two players, one roster spot, and statistics that disagree about which one is better.",
 "math_branches": ["pre-algebra", "algebra-1", "prob-stats", "discrete"],
 "signature_skills": [
   "statistics-and-probability-mean", "statistics-and-probability-median",
   "statistics-and-probability-how-to-find-the-mean-of-a-set-of-data",
   "statistics-and-probability-quartiles", "statistics-and-probability-outlier",
   "statistics-and-probability-scatter-plot",
   "statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data",
   "statistics-and-probability-correlation", "statistics-and-probability-sample-size",
   "statistics-and-probability-variability", "measurement-ratio",
   "advanced-numbers-how-to-convert-numbers-to-percents"],
 "why_it_engages": "It is the one argument where a teenager will voluntarily demand better evidence than the adult they are arguing with.",
 "decision_archetypes": [
   "Start the high-average, low-power hitter or the streaky slugger, given the ballpark and the opposing pitcher.",
   "Rank the two-loss champion above the one-loss non-champion, defended with a stated formula.",
   "Rest the star for the playoffs or chase the seed, with win-probability attached to each."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("Retrosheet", "https://www.retrosheet.org/", "LIVE", "play-by-play for essentially every MLB game since 1901, free"),
   S("Baseball Savant (Statcast)", "https://baseballsavant.mlb.com/", "LIVE", "pitch-level velocity, spin and exit velocity, downloadable"),
   S("FiveThirtyEight data repo", "https://github.com/fivethirtyeight/data", "LIVE", "Elo ratings and forecast archives for several sports"),
   S("data.gov / Olympic and federation results", "https://data.gov/", "LIVE", "general portal; sport-specific results usually live on federation sites")],
  "note": "Baseball is the best-documented sport in history and Retrosheet is free and complete. Other sports are thinner: NBA/NFL play-by-play exists via unofficial scrapes with unstable terms, and IOC/federation results are usually HTML tables rather than datasets. Prefer baseball, chess or athletics when the case needs depth."},
 "existing_cases": ["A Coach_s Dilemma", "Baseball Lineup", "College Football Playoff Committee", "Player Of The Year", "LeBron Vs. Michael", "Speed Climbing", "Archery Camp"],
 "careers": [
  {"title": "Sports Data Scientist", "math_used": "Regresses observed performance toward the mean by a factor set by sample size, so 40 at-bats is not treated like 600.", "entry_path": "Statistics or CS degree; a public portfolio project is the usual way in."},
  {"title": "Scouting Analyst", "math_used": "Converts raw measurements to z-scores against a positional baseline so a shortstop's speed and a catcher's arm sit on one scale.", "entry_path": "Playing or coaching background plus analytics self-training."},
  {"title": "Sports Betting Trader", "math_used": "Converts odds to implied probability, removes the bookmaker's overround so the probabilities sum to one, and prices the residual edge.", "entry_path": "Maths degree into a trading desk; heavily quantitative."}],
 "authoring_priority": "LOW"
},
{
 "id": "games-and-gambling",
 "name": "Games, Gambling & Tournament Design",
 "cluster": "Culture, Play & Performance",
 "one_line": "The house edge is a number, the bracket is a graph, and both are designed on purpose.",
 "math_branches": ["pre-algebra", "algebra-1", "prob-stats", "discrete"],
 "signature_skills": [
   "statistics-and-probability-probability", "statistics-and-probability-theoretical-probability",
   "statistics-and-probability-experimental-probability",
   "statistics-and-probability-independent-event", "statistics-and-probability-dependent-event",
   "statistics-and-probability-how-to-determine-the-probability-of-a-compound-event",
   "statistics-and-probability-permutation", "statistics-and-probability-combination",
   "statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-permutation",
   "statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination",
   "advanced-operations-factorial", "advanced-operations-how-to-evaluate-a-factorial-expression",
   "fractions-how-to-multiply-two-fractions"],
 "why_it_engages": "Expected value is the concept that permanently ruins the lottery for you, and that is a gift.",
 "decision_archetypes": [
   "Run the tournament as single elimination (fast, high upset rate) or Swiss (fair, needs more rounds), for a fixed venue booking.",
   "Add the high-variance slot bank or the low-variance table game, given floor space and a target hold percentage.",
   "Seed the bracket strictly by rating or protect regional diversity, judged on the probability the best player wins."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("Lichess open database", "https://database.lichess.org/", "LIVE", "billions of rated games with ratings, clocks and results, free"),
   S("Chess.com Published-Data API", "https://www.chess.com/news/view/published-data-api", "LIVE", "public player and game endpoints, no key"),
   S("Wizard of Odds", "https://wizardofodds.com/", "LIVE", "worked house-edge derivations for essentially every casino game"),
   S("FiveThirtyEight data repo", "https://github.com/fivethirtyeight/data", "LIVE", "tournament forecast and Elo archives")],
  "note": "Game outcome data is superb and Lichess in particular is a gift — real Elo, real results, tens of millions of games. Casino *hold* and handle figures per property are filed with state gaming commissions (Nevada Gaming Control Board publishes monthly) and are free, but per-machine data is not. Wizard of Odds is a private site, not a regulator; cite it as a worked derivation, not an authority."},
 "existing_cases": ["Casino Owner"],
 "careers": [
  {"title": "Casino Game Mathematician", "math_used": "Enumerates every outcome to compute expected value per unit wagered, then derives the standard deviation to tell the operator how big a bankroll the game needs.", "entry_path": "Maths degree; a small specialist field of consultancies."},
  {"title": "Tournament Director", "math_used": "Computes rounds needed as log base 2 of the field for elimination, or applies the Swiss pairing rule and Buchholz tiebreak.", "entry_path": "Federation certification (FIDE arbiter, USCF TD) plus experience."},
  {"title": "Game Balance Designer", "math_used": "Models a matchmaking system as Elo/Glicko updates and simulates thousands of matches to check the rating distribution stays stable.", "entry_path": "Game design or CS degree; studio design teams."}],
 "authoring_priority": "MEDIUM"
},
{
 "id": "drill-choreography",
 "name": "Marching Drill & Choreography",
 "cluster": "Culture, Play & Performance",
 "one_line": "One hundred and twenty people, eight counts, and a formation that has to rotate without anyone colliding.",
 "math_branches": ["pre-algebra", "geometry", "algebra-1", "linear-algebra"],
 "signature_skills": [
   "geometry-transformation", "geometry-rotation", "geometry-translation", "geometry-reflection",
   "geometry-dilation", "geometry-scale-factor",
   "geometry-clockwise", "geometry-counter-clockwise",
   "geometry-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-clockwise",
   "geometry-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-counterclockwise",
   "geometry-how-to-translate-a-figure-on-the-coordinate-plane",
   "geometry-how-to-dilate-a-figure-on-the-coordinate-plane-given-a-scale-factor",
   "geometry-coordinate-plane", "geometry-coordinate-pair-also-ordered-pair",
   "geometry-how-to-graph-a-coordinate-pair-on-the-coordinate-plane",
   "geometry-fundamentals-of-geometry-congruent", "geometry-similar",
   "measurement-how-to-convert-an-amount-from-one-unit-to-another-unit"],
 "why_it_engages": "A football field is literally a coordinate grid with the axes painted on it, and a drill chart is a list of ordered pairs that 120 teenagers execute in eight counts.",
 "decision_archetypes": [
   "Rotate the block 90 degrees about its centre in 16 counts (some players must cover 12 yards) or translate and reform (safe, less dramatic).",
   "Dilate the company front to fill the field for the visual, or keep it tight so the sound stays coherent.",
   "Set the drill to the 50-yard line for symmetry, or offset it toward the judges' box for the score."],
 "data_availability": {"grade": "MEDIUM", "sources": [
   S("NCAA Football Rules Book (field diagrams)", "https://ncaaorg.s3.amazonaws.com/championships/sports/football/rules/PRMFB_RulesBook.pdf", "LIVE", "official field dimensions, yard-line and hash spacing — the coordinate grid"),
   S("Drum Corps International scores", "https://www.dci.org/scores", "LIVE", "real judged scores by caption for real shows"),
   S("NFHS", "https://www.nfhs.org/", "LIVE", "high school rules body; field and competition standards"),
   S("GeoGebra", "https://www.geogebra.org/", "LIVE", "free tool to plot and transform the formation on the grid")],
  "note": "The field grid is exactly specified and free, and DCI scores are public. What is NOT public is any actual drill chart — Pyware and similar are paid tools and shows are copyrighted. The case must supply its own formation coordinates in the appendix, declared as authored, with only the field geometry and the scores cited. Graded MEDIUM for that reason."},
 "existing_cases": [],
 "careers": [
  {"title": "Drill Designer", "math_used": "Writes each performer's position as an ordered pair on the yard-line grid per set, then checks that no path exceeds the maximum step size — 8-to-5 marching is exactly 22.5 inches per step.", "entry_path": "Music education degree plus apprenticeship with a designer; heavily freelance."},
  {"title": "Choreographer / Movement Director", "math_used": "Builds formations from symmetry operations — reflect the left half onto the right, rotate the group about a focal point — and counts spacing in body widths.", "entry_path": "Dance training and company experience."},
  {"title": "Stage / Event Production Manager", "match_check": True, "math_used": "Lays out sightlines as angles from the furthest seat and computes rigging load as a sum of point loads against a rated capacity.", "entry_path": "Technical theatre degree or IATSE apprenticeship."}],
 "authoring_priority": "HIGH"
},
# ===================== DEEP TIME & LANGUAGE ===============================
{
 "id": "archaeology",
 "name": "Archaeology & Heritage Science",
 "cluster": "Deep Time & Language",
 "one_line": "You get one dig season, a grid of squares, and a date that is always a range, never a number.",
 "math_branches": ["pre-algebra", "geometry", "algebra-2", "prob-stats", "precalc"],
 "signature_skills": [
   "geometry-coordinate-plane", "geometry-quadrant", "geometry-origin",
   "geometry-how-to-graph-a-coordinate-pair-on-the-coordinate-plane",
   "geometry-area", "geometry-how-to-find-the-area-of-a-rectangle",
   "geometry-volume", "geometry-how-to-find-the-volume-of-a-prism",
   "statistics-and-probability-systematic-sampling", "statistics-and-probability-simple-random-sampling",
   "statistics-and-probability-stratified-sampling",
   "advanced-operations-exponent-also-power", "advanced-operations-how-to-evaluate-an-exponential-expression",
   "number-sense-depth"],
 "why_it_engages": "Radiocarbon dating is exponential decay you can hold in your hand, and the answer comes out as \"1450 to 1620 CE\" — which is a lesson about uncertainty no textbook delivers as well.",
 "decision_archetypes": [
   "Excavate 12 one-metre test pits across the whole site or one 4x4 metre trench in the promising corner.",
   "Spend the dating budget on three samples from one layer (tight date, one context) or one sample from each of three layers (a sequence, each loose).",
   "Excavate now ahead of the road, or leave it in the ground and lose access forever."],
 "data_availability": {"grade": "MEDIUM", "sources": [
   S("Open Context", "https://opencontext.org/", "LIVE", "published excavation datasets: finds, contexts, coordinates, open licence"),
   S("Archaeology Data Service (UK)", "https://archaeologydataservice.ac.uk/", "LIVE", "site archives, reports and finds databases, free"),
   S("OxCal (Oxford Radiocarbon Accelerator Unit)", "https://c14.arch.ox.ac.uk/oxcal.html", "LIVE_LOGIN", "the standard calibration tool; downloadable free, online version wants a free login"),
   S("USGS National Map Downloader", "https://apps.nationalmap.gov/downloader/", "LIVE", "LiDAR-derived terrain for site prospection")],
  "note": "Published excavation data is real but scattered and inconsistently structured — Open Context is the best single entry point. Radiocarbon *lab costs* per sample are quoted per-lab (Beta Analytic publishes a price list); cite the lab you use. Graded MEDIUM because assembling a coherent site dataset takes real work."},
 "existing_cases": [],
 "careers": [
  {"title": "Field Archaeologist", "math_used": "Records every find as a three-dimensional coordinate against a site datum, and computes soil volume removed per context to report finds density per cubic metre.", "entry_path": "Archaeology degree plus field school; commercial units hire at BA level."},
  {"title": "Archaeological Scientist (Dating Specialist)", "math_used": "Applies N(t) = N0 e^(-lambda t) with carbon-14's 5,730-year half-life, then calibrates against the tree-ring curve to turn one number into a probability distribution over calendar years.", "entry_path": "Chemistry or physics degree into an MSc in archaeological science."},
  {"title": "Heritage Impact Assessor", "math_used": "Scores sites on a weighted multi-criteria matrix — significance, condition, threat — and computes how much of a site a proposed route destroys as a percentage of known extent.", "entry_path": "Archaeology or planning degree; consultancy and government."}],
 "authoring_priority": "MEDIUM"
},
{
 "id": "linguistics",
 "name": "Linguistics & Language Data",
 "cluster": "Deep Time & Language",
 "one_line": "Word frequencies obey a law so sharp it looks fake, and it holds in every language anyone has checked.",
 "math_branches": ["pre-algebra", "algebra-2", "prob-stats", "discrete"],
 "signature_skills": [
   "statistics-and-probability-how-to-create-a-histogram-given-a-set-of-data",
   "statistics-and-probability-non-linear", "statistics-and-probability-linear",
   "statistics-and-probability-scatter-plot",
   "statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data",
   "statistics-and-probability-how-to-identify-correlation-given-a-scatter-plot-or-set-of-data",
   "statistics-and-probability-mode", "statistics-and-probability-range",
   "statistics-and-probability-sample", "statistics-and-probability-population",
   "measurement-ratio", "advanced-numbers-how-to-convert-numbers-to-percents"],
 "why_it_engages": "Rank a book's words by frequency and the second word appears half as often as the first, the third a third as often — in English, Mandarin and Swahili alike. That is uncanny, and they can check it in an afternoon.",
 "decision_archetypes": [
   "Spend the revitalisation budget on the language with 800 elderly speakers or the one with 6,000 speakers and no young ones.",
   "Build the translation system from 400 hours of clean speech or 4,000 hours of noisy speech.",
   "Standardise the orthography on the majority dialect (fast literacy for most) or a compromise spelling (slower, but nobody is excluded)."],
 "data_availability": {"grade": "HIGH", "sources": [
   S("WALS — World Atlas of Language Structures", "https://wals.info/", "LIVE", "structural features coded for 2,600+ languages, free download"),
   S("Google Books Ngram Viewer", "https://books.google.com/ngrams/", "LIVE", "word frequency over 200 years, with downloadable n-gram corpora"),
   S("Universal Dependencies", "https://universaldependencies.org/", "LIVE", "syntactically annotated treebanks across 100+ languages, free"),
   S("Our World in Data", "https://ourworldindata.org/", "LIVE", "literacy and language demographics by country")],
  "note": "Corpus and typological data are excellent. Speaker-count data is the weak point: Ethnologue is the standard source and is paywalled, so use UNESCO's Atlas of Endangered Languages or a national census language question instead, and say which one."},
 "existing_cases": [],
 "careers": [
  {"title": "Computational Linguist", "math_used": "Estimates n-gram probabilities with smoothing so unseen word pairs do not get probability zero, and evaluates a model by perplexity — an exponentiated average log probability.", "entry_path": "Linguistics plus CS; MS is common; NLP teams everywhere."},
  {"title": "Field Linguist / Language Documenter", "math_used": "Designs a sampling frame across speaker age and village so a 30-speaker corpus actually represents the community, and reports inter-annotator agreement as Cohen's kappa.", "entry_path": "Linguistics PhD; SIL and university documentation projects."},
  {"title": "Forensic Linguist", "math_used": "Compares authorship by frequency profiles of function words and computes a likelihood ratio for the disputed text.", "entry_path": "Linguistics PhD plus expert-witness training; a very small field."}],
 "authoring_priority": "MEDIUM"
},
]


# --------------------------------------------------------------------------
def load(name):
    with open(os.path.join(RM, name)) as f:
        return json.load(f)


def spine_index(spine):
    idx = {}
    for dom in spine["domains"]:
        for grp in dom["groups"]:
            for sk in grp["skills"]:
                idx[sk["id"]] = {
                    "label": sk["label"], "n": sk["n"],
                    "domain": dom["domain"], "group": grp["group"],
                }
    return idx


def main():
    dry = "--dry-run" in sys.argv
    spine = load("standards_spine.json")
    tree = load("curriculum_tree.json")
    corpus = load("corpus_index.json")

    skills = spine_index(spine)
    branch_ids = {b["id"] for b in tree["branches"]}
    corpus_titles = {c["title"] for c in corpus["cases"]}
    cluster_names = {c["name"] for c in CLUSTERS}

    errs, warns, dropped = [], [], []
    seen = set()

    for d in DOMAINS:
        did = d["id"]
        if did in seen:
            errs.append(f"duplicate domain id: {did}")
        seen.add(did)
        if d["cluster"] not in cluster_names:
            errs.append(f"{did}: unknown cluster {d['cluster']!r}")
        good = []
        for s in d["signature_skills"]:
            if s in skills:
                good.append(s)
            else:
                dropped.append((did, s))
        d["signature_skills"] = good
        if not good:
            errs.append(f"{did}: no valid signature_skills")
        for b in d["math_branches"]:
            if b not in branch_ids:
                errs.append(f"{did}: unknown branch {b!r}")
        for t in d["existing_cases"]:
            if t not in corpus_titles:
                errs.append(f"{did}: existing_case title not in corpus_index: {t!r}")
        if not d["careers"]:
            errs.append(f"{did}: no careers")
        if not d["decision_archetypes"]:
            errs.append(f"{did}: no decision_archetypes")
        for c in d["careers"]:
            c.pop("match_check", None)
            for k in ("title", "math_used", "entry_path"):
                if not c.get(k):
                    errs.append(f"{did}: career missing {k}")
        if d["data_availability"]["grade"] not in ("HIGH", "MEDIUM", "LOW"):
            errs.append(f"{did}: bad data grade")
        if not d["data_availability"]["sources"]:
            errs.append(f"{did}: no sources")
        if d["authoring_priority"] not in ("HIGH", "MEDIUM", "LOW"):
            errs.append(f"{did}: bad authoring_priority")
        # derived
        d["uncovered_signature_skills"] = [s for s in good if skills[s]["n"] == 0]
        d["n_signature_skills"] = len(good)
        d["n_uncovered_signature_skills"] = len(d["uncovered_signature_skills"])

    if dropped:
        for did, s in dropped:
            warns.append(f"DROPPED invalid skill id {s!r} from {did}")

    if errs:
        print("VALIDATION FAILED")
        for e in errs:
            print("  ERROR:", e)
        for w in warns:
            print("  WARN :", w)
        sys.exit(1)

    for w in warns:
        print("  WARN :", w)

    # ---------------- domains.json ----------------
    all_urls = []
    for d in DOMAINS:
        for s in d["data_availability"]["sources"]:
            all_urls.append(s["verified"])
    n_live = sum(1 for v in all_urls if v.startswith("LIVE"))
    n_know = sum(1 for v in all_urls if v == "KNOWLEDGE")

    out = {
        "_schema": {
            "purpose": "Phase-4 'Root Connections' spine. The application domains that consume the curriculum tree. Supersedes curriculum_tree.intersections[].",
            "join_keys": "signature_skills[] -> standards_spine skill ids; math_branches[] -> curriculum_tree branch ids; existing_cases[] -> corpus_index case titles.",
            "fields": {
                "id": "stable slug, unique",
                "name": "display name",
                "cluster": "one of clusters[].name",
                "one_line": "what the domain actually decides, in one sentence",
                "math_branches": "curriculum_tree branch ids this domain genuinely consumes",
                "signature_skills": "standards_spine skill ids this domain naturally exercises; validated at build time",
                "uncovered_signature_skills": "DERIVED: the subset of signature_skills with n == 0 in the spine",
                "n_signature_skills": "DERIVED count",
                "n_uncovered_signature_skills": "DERIVED count",
                "why_it_engages": "one honest sentence about why a 13-year-old would care",
                "decision_archetypes": "2-4 binary dilemmas a case in this domain could pose",
                "data_availability": {
                    "grade": "HIGH | MEDIUM | LOW — how easily a student can source real numbers here",
                    "sources": "[{label, url, verified, offers}]",
                    "verified": "LIVE = fetched during authoring and renders free; LIVE_JS = free but browser-only (scripted fetch returns nothing); LIVE_LOGIN = free but needs an account; KNOWLEDGE = listed from knowledge, NOT fetched",
                    "note": "what is easy to source and what is not — read this before authoring",
                },
                "existing_cases": "corpus_index titles that already sit in this domain (a case may appear under two domains)",
                "careers": "[{title, math_used, entry_path}] — math_used must name the actual computation",
                "authoring_priority": "HIGH | MEDIUM | LOW. HIGH = closes uncovered spine skills AND has strong free data AND is under-represented in the existing 56.",
            },
            "deviation_note": "The commissioning brief specified data_availability.sources as a list of strings. It is emitted as a list of objects so the verification state of each URL is machine-readable. `label` + `url` reconstruct the string form.",
        },
        "_generated": {
            "generated_at": datetime.date.today().isoformat(),
            "generator": "app/build_domains.py",
            "domain_count": len(DOMAINS),
            "cluster_count": len(CLUSTERS),
            "verified": {
                "signature_skill_ids": f"all {sum(d['n_signature_skills'] for d in DOMAINS)} ids checked against readmodel/standards_spine.json at build time; build aborts on a miss",
                "math_branch_ids": "all checked against readmodel/curriculum_tree.json branches[].id",
                "existing_case_titles": "all checked verbatim against readmodel/corpus_index.json cases[].title (including the corpus's own typos, e.g. 'Castle Securtiy')",
                "urls_fetched_live": n_live,
                "urls_listed_from_knowledge": n_know,
                "url_method": "Each URL was retrieved during authoring on 2026-07-31 via the workspace web_fetch tool and its rendered content inspected. Anything that could not be retrieved was either replaced with a verified alternative or downgraded and flagged in the domain's data_availability.note. No URL in this file was written from memory without a fetch except those marked KNOWLEDGE.",
                "not_verified": [
                    "Whether every dataset behind a live landing page is still updated — freshness is the case author's job at research time.",
                    "Paid sources are named in notes as paid (IFR World Robotics, RSMeans, Ethnologue, Clarksons) and are deliberately NOT given as sources.",
                ],
            },
            "supersedes": "curriculum_tree.json intersections[] (3 items), preserved there as legacy_intersections[]",
        },
        "clusters": CLUSTERS,
        "domains": DOMAINS,
    }

    # ---------------- domain_coverage.json ----------------
    by_branch = []
    for b in tree["branches"]:
        feeders = [d for d in DOMAINS if b["id"] in d["math_branches"]]
        case_titles = sorted({t for d in feeders for t in d["existing_cases"]})
        sk_ids = sorted({s for d in feeders for s in d["signature_skills"]})
        unc = [s for s in sk_ids if skills[s]["n"] == 0]
        has_rows = bool(b.get("acton_domains"))
        n_high = len([d for d in feeders if d["authoring_priority"] == "HIGH"])
        domain_starved = (len(feeders) < 6) or (n_high == 0)
        case_starved = len(case_titles) < 10
        reasons = []
        if len(feeders) < 6:
            reasons.append("fewer than 6 feeding domains")
        if n_high == 0:
            reasons.append("no HIGH-priority domain feeds it")
        if case_starved:
            reasons.append("fewer than 10 of the 56 existing cases sit in its domains")
        by_branch.append({
            "branch": b["id"], "name": b["branch"], "phase": b["phase"],
            "has_standards_rows": has_rows,
            "n_domains": len(feeders),
            "domains": [d["id"] for d in feeders],
            "high_priority_domains": [d["id"] for d in feeders if d["authoring_priority"] == "HIGH"],
            "n_existing_cases_in_those_domains": len(case_titles),
            "existing_cases": case_titles,
            "n_signature_skills_reachable": len(sk_ids),
            "n_uncovered_signature_skills_reachable": len(unc),
            "domain_starved": domain_starved,
            "case_starved": case_starved,
            "starvation_reasons": reasons,
        })

    by_domain = [{
        "domain": d["id"], "name": d["name"], "cluster": d["cluster"],
        "authoring_priority": d["authoring_priority"],
        "data_grade": d["data_availability"]["grade"],
        "branches": d["math_branches"],
        "n_existing_cases": len(d["existing_cases"]),
        "n_signature_skills": d["n_signature_skills"],
        "n_uncovered_signature_skills": d["n_uncovered_signature_skills"],
        "uncovered_signature_skills": [
            {"id": s, "label": skills[s]["label"], "spine_domain": skills[s]["domain"], "spine_group": skills[s]["group"]}
            for s in d["uncovered_signature_skills"]
        ],
    } for d in DOMAINS]

    # which uncovered spine skills are now reachable from at least one domain?
    all_uncovered = {sid for sid, v in skills.items() if v["n"] == 0}
    reached = {s for d in DOMAINS for s in d["uncovered_signature_skills"]}
    orphan = sorted(all_uncovered - reached)

    # spine group -> which domains touch it
    grp_map = {}
    for d in DOMAINS:
        for s in d["signature_skills"]:
            key = f"{skills[s]['domain']} / {skills[s]['group']}"
            grp_map.setdefault(key, set()).add(d["id"])

    cov = {
        "_schema": {
            "purpose": "Derived join over domains.json x curriculum_tree.json x standards_spine.json. Answers: which domains feed a branch, which branches are domain-starved, and which uncovered skills sit in a compelling domain.",
            "generated_by": "app/build_domains.py",
            "domain_starved": "true if a branch has fewer than 6 of the 40 domains feeding it, OR no HIGH-priority domain feeds it. This is about whether the SPINE reaches the branch.",
            "case_starved": "true if fewer than 10 of the 56 existing corpus cases sit in the branch's domains. This is about whether the CORPUS reaches the branch, and it is the real authoring signal.",
            "orphan_uncovered_skills": "spine skills with n==0 that no domain lists as a signature skill — still genuinely unreachable and the residual authoring risk",
        },
        "_generated_at": datetime.date.today().isoformat(),
        "totals": {
            "domains": len(DOMAINS),
            "clusters": len(CLUSTERS),
            "branches": len(tree["branches"]),
            "spine_skills": len(skills),
            "spine_skills_uncovered": len(all_uncovered),
            "uncovered_skills_now_reachable_from_a_domain": len(reached),
            "uncovered_skills_still_orphaned": len(orphan),
            "corpus_cases": len(corpus_titles),
            "corpus_cases_assigned_to_a_domain": len({t for d in DOMAINS for t in d["existing_cases"]}),
        },
        "by_branch": by_branch,
        "by_domain": by_domain,
        "by_spine_group": [
            {"spine_group": k, "n_domains": len(v), "domains": sorted(v)}
            for k, v in sorted(grp_map.items())
        ],
        "orphan_uncovered_skills": [
            {"id": s, "label": skills[s]["label"], "spine_group": f"{skills[s]['domain']} / {skills[s]['group']}"}
            for s in orphan
        ],
        "unassigned_corpus_cases": sorted(corpus_titles - {t for d in DOMAINS for t in d["existing_cases"]}),
    }

    if dry:
        print("DRY RUN OK — %d domains, %d clusters, %d URLs (%d fetched-live, %d knowledge)"
              % (len(DOMAINS), len(CLUSTERS), len(all_urls), n_live, n_know))
        return

    # ---------------- curriculum_tree.json: supersede intersections[] -------
    # The 3-item hand-written intersections[] is replaced by pointers into
    # domains.json. The originals are preserved, never silently dropped.
    if "legacy_intersections" not in tree:
        tree["legacy_intersections"] = tree["intersections"]
    tree["intersections_superseded_by"] = "domains.json"
    tree["intersections"] = [{
        "domain": d["name"],
        "branches": d["math_branches"],
        "note": d["one_line"],
        "ref": "domains.json#" + d["id"],
        "cluster": d["cluster"],
        "authoring_priority": d["authoring_priority"],
    } for d in DOMAINS]
    tree["_schema"]["intersections_note"] = (
        "intersections[] is DERIVED from readmodel/domains.json by app/build_domains.py — "
        "do not hand-edit. The original three hand-written intersections are preserved verbatim "
        "in legacy_intersections[]. Full domain records (signature skills, data sources, careers, "
        "authoring priority) live in domains.json; the join key is ref / domains.json#<id>."
    )
    with open(os.path.join(RM, "curriculum_tree.json"), "w") as f:
        json.dump(tree, f, indent=2, ensure_ascii=False)

    with open(os.path.join(RM, "domains.json"), "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    with open(os.path.join(RM, "domain_coverage.json"), "w") as f:
        json.dump(cov, f, indent=2, ensure_ascii=False)
    print("wrote readmodel/domains.json (%d domains, %d clusters)" % (len(DOMAINS), len(CLUSTERS)))
    print("wrote readmodel/domain_coverage.json")
    print("URLs: %d total, %d fetched live, %d knowledge-only" % (len(all_urls), n_live, n_know))


if __name__ == "__main__":
    main()
