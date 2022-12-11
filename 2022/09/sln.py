#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


DIRS = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}

# part 1
hx = hy = tx = ty = 0
v = {(0, 0)}
for l in ls:
    nd, nm = pa(l, "{} {i}")
    for _ in range(nm):
        hx += DIRS[nd][0]
        hy += DIRS[nd][1]
        if tx == hx and ty in {hy + 2, hy - 2}:
            ty += 1 if hy > ty else -1
        elif ty == hy and tx in {hx + 2, hx - 2}:
            tx += 1 if hx > tx else -1
        elif (tx in {hx + 1, hx - 1} and ty in {hy + 2, hy - 2}) or (
            ty in {hy + 1, hy - 1} and tx in {hx + 2, hx - 2}
        ):
            tx += 1 if hx > tx else -1
            ty += 1 if hy > ty else -1
        v.add((tx, ty))
sm(len(v))


# part 2
ks = [[0, 0] for i in range(10)]
v = {(0, 0)}
for l in ls:
    nd, nm = pa(l, "{} {i}")
    for _ in range(nm):
        ks[0][0] += DIRS[nd][0]
        ks[0][1] += DIRS[nd][1]
        for i in range(9):
            (hx, hy), (tx, ty) = ks[i], ks[i + 1]
            if tx == hx and abs(ty - hy) >= 2:
                ks[i + 1][1] += 1 if hy > ty else -1
            elif ty == hy and abs(tx - hx) >= 2:
                ks[i + 1][0] += 1 if hx > tx else -1
            elif abs(tx - hx) > 1 or abs(ty - hy) > 1:
                ks[i + 1][0] += 1 if hx > tx else -1
                ks[i + 1][1] += 1 if hy > ty else -1
        # for y in range(5, -1, -1):
        #     for x in range(7):
        #         a = next(
        #             (i for i, e in reversed(list(enumerate(ks))) if e == [x, y]), None
        #         )
        #         if a is not None:
        #             print(a, end="")
        #         else:
        #             print(".", end="")
        #     print()
        # print()
        v.add(tuple(ks[-1]))
sm(len(v))
