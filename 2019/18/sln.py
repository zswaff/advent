#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from collections import deque, defaultdict
from heapq import heappush, heappop
from functools import lru_cache


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]
g = {(x, y): e for y, row in enumerate(lines) for x, e in enumerate(row)}
st = [k for k, v in g.items() if v == '@'][0]
g[st] = '.'
aks = frozenset(e for e in g.values() if e.islower())


# part 1
# @lru_cache()
# def cached_tile_search(start, keys):
#     ks = set(keys)
#     s = set()
#     q = deque([(start, 0)])
#     res = []
#     while len(q) != 0:
#         l, c = q.popleft()
#         s.add(l)
#         for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             n = l[0] + d[0], l[1] + d[1]
#             e = g[n]
#             if n in s or e == '#' or (e.isupper() and e.lower() not in ks):
#                 continue
#             if e.islower() and e not in ks:
#                 res.append((e, n, c + 1))
#                 continue
#             q.append((n, c + 1))
#     return res
#
# def bfs():
#     s = set()
#     q = [(0, st, frozenset())]
#     c = 0
#     while len(q) != 0:
#         # print(q)
#         d, l, ks = heappop(q)
#         c += 1
#         if c % 10000 == 0:
#             print(c, d)
#         # print(l, d, ks)
#         if ks == aks:
#             return d
#         s.add((l, ks))
#         ns = cached_tile_search(l, ks)
#         for k, nl, dd in ns:
#             nks = ks | {k}
#             if (nl, nks) in s:
#                 continue
#             heappush(q, (d + dd, nl, nks))
#
# print(bfs())


@lru_cache()
def accessible(s, ks):
    q = deque([(s, 0)])
    s = set()
    res = []
    while len(q) != 0:
        l, c = q.popleft()
        s.add(l)
        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            n = l[0] + d[0], l[1] + d[1]
            e = g[n]
            if n in s or e == '#' or (e.isupper() and e.lower() not in ks):
                continue
            if e.islower() and e not in ks:
                res.append((n, c + 1))
                continue
            q.append((n, c + 1))
    return res

@lru_cache()
def search(s, ks):
    if ks == aks:
        return 0
    k = g[s]
    nks = ks | {k}
    y = accessible(s, nks)
    # print(y)
    x = [c + search(n, nks) for n, c in y]
    # print(x)
    return min(x + [math.inf])

print(search(st, frozenset()))
