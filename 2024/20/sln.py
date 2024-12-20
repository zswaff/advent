#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
DS = ((0, -1), (1, 0), (0, 1), (-1, 0))

g = gr()
st = next(k for k, v in g.items() if v == "S")
en = next(k for k, v in g.items() if v == "E")
g = {k for k, v in g.items() if v != "#"}
d = {}
c = st
v = set()
for i in count():
    d[c] = i
    if c == en:
        break
    v.add(c)
    for dx, dy in DS:
        ne = c[0] + dx, c[1] + dy
        if ne in g and ne not in v:
            break
    c = ne

c = 0
for e in d:
    for dx, dy in DS:
        ne = e[0] + dx * 2, e[1] + dy * 2
        if ne in d and d[ne] >= d[e] + 102:
            c += 1
sm(c)


# part 2
c = 0
for e in d:
    for dx in range(-20, 21):
        adx = abs(dx)
        ldy = 20 - adx
        for dy in range(-ldy, ldy + 1):
            ne = e[0] + dx, e[1] + dy
            if ne in d and d[ne] >= d[e] + 100 + adx + abs(dy):
                c += 1
sm(c)
