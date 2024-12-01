#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *
from web import *


# part 1
g = {(x, y): int(e) for y, l in enumerate(ls) for x, e in enumerate(l)}
c = 0
for _ in range(100):
    ng = {k: v + 1 for k, v in g.items()}
    z = {k for k, v in ng.items() if v > 9}
    q = list(z)
    while q:
        w = q.pop()
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == dy == 0:
                    continue
                dw = w[0] + dx, w[1] + dy
                if dw not in ng or dw in z:
                    continue
                ng[dw] += 1
                if ng[dw] <= 9:
                    continue
                z.add(dw)
                q.append(dw)
    g = {k: 0 if k in z else v for k, v in ng.items()}
    c += len(z)
sm(c)


# part 2
g = {(x, y): int(e) for y, l in enumerate(ls) for x, e in enumerate(l)}
for itr in count():
    ng = {k: v + 1 for k, v in g.items()}
    z = {k for k, v in ng.items() if v > 9}
    q = list(z)
    while q:
        w = q.pop()
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == dy == 0:
                    continue
                dw = w[0] + dx, w[1] + dy
                if dw not in ng or dw in z:
                    continue
                ng[dw] += 1
                if ng[dw] <= 9:
                    continue
                z.add(dw)
                q.append(dw)
    g = {k: 0 if k in z else v for k, v in ng.items()}
    if len(z) == len(g):
        break
sm(itr + 1)
