#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
g = defaultdict(set)
for e, f in pas("{}-{}"):
    g[e].add(f)
    g[f].add(e)

c = set()
for k, vs in g.items():
    if k[0] != "t":
        continue
    for e, f in combinations(vs, 2):
        if f not in g[e]:
            continue
        c.add(tuple(sorted([k, e, f])))
sm(len(c))


# part 2
while True:
    nc = set()
    for e in c:
        se = set(e)
        v = e[0]
        for nv in g[v]:
            if nv in se or se - g[nv]:
                continue
            nc.add(tuple(sorted(e + (nv,))))
    if not nc:
        break
    c = nc
sm(",".join(list(c)[0]))
