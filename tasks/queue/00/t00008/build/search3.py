import sys, random, numpy as np
sys.path.insert(0,"build")
from fast import det_bareiss, smith
from fractions import Fraction as F

def hj(ws):
    x=F(-ws[-1])
    for b in reversed(ws[:-1]): x=(-b)-1/x
    return x

def build(cyc, chains):
    W=list(cyc); E=[(0,1),(1,2),(2,3),(3,0)]
    for node,ws in chains:
        prev=node
        for w in ws:
            W.append(w); i=len(W)-1; E.append((prev,i)); prev=i
    return W,E

def mat(W,E):
    n=len(W); M=[[0]*n for _ in range(n)]
    for i,w in enumerate(W): M[i][i]=w
    for a,b in E: M[a][b]+=1; M[b][a]+=1
    return M

rng=random.Random(9); best=[]; nd=0
for _ in range(120000):
    cyc=[rng.choice([-2,-3,-3,-4,-5]) for _ in range(4)]
    chains=[(k,[rng.choice([-2,-2,-2,-3,-4]) for _ in range(rng.choice([2,3,4]))]) for k in range(4)]
    W,E=build(cyc,chains); M=mat(W,E)
    ev=np.linalg.eigvalsh(-np.array(M,dtype=float))
    if ev.min()<=1e-9: continue
    nd+=1
    nums=[hj(ws).numerator for _,ws in chains]
    if len(set(nums))<4: continue
    d=abs(det_bareiss(M))
    if not (800 <= d <= 120000): continue
    inv=[x for x in smith(M) if x!=1]
    if len(inv)<3: continue
    best.append((len(inv), d, inv, W, E, cyc, chains, nums))
best.sort(key=lambda t:(-t[0], t[1]))
print(f"{nd} negative definite, {len(best)} pass every filter\n")
seen=set()
for k,d,inv,W,E,cyc,chains,nums in best:
    key=tuple(inv)
    if key in seen: continue
    seen.add(key)
    print(f"  {len(W)} vertices  det={d}  invariant factors {inv}")
    print(f"     cycle {cyc}  branch numerators {nums}")
    print(f"     chains {[ws for _,ws in chains]}")
    if len(seen)>=5: break
import pickle; pickle.dump(best[:20], open("build/cands.pkl","wb"))
