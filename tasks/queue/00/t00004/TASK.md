# Task t00004 draft package

Subdomain: Algebra (toric geometry; also reads as Geometry & Topology)
Target failure modes: figure-based quantitative estimation (primary), geometric relation error (secondary)
Image: `figure.png`, self-authored with matplotlib, opaque RGB PNG, 2012 x 2012.
Source line: "Original, self-authored figure". URL/DOI and license: N/A.

## Why this one is built differently

The three earlier drafts all had the same shape: read a structure off a figure, then apply
a single formula. Once the formula is known the mathematics is one substitution, so the
only difficulty was in the reading, and that caps out well below the required level.

Here the derivation has its own traps, independent of the figure. Even a solver who reads
all five rays perfectly still has to put each cone into normal form, which requires a
unimodular change of basis and is where the index q is usually got wrong, and then expand
in **negative** continued fractions. Four of the five cones have an ordinary continued
fraction of a different length from the Hirzebruch-Jung one, so reaching for the ordinary
algorithm, the overwhelmingly more familiar one, gives 17 instead of 13.

## Ground truth

The figure shows a complete fan in the lattice $N = \mathbb{Z}^2$ with five rays. Reading
the primitive generator of each ray off the lattice, in counterclockwise order:

$$v_1 = (1,0),\quad v_2 = (4,7),\quad v_3 = (-1,2),\quad v_4 = (-5,-3),\quad v_5 = (1,-3).$$

Consecutive pairs span five two-dimensional cones which cover the plane. Writing
$d_i = \det(v_i, v_{i+1})$ for the index of the cone and $(d,q)$ for its normal form
$\langle (1,0), (-q, d) \rangle$:

| cone | $d$ | $q$ | negative continued fraction $d/q$ | exceptional divisors |
| --- | --- | --- | --- | --- |
| $\langle v_1, v_2 \rangle$ | 7 | 3 | $7/3 = [3,2,2]$ | 3 |
| $\langle v_2, v_3 \rangle$ | 15 | 4 | $15/4 = [4,4]$ | 2 |
| $\langle v_3, v_4 \rangle$ | 13 | 8 | $13/8 = [2,3,3]$ | 3 |
| $\langle v_4, v_5 \rangle$ | 18 | 11 | $18/11 = [2,3,4]$ | 3 |
| $\langle v_5, v_1 \rangle$ | 3 | 2 | $3/2 = [2,2]$ | 2 |

Every index exceeds 1, so all five cones are singular and each contributes.

**GTFA: 13**

Verified two ways with no shared code path.

1. Hirzebruch-Jung. Each cone is put in normal form by an explicit unimodular change of
   basis, and $d/q$ is expanded as $b_1 - 1/(b_2 - 1/(\cdots))$ with every $b_i \ge 2$.
   The number of exceptional divisors over a cone is the length of that expansion.
2. Convex hull. The rays of the minimal resolution of a two-dimensional cone are exactly
   the primitive lattice points on the compact boundary of $\mathrm{conv}(\sigma \cap
   \mathbb{Z}^2 \setminus \{0\})$, computed here by lattice enumeration and a domination
   test that never forms a continued fraction. The new rays it returns are

   $\langle v_1,v_2\rangle$: $(1,1), (2,3), (3,5)$;
   $\langle v_2,v_3\rangle$: $(1,2), (0,1)$;
   $\langle v_3,v_4\rangle$: $(-1,1), (-1,0), (-2,-1)$;
   $\langle v_4,v_5\rangle$: $(-3,-2), (-1,-1), (0,-1)$;
   $\langle v_5,v_1\rangle$: $(1,-2), (1,-1)$.

   That is $3+2+3+3+2 = 13$, agreeing with method 1 cone by cone, not merely in total.

The machinery was validated before use: the family $\langle (1,0),(1,n) \rangle$ must give
the $A_{n-1}$ singularity with $n-1$ exceptional divisors, confirmed for $n = 1$ to $8$;
every expansion was checked to have all $b_i \ge 2$ and to evaluate exactly to $d/q$ as a
rational number; and the two methods were compared on several thousand random cones.

