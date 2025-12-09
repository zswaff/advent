#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
vs = [tuple(int(e) for e in l.split(",")) for l in ls]
ss = []
for i, (x1, y1) in enumerate(vs):
    for j, (x2, y2) in enumerate(vs[i + 1 :], i + 1):
        ss.append((abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))
sm(max(ss))


# part 2
pg = Polygon(vs)
ss = []
for i, (x1, y1) in enumerate(vs):
    for j, (x2, y2) in enumerate(vs[i + 1 :], i + 1):
        mnx, mxx = min(x1, x2), max(x1, x2)
        mny, mxy = min(y1, y2), max(y1, y2)
        pc = Polygon([(mnx, mny), (mnx, mxy), (mxx, mxy), (mxx, mny)])
        if not pg.contains(pc):
            continue
        ss.append((mxx - mnx + 1) * (mxy - mny + 1))
sm(max(ss))
