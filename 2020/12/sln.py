#!/usr/bin/env python3
# -*- coding: utf-8 -*-


DIRS = [(1, 0), (0, -1), (-1, 0), (0, 1)]


with open('inp.txt') as fin:
    instrs = [
        (f[0], int(f[1:])) for f in
        [e.strip() for e in fin.readlines()]
    ]


# part 1
x = y = d = 0
for cmd, amt in instrs:
    if cmd == 'N':
        y += amt
        continue
    if cmd == 'S':
        y -= amt
        continue
    if cmd == 'E':
        x += amt
        continue
    if cmd == 'W':
        x -= amt
        continue
    if cmd == 'L':
        d = (d - (amt // 90)) % 4
        continue
    if cmd == 'R':
        d = (d + (amt // 90)) % 4
        continue
    if cmd == 'F':
        xm, ym = DIRS[d]
        x += xm * amt
        y += ym * amt
        continue

print(abs(x) + abs(y))


# part 2
x = y = 0
wx, wy = 10, 1
for cmd, amt in instrs:
    if cmd == 'N':
        wy += amt
        continue
    if cmd == 'S':
        wy -= amt
        continue
    if cmd == 'E':
        wx += amt
        continue
    if cmd == 'W':
        wx -= amt
        continue
    if cmd == 'L':
        r = (amt // 90) % 4
        if r == 1:
            wx, wy = -wy, wx
        if r == 2:
            wx, wy = -wx, -wy
        if r == 3:
            wx, wy = wy, -wx
        continue
    if cmd == 'R':
        r = (amt // 90) % 4
        if r == 1:
            wx, wy = wy, -wx
        if r == 2:
            wx, wy = -wx, -wy
        if r == 3:
            wx, wy = -wy, wx
        continue
    if cmd == 'F':
        x += wx * amt
        y += wy * amt
        continue

print(abs(x) + abs(y))
