#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *

bs = [1 if e == ">" else -1 for e in l]
ps = [
    {(0, 0), (1, 0), (2, 0), (3, 0)},
    {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)},
    {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)},
    {(0, 0), (0, 1), (0, 2), (0, 3)},
    {(0, 0), (0, 1), (1, 0), (1, 1)},
]

# part 1
g = set()
c = 0
cmy = 0
for i in range(2022):
    p = ps[i % len(ps)]
    ox, oy = 2, cmy + 4
    while True:
        dx = bs[c % len(bs)]
        c += 1
        if all(
            (px + ox + dx, py + oy) not in g and 0 <= px + ox + dx < 7 for px, py in p
        ):
            ox += dx
        if oy == 1 or any((px + ox, py + oy - 1) in g for px, py in p):
            break
        oy -= 1
    ng = {(px + ox, py + oy) for px, py in p}
    cmy = max(max(e[1] for e in ng), cmy)
    g |= ng

sm(cmy)


# part 2
g = set()
i = 0
c = 0
cmy = 0
cach = {}
done = False
for i in range(1000000000000):
    # print(i)
    p = ps[i % len(ps)]
    ox, oy = 2, cmy + 4
    while True:
        dx = bs[c % len(bs)]
        c += 1
        if all(
            (px + ox + dx, py + oy) not in g and 0 <= px + ox + dx < 7 for px, py in p
        ):
            ox += dx
        if oy == 1 or any((px + ox, py + oy - 1) in g for px, py in p):
            break
        oy -= 1
    ng = {(px + ox, py + oy) for px, py in p}
    cmy = max(max(e[1] for e in ng), cmy)
    g |= ng
    if i < 50000:
        continue

    key = (
        i % len(ps),
        c % len(bs),
        tuple(
            cmy - next((y for y in range(cmy, -1, -1) if (x, y) in g), 0)
            for x in range(7)
        ),
    )
    if key in cach:
        break
    cach[key] = i, cmy

old_i, old_cmy = cach[key]
i_dif = i - old_i
reps, rem = divmod(1000000000000 - i, i_dif)
delta = reps * (cmy - old_cmy)
for rem_i, rem_cmy in cach.values():
    if rem_i == old_i + rem - 1:
        delta += rem_cmy - old_cmy
        break

sm(cmy + delta)
