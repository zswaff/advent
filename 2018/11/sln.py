#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common import *
from web import *

dt = int(dt)
d = np.zeros((300, 300))
for x in range(300):
    for y in range(300):
        r = (x + 1) + 10
        d[x, y] = (r * (y + 1) + dt) * r % 1000 // 100 - 5

# part 1
mx = 0, 0, 0
for x in range(298):
    for y in range(298):
        mx = max(mx, (d[x : x + 3, y : y + 3].sum(), x, y))
sm(f"{mx[1] + 1},{mx[2] + 1}")

# part 2
mx = 0, 0, 0, 0
for i in range(1, 301):
    for x in range(301 - i):
        for y in range(301 - i):
            mx = max(mx, (d[x : x + i, y : y + i].sum(), x, y, i))
sm(f"{mx[1] + 1},{mx[2] + 1},{mx[3]}")
