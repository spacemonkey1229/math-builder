const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, AlignmentType, LevelFormat, convertInchesToTwip, ImageRun,
  ExternalHyperlink,
} = require("docx");

const NAVY = "1a3a5c";

const numbering = {
  config: [
    {
      reference: "bullets",
      levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: convertInchesToTwip(0.35), hanging: convertInchesToTwip(0.2) } } } }],
    },
  ],
};

function h1(text) { return new Paragraph({ text, heading: HeadingLevel.HEADING_1, spacing: { before: 300, after: 150 } }); }
function h2(text) { return new Paragraph({ text, heading: HeadingLevel.HEADING_2, spacing: { before: 260, after: 120 } }); }
function p(text, opts = {}) { return new Paragraph({ children: [new TextRun({ text, ...opts })], spacing: { after: 120 } }); }
function pRuns(runs, opts = {}) { return new Paragraph({ children: runs, spacing: { after: 120 }, ...opts }); }
function bullet(text) { return new Paragraph({ text, numbering: { reference: "bullets", level: 0 }, spacing: { after: 60 } }); }
function bold(text) { return new TextRun({ text, bold: true }); }
function link(text, url) {
  return new ExternalHyperlink({ link: url, children: [new TextRun({ text, style: "Hyperlink" })] });
}

function cell(text, opts = {}) {
  return new TableCell({
    width: { size: opts.width || 2000, type: WidthType.DXA },
    shading: opts.header ? { type: ShadingType.CLEAR, color: "auto", fill: NAVY } : undefined,
    children: [new Paragraph({ children: [new TextRun({ text: String(text), bold: !!opts.header, color: opts.header ? "FFFFFF" : undefined, size: 20 })] })],
  });
}
function table(headers, rows, widths) {
  const w = widths || headers.map(() => Math.floor(9000 / headers.length));
  return new Table({
    width: { size: 9000, type: WidthType.DXA },
    columnWidths: w,
    rows: [
      new TableRow({ children: headers.map((h, i) => cell(h, { header: true, width: w[i] })) }),
      ...rows.map(r => new TableRow({ children: r.map((c, i) => cell(c, { width: w[i] })) })),
    ],
  });
}

const diagramBuf = fs.readFileSync(__dirname + "/published/_parcel_diagram.png");
// PNG intrinsic size 1380x576 -- scale to fit page width (~9000 DXA ~ 6.25in @ 1440 DXA/in => target width 6.2in)
const targetWidthIn = 6.2;
const aspect = 576 / 1380;
const imageParagraph = new Paragraph({
  children: [new ImageRun({
    data: diagramBuf,
    transformation: { width: Math.round(targetWidthIn * 96), height: Math.round(targetWidthIn * 96 * aspect) },
    type: "png",
  })],
  alignment: AlignmentType.CENTER,
  spacing: { after: 100 },
});

