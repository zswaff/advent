#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *
from web import *


# part 1
c = Counter()
for l in ls:
    spl = l.split(" -> ")
    x1, y1 = (int(e) for e in spl[0].split(","))
    x2, y2 = (int(e) for e in spl[1].split(","))
    if x1 == x2:
        ymn, ymx = min(y1, y2), max(y1, y2)
        for y in range(ymn, ymx + 1):
            c[(x1, y)] += 1
    if y1 == y2:
        xmn, xmx = min(x1, x2), max(x1, x2)
        for x in range(xmn, xmx + 1):
            c[(x, y1)] += 1
sm(sum(1 for e in c.values() if e > 1))


# part 2
c = Counter()
for l in ls:
    spl = l.split(" -> ")
    x1, y1 = (int(e) for e in spl[0].split(","))
    x2, y2 = (int(e) for e in spl[1].split(","))
    if x1 == x2:
        ymn, ymx = min(y1, y2), max(y1, y2)
        for y in range(ymn, ymx + 1):
            c[(x1, y)] += 1
        continue
    if y1 == y2:
        xmn, xmx = min(x1, x2), max(x1, x2)
        for x in range(xmn, xmx + 1):
            c[(x, y1)] += 1
        continue
    xs = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
    ys = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
    for x, y in zip(xs, ys):
        c[(x, y)] += 1
sm(sum(1 for e in c.values() if e > 1))
