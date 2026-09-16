# Task 02 draft package

Subdomain: Geometry & Topology
Target failure modes: connectivity / topology error (primary), prior override (secondary)
Image: `figure.png`, self-authored with matplotlib, opaque RGB PNG, 1550 x 1550.
Source line: "Original, self-authored figure". URL/DOI and license: N/A.

## Ground truth

The figure is a diagram of a knot, drawn as the closure of a 3-strand braid laid out
radially in an annulus. It has ten crossings and is a single closed curve. The diagram
does not alternate: travelling once along the knot, the over and under passages read

    U O O U O U U O U U O U O O U O O U O U

**GTFA: 31**

Verified two independent ways.

1. Fox colouring matrix. The ten undercrossings cut the knot into ten arcs. Each crossing
   contributes the relation 2(over arc) - (under arc in) - (under arc out) = 0. Deleting
   one row and one column and taking the absolute determinant of the 9 by 9 minor by
   fraction-free elimination gives 31.
2. Gaussian elimination modulo p, which never forms a determinant. For each prime p the
   rank of the full colouring matrix was computed over F_p. The rank drops below 9 exactly
   at p = 31, and at no other prime up to 43. Non-trivial Fox p-colourings therefore exist
   precisely when p = 31, which is equivalent to p dividing the determinant.

The two methods agree on every prime tested. The determinant machinery was separately
validated against known values first: trefoil 3, figure-eight 5, 5_1 5, 5_2 7, 6_2 11,
6_3 13, 7_1 7, T(2,q) = q for q up to 11, T(3,4) = 3 and T(3,5) = 1.

The drawing was then checked against the mathematics by recovering the braid word from the
rendered geometry and recomputing: the recovered word matches, and gives 31 again.

Answer format: exact positive odd integer, no rounding or tolerance.
Rendered length: 2 characters.

## Arc incidence, for the grader

Label the arcs a1 to a10 in order along the knot, starting from the arc that leaves the
first undercrossing. The ten crossings then read:

| crossing | over arc | under arcs |
| --- | --- | --- |
| 1 | a7 | a2, a3 |
| 2 | a7 | a1, a10 |
| 3 | a1 | a3, a4 |
| 4 | a4 | a7, a8 |
| 5 | a8 | a4, a5 |
| 6 | a1 | a5, a6 |
| 7 | a8 | a1, a2 |
| 8 | a6 | a8, a9 |
| 9 | a9 | a6, a7 |
| 10 | a2 | a9, a10 |

## Step-by-step solution

**Step 1.** Trace the drawn curve. It closes up after passing through every strand of the
figure, so the diagram has one component and is a knot rather than a link. Counting the
places where two strands meet gives ten crossings, and at each one the break in the drawn
line identifies which strand passes underneath.

**Step 2.** Record the over and under data in the order they are met along the knot. The
sequence is U O O U O U U O U U O U O O U O O U O U. Because this sequence contains
adjacent equal letters, the diagram is not alternating, so no shortcut that assumes
alternation applies.

**Step 3.** The ten undercrossings cut the curve into ten arcs. Label them a1 to a10 in
the order they are traversed, starting with the arc leaving the first undercrossing, and
record for each crossing which arc passes over and which two arc ends meet underneath.
This gives the incidence table above.

**Step 4.** The determinant of a knot is the order of the first homology of its double
branched cover, and is computed from any diagram by the Fox colouring relations: at a
crossing where arc c passes over and arcs a and b meet underneath, a labelling by integers
must satisfy 2c - a - b = 0. Assembling one such row per crossing gives a 10 by 10 integer
matrix M whose rows and columns each sum to zero.

**Step 5.** From the table, M is

$$M=\begin{pmatrix}
0&-1&-1&0&0&0&2&0&0&0\\
-1&0&0&0&0&0&2&0&0&-1\\
2&0&-1&-1&0&0&0&0&0&0\\
0&0&0&2&0&0&-1&-1&0&0\\
0&0&0&-1&-1&0&0&2&0&0\\
2&0&0&0&-1&-1&0&0&0&0\\
-1&-1&0&0&0&0&0&2&0&0\\
0&0&0&0&0&2&0&-1&-1&0\\
0&0&0&0&0&-1&-1&0&2&0\\
0&2&0&0&0&0&0&0&-1&-1
\end{pmatrix}$$

Every row has exactly one entry 2 and two entries -1, which is the arithmetic check that
each crossing was recorded with one over arc and two under arc ends.

**Step 6.** Delete the last row and the last column and evaluate the resulting 9 by 9
determinant. The matrix is sparse, three non-zero entries per row, so fraction-free
elimination clears quickly and yields an absolute value of 31. The value does not depend
on which row and column are deleted.

**Step 7.** Therefore the determinant of the knot is 31.

## Image description

