#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


DIRS = [
    ((0, -1), ((1, -1), (-1, -1))),
    ((0, 1), ((1, 1), (-1, 1))),
    ((-1, 0), ((-1, -1), (-1, 1))),
    ((1, 0), ((1, -1), (1, 1))),
]


# part 1
g = {k for k, v in gr(ls, lambda x: x == "#").items() if v}
for i in range(10):
    prs = defaultdict(list)
    for x, y in g:
        if not any(
            not dx == dy == 0 and (x + dx, y + dy) in g
            for dx in range(-1, 2)
            for dy in range(-1, 2)
        ):
            prs[(x, y)].append((x, y))
            continue
        for j in range(4):
            (dx, dy), ((cx1, cy1), (cx2, cy2)) = DIRS[(i + j) % 4]
            if (
                (x + dx, y + dy) not in g
                and (x + cx1, y + cy1) not in g
                and (x + cx2, y + cy2) not in g
            ):
                prs[(x + dx, y + dy)].append((x, y))
                break
        else:
            prs[(x, y)].append((x, y))
    ng = set()
    for k, v in prs.items():
        if len(v) == 1:
            ng.add(k)
        else:
            ng |= set(v)
    g = ng
sm(
    (
        (max(e[0] for e in g) - min(e[0] for e in g) + 1)
        * (max(e[1] for e in g) - min(e[1] for e in g) + 1)
    )
    - len(g)
)


# part 2
g = {k for k, v in gr(ls, lambda x: x == "#").items() if v}
for i in count(0):
    if i % 1000 == 0:
        print(i)
    prs = defaultdict(list)
    for x, y in g:
        if not any(
            not dx == dy == 0 and (x + dx, y + dy) in g
            for dx in range(-1, 2)
            for dy in range(-1, 2)
        ):
            prs[(x, y)].append((x, y))
            continue
        for j in range(4):
            (dx, dy), ((cx1, cy1), (cx2, cy2)) = DIRS[(i + j) % 4]
            if (
                (x + dx, y + dy) not in g
                and (x + cx1, y + cy1) not in g
                and (x + cx2, y + cy2) not in g
            ):
                prs[(x + dx, y + dy)].append((x, y))
                break
        else:
            prs[(x, y)].append((x, y))
    ng = set()
    for k, v in prs.items():
        if len(v) == 1:
            ng.add(k)
        else:
            ng |= set(v)
    if g == ng:
        break
    g = ng
sm(i + 1)
