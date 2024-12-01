#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


g = gr(ls, int)
mx = max(x for x, _ in g.keys())
my = max(y for _, y in g.keys())


# part 1
visible = set()
for (x, y), e in g.items():
    if (
        all(g[(x, i)] < e for i in range(0, y))
        or all(g[(x, i)] < e for i in range(y + 1, my + 1))
        or all(g[(i, y)] < e for i in range(0, x))
        or all(g[(i, y)] < e for i in range(x + 1, mx + 1))
    ):
        visible.add((x, y))
sm(len(visible))


# part 2
r = []
for (x, y), e in g.items():
    r.append(
        next((i for i in range(1, y + 1) if g[(x, y - i)] >= e), y)
        * next((i for i in range(1, my - y + 1) if g[(x, y + i)] >= e), my - y)
        * next((i for i in range(1, x + 1) if g[(x - i, y)] >= e), x)
        * next((i for i in range(1, mx - x + 1) if g[(x + i, y)] >= e), mx - x)
    )
sm(max(r))
