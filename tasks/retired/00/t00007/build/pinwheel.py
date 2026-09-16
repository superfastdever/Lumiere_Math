import math, sys
sys.path.insert(0, "build")
from dessin import build

def ring(k, rad, rot, tag):
    return {f"{tag}{i}": (rad*math.cos(rot+2*math.pi*i/k), rad*math.sin(rot+2*math.pi*i/k))
            for i in range(k)}

def make(k, spokes_out=True, extra=True):
    """concentric rings: centre black, ring of white, ring of black, ring of white."""
    B = {"c": (0.0, 0.0)}
    W = {}
    W.update(ring(k, 1.0, 0.0, "p"))                    # white ring 1
    B.update(ring(k, 2.0, math.pi/k, "q"))              # black ring 2
    W.update(ring(k, 3.1, 0.0, "r"))                    # white ring 3
    E = [("c", f"p{i}") for i in range(k)]
    for i in range(k):                                  # white ring1 to black ring2
        E.append((f"q{i}", f"p{i}"))
        E.append((f"q{i}", f"p{(i+1) % k}"))
    for i in range(k):                                  # black ring2 to white ring3
        E.append((f"q{i}", f"r{i}"))
        E.append((f"q{i}", f"r{(i+1) % k}"))
    if extra:                                           # outer white ring gets one more each
        pass
    return B, W, E

for k in (4, 5, 6):
    B, W, E = make(k)
    r, err = build(B, W, E)
    if err:
        print(f"k={k}: {err}"); continue
    print(f"k={k}: degree {r['E']}, V={r['V']} F={r['F']} genus={r['genus']}, "
          f"|G|={r['order']}, transitive={r['transitive']}")
    print(f"    black degrees {r['deg0']}   white degrees {r['deg1']}")
    print(f"    face degrees  {r['degf']}")
