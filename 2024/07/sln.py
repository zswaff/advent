#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
def rec(vs, target):
    if len(vs) == 1:
        return vs[0] == target
    if rec([vs[0] + vs[1]] + vs[2:], target):
        return True
    return rec([vs[0] * vs[1]] + vs[2:], target)


c = 0
for l in ls:
    x, y = pa("{i}: {}", l)
    ys = [int(e) for e in y.split(" ")]
    if rec(ys, x):
        c += x
sm(c)


# part 2
def rec(vs, target):
    if len(vs) == 1:
        return vs[0] == target
    if rec([vs[0] + vs[1]] + vs[2:], target):
        return True
    if rec([vs[0] * vs[1]] + vs[2:], target):
        return True
    return rec([int(str(vs[0]) + str(vs[1]))] + vs[2:], target)


c = 0
for l in ls:
    x, y = pa("{i}: {}", l)
    ys = [int(e) for e in y.split(" ")]
    if rec(ys, x):
        c += x
sm(c)
