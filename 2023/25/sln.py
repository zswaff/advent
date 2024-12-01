#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
g = defaultdict(set)
for l in ls:
    a, rbs = l.split(": ")
    bs = rbs.split(" ")
    g[a] |= set(bs)
    for b in bs:
        g[b].add(a)

s = set(g)
while sum(len(g[e] - s) for e in s) != 3:
    v = max(s, key=lambda x: len(g[x] - s))
    s.remove(v)
sm(len(s) * len(set(g) - s))
