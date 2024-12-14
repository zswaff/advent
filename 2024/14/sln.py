#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
W, H = 101, 103
W2, H2 = W // 2, H // 2

rs = pas("p={i},{i} v={i},{i}")
for i in range(100):
    rs = [((r[0] + r[2]) % W, (r[1] + r[3]) % H, r[2], r[3]) for r in rs]
p = defaultdict(int)
for r in rs:
    x, y = r[:2]
    if x == W2 or y == H2:
        continue
    p[(x < W2, y < H2)] += 1
sm(prod(p.values()))


# part 2
rs = pas("p={i},{i} v={i},{i}")
for i in count():
    rs = [((r[0] + r[2]) % W, (r[1] + r[3]) % H, r[2], r[3]) for r in rs]
    g = set()
    for r in rs:
        g.add(tuple(r[:2]))
    for e in g:
        if all(
            (e[0] + dx, e[1] + dy) in g for dx in range(-2, 3) for dy in range(-2, 3)
        ):
            break
    else:
        continue
    break
sm(i + 1)
