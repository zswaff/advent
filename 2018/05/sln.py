#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
def fn(ld):
    l = len(ld)
    while True:
        rm = set()
        for i, e in enumerate(ld[:-1]):
            if i in rm:
                continue
            f = ld[i+1]
            if e != f and e.lower() == f.lower():
                rm |= {i, i + 1}
        ld = [c for i, c in enumerate(ld) if i not in rm]
        nl = len(ld)
        if nl == l:
            break
        l = nl
    return l
sm(fn(list(dt)))


# part 2
cs = set(e.lower() for e in dt)
sm(min(fn([f for f in dt if f.lower() != e]) for e in cs))
