#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
g = gr()
h, w = len(ls), len(ls[0])
c = 0
for y in range(1, h):
    for x in range(w):
        s = g[(x, y)]
        if g[(x, y - 1)] not in {"|", "S"}:
            continue
        if s == ".":
            g[(x, y)] = "|"
            continue
        if s == "^":
            g[(x - 1, y)] = g[(x + 1, y)] = "|"
            c += 1
sm(c)


# part 2
R = {"^": "^", "S": 1, ".": 0}
g = gr(ls, lambda x: R[x])
for y in range(1, h):
    for x in range(w):
        s = g[(x, y)]
        ps = g[(x, y - 1)]
        if ps in {0, "^"}:
            continue
        if s == "^":
            g[(x - 1, y)] += ps
            g[(x + 1, y)] += ps
            continue
        g[(x, y)] += ps
sm(sum(e for e in [g[(i, h - 1)] for i in range(w)] if e != "^"))
