"""Render the real curve by root finding rather than contouring.

For each x on a fine grid, solve the degree-6 polynomial f(x, y) = 0 for y and keep the
real roots; then do the same with the roles of x and y swapped. Overlaying the two sweeps
covers vertical and horizontal tangents alike, and nothing is ever interpolated across a
singular point, so cusps and tacnodes render closed rather than broken.
"""
import sympy as sp, pickle, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
x, y = sp.symbols('x y')
f = sp.sympify(pickle.load(open("build/curve.pkl","rb")))
P = sp.Poly(f, x, y)
h = max(abs(c) for c in P.coeffs())
fs = sp.expand(f / h)

cy = [sp.Poly(fs, y).coeff_monomial(y**k) for k in range(6, -1, -1)]
cx = [sp.Poly(fs, x).coeff_monomial(x**k) for k in range(6, -1, -1)]
fy = [sp.lambdify(x, sp.expand(c), "numpy") for c in cy]     # coefficients in y, funcs of x
fx = [sp.lambdify(y, sp.expand(c), "numpy") for c in cx]

def sweep(lo, hi, olo, ohi, coeffs, n=9000):
    pts = []
    for t in np.linspace(lo, hi, n):
        c = np.array([float(g(t)) for g in coeffs], dtype=float)
        nz = np.nonzero(np.abs(c) > 1e-14)[0]
        if len(nz) == 0: continue
        c = c[nz[0]:]
        if len(c) < 2: continue
        r = np.roots(c)
        for z in r:
            if abs(z.imag) < 1e-7 and olo <= z.real <= ohi:
                pts.append((t, z.real))
    return pts

XL, XH, YL, YH = -5.0, 4.0, -5.0, 5.0
A = sweep(XL, XH, YL, YH, fy)                 # (x, y)
B = [(b, a) for a, b in sweep(YL, YH, XL, XH, fx)]   # (x, y) from the y sweep
pts = np.array(A + B)
print("sampled points on the curve:", len(pts))

for tag, (cx0, cy0, r) in {
    "full": ((XL+XH)/2, (YL+YH)/2, None),
    "zoom_cusp": (1, 3, 0.5),
    "zoom_tacnode": (-2, -3, 0.5),
    "zoom_triple": (0, 0, 0.5),
    "zoom_node": (2, -2, 0.5),
}.items():
    if r is None:
        fig, ax = plt.subplots(figsize=(8.4, 8.4*(YH-YL)/(XH-XL)), dpi=300)
        m = np.ones(len(pts), bool); lo_x, hi_x, lo_y, hi_y = XL, XH, YL, YH; ms = 0.75
    else:
        fig, ax = plt.subplots(figsize=(4.2, 4.2), dpi=180)
        lo_x, hi_x, lo_y, hi_y = cx0-r, cx0+r, cy0-r, cy0+r
        m = ((pts[:,0] >= lo_x) & (pts[:,0] <= hi_x) &
             (pts[:,1] >= lo_y) & (pts[:,1] <= hi_y)); ms = 2.4
    ax.plot(pts[m,0], pts[m,1], ".", ms=ms, color="#16324f", mec="none")
    ax.set_xlim(lo_x, hi_x); ax.set_ylim(lo_y, hi_y)
    ax.set_aspect("equal"); ax.axis("off")
    fig.patch.set_facecolor("white")
    out = "figure.png" if tag == "full" else f"build/{tag}.png"
    fig.savefig(out, facecolor="white", bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)
from PIL import Image
im = Image.open("figure.png"); bg = Image.new("RGB", im.size, (255,255,255))
bg.paste(im, mask=im.split()[-1] if im.mode=="RGBA" else None)
bg.save("figure.png", "PNG", optimize=True)
print("figure:", Image.open("figure.png").mode, Image.open("figure.png").size)
