#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
x = 1
c = 0
q = []
for l in ls:
    op, rest = pa(l, ["noop", "addx {i}"])
    if op == 0:
        q.append([0, 0])
    if op == 1:
        q.append([1, list(rest)[0]])
for i in range(1, 221):
    if i % 40 == 20:
        c += i * x
    if q[0][0] > 0:
        q[0][0] -= 1
    else:
        op = q.pop(0)
        x += op[1]
sm(c)


# part 2
sx = 1
q = []
pts = set()
for l in ls:
    op, rest = pa(l, ["noop", "addx {i}"])
    if op == 0:
        q.append([0, 0])
    if op == 1:
        q.append([1, list(rest)[0]])
for i in range(1, 240):
    if q[0][0] > 0:
        q[0][0] -= 1
    else:
        op = q.pop(0)
        sx += op[1]
    y, x = divmod(i, 40)
    if abs(sx - x) <= 1:
        pts.add((x, y))
for y in range(6):
    for x in range(40):
        print("#" if (x, y) in pts else ".", end="")
    print()
sm("PGPHBEAB")
