#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


ls = [eval(e) for e in ls]


def ladd(x, r):
    if r is None:
        return x
    if isinstance(x, int):
        return x + r
    return [ladd(x[0], r), x[1]]


def radd(x, r):
    if r is None:
        return x
    if isinstance(x, int):
        return x + r
    return [x[0], radd(x[1], r)]


def explode(x, d):
    if isinstance(x, int):
        return x, False, None
    if isinstance(x[0], int) and isinstance(x[1], int):
        if d >= 4:
            return 0, True, x
        return x, False, None
    x1, c1, r1 = explode(x[0], d + 1)
    if c1:
        return [x1, ladd(x[1], r1[1])], True, [r1[0], None]
    x2, c2, r2 = explode(x[1], d + 1)
    if c2:
        return [radd(x1, r2[0]), x2], True, [None, r2[1]]
    return x, False, None


def split(x):
    if isinstance(x, int):
        return (x, False) if x < 10 else ([floor(x / 2), ceil(x / 2)], True)
    x1, c1 = split(x[0])
    if c1:
        return [x1, x[1]], True
    x2, c2 = split(x[1])
    return [x1, x2], c2


def add(x1, x2):
    x = [x1, x2]
    while True:
        x, c, _ = explode(x, 0)
        if c:
            continue
        x, c = split(x)
        if c:
            continue
        return x


def mag(x):
    if isinstance(x, int):
        return x
    return 3 * mag(x[0]) + 2 * mag(x[1])


# part 1
x = ls[0]
for l in ls[1:]:
    x = add(x, l)
sm(mag(x))


# part 2
mx = 0
for x in ls:
    for y in ls:
        mx = max(mx, mag(add(x, y)), mag(add(y, x)))
sm(mx)
