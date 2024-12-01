#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *
from web import *


FNS = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda y: int(y[0] > y[1]),
    6: lambda y: int(y[0] < y[1]),
    7: lambda y: int(y[0] == y[1]),
}


d = bin(int(dt, 16))[2:].zfill(len(dt) * 4)


def p(s):
    v = int(s[:3], 2)
    t = int(s[3:6], 2)
    if t == 4:
        c = ""
        x = 6
        while s[x] == "1":
            c += s[x + 1 : x + 5]
            x += 5
        return v, int(c + s[x + 1 : x + 5], 2), x + 5
    i = s[6]
    if i == "0":
        l = int(s[7:22], 2)
        tv = v
        rs = []
        x = 22
        while l > x - 22:
            cv, cr, cx = p(s[x:])
            tv += cv
            rs.append(cr)
            x += cx
    else:
        l = int(s[7:18], 2)
        tv = v
        rs = []
        x = 18
        for j in range(l):
            cv, cr, cx = p(s[x:])
            tv += cv
            rs.append(cr)
            x += cx
    r = FNS[t](rs)
    return tv, r, x


# part 1
sm(p(d)[0])


# part 2
sm(p(d)[1])
