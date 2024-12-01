#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
def works_x(g, x):
    for dx in count():
        for y in range(0, my):
            pl = x - dx - 1, y
            pm = x + dx, y
            if pl not in g or pm not in g:
                return True
            if g[pl] != g[pm]:
                return False


def works_y(g, y):
    for dy in count():
        for x in range(0, mx):
            pl = x, y - dy - 1
            pm = x, y + dy
            if pl not in g or pm not in g:
                return True
            if g[pl] != g[pm]:
                return False


c = 0
for s in ss:
    g = gr(s)
    mx = max(e[0] for e in g) + 1
    my = max(e[1] for e in g) + 1
    for x in range(1, mx):
        if works_x(g, x):
            c += x
    for y in range(1, my):
        if works_y(g, y):
            c += y * 100
sm(c)


# part 2
def fold(g, mx, my, ignore=0):
    for x in range(1, mx):
        if works_x(g, x):
            res = x
            if res != ignore:
                return res
    for y in range(1, my):
        if works_y(g, y):
            res = y * 100
            if res != ignore:
                return res
    return 0


c = 0
for s in ss:
    g = gr(s)
    mx = max(e[0] for e in g) + 1
    my = max(e[1] for e in g) + 1
    old = fold(g, mx, my)
    for k, v in g.items():
        new = fold(g | {k: "." if v == "#" else "#"}, mx, my, old)
        if new != 0 and new != old:
            c += new
            break
sm(c)
