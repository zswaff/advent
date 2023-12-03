#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import count

from common import *


# part 1
grid = gr(ls)
tot = 0
for (x, y), char in grid.items():
    if not char.isdigit() or grid.get((x - 1, y), ".").isdigit():
        continue
    valid = False
    nstr = ""
    for nx in count(x):
        cchar = grid.get((nx, y), ".")
        if not cchar.isdigit():
            break
        nstr += cchar
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                dchar = grid.get((nx + dx, y + dy), ".")
                if dchar != "." and not dchar.isdigit():
                    valid = True
    if valid:
        tot += int(nstr)
sm(tot)


# part 2
gears = {}
for (x, y), char in grid.items():
    if not char.isdigit() or grid.get((x - 1, y), ".").isdigit():
        continue
    adj = set()
    nstr = ""
    for nx in count(x):
        cchar = grid.get((nx, y), ".")
        if not cchar.isdigit():
            break
        nstr += cchar
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                pt = nx + dx, y + dy
                if grid.get(pt, ".") == "*":
                    adj.add(pt)
    n = int(nstr)
    for pt in adj:
        gears.setdefault(pt, []).append(n)
sm(sum(e[0] * e[1] for e in gears.values() if len(e) == 2))
