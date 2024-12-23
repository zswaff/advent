#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
ns = [int(l) for l in ls]
for _ in range(2000):
    for i, e in enumerate(ns):
        e = (e ^ (e << 6)) % 16777216
        e = (e ^ (e >> 5)) % 16777216
        e = (e ^ (e << 11)) % 16777216
        ns[i] = e
sm(sum(ns))


# part 2
ns = [int(l) for l in ls]
ds = defaultdict(int)
for i, e in enumerate(ns):
    c = e
    r = [c]
    dr = []
    v = set()
    for _ in range(2000):
        c = (c ^ (c << 6)) % 16777216
        c = (c ^ (c >> 5)) % 16777216
        c = (c ^ (c << 11)) % 16777216
        x = c % 10
        dr.append(x - r[-1])
        r.append(x)
        if len(dr) < 4:
            continue
        k = tuple(dr[-4:])
        if k in v:
            continue
        v.add(k)
        ds[k] += x
sm(max(ds.values()))
