# Learning Goal Check — Wind Call

Bidirectional deliverable ↔ skill matrix. "Forces" test applied to every row: *could a competent
student produce this deliverable correctly without ever performing this skill?* If yes, the
mapping is fake.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 wind-triangle vector diagram | pre-calculus-vector, pre-calculus-magnitude-of-a-vector, pre-calculus-how-to-find-the-magnitude-and-direction-of-a-vector, pre-calculus-how-to-add-and-subtract-vectors |
| D2 wind-component table (dot product) | pre-calculus-dot-product, pre-calculus-how-to-find-the-dot-product-of-two-vectors, pre-calculus-unit-vector |
| D3 groundspeed and heading table | geometry-pythagorean-theorem, geometry-hypotenuse |
| D4 flight-time and fuel-burn table | measurement-how-to-find-elapsed-time, measurement-how-to-convert-an-amount-with-compound-units |
| D5 gallons-per-nautical-mile comparison | measurement-how-to-convert-an-amount-with-compound-units |

## Forces-test notes

- **D1** cannot be produced without plotting the true-airspeed vector and the wind vector as
  vectors (not scalars) and adding them tip-to-tail to find the resultant — a student who just
  writes down two speeds has not done this deliverable. Magnitude and direction of the resultant
  require the magnitude/direction how-to directly.
- **D2** cannot be produced without the dot product: decomposing a wind vector into a component
  along a given course direction and a component perpendicular to it is the textbook application
  of `wind · unit_course`. A student who "eyeballs" a headwind/tailwind guess has not shown this
  work, which the deliverable explicitly requires ("shown as work").
- **D3** requires resolving the resultant groundspeed. Once the wind's cross-course component and
  the wind-correction angle are known (D2), finding the resultant's magnitude uses the
  Pythagorean/right-triangle relationship between the along-course and cross-course legs — this is
  the same reasoning the Turbine Channel case uses for cylinder geometry, applied here to a
  velocity triangle instead of a shape.
- **D4** requires converting a distance (nm) and a rate (kn = nm/hr) into an elapsed time, and then
  an elapsed time (hr) and a rate (gal/hr) into a fuel total (gal) — two chained compound-unit
  conversions, not a single lookup.
- **D5** requires dividing the D4 fuel total by the fixed route distance for each altitude and
  comparing the two ratios — the primary metric itself, which is a compound-unit quantity
  (gal/nm).

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 11    new_coverage: 0 (reinforcement_note, see case.json)
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```
