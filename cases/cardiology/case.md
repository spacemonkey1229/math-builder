# Case Study: Cardiology

MS | Math | Case Study | 2026-27 | Heroes Academy

---

## Overview

"Your afternoon appointment is here," pages Wendy. "Thank you, I'll come out and meet them," replies Dr. Zeke Hotchkiss. He walks to the lobby and greets Cindy and Paul. "It's good to see you this morning, thank you for coming in." "Good to see you too," Paul responds. "Let's head down to my office so we can chat."

Dr. Hotchkiss leads the couple to his office, where they sit down around a coffee table. "We have your lab results, and we're here to discuss treatment options for your coronary artery disease, Paul," the doctor starts. "There are essentially two therapy options we could pursue. I'll share the pros and cons of each and give you my recommendation."

Paul nods slowly. He's been dreading this appointment for weeks, ever since the angiogram, ever since the words "coronary artery disease" first came up in a hallway conversation he wasn't ready for. Cindy reaches for his hand under the table, the way she always does before hard news.

"I want you to understand both paths clearly before you decide anything," Dr. Hotchkiss continues. "One is medication, managed carefully, for as long as it keeps working. The other adds surgery on top of that medication. Neither one is automatically right for every patient who walks through that door — but for you specifically, the numbers point somewhere. Let's walk through them together."

Whatever Dr. Hotchkiss recommends today, Paul is the one who has to live with it — literally. Cindy squeezes his hand once, and the room goes quiet as the doctor reaches for the folder on his desk.

---

## Background

Dr. Zeke Hotchkiss has worked as a cardiologist for over a decade at the Denver Health Medical Center, consulting with over 1,700 patients over his career. He has participated in several research studies on cardiovascular disease and treatment, including a recently-completed landmark study run by Duke University comparing two therapies for patients with coronary artery disease (CAD) — **SEE APPENDIX A**.

The study compared two therapies: **medication only (MT)**, and **medication plus coronary artery bypass graft surgery (CABG)**. Both treat CAD — specifically, congestive heart failure caused by a prior heart attack.

One detail Paul and Cindy don't know: the medication used in MT is made by a pharmaceutical company that has an affiliate agreement with Dr. Hotchkiss's office, paying it 0.97% of every sale of the medication his office prescribes. The CABG surgery is performed through a different office, from which Dr. Hotchkiss's office receives no referral benefit, and the follow-up medication used after CABG surgery is a different drug, unaffected by the agreement. This is disclosed here as real background, not a number the case's math turns on — it's the kind of fact a careful advisor discloses to a patient regardless of whether it changes the recommendation.

**Paul Cadenson** is a 57-year-old with no previous cardiovascular treatment. His history includes pre-diabetes, Class I obesity, a family history of premature CAD, and daily tobacco use. An angiogram showed 98% occlusion of his left coronary artery. His full lab profile is in **APPENDIX B**.

Exactly how to compute Paul's Ejection Fraction, and how each therapy's costs are modeled year over year, are fixed in **APPENDIX D** — use those conventions, or your numbers won't match anyone else's.

The vocabulary and the "how to…" skills this case will ask of you are listed in **Appendix F** — that is where Challenge 1 sends you. Curious about the real medicine behind this case, beyond the math? **SEE APPENDIX E** for further reading.

---

## Dilemma

You are Dr. Hotchkiss.

Do you:

**A.)** Recommend the medical treatment only (MT) therapy **OR**

**B.)** Recommend the medical treatment + CABG therapy

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — Paul's 5-year survival rate for each therapy**, from the real trial results (Appendix A), and how much higher CABG's survival rate is than MT's, in percentage points.
- **D2 — Paul's Ejection Fraction**, computed from his own stroke volume and end-diastolic volume (Appendix B), expressed as a percent.
- **D3 — Paul's total expected expenses for each therapy**, after Year 1, Year 2, Year 3, Year 4, and Year 5 (Appendix C).
- **D4 — The slope and y-intercept of each therapy's 5-year cost line** from your Year 1-5 totals, and what each one means for Paul in plain English.
- **D5 — A recommendation** weighing survival rate, Ejection Fraction, and total cost.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A: The STICH Trial — Real Outcomes at ~5 Years

**Study:** Comparison of Surgical and Medical Treatment for Congestive Heart Failure and Coronary Artery Disease (ClinicalTrials.gov Identifier: **NCT00023595**). **Sponsor:** Duke University. **Collaborator:** National Heart, Lung, and Blood Institute.

The study randomized patients with CAD, reduced heart function, and congestive heart failure to medical therapy only (MT) or medical therapy plus bypass surgery (CABG), and tracked all-cause mortality over time. The trial's own design only compared MT and CABG — it did not include a stenting (angioplasty) arm, because it specifically enrolled patients whose disease pattern made them candidates for bypass surgery. This case follows the trial's own real comparison and does not introduce a third option the trial itself never tested.

