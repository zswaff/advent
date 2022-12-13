#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from functools import cmp_to_key

from common import *


def rec(p1, p2):
    l1, l2 = isinstance(p1, list), isinstance(p2, list)
    if not l1 and not l2:
        return 1 if p1 < p2 else (-1 if p1 > p2 else 0)
    if l1 and l2:
        for i in range(max(len(p1), len(p2))):
            if i >= len(p1):
                return 1
            if i >= len(p2):
                return -1
            r = rec(p1[i], p2[i])
            if r != 0:
                return r
        return 0
    return rec((p1 if l1 else [p1]), (p2 if l2 else [p2]))


# part 1
c = 0
for i, (p1, p2) in enumerate(ss, 1):
    if rec(eval(p1), eval(p2)) == 1:
        c += i
sm(c)


# part 2
d1, d2 = [[2]], [[6]]
x = [d1, d2] + [eval(e) for e in ls if e != ""]
x.sort(key=cmp_to_key(rec), reverse=True)
sm((x.index(d1) + 1) * (x.index(d2) + 1))
