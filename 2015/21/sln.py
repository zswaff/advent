#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


bh = 103
bd = 9
ba = 2

def fight(h, d, a):
    cbh = 103
    ch = h
    while True:
        cbh -= max(d - ba, 1)
        if cbh <= 0:
            return True
        ch -= max(bd - a, 1)
        if ch <= 0:
            return False

sws = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0)
]
sas = [
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
    (0, 0, 0)
]
srs = [
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
    (0, 0, 0),
    (0, 0, 0)
]


# part 1
m = math.inf
for w1 in sws:
    for a1 in sas:
        for i, r1 in enumerate(srs):
            for r2 in srs[i + 1:]:
                c, d, a = [sum(e) for e in zip(w1, a1, r1, r2)]
                if fight(100, d, a):
                    m = min(m, c)
print(m)


# part 2
m = 0
for w1 in sws:
    for a1 in sas:
        for i, r1 in enumerate(srs):
            for r2 in srs[i + 1:]:
                c, d, a = [sum(e) for e in zip(w1, a1, r1, r2)]
                if not fight(100, d, a):
                    m = max(m, c)
print(m)
