#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *
from web import *


# part 1
ln = len(ls[0])
cs = [Counter([e[i] for e in ls]) for i in range(ln)]
gams = "".join(e.most_common()[0][0] for e in cs)
lams = "".join("1" if e == "0" else "0" for e in gams)
sm(int(gams, 2) * int(lams, 2))


# part 2
w = list(ls)
for i in range(ln):
    os, zs = [e for e in w if e[i] == "1"], [e for e in w if e[i] == "0"]
    w = os if len(os) >= len(zs) else zs
    if len(w) == 1:
        break
ox = int(w[0], 2)
w = list(ls)
for i in range(ln):
    os, zs = [e for e in w if e[i] == "1"], [e for e in w if e[i] == "0"]
    w = os if len(os) < len(zs) else zs
    if len(w) == 1:
        break
sm(ox * int(w[0], 2))
