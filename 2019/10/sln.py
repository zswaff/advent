#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict


with open('inp.txt') as fin:
    arr = [[f == '#' for f in e.strip()] for e in fin.readlines()]
sparse = {(x, y)
    for y, row in enumerate(arr)
    for x, e in enumerate(row)
    if e
}


# part 1
m = 0, None, None
for stat in sparse:
    sx, sy = stat
    lslps, rslps, abv, bel = defaultdict(list), defaultdict(list), [], []
    for ast in sparse:
        if ast == stat:
            continue
        ax, ay = ast
        if ax == sx:
            if ay > sy:
                bel.append(ast)
            else:
                abv.append(ast)
        else:
            if stat == (8, 3) and ast == (9, 0):
                print()
            slp = (sy - ay) / (ax - sx)
            if ax < sx:
                lslps[slp].append(ast)
            else:
                rslps[slp].append(ast)
    c = len(lslps) + len(rslps) + int(bool(abv)) + int(bool(bel))
    if c > m[0]:
        m = c, stat, (lslps, rslps, abv, bel)
print(m[0])


# part 2
_, (sx, sy), (lslps, rslps, abv, bel) = m
dirs = [abv] + [e[1] for e in sorted(rslps.items(), reverse=True)] + [bel] + [e[1] for e in sorted(lslps.items(), reverse=True)]
for e in dirs:
    e.sort(key=lambda x: ((sx - x[0]) ** 2 + (sy - x[1]) ** 2) ** .5)

idx = 0
last = None
for i in range(200):
    while len(dirs[idx]) == 0:
        idx = (idx + 1) % len(dirs)
    last = dirs[idx].pop(0)
    # print(last)
    idx = (idx + 1) % len(dirs)
print(last[0] * 100 + last[1])