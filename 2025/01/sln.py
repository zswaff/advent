#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
c = 0
p = 50
for l in ls:
    d = 1 if l[0] == "L" else -1
    n = int(l[1:])
    p = (p + (n * d)) % 100
    if p == 0:
        c += 1
sm(c)


# part 2
c = 0
p = 50
for l in ls:
    d = l[0] == "R"
    n = int(l[1:])
    if d:
        p += n
        while p >= 100:
            c += 1
            p -= 100
    else:
        if p == 0:
            c -= 1
        p -= n
        while p < 0:
            p += 100
            c += 1
        if p == 0:
            c += 1
    print(l, p, c)
sm(c)
