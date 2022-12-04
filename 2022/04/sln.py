#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


# part 1
c = 0
for l in ls:
    n1, x1, n2, x2 = pa(l, "{i}-{i},{i}-{i}")
    r1 = set(range(n1, x1 + 1))
    r2 = set(range(n2, x2 + 1))
    if (r1 <= r2) or (r2 <= r1):
        c += 1
sm(c)


# part 2
c = 0
for l in ls:
    n1, x1, n2, x2 = pa(l, "{i}-{i},{i}-{i}")
    r1 = set(range(n1, x1 + 1))
    r2 = set(range(n2, x2 + 1))
    if len(r1 & r2) > 0:
        c += 1
sm(c)
