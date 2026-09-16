import sys, random, numpy as np, collections, pickle
sys.path.insert(0,"build")
from fast import det_bareiss, smith
from fractions import Fraction as F

def hj(ws):
    x=F(-ws[-1])
    for b in reversed(ws[:-1]): x=(-b)-1/x
    return x

def build(wA, wB, link, chainsA, chainsB):
    """two branch nodes A(0) and B(1) joined by a chain; chains hang off each."""
    W=[wA,wB]; E=[]
    prev=0
    for w in link:
        W.append(w); i=len(W)-1; E.append((prev,i)); prev=i
    E.append((prev,1))
    for src, chains in ((0,chainsA),(1,chainsB)):
        for ws in chains:
            p=src
            for w in ws:
                W.append(w); i=len(W)-1; E.append((p,i)); p=i
    return W,E

def mat(W,E):
    n=len(W); M=[[0]*n for _ in range(n)]
    for i,w in enumerate(W): M[i][i]=w
    for a,b in E: M[a][b]+=1; M[b][a]+=1
    return M

rng=random.Random(21); best=[]; nd=0; ninv=collections.Counter()
for _ in range(150000):
    wA=rng.choice([-3,-4,-5,-6]); wB=rng.choice([-3,-4,-5,-6])
    link=[rng.choice([-2,-2,-3]) for _ in range(rng.choice([1,2,3]))]
    kA=rng.choice([3,4]); kB=rng.choice([3,4])
    chainsA=[[rng.choice([-2,-2,-2,-3,-4,-5]) for _ in range(rng.choice([1,2,3,4]))] for _ in range(kA)]
    chainsB=[[rng.choice([-2,-2,-2,-3,-4,-5]) for _ in range(rng.choice([1,2,3,4]))] for _ in range(kB)]
    W,E=build(wA,wB,link,chainsA,chainsB)
    if len(W)>26: continue
    M=mat(W,E)
    if np.linalg.eigvalsh(-np.array(M,dtype=float)).min()<=1e-9: continue
    nd+=1
    nums=[hj(c).numerator for c in chainsA+chainsB]
    if len(set(nums))<len(nums)-1: pass
    d=abs(det_bareiss(M))
    if not (2000<=d<=400000): continue
    inv=[x for x in smith(M) if x!=1]
    ninv[len(inv)]+=1
    if len(inv)<3: continue
    if len(set(nums))<4: continue          # branches must not be uniform
    best.append((len(inv),d,inv,W,E,wA,wB,link,chainsA,chainsB,nums))
print(f"{nd} negative definite;  invariant-factor count distribution {dict(sorted(ninv.items()))}")
best.sort(key=lambda t:(-t[0],t[1]))
print(f"{len(best)} candidates with 3 or more invariant factors and mixed branches\n")
seen=set()
for k,d,inv,W,E,wA,wB,link,cA,cB,nums in best:
    key=tuple(inv)
    if key in seen: continue
    seen.add(key)
    print(f"  {len(W)} vertices  det={d}  invariant factors {inv}")
    print(f"     A={wA} B={wB} link={link}")
    print(f"     chains at A {cA}")
    print(f"     chains at B {cB}")
    print(f"     branch numerators {nums}")
    print()
    if len(seen)>=4: break
pickle.dump(best[:20], open("build/cands.pkl","wb"))