Answer format: exact positive integer, no rounding or tolerance.
Rendered length: 2 characters.

## Step-by-step solution

**Step 1.** Read the five rays off the lattice. Each drawn ray passes through lattice
points, and its primitive generator is the first one met leaving the origin. Going
counterclockwise from the horizontal ray these are $(1,0)$, $(4,7)$, $(-1,2)$, $(-5,-3)$
and $(1,-3)$.

**Step 2.** Record that the five rays occur in counterclockwise order and that the five
cones spanned by consecutive pairs cover the plane, so the fan is complete and the
associated toric surface is compact. No ray is repeated and no two are opposite.

**Step 3.** For consecutive generators $u, v$ the cone $\langle u, v \rangle$ is smooth
exactly when $\det(u,v) = \pm 1$, and otherwise defines a cyclic quotient singularity of
order $|\det(u,v)|$. Here the determinants are

$$\det(v_1,v_2) = 7,\quad \det(v_2,v_3) = 15,\quad \det(v_3,v_4) = 13,\quad
\det(v_4,v_5) = 18,\quad \det(v_5,v_1) = 3,$$

so all five cones are singular and none can be skipped.

**Step 4.** Put each cone in normal form. Choose $M \in GL_2(\mathbb{Z})$ with
$M u = (1,0)$; then $M v = (-q, d)$ with $d = \det(u,v)$ and $0 < q < d$ coprime to $d$,
and the cone defines the cyclic quotient singularity of type $\tfrac{1}{d}(1,q)$. Carrying
this out gives $(d,q) = (7,3), (15,4), (13,8), (18,11)$ and $(3,2)$ respectively. This step
is where the index is most easily mistaken: $q$ depends on the change of basis and is not
read off $\det$ alone.

**Step 5.** Resolve each singularity. The minimal resolution of $\tfrac{1}{d}(1,q)$ has
exceptional locus a chain of rational curves whose self-intersections are the terms of the
**negative** continued fraction
$$\frac{d}{q} = b_1 - \cfrac{1}{b_2 - \cfrac{1}{\ddots - \cfrac{1}{b_r}}},
\qquad b_i \ge 2,$$
and the number of exceptional divisors is $r$. The ordinary continued fraction algorithm
gives a different expansion and in general a different length, so it cannot be substituted
here. The expansions are $7/3 = [3,2,2]$, $15/4 = [4,4]$, $13/8 = [2,3,3]$,
$18/11 = [2,3,4]$ and $3/2 = [2,2]$, of lengths $3, 2, 3, 3, 2$.

**Step 6.** Check each expansion by evaluating it back. For instance
$[2,3,4] = 2 - 1/(3 - 1/4) = 2 - 1/(11/4) = 2 - 4/11 = 18/11$, as required, and every
term is at least 2, which is what makes the resolution minimal rather than merely a
resolution.

**Step 7.** The resolutions of distinct cones meet only along the rays they share, which
are not exceptional, so the counts add. The total is $3 + 2 + 3 + 3 + 2 = 13$.

## Image description

The figure is a self-authored line drawing of a fan in a rank two lattice, produced with
matplotlib and exported as a single-panel opaque PNG at 300 dpi. The background is plain
white. A square array of small grey dots fills the frame on unit centres, representing the
lattice $\mathbb{Z}^2$; the dots are drawn on top of everything else, so wherever a ray
passes through a lattice point that point remains visible sitting on the stroke.

Five straight rays are drawn in a single uniform dark slate-blue stroke. All five emanate
from a common point, marked by a slightly larger dot of the same dark colour, which sits
at a lattice point roughly in the middle of the frame and is the origin. Each ray runs from
that point outward to the edge of the frame and stops there; none continues through the
origin to the other side, so all five are rays rather than lines.

