#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


# part 1
ts = [int(e) for e in ls[0][10:].strip().split(" ") if e != ""]
ds = [int(e) for e in ls[1][10:].strip().split(" ") if e != ""]
p = 1
for t, d in zip(ts, ds):
    n = 0
    for i in range(1, t):
        if i * (t - i) > d:
            n += 1
    p *= n
sm(p)


# part 2
t = int(ls[0][10:].replace(" ", ""))
d = int(ls[1][10:].replace(" ", ""))
for i in range(1, t):
    if i * (t - i) > d:
        sm(t - (2 * i) + 1)
        break
