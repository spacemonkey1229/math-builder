const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType,
} = require("docx");

const NAVY = "1a3a5c";

function h1(text) { return new Paragraph({ text, heading: HeadingLevel.HEADING_1, spacing: { before: 300, after: 150 } }); }
function h2(text) { return new Paragraph({ text, heading: HeadingLevel.HEADING_2, spacing: { before: 240, after: 100 } }); }
function p(text, opts = {}) { return new Paragraph({ children: [new TextRun({ text, ...opts })], spacing: { after: 120 } }); }
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

const doc = new Document({
  styles: { default: { document: { run: { font: "Calibri", size: 22 } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1000, bottom: 1000, left: 1100, right: 1100 } } },
    children: [
      new Paragraph({ children: [new TextRun({ text: "Facilitator Guide: The Odd Lot", bold: true, size: 40, color: NAVY })], spacing: { after: 80 } }),
      p("FACILITATOR ONLY — contains the balance argument, the margin, and the trap. Do not distribute to Heroes.", { bold: true, color: "a3312a" }),
      p("Case: The Odd Lot  ·  Tier: T3 (MS-stretch / HS-entry)  ·  Studio: Adventure  ·  Primary metric: dwelling-unit-years delivered within the planning horizon  ·  Base margin: 5.89% (fragile — see the sensitivity note before Lessons Learned)"),
      p("Standards: Polygon, Irregular Polygon, Convex, Concave, Regular Polygon, Sum of the interior angles of a polygon theorem, How to find the measure of an interior angle of a polygon given the other angles, How to find the area of a regular polygon, Octagon, Area, Perimeter, Ratio, Proportion, How to find the percent of a number, Population (see case.json.standards[])."),

      h1("The Balance Argument (Answer Key — Facilitator Only)"),
      p("Argument for A (Plat As-Is): Plat As-Is wins if the planning horizon is short enough that Option B’s extra 12 months of lead time erases more housing-supply value than its larger eventual unit count adds back — and a real, disclosed scenario (the twist) shows that threshold is not hypothetical: a housing-production deadline moved up from 10 years to 5 years flips the winner outright, because B’s units simply don’t have as many years left in the (now shorter) window to count."),
      p("Argument for B (Replat & Consolidate): Replat & Consolidate wins on the city’s stated 10-year planning horizon (5.89% margin) because a single larger, regular zoning lot loses proportionally less area to the required yard than three small irregular parcels do — especially the concave one — so it realizes about 18% more buildable footprint and, at the same FAR, meaningfully more total dwelling units; over a long enough horizon that extra density outweighs the 12-month process delay."),
      p("Margin at the city’s base 10-year horizon: 5.89%, Replat & Consolidate (B) wins.", { bold: true }),
      p("The Trap: most learners will assume that because Option B’s buildable percentage (80%) is clearly higher than Option A’s (67.6%), Option B is simply the better plan, full stop — treating the buildable-footprint comparison (D2/D3) as if it were the final answer instead of one input into D4. The real trap is that D4’s dwelling-unit-YEARS metric also depends on when the units arrive, not just how many there eventually are — and a learner who stops at “B has more square footage” without running the lead-time and horizon arithmetic will miss that the two options are genuinely close, and could even reach the wrong winner if the horizon were shorter than they assumed."),

      h1("Facilitator Notes"),
      h2("Intro"),
      p("Heroes, Priya has one memo due Thursday and three oddly-shaped parcels nobody designed on purpose. One option changes nothing and starts building next month. The other option is a better shape on paper but needs three property owners to agree to something first. There’s no answer to hand them either — that’s what the numbers are for."),
      h2("Launch"),
      p("Show a map or satellite image of any city block where a diagonal street cuts through a rectangular grid (Broadway through Manhattan works well — Union Square, Madison Square, Times Square are all real examples). Ask: “Why do you think this block is shaped like a wedge instead of a rectangle? Who do you think decided that?” Let them guess. Then: “Nobody did. That’s the whole problem Priya has to solve.” Ask each Hero: Plat As-Is, or Replat & Consolidate? Commit out loud."),
      h2("Anchor 1 — Take a stand and vote"),
      p("Plat As-Is (A) or Replat & Consolidate (B). No reasoning yet. Hands up for A. Hands up for B. Write the split on the board. “Is anyone courageous enough to stand with ______?”"),
      h2("Anchor 2 — What is the problem we’re solving?"),
      p("Do not let them start calculating yet. What’s the actual question, in one sentence? Is it “which option builds more apartments”? Is it “which option is fastest”? Is it “which option delivers the most total housing, counted over time, given the city has a deadline”? Those sound similar and are not the same question — only the last one is what this case’s numbers actually measure. Someone will say “obviously consolidate, one big regular lot is always more efficient than three weird ones.” Push: “More efficient at what — building footprint, or delivering housing by a real deadline? Does merging three lots cost anything besides paperwork?” This is where the trap above lives — let the confusion grow, do not rescue them."),
      h2("Anchor 3 — What is the process?"),
      p("What’s the process we’ll go through to answer it? If we calculate buildable footprint for each option, are we done? Is that the same question as “how much housing does each option actually deliver by some real deadline”? If we end up with two numbers like 928 and 983 unit-years, how do we decide that’s close enough to be a real discussion, versus one option just winning? What’s our tiebreaker before we see the numbers?"),
      h2("Anchor 4 — What don’t we know?"),
      p("What’s missing that we’d need to answer this properly? Appendix F gives you the assumptions behind the lead times and the planning horizon. Do you believe them? Have them actually try a longer and a shorter horizon and see how much the comparison moves. What are we assuming stays fixed about the city’s own housing deadline between now and when either option finishes construction? (This is the case’s built-in opening for the twist — don’t tip it.)"),
      h2("Data Deep Dive"),
      p("Step 1 — classify the parcels and find L1’s missing angle (D1). L1 (pentagon, convex): 90 + 90 + 141.3 + 128.7 + ? = 540° (pentagon interior angle sum, (5−2)×180). Missing angle = 90°. L2 is the concave parcel — two of its six interior angles are reflex (greater than 180°): 192.5° and 218.7°, at the two corners where the diagonal cut notches inward."),
      table(["Parcel", "Area", "Rear/notch length", "Required yard (× 30 ft)", "Buildable"], [
        ["L1", "11,000", "40 ft", "1,200", "9,800"],
        ["L2 (concave)", "7,900", "204 ft (80+60+64)", "6,120", "1,780"],
        ["L3", "11,100", "80 ft", "2,400", "8,700"],
        ["Total", "30,000", "", "9,720", "20,280 (67.6%)"],
      ], [1800, 1400, 2200, 2000, 1600]),
      p("Push the room directly: “L2 is less than 27% of the total land area, but it loses over 63% of its own area to the required yard. Why does the concave shape cost it so much more?” (Answer: its notch creates two extra lot lines that this case’s rule also treats as requiring the yard — the more edges a shape’s boundary has facing away from the street, the more of it a fixed-depth yard eats into.)"),
      p("Step 3 — buildable footprint, Option B, and the plaza (D3). Consolidated lot: 30,000 − (200 × 30) = 30,000 − 6,000 = 24,000 sq ft (80%). Octagon plaza: perimeter = 8 × 30 = 240 ft; area = ½ × 240 × 36.2 = 4,344 sq ft, well clear of the real 2,000 sq ft minimum."),
      p("Step 4 — dwelling units and unit-years (D4). Units A = 20,280 × 3.44 ÷ 714 ≈ 97.7. Units B = 24,000 × 3.44 ÷ 714 ≈ 115.6. Unit-years A = 97.7 × (120 − 6) / 12 ≈ 928.2. Unit-years B = 115.6 × (120 − 18) / 12 ≈ 982.9."),
      p("Replat & Consolidate wins by 5.89% — comfortably inside the 20% balance cap, but not by much.", { bold: true }),

      h1("Twist — drop this at ~15 minutes into the discussion"),
      p("Deliver it slowly. Let each piece land. “The mayor’s office just announced it.” (pause) “The city’s housing plan isn’t a ten-year horizon anymore. It’s five.” (pause) “Every unit that doesn’t exist yet in five years doesn’t count toward the target — no matter how good the design is.” (pause) “And it applies to every project that hasn’t broken ground yet — including one already mid-filing on the old timeline. There’s no grandfathering for a zoning lot merger already in progress, and no partial credit for time already spent on it either — every option’s own lead time still counts in full, measured from today, regardless of how far along it already was.”"),
      p("Those last two lines are deliberate, not filler — they close off two real objections a sharp Hero will otherwise raise, in order. First: in actual zoning practice, a project already filed before a deadline change is sometimes exempted (a “vested rights” argument) — say “no grandfathering” so nobody argues Option B’s already-underway merger buys it an exemption from the shortened horizon. Second, and easier to miss: even once a Hero accepts the deadline applies to Option B, “already mid-filing” invites a natural but wrong follow-up — that if the merger is already halfway done, only the remaining lead time (not the full 18 months) should count against the new, shorter clock. It should not: sensitivity_model.py’s evaluate_twist() still charges B’s full stated lead_B (18 months) against the shortened horizon, with no credit for partial progress. Say the “no partial credit” line explicitly, or a room that runs the math with a discounted lead time may reach a different unit-years total for B and not see the winner flip at all — solved out, giving B even 9 of its 18 months of “credit” already spent reverses the flip back to B (491.4 vs. 439.7 unit-years)."),
      p("Facilitator only — read before you drop this, do not read aloud: horizon drops from 120 to 60 months. Unit-years A = 97.7 × (60−6)/12 ≈ 439.7. Unit-years B = 115.6 × (60−18)/12 ≈ 404.7. The winner flips to Plat As-Is, by 8.64%. Confirm a room that gets there against these numbers, not just the logic — B’s extra 18 units no longer have enough years left in the shorter window to outweigh its 12-month head start disadvantage.", { italics: true }),
      p("Now: “Sixty seconds. Are you changing your recommendation — or not?”"),

      h2("Immediate recommit"),
      p("Who is not changing? Why? Who is reconsidering, even if they’re not flipping? What just broke in your original model? Were you wrong — or were you just missing information? (Sit on this one.) Who built their case entirely on “80% beats 67.6%” without ever running D4’s timeline arithmetic?"),

      h1("Deep Conflict — Threads (20–30 min)"),
      p("Thread 1 — Efficiency vs. speed. Option B is the better shape on paper; Option A is faster to start. “If Option B is simply the more efficient design, why does it ever lose?” Push toward: a better design that arrives too late doesn’t out-produce a worse design that’s already running, within a bounded window — efficiency and speed are genuinely different currencies, and the horizon length is the exchange rate between them."),
      p("Thread 2 — Fragility to a single number. All three timeline dials (Appendix F, MA3–MA4) are disclosed assumptions with no real public source behind them. Flex lead_B or horizon by 50% in either direction, and the winner flips (see case.json’s sensitivity_disclosure — do not read this section aloud, but use it to steer questions). “Which option would you put your name on if the mayor’s office changed the deadline again next year?”"),

      h1("Five Socratic Questions"),
      p("1. Option B’s buildable footprint (80%) clearly beats Option A’s (67.6%) — why isn’t that the whole answer?"),
      p("2. If we end up with two unit-year totals like 928 and 983, how close is “close” before you’d call this a real toss-up rather than one option clearly winning?"),
      p("3. None of the three timeline assumptions (Appendix F, MA3–MA4) come from a published source for this exact city — which single one, if it moved, would worry you the most, and why?"),
      p("4. L2 is less than 27% of the assemblage’s total land, but loses over 63% of its own area to the required yard — what does that tell you about how a fixed-depth yard interacts with a concave shape specifically?"),
      p("5. Replat & Consolidate wins on the base 10-year horizon by 5.89% — but two of the three timeline assumptions flip the winner at a plausible ±50% swing, and a realistic policy change (the twist) flips it for real. Is a 5.89% margin built on assumptions this shaky a “real” win?"),

      h1("Sensitivity Note (boxed — read before Lessons Learned)"),
      p("Base margin (5.89%) is a direct, computable function of the three disclosed Modeling Assumption dials (MA3’s two lead times, MA4’s horizon) via sensitivity_model.py. lead_A is the least load-bearing: flexing it ±50% narrows or widens B’s win (3.17% to 8.75%) but never flips the winner or breaches the cap. lead_B is one of the two most load-bearing: +50% (to 27 months) flips the winner to A at 3.58%; −50% (to 9 months) widens B’s win to 15.23%, still within cap. horizon is a disclosed scenario dial with no single universal real value: +50% (to 15 years) widens B’s win to 10.18%; −50% (to 5 years) flips the winner to A at 8.64% — this is also exactly the lever the twist pulls, deliberately, so a facilitator can connect the twist directly back to this disclosure. No flex breaches the SPEC §2 20% cap in either direction — a comparatively stable case relative to its sibling (The Cold Hit), disclosed honestly either way. No SPEC §6 subject-matter sensitivity applies; this is a zoning/housing-capacity planning decision with no death, illness, or family-hardship stakes."),

      h1("What a Strong Defense Sounds Like"),
      p("Not an answer key — a Hero defending either option well will do more than compare the two buildable-footprint percentages and stop. A weaker defense says “B has 80% buildable versus A’s 67.6%, so B wins” and never runs the timeline arithmetic at all. A strong defense runs the full chain: buildable footprint (D2/D3) into dwelling units via FAR and average unit size, into dwelling-unit-years using each option’s own lead time against the stated planning horizon (D4), and only then states a winner and a margin. A strong defense also names which timeline assumption its answer is most sensitive to, and addresses the twist directly — acknowledging that Replat & Consolidate’s win is real on the city’s numbers and also genuinely fragile to a plausible shortened deadline — rather than picking a side and ignoring the disclosed uncertainty."),

      h1("Cohort Bands"),
      table(["Band", "What changes"], [
        ["Full (12-20)", "Socratic plan runs as written. Anchor 1 vote is a real show-of-hands split worth reading; both deep-conflict threads run."],
        ["Compressed (6-11)", "Combine Anchor 2 and Anchor 3 into one pass. Run only the sharper deep-conflict thread (the horizon-length fragility) at 20:00-30:00. Twist still drops at 15:00. Total runtime ~30 min."],
        ["1:1 or pair (1-2)", "No vote at Anchor 1 — the learner states an initial position instead. The guide argues the other side directly rather than cold-calling. The twist still lands; ‘who reverses’ becomes ‘would you reverse, and why’. Skip the deep-conflict threads; go straight from twist-recommit to Close."],
      ], [2600, 6400]),

      h1("45-Minute Socratic Plan"),
      table(["Time", "Move"], [
        ["0:00-3:00", "Cold-call launch. “Thirty seconds — as-is, or consolidate?” Two or three learners, fast. Stand/sit vote, no explanation yet."],
        ["3:00-10:00", "Position defense (pre-twist). “Convince us it’s better, not just bigger-sounding.” · “What’s your actual dwelling-unit-years number — not a guess.”"],
        ["10:00-15:00", "Pressure-test the models. “Which option is more fragile to one wrong timeline estimate?” · “What single number does your option depend on most?”"],
        ["15:00", "DROP THE TWIST. Slowly, with pauses. Finish with: “Sixty seconds. Are you changing your recommendation — or not?”"],
        ["15:00-20:00", "Immediate recommit. Who reverses? “What just broke?”"],
        ["20:00-30:00", "The two threads: efficiency vs. speed · fragility to a single assumption."],
        ["30:00-45:00", "Close, re-vote, reflection, lessons learned."],
      ], [1800, 7200]),

      h1("Close"),
      p("Vote again. Compare to the Anchor 1 board. Who moved? We asked ______ as our key question — was it the right one? What math was new to you here, and how did you attack it? If you got a case like this again, what would you check first?"),

      h1("Lessons Learned"),
      p("The arithmetic has a clean structure: a fixed-depth required yard eats into an irregular, especially concave, shape’s area far more than it does a compact regular one, but “more buildable footprint” and “more housing delivered by a real deadline” are not automatically the same question once a process delay enters the picture. Replat & Consolidate’s win (5.89%) is real on the city’s stated 10-year horizon, and it is also fragile — two of the three underlying timeline assumptions flip the winner at a plausible ±50% swing, and a realistic policy change (a shortened housing deadline) is enough to flip it for real. That is a disclosed, not eliminated, sensitivity — case.json.sensitivity_disclosure[] carries a Category-F entry for every timeline dial, because none of them can be tightened by more research; they are genuine planning unknowns no public source measures for a specific hypothetical project."),
      p("A facilitator running this room should say plainly what the case says: Replat & Consolidate wins on the numbers as modeled, that win is real, and it is also genuinely fragile to several disclosed assumptions and to a realistic policy shift — both things are true at once, and naming both is stronger than picking one."),

      h1("Skills This Case Exercises"),
      p("Polygon · Irregular Polygon · Convex · Concave · Regular Polygon · Octagon · Area · Perimeter · Ratio · Proportion · Population · Sum of the interior angles of a polygon theorem · How to find the measure of an interior angle of a polygon given the other angles · How to find the area of a regular polygon · How to find the percent of a number — name these explicitly in debrief so learners connect tonight’s decision back to the vocabulary from Appendix H."),
    ],
  }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(__dirname + "/published/The Odd Lot - Facilitator Guide.docx", buf);
  console.log("wrote docx", buf.length, "bytes");
});
