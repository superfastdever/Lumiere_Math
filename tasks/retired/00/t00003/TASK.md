# Task t00003 draft package

Subdomain: Geometry & Topology
Target failure modes: geometric relation error (primary), figure-based quantitative estimation (secondary)
Image: `figure.png`, self-authored with matplotlib, opaque RGB PNG, 2044 x 1682.
Source line: "Original, self-authored figure". URL/DOI and license: N/A.

## Ground truth

The figure shows an arrangement of nine distinct lines in the real plane. No two are
parallel, so all 36 pairs meet, and every intersection point lies inside the frame.

The 36 pairs collapse onto 25 distinct points: 21 simple points, three points where
exactly three lines concur, and one point where exactly four lines concur.

For a complex hyperplane arrangement the Orlik-Solomon description of the complement
M = C^2 minus the union of the complexified lines gives Poincare polynomial
1 + n t + (sum over points p of (m_p - 1)) t^2, so for this arrangement

    b_0 = 1,   b_1 = 9,   b_2 = sum_p (m_p - 1) = 21(1) + 3(2) + 1(3) = 30.

**GTFA: 30**

Verified three ways, all on exact rational arithmetic, no floating point anywhere in the
lattice computation.

1. Direct sum over the intersection lattice: 21 + 6 + 3 = 30.
2. Correction form: C(9,2) minus the concurrency corrections, that is
   36 - [3 x (C(3,2) - 2) + (C(4,2) - 3)] = 36 - [3(1) + 3] = 30.
3. Zaslavsky consistency: the real arrangement then has 1 + 9 + 30 = 40 regions of which
   1 - 9 + 30 = 22 are bounded, both positive and mutually consistent, which they would
   not be for an inconsistent lattice.

Answer format: exact positive integer, no rounding or tolerance.
Rendered length: 2 characters.

## The intersection lattice, for the grader

Numbering the lines L1 to L9 by the equations below (given only so a grader can check the
arithmetic; the figure itself carries no labels):

| line | equation |
| --- | --- |
| L1 | $y = -1$ |
| L2 | $x + 2y = -4$ |
| L3 | $2x - 3y = -1$ |
| L4 | $3x + y = -7$ |
| L5 | $x = -4$ |
| L6 | $x - 2y = -2$ |
| L7 | $x + 4y = -10$ |
| L8 | $x + y = -1$ |
| L9 | $3x + 2y = -5$ |

The four special points are

| point | multiplicity | lines through it |
| --- | --- | --- |
| (-2, -1) | 4 | L1, L2, L3, L4 |
| (-4, -1) | 3 | L1, L5, L6 |
| (2, -3) | 3 | L2, L7, L8 |
| (-3, 2) | 3 | L4, L8, L9 |

Every other pair of lines meets at a point of its own, giving 21 simple points.

## Step-by-step solution

**Step 1.** Count the distinct straight lines drawn in the figure. There are nine. Check
that no two are parallel by confirming that every pair meets somewhere inside the frame;
no pair runs off the edge without crossing.

**Step 2.** Work through the crossings and record, for each, how many of the nine lines
pass through it. Twenty-one crossings carry exactly two lines. Three crossings carry
exactly three. One crossing, near the middle of the figure, carries four. The care needed
is in separating genuine concurrence from three lines that bound a small triangle; the
smallest such triangle in this figure is about a seventh the size of the gap between the
two closest genuine crossings, so the distinction is visible but not free.

**Step 3.** Check the bookkeeping before going further. A point where m lines meet
accounts for C(m,2) of the pairs, so the points must account for all C(9,2) = 36 pairs:
21(1) + 3(3) + 1(6) = 21 + 9 + 6 = 36. They do, so no crossing has been missed or
double counted.

**Step 4.** Complexify. The complement is M = C^2 minus the union of the nine complex
lines. By the Orlik-Solomon theorem the cohomology of M is determined by the intersection
lattice alone, with Poincare polynomial

$$P(M, t) = \sum_{X \in L(\mathcal{A})} \mu(X)\,(-t)^{\mathrm{rank}(X)}
= 1 + 9t + \Big(\sum_{p} (m_p - 1)\Big) t^2 ,$$

the sum running over the intersection points, since the Mobius function of the whole space
is 1, of each line is -1, and of a point where m lines meet is m - 1.

**Step 5.** Substitute the multiplicities recorded in Step 2:

$$\sum_{p} (m_p - 1) = 21 \cdot 1 + 3 \cdot 2 + 1 \cdot 3 = 21 + 6 + 3 = 30 .$$

**Step 6.** As an arithmetic check, compute the same number the other way. In general
position the sum would be C(9,2) = 36; each triple point removes C(3,2) - 2 = 1 and the
quadruple point removes C(4,2) - 3 = 3, giving 36 - 3 - 3 = 30, which agrees.

