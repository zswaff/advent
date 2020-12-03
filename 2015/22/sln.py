#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


# psh = 50
# psm = 500
# bh = 55
# bd = 8
psh = 10
psm = 250
bh = 13
bd = 8


# part 1
def rec(ch, cm, cbh, fx):
    for f, t in fx.items():
        if t <= 0:
            continue
        if f == 'p':
            cbh -= 3
        if f == 'r':
            cm += 101
        fx[f] -= 1
    if cbh <= 0:
        return 0, [' ']

    m = math.inf, [' ']
    for e in ['m', 'd', 's', 'p', 'r']:
        if fx.get(e, 0) > 0:
            continue
        nfx = dict(fx.items())
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
            nfx[e] = 6
        if e == 'p':
            cost = 173
            nfx[e] = 6
        if e == 'r':
            cost = 229
            nfx[e] = 5
        if cm < cost:
            continue

        a = 0
        for f, t in nfx.items():
            if t <= 0:
                continue
            if f == 's':
                a = 7
            if f == 'p':
                cbh -= 3
            if f == 'r':
                cm += 101
            nfx[f] -= 1
        if cbh <= 0:
            m = min(m, (cost, [e]))

        d = max(bd - a, 1)
        if ch <= d:
            continue
        ncost, ne = rec(ch - d, cm - cost, cbh, nfx)
        m = min(m, (cost + ncost, ne + [e]))
    return m

print(rec(psh, psm, bh, {}))


# part 2