| Follow-up | MT mortality | CABG mortality |
|---|---|---|
| ~5 years (primary report, median follow-up 56 months) | 41% | 36% |

---

## Appendix B: Paul Cadenson — Patient Profile

57-year-old male. Pre-diabetes (HgA1C 6.4). Class I obesity (BMI 31). Family history of premature CAD. Daily tobacco smoker (1/2 pack/day for 35 years). Blood pressure 145/60 at his last two visits. Angiogram showed 98% occlusion of the left coronary artery. E/A ratio at his last two lab visits: 2.47 and 2.468.

**Stroke Volume (SV): 72.5 mL. End-Diastolic Volume (EDV): 228.6 mL.**

---

## Appendix C: Treatment Cost Figures

The original case materials did not include cost data, so the figures below are a disclosed, stated modeling convention, not sourced from the original trial.

**Medication Only (MT):** $450 per month, every month, for as long as Paul is on the therapy.

**Medication + CABG:** a one-time surgery cost of $85,000 in Year 1, plus $150 per month in follow-up medication starting immediately.

---

## Appendix D: Modeling Assumptions

**Assumption 1 — Ejection Fraction.** Ejection Fraction is calculated as Paul's stroke volume divided by his end-diastolic volume (Appendix B), expressed as a percent: EF = SV / EDV.

**Assumption 2 — Cost figures.** Appendix C's cost figures are a disclosed modeling convention (see Appendix C), not data from the original trial. Treat MT as a flat $450/month with no cost in Year 0. Treat CABG as a one-time $85,000 charge that lands entirely in Year 1, plus $150/month in follow-up medication starting in Year 1 and continuing every year after.

**Assumption 3 — Cumulative cost as a line.** Each therapy's cumulative cost, plotted against the year number (1 through 5), forms a straight line: cost = (yearly rate) x (year) + (fixed cost, if any). The yearly rate is the line's slope; the fixed cost that doesn't depend on the year is its y-intercept.

---

## Appendix E: Learn More

Beyond the math, this case is grounded in real cardiology. Here's where to go if you want to understand the medicine, not just the numbers:

