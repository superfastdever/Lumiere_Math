import math, sys
sys.path.insert(0, "build")
from dessin import build

def subdivide(V, E, name):
    """V: name->(x,y) for the base planar graph; E: edges. White vertices at midpoints."""
    B = dict(V)
    W, EE = {}, []
    for k,(a,b) in enumerate(E):
        m = ((V[a][0]+V[b][0])/2.0, (V[a][1]+V[b][1])/2.0)
        w = f"w{k}"; W[w] = m
        EE.append((a,w)); EE.append((b,w))
    r, err = build(B, W, EE)
    if err: print(f"{name}: {err}"); return None
    print(f"{name}: degree {r['E']}, V={r['V']} F={r['F']} genus={r['genus']}, "
          f"|G|={r['order']}, transitive={r['transitive']}")
    print(f"    black degrees {r['deg0']}")
    print(f"    face degrees  {r['degf']}")
    return r

def poly(n, rad=1.0, rot=0.0):
    return {f"v{i}": (rad*math.cos(rot+2*math.pi*i/n), rad*math.sin(rot+2*math.pi*i/n))
            for i in range(n)}

# K4 drawn with one vertex inside a triangle
V = {**poly(3, 1.0, math.pi/2), "v3": (0.0, 0.0)}
E = [("v0","v1"),("v1","v2"),("v2","v0"),("v3","v0"),("v3","v1"),("v3","v2")]
subdivide(V, E, "subdivided K4 (tetrahedral map)")

# 3-prism: outer triangle, inner triangle, three spokes
V = {**{f"o{i}":p for i,p in enumerate(poly(3,1.6,math.pi/2).values())},
     **{f"i{i}":p for i,p in enumerate(poly(3,0.8,math.pi/2).values())}}
E = [("o0","o1"),("o1","o2"),("o2","o0"),("i0","i1"),("i1","i2"),("i2","i0"),
     ("o0","i0"),("o1","i1"),("o2","i2")]
subdivide(V, E, "subdivided 3-prism")

# octahedron: outer triangle + inner triangle rotated, fully joined
V = {**{f"o{i}":p for i,p in enumerate(poly(3,1.7,math.pi/2).values())},
     **{f"i{i}":p for i,p in enumerate(poly(3,0.75,-math.pi/2).values())}}
E = [("o0","o1"),("o1","o2"),("o2","o0"),("i0","i1"),("i1","i2"),("i2","i0"),
     ("o0","i1"),("o0","i2"),("o1","i0"),("o1","i2"),("o2","i0"),("o2","i1")]
subdivide(V, E, "subdivided octahedron")

# an irregular planar graph, no symmetry
V = {"a":(-1.9,0.1),"b":(-0.7,1.35),"c":(0.85,1.15),"d":(1.75,-0.25),
     "e":(0.55,-1.35),"f":(-0.95,-1.15),"g":(-0.15,0.15)}
E = [("a","b"),("b","c"),("c","d"),("d","e"),("e","f"),("f","a"),
     ("g","a"),("g","b"),("g","c"),("g","d"),("g","e"),("g","f")]
subdivide(V, E, "subdivided wheel W6 (irregular positions)")
