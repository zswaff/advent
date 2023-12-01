#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


k = [e == "#" for e in ss[0][0]]
h = gr(ss[1], lambda x: x == "#")
mxx, mxy = max(e[0] for e in h.keys()), max(e[1] for e in h.keys())


# part 1
g = dict(h)
for i in range(2):
    d = (i % 2 != 0) if k[0] else False
    ng = {}
    for y in range(-i - 1, mxy + i + 2):
        for x in range(-i - 1, mxx + i + 2):
            s = int(
                "".join(
                    str(int(g.get((x + dx, y + dy), d)))
                    for dy in range(-1, 2)
                    for dx in range(-1, 2)
                ),
                2,
            )
            ng[(x, y)] = k[s]
    g = ng
sm(sum(g.values()))


# part 2
g = dict(h)
for i in range(50):
    d = (i % 2 != 0) if k[0] else False
    ng = {}
    for y in range(-i - 1, mxy + i + 2):
        for x in range(-i - 1, mxx + i + 2):
            s = int(
                "".join(
                    str(int(g.get((x + dx, y + dy), d)))
                    for dy in range(-1, 2)
                    for dx in range(-1, 2)
                ),
                2,
            )
            ng[(x, y)] = k[s]
    g = ng
sm(sum(g.values()))
