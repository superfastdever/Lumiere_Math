import sympy as sp, pickle, random, itertools, sys
from sympy import Rational as R
x, y, Z = sp.symbols('x y Z')
basis = [sp.sympify(s) for s in pickle.load(open("build/basis.pkl","rb"))]
DESIGNED = {(R(0),R(0)):'triple', (R(-2),R(1)):'node', (R(2),R(-1)):'node',
            (R(0),R(3)):'cusp', (R(-3),R(-2)):'tacnode'}

def sing_ideal(f):
    return [sp.expand(f), sp.expand(sp.diff(f,x)), sp.expand(sp.diff(f,y))]

def singular_points_count(f):
    """dimension of C[x,y]/(f,fx,fy): finite iff isolated singularities."""
    G = sp.groebner(sing_ideal(f), x, y, order='grevlex')
    if G.is_zero_dimensional is False:
        return None
    lead = [sp.Poly(g, x, y).LM(order='grevlex') for g in G.exprs]
    # count standard monomials under the leading terms
    degs = [(sp.Poly(g, x, y).monoms(order='grevlex')[0]) for g in G.exprs]
    bound = 40
    std = 0
    for a in range(bound):
        for b in range(bound):
            if not any(a >= d[0] and b >= d[1] for d in degs):
                std += 1
    return std

def smooth_at_infinity(f):
    F = sp.expand(sp.together(sp.Poly(f, x, y).homogenize(Z).as_expr()))
    top = sp.Poly(f, x, y).homogenize(Z).as_expr().subs(Z, 0)
    top = sp.Poly(sp.expand(top), x, y)
    # singular at infinity iff the top-degree form has a repeated root
    d = sp.discriminant(sp.Poly(top.as_expr().subs(y,1), x))
    return d != 0, top.as_expr()

rng = random.Random(0)
found = []
for trial in range(4000):
    co = [R(rng.randint(-4,4)) for _ in basis]
    if all(c == 0 for c in co): continue
    f = sp.expand(sum(c*b for c, b in zip(co, basis)))
    if f == 0: continue
    P = sp.Poly(f, x, y)
    if P.total_degree() != 6: continue
    fl = sp.factor_list(f)
    if len(fl[1]) > 1 or fl[1][0][1] > 1: continue      # reducible or non-reduced
    ok_inf, top = smooth_at_infinity(f)
    if not ok_inf: continue
    found.append((co, f))
    if len(found) >= 6: break

print(f"{len(found)} irreducible degree-6 candidates smooth at infinity\n")
for co, f in found[:6]:
    n = singular_points_count(f)
    # designed delta sum: triple 3 + node 1 + node 1 + cusp 1 + tacnode 2 = 8
    # expected Tjurina/Milnor total for exactly these: mu = 4+1+1+2+3 = 11
    print(f"  coeffs {co}: dim C[x,y]/(f,fx,fy) = {n}   (designed total Milnor number = 11)")
pickle.dump([(list(map(str,co)), sp.srepr(f)) for co, f in found], open("build/cands.pkl","wb"))
