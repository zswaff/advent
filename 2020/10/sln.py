#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


with open('inp.txt') as fin:
    ads = sorted([int(e.strip()) for e in fin.readlines()])


diffs = [ads[0]] + [ads[i + 1] - ads[i] for i in range(len(ads) - 1)] + [3]


# part 1
d1 = len([e for e in diffs if e == 1])
d3 = len([e for e in diffs if e == 3])
print(d1 * d3)


# part 2
def count_combs(t, v):
    if t in v:
        return 0
    v.add(t)
    if len(t) <= 1:
        return 1
    c = 1
    for i in range(len(t) - 1):
        s = t[i] + t[i + 1]
        if s > 3:
            continue
        c += count_combs(t[:i] + (s,) + t[i + 2:], v)
    return c

seqs = [
    tuple(int(g) for g in f)
    for f in ''.join(str(e) for e in diffs).split('3')
]
print(math.prod(count_combs(e, set()) for e in seqs))
