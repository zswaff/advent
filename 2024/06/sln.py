#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
DS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

g = gr()
oga = next(k for k, v in g.items() if v == "^")
g[oga] = "."

ga = oga
d = 0
v = {ga}
while True:
    nga = (ga[0] + DS[d][0], ga[1] + DS[d][1])
    if nga not in g:
        break
    if g[nga] == "#":
        d = (d + 1) % 4
        continue
    v.add(nga)
    ga = nga
sm(len(v))


# part 2
c = 0
for k, v in g.items():
    if v == "#":
        continue
    ga = oga
    d = 0
    v = set()
    while True:
        if (ga, d) in v:
            c += 1
            break
        v.add((ga, d))
        nga = (ga[0] + DS[d][0], ga[1] + DS[d][1])
        if nga not in g:
            break
        if g[nga] == "#" or nga == k:
            d = (d + 1) % 4
            continue
        ga = nga
sm(c)
