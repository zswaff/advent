#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
DS = [(0, 1, "v"), (1, 0, ">"), (0, -1, "^"), (-1, 0, "<")]

g = gr(ls)
mxx = max(e[0] for e in g)
mxy = max(e[1] for e in g)

c = 0
q = [(1, 0, {(1, 0)})]
while q:
    x, y, vis = q.pop()
    if x == mxx - 1 and y == mxy:
        c = max(c, len(vis))
        continue
    for dx, dy, d in DS:
        p = nx, ny = x + dx, y + dy
        v = g.get(p, "#")
        if p in vis or v not in {".", d}:
            continue
        q.append((nx, ny, vis | {p}))
sm(c - 1)


# part 2
es = defaultdict(dict)
for x in range(mxx + 1):
    for y in range(mxy + 1):
        p = x, y
        if g.get(p) == "#":
            continue
        for dx, dy, _ in DS:
            np = nx, ny = x + dx, y + dy
            if g.get(np, "#") == "#":
                continue
            es[p][np] = 1
            es[np][p] = 1
changed = True
while changed:
    changed = False
    for p in es:
        if len(es[p]) != 2:
            continue
        changed = True
        (p1, v1), (p2, v2) = es[p].items()
        del es[p]
        del es[p1][p]
        del es[p2][p]
        es[p1][p2] = v1 + v2
        es[p2][p1] = v1 + v2
        break

c = 0
q = [(1, 0, 0, {(1, 0)})]
while q:
    x, y, d, vis = q.pop()
    if x == mxx - 1 and y == mxy:
        c = max(c, d)
        continue
    for p, dd in es[(x, y)].items():
        if p in vis:
            continue
        q.append((*p, d + dd, vis | {p}))
sm(c)
