#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
ns = defaultdict(list)
for i, l in enumerate(ls):
    ms = [e for e in l.split() if e]
    if i == len(ls) - 1:
        break
    for j, e in enumerate(ms):
        ns[j].append(int(e))
c = 0
for i, m in enumerate(ms):
    c += (sum if m == "+" else prod)(ns[i])
sm(c)


# part 2
g = gr(ls[:-1])
nrs = len(ls) - 1
c = 0
xs = []
x = ""
for i in range(len(ls[0])):
    for j in range(nrs):
        x += g[(i, j)]
    x = x.strip()
    if x == "":
        m = ms.pop(0)
        c += (sum if m == "+" else prod)(xs)
        xs = []
    else:
        xs.append(int(x))
        x = ""
c += (sum if ms[0] == "+" else prod)(xs)
sm(c)
