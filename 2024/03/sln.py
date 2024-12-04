#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
c = 0
for a, b in apa("mul({i},{i})", dt):
    c += a * b
sm(c)


# part 2
c = 0
on = True
for i, r in apa(["mul({i},{i})", "do()", "don't()"], dt):
    if i != 0:
        on = i == 1
        continue
    if on:
        c += r[0] * r[1]
sm(c)
