#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


def mx_and_amx(vs):
    mx = max(vs)
    amx = vs.index(mx)
    return mx, amx


# part 1
c = 0
for l in ls:
    iss = [int(e) for e in l]
    mx1, amx = mx_and_amx(iss[:-1])
    mx2 = max(iss[amx + 1 :])
    c += mx1 * 10 + mx2
sm(c)


# part 2
c = 0
for l in ls:
    iss = [int(e) for e in l]
    x = 0
    for i in range(11, -1, -1):
        mx, amx = mx_and_amx(iss[x : (-i or None)])
        c += mx * 10**i
        x += amx + 1
sm(c)
