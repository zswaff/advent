#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from math import inf
from itertools import count

from web import *


ps = [
    [
        tuple(int(f) for f in e.split('<')[1].split(','))
        for e in l[:-1].split('> ')
    ]
    for l in ls
]


# part 1
dist = inf
sz = len(ps)
for i in count():
    nps = []
    for j in range(sz):
        (px, py), (vx, vy) = ps[j]
        nps.append([(px + vx, py + vy), (vx, vy)])
    cx, cy = sum(e[0][0] for e in nps) / sz, sum(e[0][1] for e in nps) / sz
    tot = sum(abs(e[0][0] - cx) + abs(e[0][0] - cx) for e in nps)
    if tot > dist:
        break
    dist = tot
    ps = nps
s = {tuple(e[0]) for e in ps}
mnx, mxx = min(e[0] for e in s), max(e[0] for e in s)
mny, mxy = min(e[1] for e in s), max(e[1] for e in s)
for y in range(mny, mxy+1):
    for x in range(mnx, mxx+1):
        print('#' if (x, y) in s else '.', end='')
    print()
sm('GPJLLLLH')

# part 2
sm(i)
