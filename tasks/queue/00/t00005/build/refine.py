import sympy as sp, pickle, random, time
from sympy import Rational as R
x, y, u, v, Zs = sp.symbols('x y u v Z')
basis = [sp.sympify(s) for s in pickle.load(open("build/basis.pkl","rb"))]
WANT = {R(0), R(-3), R(2), R(1), R(-2)}
PTS = {(R(0),R(0)):'triple', (R(-3),R(1)):'node', (R(2),R(-2)):'node',
       (R(1),R(3)):'cusp', (R(-2),R(-3)):'tacnode'}

def clear(f):
    P = sp.Poly(f, x, y)
    den = sp.lcm([sp.denom(c) for c in P.coeffs()])
    g = sp.expand(f*den)
    P = sp.Poly(g, x, y)
    cg = sp.gcd([sp.numer(c) for c in P.coeffs()])
    return sp.expand(g/cg)

def height(f):
    return max(abs(c) for c in sp.Poly(f, x, y).coeffs())

def smooth_inf(f):
    top = sp.Poly(f, x, y).homogenize(Zs).as_expr().subs(Zs, 0)
    t1 = sp.Poly(sp.expand(top).subs(y, 1), x)
    return t1.degree() == 6 and sp.discriminant(t1) != 0

def sing_x(f):
    r1 = sp.resultant(sp.Poly(f, y), sp.Poly(sp.diff(f,x), y))
    r2 = sp.resultant(sp.Poly(f, y), sp.Poly(sp.diff(f,y), y))
    g = sp.gcd(sp.Poly(r1,x), sp.Poly(r2,x))
    if g.degree() < 1: return None, None
    lin, other = set(), []
    for p, e in sp.factor_list(g.as_expr())[1]:
        pp = sp.Poly(p, x)
        if pp.degree() == 1:
            a, b = pp.all_coeffs(); lin.add(R(-b, a))
        else: other.append(p)
    return lin, other

def classify(f, p):
    g = sp.expand(f.subs({x: p[0]+u, y: p[1]+v}))
    P = sp.Poly(g, u, v)
    def c(i, j): return P.coeff_monomial(u**i * v**j)
    if any(c(i,j) != 0 for i,j in [(0,0),(1,0),(0,1)]) is False:
        pass
    j2 = [c(2,0), c(1,1), c(0,2)]
    j3 = [c(3,0), c(2,1), c(1,2), c(0,3)]
    if c(0,0) != 0 or c(1,0) != 0 or c(0,1) != 0:
        return "smooth/not on curve"
    if any(t != 0 for t in j2):
        disc = j2[1]**2 - 4*j2[0]*j2[2]
        if disc != 0:
            return "node (A1)" if disc != 0 else "?"
        # degenerate quadratic: square of a linear form
        if any(t != 0 for t in j3):
            return "cusp (A2)"
        return "higher"
    if any(t != 0 for t in j3):
        cub = sum(cc*u**i*v**(3-i) for i, cc in
                  zip([3,2,1,0], [c(3,0), c(2,1), c(1,2), c(0,3)]))
        d = sp.discriminant(sp.Poly(sp.expand(cub.subs(v, 1)), u))
        return "ordinary triple point (D4)" if d != 0 else "non-ordinary triple point"
    return "multiplicity >= 4"

def refine_tac(f, p):
    """distinguish A2 (cusp) from A3 (tacnode) at a point whose 2-jet is a square."""
    g = sp.expand(f.subs({x: p[0]+u, y: p[1]+v}))
    P = sp.Poly(g, u, v)
    if P.coeff_monomial(u**3) != 0:
        return "cusp (A2), delta 1"
    if P.coeff_monomial(u**4) != 0:
        return "tacnode (A3), delta 2"
    return "A_{>=4}"

rng = random.Random(99); best = None; t0 = time.time(); seen = 0
while time.time() - t0 < 420:
    co = [R(rng.randint(-5,5)) for _ in basis]
    f = sp.expand(sum(c*b for c, b in zip(co, basis)))
    if f == 0 or sp.Poly(f,x,y).total_degree() != 6: continue
    fl = sp.factor_list(f)[1]
    if len(fl) != 1 or fl[0][1] != 1: continue
    if not smooth_inf(f): continue
    lin, other = sing_x(f)
    if lin != WANT or other: continue
    fi = clear(f); h = height(fi); seen += 1
    if best is None or h < best[0]:
        best = (h, co, fi)
print(f"{seen} exact matches; smallest integer height {best[0]}")
print("coeffs:", best[1])
f = best[2]
print("\nsingularity classification:")
for p, want in PTS.items():
    k = classify(f, p)
    extra = refine_tac(f, p) if "cusp" in k else ""
    print(f"   {tuple(map(str,p))}: designed {want:8s} -> found {k} {extra}")
pickle.dump(sp.srepr(f), open("build/curve.pkl","wb"))
print("\nsaved")
