#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


DIRS = [(0, 1), (-1, 1), (1, 1)]

# part 1
g = {}
for l in ls:
    lx = ly = None
    for p in l.split(" -> "):
        x, y = pa(p, "{i},{i}")
        if lx is not None:
            if x == lx:
                g.update({(x, i): True for i in range(min(y, ly), max(y, ly) + 1)})
            else:
                g.update({(i, y): True for i in range(min(x, lx), max(x, lx) + 1)})
        lx, ly = x, y
mxy = max(y for _, y in g)
for i in count():
    done = False
    cx, cy = 500, 0
    while True:
        if cy == mxy:
            done = True
            break
        settled = True
        for dx, dy in DIRS:
            if (cx + dx, cy + dy) in g:
                continue
            settled = False
            cx += dx
            cy += dy
            break
        if settled:
            g[(cx, cy)] = False
            break
    if done:
        break
sm(i)


# part 2
g = {}
for l in ls:
    lx = ly = None
    for p in l.split(" -> "):
        x, y = pa(p, "{i},{i}")
        if lx is not None:
            if x == lx:
                g.update({(x, i): True for i in range(min(y, ly), max(y, ly) + 1)})
            else:
                g.update({(i, y): True for i in range(min(x, lx), max(x, lx) + 1)})
        lx, ly = x, y
mxy = max(y for _, y in g) + 1
for i in count():
    cx, cy = 500, 0
    if (cx, cy) in g:
        break
    while True:
        settled = True
        for dx, dy in DIRS:
            if (cx + dx, cy + dy) in g:
                continue
            settled = False
            cx += dx
            cy += dy
            break
        if settled or cy == mxy:
            g[(cx, cy)] = False
            break
sm(i)
