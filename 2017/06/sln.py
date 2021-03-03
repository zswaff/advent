#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import count


with open('inp.txt') as fin:
    l = [int(e) for e in fin.read().strip().split()]


# parts 1 and 2
seen = {tuple(l): 0}
for i in count():
    idx = max(range(len(l)), key=lambda x: (l[x], -x))
    c = l[idx]
    l[idx] = 0
    for j in range(c):
        l[(idx + j + 1) % len(l)] += 1
    t = tuple(l)
    if t in seen:
        print(i + 1)
        print(i - seen[t] + 1)
        break
    seen[t] = i + 1
