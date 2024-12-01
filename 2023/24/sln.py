#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


vs = [[[int(f) for f in e.split(", ")] for e in l.split(" @ ")] for l in ls]
c = 0
for i, v1 in enumerate(vs):
    (x1, y1, _), (dx1, dy1, _) = v1
    for v2 in vs[i + 1 :]:
        (x2, y2, _), (dx2, dy2, _) = v2
        denom = dy2 * dx1 - dx2 * dy1
        if denom == 0:
            continue
        t1 = (dx2 * (y1 - y2) - dy2 * (x1 - x2)) / denom
        t2 = (x1 + dx1 * t1 - x2) / dx2
        x = x1 + dx1 * t1
        y = y1 + dy1 * t1
        if (
            t1 > 0
            and t2 > 0
            and 200000000000000 <= x <= 400000000000000
            and 200000000000000 <= y <= 400000000000000
        ):
            c += 1
sm(c)


# part 2
vs2 = [[*e, *f] for e, f in vs]
res = z3.RealVector("r", 6)
t = z3.RealVector("t", 3)
s = z3.Solver()
for d in range(3):
    for e, v in zip(t, vs2):
        s.add(res[d] + res[d + 3] * e == v[d] + v[d + 3] * e)
s.check()
m = s.model()
sm(m.eval(sum(res[:3])))