The figure is a self-authored line drawing of a knot diagram, produced with matplotlib and
exported as a single-panel opaque PNG at 240 dpi. A single closed curve of uniform dark
slate-blue stroke is drawn in an annular region of an otherwise empty white field. The
curve winds around a common centre three times, so at any radius away from the crossings
three concentric strands are visible, evenly spaced and well separated.

Ten crossings are distributed at regular angular intervals around the annulus. At each
crossing exactly two strands meet, always two that are at neighbouring radial levels, and
they meet nearly at right angles, between seventy-eight and eighty-four degrees. Over and
under information is given in the standard way, by a clean break in the strand that passes
underneath; the break is wide relative to the stroke width and no other feature of the
figure resembles one. No crossing involves more than two strands and no two crossings are
close enough to be confused, the nearest pair being separated by roughly twenty stroke
widths.

Reading the passages in the order they occur along the curve, the sequence of over and
under passages is U O O U O U U O U U O U O O U O O U O U, where U marks a passage
underneath. This sequence has adjacent repeats, so the diagram is not an alternating one,
which is the single most important feature of the figure and the one most easily lost.

Quality is high: line weight is even throughout, no strand is cropped, nothing is blurred
or aliased into ambiguity, and the background is uniform white with no gridlines, axes or
shading. The figure carries no annotation of any kind: no labels, arrows, orientation
markers, base point, captions, scale bar or legend. Nothing in the drawing names the knot.

## Distractors

Distractors (incorrect answers only). Note that in testing we provided the model all
potential answers, including the GTFA.

| value | the specific misreading it encodes |
| --- | --- |
| 97 | the diagram read as alternating, which flips four crossings |
| 27 | one crossing reversed, the second one met along the curve |
| 23 | one crossing reversed, the first one met along the curve |
| 17 | one crossing reversed, the third or the tenth |
| 15 | one crossing reversed, the sixth |

Every value is the exact determinant of the knot obtained from the corresponding
misreading, computed the same two ways as the GTFA, so each one is what a model actually
lands on rather than a number chosen to look plausible. The remaining single-crossing
misreadings give 13, 9 and 3, which are held in reserve.

## Why a model is expected to fail

The whole answer rests on ten binary decisions, each carried by a gap a few pixels wide,
and there is no redundancy anywhere in the computation. Reversing any single crossing
changes the determinant from 31 to one of 3, 9, 13, 15, 17, 23 or 27. Nothing in the
arithmetic downstream can absorb or reveal the error, because the wrong reading is a
perfectly consistent knot diagram with its own perfectly well defined determinant.

Three properties of this particular diagram apply pressure:

1. It does not alternate. The overwhelming majority of knot diagrams in textbooks and in
   training data alternate, and a model carrying that prior will read at least four
   crossings the wrong way round and return 97.
2. The three strands are concentric and locally near-parallel, so deciding which of two
   strands owns a given break requires following a strand around the annulus rather than
   reading a local neighbourhood.
3. The diagram is not a table diagram of any named knot, so recognition does not help. The
   crossings have to be read.

Failure reason, 1 to 3 sentences, for the submission form: the model misreads the over and
under data of the diagram, most often by assuming the diagram alternates or by reversing a
single crossing, and then carries out the colouring or Alexander computation correctly on
the wrong diagram. The algebra in the response is typically sound, which is what makes
this a visual extraction failure rather than a reasoning failure.

## What the prompt has to pin down

Writing the prompt sentence is yours. It needs to fix the following.

Must state:
- that the figure shows a diagram of a knot, and that breaks in a strand mark undercrossings;
- which invariant is wanted, namely the determinant of the knot, with the convention made
  explicit as the absolute value of the Alexander polynomial evaluated at -1, equivalently
  the order of the first homology of the double branched cover;
- that the answer is an exact positive integer.

Making the convention explicit matters here. Without it a reviewer can argue the word
"determinant" is ambiguous, and ambiguity is a major error at Stage 4.

Must not:
- mention Fox colourings, the Goeritz or Alexander matrix, or any other method, since
  Part 7 forbids method steering;
- state the crossing number, say whether the diagram alternates, or name the knot;
- embed any answer options.

## Checklist status

Passing on my side: PNG, opaque, original resolution, self-authored so no licensing
exposure, single image, no post-processing, zero annotation, image not reused, single
question, image-dependent, not OCR, not a table, not a pure count, not stacked, GTFA unique
and self-contained at 2 characters, far more than 10 naively possible answers, five
distinct distractors each tied to a real misreading, numbered solution with the first two
steps purely observational and seven steps in total, image description over 300 words
without revealing the answer, KaTeX-safe LaTeX throughout.

Worth knowing: hand verification is a sparse 9 by 9 integer determinant with three
non-zero entries per row. That is inside the one hour budget but it is not quick, so the
step-by-step carries the full incidence table to keep a grader off the figure.

Open, and yours: the prompt text, and the two model runs.
