#!/usr/bin/env python3
# -*- coding: utf-8 -*-20


from collections import defaultdict


with open("inp.txt") as fin:
    lines = [e.strip() for e in fin.readlines()]
og = {(x, y): e == "#" for y, row in enumerate(lines) for x, e in enumerate(row)}


DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1]]


# part 1
g = og
bs = set()
while True:
    b = sum(2 ** (y * 5 + x) for (x, y), e in g.items() if e)
    if b in bs:
        print(b)
        break
    bs.add(b)

    ng = {}
    for l, e in g.items():
        x, y = l
        c = sum(g.get((x + dx, y + dy), False) for dx, dy in DIRS)
        ng[l] = (e and c == 1) or (not e and 1 <= c <= 2)
    g = ng


# part 2
g = {0: {k: v for k, v in og.items() if k != (2, 2)}}
for i in range(200):
    g.update(
        {
            j: {(x, y): False for x in range(5) for y in range(5) if not x == y == 2}
            for j in [-i - 2, -i - 1, i + 1, i + 2]
        }
    )
    ng = defaultdict(dict)
    for j in range(-i - 1, i + 2):
        for x in range(5):
            for y in range(5):
                if x == y == 2:
                    continue
                l = x, y
                e = g[j][l]
                c = 0
                for k, (dx, dy) in enumerate(DIRS):
                    nl = x + dx, y + dy
                    if nl in g[j]:
                        c += g[j][nl]
                        continue
                    if nl == (2, 2):
                        c += {
                            0: lambda: sum(v for ll, v in g[j + 1].items() if ll[0] == 0),
                            1: lambda: sum(v for ll, v in g[j + 1].items() if ll[0] == 4),
                            2: lambda: sum(v for ll, v in g[j + 1].items() if ll[1] == 0),
                            3: lambda: sum(v for ll, v in g[j + 1].items() if ll[1] == 4),
                        }[k]()
                        continue
                    c += g[j - 1][2 + dx, 2 + dy]
                ng[j][l] = (e and c == 1) or (not e and 1 <= c <= 2)
    g = ng

print(sum(sum(e.values()) for e in g.values()))
