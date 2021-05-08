#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict

import numpy as np


with open('inp.txt') as fin:
    lines = [e.strip() for e in sorted(fin.readlines())]


# part 1
d = defaultdict(lambda: np.zeros((60,), int))
c = 0
s = 0
for l in lines:
    spl = l.split()
    if spl[2] == 'Guard':
        c = int(spl[3][1:])
        continue
    if spl[2] == 'falls':
        s = int(spl[1][3:5])
        continue
    d[c][s:int(spl[1][3:5])] += 1
g = max(d.keys(), key=lambda x: d[x].sum())
m = d[g].argmax()
print(g * m)


# part 2
m = max((d[k].max(), d[k].argmax(), k) for k in d.keys())
print(m[1] * m[2])
