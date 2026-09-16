"""Minimal resolution of a complete toric surface given by a fan in Z^2.

Two independent computations of the number of exceptional divisors:
  (A) convex hull: the rays of the minimal resolution of a 2-dimensional cone are
      exactly the primitive lattice points on the boundary of conv(sigma \ {0}).
  (B) Hirzebruch-Jung: put the cone in normal form <(1,0),(-q,d)>, expand d/q as a
      negative continued fraction, and count its terms.
They share no code path, so agreement is a real check.
"""
from fractions import Fraction as F
from math import gcd
from itertools import combinations

def det(u, v):
    return u[0]*v[1] - u[1]*v[0]

def primitive(v):
    g = gcd(abs(v[0]), abs(v[1]))
    if g == 0:
        return None
    return (v[0]//g, v[1]//g)

# ---------------------------------------------------------------- method A
def hull_rays(u, v, bound=400):
    """Primitive lattice points on the compact boundary of conv(sigma cap Z^2 \ {0})."""
    d = det(u, v)
    assert d > 0
    pts = []
    for a in range(-bound, bound+1):
        for b in range(-bound, bound+1):
            if (a, b) == (0, 0):
                continue
            # inside the cone spanned by u,v (closed)
            if det(u, (a, b)) >= 0 and det((a, b), v) >= 0:
                pts.append((a, b))
    # lower convex hull facing the origin: keep points not expressible as p + (cone point)
    S = set(pts)
    keep = []
    for p in pts:
        if max(abs(p[0]), abs(p[1])) > bound - 6:
            continue
        dominated = False
        for q in pts:
            if q == p:
                continue
            r = (p[0]-q[0], p[1]-q[1])
            if r == (0, 0):
                continue
            if det(u, r) >= 0 and det(r, v) >= 0:
                dominated = True
                break
        if not dominated:
            keep.append(p)
    keep.sort(key=lambda p: F(det(u, p), 1) if det(u, p) else 0)
    order = sorted(keep, key=lambda p: (det(u, p), -det(p, v)))
    return order

def exceptional_hull(u, v):
    r = hull_rays(u, v, bound=60)
    assert r[0] == u and r[-1] == v, (u, v, r[:3], r[-3:])
    return len(r) - 2, r

# ---------------------------------------------------------------- method B
def normal_form(u, v):
    """Unimodular change of basis sending u -> (1,0); returns (d, q) with 0 < q < d,
    the cone becoming <(1,0), (-q, d)>; q = d - (image of v)_x mod d."""
    d = det(u, v)
    # extended euclid to build M in SL_2(Z) with M u = (1,0)
    a, b = u
    g, x, y = a, 1, 0
    a2, x2, y2 = b, 0, 1
    while a2:
        k = g // a2
        g, a2 = a2, g - k*a2
        x, x2 = x2, x - k*x2
        y, y2 = y2, y - k*y2
    if g < 0:
        g, x, y = -g, -x, -y
    assert g == 1, f"ray not primitive: {u}"
    M = [[x, y], [-b, a]]
    assert (M[0][0]*a + M[0][1]*b, M[1][0]*a + M[1][1]*b) == (1, 0)
    vv = (M[0][0]*v[0] + M[0][1]*v[1], M[1][0]*v[0] + M[1][1]*v[1])
    assert vv[1] == d, (vv, d)
    q = (-vv[0]) % d
    return d, q

def hj(d, q):
    """Negative continued fraction d/q = b1 - 1/(b2 - 1/...), all b_i >= 2."""
    out = []
    while q:
        b = -(-d // q)              # ceiling division
        out.append(b)
        d, q = q, b*q - d
    return out

def exceptional_hj(u, v):
    d, q = normal_form(u, v)
    if d == 1:
        return 0, (d, q, [])
    f = hj(d, q)
    return len(f), (d, q, f)

# ---------------------------------------------------------------- validation
if __name__ == "__main__":
    print("validation 1: the A_n family <(1,0),(1,n)> must give n-1 exceptional divisors")
    for n in range(1, 9):
        eh, _ = exceptional_hull((1,0), (1,n))
        ej, info = exceptional_hj((1,0), (1,n))
        assert eh == ej == n-1, (n, eh, ej)
        print(f"   n={n}: d={n} hull={eh} hj={ej} chain={info[2]}  ok")

    print("\nvalidation 2: the continued fraction must actually evaluate to d/q")
    from fractions import Fraction as Fr
    def eval_hj(f):
        x = Fr(f[-1])
        for b in reversed(f[:-1]):
            x = b - 1/x
        return x
    import random
    rng = random.Random(5)
    checked = 0
    for _ in range(4000):
        u = primitive((rng.randint(-9,9), rng.randint(-9,9)))
        v = primitive((rng.randint(-9,9), rng.randint(-9,9)))
        if u is None or v is None or det(u,v) <= 0 or det(u,v) > 30: continue
        d, q = normal_form(u, v)
        if d == 1: continue
        f = hj(d, q)
        assert all(b >= 2 for b in f), (d,q,f)
        assert eval_hj(f) == Fr(d, q), (d,q,f,eval_hj(f))
        checked += 1
    print(f"   {checked} random cones: every chain has all b_i >= 2 and evaluates to d/q")

    print("\nvalidation 3: the two independent methods on random cones")
    rng = random.Random(17)
    agree = 0
    for _ in range(3000):
        u = primitive((rng.randint(-7,7), rng.randint(-7,7)))
        v = primitive((rng.randint(-7,7), rng.randint(-7,7)))
        if u is None or v is None or det(u,v) <= 0 or det(u,v) > 14: continue
        eh, _ = exceptional_hull(u, v)
        ej, _ = exceptional_hj(u, v)
        assert eh == ej, (u, v, eh, ej)
        agree += 1
    print(f"   {agree} random cones: convex hull and Hirzebruch-Jung agree on every one")
