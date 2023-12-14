#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json

from bidict import bidict

from common import *


# part 1
g = gr(ls)
mx = max(e[0] for e in g)
my = max(e[1] for e in g)
c = 0
for x in range(mx + 1):
    l = -1
    for y in range(my + 1):
        v = g[(x, y)]
        if v == "O":
            c += my - l
            l += 1
            continue
        if v == "#":
            l = y
sm(c)


# part 2
g = {k: v for k, v in gr(ls).items() if v != "."}
mx = max(e[0] for e in g)
my = max(e[1] for e in g)
sts = bidict({json.dumps(sorted(g.items())): 0})
for i in count(1):
    ng = {}
    for x in range(mx + 1):
        l = -1
        for y in range(my + 1):
            p = x, y
            v = g.get(p)
            if v is None:
                continue
            if v == "#":
                l = y
                ng[p] = v
                continue
            if v == "O":
                l += 1
                ng[(x, l)] = v
    g = ng
    ng = {}
    for y in range(my + 1):
        l = -1
        for x in range(mx + 1):
            p = x, y
            v = g.get(p)
            if v is None:
                continue
            if v == "#":
                l = x
                ng[p] = v
                continue
            if v == "O":
                l += 1
                ng[(l, y)] = v
    g = ng
    ng = {}
    for x in range(mx + 1):
        l = my + 1
        for y in range(my, -1, -1):
            p = x, y
            v = g.get(p)
            if v is None:
                continue
            if v == "#":
                l = y
                ng[p] = v
                continue
            if v == "O":
                l -= 1
                ng[(x, l)] = v
    g = ng
    ng = {}
    for y in range(my + 1):
        l = mx + 1
        for x in range(mx, -1, -1):
            p = x, y
            v = g.get(p)
            if v is None:
                continue
            if v == "#":
                l = x
                ng[p] = v
                continue
            if v == "O":
                l -= 1
                ng[(l, y)] = v
    g = ng
    k = json.dumps(sorted(g.items()))
    if k in sts:
        o = sts[k]
        dt = (1000000000 - o) % (i - o) + o
        break
    sts[k] = i
g = json.loads(sts.inverse[dt])
sm(sum(my - k[1] + 1 for k, v in g if v == "O"))
