#!/usr/bin/env python3
# -*- coding: utf-8 -*-

DIRS = {
    'n': (0, 2),
    'ne': (1, 1),
    'se': (1, -1),
    's': (0, -2),
    'sw': (-1, -1),
    'nw': (-1, 1),
}

with open('inp.txt') as fin:
    mvs = fin.read().strip().split(',')

# part 1
x, y = 0, 0
for mv in mvs:
    d = DIRS[mv]
    x += d[0]
    y += d[1]
print(abs(x) + max(0, (abs(y) - abs(x)) // 2))

# part 2
x, y = 0, 0
m = 0
for mv in mvs:
    d = DIRS[mv]
    x += d[0]
    y += d[1]
    m = max(m, abs(x) + max(0, (abs(y) - abs(x)) // 2))
print(m)
