"""A dessin d'enfant: a bipartite graph embedded in the plane.

The embedding gives a rotation system. Reading the edges counterclockwise around each
black vertex gives a permutation sigma0 of the edge set; around each white vertex, sigma1.
Then sigma_inf = (sigma0 sigma1)^{-1} and its cycles are the faces. The monodromy group
is G = <sigma0, sigma1>, and Euler's formula gives the genus.

Everything here is exact: permutations and a permutation group order, no numerics beyond
sorting angles, and the planarity of the drawing is checked by segment intersection.
"""
import math, itertools
from sympy.combinatorics import Permutation, PermutationGroup

def build(BLACK, WHITE, EDGES):
    """BLACK/WHITE: name -> (x,y).  EDGES: list of (black, white), index = edge label."""
    pos = {**BLACK, **WHITE}
    # planarity of the straight-line drawing
    def seg(a,b): return (pos[a], pos[b])
    def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    def proper(p1,p2,p3,p4):
        d1,d2 = cross(p3,p4,p1), cross(p3,p4,p2)
        d3,d4 = cross(p1,p2,p3), cross(p1,p2,p4)
        return (d1*d2 < 0) and (d3*d4 < 0)
    for (e1,e2) in itertools.combinations(range(len(EDGES)), 2):
        a,b = EDGES[e1]; c,d = EDGES[e2]
        if len({a,b,c,d}) < 4: continue
        if proper(*seg(a,b), *seg(c,d)):
            return None, f"edges {e1} and {e2} cross"
    def rotation(vertex):
        inc = [i for i,(b,w) in enumerate(EDGES) if b==vertex or w==vertex]
        def ang(i):
            b,w = EDGES[i]; other = w if b==vertex else b
            return math.atan2(pos[other][1]-pos[vertex][1], pos[other][0]-pos[vertex][0])
        return sorted(inc, key=ang)
    n = len(EDGES)
    s0 = list(range(n)); s1 = list(range(n))
    for v in BLACK:
        c = rotation(v)
        for k in range(len(c)): s0[c[k]] = c[(k+1) % len(c)]
    for v in WHITE:
        c = rotation(v)
        for k in range(len(c)): s1[c[k]] = c[(k+1) % len(c)]
    S0, S1 = Permutation(s0), Permutation(s1)
    Sinf = (S0*S1)**-1
    V = len(BLACK)+len(WHITE); E = n; F = len(Sinf.full_cyclic_form)
    genus = (2 - V + E - F)//2
    G = PermutationGroup([S0, S1])
    return dict(s0=S0, s1=S1, sinf=Sinf, V=V, E=E, F=F, genus=genus,
                order=G.order(), transitive=G.is_transitive(), group=G,
                deg0=sorted(len(c) for c in S0.full_cyclic_form),
                deg1=sorted(len(c) for c in S1.full_cyclic_form),
                degf=sorted(len(c) for c in Sinf.full_cyclic_form)), None

# ---- candidate 1: the cube graph Q3 drawn as two nested squares
B1 = {"b1":(-3,3), "b2":(3,-3), "b3":(-1,1), "b4":(1,-1)}
W1 = {"w1":(3,3), "w2":(-3,-3), "w3":(1,1), "w4":(-1,-1)}
E1 = [("b1","w1"),("b1","w2"),("b1","w3"),("b2","w1"),("b2","w2"),("b2","w4"),
      ("b3","w1"),("b3","w3"),("b3","w4"),("b4","w2"),("b4","w3"),("b4","w4")]
r, err = build(B1, W1, E1)
print("cube-like dessin:", err if err else
      f"V={r['V']} E={r['E']} F={r['F']} genus={r['genus']} |G|={r['order']} "
      f"transitive={r['transitive']}\n   black degrees {r['deg0']}, white {r['deg1']}, faces {r['degf']}")
