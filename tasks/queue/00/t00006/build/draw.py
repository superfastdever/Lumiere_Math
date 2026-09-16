import json, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

D = json.load(open("build/arquiver.json"))
VERT = {tuple(map(int,k.split(','))): tuple(v) for k,v in D["verts"].items()}
AR = [tuple(map(tuple,a)) for a in D["arrows"]]

# layer = longest path from a source in the AR quiver (acyclic), so arrows go left to right
succ = {}
for s,t in AR: succ.setdefault(s,[]).append(t)
indeg = {v:0 for v in VERT}
for s,t in AR: indeg[t]+=1
layer = {v:0 for v in VERT}
order, q = [], [v for v in VERT if indeg[v]==0]
deg = dict(indeg)
while q:
    v=q.pop(); order.append(v)
    for w in succ.get(v,[]):
        layer[w]=max(layer[w], layer[v]+1)
        deg[w]-=1
        if deg[w]==0: q.append(w)
assert len(order)==len(VERT), "AR quiver is not acyclic"
ROW = {0:0, 1:1, 2:2, 5:3, 3:4, 4:5}          # branch node 5 placed next to its neighbour 2
pos = {v: (layer[v]*1.0, ROW[v[0]]*1.0) for v in VERT}
coll = len(pos.values()) - len(set(pos.values()))
print("layers used:", max(layer.values())+1, " position collisions:", coll)
assert coll == 0

fig, ax = plt.subplots(figsize=(20, 7.0), dpi=220)
for s,t in AR:
    x1,y1 = pos[s]; x2,y2 = pos[t]
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2), arrowstyle='-|>', mutation_scale=11,
        color="#22405e", lw=1.25, shrinkA=15, shrinkB=15, zorder=2))
for (i,k) in VERT:
    if (i,k-1) in VERT:
        x1,y1 = pos[(i,k)]; x2,y2 = pos[(i,k-1)]
        ax.plot([x1,x2],[y1,y2], ls=(0,(3,3)), color="#9aa6b2", lw=1.0, zorder=1)
for v,(x,y) in pos.items():
    s = "".join(str(d) for d in VERT[v])
    ax.text(x, y, s, ha="center", va="center", fontsize=8.6, zorder=3,
            family="DejaVu Sans Mono",
            bbox=dict(boxstyle="round,pad=0.30", fc="white", ec="#22405e", lw=0.85))
ax.set_xlim(-0.8, max(layer.values())+0.8); ax.set_ylim(-0.8, 5.8)
ax.set_aspect("equal"); ax.axis("off"); fig.patch.set_facecolor("white")
fig.savefig("figure.png", facecolor="white", bbox_inches="tight", pad_inches=0.18)
from PIL import Image
im=Image.open("figure.png"); bg=Image.new("RGB",im.size,(255,255,255))
bg.paste(im, mask=im.split()[-1] if im.mode=="RGBA" else None)
bg.save("figure.png","PNG",optimize=True)
o=Image.open("figure.png"); print("figure:", o.mode, o.size)
T = json.load(open("build/chosen_T.json"))
print("T summands and their AR positions:")
for s in T["summands"]:
    v=[k for k,val in VERT.items() if list(val)==s][0]
    print(f"   {''.join(map(str,s))}  layer {layer[v]}, row {ROW[v[0]]}")
