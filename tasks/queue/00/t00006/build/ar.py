"""AR quiver of kQ, Q of Dynkin type E6, verified by the mesh (additivity) relations."""
import numpy as np, itertools, json

N = 6
ADJ    = [(0,1),(1,2),(2,3),(3,4),(2,5)]     # E6 shape: chain 0-1-2-3-4 with 5 on 2
ARROWS = [(0,1),(1,2),(2,3),(3,4),(2,5)]

def proj_dim(i):
    seen={i}; st=[i]
    while st:
        a=st.pop()
        for (p,q) in ARROWS:
            if p==a and q not in seen: seen.add(q); st.append(q)
    return [1 if k in seen else 0 for k in range(N)]

P = np.array([proj_dim(i) for i in range(N)], dtype=float)
C = P.T
Phi = -C.T @ np.linalg.inv(C)
TauInv = np.linalg.inv(Phi)

def positive_roots():
    Cm = np.zeros((N,N), dtype=int)
    for i in range(N): Cm[i][i]=2
    for (i,j) in ADJ: Cm[i][j]=Cm[j][i]=-1
    R = {tuple(int(k==i) for k in range(N)) for i in range(N)}
    ch=True
    while ch:
        ch=False
        for r in list(R):
            v=np.array(r)
            for i in range(N):
                s=v-(v@Cm[i])*np.eye(N,dtype=int)[i]
                t=tuple(int(a) for a in s)
                if all(a>=0 for a in t) and any(t) and t not in R:
                    R.add(t); ch=True
    return R
ROOTS = positive_roots()
print(f"E6: {len(ROOTS)} positive roots")

verts={}
for i in range(N):
    d=P[i].copy(); k=0
    while True:
        t=tuple(int(round(a)) for a in d)
        if any(a<0 for a in t) or not any(t) or t not in ROOTS: break
        verts[(i,k)]=t
        d=TauInv@d; k+=1
print(f"knitted {len(verts)} vertices")
assert sorted(verts.values())==sorted(ROOTS), "knitting mismatch"
print("knitting reproduces the root system exactly")

def mesh_ok(arrows):
    """for every non-projective (i,k>0): dim tau N + dim N == sum of dim over sources"""
    for (i,k), d in verts.items():
        if k==0: continue
        tau=verts[(i,k-1)]
        want=tuple(a+b for a,b in zip(tau,d))
        got=[0]*N
        for (s,t) in arrows:
            if t==(i,k):
                for m in range(N): got[m]+=verts[s][m]
        if tuple(got)!=want: return False, ((i,k), want, tuple(got))
    return True, None

for label, rule in [
    ("A: (i,k)->(j,k) for j->i in Q ;  (j,k)->(i,k+1) for j->i in Q",
     lambda: [((i,k),(j,k)) for (i,k) in verts for (a,b) in ARROWS if (b,a)==(i,j := a) and False]),
]:
    pass

def build(rule):
    A=[]
    for (i,k) in verts:
        for (a,b) in ARROWS:
            if rule=="fwd":
                if a==i and (b,k) in verts: A.append(((i,k),(b,k)))
                if b==i and (a,k+1) in verts: A.append(((i,k),(a,k+1)))
            else:
                if b==i and (a,k) in verts: A.append(((i,k),(a,k)))
                if a==i and (b,k+1) in verts: A.append(((i,k),(b,k+1)))
    return A

for rule in ("fwd","rev"):
    A=build(rule)
    ok,bad=mesh_ok(A)
    print(f"rule {rule}: {len(A)} arrows, mesh relations hold: {ok}" + ("" if ok else f"  first failure {bad}"))
    if ok:
        json.dump({"verts":{f"{i},{k}":list(v) for (i,k),v in verts.items()},
                   "arrows":[[list(s),list(t)] for s,t in A], "rule":rule},
                  open("build/arquiver.json","w"))
        print("saved build/arquiver.json")
        break
