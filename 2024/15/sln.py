#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
D = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
X = {".": 0, "#": 1, "O": 2, "@": 3}

rg, ins = ss
g = gr(rg, lambda x: X[x])
c = next(k for k, v in g.items() if v == 3)
g[c] = 0
g = {k: v == 1 for k, v in g.items() if v != 0}

for inst in "".join(ins):
    d = D[inst]
    worked = False
    for i in count(1):
        nc = c[0] + d[0] * i, c[1] + d[1] * i
        if nc not in g:
            worked = True
            break
        if g[nc]:
            break
    if not worked:
        continue
    c = c[0] + d[0], c[1] + d[1]
    if i == 1:
        continue
    g.pop(c)
    g[c[0] + d[0] * (i - 1), c[1] + d[1] * (i - 1)] = False
sm(sum(k[0] + k[1] * 100 for k, v in g.items() if not v))


# part 2
og = gr(rg)
c = next(k for k, v in og.items() if v == "@")
og[c] = "."
c = c[0] * 2, c[1]

g = {}
for (x, y), v in og.items():
    if v == ".":
        continue
    g[x * 2, y] = v if v != "O" else "["
    g[x * 2 + 1, y] = v if v != "O" else "]"

for inst in "".join(ins):
    d = D[inst]
    worked = True
    q = [(c[0] + d[0], c[1] + d[1])]
    m = []
    while q:
        cr = q.pop()
        if cr not in g or cr in m:
            continue
        e = g[cr]
        if e == "#":
            worked = False
            break
        m.append(cr)
        if e == "[":
            q.append((cr[0] + 1, cr[1]))
        elif e == "]":
            q.append((cr[0] - 1, cr[1]))
        q.append((cr[0] + d[0], cr[1] + d[1]))
    if not worked:
        continue
    c = c[0] + d[0], c[1] + d[1]
    ng = {k: v for k, v in g.items() if k not in m}
    for e in m:
        ng[e[0] + d[0], e[1] + d[1]] = g[e]
    g = ng
sm(sum(k[0] + k[1] * 100 for k, v in g.items() if v == "["))
