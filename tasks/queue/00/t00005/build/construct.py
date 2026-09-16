"""Build a plane curve of prescribed degree carrying several distinct singularity types.

Every condition used is LINEAR in the coefficients of f:
  node at p            : f = f_x = f_y = 0                                  (3)
  cusp at p, horiz tgt : also f_xx = f_xy = 0, need f_yy != 0, u^3 coef != 0 (5)
  tacnode at p, h tgt  : also coefficient of u^3 vanishes                    (6)
  ordinary triple pt   : f and all first and second partials vanish          (6)
"""
import sympy as sp
from sympy import Rational as R

x, y = sp.symbols('x y')

def monomials(d):
    return [x**i * y**j for i in range(d+1) for j in range(d+1-i)]

def local_coeff(f, p, i, j):
    """coefficient of u^i v^j in f(p1+u, p2+v)"""
    u, v = sp.symbols('u v')
    g = sp.expand(f.subs({x: p[0]+u, y: p[1]+v}))
    return sp.expand(g).coeff(u, i).coeff(v, j)

def conditions(f, spec):
    p, kind = spec['at'], spec['type']
    C = [local_coeff(f, p, 0, 0), local_coeff(f, p, 1, 0), local_coeff(f, p, 0, 1)]
    if kind == 'node':
        return C
    if kind in ('cusp', 'tacnode'):
        C += [local_coeff(f, p, 2, 0), local_coeff(f, p, 1, 1)]   # 2-jet = c v^2
        if kind == 'tacnode':
            C += [local_coeff(f, p, 3, 0)]                        # kill u^3
        return C
    if kind == 'triple':
        return C + [local_coeff(f, p, 2, 0), local_coeff(f, p, 1, 1), local_coeff(f, p, 0, 2)]
    raise ValueError(kind)

def build(deg, specs):
    mons = monomials(deg)
    cs = sp.symbols(f'c0:{len(mons)}')
    f = sum(c*m for c, m in zip(cs, mons))
    eqs = []
    for s in specs:
        eqs += conditions(f, s)
    sol = sp.linsolve(eqs, cs)
    basis = []
    sol = list(sol)[0]
    free = sorted({s for e in sol for s in e.free_symbols} & set(cs), key=lambda s: s.name)
    for fv in free:
        sub = {g: (1 if g == fv else 0) for g in free}
        basis.append(sp.expand(sum(sp.simplify(e.subs(sub))*m for e, m in zip(sol, mons))))
    return f, cs, basis, free

DEG = 6
SPECS = [
    {'at': (R(0), R(0)),   'type': 'triple'},
    {'at': (R(-3), R(1)),  'type': 'node'},
    {'at': (R(2), R(-2)),  'type': 'node'},
    {'at': (R(1), R(3)),   'type': 'cusp'},
    {'at': (R(-2), R(-3)), 'type': 'tacnode'},
]
f, cs, basis, free = build(DEG, SPECS)
print(f"degree {DEG}: {len(monomials(DEG))} coefficients, "
      f"{sum(len(conditions(f, s)) for s in SPECS)} linear conditions")
print(f"solution space dimension: {len(basis)}  (free: {[s.name for s in free]})")
for b in basis[:3]:
    print("   basis element:", sp.Poly(b, x, y).total_degree(), sp.count_ops(b), "ops")
import pickle
pickle.dump([sp.srepr(b) for b in basis], open("build/basis.pkl", "wb"))
print("basis saved")
