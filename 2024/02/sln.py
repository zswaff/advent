#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
c = 0
for l in ls:
    x = [int(e) for e in l.split()]
    if x[0] < x[1]:
        x.reverse()
    ds = [x[i] - x[i + 1] for i in range(0, len(x) - 1)]
    if all(1 <= e <= 3 for e in ds):
        c += 1
sm(c)


# part 2
def f(x):
    ds = [x[i] - x[i + 1] for i in range(0, len(x) - 1)]
    return all(1 <= e <= 3 for e in ds)


c = 0
for l in ls:
    x = [int(e) for e in l.split()]
    xr = list(reversed(x))
    if (
        f(x)
        or any(f(x[:i] + x[i + 1 :]) for i in range(len(x)))
        or f(xr)
        or any(f(xr[:i] + xr[i + 1 :]) for i in range(len(xr)))
    ):
        c += 1
sm(c)
