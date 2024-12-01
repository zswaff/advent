#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


ROTS = [
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
    [[1, 0, 0], [0, 0, -1], [0, 1, 0]],
    [[1, 0, 0], [0, -1, 0], [0, 0, -1]],
    [[1, 0, 0], [0, 0, 1], [0, -1, 0]],
    [[0, -1, 0], [1, 0, 0], [0, 0, 1]],
    [[0, 0, 1], [1, 0, 0], [0, 1, 0]],
    [[0, 1, 0], [1, 0, 0], [0, 0, -1]],
    [[0, 0, -1], [1, 0, 0], [0, -1, 0]],
    [[-1, 0, 0], [0, -1, 0], [0, 0, 1]],
    [[-1, 0, 0], [0, 0, -1], [0, -1, 0]],
    [[-1, 0, 0], [0, 1, 0], [0, 0, -1]],
    [[-1, 0, 0], [0, 0, 1], [0, 1, 0]],
    [[0, 1, 0], [-1, 0, 0], [0, 0, 1]],
    [[0, 0, 1], [-1, 0, 0], [0, -1, 0]],
    [[0, -1, 0], [-1, 0, 0], [0, 0, -1]],
    [[0, 0, -1], [-1, 0, 0], [0, 1, 0]],
    [[0, 0, -1], [0, 1, 0], [1, 0, 0]],
    [[0, 1, 0], [0, 0, 1], [1, 0, 0]],
    [[0, 0, 1], [0, -1, 0], [1, 0, 0]],
    [[0, -1, 0], [0, 0, -1], [1, 0, 0]],
    [[0, 0, -1], [0, -1, 0], [-1, 0, 0]],
    [[0, -1, 0], [0, 0, 1], [-1, 0, 0]],
    [[0, 0, 1], [0, 1, 0], [-1, 0, 0]],
    [[0, 1, 0], [0, 0, -1], [-1, 0, 0]],
]


ss = [{tuple(int(g) for g in f.split(",")) for f in e[1:]} for e in ss]


def diffs(cent, rest, rot):
    return (
        {
            tuple(
                np.matmul(
                    (e[0] - cent[0], e[1] - cent[1], e[2] - cent[2]), rot
                ).tolist()
            )
            for e in rest
        },
        tuple(np.matmul(cent, rot).tolist()),
    )


# part 1
r = ss[0]
scrs = [(0, 0, 0)]


def match(n):
    global r
    for rot in ROTS:
        for c in n:
            dc, tf = diffs(c, n, rot)
            for o in r:
                nr = {(o[0] + dx, o[1] + dy, o[2] + dz) for dx, dy, dz in dc}
                if len(r & nr) >= 12:
                    r |= nr
                    scrs.append((o[0] - tf[0], o[1] - tf[1], o[2] - tf[2]))
                    return True
    return False


q = ss[1:]
while q:
    print(len(q))
    n = q.pop(0)
    if not match(n):
        q.append(n)
sm(len(r))


# part 2
sm(
    max(
        abs(x0 - x1) + abs(y0 - y1) + abs(z0 - z1)
        for x0, y0, z0 in scrs
        for x1, y1, z1 in scrs
    )
)
