"""Is any SMOOTH point of the real curve sharp enough to be mistaken for a singularity?

Implicit curvature: k = |f_y^2 f_xx - 2 f_x f_y f_xy + f_x^2 f_yy| / (f_x^2 + f_y^2)^{3/2}
Radius of curvature 1/k, converted to pixels at the figure's scale.
"""
import sympy as sp, pickle, numpy as np
x, y = sp.symbols('x y')
f = sp.sympify(pickle.load(open("build/curve.pkl","rb")))
h = max(abs(c) for c in sp.Poly(f, x, y).coeffs())
fs = sp.expand(f/h)
F  = sp.lambdify((x,y), fs, "numpy")
Fx = sp.lambdify((x,y), sp.diff(fs,x), "numpy"); Fy = sp.lambdify((x,y), sp.diff(fs,y), "numpy")
Fxx= sp.lambdify((x,y), sp.diff(fs,x,2), "numpy"); Fyy= sp.lambdify((x,y), sp.diff(fs,y,2), "numpy")
Fxy= sp.lambdify((x,y), sp.diff(fs,x,1,y,1), "numpy")
cy = [sp.lambdify(x, sp.expand(sp.Poly(fs,y).coeff_monomial(y**k)), "numpy") for k in range(6,-1,-1)]
cx = [sp.lambdify(y, sp.expand(sp.Poly(fs,x).coeff_monomial(x**k)), "numpy") for k in range(6,-1,-1)]
XL,XH,YL,YH = -5.0,4.0,-5.0,5.0
SING = [(0,0),(-3,1),(2,-2),(1,3),(-2,-3)]

def sweep(lo,hi,olo,ohi,co,n):
    out=[]
    for t in np.linspace(lo,hi,n):
        c=np.array([float(g(t)) for g in co]); nz=np.nonzero(np.abs(c)>1e-15)[0]
        if not len(nz): continue
        c=c[nz[0]:]
        if len(c)<2: continue
        for z in np.roots(c):
            if abs(z.imag)<1e-9 and olo<=z.real<=ohi: out.append((t,z.real))
    return out
pts = np.array(sweep(XL,XH,YL,YH,cy,14000) + [(b,a) for a,b in sweep(YL,YH,XL,XH,cx,14000)])
print("sampled", len(pts), "points")

px, py = pts[:,0], pts[:,1]
gx, gy = Fx(px,py), Fy(px,py)
g2 = gx**2 + gy**2
num = np.abs(gy**2*Fxx(px,py) - 2*gx*gy*Fxy(px,py) + gx**2*Fyy(px,py))
with np.errstate(divide='ignore', invalid='ignore'):
    kappa = num / g2**1.5
    radius = 1.0/kappa
dist = np.min(np.stack([np.hypot(px-a, py-b) for a,b in SING]), axis=0)

PPU = 2012/(XH-XL)     # pixels per unit in the exported figure
print(f"figure scale: {PPU:.0f} px per unit\n")
for cutoff in (0.05, 0.10, 0.20, 0.35):
    m = (dist > cutoff) & np.isfinite(radius)
    r = radius[m]
    print(f"  ignoring points within {cutoff} of a singularity ({m.sum()} samples):")
    print(f"     min radius of curvature {r.min():.4f} units = {r.min()*PPU:.1f} px")
    idx = np.argsort(r)[:4]
    sel = np.where(m)[0][idx]
    print(f"     sharpest smooth points: " +
          ", ".join(f"({px[i]:.2f},{py[i]:.2f}) r={radius[i]*PPU:.1f}px" for i in sel))