const doc = new Document({
  numbering,
  styles: { default: { document: { run: { font: "Calibri", size: 22 } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1000, bottom: 1000, left: 1100, right: 1100 } } },
    children: [
      new Paragraph({ children: [new TextRun({ text: "Case Study: The Odd Lot", bold: true, size: 40, color: NAVY })], spacing: { after: 80 } }),
      p("MS | Math | Case Study | 2026-27 | Adventure", { italics: true, size: 20 }),

      h1("Overview"),
      p("Priya Chandrasekaran has the survey map spread across two desks because it won’t fit on one."),
      p("The assemblage — three parcels the city has been trying to develop for a decade — sits exactly where it always has: on the wedge-shaped block where the old diagonal avenue slices through the numbered grid, the way it has for two hundred years. Nobody drew these lot lines on purpose. They’re what was left over after the angle cut through."),
      p("The community board meeting is in nine days. Her director wants one recommendation, not a menu. Priya has spent the morning with a protractor and a calculator, and the honest truth is that the map on the left desk and the map on the right desk both work — they just don’t agree with each other at all."),
      pRuns([new TextRun("Her phone buzzes. It’s the director: "), new TextRun({ text: "“Which one are we bringing Thursday?”", italics: true })]),
      p("Priya doesn’t answer yet. She picks up the protractor again."),

      h1("Background"),
      pRuns([
        new TextRun("Priya Chandrasekaran is a zoning analyst in a mid-sized city’s Department of City Planning. A "),
        bold("zoning analyst"),
        new TextRun(" reviews whether a proposed development follows the city’s zoning code and writes the department’s official recommendation on what should be allowed; a community board is a real, local advisory body of residents that a city’s planning department reports to before a project moves forward. Priya’s recommendation memo becomes the department’s official position at Thursday’s meeting, and the board will hold her to whatever number she puts in it. Every parcel in the city belongs to a "),
        bold("zoning lot"),
        new TextRun(" — the legal unit of land zoning rules are applied to, which can be one parcel or several combined — and every zoning lot sits in a "),
        bold("zoning district"),
        new TextRun(", a designated area (like this case’s R7-2) with its own rulebook for how much can be built and how it must be arranged on the land."),
      ]),
      pRuns([
        new TextRun("The assemblage in question is three adjoining parcels on a block shaped, in part, by a diagonal avenue that predates the city’s numbered street grid — a real and common pattern in gridded cities, where an older diagonal road cuts through the rectangular blocks laid out later and leaves oddly angled, irregular parcels behind at every crossing (SEE APPENDIX A). All three parcels sit in an R7-2 residence district — in real NYC zoning, the letter and number (R7) name a whole family of similar residential districts allowing roughly the same building bulk, and the suffix (-2) picks out one specific variant within that family with its own exact FAR and yard numbers; this case only ever needs R7-2’s own two numbers, not the wider naming scheme — a real zoning designation that sets two rules load-bearing to this case (SEE APPENDIX B): a "),
        bold("floor area ratio (FAR)"),
        new TextRun(" — the maximum total interior floor area a building may contain, as a multiple of the lot’s own land area, so a building can legally contain more square feet of floor than the lot has square feet of land by building upward across multiple stories — and a "),
        bold("required yard"),
        new TextRun(": a strip of open land, measured a fixed depth in from a lot line, that a building is not allowed to occupy, so light and air reach the building and its neighbors. Concretely, a building’s total floor area equals its footprint (the part of the lot it’s actually allowed to build on) multiplied by the FAR; dividing that total floor area by the size of one typical apartment then gives the number of apartments the building could hold — that chain (footprint → floor area → apartment count) is exactly what Challenge 3’s D4 asks you to run for each option."),
      ]),
      pRuns([
        new TextRun("Priya has exactly two development paths available, and department policy requires she recommend one before Thursday. "),
        bold("Plat As-Is"),
        new TextRun(" keeps the three existing irregular parcels exactly as "),
        bold("platted"),
        new TextRun(" — “platted” means the parcel’s legal boundary lines are the ones already on file with the city, so no property lines change and the standard permit review — the ordinary process where the city checks a building application against the zoning rules already on the books before issuing a construction permit, with no separate ownership filing required first — can begin immediately. But each odd-shaped parcel loses a different amount of its own area to its required yard, because the required yard runs the full length of a parcel’s rear lot line — and a parcel with an unusual shape, especially a "),
        bold("concave"),
        new TextRun(" one with a notch cut into it, has more rear-lot-line length per square foot of area than a compact, regular shape does, so more of it falls inside the required-yard strip and cannot be built on (SEE APPENDIX C). "),
        bold("Replat & Consolidate"),
        new TextRun(" merges the three parcels into a single, larger rectangular zoning lot before anything can be built. Merging requires filing a "),
        bold("zoning lot merger"),
        new TextRun(" — a real, formal city process, filed with the planning department as a recorded legal document (the way a property deed is recorded), in which every current owner of the parcels being combined must sign an agreement — which adds real months to the timeline before construction can even start. But a single larger regular lot has proportionally less rear-lot-line length, so less of its area falls inside the required yard, and the design includes a public plaza that earns the project a real, city-recognized "),
        bold("floor-area bonus"),
        new TextRun(" — extra buildable floor area a city grants in exchange for the developer providing public open space (SEE APPENDIX D)."),
      ]),
      p("Department policy doesn’t just want the bigger eventual apartment count, though — it wants to know how much housing each option actually delivers within the city’s stated planning window. So the primary number Priya’s memo has to report is each option’s dwelling-unit-years: the number of apartments an option could eventually hold, multiplied by however many years remain in the planning horizon once that option’s own lead time to construction start is subtracted. A design that holds more apartments but starts months later doesn’t automatically win — it only wins if those extra apartments are worth more, over the years they’re actually available for people to live in, than the head start the other option gets from starting sooner."),
      p("For this case, treat every lot line that is not on the block’s front street as a rear lot line requiring the full yard depth — a simplification of the real, more detailed rules that classify a parcel’s lot lines, disclosed here rather than hidden (SEE APPENDIX F). Every figure in this case is either cited to a real source (SEE APPENDIX G) or disclosed as a stated Modeling Assumption (SEE APPENDIX F). The vocabulary and “how to…” skills this case will ask you to research are listed in Appendix H."),

      h1("Dilemma"),
      p("You are Priya Chandrasekaran."),
      p("Do you:"),
      pRuns([bold("A.) "), new TextRun("Recommend Plat As-Is — keep the three existing irregular parcels exactly as platted, so standard permit review can begin immediately OR")]),
      pRuns([bold("B.) "), new TextRun("Recommend Replat & Consolidate — merge the three parcels into one larger regular zoning lot, which needs a formal lot-merger process before anything can be built")]),

      h1("Challenges"),
      p("1.) Research and find an online resource that answers one of the “how to…” questions from the case study launch. Post a link to the resource as your submission."),
      p("2.) Post 250 or more “excellent” words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:"),
      p("    a.) Use of the “how to…” resource you researched in Challenge 1."),
      p("    b.) At least one original visual display of the data."),
      p("3.) Your pitch must include:"),
      pRuns([bold("D1 — A parcel classification table and one missing-angle calculation. "), new TextRun("Using Appendix C’s three parcel diagrams, classify each of the three “as-is” parcels using the terms Polygon, Irregular Polygon, Convex, and Concave — state which single parcel is concave and identify, by its listed vertex, where the notch is. Then, for Parcel L1, four of its five interior angles are given; use the sum-of-interior-angles theorem to calculate the fifth.")]),
      pRuns([bold("D2 — A buildable-footprint table for Plat As-Is (Option A). "), new TextRun("Using Appendix C’s parcel areas and rear-lot-line lengths and Appendix B’s required yard depth, calculate the required-yard area and the buildable footprint for each of the three parcels, then the combined buildable footprint and buildable-footprint percentage for the assemblage as a whole.")]),
      pRuns([bold("D3 — A buildable-footprint calculation and a plaza area for Replat & Consolidate (Option B). "), new TextRun("Using Appendix D’s consolidated-lot dimensions and rear-lot-line length, calculate its required-yard area, buildable footprint, and buildable-footprint percentage. Then, using Appendix D’s regular octagon plaza dimensions, calculate the plaza’s area using the regular-polygon area formula, and state whether it clears Appendix D’s cited minimum public plaza size.")]),
      pRuns([bold("D4 — A dwelling-unit-years comparison. "), new TextRun("Using Appendix B’s floor-area ratio and Appendix E’s average unit size, calculate the total number of dwelling units each option’s buildable footprint could realize. Then, using Appendix E’s lead-time figures and stated development planning window, calculate each option’s dwelling-unit-years delivered within the horizon, and the percent margin between them. State which option wins on these numbers.")]),
      pRuns([bold("D5 — A short written reflection. "), new TextRun("Using the term Population and what you found in Challenge 1’s research, explain in a short paragraph why cities end up with blocks shaped like this one, and whether you think Priya’s simplification in the Background (treating every non-front lot line the same way) is a reasonable one for a recommendation memo — or whether it’s the kind of shortcut that should worry the community board.")]),
      p("4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count."),
      p("5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 “excellent” words on the questions above."),

      h1("Appendix A — Why This Block Is Shaped Like This"),
      p("Referenced in Background and Challenge 3 (D5). Many gridded American cities have at least one older, diagonal road that predates the rectangular street grid laid over it later. Where that diagonal crosses the grid, it slices ordinary rectangular blocks into smaller, irregular pieces — triangles, trapezoids, and odd-angled parcels that were never intentionally designed, just left over. In Manhattan, this exact pattern — a pre-grid diagonal road (Broadway) crossing the 1811 street grid — produced some of the city’s most famous public spaces (Union Square, Madison Square, Herald Square, Times Square, Columbus Circle), all originally just the geometric leftovers where the angle met the grid, not planned civic space [S1]. This case’s assemblage is a constructed scenario built on that same real pattern, not a specific real address."),

      h1("Appendix B — Zoning Rules for This District"),
      p("Referenced in Background and Challenge 3 (D2, D3, D4). The assemblage sits in an R7-2 district, a real New York City residential zoning designation."),
      table(["Rule", "Value", "Applies to"], [
        ["Maximum residential floor area ratio (FAR), standard", "3.44", "Both options — total buildable floor area = FAR × buildable footprint (SEE APPENDIX D for this case’s simplification)"],
        ["Required rear yard depth", "30 feet, at every rear lot line", "Both options"],
      ], [3200, 2400, 3400]),

      h1("Appendix C — Option A: The Three “As-Is” Parcels"),
      p("Referenced in Background and Challenge 3 (D1, D2). All dimensions are for this case’s constructed scenario (SEE APPENDIX F)."),
      table(["Parcel", "Shape", "Area (sq ft)", "Front lot line (street)", "Rear/notch lot-line length requiring a yard", "Interior angles (°), in order around the parcel"], [
        ["L1", "Pentagon (convex)", "11,000", "80 ft", "40 ft", "90, 90, 141.3, 128.7, ? (Challenge D1)"],
        ["L2", "Hexagon (concave — two notch corners)", "7,900", "60 ft", "80 + 60 + 64 = 204 ft", "90, 77.5, 192.5, 90, 51.3, 218.7"],
        ["L3", "Pentagon (convex)", "11,100", "60 ft", "80 ft", "102.5, 90, 90, 90, 167.5"],
      ], [900, 2200, 1100, 1500, 1900, 1400]),
      p("How to read the “rear/notch lot-line length” column: for L1 and L3, this is the length of the single lot line farthest from the front street. For L2 — the concave parcel — this case treats the required yard as running along three lot lines: the one farthest from the front street, plus the two lot lines that form the inward notch, because a concave (re-entrant) lot line is treated the same way a real rear lot line is for the purposes of this assignment’s required yard (a simplification of the real, more detailed “inner court” open-space provisions many zoning codes apply to re-entrant building and lot shapes — SEE APPENDIX F). Working out each parcel’s required-yard area is a simple multiplication, not a geometric overlay: multiply each qualifying lot-line length by the 30 ft yard depth (Appendix B) and add those products together — you do not need to reason about whether the resulting yard strips physically overlap at a corner; this case’s model doesn’t require that level of geometric precision (SEE APPENDIX F, MA2)."),
      p("What L2 actually looks like, in words, for anyone working from the table alone: start at the left end of L2’s own 60 ft front lot line and walk the boundary clockwise. The first side runs back from the street; then, partway back, the boundary suddenly turns inward toward the center of the parcel instead of continuing outward — that’s the first notch corner, a reflex angle, meaning the parcel’s interior bends around it by more than a straight line (more than 180°). The boundary then runs across to a second point deeper inside the parcel’s own footprint, turns again — the second notch corner — and continues back out to the rear before closing the shape. The net effect is a six-sided lot shaped roughly like a wide “V” bitten out of one side of an otherwise ordinary lot: two of its six corners point in toward the parcel instead of out away from it, which is what “concave” means for a shape, and is also exactly why its total rear/notch lot-line length (204 ft, split across three separate boundary segments: 80 + 60 + 64) is so long relative to its 7,900 sq ft of area."),
      p("A picture of the three parcels and the consolidated lot, to scale, all dimensions in feet (front street runs along the bottom, y = 0):"),
      imageParagraph,
      p("L2’s two inward corners are the “notch” — the two extra lot-line segments Appendix C’s table adds to L2’s required-yard length. The right-hand panel shows Option B’s consolidated rectangular lot for comparison — the same total 30,000 sq ft of land, but with no concave notch and one straight rear lot line.", { size: 18, italics: true }),

      h1("Appendix D — Option B: The Consolidated Lot"),
      p("Referenced in Background and Challenge 3 (D3, D4). All dimensions are for this case’s constructed scenario (SEE APPENDIX F)."),
      table(["Figure", "Value"], [
        ["Consolidated lot dimensions", "200 ft (front) × 150 ft (depth)"],
        ["Consolidated lot area", "30,000 sq ft (same total area as the three “as-is” parcels combined)"],
        ["Rear lot-line length", "200 ft"],
        ["Required yard depth (SEE APPENDIX B)", "30 feet"],
      ], [4500, 4500]),
      p("The public plaza. The consolidation design includes a regular octagon plaza sited across the consolidated lot’s open, non-building area — overlapping the required-yard strip along the rear but, since the octagon’s own width (about 72 ft across) is wider than the 30 ft yard depth alone, extending into the surrounding open design as well, the way a real public plaza commonly combines a building’s required open space with additional voluntarily provided open area. Real New York City zoning recognizes a plaza like this with a floor-area bonus for developments that provide public plaza space [S2] — this case does not compute that bonus, and does not ask you to work out the plaza’s exact position on the lot, only whether the plaza’s own area (below) clears the minimum size."),
      table(["Plaza figure", "Value"], [
        ["Shape", "Regular octagon (8 equal sides)"],
        ["Side length", "30 ft"],
        ["Apothem (center-to-side distance)", "36.2 ft"],
        ["Real minimum public plaza area, New York City Zoning Resolution §37-712 [S2]", "2,000 sq ft"],
      ], [5500, 3500]),

      h1("Appendix E — Timeline and Housing Figures"),
      p("Referenced in Challenge 3 (D4). All figures in this appendix are disclosed Modeling Assumptions — see Appendix F, MA1–MA4."),
      table(["Figure", "Value", "Applies to"], [
        ["Average new-apartment unit size, this region", "714 sq ft/unit", "Both options (Appendix G, S3)"],
        ["Lead time to start of construction, Plat As-Is", "6 months", "Option A"],
        ["Lead time to start of construction, Replat & Consolidate", "18 months", "Option B"],
        ["City’s stated development planning window", "10 years (120 months)", "Both options"],
      ], [3800, 2800, 2400]),

      h1("Appendix F — Modeling Assumptions"),
      p("These figures are not published for this specific assemblage — no city publishes a specific block’s exact parcel geometry, lead times, or planning-horizon length as a general fact; those depend on the specific project. They are stated scenario assumptions chosen by the case author, at a scale consistent with a real mid-sized urban infill project — “infill” meaning new construction built on an already-developed city block, on land the city passed over the first time around, rather than on the undeveloped edge of a city. A Hero may challenge any of these numbers in discussion — that is a legitimate move.", { italics: true }),
      table(["#", "Assumption", "Value used", "Basis", "Sensitivity"], [
        ["MA1", "The three “as-is” parcels’ exact dimensions, areas, and shapes (Appendix C)", "As tabulated", "Constructed to be consistent with the real, cited pattern of irregular parcels formed where a diagonal road crosses a rectangular grid (Appendix A, S1) — not a specific real address’s surveyed parcel data.", "The whole comparison depends on these shapes; a different partition of the same 30,000 sq ft would change how much area each option loses to required yards."],
        ["MA2", "The simplified yard rule: every non-front lot line requires the yard, and a concave parcel’s notch lot lines are treated as also requiring it", "As applied in Appendix C", "Real zoning lot-line classification for irregular, multi-frontage parcels is materially more detailed than this case models (see Challenge D5) — this is a disclosed simplification chosen so the arithmetic is tractable at this grade band.", "This simplification affects both options in the same direction (irregular shapes lose more), so it is not the main driver of which option wins."],
        ["MA3", "Lead time to start of construction for each option", "6 months (A), 18 months (B)", "No public source publishes standard permit-review or lot-merger-filing timelines for a specific city; set to reflect that a lot-line merger genuinely requires additional real process (owner agreements, a replat filing) beyond standard permit review.", "Highly sensitive."],
        ["MA4", "The city’s stated development planning window", "10 years (120 months)", "No single “the” planning window exists across cities; many long-range housing plans use multi-year horizons in this general range. Set as a disclosed scenario dial.", "Highly sensitive — this is also exactly the lever the case’s discussion twist pulls."],
      ], [500, 2200, 1600, 3300, 1400]),

      h1("Appendix G — Sources"),
      table(["#", "Claim", "Value", "Source", "Date", "Confidence"], [
        ["S1", "A pre-grid diagonal road (Broadway) crossing Manhattan’s 1811 street grid created triangular and irregular parcels/plazas at its crossings, including Union Square, Madison Square, Herald Square, Times Square, and Columbus Circle", "as described", "Museum of the City of New York — Broadway and Its Bowties, The Greatest Grid", "accessed 2026-09-18", "HIGH"],
        ["S2", "Maximum residential floor area ratio for an R7-2 district (standard)", "3.44", "NYC Department of City Planning — Zoning Resolution §23-22", "accessed 2026-09-18", "HIGH"],
        ["S3", "Required rear yard depth in R7 and R8 residence districts", "not less than 30 feet", "NYC Department of City Planning — Zoning Resolution §24-36", "accessed 2026-09-18", "HIGH"],
        ["S4", "Minimum area of a public plaza that earns a zoning floor-area bonus", "not less than 2,000 sq ft", "NYC Department of City Planning — Zoning Resolution §37-712", "accessed 2026-09-18", "HIGH"],
        ["S5", "Average size of a new apartment unit, a real U.S. city (used as this case’s regional unit-size figure)", "714 sq ft/unit (Brooklyn, NY)", "RentCafe, citing Yardi Matrix — National Average Apartment Size report", "data as of 2026", "HIGH"],
      ], [500, 2700, 1600, 2600, 1000, 900]),
      p("Full source links:", { bold: true, size: 18 }),
      pRuns([new TextRun({ text: "S1 — ", size: 18 }), link("thegreatestgrid.mcny.org/greatest-grid/broadway-and-its-bowties", "https://thegreatestgrid.mcny.org/greatest-grid/broadway-and-its-bowties")], { spacing: { after: 40 } }),
      pRuns([new TextRun({ text: "S2 — ", size: 18 }), link("zr.planning.nyc.gov/article-ii/chapter-3/23-22", "https://zr.planning.nyc.gov/article-ii/chapter-3/23-22")], { spacing: { after: 40 } }),
      pRuns([new TextRun({ text: "S3 — ", size: 18 }), link("zoningresolution.planning.nyc.gov/article-ii/chapter-4/24-36", "https://zoningresolution.planning.nyc.gov/article-ii/chapter-4/24-36")], { spacing: { after: 40 } }),
      pRuns([new TextRun({ text: "S4 — ", size: 18 }), link("zoningresolution.planning.nyc.gov/article-iii/chapter-7/37-712", "https://zoningresolution.planning.nyc.gov/article-iii/chapter-7/37-712")], { spacing: { after: 40 } }),
      pRuns([new TextRun({ text: "S5 — ", size: 18 }), link("www.rentcafe.com/blog/rental-market/market-snapshots/national-average-apartment-size/", "https://www.rentcafe.com/blog/rental-market/market-snapshots/national-average-apartment-size/")], { spacing: { after: 120 } }),

      h1("Appendix H — “How To…” Math Questions To Research"),
      h2("Vocabulary terms"),
      bullet("Polygon"), bullet("Irregular Polygon"), bullet("Convex"), bullet("Concave"), bullet("Regular Polygon"),
      bullet("Sum of the interior angles of a polygon theorem"), bullet("Octagon"), bullet("Area"), bullet("Perimeter"),
      bullet("Ratio"), bullet("Proportion"), bullet("Population"),
      h2("“How to…” questions"),
      bullet("How to find the measure of an interior angle of a polygon given the other angles"),
      bullet("How to find the area of a regular polygon"),
      bullet("How to find the percent of a number"),
    ],
  }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(__dirname + "/published/The Odd Lot - Case Study.docx", buf);
  console.log("wrote docx", buf.length, "bytes");
});
