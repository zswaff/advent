#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *
from web import *


# part 1
cs = [[tuple(int(f) for f in e.split(","))] for e in ls]
lc = inf
while len(cs) != lc:
    lc = len(cs)
    ncs = [cs[0]]
    for nc in cs[1:]:
        for oc in ncs:
            if any(sum(abs(v1 - v2) for v1, v2 in zip(*e)) <= 3 for e in product(nc, oc)):
                oc += nc
                break
        else:
            ncs.append(nc)
    cs = ncs
sm(lc)
