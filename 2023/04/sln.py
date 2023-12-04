#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


# part 1
c = 0
for l in ls:
    spl = l.split(": ")[1].split(" | ")
    wins = set(int(e) for e in spl[0].split(" ") if e)
    yours = set(int(e) for e in spl[1].split(" ") if e)
    mts = len(wins & yours)
    if mts:
        c += 2 ** (mts - 1)
sm(c)


# part 2
c = [1] * len(ls)
for i, l in enumerate(ls):
    spl = l.split(": ")[1].split(" | ")
    wins = set(int(e) for e in spl[0].split(" ") if e)
    yours = set(int(e) for e in spl[1].split(" ") if e)
    mts = len(wins & yours)
    for j in range(1, mts + 1):
        c[i + j] += c[i]
sm(sum(c))
