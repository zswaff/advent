#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *

# part 1
DS = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0),
}
SR = {
    "N": "E",
    "E": "N",
    "S": "W",
    "W": "S",
}
BSR = {
    "N": "W",
    "E": "S",
    "S": "E",
    "W": "N",
}

g = gr(ls)


def laze(ini):
    en = set()
    q = [ini]
    while q:
        x, y, d = fp = q.pop()
        if fp in en:
            continue
        en.add(fp)
        nx, ny = x + DS[d][0], y + DS[d][1]
        np = nx, ny
        if np not in g:
            continue
        v = g[np]
        if v == "." or (v == "|" and d in "NS") or (v == "-" and d in "EW"):
            q.append((nx, ny, d))
            continue
        if v == "/":
            q.append((nx, ny, SR[d]))
            continue
        if v == "\\":
            q.append((nx, ny, BSR[d]))
            continue
        if v == "|":
            q.append((nx, ny, "N"))
            q.append((nx, ny, "S"))
            continue
        if v == "-":
            q.append((nx, ny, "E"))
            q.append((nx, ny, "W"))
    return len(set((e[0], e[1]) for e in en)) - 1


sm(laze((-1, 0, "E")))


# part 2
mx = max(e[0] for e in g)
my = max(e[1] for e in g)
sm(
    max(
        [laze((-1, i, "E")) for i in range(my + 1)]
        + [laze((mx + 1, i, "W")) for i in range(my + 1)]
        + [laze((i, -1, "S")) for i in range(mx + 1)]
        + [laze((i, my + 1, "N")) for i in range(mx + 1)]
    )
)