**Step 7.** Therefore the second Betti number of the complement is 30.

## Image description

The figure is a self-authored line drawing of an arrangement of nine distinct straight
lines in the real plane, produced with matplotlib and exported as a single-panel opaque
PNG at 280 dpi. Every line is drawn in the same uniform dark slate-blue stroke of the same
width, running edge to edge across a plain white field. There is no coordinate frame: no
axes, no tick marks, no gridlines, no origin marker, no shading and no colour coding that
would distinguish one line from another.

No two of the nine lines are parallel, and the frame has been chosen so that all
thirty-six pairwise intersections fall strictly inside it, the closest any of them comes
to an edge being about half the distance between the two closest crossings. The crossings
are therefore all visible and the picture is complete: nothing relevant happens off the
page.

The thirty-six pairs do not give thirty-six separate points. Near the middle of the figure
four lines pass through one common point. At three further places, one to the left of that
point and roughly level with it, one low and to the right, and one above and to the left,
exactly three lines pass through a single common point. Every remaining crossing carries
exactly two lines. Several triples of lines come close to concurring without doing so,
bounding small but clearly open triangles; the tightest of these lies immediately beside
one of the genuine triple points, so the two configurations can be compared directly.

Quality is high. Stroke weight is even, no line is broken or occluded, the background is
uniform white, and nothing is cropped. The closest pair of distinct crossings is separated
by roughly eighty-six pixels at the exported size, against a stroke width of about eight,
so every crossing resolves cleanly. The figure carries no annotation whatsoever: no
labels, arrows, circles, boxes, highlighting, captions, legend or scale.

## Distractors

Distractors (incorrect answers only). Note that in testing we provided the model all
potential answers, including the GTFA.

| value | the specific misreading it encodes |
| --- | --- |
| 36 | all crossings taken to be simple, the arrangement read as generic |
| 33 | the quadruple point missed entirely, read as six separate simple crossings |
| 32 | the quadruple point read as a triple, the fourth line taken to miss it |
| 31 | one of the three triple points missed, read as three simple crossings |
| 29 | one near-miss triangle read as a genuine concurrence |

Each value is the exact second Betti number of the arrangement that the corresponding
misreading describes, so every one is a number a model actually lands on rather than a
plausible-looking guess.

## Why a model is expected to fail

The answer is a sum over twenty-five points of a quantity that depends only on how many
lines pass through each. Nothing else in the computation can absorb an error: one
misclassified point shifts the total by one, three, or more, and the wrong total is the
correct answer for the arrangement the model thinks it sees. There is no internal
inconsistency to catch it, because a misread arrangement is still a perfectly valid
arrangement.

Three properties apply pressure:

1. Concurrence versus near-concurrence is the whole task, and the tightest near-miss sits
   directly beside a genuine triple point, so a local glance is not enough.
2. The lines are visually identical and unlabelled, so tracking which line is which across
   the figure requires following a stroke rather than reading a neighbourhood.
3. Assuming general position is the overwhelmingly common case and gives 36, which is the
   single most likely wrong answer.

Failure reason, 1 to 3 sentences, for the submission form: the model misreads the
multiplicity structure of the arrangement, most often by assuming the lines are in general
position or by missing that a fourth line passes through the central triple point, and then
applies the Orlik-Solomon formula correctly to the wrong intersection lattice. The algebra
is typically sound, which is what makes this a visual extraction failure.

## What the prompt has to pin down

Writing the prompt sentence is yours. It needs to fix the following.

Must state:
- that the figure shows a finite arrangement of distinct lines in the real plane;
- that every intersection point of the arrangement lies within the frame, so nothing
  happens off the page (without this a reviewer can argue the reader cannot rule out two
  lines meeting outside, which is an ambiguity and therefore a major error);
- which invariant is wanted: the second Betti number, equivalently the rank of H^2, of
  the complement of the complexified arrangement in C^2;
- that the answer is an exact non-negative integer.

Must not:
- name Orlik-Solomon, the Mobius function, the characteristic polynomial or any other
  method, since Part 7 forbids method steering;
- state the number of lines, the number of intersection points, or any multiplicity;
- embed any answer options.

## Checklist status

Passing: PNG, opaque, high resolution, self-authored so no licensing exposure, single
image, no post-processing, zero annotation, single question, image-dependent, not OCR, not
a table, not a pure count, not stacked, GTFA unique and self-contained at 2 characters,
five distinct distractors each tied to a real misreading, numbered solution with the first
three steps observational and seven steps in total, image description over 300 words
without revealing the answer, KaTeX-safe LaTeX.

On the "at least ten naively possible answers" rule, if it is queried: for nine lines the
second Betti number can be any value from 8, when all nine are concurrent, up to 36 in
general position, so the naive answer set has 29 elements.

Open, and yours: the prompt text, and the two model runs.
