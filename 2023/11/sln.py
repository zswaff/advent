#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


# part 1
nls = []
for l in ls:
    nls.append(l)
    if all(e == "." for e in l):
        nls.append(l)
nnls = [""] * len(nls)
for i in range(len(nls[0])):
    nl = [e[i] for e in nls]
    x = all(e == "." for e in nl)
    for j in range(len(nls)):
        nnls[j] += nl[j] * (2 if x else 1)

g = gr(nnls)
pts = [k for k, v in g.items() if v == "#"]
c = 0
for i, e in enumerate(pts):
    for f in pts[i + 1 :]:
        c += abs(e[0] - f[0]) + abs(e[1] - f[1])
sm(c)


# part 2
rs = {i for i in range(len(ls)) if all(e == "." for e in ls[i])}
cs = {i for i in range(len(ls[0])) if all(e == "." for e in [l[i] for l in ls])}

g = gr(ls)
pts = [k for k, v in g.items() if v == "#"]
c = 0
for i, e in enumerate(pts):
    for f in pts[i + 1 :]:
        mnx = min(e[0], f[0])
        mxx = max(e[0], f[0])
        mny = min(e[1], f[1])
        mxy = max(e[1], f[1])
        c += mxx - mnx + mxy - mny
        c += 999999 * sum(1 for e in range(mnx + 1, mxx) if e in cs)
        c += 999999 * sum(1 for e in range(mny + 1, mxy) if e in rs)
sm(c)
