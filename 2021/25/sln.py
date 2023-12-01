#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


# part 1
g = gr(ls)
mxx, mxy = max(e[0] for e in g.keys()) + 1, max(e[1] for e in g.keys()) + 1
for i in count(1):
    c = 0
    ng = {k: "v" if v == "v" else "." for k, v in g.items()}
    for k, v in g.items():
        if v != ">":
            continue
        nk = (k[0] + 1) % mxx, k[1]
        if g[nk] == ".":
            ng[nk] = v
            c += 1
        else:
            ng[k] = v
    same = ng == g
    g = ng
    ng = {k: ">" if v == ">" else "." for k, v in g.items()}
    for k, v in g.items():
        if v != "v":
            continue
        nk = k[0], (k[1] + 1) % mxy
        if g[nk] == ".":
            ng[nk] = v
            c += 1
        else:
            ng[k] = v
    if same and ng == g:
        break
    g = ng
sm(i)
