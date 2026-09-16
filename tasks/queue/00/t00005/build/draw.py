import sympy as sp, pickle, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
x, y = sp.symbols('x y')
f = sp.sympify(pickle.load(open("build/curve.pkl","rb")))
P = sp.Poly(f, x, y)
h = max(abs(c) for c in P.coeffs())
fn = sp.lambdify((x, y), sp.expand(f/h), "numpy")
PTS = [(0,0),(-3,1),(2,-2),(1,3),(-2,-3)]
XL, XH, YL, YH = -5.0, 4.0, -5.0, 5.0
n = 2200
X, Y = np.meshgrid(np.linspace(XL, XH, n), np.linspace(YL, YH, n))
Zv = fn(X, Y)
print("finite values:", np.isfinite(Zv).all(), " range:", float(np.nanmin(Zv)), float(np.nanmax(Zv)))
fig, ax = plt.subplots(figsize=(8, 8*(YH-YL)/(XH-XL)), dpi=260)
ax.contour(X, Y, Zv, levels=[0], colors="#16324f", linewidths=2.0)
for p in PTS:
    ax.plot([p[0]], [p[1]], marker="o", ms=5, color="crimson", zorder=5)  # QC only
ax.set_xlim(XL, XH); ax.set_ylim(YL, YH); ax.set_aspect("equal"); ax.axis("off")
fig.savefig("build/qc_curve.png", facecolor="white", bbox_inches="tight", pad_inches=0.1)
print("qc image written")
