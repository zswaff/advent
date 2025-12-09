#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
vs = []
for l in ls:
    vs.append(tuple(int(e) for e in l.split(",")))
es = []
for i, v1 in enumerate(vs):
    for j, v2 in enumerate(vs[i + 1 :], i + 1):
        es.append((sqrt(sum((e - f) ** 2 for e, f in zip(v1, v2))), i, j))
es.sort()
gps = {i: i for i in range(len(vs))}
for c, (d, i, j) in enumerate(es):
    if c == 1000:
        break
    gi, gj = gps[i], gps[j]
    if gi == gj:
        continue
    for k in range(len(vs)):
        if gps[k] == gi:
            gps[k] = gj
ctr = Counter(gps.values())
sm(prod(e[1] for e in ctr.most_common(3)))


# part 2
gps = {i: i for i in range(len(vs))}
t = len(vs) - 1
c = 0
for d, i, j in es:
    gi, gj = gps[i], gps[j]
    if gi == gj:
        continue
    for k in range(len(vs)):
        if gps[k] == gi:
            gps[k] = gj
    c += 1
    if c == t:
        break
sm(vs[i][0] * vs[j][0])
