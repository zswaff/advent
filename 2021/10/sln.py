#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *
from web import *


PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}


# part 1
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
c = 0
for l in ls:
    s = []
    for e in l:
        if e not in scores:
            s.append(e)
            continue
        f = s.pop()
        if e != PAIRS[f]:
            c += scores[e]
            break
sm(c)


# part 2
scores = {")": 1, "]": 2, "}": 3, ">": 4}
cs = []
for l in ls:
    s = []
    for e in l:
        if e not in scores:
            s.append(e)
            continue
        f = s.pop()
        if e != PAIRS[f]:
            break
    else:
        c = 0
        for e in reversed(s):
            c *= 5
            c += scores[PAIRS[e]]
        cs.append(c)
sm(sorted(cs)[len(cs) // 2])
