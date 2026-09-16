import sympy as sp
from fractions import Fraction as F
from sympy.matrices.normalforms import smith_normal_form

def hj(ws):
    x = F(-ws[-1])
    for b in reversed(ws[:-1]): x = (-b) - 1/x
    return x

A_W, B_W = -3, -4
LINK     = [-2, -3]
CHAINS_A = [[-2,-3], [-3,-3], [-2,-2,-2]]
CHAINS_B = [[-4,-3], [-2,-2,-2,-2,-2], [-3,-2,-3]]

W=[A_W,B_W]; E=[]; prev=0
for w in LINK:
    W.append(w); i=len(W)-1; E.append((prev,i)); prev=i
E.append((prev,1))
NODE_OF={}
for src,chains in ((0,CHAINS_A),(1,CHAINS_B)):
    for ci,ws in enumerate(chains):
        p=src
        for w in ws:
            W.append(w); i=len(W)-1; E.append((p,i)); p=i

n=len(W)
print(f"vertices {n}, edges {len(E)}  (tree: {len(E)==n-1})")
print("branch continued fractions, read from the branch node outward:")
for tag,chains in (("A",CHAINS_A),("B",CHAINS_B)):
    for c in chains:
        v=hj(c); print(f"   node {tag}  {c}  ->  {v}   d={v.numerator}, q={v.denominator}")
nums=[hj(c).numerator for c in CHAINS_A+CHAINS_B]
print(f"numerators {nums}   all distinct: {len(set(nums))==len(nums)}")

M=sp.zeros(n,n)
for i,w in enumerate(W): M[i,i]=w
for a,b in E: M[a,b]+=1; M[b,a]+=1
nd=all((-M)[:k,:k].det()>0 for k in range(1,n+1))
print("\nnegative definite:", nd)
d=abs(M.det()); print("det =", d, "=", sp.factorint(d))
S=smith_normal_form(sp.Matrix(M))
inv=[abs(S[i,i]) for i in range(n) if abs(S[i,i])!=1]
print("invariant factors:", inv, "  product:", sp.prod(inv), " == det:", sp.prod(inv)==d)
print("H_1(boundary X) =", " + ".join(f"Z/{x}Z" for x in inv))

def rank_mod(p):
    A=[[int(M[i,j])%p for j in range(n)] for i in range(n)]; r=0
    for c in range(n):
        piv=next((i for i in range(r,n) if A[i][c]%p),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]; iv=pow(A[r][c],p-2,p); A[r]=[(x*iv)%p for x in A[r]]
        for i in range(n):
            if i!=r and A[i][c]%p:
                f=A[i][c]; A[i]=[(a-f*b)%p for a,b in zip(A[i],A[r])]
        r+=1
    return r
print("\nindependent rank cross-check over F_p (no Smith form involved):")
for p in sorted(set(list(sp.factorint(d))+[2,3,5,7,11,13])):
    print(f"   p={p:3d}: rank {rank_mod(p):2d} -> {n-rank_mod(p)} factor(s) divisible by {p}"
          f"   predicted {sum(1 for x in inv if x%p==0)}")
import pickle
pickle.dump((W,E,A_W,B_W,LINK,CHAINS_A,CHAINS_B,inv,int(d)), open("build/graph.pkl","wb"))
print("\nsaved")
