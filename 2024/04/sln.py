#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
g = gr()
c = 0
for (x, y), v in g.items():
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == dy == 0:
                continue
            s = "".join(g.get((x + dx * i, y + dy * i), "") for i in range(4))
            if s == "XMAS":
                c += 1
sm(c)

# part 2
c = 0
for (x, y), v in g.items():
    s1 = "".join(g.get((x + i, y + i), "") for i in range(3))
    s2 = "".join(g.get((x + 2 - i, y + i), "") for i in range(3))
    if s1 in {"MAS", "SAM"} and s2 in {"MAS", "SAM"}:
        c += 1
sm(c)
