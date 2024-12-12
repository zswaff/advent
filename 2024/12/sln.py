#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
g = gr()
rs = {k: i for i, k in enumerate(g.keys())}
for (x, y), ov in tqdm(g.items()):
    for dx, dy in [(1, 0), (0, 1)]:
        nx, ny = x + dx, y + dy
        nv = g.get((nx, ny), None)
        if nv != ov:
            continue
        org, nrg = rs[x, y], rs[nx, ny]
        rs = {k: (v if v != nrg else org) for k, v in rs.items()}
rrs = defaultdict(set)
for k, v in rs.items():
    rrs[v].add(k)
c = 0
for k, v in rrs.items():
    lv = len(v)
    p = lv * 4
    for x, y in v:
        for dx, dy in [(1, 0), (0, 1)]:
            if (x + dx, y + dy) not in v:
                continue
            p -= 2
    c += p * lv
sm(c)


# part 2
c = 0
for k, v in rrs.items():
    lv = len(v)
    p = set()
    for x, y in v:
        p ^= {(2 * x + dx, 2 * y + dy) for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]}
    d = len(p)
    for x, y in p:
        dx, dy = (2, 0) if x % 2 == 0 else (0, 2)
        if (x + dx, y + dy) not in p or (x + 1, y + 1) in p:
            continue
        d -= 1
    c += d * lv
sm(c)
