#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


def combine_ranges(ranges):
    ranges.sort()
    i = 0
    while i < len(ranges) - 1:
        if ranges[i][1] >= ranges[i + 1][0]:
            ranges[i] = (ranges[i][0], max(ranges[i][1], ranges[i + 1][1]))
            del ranges[i + 1]
        else:
            i += 1
    return ranges


# part 1
g = []
b = set()
for l in ls:
    sx, sy, bx, by = pa(l, "Sensor at x={i}, y={i}: closest beacon is at x={i}, y={i}")
    if by == 2000000:
        b.add(bx)
    md = abs(sx - bx) + abs(sy - by)
    rm = md - abs(sy - 2000000)
    if rm < 0:
        continue
    g.append((sx - rm, sx + rm))
g = combine_ranges(g)
sm(sum(en - st + 1 for st, en in g) - len(b))


# part 2
for y in range(4000001):
    g = []
    for l in ls:
        sx, sy, bx, by = pa(l, "Sensor at x={i}, y={i}: closest beacon is at x={i}, y={i}")
        if by == y:
            b.add(bx)
        md = abs(sx - bx) + abs(sy - by)
        rm = md - abs(sy - y)
        if rm < 0:
            continue
        g.append((sx - rm, sx + rm))
    g = combine_ranges(g)
    if len(g) != 1:
        print(g, y)
        x = set(range(0, 4000001))
        for st, en in g:
            x -= set(range(st, en + 1))
        if len(x) != 1:
            continue
        sm(list(x)[0] * 4000000 + y)
        break
