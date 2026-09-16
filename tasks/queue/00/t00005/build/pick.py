import sympy as sp, pickle, random, time
from sympy import Rational as R
x, y, Zs = sp.symbols('x y Z')
basis = [sp.sympify(s) for s in pickle.load(open("build/basis.pkl","rb"))]
WANT = {R(0), R(-3), R(2), R(1), R(-2)}

def smooth_inf(f):
    top = sp.Poly(f, x, y).homogenize(Zs).as_expr().subs(Zs, 0)
    t1 = sp.Poly(sp.expand(top).subs(y, 1), x)
    return t1.degree() == 6 and sp.discriminant(t1) != 0

def sing_x(f):
    fx, fy = sp.diff(f, x), sp.diff(f, y)
    r1 = sp.resultant(sp.Poly(f, y), sp.Poly(fx, y))
    r2 = sp.resultant(sp.Poly(f, y), sp.Poly(fy, y))
    g = sp.gcd(sp.Poly(r1, x), sp.Poly(r2, x))
    if g.degree() < 1: return None, None
    fac = sp.factor_list(g.as_expr())[1]
    lin, other = set(), []
    for p, e in fac:
        pp = sp.Poly(p, x)
        if pp.degree() == 1:
            a, b = pp.all_coeffs()
            lin.add(R(-b, a))
        else:
            other.append((p, e))
    return lin, other

rng = random.Random(23)
t0 = time.time(); checked = 0
for trial in range(3000):
    if time.time() - t0 > 600: break
    co = [R(rng.randint(-4, 4)) for _ in basis]
    f = sp.expand(sum(c*b for c, b in zip(co, basis)))
    if f == 0 or sp.Poly(f, x, y).total_degree() != 6: continue
    fl = sp.factor_list(f)[1]
    if len(fl) != 1 or fl[0][1] != 1: continue
    if not smooth_inf(f): continue
    checked += 1
    lin, other = sing_x(f)
    if lin is None: continue
    if lin == WANT and not other:
        print(f"FOUND after {checked} irreducible candidates, coeffs {co}")
        pickle.dump((list(map(str, co)), sp.srepr(f)), open("build/chosen.pkl", "wb"))
        print("f =", sp.factor(f) if False else f)
        break
else:
    print(f"no exact match in {checked} irreducible candidates")
print(f"elapsed {time.time()-t0:.0f}s")