- [Coronary Artery Bypass Grafting (NHLBI, NIH)](https://www.nhlbi.nih.gov/health/coronary-artery-bypass-grafting) — the National Heart, Lung, and Blood Institute's official explainer on what CABG surgery is, how it's performed, and what recovery looks like.
- [Ejection Fraction: An Important Heart Measurement (Cleveland Clinic)](https://my.clevelandclinic.org/health/articles/16950-ejection-fraction) — a plain-language explanation of what ejection fraction measures and why it matters for heart failure patients like Paul.
- [Coronary Artery Disease (MedlinePlus, U.S. National Library of Medicine)](https://medlineplus.gov/coronaryarterydisease.html) — an overview of CAD, its causes, risk factors (including the ones Paul has: pre-diabetes, obesity, family history, tobacco use), and treatment options.
- [Comparison of Surgical and Medical Treatment for Congestive Heart Failure and Coronary Artery Disease — NCT00023595 (ClinicalTrials.gov)](https://clinicaltrials.gov/study/NCT00023595) — the official registry record for the real STICH trial this case's Appendix A data comes from, including its full design and Duke University/NHLBI sponsorship.

---

## Story Vocabulary — Cardiology & Clinical-Trial Terms

This case also uses real cardiology and clinical-trial vocabulary you may not have met in a math
class. These terms appear in the Background, Appendices A-D, and Appendix E above; each is defined
here in plain English, with a real source if you want to read further. This is separate from the
math vocabulary in Appendix F.

- **Angiogram** — an X-ray procedure that uses a special dye to make blood vessels visible, often
  used to find blockages in the arteries that supply the heart; the test that showed Paul's 98%
  occlusion. [MedlinePlus, Coronary angiography](https://medlineplus.gov/ency/article/003876.htm)
- **Ejection Fraction** — a measurement of how much blood the heart's main pumping chamber pushes
  out with each beat, expressed as a percent. A healthy heart usually pumps out more than half of
  the chamber's blood each beat. [Cleveland Clinic, Ejection Fraction](https://my.clevelandclinic.org/health/articles/16950-ejection-fraction)
- **Coronary Artery Disease** — a condition in which the arteries that supply blood to the heart
  become narrowed, usually by a buildup of fatty deposits, which can reduce the oxygen the heart
  muscle receives; the condition Paul has. [MedlinePlus, Coronary Artery Disease](https://medlineplus.gov/coronaryarterydisease.html)
- **Congestive Heart Failure** — a condition in which the heart cannot pump blood as well as it
  should, so blood and fluid can back up in the body. It does not mean the heart has stopped — it
  means it isn't pumping efficiently enough. [NHLBI, Heart Failure](https://www.nhlbi.nih.gov/health/heart-failure)
- **Coronary Artery Bypass Graft (CABG)** — a surgery that reroutes blood around a blocked section
  of a coronary artery using a healthy blood vessel taken from elsewhere in the body, restoring
  blood flow to the heart muscle; the CABG option in Paul's Dilemma. [NHLBI, Coronary Artery Bypass Grafting](https://www.nhlbi.nih.gov/health/coronary-artery-bypass-grafting)
- **Occlusion** — a blockage or narrowing of a blood vessel; Paul's angiogram found 98% occlusion of
  his left coronary artery, meaning it was almost completely blocked, usually by a buildup of fatty
  plaque. [NHLBI, Atherosclerosis](https://www.nhlbi.nih.gov/health/atherosclerosis)
- **Stroke Volume** — the amount of blood the heart's main pumping chamber ejects with a single
  heartbeat; one of the two numbers (with End-Diastolic Volume) used to compute Paul's Ejection
  Fraction. [NCBI Bookshelf, Physiology, Stroke Volume](https://www.ncbi.nlm.nih.gov/books/NBK547686/)
- **End-Diastolic Volume** — the amount of blood filling the heart's main pumping chamber right
  before it contracts; the chamber's "full" volume, used with Stroke Volume to compute Ejection
  Fraction. [NCBI Bookshelf, Physiology, Stroke Volume](https://www.ncbi.nlm.nih.gov/books/NBK547686/)
- **HgA1C** — a blood test (also written A1C) that measures average blood sugar over about three
  months, used to diagnose and monitor pre-diabetes and diabetes; Paul's result of 6.4 is in the
  pre-diabetes range. [NIDDK, The A1C Test & Diabetes](https://www.niddk.nih.gov/health-information/diagnostic-tests/a1c-test)
- **Body Mass Index (BMI)** — a number calculated from height and weight, used as a screening
  estimate of body fat. Doctors group higher BMI values into classes; Paul's BMI of 31 falls in the
  "Class I obesity" range. [MedlinePlus, Body Mass Index](https://medlineplus.gov/ency/article/007196.htm)
- **All-Cause Mortality** — death from any cause, not just the condition being studied; the STICH
  trial tracked all-cause mortality so the comparison couldn't be skewed by how a death got labeled.
  [NCI Dictionary of Cancer Terms, all-cause mortality](https://www.cancer.gov/publications/dictionaries/cancer-terms/def/all-cause-mortality)
- **Randomized** — in a clinical trial, assigning patients to a treatment group purely by chance, so
  the groups being compared start out similar; how the STICH trial assigned patients to MT or CABG.
  [NIH RaDaR, Randomized controlled trial](https://registries.ncats.nih.gov/glossary/randomized-controlled-trial/)
- **Blood Pressure** — written as two numbers, e.g. 145/60: the first (systolic) is the pressure in
  the arteries when the heart beats; the second (diastolic) is the pressure when the heart rests
  between beats. [MedlinePlus, High blood pressure in adults](https://medlineplus.gov/ency/article/000468.htm)
- **E/A Ratio** — a measurement from a heart ultrasound comparing two phases of how the heart's
  chamber fills with blood between beats; one of several lab values in Paul's profile beyond what
  the Challenges require. [Wikipedia, E/A ratio](https://en.wikipedia.org/wiki/E/A_ratio)
- **Affiliate Agreement** — a financial arrangement in which a doctor's office receives payment tied
  to sales of a specific product; disclosed here because a patient deserves to know about a
  financial interest that could affect a recommendation, even one that doesn't change the
  underlying math. [NCBI Bookshelf, Conflicts of Interest and Medical Practice](https://www.ncbi.nlm.nih.gov/books/NBK22944/)
- **Premature CAD** — coronary artery disease that shows up unusually early in life; research
  studies commonly define it as CAD before about age 55 in men or 65 in women. Paul's family
  history of premature CAD means a close relative was diagnosed at an unusually young age, which
  raises his own risk. [NIH/NCBI, Pathogenesis of premature coronary artery disease](https://pmc.ncbi.nlm.nih.gov/articles/PMC8843894/)

---

## Appendix F: "How To…" Math Questions To Research

**Vocabulary**

Percent · Ratio · Slope

**How to…**

- How to convert numbers to percents
- How to multiply decimal numbers
- How to add decimal numbers
- How to identify the slope of a line given a set of data, or a graph of a line of a set of data, or its linear equation
- How to compare two or more values

---

<!-- FACILITATOR ONLY -->

## Facilitator-Only: STICH Extended Follow-Up (10-Year)

Not needed for Challenges 1–5 — D1 only asks for the 5-year figures in Appendix A above. This
section holds the real, sourced 10-year data back from the student-facing read (everything above
the `<!-- FACILITATOR ONLY -->` marker is what a student sees) so the Twist is an actual reveal
in discussion, not a repeat of a number already sitting in the packet. See FACILITATOR.md's Twist
section for when and how to bring it into the room.

**STICHES extension (Velazquez et al., NEJM 2016, DOI 10.1056/NEJMoa1602001, median follow-up 9.8
years):** MT mortality 66.1%, CABG mortality 58.9% (p=0.02, statistically significant — case.json
source S2).
