#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
g = gr()
h = defaultdict(set)
for k, v in g.items():
    if v == ".":
        continue
    h[v].add(k)
ans = set()
for k, v in h.items():
    if len(v) == 1:
        continue
    for (x1, y1), (x2, y2) in combinations(v, 2):
        dx = x1 - x2
        dy = y1 - y2
        for nl in [(x1 + dx, y1 + dy), (x2 - dx, y2 - dy)]:
            if nl not in g:
                continue
            ans.add(nl)
sm(len(ans))


# part 2
ans = set()
for k, v in h.items():
    if len(v) == 1:
        continue
    for l1, l2 in combinations(v, 2):
        (x1, y1), (x2, y2) = l1, l2
        dx = x1 - x2
        dy = y1 - y2
        for it in [count(), count(-1, -1)]:
            for i in it:
                nl = (x1 + i * dx, y1 + i * dy)
                if nl not in g:
                    break
                ans.add(nl)
sm(len(ans))