Reading counterclockwise from the ray that runs horizontally to the right, the rays leave
the origin through the lattice points four right and seven up, one left and two up, five
left and three down, and one right and three down. Each ray passes exactly through the
lattice point named and through its positive multiples, and through no other lattice point
nearer the origin. Consecutive rays are well separated in angle, the smallest gap being
over fifty degrees, and together the five cones between consecutive rays sweep out the
whole plane exactly once.

Quality is high. Stroke weight is uniform, the lattice dots are evenly spaced and clearly
distinguishable from the strokes by both size and colour, nothing is cropped and nothing
is blurred. The figure carries no annotation of any kind: no coordinate axes, no tick
marks, no numbers, no ray labels, no arrowheads, no shading of the cones, no arrows,
circles, boxes or highlighting, and no caption or legend.

## Distractors

Distractors (incorrect answers only). Note that in testing we provided the model all
potential answers, including the GTFA.

| value | the specific error it encodes |
| --- | --- |
| 17 | ordinary continued fractions used in place of the negative ones |
| 18 | the rays of the resolution fan counted instead of the exceptional divisors |
| 15 | the index taken as $d-q$ rather than $q$, a normal form convention slip |
| 12 | the ray $(-1,2)$ misread as $(-1,1)$ |
| 11 | the cone $\langle v_5, v_1 \rangle$ closing the fan overlooked |

Each value is the exact answer produced by the corresponding error, computed by the same
verified machinery as the GTFA, so none is a plausible-looking invention.

## Why a model is expected to fail

There are two independent places to go wrong and both must be got right.

The reading. Five primitive generators have to be recovered from a bare lattice with no
axes and no labels, including $(4,7)$ and $(-5,-3)$, which require counting several steps
in both directions. A single misread coordinate changes two determinants at once, since
each ray bounds two cones, and so changes two continued fractions.

The derivation. The index $q$ is not visible in the determinant and only appears after a
unimodular change of basis, which is the classic place to slip. Then the resolution needs
negative continued fractions, while the familiar algorithm is the ordinary one; on this fan
four of the five cones have expansions of different lengths under the two algorithms, so
that substitution alone moves the answer from 13 to 17.

Failure reason, 1 to 3 sentences, for the submission form: the model either misreads at
least one primitive ray generator off the unlabelled lattice, which changes the indices of
the two cones that ray bounds, or recovers the cone indices correctly but resolves them
with ordinary rather than negative continued fractions. In both cases the downstream
reasoning is internally consistent, so nothing in the response signals the error.

## What the prompt has to pin down

Writing the prompt sentence is yours. It needs to fix the following.

Must state:
- that the grey dots are the lattice $\mathbb{Z}^2$, that the common point of the rays is
  the origin, and that the drawn rays are precisely the rays of a complete fan in that
  lattice;
- that the surface in question is the toric surface associated with that fan;
- which number is wanted: the number of exceptional divisors, that is the number of
  irreducible components of the exceptional locus, of the **minimal** resolution. The word
  minimal is essential, since without it any number of further blowups is admissible and
  the answer is not unique, which would be a major error;
- that the answer is an exact positive integer.

Must not:
- mention Hirzebruch-Jung, continued fractions of either kind, the normal form
  $\tfrac{1}{d}(1,q)$, determinants, or blowups as a method, since Part 7 forbids method
  steering;
- state the number of rays, any ray coordinate, or any index;
- embed any answer options.

## Checklist status

Passing: PNG, opaque, high resolution, self-authored so no licensing exposure, single
image, no post-processing, zero annotation, single question, image-dependent, not OCR,
not a table, not a pure count, not stacked, GTFA unique and self-contained at 2 characters,
five distinct distractors each tied to a real error, numbered solution with the first two
steps observational and seven steps in total, image description over 300 words without
revealing the answer, KaTeX-safe LaTeX.

Hand verification: five determinants, five changes of basis and five short continued
fractions, each checkable by evaluating the expansion back. Comfortably inside an hour.

Level: the minimal resolution of cyclic quotient surface singularities by Hirzebruch-Jung
is standard graduate toric geometry, in Fulton and in Cox-Little-Schenck. It is not a
formula that can be applied blind.

Open, and yours: the prompt text, and the two model runs.
