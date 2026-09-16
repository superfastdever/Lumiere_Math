"""Among curves with exactly the designed singular locus, pick one with no false cusps:
every smooth point must have a radius of curvature large enough to read as smooth.
"""
import sympy as sp, pickle, random, time, numpy as np
from sympy import Rational as R
x, y, Zs = sp.symbols('x y Z')
basis = [sp.sympify(s) for s in pickle.load(open("build/basis.pkl","rb"))]
WANT = {R(0), R(-3), R(2), R(1), R(-2)}
SING = [(0,0),(-3,1),(2,-2),(1,3),(-2,-3)]
XL,XH,YL,YH = -5.0,4.0,-5.0,5.0
PPU = 2000/(XH-XL)
EXCL = 0.15          # ignore points this close to a genuine singularity

def smooth_inf(f):
    top = sp.Poly(f,x,y).homogenize(Zs).as_expr().subs(Zs,0)
    t1 = sp.Poly(sp.expand(top).subs(y,1), x)
    return t1.degree()==6 and sp.discriminant(t1)!=0

def sing_ok(f):
    r1 = sp.resultant(sp.Poly(f,y), sp.Poly(sp.diff(f,x),y))
    r2 = sp.resultant(sp.Poly(f,y), sp.Poly(sp.diff(f,y),y))
    g = sp.gcd(sp.Poly(r1,x), sp.Poly(r2,x))
    if g.degree()<1: return False
    lin=set()
    for p,e in sp.factor_list(g.as_expr())[1]:
        pp=sp.Poly(p,x)
        if pp.degree()!=1: return False
        a,b=pp.all_coeffs(); lin.add(R(-b,a))
    return lin==WANT

def all_branches_real(f):
    """Every branch of every singularity must be visible in the REAL picture:
    the triple point's cubic tangent cone needs three distinct real roots, and each
    node's quadratic tangent cone needs two distinct real roots (a crossing, not an
    isolated real point). Cusp and tacnode have v^2 as tangent cone by construction."""
    u, v = sp.symbols('u v')
    for p, kind in [((0,0),'triple'), ((-3,1),'node'), ((2,-2),'node'),
                    ((1,3),'cusp'), ((-2,-3),'tacnode')]:
        G = sp.Poly(sp.expand(f.subs({x: p[0]+u, y: p[1]+v})), u, v)
        c = lambda i, j: G.coeff_monomial(u**i * v**j)
        if kind == 'triple':
            cub = c(3,0)*u**3 + c(2,1)*u**2*v + c(1,2)*u*v**2 + c(0,3)*v**3
            d = sp.discriminant(sp.Poly(sp.expand(cub.subs(v, 1)), u))
            if d <= 0:                      # <0 means one real root, =0 not ordinary
                return False
        elif kind == 'node':
            if c(1,1)**2 - 4*c(2,0)*c(0,2) <= 0:   # <0 is an isolated real point
                return False
        else:
            # tangent cone is v^2; the two branches are real iff the quartic in u
            # obtained after completing the square is positive somewhere nearby
            if c(4,0) == 0 and kind == 'tacnode':
                return False
    return True

def sharpness(f, n=2600):
    h = max(abs(c) for c in sp.Poly(f,x,y).coeffs()); fs = sp.expand(f/h)
    cy=[sp.lambdify(x, sp.expand(sp.Poly(fs,y).coeff_monomial(y**k)),"numpy") for k in range(6,-1,-1)]
    cx=[sp.lambdify(y, sp.expand(sp.Poly(fs,x).coeff_monomial(x**k)),"numpy") for k in range(6,-1,-1)]
    Fx=sp.lambdify((x,y),sp.diff(fs,x),"numpy"); Fy=sp.lambdify((x,y),sp.diff(fs,y),"numpy")
    Fxx=sp.lambdify((x,y),sp.diff(fs,x,2),"numpy"); Fyy=sp.lambdify((x,y),sp.diff(fs,y,2),"numpy")
    Fxy=sp.lambdify((x,y),sp.diff(fs,x,1,y,1),"numpy")
    def sweep(lo,hi,olo,ohi,co):
        out=[]
        for t in np.linspace(lo,hi,n):
            c=np.array([float(g(t)) for g in co]); nz=np.nonzero(np.abs(c)>1e-15)[0]
            if not len(nz): continue
            c=c[nz[0]:]
            if len(c)<2: continue
            for z in np.roots(c):
                if abs(z.imag)<1e-9 and olo<=z.real<=ohi: out.append((t,z.real))
        return out
    P=np.array(sweep(XL,XH,YL,YH,cy)+[(b,a) for a,b in sweep(YL,YH,XL,XH,cx)])
    if len(P)<500: return None, 0
    px,py=P[:,0],P[:,1]
    gx,gy=Fx(px,py),Fy(px,py); g2=gx**2+gy**2
    num=np.abs(gy**2*Fxx(px,py)-2*gx*gy*Fxy(px,py)+gx**2*Fyy(px,py))
    with np.errstate(divide='ignore',invalid='ignore'):
        rad=g2**1.5/num
    d=np.min(np.stack([np.hypot(px-a,py-b) for a,b in SING]),axis=0)
    m=(d>EXCL)&np.isfinite(rad)
    return float(rad[m].min()*PPU), int(m.sum())

rng=random.Random(2027); t0=time.time(); best=None; tested=0
while time.time()-t0 < 1500:
    co=[R(rng.randint(-5,5)) for _ in basis]
    f=sp.expand(sum(c*b for c,b in zip(co,basis)))
    if f==0 or sp.Poly(f,x,y).total_degree()!=6: continue
    fl=sp.factor_list(f)[1]
    if len(fl)!=1 or fl[0][1]!=1: continue
    if not smooth_inf(f) or not sing_ok(f): continue
    if not all_branches_real(f): continue
    r,cnt=sharpness(f); tested+=1
    if r is None: continue
    if best is None or r>best[0]:
        best=(r,co,f); print(f"  candidate {tested}: min smooth radius {r:6.1f} px   coeffs {co}")
print(f"\ntested {tested} valid curves in {time.time()-t0:.0f}s")
print(f"best: min smooth radius {best[0]:.1f} px with coeffs {best[1]}")
pickle.dump(sp.srepr(best[2]), open("build/curve3.pkl","wb"))
