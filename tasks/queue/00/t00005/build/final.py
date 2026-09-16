import sympy as sp, pickle, numpy as np
from sympy import Rational as R
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
x, y, Zs, u, v = sp.symbols('x y Z u v')
f = sp.sympify(pickle.load(open("build/curve2.pkl","rb")))
DESIGN = {(R(0),R(0)):'ordinary triple point', (R(-3),R(1)):'node', (R(2),R(-2)):'node',
          (R(1),R(3)):'cusp', (R(-2),R(-3)):'tacnode'}
DELTA = {'ordinary triple point':3, 'node':1, 'cusp':1, 'tacnode':2}

fl = sp.factor_list(f)[1]
print("irreducible over Q:", len(fl)==1 and fl[0][1]==1)
top = sp.Poly(f,x,y).homogenize(Zs).as_expr().subs(Zs,0)
t1 = sp.Poly(sp.expand(top).subs(y,1), x)
print("smooth at infinity:", t1.degree()==6 and sp.discriminant(t1)!=0)
r1 = sp.resultant(sp.Poly(f,y), sp.Poly(sp.diff(f,x),y))
r2 = sp.resultant(sp.Poly(f,y), sp.Poly(sp.diff(f,y),y))
g = sp.gcd(sp.Poly(r1,x), sp.Poly(r2,x))
print("gcd of resultants factors as:",
      " ".join(f"({sp.factor(p)})^{e}" for p,e in sp.factor_list(g.as_expr())[1]))
found=[]
for p,e in sp.factor_list(g.as_expr())[1]:
    pp=sp.Poly(p,x); assert pp.degree()==1, "irrational singular point"
    a,b=pp.all_coeffs(); x0=R(-b,a)
    for s in sp.solve([f.subs(x,x0), sp.diff(f,x).subs(x,x0), sp.diff(f,y).subs(x,x0)], y, dict=True):
        found.append((x0, s[y]))
print("singular points:", [(str(a),str(b)) for a,b in found])
print("exactly the five designed:",
      sorted((str(a),str(b)) for a,b in found)==sorted((str(a),str(b)) for a,b in DESIGN))
tot=0
for p,want in DESIGN.items():
    G=sp.Poly(sp.expand(f.subs({x:p[0]+u, y:p[1]+v})), u, v)
    c=lambda i,j: G.coeff_monomial(u**i*v**j)
    mult=min(i+j for (i,j),co in zip(G.monoms(),G.coeffs()) if co!=0)
    if want=='ordinary triple point':
        ok = mult==3 and sp.discriminant(sp.Poly(sp.expand(
             (c(3,0)*u**3+c(2,1)*u**2*v+c(1,2)*u*v**2+c(0,3)*v**3).subs(v,1)), u))!=0
    elif want=='node':   ok = mult==2 and c(1,1)**2-4*c(2,0)*c(0,2)!=0
    elif want=='cusp':   ok = mult==2 and c(1,1)**2-4*c(2,0)*c(0,2)==0 and c(3,0)!=0
    else:                ok = mult==2 and c(1,1)**2-4*c(2,0)*c(0,2)==0 and c(3,0)==0 and c(4,0)!=0
    tot+=DELTA[want]
    print(f"   {tuple(map(str,p))}: {want:22s} confirmed={ok}  delta={DELTA[want]}")
print(f"sum delta = {tot}, arithmetic genus 10, GEOMETRIC GENUS = {10-tot}")

h=max(abs(c) for c in sp.Poly(f,x,y).coeffs()); fs=sp.expand(f/h)
cy=[sp.lambdify(x, sp.expand(sp.Poly(fs,y).coeff_monomial(y**k)),"numpy") for k in range(6,-1,-1)]
cx=[sp.lambdify(y, sp.expand(sp.Poly(fs,x).coeff_monomial(x**k)),"numpy") for k in range(6,-1,-1)]
def sweep(lo,hi,olo,ohi,co,n):
    out=[]
    for t in np.linspace(lo,hi,n):
        c=np.array([float(gg(t)) for gg in co]); nz=np.nonzero(np.abs(c)>1e-15)[0]
        if not len(nz): continue
        c=c[nz[0]:]
        if len(c)<2: continue
        for z in np.roots(c):
            if abs(z.imag)<1e-9 and olo<=z.real<=ohi: out.append((t,z.real))
    return out
XL,XH,YL,YH=-4.6,3.6,-4.4,4.4
pts=np.array(sweep(XL,XH,YL,YH,cy,16000)+[(b,a) for a,b in sweep(YL,YH,XL,XH,cx,16000)])
print("sampled", len(pts))
fig,ax=plt.subplots(figsize=(8.6, 8.6*(YH-YL)/(XH-XL)), dpi=300)
ax.plot(pts[:,0],pts[:,1],".",ms=1.9,color="#16324f",mec="none")
ax.set_xlim(XL,XH); ax.set_ylim(YL,YH); ax.set_aspect("equal"); ax.axis("off")
fig.patch.set_facecolor("white")
fig.savefig("figure.png",facecolor="white",bbox_inches="tight",pad_inches=0.12)
from PIL import Image
im=Image.open("figure.png"); bg=Image.new("RGB",im.size,(255,255,255))
bg.paste(im, mask=im.split()[-1] if im.mode=="RGBA" else None)
bg.save("figure.png","PNG",optimize=True)
o=Image.open("figure.png"); print("figure:",o.mode,o.size)
fig2,axes=plt.subplots(1,5,figsize=(20,4.3),dpi=150)
for ax2,(p,name) in zip(axes, DESIGN.items()):
    r=0.45; m=((pts[:,0]>=float(p[0])-r)&(pts[:,0]<=float(p[0])+r)&
               (pts[:,1]>=float(p[1])-r)&(pts[:,1]<=float(p[1])+r))
    ax2.plot(pts[m,0],pts[m,1],".",ms=2.6,color="#16324f",mec="none")
    ax2.set_xlim(float(p[0])-r,float(p[0])+r); ax2.set_ylim(float(p[1])-r,float(p[1])+r)
    ax2.set_aspect("equal"); ax2.set_xticks([]); ax2.set_yticks([])
    ax2.set_title(f"{name}\nat {tuple(map(str,p))}", fontsize=11)
fig2.tight_layout(); fig2.savefig("build/qc_zoom2.png",facecolor="white",bbox_inches="tight",pad_inches=0.12)
print("zoom written")
