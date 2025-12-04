#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
g = gr(ls, lambda x: x == "@")
c = 0
for (x, y), v in g.items():
    if not v:
        continue
    tc = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == dy == 0 or not g.get((x + dx, y + dy), False):
                continue
            tc += 1
    if tc >= 4:
        continue
    c += 1
sm(c)


# part 2
c = 0
while True:
    rms = set()
    for (x, y), v in g.items():
        if not v:
            continue
        tc = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == dy == 0 or not g.get((x + dx, y + dy), False):
                    continue
                tc += 1
        if tc >= 4:
            continue
        rms.add((x, y))
    if not rms:
        break
    for x, y in rms:
        g[(x, y)] = False
    c += len(rms)
sm(c)
