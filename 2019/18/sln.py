#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
from collections import defaultdict
from heapq import heappush, heappop


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]
g = {(x, y): e for y, row in enumerate(lines) for x, e in enumerate(row)}


# part 1
def flat(x):
    return tuple(sorted(x))

def construct(g, l):
    res = defaultdict(list)
    s = defaultdict(list)
    q = [(l, 0, set())]
    while len(q) != 0:
        c, d, x = q.pop(0)
        s[c].append(x)
        for n in [(c[0] + e[0], c[1] + e[1]) for e in [(1, 0), (-1, 0), (0, 1), (0, -1)]]:
            if n not in g or g[n] == '#':
                continue
            if any(x >= e for e in s[n]):
                continue
            t = x
            if g[n] != '.':
                if 'A' <= g[n] <= 'Z':
                    t = x | {g[n]}
                else:
                    res[g[n]].append((x, d + 1))
            q.append((n, d + 1, t))
    return res

w = {}
for l, e in g.items():
    if e == '@' or 'a' <= e <= 'z':
        w[e] = {k: [({h.lower() for h in f}, g) for f, g in v] for k, v in construct(g, l).items()}
# print(json.dumps(w, indent=2))

goal = set(w.keys())
def search():
    q = [(0, '@', {'@'})]
    while len(q) != 0:
        d, l, s = heappop(q)
        if s == goal:
            return d
        for n, os in w[l].items():
            if n in s:
                continue
            ps = [v for k, v in os if k <= s]
            if len(ps) == 0:
                continue
            heappush(q, (d + min(ps), n, s | {n}))

print(search())


# part 2

