import pickle, numpy as np, itertools, math
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
W,E,A_W,B_W,LINK,CA,CB,inv,det = pickle.load(open("build/graph.pkl","rb"))
n=len(W)

def layout(seed, iters=1400):
    rng=np.random.default_rng(seed)
    P=rng.normal(0,1.6,(n,2))
    adj=[[] for _ in range(n)]
    for a,b in E: adj[a].append(b); adj[b].append(a)
    for t in range(iters):
        F=np.zeros((n,2))
        for i in range(n):                         # repulsion
            d=P[i]-P; dist=np.linalg.norm(d,axis=1); dist[i]=1
            F[i]+=np.sum(d/ (dist**2)[:,None] *0.85, axis=0)
        for a,b in E:                              # springs
            d=P[b]-P[a]; L=np.linalg.norm(d)+1e-9
            f=(L-1.15)*d/L*0.95; F[a]+=f; F[b]-=f
        P+=F*0.016
    return P

def crossings(P):
    def o(p,q,r): return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
    c=0
    for (a,b),(x,y) in itertools.combinations(E,2):
        if len({a,b,x,y})<4: continue
        d1,d2=o(P[x],P[y],P[a]),o(P[x],P[y],P[b])
        d3,d4=o(P[a],P[b],P[x]),o(P[a],P[b],P[y])
        if d1*d2<0 and d3*d4<0: c+=1
    return c

def minsep(P):
    return min(np.linalg.norm(P[i]-P[j]) for i,j in itertools.combinations(range(n),2))

best=None
for s in range(60):
    P=layout(s)
    c=crossings(P); m=minsep(P)
    if c==0 and (best is None or m>best[1]):
        best=(P,m,s)
P,m,s=best
print(f"layout seed {s}: 0 edge crossings, minimum vertex separation {m:.2f}")

span=max(np.ptp(P[:,0]),np.ptp(P[:,1]))
R=m*0.34
fig,ax=plt.subplots(figsize=(12,12*np.ptp(P[:,1])/np.ptp(P[:,0])),dpi=230)
for a,b in E:
    ax.plot([P[a,0],P[b,0]],[P[a,1],P[b,1]],color="#333333",lw=2.1,zorder=1,
            solid_capstyle="round")
for i in range(n):
    ax.add_patch(plt.Circle(P[i],R,facecolor="white",edgecolor="#111111",lw=2.2,zorder=3))
    ax.text(P[i,0],P[i,1],str(W[i]),ha="center",va="center",fontsize=200*R/span,zorder=4)
ax.set_aspect("equal"); ax.axis("off")
pad=R*1.8
ax.set_xlim(P[:,0].min()-pad,P[:,0].max()+pad); ax.set_ylim(P[:,1].min()-pad,P[:,1].max()+pad)
fig.patch.set_facecolor("white")
fig.savefig("figure.png",facecolor="white",bbox_inches="tight",pad_inches=0.2)
from PIL import Image
im=Image.open("figure.png"); bg=Image.new("RGB",im.size,(255,255,255))
bg.paste(im, mask=im.split()[-1] if im.mode=="RGBA" else None)
bg.save("figure.png","PNG",optimize=True)
o=Image.open("figure.png"); print("figure:",o.mode,o.size)
val=[0]*n
for a,b in E: val[a]+=1; val[b]+=1
print("valences:", sorted(val, reverse=True)[:6], " (two branch nodes of valence 4)")
print("answer: H_1 =", " + ".join(f"Z/{x}Z" for x in inv), " det =", det)
