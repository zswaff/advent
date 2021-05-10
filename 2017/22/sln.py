#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict


DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
g = defaultdict(bool, {
    (x, y): c == '#'
    for y, e in enumerate(lines) for x, c in enumerate(e)
})
x = y = len(lines) // 2
d = 0
c = 0
for _ in range(10000):
    ci = g[(x, y)]
    d = (d + (1 if ci else -1)) % 4
    if not ci:
        c += 1
    g[(x, y)] = not ci
    dx, dy = DIRS[d]
    x += dx
    y += dy
print(c)


# part 2
g = defaultdict(int, {
    (x, y): 2 if c == '#' else 0
    for y, e in enumerate(lines) for x, c in enumerate(e)
})
x = y = len(lines) // 2
d = 0
c = 0
for _ in range(10000000):
    ci = g[(x, y)]
    d = (d + ci - 1) % 4
    if ci == 1:
        c += 1
    g[(x, y)] = (ci + 1) % 4
    dx, dy = DIRS[d]
    x += dx
    y += dy
print(c)
