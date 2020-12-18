#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
ns = {}
for line in lines[2:]:
    splt = line.split()
    locstrs = splt[0].split('/')[-1].split('-')[1:]
    loc = int(locstrs[0][1:]), int(locstrs[1][1:])
    ns[loc] = [int(e[:-1]) for e in splt[1:]]
mnx, mxx = min(e[0] for e in ns.keys()), max(e[0] for e in ns.keys())
mny, mxy = min(e[1] for e in ns.keys()), max(e[1] for e in ns.keys())

c = 0
for loca, (_, useda, _, _) in ns.items():
    if useda == 0:
        continue
    for locb, (_, _, availb, _) in ns.items():
        if loca == locb:
            continue
        if useda <= availb:
            c += 1
print(c)


# part 2

