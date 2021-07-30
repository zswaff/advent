#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *
from web import *


dpt, trg = ls
dpt = int(dpt.split(' ')[1])
tx, ty = (int(e) for e in trg.split(' ')[1].split(','))

g = {(0, 0): 0, (tx, ty): 0}
t = {}
for y in range(0, ty + 1):
    print(y, len(g))
    for x in range(0, tx + 1):
        if (x, y) in g:
            continue
        if y == 0:
            g[(x, y)] = x * 16807
            continue
        if x == 0:
            g[(x, y)] = y * 48271
            continue
        g[(x, y)] = g[(x - 1, y)] * g[(x, y - 1)]
        t[(x, y)] = ((g[(x, y)] + dpt) % 20183) % 3

# part 1
# for y in range(0, ty + 1):
#     for x in range(0, tx + 1):
#         print({0:'.',1:'=',2:'|'}[t[(x,y)]],end='')
#     print()
sm(sum(t.values()))


# part 2

