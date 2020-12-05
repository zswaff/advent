#!/usr/bin/env python3
# -*- coding: utf-8 -*-


DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


with open('inp.txt') as fin:
    steps = [e.strip() for e in fin.readlines()][0].split(', ')


# part 1
x = y = o = 0
for step in steps:
    o = (o + (1 if step[0] == 'R' else -1)) % 4
    x += DIRS[o][0] * int(step[1:])
    y += DIRS[o][1] * int(step[1:])
print(abs(x) + abs(y))


# part 2
def solve():
    x = y = o = 0
    visited = set()
    for step in steps:
        o = (o + (1 if step[0] == 'R' else -1)) % 4
        if DIRS[o][0] != 0:
            for i in range(int(step[1:])):
                x += DIRS[o][0]
                pos = x, y
                if pos in visited:
                    return pos
                visited.add(pos)
        else:
            for i in range(int(step[1:])):
                y += DIRS[o][1]
                pos = x, y
                if pos in visited:
                    return pos
                visited.add(pos)

x, y = solve()
print(abs(x) + abs(y))
