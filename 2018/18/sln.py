#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *
from web import *


og = {(x, y): c for y, l in enumerate(ls) for x, c in enumerate(l)}


# part 1
g = og
for _ in range(10):
    ng = {}
    for x in range(50):
        for y in range(50):
            c = g[(x, y)]
            nbs = Counter(
                g[(x + dx, y + dy)]
                for dx in range(-1, 2) for dy in range(-1, 2)
                if not dx == dy == 0 and (x + dx, y + dy) in g
            )
            if c == '.':
                ng[(x, y)] = '|' if nbs['|'] >= 3 else '.'
            if c == '|':
                ng[(x, y)] = '#' if nbs['#'] >= 3 else '|'
            if c == '#':
                ng[(x, y)] = '#' if nbs['#'] >= 1 and nbs['|'] >= 1 else '.'
    g = ng
t = Counter(g.values())
sm(t['|'] * t['#'])


# part 2
ss = {}
cs = {}
g = og
for i in range(int(1e9)):
    ng = {}
    s = ''
    for x in range(50):
        for y in range(50):
            c = g[(x, y)]
            nbs = Counter(
                g[(x + dx, y + dy)]
                for dx in range(-1, 2) for dy in range(-1, 2)
                if not dx == dy == 0 and (x + dx, y + dy) in g
            )
            if c == '.':
                ng[(x, y)] = '|' if nbs['|'] >= 3 else '.'
            if c == '|':
                ng[(x, y)] = '#' if nbs['#'] >= 3 else '|'
            if c == '#':
                ng[(x, y)] = '#' if nbs['#'] >= 1 and nbs['|'] >= 1 else '.'
            s += ng[(x, y)]
    if s in ss:
        break
    ss[s] = i
    g = ng
    t = Counter(g.values())
    cs[i] = t['|'] * t['#']
oi = ss[s]
sm(cs[(int(1e9) - oi) % (i - oi) + oi - 1])
