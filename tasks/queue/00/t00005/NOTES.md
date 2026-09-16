# t00005, work in progress

Plane sextic carrying five singularities of four distinct types. Not yet finished:
the curve has not been selected or fully verified, so there is no GTFA here yet.

## Design

| point | type | delta |
| --- | --- | --- |
| (0, 0) | ordinary triple point | 3 |
| (-3, 1) | node | 1 |
| (2, -2) | node | 1 |
| (1, 3) | cusp, horizontal tangent | 1 |
| (-2, -3) | tacnode, horizontal tangent | 2 |

Every condition is linear in the 28 coefficients of a sextic, which is what makes the
family computable: a node is f = f_x = f_y = 0; a cusp with horizontal tangent adds
f_xx = f_xy = 0; a tacnode adds the vanishing of the u^3 coefficient; an ordinary triple
point is the vanishing of f and all first and second partials. That is 23 conditions,
leaving a 5-dimensional solution space.

If the curve is irreducible with no further singularities and is smooth at infinity, the
geometric genus is (6-1)(6-2)/2 - sum(delta) = 10 - 8 = 2.

## Why the first attempt was structurally dead

The first choice of points put the triple point and both nodes on one line. A line through
a triple point and two nodes meets a sextic with multiplicity at least 3 + 2 + 2 = 7, which
exceeds 6, so by Bezout the line must be a component of the curve. Every member of that
family was therefore reducible, by necessity rather than bad luck: 0 of 60 sampled members
were irreducible. Moving the points into general position fixed it at once, 40 of 40
sampled members irreducible and 37 of those smooth at infinity.

This is recorded because it is a reusable constraint, not a one-off: imposed singular
points must be in sufficiently general position that no low-degree curve through them is
forced to split off by Bezout.

## Files

- `build/construct.py` builds the linear system and saves a basis of the solution space
- `build/pick.py` fast exact test that the singular locus is exactly the designed points,
  by resultants and gcd rather than Groebner bases, which were far too slow
- `build/refine.py` searches for a member with small integer coefficients and classifies
  each singularity from its local jets

## Still to do

Select the curve, confirm each singularity is the designed type rather than merely a
singular point, confirm no further singularities anywhere including at infinity, render
the real picture, and only then write the package.
