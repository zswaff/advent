#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict


with open("inp.txt") as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
my, mx = len(lines), len(lines[0])
d = defaultdict(bool)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        d[(x, y, 0)] = c == "#"
for i in range(6):
    nd = defaultdict(bool)
    for x, y, z in [
        (x, y, z)
        for x in range(-i - 1, mx + i + 1)
        for y in range(-i - 1, my + i + 1)
        for z in range(-i - 1, i + 2)
    ]:
        c = sum(
            d[(x + dx, y + dy, z + dz)]
            for dx in range(-1, 2)
            for dy in range(-1, 2)
            for dz in range(-1, 2)
        ) - int(d[(x, y, z)])
        f = d[(x, y, z)]
        nd[(x, y, z)] = (2 <= c <= 3 and f) or (c == 3 and not f)
    d = nd
print(sum(d.values()))


# part 2
d = defaultdict(bool)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        d[(x, y, 0, 0)] = c == "#"
for i in range(6):
    nd = defaultdict(bool)
    for x, y, z, w in [
        (x, y, z, w)
        for x in range(-i - 1, mx + i + 1)
        for y in range(-i - 1, my + i + 1)
        for z in range(-i - 1, i + 2)
        for w in range(-i - 1, i + 2)
    ]:
        c = sum(
            d[(x + dx, y + dy, z + dz, w + dw)]
            for dx in range(-1, 2)
            for dy in range(-1, 2)
            for dz in range(-1, 2)
            for dw in range(-1, 2)
        ) - int(d[(x, y, z, w)])
        f = d[(x, y, z, w)]
        nd[(x, y, z, w)] = (2 <= c <= 3 and f) or (c == 3 and not f)
    d = nd
print(sum(d.values()))
