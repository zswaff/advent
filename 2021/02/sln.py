#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *
from web import *


# part 1
dirs = {"forward": (1, 0), "down": (0, 1), "up": (0, -1)}
x = y = 0
for l in ls:
    d, m = l.split(" ")
    m = int(m)
    dx, dy = dirs[d]
    x += dx * m
    y += dy * m
sm(x * y)


# part 2
x = y = a = 0
for l in ls:
    d, m = l.split(" ")
    m = int(m)
    if d == "forward":
        x += m
        y += m * a
        continue
    a += m * (1 if d == "down" else -1)
sm(x * y)
