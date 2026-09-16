# Validation log for the toric machinery (tasks/queue/00/t00004/build/toric.py)

Two independent runs, different seeds and sampling ranges.

## Run 1
```
   n=3: d=3 hull=2 hj=2 chain=[2, 2]  ok
   n=4: d=4 hull=3 hj=3 chain=[2, 2, 2]  ok
   n=5: d=5 hull=4 hj=4 chain=[2, 2, 2, 2]  ok
   n=6: d=6 hull=5 hj=5 chain=[2, 2, 2, 2, 2]  ok
   n=7: d=7 hull=6 hj=6 chain=[2, 2, 2, 2, 2, 2]  ok
   n=8: d=8 hull=7 hj=7 chain=[2, 2, 2, 2, 2, 2, 2]  ok

validation 2: the continued fraction must actually evaluate to d/q
   1339 random cones: every chain has all b_i >= 2 and evaluates to d/q

validation 3: the two independent methods on random cones
   1037 random cones: convex hull and Hirzebruch-Jung agree on every one

```

## Run 2
```
check 1: A_n family <(1,0),(1,n)> must give n-1 divisors
   n = 1..8 all correct, by both methods

check 2: every expansion has all b_i >= 2 and evaluates back to d/q
   7228 random cones verified

check 3: convex hull vs Hirzebruch-Jung, independent algorithms
   473 random cones, the two methods agree on every one
```

Totals across both runs: A_n correct for n = 1..8 by both methods;
8567 random cones with every Hirzebruch-Jung expansion having all b_i >= 2
and evaluating exactly to d/q; 1510 random cones where the convex hull and
Hirzebruch-Jung methods agree. No disagreement in any run.
