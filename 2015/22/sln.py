#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


bh = 55
bd = 8


# part 1
def rec(ch, cm, cbh, fx):
    a = 0
    for e, t in fx.items():
        if t <= 0:
            continue
        if e == 's':
            a += 7
        if e == 'p':
            cbh -= 3
        if e == 'r':
            cm += 101
        fx[e] -= 1
    if cbh <= 0:
        return 0
    m = math.inf
    for e in ['m', 'd', 's', 'p', 'r']:
        if fx.get(e, 0) > 0:
            continue
        cost = 0
        if e == 'm':
            cost = 53
            cbh -= 4
        if e == 'd':
            cost = 73
            cbh -= 2
            ch += 2
        if e == 's':
            cost = 113
            fx[e] = 6
        if e == 'p':
            cost = 173
            fx[e] = 6
        if e == 'r':
            cost = 229
            fx[e] = 5
        if cm < cost:
            continue
        if cbh <= 0:
            m = min(m, cost)

        ch -= max(bd - a, 1)
        if ch > 0:
            m = min(m, rec(ch, cm - cost, cbh, dict(fx.items())) + cost)
    return m

print(rec(50, 500, 55, {}))


# part 2
