import sys; sys.path.insert(0, "/home/user/Lumiere_Math/tasks/t02")
from knot import determinant, walk, count_colourings

print("torus knots T(2,q) = closure of sigma_1^q on 2 strands, det should be q")
for q in [3, 5, 7, 9, 11]:
    print(f"   T(2,{q}): det = {determinant([1]*q, 2)}")

print("\ntorus knots on 3 strands")
for k, exp in [(4, 3), (5, 1)]:
    w = [1, 2] * k
    print(f"   T(3,{k}) = (s1 s2)^{k}: det = {determinant(w, 3)}  (expected {exp})")

print("\nnamed 6- and 7-crossing knots")
for name, w, n, exp in [
    ("6_2", [1,1,1,-2,1,-2], 3, 11),
    ("6_3", [1,1,-2,1,-2,-2], 3, 13),
    ("7_1", [1]*7, 2, 7),
]:
    print(f"   {name}: det = {determinant(w, n)}  (expected {exp})")

print("\nindependent cross-check: p divides det(K) iff non-trivial p-colourings exist")
print("   (a diagram with a arcs has exactly p trivial colourings)")
for name, w, n in [("trefoil", [1,1,1], 2), ("fig-8", [1,-2,1,-2], 3),
                   ("6_2", [1,1,1,-2,1,-2], 3), ("6_3", [1,1,-2,1,-2,-2], 3)]:
    d = determinant(w, n)
    row = []
    for p in [3, 5, 7, 11, 13]:
        c = count_colourings(w, n, p)
        row.append(f"p={p}: {c:5d} {'nontrivial' if c > p else 'trivial only':<13s}"
                   f"{'[p|det]' if d % p == 0 else '':7s}")
    print(f"   {name} (det {d})")
    for r in row:
        print("      ", r)
