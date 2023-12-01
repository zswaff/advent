#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict


INP = [15, 12, 0, 14, 3, 1]


# part 1
r = list(reversed(INP))
for i in range(2020 - len(r)):
    try:
        f = r[1:].index(r[0]) + 1
    except ValueError:
        f = 0
    r.insert(0, f)
print(r[0])


# part 2
r = INP[-1]
d = defaultdict(list)
for i, e in enumerate(INP):
    d[e].append(i)
for i in range(len(INP), 30000000):
    if len(d[r]) > 1:
        r = i - d[r][-2] - 1
    else:
        r = 0
    d[r].append(i)
print(r)
