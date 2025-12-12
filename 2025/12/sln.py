#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
pas = ["".join(e).count("#") for e in ss[:-1]]
c = 0
for e in ss[-1]:
    x, y, cs = pa("{i}x{i}: {}", e)
    if sum(pas[i] * int(f) for i, f in enumerate(cs.split())) <= x * y:
        c += 1
sm(c)


# part 2
