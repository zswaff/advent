#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import count


DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


with open("inp.txt") as fin:
    lines = [e.rstrip() for e in fin.readlines()]


# parts 1 and 2
g = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        g[(x, y)] = c
        if y == 0 and c == "|":
            cx = x

cy = -1
dx, dy = 0, 1
res = ""
for i in count():
    cx += dx
    cy += dy
    c = g.get((cx, cy), " ")
    if c == " ":
        break
    if c.isalpha():
        res += c
        continue
    if c != "+":
        continue
    dx, dy = [
        (nx, ny)
        for nx, ny in DIRS
        if g.get((cx + nx, cy + ny), " ") != " " and (nx, ny) != (-dx, -dy)
    ][0]

print(res)
print(i)
