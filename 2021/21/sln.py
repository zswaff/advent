#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


oo = int(ls[0].split(" ")[-1])
ot = int(ls[1].split(" ")[-1])


# part 1
o, t = oo, ot
os = ts = 0
d = count(1)
n = True
while os < 1000 and ts < 1000:
    if n:
        o = (o + next(d) + next(d) + next(d) - 1) % 10 + 1
        os += o
    else:
        t = (t + next(d) + next(d) + next(d) - 1) % 10 + 1
        ts += t
    n = not n
sm(min(os, ts) * (next(d) - 1))


# part 2
def rec(o, t, os, ts, n):
    if os >= 21:
        return 1, 0
    if ts >= 21:
        return 0, 1
    ow = tw = 0
    for r, p in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
        if n:
            no = (o + r - 1) % 10 + 1
            co, ct = rec(no, t, os + no, ts, False)
        else:
            nt = (t + r - 1) % 10 + 1
            co, ct = rec(o, nt, os, ts + nt, True)
        ow += p * co
        tw += p * ct
    return ow, tw


sm(max(rec(oo, ot, 0, 0, True)))
