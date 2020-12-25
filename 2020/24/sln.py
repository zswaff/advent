#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict


DIRS = {
    'e': (2, 0),
    'se': (1, -1),
    'sw': (-1, -1),
    'w': (-2, 0),
    'nw': (-1, 1),
    'ne': (1, 1),
}


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
grid = defaultdict(bool)
for l in lines:
    x, y = 0, 0
    i = 0
    while i < len(l):
        c = l[i]
        if c == 's' or c == 'n':
            i += 1
            c += l[i]
        i += 1
        dx, dy = DIRS[c]
        x += dx
        y += dy
    grid[(x,y)] = not grid[(x,y)]
print(sum(grid.values()))


# part 2
for _ in range(100):
    ngrid = defaultdict(bool)
    for ox, oy in grid.keys():
        for dx, dy in list(DIRS.values()) + [(0, 0)]:
            x = ox + dx
            y = oy + dy
            loc = x, y
            if loc in ngrid:
                continue
            old = grid[loc] if loc in grid else False
            c = sum(grid.get((x + dx2, y + dy2), False) for dx2, dy2 in DIRS.values())
            if old and (c == 0 or c > 2):
                ngrid[loc] = False
            elif not old and c == 2:
                ngrid[loc] = True
            else:
                ngrid[loc] = old
    grid = ngrid
print(sum(grid.values()))
