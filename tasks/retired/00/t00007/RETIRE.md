# t00007 retired: dessins d'enfants, monodromy group

## What was built

Machinery for dessins d'enfants: a bipartite graph embedded in the plane, with the
rotation system read off the drawing by sorting incident edges by angle. From that,
sigma0 (counterclockwise at black vertices), sigma1 (at white vertices),
sigma_inf = (sigma0 sigma1)^-1, the faces, the genus by Euler's formula, and the
monodromy group G = <sigma0, sigma1> as a sympy permutation group. The straight-line
drawing is checked for edge crossings, and that check caught a hand-drawn layout that
was not in fact planar.

## Results

| dessin | degree | genus | \|G\| |
| --- | --- | --- | --- |
| subdivided K4 (tetrahedral map) | 12 | 0 | 12 |
| subdivided 3-prism | 18 | 0 | 648 |
| subdivided octahedron | 24 | 0 | 24 |
| subdivided wheel W6 | 24 | 0 | 192 |
| concentric quadrangulation, k=4 | 20 | 0 | 7680 |
| concentric quadrangulation, k=5 | 25 | 0 | 375000 |
| concentric quadrangulation, k=6 | 30 | 0 | 58320 |

The 3-prism case is genuinely attractive as an adversarial item: its monodromy group has
order 648 while the rotation group of the triangular prism has order 12, so the natural
wrong move, identifying the monodromy group with the symmetry group of the solid, is off
by a factor of 54. The octahedron case shows the contrast: it is a regular map, so there
\|G\| really is 24 and the shortcut works.

## Why it is retired

Hand verification. The playbook requires that a knowledgeable PhD scholar can verify the
task with pen, paper and a basic calculator in about an hour. Computing the order of a
permutation group of degree 18 to 25 means running Schreier-Sims by hand, which is not an
hour's work, and none of these orders is recognisable on sight: 648, 192, 7680, 375000.

The invariants of a dessin that ARE hand-computable fail a different rule. The genus, the
face count and the passport (the cycle types of sigma0, sigma1, sigma_inf) can all be read
almost directly off the drawing, which makes them too close to a pure count and far too
easy. The automorphism group of the dessin is hand-checkable but is almost always trivial
or of order 2, so the answer space collapses.

So the interesting invariant is not verifiable by hand and the verifiable invariants are
not interesting. That is a structural conflict in this object, not a fixable defect in a
particular choice of dessin, which is why this is retired rather than iterated.

## Kept

`build/dessin.py` and the surveys are reproducible. If the hand-verification rule is ever
relaxed, or if a dessin is found whose monodromy group is recognisable on sight (a
symmetric or alternating group, or a classical group of small order), this becomes usable
immediately.
