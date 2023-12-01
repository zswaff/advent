#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *
from web import *


DIRS = ((0, -1), (1, 0), (0, 1), (-1, 0))


d = defaultdict(
    lambda: " ",
    {
        (x, y): {"^": "|", ">": "-", "v": "|", "<": "-"}.get(c, c)
        for y, l in enumerate(ls)
        for x, c in enumerate(l)
    },
)
g = {}
cas = []
for y, l in enumerate(ls):
    for x, c in enumerate(l):
        p = x, y
        if c == "^" or c == "v":
            cas.append((p, 0 if c == "^" else 2, 0))
            c = "|"
        if c == ">" or c == "<":
            cas.append((p, 1 if c == ">" else 3, 0))
            c = "-"
        if c == "+":
            g[p] = (0, 1, 2, 3)
        if c == "|":
            g[p] = (0, 2)
        if c == "-":
            g[p] = (1, 3)
        if c == "/":
            g[p] = (0, 3) if d[(x, y - 1)] in {"|", "+"} else (1, 2)
        if c == "\\":
            g[p] = (0, 1) if d[(x, y - 1)] in {"|", "+"} else (2, 3)


# part 1
def fn(cas):
    cals = {e[0] for e in cas}
    for _ in count():
        cas = sorted(cas, key=lambda x: (x[0][1], x[0][0]))
        ncas = []
        for p, dr, t in cas:
            x, y = p
            cals.remove(p)
            dx, dy = DIRS[dr]
            np = x + dx, y + dy
            if np in cals:
                return f"{np[0]},{np[1]}"
            cals.add(np)
            dirs = g[np]
            if len(dirs) == 2:
                ndr = list(set(dirs) - {(dr + 2) % 4})[0]
                ncas.append((np, ndr, t))
            else:
                ndr = (dr + t - 1) % 4
                ncas.append((np, ndr, (t + 1) % 3))
        cas = ncas


sm(fn(cas))


# part 2
def fn(cas):
    cals = {e[0] for e in cas}
    for _ in count():
        cas = sorted(cas, key=lambda x: (x[0][1], x[0][0]))
        ncas = []
        rms = set()
        for p, dr, t in cas:
            x, y = p
            if p in rms:
                continue
            cals.remove(p)
            dx, dy = DIRS[dr]
            np = x + dx, y + dy
            if np in cals:
                cals.remove(np)
                rms.add(np)
                continue
            cals.add(np)
            dirs = g[np]
            if len(dirs) == 2:
                ndr = list(set(dirs) - {(dr + 2) % 4})[0]
                ncas.append((np, ndr, t))
            else:
                ndr = (dr + t - 1) % 4
                ncas.append((np, ndr, (t + 1) % 3))
        cas = [e for e in ncas if e[0] not in rms]
        if len(cas) == 1:
            return f"{cas[0][0][0]},{cas[0][0][1]}"


sm(fn(cas))
