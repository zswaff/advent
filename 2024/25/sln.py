#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
ks, ls = [], []
for s in ss:
    g = gr(s, lambda x: x == "#")
    l = []
    for x in range(5):
        l.append(sum(g[x, y] for y in range(1, 6)))
    if g[0, 0]:
        ls.append(l)
    else:
        ks.append(l)

c = 0
for k in ks:
    for l in ls:
        if all(sum(e) <= 5 for e in zip(k, l)):
            c += 1
sm(c)


# part 2
