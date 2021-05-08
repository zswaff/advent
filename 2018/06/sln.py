#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


ps = [tuple(int(f) for f in e.split(',')) for e in ls]


# part 1
mnx = min(e[0] for e in ps)
mxx = max(e[0] for e in ps)
mny = min(e[1] for e in ps)
mxy = max(e[1] for e in ps)
d = [0] * len(ps)
for x in range(mnx - 10, mxx + 11):
    for y in range(mnx - 10, mxx + 11):
        ds = sorted(
            (abs(x - px) + abs(y - py), i)
            for i, (px, py) in enumerate(ps)
        )
        if ds[0][0] != ds[1][0]:
            d[ds[0][1]] += 1
d2 = [0] * len(ps)
for x in range(mnx - 11, mxx + 12):
    for y in range(mnx - 11, mxx + 12):
        ds = sorted(
            (abs(x - px) + abs(y - py), i)
            for i, (px, py) in enumerate(ps)
        )
        if ds[0][0] != ds[1][0]:
            d2[ds[0][1]] += 1
sm(max(e for e, f in zip(d, d2) if e == f))




# part 2
c = 0
for x in range(mnx - 200, mxx + 201):
    for y in range(mnx - 200, mxx + 201):
        tot = sum(abs(x - px) + abs(y - py) for i, (px, py) in enumerate(ps))
        if tot < 10000:
            c += 1
sm(c)
